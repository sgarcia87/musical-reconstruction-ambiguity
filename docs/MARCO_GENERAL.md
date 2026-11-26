# RGO — Marco general y trayectoria

**Sergi Garcia Mecinas · v0.6 · 26/11/2026**

[Inicio](../README.md) · [Informe matemático I–XI](INVESTIGACION.md) · [Informe semántico XII–XVII](SEMANTICA.md) · [Fase XVII: órdenes](rgo_fase17_nota.md)

[**Introducción desde la música, sin conocimientos previos**](EMPEZAR.md) · [Investigación musical XVIII–XIX](MUSICA.md)

## La pregunta común

Una estructura desconocida no se identifica por la coherencia de una representación, sino por su capacidad de distinguirla de las alternativas relevantes. RGO estudia qué información conserva cada observación, qué diferencias quedan invisibles, qué hipótesis previas restringen las alternativas y qué relación adicional puede discriminarlas. El proyecto no identifica una nota musical, un qubit y un concepto como objetos físicamente equivalentes. Transfiere un problema matemático de identificación, con hipótesis diferentes en cada dominio.

## Modelo de observación

1. **Universo U:** objetos admisibles en el problema amplio; se especifican las equivalencias, por ejemplo traslación, inversión o una acción de grupo. Las hipótesis pueden ser continuas o discretas.
2. **Prior P:** subconjunto de U admitido por el observador. Un prior probabilístico es una distribución, no una simple restricción, y exige distinguir soporte, ponderación e incertidumbre.
3. **Diccionario Q:** cada consulta q define un mapa de observación O_q sobre U. En el modelo exacto, el vector de lecturas acumuladas y determina F_U(y)={x∈U: O_Q(x)=y}; F_P(y)=F_U(y)∩P. El cociente por simetrías se usa solo si la medición o la tarea respeta la equivalencia.
4. **Ambigüedad:** para una fibra finita, log₂|F_U| cuantifica alternativas equiprobables, no la entropía de una distribución arbitraria. Para fibras continuas, dimensión, componentes y medidas requieren definiciones distintas.
5. **Compatibilidad:** una fibra vacía refuta la conjunción de modelo, lecturas exactas y prior. Una fibra única identifica el objeto únicamente bajo esas hipótesis. Con un presupuesto de errores, se conserva el conjunto de firmas a distancia no mayor que dicho presupuesto.
6. **Selección:** una observación adicional induce una partición de la fibra; se puede maximizar reducción esperada de entropía o minimizar tamaño de la rama peor. Una estrategia adaptativa selecciona en función de la lectura previa. Las soluciones exactas, óptimos combinatorios y heurísticas se distinguen.
7. **Robustez:** la distancia mínima entre firmas controla la separación ante sustituciones y borrados. Para ruido estadístico se necesita un modelo de probabilidad y estimación; coherencia no reemplaza identificabilidad. Si el verdadero objeto no está en U o todas las mediciones comparten sesgo, el protocolo puede fallar.

Con datos finitos, este modelo permite verificar familias de candidatos, contar alternativas, elegir preguntas y certificar o rechazar hipótesis. Se inscribe en teoría de la información, problemas inversos, diseño de experimentos y códigos. No se reclama la originalidad del marco general.

## Trayectoria y evidencia

| Fases | Qué se investigó | Qué permanece |
|---|---|---|
| I–VIII | Música, simetrías, cambio de perspectiva, fase y reconstrucción temporal. | El laboratorio musical y el criterio temporal condicionado; [historial](ANTECEDENTES.md). |
| IX | Relaciones de fase y ambigüedad residual mediante retículos/Smith; Walsh del conjunto Q48. | Censo, criterios de soporte, dependencia de las simetrías. |
| X | Cociente relacional de Q48, homometría y consultas; aplicación algebraica a Cubo64 y dos copias cuánticas. | Resultados algebraicos, no equivalencia de todos los objetos ni experimento físico. |
| XI | Prior binario, certificado de pertenencia, reconstrucción robusta y observación adaptativa. | Cotas y mínimos bajo protocolos explícitos, simulaciones ruidosas. |
| XII | Fragilidad del prior y coherencia en un grafo interno. | Contraejemplos; circularidad de la aparente validación. |
| XIII | Asociaciones humanas y escala externa. | Difracción no supera consistentemente al mínimo PPR. |
| XIV | Perfiles entrantes/salientes y proyección sobre extremos conocidos. | Evidencia exploratoria, condicionada a anclajes y pertenencia. |
| XV | Descubrimiento de familias sin anclajes y seriación. | La pertenencia emerge parcialmente, el orden no es fiable; óptimos geométricos incorrectos. |
| XVI | Segundo banco de semiescalas. | La mejora de orden no se reproduce robustamente. |
| XVII | Intermediación de tres resultados, distancia, listas mínimas y observador adaptativo. | Modelo ordinal exacto; profundidad adaptativa óptima hasta n=8, pilotos iniciales sin cobertura, JJGraph con cobertura parcial y errores semánticos. [Ampliación](rgo_fase17_extension.md). |
| XVIII | Identificación simbólica y órbitas conjuntas de ventanas. | Criterio de desplazamiento relativo y contraste con Fourier; alineación más eficaz en la condición difícil. |
| XIX | Fourier, homología persistente y tiempo en Bach y variantes tradicionales. | Las relaciones temporales discriminan mejor que las firmas topológicas ensayadas; falta audio real. |

## Correspondencia entre dominios

| Dominio | Objeto y equivalencia | Observación | Alcance |
|---|---|---|---|
| Música | Indicador de clases de altura, módulo traslación | Correlaciones y magnitudes de Fourier | Censos y mínimos exactos; no audio ni interpretación musical general. |
| Q48 / Walsh | Indicadores o señales reales, módulo traslación | Magnitudes y signos de relaciones de fase | Ambigüedad dependiente del prior, resultados algebraicos. |
| Cuántica | Estado y preparación especificados | Esperanzas de observables, una/dos copias correlacionadas | Predicción teórica; no ejecución física ni equivalencia con el coste de consultas clásicas. |
| Tiempo musical | Secuencia de órbitas locales | Productos cross-Fourier entre ventanas | Criterio de identificación relativo y condicionado. |
| Orden ordinal | Orden total estricto, módulo inversión | Elemento intermedio de una terna | Distancia n−2, mínimos fijos n≤6 y adaptativos n≤8, pruebas ideales de priors equivocados. |
| Lenguaje | Palabras, sentidos y atributos, con empates/contextos posibles | Asociaciones, juicios, patrones u otras mediciones | Pruebas parciales: no se ha validado un oráculo general ni descubierto ejes fiables. |

## Qué queda abierto

En música, XVIII–XIX distinguen identificación en catálogo de reconstrucción exacta, y muestran que la topología sin tiempo pierde orden. La prioridad empírica siguiente es comparar versiones de audio reales con representaciones y costes equivalentes. [Música](MUSICA.md).


La fase XVII demuestra propiedades del observador ordinal, no que sea posible extraer todas las lecturas fiables del lenguaje. JJGraph aporta restricciones pero también numerosas contradicciones y certificados incorrectos. Queda estudiar el descubrimiento del atributo, la fiabilidad y cobertura de fuentes independientes, los empates, órdenes parciales y contextos, la estimación de fiabilidad, el coste real y la selección robusta de consultas con modelo equivocado. Paralelamente, queda contrastar prioridad bibliográfica de los resultados matemáticos y extender protocolos a grupos, tamaños y mediciones distintos.

La relación dualidad–intermediación–síntesis puede motivar preguntas, pero no es una conclusión general. La intermediación estricta no determina un punto medio métrico; la síntesis necesita definición y observaciones propias. Ninguna analogía se toma como prueba física o semántica.

[Correcciones científicas](CORRECCIONES.md) · [Agenda actualizada](ROADMAP.md) · [Laboratorios](https://sgarcia87.github.io/relational-geometry-observability/)
