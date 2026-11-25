# Geometría relacional y observabilidad

**RGO · Introducción e informe principal · v0.2 · Sergi Garcia Mecinas · 25 de noviembre de 2026**

[Web interactiva](https://sgarcia87.github.io/relational-geometry-observability/) · [Nota técnica](OBSERVABILIDAD_TEMPORAL.md) · [Agenda](ROADMAP.md) · [Apéndice](ANTECEDENTES.md)

## Resumen

Una medición puede ser correcta y, aun así, insuficiente para distinguir dos objetos. El objetivo de RGO es estudiar qué información conserva una observación, qué ambigüedad deja y qué observaciones adicionales son necesarias para recuperar las relaciones que interesan. Se emplean conjuntos finitos, transformadas de Fourier, grafos y teoría de la información. La música constituye un ejemplo calculable; la recuperación de fases cuánticas es un problema relacionado. Se presentan una caracterización exacta de 48 conjuntos de clases de altura, una separación de ambigüedades mediante productos de Fourier de orden tres y un criterio general de reconstrucción temporal por conectividad en grupos cíclicos. Los resultados no implican una teoría física unificada ni prioridad científica establecida.

## 1. Empezar desde cero: observar no es conocerlo todo

Imaginemos un reloj de doce posiciones. Encendemos seis puntos y dejamos seis apagados. Conocer que hay seis luces encendidas no permite saber dónde están: hay 924 posibilidades. Medir las distancias entre todos los pares de luces aporta información, pero tampoco siempre basta. Dos figuras distintas pueden compartir exactamente las mismas distancias.

Llamamos **estado** a la configuración completa, **observación** a una función que extrae información y **ambigüedad** al conjunto de estados que producen el mismo resultado. En música las posiciones del reloj representan las doce clases de altura, numeradas de 0 a 11 (Do, Do♯, Re, ..., Si). Una clase agrupa todas las notas separadas por octavas; esta simplificación no conserva registro ni timbre.

Si el objetivo es reconocer la forma de una figura, girar todo el reloj no debería importar. Sin embargo, girar una parte respecto a otra sí puede modificar la estructura. Esta diferencia entre transformación global irrelevante y cambio interno relevante es esencial.

Formalmente, para una observación $O:X\to Y$, los estados $x,x'$ son indistinguibles cuando $O(x)=O(x')$. Si un grupo $G$ expresa las transformaciones que decidimos ignorar, queremos identificar las órbitas de $G$, no necesariamente los estados absolutos. Una observación invariante no es automáticamente completa.

## 2. De doce signos a un modelo musical

El espacio de estados es $X=\{0,1\}^{12}$, con $2^{12}=4096$ configuraciones. Se interpreta el bit 1 como presencia de una clase de altura y el bit 0 como ausencia. Esta correspondencia es una codificación; no afirma que toda la música sea binaria.

Las doce posiciones forman el grupo cíclico $\mathbb Z_{12}$. El teorema chino del resto permite organizarlas en una tabla usando simultáneamente el resto módulo 3 (fila) y módulo 4 (columna):

| | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| 0 | 0 | 9 | 6 | 3 |
| 1 | 4 | 1 | 10 | 7 |
| 2 | 8 | 5 | 2 | 11 |

Al convertir presencia/ausencia en signos +1/−1, cada fila tiene cuatro componentes. Exigimos que su suma sea cero (dos positivos y dos negativos) y que los productos internos entre filas distintas sean cero. Esto produce exactamente 48 estados, denominados **Q48**. Hay tres direcciones equilibradas ortogonales, cada una con dos orientaciones: $3!2^3=48$.

Esta construcción sirve como ejemplo pequeño y completamente auditable. No presupone que Q48 sea privilegiado en la percepción o en las composiciones.

## 3. Fourier: por qué las magnitudes no bastan

Para un conjunto de notas $A\subseteq\mathbb Z_{12}$ definimos

$$F_k(A)=\sum_{a\in A}e^{-2\pi i ka/12}.$$

Cada coeficiente es un número complejo. Su módulo indica la intensidad de un patrón; su fase expresa información sobre su orientación. El espectro de potencia $|F_k|^2$ equivale a la autocorrelación mediante Fourier, por lo que contiene el contenido interválico, pero no toda la configuración.

Una transposición de $s$ semitonos multiplica $F_k$ por $e^{-2\pi i ks/12}$. Por eso el módulo no cambia. Tampoco cambia bajo reflexión cromática (inversión). Sin embargo, existen conjuntos con idénticos módulos que no se relacionan por esas transformaciones: se denominan homométricos o Z-relacionados en teoría musical.

No se trata de una idea nueva: Mandereau y colaboradores conectaron explícitamente la relación Z con la recuperación de fase y la homometría; Amiot y Yust estudiaron la información de fase invariante mediante productos de Fourier (véase bibliografía).

### 3.1 Un resultado exacto sobre Q48

Para un conjunto de seis clases de altura, la condición de equilibrio y ortogonalidad de las tres filas es equivalente a

$$F_4=0,\qquad |F_3|^2=4.$$

$F_4=0$ obliga a que haya dos notas en cada fila. Entre las configuraciones así equilibradas, el módulo de $F_3$ selecciona exactamente las que utilizan las tres direcciones ortogonales distintas. La demostración está en la [nota técnica](OBSERVABILIDAD_TEMPORAL.md#1-caracterización-exacta-de-q48).

Los 48 conjuntos pertenecen a cuatro clases de Forte, 12 transposiciones por clase. Basta el producto cúbico $B=F_1^2\overline{F_2}$, invariante bajo transposición, para identificarlas:

| Clase | B (real y exacto) |
|---|---|
| 6-Z37 | $8+4\sqrt3$ |
| 6-Z4 | $-8-4\sqrt3$ |
| 6-Z48 | $8-4\sqrt3$ |
| 6-Z26 | $-8+4\sqrt3$ |

Complementar un hexacordo de Q48 cambia el signo de $B$, pero no su potencia espectral. Su magnitud separa los dos perfiles interválicos y su signo distingue los complementarios.

### 3.2 Fuera de Q48: todas las configuraciones cromáticas

Se enumeraron los 4096 conjuntos, identificando transposición e inversión. Los resultados:

| Información disponible | Clases distinguibles |
|---|---:|
| Cardinalidad (número de notas) | 13 |
| Espectro de potencia completo | 201 |
| Espectro más dos productos cúbicos reales | 224 de 224 |

Hay 23 pares Z entre las 224 clases (15 de seis notas). Las partes reales de $F_1^2\overline{F_2}$ y $F_1F_2\overline{F_3}$ completan la distinción. Ninguno de los 12 tipos de productos cúbicos no constantes examinados la completa individualmente; hay 14 parejas suficientes. Se trata de minimalidad dentro de un diccionario concreto, no entre todas las observaciones posibles.

Los cálculos se realizan con aritmética exacta en el anillo ciclotómico $\mathbb Z[\zeta_{12}]$. La teoría general de correlaciones de orden superior y biespectro es conocida. La prioridad de estas selecciones concretas no se ha determinado.

## 4. Introducir el tiempo: una canción no es solo una colección de figuras

Do mayor → Re mayor y Do mayor → Do mayor contienen la misma clase de acorde en cada instante, si se elimina su transposición individual. Sin embargo, en la primera secuencia hay desplazamiento y en la segunda no. Por ello, la invariancia deseada es ante una transposición **común a toda la secuencia**, no una independiente por ventana.

Suponiendo conocida la órbita por transposición de cada ventana musical, podemos medir un producto cruzado

$$R_{ij,k}=F_k(A_j)\overline{F_k(A_i)}.$$

La transposición común se cancela. Los desplazamientos relativos aparecen en la fase del producto. Si alguno de los coeficientes es cero, esa frecuencia deja de informar sobre la relación.

Dentro de Q48, $B$ identifica la órbita local y $F_1$ nunca se anula. Conocer los productos de $F_1$ entre instantes consecutivos permite reconstruir una secuencia completa de estados Q48 salvo una transposición global. Se comprobaron los 2304 pares ordenados, con 192 órbitas globales distintas y 192 firmas.

Fuera de Q48, **el conocimiento de la clase local por transposición es una hipótesis adicional**. La clasificación de la sección 3.2 identifica hasta transposición e inversión, no hasta transposición solamente. No debe utilizarse esa clasificación como sustituto automático de las órbitas locales necesarias para el teorema temporal.

## 5. Resultado central: contar las reconstrucciones compatibles

Consideramos una secuencia de conjuntos de un grupo cíclico $\mathbb Z_n$. Cada conjunto tiene un período mínimo $p_i$ (número de transposiciones distintas). Para cada par observado, sea $d_{ij}$ el mínimo común múltiplo de los órdenes de las frecuencias medidas no nulas en ambos estados. Si no hay ninguna, $d_{ij}=1$.

Dos reconstrucciones que coinciden en sus observaciones solo pueden diferir por desplazamientos locales $s_i$ que cumplen las congruencias $s_i\equiv s_j\pmod{d_{ij}}$.

Para cada potencia prima $\ell=p^e$ que divide a $n$, se construye un grafo: se incluyen los instantes con $p_i$ múltiplo de $\ell$ y las relaciones con $d_{ij}$ múltiplo de $\ell$. Denotamos por $c_\ell$ su número de componentes conexas. El número de reconstrucciones compatibles, salvo una transposición global, es

$$\boxed{N=\prod_{p^e\mid n}p^{\max(0,c_{p^e}-1)}}.$$

Para $n=12$ hay niveles 2, 4 y 3:

$$N=2^{(c_2-1)_++(c_4-1)_+}3^{(c_3-1)_+}.$$

**Hay reconstrucción única si todos los grafos activos están conectados.** Cada componente desconectada aporta una libertad relativa. La demostración descompone las congruencias en dígitos de potencias primas y elimina la transposición común; véase [nota técnica](OBSERVABILIDAD_TEMPORAL.md#4-teorema-de-ambigüedad-temporal-para-grupos-cíclicos-finitos).

Ejemplo: los conjuntos {0,1} y {0,2,4,6,8,10} no comparten frecuencias no constantes no nulas. Cambiar el segundo por {1,3,5,7,9,11} deja todas las correlaciones cruzadas iguales. Hay dos reconstrucciones relativas posibles. Una tercera figura que comparta las frecuencias necesarias con ambas puede revelar la diferencia.

**Verificación:** 352 órbitas locales por transposición; 1.398.500 clases de pares ordenados por transposición global, de las que 1.393.108 son identificables bajo el protocolo. Otras 5.392 pertenecen a fibras ambiguas. La fórmula se contrastó también con 300 secuencias de tres estados y grafos aleatorios mediante enumeración de desplazamientos.

La sincronización de fase es un área consolidada. Lo que se estudia aquí es el criterio explícito de ambigüedad discreta con períodos locales heterogéneos y relaciones de orden parcial; su originalidad bibliográfica está pendiente.

## 6. Experimento en 382 corales de Bach

Se utiliza el [corpus JSB Chorales](https://github.com/czhuang/JSB-Chorales-dataset), discretizado en negras. En cada ventana deslizante se toma la unión de las clases de altura presentes. Se conoce la órbita local por transposición de cada ventana y se presupone acceso a toda la correlación cruzada de cada par seleccionado. La pregunta es cuántas relaciones son necesarias para identificar esa secuencia binaria hasta una transposición común.

| Ventana | Ventanas analizadas | Piezas identificables con relaciones consecutivas | Con relaciones adicionales | Aristas adicionales mínimas (suma sobre corpus) |
|---:|---:|---:|---:|---:|
| 1 negra | 23.134 | 225 | 382 | 299 |
| 2 negras | 22.752 | 356 | 382 | 41 |
| 4 negras | 21.988 | 377 | 382 | 6 |
| 8 negras | 20.460 | 370 | 382 | 16 |

Con cuatro negras, cinco piezas presentan ambigüedad bajo observaciones consecutivas. Un algoritmo que conecta los niveles desconectados añade seis aristas en total (cuatro piezas requieren una, una requiere dos). Una arista reduce como máximo en uno el número de componentes de cada nivel; la cota inferior es el mayor déficit de conectividad. En este corpus el algoritmo alcanza la cota para todas las piezas y longitudes probadas. No se afirma que sea óptimo para cualquier instancia.

**Qué no significa:** no se reconstruye una grabación, ni una partitura completa, ni se reconoce una canción desconocida. Se pierden octavas, voces, timbre, dinámica y orden interno de las notas de cada ventana. Los resultados dependen de la representación y de las hipótesis de acceso a información local. Se trata de una auditoría de identificabilidad, no de una comparación de sistemas de reconocimiento de versiones.

Los experimentos anteriores de aparición y proximidad de Q48 en Bach no establecieron un privilegio musical independiente de la tonalidad; se conservan en el apéndice, no como argumento principal.

## 7. Observabilidad condicionada: conservar lo que importa

Sea $X$ el estado, $T=t(X)$ la variable objetivo e $Y$ el resultado de observarlo. Buscamos conservar información sobre $T$ y eliminar, cuando sea pertinente, información sobre el estado que no hace falta para identificar $T$. Con un prior explícito, se pueden medir

$$R=I(T;Y)/H(T),\qquad L=I(X;Y\mid T)/H(X\mid T),$$

si los denominadores son positivos. Son dos medidas distintas, no una única puntuación universal.

Una auditoría previa utilizaba $C=1-\operatorname{mean}(\mathrm{JSD})$ para comparar distribuciones obtenidas bajo diferentes perspectivas. Si se aplica un canal de difusión común, la desigualdad de procesamiento de datos explica por qué las divergencias pueden disminuir mientras se pierde información sobre su origen. Eso no implica que cualquier aumento de $C$ en cualquier sistema cause pérdida informativa.

En un experimento PPR sobre el hipercubo de 12 bits, tomando como objetivo las cuatro familias Q48 y como diferencia irrelevante la transposición, se observa algo distinto. Con difusión 0,85, reducir la observación a su órbita conserva los 0,51335 bits disponibles sobre la familia y reduce la información condicional sobre la orientación de 1,72014 bits a cero. La coherencia dentro de familia pasa de 0,42989 a 1. El resultado usa simetría del canal, prior uniforme sobre Q48 y una sola muestra. No demuestra éxito sobre otros grafos.

La razón: cuando un canal es equivariante bajo las transformaciones y el prior condicionado a cada objetivo es uniforme en su órbita, la distribución marginal de observaciones para cada objetivo es invariante. La probabilidad posterior del objetivo depende únicamente de la órbita observada. Por tanto, la órbita es un estadístico suficiente para ese objetivo. Este mecanismo conserva información útil en lugar de borrar todas las diferencias por difusión.

En grafos semánticos, el reto pendiente es definir objetivos y perturbaciones mediante validación externa. No se puede declarar irrelevante una modificación que cambie el significado. La [agenda de investigación](ROADMAP.md) establece un protocolo y criterios de comparación.

## 8. Relación con la física cuántica: un límite preciso

Un estado cuántico puro puede escribirse como $\sum_i\alpha_i|i\rangle$. Medir en la base computacional proporciona probabilidades $|\alpha_i|^2$, que no determinan las fases relativas. Si se conocen coherencias complejas $\alpha_i\overline{\alpha_j}$, un grafo conectado sobre las amplitudes no nulas permite recuperar esas fases salvo una fase global. Si está desconectado, queda una fase libre por componente, menos una global.

Esto es el análogo continuo de la sincronización de desplazamientos en secuencias cromáticas. No identifica la fase de una nota con la fase de una amplitud cuántica, ni modela la consciencia. Requiere estados puros, magnitudes conocidas y observaciones sensibles a fase; los estados mixtos y el coste experimental de obtener tales coherencias constituyen otros problemas. Las simulaciones antiguas del Hamiltoniano Q48 se mantienen como material de contexto.

## 9. Qué se sabe y qué falta

| Estado | Resultado |
|---|---|
| Demostración | Equivalencia Fourier/Q48 y fórmula de ambigüedad bajo hipótesis explícitas. |
| Enumeración exacta | Separación de las 224 clases y auditoría de pares y secuencias. |
| Empírico condicionado | Reconstrucción cromática en las corales y mínimo de aristas para el protocolo probado. |
| Numérico | Ejemplo PPR y observabilidad condicionada. |
| Pendiente | Prioridad bibliográfica, ruido, comparaciones con referencias musicales, prueba en grafos semánticos y costes de adquisición. |

RGO no parte de una afirmación acerca de la naturaleza de la realidad. Parte de un problema comprobable: **conocer la estructura a partir de relaciones parciales, y saber qué sigue siendo desconocido**.

## 10. Reproducibilidad y referencias

Ejecutar desde la raíz:

~~~bash
python audits/phase_temporal.py
python audits/temporal_corpus.py jsb-chorales-quarter.json
pip install numpy
python audits/conditional_observability.py
~~~

Los resultados están en [results](../results/). El corpus externo tiene Git blob SHA-1 ff93746647d1f5af2f719d235329c294267f3088. Se conserva el origen de los cálculos, no el corpus de terceros. Las auditorías algebraicas de las fases VII y VIII se volvieron a ejecutar al preparar v0.2; los resultados del corpus proceden de la ejecución documentada sobre la fuente original.

Lecturas esenciales:

- E. Amiot, *Music Through Fourier Space* (2016), https://doi.org/10.1007/978-3-319-45581-5.
- J. Mandereau et al., *Z-relation and homometry in musical distributions* (2011), https://doi.org/10.1080/17459737.2011.608819.
- J. Mandereau et al., *Discrete phase retrieval in musical structures* (2011), https://doi.org/10.1080/17459737.2011.608820.
- J. Yust y E. Amiot, *Non-Spectral Transposition-Invariant Information in Pitch-Class Sets and Distributions* (2022), https://sites.bu.edu/jyust/files/2022/09/nonSpectralrevFin.pdf.
- A. Singer, *Angular synchronization by eigenvectors and semidefinite programming* (2011), https://doi.org/10.1016/j.acha.2010.02.001.
- D. Tymoczko, *The Geometry of Musical Chords* (2006), https://pubmed.ncbi.nlm.nih.gov/16825563/.
- J. Foote, *Visualizing Music and Audio Using Self-Similarity* (1999), https://doi.org/10.1145/319463.319472.
- V. Callet-Feltz, [trabajos sobre Fourier y homología persistente](https://victoriacallet.github.io/recherche.html).

La [nota técnica](OBSERVABILIDAD_TEMPORAL.md) amplía las demostraciones y la bibliografía. El [apéndice histórico](ANTECEDENTES.md) recoge los antecedentes propios, la motivación filosófica y las líneas aparcadas. No se requiere su lectura para entender los resultados.
