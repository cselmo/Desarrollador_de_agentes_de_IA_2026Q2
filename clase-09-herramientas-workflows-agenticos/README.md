# Clase 9 — Herramientas y workflows agénticos

## Contenido de esta carpeta

- `clase-09.ipynb`: notebook de la clase (teoría, demos ejecutables y laboratorio).
- `requirements.txt`: dependencias para correr el notebook.

Al correr el notebook se crea `tickets.db` (SQLite) en esta misma carpeta — es un archivo generado localmente, no está versionado (ver `.gitignore` en la raíz del repo). Si querés empezar de cero, simplemente borrá el archivo y volvé a correr la sección 2 del notebook.

## Cómo correr el notebook

Desde la raíz del repo (donde está el `.env` con tus credenciales):

```bash
pip install -r clase-09-herramientas-workflows-agenticos/requirements.txt
jupyter notebook clase-09-herramientas-workflows-agenticos/clase-09.ipynb
```
