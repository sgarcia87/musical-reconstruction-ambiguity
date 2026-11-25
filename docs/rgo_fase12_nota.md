# RGO XII — Falsa estabilidad, conocimiento previo y cambio de perspectiva

> **Corrección editorial v0.4 (26/11/2026):** la referencia y las aristas de validación del experimento XII proceden del mismo sistema de anotación. El rechazo observado es circular en gran medida: para los priors incorrectos, «prior rechazado» coincide con «validador coincide con la referencia». Esta fase mide consistencia interna, no capacidad demostrada de detectar conocimiento previo falso en el mundo. Véase [síntesis y correcciones](SEMANTICA.md).

**Cuaderno de investigación · 25 de noviembre de 2026. Piloto exploratorio de consistencia interna, no validación semántica externa.**

## Pregunta

¿Puede una restricción equivocada del espacio de candidatos producir una respuesta aparentemente estable? ¿Aporta información una perspectiva adicional que no participó en la selección inicial? ¿Cuándo fracasa esa auditoría?

La pregunta enlaza la reconstrucción condicionada de RGO con Structural-Coherence-Audit y Semantic Diffraction. Un observador puede reducir su incertidumbre dentro de un modelo sin demostrar que el modelo incluye al estado verdadero. Esta distinción tiene antecedentes en la crítica de modelos, la inferencia bajo mala especificación y la predicción selectiva; no se reivindica originalidad de esos principios generales.

## 1. Datos y protocolo

Fuente: [red_fractal_sample.json](https://github.com/sgarcia87/Semantic-Diffraction-in-Conceptual-Graphs/blob/main/red_fractal_sample.json), Git blob SHA-1 `f5f9c2d2652d3b6bda5e8c1e799631233f2161c1`.

El archivo contiene 42 nodos y 176 aristas dirigidas. Siguiendo el modo estructural, se excluyen 18 aristas `embedding`; quedan 158. Se extraen todos los roles `equilibrio` cuyos dos polos y candidato aparecen en el archivo: 27 referencias, 11 en ejes cuyo nombre no comienza por `eje:descubierta:` y 16 en ejes descubiertos. Esa separación se basa en metadatos, no en una revisión humana externa. El grafo es una muestra pública, no la red completa de IA_m. Las referencias son anotaciones del propio sistema; algunas relaciones pueden ser discutibles. Los casos comparten nodos y aristas, por lo que no se tratan como 27 muestras independientes de una población.

Para cada par A,B y referencia t:

1. Reservar todas las aristas de tipo `equilibrio` que llegan desde cualquier candidato a A o B. No utilizar sus pesos, etiquetas de eje ni el atributo `roles` en el predictor. El resto forma la primera vista; conserva aristas salientes y otras relaciones, incluidas relaciones relacionadas con la anotación.
2. Calcular dos Personalized PageRank, con alfa=0,85, pesos recortados a [0,05,5], reinicio en cada polo y redistribución de nodos sin salidas a ese mismo polo. Convergencia L1 < 10^-12.
3. Ordenar los nodos distintos de ambos polos mediante s(n)=p_A(n)+p_B(n)-0,6|p_A(n)-p_B(n)|. No utilizar filtro de ejes ni exclusión por tipo de nodo. Es una adaptación del núcleo de `audit.py`, no una ejecución completa de todas sus reglas y refinamientos.
4. Construir dos priors de igual tamaño: el correcto contiene t y los cuatro mejores distractores; el incorrecto contiene los cinco mejores distractores. La anotación se usa deliberadamente para construir el control de estrés, nunca para calcular la puntuación. En ambos, seleccionar el mayor s; desempatar por orden de nodos del archivo. Estabilidad: s1>0, cociente s1/s2 >=1,35 y desequilibrio |p_A-p_B|/(p_A+p_B) <=0,80.
5. Abrir la vista reservada. El candidato está doblemente respaldado si existen aristas `equilibrio` de ese candidato hacia ambos polos. Se considera toda la lista de nodos, no solo los admitidos por el prior. Si hay exactamente un candidato con doble respaldo y está fuera del prior, se marca rechazo del prior. Si está dentro pero difiere del ganador, desacuerdo de clasificación; si coincide, corroboración interna. Cero o varios candidatos implican abstención.

El validador es intencionalmente sencillo: recuento de conexiones reservadas, no un nuevo algoritmo de aprendizaje. La vista reservada no es una fuente semántica independiente: contiene redundancia de anotaciones del mismo grafo. En particular, no puede establecer verdad fuera de él. Comparar predicción de aristas inversas sin tener en cuenta esa redundancia produciría una evaluación demasiado optimista.

## 2. Resultados de las consultas individuales

- Prior incorrecto: 18/27 superan los umbrales de estabilidad pese a excluir por construcción la referencia. En los 11 ejes no descubiertos: 4/11. En los 16 descubiertos: 14/16.
- Prior que contiene la referencia: 18/27 estables, cinco de esos 18 seleccionan un candidato distinto de la anotación. Que el prior contenga la referencia no garantiza que el ranking la seleccione.
- Vista reservada: 24/27 tienen un único candidato doblemente respaldado que coincide con la referencia. En dos casos no hay doble respaldo y en uno hay dos candidatos.
- Prior incorrecto + vista reservada: 24 rechazos y 3 abstenciones; se rechazan 17 de los 18 errores aparentemente estables.
- Prior que contiene la referencia + vista reservada: 17 corroboraciones del ganador, 7 desacuerdos de ranking y 3 abstenciones; cero rechazos del prior. En los 11 ejes no descubiertos, 8/11 priors incorrectos son rechazados y tres quedan indeterminados.

Ejemplo calor/frío: la referencia es `tibio`; la primera vista da `temperatura` en primer lugar incluso cuando se admite tibio. Con tibio excluido, el cociente de puntuaciones es 3,247103 y el desequilibrio 0,064194: pasa ambos umbrales. La vista reservada contiene las dos conexiones de tibio a los polos y no ambas para temperatura. El prior incompleto es rechazado. Esto es recuperación de una relación registrada, no un juicio físico sobre temperatura y calor.

## 3. Cambio efectivo de polos para conservar el objetivo

Se agrupan las referencias que aparecen en más de un par de polos: aceleración (4), centro focal (3), espacio (5) y tiempo (7). Para cada grupo se usa un único grafo de primera vista (se reservan todas las aristas `equilibrio` desde candidatos hacia cualquiera de sus polos), un conjunto común de candidatos que excluye todos los polos y un prior válido/incorrecto de cinco candidatos, construido por la media de puntuaciones de las perspectivas. Se calcula la medida original C=1-media(JSD) en base 2 sobre campos pi=(p_A+p_B)/2 de todos los pares distintos de perspectivas. No se recorta el campo antes de calcular C.

| Objetivo anotado | Perspectivas | C | Ganador si se excluye la referencia | Candidatos con máximo respaldo en vista reservada |
|---|---:|---:|---|---|
| aceleración | 4 | 0,442790 | flecha del tiempo (1), espacio (3) | aceleración, 4 pares |
| centro focal | 3 | 0,969042 | espacio (3 de 3) | centro focal, 1 par |
| espacio | 5 | 0,912123 | tiempo (5 de 5) | espacio, 5 pares |
| tiempo | 7 | 0,913207 | espacio (7 de 7) | tiempo, 7 pares |

En el caso centro focal, arriba/abajo, izquierda/derecha y delante/detrás producen el mismo ganador, espacio, incluso si se permite centro focal. La coherencia 0,969 no demuestra identidad con el objetivo. La segunda vista solo ofrece respaldo doble en uno de los tres pares; las otras dos perspectivas no aportan confirmación suficiente de esa anotación. En tiempo, permitir el objetivo produce siete ganadores correctos; excluirlo produce siete ganadores idénticos equivocados, sin alterar C.

C permanece exactamente igual al cambiar solo la máscara de candidatos porque depende de los campos anteriores al ranking. No es un defecto aritmético de JSD; la métrica no fue definida para auditar ese tipo de restricción.

## 4. Comparaciones y resultado negativo

Se comparó el ganador no restringido por prior (excluyendo polos) de difracción con suma PPR, mínimo PPR, peso total de aristas salientes directas de los polos hacia el candidato y grado total. Se repitió tras retirar además TODAS las aristas `equilibrio` desde cualquiera de los dos polos hacia candidatos; no solo las del objetivo. Las etiquetas de roles no se usan como características.

| Método | Aciertos primera vista, 27 | Ejes no descubiertos, 11 | Aciertos con retirada bidireccional, 27 |
|---|---:|---:|---:|
| Difracción | 17 | 3 | 0 |
| Suma PPR | 16 | 2 | 0 |
| Mínimo PPR | 18 | 4 | 0 |
| Peso directo | 10 | 2 | 0 |
| Grado | 5 | 0 | 0 |

Las cifras son top-1 con desempate por orden original del grafo, no una medida de relevancia semántica graduada. No muestran superioridad de la difracción sobre un mínimo PPR sencillo. El fallo tras retirada bidireccional muestra que, en esta muestra y con esta intervención, los métodos dependen fuertemente de relaciones explícitas. La comparación estricta no mide el rendimiento de la implementación completa de IA_m ni supone que los enlaces retirados sean semánticamente irrelevantes. Es un diagnóstico de dependencia. Falta evaluar generalización externa, con un objetivo operacional definido y referencias independientes.

## 5. Qué sucede si también falla la segunda perspectiva

Modelo de omisión: cada arista reservada se elimina independientemente con probabilidad p; las aristas de la primera vista permanecen fijas. No se introducen nuevas aristas. Se calculan las esperanzas exactas, promediando sobre los 27 casos; no se usan muestras Monte Carlo. Un candidato con las dos aristas originales intactas sobrevive con q=(1-p)^2. Si hay k candidatos completos originalmente, la probabilidad de que uno concreto sea el único superviviente es q(1-q)^(k-1). Esto puede convertir un caso originalmente ambiguo en una aparente corroboración única incorrecta.

| p | Rechazo del prior incorrecto | Rechazo erróneo del prior válido | Vista inconcluyente |
|---:|---:|---:|---:|
| 0% | 88,89% | 0% | 11,11% |
| 10% | 72,57% | 0,57% | 26,86% |
| 25% | 50,91% | 0,91% | 48,18% |
| 50% | 22,92% | 0,69% | 76,39% |
| 75% | 5,77% | 0,22% | 94,01% |

Esos porcentajes son consecuencias de un modelo de omisión concreto, no frecuencias de error de un sistema real. Si se comparten errores sistemáticos, la abstención no es suficiente. Para el par calor/frío, se simula sustituir las dos aristas reservadas tibio→polos por temperatura→polos. No se modifica la primera vista. El validador pasa a corroborar temperatura, pese a que el prior sigue excluyendo la referencia original. Es un contraejemplo calculado: no se afirma que esa contaminación haya ocurrido en IA_m.

## 6. Formulación de la observabilidad y la falsabilidad del prior

Sea U el universo de referencia, P un subconjunto admisible, x* el estado objetivo y O una familia de observaciones. Con datos exactos y operadores correctos, la fibra F_U(y) contiene todos los estados compatibles con y. La fibra dentro del modelo es F_P(y)=F_U(y) intersección P.

- F_P vacía: incompatibilidad detectable (si las mediciones y operadores son fiables).
- F_P con un único elemento: unicidad condicionada, no prueba de verdad externa.
- F_U con candidatos tanto dentro como fuera de P: la observación no basta para validar la pertenencia al prior.

Si x* no pertenece a P pero existe x' en P con O(x')=O(x*), ningún procedimiento que utilice únicamente esos resultados puede distinguir el mundo con x* del mundo con x'. Una observación adicional V rompe la equivalencia si V(x') difiere de V(x*). Para falsar todo el prior con datos exactos, debe descartar a TODOS los candidatos restantes, no solo al mejor. En un modelo ruidoso se sustituye la igualdad por regiones de compatibilidad o un modelo de probabilidad calibrado; aquí no se demuestra una garantía universal.

Un ejemplo exacto anterior: los hexacordos A={0,1,3,4,5,8} y B={0,3,4,5,7,8} tienen correlaciones completas de orden 2 y 3 idénticas. Si el prior permite solo B cuando el estado es A, obtendremos una solución única equivocada. El patrón de cuatro notas {0,3,4,8} distingue sus recuentos (1 frente a 2). Cambiar entre observaciones que no separan A y B no puede resolver el error. Este es el principio de separación de fibras que el piloto de grafos intenta operacionalizar, no una identificación literal de PPR con Fourier.

## 7. Interpretación y agenda

Distinguir cuatro indicadores: estabilidad del ranking, compatibilidad del prior, evidencia de validación y cobertura de casos en que se puede decidir. La vista nueva debe aportar evidencia no redundante sobre el objetivo; la diversidad de polos por sí sola no basta. Los resultados del piloto no justifican vender un producto validado ni afirmar una tasa de verdad del 89%.

Próxima prueba: corpus mayor con etiquetas externas y separación de relaciones que se generaron juntas; perturbaciones semánticas definidas por revisión independiente; comparar un rechazo simple por recuento de aristas, PPR, mínimo PPR y método de observación condicionado con el mismo presupuesto. Informar riesgo y cobertura, falsas alarmas y abstenciones, especialmente cuando la evidencia de validación comparte sesgos con la de ajuste. Separar datos de desarrollo de datos de evaluación. Obtener el grafo completo, que no está en el repositorio de ejemplo consultado.

## Reproducibilidad

`python rgo_fase12_audit.py rgo_fase12_graph.json > rgo_fase12_results.json`

El JSON compacto conserva los 42 nombres, las 158 aristas estructurales con pesos/tipos y las 27 referencias extraídas del archivo público; no contiene el resto de los metadatos. También se admite el JSON original como entrada. El archivo original se leyó mediante el conector de GitHub; no se redistribuye el grafo completo de IA_m. Se replicaron las cifras principales en JavaScript sobre el original y en Python sobre la extracción compacta. No se actualizó GitHub durante esta fase.

Referencias de contexto (no revisión de prioridad exhaustiva):
- Gelman, Meng y Stern (1996), *Posterior predictive assessment of model fitness via realized discrepancies* (https://www.cs.columbia.edu/~blei/fogm/2019F/readings/GelmanMengStern1996.pdf).
- El-Yaniv y Wiener (2010), *On the Foundations of Noise-free Selective Classification* (https://jmlr.org/papers/v11/el-yaniv10a.html).
- Toutanova y Chen (2015), *Observed versus latent features for knowledge base and text inference* (https://aclanthology.org/W15-4007/).
- [Structural-Coherence-Audit](https://github.com/sgarcia87/Structural-Coherence-Audit) y [Semantic-Diffraction-in-Conceptual-Graphs](https://github.com/sgarcia87/Semantic-Diffraction-in-Conceptual-Graphs).
