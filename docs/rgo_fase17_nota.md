# RGO XVII — Observabilidad de órdenes mediante intermediación

**Sergi Garcia Mecinas · RGO v0.5 · 26 de noviembre de 2026**

[Volver al marco general](INVESTIGACION.md) · [Experimentos semánticos](SEMANTICA.md) · [Laboratorio XVII](../demos/rgo_fase17.html)

> **Ampliación posterior (v0.5.1):** se ha completado la prueba de JJGraph, la optimalidad adaptativa hasta n=8 y un segundo ensayo de prior. Véase [la ampliación XVII](rgo_fase17_extension.md). Los pilotos originales y sus resultados se conservan aquí como registro histórico.

## 1. Objeto, hipótesis y observación

Las fases IX–XI estudiaron la recuperación de señales, los priors y las consultas resistentes a errores. XII–XVI pusieron de manifiesto que la asociación no equivale a orden. XVII aísla matemáticamente esa segunda propiedad. No presupone que la semántica real sea un orden lineal.

Sea X un conjunto de n≥3 elementos distintos, de pertenencia conocida a una dimensión D. Una hipótesis es un orden total estricto, identificando un orden con su inverso. El espacio U tiene n!/2 clases. Una consulta q={a,b,c} devuelve **el elemento intermedio** de los tres, no una respuesta binaria a una proposición específica. El oráculo ideal responde sin ruido excepto en el experimento de errores indicado. No proporciona distancias ni extremos, y no puede determinar la orientación absoluta. Si D es desconocida, además hay que inferirla: dos dimensiones con la misma relación de intermediación no son distinguibles con estas consultas.

La relación B_D(a,b,c) es simétrica en los extremos. Dos comparaciones ordinales transitivas, a <_D b <_D c, implican B_D(a,b,c); la mera asociación por parejas no lo implica. Tampoco implica que b sea el punto medio métrico.

Para cada lista Q de consultas, la firma s_Q(pi) contiene los intermedios observados para cada hipótesis pi. La fibra de un resultado y es F_U(y)={pi∈U:s_Q(pi)=y}. Con un prior P⊆U, F_P(y)=F_U(y)∩P. Esta formulación es exactamente el problema de identificación de alternativas empleado en RGO: cambia el objeto y el observador, no la definición de la fibra.

## 2. Resultado general: la firma completa y su distancia mínima

**Proposición.** Las C(n,3) consultas de intermediación identifican cualquier orden estricto salvo inversión. La distancia mínima de Hamming entre firmas de órdenes diferentes es exactamente n−2.

**Identificación.** Fijemos un elemento d. La consulta {d,x,y} devuelve d si y solo si x e y están en lados opuestos de d. Esto determina la partición de los demás elementos en los dos lados (uno puede estar vacío), hasta intercambiarlos. Para dos elementos de un mismo lado, la respuesta indica cuál está más cerca de d en el orden. Ordenando cada lado y eligiendo arbitrariamente cuál es izquierdo, recuperamos el orden completo salvo inversión. En particular, las C(n−1,2) consultas que contienen d bastan, sin que d sea un extremo conocido.

**Cota inferior de distancia.** Si dos órdenes no son iguales ni inversos, alguna terna {a,b,c} difiere. Para cada d fuera de esa terna debe diferir al menos una de {d,a,b}, {d,a,c}, {d,b,c}. Si las tres coincidieran, el argumento anterior sobre cuatro elementos reconstruiría el mismo orden restringido salvo inversión y, por tanto, también coincidiría {a,b,c}. Estas consultas son distintas para cada d. La distancia es al menos 1+(n−3)=n−2.

**Igualdad.** Intercambiar dos elementos adyacentes en cualquier orden cambia exactamente las n−2 consultas que contienen ambos elementos; las demás no cambian. Para n≥3 el orden obtenido no es el inverso. Esto alcanza la cota.

Con todas las consultas, se detectan hasta n−3 sustituciones arbitrarias de respuestas y se corrigen hasta floor((n−3)/2) mediante distancia mínima, siempre que el orden verdadero pertenezca a U. Con e errores y b borrados se exige 2e+b<n−2. Son garantías sobre el código de firmas, no sobre ruido lingüístico correlacionado ni sobre priors que excluyen la verdad.

## 3. Consultas fijas, adaptativas y certificados

Cada consulta tiene tres resultados; la cota de información para un árbol adaptativo de profundidad d es 3^d ≥ n!/2. Para cualquier lista fija con distancia mínima h, cada par de elementos debe aparecer en al menos h consultas (considérese un orden donde sean adyacentes y su intercambio). Como una consulta contiene tres pares, el número de consultas es al menos ceil(h·C(n,2)/3), incluso si se permite repetición. Para los mínimos enumerados a continuación se prohíbe la repetición.

Se enumeraron todos los órdenes canónicos para n=3,…,6 y todas las diferencias de firmas. Para buscar una lista fija, basta golpear cada soporte de diferencias en al menos h posiciones. Los soportes que contienen otro soporte pueden descartarse. Se recorren exhaustivamente todas las listas de tamaño creciente a partir de la cota inferior. Para la adaptación se enumeran todos los cortes realizables de la fibra por una consulta y se busca por profundidad creciente, descartando ramas con más de 3^d candidatos. Se verifican todos los recorridos del árbol resultante. El código no presupone un orden de referencia para elegir las consultas.

| n | Órdenes | Todas las ternas | Distancia completa | Fijo h=1 | Fijo h=2 | Fijo h=3 | Fijo h=4 | Adaptativo, peor caso | Certificado de un orden dado |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 3 | 1 | 1 | 1 | — | — | — | 1 | 1 |
| 4 | 12 | 4 | 2 | 3 | 4 | — | — | 3 | 2 |
| 5 | 60 | 10 | 3 | 5 | 8 | 10 | — | 4 | 3 |
| 6 | 360 | 20 | 4 | 7 | 10 | 16 | 20 | 6 | 4 |

Para n=6, la profundidad media del árbol óptimo exhibido es 5,625 (orden uniforme). No se reclama optimalidad de esa media. Para n=5 y n=6 la adaptación mejora la lista fija universal sin errores. El certificado de un orden dado no es un protocolo de descubrimiento: su selección puede depender del orden que ya se conoce. Para cualquier n, n−2 consultas sobre ternas consecutivas bastan para certificar un orden dado salvo inversión; la minimalidad se comprobó solo para n≤6. No se generalizan los mínimos fijos 1,3,5,7 a tamaños mayores.

Las salidas contienen listas testigo, soportes mínimos, número de listas examinadas, cotas y rutas verificadas. Una [comprobación independiente](../audits/verify_ordinal.py) de los casos n≤6 mediante Python y programación entera obtuvo los mismos mínimos para h=1,2,3 y la misma profundidad adaptativa. La versión JavaScript enumerativa comprueba además h=4 para n=6. La clasificación con corrección de errores utiliza únicamente la distancia de Hamming de las firmas; no confundir el mínimo de 16 consultas distintas con el de la fase XI en música (otro diccionario y repetición permitida).

## 4. Prior equivocado: auditar la fibra, no solo el candidato

Se estresó el observador con un prior artificial: solo admite los órdenes para los que el intermedio de {0,1,2} es 1. Para n=6 hay 120 órdenes admitidos y 240 excluidos. Se utiliza un oráculo ideal que responde según cada uno de los 360 órdenes reales. La selección voraz maximiza la entropía de las respuestas bajo una distribución uniforme de los candidatos todavía admitidos (desempates por mayor equilibrio y posición de la consulta). Se detiene al alcanzar cero o un candidato en P. Simultáneamente se conserva la fibra en U.

| Resultado | Cuenta |
|---|---:|
| Priors válidos identificados correctamente | 120/120 |
| Priors inválidos que producen rechazo con la estrategia restringida | 22/240 |
| Priors inválidos que producen una única respuesta falsa | 218/240 |
| Priors inválidos rechazados tras ampliar la auditoría a U | 240/240 |

La ampliación selecciona consultas de entropía alta en U cuando aún queda un candidato en P, hasta que se excluye ese candidato o se identifica el orden en U. En los casos inválidos: hasta 2 consultas adicionales, media 247/240≈1,029 incluyendo los rechazos iniciales. Los 218 falsos únicos conservan más de un candidato en U. **Control imprescindible:** puesto que el prior es una sola restricción explícita, preguntar directamente por {0,1,2} rechazaría todos los priors inválidos con una consulta. No hay superioridad del observador genérico frente a esa comprobación dirigida. El ensayo aísla el mecanismo de falsa certeza y no estima su frecuencia en lenguaje real.

La conclusión general es condicional: con mediciones correctas, U que contiene al verdadero estado y un diccionario que separa todos los estados, la auditoría puede detectar un prior falso. Si el estado verdadero está fuera de U, incluso U puede dar una respuesta única errónea. Una fibra vacía implica incompatibilidad entre el modelo, las mediciones y el presupuesto de errores, no identifica por sí sola cuál de ellos ha fallado.

## 5. Prueba lingüística independiente: el límite de cobertura

No se usan rangos de Wilkinson y Oates como observaciones. Se exploraron dos fuentes separadas, sin ajustar el extractor a los resultados de referencia:

1. Corpus etiquetado Universal Dependencies English Web Treebank (train/dev/test). Se buscaron globalmente los patrones ADJ + but not / if not / or even / and even / , even / and almost / or perhaps even + ADJ, admitiendo una coma opcional antes del patrón, utilizando lemas y excluyendo comparativos/superlativos marcados. Son indicios de intensidad, no hechos ordinales garantizados: pueden expresar negación, contraste o sentidos distintos. Los 16.622 enunciados y 254.820 tokens contienen solo tres ocurrencias que cumplen el filtro (tres pares distintos; todas con but not); **ninguna conecta dos miembros de una escala de Wilkinson**. Por tanto no hay prueba de precisión ni reconstrucción con esas observaciones, ni se atribuye al corpus general una ausencia de comparaciones; el extractor es deliberadamente estrecho.
2. Las 87 semiescalas de de Melo/Bansal (versión inglesa de la tabla de Garí Soler/Apidianaki) se utilizaron como observaciones ordinales de otra anotación humana. Se extrajeron 344 ternas de palabras distintas con rangos estrictos (las inversiones se identifican), sin consultar los rangos de evaluación. Ninguna de esas ternas aparece íntegramente en una de las 12 escalas completas de Wilkinson. Por tanto **0/180 ternas evaluables observadas y 0 certificadas** en este intento de transferencia directa. No se infirieron cadenas entre sentidos o semiescalas diferentes. No es descubrimiento no supervisado: las etiquetas de un estudio actúan como observaciones, y el otro solo como referencia.

Los ensayos preliminares de WordNet y valencia descritos en la conversación no se incorporan como un benchmark verificado en esta versión: la fuente de valencia no mide necesariamente el atributo; no se dispone aquí de un paquete de reproducción de esos tanteos. El nuevo piloto sí tiene código y procedencia verificable. No se pudo obtener el diccionario completo de observaciones de patrones de de Melo y Bansal ni PPDB/JJGRAPH o DoQ; no se afirma haberlos evaluado.

El resultado negativo es operativo: el observador matemático está implementado, pero su uso semántico necesita una fuente de observaciones ordinales con cobertura suficiente, atributos contextualizados, fiabilidad y anotaciones independientes de evaluación. No hay inferencia de superioridad sobre PPR, métodos de intensidad o embeddings, ni descubrimiento fiable de ejes. Próximo paso: ensayar con una fuente amplia de intensidades o cantidades por atributo, fijar antes los criterios, separar escalas y vocabulario de desarrollo y prueba, permitir empates/abstenciones, y comparar precisión condicionada, cobertura y coste.

## 6. Antecedentes y reproducción

La ordenación con consultas de mediana de tres tiene antecedentes (Horváth y Verhoeff, *Finding the median under IOI condition*, 2002; ordenación por comparaciones ternarias). La identificación por intermediación de grafos y la recuperación de órdenes parciales también tienen literatura propia; aquí el oráculo de tres resultados de un orden total es distinto de una pregunta sí/no sobre caminos de un grafo. No se reclama prioridad sobre la proposición o los mínimos. Para evidencia lingüística: [de Melo y Bansal, 2013](https://aclanthology.org/Q13-1023/) (patrones e inferencia global), [Cocos et al., 2018](https://aclanthology.org/D18-1202/) (paráfrasis), [Garí Soler y Apidianaki, 2020](https://aclanthology.org/2020.emnlp-main.598/), [Elazar et al., 2019](https://aclanthology.org/P19-1388/) (distribuciones de cantidades). El árbol exacto, el código de firmas y el control del prior son la extensión específica estudiada aquí, no una reivindicación de novedad bibliográfica.

```bash
node audits/rgo_fase17_audit.mjs > phase17_full.json
python audits/verify_ordinal.py
node audits/rgo_fase17_evidence.mjs --data ./rgo_data > phase17_evidence.json
```

Node 18+, sin dependencias. La parte matemática se ejecutó íntegramente en JavaScript y se contrastaron sus mínimos principales mediante un procedimiento independiente Python/SciPy. La extracción se ejecutó directamente sobre los tres archivos originales EWT y los dos bancos de escalas; el script usa esa misma función y comprueba las huellas Git al descargar o leer los datos. No se repitió la descarga desde Node local. Los corpus no se redistribuyen. [Resultados exactos](../results/rgo_fase17_resultados.json) · [Resultados del piloto](../results/rgo_fase17_evidence.json).

**Alcance:** las garantías de identificación, distancia y rechazo dependen del objeto y del oráculo especificados. No demuestran una teoría general de la realidad, un significado universal de la tríada ni una ventaja cuántica.
