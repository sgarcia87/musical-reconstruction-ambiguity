# Relational Geometry and Observability (RGO)

**Sergi Garcia Mecinas · November 26, 2026**

[Interactive overview (Spanish)](https://sgarcia87.github.io/relational-geometry-observability/) · [Español](README.md)

RGO studies the structures compatible with an observation and the additional relations required to distinguish them.

## Six principles

1. Observation groups candidates into equivalence classes.
2. Prior knowledge provides information.
3. Coherence is not truth.
4. Changing perspective means distinguishing new alternatives.
5. Recognition is not reconstruction.
6. Recording associations is not sufficient to discover meaning.

## Musical reconstruction

For 382 Bach chorales and 51 traditional tunes, exact reconstruction counts were computed from multisets of consecutive pitch-class intervals and known boundaries.

| Corpus | Original | Bigram control | Repetition-profile control |
|---|---:|---:|---:|
| Bach | 6.586 | 5.629 | 6.644 |
| The Session | 11.098 | 6.711 | 11.431 |

Mean minimum fragment length. The original difference largely disappears under the stricter controls. Sampling is not proven to mix uniformly; no additional music-specific effect has been established.

The binary words 0000101 and 0001001 share endpoints, bigrams and factor multiplicity histograms at every length but require fragments of length 3 and 4 respectively for unique reconstruction. The BEST formula separates ambiguity into local permutations and a global connectivity correction.

[Scientific synthesis](docs/SINTESIS_RGO.md) · [Fragment study](docs/ESTUDIO_FRAGMENTOS.md) · [Final repetition study](docs/REPETICIONES.md) · [Audit code](audits/auditoria_repeticiones.mjs) · [Results](results/repeticiones.json) · [Historical archive](docs/ARCHIVO.md).

## Sequence reconstruction and observation selection

- [Mitochondrial DNA](docs/ADN.md): 191 windows of 128/256 bases and exhaustive enumeration of 276 short windows. Repetition-profile controls substantially reduce the observed differences in ambiguity.
- [Query optimization and implicit reconstruction](docs/CONSULTAS.md): exact positional and XOR marginals and adaptive conditioning by dynamic programming. 240,606 count comparisons; complete reconstruction of an initial fiber of 68,557,426,042,230,000 candidates. The local XOR method shows no consistent performance advantage over the tested references.
- [Experiments and reproduction](experiments/) · [Aggregated results](results/consultas.json).

Exploratory research concluded; not peer reviewed. No claim of bibliographic priority.
