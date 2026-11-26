# RGO — Geometría relacional y observabilidad

**Relational Geometry and Observability · Sergi Garcia Mecinas · v0.6 · 26 de noviembre de 2026**

🌐 **[Abrir RGO — investigación y laboratorios interactivos](https://sgarcia87.github.io/relational-geometry-observability/)** · [English overview](README.en.md)

**¿Por qué reconocemos una melodía aunque se toque en otra tonalidad? ¿Qué información hace que siga siendo la misma música?**

RGO nació estudiando la geometría de las frecuencias y de los acordes. La pregunta se convirtió en una investigación matemática: qué información conserva una observación, qué alternativas no distingue y qué relaciones adicionales permiten reconstruir una estructura. **No necesitas conocer IA_m, Q48, teoría cuántica ni ningún trabajo previo.**

[**Empezar desde cero: explicación sin tecnicismos**](docs/EMPEZAR.md) · [**Investigación musical y resultados XVIII–XIX**](docs/MUSICA.md)

## Música: la prueba más reciente

En partituras simbólicas de 382 corales de Bach y 297 transcripciones de melodías tradicionales (51 IDs, diez familias), las relaciones temporales resultan más discriminantes que los resúmenes topológicos probados. No obstante, una referencia de alineación cromática supera a los trigramas en la prueba de 51 representantes (48,04% frente a 33,33%). No se ha probado reconocimiento desde audio ni superioridad general.

| Resultado | Alcance |
|---|---|
| 79,92% | Identificación de otra transcripción del mismo ID (288 consultas, azar 3,33%). |
| 36,03% | Identificación de otro ID de la misma familia (297 consultas, azar 7,53%). |
| 32 transiciones | En Bach, la órbita conjunta conserva información que las correlaciones cruzadas pierden. |
| 77/77 | Permutar ventanas no altera el resumen de PH sin tiempo; añadir tiempo cambia el resumen en estos controles, sin garantía de unicidad. |

[Nota XVIII](docs/rgo_fase18_nota.md) · [Nota XIX](docs/rgo_fase19_nota.md) · [Auditorías](audits/) · [Resultados](results/)

## Cómo se generalizó la pregunta musical

[Leer el marco general desde cero](docs/MARCO_GENERAL.md) · [Informe matemático de las fases I–XI](docs/INVESTIGACION.md) · [Cronología de experimentos](docs/MARCO_GENERAL.md#trayectoria-y-evidencia)

Cada problema especifica un universo de candidatos, las simetrías que se consideran irrelevantes, el conocimiento previo y un diccionario de observaciones. La reconstrucción busca reducir la fibra de alternativas compatibles. La robustez, la selección adaptativa y la certificación del modelo son problemas diferentes de la mera coherencia entre perspectivas.

## Resultados matemáticos

| Línea | Resultado y alcance |
|---|---|
| Recuperación de fase | Retículos de relaciones de fase y forma normal de Smith caracterizan la ambigüedad, fijados soporte y magnitudes y descontadas las traslaciones. [Detalle](docs/AMBIGUEDAD_ESPECTRAL.md). |
| Música: conocimiento previo | En 4096 indicadores de Z₁₂, 262 requieren orden cuatro entre señales reales admisibles y 24 entre indicadores. Censo exacto adicional para n=2,…,16. [Fase XI](docs/rgo_fase11_nota.md). |
| Certificación del modelo | Momentos de orden tres (no negativos) o cuatro (reales) certifican binariedad y acotan distancia a algún indicador, no su identidad. [Fase XI](docs/rgo_fase11_nota.md). |
| Consultas robustas | Para el diccionario de 19 tricordos y 43 tetracordos de Z₁₂, espectro/DC exactos y repetición permitida, el mínimo universal es 8h consultas para distancia h. [Demostración](docs/rgo_fase11_nota.md). |
| Tiempo | Con órbitas locales conocidas y relaciones cross-Fourier especificadas, el criterio por conectividad determina la ambigüedad relativa. En 382 corales de Bach, 377 quedan identificadas con relaciones consecutivas y las otras cinco con seis conexiones adicionales. [Detalle](docs/OBSERVABILIDAD_TEMPORAL.md). |
| Q48 y cuántica | La homometría Walsh, el cociente bent y la distinción teórica entre una copia y dos copias con traslación compartida son casos de estudio; no prueban una ventaja cuántica ni una unificación física. [Fase X](docs/rgo_fase10_nota.md). |
| **Intermediación y orden (XVII)** | Para n elementos ordenados salvo inversión, la firma de todas las ternas tiene distancia mínima exactamente n−2. Para seis elementos: mínimos fijos 7, 10 y 16 para identificación, detección de un error y corrección de un error, respectivamente, sin repetición. Adaptativamente bastan seis consultas exactas; con ocho elementos (20.160 órdenes), diez consultas exactas son óptimas en el peor caso. [Demostración](docs/rgo_fase17_nota.md) · [Ampliación y auditorías](docs/rgo_fase17_extension.md). |

## Aplicación separada: semántica y órdenes

Las fases XII–XVI separan asociación, pertenencia a una dimensión, intermediación y orientación. Los resultados no justifican identificar asociación con intensidad ni coherencia con verdad. El control XVII incorpora una primera búsqueda de observaciones ordinales externas y una ampliación con evidencia de paráfrasis de JJGraph; hay cobertura parcial, pero no fiabilidad suficiente.

- XII: el rechazo del prior fue en gran parte circular porque la referencia y las aristas reservadas tenían origen compartido.
- XIII: difracción no supera de forma consistente a PPR mínimo; con pertenencia conocida y ablación, 58,70% frente a 65,22%.
- XIV: 26/28 pares internos se ordenan con extremos conocidos y ablación informada por pertenencia.
- XV: la agrupación entrante reúne 50/96 pares positivos anotados, pero la pertenencia y el orden conjuntos recuperan solo 19/106 ternas. Un óptimo geométrico puede ser semánticamente incorrecto.
- XVI: segundo banco de semiescalas, 40/353 ternas cubiertas; Fiedler combinado 25,83%, PC1 entrante 39,17%, azar 33,33%.
- XVII: los primeros dos pilotos no cubren ternas objetivo; la ampliación con JJGraph sí produce restricciones. En 87 semiescalas, la regla principal certifica solo dos ternas, una correcta; 22 escalas incompatibles. Se mantiene la distinción entre certificación matemática y validez empírica. [Ampliación XVII](docs/rgo_fase17_extension.md).

[Informe completo XII–XVII](docs/SEMANTICA.md) · [Límites y correcciones](docs/CORRECCIONES.md) · [Agenda de investigación](docs/ROADMAP.md).

## Laboratorios interactivos

| Laboratorio | Qué permite comprobar |
|---|---|
| [Fase X — La fase invisible](https://sgarcia87.github.io/relational-geometry-observability/demos/rgo_fase10.html) | Magnitudes idénticas y observador adaptativo. |
| [Fase XI — Reconstrucción robusta](https://sgarcia87.github.io/relational-geometry-observability/demos/rgo_fase11.html) | Consultas musicales con errores. |
| [Fase XII — Cambiar de perspectiva](https://sgarcia87.github.io/relational-geometry-observability/demos/rgo_fase12.html) | Coherencia interna con priors excluyentes (advertencia de circularidad incluida). |
| [Fase XIV — Una relación tiene dirección](https://sgarcia87.github.io/relational-geometry-observability/demos/rgo_fase14.html) | Proyección con extremos conocidos. |
| [Fase XV — Emergencia de ejes](https://sgarcia87.github.io/relational-geometry-observability/demos/rgo_fase15.html) | Asociación sin anclajes y límites del orden. |
| [Fase XVII — ¿Quién está entre quién?](https://sgarcia87.github.io/relational-geometry-observability/demos/rgo_fase17.html) | Fibras U/P, selección de consultas y reconstrucción con errores en un modelo ordinal ideal. |
| [Fase XVII · ampliación: observador de hasta ocho elementos](https://sgarcia87.github.io/relational-geometry-observability/demos/rgo_fase17_observador.html) | Órdenes ocultos, prior de extremo y validación global. |

## Reproducibilidad

```bash
pip install -r requirements-research.txt
python audits/rgo_fase9_audit.py
python audits/rgo_fase10_audit.py
python audits/rgo_fase11_audit.py
python audits/verify_robustness.py
node audits/rgo_fase17_audit.mjs
node audits/rgo_fase17_math.mjs
node audits/rgo_fase17_prior.mjs
# Música: las fuentes externas se descargan y se comprueban
node audits/rgo_fase18_audit.mjs
node audits/rgo_fase19_audit.mjs --data ./rgo_data
```

Los JSON están en [results/](results/). XVIII y XIX se ejecutaron en JavaScript sobre los corpus recuperados; XIX verifica la invariancia de las 77 transposiciones y la persistencia de un cuadrado. La descarga completa desde el contenedor local no se repitió. Las auditorías matemáticas IX–XI se reprodujeron exactamente en v0.3; XVII se ejecutó exhaustivamente y sus mínimos principales se contrastaron mediante un procedimiento Python/SciPy independiente. Los resultados lingüísticos se calcularon sobre fuentes originales recuperadas, con límites específicos de reproducción. Véanse [comandos para los corpus externos](docs/SEMANTICA.md#conclusión-científica-y-reproducibilidad) y [procedencia de XVII](docs/rgo_fase17_nota.md#6-antecedentes-y-reproducción) y [ampliación con JJGraph](docs/rgo_fase17_extension.md#6-reproducción). Para el corpus de Bach: `python audits/phase_temporal.py` y `python audits/temporal_corpus.py jsb-chorales-quarter.json`; el corpus externo no se redistribuye.

**Estado científico:** investigación abierta, no revisada por pares; originalidad bibliográfica de los resultados particulares pendiente. Los problemas de fase, homometría, ordenación mediante consultas ternarias, códigos y recuperación de órbitas tienen antecedentes. No hay validación general de IA_m, de una teoría de la consciencia ni de una ventaja cuántica. Las versiones anteriores están en el historial y [antecedentes](docs/ANTECEDENTES.md). La licencia sigue pendiente de decisión del autor.
