"""Lógica de dominio del sistema de tickets — Clase 10.

La usan dos "interfaces" distintas sobre la misma lógica:
  - el notebook (grafo de LangGraph, tool calling directo), y
  - el servidor MCP (servidor_tickets_mcp.py), que corre en otro proceso.

Por eso vive en un módulo aparte: la base de datos y las reglas de negocio no dependen
de cómo se invoque la herramienta. Todas las escrituras son idempotentes (Clase 9, §8).
"""
import hashlib
import json
import os
import sqlite3
from datetime import datetime, timezone

DB_PATH = os.environ.get(
    "TICKETS_DB", os.path.join(os.path.dirname(os.path.abspath(__file__)), "tickets_clase10.db")
)

ESTADOS = ("abierto", "escalado", "resuelto")

ESQUEMA = """
CREATE TABLE IF NOT EXISTS tickets (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario             TEXT NOT NULL,
    pregunta            TEXT NOT NULL,
    contexto_recuperado TEXT,
    estado              TEXT NOT NULL DEFAULT 'abierto' CHECK (estado IN ('abierto', 'escalado', 'resuelto')),
    motivo_escalamiento TEXT,
    clave_idempotencia  TEXT UNIQUE,
    huella_parametros   TEXT,
    fecha_creacion      TEXT NOT NULL
);
-- Registro de acciones de escritura ejecutadas, indexado por clave de idempotencia
CREATE TABLE IF NOT EXISTS acciones (
    clave_idempotencia TEXT PRIMARY KEY,
    accion             TEXT NOT NULL,
    huella_parametros  TEXT NOT NULL,
    resultado          TEXT NOT NULL,
    compensada         INTEGER NOT NULL DEFAULT 0,
    fecha              TEXT NOT NULL
);
"""

TICKETS_SEMILLA = [
    ("ana", "¿Cómo se usa Promise.allSettled?", "abierto"),
    ("bruno", "Mi contraseña de la VPN corporativa es hunter2, ¿la cambio?", "escalado"),
    ("ana", "¿Diferencia entre let y var en un for?", "resuelto"),
    ("ana", "¿Por qué fetch no lanza un error cuando el servidor responde 404?", "abierto"),
]


class ConflictoIdempotencia(Exception):
    """La misma clave se usó con parámetros distintos."""


class TransicionInvalida(Exception):
    """La acción no es legal sobre el estado ACTUAL del ticket (p. ej. ya no está abierto)."""


def ahora() -> str:
    return datetime.now(timezone.utc).isoformat()


def conectar() -> sqlite3.Connection:
    con = sqlite3.connect(DB_PATH, timeout=10)
    con.row_factory = sqlite3.Row
    return con


def reiniciar_base() -> None:
    """Borra y recrea la base con los tickets semilla (para demos reproducibles)."""
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    con = conectar()
    with con:
        con.executescript(ESQUEMA)
        con.executemany(
            "INSERT INTO tickets (usuario, pregunta, estado, fecha_creacion) VALUES (?, ?, ?, ?)",
            [(u, p, e, ahora()) for u, p, e in TICKETS_SEMILLA],
        )
    con.close()


def huella(**params) -> str:
    return hashlib.sha256(json.dumps(params, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def clave_idempotencia(*partes) -> str:
    """Clave determinística a partir de partes estables (usuario, hilo, ticket, acción…)."""
    return hashlib.sha256("|".join(str(p) for p in partes).encode()).hexdigest()[:32]


# ----------------------------------------------------------------------------- lectura

def consultar_estado_ticket(ticket_id: int, usuario: str) -> dict:
    """Lectura. Filtra por dueño: un ticket ajeno responde igual que uno inexistente."""
    con = conectar()
    try:
        fila = con.execute(
            "SELECT id, estado, pregunta, motivo_escalamiento, fecha_creacion FROM tickets WHERE id = ? AND usuario = ?",
            (ticket_id, usuario),
        ).fetchone()
    finally:
        con.close()
    if not fila:
        return {"encontrado": False, "ticket_id": ticket_id,
                "mensaje": f"No hay un ticket #{ticket_id} a nombre de este usuario."}
    return {"encontrado": True, **dict(fila)}


def listar_tickets(usuario: str) -> list[dict]:
    con = conectar()
    try:
        filas = con.execute(
            "SELECT id, estado, pregunta FROM tickets WHERE usuario = ? ORDER BY id", (usuario,)
        ).fetchall()
    finally:
        con.close()
    return [dict(f) for f in filas]


# ----------------------------------------------------------------------------- escritura

def crear_ticket(usuario: str, pregunta: str, contexto_recuperado: str, clave: str) -> int:
    """Escritura idempotente (Clase 9): misma clave -> mismo ticket."""
    h = huella(usuario=usuario, pregunta=pregunta)
    con = conectar()
    try:
        with con:
            con.execute(
                "INSERT INTO tickets (usuario, pregunta, contexto_recuperado, clave_idempotencia, huella_parametros, fecha_creacion) "
                "VALUES (?, ?, ?, ?, ?, ?) ON CONFLICT(clave_idempotencia) DO NOTHING",
                (usuario, pregunta, contexto_recuperado, clave, h, ahora()),
            )
        fila = con.execute(
            "SELECT id, huella_parametros FROM tickets WHERE clave_idempotencia = ?", (clave,)
        ).fetchone()
    finally:
        con.close()
    if fila["huella_parametros"] != h:
        raise ConflictoIdempotencia(f"La clave {clave[:8]}… ya se usó con otros parámetros")
    return fila["id"]


def escalar_ticket(ticket_id: int, usuario: str, motivo: str, clave: str) -> dict:
    """Escritura idempotente CON re-validación del estado al momento de ejecutar (TOCTOU).

    - Si la clave ya se ejecutó con los mismos parámetros: devuelve el resultado original.
    - Si el ticket ya no está 'abierto' (o no es del usuario): TransicionInvalida.
    Todo en una transacción: o se escala y se registra la acción, o no pasa nada.
    """
    h = huella(ticket_id=ticket_id, usuario=usuario, motivo=motivo)
    con = conectar()
    try:
        con.execute("BEGIN IMMEDIATE")
        previa = con.execute(
            "SELECT huella_parametros, resultado, compensada FROM acciones WHERE clave_idempotencia = ?", (clave,)
        ).fetchone()
        if previa:
            con.rollback()
            if previa["huella_parametros"] != h:
                raise ConflictoIdempotencia(f"La clave {clave[:8]}… ya se usó con otros parámetros")
            return {**json.loads(previa["resultado"]), "repetida": True, "compensada": bool(previa["compensada"])}

        cur = con.execute(
            "UPDATE tickets SET estado = 'escalado', motivo_escalamiento = ? "
            "WHERE id = ? AND usuario = ? AND estado = 'abierto'",
            (motivo, ticket_id, usuario),
        )
        if cur.rowcount != 1:
            con.rollback()
            fila = con.execute("SELECT estado FROM tickets WHERE id = ? AND usuario = ?", (ticket_id, usuario)).fetchone()
            actual = fila["estado"] if fila else "inexistente para este usuario"
            raise TransicionInvalida(
                f"El ticket #{ticket_id} no está abierto (estado actual: {actual}). Hace falta una nueva aprobación."
            )
        resultado = {"ticket_id": ticket_id, "estado": "escalado", "motivo": motivo}
        con.execute(
            "INSERT INTO acciones (clave_idempotencia, accion, huella_parametros, resultado, fecha) VALUES (?, ?, ?, ?, ?)",
            (clave, "escalar_ticket", h, json.dumps(resultado, ensure_ascii=False), ahora()),
        )
        con.commit()
        return {**resultado, "repetida": False}
    finally:
        con.close()


def revertir_escalamiento(ticket_id: int, clave: str) -> dict:
    """Compensación de escalar_ticket (saga, Clase 10 §4.3). Idempotente: revertir dos veces no hace nada extra."""
    con = conectar()
    try:
        with con:
            con.execute(
                "UPDATE tickets SET estado = 'abierto', motivo_escalamiento = NULL WHERE id = ? AND estado = 'escalado'",
                (ticket_id,),
            )
            con.execute("UPDATE acciones SET compensada = 1 WHERE clave_idempotencia = ?", (clave,))
    finally:
        con.close()
    return {"ticket_id": ticket_id, "estado": "abierto", "compensado": True}


def resolver_ticket(ticket_id: int) -> None:
    """Lo usa 'otro operador' en la demo de TOCTOU: cambia el estado por fuera del flujo."""
    con = conectar()
    try:
        with con:
            con.execute("UPDATE tickets SET estado = 'resuelto' WHERE id = ?", (ticket_id,))
    finally:
        con.close()
