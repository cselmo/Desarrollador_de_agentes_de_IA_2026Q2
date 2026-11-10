# Clase 8 — Evaluación y mejora de RAG

## Contenido de esta carpeta

- `clase-08.ipynb`: notebook de la clase (teoría, demos ejecutables y laboratorio).
- `requirements.txt`: dependencias para correr el notebook.

## Cómo correr el notebook

Desde la raíz del repo (donde está el `.env` con tus credenciales):

```bash
pip install -r clase-08-evaluacion-mejora-rag/requirements.txt
jupyter notebook clase-08-evaluacion-mejora-rag/clase-08.ipynb
```

## Nota sobre RAGAS

La sección 7 usa RAGAS real contra AWS Bedrock vía `langchain-aws` (`ChatBedrockConverse`), siguiendo la integración oficialmente documentada en [docs.ragas.io](https://docs.ragas.io) para Amazon Bedrock — es la forma más estable de usar RAGAS con Bedrock, incluso si otras partes de la API de RAGAS cambian entre versiones. Si tu proveedor del TP no es Bedrock, `LangchainLLMWrapper` también envuelve `ChatOpenAI` (`langchain-openai`) y `ChatAnthropic` (`langchain-anthropic`) con el mismo patrón.
