# RGO — Geometría relacional y observabilidad

**Sergi Garcia Mecinas · 26 de noviembre de 2026**

[Web interactiva](https://sgarcia87.github.io/relational-geometry-observability/) · [English](README.en.md) · [Síntesis](docs/SINTESIS_RGO.md)

RGO estudia qué estructuras son compatibles con una observación, qué información se pierde al representarlas y qué relaciones permiten distinguirlas. El punto de partida es la geometría musical y la invariancia por transposición.

## Seis principios

1. Observar es agrupar.
2. El conocimiento previo aporta información.
3. Coherencia no equivale a verdad.
4. Cambiar de perspectiva significa distinguir nuevas alternativas.
5. Reconocer no equivale a reconstruir.
6. Registrar asociaciones no basta para descubrir significado.

## Estudio final: repeticiones y reconstrucción musical

Se analizaron 382 corales de Bach y 51 melodías tradicionales de The Session, como secuencias de intervalos módulo 12. Se cuenta exactamente el número de reconstrucciones compatibles con todos los fragmentos de longitud k y sus fronteras.

| Corpus | Original | Control de transiciones | Control de repeticiones |
|---|---:|---:|---:|
| Bach | 6,586 | 5,629 | 6,644 |
| The Session | 11,098 | 6,711 | 11,431 |

Longitud mínima media en intervalos. El control reforzado conserva además el perfil de multiplicidades de fragmentos y de sufijos. La diferencia inicial de ambigüedad entre originales y controles de transiciones se reduce sustancialmente. No se ha demostrado un efecto musical adicional. Las propuestas de intercambio no garantizan mezcla ni muestreo uniforme.

Las palabras **0000101** y **0001001** comparten bigramas y perfil de multiplicidades de fragmentos de todas las longitudes, pero necesitan respectivamente fragmentos de longitud 3 y 4 para una reconstrucción única con fronteras conocidas. El perfil no determina la reconstruibilidad.

La fórmula BEST permite separar la ambigüedad en dos términos: H = L + G, donde L cuenta las ordenaciones locales en bits y G ≤ 0 expresa la compatibilidad global mediante arborescencias dirigidas. Es una reescritura de un resultado conocido.

[Estudio de fragmentos](docs/ESTUDIO_FRAGMENTOS.md) · [Repeticiones y observabilidad](docs/REPETICIONES.md) · [Resultados](results/repeticiones.json)

## Documentación

- [Síntesis científica](docs/SINTESIS_RGO.md)
- [Resultados matemáticos](docs/INVESTIGACION.md) y [marco general](docs/MARCO_GENERAL.md)
- [Antecedentes](docs/ANTECEDENTES.md) y [referencias del estudio final](docs/REPETICIONES.md#referencias)
- [Correcciones y límites](docs/CORRECCIONES.md)
- [Archivo histórico](docs/ARCHIVO.md) · [Portada anterior](archive/v0.6.1/)

## Reproducción

Node.js 18+ y Python 3.

```bash
python audits/verify_repetition_profiles.py
node audits/auditoria_repeticiones.mjs --self-test
node audits/auditoria_repeticiones.mjs --data ./rgo_data --simple > simple.json
node audits/auditoria_repeticiones.mjs --data ./rgo_data > strict.json
```

Los corpus externos se verifican por SHA-1 de blob Git. Los JSON publicados son agregados de las ejecuciones, no datos brutos. El código de auditoría permite generar filas por pieza. No se redistribuyen los corpus.

Investigación exploratoria concluida; no revisada por pares. La prioridad bibliográfica de los resultados particulares no está establecida. Licencia pendiente de decisión del autor.
