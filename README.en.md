# Relational Geometry and Observability (RGO)

**Sergi Garcia Mecinas · v0.6.1**

[**Interactive website**](https://sgarcia87.github.io/relational-geometry-observability/) · [Español](README.md) · [Introduction (Spanish)](docs/EMPEZAR.md)

## What makes a melody remain the same?

RGO grew from the geometry of musical frequencies and chords. Its central question is what information observations preserve, which alternative structures remain indistinguishable, and which additional relationships identify them. No knowledge of the author's earlier projects is required.

**Established under explicit mathematical assumptions:** phase-ambiguity criteria, conditional temporal reconstruction and minimum observation counts.

**Limits:** temporal fingerprints are useful in symbolic music but have not generally outperformed chroma alignment. The tested topological and semantic discovery hypotheses were not validated.

**Open question:** when do invariant temporal fingerprints provide better identification, robustness or cost than sequence alignment?

## Musical research

| Experiment | Result |
|---|---|
| 382 Bach chorales, 462 synthetic queries | For quarter-length excerpts with edits and deletions, multilag temporal signatures achieve 75.32% top-1 versus 91.56% for chroma alignment. |
| 297 traditional tune settings, 51 IDs, 10 annotated families | Invariant trigrams retrieve another setting of the same ID at 79.92% top-1 (288 queries; chance 3.33%). |
| Family retrieval across different tune IDs | Trigrams reach 36.03% (297 queries; chance 7.53%). With one representative per ID, alignment reaches 48.04% vs 33.33% for trigrams. |

These are exploratory symbolic-music experiments, not audio recognition. See [musical research](docs/MUSICA.md), [phase XVIII](docs/rgo_fase18_nota.md) and [phase XIX](docs/rgo_fase19_nota.md) for protocols, comparisons and full results.

## Mathematical results

| Result | Scope |
|---|---|
| Phase ambiguity | A lattice quotient and Smith normal form characterize residual ambiguity at fixed support and magnitudes, modulo translation. [Proof](docs/AMBIGUEDAD_ESPECTRAL.md). |
| Model constraints | Of 4,096 initial pitch-class indicators, 262 need fourth-order observations over arbitrary real candidates, but only 24 over binary candidates. [Details](docs/rgo_fase11_nota.md). |
| Robust reconstruction | Under the specified exact-spectrum music protocol, universal fixed lists of 8, 16 and 24 queries suffice and are minimal for identification, detection of one substitution and correction of one, respectively, with repetitions allowed. [Proof](docs/rgo_fase11_nota.md). |
| Temporal reconstruction | A connectivity criterion counts ambiguity when local orbits are known. 377/382 Bach chorales are identified by consecutive four-quarter-window relations; six extra links resolve the remaining five. [Proof](docs/OBSERVABILIDAD_TEMPORAL.md). |
| Relative information | Joint pair orbits can retain relative shifts lost by cross-Fourier observations: 32 of 18,094 Bach transitions. [Extension](docs/rgo_fase18_nota.md). |

[General framework](docs/MARCO_GENERAL.md) · [Mathematical report](docs/INVESTIGACION.md) · [Secondary mathematical study: betweenness and orders](docs/rgo_fase17_nota.md).

## Reproduce

```bash
pip install -r requirements-research.txt
python audits/rgo_fase9_audit.py
python audits/rgo_fase10_audit.py
python audits/rgo_fase11_audit.py
python audits/verify_robustness.py
node audits/rgo_fase18_audit.mjs
node audits/rgo_fase19_audit.mjs --data ./rgo_data
```

Python 3.10+, Node.js 18+. External datasets are not redistributed. Audits IX–XI were reproduced exactly in v0.3; XVIII–XIX were executed on the retrieved original datasets without repeating the full download in the local container. [Code](audits/) · [Results](results/) · [Research agenda](docs/ROADMAP.md) · [Corrections](docs/CORRECCIONES.md) · [Scientific archive, exploratory and negative results](docs/ARCHIVO.md).

**Status:** open, not peer-reviewed research. Phase retrieval, homometry, musical geometry, codes and seriation have established prior literature. Priority of the specific results remains unresolved. Project license pending author decision.
