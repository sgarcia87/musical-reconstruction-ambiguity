# Relational Geometry and Observability (RGO)

**Sergi Garcia Mecinas · v0.6 · 26 November 2026**

🌐 **[Open the RGO website and interactive laboratories](https://sgarcia87.github.io/relational-geometry-observability/)** · [Español](README.md)

**Why do we recognize the same melody in a different key? What information makes it the same music?**

RGO grew from audiovisual harmonographs, frequencies and chord geometry into a mathematical investigation of what observations preserve, which alternative structures remain compatible, and how additional observations can identify them. No knowledge of IA_m, Q48, or earlier projects is required. [Start from the beginning (Spanish)](docs/EMPEZAR.md) · [Musical research XVIII–XIX](docs/MUSICA.md).

## Recent musical experiments

| Experiment | Result and scope |
|---|---|
| XVIII · 382 Bach chorales | Synthetic retrieval from 77 test sources; temporal features outperform local magnitude bags, but chroma alignment is stronger in the hardest condition. Joint pair orbits can preserve relative displacement lost by cross-Fourier measurements (32 transitions). |
| XIX · 297 Irish tune settings, 51 IDs, 10 annotated families | Transposition-invariant temporal trigrams retrieve another setting of the same ID at 79.92% top-1 (288 queries; chance 3.33%). Other-ID family retrieval: 36.03% (297 queries; chance 7.53%). |
| XIX · one representative per ID | Chroma alignment 48.04%, temporal trigrams 33.33%, chance 9.65%. Topological summaries are less effective in this protocol. No audio or timbre experiment. |

[Phase XVIII](docs/rgo_fase18_nota.md) · [Phase XIX](docs/rgo_fase19_nota.md). Distinguish catalog identification from exact reconstruction; these experiments do not establish superiority over existing methods.

[General framework (Spanish)](docs/MARCO_GENERAL.md) · [Mathematical report](docs/INVESTIGACION.md) · [Corrections](docs/CORRECCIONES.md) · [Research agenda](docs/ROADMAP.md)

## Mathematical results

- **Phase ambiguity:** invariant phase relations generate a lattice; its quotient and Smith normal form characterize residual ambiguity modulo translation at fixed support and magnitudes. [Details](docs/AMBIGUEDAD_ESPECTRAL.md).
- **Prior-dependent identification:** among 4,096 initial binary indicators on Z₁₂, 262 require order four over arbitrary real admissible signals, but only 24 over binary candidates. Enumeration extends to cyclic groups of sizes 2–16. Complete moments through order three (nonnegative signals) or four (real signals) certify binary membership and bound distance to some indicator, not identity. [Phase XI](docs/rgo_fase11_nota.md).
- **Robust queries:** given exact spectrum/DC and the specified 19 three-point and 43 four-point translated patterns, universal fixed lists with repetitions require 8h queries for minimum Hamming distance h. [Phase XI](docs/rgo_fase11_nota.md).
- **Temporal reconstruction:** prime-power connectivity determines relative ambiguity when local orbits and selected cross-Fourier products are known. Among 382 Bach chorales, 377 are identified from consecutive relations; six extra links resolve the remaining five. Not reconstruction from audio. [Details](docs/OBSERVABILIDAD_TEMPORAL.md).
- **Q48:** bent-function quotient, GF(4) correspondence and a shared-translation two-copy quantum observable are mathematical case studies, not demonstrations of quantum advantage. [Phase X](docs/rgo_fase10_nota.md).
- **Ordinal observability (XVII):** the full three-outcome median-of-three signature of a strict total order on n≥3 elements, modulo reversal, has exact minimum Hamming distance n−2. Exhaustive minima for six elements: seven fixed queries for identification, ten to detect one substitution and sixteen to correct one, without repetitions. Six adaptive queries suffice in the worst case with an exact oracle; the extension verifies an optimal depth of ten for all 20,160 orders on eight elements. [Proof and audit](docs/rgo_fase17_nota.md) · [Extension](docs/rgo_fase17_extension.md).

## Semantic experiments: evidence and limitations

| Phase | Main result |
|---|---|
| XII | Internal prior-rejection experiment is substantially circular: reserved edges and reference share the annotation source. |
| XIII | Diffraction does not consistently outperform minimum PPR on USF associations with external human rankings. |
| XIV | Incoming-profile projection orders 26/28 internal pairs with known endpoints and gold-membership-informed ablation. |
| XV | Unanchored clustering recovers 50/96 annotated positive pairs, but joint membership and order recovery is only 19/106 triples. A perfect geometric optimum may contradict human order. |
| XVI | Second benchmark, 40/353 strict triples covered: incoming PC1 39.17%, combined Fiedler 25.83%, chance 33.33%. No robust transfer. |
| XVII | The first two pilots yield no covered target triples. The JJGraph extension yields partial coverage but poor validity: with gold membership, 22/87 half-scales are incompatible and only two triples are certified by the main rule, one correct. Empirical axis discovery remains open. |

[Full report and reproducibility details](docs/SEMANTICA.md). These are exploratory tests; association, scale membership, betweenness and orientation are distinct. No claim of general semantic performance.

## Reproduce

```bash
pip install -r requirements-research.txt
python audits/rgo_fase9_audit.py
python audits/rgo_fase10_audit.py
python audits/rgo_fase11_audit.py
python audits/verify_robustness.py
node audits/rgo_fase17_audit.mjs
node audits/rgo_fase17_math.mjs
node audits/rgo_fase17_prior.mjs
node audits/rgo_fase18_audit.mjs
node audits/rgo_fase19_audit.mjs --data ./rgo_data
```

Mathematical audits IX–XI were reproduced exactly for v0.3. XVII was executed exhaustively and its main minima cross-checked with an independent Python/SciPy method. The extension also evaluates published JJGraph paraphrases and a second synthetic prior. External corpora are not bundled; [semantic reproduction commands](docs/SEMANTICA.md#conclusión-científica-y-reproducibilidad) and [XVII data provenance](docs/rgo_fase17_nota.md) describe what was and was not repeated.

[Phase X demo](https://sgarcia87.github.io/relational-geometry-observability/demos/rgo_fase10.html) · [Phase XI demo](https://sgarcia87.github.io/relational-geometry-observability/demos/rgo_fase11.html) · [Phase XV demo](https://sgarcia87.github.io/relational-geometry-observability/demos/rgo_fase15.html) · [Phase XVII demo](https://sgarcia87.github.io/relational-geometry-observability/demos/rgo_fase17.html).

**Status:** open research, not peer-reviewed. The specific results' bibliographic priority is unresolved. Phase retrieval, higher-order correlations, group-action recovery, error-correcting codes and ternary comparison sorting are established areas. No claim of a unified physical theory, quantum advantage, or reliable general semantic-axis discovery. Earlier releases remain in history and [background](docs/ANTECEDENTES.md). License pending author decision.

[Extended ordinal observer](https://sgarcia87.github.io/relational-geometry-observability/demos/rgo_fase17_observador.html) · [JJGraph and eight-element study](docs/rgo_fase17_extension.md).
