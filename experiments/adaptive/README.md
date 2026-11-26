# Reconstrucción adaptativa implícita

Palabras binarias, espectro completo de k-gramas (k=2,3), extremos conocidos, prior uniforme y consultas sin ruido de coste unitario. Se reconstruye la palabra completa sin enumerar los candidatos durante la inferencia. La enumeración se utiliza solo para verificar casos pequeños. No se optimiza el árbol de decisión completo: cada consulta exacta maximiza la entropía de su respuesta condicionada a las observaciones previas.

## Método

El estado contiene el vértice actual, las multiplicidades de aristas restantes y las paridades de los componentes de consultas XOR aún abiertos. Una consulta posicional fija un bit; una relacional impone una ecuación XOR. Cada componente de estas ecuaciones se fija si contiene una posición conocida; de lo contrario basta un bit libre que se retiene entre su primera y última posición. El conteo de sufijos mediante programación dinámica y los momentos de prefijos agregados dan exactamente las cardinalidades de ambas respuestas de cada consulta. El recuento no etiqueta aristas repetidas. Se emplean enteros arbitrarios. La consulta elegida minimiza |2 N_1 - N|. Cada respuesta restringe la fibra y el algoritmo termina cuando queda un candidato.

Para relaciones de distancia máxima b, a través de cualquier corte cada componente abierto contiene un extremo de una arista de consulta que cruza el corte. Hay como máximo b posiciones posibles en el lado izquierdo y por tanto b componentes abiertos; la memoria de paridad multiplica por como máximo 2^b el espacio de estados base (no una cota del coste total). La restricción b=3 controla ese factor pero reduce las consultas admisibles. La implementación local mantiene los últimos tres momentos de prefijo en lugar de todos.

## Experimentos

Una verdad elegida con semilla fija por cada una de 1.160 clases de 2–32 candidatos, n=8,10,12. Se comprueban todos los conteos posicionales y XOR de las estrategias exactas en cada paso frente a enumeración: 211.570 comparaciones, sin errores. Los 3.480 recorridos completos terminan con la palabra verdadera. Consultas medias: posiciones 2,3147; posiciones+XOR sin límite 2,2534; muestreo 2,2233. Muestreo utiliza 32 muestras exactas de la distribución posterior, generadas con el mismo contador de sufijos, no un algoritmo externo independiente. La selección voraz de máxima entropía inmediata no garantiza mínimo de consultas total. Una verdad por clase no mide el coste esperado exacto del árbol.

22 casos de mayor longitud (8 de n=24, 8 de n=32, 6 de n=48, k=2). Posiciones y muestreo completan los 22; XOR sin límite completa 19, fallando en 3 de 6 casos de n=48 al superar el límite de 100.000 estados por paso. El programa genera results.json con los casos completos y los fallos hasta n=48. La ejecución original se interrumpió en n=64; el script se limita a los grupos guardados.

Segundo ensayo: 18 casos nuevos (6 de n=48,k=2; 6 de n=64,k=2; 6 de n=24,k=3). Todos completan con las tres estrategias comparadas. Mayor fibra inicial: 68.557.426.042.230.000 candidatos. Consultas medias: posiciones 36,1667; XOR local 35,5; muestreo 35,7778. Tiempos medios en esta ejecución: 0,237; 0,514; 0,445 s. Son dependientes del equipo y no un benchmark universal. En n=64: 57; 54,8333; 56 consultas, respectivamente. En n=48: 38,6667; 39,3333; 39. La ventaja no es consistente y el tiempo aumenta respecto a posiciones. La implementación local se verifica además mediante 29.036 comparaciones exactas de conteos sobre estados condicionados de palabras de longitud 10.

## Conclusión

La reconstrucción adaptativa implícita es viable en este modelo. La explosión de estados de las consultas no locales puede limitarse formalmente restringiendo su alcance. No se ha demostrado una ventaja general de consultas ni de coste respecto a las referencias. No se reivindica originalidad de la programación dinámica ni del método de paridades. No se comparan algoritmos bioinformáticos o de reconocimiento acústico. No se ha probado sobre datos reales ni con ruido.

## Reproducción

Python 3 y NumPy (el módulo first_query.py contiene el código de la investigación precedente). Ejecutar desde este directorio:

    OPENBLAS_NUM_THREADS=1 python adaptive.py
    OPENBLAS_NUM_THREADS=1 python local.py
    OPENBLAS_NUM_THREADS=1 python verify_local.py

Los resultados incluyen tiempos medidos y fallos por límite de estados. Los conteos se evalúan exactamente, pero el rendimiento se estima sobre verdades seleccionadas por semilla, no sobre todos los árboles de decisión.
