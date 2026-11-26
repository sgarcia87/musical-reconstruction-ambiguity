# Phase retrieval and conditional temporal observability on cyclic pitch-class spaces

**RGO · v0.2 · Nota técnica (2026-11-25)**  
Autor del proyecto: Sergi Garcia Mecinas. Documento de trabajo, no revisado por pares.

> **Extensión XVIII:** la [nota sobre huella relacional musical](rgo_fase18_nota.md) distingue la observación cross-Fourier de la órbita conjunta, cuyo módulo es mcd(pᵢ,pⱼ). Se conservan las hipótesis del teorema original.

## Resumen

Se caracteriza Q48 por dos condiciones de Fourier y se construye un procedimiento exacto para medir la ambigüedad de secuencias de conjuntos de clases de altura ante observaciones locales y relaciones de fase entre instantes. Para una introducción sin conocimientos previos, véase [INVESTIGACION.md](INVESTIGACION.md). La construcción se apoya en resultados conocidos de homometría, análisis armónico y sincronización de fase. No se reivindica prioridad científica sin una revisión bibliográfica adicional.

## 1. Caracterización exacta de Q48

Sea $A\subseteq\mathbb Z_{12}$, $a=1_A$, $\zeta=e^{-2\pi i/12}$ y $F_k(A)=\sum_{n\in A}\zeta^{kn}$. Se dispone $a$ en la tabla CRT $(n\bmod3,n\bmod4)$. Las filas de signos $2a-1$ definen Q48 cuando tienen suma cero y son mutuamente ortogonales. Entonces:

$$A\in Q48\iff |A|=6,\quad F_4(A)=0,\quad |F_3(A)|^2=4.$$

**Prueba.** Si $r_j$ cuenta las notas de la fila $j$, $F_4=r_0+r_1\omega+r_2\omega^2$ con $\omega=e^{-2\pi i/3}$. Como $r_j$ son reales, el cero implica $r_0=r_1=r_2=2$ bajo la hipótesis de cardinalidad seis. Las tres direcciones de signos equilibradas, salvo signo global de cada fila, son $(1,1,-1,-1)$, $(1,-1,1,-1)$ y $(1,-1,-1,1)$. Sus contribuciones a $F_3$ son respectivamente $\pm(1-i)$, $0$ y $\pm(1+i)$. Una suma de un número impar de contribuciones no nulas tiene ambas coordenadas impares y no puede tener norma cuadrada 4. Cero contribuciones no nulas da 0. Dos contribuciones de la misma dirección dan 0 u 8; dos de direcciones distintas dan 4. Así debe haber exactamente una de cada tipo, equivalente a ortogonalidad por pares. Hay $3!2^3=48$ configuraciones. QED.

## 2. Biespectro y clases musicales

El producto $B=F_1^2\overline{F_2}$ es invariante por transposición. Su parte real es también invariante por inversión. En Q48 es real, no nulo, y sus valores son:

| Clase | B |
|---|---|
| 6-Z37 | $8+4\sqrt3$ |
| 6-Z4 | $-8-4\sqrt3$ |
| 6-Z48 | $8-4\sqrt3$ |
| 6-Z26 | $-8+4\sqrt3$ |

Cada clase contiene doce transposiciones distintas; la inversión no amplía ninguna órbita. Complementar cambia el signo de B. La aritmética exacta en $\mathbb Z[\zeta]$ permite verificar los 4096 estados sin tolerancias. Hay 224 órbitas por transposición/inversión, 201 perfiles de potencia y 23 pares Z (15 de seis notas). De los doce tipos de productos cúbicos con índices no nulos que suman cero módulo 12, identificados por permutación y conjugación, ninguna parte real individual completa el espectro de potencia, pero catorce parejas lo hacen. Un ejemplo es Re$(F_1^2\bar F_2)$ y Re$(F_1 F_2\bar F_3)$. Esta minimalidad solo concierne al diccionario de observables especificado.

## 3. Secuencias: reconstrucción de Q48

Una secuencia $A_0,\ldots,A_{L-1}$ de estados Q48 se determina hasta una única transposición global por la familia B de cada estado y los productos complejos $F_1(A_{t+1})\overline{F_1(A_t)}$. Fijar representantes locales permite dividir cada producto por el producto de los coeficientes de los representantes; resulta $\zeta^{s_{t+1}-s_t}$. Como $F_1$ nunca es cero en Q48 y $\zeta$ es primitiva, la diferencia de transposiciones se recupera exactamente. La trayectoria relativa se obtiene sumando diferencias. Un grafo conectado de relaciones basta, no necesariamente el camino cronológico. Los 2304 pares ordenados producen 192 órbitas globales distintas y 192 firmas observadas. Con etiquetas locales fijadas, un grafo de aristas de esta clase necesita al menos $L-1$ aristas para conectar $L$ instantes.

## 4. Teorema de ambigüedad temporal para grupos cíclicos finitos

Sea $n$ arbitrario. Se conocen las órbitas locales por **transposición**, no por inversión, de una secuencia $A_i\subseteq\mathbb Z_n$. El período mínimo $p_i$ es el número de transposiciones distintas de $A_i$: es el menor desplazamiento positivo que deja invariante el conjunto y divide a $n$. Equivale al mcm de los órdenes de los caracteres de su soporte espectral no constante. Para cada arista observada $(i,j)$ se conocen los productos complejos $F_k(A_j)\overline{F_k(A_i)}$ en las frecuencias medidas. Defínase $d_{ij}$ como el mcm de los órdenes $n/\gcd(n,k)$ de las frecuencias medidas que no se anulan en ninguno de los dos extremos (mcm vacío = 1).

Una segunda reconstrucción con las mismas órbitas locales y medidas se expresa mediante desplazamientos $s_i\bmod p_i$ respecto de una reconstrucción compatible. Las aristas exigen exactamente $s_i\equiv s_j\pmod{d_{ij}}$. En particular $d_{ij}$ divide $\gcd(p_i,p_j)$.

Para cada potencia prima $\ell=p^e$ que divide $n$, construimos un grafo $G_{\ell}$ con los vértices cuyo período es múltiplo de $\ell$ y las aristas con $\ell\mid d_{ij}$. Sea $c_\ell$ su número de componentes conexas (cero para grafo vacío). Entonces el número de reconstrucciones compatibles, identificando transposiciones globales, es exactamente

$$N=\prod_{p^e\mid n}p^{\max(0,c_{p^e}-1)}.$$

**Prueba.** Aplicar el teorema chino del resto a cada desplazamiento local separa las potencias de primos. Para el dígito de orden $e$ (en base $p$), las congruencias fuerzan igualdad precisamente dentro de cada componente de $G_{p^e}$. Los grafos están anidados: una arista presente al nivel superior también está presente al inferior. Por tanto cada componente activa aporta una elección independiente de $p$ valores para ese dígito. Hay $\prod p^{c_{p^e}}$ asignaciones locales. El grupo de desplazamientos globales actúa sobre ellas con órbitas de tamaño $\operatorname{lcm}_i p_i$; dividir por ese tamaño resta una potencia de $p$ por cada nivel activo. QED.

Para $n=12$:

$$N=2^{(c_2-1)_++(c_4-1)_+}3^{(c_3-1)_+}.$$

El criterio de unicidad es que cada grafo activo esté conectado. La prueba no depende de las fases concretas observadas; predice la ambigüedad a partir de los soportes de Fourier y la selección de aristas. Con una distribución uniforme sobre completaciones compatibles, $\log_2N$ es la entropía residual de esa fibra. No es necesariamente una entropía bajo un prior no uniforme.

### Contraejemplo

$A=\{0,1\}$, $B=\{0,2,4,6,8,10\}$ y $B'=B+1$. Las secuencias $(A,B)$ y $(A,B')$ no son transposiciones globales entre sí, pero poseen las mismas órbitas locales y toda su correlación cruzada cíclica coincide: cada desplazamiento produce exactamente una intersección. El primer estado tiene período 12, el segundo período 2 y no comparten ningún coeficiente no constante distinto de cero. El criterio predice exactamente dos soluciones.

### Auditoría

Se enumeran 352 órbitas locales por transposición. Entre todos los pares de estados de Q12 existen 1 398 500 órbitas globales ordenadas; 1 393 108 se recuperan de manera única a partir de las órbitas locales y de toda la correlación cruzada. Las 5392 restantes pertenecen a fibras ambiguas. El porcentaje se refiere a clases de pares de conjuntos, no a reconstrucción de audio. Se han contrastado además 1000 pares por cálculo directo de correlación y 300 secuencias de tres estados con grafos aleatorios mediante enumeración exhaustiva de desplazamientos.

## 5. Corpus Bach: reparar la observabilidad

Corpus JSB Chorales: 382 corales, discretización de negra, ventanas deslizantes de unión binaria de clases de altura. Git blob SHA-1 `ff93746647d1f5af2f719d235329c294267f3088`. Se supone que las órbitas locales por transposición están conocidas. Cada arista incluye todos los productos cruzados complejos de Fourier (equivalentemente, toda la correlación cruzada cíclica). Resultados:

| Ventana | Ventanas | Secuencias únicas con aristas consecutivas | Únicas con todas las aristas | Aristas adicionales para recuperar todas |
|---:|---:|---:|---:|---:|
| 1 | 23134 | 225 | 382 | 299 |
| 2 | 22752 | 356 | 382 | 41 |
| 4 | 21988 | 377 | 382 | 6 |
| 8 | 20460 | 370 | 382 | 16 |

Una arista adicional reduce en a lo sumo uno el número de componentes de cada grafo de nivel primo. Por ello $\max_\ell(c_\ell-1)_+$ es una cota inferior al número de aristas nuevas. Un algoritmo voraz (maximizar niveles conectados, desempatar por menor separación temporal y posición inicial) alcanza dicha cota en cada una de las 382 piezas para las cuatro longitudes. Este es un resultado de identificabilidad condicional, no de reconocimiento de canciones desde audio, ni de superioridad frente a métodos de identificación de versiones. Se ignoran octavas, intensidad, articulación, duración dentro de ventana, y conducción individual de voces. Los cálculos se ejecutaron sobre el JSON original mediante el conector de GitHub; el programa Python equivalente fue probado con contraejemplos sintéticos, no reejecutado localmente sobre todo el corpus.

## 6. Conexión cuántica y semántica

Para estados puros cuánticos con magnitudes de amplitudes conocidas, las coherencias complejas $\rho_{ij}=\alpha_i\overline{\alpha_j}$ permiten sincronizar las fases en un grafo sobre las amplitudes no nulas. Si el grafo está conectado, se recupera el estado puro hasta fase global; si no, queda una fase independiente por componente, salvo una global. Este es el análogo continuo de la sincronización de desplazamientos de los conjuntos musicales; no identifica la fase musical con una magnitud física cuántica. Los observables diagonales de orden tres en la base computacional no revelan por sí solos coherencias entre amplitudes. Se necesitan mediciones sensibles a fase, y la reconstrucción de estados mixtos requiere hipótesis diferentes.

Para la auditoría estructural, la variable objetivo T puede ser la órbita global de la secuencia y la perturbación irrelevante N su transposición común. La ambigüedad de la fibra cuantifica la pérdida del objetivo bajo una familia de observables invariantes. La invariancia bajo transformaciones irrelevantes no equivale a borrar información indiscriminadamente. La disminución de información bajo difusión común sigue de procesamiento de datos; un incremento arbitrario de C no implica necesariamente una reducción de información mutua en cualquier sistema. Falta ensayar T/N en grafos semánticos con etiquetas y perturbaciones validadas de manera externa y con referencias comparativas.

## Referencias y alcance de originalidad

- Amiot, E. (2016). *Music Through Fourier Space*. Springer. https://doi.org/10.1007/978-3-319-45581-5
- Mandereau, J. et al. (2011). *Z-relation and homometry in musical distributions*. https://doi.org/10.1080/17459737.2011.608819
- Mandereau, J. et al. (2011). *Discrete phase retrieval in musical structures*. https://doi.org/10.1080/17459737.2011.608820
- Yust, J.; Amiot, E. (2022). *Non-Spectral Transposition-Invariant Information in Pitch-Class Sets and Distributions*. https://sites.bu.edu/jyust/files/2022/09/nonSpectralrevFin.pdf
- Pebody, L. (2004). *The Reconstructibility of Finite Abelian Groups*. https://doi.org/10.1017/S0963548303005807
- Singer, A. (2011). *Angular synchronization by eigenvectors and semidefinite programming*. https://doi.org/10.1016/j.acha.2010.02.001
- *Chroma Interval Content as a Key-Independent Harmonic Progression Feature*. https://www.ime.usp.br/~rcborges/mmrp2019.pdf
- JSB Chorales dataset. https://github.com/czhuang/JSB-Chorales-dataset

La bibliografía confirma que homometría, biespectro, sincronización de fase y progresiones invariantes por tonalidad son campos existentes. La fórmula de ambigüedad en grafos de potencias primas es una deducción explícita de este estudio que deberá contrastarse en la literatura de sincronización sobre grupos finitos, congruencias y restricciones de cosets. No se afirma novedad global, ventaja cuántica, relevancia perceptual ni teoría de la consciencia. 
