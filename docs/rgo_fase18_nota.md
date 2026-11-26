# RGO XVIII — La huella relacional de la música

**Sergi Garcia Mecinas · 26 de noviembre de 2026 · Cuaderno de investigación.**

## Origen y alcance

Se recupera la pregunta del informe v0.1: si una composición tiene una representación geométrica que permanezca reconocible bajo transformaciones irrelevantes. Esta fase distingue tres problemas: identificación de una pieza dentro de un catálogo; identificación exacta de una secuencia simbólica hasta transposición; adquisición de una representación fiable a partir de audio. Solo se ensayan los dos primeros. No se supone un privilegio musical de Q48 ni se propone una teoría física unificada.

## 1. Datos y protocolo de reconocimiento

Se utiliza el JSB Chorales quarter-note JSON, blob Git `ff93746647d1f5af2f719d235329c294267f3088`. Hay 382 piezas (229 train, 76 valid, 77 test). Todas constituyen el catálogo de referencia; se generan consultas únicamente desde las 77 fuentes del split test. Es búsqueda dentro de un catálogo, no entrenamiento y generalización a obras nuevas. Se produce una versión por condición y pieza (462 consultas). El identificador de la pieza original es la etiqueta de evaluación, no una opinión perceptiva sobre equivalencia musical.

Cada instante se reduce a un conjunto de clases de altura de Z12, descartando registro, voces y multiplicidad. Se colapsan repeticiones consecutivas del mismo conjunto. Se aplica una transposición común entre 1 y 11 semitonos y desplazamientos independientes de −1, 0 o +1 octavas a las notas MIDI. Variar la duración significa repetir cada estado colapsado 1–4 veces y volver a colapsar: la invariancia es exacta por construcción, no valida seguimiento de tempo en grabaciones. En los ensayos con errores se elimina cada estado con probabilidad 0,1 y se cambia un bit cromático con probabilidad 0,2 en cada estado conservado. Los fragmentos son ventanas contiguas de 50% o 25% de la secuencia colapsada, seleccionadas mediante semilla determinista. Las perturbaciones son artificiales.

Se comparan bolsas de autocorrelaciones (magnitudes locales), bolsas de órbitas locales, un descriptor simple de histograma de autosimilitud por retardos, órbitas conjuntas de pares y triples, y relaciones espectrales por pares consecutivos o retardos 1,2,4. Las firmas de pares incluyen las órbitas locales exactas, por lo que **no** se infieren desde las magnitudes de Fourier solamente. Los descriptores de bolsa usan frecuencia logarítmica, IDF calculada sobre el catálogo y coseno. Como referencia más fuerte se emplea una alineación local de conjuntos cromáticos: se escoge un índice global de transposición que maximiza el producto escalar de histogramas cromáticos, se usa Jaccard de conjuntos, recompensa 2J−1, penalización de hueco 0,5 y puntuación máxima dividida por longitud de la consulta. Es un baseline sencillo inspirado en OTI y alineación local, no una reproducción de Serrà et al. ni de Essentia. No se optimizan parámetros con etiquetas. Los empates reciben crédito esperado bajo desempate uniforme. Se registran top-1 y top-5.

| Consulta | Potencia local, top-1 | Pares directos | Fase multirretardo | Pares directos multirretardo | Alineación cromática |
|---|---:|---:|---:|---:|---:|
| Transposición y registro |100%|100%|100%|100%|100%|
| Duraciones repetidas |100%|100%|100%|100%|100%|
| Fragmento 50% |45,45%|100%|100%|100%|100%|
| Alteraciones + eliminaciones |32,47%|100%|100%|100%|100%|
| Fragmento 50% + alteraciones |16,88%|84,42%|90,91%|90,91%|98,70%|
| Fragmento 25% + alteraciones |6,49%|62,34%|75,32%|75,32%|91,56%|

La alineación obtiene 76/77 aciertos para fragmentos de 50% con errores y crédito top-1 equivalente a 70,5/77 para los de 25%. No se demuestra superioridad de RGO. En las dos condiciones difíciles, la mejora de la huella multirretardo respecto a una bolsa de magnitudes está explicada también por la órbita conjunta directa de pares. El descriptor de autosimilitud es deliberadamente sencillo y no representa todas las posibilidades de los métodos de Foote. Las consultas reutilizan las mismas 77 fuentes y no son independientes. El banco es pequeño, homogéneo y contiene originales de cada consulta. Falta replicar en otros estilos, versiones humanas e instrumentos.

## 2. Resultado matemático: observación de pares vs fase

Sea A_i un conjunto de Z_n y p_i el menor desplazamiento positivo que lo preserva. Fijar un representante de cada órbita permite escribir A_i = R_i + s_i, con s_i mod p_i. Sea d_ij el mcm de los órdenes de los caracteres de Fourier no constantes presentes simultáneamente en ambos conjuntos, tal como en la Fase VIII. Las correlaciones cruzadas completas permiten conocer s_j−s_i mod d_ij, y d_ij divide gcd(p_i,p_j).

**Proposición.** La órbita conjunta de un par (A_i,A_j), con la misma transposición aplicada a ambos, determina exactamente la diferencia de los desplazamientos módulo g_ij = gcd(p_i,p_j), dado que se conocen sus órbitas locales.

**Prueba.** Otra configuración con desplazamientos t_i y t_j pertenece a la misma órbita conjunta si y solo si existe una traslación global u tal que u ≡ t_i−s_i mod p_i y u ≡ t_j−s_j mod p_j. El teorema chino del resto generalizado dice que existe tal u si y solo si las dos diferencias son congruentes módulo g_ij. Por tanto la órbita conjunta equivale exactamente a conservar s_j−s_i mod g_ij. QED.

La información de fase cruzada puede ser estrictamente menor. Ejemplo: A={0,1}, B={0,2,4,6,8,10} y B'=B+1. Los conjuntos A y B tienen períodos 12 y 2; el mcm de órdenes de su soporte común es 1. La correlación cruzada de ambos pares es el vector constante de doce unos. Sin embargo, las parejas no son equivalentes por una transposición común, puesto que A no tiene una simetría traslacional no trivial. La órbita conjunta distingue dos posibilidades que la correlación no distingue.

En 18.094 transiciones consecutivas de los estados colapsados del corpus, hay 32 con d_ij < g_ij. No se afirma que sea más barato medir una órbita conjunta que un producto de Fourier; el modelo de observación cambia.

## 3. Extensión de la observabilidad temporal

El criterio previo por componentes conexas de grafos de potencias primas se aplica sin cambio de la prueba al sustituir el módulo d_ij por g_ij para la observación conjunta. Para Z12 se usa un grafo por nivel 2,4,3. Cada componente aporta un dígito libre, descontando el desplazamiento global. La ambigüedad en bits para candidatos equiprobables es (c2−1)_+ + (c4−1)_+ + log2(3)(c3−1)_+.

| Ventana | Secuencias determinadas con Fourier adyacente | Con órbitas conjuntas adyacentes | Conexiones adicionales (Fourier / conjuntas) |
|---|---:|---:|---:|
| Estados colapsados |225/382|225/382|299 / 295|
| 1 negra |225/382|225/382|299 / 295|
| 2 negras |356/382|356/382|41 / 41|
| 4 negras |377/382|378/382|6 / 5|
| 8 negras |370/382|370/382|16 / 16|

La selección de relaciones adicionales maximiza la reducción de log2 del tamaño de la fibra. En todos los casos estudiados recupera la unicidad y alcanza la cota inferior max_l(c_l−1) del número de aristas adicionales (manteniendo todas las aristas consecutivas inicialmente medidas). No se demuestra optimalidad general del algoritmo, ni se contabiliza el coste de cada coeficiente individual. Las relaciones de retardos 1,2,4 sobre estados colapsados bastan también para las 382 secuencias, pero requieren muchas más observaciones. La secuencia reconstruida es únicamente de conjuntos cromáticos; no recupera notas de voces, registro, orden interno de ventanas ni duración original.

## 4. Identidad de catálogo no equivale a identificación universal

Las 382 secuencias originales se distinguen incluso por la secuencia completa de magnitudes locales. Esto no prueba que dichas magnitudes identifiquen una estructura musical desconocida. Se generaron 77 controles con transposiciones independientes de cada estado y 77 con un desplazamiento no trivial de la segunda mitad. Todos preservan las órbitas locales y ninguno es una transposición global de su fuente. Las firmas consecutivas ordenadas de fase y de órbitas conjuntas detectan los 77 controles independientes; en el control de dos bloques cada una detecta 76/77. Una observación local puede no conectar ambas mitades. La adición de conexiones debe estudiarse en función de la ambigüedad, no por simple similitud.

Por otra parte, las bolsas de relaciones pierden información temporal. Dos secuencias de notas individuales 0,1,3 y 0,2,3 tienen las mismas bolsas de intervalos orientados a retardos 1 y 2, pero no son transposiciones globales. Una huella para búsqueda aproximada y una firma completa de identificación cumplen objetivos distintos.

## 5. Qué aporta y qué falta

El resultado conceptual conecta con las fases IX–XVII: la clase de observación, las simetrías y el prior determinan qué información es visible. La evidencia de esta fase no apoya una ventaja empírica de Fourier sobre pares directos ni sobre alineación cromática. La contribución concreta es la comparación exacta de los módulos de observabilidad y la cuantificación de cuándo una medición distinta es necesaria. El siguiente experimento debe usar interpretaciones distintas de una misma obra y piezas distractoras, medir extracción cromática desde audio y comparar con métodos de referencia de reconocimiento de versiones. La invariancia al timbre no está demostrada. Para el origen topológico, queda comparar con descriptores persistentes y Tonnetz sobre el mismo banco, controlando coste, resolución temporal y pérdidas. No se reclama prioridad bibliográfica de la proposición.

## Reproducción

Node.js ≥18, sin dependencias. El programa descarga el corpus original si no se da una ruta y verifica la huella del blob Git. Si la fuente cambia, falla en vez de aceptar silenciosamente otros datos.

```bash
node rgo_fase18_audit.mjs --self-test
node rgo_fase18_audit.mjs jsb-chorales-quarter.json > rgo_fase18_full.json
```

La ejecución completa se realizó en JavaScript directamente sobre el fichero recuperado mediante GitHub. El fichero de resultados incluido es un registro compacto de esa ejecución, no su salida íntegra byte por byte. El script local reproduce el protocolo y ha superado 4096 identidades de período, 10.000 comprobaciones de pares y pruebas sintéticas de ambos experimentos. No se repitió la descarga y ejecución integral localmente por falta de conectividad. No se redistribuye el corpus. No se modificó el repositorio de RGO.

## Referencias

- [Informe RGO v0.1](https://github.com/sgarcia87/relational-geometry-observability/blob/main/docs/INVESTIGACION-v0.1.md), §2: origen musical y antecedentes Foote, Tymoczko, Forte, Lewin, Bergomi, Yust y Callet-Feltz.
- [RGO, observabilidad temporal](https://github.com/sgarcia87/relational-geometry-observability/blob/main/docs/OBSERVABILIDAD_TEMPORAL.md).
- Tymoczko, D. (2006). The Geometry of Musical Chords. https://doi.org/10.1126/science.1126287
- Foote, J. (1999). Visualizing Music and Audio Using Self-Similarity. https://doi.org/10.1145/319463.319472
- Serrà, J., Gómez, E., Herrera, P., Serra, X. (2008). Chroma Binary Similarity and Local Alignment Applied to Cover Song Identification. https://doi.org/10.1109/TASL.2008.924595
- Serrà, J., Serra, X., Andrzejak, R. G. (2009). Cross recurrence quantification for cover song identification. https://doi.org/10.1088/1367-2630/11/9/093017
- JSB Chorales corpus: https://github.com/czhuang/JSB-Chorales-dataset
