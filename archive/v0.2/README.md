# RGO — Geometría relacional y observabilidad

**Relational Geometry and Observability** · Sergi Garcia Mecinas · v0.2 · 25 de noviembre de 2026

🌐 **[Abrir la web oficial de RGO — demostraciones interactivas](https://sgarcia87.github.io/relational-geometry-observability/)**

> ¿Qué información debemos observar para reconstruir una estructura, sin confundir las diferencias relevantes con las que solo dependen de la perspectiva?

Dos objetos pueden tener las mismas magnitudes medidas y, sin embargo, estar organizados de forma diferente. RGO estudia cómo detectar esa ambigüedad y qué relaciones adicionales permiten resolverla. El punto de partida es la geometría de conjuntos finitos; la música proporciona un laboratorio concreto y la reconstrucción de fases cuánticas ofrece un problema matemático relacionado.

**No se necesita conocer IA_m, los trabajos anteriores del autor ni teoría musical para comenzar.**

[Introducción e informe en español](docs/INVESTIGACION.md) · [English overview](README.en.md) · [Nota técnica y demostraciones](docs/OBSERVABILIDAD_TEMPORAL.md)

## Resultados principales

| Problema | Resultado | Evidencia |
|---|---|---|
| ¿Qué distingue dos estructuras con el mismo espectro? | En los 4096 conjuntos de la escala cromática hay 224 clases por transposición e inversión; el espectro distingue 201. Dos productos cúbicos concretos completan la distinción. | Enumeración exacta; enmarcada en literatura de homometría y biespectro. |
| ¿Cómo se relacionan equilibrio, geometría y Fourier? | Q48 son exactamente los hexacordos con F₄=0 y módulo de F₃ al cuadrado igual a 4. Un producto cúbico separa sus cuatro familias. | Demostración y enumeración. |
| ¿Qué se pierde al observar una secuencia? | Fórmula de ambigüedad a partir de componentes conexas de grafos de potencias primas, válida para grupos cíclicos finitos bajo hipótesis explícitas. | Demostración y verificaciones finitas. |
| ¿Cuántas observaciones adicionales hacen falta? | En 382 corales de Bach, con ventanas de cuatro negras, 377 secuencias quedan determinadas usando relaciones consecutivas; seis conexiones adicionales resuelven las cinco restantes. | Resultado empírico condicionado a conocer las órbitas locales y medir correlaciones cruzadas completas. |
| ¿Es suficiente que dos perspectivas se parezcan? | No. La difusión común puede aumentar la similitud mientras reduce la información. Una reducción por simetría, en cambio, puede conservar toda la información sobre el objetivo. | Procesamiento de datos y ejemplo PPR numérico. |

La originalidad bibliográfica de los resultados particulares todavía debe contrastarse. No se propone una teoría física de la realidad ni se afirma ventaja cuántica, reconstrucción de grabaciones, relevancia perceptual especial de Q48 o superioridad frente a métodos musicales existentes.

## Reproducir

Python ≥ 3.10. La auditoría de Fourier y reconstrucción temporal usa únicamente la biblioteca estándar.

```bash
python audits/phase_temporal.py
python audits/temporal_corpus.py jsb-chorales-quarter.json
# Experimento de observabilidad condicionada (requiere NumPy)
pip install numpy
python audits/conditional_observability.py
```

Los datos originales del corpus externo no se redistribuyen. Se indica su fuente y la huella Git en la documentación y en los resultados. Las ventanas son deslizantes y la identificabilidad es condicional, no una prueba de reconocimiento de obras desde audio.

## Lectura y organización

- [Introducción desde cero](docs/INVESTIGACION.md): problema, definiciones, resultados, límites y ejemplos.
- [Nota técnica](docs/OBSERVABILIDAD_TEMPORAL.md): Fourier, biespectro, demostración de la fórmula temporal y protocolo del corpus.
- [Agenda](docs/ROADMAP.md): preguntas abiertas, comparaciones y criterios de rechazo.
- [Apéndice histórico](docs/ANTECEDENTES.md): geometría discreta, energía, cuántica, grafos semánticos y motivación de los trabajos previos.
- `audits/`, `results/`: código y resultados con procedencia.
- `demos/`: laboratorios de etapas anteriores; no sustituyen las demostraciones.

El [informe v0.1](docs/INVESTIGACION-v0.1.md) se conserva como registro histórico. La versión actual lo sustituye como referencia principal.

**Estado:** cuaderno de investigación abierto, no revisado por pares. Licencia pendiente de decisión del autor. Se conservan las condiciones de uso de las fuentes externas.
