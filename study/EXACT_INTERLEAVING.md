# Exact control of repetition interleaving

**Status: hypothesis not supported.**

A follow-up exploratory analysis compared the spatial organization of repeated factors in the 740 Essen interval words with samples from the full repetition-profile control. A strict crossing involves distinct factors A and B, with occurrence starts i < j < l < m in order A–B–A–B and adjacent start differences at least k (non-overlapping interval-factor occurrences).

The numerator counts strict crossings. The denominator is the total number of pairs of occurrence-pairs of distinct factors of length k, whether disjoint or not: sum over unordered distinct factor types of binom(m_A,2) binom(m_B,2). This denominator is fixed by the multiplicity profile. Words with zero denominator are excluded from that order. Means are computed per melody.

The full-corpus constrained-chain analysis gave original-minus-control differences of −2.18 and −1.92 percentage points at k=4 and k=5. This was exploratory: multiple definitions, lengths and representations were inspected; correction within one metric does not control the entire search. The chains start at the original and uniform mixing has not been established.

## Exhaustive check

The follow-up criterion was fixed before enumeration: the proposed direction would receive support only if both exact mean contrasts at k=4 and k=5 were negative. The test reused the tractable subset of 36 Essen words with exact bigram-class cardinality greater than one and at most 10,000, in the original modulo-12 representation.

The program recursively enumerates distinct Eulerian interval words with fixed bigrams and boundaries. Each enumeration count is checked against the exact counter. Only words matching the complete factor-multiplicity histogram and suffix multiplicities are retained, including the original. The control mean is uniform over this finite set. No MCMC is used.

| Order | Eligible words | Original | Exact control | Original − control |
|---|---:|---:|---:|---:|
| 4 | 20 | 7.803% | 6.286% | +1.517 pp |
| 5 | 14 | 4.262% | 3.336% | +0.926 pp |

97,328 bigram-compatible words were enumerated, of which 15,807 satisfy the full profile. Thirty-one of 36 classes have more than one full-profile word. At order 4 the contrast is negative in one melody, positive in four, zero in fifteen; at order 5 it is positive in two and zero in twelve. Among eligible non-singleton classes the mean contrasts are +2.023 and +1.296 pp. The mean minimum reconstruction length is 4.528 in originals and 4.413 in the exact controls, also reversing the full-corpus sampled contrast.

## Interpretation

The exact check does not support the predicted direction. The subset has smaller tractable classes and is not a representative sample of the full corpus. These results therefore do not establish that sampling bias alone causes the reversal, but prevent a claim of a robust musical interleaving regularity. Neither uniform convergence of the full-profile chains nor a causal explanation of reconstruction ambiguity is established. The empirical bigram contrasts and exact counting method are distinct from this failed hypothesis.

## Reproduction

From the study directory:

```sh
node exact_interleaving.mjs --self-test
node exact_interleaving.mjs --data ./essen_data > exact_interleaving_full.json
```

The recorded aggregate results are in [results/exact_interleaving.json](results/exact_interleaving.json). The script emits all 36 individual rows and checks pinned Essen source hashes. Full standalone replay remains pending. The exploratory phase is closed; no further post-hoc metric search is planned.
