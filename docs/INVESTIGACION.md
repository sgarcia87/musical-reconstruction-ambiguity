# Geometría relacional y observabilidad

**RGO · Informe matemático v0.3 · Sergi Garcia Mecinas · 25 de noviembre de 2026**

[Web interactiva](https://sgarcia87.github.io/relational-geometry-observability/) · [Nota de ambigüedad espectral](AMBIGUEDAD_ESPECTRAL.md) · [Robustez](rgo_fase11_nota.md) · [Agenda](ROADMAP.md) · [Correcciones](CORRECCIONES.md)

> **Actualización v0.4 (26/11/2026):** este informe conserva la investigación matemática de v0.3 y sus condiciones. Las nuevas fases XII–XVI sobre fragilidad del prior y observabilidad semántica se encuentran en [SEMANTICA.md](SEMANTICA.md), incluidos los resultados negativos y las limitaciones. No se transfieren automáticamente los teoremas a grafos semánticos.

## Resumen

Este proyecto estudia cómo reconstruir estructuras finitas a partir de observaciones que conservan algunas relaciones y pierden otras. El espacio de candidatos admisibles, las simetrías, el orden de las observaciones y su fiabilidad determinan la ambigüedad residual. Se utiliza la música como laboratorio discreto: las doce clases de altura forman un grupo cíclico de doce posiciones, y cada conjunto de notas puede representarse mediante doce bits. Los resultados incluyen una formulación de la ambigüedad de fase mediante retículos, una comparación exacta del orden de reconstrucción con diferentes conocimientos previos, un diseño mínimo de consultas resistentes a errores y un criterio de reconstrucción temporal por conectividad. Se distingue lo demostrado de las simulaciones, los resultados condicionados y las preguntas abiertas.

El informe es independiente de los proyectos anteriores del autor. No requiere conocer IA_m ni aceptar una premisa filosófica.

## 1. Estructura: un reloj de doce posiciones

Imaginemos doce luces en círculo. Cada una puede estar encendida o apagada. Existen 2¹² = 4096 configuraciones posibles. Si sabemos que hay seis luces encendidas, quedan 924 candidatos. Si además conocemos todas las distancias entre las luces, reducimos las posibilidades, pero no necesariamente a una.

En música, cada posición representa una clase de altura: Do=0, Do♯=1, ..., Si=11. Dos notas separadas por octavas se identifican. Un conjunto $A$ queda representado por un indicador $f(x)$, igual a 1 si $x$ pertenece a $A$ y 0 en caso contrario. No representa timbre, registro ni dinámica.

El grupo $\mathbb Z_{12}$ describe las posiciones y su suma modular. Girar todas las luces equivale a transponer todas las notas. Si buscamos la forma relativa, tratamos todas las transposiciones como equivalentes. Este conjunto de estados equivalentes se llama órbita. Una reflexión no se ignora salvo que se especifique.

Formalmente, una observación $O$ produce información $O(x)$ sobre un estado $x$. La fibra de candidatos compatible con un resultado $y$ y un conocimiento previo $\mathcal A$ es

$$\mathcal F(y;\mathcal A)=\{x\in\mathcal A:O(x)=y\}.$$

Si el objetivo es identificar la órbita, contamos las órbitas compatibles, no las posiciones absolutas. Una observación invariante puede ser correcta pero incompleta.

## 2. Ambigüedad: magnitud y fase

Para una señal sobre $\mathbb Z_n$ se define

$$F_k=\sum_{x=0}^{n-1} f(x)e^{-2\pi ikx/n}.$$

El coeficiente complejo contiene módulo y fase. El espectro de potencia $|F_k|^2$ equivale a la autocorrelación; para un indicador codifica los recuentos de pares de posiciones a cada distancia. La traslación multiplica $F_k$ por un factor de módulo uno, por lo que las magnitudes no cambian.

Dos conjuntos distintos pueden compartir todas esas magnitudes. Son homométricos. En teoría musical, la relación Z suele distinguir conjuntos no equivalentes por transposición ni inversión. Esta es una cuestión conocida en teoría de conjuntos musicales y cristalografía.

Las correlaciones de orden $r$ describen relaciones entre $r$ posiciones:

$$C_r(t_1,\ldots,t_{r-1})=\sum_x f(x)f(x+t_1)\cdots f(x+t_{r-1}).$$

El orden 1 mide la suma; el 2 las relaciones por pares; el 3 las relaciones triples y el 4 las cuádruples. En este informe se conocen las correlaciones de todos los órdenes hasta el indicado, incluidos desplazamientos repetidos, salvo en el protocolo explícito de consultas escalares.

En Fourier, un producto $F_aF_b\overline{F_{a+b}}$ conserva información sobre la combinación de fases $\theta_a+\theta_b-\theta_{a+b}$ y es invariante bajo traslación. Se denomina coeficiente del biespectro. No garantiza por sí solo reconstrucción única.

### Un ejemplo que necesita el cuarto orden

Los conjuntos

- A = {0,1,3,4,5,8}
- B = {0,3,4,5,7,8}

son reflejos, pero no transposiciones. Sus correlaciones completas de orden 2 y 3 son idénticas. Una observación de orden 4, $F_1^3\overline{F_3}$, los distingue: toma los valores −8+24i y −8−24i, respectivamente. Alternativamente, contar el patrón trasladado {0,3,4,8} produce 1 y 2.

Ambos conjuntos se complementan al trasladarlos seis posiciones. Esto anula los coeficientes pares no constantes; tres frecuencias impares no pueden sumar cero módulo 12. El fallo de las correlaciones triples se explica por el soporte espectral.

Cuando también se identifica la reflexión, esa pareja deja de ser una ambigüedad relevante. En las 224 clases por transposición e inversión, el espectro distingue 201; dos productos cúbicos reales específicos completan las 224. Los 23 pares Z en sentido T/I se distinguen por el contenido de tricordos.

## 3. Qué revela el conocimiento previo

Una observación puede admitir muchas señales reales y, al mismo tiempo, solo un conjunto binario. El prior cambia el espacio de candidatos: no aporta una medición nueva, sino una restricción sobre qué soluciones son admisibles.

Se enumeraron los 4096 indicadores de $\mathbb Z_{12}$ comparando dos problemas: recuperar el indicador entre señales reales cualesquiera con las magnitudes dadas, o recuperarlo entre indicadores. Ambos identifican traslaciones, no reflexiones, y agrupan en «hasta 2» los casos resueltos por cardinalidad o por información de segundo orden.

| Orden necesario | Señales reales | Indicadores binarios |
|---|---:|---:|
| Hasta 2 | 4 | 796 |
| 3 | 3830 | 3276 |
| 4 | 262 | 24 |
| Total | 4096 | 4096 |

Entre los 262 casos que requieren orden 4 en el espacio real, 190 se resuelven hasta orden 2 al exigir binariedad, 48 con orden 3 y 24 conservan la necesidad de orden 4. Es decir, el orden disminuye en 238 de 262 (90,84%).

Esta comparación se extendió por enumeración exacta a los grupos cíclicos de tamaños 2 a 16. No es un teorema para todos los tamaños. La distinción entre conjuntos y funciones y la reconstrucción por k-decks ya se estudian en la literatura; véanse Jaming, Keleti y Kolountzakis.

### Certificar el prior, no solo asumirlo

Sea $m_j=\sum_x g(x)^j$. Para un indicador de cardinalidad $m$, todos los momentos $m_j$ valen $m$. Si $g$ es no negativa,

$$D_3=m_3-2m_2+m_1=\sum_x g(x)(g(x)-1)^2.$$

Si $g$ es real arbitraria,

$$D_4=m_4-2m_3+m_2=\sum_x g(x)^2(g(x)-1)^2.$$

En ambos casos, la suma no negativa se anula si y solo si la señal es binaria. Así, correlaciones completas de orden 3 pueden certificar binariedad entre señales no negativas, y las de orden 4 entre señales reales. Esto se relaciona con la proposición 2.7 de Jaming y Kolountzakis (2003).

Si $r_B$ es el orden mínimo para identificar un indicador entre indicadores, $r_+$ entre no negativas y $r_R$ entre reales, se obtienen las cotas:

$$r_B\le r_+\le\max(3,r_B),\qquad r_B\le r_R\le\max(4,r_B).$$

También se puede acotar la distancia cuadrática a algún indicador:

$$d_B(g)^2=\sum_x\min\{g(x)^2,(g(x)-1)^2\}.$$

Para señales no negativas, $d_B^2\le2D_3$; para señales reales, $d_B^2\le4D_4$. Las constantes se alcanzan en $g(x)=1/2$. Si cada momento requerido difiere de $m$ en a lo sumo $\varepsilon$, las cotas correspondientes son $8\varepsilon$ y $16\varepsilon$. Esto certifica proximidad a **algún** indicador, no identidad con el objeto verdadero.

## 4. Criterio general: la geometría de las fases desconocidas

Fijemos el soporte espectral $S$ de una señal real sobre un grupo abeliano finito, las magnitudes de sus coeficientes y el coeficiente constante. Las relaciones de fase invariantes imponen ecuaciones lineales enteras módulo $2\pi$.

Sea $H$ el subgrupo generado por $S$. La aplicación $\pi:\mathbb Z^S\to H$ asigna a cada coordenada formal su frecuencia. Las relaciones observadas, junto a la condición de realidad y DC conocido, generan un retículo $L_r\subseteq\ker\pi$.

La ambigüedad de fase módulo traslaciones es el grupo dual de $\ker\pi/L_r$. Por tanto:

$$\text{Reconstrucción única hasta traslación}\iff L_r=\ker\pi.$$

La forma normal de Smith permite calcular el rango libre (ambigüedad continua) y la torsión (ambigüedad finita). Este criterio presupone magnitudes exactas y admite señales reales arbitrarias. Restricciones como binariedad pueden reducir adicionalmente las soluciones compatibles. La [nota técnica](AMBIGUEDAD_ESPECTRAL.md) desarrolla la prueba, el caso binario y los antecedentes.

La conexión entre grupos, invariantes y recuperación de fase no es nueva en sí misma. El objetivo de RGO es convertirla en un criterio explícito de conteo y selección de observaciones para problemas concretos.

## 5. Elegir las observaciones: reconstrucción robusta

Con el espectro exacto, la componente constante conocida y el objetivo de distinguir órbitas de indicadores sobre $\mathbb Z_{12}$, quedan 125 familias ambiguas que contienen 276 órbitas, con 189 pares a separar.

El diccionario de consultas consta de 19 clases de patrones de tres posiciones y 43 de cuatro, hasta traslación. Cada consulta devuelve un recuento escalar de ocurrencias. Cada candidato tiene una firma de respuestas.

Si las firmas de dos candidatos de la misma familia difieren en al menos $h$ posiciones, la distancia de Hamming mínima es al menos $h$. Esto permite identificar sin errores ($h=1$), detectar un error arbitrario o corregir un borrado conocido ($h=2$), o corregir un error arbitrario desconocido ($h=3$).

### Un mínimo exacto para este protocolo

$$M_{\min}(h)=8h,\quad h\ge1.$$

Hipótesis: lista fija universal, espectro/DC exactos, diccionario anterior y repeticiones permitidas. La cota inferior procede de ocho restricciones disjuntas de separación: siete pares de tricordos reflejados y el par de seis posiciones que requiere orden 4. Una lista de ocho consultas separa los 189 pares; repetirla $h$ veces alcanza la cota. Véase [la demostración y los testigos](rgo_fase11_nota.md#6-selección-fija-robusta-como-código-de-observación).

| Objetivo | Distancia mínima | Consultas |
|---|---:|---:|
| Identificar sin error | 1 | 8 |
| Detectar un error / recuperar un borrado | 2 | 16 |
| Corregir un error | 3 | 24 |

En general, para corregir $e$ errores arbitrarios, se requieren $8(2e+1)$ lecturas. Las repeticiones cuentan como lecturas distintas: no corrigen un sesgo que corrompa todas las repeticiones más allá del presupuesto de errores. Sin repetición, la distancia mínima de todo el diccionario de 62 consultas es 2, por lo que no garantiza corregir un error.

No se trata de una cota universal sobre mediciones físicas, bits de información ni recuperación a partir de audio.

### Perspectivas adaptativas

Cuando ya se conoce la familia ambigua, puede elegirse un protocolo específico. De las 125 familias, 112 necesitan una consulta fija, 12 necesitan dos y una necesita tres. En esa última, un árbol adaptativo necesita solo dos. El peor caso baja de tres a dos consultas.

En simulaciones de recuentos con ruido gaussiano independiente, se compara una estrategia adaptativa de varianza posterior, una fija diversa, una fija repetida y una aleatoria informativa. Con desviación típica 1 y seis consultas, las tasas de identificación son aproximadamente 89,71%, 89,32%, 85,88% y 85,91%. La estrategia fija diversa es competitiva. No se afirma una ventaja adaptativa general ni significación estadística de diferencias pequeñas.

## 6. Ruido y orden de observación

Un segundo modelo estadístico observa una señal trasladada uniformemente al azar y perturbada por ruido gaussiano. Para dos candidatos fijos, si el primer momento invariante que los distingue es de orden $r$, una distancia cuadrática ponderada entre sus distribuciones decrece asintóticamente como $\sigma^{-2r}$ en ruido alto.

La teoría de recuperación de órbitas relaciona el orden con el coste muestral asintótico. Duplicar el ruido multiplica la escala de muestras por $2^{2r}$: 16, 64 o 256 para órdenes 2, 3 o 4, respectivamente, bajo las hipótesis correspondientes. No son factores exactos para un número finito de mediciones ni resultados perceptuales de música real.

La [nota XI](rgo_fase11_nota.md) calcula las constantes para dos pares de indicadores mediante sumas exactas de solapamientos. El ruido sobre muestras trasladadas y el ruido sobre consultas escalares son modelos distintos; no se mezclan sus resultados.

## 7. Añadir el tiempo: reconstruir una secuencia

Conocer la forma local de cada ventana salvo transposición no determina sus desplazamientos relativos. Dos secuencias de acordes mayores pueden ser idénticas tras normalizar cada acorde de manera independiente, aunque una cambie de tonalidad y otra no.

Al medir $F_k(A_j)\overline{F_k(A_i)}$ se conserva la diferencia de fase entre dos ventanas y se elimina la transposición común. Los ceros espectrales limitan qué desplazamientos se pueden recuperar.

Para cada potencia prima que divide el tamaño $n$ del grupo cíclico, construimos un grafo de relaciones capaces de determinar ese nivel. Si $c_{p^j}$ es el número de componentes conexas, el número de reconstrucciones relativas compatibles es

$$N=\prod_{p^j\mid n}p^{\max(0,c_{p^j}-1)},$$

donde el producto recorre las potencias de primos con $j\ge1$. La [nota temporal](OBSERVABILIDAD_TEMPORAL.md) demuestra esta fórmula con períodos locales y relaciones parciales conocidos.

En 382 corales de Bach, con uniones de clases de altura en ventanas de cuatro negras y sus órbitas locales conocidas, 377 secuencias son identificables usando correlaciones cruzadas completas entre ventanas consecutivas. Seis conexiones no consecutivas resuelven las cinco restantes, alcanzando una cota inferior para ese corpus y protocolo. No se recuperan grabaciones, octavas, voces ni la secuencia interna de cada ventana. Los resultados se conservaron de la ejecución anterior sobre el corpus original.

## 8. Casos de estudio: equilibrio, Walsh y cuántica

Q48 es una familia de 48 indicadores de doce posiciones definida por tres filas equilibradas y ortogonales. Sobre las clases de altura en $\mathbb Z_{12}$, coincide con los hexacordos que satisfacen $F_4=0$ y $|F_3|^2=4$. Es una caracterización exacta.

Otro problema diferente considera el **conjunto de esos 48 estados** como un subconjunto del hipercubo $\mathbb F_2^{12}$ y aplica la transformada de Walsh. Tras separar restricciones y simetrías, se obtiene un cociente de cuatro bits y seis puntos, relacionado con una función bent cuadrática y con las formas alternantes no degeneradas.

Entre señales reales con las magnitudes Walsh de Q48 hay 502 bits de ambigüedad relativa (DC positivo fijado); entre indicadores, 28 clases de traslación, equivalentes a $\log_2(28)$ bits con prior uniforme. El conteo de formas simplécticas es clásico. Seis consultas cúbicas binarias fijas o cinco adaptativas distinguen las 28 clases en ese ejemplo.

La transformación Walsh es algebraicamente la operación Hadamard sobre un registro cuántico. En el caso reducido de cuatro qubits, una copia promediada sobre una traslación uniforme desconocida es indistinguible entre las 28 clases. Con dos copias que comparten la traslación, ciertas esperanzas de observables revelan signos cúbicos. Es una predicción teórica dentro de un modelo, no discriminación perfecta con dos ejecuciones ni ventaja cuántica demostrada.

Estos casos se documentan en [la nota X](rgo_fase10_nota.md) y [el registro de correcciones](CORRECCIONES.md). La homometría Walsh del conjunto Q48 no equivale a la homometría musical de cada hexacordo. No se reivindica una excepcionalidad universal del número cuatro.

## 9. Coherencia, observabilidad y conocimiento previo equivocado

Una auditoría basada exclusivamente en la similitud entre perspectivas puede premiar que sus distribuciones se vuelvan indistinguibles. Una difusión común puede aumentar $1-\operatorname{JSD}$ mientras reduce la información sobre el origen. No significa que cualquier aumento de coherencia en cualquier contexto destruya información.

Si el objetivo $T$ es invariante y el canal y el prior respetan las simetrías apropiadas, el estadístico de órbita puede conservar la información sobre $T$ y eliminar la orientación irrelevante. De ahí la necesidad de especificar qué diferencias importan antes de optimizar una métrica.

El siguiente reto es la **fragilidad del conocimiento previo**: un conjunto de candidatos incorrecto puede generar una solución única y coherente que no contiene la estructura verdadera. Los certificados de la sección 3 son un primer paso, pero no bastan para garantizar identidad. Se investigarán detección de modelos incompatibles, errores en las magnitudes iniciales, ruido y selección de perspectivas con objetivos verificados externamente. Aún no se ha validado este marco sobre grafos semánticos reales.

## 10. Evidencia y límites

| Tipo | Resultado |
|---|---|
| Demostración algebraica | Retículo de relaciones de fase; cota de certificación; fórmula temporal; mínimo 8h bajo el diccionario establecido. |
| Enumeración exacta | Órdenes en los 4096 indicadores de Z₁₂ y censo hasta n=16; testigos de consultas; caso Walsh. |
| Simulación | Consultas escalares gaussianas; comparación de estrategias. |
| Resultado empírico condicionado | Identificabilidad temporal en el corpus de Bach. |
| Predicción teórica | Observables de dos copias cuánticas bajo traslación compartida. |
| Pendiente | Prioridad bibliográfica, costes físicos de adquisición, validación semántica y pruebas con prior/espectro erróneos. |

No se postula una teoría física de la realidad ni de la consciencia. No se afirma que Q48 sea musicalmente privilegiado. El objetivo es preciso: **cuantificar lo que una observación deja indeterminado y elegir las relaciones necesarias para resolverlo.**

## 11. Reproducibilidad y bibliografía

Ejecutar desde la raíz:

~~~bash
pip install -r requirements-research.txt
python audits/rgo_fase9_audit.py
python audits/rgo_fase10_audit.py
python audits/rgo_fase11_audit.py
python audits/verify_robustness.py
~~~

Las salidas de las tres auditorías recientes coinciden byte por byte con los JSON registrados. El verificador independiente calcula los recuentos por enumeración directa de subconjuntos y confirma la cota de 8h. No se ha repetido el análisis completo de Bach en v0.3.

Referencias de entrada:

- P. Jaming y M. N. Kolountzakis, *Reconstruction of functions from their triple correlations* (2003), https://nyjm.albany.edu/j/2003/9-12.pdf.
- T. Keleti y M. N. Kolountzakis, *On the determination of sets by their triple correlation in finite cyclic groups* (2006), https://doi.org/10.61091/ojac-104.
- E. Amiot, *Music Through Fourier Space* (2016), https://doi.org/10.1007/978-3-319-45581-5.
- J. Yust y E. Amiot, *Non-Spectral Transposition-Invariant Information in Pitch-Class Sets and Distributions* (2022), https://sites.bu.edu/jyust/files/2022/09/nonSpectralrevFin.pdf.
- A. S. Bandeira et al., *Estimation under group actions: Recovering orbits from invariants* (2023), https://doi.org/10.1016/j.acha.2023.06.001.
- A. Agulnick y T. Busick-Warner, *Higher-Order Autocorrelations on Finite Abelian Groups* (preprint 2026), https://arxiv.org/abs/2604.13310.
- W. R. Casper y B. Orozco, *Reconstructing rational functions on finite Abelian groups with higher autocorrelations*, https://arxiv.org/abs/2503.21022.

Los antecedentes y las correcciones de alcance quedan en [CORRECCIONES.md](CORRECCIONES.md). Las notas [X](rgo_fase10_nota.md), [XI](rgo_fase11_nota.md) y [temporal](OBSERVABILIDAD_TEMPORAL.md) contienen demostraciones y bibliografía ampliada. La [agenda](ROADMAP.md) establece las pruebas pendientes.
