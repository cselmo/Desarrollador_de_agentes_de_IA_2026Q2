# Apunte — Clase 8: Evaluación y mejora de RAG

> **Cómo usar este apunte.** Es el marco teórico de la clase: el notebook muestra *cómo* se implementa; este documento explica *por qué* y de dónde sale cada idea. Las referencias entre corchetes remiten a la sección **Fuentes**, que está a continuación y explica qué contiene cada fuente y por qué se usa. 📄 = PDF descargable con `bibliography/descargar.sh` (ver [`bibliography/README.md`](../bibliography/README.md)).
>
> **Lectura obligatoria antes de la clase:** cap. 8 de [1] (§8.1–8.4, gratuito online) y [5] (RAGAS, 8 páginas).
> **Lectura recomendada después:** [7] (MT-Bench, §3 sobre sesgos), [3] (RRF, 2 páginas) y [16].

---

## Fuentes

La evaluación de RAG combina tres tradiciones: (a) la **recuperación de información** clásica, que lleva 60 años midiendo buscadores; (b) la literatura reciente sobre **evaluación automática con LLMs** y sus sesgos; y (c) la **estadística** necesaria para saber si una diferencia medida es real. El apunte usa fuentes primarias de las tres. 📄 = PDF descargable con `bibliography/descargar.sh` (en `bibliography/papers/`).

### Recuperación de información y evaluación clásica

**[1] 📄 Manning, C. D., Raghavan, P. & Schütze, H. (2008). *Introduction to Information Retrieval*. Cambridge University Press.** Online gratuito: https://nlp.stanford.edu/IR-book/ — `2008_manning_introduction-to-information-retrieval.pdf`
- *Qué contiene:* el libro de texto estándar de IR. El cap. 6 desarrolla la ponderación de términos (tf-idf, modelo vectorial); el cap. 8 la evaluación: colecciones de prueba al estilo Cranfield, precision, recall, F, curvas precision-recall, MAP, juicios de relevancia y acuerdo entre evaluadores; el cap. 11 el modelo probabilístico que lleva a BM25.
- *Por qué está:* es la fuente de §1.1 y §2. Las métricas de recuperación que usamos en RAG son las de IR, y este libro las define con rigor y gratis. Lectura obligatoria del cap. 8.

**[2] Järvelin, K. & Kekäläinen, J. (2002). *Cumulated gain-based evaluation of IR techniques*. ACM Transactions on Information Systems, 20(4), 422–446.**
- *Qué contiene:* propone las métricas de ganancia acumulada (CG, DCG y su versión normalizada nDCG), que admiten relevancia graduada y descuentan por posición.
- *Por qué está:* es la fuente primaria de nDCG (§2.2), la métrica principal de los benchmarks actuales de recuperación y embeddings (BEIR, MTEB).

**[3] 📄 Robertson, S. & Zaragoza, H. (2009). *The Probabilistic Relevance Framework: BM25 and Beyond*. Foundations and Trends in Information Retrieval, 3(4), 333–389.** — `2009_robertson_bm25-probabilistic-relevance-framework.pdf`
- *Qué contiene:* monografía de uno de los creadores de BM25 que deriva la función desde el marco probabilístico de relevancia, explica el rol de la saturación de frecuencias ($k_1$) y la normalización por longitud ($b$), y presenta extensiones (BM25F para documentos con campos).
- *Por qué está:* fuente primaria de la fórmula y la interpretación de parámetros de §5.1. Permite entender BM25 como un modelo con justificación, no como "un número mágico".

**[4] 📄 Cormack, G. V., Clarke, C. L. A. & Büttcher, S. (2009). *Reciprocal Rank Fusion outperforms Condorcet and individual Rank Learning Methods*. SIGIR 2009.** — `2009_cormack_reciprocal-rank-fusion.pdf`
- *Qué contiene:* paper corto (2 páginas) que propone RRF, con $k = 60$, y lo compara contra métodos de fusión (Condorcet, CombMNZ) y de learning-to-rank en colecciones TREC y LETOR.
- *Por qué está:* fuente primaria de la fusión que implementamos en la búsqueda híbrida (§5.3). Es corto y legible: lectura recomendada.

### Evaluación de RAG y LLM-as-a-Judge

**[5] 📄 Es, S., James, J., Espinosa-Anke, L. & Schockaert, S. (2023). *RAGAS: Automated Evaluation of Retrieval Augmented Generation*. EACL 2024 (demo). arXiv:2309.15217.** — `2023_es_2309.15217.pdf`
- *Qué contiene:* define métricas sin referencia para RAG — faithfulness (proporción de afirmaciones atómicas sustentadas por el contexto), answer relevance (similitud entre la pregunta y preguntas regeneradas desde la respuesta) y context relevance — y las valida contra juicios humanos (dataset WikiEval).
- *Por qué está:* es el paper detrás de la librería que usamos en vivo; explica qué calcula cada métrica para que no sea una caja negra (§3.2). Lectura obligatoria.

**[6] 📄 Saad-Falcon, J., Khattab, O., Potts, C. & Zaharia, M. (2023). *ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems*. NAACL 2024. arXiv:2311.09476.** — `2023_saad-falcon_2311.09476.pdf`
- *Qué contiene:* genera datos sintéticos, entrena jueces livianos por dimensión (relevancia del contexto, fidelidad, relevancia de la respuesta) y usa un conjunto chico anotado por humanos con *prediction-powered inference* para obtener intervalos de confianza de la métrica.
- *Por qué está:* aporta la idea que falta en RAGAS: el juez es un instrumento con error que puede calibrarse con etiquetas humanas (§3.3). También es fuente de la generación sintética de datasets (§1.3).

**[7] 📄 Zheng, L. et al. (2023). *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*. NeurIPS 2023 (Datasets & Benchmarks). arXiv:2306.05685.** — `2023_zheng_2306.05685.pdf`
- *Qué contiene:* estudia sistemáticamente el uso de LLMs como jueces; mide acuerdo con humanos (más del 80% para el juez fuerte, comparable al acuerdo entre humanos); identifica sesgos de posición, verbosidad y auto-preferencia, y la capacidad de razonamiento limitada; propone mitigaciones (intercambio de posiciones, juicio guiado por referencia).
- *Por qué está:* es la referencia más citada sobre LLM-as-a-Judge y la base de la tabla de sesgos de §4. Lectura recomendada (§3 del paper).

**[8] 📄 Wang, P. et al. (2023). *Large Language Models are not Fair Evaluators*. ACL 2024. arXiv:2305.17926.** — `2023_wang_2305.17926.pdf`
- *Qué contiene:* muestra que el ranking entre dos respuestas puede invertirse con solo cambiar el orden de presentación, y propone calibraciones: Multiple Evidence Calibration (explicación antes del puntaje, múltiples muestras), Balanced Position Calibration (promediar ambos órdenes) y Human-in-the-Loop Calibration.
- *Por qué está:* cuantifica el sesgo de posición y aporta mitigaciones concretas que se pueden implementar en el juez del TP (§4.2).

**[9] 📄 Liu, Y. et al. (2023). *G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment*. EMNLP 2023. arXiv:2303.16634.** — `2023_liu_2303.16634.pdf`
- *Qué contiene:* evaluación con LLM usando pasos de evaluación generados por chain-of-thought y un formulario de criterios, ponderando el puntaje por las probabilidades de los tokens de salida; mejora la correlación con humanos en resumen y diálogo. También advierte que el juez puede preferir textos generados por LLMs.
- *Por qué está:* respalda las buenas prácticas de diseño del prompt del juez (criterios explícitos, razonamiento antes del puntaje) (§4.1).

**[10] 📄 Panickssery, A., Bowman, S. R. & Feng, S. (2024). *LLM Evaluators Recognize and Favor Their Own Generations*. NeurIPS 2024. arXiv:2404.13076.** — `2024_panickssery_2404.13076.pdf`
- *Qué contiene:* muestra que los LLMs pueden reconocer sus propios textos y que esa capacidad de auto-reconocimiento correlaciona linealmente con la auto-preferencia al evaluar.
- *Por qué está:* es la evidencia de por qué el juez debería ser de una familia distinta a la del generador — un riesgo concreto del TP, donde muchos usan el mismo proveedor para ambos (§4.2).

### Recuperación neuronal y reranking

**[11] 📄 Khattab, O. & Zaharia, M. (2020). *ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT*. SIGIR 2020. arXiv:2004.12832.** — `2020_khattab_2004.12832.pdf`
- *Qué contiene:* propone la "interacción tardía": codificar consulta y documento por separado pero conservando un vector por token, y puntuar con la suma de máximos de similitud (MaxSim); logra calidad cercana a un cross-encoder con costo mucho menor.
- *Por qué está:* completa el espectro bi-encoder ↔ cross-encoder con la arquitectura intermedia (§6.1); es la base de muchos recuperadores actuales.

**[12] 📄 Thakur, N. et al. (2021). *BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models*. NeurIPS 2021 (Datasets & Benchmarks). arXiv:2104.08663.** — `2021_thakur_2104.08663.pdf`
- *Qué contiene:* 18 colecciones de recuperación de dominios variados, evaluadas zero-shot con nDCG@10; compara modelos léxicos, densos, de interacción tardía y rerankers, y encuentra que BM25 es un baseline robusto fuera de dominio y que los rerankers generalizan mejor a mayor costo.
- *Por qué está:* es la evidencia empírica de que conviene combinar búsqueda léxica y densa (§5.2) y de que el reranking vale su costo (§6).

**[13] 📄 Nogueira, R. & Cho, K. (2019). *Passage Re-ranking with BERT*. arXiv:1901.04085.** — `2019_nogueira_1901.04085.pdf`
- *Qué contiene:* usa BERT como cross-encoder (consulta y pasaje concatenados → puntaje de relevancia) para reordenar candidatos de BM25 en MS MARCO, con una mejora grande sobre el estado del arte de entonces.
- *Por qué está:* es el paper fundacional del reranking neuronal en cascada que usamos con Cohere Rerank (§6).

**[14] 📄 Barnett, S. et al. (2024). *Seven Failure Points When Engineering a Retrieval Augmented Generation System*. CAIN 2024. arXiv:2401.05856.** — `2024_barnett_2401.05856.pdf`
- *Qué contiene:* experiencia de construir tres sistemas RAG en dominios reales; cataloga siete puntos de falla y lecciones de ingeniería, incluyendo que la validación de un RAG solo es posible en operación.
- *Por qué está:* da una taxonomía de errores con respaldo empírico para el análisis por etapa (§9); se usa también en la Clase 7.

### Estadística para evaluación

**[15] Schenker, N. & Gentleman, J. F. (2001). *On Judging the Significance of Differences by Examining the Overlap Between Confidence Intervals*. The American Statistician, 55(3), 182–186.**
- *Qué contiene:* demuestra que el criterio "los intervalos no se superponen" es demasiado conservador para decidir si dos estimaciones difieren, y cuantifica cuánto.
- *Por qué está:* fundamenta la corrección de §8.3 — un error que estaba en versiones anteriores del notebook y que es muy común en informes técnicos.

**[16] Smucker, M. D., Allan, J. & Carterette, B. (2007). *A Comparison of Statistical Significance Tests for Information Retrieval Evaluation*. CIKM 2007.**
- *Qué contiene:* compara empíricamente tests de significancia (aleatorización, bootstrap, t-test, Wilcoxon, signo) sobre resultados de TREC; los tres primeros concuerdan, los dos últimos no, y recomiendan el test de aleatorización.
- *Por qué está:* es la referencia específica de IR para elegir el test (§8.4). Lectura recomendada para quien quiera profundizar.

**[18] Efron, B. (1979). *Bootstrap Methods: Another Look at the Jackknife*. The Annals of Statistics, 7(1), 1–26.**
- *Qué contiene:* el paper que introduce el bootstrap: estimar la distribución de un estadístico remuestreando los datos con reposición.
- *Por qué está:* fuente primaria del método que implementamos en el notebook (§8.2).

**[19] Efron, B. & Tibshirani, R. J. (1993). *An Introduction to the Bootstrap*. Chapman & Hall/CRC.** — Libro comercial.
- *Qué contiene:* tratamiento de libro de texto del bootstrap: intervalos percentil y BCa, tests de hipótesis por bootstrap y permutación, diseños pareados.
- *Por qué está:* referencia de consulta para los intervalos y el bootstrap pareado (§8.2, §8.4).

**[20] Cohen, J. (1960). *A Coefficient of Agreement for Nominal Scales*. Educational and Psychological Measurement, 20(1), 37–46.**
- *Qué contiene:* define el coeficiente kappa, que corrige el acuerdo observado entre dos evaluadores por el acuerdo esperado por azar.
- *Por qué está:* fuente primaria de la métrica para medir la calidad del juez contra humanos (§4.4).

### Sistemas y metodología

**[17] Dean, J. & Barroso, L. A. (2013). *The Tail at Scale*. Communications of the ACM, 56(2), 74–80.**
- *Qué contiene:* explica por qué en sistemas con muchas llamadas por petición la latencia de cola (p99) domina la experiencia del usuario, y técnicas para mitigarla (hedged requests, entre otras).
- *Por qué está:* justifica reportar percentiles y no promedios de latencia (§7); un pipeline RAG es una cadena de llamadas de ese tipo.

**[21] Strathern, M. (1997). *'Improving ratings': audit in the British University system*. European Review, 5(3), 305–321.**
- *Qué contiene:* análisis crítico de las auditorías universitarias, donde aparece la formulación hoy más citada de la ley de Goodhart ("cuando una medida se vuelve objetivo, deja de ser una buena medida").
- *Por qué está:* da el principio metodológico de §1.2 y §8.5: optimizar contra el propio dataset de evaluación lo degrada como medida.

---

## 1. Por qué evaluar es la parte difícil

### 1.1 El paradigma de Cranfield

La recuperación de información tiene más de 60 años de tradición en evaluación, y casi todo lo que hacemos en RAG la hereda. El **paradigma de Cranfield** (los experimentos de Cleverdon en los años 60) define una *colección de prueba* con tres componentes [1, cap. 8]:

1. un **corpus** de documentos,
2. un conjunto de **consultas** (necesidades de información),
3. **juicios de relevancia**: para cada consulta, qué documentos son relevantes.

Con esos tres elementos fijos, cualquier sistema puede evaluarse de forma **reproducible** y **comparable**. Nuestro `dataset_evaluacion` (pregunta + `chunks_relevantes` + respuesta esperada) es exactamente una colección de Cranfield en miniatura, extendida para evaluar también la generación.

### 1.2 La ley de Goodhart

"Cuando una medida se convierte en objetivo, deja de ser una buena medida" (formulación de Strathern [21] de una observación de Goodhart). En evaluación de sistemas de ML esto tiene una consecuencia concreta: **si iteramos el sistema mirando siempre el mismo dataset de evaluación, terminamos sobreajustándolo a ese dataset**. La mitigación estándar es separar un conjunto de *desarrollo* (sobre el que se itera) de un conjunto de *test* (que se mira poco y al final), igual que en aprendizaje supervisado.

### 1.3 Qué debe tener un buen dataset de evaluación

- **Cobertura del tipo de preguntas reales**: puntuales, de síntesis (varios chunks), comparativas.
- **Casos negativos**: preguntas fuera de dominio, donde la respuesta correcta es *abstenerse* (Clase 6) — y en el TP, abrir un ticket.
- **Casos con más de un chunk relevante**: sin ellos, recall y precision coinciden y no se distinguen (ver §2).
- **Tamaño suficiente para que las diferencias sean detectables** — la sección 8 cuantifica qué significa "suficiente".

Construir este dataset a mano es caro. Tanto RAGAS [5] como ARES [6] proponen **generación sintética**: un LLM lee chunks del corpus y genera preguntas cuya respuesta está en ese chunk (con lo cual el juicio de relevancia viene "gratis"). Es útil para escalar, pero introduce un sesgo: las preguntas sintéticas tienden a reusar el vocabulario del chunk, lo que favorece artificialmente a la búsqueda léxica. Lo razonable es combinar un núcleo de preguntas reales (o escritas por humanos) con un complemento sintético revisado.

---

## 2. Métricas de recuperación

Sea una consulta $q$, el conjunto de documentos relevantes $R$ y la lista ordenada de los $k$ primeros recuperados $L_k = (d_1, \dots, d_k)$.

### 2.1 Métricas de conjunto (no miran el orden dentro del top-k)

$$
\text{Precision@}k = \frac{|L_k \cap R|}{k}
\qquad
\text{Recall@}k = \frac{|L_k \cap R|}{|R|}
\qquad
\text{Hit@}k = \mathbb{1}\big[\,|L_k \cap R| > 0\,\big]
$$

El *hit rate* es el promedio de Hit@k sobre las consultas. Precision y recall están en tensión: subir $k$ sube (o mantiene) el recall y en general baja la precision [1, §8.3]. En RAG, **el recall de recuperación es una cota superior de la calidad de la respuesta**: si la evidencia no llegó al prompt, el modelo solo puede acertar por conocimiento paramétrico (es decir, sin sustento).

### 2.2 Métricas de ranking (sí miran el orden)

**Reciprocal Rank** — el inverso de la posición del primer relevante; su promedio sobre consultas es el **MRR**:

$$
\text{MRR} = \frac{1}{|Q|}\sum_{q\in Q} \frac{1}{\text{rank}_q}
$$

Es adecuada cuando solo importa el primer acierto (por ejemplo, si el prompt usa solo el top-1).

**Average Precision** — promedia la precision en cada posición donde aparece un relevante; su media es **MAP** [1, §8.4]:

$$
\text{AP}(q) = \frac{1}{|R|}\sum_{i=1}^{k} \text{Precision@}i \cdot \mathbb{1}[d_i \in R]
$$

**nDCG** (Järvelin & Kekäläinen [2]) admite **relevancia graduada** $\text{rel}_i \in \{0,1,2,\dots\}$ ("muy relevante", "algo relevante") y descuenta logarítmicamente por posición:

$$
\text{DCG@}k = \sum_{i=1}^{k} \frac{2^{\text{rel}_i}-1}{\log_2(i+1)}
\qquad
\text{nDCG@}k = \frac{\text{DCG@}k}{\text{IDCG@}k}
$$

donde IDCG es el DCG del ranking ideal (normaliza a $[0,1]$). nDCG@10 es la métrica principal de benchmarks modernos como BEIR [12] y MTEB (Clase 4).

### 2.3 Ejemplo resuelto

$R = \{a, b\}$, recuperados $L_3 = (x, a, y)$:
Precision@3 $= 1/3$; Recall@3 $= 1/2$; Hit@3 $= 1$; RR $= 1/2$; AP $= \frac{1}{2}\cdot\frac{1}{2} = 0{,}25$ (solo hay un relevante recuperado, en posición 2, con Precision@2 $= 1/2$); con relevancia binaria, DCG@3 $= \frac{1}{\log_2 3} \approx 0{,}631$, IDCG@3 $= 1 + \frac{1}{\log_2 3} \approx 1{,}631$, nDCG@3 $\approx 0{,}387$.

---

## 3. Métricas de generación

### 3.1 Tres preguntas distintas

Para la respuesta $a$ a la pregunta $q$ con contexto recuperado $c$, la literatura de evaluación de RAG [5][6] separa:

| Dimensión | Pregunta | Depende de |
|---|---|---|
| **Fidelidad** (*faithfulness*, *groundedness*) | ¿Todo lo que afirma $a$ está sustentado por $c$? | $a$, $c$ |
| **Relevancia de la respuesta** | ¿$a$ responde lo que preguntó $q$? | $a$, $q$ |
| **Relevancia del contexto** | ¿$c$ contiene lo necesario y poco más? | $c$, $q$ |

Una respuesta puede ser **fiel pero irrelevante** (cita correctamente algo que no se preguntó) o **relevante pero infiel** (responde lo preguntado con información inventada). Por eso se miden por separado. Notar que ninguna de las tres es "corrección" contra la realidad: un sistema perfectamente fiel a un documento equivocado está *bien* según fidelidad.

### 3.2 Cómo las operacionaliza RAGAS [5]

- **Faithfulness**: un LLM descompone la respuesta en **afirmaciones atómicas**; luego verifica cada una contra el contexto. $F = \frac{\#\text{afirmaciones sustentadas}}{\#\text{afirmaciones totales}}$. La descomposición es lo que la hace más fina que un puntaje holístico como el de nuestro `juzgar()`.
- **Answer relevance**: un LLM genera $n$ preguntas *a partir de la respuesta*; se mide la similitud coseno media entre esos embeddings y el de la pregunta original. Idea: si la respuesta es relevante, debería permitir reconstruir la pregunta.
- **Context relevance**: proporción de oraciones del contexto que son necesarias para responder.

El aporte de RAGAS es que estas métricas son **sin referencia** (*reference-free*): no necesitan una respuesta "de oro" escrita por humanos.

### 3.3 ARES: jueces entrenados con intervalos de confianza [6]

ARES genera datos sintéticos, **entrena jueces livianos** (clasificadores) para cada dimensión, y usa un pequeño conjunto anotado por humanos (del orden de cientos de ejemplos) para corregir el sesgo del juez mediante *prediction-powered inference*, que produce **intervalos de confianza** para la métrica. La lección conceptual es la más importante: **un juez automático es un instrumento de medición con error, y ese error se puede estimar si tenemos algunas etiquetas humanas**.

---

## 4. LLM-as-a-Judge: qué sabemos de sus sesgos

### 4.1 Evidencia de que funciona (con matices)

Zheng et al. [7] (MT-Bench / Chatbot Arena) muestran que un juez fuerte (GPT-4 en su momento) alcanza un acuerdo con humanos **superior al 80%**, comparable al acuerdo entre humanos. G-Eval [9] muestra que pedir al juez razonamiento paso a paso (chain-of-thought) y un formulario de criterios, y ponderar el puntaje por las probabilidades de los tokens, mejora la correlación con juicios humanos.

### 4.2 Los sesgos documentados

| Sesgo | Evidencia | Mitigación |
|---|---|---|
| **Posición**: en comparaciones de a pares, preferir la respuesta presentada primero (o segunda) | [7][8]: el ganador puede cambiar con solo invertir el orden | Evaluar ambos órdenes y promediar ("balanced position calibration" [8]); declarar empate si discrepan |
| **Verbosidad**: preferir respuestas más largas | [7] | Rúbricas que penalicen relleno; normalizar longitud |
| **Auto-preferencia**: un modelo favorece sus propias generaciones | [10]: la auto-preferencia correlaciona con la capacidad del modelo de *reconocer* sus propios textos | Usar como juez un modelo de **otra familia** que el generador |
| **Razonamiento limitado**: el juez falla en preguntas de matemática/lógica que él mismo resolvería mal | [7] | Juicio guiado por referencia (dar la respuesta correcta al juez) |

Wang et al. [8] proponen además **Multiple Evidence Calibration**: pedir al juez que genere la explicación *antes* del puntaje, y muestrear varias veces.

### 4.3 Puntual vs. de a pares

- **Puntual** (*pointwise*): un puntaje absoluto por respuesta (nuestro `juzgar()`). Escalable, pero los puntajes absolutos se calibran mal (el juez puede dar "4/5" a casi todo).
- **De a pares** (*pairwise*): "¿A o B es mejor?". Más discriminativo y más alineado con cómo juzgan los humanos, pero expuesto al sesgo de posición y con costo cuadrático si hay muchos sistemas.

### 4.4 Meta-evaluación: medir al juez

Antes de confiar en un juez, se mide su acuerdo con etiquetas humanas sobre una muestra. El porcentaje de acuerdo es engañoso cuando las clases están desbalanceadas (si el 90% de las respuestas son fieles, un juez que siempre dice "fiel" acuerda el 90%). Por eso se usa el **kappa de Cohen** [20], que descuenta el acuerdo esperado por azar:

$$
\kappa = \frac{p_o - p_e}{1 - p_e}
$$

donde $p_o$ es el acuerdo observado y $p_e$ el acuerdo esperado si ambos evaluadores etiquetaran al azar con sus propias tasas marginales. $\kappa = 1$ es acuerdo perfecto, $\kappa = 0$ es acuerdo de azar. En el ejemplo anterior, el juez trivial tiene $p_o = 0{,}9$ pero $\kappa = 0$.

---

## 5. Búsqueda híbrida: BM25 + densa

### 5.1 BM25 y el marco probabilístico

BM25 nace del **marco probabilístico de relevancia** (Robertson & Spärck Jones, años 70–90), resumido por Robertson & Zaragoza [3]. Para una consulta $q$ con términos $t$ y un documento $D$:

$$
\text{BM25}(D,q) = \sum_{t \in q} \text{IDF}(t)\cdot
\frac{f(t,D)\,(k_1+1)}{f(t,D) + k_1\left(1 - b + b\,\frac{|D|}{\text{avgdl}}\right)}
\qquad
\text{IDF}(t) = \ln\!\left(\frac{N - n_t + 0{,}5}{n_t + 0{,}5} + 1\right)
$$

donde $f(t,D)$ es la frecuencia del término en el documento, $|D|$ su longitud, avgdl la longitud media, $N$ el tamaño del corpus y $n_t$ cuántos documentos contienen $t$. Los dos parámetros tienen interpretación directa:

- $k_1$ (típicamente 1,2–2,0) controla la **saturación**: la décima aparición de un término aporta mucho menos que la primera. Con $k_1 = 0$ solo importa presencia/ausencia.
- $b \in [0,1]$ (típicamente 0,75) controla la **normalización por longitud**: con $b = 1$ un documento el doble de largo necesita el doble de apariciones para el mismo puntaje.

El IDF hace que los términos **raros** pesen mucho — por eso BM25 gana en consultas con identificadores, nombres propios, códigos de error o términos técnicos poco frecuentes, donde un embedding denso tiende a "suavizar" el término hacia vecinos semánticos.

### 5.2 Evidencia: BM25 es un baseline difícil

En BEIR [12], un benchmark de 18 conjuntos de recuperación heterogéneos evaluados *zero-shot* (fuera del dominio de entrenamiento), BM25 resulta un baseline sorprendentemente robusto: muchos modelos densos entrenados en un dominio lo superan en ese dominio pero quedan por debajo fuera de él, mientras que los enfoques de reranking y de interacción tardía generalizan mejor (con mayor costo computacional). Las dos familias cometen errores **distintos**, que es exactamente la condición en que combinarlas ayuda.

### 5.3 Reciprocal Rank Fusion

Los puntajes de BM25 (no acotados) y de similitud coseno (en $[-1,1]$) no son comparables, así que sumarlos requiere normalizaciones frágiles. Cormack, Clarke & Büttcher [4] proponen fusionar **solo con las posiciones**:

$$
\text{RRF}(d) = \sum_{r \in \text{rankings}} \frac{1}{k + \text{rank}_r(d)}
$$

con $k = 60$ en el paper original. La constante $k$ amortigua la ventaja de las primeras posiciones: con $k = 60$, estar 1.º aporta $1/61 \approx 0{,}0164$ y estar 10.º aporta $1/70 \approx 0{,}0143$ — la diferencia es chica, de modo que **un documento bien ubicado en varios rankings le gana a uno primero en un solo ranking**. En su evaluación, RRF superó a métodos de fusión más sofisticados (Condorcet, CombMNZ) y a métodos de *learning to rank*, sin requerir entrenamiento.

---

## 6. Reranking: la cascada recuperar → reordenar

### 6.1 Tres arquitecturas

| Arquitectura | Cómo puntúa $(q,d)$ | Costo por consulta | Calidad |
|---|---|---|---|
| **Bi-encoder** (Clase 4–5) | $\cos(E(q), E(d))$, con $E(d)$ precomputado | Una codificación de $q$ + búsqueda ANN | Base |
| **Late interaction** (ColBERT [11]) | Un vector por token; suma de máximos de similitud token a token (*MaxSim*) | Mayor almacenamiento, búsqueda más cara | Intermedia–alta |
| **Cross-encoder** (monoBERT [13]) | Un transformer lee $q$ y $d$ **juntos** y emite un puntaje | Una pasada del modelo **por cada par** | Alta |

El cross-encoder es más preciso porque la atención (Clase 1) opera *entre* tokens de la consulta y del documento; el bi-encoder comprime cada uno por separado en un solo vector antes de compararlos. Nogueira & Cho [13] mostraron con BERT como cross-encoder una mejora grande sobre el estado del arte de MS MARCO de su momento.

### 6.2 Por qué en cascada

Si el corpus tiene $N$ chunks, un cross-encoder requiere $N$ pasadas por consulta — inviable. La arquitectura estándar es una **cascada**: un recuperador barato (BM25, denso o híbrido) reduce $N$ a $k_{\text{candidatos}}$ (decenas), y el reranker reordena esos candidatos para quedarse con $k_{\text{final}}$. El reranker **no puede recuperar lo que la primera etapa no trajo**: el recall de la primera etapa sigue siendo la cota superior.

---

## 7. Costo y latencia: promedios que mienten

El costo agregado es aditivo y su promedio es informativo. La **latencia no**: los usuarios perciben la *cola* de la distribución. Por eso se reportan percentiles (p50, p95, p99), no la media. Dean & Barroso [17] muestran que en sistemas que hacen varias llamadas por petición la cola domina: si una petición hace 100 llamadas en paralelo y cada una tiene 1% de probabilidad de ser lenta, el 63% de las peticiones ($1 - 0{,}99^{100}$) va a sufrir al menos una llamada lenta. Un pipeline RAG con embedding + búsqueda + rerank + generación (+ juez) es una cadena de dependencias de este tipo.

---

## 8. ¿La mejora es real? Inferencia estadística para evaluación

Esta sección corrige un error frecuente (que estaba en versiones anteriores del notebook).

### 8.1 El problema: la métrica es una variable aleatoria

El hit rate medido sobre $n$ preguntas es una **estimación** del hit rate "verdadero" sobre la distribución de preguntas reales. Para una métrica binaria con tasa $p$, el error estándar es aproximadamente

$$
\text{SE} = \sqrt{\frac{p(1-p)}{n}}
$$

Con $n = 10$ y $p = 0{,}8$: SE $\approx 0{,}126$, y un intervalo al 95% de aproximadamente $\pm 0{,}25$. **Con 10 preguntas, un hit rate de 0,8 es compatible con un valor real entre ~0,55 y ~1.** Para bajar ese margen a $\pm 0{,}05$ hacen falta del orden de 250 preguntas. Esto no es un detalle: define cuánto podemos concluir del laboratorio.

### 8.2 Bootstrap

Efron [18][19] propuso estimar la variabilidad de un estadístico **remuestreando los datos con reposición**: se generan $B$ muestras bootstrap del mismo tamaño $n$, se recalcula el estadístico en cada una, y los percentiles $2{,}5$ y $97{,}5$ de esa distribución forman un **intervalo de confianza percentil** al 95%. Funciona sin suponer normalidad, lo que lo hace adecuado para métricas como MRR o nDCG cuya distribución es incómoda.

### 8.3 El error: comparar intervalos "a ojo"

Calcular el intervalo de cada sistema por separado y concluir "se superponen ⇒ no hay diferencia" es **incorrecto**, por dos razones:

1. **La superposición es un criterio demasiado conservador.** Schenker & Gentleman [15] muestran que dos intervalos al 95% pueden superponerse y la diferencia ser estadísticamente significativa. (Intuición: el error estándar de la diferencia de dos estimaciones independientes es $\sqrt{SE_A^2 + SE_B^2}$, que es *menor* que $SE_A + SE_B$, la distancia que exige el criterio de no-superposición.)
2. **Ignora el diseño pareado.** Los dos sistemas se evalúan sobre **las mismas preguntas**. La variabilidad entre preguntas (hay preguntas fáciles y difíciles) es la fuente principal de varianza, y es **común** a ambos sistemas. Comparar intervalos separados no la cancela; comparar diferencias por pregunta, sí.

### 8.4 Lo correcto: diferencias pareadas

Para cada pregunta $i$ calculamos $d_i = m_B(i) - m_A(i)$ y hacemos inferencia sobre la media de los $d_i$:

- **Bootstrap pareado**: remuestrear *preguntas* con reposición, recalcular $\bar d$, y tomar el intervalo percentil. Si el intervalo **no contiene el 0**, hay evidencia de diferencia.
- **Test de permutación (aleatorización) pareado**: bajo la hipótesis nula "los sistemas son intercambiables", el signo de cada $d_i$ es arbitrario. Se invierten signos al azar muchas veces y se cuenta qué fracción de las permutaciones produce un $|\bar d|$ al menos tan grande como el observado: ese es el p-valor.
- **McNemar** (métricas binarias pareadas): solo usa los casos **discordantes** (acierta A y falla B, o viceversa). Hace explícito algo que se olvida fácilmente: las preguntas donde ambos aciertan o ambos fallan **no aportan información** sobre la diferencia.

Smucker, Allan & Carterette [16] compararon tests de significancia en evaluación de recuperación de información y encontraron que el test de aleatorización, el bootstrap y el t-test pareado concuerdan en gran medida, mientras que el test de Wilcoxon y el test del signo pueden llevar a conclusiones distintas; recomiendan el test de aleatorización.

### 8.5 Comparaciones múltiples

Si probamos 20 variantes del sistema (tamaños de chunk, $k$, umbrales…) y elegimos la mejor sobre el mismo dataset, por azar alguna va a parecer significativamente mejor. Es la ley de Goodhart (§1.2) en forma estadística. Mitigaciones: corrección de Bonferroni (usar umbral $\alpha/m$ con $m$ comparaciones), o — más simple — confirmar la variante elegida sobre un conjunto de test que no se usó para elegirla.

---

## 9. Análisis de errores por etapa

Las métricas agregadas dicen *cuánto* falla el sistema; el análisis por etapa dice *dónde*. La regla práctica:

| Recuperación (¿llegó la evidencia?) | Generación (¿es fiel?) | Diagnóstico |
|---|---|---|
| No | — | Error de **recuperación**: chunking, embeddings, consulta (Clase 7) |
| Sí | No | Error de **generación**: prompt, modelo, contexto con ruido |
| Sí | Sí, pero la respuesta es mala | Error de **dataset** o de **pregunta** (ambigua, mal etiquetada) |

Barnett et al. [14] catalogan siete puntos de falla en sistemas RAG reales (contenido faltante, documento relevante fuera del top-k, fuera del contexto tras la consolidación, no extraído, formato incorrecto, especificidad incorrecta, respuesta incompleta) — es la versión fina de esta tabla y conecta con la Clase 7.

---

## Preguntas de repaso

1. Para $R = \{a,b,c\}$ y $L_5 = (a, x, b, y, z)$, calcule Precision@5, Recall@5, RR, AP y nDCG@5 (relevancia binaria).
2. ¿Por qué un juez con 95% de acuerdo con humanos puede ser inútil? ¿Qué métrica lo detecta?
3. Explique qué hacen $k_1$ y $b$ en BM25. ¿Qué valor de $b$ usaría en un corpus donde todos los chunks tienen la misma longitud?
4. Con RRF y $k = 60$, ¿qué documento queda primero: uno que es 1.º en un ranking y no aparece en el otro, o uno que es 5.º en ambos?
5. Un sistema A tiene hit rate 0,70 [0,45; 0,90] y B tiene 0,85 [0,65; 1,0] sobre las mismas 20 preguntas. ¿Se puede concluir algo de la superposición? ¿Qué calcularía en su lugar?
6. ¿Por qué usar como juez un modelo de la misma familia que el generador es un riesgo, y qué evidencia lo respalda?
