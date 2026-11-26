# RGO — Geometría relacional y observabilidad

**Relational Geometry and Observability · Sergi Garcia Mecinas · v0.6.1**

[**Web interactiva**](https://sgarcia87.github.io/relational-geometry-observability/) · [English](README.en.md) · [Empezar desde cero](docs/EMPEZAR.md)

## ¿Qué hace que una melodía siga siendo la misma?

Podemos reconocer una melodía en otra tonalidad. Pero si cambiamos sus notas o su orden, puede convertirse en otra. ¿Qué información distingue ambas situaciones? RGO nació estudiando las frecuencias y la geometría musical y desarrolla herramientas matemáticas para saber qué información conserva una observación, qué alternativas deja abiertas y cómo resolverlas.

No requiere conocer proyectos anteriores del autor.

**Demostrado:** criterios de ambigüedad de fase, reconstrucción temporal condicionada y mínimos de observación bajo protocolos finitos.

**Límites:** las huellas temporales son útiles en música simbólica, pero todavía no superan de forma general a la alineación cromática. Los ensayos de topología y descubrimiento semántico no validaron las hipótesis generales probadas.

**Pregunta abierta:** ¿en qué condiciones una huella temporal invariante ofrece mejor identificación, robustez o coste que la alineación de secuencias?

## 1. Investigación musical

Se comparan descriptores de magnitudes espectrales, relaciones temporales de notas y acordes, y métodos de alineación. Un descriptor que reconoce una pieza dentro de un catálogo no necesariamente contiene toda la información necesaria para reconstruirla.

| Experimento | Resultado |
|---|---|
| 382 corales de Bach, 462 consultas sintéticas | En fragmentos del 25% con alteraciones y eliminaciones, las relaciones multilag alcanzan 75,32% de identificación top-1; la alineación cromática, 91,56%. |
| 297 transcripciones tradicionales, 51 IDs, 10 familias | Trigramas invariantes: 79,92% al recuperar otra transcripción del mismo ID (288 consultas; azar 3,33%). |
| Parentesco entre melodías de IDs diferentes | 36,03% con trigramas (297 consultas; azar 7,53%). En un control con 51 representantes, alineación 48,04% frente a trigramas 33,33%. |

Son estudios exploratorios sobre partituras simbólicas, no grabaciones. Todavía no se ha probado invariancia frente a timbre o interpretación acústica. Los protocolos, comparaciones y resultados completos están en [investigación musical](docs/MUSICA.md), [fase XVIII](docs/rgo_fase18_nota.md) y [fase XIX](docs/rgo_fase19_nota.md).

## 2. Resultados matemáticos

| Resultado | Alcance |
|---|---|
| Ambigüedad de fase | Retículos de relaciones y forma normal de Smith para calcular ambigüedad con soporte y magnitudes fijados, módulo traslación. [Demostración](docs/AMBIGUEDAD_ESPECTRAL.md). |
| Efecto del modelo | De los 4096 conjuntos de notas de la escala cromática, 262 necesitan observaciones de orden cuatro si se admiten señales reales arbitrarias; solo 24 si se restringen a indicadores binarios. [Detalle](docs/rgo_fase11_nota.md). |
| Reconstrucción resistente a errores | Para el diccionario musical y espectro exacto especificados, 8, 16 y 24 consultas son los mínimos universales para identificar, detectar un error y corregir uno (con repeticiones permitidas). [Demostración](docs/rgo_fase11_nota.md). |
| Reconstrucción temporal | Un criterio de conectividad cuenta las ambigüedades de una secuencia con órbitas locales conocidas. En 382 corales, 377 son identificables mediante correlaciones consecutivas de ventanas de cuatro negras; seis enlaces adicionales resuelven las cinco restantes. [Criterio](docs/OBSERVABILIDAD_TEMPORAL.md). |
| Información relativa | La órbita conjunta de dos ventanas puede conservar desplazamientos que las correlaciones cruzadas pierden: 32 de 18.094 transiciones del corpus de Bach. [Extensión](docs/rgo_fase18_nota.md). |

[Marco matemático](docs/MARCO_GENERAL.md) · [Informe y demostraciones](docs/INVESTIGACION.md) · [Extensión matemática a órdenes e intermediación](docs/rgo_fase17_nota.md).

## 3. Explorar

- [Dos acordes, mismas mediciones](https://sgarcia87.github.io/relational-geometry-observability/#ejemplo): por qué observar no basta.
- [Reconstrucción robusta](https://sgarcia87.github.io/relational-geometry-observability/demos/rgo_fase11.html): experimentar con errores.
- [Fase y tiempo](https://sgarcia87.github.io/relational-geometry-observability/archive/v0.2/): relaciones entre ventanas musicales.

## 4. Reproducir y consultar

```bash
pip install -r requirements-research.txt
python audits/rgo_fase9_audit.py
python audits/rgo_fase10_audit.py
python audits/rgo_fase11_audit.py
python audits/verify_robustness.py
node audits/rgo_fase18_audit.mjs
node audits/rgo_fase19_audit.mjs --data ./rgo_data
```

Python 3.10+ y Node.js 18+. Los corpus externos no se redistribuyen: los scripts musicales comprueban las huellas de los archivos originales. Las auditorías IX–XI se reprodujeron exactamente en v0.3; XVIII–XIX se ejecutaron sobre los corpus recuperados, sin repetir la descarga completa desde el contenedor local. [Código](audits/) · [Resultados](results/).

[Agenda musical](docs/ROADMAP.md) · [Correcciones y límites](docs/CORRECCIONES.md) · [Archivo científico: antecedentes, cronología y líneas no prioritarias](docs/ARCHIVO.md).

**Estado:** investigación abierta, no revisada por pares. La recuperación de fase, la homometría, la geometría musical, los códigos y la seriación tienen antecedentes establecidos. La prioridad bibliográfica de los resultados particulares está pendiente. Licencia del proyecto pendiente de decisión del autor.
