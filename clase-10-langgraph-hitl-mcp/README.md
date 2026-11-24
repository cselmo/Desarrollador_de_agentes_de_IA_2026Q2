# Clase 10 — LangGraph, human-in-the-loop y MCP

## Contenido de esta carpeta

- `apunte.md`: **marco teórico de la clase**, con las fuentes anotadas al principio (qué contiene cada una y por qué se usa), diagramas y una tabla de correspondencia con las secciones del notebook. Lectura obligatoria antes de la clase: la página *Interrupts* de LangGraph, la página *Architecture* de MCP y *Ironies of Automation* (Bainbridge, 1983).
- `clase-10.ipynb`: notebook de la clase (demos ejecutables y laboratorio).
- `clase-10-ejecutada.ipynb`: el mismo notebook ya corrido de punta a punta (con AWS Bedrock), para ver las salidas sin ejecutar nada.
- `tickets_db.py`: lógica del sistema de tickets (SQLite), compartida por el notebook y el servidor MCP. Todas las escrituras son idempotentes.
- `servidor_tickets_mcp.py`: servidor MCP mínimo que expone la consulta de tickets (solo lectura).
- `servidor_malicioso_mcp.py`: servidor MCP para la demo de *tool poisoning* y *rug pull* (sección 8). Es inofensivo: lo que "roba" lo escribe en un archivo local temporal.
- `requirements.txt`: dependencias.

Al correr el notebook se crean `tickets_clase10.db` y `checkpoints_clase10.db` en esta carpeta. Se recrean en cada corrida y no están versionados.

Los diagramas están en Mermaid: se ven en GitHub y en JupyterLab 4.1+; en VS Code hace falta la extensión *Markdown Preview Mermaid Support* (`bierner.markdown-mermaid`).

## Requisito: Python 3.11 o superior

El SDK oficial de MCP (`mcp` v2) requiere Python 3.11+. Si tu entorno del curso es más viejo, creá uno nuevo:

```bash
conda create -n agentes-clase10 python=3.12 -y && conda activate agentes-clase10
# o bien: python3.12 -m venv .venv && source .venv/bin/activate
pip install -r clase-10-langgraph-hitl-mcp/requirements.txt jupyter
```

## Cómo correr el notebook

Desde la raíz del repo (donde está el `.env` con tus credenciales):

```bash
jupyter notebook clase-10-langgraph-hitl-mcp/clase-10.ipynb
```

## Probar el servidor MCP con otro host

El servidor de tickets funciona con cualquier cliente MCP. Por ejemplo, con el MCP Inspector:

```bash
cd clase-10-langgraph-hitl-mcp
TICKETS_USUARIO=ana npx @modelcontextprotocol/inspector python servidor_tickets_mcp.py
```

El usuario (`TICKETS_USUARIO`) lo fija quien lanza el servidor, nunca el modelo.
