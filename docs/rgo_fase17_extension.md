# RGO XVII · Ampliación — Observabilidad de los órdenes y evidencia de paráfrasis

**Sergi Garcia Mecinas · 26 de noviembre de 2026 · RGO v0.5.1**

[Informe general](INVESTIGACION.md) · [Síntesis semántica XII–XVII](SEMANTICA.md) · [Nota XVII original](rgo_fase17_nota.md) · [Laboratorio ampliado](../demos/rgo_fase17_observador.html)

## Resumen y alcance

La fase XV encontró órdenes de Robinson geométricamente perfectos que contradicen juicios humanos. XVI mostró que la ventaja de una seriación sin anclajes no se transfiere robustamente a otro banco. La nota XVII original y esta ampliación cambian la información observada: estudian la intermediación como una consulta ternaria explícita, su ambigüedad, el coste de reconstrucción, los errores y la fragilidad del conocimiento previo. La ampliación extiende los árboles hasta ocho elementos y contrasta estas ideas con evidencia lingüística de paráfrasis independiente del grafo USF.

Los resultados matemáticos siguientes son exactos para órdenes estrictos finitos y un oráculo ideal. Los resultados lingüísticos son exploratorios y en gran parte negativos. No identifican todavía atributos o sentidos de palabras en un universo abierto.

## 1. Modelo y relación con RGO

Sea X un conjunto de n elementos distintos, una dimensión D fijada y un orden total estricto p sobre X. Para cada terna no ordenada T, q_T(p) devuelve su elemento intermedio. B_D(a,b,c) significa que b ocupa una posición estrictamente entre a y c en la dimensión D; no significa equidistancia ni equilibrio métrico. Un orden y su reverso producen las mismas respuestas, de modo que el universo U tiene n!/2 clases para n >= 2.

Para una lista de observaciones E, con respuestas y, definimos el conjunto compatible F_U(E,y) y, con un prior P contenido en U, F_P = F_U intersección P. El número de candidatos es una medida de ambigüedad combinatoria; log2 de ese número expresa la entropía bajo distribución uniforme, no necesariamente la entropía de un posterior real. Una intermediación está certificada condicionalmente si F no es vacío y todos sus candidatos responden igual. No se certifica nada por unanimidad vacía.

Una consulta dirigida a <_D b aporta información diferente de una asociación simétrica. Si las observaciones dirigidas forman un DAG, sus extensiones lineales son exactamente los órdenes compatibles. Una terna tiene el mismo intermedio en todas las extensiones lineales si y solo si su restricción al orden parcial (cierre transitivo) es una cadena. En efecto, toda extensión lineal de un subconjunto de un poset puede extenderse al poset completo: las restricciones adicionales del subconjunto no crean ciclos, porque cualquier camino previo entre sus elementos ya se refleja en la restricción. Entre los tres elementos, una cadena tiene un único orden, mientras que cualquier incomparabilidad permite un intercambio entre extensiones y al menos dos intermedios posibles. Un ciclo dirigido impide una solución estricta. Esto supone un atributo común, no una mezcla de sentidos.

El problema de satisfacer restricciones de intermediación sin orientación es clásico: Opatrný (1979) demostró NP-completitud. No se reclama una solución polinómica general ni originalidad de la teoría de betweenness. Las enumeraciones siguientes constituyen un estudio exacto de protocolos pequeños.

## 2. Consultas fijas y adaptativas

Cada consulta devuelve uno de tres elementos. Un árbol adaptativo de profundidad m tiene como máximo 3^m hojas, por lo que m >= ceil(log_3(n!/2)). El algoritmo usa todas las ternas disponibles y elige, entre las que separan el conjunto compatible, la de menor rama máxima; desempata por menor suma de |rama| log2 |rama| y luego por el orden lexicográfico de las ternas. Se recorre el árbol completo y se comprueba que todas las hojas tienen un solo candidato.

| n | Órdenes hasta inversión | Consultas fijas mínimas | Peor caso adaptativo mínimo | Media del árbol bajo prior uniforme |
|--:|--:|--:|--:|--:|
| 3 | 3 | 1 | 1 | 1 |
| 4 | 12 | 3 | 3 | 2,5 |
| 5 | 60 | 5 | 4 | 4 |
| 6 | 360 | 7 | 6 | 5,625 |
| 7 | 2.520 | no calculado | 8 | 7,3651 |
| 8 | 20.160 | no calculado | 10 | 9,3813 |

El árbol construido alcanza la cota de hojas en todos estos tamaños. Por ello el mínimo adaptativo en el peor caso es exacto para n=3,...,8. No se afirma optimalidad de la media.

Para listas fijas, dos órdenes generan un conjunto de consultas en las que difieren. Un protocolo separa todos los órdenes si corta cada uno de esos conjuntos; basta conservar los conjuntos de diferencias minimales por inclusión. Además, toda pareja de elementos debe estar cubierta al menos una vez: si no, puede situarse contigua y permutarse sin alterar ninguna consulta. Cada elemento aparece en al menos ceil((n−1)/2) ternas, así que m >= ceil(n ceil((n−1)/2)/3). La auditoría enumera todos los subconjuntos de tamaño inferior al primer testigo desde esa cota y verifica las firmas. Para n=5 rechaza los 210 subconjuntos de cuatro consultas; para n=6 rechaza los 38.760 subconjuntos de seis consultas. Los testigos se guardan en JSON.

Distinto es certificar un orden ya conocido: las n−2 ternas contiguas de ese orden son suficientes. La primera establece una orientación salvo inversión, y las ternas sucesivas comparten dos elementos e imponen la misma orientación. La minimalidad de n−2 se verificó por enumeración para n=3,...,6; no se reivindica aquí una cota inferior general de certificados conocidos.

## 3. Teorema: distancia mínima de las firmas completas

**Proposición.** Para n >= 3, con una lectura de cada una de las C(n,3) ternas, la distancia de Hamming mínima entre firmas de órdenes distintos salvo inversión es exactamente n−2.

**Demostración.** Para dos órdenes p y p', coloreamos cada pareja no ordenada según si su orden relativo se conserva o se invierte. Una terna devuelve el mismo intermedio si y solo si sus tres parejas tienen el mismo color: en ese caso los dos órdenes restringidos a la terna coinciden o son inversos. Si p' no es p ni su inverso, aparecen ambos colores. En el grafo completo existe un vértice incidente a ambos colores (si no, todos los vértices y parejas tendrían un único color). Si a de sus n−1 aristas tienen un color y b el otro, cada selección de una de cada color produce una terna con respuestas distintas. Hay ab >= n−2 ternas distintas. Por otra parte, permutar dos elementos contiguos de un orden cambia exactamente las n−2 ternas que contienen esa pareja. Se alcanza la cota. QED.

Por teoría de códigos, la firma completa detecta hasta n−3 errores arbitrarios y corrige hasta floor((n−3)/2), con el decodificador de mínima distancia. Si cada consulta se repite h veces, la distancia es h(n−2); ello presupone un presupuesto de errores por lectura, no un sesgo sistemático que afecte siempre a las repeticiones.

Más generalmente, con errores acotados e, F_U^e = {p: d_H(q(p),y) <= e}. Si el estado verdadero está en U y el error respeta la cota, la fibra no es vacía. Un prior que excluya al estado verdadero queda refutado para cualquier ruido admisible si todas sus firmas distan más de 2e de la verdadera. La condición es necesaria para una garantía uniforme sobre todos los posibles errores de hasta e: las bolas de Hamming de dos firmas se intersectan cuando su distancia es <= 2e. Sin distancia suficiente una solución única dentro de P puede ser falsa.

Esta proposición prolonga el diseño de observaciones resistentes de XI sobre otro dominio combinatorio. Se incluye una prueba, un censo de firmas y una comprobación por intercambios contiguos; queda pendiente establecer la prioridad bibliográfica específica.

## 4. Experimento exhaustivo con un prior fijo incorrecto

Modelo sintético sin ruido. El prior P impone que el elemento 0 sea un extremo. Se evalúa **cada** orden del universo como verdad, incluido el conjunto excluido por P. El prior está definido antes de las observaciones. El observador elige consultas minimax dentro de P y se detiene cuando queda una solución o ninguna. El validador continúa usando la fibra del universo completo; se detiene al refutar P o certificar unicidad global. Respuestas del oráculo exacto, no etiquetas compartidas de un grafo semántico.

| n | Órdenes excluidos por P | Rechazos iniciales | Unicidades incorrectas | Rechazos tras validar | Consultas extra máximas |
|--:|--:|--:|--:|--:|--:|
| 4 | 6 | 4 | 2 | 6 | 1 |
| 5 | 36 | 24 | 12 | 36 | 1 |
| 6 | 240 | 145 | 95 | 240 | 2 |
| 7 | 1.800 | 960 | 840 | 1.800 | 2 |
| 8 | 15.120 | 7.580 | 7.540 | 15.120 | 2 |

En n=8, 7.540 casos excluidos (49,87%) producen unicidad errónea antes de validar. Con este prior y esta política, se añade una media de 0,6074 consultas sobre todos los 20.160 estados, incluidos los que no necesitan ninguna. Se confirman las 5.040 soluciones verdaderas que estaban en P. No se generaliza el máximo de dos consultas a otros priors, ni se afirma que sea un protocolo óptimo de validación. No es evidencia de capacidad semántica real.

## 5. Evidencia ordinal externa: JJGraph

Cocos et al. (2018) estudiaron intensidades mediante paráfrasis de PPDB, como un adjetivo modificado por un adverbio y un segundo adjetivo. Se usa su JJGraph publicado (3.704 nodos, 36.756 enlaces; 33.394 enlaces válidos no reflexivos del tipo adv+jj->jj, 18.030 parejas dirigidas distintas). La dirección de un enlace es una **hipótesis** de mayor intensidad, no una observación ordinal infalible. Palabras polisémicas, paráfrasis aproximadas y adverbios ambiguos generan errores.

La extracción del grafo no consulta las etiquetas de los bancos. Se fijan tres variantes: todos los enlaces; 21 intensificadores convencionales (lista explícita en el código, 7.354 parejas); al menos dos adverbios distintos de esa lista (1.713 parejas). No se ajusta la lista a las etiquetas, ni se interpreta la presencia de dos adverbios como independencia estadística.

Se dan los miembros de cada escala al algoritmo, no el orden ni los extremos. La referencia de de Melo/Bansal (2013), a través de las semiescalas inglesas del fichero publicado por Garí Soler/Apidianaki, permite probar intensidad orientada. Se conserva todo el vocabulario de referencia, incluso las palabras sin enlace; por ello los denominadores son 353 ternas estrictas en 87 semiescalas y 257 ternas en las 64 semiescalas que quedan al eliminar términos de Wilkinson y exigir al menos tres rangos distintos. El orden humano admite empates; se evalúan solo ternas con tres rangos diferentes. El modelo candidato es estricto y se considera compatible con la referencia si alguna extensión lineal de sus empates pertenece a la fibra.

En escalas bipolares (Wilkinson/Oates), más intensidad no significa necesariamente mayor coordenada firmada del atributo. Por eso no se impone la dirección global de la intensidad; únicamente se usan cadenas de dos enlaces que proponen un solo intermedio para la terna. Se cuentan 180 ternas estrictas (todas las palabras del banco, no únicamente las 106 cubiertas por USF en XV). Los resultados no son directamente comparables con porcentajes sobre subconjuntos cubiertos en XIII–XVI.

### 5.1. Semiescalas: observaciones dirigidas

| Variante | Parejas propuestas dentro de escalas | Acuerdos / desacuerdos / empates humanos | Escalas incompatibles (87) | Referencia excluida (87) | Únicas | Ternas certificadas / correctas (353) |
|---|---:|---:|---:|---:|---:|---:|
| Todos los adverbios | 274 | 118 / 98 / 58 | 39 | 51 | 2 | 3 / 1 |
| Lista de 21 intensificadores | 190 | 85 / 62 / 43 | 22 | 36 | 2 | 2 / 1 |
| Dos adverbios distintos | 93 | 35 / 30 / 28 | 13 | 23 | 0 | 2 / 1 |

De las 190 parejas de la lista principal, 85 de 147 comparaciones estrictas coinciden con la orientación de referencia (57,82%); las 43 restantes de las 190 corresponden a empates de referencia. La relación de intermediación identificada en dos escalas únicas acierta en una y falla en otra. En la semiescala de incomodidad, las relaciones propuestas son painful < uncomfortable < uneasy, pero la referencia ordena uncomfortable < uneasy < painful (el intermedio humano es uneasy). La fibra contiene un único orden y excluye la referencia. No se afirma que una anotación humana única agote todos los contextos posibles.

En el subconjunto sin vocabulario de Wilkinson (64 escalas, 257 ternas), la lista principal produce 97 parejas: 49 acuerdos estrictos, 35 desacuerdos y 13 empates; 13 escalas incompatibles, 22 sin una extensión de la referencia en la fibra; un único orden identificado cuya terna es incorrecta. No se reproduce una ventaja robusta. Con presupuesto absoluto de una violación permitida, la variante principal deja 11 escalas incompatibles y 14 sin la referencia; no certifica ninguna terna de las 353. Reducir falsas certezas tiene un coste de cobertura.

### 5.2. Escalas bipolares: intermediación sin orientación

| Variante | Restricciones ternarias propuestas | Escalas incompatibles | Ternas certificadas / correctas (180) |
|---|---:|---:|---:|
| Todos los adverbios | 33 | 1 | 16 / 12 |
| Lista de 21 intensificadores | 22 | 0 | 50 / 12 |
| Dos adverbios distintos | 11 | 0 | 22 / 6 |

La variante principal certifica condicionalmente 50 ternas, pero solo 12 coinciden con la referencia (24% entre las certificadas). Una geometría compatible con restricciones no necesariamente observa el atributo requerido. Con una violación permitida certifica 12, solo una correcta. Se publican resultados por escala, casos erróneos y presupuesto alternativo. No se elige retrospectivamente el mejor filtro como resultado principal.

### 5.3. Interpretación

La fuente de paráfrasis es independiente de USF y de la construcción original de IA_m, y los bancos de evaluación son anotaciones humanas anteriores. Ello no convierte enlaces léxicos en mediciones exactas ni los ejemplos en muestras independientes. Los métodos de Cocos et al. y de de Melo/Bansal incluyen aprendizaje de patrones, pesos y/o inferencia global; aquí **no se reproduce su modelo completo ni se afirma superarlo**. El experimento evalúa la suficiencia de las restricciones extraídas por reglas simples, no el estado del arte. No hay evaluación confirmatoria de descubrimiento de dimensiones, desambiguación de sentidos o fuentes por atributo.

La siguiente etapa debería obtener comparaciones contextualizadas y calibradas (por ejemplo, datos de pares comparativos con atributo explícito), desarrollar por escalas separadas y reservar un banco nuevo. La solución matemática de XVII puede cuantificar la incertidumbre y seleccionar preguntas; la adquisición de observaciones válidas sigue siendo la dificultad empírica.

## 6. Reproducción

Node.js 18+, sin dependencias externas de código. Las dos auditorías matemáticas no requieren red; la lingüística descarga tres ficheros de terceros o usa copias locales, comprobando los hashes Git.

```bash
node audits/rgo_fase17_math.mjs > /tmp/rgo17_math.json
node audits/rgo_fase17_prior.mjs > /tmp/rgo17_prior.json
node audits/rgo_fase17_semantic.mjs --data ./rgo_data > /tmp/rgo17_semantic.json
```

Resultados registrados: [matemática](../results/rgo_fase17_math.json), [prior](../results/rgo_fase17_prior.json), [semántica](../results/rgo_fase17_semantic.json). Los cálculos se ejecutaron mediante JavaScript sobre los datos recuperados y por enumeración exhaustiva. Los scripts contienen las mismas funciones de cálculo. Las fuentes se identifican mediante repositorio, ruta, rama y blob; no se redistribuyen los corpus. No se ha ejecutado un experimento cuántico nuevo.

## Referencias

- Opatrný, J. (1979). Total Ordering Problem. SIAM Journal on Computing. https://doi.org/10.1137/0208008
- Chor, B. y Sudan, M. (1998). A Geometric Approach to Betweenness. https://doi.org/10.1137/S0895480195296221
- de Melo, G. y Bansal, M. (2013). Good, Great, Excellent: Global Inference of Semantic Intensities. https://aclanthology.org/Q13-1023/
- Cocos, A. et al. (2018). Learning Scalar Adjective Intensity from Paraphrases. https://aclanthology.org/D18-1202/ ; [código y datos](https://github.com/acocos/scalar-adj).
- Wilkinson, B. y Oates, T. (2016). A Gold Standard for Scalar Adjectives. https://aclanthology.org/L16-1424/
- Garí Soler, A. y Apidianaki, M. (2021). Scalar Adjective Identification and Multilingual Ranking. https://aclanthology.org/2021.naacl-main.370/

**Estado:** resultados combinatorios demostrados bajo hipótesis explícitas; experimento semántico exploratorio negativo; originalidad de los resultados particulares pendiente de contraste exhaustivo.
