# Ambigüedad estructural y longitud mínima de observación en secuencias musicales

26/11/2026 · Estudio exploratorio

## Representación

Para clases de altura p₀,…,pₙ, xᵢ=(pᵢ₊₁−pᵢ) mod 12. Dₖ es el multiconjunto de todos los fragmentos consecutivos de k intervalos. La observación incluye los extremos de longitud k−1. Nₖ cuenta palabras compatibles; Hₖ=log₂ Nₖ; k_min es el primer k con Nₖ=1. Los intervalos determinan las alturas módulo transposición, no ritmo, octavas, timbre ni polifonía.

Para k≥2 se construye el multigrafo de De Bruijn. Cada k-grama es una arista del prefijo al sufijo. Una reconstrucción es un recorrido euleriano con aristas idénticas indistinguibles. El recuento por BEST y matriz-árbol se desarrolla en [REPETICIONES.md](REPETICIONES.md). Para k=1 se emplea el multinomial. Con fronteras, la observación de orden k+1 determina la de k. Sin fronteras, los grados desequilibrados fuerzan los extremos; si el grafo es equilibrado, N_libre=N_fijo (n−k+1)/d_s. Se cuentan palabras lineales.

## Datos y controles

382 corales JSB (77 test, 229 train, 76 valid); nota más aguda de cada instante no vacío, clase de altura, conservando repeticiones. No es una extracción fiable de soprano. Longitud media: 59,393 intervalos.

The Session / Polifonia: 315 transcripciones ABC, 297 utilizables mediante parser limitado, 51 melodías (menor ID de transcripción), diez familias. No se expanden repeticiones ni se preservan duraciones, registro, silencios o adornos. Longitud media: 142,431 intervalos.

12 realizaciones por pieza de cada control (20.784 en total): permutación de notas interiores, permutación de intervalos, bigramas de notas, bigramas de intervalos. Los dos últimos usan arborescencias de últimas salidas con paseos aleatorios y ordenaciones de aristas. Medias por pieza y después por corpus.

## Resultados de la primera ejecución

| Secuencia | Bach | The Session |
|---|---:|---:|
| Original | 6,5864 | 11,0980 |
| Notas permutadas | 4,4396 | 5,3186 |
| Intervalos permutados | 5,1710 | 5,4739 |
| Bigramas de notas | 5,4378 | 6,4477 |
| Bigramas de intervalos | 5,6228 | 6,6650 |

| k | Bach real | Bach bigramas | Session real | Session bigramas |
|---:|---:|---:|---:|---:|
| 1 | 140,9051 | 140,9051 | 409,7733 | 409,7733 |
| 2 | 71,6933 | 71,6933 | 224,2000 | 224,2000 |
| 3 | 24,5521 | 30,7329 | 94,2653 | 123,7481 |
| 4 | 7,5843 | 9,8793 | 36,0667 | 47,3394 |
| 6 | 1,1154 | 0,6108 | 7,8162 | 2,5249 |
| 8 | 0,3050 | 0,0733 | 2,5052 | 0,0281 |

Ambigüedad media en bits. La igualdad en k=1,2 es por construcción. La inversión es agregada, no necesariamente presente en cada pieza.

### Sensibilidad

| Corpus | Extremos conocidos: real/control | Sin extremos: real/control |
|---|---|---|
| Bach original | 6,586/5,624 | 6,586/5,625 |
| Bach, repeticiones colapsadas | 5,634/5,105 | 5,636/5,108 |
| Session original | 11,098/6,694 | 11,098/6,694 |
| Session, repeticiones colapsadas | 10,922/6,850 | 10,922/6,850 |

10.392 controles adicionales; las dos convenciones de extremos comparten controles. El efecto en Bach disminuye al colapsar repeticiones. No se calcularon valores p ni se empleó corpus reservado.

## Conclusión

La hipótesis de que la música necesita menos longitud para lograr unicidad no se sostiene en estos datos. El estudio posterior de perfiles de repeticiones explica descriptivamente gran parte de la diferencia. Véase [REPETICIONES.md](REPETICIONES.md).

## Fuentes de datos

- czhuang/JSB-Chorales-dataset: jsb-chorales-quarter.json, blob ff93746647d1f5af2f719d235329c294267f3088.
- polifonia-project/folk_ngram_analysis: FoNN/SIATEC_comparison/data/thesession_subset_metadata_with_tune_family_annotation.csv, blob 9f172a30b41b48398d6aa0b0e48b40b94bf093dc.

Los corpus externos no se redistribuyen. Los resultados originales se registraron como agregados. El ensayo final y el criterio de unicidad disponen de [auditoría](auditoria_repeticiones.mjs).

## Reproducción

```bash
node auditoria_repeticiones.mjs --self-test
node auditoria_repeticiones.mjs --data ./rgo_data --fragments > fragmentos.json
```

El modo de fragmentos ejecuta los cuatro controles y el análisis de sensibilidad con las semillas documentadas. [Agregados de la primera ejecución](results/fragmentos.json).
