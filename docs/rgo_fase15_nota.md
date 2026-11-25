# RGO XV — Emergencia de ejes semánticos sin anclajes

**Cuaderno de investigación · Sergi Garcia Mecinas · Fase exploratoria (26/11/2026)**

## Pregunta y protocolo

¿Pueden emerger tanto la pertenencia a una dimensión como la posición ordinal a partir de una red asociativa humana, sin anotaciones de IA_m ni extremos de escala conocidos? Se distinguen dos tareas: (1) descubrimiento global de familias; (2) identificación del término intermedio dentro de una terna, sin imponer orientación absoluta. Una secuencia y su inversa son equivalentes para la segunda tarea.

Datos: las normas USF (Nelson, McEvoy y Schreiber, 2004), espejo `teonbrooks/free_association/src/Cue_Target_Pairs.*.html`, 10.617 palabras, 72.176 aristas dirigidas con peso FSG. La referencia externa es `Coral-Lab/scales/ordering/ordering_gold_standard.csv`, blob `dc5ecb8805270be3fd135a2c1ff926b03926078d` (Wilkinson y Oates, 2016). Se preserva la procedencia en el JSON y el código verifica las huellas de los ocho archivos USF. Se admiten las 4.870 palabras con al menos una arista entrante y otra saliente, entre ellas 52 términos de las 12 escalas evaluadas. Hay 96 parejas positivas de 1.326 parejas evaluadas y 106 ternas de una misma escala. El orden se toma del ranking humano; no se supone una escala métrica de intensidad. El conjunto de evaluación no permite etiquetar semánticamente todos los demás términos.

## 1. Descubrimiento sin pertenencia ni extremos conocidos

Para cada palabra construimos dos perfiles L2-normalizados: las filas y las columnas de la matriz ponderada de asociación. Calculamos el coseno entre perfiles de un mismo tipo. Para cada k = 5, 10, 20, se construye un grafo de vecinos recíprocos (solo similitudes positivas), ponderado por el coseno medio, con todos los 4.870 candidatos. Se usa una optimización local de modularidad ponderada, de un solo nivel, resolución 1; inicio en singletones, barrido léxico determinista, empates por índice y tolerancia numérica. No se impone el número de grupos y no se eliminan aristas empleando las etiquetas externas. k es un análisis de sensibilidad, no una elección validada en un conjunto de prueba nuevo.

Dentro de cada comunidad ordenamos todos sus términos, no solo los de la referencia, por (i) PC1 de los perfiles normalizados (Gram centrado; iteración de potencia determinista) y (ii) proyección sobre el segmento entre los dos perfiles más distantes (coseno mínimo). La orientación absoluta no es identificable por estos procedimientos: se evalúa la pertenencia al intervalo ordinal con ternas, invariante ante invertir el orden. La referencia solo se utiliza para identificar parejas y ternas que se deben evaluar, nunca para calcular las particiones ni las coordenadas. En la ejecución se calcularon coordenadas solo para las comunidades relevantes para la evaluación (todos los miembros intervienen).

| Perfil | k | Comunidades | Parejas predichas / correctas (entre términos anotados) | Ternas reunidas | Ternas correctas PC1 | Diámetro |
|---|---:|---:|---:|---:|---:|---:|
| Entrante | 5 | 1231 | 44 / 44 | 28 | 9 | 8 |
| Entrante | 10 | 953 | 44 / 44 | 28 | 11 | 8 |
| Entrante | 20 | 797 | 50 / 50 | 33 | 19 | 12⅓ |
| Saliente | 5 | 1794 | 32 / 32 | 12 | 4 | 5 |
| Saliente | 10 | 989 | 48 / 46 | 21 | 10 | 9 |
| Saliente | 20 | 576 | 63 / 58 | 39 | 15 | 11 |

El total de parejas positivas es 96; el de ternas 106. Si las tres palabras están en grupos distintos, o no todas en el mismo grupo, la terna cuenta como no recuperada para la tarea conjunta. En la evaluación de orden se asigna crédito esperado 1/2 ante empate de dos posiciones y 1/3 ante empate de tres (tolerancia 1e-10). El azar de un orden uniforme acierta el término medio con probabilidad 1/3. Por ello la comparación condicional debe separarse de la cobertura. En k=20 entrante, 19/33 es 57,58% condicional, pero solo 19/106 = 17,92% de recuperación conjunta. La pureza de parejas 50/50 es **solo entre las 52 palabras anotadas**, no pureza de las 797 comunidades del vocabulario. En saliente k=20 la cobertura de parejas es 58/96 = 60,42% y la precisión 58/63 = 92,06%. La asignación aleatoria de etiquetas preservando tamaños esperaría 50·96/1326 ≈ 3,62 coincidencias para la configuración entrante k=20; es un valor esperado descriptivo, no una prueba estadística.

El coseno solo, sin agrupar, tiene AUC 0,97475 (entrante) y 0,96189 (saliente) para distinguir parejas de la misma escala frente a parejas de distintas escalas dentro de los 52 términos. Es una medida de pertenencia, no de orden ni de clasificación de palabras fuera del banco. Una escala puede tener muchos pares cercanos aunque sus extremos también estén muy relacionados.

Ejemplo positivo: en k=20 entrante, la comunidad de seis miembros contiene `canyon, huge, large, big, small, tiny` en orden PC1; las cinco palabras anotadas de tamaño aparecen correctamente ordenadas salvo inversión. No se evalúa `canyon` como miembro válido o inválido del eje. Ejemplo negativo: `cold`, `warm`, `hot` no aparecen los tres en una misma comunidad; la comunidad que contiene `cold` incluye palabras de hielo y congelación, lo que demuestra proximidad temática, no un eje térmico completo.

## 2. Control de pertenencia conocida: aislar el problema ordinal

En este control se proporcionan únicamente los miembros de cada escala (oráculo de pertenencia), no sus extremos ni sus posiciones. Se evalúa el mismo conjunto de 106 ternas con cuatro métodos: PC1; eje del diámetro; seriación espectral por el segundo autovector del Laplaciano de similitudes (Fiedler); minimización exhaustiva de un coste de Robinson. Para Fiedler y Robinson se prueba además la media 50/50 de los cosenos entrante y saliente, sin ajustar pesos.

Si S es una matriz de similitud, una hipótesis usual de seriación es que los extremos de cualquier terna ordenada sean menos similares que los pares que contienen al medio. Definimos la pérdida

`L(pi) = sum_{i<j<k} ([S(pi_i,pi_k)-S(pi_i,pi_j)]_+ + [S(pi_i,pi_k)-S(pi_j,pi_k)]_+)`.

Se recorren todas las permutaciones, identificando cada orden con su inverso, hasta 8!/2 = 20.160 por escala. Se usa tolerancia 1e-10 para igualdad del coste. Los minimizadores son únicos hasta inversión en las 36 combinaciones escala/perfil estudiadas. El orden humano no influye en la elección; se usa al evaluar los minimizadores. Fiedler usa una matriz simétrica con diagonal del Laplaciano igual a la suma de pesos fuera de diagonal y entradas fuera de diagonal -S. El signo del vector es arbitrario.

| Método | Entrante (ternas correctas / 106) | Saliente | Media de cosenos |
|---|---:|---:|---:|
| PC1 | 53 | 35 | — |
| Diámetro | 45 | 24 | — |
| Fiedler | 46 | 42 | 70 |
| Óptimo Robinson | 52 | 38 | 51 |

La referencia aleatoria es 35⅓/106 en esperanza. El mejor resultado micro del control es 70/106, pero 50 de esas 70 ternas correctas son de la escala de valoración, que aporta 56 de las 106 ternas. Excluyéndola quedan 20/50 = 40%; la media por escala de Fiedler combinado es 52,86%. No hay ajuste de hiperparámetros sobre la referencia, pero la comparación es exploratoria y reutiliza el banco anterior. No se han obtenido intervalos de confianza ni validación en un segundo banco independiente.

El orden humano satisface la desigualdad de Robinson débil para 48/106 ternas entrantes, 45/106 salientes y 60/106 combinadas. Entre las 12 escalas, el orden humano es un minimizador global para solo 1, 2 y 2 respectivamente. No es un fallo de convergencia del optimizador: se agotó el espacio de permutaciones bajo esta función de coste. Esto rechaza la hipótesis de que la similitud coseno sea universalmente monótona con la proximidad ordinal humana; no prueba que sea imposible extraer orden de las asociaciones con otros modelos.

## 3. Cambio de perspectiva y falsos óptimos

La escala de velocidad ofrece un contraejemplo exacto en el modelo: la referencia es `slow < quick < fast`. El mínimo de Robinson de la vista entrante es `slow < fast < quick`, con pérdida 0. El de la vista saliente es `slow < quick < fast`, también con pérdida 0. Dos óptimos geométricamente impecables no representan la misma relación de intermediación. Su coste solo certifica la compatibilidad con la matriz de similitud empleada.

En cantidad, el orden humano `few, some, several, many` tiene pérdida entrante 1,3823080886861647. El orden `few, several, many, some` tiene pérdida 0 y solo acierta una de las cuatro ternas. La hipótesis geométrica es insuficiente para la tarea, incluso con un óptimo único.

En los minimizadores exactos entrante/saliente, ambas perspectivas seleccionan el mismo elemento medio en 29/106 ternas: 16 acuerdos correctos y 13 acuerdos incorrectos. Con Fiedler son 25 coincidencias, de las cuales 16 correctas y 9 incorrectas. Los dos perfiles proceden del mismo conjunto de datos; no son fuentes estadísticamente independientes. El acuerdo no equivale a verdad. Tampoco la discrepancia informa por sí sola de cuál es la perspectiva válida.

## 4. Consecuencias para RGO

Una comunidad asociativa proporciona una hipótesis de dimensión; no una escala ordenada. La relación ternaria B(a,b,c) expresa que b está entre a y c. A diferencia del orden orientado, B no cambia al invertir todos los signos. Es un objetivo adecuado cuando no se dispone de anclajes, pero no basta con un orden lineal de máxima coherencia geométrica para identificar B. Un grafo con tres perfiles equisimilares es un ejemplo elemental de no identificabilidad: las tres elecciones de medio son compatibles con la observación simétrica. Este contraejemplo no impide que ciertas matrices permitan identificarlo.

La dirección siguiente sería introducir observaciones ordinales de origen distinto — patrones lingüísticos comparativos, gradación explícita, o medidas externas — sin incluir la escala de evaluación en la fuente de entrenamiento, y comprobar recuperación de pertenencia y ternas en un banco nuevo. La literatura de intensidad léxica y seriación ya utiliza varios de estos recursos. El interés particular de RGO es distinguir entre ajuste interno, ambigüedad residual, validez externa y coste de observaciones adicionales. No se afirma originalidad científica del agrupamiento, PCA, Fiedler ni del coste de Robinson. La utilidad específica de RGO sigue por demostrar.

## 5. Reproducibilidad y limitaciones

Los cálculos completos sobre los archivos originales se ejecutaron en JavaScript mediante el conector GitHub. El archivo `rgo_fase15_audit.mjs` reúne los procedimientos ejecutados en una versión local reproducible (Node.js 18+; sin dependencias). Se ha comprobado su sintaxis y ejecutado `--self-test` con ejemplos sintéticos, pero no se pudo repetir la descarga completa en el contenedor local por falta de acceso a red. `rgo_fase15_resultados.json` es una transcripción compacta de las salidas observadas; el recuento de acuerdos y los resultados de los órdenes exactos se volvieron a comprobar localmente sobre las permutaciones registradas. No se redistribuyen los corpus originales.

```bash
node rgo_fase15_audit.mjs --self-test
node rgo_fase15_audit.mjs --data ./rgo_data > phase15_full.json
```

Este resultado no es una generalización sobre todas las palabras, todos los atributos o la cognición humana. Las 106 ternas comparten términos y no son observaciones independientes. El corpus USF y los juicios de 2016 proceden de investigaciones distintas, pero se reutiliza el mismo banco de escalas que en las fases XIII-XIV. La v0.3 de GitHub no se ha modificado en esta fase.

## Referencias

- Nelson, McEvoy y Schreiber (2004). *The University of South Florida Free Association, Rhyme, and Word Fragment Norms*. https://doi.org/10.3758/BF03195588
- Wilkinson y Oates (2016). *A Gold Standard for Scalar Adjectives*. https://aclanthology.org/L16-1424/
- Atkins, Boman y Hendrickson (1998). *A Spectral Algorithm for Seriation and the Consecutive Ones Problem*. https://doi.org/10.1137/S0097539795285771
- de Melo y Bansal (2013). *Good, Great, Excellent: Global Inference of Semantic Intensities*. https://aclanthology.org/Q13-1023/
- Garí Soler y Apidianaki (2020). *BERT Knows Punta Cana is not just beautiful, it's gorgeous: Ranking Scalar Adjectives with Contextualised Representations*. https://aclanthology.org/2020.emnlp-main.598/
