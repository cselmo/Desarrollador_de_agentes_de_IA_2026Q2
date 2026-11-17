# Apunte — Clase 7: RAG avanzado y debugging

> **Cómo usar este apunte.** Es el marco teórico de la clase: el notebook muestra *cómo* se implementa; este documento explica *por qué* y de dónde sale cada idea. Las referencias entre corchetes remiten a la sección **Fuentes**, que está a continuación y explica qué contiene cada fuente y por qué se usa. 📄 = PDF descargable con `bibliography/descargar.sh` (ver [`bibliography/README.md`](../bibliography/README.md)).
>
> **Lectura obligatoria antes de la clase:** [2] (Seven Failure Points, 6 páginas) y §1–3 de [7] (Lost in the Middle).
> **Lectura recomendada después:** §II–IV de [1] (survey de RAG), [17] y [4].

---

## Fuentes

Las técnicas de "RAG avanzado" aparecieron casi todas entre 2022 y 2024, en papers de investigación y en reportes de ingeniería de la industria. El apunte usa como columna vertebral un **survey** [1] que las organiza, un **estudio empírico de fallas** [2] para el framework de diagnóstico, y luego la **fuente primaria** de cada técnica — porque los blogs que las resumen suelen perder las condiciones en que funcionan. 📄 = PDF descargable con `bibliography/descargar.sh`.

### Marco general y diagnóstico

**[1] 📄 Gao, Y. et al. (2023). *Retrieval-Augmented Generation for Large Language Models: A Survey*. arXiv:2312.10997.** — `2023_gao_2312.10997.pdf`
- *Qué contiene:* revisión de más de cien trabajos de RAG organizados en tres paradigmas — *naive*, *advanced* (optimizaciones antes y después de la recuperación) y *modular* — y en sus componentes: recuperación (fuente, granularidad, indexado, optimización de consultas), generación (curado y compresión de contexto), y patrones de recuperación iterativa, recursiva y adaptativa; incluye métricas y benchmarks.
- *Por qué está:* da el mapa y la taxonomía de la clase (§1); cada técnica que vemos se ubica en una de sus etapas. Es el punto de entrada más completo a la literatura.

**[2] 📄 Barnett, S., Kurniawan, S., Thudumu, S., Brannelly, Z. & Abdelrazek, M. (2024). *Seven Failure Points When Engineering a Retrieval Augmented Generation System*. CAIN 2024. arXiv:2401.05856.** — `2024_barnett_2401.05856.pdf`
- *Qué contiene:* reporte de experiencia de tres sistemas RAG reales (investigación, educación, biomedicina); identifica siete puntos de falla a lo largo del pipeline y extrae lecciones de ingeniería.
- *Por qué está:* es la base empírica del framework de diagnóstico por etapa (§2). A diferencia de los papers de técnicas, describe cómo fallan los sistemas *en la práctica*. Lectura obligatoria.

### Optimización de la consulta (pre-recuperación)

**[3] 📄 Ma, X., Gong, Y., He, P., Zhao, H. & Duan, N. (2023). *Query Rewriting for Retrieval-Augmented Large Language Models*. EMNLP 2023. arXiv:2305.14283.** — `2023_ma_2305.14283.pdf`
- *Qué contiene:* propone el esquema *Rewrite-Retrieve-Read*: reescribir la consulta antes de recuperar, primero con un LLM por prompting y luego con un reescritor chico entrenado por refuerzo usando como recompensa el desempeño del lector.
- *Por qué está:* fuente primaria de la reescritura de consultas (§3.2); muestra que la brecha entre cómo pregunta el usuario y lo que necesita el recuperador es un problema en sí mismo.

**[4] 📄 Gao, L., Ma, X., Lin, J. & Callan, J. (2022). *Precise Zero-Shot Dense Retrieval without Relevance Labels*. ACL 2023. arXiv:2212.10496.** — `2022_gao_2212.10496.pdf`
- *Qué contiene:* HyDE: un LLM genera un documento *hipotético* que respondería la consulta; se embebe ese documento (no la consulta) con un encoder contrastivo no supervisado y se buscan vecinos reales. El "cuello de botella" denso del encoder filtra los detalles inventados.
- *Por qué está:* fuente primaria de HyDE (§3.3) y una explicación elegante de la asimetría consulta–documento, que conecta con `input_type` de la Clase 4.

**[5] 📄 Zheng, H. S. et al. (2023). *Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models*. ICLR 2024. arXiv:2310.06117.** — `2023_zheng_2310.06117.pdf`
- *Qué contiene:* *step-back prompting*: antes de responder, el modelo formula una pregunta más general (el principio o concepto de fondo), recupera/razona sobre ella, y luego responde la original; mejora en ciencias (MMLU), preguntas temporales y multi-hop.
- *Por qué está:* aporta una tercera forma de transformar la consulta (abstraer en vez de reescribir o expandir) (§3.4), útil para preguntas demasiado específicas para el corpus.

**[6] 📄 Rackauckas, Z. (2024). *RAG-Fusion: a New Take on Retrieval-Augmented Generation*. International Journal on Natural Language Computing, 13(1). arXiv:2402.03367.** — `2024_rackauckas_2402.03367.pdf`
- *Qué contiene:* caso de aplicación en Infineon: generar varias reformulaciones de la consulta, recuperar con cada una y fusionar los rankings con RRF; la evaluación (manual) reporta respuestas más completas, pero también mayor latencia y respuestas que a veces se desvían cuando las reformulaciones se alejan de la intención original.
- *Por qué está:* fuente de la técnica multi-query del notebook (§3.5). Se elige justamente porque reporta también los costos y las fallas, no solo las mejoras.

### Uso del contexto y post-recuperación

**[7] 📄 Liu, N. F. et al. (2023). *Lost in the Middle: How Language Models Use Long Contexts*. TACL 2024. arXiv:2307.03172.** — `2023_liu_2307.03172.pdf`
- *Qué contiene:* experimentos controlados (QA multi-documento y recuperación clave-valor) moviendo la posición del dato relevante dentro del contexto: el desempeño es máximo al principio o al final y cae en el medio (curva en U), incluso en modelos de contexto largo; agregar más documentos puede empeorar el resultado.
- *Por qué está:* es la evidencia de que subir top-k no es gratis y de que el orden del contexto importa (§4.1). Lectura obligatoria.

**[8] 📄 Shi, F. et al. (2023). *Large Language Models Can Be Easily Distracted by Irrelevant Context*. ICML 2023. arXiv:2302.00093.** — `2023_shi_2302.00093.pdf`
- *Qué contiene:* construye GSM-IC (problemas de matemática con información irrelevante agregada) y muestra caídas grandes de exactitud; evalúa mitigaciones como self-consistency, ejemplos con distractores e instruir explícitamente al modelo a ignorar lo irrelevante.
- *Por qué está:* complementa a [7]: no solo la posición, sino el ruido mismo degrada la respuesta — justifica la compresión y la deduplicación (§4.2).

**[9] Carbonell, J. & Goldstein, J. (1998). *The Use of MMR, Diversity-Based Reranking for Reordering Documents and Producing Summaries*. SIGIR '98.**
- *Qué contiene:* define Maximal Marginal Relevance: seleccionar documentos que sean relevantes a la consulta y a la vez poco similares a los ya seleccionados, con un parámetro $\lambda$ que regula el balance.
- *Por qué está:* es la solución clásica (y todavía muy usada; la implementan la mayoría de los vector stores) al problema de chunks redundantes que vemos en el notebook (§4.3). Muestra que la redundancia no es un problema nuevo de RAG.

**[10] 📄 Xu, F., Shi, W. & Choi, E. (2023). *RECOMP: Improving Retrieval-Augmented LMs with Compression and Selective Augmentation*. ICLR 2024. arXiv:2310.04408.** — `2023_xu_2310.04408.pdf`
- *Qué contiene:* dos compresores entrenados — extractivo (elige oraciones) y abstractivo (resume) — que reducen el contexto a una fracción pequeña con poca pérdida; el compresor puede devolver vacío si los documentos no ayudan ("aumentación selectiva").
- *Por qué está:* fuente de la compresión de contexto (§4.4) y de una idea clave para el TP: a veces la mejor evidencia es *ninguna*.

**[11] 📄 Jiang, H., Wu, Q., Lin, C.-Y., Yang, Y. & Qiu, L. (2023). *LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models*. EMNLP 2023. arXiv:2310.05736.** — `2023_jiang_2310.05736.pdf`
- *Qué contiene:* compresión de prompts de grueso a fino: un controlador de presupuesto por segmento y una compresión iterativa a nivel token guiada por la perplejidad de un modelo chico; reporta compresiones de hasta 20× con poca pérdida.
- *Por qué está:* muestra la compresión desde otro ángulo (eliminar tokens poco informativos, sin entrenar un resumidor) (§4.4) y conecta con el costo por token de la Clase 3.

### Recuperación jerárquica, adaptativa y en grafos

**[12] 📄 Sarthi, P. et al. (2024). *RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval*. ICLR 2024. arXiv:2401.18059.** — `2024_sarthi_2401.18059.pdf`
- *Qué contiene:* construye un árbol de resúmenes: agrupa chunks por similitud (clustering con mezclas gaussianas), resume cada grupo y repite recursivamente; en consulta recupera de cualquier nivel del árbol. Mejora en QA sobre documentos largos (QuALITY, NarrativeQA, QASPER).
- *Por qué está:* es la formulación más rigurosa de la recuperación jerárquica del notebook (§5.2): preguntas de síntesis necesitan niveles de abstracción que un chunk solo no tiene.

**[13] 📄 Asai, A., Wu, Z., Wang, Y., Sil, A. & Hajishirzi, H. (2023). *Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection*. ICLR 2024. arXiv:2310.11511.** — `2023_asai_2310.11511.pdf`
- *Qué contiene:* entrena un modelo que emite *tokens de reflexión* para decidir si recuperar, juzgar si cada pasaje es relevante, si la generación está sustentada y si es útil; la recuperación pasa a ser adaptativa.
- *Por qué está:* formaliza la recuperación adaptativa y la autocrítica (§6.1), que en el TP implementamos de forma explícita con un umbral y un juez.

**[14] 📄 Yan, S.-Q., Gu, J.-C., Zhu, Y. & Ling, Z.-H. (2024). *Corrective Retrieval Augmented Generation*. arXiv:2401.15884.** — `2024_yan_2401.15884.pdf`
- *Qué contiene:* CRAG: un evaluador liviano estima la calidad de lo recuperado y dispara una de tres acciones (correcto → refinar; incorrecto → buscar en la web; ambiguo → combinar), con un algoritmo de descomposición y recomposición que filtra fragmentos irrelevantes.
- *Por qué está:* es el antecedente directo del flujo del TP: "si la evidencia no alcanza, hacer otra cosa" (en nuestro caso, abrir un ticket) (§6.2).

**[15] 📄 Hogan, A. et al. (2021). *Knowledge Graphs*. ACM Computing Surveys, 54(4). arXiv:2003.02320.** — `2020_hogan_2003.02320.pdf`
- *Qué contiene:* introducción exhaustiva a grafos de conocimiento: modelos de datos (grafos dirigidos etiquetados/RDF, grafos de propiedades), consultas, ontologías y razonamiento, embeddings de grafos, construcción y calidad.
- *Por qué está:* da las definiciones formales que GraphRAG presupone (§7.1). Es largo: alcanza con las secciones 1–2.

**[16] 📄 Edge, D. et al. (2024). *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*. arXiv:2404.16130.** — `2024_edge_2404.16130.pdf`
- *Qué contiene:* GraphRAG de Microsoft: un LLM extrae entidades y relaciones del corpus, se detectan comunidades jerárquicas con el algoritmo de Leiden, se pre-generan resúmenes por comunidad, y las consultas globales se responden con map-reduce sobre esos resúmenes; mejora la exhaustividad y diversidad frente a RAG vectorial en preguntas de "sentido global" del corpus.
- *Por qué está:* fuente primaria del contenido complementario de GraphRAG (§7.2); delimita con claridad para qué tipo de pregunta sirve (global) y para cuál no hace falta (puntual).

**[18] Traag, V. A., Waltman, L. & van Eck, N. J. (2019). *From Louvain to Leiden: guaranteeing well-connected communities*. Scientific Reports, 9, 5233.**
- *Qué contiene:* el algoritmo de Leiden de detección de comunidades, que corrige un defecto de Louvain (comunidades mal conectadas) y es más rápido.
- *Por qué está:* es la pieza algorítmica de GraphRAG [16] que convierte un grafo en "temas" resumibles (§7.2); se cita para que el paso no quede como magia.

### Industria y herramientas

**[17] Anthropic (2024). *Introducing Contextual Retrieval*.** https://www.anthropic.com/news/contextual-retrieval
- *Qué contiene:* propone anteponer a cada chunk un breve contexto generado por un LLM (a qué documento pertenece y de qué trata) antes de embeberlo e indexarlo en BM25; reporta que reduce las fallas de recuperación top-20 un 49%, y un 67% combinado con reranking.
- *Por qué está:* ataca la causa más común de falla de recuperación — el chunk perdió su contexto al cortarlo — con un experimento cuantificado (§3.6). Cruza con las clases 4 (chunking) y 8 (híbrida + reranking). Lectura recomendada.

**[19] Streamlit. Documentación: *Run your Streamlit app*, *Session State*, *Caching overview*, *Build a basic LLM chat app*.**
https://docs.streamlit.io/develop/concepts/architecture/run-your-app — https://docs.streamlit.io/develop/concepts/architecture/session-state — https://docs.streamlit.io/develop/concepts/architecture/caching — https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps
- *Qué contiene:* el modelo de ejecución de Streamlit (el script se re-ejecuta completo ante cada interacción), el estado por sesión, las dos formas de caché (`st.cache_data` y `st.cache_resource`) y el patrón de una app de chat.
- *Por qué está:* fuente primaria de §9; entender el modelo de ejecución evita los dos errores típicos de la demo (re-crear el cliente/índice en cada mensaje y perder el historial).

---

## 1. De RAG "naive" a RAG modular

Gao et al. [1] proponen tres paradigmas que sirven como mapa de la clase:

1. **Naive RAG** — lo que construimos en la Clase 6: indexar → recuperar top-k por similitud → concatenar en el prompt → generar. Sus problemas típicos: baja precision (chunks irrelevantes), bajo recall (chunks necesarios que no llegan), alucinaciones cuando el contexto no alcanza, y redundancia.
2. **Advanced RAG** — agrega optimizaciones en dos lugares:
   - **pre-recuperación**: mejorar el índice (chunking, metadata, granularidad) y la consulta (reescritura, expansión, transformación) — §3;
   - **post-recuperación**: reordenar, filtrar, comprimir el contexto — §4 y Clase 8.
3. **Modular RAG** — el pipeline deja de ser lineal: módulos intercambiables (búsqueda, memoria, enrutamiento, validación) y patrones de flujo **iterativos** (recuperar varias veces), **recursivos** (refinar la consulta a partir de lo recuperado) y **adaptativos** (decidir si recuperar) — §6.

La lección práctica: **no se agrega una técnica porque existe, sino porque el diagnóstico señaló una etapa que falla.** De ahí que la clase empiece por el diagnóstico.

---

## 2. Framework de diagnóstico por etapa

### 2.1 Los siete puntos de falla

Barnett et al. [2] identifican, a partir de tres sistemas reales, siete puntos donde un RAG falla. Los ordenamos según la etapa del pipeline:

| # | Punto de falla [2] | Etapa | Síntoma típico | Técnica de la clase |
|---|---|---|---|---|
| FP1 | **Contenido faltante**: la respuesta no está en el corpus | Corpus | El modelo inventa o responde "a medias" | Abstención (Clase 6) / ticket (TP) |
| FP2 | **Documentos relevantes fuera del top-k** | Recuperación | Recall bajo | Reescritura, multi-query, híbrida, ajuste de k |
| FP3 | **No entra en el contexto**: recuperado, pero descartado al consolidar | Consolidación | Se perdió al truncar | Compresión, reranking, orden |
| FP4 | **No extraído**: está en el contexto pero el modelo no lo usa | Generación | Respuesta incompleta con evidencia presente | Menos ruido [8], mejor posición [7] |
| FP5 | **Formato incorrecto** | Generación | No respeta la estructura pedida | Structured outputs (Clase 3) |
| FP6 | **Especificidad incorrecta** | Generación | Demasiado general o demasiado detallada | Prompt, step-back [5] |
| FP7 | **Incompleta** | Generación | Responde una parte de una pregunta compuesta | Descomposición de la consulta |

Una observación del paper que vale citar: la robustez de un RAG **evoluciona** con el uso en lugar de diseñarse completamente de antemano, porque muchas fallas solo aparecen con consultas reales. Por eso el laboratorio pide guardar los casos fallidos como **casos de regresión** (§8).

### 2.2 El método: aislar la etapa

El diagnóstico es una aplicación del método científico: **cambiar una variable por vez**. Para un caso que falla:

1. **¿Está la respuesta en el corpus?** (si no → FP1; ninguna técnica de recuperación lo arregla).
2. **¿Está en los chunks recuperados?** Mirar el top-k *antes* de mirar la respuesta (si no → FP2: problema de recuperación).
3. **¿Está en el prompt final?** (si se perdió al truncar o comprimir → FP3).
4. **¿El modelo la usó?** (si estaba y no la usó → FP4–FP7: problema de generación).

Este orden importa: es inútil tocar el prompt de generación si la evidencia nunca llegó.

---

## 3. Optimización de la consulta

### 3.1 La asimetría consulta–documento

Una consulta ("¿cómo comparo dos objetos?") y el chunk que la responde ("La igualdad estricta `===` compara referencias…") viven en regiones distintas del espacio de embeddings: una es corta, interrogativa y en vocabulario del usuario; el otro es largo, declarativo y en vocabulario del autor. Las técnicas de esta sección transforman la consulta para acercarla a donde están los documentos. (En la Clase 4 vimos la otra mitad de la solución: modelos que embeben distinto la consulta y el documento, vía `input_type`.)

### 3.2 Reescritura (Rewrite-Retrieve-Read) [3]

Un LLM reescribe la consulta antes de recuperar: resuelve referencias del diálogo ("¿y eso cómo se usa?" → "¿cómo se usa `Array.prototype.map`?"), corrige errores, quita ruido conversacional. Ma et al. [3] muestran además que el reescritor puede ser un modelo chico entrenado con la señal del resultado final, lo que confirma que *la consulta óptima para el recuperador no es la que escribe el usuario*.

### 3.3 HyDE: buscar con una respuesta hipotética [4]

En vez de embeber la pregunta, se le pide al LLM que escriba un **documento hipotético** que la respondería, y se embebe *ese* documento. El documento puede contener errores factuales, pero tiene la **forma** de un documento del corpus (vocabulario, estilo, longitud), con lo cual cae cerca de los documentos reales. Los errores factuales importan poco porque el embedding comprime el texto en un vector que conserva sobre todo el tema, no los detalles. El costo: una llamada extra al LLM por consulta, y riesgo cuando el modelo desconoce completamente el dominio (el documento hipotético apunta a cualquier lado).

### 3.4 Step-back: abstraer antes de buscar [5]

Para preguntas muy específicas ("¿por qué `typeof null` devuelve `'object'`?"), recuperar primero sobre la pregunta más general ("¿cómo funciona `typeof` y los tipos primitivos en JavaScript?") trae los principios necesarios para responder. Es la transformación opuesta a la reescritura: en lugar de precisar, generaliza.

### 3.5 Multi-query y RAG-Fusion [6]

Se generan $n$ reformulaciones de la consulta, se recupera con cada una y se fusionan los rankings con RRF (Clase 8). La justificación es de **varianza**: cada reformulación cae en una zona algo distinta del espacio; un chunk que aparece en varios rankings es robustamente relevante. Rackauckas [6] reporta respuestas más completas pero también los dos costos que hay que vigilar: **latencia** ($n$ recuperaciones + una llamada de generación de consultas) y **deriva** (reformulaciones que se alejan de la intención original y traen contexto irrelevante).

### 3.6 Mejorar el lado del documento: contextual retrieval [17]

La misma brecha puede atacarse desde el índice: un chunk que dice "Esto devuelve un nuevo array" perdió de qué método habla al cortarlo. Anthropic [17] propone que un LLM genere, para cada chunk, una o dos oraciones de contexto ("Este fragmento pertenece a la documentación de `Array.prototype.map`…") que se anteponen antes de embeber e indexar en BM25. Reportan reducir las fallas de recuperación en el top-20 un 49%, y un 67% combinándolo con reranking. Es una técnica de **ingesta** (Clase 4) que se motiva con un diagnóstico de **recuperación**.

---

## 4. El contexto: más no es mejor

### 4.1 Posición: lost in the middle [7]

Liu et al. [7] colocan el documento con la respuesta en distintas posiciones entre 10, 20 o 30 documentos. El resultado es una **curva en U**: el modelo usa bien la información al principio y al final del contexto, y mal la del medio. En algunos casos, la exactitud con el documento relevante en el medio fue *peor* que sin documentos. Consecuencias de diseño:

- **subir top-k tiene un costo de calidad**, no solo de tokens;
- conviene ubicar los chunks más relevantes en los **extremos** (por ejemplo, ordenar por score y alternar principio/final);
- el reranking (Clase 8) importa no solo para elegir *qué* entra sino *en qué orden*.

### 4.2 Ruido: el modelo se distrae [8]

Shi et al. [8] agregan una oración irrelevante (pero temáticamente cercana) a problemas de matemática y observan caídas grandes de exactitud. En RAG, los chunks recuperados que son "parecidos pero no pertinentes" cumplen exactamente ese papel de distractor. Una de las mitigaciones que evalúan — instruir explícitamente al modelo que puede haber información irrelevante y que debe ignorarla — es barata e implementable en el prompt de la Clase 6.

### 4.3 Redundancia: MMR [9]

Si el top-5 contiene tres versiones casi idénticas del mismo párrafo (frecuente con solapamiento de chunks), desperdiciamos contexto. **Maximal Marginal Relevance** elige iterativamente el siguiente documento $d$ de los candidatos $R$ no seleccionados ($S$ = ya seleccionados):

$$
\text{MMR} = \arg\max_{d \in R \setminus S}\Big[\lambda\,\text{sim}(d, q) - (1-\lambda)\max_{d' \in S}\text{sim}(d, d')\Big]
$$

Con $\lambda = 1$ es el ranking por relevancia puro; al bajar $\lambda$ se penaliza la similitud con lo ya elegido. La deduplicación por umbral del notebook es un caso particular (penalización infinita por encima del umbral).

### 4.4 Compresión [10][11]

Dos familias:

- **Selección/resumen con un modelo** (RECOMP [10]): extraer las oraciones útiles o resumir los chunks en función de la pregunta. Su aporte conceptual es la **aumentación selectiva**: si nada es útil, el compresor devuelve vacío, y el generador responde sin contexto (o, en nuestro caso, se abstiene).
- **Poda de tokens** (LLMLingua [11]): un modelo chico estima qué tokens son predecibles (baja información) y se eliminan, manteniendo el sentido con muchos menos tokens.

El trade-off es siempre el mismo: una llamada (o un modelo) más a cambio de menos tokens y menos ruido en la generación. Se justifica cuando el contexto es largo y ruidoso; con chunks pocos y precisos suele no hacer falta.

---

## 5. Granularidad y recuperación jerárquica

### 5.1 El dilema del tamaño de chunk

Chunks **chicos** dan embeddings precisos (un solo tema por vector) pero poco contexto para generar; chunks **grandes** dan contexto pero embeddings "promediados" de varios temas. La recuperación jerárquica rompe el dilema separando **la unidad que se busca** de **la unidad que se entrega** [1]:

- **Small-to-big / parent document**: se indexan chunks chicos (o incluso oraciones), pero al recuperar uno se entrega su sección o párrafo padre.
- **Resumen → detalle**: se busca primero sobre resúmenes de documentos o secciones y, dentro de los elegidos, sobre chunks.

### 5.2 RAPTOR [12]

RAPTOR generaliza la idea a un árbol de abstracción construido de abajo hacia arriba: los chunks se agrupan por similitud, cada grupo se resume con un LLM, los resúmenes se vuelven a agrupar y resumir, y así hasta la raíz. En consulta, se puede buscar sobre **todos los nodos a la vez** ("árbol colapsado"), de modo que una pregunta puntual encuentra una hoja y una pregunta de síntesis encuentra un resumen. Es la respuesta a FP7 (respuestas incompletas en preguntas que necesitan juntar información dispersa).

---

## 6. Recuperación adaptativa y correctiva

### 6.1 ¿Siempre hay que recuperar?

Naive RAG recupera para toda consulta. Pero "hola" o "reformulá lo anterior en una lista" no necesitan recuperación, y recuperar agrega ruido [8]. **Self-RAG** [13] entrena al modelo para decidir *cuándo* recuperar y para criticar lo recuperado y su propia respuesta mediante tokens especiales. Sin entrenar un modelo, la versión de ingeniería es un **router** (Clase 9) que clasifica la consulta antes de decidir.

### 6.2 Evaluar lo recuperado antes de usarlo

**CRAG** [14] agrega un evaluador de la calidad de la recuperación que dispara acciones distintas según la confianza: usar lo recuperado (refinado), descartarlo y buscar en otra fuente, o combinar. Es exactamente la estructura del flujo del TP:

```
consulta → recuperar → ¿la evidencia alcanza?
                          ├── sí  → generar con citas
                          └── no  → crear_ticket (en vez de inventar)
```

La diferencia es que nosotros implementamos el "evaluador" con un umbral de similitud y/o un juez LLM, y la acción alternativa es escalar a un humano en vez de buscar en la web.

---

## 7. GraphRAG

### 7.1 Grafos de conocimiento [15]

Un **grafo de conocimiento** representa conocimiento como un grafo dirigido y etiquetado: los nodos son entidades (`Promise`, `async function`) y las aristas, relaciones etiquetadas (`async function —devuelve→ Promise`); cada arista es una tripla (sujeto, predicado, objeto) — el modelo de datos de RDF [15]. A diferencia de un índice vectorial, que captura *similitud*, el grafo captura **relaciones explícitas** que se pueden recorrer.

### 7.2 GraphRAG [16]

Edge et al. [16] observan que el RAG vectorial falla en **preguntas globales** sobre el corpus ("¿cuáles son los temas principales de esta documentación?"): ningún chunk individual es similar a esa pregunta, porque la respuesta es una propiedad del corpus entero. Su pipeline:

1. un LLM extrae entidades y relaciones de cada chunk y arma el grafo;
2. se detectan **comunidades** jerárquicas con el algoritmo de **Leiden** [18] (grupos de entidades densamente conectadas ≈ temas);
3. un LLM pre-genera un **resumen por comunidad**;
4. una pregunta global se responde con **map-reduce**: respuesta parcial con cada resumen (map), y síntesis final (reduce).

También habilita **recuperación multi-hop**: partir de las entidades de la consulta y expandir por las aristas para encontrar información conectada que no es similar a la consulta (lo que hace el notebook). El costo es alto (muchas llamadas al LLM en la ingesta) y la extracción de entidades introduce sus propios errores; por eso es contenido complementario: para preguntas puntuales sobre documentación como MDN, el RAG vectorial con híbrida y reranking suele alcanzar.

---

## 8. Casos de prueba: del debugging a la regresión

Cada caso diagnosticado en esta clase debería convertirse en un **caso de prueba** con: la consulta, los chunks que deberían recuperarse, el comportamiento esperado (responder / abstenerse / abrir ticket) y la etapa donde falló. Esto tiene dos funciones:

- **regresión**: al aplicar una técnica para arreglar un caso, verificar que no se rompieron otros (cada técnica de esta clase tiene efectos secundarios: multi-query puede derivar [6], la compresión puede descartar evidencia [10]);
- **evaluación**: estos casos son la semilla del dataset de evaluación de la Clase 8, donde la pregunta pasa de "¿anda este caso?" a "¿cuánto anda el sistema, y la mejora es real?".

---

## 9. Streamlit: el modelo de ejecución (contenido complementario)

Streamlit tiene un modelo de ejecución poco habitual que conviene entender antes de escribir una demo [19]:

- **El script se re-ejecuta completo, de arriba abajo, en cada interacción** del usuario (cada mensaje enviado, cada botón). No hay callbacks ni loop de eventos explícito.
- Por lo tanto, todo lo que debe **persistir entre interacciones de una sesión** (el historial del chat) va en `st.session_state`, que sobrevive a las re-ejecuciones.
- Todo lo que es **caro de crear y compartible entre sesiones** (el cliente del proveedor, la colección de ChromaDB, un modelo cargado) va detrás de `st.cache_resource`, que lo crea una sola vez. `st.cache_data`, en cambio, es para resultados serializables (devuelve copias).

Los dos errores típicos — re-crear el índice en cada mensaje (lento) y guardar el historial en una variable común (se pierde) — salen directamente de no tener presente este modelo.

---

## Preguntas de repaso

1. Un usuario pregunta algo cuya respuesta está en el corpus, pero el sistema responde "no tengo información". Describa, en orden, qué verificaría y qué punto de falla de [2] correspondería a cada resultado.
2. ¿Por qué HyDE funciona aunque el documento hipotético contenga errores factuales? ¿En qué situación esperaría que falle?
3. Según [7], ¿qué riesgo tiene pasar de top-3 a top-15 "para no perder nada"? Proponga dos mitigaciones.
4. Calcule a mano el orden MMR con $\lambda = 0{,}5$ para tres candidatos con sim$(d,q)$ = 0,9; 0,85; 0,6, donde los dos primeros tienen similitud 0,95 entre sí y el tercero 0,2 con ambos.
5. ¿Qué tipo de pregunta motiva GraphRAG y por qué el RAG vectorial no la resuelve? ¿Lo usaría para el corpus del TP?
6. Relacione CRAG [14] con el flujo de tickets del TP: ¿qué cumple el rol del evaluador y qué el de la acción correctiva?
7. En una app Streamlit, ¿qué pasa si crea el cliente de ChromaDB fuera de `st.cache_resource`? ¿Y si guarda el historial en una lista global común?
