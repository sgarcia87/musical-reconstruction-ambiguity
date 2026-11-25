# Relational Geometry and Observability (RGO)

**Sergi Garcia Mecinas · v0.4 · 26 November 2026**

🌐 **[Explore the RGO website — interactive demonstrations (Spanish)](https://sgarcia87.github.io/relational-geometry-observability/)**

[Spanish introduction](docs/INVESTIGACION.md) · [Phase ambiguity and reconstruction](docs/AMBIGUEDAD_ESPECTRAL.md) · [Robust observation note](docs/rgo_fase11_nota.md) · [Corrections and scope](docs/CORRECCIONES.md)

**How much information is required to reconstruct a structure when measurements are partial, ambiguous or erroneous, and how does the answer change with prior knowledge?**

Different objects can share the same Fourier magnitudes. RGO studies the resulting ambiguity, invariant phase relations, conditional reconstruction, and robust selection of observations. Music is a concrete finite test domain; quantum phase observability is a related mathematical application. No knowledge of the author's earlier projects is needed.

## Main findings

- **Phase ambiguity as a quotient:** for a fixed Fourier support and magnitudes, observed invariant phase monomials generate an integer relation lattice. Reconstruction modulo translations is equivalent to completeness of that lattice. Smith normal form characterizes finite and continuous ambiguities. This is a mathematical formulation, not a priority claim.
- **Prior information changes the required order:** of 4,096 binary indicators on Z₁₂, 262 require order four when arbitrary real signals are admissible. Among binary candidates only 24 do. Of the 262 cases, 190 are resolved by order at most two and 48 by order three. Exact enumeration also covers cyclic groups of sizes 2 through 16.
- **Prior certification:** complete moments through order three (nonnegative signals) or four (real signals) certify binarity and provide quantitative distance bounds to some binary indicator. They do not certify the identity of the original structure.
- **Robust query design:** given exact second-order information, consider scalar counts of 19 translated three-point patterns and 43 translated four-point patterns. The minimum universal fixed list length for within-family Hamming distance h is 8h if repetitions are allowed. Thus 8(2e+1) queries correct e arbitrary reading errors in this protocol. A context-dependent four-candidate family needs three fixed queries or two adaptive queries. A good diversified fixed strategy is competitive in exploratory Gaussian-noise simulations.
- **Temporal identifiability:** prime-power connectivity graphs yield an exact count of relative reconstructions, assuming local translation orbits and selected cross-Fourier products are known. On 382 Bach chorales, 377 four-quarter-window pitch-class sequences are identifiable from consecutive relations; six further links resolve the remaining five. This is not audio reconstruction or cover-song recognition.

The 48-state example Q48, bent-function quotient, GF(4) correspondence and two-copy quantum expectation are retained as case studies. The Walsh homometry of the set Q48 is distinct from the pitch-class homometry of an individual subset of Z₁₂. The two-copy result is theoretical and requires estimation of expectation values.

## New research line: semantic observability (phases XII–XVI)

[Full synthesis and corrections (Spanish)](docs/SEMANTICA.md) · [Unanchored axes demo](demos/rgo_fase15.html) · [Second benchmark](docs/rgo_fase16_nota.md).

| Phase | Evidence and scope |
|---|---|
| XII · Wrong priors | Rejection and agreement with the reference are circular in this setup. No independent semantic validation. |
| XIII · External associations | With gold membership and same-scale edges removed, diffraction reaches 58.70% vs minimum PPR 65.22% (46 queries). |
| XIV · Known anchors | Incoming-profile projection orders 26/28 internal pairs after a gold-membership-informed ablation. |
| XV · No anchors | Incoming clustering recovers 50/96 annotated positive pairs; PC1 recovers only 19/106 triples end to end. |
| XVI · Second benchmark | de Melo/Bansal: 87 half-scales, only 40/353 strict triples covered. Incoming PC1 39.17%, combined Fiedler 25.83%, chance 33.33%. No robust transfer. |

Association, scale membership and ordinal betweenness are different targets. Structural coherence does not guarantee semantic truth. Phases XIII–XVI are exploratory and reuse the USF graph. No claim of superiority or semantic generalization.

## Reproduce

Python 3.10+:

```bash
pip install -r requirements-research.txt
python audits/rgo_fase9_audit.py
python audits/rgo_fase10_audit.py
python audits/rgo_fase11_audit.py
python audits/verify_robustness.py
```

The three recent audit outputs were reproduced byte for byte for v0.3. The independent robustness checker uses direct enumeration of actual subsets rather than translated-pattern signatures. Stored outputs are under `results/`. The external Bach dataset is not bundled; its provenance is recorded in the temporal-corpus results.

[Technical documentation](docs/AMBIGUEDAD_ESPECTRAL.md) · [Temporal reconstruction](docs/OBSERVABILIDAD_TEMPORAL.md) · [Research agenda](docs/ROADMAP.md) · [Historical background](docs/ANTECEDENTES.md).

For semantic audits XII–XVI, see [commands and reproducibility limits](docs/SEMANTICA.md#conclusión-científica-y-reproducibilidad). Node.js 18+ and SciPy are required for the respective scripts.

**Status:** open research notebook, not peer-reviewed. Homometry, higher-order correlations, group-action recovery, bent functions, adaptive queries and error-correcting codes are established research areas. Priority of the specific results remains unresolved. No claim of quantum advantage, theory of consciousness, or validated semantic-graph performance. License pending author decision.
