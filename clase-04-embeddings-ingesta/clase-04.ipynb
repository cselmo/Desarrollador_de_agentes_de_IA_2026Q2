{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Certificación Profesional en Desarrollador de Agentes de IA\n",
    "## Clase 4 — Embeddings e ingesta documental\n",
    "\n",
    "ITBA Educación Ejecutiva\n",
    "\n",
    "Preparación de información para recuperación semántica: hoy dejamos de hablarle al modelo de a una consulta por vez, y empezamos a construir el corpus sobre el que va a buscar."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Cómo se usa este notebook\n",
    "\n",
    "- El docente corre y explica cada celda en vivo (demo con AWS Bedrock). No programás en simultáneo durante la clase.\n",
    "- Celdas **🏠 Practicá**: tarea individual para después de la clase.\n",
    "- **Sección 9 (Laboratorio)**: tarea principal de la semana — checkpoint del proyecto integrador. Se resuelve con el proveedor de cada uno."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Objetivo de la clase\n",
    "\n",
    "Al final de la clase vas a poder:\n",
    "- Explicar qué es un embedding y por qué la similitud coseno mide \"cercanía de significado\".\n",
    "- Limpiar y normalizar texto antes de vectorizarlo.\n",
    "- Elegir una estrategia de chunking (tamaño, solapamiento) con criterio, no por default.\n",
    "- Diseñar metadata que permita trazar cada fragmento hasta su documento de origen.\n",
    "- Separar claramente el pipeline de ingesta del de consulta.\n",
    "\n",
    "**Checkpoint del proyecto integrador de hoy**: pipeline de ingesta del corpus (limpieza, chunking y metadata) — ver `proyecto-integrador/README.md`, checkpoint Clase 4."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Agenda\n",
    "\n",
    "1. Información estructurada vs. no estructurada\n",
    "2. Embeddings y similitud semántica\n",
    "3. Tu proveedor: embeddings — referencia rápida\n",
    "4. Limpieza y normalización\n",
    "5. Estrategias de chunking y solapamiento\n",
    "6. Metadata, identificadores y trazabilidad\n",
    "7. Separación entre ingesta y consulta\n",
    "8. Comparación de estrategias de chunking\n",
    "9. Chunking semántico (contenido complementario)\n",
    "10. Laboratorio: pipeline de ingesta documental"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Información estructurada vs. no estructurada\n",
    "\n",
    "- **Estructurada**: tablas, JSON, filas de una base de datos — ya tiene un esquema. Se consulta con SQL/filtros exactos, no necesita embeddings.\n",
    "- **No estructurada**: texto libre (documentación, tickets, emails, PDFs) — no tiene un esquema uniforme. Es el caso que nos ocupa de acá en adelante: para \"buscar por significado\" en texto libre necesitamos convertirlo a una representación que capture semántica, no solo keywords.\n",
    "\n",
    "El corpus del TP integrador (documentación técnica) es no estructurado — eso es justamente lo que hace necesario todo lo que viene en esta clase."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Embeddings y similitud semántica\n",
    "\n",
    "Un embedding es un vector $\\vec{v} \\in \\mathbb{R}^d$ que representa el significado de un texto. Textos semánticamente parecidos quedan \"cerca\" en ese espacio — se mide con **similitud coseno**:\n",
    "\n",
    "$$\n",
    "\\text{sim}(\\vec{a}, \\vec{b}) = \\frac{\\vec{a} \\cdot \\vec{b}}{\\lVert \\vec{a} \\rVert \\, \\lVert \\vec{b} \\rVert}\n",
    "$$\n",
    "\n",
    "Cercano a 1 → misma dirección → mismo significado aproximado. Cercano a 0 → sin relación. (Esto ya se mencionó en la Clase 1 — hoy lo usamos en código real por primera vez.)"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "import os, json\n",
    "from dotenv import load_dotenv\n",
    "load_dotenv()\n",
    "\n",
    "import boto3\n",
    "bedrock = boto3.client(\"bedrock-runtime\", region_name=os.environ.get(\"AWS_REGION\", \"us-east-1\"))\n",
    "EMBED_MODEL_ID = os.environ.get(\"BEDROCK_MODEL_ID_EMBED\", \"cohere.embed-v4:0\")\n",
    "\n",
    "def embed_bedrock(textos: list[str], input_type: str = \"search_document\") -> list[list[float]]:\n",
    "    \"\"\"Devuelve un embedding (lista de floats) por cada texto de la lista, usando Cohere Embed v4 en Bedrock.\"\"\"\n",
    "    body = json.dumps({\"texts\": textos, \"input_type\": input_type, \"embedding_types\": [\"float\"]})\n",
    "    resp = bedrock.invoke_model(modelId=EMBED_MODEL_ID, body=body, accept=\"*/*\", contentType=\"application/json\")\n",
    "    resp_body = json.loads(resp[\"body\"].read())\n",
    "    return resp_body[\"embeddings\"][\"float\"]"
   ],
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "import numpy as np\n",
    "\n",
    "def similitud_coseno(a, b):\n",
    "    a, b = np.array(a), np.array(b)\n",
    "    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))\n",
    "\n",
    "frases = [\n",
    "    \"La ventana de contexto limita cuánto texto puede procesar un modelo por llamada.\",\n",
    "    \"El límite de tokens de entrada y salida define cuánta información cabe en una consulta.\",\n",
    "    \"Ualá es una fintech argentina que ofrece una tarjeta prepaga y una cuenta digital.\",\n",
    "]\n",
    "\n",
    "vectores = embed_bedrock(frases)\n",
    "print(f\"Dimensión de cada embedding: {len(vectores[0])}\")\n",
    "\n",
    "print(\"\\nSimilitud entre frase 1 y 2 (ambas sobre contexto/tokens):\", round(similitud_coseno(vectores[0], vectores[1]), 3))\n",
    "print(\"Similitud entre frase 1 y 3 (temas no relacionados):       \", round(similitud_coseno(vectores[0], vectores[2]), 3))"
   ],
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**🏠 Practicá**: agregá una cuarta frase que hable de otra cosa totalmente distinta (ej. una receta de cocina) y confirmá que su similitud con las otras tres es la más baja del grupo."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Tu proveedor: embeddings — referencia rápida\n",
    "\n",
    "Igual que con generación (Clase 2), elegí el proveedor que tengas disponible. **Anthropic no tiene modelo de embeddings propio** — si tu proveedor de generación es Anthropic, combinalo con cualquiera de los otros tres para esta parte.\n",
    "\n",
    "```bash\n",
    "pip install numpy       # ya instalado si veniás de clases anteriores\n",
    "pip install openai      # si usás OpenAI\n",
    "pip install google-genai\n",
    "pip install ollama\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# --- OpenAI ---\n",
    "from openai import OpenAI\n",
    "\n",
    "def embed_openai(textos: list[str]) -> list[list[float]]:\n",
    "    client = OpenAI(api_key=os.environ[\"OPENAI_API_KEY\"])\n",
    "    resp = client.embeddings.create(model=os.environ.get(\"OPENAI_EMBEDDING_MODEL_ID\", \"text-embedding-3-large\"), input=textos)\n",
    "    return [d.embedding for d in resp.data]\n",
    "\n",
    "\n",
    "# --- Google Gemini ---\n",
    "from google import genai\n",
    "from google.genai import types\n",
    "\n",
    "def embed_google(textos: list[str]) -> list[list[float]]:\n",
    "    client = genai.Client(api_key=os.environ[\"GOOGLE_API_KEY\"])\n",
    "    resp = client.models.embed_content(\n",
    "        model=os.environ.get(\"GOOGLE_EMBEDDING_MODEL_ID\", \"text-embedding-004\"),\n",
    "        contents=textos,\n",
    "    )\n",
    "    return [e.values for e in resp.embeddings]\n",
    "\n",
    "\n",
    "# --- Ollama (local) ---\n",
    "import ollama\n",
    "\n",
    "def embed_ollama(textos: list[str]) -> list[list[float]]:\n",
    "    resp = ollama.embed(model=os.environ.get(\"OLLAMA_EMBEDDING_MODEL_ID\", \"nomic-embed-text\"), input=textos)\n",
    "    return resp.embeddings"
   ],
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**🏠 Practicá**: corré la misma lista de `frases` de la sección 2 con la función de tu proveedor y recalculá las similitudes coseno. Los valores exactos van a diferir de los de Bedrock (cada modelo de embeddings vive en su propio espacio vectorial — nunca mezcles embeddings de dos proveedores distintos en el mismo índice), pero el **orden relativo** (frase 1 más parecida a frase 2 que a frase 3) debería mantenerse."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Limpieza y normalización\n",
    "\n",
    "Antes de vectorizar, conviene limpiar el texto — no es cosmético, afecta directamente la calidad de la búsqueda:\n",
    "\n",
    "- **Espacios y saltos de línea redundantes**: texto extraído de PDF/HTML suele traer basura de formato.\n",
    "- **Boilerplate repetido** (headers/footers, \"Página X de Y\", menús de navegación): si aparece en todos los chunks, contamina la similitud — todo se parece un poco entre sí por el ruido compartido.\n",
    "- **Normalización Unicode**: comillas tipográficas, acentos mal codificados, etc.\n",
    "- **¿Lowercase?** Depende: para texto natural generalmente no hace falta (los embeddings modernos son robustos a mayúsculas), pero para código o identificadores técnicos, bajar a minúsculas puede destruir información relevante (`API_KEY` ≠ `api_key` en un fragmento de código). No lo hagas por default sin pensarlo."
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "import re\n",
    "import unicodedata\n",
    "\n",
    "def limpiar_texto(texto: str) -> str:\n",
    "    texto = unicodedata.normalize(\"NFKC\", texto)           # normaliza comillas/acentos\n",
    "    texto = re.sub(r\"[ \\t]+\", \" \", texto)                   # espacios repetidos\n",
    "    texto = re.sub(r\"\\n{3,}\", \"\\n\\n\", texto)                # más de 2 saltos de línea seguidos\n",
    "    return texto.strip()\n",
    "\n",
    "\n",
    "texto_sucio = \"\"\"   Página 1 de 3\n",
    "\n",
    "\n",
    "Guía  de   configuración\n",
    "\n",
    "\n",
    "Para configurar  las credenciales,   copiá .env.example a .env.\\n\\n\\n\\nCompletá la sección de tu proveedor.\n",
    "\"\"\"\n",
    "\n",
    "print(repr(limpiar_texto(texto_sucio)))"
   ],
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**🏠 Practicá**: agregá una regla a `limpiar_texto` que detecte y elimine una línea de boilerplate recurrente (ej. `\"Página X de Y\"` con una regex) — es el tipo de ruido que vas a encontrar en PDFs reales del corpus del TP."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. Estrategias de chunking y solapamiento\n",
    "\n",
    "Un documento entero casi nunca entra (ni conviene que entre) en un solo embedding — hay que partirlo en **chunks**. Dos decisiones centrales:\n",
    "\n",
    "- **Tamaño del chunk**: muy chico → pierde contexto (una oración sola puede ser ambigua). Muy grande → mezcla varios temas en un solo vector, diluyendo la similitud con cualquiera de ellos.\n",
    "- **Solapamiento (overlap)**: sin overlap, una idea que cruza el límite entre dos chunks queda cortada en ambos. Con un poco de overlap (ej. 10-20% del tamaño del chunk), se mitiga ese corte a costa de un poco de redundancia."
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "def chunking_por_caracteres(texto: str, tamano: int = 300, solapamiento: int = 50) -> list[str]:\n",
    "    \"\"\"Chunking de tamaño fijo con solapamiento, por caracteres (simple, no respeta oraciones).\"\"\"\n",
    "    chunks = []\n",
    "    paso = tamano - solapamiento\n",
    "    for inicio in range(0, len(texto), paso):\n",
    "        chunk = texto[inicio:inicio + tamano]\n",
    "        if chunk.strip():\n",
    "            chunks.append(chunk)\n",
    "        if inicio + tamano >= len(texto):\n",
    "            break\n",
    "    return chunks\n",
    "\n",
    "\n",
    "def chunking_por_parrafos(texto: str, max_chars: int = 500) -> list[str]:\n",
    "    \"\"\"Agrupa párrafos (separados por línea en blanco) hasta llegar al tamaño máximo.\"\"\"\n",
    "    parrafos = [p.strip() for p in texto.split(\"\\n\\n\") if p.strip()]\n",
    "    chunks, actual = [], \"\"\n",
    "    for p in parrafos:\n",
    "        if len(actual) + len(p) + 1 <= max_chars:\n",
    "            actual = (actual + \"\\n\\n\" + p).strip()\n",
    "        else:\n",
    "            if actual:\n",
    "                chunks.append(actual)\n",
    "            actual = p\n",
    "    if actual:\n",
    "        chunks.append(actual)\n",
    "    return chunks"
   ],
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6. Metadata, identificadores y trazabilidad\n",
    "\n",
    "Un chunk suelto, sin contexto de dónde vino, no sirve para citar fuentes (Clase 6) ni para debuggear por qué el sistema recuperó algo irrelevante (Clase 7). Cada chunk necesita viajar con su metadata."
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "import hashlib\n",
    "from dataclasses import dataclass, field\n",
    "\n",
    "@dataclass\n",
    "class Chunk:\n",
    "    texto: str\n",
    "    documento_id: str\n",
    "    posicion: int           # orden del chunk dentro del documento\n",
    "    chunk_id: str = field(init=False)\n",
    "\n",
    "    def __post_init__(self):\n",
    "        # id determinístico: mismo documento + misma posición -> mismo id, siempre\n",
    "        hash_contenido = hashlib.sha256(self.texto.encode()).hexdigest()[:8]\n",
    "        self.chunk_id = f\"{self.documento_id}-{self.posicion:03d}-{hash_contenido}\"\n",
    "\n",
    "\n",
    "def construir_chunks(texto: str, documento_id: str, tamano: int = 300, solapamiento: int = 50) -> list[Chunk]:\n",
    "    textos = chunking_por_caracteres(texto, tamano, solapamiento)\n",
    "    return [Chunk(texto=t, documento_id=documento_id, posicion=i) for i, t in enumerate(textos)]\n",
    "\n",
    "\n",
    "corpus_ejemplo = \"\"\"La Converse API de Bedrock es una interfaz unificada para conversación. Funciona igual para\n",
    "distintos modelos: cambia el modelId, no la forma de llamar. Soporta mensajes de sistema,\n",
    "parámetros de inferencia como temperatura y top_p, y tool calling con un schema JSON de argumentos.\n",
    "\n",
    "Para usarla se necesita un cliente de boto3 apuntando al servicio bedrock-runtime, y credenciales\n",
    "configuradas vía variables de entorno o un perfil de AWS.\"\"\"\n",
    "\n",
    "chunks = construir_chunks(limpiar_texto(corpus_ejemplo), documento_id=\"doc-converse-api\")\n",
    "for c in chunks:\n",
    "    print(f\"[{c.chunk_id}] (pos {c.posicion}) {c.texto[:60]}...\")"
   ],
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**🏠 Practicá**: agregá un campo `fuente: str` (ej. una URL o un nombre de archivo) al dataclass `Chunk`, y otro campo `fecha_ingesta` con un timestamp. Esto es exactamente lo que vas a necesitar en la Clase 6 para implementar citas."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 7. Separación entre ingesta y consulta\n",
    "\n",
    "Son dos pipelines distintos, que corren en momentos distintos:\n",
    "\n",
    "- **Ingesta** (lo de hoy): se corre una vez (o cada vez que el corpus cambia) — limpiar, chunkear, embeber, guardar en un índice. Es costoso en tiempo pero infrecuente.\n",
    "- **Consulta** (Clase 5 en adelante): se corre en cada pregunta del usuario — embeber la consulta y buscar en el índice ya construido. Tiene que ser rápido.\n",
    "\n",
    "Error común: mezclar la lógica de las dos etapas en una sola función que \"ingesta y busca\" — hace que no se pueda optimizar cada una por separado (por ejemplo, batchear la ingesta, cachear embeddings de consultas frecuentes)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 8. Comparación de estrategias de chunking\n",
    "\n",
    "No hay un tamaño \"correcto\" — depende del corpus y de qué tipo de pregunta se espera responder. Comparemos en la práctica."
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "documento_largo = corpus_ejemplo * 3  # simulamos un documento más largo repitiendo el de ejemplo\n",
    "\n",
    "for tamano, overlap in [(150, 0), (150, 30), (400, 0), (400, 80)]:\n",
    "    chunks_resultantes = chunking_por_caracteres(documento_largo, tamano=tamano, solapamiento=overlap)\n",
    "    print(f\"tamano={tamano:>4} overlap={overlap:>3} -> {len(chunks_resultantes)} chunks\")"
   ],
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**🏠 Practicá**: corré `chunking_por_parrafos` sobre el mismo `documento_largo` con dos valores de `max_chars` distintos, y compará la cantidad de chunks contra `chunking_por_caracteres`. ¿En qué casos el chunking por párrafos corta \"mejor\" (en límites de idea) que el de tamaño fijo?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 9. Chunking semántico (contenido complementario)\n",
    "\n",
    "Más allá de tamaño fijo o por párrafos, existe el **chunking semántico**: se embeben oraciones consecutivas y se corta el chunk donde la similitud entre una oración y la siguiente cae por debajo de un umbral — la idea es que el corte coincida con un cambio real de tema, no con un límite arbitrario de caracteres.\n",
    "\n",
    "Es más costoso (requiere embeber a nivel oración durante la ingesta, no solo el chunk final) y no siempre mejora los resultados lo suficiente para justificar el costo — por eso queda como lectura complementaria, no como técnica obligatoria del curso. Si te interesa, buscá \"semantic chunking\" + el framework que estés usando (ej. LangChain tiene un `SemanticChunker`)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 10. Laboratorio: pipeline de ingesta documental\n",
    "\n",
    "**🏠 Tarea de la semana — entregar/completar antes de la Clase 5.**\n",
    "\n",
    "**Checkpoint del proyecto integrador (Clase 4)**: pipeline de ingesta del corpus (limpieza, chunking y metadata) listo para alimentar el índice vectorial de la Clase 5.\n",
    "\n",
    "### Consigna\n",
    "\n",
    "1. Tomá el corpus de referencia provisto por la cátedra (o un subconjunto representativo, para no esperar horas de embeddings si el corpus es grande).\n",
    "2. Aplicá `limpiar_texto` (o tu propia versión extendida con la practicá de la sección 4) a cada documento.\n",
    "3. Chunkeá cada documento con la estrategia que prefieras (tamaño fijo o por párrafos) — justificá en un comentario por qué elegiste ese tamaño/overlap para este corpus en particular.\n",
    "4. Construí un `Chunk` por fragmento, con `documento_id`, `posicion`, y al menos `fuente` (de la practicá de la sección 6).\n",
    "5. Embebé todos los chunks con la función de tu proveedor y guardá los vectores junto con su `chunk_id` en una estructura simple (una lista de dicts, o un `.json` / `.pkl` — en la Clase 5 esto se migra a un vector store real).\n",
    "\n",
    "### Criterio de éxito\n",
    "\n",
    "- Corriendo el pipeline sobre el corpus completo (o el subconjunto elegido) no tira ningún error.\n",
    "- Cada chunk resultante tiene menos de ~1500 caracteres (si no, revisá el tamaño elegido).\n",
    "- Podés tomar cualquier `chunk_id` y recuperar de qué documento y qué posición vino, sin ambigüedad.\n",
    "- El código de ingesta no incluye ninguna lógica de \"búsqueda\" — eso es, a propósito, la Clase 5."
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "def pipeline_ingesta(documentos: dict[str, str], tamano=300, solapamiento=50, embed_fn=embed_bedrock) -> list[dict]:\n",
    "    \"\"\"documentos: {documento_id: texto_crudo}. Devuelve una lista de {chunk_id, texto, vector, documento_id, posicion}.\"\"\"\n",
    "    # TODO: para cada documento, limpiar -> chunkear -> construir Chunk -> embeber (en batch, no uno por uno)\n",
    "    # TODO: devolver la lista combinando los datos del Chunk con su vector correspondiente\n",
    "    raise NotImplementedError\n",
    "\n",
    "\n",
    "# Prueba (va a fallar hasta que completes el TODO):\n",
    "# resultado = pipeline_ingesta({\"doc-converse-api\": corpus_ejemplo})\n",
    "# print(len(resultado), \"chunks ingeridos\")"
   ],
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Cierre\n",
    "\n",
    "- Hoy construimos la mitad \"offline\" de un sistema RAG: limpieza, chunking con criterio, metadata trazable y embeddings — sin tocar todavía la parte de búsqueda.\n",
    "- Próxima clase: vector stores — ahí vive el índice que el pipeline de hoy alimenta, y ahí empieza la mitad \"online\" (la consulta).\n",
    "- Antes de la próxima clase: dejar el pipeline de la sección 10 funcionando sobre el corpus del TP."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}