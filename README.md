# Relational Geometry and Observability (RGO)

**Geometría relacional y observabilidad** · Investigación de Sergi Garcia Mecinas · v0.1 (25 de noviembre de 2026)

> ¿Qué estructura permanece cuando cambia la perspectiva desde la que la observamos, y qué información necesitamos para distinguir sus estados?

Este proyecto estudia un modelo finito de doce signos, llamado **Q12**, como laboratorio de relaciones, simetría, equilibrio y observación. No hace falta conocer IA_m, teoría musical ni computación cuántica para empezar. El propósito es construir un marco matemático contrastable, no postular una teoría física o una explicación de la consciencia.

**[Leer el informe completo en español](docs/INVESTIGACION.md)** · [English overview](README.en.md) · [Informe HTML para móvil](index.html)

## Qué contiene

| Resultado | Alcance |
|---|---|
| 4096 configuraciones; 48 equilibradas y ortogonales | Demostración combinatoria y enumeración |
| Cuatro clases de hexacordos, dos perfiles de Fourier | Correspondencia exacta bajo una codificación musical explícita |
| Grafo de ortogonalidad, marco ajustado y homología | Cálculos exactos en Q48 |
| 192 mínimos locales no globales | Enumeración de una penalización específica |
| Q48 como subespacio fundamental; separación de orientación y relación | Construcción algebraica; simulación estática en 4096 dimensiones |
| Observadores con 1, 2, 24 o 48 clases; reconstrucción adaptativa | Enumeración exhaustiva y árbol de decisiones |
| Difusión PPR: coherencia aumenta, información sobre la perspectiva disminuye | Experimento reproducible y explicación por procesamiento de datos |
| 382 corales de Bach | Exploración empírica; no evidencia concluyente de privilegio musical de Q48 |

## Reproducir

Python 3.10 o superior. Las auditorías exactas no requieren dependencias externas.

```bash
python audits/music_geometry.py
python audits/observability.py
python audits/energy.py
# Opcional: diagonalización numérica del Hamiltoniano
pip install -r requirements-quantum.txt
python audits/energy.py --quantum
# Corpus externo: usar copia local del JSON o permitir descarga de la fuente
python audits/bach_hexachords.py jsb-chorales-quarter.json
python audits/bach_distance.py jsb-chorales-quarter.json
```

Los resultados del corpus original no se redistribuyen como datos de entrada; se documenta el origen y SHA del archivo utilizado. Los resultados ya calculados están en `results/`. Las ventanas de análisis son exploratorias y se solapan.

## Laboratorios sin instalación

- [CONSONA: señales sinusoidales y relaciones](demos/consona.html)
- [Q12 y música: complementariedad y Bach](demos/q12_musica.html)
- [Anatomía del equilibrio](demos/q12_equilibrio.html)
- [El observador: distinción de estados y difusión](demos/q12_observador.html)

Los laboratorios son material didáctico de distintas fases; las auditorías y el informe son la referencia científica de esta versión.

## Organización

- `docs/INVESTIGACION.md`: informe autónomo, pruebas, antecedentes, resultados, límites y agenda.
- `audits/`: código reproducible; `results/`: salidas y procedencia.
- `demos/`: visualizadores HTML históricos de la investigación; `index.html`: informe para lectura móvil.
- `docs/ROADMAP.md`: próximas pruebas y criterios de falsación.

## Estado del proyecto

Borrador de investigación, no artículo revisado por pares. La conexión con consciencia y realidad material es filosófica; la relevancia musical general, la ventaja cuántica y la generalización a IA_m son hipótesis por evaluar. No se afirma originalidad bibliográfica de resultados combinatorios ya conocidos. La licencia de esta nueva recopilación queda pendiente de decisión del autor; los proyectos y datos de terceros conservan sus condiciones originales.
