# Clase 9 — Herramientas y workflows agénticos

## Contenido de esta carpeta

- `apunte.md`: **marco teórico de la clase**, con las fuentes anotadas al principio (qué contiene cada una y por qué se usa) y diagramas. Incluye una tabla de correspondencia con las secciones del notebook. Lectura obligatoria antes de la clase: *Building effective agents* (Anthropic) y §1–3 del paper de ReAct.
- `clase-09.ipynb`: notebook de la clase (demos ejecutables y laboratorio). Cada sección indica el § del apunte donde está la teoría.
- `clase-09-ejecutada.ipynb`: el mismo notebook ya corrido de punta a punta (con AWS Bedrock), para ver las salidas sin ejecutar nada.
- `requirements.txt`: dependencias para correr el notebook.

Al correr el notebook se crea `tickets_clase09.db` (SQLite) en esta carpeta. Se borra y se recrea al inicio de cada corrida, y no está versionado (ver `.gitignore` en la raíz del repo).

Los diagramas (en el apunte y en el notebook) están en Mermaid: se ven en GitHub y en JupyterLab 4.1+; en VS Code hace falta la extensión *Markdown Preview Mermaid Support* (`bierner.markdown-mermaid`).

## Cómo correr el notebook

Desde la raíz del repo (donde está el `.env` con tus credenciales):

```bash
pip install -r clase-09-herramientas-workflows-agenticos/requirements.txt
jupyter notebook clase-09-herramientas-workflows-agenticos/clase-09.ipynb
```
