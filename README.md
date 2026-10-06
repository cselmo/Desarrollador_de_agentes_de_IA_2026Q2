# Certificación Profesional en Desarrollador de Agentes de IA

La Inteligencia Artificial Generativa pasó de la experimentación aislada a la construcción de aplicaciones capaces de interactuar con documentos, bases de datos, APIs y sistemas corporativos. Cada vez más organizaciones impulsan la adopción y creación de agentes de IA como palanca estratégica para escalar procesos, automatizar tareas complejas y potenciar la toma de decisiones.

Sin embargo, existe una diferencia sustancial entre desarrollar una demostración y construir un agente confiable, evaluable e integrable a los sistemas productivos de una empresa. Los sistemas basados en modelos de lenguaje deben resolver problemas concretos relacionados con la recuperación de información, la calidad de las respuestas, la seguridad, los costos, la observabilidad y la integración con el software existente —desafíos que se vuelven críticos cuando los agentes operan sobre datos sensibles, transacciones y flujos de negocio en producción.

Esta certificación, desarrollada por **ITBA Educación Ejecutiva**, es una formación intensiva y aplicada en ingeniería de aplicaciones basadas en modelos de lenguaje, Retrieval-Augmented Generation (RAG) y workflows agénticos. El programa prioriza la construcción progresiva de una solución completa, combinando clases sincrónicas, actividades asincrónicas y un **Trabajo Práctico Final Integrador**.

## Objetivos del programa

- Presentar el funcionamiento práctico de los modelos de lenguaje, sus capacidades, limitaciones y criterios de selección.
- Desarrollar aplicaciones que consuman modelos mediante APIs y produzcan resultados estructurados y validados.
- Diseñar pipelines de ingesta, embeddings y recuperación sobre documentos y datos privados.
- Construir soluciones RAG que generen respuestas sustentadas en evidencia recuperada.
- Aplicar técnicas de evaluación para medir recuperación, fidelidad, relevancia, costo y latencia.
- Diseñar workflows agénticos capaces de utilizar herramientas externas de manera controlada y trazable.
- Incorporar medidas básicas de seguridad, observabilidad y manejo de errores.
- Exponer la aplicación mediante una API y preparar un prototipo reproducible y documentado.
- Desarrollar criterio técnico para evaluar factibilidad, costos, riesgos y decisiones arquitectónicas.

## Objetivos de formación

Se espera que los participantes puedan:

- Consumir modelos de lenguaje mediante APIs, administrando configuración, credenciales, parámetros y errores.
- Diseñar prompts y contratos de salida mediante esquemas estructurados y Pydantic.
- Seleccionar modelos según criterios de calidad, costo, latencia y privacidad.
- Construir procesos de ingesta documental, normalización, chunking y vectorización.
- Implementar sistemas de recuperación semántica con embeddings, metadata y filtros.
- Construir un pipeline RAG con respuestas sustentadas y referencias a fuentes.
- Diferenciar errores de ingesta, recuperación, construcción de contexto y generación.
- Construir conjuntos de evaluación y comparar versiones de una solución.
- Aplicar técnicas de mejora como búsqueda híbrida o reranking.
- Diseñar workflows con estado, herramientas, rutas condicionales y límites de ejecución.
- Integrar servicios externos mediante APIs o Model Context Protocol.
- Aplicar controles básicos de seguridad sobre entradas, salidas, datos y herramientas.
- Registrar errores, costos, latencia y trazas de ejecución.
- Exponer una solución mediante FastAPI y documentar su ejecución.
- Defender decisiones técnicas relacionadas con arquitectura, calidad, costos y riesgos.

## Perfil del participante

La certificación está orientada a personas con base técnica que deseen especializarse en el desarrollo de aplicaciones de IA Generativa:

- Desarrolladores de software.
- Ingenieros y analistas de datos.
- Arquitectos de soluciones.
- Líderes técnicos y/o managers.
- Líderes de producto con experiencia técnica.

El programa requiere participación activa en laboratorios de programación. No está diseñado como una formación exclusivamente conceptual o gerencial.

## Metodología

La certificación se desarrolla mediante **12 clases sincrónicas virtuales de 3 horas, semanales**, actividades asincrónicas, laboratorios guiados, entregas incrementales y un Trabajo Práctico Final Integrador (ver [proyecto-integrador/README.md](proyecto-integrador/README.md)).

## Conocimientos mínimos

Se requiere conocimiento intermedio de programación en Python. El estudiante debe sentirse cómodo:

- definiendo funciones;
- trabajando con listas y diccionarios;
- instalando dependencias;
- utilizando entornos virtuales;
- interpretando excepciones;
- consumiendo APIs REST;
- trabajando con JSON;
- utilizando Git en operaciones básicas;
- leyendo documentación técnica.

También se recomienda conocimiento básico de bases de datos, familiaridad con desarrollo web, capacidad para utilizar una terminal y lectura de documentación técnica en inglés. No es obligatorio contar con experiencia previa en Machine Learning.

## Stack técnico

El curso es **agnóstico de proveedor**: el objetivo es que el estudiante sepa integrar cualquiera de los grandes proveedores de modelos, no atarse a uno solo. Desde la Clase 3 ("Abstracción de proveedores") el código se construye contra una interfaz propia, de modo que cambiar de proveedor sea una cuestión de configuración, no de reescribir lógica.

Proveedores cubiertos en los ejemplos y laboratorios:

- **Anthropic** (Claude, directo vía API o vía AWS Bedrock).
- **OpenAI** (GPT).
- **Google** (Gemini).
- **AWS Bedrock** como gateway multi-proveedor (incluye Claude, Cohere Embed, Llama, entre otros).
- **Modelos abiertos locales** (Ollama), como alternativa sin costo de API para practicar.

No hace falta tener cuenta en los cuatro — alcanza con **una** credencial de algún proveedor para seguir los laboratorios (la cátedra provee acceso a AWS Bedrock para quien no tenga credenciales propias). Ver [.env.example](.env.example) para la configuración. Las credenciales se cargan únicamente vía variables de entorno — nunca se hardcodean ni se suben al repositorio.

## Programa

### Clase 1: Fundamentos prácticos de aplicaciones con LLMs
Comprender el modelo, sus límites y sus costos.
- Qué es un modelo de lenguaje. Capacidades y limitaciones.
- Tokens y ventana de contexto. Generación probabilística. Temperatura y parámetros principales.
- Diferencia entre generación, embeddings y reranking.
- Modelos propietarios y modelos abiertos. Costo, latencia y privacidad. Criterios de selección de modelos.
- Presentación del Trabajo Práctico Final Integrador.
- Evolución desde RNN hasta Transformers. Intuición del mecanismo de self-attention. Tokenización BPE.
- Actividad: comparación entre modelos y elaboración de una matriz de selección.

### Clase 2: APIs, prompting y configuración
Del modelo a una aplicación de software.
- Configuración del entorno. Gestión de dependencias. Variables de entorno y credenciales.
- Consumo de APIs. Mensajes de sistema y usuario. Zero-shot y few-shot prompting.
- Delimitación de instrucciones y contexto. Parámetros de generación. Manejo básico de errores.
- Comparación entre llamadas síncronas y asíncronas.
- Laboratorio: construcción de un cliente básico para consumir un modelo mediante API.

### Clase 3: Salidas estructuradas y aplicaciones robustas
Generar resultados utilizables por otros sistemas.
- Structured outputs. JSON Schema. Validación con Pydantic. Manejo de respuestas inválidas.
- Tool calling. Timeouts. Reintentos. Rate limits.
- Registro de tokens. Estimación de costos. Medición de latencia.
- Streaming. Backoff. Abstracción de proveedores.
- Laboratorio: construcción de un servicio que transforme entradas no estructuradas en objetos validados.

### Clase 4: Embeddings e ingesta documental
Preparación de información para recuperación semántica.
- Información estructurada y no estructurada. Embeddings. Similitud semántica.
- Limpieza y normalización. Estrategias de chunking. Solapamiento.
- Metadata. Identificadores y trazabilidad. Separación entre ingesta y consulta.
- Laboratorio: construcción del pipeline inicial de ingesta documental.

### Clase 5: Vector stores y recuperación
Construcción del motor de búsqueda semántica.
- Almacenamiento vectorial. Similitud coseno. Recuperación por vecinos cercanos. Top-k.
- Filtrado por metadata. Persistencia del índice. Selección de modelos de embeddings.
- Diagnóstico de resultados irrelevantes y redundantes. Comparación entre ChromaDB y FAISS. Embeddings locales.
- Laboratorio: implementación de un buscador semántico sobre el conjunto documental.

### Clase 6: Arquitectura RAG
Construcción de un sistema de generación sustentada.
- Arquitectura Retrieval-Augmented Generation. Flujo consulta-recuperación-contexto-generación.
- Construcción explícita sin frameworks de alto nivel. Diseño del prompt con evidencia recuperada.
- Gestión de la ventana de contexto. Separación entre instrucciones, evidencia y consulta.
- Respuestas sustentadas. Manejo de ausencia de evidencia. Implementación de citas.
- Laboratorio: integración del recuperador con el modelo generativo.

### Clase 7: RAG avanzado y debugging
Diagnóstico y mejora del pipeline.
- Errores de ingesta, recuperación, construcción del contexto y generación.
- Query rewriting. Ajuste de top-k. Redundancia de contexto. Context compression.
- Respuestas no sustentadas. Estrategias de debugging. Multi-query retrieval. Recuperación jerárquica.
- Laboratorio: análisis y corrección de casos fallidos del sistema RAG.

### Clase 8: Evaluación y mejora de RAG
Medir antes de optimizar.
- Evaluación de recuperación y generación. Construcción de un dataset de evaluación.
- Hit rate y recall. Fidelidad. Relevancia. Evaluación humana. LLM-as-a-Judge.
- Comparación de versiones. Medición de costo y latencia. Análisis de errores.
- RAGAS. Precision@k y MRR. BM25. Búsqueda híbrida. Reranking.
- Laboratorio: medición del sistema base y comparación de resultados.

### Clase 9: Herramientas y workflows agénticos
Automatización inteligente bajo control.
- Diferencia entre chatbot, workflow y agente. Casos en los que no conviene utilizar agentes.
- Tool calling. Diseño de herramientas. Contratos de entrada y salida. Validación de argumentos.
- Estado de ejecución. Rutas condicionales. Límites de pasos. Registro de decisiones.
- Reintentos. Fallbacks. Prevención de loops. Idempotencia. Registro de acciones.
- Laboratorio: construcción de un workflow que seleccione entre consulta documental y herramienta externa.

### Clase 10: LangGraph, human-in-the-loop y MCP
Orquestación e interoperabilidad.
- Workflows con estado. Nodos, transiciones y condiciones. Manejo de errores.
- Aprobación humana. Acciones sensibles.
- Introducción a Model Context Protocol. Clientes, servidores, herramientas y recursos.
- Consumo de una herramienta mediante MCP. Comparación entre API directa, tool calling y MCP.
- Creación mínima de un servidor MCP. Comparación con otros frameworks.
- Laboratorio: integración de una herramienta externa con aprobación humana.

### Clase 11: Seguridad, observabilidad y despliegue
Preparación de un prototipo reproducible e integrable.
- Seguridad: prompt injection directa e indirecta, contenido recuperado no confiable, validación de entradas y salidas, autorización de herramientas, mínimo privilegio y gestión de credenciales.
- Observabilidad: logging estructurado, trazas por ejecución, tokens y costos, latencia por etapa, errores, reintentos y herramientas invocadas.
- Despliegue: FastAPI, modelos de entrada y salida, manejo de errores HTTP, configuración por entorno, health checks y documentación automática.
- Docker. Persistencia mínima. Streamlit para demostraciones. Checklist de seguridad.
- Laboratorio: exposición de la solución mediante una API.

### Clase 12: Integración y cierre del Trabajo Práctico Final
Validación técnica de la solución.
- Integración de componentes. Pruebas end-to-end. Revisión de arquitectura y del pipeline de evaluación.
- Análisis de costos. Identificación de riesgos. Validación de resultados y cumplimiento de la consigna.
- Revisión final de criterios técnicos y de entrega. Retroalimentación docente.
- Finalización del repositorio, documentación, métricas y diagrama de arquitectura.
- Entrega: envío individual del Trabajo Práctico Final.

## Requisitos de aprobación

Asistencia igual o superior al 75%. Realización y aprobación de trabajos prácticos. Realización, aprobación y exposición del Trabajo Práctico Final Integrador.

## Cuerpo docente

**Carlos Selmo** — Ingeniero Electrónico (ITBA), desarrolla tareas en el área de procesamiento de señales y machine learning en el Grupo de Electrónica Digital Aplicada (GEDA). Profesor adjunto de materias en el área de procesamiento de señales, bio-electrónica y sistemas digitales, entre ellas Redes Neuronales y Redes Neuronales en Bioingeniería.

## Ficha técnica

- **Acreditación final:** Certificación Profesional en Desarrollador de Agentes de IA (ITBA Educación Ejecutiva)
- **Modalidad:** Virtual (sincrónica)
- **Duración:** 36 horas (12 clases x 3 horas)
- **Cursada:** Semanal
