"""
Agente RAG con interfaz de chat en Streamlit.

Integra lo construido en las Clases 2 a 7:
- Cliente de modelo generativo (Clase 2-3) vía AWS Bedrock Converse API.
- Embeddings y recuperación semántica con ChromaDB (Clase 4-5).
- Prompt delimitado, presupuesto de contexto, manejo de ausencia de evidencia
  y citas trazables (Clase 6).
- Umbral de relevancia para evitar respuestas forzadas (Clase 7).

El corpus de abajo es el mismo corpus de juguete usado en las Clases 6 y 7,
para que este archivo corra standalone sin depender de tu índice real del TP.
Reemplazá `CORPUS` (y, si hace falta, `coleccion`) por tu propio índice
persistente (Clase 5) para usarlo con el corpus real de MDN Web Docs.

Cómo correrlo:
    pip install streamlit chromadb boto3 python-dotenv
    streamlit run app_rag_streamlit.py
"""

import os
import json

import boto3
import chromadb
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

MODEL_ID = os.environ.get("BEDROCK_MODEL_ID_CLAUDE", "global.anthropic.claude-sonnet-4-6")
EMBED_MODEL_ID = os.environ.get("BEDROCK_MODEL_ID_EMBED", "cohere.embed-v4:0")
REGION = os.environ.get("AWS_REGION", "us-east-1")

SYSTEM_RAG = (
    "Sos un asistente que responde preguntas usando EXCLUSIVAMENTE la evidencia provista. "
    "No uses conocimiento propio ni inventes información que no esté en la evidencia. "
    "Citá la evidencia usada con el número entre corchetes correspondiente, "
    "ej. 'La temperatura se configura en inferenceConfig [1].'"
)

CORPUS = [
    {"id": "apis-001", "texto": "La Converse API de Bedrock unifica la forma de llamar a distintos modelos: cambia el modelId, no el código.", "doc": "guia-apis"},
    {"id": "apis-002", "texto": "Los parámetros de inferencia como temperature y maxTokens van en inferenceConfig en Bedrock.", "doc": "guia-apis"},
    {"id": "seguridad-001", "texto": "La inyección de prompts ocurre cuando contenido no confiable manipula las instrucciones del modelo.", "doc": "guia-seguridad"},
    {"id": "seguridad-002", "texto": "El principio de mínimo privilegio limita qué herramientas puede invocar un agente según el contexto.", "doc": "guia-seguridad"},
    {"id": "rag-001", "texto": "Un pipeline RAG combina recuperación de evidencia con generación sustentada en esa evidencia.", "doc": "guia-rag"},
    {"id": "rag-002", "texto": "El top-k determina cuántos fragmentos recuperados se incluyen como contexto para el modelo generador.", "doc": "guia-rag"},
]


@st.cache_resource
def get_bedrock_client():
    return boto3.client("bedrock-runtime", region_name=REGION)


@st.cache_resource
def get_coleccion():
    """Construye (una sola vez, cacheado) el índice en memoria con el corpus de juguete."""
    client = get_bedrock_client()
    textos = [c["texto"] for c in CORPUS]
    vectores = embed(client, textos, input_type="search_document")

    cliente_chroma = chromadb.Client()
    coleccion = cliente_chroma.get_or_create_collection("corpus_streamlit_demo")
    coleccion.add(
        ids=[c["id"] for c in CORPUS],
        embeddings=vectores,
        documents=textos,
        metadatas=[{"doc": c["doc"]} for c in CORPUS],
    )
    return coleccion


def embed(client, textos: list[str], input_type: str = "search_document") -> list[list[float]]:
    body = json.dumps({"texts": textos, "input_type": input_type, "embedding_types": ["float"]})
    resp = client.invoke_model(modelId=EMBED_MODEL_ID, body=body, accept="*/*", contentType="application/json")
    return json.loads(resp["body"].read())["embeddings"]["float"]


def generar(client, prompt: str, system: str = None, temperature: float = 0.0, max_tokens: int = 500) -> str:
    kwargs = {
        "modelId": MODEL_ID,
        "messages": [{"role": "user", "content": [{"text": prompt}]}],
        "inferenceConfig": {"temperature": temperature, "maxTokens": max_tokens},
    }
    if system:
        kwargs["system"] = [{"text": system}]
    resp = client.converse(**kwargs)
    return resp["output"]["message"]["content"][0]["text"]


def recuperar(client, coleccion, consulta: str, k: int = 3) -> list[dict]:
    vec = embed(client, [consulta], input_type="search_query")[0]
    resultado = coleccion.query(query_embeddings=[vec], n_results=k)
    return [
        {"chunk_id": id_, "texto": texto, "doc": meta["doc"], "distancia": dist}
        for id_, texto, meta, dist in zip(
            resultado["ids"][0], resultado["documents"][0], resultado["metadatas"][0], resultado["distances"][0]
        )
    ]


def armar_contexto(chunks: list[dict]) -> str:
    return "\n\n".join(f"[{i + 1}] (fuente: {c['doc']}) {c['texto']}" for i, c in enumerate(chunks))


def responder_rag(consulta: str, k: int = 3, umbral_distancia: float = 1.0) -> dict:
    client = get_bedrock_client()
    coleccion = get_coleccion()

    chunks = recuperar(client, coleccion, consulta, k)
    chunks_relevantes = [c for c in chunks if c["distancia"] < umbral_distancia]

    if not chunks_relevantes:
        return {"respuesta": "No encontré evidencia suficiente en el corpus para responder esta pregunta.", "fuentes": []}

    contexto = armar_contexto(chunks_relevantes)
    prompt = (
        f"<evidencia>\n{contexto}\n</evidencia>\n\n"
        f"<pregunta>\n{consulta}\n</pregunta>\n\n"
        "Respondé la pregunta usando solo la evidencia. Si la evidencia no alcanza, decilo explícitamente."
    )
    respuesta = generar(client, prompt, system=SYSTEM_RAG)
    fuentes = [{"ref": i + 1, "chunk_id": c["chunk_id"], "doc": c["doc"]} for i, c in enumerate(chunks_relevantes)]
    return {"respuesta": respuesta, "fuentes": fuentes}


# --- Interfaz de chat ---

st.title("🤖 Agente RAG — demo")
st.caption(
    "Corpus de juguete (Clases 6-7). Para usar el corpus real del TP, reemplazá `CORPUS` "
    "y `get_coleccion()` por tu índice persistente de la Clase 5."
)

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

for mensaje in st.session_state.mensajes:
    with st.chat_message(mensaje["role"]):
        st.write(mensaje["content"])
        if mensaje.get("fuentes"):
            with st.expander("Fuentes citadas"):
                for f in mensaje["fuentes"]:
                    st.write(f"[{f['ref']}] `{f['chunk_id']}` (doc: {f['doc']})")

consulta = st.chat_input("Preguntá algo sobre el corpus...")

if consulta:
    st.session_state.mensajes.append({"role": "user", "content": consulta})
    with st.chat_message("user"):
        st.write(consulta)

    with st.chat_message("assistant"):
        with st.spinner("Recuperando evidencia y generando respuesta..."):
            resultado = responder_rag(consulta)
        st.write(resultado["respuesta"])
        if resultado["fuentes"]:
            with st.expander("Fuentes citadas"):
                for f in resultado["fuentes"]:
                    st.write(f"[{f['ref']}] `{f['chunk_id']}` (doc: {f['doc']})")

    st.session_state.mensajes.append(
        {"role": "assistant", "content": resultado["respuesta"], "fuentes": resultado["fuentes"]}
    )
