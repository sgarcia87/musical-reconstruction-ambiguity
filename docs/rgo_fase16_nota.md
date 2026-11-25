# RGO XVI — Replicación en un segundo banco de escalas

**Sergi Garcia Mecinas · 26 de noviembre de 2026 · estudio exploratorio**

## Pregunta

¿Se mantiene la capacidad de inferir relaciones de intermediación ordinal sin extremos conocidos cuando se sustituye la referencia de Wilkinson y Oates por otro banco de anotaciones humanas? Se proporciona la pertenencia de los términos a cada escala (oráculo); no se proporciona orientación, extremos ni rangos al algoritmo. No se estudia descubrimiento de familias en esta fase.

## Datos y método

Se reutiliza el grafo de asociación libre USF (10.617 nodos, 72.176 aristas dirigidas ponderadas FSG; 4.870 términos con perfiles entrante y saliente no nulos). La nueva referencia son las 87 semiescalas inglesas de de Melo y Bansal (2013), tal como aparecen en la tabla `multilingual_data/all_translations.csv` de Garí Soler y Apidianaki (2021), blob `a281181b88078bfd858e77b2eda2cf36eaca94f8`. No es el mismo tipo de escala que el banco de Wilkinson: las semiescalas ordenan intensidad en un solo sentido, no necesariamente polos antónimos.

Los perfiles se normalizan en L2. Para cada semiescala, se ordenan alfabéticamente sus términos cubiertos y se construyen matrices de coseno entrante, saliente y su media. Se comparan PC1 del Gram centrado, eje del diámetro (par de coseno mínimo), segundo autovector del Laplaciano simétrico (Fiedler), la media local de cosenos (el par menos similar se considera extremo) y el grado total como referencia. No se ajustan pesos ni parámetros a las etiquetas. Las ternas con empates en los rangos humanos se excluyen. Se asigna crédito esperado en empates de predicción; espacios propios degenerados o diámetros no únicos se consideran orden indeterminado. La orientación global es irrelevante.

Se evaluaron dos configuraciones: todas las semiescalas y un control que elimina **antes de construir las coordenadas** todas las palabras presentes en la referencia previa de Wilkinson y Oates. Los rangos humanos solo intervienen para evaluar ternas. La pertenencia a las escalas sí es conocida por diseño.

## Resultados

| Método | Todos: 40 ternas (micro) | Sin palabras Wilkinson: 20 ternas (micro) |
|---|---:|---:|
| PC1 entrante | 39,17% | 41,67% |
| Diámetro entrante | 30,00% | 31,67% |
| Fiedler entrante | 32,92% | 40,83% |
| PC1 saliente | 20,83% | 39,17% |
| Diámetro saliente | 25,00% | 40,00% |
| Fiedler saliente | 27,92% | 43,33% |
| Fiedler combinado | 25,83% | 41,67% |
| Coseno combinado local | 35,83% | 46,67% |
| Grado total | 27,50% | 30,00% |
| Azar uniforme | 33,33% | 33,33% |

La cobertura limita la interpretación: 339 apariciones de términos, 172 cubiertas; 353 ternas estrictas posibles y solo 40 cubiertas en 19 semiescalas. Sin las palabras del banco previo: 304 apariciones, 138 cubiertas; 257 ternas posibles, solo 20 cubiertas en 12 semiescalas. Las cifras de términos cuentan apariciones por escala, no palabras únicas.

El método de mayor puntuación en el control de pertenencia de XV (Fiedler combinado, 70/106) no mantiene ese rendimiento: 25,83% micro y 26,75% macro en el segundo banco. PC1 entrante obtiene 39,17% micro, 36,40% macro; el resultado descriptivo no demuestra una ventaja sobre azar. En el subconjunto disjunto, el coseno local obtiene 46,67% micro y 48,61% macro; son solo 20 ternas dependientes, no una validación de superioridad. Los resultados por semiescala y créditos fraccionarios se registran en el JSON.

## Interpretación y siguiente hipótesis

La comparación refuerza la separación entre pertenencia, orientación e intermediación. Una asociación fuerte no mide necesariamente intensidad ordinal. El patrón positivo de XIV dependía de extremos conocidos, vocabulario restringido y una ablación informada por pertenencia. XV y XVI no permiten concluir que una red asociativa baste para recuperar ejes semánticos ordenados en general.

Formalmente, una observación que no distingue permutaciones de tres elementos no identifica cuál es el intermedio. Si el objetivo es un orden estricto de n elementos salvo inversión, hay n!/2 alternativas (n >= 2). Las observaciones ternarias exactas de intermediación pueden separar esas alternativas: el conjunto completo determina los extremos (los únicos elementos que nunca son intermedios) y, elegido uno de ellos, el orden de los demás. Esta es una propiedad combinatoria elemental, no una afirmación de novedad científica. Sin observaciones ordinales genuinamente informativas, la coherencia no sustituye a la identificabilidad.

La prueba siguiente debe utilizar una fuente de relaciones ordinales independiente (por ejemplo, evidencia lingüística comparativa), con separación entre desarrollo y evaluación, medir cobertura y coste y contrastar con baselines de frecuencia y métodos de intensidad conocidos. Esa prueba **no** se ha efectuado en XVI. De Melo y Bansal (2013) y Cocos et al. (2018) ofrecen antecedentes metodológicos. No se ha demostrado ventaja frente al estado del arte ni generalización a IA_m.

## Reproducción

```bash
node audits/rgo_fase16_audit.mjs --data ./rgo_data > phase16_full.json
```

Node.js 18+, sin dependencias. El script descarga o lee los diez archivos de origen y verifica las huellas de blobs Git. Los cálculos de esta fase se ejecutaron en JavaScript sobre los archivos recuperados a través de GitHub; la versión local incorpora la misma función y una comprobación explícita del tamaño del grafo. El contenedor local no tenía acceso a red, por lo que no se repitió el proceso completo desde Node local. No se redistribuyen los corpus.

- [Auditoría](../audits/rgo_fase16_audit.mjs) · [Resultados](../results/rgo_fase16_resultados.json).
- De Melo y Bansal (2013), *Good, Great, Excellent: Global Inference of Semantic Intensities*. https://aclanthology.org/Q13-1023/
- Garí Soler y Apidianaki (2021), *Scalar Adjective Identification and Multilingual Ranking*. https://aclanthology.org/2021.naacl-main.370/
- Datos: https://github.com/ainagari/scalar_adjs/tree/master/multilingual_data
- Nelson, McEvoy y Schreiber (2004), *The University of South Florida Free Association, Rhyme, and Word Fragment Norms*. https://doi.org/10.3758/BF03195588
- Cocos et al. (2018), *Learning Scalar Adjective Intensity from Paraphrases*. https://aclanthology.org/D18-1202/
