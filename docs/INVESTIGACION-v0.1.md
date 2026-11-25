# Geometría relacional y observabilidad

**Sergi Garcia Mecinas · Cuaderno de investigación v0.1 · 25 de noviembre de 2026**

*De la dualidad binaria a la música, la geometría discreta y la observación cuántica.*

## Resumen ejecutivo

¿Puede una misma estructura matemática ayudar a estudiar fenómenos aparentemente distintos, como la organización de una composición musical, la estabilidad de una red semántica y la información accesible mediante una medición cuántica? El presente proyecto no presupone que sean el mismo fenómeno. Busca un lenguaje común: **estado, relación, transformación y observación**.

Se estudia un espacio finito de 4096 configuraciones de doce signos. Al exigir equilibrio en tres bloques y ortogonalidad mutua, aparecen exactamente 48 configuraciones. Una codificación modular permite interpretarlas como conjuntos de seis clases de altura de la escala cromática; se conservan transposición, inversión y complementación. Los estados pertenecen a cuatro clases musicales de Forte, agrupadas en dos perfiles interválicos. Sobre el mismo espacio se construyen un campo de distancias, una penalización con mínimos locales y un Hamiltoniano cuántico. Se cuantifica además cuánta información revela cada operador de observación y se demuestra por qué una medida de coherencia basada en semejanza entre perspectivas no puede confundirse con la capacidad de distinguirlas.

La evidencia musical es exploratoria: el análisis de 382 corales de Bach no muestra una sobrerrepresentación concluyente de coincidencias exactas con los 48 estados. La proximidad media a ellos sí supera una referencia uniforme condicionada por cardinalidad, pero gran parte de esa diferencia se explica al controlar la diatonicidad. No se ha demostrado una ley universal de equilibrio, una ventaja cuántica, ni una teoría de la consciencia. El valor actual está en un conjunto de correspondencias explícitas, resultados reproducibles y preguntas falsables.

**Cómo leer este informe.** Un resultado **exacto** se deduce de definiciones y/o se ha verificado exhaustivamente en un espacio finito; un resultado **numérico** depende de una simulación; un resultado **empírico** depende de datos y protocolo; una **hipótesis** requiere validación. Una analogía filosófica no constituye una demostración física.

## 1. Punto de partida: por qué estudiar relaciones

En una descripción elemental, un objeto puede tener dos valores: presencia/ausencia, 0/1 o −1/+1. Elegir una de estas codificaciones es una decisión de modelado. La existencia de oposiciones en matemáticas no demuestra que toda propiedad del mundo sea binaria. Lo interesante es estudiar qué estructuras se obtienen al relacionar varias variables binarias mediante reglas explícitas.

La **cualidad** designará aquí la configuración y el tipo de relación, mientras que la **cantidad** será una magnitud calculada sobre ella. Ejemplo: dos conjuntos de seis notas tienen la misma cardinalidad, pero pueden contener intervalos distintos. Del mismo modo, dos distribuciones pueden tener idéntico espectro de potencia y distinta fase. Un número aislado no siempre determina el objeto observado.

Llamaremos **estado** a una configuración x de un espacio X; **relación** a una función o regla entre estados o componentes (distancia, producto interno, arista); **transformación** a una operación sobre ese espacio; y **observación** a una función, distribución o medición que revela determinadas propiedades del estado. La geometría dependerá de las relaciones elegidas, no de un dibujo impuesto de antemano.

## 2. De una pregunta musical a una investigación común

El trabajo comenzó con un armonógrafo audiovisual: ¿pueden las proporciones de frecuencia generar figuras? Si dos señales son x(t)=sin(2π f₁t+φ₁) e y(t)=sin(2π f₂t+φ₂), su trayectoria es una curva de Lissajous. Con tres señales reales independientes se obtiene una trayectoria espacial, sin necesidad de añadir un eje ficticio. Si fᵢ=nᵢf₀ y los enteros nᵢ tienen máximo común divisor 1, la trayectoria completa se repite tras T=1/f₀. La fase puede modificar la figura manteniendo las frecuencias; cambiar conjuntamente las frecuencias por un mismo factor cambia el período, no el lugar geométrico de un ciclo. Por ejemplo, 220, 275 y 330 Hz (4:5:6) tienen período común 1/55 s. Durante este período las tres sinusoides de frecuencias distintas son ortogonales en el producto interno integral. Este resultado es de análisis de Fourier, no una nueva ley musical ni una equivalencia con Q48.

El primer prototipo, Armonógrafo 3D, dio paso a RESONANTIA y después a CONSONA: se retiraron coordenadas decorativas y se priorizaron señales, frecuencias, fases y matrices de Gram. Estos laboratorios estudiaban tonos ideales, no la identidad de canciones completas, ni la propagación física de vibraciones en placas. La cuestión siguiente fue si existe una geometría de la estructura musical que permanezca al cambiar instrumento, tonalidad o velocidad.

### Antecedentes externos

| Trabajo | Qué estudia | Puente con este proyecto |
|---|---|---|
| Foote (1999) [1] | Matriz de autosimilitud entre instantes de audio. | Comparar relaciones temporales de una secuencia de estados. |
| Tymoczko (2006, 2012) [2–3] | Espacios de acordes, simetrías y conducción de voces; Tonnetze generalizados. | Definir distancias musicalmente motivadas y grafos de transformaciones. |
| Forte (1973), Babbitt y Lewin (1960) [4–5] | Conjuntos de clases de altura, contenido interválico y complementación. | Clasificar los hexacordos obtenidos de Q48. |
| Bergomi, Baraté y Di Fabio (2016) [6] | Huellas topológicas a partir del Tonnetz. | Estudiar complejos simpliciales y persistencia. |
| Yust (2020) [7] | Tonnetze, espacios de fase de Fourier y topología. | Conectar representaciones musicales geométricas y espectrales. |
| Callet-Feltz (2025) [8] | Fourier discreta y homología persistente aplicadas a datos musicales simbólicos. | Comparar invariantes y distancias sin confundirlas con las propias. |

En el espacio continuo de Tymoczko, identificar alturas separadas por octavas produce el círculo ℝ/12ℤ; identificar permutaciones en acordes de n voces produce el cociente de un toro por el grupo Sₙ. Nuestro modelo es discreto, binario y no conserva ni registro ni multiplicidad de notas. No es ese orbifold. Foote parte de audio; Q12 utiliza clases de altura simbólicas. La distancia euclídea, la conducción de voces, Hamming y las métricas sobre coeficientes de Fourier responden a preguntas diferentes. La conexión es metodológica y algebraica, no una identificación automática de todas estas geometrías.

## 3. Construcción matemática de Q12 y Q48 [exacto]

Sea X={−1,+1}¹², con 2¹²=4096 estados. Se organizan los signos en una matriz A de tres filas a,b,c y cuatro columnas. La familia Q48 se define por dos restricciones:

- Equilibrio: Σaᵢ=Σbᵢ=Σcᵢ=0.
- Ortogonalidad: a·b=b·c=c·a=0, con el producto interno usual.

Cada fila equilibrada tiene dos signos de cada tipo. Hay C(4,2)=6 filas posibles, que son los pares opuestos de tres vectores mutuamente ortogonales:

```text
u = (+ + − −)    v = (+ − + −)    w = (+ − − +)
```

En una tríada ortogonal cada dirección se usa una vez; podemos permutarlas de 3!=6 maneras y elegir sus tres signos independientemente de 2³=8 maneras. **Resultado: 48 estados ordenados.** Si se añade como primera fila (+,+,+,+), se obtiene una matriz de Hadamard de orden 4. Los 48 estados admiten una identificación con el grupo hiperoctaédrico B₃ (permutaciones con signo), cuyo conjunto subyacente se puede etiquetar por {−1,+1}³ × S₃. La multiplicación es un producto semidirecto, no necesariamente un producto directo de grupos. El grafo de Cayley de la Tríada Emergente con su conjunto de generadores particular es Q₃ □ K₃,₃; no debe confundirse con los grafos definidos aquí por otras distancias.

Sin exigir ortogonalidad hay 6³=216 configuraciones con filas equilibradas. La complementación C(x)=−x preserva ambas restricciones. Cada estado perfecto tiene seis signos positivos y seis negativos. Q48 se divide en 24 pares antipodales, ninguno fijo bajo complementación.

## 4. El puente con las doce clases de altura [exacto]

Una clase de altura identifica notas que difieren por una o varias octavas. En la escala cromática de doce semitonos, se codifica Do=0, Do♯=1, …, Si=11. Para un conjunto A de clases de altura, se asigna +1 a cada nota presente y −1 a cada nota ausente. El espacio de todos los conjuntos posibles es isomorfo, como espacio binario, a X. No se conservan duplicaciones de voces, octavas, duración ni dinámica.

La asignación de notas a los bloques es esencial. El teorema chino del resto da ℤ₁₂ ≅ ℤ₃ × ℤ₄ mediante n ↦ (n mod 3,n mod 4). La tabla resultante es:

| Fila / columna | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| 0 | 0 | 9 | 6 | 3 |
| 1 | 4 | 1 | 10 | 7 |
| 2 | 8 | 5 | 2 | 11 |

Una transposición n↦n+t permuta cíclicamente filas y columnas; la inversión musical n↦−n+t también actúa mediante permutaciones. Las sumas de fila y productos internos se conservan. La inversión de todas las presencias/ausencias es una operación distinta: la **complementación**. Con esta codificación, los 48 estados son invariantes como conjunto bajo las doce transposiciones, las inversiones y la complementación. La elección modular no es una equivalencia con cualquier agrupación arbitraria de doce bits.

### Cuatro familias y dos perfiles

Para un conjunto de seis clases de altura (hexacordo), el vector interválico cuenta los pares de notas a distancias circulares mínimas 1,2,3,4,5,6. Cada vector suma C(6,2)=15. Clasificando Q48 por transposición e inversión se obtienen cuatro órbitas, de 12 estados cada una. Los representantes siguientes no necesitan ser la forma prima canónica de cada clase; los identificadores de Forte se emplean como etiquetas musicales establecidas.

| Clase | Representante | Vector interválico |
|---|---|---|
| 6-Z37 | 0,1,2,3,4,8 | (4,3,2,3,2,1) |
| 6-Z4 | 0,1,2,4,5,6 | (4,3,2,3,2,1) |
| 6-Z48 | 0,1,2,5,7,9 | (2,3,2,3,4,1) |
| 6-Z26 | 0,1,3,5,7,8 | (2,3,2,3,4,1) |

Las clases 6-Z37/6-Z4 y 6-Z48/6-Z26 son parejas complementarias; comparten contenido interválico aunque no son equivalentes por transposición e inversión. La complementación C y la multiplicación modular M₅:n↦5n mod 12 conmutan y son involuciones. Sobre las cuatro clases forman una acción regular del grupo de Klein V₄. M₅ conecta 6-Z37 con 6-Z48 y 6-Z4 con 6-Z26.

**Verificación inversa:** entre los 924 hexacordos posibles, exactamente 48 tienen uno de estos dos vectores interválicos; son los mismos que genera la construcción triádica. La auditoría enumera ambos conjuntos y comprueba igualdad. Esto establece una caracterización equivalente, sin afirmar que las cuatro clases musicales o la teoría Z sean inéditas.

### Fourier y dualidad

Con f_A(n)=1 si n∈A y 0 en otro caso, definimos F_A(k)=Σₙ f_A(n) exp(−2πikn/12). La magnitud al cuadrado es la transformada de la autocorrelación circular. El teorema de los hexacordos de Babbitt explica la igualdad de contenido interválico de complementarios de cardinalidad seis. En efecto, F_{Aᶜ}(k)=−F_A(k) para k≠0 y F_{Aᶜ}(0)=F_A(0)=6.

| Componente k | Perfil 6-Z37/6-Z4 | Perfil 6-Z48/6-Z26 |
|---:|---:|---:|
| 1 | 4+2√3 | 4−2√3 |
| 2 | 4 | 4 |
| 3 | 4 | 4 |
| 4 | 0 | 0 |
| 5 | 4−2√3 | 4+2√3 |
| 6 | 4 | 4 |

Se muestran potencias de la función indicadora, no amplitudes de una grabación. Por simetría de conjugación se obtienen las restantes componentes; k=0 tiene potencia 36. Para los signos x=2f_A−1, las potencias no nulas se multiplican por 4 y el componente DC es 0. La DFT unitaria preserva productos internos y distancias euclídeas (Parseval); sus magnitudes sin fase no son una transformación inyectiva. La transformada de Walsh–Hadamard sobre el hipercubo y la DFT sobre ℤ₁₂ pertenecen a grupos distintos. No se identifican entre sí sin una aplicación explícita.

## 5. Geometría de los 48 estados [exacto]

La distancia de Hamming d_H(x,y) cuenta coordenadas diferentes. Para signos, x·y=12−2d_H(x,y). El producto interno normalizado S=x·y/12=1−d_H/6 es un coseno de similitud. Una composición representada como secuencia binaria x₁,…,xₘ permite construir la matriz Sᵢⱼ; es una autosimilitud de tipo Foote sobre estas características concretas. Un valor −1 significa complementación completa, no necesariamente oposición perceptiva musical.

| Distancia desde cualquier q∈Q48 | 0 | 4 | 6 | 8 | 12 |
|---|---:|---:|---:|---:|---:|
| Número de estados | 1 | 15 | 16 | 15 | 1 |

Si se conecta exclusivamente d_H=6, el grafo es K₈,₈,₈ ⊔ K₈,₈,₈: dos componentes de 24 vértices asociadas a paridad de la permutación. Dentro de cada componente existen tres grupos de ocho signos y todas las conexiones entre grupos. No es el mismo grafo que el Cayley de la Tríada Emergente.

Con X como matriz de 48×12 que contiene los estados (columnas agrupadas por filas CRT), XᵀX tiene tres bloques diagonales 16(4I₄−J₄) y ceros entre bloques. Su espectro es 64 con multiplicidad 9 y 0 con multiplicidad 3. Los estados abarcan el subespacio de nueve dimensiones de sumas de fila nulas y forman un marco ajustado (tight frame) en él. Esta propiedad puede ser útil como conjunto de referencias, pero aún no se ha demostrado una aplicación musical superior a otras bases.

### Topología por umbrales

Un complejo de Vietoris–Rips incorpora una arista cuando dos puntos están a distancia ≤r y un símplice cuando todos sus pares satisfacen esa condición. Con distancia Hamming, se calcularon los rangos de matrices de frontera sobre 𝔽₂.

| r | β₀ (componentes) | β₁ (ciclos) | β₂ (clases de 2-ciclos) |
|---:|---:|---:|---:|
| 0 | 48 | 0 | 0 |
| 4 | 1 | 13 | 6 |
| 6 | 1 | 0 | 0 |
| 8 | 1 | 0 | 0 |
| 12 | 1 | 0 | 0 |

Al umbral 8 solo faltan las 24 aristas entre complementarios. El complejo es el join de 24 pares de puntos (S⁰), es decir, la frontera combinatoria del politopo cruzado de dimensión 24, homeomorfa a S²³. Tiene β₂₃=1, que desaparece al umbral 12, donde se obtiene el símplice completo. No se afirma que el espacio de estados posea 24 dimensiones lineales físicas: se trata de la dimensión del complejo abstracto. En los umbrales 4 y 6 se calcularon únicamente β₀, β₁ y β₂; no se han caracterizado todas las dimensiones superiores. La homología no distingue necesariamente todos los objetos que la comparten.

### Distancias musicales y escalas

Se calculó la mínima asignación de voces con coste circular L¹ (suma de distancias de semitonos), inspirada en geometrías de conducción de voces. Para coste ≤2, Q48 induce seis ciclos de cuatro estados y 24 vértices aislados. Por ello no es una red conexa de transiciones musicales próximas. Restringir toda la música a Q48 sería arbitrario.

De los 72 hexacordos distintos extraíbles de escalas diatónicas (considerando transposiciones), 12 pertenecen a Q48, todos a 6-Z26. No hubo coincidencias con los subconjuntos estudiados de escalas menor armónica, menor melódica, octatónica ni de tonos enteros, incluyendo sus inversiones. Los resultados dependen de estas definiciones de escala, no son una clasificación universal de músicas.

| Familia | Tríadas mayores contenidas | Menores | Disminuidas | Aumentadas |
|---|---:|---:|---:|---:|
| 6-Z37 | 1 | 1 | 0 | 1 |
| 6-Z4 | 0 | 0 | 0 | 0 |
| 6-Z48 | 1 | 1 | 0 | 1 |
| 6-Z26 | 2 | 2 | 0 | 0 |

Esto diferencia conjuntos con idéntico perfil interválico: una observación que retiene solamente ese perfil no ve la organización específica de tríadas.

## 6. Primera comprobación en música real [empírico]

Se utilizó JSB Chorales [9], 382 secuencias de corales de Bach (229 train, 76 valid y 77 test; total 23.134 posiciones de negra). La representación recoge números de nota MIDI en instantes discretos y no conserva de forma explícita fermatas, ataques frente a notas sostenidas, ritmo detallado ni identificación de cada voz. El blob de Git utilizado es `ff93746647d1f5af2f719d235329c294267f3088`, archivo `jsb-chorales-quarter.json`. No se requiere acceso a una grabación.

En cada ventana deslizante de w negras, se toma la unión de clases de altura de sus posiciones y se comprueba si coincide con Q48. Una ventana no es necesariamente un acorde simultáneo ni un compás. Las ventanas consecutivas se solapan, de modo que no se pueden tratar como observaciones independientes.

| w (negras) | Ventanas | Con 6 clases | Q48 exactos | Proporción entre hexacordos |
|---:|---:|---:|---:|---:|
| 1 | 23.134 | 0 | 0 | — |
| 2 | 22.752 | 5.036 | 193 | 3,83 % |
| 4 | 21.988 | 5.480 | 291 | 5,31 % |
| 8 | 20.460 | 1.393 | 84 | 6,03 % |
| 16 | 17.404 | 138 | 0 | 0 % |

Todas las coincidencias corresponden a 6-Z26. Para cuatro negras, 120 composiciones tienen al menos una coincidencia. El azar uniforme entre 924 hexacordos da 48/924=5,19 %. Un control de permutación aplica una misma permutación aleatoria de las doce clases a todas las ventanas de una composición; conserva cardinalidad, solapamiento y patrones temporales de identidad, pero destruye relaciones tonales específicas. En 199 réplicas, las medias de coincidencias fueron 283,75 (w=4) y 72,47 (w=8); p unilateral Monte Carlo =0,415 y 0,295 respectivamente. **No hay evidencia concluyente de enriquecimiento de coincidencias exactas en estas pruebas.**

### Campo de distancia al equilibrio

En lugar de exigir coincidencia, se define E(x)=min_{q∈Q48} d_H(x,q). Es un entero entre 0 y 6 y cumple E(−x)=E(x). Su histograma completo es:

| E | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Estados | 48 | 576 | 1440 | 1376 | 552 | 96 | 8 |

El número de clases activas influye en E. Se controla primero comparando cada ventana con todos los estados del mismo número k de notas. Después se controla además una medida simple de diatonicidad, m(x)=mínimo número de notas de x fuera de cualquier escala mayor transportada. Para cada par (k,m) se calcula la media uniforme exacta de E en el estrato. Los residuos negativos significan proximidad mayor que la referencia; los positivos, menor.

| Ventana | Media E real | Residuo condicionado por k | Residuo condicionado por (k,m) |
|---|---:|---:|---:|
| 2 | 2,1770 | −0,3487 | −0,1735 |
| 4 | 1,8023 | −0,5773 | −0,0544 |
| 8 | 2,0433 | −0,5560 | +0,0707 |

El efecto inicial de w=4 equivale a una reducción aproximada del 24 % frente a la referencia por cardinalidad. En 199 permutaciones por composición, ninguna reprodujo una media por pieza tan negativa para w=2,4,8 (p Monte Carlo=0,005 por condición, sin ajuste de comparaciones). Pero el control por diatonicidad reduce mucho el efecto y cambia su signo para w=8. No es una prueba de que exista una propiedad adicional independiente de la tonalidad. Ese control es descriptivo y no es un modelo tonal completo ni una prueba inferencial del residuo. Se observó además que la última ventana no tiene menor residuo medio que el resto; las diferencias finales fueron positivas (+0,243, +0,096, +0,223 para w=2,4,8). No se han identificado cadencias, por lo que no se puede concluir sobre resolución musical en general.

**Interpretación:** en Bach aparece una relación medible entre Q48 y organización tonal, no evidencia de que la música busque una energía matemática mínima universal. Queda por evaluar otros estilos, controles de conducción de voces, ventanas no solapadas, métricas alternativas y datos independientes. El corpus no se redistribuye; `results/bach_recorded.json` registra los valores de la ejecución sobre el conector de GitHub. Los scripts permiten repetirla al obtener el archivo original.

## 7. Una energía relacional y sus falsos equilibrios [exacto]

Para cada estado se distinguen dos componentes: balance interno B=(Σaᵢ)²+(Σbᵢ)²+(Σcᵢ)² y falta de ortogonalidad O=(a·b)²+(b·c)²+(c·a)². Se define H=B+O. Ambas son no negativas y H=0 exactamente en Q48. No es una energía física (no se expresa en julios); es una penalización adimensional definida por nosotros.

| H | 0 | 12 | 16 | 28 | 32 | 48 | 60 | 96 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Multiplicidad | 48 | 768 | 1152 | 1152 | 648 | 192 | 128 | 8 |

Se declara vecindad por cambio de un solo signo. Un mínimo local estricto tiene H menor que la de todos sus 12 vecinos. La enumeración produce 240 mínimos locales estrictos: 48 globales y 192 no globales. Todos los no globales tienen B=12, O=0, H=12 y E=3. Cada uno tiene un vecino de energía 16 y ninguno de energía menor o igual a 12. En el subgrafo de H≤16 todos alcanzan algún mínimo global. Por tanto, la barrera minimax desde cada trampa hasta Q48 es exactamente 4 unidades. Un camino real es 12→16→12→0 (máscaras 7→71→103→119 con codificación cromática y orden CRT).

```text
Equilibrio global          Mínimo local no global
+ + − −                    + + − +
+ − + −                    + − + +
+ − − +                    − + + +
B=0  O=0  H=0             B=12 O=0  H=12
```

Ambos tienen ortogonalidad perfecta. La observación de O no distingue los estados de sus respectivas clases; B sí lo hace. El resultado muestra un fallo concreto de una observación parcial y una dificultad de optimización local. Depende de la función H y de la regla de movimiento; no demuestra una ley psicológica o física de que todo equilibrio requiera desequilibrio previo.

## 8. Construcción cuántica [exacto y numérico]

Un registro de doce qubits tiene 4096 vectores de base computacional |x⟩. Su estado general es una superposición Σₓαₓ|x⟩, con Σₓ|αₓ|²=1. El espacio de amplitudes es complejo y no debe confundirse con el conjunto clásico de 4096 estados. La regla de Born proporciona probabilidades |αₓ|² al medir en esa base.

El operador diagonal Ĥ=Σₓ H(x)|x⟩⟨x| es un Hamiltoniano matemático de optimización cuyo subespacio fundamental tiene dimensión 48. Sustituyendo cada signo por un operador de Pauli Z correspondiente (con la convención de signo ajustada a la codificación), se obtiene una expresión diagonal de interacciones de hasta cuarto orden. Se añade un campo transversal: Ĥγ=Ĥ−γΣᵢXᵢ, donde Xᵢ invierte el bit i. La matriz es real simétrica de 4096×4096 con una estructura dispersa. Se calcularon estados fundamentales estáticos con `eigsh` de SciPy, tolerancia 1e−10 y residuo verificado.

| γ | Energía fundamental | P(Q48) en la base computacional |
|---:|---:|---:|
| 0,5 | −0,260941 | 97,6766 % |
| 1 | −1,200840 | 87,1160 % |
| 3 | −17,272238 | 11,4682 % |
| 6 | −51,167868 | 4,0060 % |
| 12 | −121,826095 | 2,2703 % |

El modelo concentra probabilidad en Q48 cuando disminuye γ en las condiciones simuladas. En γ=0, cualquier vector del subespacio fundamental tiene P(Q48)=1; eso no dice qué amplitudes o fases lo componen. No se ha simulado una trayectoria de recocido con tiempos definidos, ni la brecha mínima a lo largo de un protocolo, ni hardware real. No es evidencia de aceleración respecto de métodos clásicos, ni demuestra que la realidad física se rija por este Hamiltoniano.

### Orientación y relaciones: un qubit lógico

Definimos s=x₀ y rᵢ=x₀xᵢ para i=1,…,11. La transformación es biyectiva: xᵢ=srᵢ. Al complementar x, cambia s pero todos los rᵢ permanecen. En la base binaria esto se implementa con once CNOT cuyo control es el bit 0. Por la permutación de bases, ℂ⁴⁰⁹⁶≅ℂ²⊗ℂ²⁰⁴⁸. Como Q48 es cerrado bajo complementación, su subespacio de base se identifica con ℂ²⊗ℂ²⁴. La complementación global X⊗¹² actúa como X sobre el qubit lógico de orientación y la identidad sobre el factor relacional. Esta factorización no implica que toda preparación sea un producto separable de ambos factores.

Si q y q̄ son complementarios, los estados (|q⟩±|q̄⟩)/√2 y la mezcla clásica equiprobable de ambos producen las mismas probabilidades al medir en Z. Al medir el operador global de complementación X⊗¹², las dos superposiciones tienen resultados +1 y −1 deterministas, mientras la mezcla tiene probabilidades 1/2 y 1/2. La fase relativa es observable mediante esta medición; la fase global de un estado cuántico no lo es. Esto es un ejemplo estándar de coherencia y distinguibilidad cuánticas aplicado a Q48, no una explicación de consciencia ni una equivalencia física con la homometría musical.

## 9. Observadores como particiones de estados [exacto]

Para una observación determinista O:X→Y, definimos x∼_O y si O(x)=O(y). Sus clases de equivalencia forman una partición de X. El número de clases no coincide necesariamente con los bits de información: si los estados tienen prior uniforme, la entropía de las clases depende de sus tamaños. La observación completa distingue todos los estados; una observación parcial puede agruparlos.

| Observación | Clases sobre Q12 | Clases sobre Q48 |
|---|---:|---:|
| Cardinalidad de signos positivos | 13 | 1 |
| B | 10 | 1 |
| O | 5 | 1 |
| Par (B,O) | 18 | 1 |
| Sumas de filas y productos internos de filas | 329 | 1 |
| Potencias DFT (autocorrelación circular) | 118 | 2 |
| Once productos relativos a un signo de referencia | 2048 | 24 |
| Los doce signos | 4096 | 48 |

**Los mismos 48 estados aparecen como una, dos, veinticuatro o cuarenta y ocho clases según el operador.** No son cuatro realidades físicas diferentes, sino cuatro particiones de un mismo conjunto. En Q48, una observación de magnitudes de Fourier transmite exactamente un bit (dos clases de tamaño 24), y la observación relacional transmite log₂24 bits. La orientación resta un bit.

### Reconstrucción mínima

Se limitan las preguntas a signos individuales para estados completos y a productos binarios de dos signos para pares complementarios. Una estrategia fija elige todas sus preguntas de antemano. Una estrategia adaptativa elige la siguiente pregunta según las respuestas anteriores; se mide la profundidad máxima (peor caso).

| Universo de hipótesis | Mínimo fijo | Mínimo adaptativo |
|---|---:|---:|
| 4096 estados | 12 | 12 |
| 2048 pares complementarios | 11 | 11 |
| 48 estados | 7 | 6 |
| 24 pares complementarios perfectos | 6 | 5 |

Para Q48 se enumeraron las C(12,6)=924 selecciones de seis coordenadas: ninguna distingue más de 40 estados; 480 selecciones de siete sí distinguen los 48. Para los 24 pares se buscaron subconjuntos de las 66 posibles preguntas de producto y se descartó una separación fija de cinco; se encontró una de seis. El algoritmo adaptativo construye árboles de decisiones de profundidad 6 y 5, respectivamente; los límites inferiores ⌈log₂48⌉ y ⌈log₂24⌉ demuestran optimalidad en peor caso. El prior de pertenencia a Q48 es esencial. No significa que una sola copia de un estado cuántico arbitrario pueda tomografiarse con esas preguntas; esto es identificación de configuraciones clásicas entre un conjunto finito conocido.

## 10. Coherencia, difusión y pérdida de observabilidad [exacto y numérico]

Una investigación anterior sobre grafos semánticos [13] definió perspectivas φ por parejas de polos y campos PPR πφ=(π_A+π_B)/2. La métrica C=1−media JSD(πφᵢ,πφⱼ) usa divergencia de Jensen–Shannon con logaritmos en base 2 para las parejas distintas. Un valor alto indica similitud entre campos. Se estudiaban además dominancia, fragmentación y estabilidad porque un colapso hacia un nodo popular puede ser aparentemente coherente.

En este proyecto se abstrae esa idea: el grafo es el hipercubo Q12 no dirigido, con transición uniforme entre doce vecinos. Las 24 perspectivas se obtienen reiniciando uniformemente en los dos vértices de cada par complementario de Q48. PPR utiliza α como probabilidad de continuar el paseo y 1−α de reiniciar. Se define la variable Φ con prior uniforme sobre las perspectivas, y Y como un único vértice muestreado de πφ. La información mutua es I(Φ;Y)=H(Y)−H(Y|Φ); aquí H denota entropía de Shannon, no la penalización de la sección 7. La probabilidad óptima de acertar la perspectiva con una sola muestra es (1/24)Σ_y max_φ πφ(y).

| α | C | I(Φ;Y) en bits | I/log₂24 | Acierto óptimo |
|---:|---:|---:|---:|---:|
| 0 | 0,000000 | 4,584963 | 100 % | 100 % |
| 0,5 | 0,076291 | 3,924433 | 85,59 % | 84,43 % |
| 0,85 | 0,562210 | 1,567969 | 34,20 % | 41,57 % |
| 0,95 | 0,862985 | 0,444339 | 9,69 % | 18,76 % |
| 0,99 | 0,982598 | 0,049877 | 1,09 % | 7,30 % |
| 0,999 | 0,999414 | 0,001332 | 0,029 % | 4,48 % |

El azar uniforme de identificación es 1/24=4,17 %. A α=0,999, los campos siguen siendo distintos si se conocen con precisión infinita, pero una muestra proporciona una información despreciable. La coherencia calculada no es idéntica a la coherencia cuántica, ni a la verdad semántica. Se trata de una medida de semejanza estadística entre campos.

### Por qué sucede: deducción general por procesamiento de datos

Sea P una matriz estocástica de transición y Kα=(1−α)(I−αP)⁻¹ el núcleo de reinicio (convención de vectores fila). Para 0≤α<β<1,

```text
Kβ = Kα Lα,β
Lα,β = [(1−β)/(1−α)] [I + (β−α) P (I−βP)⁻¹]
```

La serie geométrica del inverso demuestra que L tiene entradas no negativas; sus filas suman 1. Por tanto, pasar de Kα a Kβ equivale a aplicar un canal estocástico común adicional. Por la desigualdad de procesamiento de datos, la divergencia de Jensen–Shannon entre dos campos no aumenta; la información mutua entre la perspectiva de origen y una muestra tampoco aumenta. En un grafo finito irreducible, al tender α a 1 las distribuciones PPR convergen a la estacionaria y el origen se vuelve indistinguible en ese límite. La inversión del núcleo para α<1 explica por qué dos distribuciones iniciales distintas no se vuelven exactamente iguales con aritmética ideal.

Asimismo, si μ es la media de los campos, la información mutua es la divergencia Jensen–Shannon generalizada H(μ)−media H(πφ). La concavidad de la entropía da media JSD de pares ≤ I(Φ;Y) en bits. El incremento de C y la caída de I en la tabla no constituyen una casualidad de Q12: son coherentes con estas propiedades generales de la difusión. Se presenta esta deducción como una aplicación de resultados conocidos de teoría de la información y cadenas de Markov; su originalidad bibliográfica no ha sido establecida.

### Reformulación de la auditoría

Es incorrecto perseguir simultáneamente C≈1 y una identificación perfecta de las **mismas** perspectivas cuando C mide su indistinguibilidad. Para un sistema útil hay que definir cuáles diferencias se desean preservar y cuáles ignorar. Se propone distinguir una variable objetivo T (contenido relevante para la tarea) de una perturbación N (perspectiva irrelevante respecto a ese objetivo). El objetivo es alta I(T;Y) y baja I(N;Y|T), junto con medidas de error y robustez. Ejemplo: en música puede interesar identificar la composición T ignorando transposición o instrumento N, siempre que estén definidos los cambios que preservan identidad. En semántica, diferenciar cambios conceptuales reales de simples reformulaciones. En cuántica, reconstruir las propiedades que requiere una tarea mediante observables adecuados. Esta reformulación es una agenda de trabajo; no se ha validado aún sobre los grafos originales ni sobre hardware.

## 11. Qué aportan los trabajos anteriores del autor

No es necesario haber leído estos repositorios para reproducir los resultados aquí, pero explican la genealogía del problema:

| Proyecto | Aportación previa | Conexión actual y límite |
|---|---|---|
| IA_m / [Semantic Diffraction in Conceptual Graphs](https://github.com/sgarcia87/Semantic-Diffraction-in-Conceptual-Graphs) [12] | Equilibrio estructural entre dos polos en grafos, PPR y penalización de asimetría: s(n)=p_A(n)+p_B(n)−λ|p_A(n)−p_B(n)|. | Posible búsqueda de intermediarios musicales; no se ha validado en corpus. No es interferencia cuántica de amplitudes complejas. |
| [Structural-Coherence-Audit](https://github.com/sgarcia87/Structural-Coherence-Audit) [13] | Coherencia entre campos de distintas perspectivas; riesgo de colapso estructural. | Se ha trasladado C al hipercubo y se ha añadido información mutua. No es una reproducción del grafo semántico original. |
| [Tríada Emergente](https://github.com/sgarcia87/Triada-emergente) [14] | Vectores equilibrados y ortogonales, Hadamard, B₃ y grafo de Cayley. | Base exacta de Q48. |
| [Q-Reality-12D](https://github.com/sgarcia87/Q-Reality-12D) [15] | Experimentos con Qiskit y amplificación de amplitud en subconjuntos estructurados de 12 qubits; diferentes restricciones según experimento. | Se construye un Hamiltoniano para las restricciones particulares de Q48. No se asume que todos los experimentos previos emplearan esos mismos 48 estados. |
| [Cubo Mágico 64](https://github.com/sgarcia87/cubo-magico-64) [16] | Construcción algebraica sobre GF(4); retícula de 64 celdas, 12 planos mágicos de constante 64 y 72 de 76 líneas consideradas. | Interés compartido en simetrías e invariantes. Aún no se dispone de una equivalencia formal con Q12 musical. No es un cubo mágico normal perfecto. |

La auditoría anterior RIFD/FWRI investigaba fragilidad ante perturbaciones. Se propone recuperarla como medida complementaria, pero el presente paquete no contiene una reproducción ni una evaluación de esas métricas. La secuencia conceptual de IA_m (dualidad, equilibrio, síntesis y geometría) inspira las hipótesis, no sustituye las pruebas.

## 12. Marco de trabajo común: estado, relaciones y observación

El siguiente esquema es una propuesta de lenguaje de investigación, no una teoría unificada demostrada.

| Dominio | Estado | Relación | Observación |
|---|---|---|---|
| Matemática discreta | Vector de signos | Hamming, producto interno | B, O, autocorrelación |
| Música simbólica | Conjunto o secuencia de notas | Intervalos, voz líder, similitud | Croma, Fourier, matriz temporal, persistencia |
| Semántica | Nodo, grafo o campo | Aristas y propagación | PPR, divergencia, estabilidad |
| Cuántica | Vector o matriz de densidad | Productos internos, operadores | Distribuciones de medición, correlaciones |

El criterio de interés es una aplicación explícita que preserve relaciones determinadas, o un método que produzca predicciones contrastables. Un mismo número, una figura parecida o una metáfora común no bastan. La representación de un estado musical a través de Q12 es exacta bajo una codificación; su relevancia para el estilo o la percepción no se deduce de esa exactitud. La orientación lógica de Q48 se implementa en un espacio cuántico; eso no demuestra que la percepción humana emplee dicha estructura.

### Motivación filosófica

La intuición de partida considera la dualidad como base de diferenciación y la consciencia como aquello que percibe relaciones en el plano material. Aquí se conserva esa pregunta, pero se separa de las afirmaciones científicas: **no se ha establecido que toda realidad material se construya a partir de dualidades binarias, ni que la consciencia provoque el resultado de una medición cuántica**. En este modelo, el observador es un operador matemático o un canal, no necesariamente una mente consciente. La interdependencia cualidad/cantidad se interpreta como motivación: una magnitud está definida sobre alguna estructura y una descripción estructural admite distintas mediciones. No se demuestra que ambos conceptos sean ontológicamente inseparables.

## 13. Resultados, límites y siguiente programa

| Resultado | Grado de evidencia |
|---|---|
| Q48, invariancia CRT, cuatro familias y dos perfiles | Exacto, enumeración y deducción. |
| Grafo ortogonal, marco ajustado, homología indicada, barreras | Exacto para las definiciones especificadas. |
| Estados fundamentales de Ĥγ | Numérico, diagonalización dispersa reproducida. |
| Clases observables y mínimos de preguntas | Exacto en el universo y preguntas definidos. |
| PPR, C e información mutua | Cálculo reproducido; monotonía deducida de procesamiento de datos. |
| Bach | Exploratorio; resultado negativo para enriquecimiento exacto y efecto de distancia dependiente del control. |
| Unicidad de firma musical, beneficio de Q48 en audio | No demostrado. |
| Generalización útil a grafos semánticos y ventaja cuántica | Por validar. |
| Consciencia, realidad material y teoría unificada | Motivación filosófica, no conclusión empírica. |

Los siguientes experimentos deben definir antes de medir qué variable es relevante, qué transformaciones son irrelevantes y qué referencia constituye un competidor justo. Para música, usar corpus independientes y modelos tonales; para semántica, comparar con las métricas originales bajo perturbaciones controladas; para cuántica, evaluar protocolos dinámicos y costes; para geometría, buscar aplicaciones algebraicas explícitas entre los modelos. Véase [agenda de investigación](ROADMAP.md).

**Pregunta central:** ¿cómo conservar información estructural relevante utilizando un número mínimo de perspectivas, sin confundir estabilidad con pérdida de capacidad de distinguir estados?

## 14. Reproducción y trazabilidad

En el directorio `audits/` se encuentran las auditorías `music_geometry.py`, `energy.py`, `observability.py`, `bach_hexachords.py` y `bach_distance.py`. Las tres primeras han sido ejecutadas nuevamente al preparar esta versión. Los datos de Bach se calcularon anteriormente sobre el archivo JSON accesible mediante el conector de GitHub; esta versión conserva los resultados y scripts, pero no pudo repetir la ejecución local completa sobre el corpus por restricciones de descarga. El script de distancia se comprueba con datos sintéticos. Python 3.10+ es suficiente para las pruebas exactas; NumPy y SciPy se requieren solo para la diagonalización cuántica. El código y las salidas están en el paquete del repositorio.

Los visualizadores HTML de CONSONA, Q12 Música, Anatomía del equilibrio y El observador se preservan como laboratorios históricos. El informe y las auditorías tienen prioridad ante cualquier discrepancia. El proceso de investigación incluyó correcciones: el histograma de distancias fue corregido a 552 estados en E=4 y 96 en E=5; las clases topológicas de dimensión 2 no deben llamarse cavidades espaciales ordinarias; los valores de similitud de PPR no deben interpretarse como una medición universal de coherencia; el objetivo de alta coherencia y alta discriminabilidad requiere variables distintas.

## 15. Referencias y fuentes

1. Jonathan Foote (1999). *Visualizing Music and Audio using Self-Similarity*. ACM Multimedia. [DOI:10.1145/319463.319472](https://doi.org/10.1145/319463.319472).
2. Dmitri Tymoczko (2006). *The Geometry of Musical Chords*. Science 313, 72–74. [DOI:10.1126/science.1126287](https://doi.org/10.1126/science.1126287).
3. Dmitri Tymoczko (2012). *The Generalized Tonnetz*. Journal of Music Theory 56(1). [DOI:10.1215/00222909-1546958](https://doi.org/10.1215/00222909-1546958).
4. Allen Forte (1973). *The Structure of Atonal Music*. Yale University Press.
5. David Lewin (1960). *The Intervallic Content of a Collection of Notes, Intervallic Relations between a Collection of Notes and Its Complement: An Application to Schoenberg's Hexachordal Pieces*. Journal of Music Theory 4, 98–101. Contexto histórico: [A Primer for Atonal Set Theory](https://symposium.music.org/index.php?id=6887&option=com_content&view=article).
6. Mattia G. Bergomi, Adriano Baraté y Barbara Di Fabio (2016). *Towards a Topological Fingerprint of Music*. [arXiv:1602.00739](https://arxiv.org/abs/1602.00739).
7. Jason Yust (2020). *Generalized Tonnetze and Zeitnetze, and the Topology of Music Concepts*. Journal of Mathematics and Music 14(2), 170–203. [DOI:10.1080/17459737.2020.1725667](https://doi.org/10.1080/17459737.2020.1725667).
8. Victoria Callet-Feltz (2025). *Persistent Homology and Discrete Fourier Transform: An Application to Topological Musical Data Analysis*. Springer. [DOI:10.1007/978-3-031-82236-0](https://doi.org/10.1007/978-3-031-82236-0). [Tesis doctoral (2023)](https://victoriacallet.github.io/recherche/manuscrit_callet.pdf). El libro completo no fue accesible; se usaron referencias bibliográficas y material disponible.
9. Nicolas Boulanger-Lewandowski, Pascal Vincent y Yoshua Bengio (2012). *Modeling Temporal Dependencies in High-Dimensional Sequences: Application to Polyphonic Music Generation and Transcription*. ICML, 1159–1166. Datos: [JSB Chorales dataset](https://github.com/czhuang/JSB-Chorales-dataset).
10. Thomas M. Cover y Joy A. Thomas (2006). *Elements of Information Theory*, 2.ª ed., Wiley. Referencia general para entropía, información mutua y procesamiento de datos.
11. Michael A. Nielsen e Isaac L. Chuang (2010). *Quantum Computation and Quantum Information*, 10th anniversary ed., Cambridge University Press. Referencia general para medición, CNOT, estados y operadores.
12. Sergi Garcia Mecinas. [Semantic Diffraction in Conceptual Graphs](https://github.com/sgarcia87/Semantic-Diffraction-in-Conceptual-Graphs), documentación y código, 2026.
13. Sergi Garcia Mecinas (2026). *Detecting Structural Coherence Loss in Semantic Systems Under Perspective Shift*, preprint y [repositorio](https://github.com/sgarcia87/Structural-Coherence-Audit).
14. Sergi Garcia Mecinas (2026). [Estructuras triádicas discretas](https://github.com/sgarcia87/Triada-emergente), repositorio.
15. Sergi Garcia Mecinas (2026). [Q-Reality-12D](https://github.com/sgarcia87/Q-Reality-12D), repositorio.
16. Sergi Garcia Mecinas (2026). [Cubo Mágico 64](https://github.com/sgarcia87/cubo-magico-64), repositorio.

Esta bibliografía es una base de trabajo, no una revisión sistemática que permita reclamar prioridad científica. No se ha copiado contenido íntegro de terceros; las referencias a sus métodos se expresan mediante síntesis propia. El proyecto continúa abierto a revisión y resultados negativos.
