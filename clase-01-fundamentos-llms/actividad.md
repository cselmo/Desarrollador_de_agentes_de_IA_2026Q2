# Actividad — Matriz de selección de modelos

Duración estimada: 25 minutos, en grupos de 2-3 personas.

## Contexto

Recordá el objetivo del [Trabajo Práctico Final Integrador](../proyecto-integrador/README.md): un sistema RAG + flujo con agentes, sobre un corpus de documentación técnica, expuesto vía API.

Antes de programar nada, hay que decidir **qué modelos usar** — no es una decisión trivial ni única: hace falta un modelo para generación/agentes y otro (o el mismo proveedor) para embeddings.

## Consigna

El curso es agnóstico de proveedor (Anthropic, OpenAI, Google, AWS Bedrock o modelos abiertos vía Ollama son todas opciones válidas para el TP). En grupo, completen la siguiente matriz comparando **al menos 3 modelos de al menos 2 proveedores distintos** (incluyendo al menos uno propietario y uno abierto), evaluando cada uno para dos roles distintos dentro del TP:

1. Como modelo de **generación / agente** (el que responde y decide qué herramienta invocar).
2. Como modelo de **embeddings** (el que vectoriza el corpus para la recuperación semántica).

### Plantilla

| Modelo (proveedor) | Rol (generación / embeddings) | Propietario / Abierto | Calidad esperada para la tarea | Costo relativo | Latencia esperada | Privacidad / dónde procesa los datos | Funciones disponibles (tool calling, structured outputs, streaming) | ¿Lo elegirían para el TP? ¿Por qué? |
|---|---|---|---|---|---|---|---|---|
| Claude Sonnet 4.6 (Anthropic / AWS Bedrock) | | | | | | | | |
| Cohere Embed 4 (AWS Bedrock) | | | | | | | | |
| GPT-4o o equivalente (OpenAI) | | | | | | | | |
| Gemini (Google) | | | | | | | | |
| (modelo abierto a elección, ej. Llama vía Ollama) | | | | | | | | |

### Preguntas guía

- ¿Qué modelo usarían si el corpus del TP tuviera datos confidenciales que no pueden salir de la infraestructura de la organización?
- Si el volumen de consultas esperado fuera muy alto (miles por día), ¿cómo cambia la decisión de costo/latencia?
- ¿Hay algún caso en el que convenga usar un modelo distinto para generación y para embeddings, en vez del mismo proveedor para ambos?

## Entregable

No hay entrega formal para esta actividad — es preparatoria para justificar, en la documentación final del TP (Clase 12), la elección de modelos que hizo el grupo durante toda la cursada. Guardar la matriz completada: se va a reutilizar como base del informe final.

## Criterio de éxito

La matriz está completa si cada celda tiene una justificación concreta (no solo "sí"/"no"), y el grupo puede explicar en una frase por qué eligieron el modelo de generación y el de embeddings que van a usar de acá en adelante en el curso.
