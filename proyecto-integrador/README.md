# Trabajo Práctico Final Integrador

## Objetivo

Construir, a lo largo de las 12 clases, un mismo sistema de software que combine:

1. Un pipeline **RAG** (ingesta → recuperación → generación sustentada con citas a fuentes) sobre un corpus documental.
2. Un **flujo con agentes/herramientas** que, además de consultar el corpus, pueda invocar al menos una herramienta externa (API, función, o servicio simulado) de forma controlada y trazable.
3. El sistema **desplegado**: expuesto vía API (FastAPI) y accesible mediante una demo (por ejemplo, Streamlit o un cliente de prueba), no solo ejecutable en notebook.

Es un **único trabajo práctico, igual para todos los participantes** — no hay elección de dominio o dataset propio. El dominio y el corpus de referencia los fija el cuerpo docente y son los mismos para toda la cohorte, de modo que el material de clase (slides, notebooks, ejemplos) es directamente aplicable al TP.

## Dominio y dataset de referencia

Corpus de documentación técnica pública (manuales/documentación de un producto o API de uso abierto, sin datos sensibles ni información propietaria), provisto por la cátedra al inicio de la Clase 1. Se usa el mismo corpus en todos los laboratorios de la cursada.

## Checkpoints por clase

Cada laboratorio semanal agrega una pieza al mismo proyecto. Al final de cada clase el estudiante debe tener:

| Clase | Checkpoint esperado |
|---|---|
| 1 | Matriz de selección de modelos completada; TP presentado y entendido. |
| 2 | Cliente funcional (`LLMClient`) para consumir un modelo generativo vía API, con manejo básico de errores y reintentos, funcionando con el proveedor que cada estudiante tenga disponible (no es obligatorio AWS Bedrock). |
| 3 | El mismo cliente, ahora detrás de una interfaz agnóstica de proveedor (Anthropic, OpenAI, Google o AWS Bedrock), más un servicio que devuelve salidas estructuradas y validadas (Pydantic) a partir de texto libre. |
| 4 | Pipeline de ingesta del corpus: limpieza, chunking y metadata. |
| 5 | Índice vectorial construido (embeddings del proveedor elegido) y buscador semántico funcionando. |
| 6 | Pipeline RAG end-to-end: consulta → recuperación → contexto → respuesta generada. |
| 7 | Casos fallidos del RAG identificados, diagnosticados y corregidos. |
| 8 | Dataset de evaluación armado y métricas base (fidelidad, relevancia, costo, latencia) medidas. |
| 9 | Al menos una herramienta externa integrada con tool calling, con contrato de entrada/salida validado. |
| 10 | Workflow con estado (LangGraph o equivalente) que decide entre consulta RAG y herramienta externa, con un punto de aprobación humana para acciones sensibles. |
| 11 | Sistema expuesto vía FastAPI, con logging estructurado, manejo de errores y checklist de seguridad aplicado. |
| 12 | Integración final, pruebas end-to-end, documentación, diagrama de arquitectura y entrega. |

## Entrega final (Clase 12)

- Repositorio del proyecto documentado (README con instrucciones de instalación y ejecución).
- API funcionando localmente (o desplegada) con endpoints documentados.
- Demo accesible (Streamlit u otro cliente) para probar el flujo RAG + agente.
- Informe breve: arquitectura, decisiones técnicas, resultados de evaluación, costos y riesgos identificados.
- Exposición individual del trabajo ante la cátedra.

## Requisitos de aprobación del TP

Cumplir con el objetivo funcional (RAG + agente + despliegue), aprobar los checkpoints intermedios de cada clase, y exponer el trabajo final, conforme a los [requisitos de aprobación](../README.md#requisitos-de-aprobación) del programa.
