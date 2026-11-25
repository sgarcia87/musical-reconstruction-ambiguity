# RGO — Fase XI: conocimiento previo, ambigüedad y robustez

**Nota de investigación · Sergi Garcia Mecinas · 25 de noviembre de 2026**

## Pregunta

¿Qué información adicional se necesita para recuperar una estructura cuando se conocen sus magnitudes, y qué cambia si conocemos su naturaleza (binaria, no negativa o real arbitraria)? ¿Qué observaciones conviene seleccionar cuando hay ruido o errores?

Esta nota sustituye la búsqueda de excepcionalidad de Q48 por un problema de reconstrucción bajo simetrías. No presupone una teoría física ni una interpretación de la consciencia. Los resultados exactos, las simulaciones y las afirmaciones de prioridad bibliográfica se distinguen.

## 1. Marco y convenciones

Sea G un grupo abeliano finito, escrito aditivamente, y f:G→R. Definimos C_k(f;t_1,…,t_{k−1})=Σ_x f(x)f(x+t_1)…f(x+t_{k−1}). Se conocen todas las correlaciones hasta el orden r, incluidos desplazamientos repetidos. C_1 es la suma; C_2 es la autocorrelación; C_3 y C_4 conservan información adicional de fase. Identificamos **traslaciones**, no reflexiones, salvo indicación explícita. Para comparar mínimos, se supone conocido el espectro de potencia (orden 2) y la componente constante, por lo que los casos determinados por cardinalidad o soporte constante se agrupan en «hasta orden 2».

En el lado de Fourier, las magnitudes y la componente constante están fijadas. Si S es el soporte no constante, las fases de una señal real satisfacen conjugación entre k y −k, y un coeficiente autoconjugado tiene signo ±. Cada producto de hasta r frecuencias cuya suma sea cero proporciona una relación entera entre fases. Las filas de estas relaciones generan un retículo. Si la matriz tiene rango completo, el índice del retículo calculado mediante forma normal de Hermite da el número de soluciones de fase; el orden del grupo de traslaciones efectivo es n/gcd(n,S). Si ambos coinciden, hay unicidad módulo traslación. Si no hay rango completo, queda ambigüedad continua. Este criterio se usa para reconstrucción real sin imponer positividad ni integridad.

Para conjuntos binarios, se enumeran las órbitas de subconjuntos y se comparan los recuentos de todos los patrones trasladados de tamaño hasta r. Esto equivale a las correlaciones completas, pues las coincidencias de posiciones se reducen a órdenes inferiores para un indicador. Se han empleado procedimientos distintos de las fases IX y X (cálculo exacto de ceros mediante divisibilidad ciclotómica, forma de Hermite y correlaciones en el dominio espacial).

## 2. Censo exacto

En Z12 hay 4096 indicadores, 352 órbitas por traslación y 224 clases por traslación/reflexión. Los recuentos de órdenes se ponderan por tamaño de órbita, de modo que suman 4096 configuraciones, no 352.

| Orden mínimo (con espectro dado) | Real arbitrario | Binario |
|---|---:|---:|
| Hasta 2 | 4 | 796 |
| 3 | 3830 | 3276 |
| 4 | 262 | 24 |

De los 262 indicadores cuyo espectro permite una ambigüedad continua en orden 3, 190 quedan determinados entre indicadores ya por orden 2, 48 por orden 3 y 24 todavía necesitan orden 4. El 90,84% reduce el orden. Los siete tipos de soporte espectral responsables se detallan en el JSON. La misma auditoría se ejecuta para cada n de 2 a 16; los resultados de orden 4 son (n, real, binario): (4,4,0), (6,6,0), (8,36,0), (10,30,0), (12,262,24), (14,126,28), (16,1316,128). No es una generalización estadística a todos los n.

## 3. Certificación y estabilidad del prior binario

Para un indicador A de cardinalidad m, los momentos diagonales m_j=Σ_x f(x)^j valen m para todo j≥1. Si g≥0 y comparte momentos hasta 3, entonces D3=Σ g(g−1)^2=m3−2m2+m1=0, luego g es binario. Para g real sin restricción de signo, D4=Σ g²(g−1)²=m4−2m3+m2=0 también fuerza g binario. La primera afirmación es el análogo discreto de Jaming–Kolountzakis (2003), Prop. 2.7.

Sea r_B el orden mínimo de reconstrucción entre indicadores, r_+ entre señales no negativas, y r_R entre reales, con correlaciones completas hasta el orden indicado. Entonces

r_B ≤ r_+ ≤ max(3,r_B),

r_B ≤ r_R ≤ max(4,r_B).

Esto vale para cualquier grupo finito. Prueba: el orden de certificación obliga a que cualquier competidor sea binario; entonces basta la unicidad dentro de ese conjunto. No se reclama prioridad. Los casos de orden 4 dentro del espacio binario son necesariamente de orden 4 entre reales. Entre los indicadores que requieren orden 4 en el espacio real, la mera no negatividad ya resuelve en orden 3 los que tienen r_B≤3. No se ha clasificado completamente el orden 2 bajo no negatividad.

Versión cuantitativa: d_B(g)^2=Σ min(g²,(g−1)²). Para g≥0, d_B²≤2D3; para cualquier g real, d_B²≤4D4. Para probar la primera cota, si 0≤g≤1/2 se tiene g²/[g(1−g)²]≤2 y si g≥1/2 el cociente es 1/g≤2 (con los ceros tratados directamente). Para la segunda, el producto de los dos cuadrados es al menos un cuarto de su mínimo. Las constantes son óptimas en g=1/2. Si cada momento requerido difiere de m en ≤ε, las cotas respectivas son 8ε y 16ε. Son certificados de cercanía a **algún** indicador, no de recuperación de la estructura verdadera. No deben confundirse con cotas de error para mediciones individuales sin procesar.

## 4. Lectura musical: qué pares de estructuras necesitan orden cuatro

Con inversión y traslación identificadas, hay 23 pares Z, 15 de seis notas. El recuento de todas las clases de tricordos (subconjuntos de tres notas, hasta inversión/traslación) distingue todos ellos. El JSON proporciona, para cada par, un tricordo testigo y sus recuentos. Con orientación conservada, hay 125 familias ambiguas tras conocer el espectro, 276 órbitas y 189 pares no ordenados dentro de esas familias. Las correlaciones triples separan 188 pares; el único que no separan es A={0,1,3,4,5,8}, B={0,3,4,5,7,8}. Son reflejos no trasladables, no un par Z en sentido T/I. Sus correlaciones de orden 4 los distinguen.

Ambos son autocomplementarios por traslación de 6. Por ello, los coeficientes pares no constantes se anulan, y tres frecuencias impares no suman cero módulo 12. Su 3-deck no contiene información de fase más allá del 2-deck. Esta familia de contraejemplos está relacionada con la literatura del k-deck, no se reclama como nueva.

## 5. Observación con ruido: predicción en el modelo de alineación multirreferencia

Sea P_A la distribución de y=T_s a + ξ, donde a es el indicador, s es una traslación uniforme independiente para cada muestra y ξ es ruido gaussiano N(0,σ²I). Sea φ_σ la densidad del ruido. Para dos indicadores a,b,

D_σ=∫(P_A(y)−P_B(y))²/φ_σ(y) dy
    = (1/n) Σ_t [exp(<a,T_t a>/σ²)+exp(<b,T_t b>/σ²)−2exp(<a,T_t b>/σ²)].

Demostración: integrar el producto de dos densidades gaussianas desplazadas dividido por φ_σ da exp(<u,v>/σ²), y la invariancia por traslación reduce la doble suma a una sola. La expansión de la exponencial da

D_σ=Σ_{k≥1} ||M_k(a)−M_k(b)||_F²/(k! σ^{2k}),

con M_k(a)=(1/n)Σ_t(T_t a)^{⊗k}. Los coeficientes se calculan mediante recuentos enteros de solapamientos; el JSON evalúa la serie hasta orden 80 (no una simulación Monte Carlo de densidades). Para ruido alto, si r es el primer momento que distingue el par, D_σ~C σ^(−2r). Es un caso particular de la teoría de recuperación de órbitas de Bandeira et al. (2023), con complejidad muestral asintótica de orden σ^(2r) para distinguibilidad entre candidatos fijos y bajo sus hipótesis. No equivale a un número de muestras exacto para grabaciones reales.

Ejemplo de tercer orden: A={0,1,2,3,4,8}, B={0,1,2,4,5,6}. Norma al cuadrado de diferencia de momento de orden 3: 8, constante C=4/3. Ejemplo de cuarto orden: el par reflejado anterior, norma al cuadrado de orden 4:16, C=2/3. Por ello la distancia ponderada del primer par es asintóticamente 2σ² veces la del segundo. Si σ se duplica en el régimen de ruido alto, el coste asintótico aumenta por 64 o 256 respectivamente. Esto aporta una predicción cuantitativa comparando pares musicales en un modelo estadístico explícito, no una afirmación perceptual o experimental sobre música real.

## 6. Selección fija robusta como código de observación

Hipótesis: se conoce exactamente el espectro/2-deck y se busca identificar la órbita de traslación del indicador. Las consultas permitidas son recuentos escalares de un patrón trasladado (19 órbitas de tricordos, 43 de tetracordos; 62 tipos). Un patrón que tiene simetrías puede contarse con multiplicidad de traslaciones; usar el recuento de subconjuntos distintos es equivalente para exactitud y distancia de Hamming, puesto que solo cambia un factor fijo por consulta.

Los 189 pares ambiguos generan 189 restricciones: se necesita al menos h consultas en las que difieran las respuestas de cada par. Si se eligen h=1, hay unicidad; h=2, se detecta una lectura arbitrariamente errónea o se recupera tras una lectura borrada con posición conocida; h=3, se corrige una lectura arbitrariamente errónea en una posición desconocida. Se trata de Hamming sobre el vector de consultas, no sobre las notas.

El mínimo global fijo es **8h** si se permiten repeticiones. La prueba inferior usa siete pares de tricordos reflejados cuyos conjuntos de consultas discriminantes (dos en cada caso) son disjuntos entre sí; los tetracordos no distinguen tricordos. El par de seis notas que requiere orden 4 añade una octava restricción disjunta. Todas deben cubrirse h veces. Una selección fija de 8 consultas alcanza la cota: [013], [034], [035], [045], [046], [056], [037], [0348]. La auditoría comprueba que separa los 189 pares; repetir cada consulta h veces alcanza 8h. El JSON contiene los testigos de la cota inferior. Sin repeticiones, existe una selección de 16 consultas de distancia mínima 2, pero ni las 62 juntas consiguen distancia mínima 3: los pares de tricordos solo difieren en dos consultas. Las repeticiones deben ser lecturas distintas; el resultado no corrige un sesgo sistemático que afecte a todas.

Si se permite elegir la lista fija según la familia conocida de 2-deck, 112 de las 125 familias necesitan una consulta, 12 necesitan dos y una necesita tres. Un árbol adaptativo óptimo resuelve esa última en dos, por lo que la cota de peor caso baja de 3 a 2. Se enumeraron las listas y árboles posibles. No confundir este coste contextual con las 8 consultas de una lista universal.

## 7. Simulación exploratoria de consultas ruidosas

Modelo diferente al de la sección 5: consultas individuales de recuentos de patrones distintos, con error gaussiano independiente de desviación típica σ, previo uniforme entre órbitas dentro de las 125 familias ambiguas (familia de 2-deck conocida exactamente). Se muestrean uniformemente las 276 órbitas ambiguas; 6000 ensayos por cada configuración (σ y presupuesto), semilla 11026. Se actualiza una distribución posterior gaussiana y se decide por MAP. Las cuatro estrategias usan el mismo conjunto de candidatos y presupuesto: consulta de máxima varianza posterior (adaptativa), repetición de la consulta de máxima varianza inicial, lista fija diversa que reduce vorazmente la suma de afinidades gaussianas entre pares, y selección aleatoria entre consultas informativas. La regla de varianza no es una optimización exacta de la información mutua. Las simulaciones son exploratorias, no se declaran diferencias estadísticamente significativas sin inferencia específica.

| σ=1 | Adaptativa | Fija diversa | Fija repetida | Aleatoria informativa |
|---|---:|---:|---:|---:|
| 3 consultas | 81,82% | 80,22% | 78,68% | 76,25% |
| 6 consultas | 89,71% | 89,32% | 85,88% | 85,91% |
| 12 consultas | 96,36% | 96,13% | 90,66% | 93,80% |

La estrategia fija diversa es una referencia fuerte: la ventaja adaptativa promedio es pequeña. En familias con más de dos candidatos, con 3 consultas y σ=1, se obtiene 67,68% frente a 60,22%; con 6, 80,82% frente a 76,44%. Las familias de dos candidatos predominan y en ellas repetir la mejor consulta ya es competitivo. No se ha demostrado superioridad general ni coste de adquisición idéntico para observaciones de orden 3 y 4 en sistemas físicos.

## 8. Correcciones y próximos pasos

- La excepcionalidad del 4 de la fase X solo vale para la unión perforada de dos subespacios complementarios. Las construcciones clásicas de partial spreads proporcionan funciones bent en otras dimensiones pares; no hay excepcionalidad general.
- Las 28 clases de la construcción reducida se relacionan con las formas alternantes no degeneradas de dimensión 4, GL(4,2)/Sp(4,2). No se reivindica como nuevo el conteo. La correspondencia con Cubo64 es una aplicación lineal concreta, no una equivalencia exclusiva entre proyectos.
- Homometría del indicador de Q48 sobre F2^12 y homometría de cada conjunto musical sobre Z12 son problemas diferentes. La relación algebraica con Hadamard no es una validación física cuántica.
- El estado central de RGO es ahora la reconstrucción condicionada: fibra de candidatos, separación por observaciones, robustez ante ruido y costo de observación. La coherencia no sustituye la capacidad de distinguir. Las cotas de distancia a un prior tampoco certifican identidad.
- El siguiente paso es probar la misma lógica en grafos semánticos con etiquetas externas y perturbaciones realmente irrelevantes: medir separación de candidatos, estabilidad bajo perturbaciones y costo de consultas. La presente fase no contiene esa validación empírica. Estudiar también la generalización de los mínimos 8h a otros tamaños y diccionarios, y la selección robusta cuando el espectro mismo tiene errores.

## Referencias y alcance bibliográfico

- P. Jaming y M. N. Kolountzakis, *Reconstruction of functions from their triple correlations* (2003), https://nyjm.albany.edu/j/2003/9-12.pdf (especialmente Prop. 2.7).
- T. Keleti y M. N. Kolountzakis, *On the determination of sets by their triple correlation in finite cyclic groups* (2006), https://doi.org/10.61091/ojac-104 (clasificación de grupos y resultados previos sobre k-deck).
- A. Agulnick y T. Busick-Warner, *Higher-Order Autocorrelations on Finite Abelian Groups*, preprint 14 de abril de 2026, https://arxiv.org/abs/2604.13310 (cotas basadas en soporte y ejemplos de orden elevado).
- W. R. Casper y B. Orozco, *Reconstructing rational functions on finite Abelian groups with higher autocorrelations*, https://doi.org/10.1016/j.acha.2026.101908 (funciones racionales, cotas de separación).
- A. S. Bandeira et al., *Estimation under group actions: Recovering orbits from invariants* (2023), https://doi.org/10.1016/j.acha.2023.06.001 (ruido alto, momentos invariantes y complejidad muestral).

Los antecedentes demuestran que ni el problema de los k-decks ni la diferencia entre conjuntos y funciones son nuevos. No se ha establecido prioridad de los recuentos particulares, de las cotas de estabilidad ni del diseño mínimo de consultas para Z12. El valor inmediato es la formulación precisa y la auditoría reproducible. No se ha actualizado GitHub en esta fase.

## Reproducir

Python 3.10+, NumPy, SymPy. `python rgo_fase11_audit.py > rgo_fase11_results.json`. Se han ejecutado las aserciones y las simulaciones. El resultado contiene el censo, las parejas Z, las restricciones de soporte, las curvas de ruido, los árboles y los testigos de minimalidad.
