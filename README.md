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

## Repeticiones y reconstrucción musical

Se analizaron 382 corales de Bach y 51 melodías tradicionales de The Session, como secuencias de intervalos módulo 12. Se cuenta exactamente el número de reconstrucciones compatibles con todos los fragmentos de longitud k y sus fronteras.

| Corpus | Original | Control de transiciones | Control de repeticiones |
|---|---:|---:|---:|
| Bach | 6,586 | 5,629 | 6,644 |
| The Session | 11,098 | 6,711 | 11,431 |

Longitud mínima media en intervalos. El control reforzado conserva además el perfil de multiplicidades de fragmentos y de sufijos. La diferencia inicial de ambigüedad entre originales y controles de transiciones se reduce sustancialmente. No se ha demostrado un efecto musical adicional. Las propuestas de intercambio no garantizan mezcla ni muestreo uniforme.

Las palabras **0000101** y **0001001** comparten bigramas y perfil de multiplicidades de fragmentos de todas las longitudes, pero necesitan respectivamente fragmentos de longitud 3 y 4 para una reconstrucción única con fronteras conocidas. El perfil no determina la reconstruibilidad.

La fórmula BEST permite separar la ambigüedad en dos términos: H = L + G, donde L cuenta las ordenaciones locales en bits y G ≤ 0 expresa la compatibilidad global mediante arborescencias dirigidas. Es una reescritura de un resultado conocido.

[Estudio de fragmentos](docs/ESTUDIO_FRAGMENTOS.md) · [Repeticiones y observabilidad](docs/REPETICIONES.md) · [Resultados](results/repeticiones.json)

## Reconstrucción y selección de observaciones

| Estudio | Resultado |
|---|---|
| [ADN mitocondrial](docs/ADN.md) | 191 ventanas de 128/256 bases; el control de repeticiones reduce la diferencia de ambigüedad frente al control de transiciones. Enumeración adicional de 276 ventanas cortas. |
| [Consultas óptimas](docs/CONSULTAS.md#optimización-explícita) | 1.160 clases binarias; el coste medio óptimo baja de 2,2932 a 2,2289 al admitir XOR de coste unitario. |
| [Selección implícita](docs/CONSULTAS.md#conteo-implícito) | Marginales exactos sin enumerar palabras; 0,97812 bits medios frente a 0,97534 del muestreo. |
| [Reconstrucción adaptativa](docs/CONSULTAS.md#condicionamiento-adaptativo) | 240.606 verificaciones de conteos; reconstrucción de fibras de hasta 68.557.426.042.230.000 candidatos. La restricción de alcance acota los estados de paridad. No se ha establecido una ventaja general de rendimiento. |

[Código y reproducción](experiments/) · [Resultados ADN](results/adn.json) · [Resultados de consultas](results/consultas.json) · [Recorridos adaptativos](results/adaptive_local.json).

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
node audits/auditoria_repeticiones.mjs --data ./rgo_data --fragments > fragmentos.json
node audits/auditoria_repeticiones.mjs --data ./rgo_data --simple > simple.json
node audits/auditoria_repeticiones.mjs --data ./rgo_data > strict.json
```

Los corpus externos se verifican por SHA-1 de blob Git. Se publican agregados de ejecución y los recorridos individuales del ensayo adaptativo local. El código de auditoría permite generar filas por pieza. No se redistribuyen los corpus.

Investigación exploratoria concluida; no revisada por pares. La prioridad bibliográfica de los resultados particulares no está establecida. Licencia pendiente de decisión del autor.
