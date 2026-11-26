# RGO XIX — Topología, tiempo y versiones musicales

**Sergi Garcia Mecinas · 26 de noviembre de 2026 · estudio exploratorio**

[Introducción](EMPEZAR.md) · [Fase XVIII](rgo_fase18_nota.md) · [Resumen musical](MUSICA.md) · [Auditoría](../audits/rgo_fase19_audit.mjs) · [Resultados completos](../results/rgo_fase19_resultados.json)

## Pregunta

¿Conserva la homología persistente información útil para reconocer melodías cuando cambian la representación y el tiempo? Se toma como antecedente a Victoria Callet-Feltz, que aplica Fourier bidimensional a compases y homología persistente. Aquí se implementa un protocolo distinto: ventanas de tres eventos de clases de altura y métricas invariantes por transposición. No es una reproducción de su algoritmo, ni un rechazo general de la homología persistente.

## 1. Fuentes y tareas

- **JSB Chorales:** 382 corales de Bach (229 train, 76 valid, 77 test); las 382 son referencias de un catálogo. Solo las 77 fuentes del split test generan consultas sintéticas. Tres condiciones: transposición común aleatoria, fragmento consecutivo del 50% y dicho fragmento con probabilidad 0,1 de omitir cada evento y probabilidad 0,2 de alternar una clase de altura en cada evento restante. Se colapsan repeticiones consecutivas. Una realización determinista por pieza y condición. Semillas fijas, distintas de XVIII, por lo que no se comparan porcentajes como si fueran exactamente las mismas consultas.
- **Polifonia/The Session:** CSV publicado con 315 filas de transcripciones y anotación de familias. Se admiten 297, con 51 IDs de melodía y 10 familias. Se descartan 13 por acordes entre corchetes o cabeceras internas y cinco por tonalidad/modo no soportado. El analizador ABC reconoce un subconjunto de la notación, lee la armadura y accidentes explícitos hasta la siguiente barra, omite registro, duraciones, silencios, adornos y desarrollo de repeticiones. No es un parser ABC completo; quedan posibles ambigüedades de interpretación. Las melodías son transcripciones aportadas por participantes, no ondas de audio. Los IDs y familias son metadatos externos, no se usan para extraer características.
- Tres tareas folk: (i) encontrar otra transcripción con el mismo ID excluyendo la propia, solo 288 consultas con al menos otra referencia; (ii) encontrar una transcripción de **otro ID** de la misma familia, 297 consultas, excluyendo todas las del mismo ID; (iii) una sola transcripción por ID (menor ID numérico de setting), 51 consultas, búsqueda de otros IDs de la misma familia. En (iii) se incluye la referencia fuerte de alineación. Los ensayos son dependientes, no se interpretan como 297 observaciones independientes. No se ajustan hiperparámetros con las etiquetas; tampoco se trata de un ensayo confirmatorio con una muestra nueva de familias.
- Métrica top-1: fracción de aciertos en primera posición, crédito esperado bajo empate uniforme; azar = promedio de proporción de referencias pertinentes. Se registra también precisión media esperada con empates en JSON. Reconocer una familia es diferente de recuperar exactamente una composición; una familia puede tener variantes de estructura.

## 2. Representación y homología

Para cada secuencia a, se toman ventanas solapadas de tres eventos y se muestrean determinísticamente hasta 16 de ellas en posiciones equiespaciadas por índice. Cada evento es un indicador cromático de 12 bits. Se prueban dos representaciones:

1. Autocorrelación circular de cada evento en retardos 0 a 6, dividida por 12: distancia euclídea de la concatenación de tres vectores, dividida por raíz de 21. Esta es una pseudométrica espectral porque las magnitudes de Fourier no identifican todos los conjuntos. En una melodía de una nota por evento, todos estos vectores son iguales, de modo que la representación pierde **toda** la identidad de las notas.
2. Distancia de órbitas conjuntas: mínimo de la distancia de Hamming (dividida por 36) entre las dos ventanas sobre las doce transposiciones comunes de una de ellas. Es una métrica en el cociente por transposición de la ventana.
3. A la segunda distancia se añade el tiempo relativo por producto euclídeo, con peso 0,25 y distancia temporal absoluta |i−j|/(N−1), con N el número de ventanas muestreadas. El tiempo significa índice normalizado, no duración real.

Para cada matriz de distancias se calcula el complejo de Vietoris–Rips sobre F₂ en dimensiones 0 y 1, con todas las aristas y triángulos; la reducción de columnas produce los intervalos positivos finitos de persistencia (la componente esencial de H0 se omite). Se verifica H1 de un cuadrado: nacimiento 1, muerte raíz de 2. Se comparan vectores de 16 integrales de Betti normalizadas por dimensión (intervalos equiespaciados en [0,1,1], más duración total normalizada y máxima), por distancia euclídea. Esto es un resumen de diagramas, **no** distancia de Wasserstein/bottleneck ni comparación de diagramas completos. También se comparan histogramas de las mismas distancias, en 16 intervalos. Los empates se contabilizan con crédito fraccionario.

Como referencias temporales se usan histogramas de trigramas de eventos canonizados por una única transposición común, normalización L2 y similitud coseno; y, en el subconjunto de 51 representantes, alineación local dinámica de cromas, maximizando sobre los 12 desplazamientos globales, con similitud de Jaccard, puntuación 2s−1 y penalización 0,5 por hueco. Esta última es una referencia sencilla inspirada en el trabajo de Serrà et al., no una implementación exacta de su sistema ni el estado del arte.

## 3. Resultados (top-1, %)

| Método | Bach: transposición | Bach: fragmento 50% | Bach: fragmento + errores | Folk mismo ID (288) | Folk otro ID, misma familia (297) | Folk un representante (51) |
|---|---:|---:|---:|---:|---:|---:|
| Azar | 0,26 | 0,26 | 0,26 | 3,33 | 7,53 | 9,65 |
| Histograma autocorrelaciones | 22,67 | 0,83 | 0 | 3,33 | 7,53 | 9,65 |
| PH autocorrelaciones | 100 | 2,60 | 0 | 3,33 | 7,53 | 9,65 |
| Histograma órbita conjunta | 100 | 1,30 | 0,65 | 4,50 | 8,50 | 18,95 |
| PH órbita conjunta | 100 | 1,30 | 1,30 | 5,00 | 8,18 | 12,09 |
| Histograma órbita + tiempo | 100 | 0 | 0 | 11,22 | 10,29 | 14,05 |
| PH órbita + tiempo | 100 | 1,30 | 0 | 12,73 | 8,75 | 7,84 |
| Trigramas de órbitas | 100 | 100 | 89,61 | 79,92 | 36,03 | 33,33 |
| Alineación cromática (control) | — | — | — | — | — | 48,04 |

En Bach, **todos** los vectores y firmas de las 77 transposiciones son iguales a los de sus respectivas referencias, dentro de la tolerancia 1e-9. El 22,67% del histograma espectral no contradice invariancia: se debe a empates con otras piezas. En el caso monofónico, las magnitudes locales de eventos singleton son idénticas: por eso sus dos métodos coinciden exactamente con el azar, un contraejemplo constructivo a la suficiencia de esa observación. La topología aplicada a la métrica conjunta aporta alguna capacidad de separación de settings; el tiempo ayuda para el mismo ID, pero no consistentemente para familias nuevas. Los trigramas y la alineación preservan más información secuencial útil en este protocolo. No se comparan aquí costes de cálculo ni se demuestra superioridad de RGO.

## 4. Observabilidad: un resultado que no depende del catálogo

Sea un conjunto de ventanas P=(p₁,…,pₙ), con una métrica que no usa las posiciones temporales. Permutar los vértices conjugando la matriz de distancias por la misma permutación da complejos filtrados isomorfos. La homología persistente no distingue ese cambio de orden. El mapa «secuencia de ventanas → diagrama» factoriza por el multiconjunto métrico no ordenado. Por ello, dos órdenes distintos del mismo conjunto de ventanas pueden ser indistinguibles aunque sus relaciones temporales sean distintas. Esto no implica que todas las permutaciones de una partitura produzcan las mismas ventanas solapadas: el argumento permuta ventanas ya construidas, no notas arbitrarias antes de construir ventanas.

Se permutaron las 77 listas muestreadas de ventanas de Bach: cambió el orden en todas, pero el resumen de PH sin tiempo permaneció idéntico en las 77. Al añadir tiempo relativo, el resumen cambió en las 77; es un resultado empírico, no inyectividad. En particular, la inversión completa de la lista con distancia temporal absoluta sigue siendo una isometría del conjunto aumentado (i → N−1−i). La orientación temporal exige observaciones dirigidas si se desea distinguirla. La homología también puede identificar espacios métricos no isométricos; no hay garantía de reconstrucción de la métrica a partir del diagrama.

Esta distinción es el vínculo con RGO: estabilidad frente a una transformación es deseable solo si esa transformación es irrelevante para el objetivo. Un descriptor puede ser estable, pero perder justo la información que necesitamos. La hipótesis de superioridad de la firma topológica aquí probada no se sostiene; quedan otros usos de la topología y otras representaciones por examinar.

## 5. Límites y siguiente prueba

No se han utilizado grabaciones, así que **no se ha demostrado invariancia frente al instrumento, el timbre, el ruido acústico ni las diferencias de interpretación real en audio**. Tampoco se comparó con los sistemas modernos de reconocimiento de versiones entrenados. El parser y el muestreo limitado pueden reducir el rendimiento. Las decisiones de métricas, tamaño 3, 16 puntos, 16 bins y peso temporal son elecciones del protocolo, no una definición intrínseca de música. No se afirma una ventaja estadísticamente significativa entre porcentajes próximos. La siguiente prueba debe comparar cromas extraídos de grabaciones reales agrupadas por obra (p. ej. Discogs-VI u otro corpus con acceso permitido), separar obras de desarrollo y prueba, controlar duración/timbre/tempo, y comparar bajo el mismo presupuesto con alineación, trigramas y representaciones topológicas más completas.

## 6. Reproducción y fuentes

Node.js 18+ sin dependencias adicionales:

```bash
node audits/rgo_fase19_audit.mjs --data ./rgo_data > phase19_full.json
```

La auditoría descarga los dos archivos originales si faltan y comprueba sus hashes de blob Git. Se ejecutó íntegramente la función de cálculo en JavaScript sobre ambos archivos recuperados mediante GitHub. No se ha repetido la descarga desde el contenedor local. Se conservan las cifras por consulta, las exclusiones y los parámetros en el JSON; no se redistribuyen los corpus.

- JSB Chorales, `czhuang/JSB-Chorales-dataset/jsb-chorales-quarter.json`, blob `ff93746647d1f5af2f719d235329c294267f3088`.
- Polifonia, `polifonia-project/folk_ngram_analysis/FoNN/SIATEC_comparison/data/thesession_subset_metadata_with_tune_family_annotation.csv`, blob `9f172a30b41b48398d6aa0b0e48b40b94bf093dc`. Véanse [documentación del proyecto](https://github.com/polifonia-project/folk_ngram_analysis) y las condiciones de las fuentes.
- Victoria Callet-Feltz (2025), *Persistent Homology and Discrete Fourier Transform: An Application to Topological Musical Data Analysis*, https://doi.org/10.1007/978-3-031-82236-0 ; [artículo DFT y homología persistente](https://victoriacallet.github.io/recherche/articleMCM24.pdf).
- Bergomi, Baraté y Di Fabio (2016), *Towards a Topological Fingerprint of Music*, https://arxiv.org/abs/1602.00739.
- Serrà, Gómez, Herrera y Serra (2008), *Chroma Binary Similarity and Local Alignment Applied to Cover Song Identification*, https://doi.org/10.1109/TASL.2008.924595.
- Araz, Serra y Bogdanov (2024), Discogs-VI, https://doi.org/10.5281/zenodo.13983028 (fuente candidata, no utilizada en esta fase).
