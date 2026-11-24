"""Servidor MCP del sistema de tickets — Clase 10.

Se lanza como subproceso del host por stdio:

    TICKETS_USUARIO=ana python servidor_tickets_mcp.py

El usuario lo fija el HOST al lanzar el proceso (variable de entorno), nunca el modelo:
la autorización no depende de los argumentos que emita el LLM (Clase 9, §9).

Expone solo LECTURA: las escrituras sensibles (escalar_ticket) quedan del lado del host,
detrás de la aprobación humana del grafo de LangGraph.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tickets_db  # noqa: E402
from mcp.server import MCPServer  # noqa: E402
from mcp.types import ToolAnnotations  # noqa: E402

USUARIO = os.environ.get("TICKETS_USUARIO")
if not USUARIO:
    raise SystemExit("Falta la variable de entorno TICKETS_USUARIO (la define el host al lanzar el servidor)")

mcp = MCPServer(
    "tickets-curso",
    instructions="Consulta de tickets de soporte del usuario actual. Solo lectura.",
)

SOLO_LECTURA = ToolAnnotations(readOnlyHint=True, idempotentHint=True, openWorldHint=False)


@mcp.tool(annotations=SOLO_LECTURA)
def consultar_estado_ticket(ticket_id: int) -> dict:
    """Consulta el estado de UN ticket de soporte del usuario actual, por su número.

    Devuelve si se encontró, el estado ('abierto', 'escalado' o 'resuelto'), la pregunta original
    y la fecha. Usala solo cuando el usuario da un número de ticket concreto; no inventes números.
    """
    if ticket_id < 1:
        raise ValueError("ticket_id debe ser un entero mayor o igual a 1")
    return tickets_db.consultar_estado_ticket(ticket_id, USUARIO)


@mcp.tool(annotations=SOLO_LECTURA)
def listar_mis_tickets() -> list[dict]:
    """Lista todos los tickets del usuario actual con su número, estado y pregunta.

    Usala cuando el usuario pregunta por sus tickets sin dar un número concreto.
    """
    return tickets_db.listar_tickets(USUARIO)


@mcp.resource("ticket://{ticket_id}", mime_type="application/json")
def recurso_ticket(ticket_id: str) -> str:
    """Un ticket del usuario actual como recurso (lo adjunta la aplicación, no lo pide el modelo)."""
    import json
    return json.dumps(tickets_db.consultar_estado_ticket(int(ticket_id), USUARIO), ensure_ascii=False)


@mcp.prompt()
def resumir_ticket(ticket_id: str) -> str:
    """Plantilla que el USUARIO elige explícitamente para pedir un resumen de un ticket."""
    return (f"Resumí en dos líneas el ticket #{ticket_id}: qué se preguntó, en qué estado está "
            f"y cuál sería el próximo paso razonable. Usá la herramienta consultar_estado_ticket.")


if __name__ == "__main__":
    mcp.run("stdio")
