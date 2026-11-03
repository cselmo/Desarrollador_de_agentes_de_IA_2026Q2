# Clase 7 — RAG avanzado y debugging

## Contenido de esta carpeta

- `clase-07.ipynb`: notebook de la clase (teoría, demos ejecutables y laboratorio).
- `app_rag_streamlit.py`: ejemplo standalone de un agente RAG completo (recuperación + generación + citas) detrás de una interfaz de chat con Streamlit — integra lo visto en las Clases 2 a 7.
- `requirements.txt`: dependencias para correr el notebook y la app de esta clase.

## Cómo correr el notebook

Desde la raíz del repo (donde está el `.env` con tus credenciales):

```bash
pip install -r clase-07-rag-avanzado-debugging/requirements.txt
jupyter notebook clase-07-rag-avanzado-debugging/clase-07.ipynb
```

## Cómo correr la app de Streamlit

```bash
pip install -r clase-07-rag-avanzado-debugging/requirements.txt
streamlit run clase-07-rag-avanzado-debugging/app_rag_streamlit.py
```

Se abre en el navegador en `localhost:8501`. Usa el mismo corpus de juguete del notebook (Clases 6-7) para correr standalone sin depender de tu índice real — para probarla con el corpus del TP (MDN Web Docs), reemplazá `CORPUS` y `get_coleccion()` en `app_rag_streamlit.py` por tu índice persistente de la Clase 5.

Requiere las credenciales del proveedor configuradas en el `.env` de la raíz del repo (ver `.env.example`).
