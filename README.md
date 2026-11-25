# RGO — Geometría relacional y observabilidad

**Relational Geometry and Observability · Sergi Garcia Mecinas · v0.4 · 26 de noviembre de 2026**

🌐 **[Abrir la web oficial de RGO — demostraciones interactivas](https://sgarcia87.github.io/relational-geometry-observability/)**

[English overview](README.en.md) · [Informe desde cero](docs/INVESTIGACION.md) · [Nota técnica de fase y reconstrucción](docs/AMBIGUEDAD_ESPECTRAL.md) · [Nota de robustez](docs/rgo_fase11_nota.md)

> ¿Cuánta información hace falta para reconstruir una estructura cuando las observaciones son parciales, ambiguas o contienen errores? ¿Cómo cambia la respuesta cuando conocemos su naturaleza de antemano?

Dos objetos distintos pueden tener exactamente el mismo patrón de magnitudes. La música ofrece un ejemplo: dos conjuntos de notas pueden compartir todas sus distancias por parejas sin tener la misma forma. RGO estudia cómo cuantificar esta ambigüedad, seleccionar relaciones adicionales y distinguir las diferencias relevantes de las simetrías que no importan para la tarea.

**No hace falta conocer los proyectos anteriores del autor.** La investigación utiliza grupos finitos, Fourier, teoría de la información y diseño de observaciones. No presupone una teoría de la realidad o de la consciencia.

## Resultados principales

| Resultado | Alcance y evidencia |
|---|---|
| Criterio de reconstrucción de fase mediante retículos | La ambigüedad de señales reales con magnitudes dadas y observaciones invariantes queda descrita por un grupo cociente. La forma normal de Smith permite calcular su parte libre y finita. Formulación y prueba, sin prioridad bibliográfica establecida. |
| El conocimiento previo cambia el orden necesario | En los 4096 indicadores sobre Z₁₂, 262 requieren orden 4 entre señales reales; entre indicadores, solo 24 requieren ese orden. De los 262, 190 se resuelven hasta orden 2 y 48 con orden 3. Enumeración exacta; censo adicional de n=2 a 16. |
| Certificación de un modelo binario | Momentos de orden 3 (señales no negativas) o 4 (reales) permiten certificar binariedad y acotar la distancia a algún indicador. No certifican por sí solos su identidad. |
| Reconstrucción robusta | Con el espectro y DC exactos, 19 tipos de tricordos y 43 de tetracordos como consultas escalares, se necesitan 8h consultas fijas universales para distancia mínima h si se permiten repeticiones. Para corregir e lecturas erróneas: 8(2e+1). Prueba inferior y construcción explícita. |
| Elección de observaciones | Si se conoce la familia ambigua, existe un caso de cuatro candidatos con mínimo fijo 3 y adaptativo 2. Las simulaciones ruidosas muestran una ventaja pequeña frente a una buena referencia fija; no se afirma superioridad general. |
| Reconstrucción temporal | Los componentes conexos de grafos por potencias primas cuentan la ambigüedad relativa. En 382 corales, con ventanas de cuatro negras y órbitas locales conocidas, 377 quedan determinadas por relaciones consecutivas; seis conexiones adicionales resuelven las cinco restantes. |

Q48 (48 configuraciones equilibradas y ortogonales), sus cocientes bent, la correspondencia con Cubo64 y la predicción cuántica de una/dos copias se mantienen como **casos de estudio**, no como prueba de una teoría física unificada.

## Nueva línea: observabilidad semántica (fases XII–XVI)

[Informe y correcciones de las cinco fases](docs/SEMANTICA.md) · [Demostración XV: ejes sin anclajes](demos/rgo_fase15.html) · [Segundo banco XVI](docs/rgo_fase16_nota.md).

| Fase | Evidencia y límite |
|---|---|
| XII · Priors erróneos | El rechazo del prior y la coincidencia del validador con la referencia son circulares en este montaje. No demuestra detección externa de errores. |
| XIII · Asociación USF | Difracción: 58,70% tras ablación; PPR mínimo: 65,22% (46 consultas con pertenencia conocida). |
| XIV · Extremos conocidos | Proyección entrante: 26/28 pares internos tras ablación, con extremos y pertenencia conocidos. |
| XV · Sin extremos | 50/96 parejas positivas reunidas (k=20 entrante); solo 19/106 ternas recuperadas conjuntamente con PC1. El mejor control ordinal con pertenencia dada depende de una escala dominante. |
| XVI · Segundo banco | 87 semiescalas, 40/353 ternas cubiertas; Fiedler combinado 25,83%, PC1 entrante 39,17%, azar 33,33%. No se reproduce una ventaja robusta. |

**Resultado:** pertenencia, intermediación y orientación son objetivos distintos. La coherencia estructural no equivale a verdad semántica. Se mantienen los resultados negativos y sus límites. No se ha demostrado una ventaja general en grafos semánticos.

## Cómo leerlo

- [Informe principal](docs/INVESTIGACION.md): explicación autónoma, desde intuiciones hasta resultados y límites.
- [Ambigüedad espectral](docs/AMBIGUEDAD_ESPECTRAL.md): criterio de fase, conocimiento previo y órdenes de observación.
- [Robustez y selección de consultas](docs/rgo_fase11_nota.md): demostraciones, censo y simulaciones.
- [Reconstrucción temporal](docs/OBSERVABILIDAD_TEMPORAL.md): criterio exacto y corpus musical.
- [Casos de estudio Q48 y Walsh](docs/rgo_fase10_nota.md): derivaciones algebraicas y predicción cuántica, con las precisiones del registro de correcciones.
- [Correcciones y alcance](docs/CORRECCIONES.md) · [Agenda de investigación](docs/ROADMAP.md) · [Antecedentes](docs/ANTECEDENTES.md).

## Reproducir

Python 3.10 o posterior. Para las auditorías recientes:

```bash
pip install -r requirements-research.txt
python audits/rgo_fase9_audit.py
python audits/rgo_fase10_audit.py
python audits/rgo_fase11_audit.py
```

Los resultados originales están en `results/`. Las tres auditorías matemáticas se ejecutaron nuevamente para v0.3 y sus salidas coinciden exactamente con los JSON guardados. Una comprobación independiente por enumeración directa de subconjuntos verifica también los testigos de minimalidad de la fase XI: [audits/verify_robustness.py](audits/verify_robustness.py).

Para las fases semánticas XII–XVI (Python con SciPy y Node.js 18+), véanse los [comandos y condiciones de reproducción](docs/SEMANTICA.md#conclusión-científica-y-reproducibilidad).

Para la reconstrucción temporal: `python audits/phase_temporal.py` y `python audits/temporal_corpus.py jsb-chorales-quarter.json`. El corpus externo no se redistribuye; su fuente y huella Git se registran en los resultados. Los datos de Bach son los de la ejecución anterior.

## Explorar desde el navegador

[Web principal](https://sgarcia87.github.io/relational-geometry-observability/) · [Laboratorio XI: reconstrucción robusta](https://sgarcia87.github.io/relational-geometry-observability/demos/rgo_fase11.html) · [Laboratorio X: la fase invisible](https://sgarcia87.github.io/relational-geometry-observability/demos/rgo_fase10.html) · [Web v0.2: fase y tiempo](https://sgarcia87.github.io/relational-geometry-observability/archive/v0.2/)

**Estado científico:** investigación abierta, no revisada por pares. La homometría, recuperación de órbitas, biespectro, funciones bent y códigos tienen extensa literatura previa. Los resultados particulares deben contrastarse bibliográficamente; no se reclama prioridad, ventaja cuántica ni superioridad semántica externa. Las fases XII–XVI se documentan en [SEMANTICA.md](docs/SEMANTICA.md).

La v0.1 y la v0.2 se conservan en el historial y en [informes históricos](docs/ANTECEDENTES.md). La licencia sigue pendiente de decisión del autor.
