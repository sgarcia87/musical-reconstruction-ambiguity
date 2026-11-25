# Ambigüedad espectral y reconstrucción condicionada

**RGO v0.3 · Nota de síntesis técnica (fases IX–XI)**

Este documento formula el problema común a la recuperación de fase, los conjuntos homométricos y la identificación bajo simetrías. Para una introducción sin conocimientos previos, véase [INVESTIGACION.md](INVESTIGACION.md). Para las demostraciones completas de los casos y los protocolos, véanse las notas [X](rgo_fase10_nota.md) y [XI](rgo_fase11_nota.md).

## 1. Grupo de ambigüedad de fase

Sea $G$ un grupo abeliano finito, $\widehat G$ su dual y $f:G\to\mathbb R$. Se conocen las magnitudes de Fourier, el coeficiente DC si existe y una colección de monomios invariantes no nulos. Sea $S$ el soporte, simétrico bajo inversión, y $H=\langle S\rangle\le\widehat G$.

Para una señal competidora con las mismas magnitudes, cada frecuencia de $S$ posee un cociente de fases $u_s\in U(1)$. La realidad impone $u_{-s}=u_s^{-1}$; si $0\in S$ y se conoce DC, $u_0=1$. Igualar los monomios observados impone $\prod_s u_s^{a_s}=1$ cuando el monomio correspondiente tiene suma de frecuencias nula. Los cocientes de fases que satisfacen las ecuaciones parametrizan exactamente los competidores reales, porque la inversa de Fourier de un espectro conjugado-simétrico es real.

Definimos $\pi:\mathbb Z^S\to H$, $e_s\mapsto s$. Sea $L$ el retículo generado por las filas de las relaciones observadas, $e_0$ si procede y $e_s+e_{-s}$. Se tiene $L\subseteq\ker\pi$. Las fases compatibles forman el grupo de caracteres de $\mathbb Z^S/L$. Las traslaciones corresponden al dual de $H$, que se incluye en ese grupo. La restricción al subgrupo $\ker\pi/L$ es sobreyectiva (los caracteres con valores en $U(1)$ se extienden) y su núcleo es el dual de $H$.

Por tanto, la ambigüedad módulo traslaciones es

$$\operatorname{Hom}(\ker\pi/L,U(1)).$$

La condición de unicidad es $L=\ker\pi$. La forma normal de Smith calcula la estructura del grupo $\mathbb Z^S/L$: si tiene rango libre positivo, la ambigüedad es continua; si es finito, el número de soluciones módulo traslación es $|\mathbb Z^S/L|/|H|$. Se puede trabajar con una sola variable por par conjugado y añadir las restricciones de signo de los coeficientes autoconjugados, como hacen las auditorías.

La fórmula presupone datos consistentes con una señal y magnitudes no nulas en el soporte declarado. En presencia de ceros o ruido mal clasificado, las ecuaciones y el retículo pueden cambiar. Para el problema binario no basta contar todas estas soluciones: hay que intersectarlas con el conjunto admisible.

## 2. Caso Walsh

En $\mathbb F_2^d$ los caracteres son reales. Con DC fijado y $s=|S\setminus\{0\}|$, hay $s$ signos de fase. Sea $d'=\dim\langle S\rangle$ y $M$ la matriz binaria de relaciones observadas. Las traslaciones aportan exactamente $d'$ libertades. Para magnitudes y relaciones consistentes, el número de señales reales compatibles modulo traslación es

$$N=2^{s-d'-\operatorname{rank}_{\mathbb F_2} M}.$$

Para el soporte completo de un subespacio, las dependencias triples generan todas las necesarias. En general, las dependencias fundamentales respecto a una base tienen longitud a lo sumo $d'+1$. Un soporte con los vectores de una base y su suma tiene una única dependencia de longitud $d'+1$; no existe suficiencia universal del orden 3.

La auditoría IX aplica esto al indicador del conjunto Q48 dentro de $\mathbb F_2^{12}$: 511 frecuencias no constantes, rango del soporte 9 y rango de las relaciones triples 502. Se trata de un espacio ambiente de señales reales. La auditoría X restringe los candidatos a indicadores y obtiene 28 órbitas de traslación. La diferencia entre ambos espacios, no el número 48, es la cuestión de observabilidad que interesa.

## 3. Caso cromático: orden mínimo y prior

En $\mathbb Z_{12}$ los indicadores tienen 22 patrones de soporte espectral si se cuenta DC. El cálculo por Smith de la fase IX y por Hermite/divisibilidad ciclotómica de la fase XI concuerda. De las 4096 señales iniciales binarias, 3830 requieren orden 3 en el espacio real, 262 requieren orden 4 y cuatro están determinadas con orden hasta 2 (DC y magnitudes dadas).

Entre indicadores, el censo espacial por órbitas ponderadas da 796, 3276 y 24 para los órdenes agrupados hasta 2, 3 y 4. Se observa una reducción de orden en 238 de los 262 casos que requieren orden 4 sin el prior. Los datos completos para $2\le n\le16$ están en [results/rgo_fase11_results.json](../results/rgo_fase11_results.json).

Hay una sola pareja de órbitas no distinguida por las correlaciones triples completas: A={0,1,3,4,5,8}, B={0,3,4,5,7,8}. Son inversas, no transpuestas. Se distinguen en orden 4. En el cociente por transposición e inversión, las 224 clases se separan ya con las correlaciones triples.

## 4. Certificación cuantitativa y consultas

Las identidades de momentos no negativos de la nota XI permiten verificar si una señal es binaria o está próxima a algún indicador. La reducción de ambigüedad por prior no prueba que el prior sea correcto. El próximo paso consiste en estudiar la distancia de las observaciones a la imagen del modelo, la posibilidad de múltiples priors y la detección de incompatibilidad.

Una vez fijada una familia de candidatos, un diccionario de consultas genera un código de observaciones. El problema de selección fija de consultas con distancia mínima $h$ equivale a cubrir al menos $h$ veces cada par ambiguo con consultas que lo separen. En Z₁₂, con espectro/DC exactos, las 62 consultas de tres y cuatro posiciones generan 189 restricciones. Ocho testigos de separación disjuntos más una lista de ocho consultas que separa todos los pares prueban el mínimo 8h si se permite repetir. La estrategia adaptativa modifica la próxima consulta según la fibra restante. Los resultados no se transfieren automáticamente a diccionarios distintos.

## 5. Alcance y referencias

La recuperación de órbitas mediante invariantes, la reconstrucción por correlaciones, la teoría de retículos y los códigos son áreas establecidas. No se reivindica originalidad de estas herramientas. La cuestión abierta es qué resultados particulares de conteo, diseño mínimo y robustez aportan algo no cubierto por la bibliografía existente, y si son útiles en otras tareas.

Consultar las referencias de [la nota XI](rgo_fase11_nota.md#referencias-y-alcance-bibliográfico), en particular Jaming–Kolountzakis (2003), Keleti–Kolountzakis (2006), Bandeira et al. (2023), Agulnick–Busick-Warner (2026) y Casper–Orozco (preprint). El [registro de correcciones](CORRECCIONES.md) delimita los casos de estudio Walsh, GF(4) y cuántica.

Reproducir: `python audits/rgo_fase9_audit.py`, `python audits/rgo_fase10_audit.py`, `python audits/rgo_fase11_audit.py`. Resultados originales bajo `results/`. Las tres salidas se reprodujeron sin diferencias al preparar v0.3.
