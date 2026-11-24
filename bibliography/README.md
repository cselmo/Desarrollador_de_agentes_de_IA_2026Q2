# Bibliografía del curso

Cada clase tiene un `apunte.md` (en su carpeta) que empieza con la sección **Fuentes**: la lista completa de referencias de esa clase, con un resumen de qué contiene cada una y por qué se usa. Este directorio guarda las que se pueden descargar libremente.

## Cómo bajar los PDFs

Los PDFs **no están en el repositorio** (es público y muchos tienen copyright de sus autores o editoriales). Cada uno los baja localmente para estudio:

```bash
bash bibliography/descargar.sh     # desde la raíz del repo
```

El script baja ~80 PDFs (papers de arXiv y algunos libros/papers de acceso abierto) a `bibliography/papers/`, que está en `.gitignore`. Respeta una pausa de 3 s entre descargas de arXiv, saltea lo que ya existe y descarta respuestas que no sean PDF (páginas anti-bot o de login). Al final lista los que hay que bajar a mano desde el navegador.

## Convención de nombres

`AÑO_primerautor_identificador.pdf`, por ejemplo `2022_yao_2210.03629.pdf` (ReAct). En los apuntes, las fuentes descargables están marcadas con 📄 y llevan el nombre de archivo al lado.

## Fuentes que no se descargan

- **Libros comerciales** (Kleppmann, *Designing Data-Intensive Applications*; Nygard, *Release It!*; Efron & Tibshirani, *An Introduction to the Bootstrap*, entre otros): se citan con capítulo; están en bibliotecas o en las plataformas de cada editorial.
- **Blogs de ingeniería y documentación oficial** (Anthropic, AWS Builders' Library, Stripe, documentación de proveedores): se citan con su URL; se leen online y pueden cambiar con el tiempo.
- **Papers de congresos sin versión abierta** (por ejemplo, Järvelin & Kekäläinen 2002, Smucker et al. 2007): se citan con su referencia completa; suelen estar disponibles a través de la biblioteca del ITBA.

## Apuntes disponibles

| Clase | Apunte |
|---|---|
| 7 — RAG avanzado y debugging | [`clase-07-rag-avanzado-debugging/apunte.md`](../clase-07-rag-avanzado-debugging/apunte.md) |
| 8 — Evaluación y mejora de RAG | [`clase-08-evaluacion-mejora-rag/apunte.md`](../clase-08-evaluacion-mejora-rag/apunte.md) |
| 9 — Herramientas y workflows agénticos | [`clase-09-herramientas-workflows-agenticos/apunte.md`](../clase-09-herramientas-workflows-agenticos/apunte.md) |
| 10 — LangGraph, human-in-the-loop y MCP | [`clase-10-langgraph-hitl-mcp/apunte.md`](../clase-10-langgraph-hitl-mcp/apunte.md) |

Los apuntes de las clases 1 a 6 están en preparación.
