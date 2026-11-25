# Relational Geometry and Observability (RGO)

**Sergi Garcia Mecinas · v0.2 · 25 November 2026**

🌐 **[Explore the RGO website — interactive demonstrations (Spanish)](https://sgarcia87.github.io/relational-geometry-observability/)**

**How much information is needed to reconstruct a relational structure, while discarding differences that are irrelevant to the task?**

No knowledge of the author's previous projects is required. RGO is an open research notebook about finite structures, symmetry, phase retrieval, conditional identifiability and information-preserving observations. Music is a concrete test domain, not an assumption about the nature of reality.

[Standalone introduction (Spanish)](docs/INVESTIGACION.md) · [Technical note and proofs (Spanish)](docs/OBSERVABILIDAD_TEMPORAL.md)

## Main findings

- **Static observations:** the 4,096 binary pitch-class sets on Z₁₂ form 224 transposition/inversion classes. Power spectra distinguish 201. Two selected real cubic Fourier products, combined with the power spectrum, separate all 224 classes. Minimality is restricted to the tested dictionary of 12 nonconstant cubic products.
- **A small structured example:** Q48 contains exactly the six-element sets satisfying F₄ = 0 and squared modulus of F₃ = 4. This is equivalent to the balanced, pairwise orthogonal sign rows of a 3 × 4 CRT array. A single bispectrum coefficient identifies the four Q48 set classes.
- **Temporal identifiability:** given local translation orbits and selected complex cross-Fourier products, construct graphs at each prime-power divisor of n. Their connected components determine the exact number of compatible reconstructions modulo a common translation. The technical note states and proves the criterion.
- **Corpus illustration:** among 382 JSB chorales, using four-quarter-note sliding unions, 377 pitch-class sequences are determined by consecutive full cross-correlations and known local orbits. Six additional nonconsecutive edges suffice for the remaining five pieces; the graph lower bound is attained. This does not reconstruct audio, register, voice leading or performance.
- **Conditional observability:** a common diffusion can increase coherence while losing information about its source. When a channel is equivariant and the target is invariant, the appropriate orbit statistic can instead remove nuisance orientation without additional loss of target information.

Phase retrieval, homometry, bispectral invariants and synchronization have extensive prior literature. Priority of the particular results reported here has not been established. Quantum phase synchronization is a mathematical analogue, not a demonstrated physical mechanism or quantum advantage. Testing semantic graphs is future work.

## Reproduce

Python 3.10+.

```bash
python audits/phase_temporal.py
python audits/temporal_corpus.py jsb-chorales-quarter.json
pip install numpy
python audits/conditional_observability.py
```

The external corpus is not bundled. Recorded outputs and provenance are under `results/`. The historical experiments and earlier work are retained in [the appendix](docs/ANTECEDENTES.md) and [v0.1](docs/INVESTIGACION-v0.1.md), not presented as the main scientific claim.

**Status:** working research, not peer-reviewed. License pending author decision.
