# RGO · Fase X — Observabilidad, homometría y reducción algebraica

**Nota de investigación · 25 de noviembre de 2026 · Sergi Garcia Mecinas**

Estado: resultados matemáticos y auditoría exacta; prioridad bibliográfica no establecida. No es una teoría física ni un experimento cuántico. Se conserva esta nota fuera de GitHub hasta la próxima actualización acordada.

## 1. Definiciones y reducción de Q48

Sea V = F₂¹², con tres filas de cuatro bits (orden CRT: [[0,9,6,3],[4,1,10,7],[8,5,2,11]]). Un bit b corresponde al signo 2b−1. En cada fila de paridad par, los cuatro bits se expresan de forma única como (r,r+u,r+v,r+u+v) en F₂. El par (u,v) es la etiqueta de dirección y r es la orientación. Hay dos positivos y dos negativos si y solo si (u,v)≠(0,0). Los tres patrones no nulos son ortogonales dos a dos, y la inversión de una fila no cambia su dirección.

Identificando F₂² con GF(4) por (u,v)↦u+vω, las tres direcciones distintas son 1, ω, ω², cuya suma es cero. El conjunto Q48 equivale a (r₁,r₂,r₃,a,b), con a,b distintos y no nulos, y tercera dirección c=a+b. Así Q48 ≅ F₂³ × D como conjunto, donde D={(a,b): det₂(a,b)=1} tiene seis puntos en F₂⁴. Se verificó exhaustivamente que esta codificación da exactamente los mismos 48 estados que las restricciones originales.

Sea L el subespacio de estados cuyas filas tienen paridad par y cuyas tres etiquetas suman cero. Tiene dimensión 7. Sea R el subespacio de inversiones independientes de las tres filas, dimensión 3. L/R ≅ F₂⁴. Q48 es la preimagen de D en L. En coordenadas (a₀,a₁,b₀,b₁), D es el soporte de la función cuadrática bent f=a₀b₁+a₁b₀, o el grupo GL(2,F₂) visto como conjunto de matrices binarias invertibles. Estas identificaciones no igualan la ley multiplicativa de GL(2,F₂) con la suma de F₂⁴.

## 2. Correspondencia exacta con Cubo64

El proyecto Cubo64 usa GF(4), ω=2 y ω²=3 en codificación binaria, y M(a,b,c)=(a+ωb+ω²c, a+ω²b+ωc). Su núcleo es la diagonal {(t,t,t)}. Al restringir a P={a+b+c=0}, M es una biyección sobre GF(4)², porque P corta al núcleo solo en 0 y ambos espacios tienen dimensión 2 sobre GF(4). Sustituyendo c=a+b, M=(ωa+b,ω²a+b). En D, b/a∈{ω,ω²}. Así M(D) es exactamente {(u,0):u≠0} ∪ {(0,v):v≠0}. Son seis posiciones. Con la numeración original F=2(4u+v)+1, los valores son 3,5,7,9,17,25. La preimagen en las 64 celdas tiene 24 puntos. Q48 tiene ocho orientaciones por elemento de D; Cubo64 cuatro celdas por imagen. Es una correspondencia entre cocientes, no una equivalencia de las estructuras completas ni de sus propiedades mágicas.

Fuente original de la fórmula: https://github.com/sgarcia87/cubo-magico-64/blob/main/README.md .

### Generalización y excepcionalidad de cuatro

En F₂ᵐ × F₂ᵐ, q=2ᵐ, sea A la unión de dos ejes complementarios sin origen. Para un carácter (k,l), su Walsh no normalizado es q·1[k=0]+q·1[l=0]−2. Por tanto: 2(q−1) en 0; q−2 en 2(q−1) frecuencias; −2 en (q−1)² frecuencias. La magnitud de todos los coeficientes no constantes coincide si y solo si q=4 (q≥2). En particular q=4 es el caso bent especial de esta familia, no una propiedad de cualquier dimensión. Comprobado para q=2,4,8,16. No se afirma que para q>4 el espectro reconstruya cualquier conjunto binario sin ambigüedad.

## 3. Todos los conjuntos binarios homométricos a Q48

Definimos W_A(k)=Σ_{x∈A}(−1)^{k·x}. Los 4096 coeficientes de Q48 tienen distribución: 32 valores +48, 192 valores +16, 288 valores −16 y 3584 ceros. El soporte es R^⊥, de dimensión 9; las frecuencias con magnitud 48 son L^⊥, de dimensión 5. El cociente D tiene W_D(0)=6 y |W_D(k)|=2 para todo k≠0. Equivale a una función bent booleana de peso 6, puesto que W_{1−2 1_D}(0)=4 y las demás magnitudes son 4. La autocorrelación de D vale 6 en cero y 2 en los otros 15 desplazamientos (difference set (16,6,2)).

Sea A⊂V cualquier conjunto binario con |W_A|=|W_Q48|. Por W_A(0), |A|=48. Como su soporte espectral es R^⊥, la inversión de Fourier implica A+R=A. Además, para k∈L^⊥, |W_A(k)|=48. Cada sumando es ±1, así que todos los sumandos de esa frecuencia deben tener el mismo signo. Para cualquier x₀∈A, k·(x+x₀)=0 para todo x∈A y k∈L^⊥. Luego A⊂x₀+L. Dentro de ese coset, A es la preimagen por R de un conjunto de seis puntos de F₂⁴ con magnitudes (6,2,…,2). El recíproco se obtiene por Fourier de la preimagen y traslación. Por tanto hemos reducido exhaustivamente todos los candidatos binarios, sin explorar 2^4096 subconjuntos.

Entre C(16,6)=8008 conjuntos reducidos existen exactamente 448 con esas magnitudes. Todos tienen órbita de traslación de tamaño 16, porque ningún coeficiente no constante se anula. Hay 28 clases de traslación. Como hay 32 cosets de L, en V hay 32×448=14.336 candidatos binarios y cada órbita de traslación tiene 512 miembros. Todos los candidatos reducidos son funciones bent cuadráticas; los números 896 bent de 4 variables (448 de peso 6) y 28 partes cuadráticas no degeneradas son clásicos. No se reivindica su descubrimiento. Véase Carlet y Mesnager (2016), *Four decades of research on bent functions*, Designs, Codes and Cryptography, y https://oeis.org/A004491.

La fase IX contaba 502 bits en otro espacio de candidatos: amplitudes reales arbitrarias con magnitudes fijadas y DC positivo, no indicadores binarios. Son 511 signos no constantes menos 9 libertades de traslación. Bajo el nuevo prior binario quedan log₂(28)≈4,807 bits si las 28 clases son equiprobables. Las dos afirmaciones son compatibles. El conjunto de soluciones no es lo mismo que el conjunto de mediciones físicamente accesibles.

## 4. Mínimo de observaciones cúbicas bajo el prior binario

En el cociente, para índices distintos no nulos a,b, usamos el signo del producto W_D(a)W_D(b)W_D(a+b). La traslación multiplica W(k) por (−1)^{k·t}, así que cancela en ese producto. Hay 35 tríos distintos {a,b,a+b}. Sea g la función dual bent, definida por W_{1−2 1_D}(k)=4(−1)^g(k); g(0)=0. Para k≠0, W_D(k)=−2(−1)^g(k). Por tanto el signo del producto es −(−1)^{B(a,b)}, donde B es la forma polar alternante de g. B se determina por seis coeficientes B(eᵢ,eⱼ), i<j. En los 448 candidatos, la forma polar no depende de la traslación; las 28 formas distintas identifican exactamente las 28 clases.

- **Seis consultas fijas bastan:** usar (eᵢ,eⱼ), para los seis pares de una base binaria de cuatro elementos.
- **Cinco consultas fijas no bastan:** los 28 vectores de seis coeficientes tienen como diferencias todos los 63 vectores no nulos de F₂⁶ (enumeración exacta). Una aplicación lineal de rango ≤5 posee núcleo no trivial, por lo que confunde dos formas candidatas. Cada signo cúbico es una función afín de esos seis coeficientes.
- **Cinco consultas adaptativas bastan:** se construye un árbol que elige la próxima consulta según las respuestas anteriores. La búsqueda exacta usa 35 consultas posibles y poda por cardinalidad de candidatos. Se verifica el árbol sobre las 28 clases: cuatro terminan en cuatro preguntas y 24 en cinco. Menos de cinco no pueden distinguir 28 resultados mediante respuestas binarias. El árbol completo y los representantes se guardan en el JSON.

Minimalidad para este diccionario de consultas binarias, en el caso exacto y sin ruido. No es una cota de la cantidad de mediciones físicas.

## 5. Predicción cuántica comprobable

La codificación lineal anterior puede extenderse a una base de V. Una permutación lineal de bits, implementable mediante CNOT y SWAP, transforma la superposición uniforme de Q48 en |0⟩^⊗5 ⊗ |+⟩^⊗3 ⊗ |D⟩, salvo orden de registros. El estado relacional |D⟩ tiene cuatro qubits y seis amplitudes computacionales iguales a 1/√6. En la base Walsh, las amplitudes son α_k=W_D(k)/(4√6), con α_0=√6/4 y |α_k|=1/(2√6) para k≠0. Sus probabilidades son 3/8 y 1/24, respectivamente; todas las 28 clases presentan esas mismas probabilidades.

Supongamos que la traslación t es desconocida y uniforme en F₂⁴. En base Walsh actúa por Z_t|k⟩=(−1)^{k·t}|k⟩. Una sola copia, promediada sobre t, tiene matriz de densidad diagonal diag(3/8,1/24,…,1/24), idéntica para todas las clases. Ninguna medición sobre una sola copia marginalizada permite distinguirlas. Con varias copias trasladadas independientemente al azar ocurre lo mismo.

Con **dos copias que comparten la misma traslación**, existe un observable hermítico invariante:

O_ab=|a,b⟩⟨a+b,0|+|a+b,0⟩⟨a,b|.

Ambas bases de dos copias adquieren el mismo signo bajo la traslación común. Su esperanza es 2α_aα_bα_{a+b}α_0, cuyo valor exacto es ±1/96. El signo coincide con la consulta cúbica anterior. Se verifican las identidades para los 28 representantes, las 16 traslaciones y los pares no nulos distintos. En consecuencia, las seis esperanzas fijas distinguen las clases; el árbol de cinco consultas también puede expresarse en términos de signos de esperanzas, si se conocen sin error. El observable no es una medición del signo en una sola ejecución: las esperanzas se estiman mediante múltiples pares preparados de forma coherente. La diferencia una/dos copias es una afirmación de identificabilidad del modelo, no de discriminación perfecta con una única realización de dos copias ni de ventaja cuántica. No se ha preparado el estado en hardware.

## 6. Criterio general de fase para grupos abelianos finitos

Sea G finito abeliano, S⊂Ĝ el soporte espectral de una señal real, S=−S en notación aditiva, y H=⟨S⟩. Se conocen magnitudes y, si existe, el coeficiente DC. Para dos señales con esas magnitudes, el cociente de fases u_s está en U(1) y satisface u_{−s}=u_s^{-1}. Medir monomios invariantes de orden hasta r impone ∏u_{s_i}=1 para toda relación observada s₁+⋯+s_j=0 con j≤r. Definimos π: Z^S→H, e_s↦s. Sea L_r el subgrupo generado por las relaciones observadas, e_0 si procede, y e_s+e_{−s}. Entonces L_r⊂ker π.

El grupo de fases compatibles es Hom(Z^S/L_r,U(1)); las traslaciones son exactamente los caracteres inducidos por H. Al cocientarlas queda el dual del grupo ker π/L_r, usando que los caracteres de un subgrupo de un grupo abeliano finitamente generado se extienden a todo el grupo. **La identificación hasta traslación es equivalente a L_r=ker π.** La forma normal de Smith permite verificar la igualdad de retículos y calcular rango libre y torsión. Si Z^S/L_r es finito, el número de soluciones módulo traslación es su orden dividido por |H|. Si no, queda ambigüedad continua. El criterio es para señales reales arbitrarias con magnitudes fijadas, salvo las restricciones explícitas, no para una clase de indicadores más estrecha.

Una cota general suficiente es el máximo entre 2 y la constante de Davenport D(H): toda secuencia de suma cero se descompone en secuencias mínimas de suma cero de longitud ≤D(H); para relaciones enteras los coeficientes negativos se reemplazan por caracteres opuestos gracias a la condición de realidad. Si todos los monomios necesarios se observan, el retículo queda generado. Esto pertenece a la teoría de invariantes y suma cero; no se afirma prioridad.

### Caso binario F₂ᵈ: una fórmula de rango

Sean s=|S\{0}| y d'=dim(span S). Las fases de señales reales son signos. Escribiendo signos como bits, cualquier relación de fase de orden r es una fila del espacio de dependencias lineales de las frecuencias. Sea M_r la matriz que recoge las dependencias observadas (XOR nulo). La cantidad de soluciones módulo traslación es

N_r = 2^(s−d'−rank₂ M_r).

El espacio completo de dependencias tiene dimensión s−d'. Se puede generar con las dependencias fundamentales de una base del soporte, de longitud a lo sumo d'+1; por ello hay una elección de s−d' consultas independientes de orden ≤d'+1. La cota de orden puede ser necesaria: si S\{0}={e₁,…,e_d,e₁+⋯+e_d}, la única dependencia no trivial tiene longitud d+1. Cuando S es un subespacio completo, las dependencias triples bastan. La fase IX sobre Q48 es un ejemplo con s=511, d'=9 y rango 502.

En Z_n, con soporte {0,±1}, una señal C+A cos(2πx/n+θ) presenta la misma información de orden <n para toda θ, si n≥4. El orden n fija nθ y resuelve la ambigüedad salvo traslación. Puede elegirse C>|A| para que la señal sea positiva. Por tanto no existe un principio de suficiencia triádica universal, incluso para señales no negativas.

## 7. Comprobación exacta de orden mínimo en Z12

Sobre los 22 patrones de soporte espectral de los 4096 indicadores originales, se admiten todas las señales reales compatibles (con DC fijado). Se construyen retículos de relaciones de orden creciente en aritmética ciclotómica y se verifica su índice por Smith. Resultados: 2 configuraciones constantes (orden 1), 2 de período dos (orden 2), 3830 (orden 3), 262 (orden 4). En los 262 casos no basta el biespectro, pero el cuarto orden sí elimina la ambigüedad. Por tanto orden 4 es suficiente para todas las magnitudes originadas por indicadores de Z12, incluso en el espacio real ambiente. Esto no significa que orden 4 sea necesario para todos los indicadores: con el prior binario, la fase IX dejó solo una pareja de clases ambigua a orden 3.

## 8. Bibliografía, alcance y siguientes pasos

La reconstrucción por autocorrelaciones, el biespectro y los límites de orden son temas consolidados y activos. Trabajos pertinentes:

- W. R. Casper y B. Orozco, *Reconstructing rational functions on finite Abelian groups with higher autocorrelations*, DOI 10.1016/j.acha.2026.101908 (disponible en 2026; volumen fechado 2027), https://arxiv.org/abs/2503.21022 . Cotas para señales racionales, con hipótesis distintas de las del caso real general.
- A. Agulnick y T. Busick-Warner, *Higher-Order Autocorrelations on Finite Abelian Groups*, preprint 14 de abril de 2026, https://arxiv.org/abs/2604.13310 . Trata explícitamente soporte espectral, órdenes de correlación y contraejemplos.
- A. S. Bandeira et al., *Estimation under group actions: Recovering orbits from invariants*, Applied and Computational Harmonic Analysis, https://www.sciencedirect.com/science/article/pii/S1063520323000465 .
- J. Rosenblatt y P. D. Seymour, *The Structure of Homometric Sets*, https://doi.org/10.1137/0603035 .
- C. Carlet y S. Mesnager, *Four decades of research on bent functions* (2016), y las referencias de OEIS A004491.

Próxima prueba: caracterizar soportes que requieren orden alto y diseñar un protocolo de observación robusto al ruido. Comparar la selección adaptativa por reducción de ambigüedad con referencias simples (observaciones aleatorias, fijas, estimación de información), tanto en conjuntos binarios como en un canal cuántico con orientación desconocida. No asumir un beneficio semántico o musical sin validación independiente.

## Reproducir

Python ≥3.10, SymPy para la forma normal de Smith. Ejecutar `python rgo_fase10_audit.py > rgo_fase10_results.json`. La auditoría enumera Q12, verifica la fórmula de Cubo64, el cociente bent, las 8008 combinaciones de seis elementos, los mínimos fijos y adaptativos, los signos de las coherencias de dos copias y el orden mínimo de Z12. Los resultados son exactos. No se ha actualizado GitHub.
