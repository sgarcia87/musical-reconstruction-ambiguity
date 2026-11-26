# RGO — Empezar por la música

**Geometría relacional y observabilidad · Sergi Garcia Mecinas · v0.6 · 26 de noviembre de 2026**

[Web interactiva](https://sgarcia87.github.io/relational-geometry-observability/) · [English overview](../README.en.md) · [Marco matemático](MARCO_GENERAL.md)

## 1. La pregunta de partida

Reconocemos una melodía aunque alguien la cante más aguda o más grave. Cambiar de instrumento no debería convertirla en otra composición. Sin embargo, ordenar sus notas de otra forma sí puede cambiarla. ¿Qué relaciones debemos conservar para reconocer la música? ¿Qué información perdemos al resumirla mediante una figura, un espectro o una huella topológica?

RGO empezó con figuras de Lissajous, un armonógrafo tridimensional y la geometría de las frecuencias. La investigación fue pasando de la señal sonora a las relaciones entre las notas, y después a una cuestión más general: **qué podemos saber de una estructura a partir de observaciones parciales**. La música continúa siendo su laboratorio inicial y una de sus principales aplicaciones.

## 2. Un ejemplo sin matemáticas avanzadas

Una octava contiene doce clases de altura (Do, Do♯, Re, etc.). Las notas separadas por una octava se identifican. Un acorde puede representarse como puntos sobre un reloj de doce posiciones. Transportar todas las notas dos semitonos gira el reloj; la organización relativa no cambia.

Dos acordes pueden tener las mismas distancias entre parejas de notas y, sin embargo, no ser el mismo acorde salvo giro o reflexión. Eso se denomina homometría. Incluso observando relaciones de tres notas, existe una pareja de clases que no se distingue hasta añadir una relación de cuatro notas, si interesa distinguir también el reflejo.

[Prueba interactiva de dos figuras](../index.html#ejemplo).

Una composición tampoco es simplemente una bolsa de acordes. Si cada acorde se transporta de forma independiente, sus formas individuales permanecen iguales, pero pueden cambiar las relaciones armónicas. Por eso debemos observar también cómo se suceden.

## 3. Cinco ideas del marco

| Idea | Significado práctico |
|---|---|
| Estado | Lo que buscamos conocer: por ejemplo, una secuencia de acordes. |
| Simetría | Cambio que decidimos considerar irrelevante para la tarea, por ejemplo una transposición común. |
| Observación | Una propiedad que podemos medir, como las distancias entre notas o una relación entre acordes. |
| Ambigüedad | Las estructuras distintas que producen las mismas observaciones. |
| Reconstrucción | Identificar una estructura, salvo las transformaciones que explícitamente hemos decidido ignorar. |

El conocimiento previo restringe las posibilidades: saber que una señal representa presencia o ausencia de notas ayuda, pero una hipótesis equivocada puede excluir la respuesta verdadera. Una observación adicional resulta útil si distingue alternativas todavía compatibles. La robustez indica si esa distinción sobrevive a errores. **Coherencia significa que las observaciones concuerdan; no significa necesariamente que sean verdaderas.**

La formalización está en [MARCO_GENERAL.md](MARCO_GENERAL.md). No es necesario conocer IA_m, Q48 ni ningún proyecto anterior del autor.

## 4. Qué se ha encontrado

**Resultados matemáticos exactos:** se han caracterizado ambigüedades de espectros en grupos finitos, calculado el efecto de restringir el espacio de soluciones a conjuntos de notas, demostrado mínimos de consultas resistentes a errores bajo protocolos explícitos y establecido un criterio por conectividad para secuencias. Se ha extendido ese enfoque a órdenes lineales y observaciones ternarias, sin afirmar que el significado lingüístico siempre sea lineal.

**Música simbólica:** en XVIII se buscaron versiones transformadas de 77 corales entre 382 originales. En XIX se estudiaron 297 transcripciones de 51 melodías irlandesas pertenecientes a diez familias. La huella de relaciones entre tres eventos obtuvo 79,92% de top-1 en 288 consultas de la misma melodía. En la prueba más exigente de parentesco entre IDs diferentes (51 representantes), alcanzó 33,33%, frente a 48,04% de una referencia de alineación cromática y 9,65% de azar. La topología probada fue claramente menos eficaz. Son resultados exploratorios, no una demostración de reconocimiento de grabaciones ni superioridad frente al estado del arte.

## 5. Cómo nació la investigación

- Jonathan Foote: autosimilitud temporal del audio.
- Dmitri Tymoczko: espacios geométricos de acordes y transformaciones.
- Forte, Babbitt y Lewin: clases de altura, intervalos y complementación.
- Amiot, Mandereau y Yust: Fourier, homometría y fase musical.
- Bergomi, Baraté y Di Fabio: huellas topológicas.
- Victoria Callet-Feltz: Fourier y homología persistente para datos musicales.
- Joan Serrà y Xavier Serra y colaboradores: reconocimiento de versiones mediante cromas y alineación.

Estos trabajos son antecedentes, no resultados de RGO. La propuesta de RGO es usar una misma pregunta de identificabilidad para comparar representaciones y seleccionar observaciones. No se afirma que el método general sea nuevo ni que la música, la geometría y el lenguaje sean físicamente equivalentes.

## 6. Seguir leyendo

[Investigación musical XVIII–XIX](MUSICA.md) · [Demostraciones matemáticas](INVESTIGACION.md) · [Historia del proyecto](ANTECEDENTES.md) · [Experimentos semánticos](SEMANTICA.md) · [Correcciones y límites](CORRECCIONES.md) · [Agenda](ROADMAP.md).
