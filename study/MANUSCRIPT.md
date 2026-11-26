# How many fragments determine a melody? Reconstruction ambiguity in folk songs and chorales

Sergi Garcia Mecinas — Independent researcher, Spain

Revised manuscript draft · 26 November 2026

## Abstract

The distribution of short melodic patterns is widely used to characterize symbolic music, yet it does not necessarily determine the order of an entire melody. We investigate reconstruction ambiguity from complete multisets of consecutive pitch-class intervals and known boundaries using established results on k-abelian equivalence and Eulerian trails. An exploratory analysis of 382 Bach chorales and 51 traditional tunes is followed by a validation study of 740 melodies from four collections of the Essen Folksong database. In the validation data, the mean minimum fragment length required for unique reconstruction is 5.984 intervals, compared with 5.228 in controls preserving interval bigrams. Mean log-cardinality is lower in the originals at fragment lengths three and four, but higher at six and eight. Controls additionally preserving factor-multiplicity profiles and suffix multiplicities reduce the absolute difference in mean minimum length by 88.9%, and the aggregate absolute difference across these four ambiguity scales by 96.6%. Graduated controls preserving repetition profiles only through length three attenuate the mean minimum-length contrast by 94.6% in a separate control run, but increase the absolute contrasts at orders six and eight. Preserving the profiles through longer lengths attenuates these late contrasts. The minimum and the ambiguity curve therefore distinguish different aspects of the representation. Estimates remain subject to limitations of constrained sampling. An exploratory strict-interleaving contrast was not supported by exhaustive enumeration on a tractable subset of 36 Essen melodies. The contribution is an empirical application of word-combinatorial reconstruction measures to melodic structure.

**Keywords:** symbolic music; melodic intervals; k-abelian equivalence; de Bruijn graphs; repetition; reconstruction ambiguity.

## 1. Introduction

A pitch sequence can be represented by a collection of local patterns that is invariant under transposition. Such a representation can support similarity or identification within a reference catalogue, while remaining compatible with multiple sequences outside that catalogue. We examine this distinction by counting the possible reconstructions of a melody from its full collection of overlapping, unordered fragments.

Fixed-length interval n-grams have a long history in symbolic music retrieval. Downie (1999) treated collections of signed pitch-interval n-grams of lengths four to six as retrieval terms; subsequent work compared n-gram matching and alignment (Uitdenbogerd and Zobel, 2002). Melodic feature systems such as FANTASTIC include interval and pattern statistics (Müllensiefen, 2009). Variable-order models such as IDyOM use sequential context for statistical prediction (Pearce, 2018). Retrieval, prediction and exact reconstruction have distinct success criteria. Our representation-specific measure quantifies how many words share a complete multiset of fixed-length interval fragments with known boundaries. This helps characterize the loss of order when such a representation is used as a descriptor. The study does not evaluate those systems directly: it cannot establish a general bound on IDyOM, FANTASTIC, perceptual similarity or retrieval accuracy. Likewise, shared local patterns can occur in distinct melodies, a distinction relevant to research on melodic similarity and copyright (Müllensiefen and Pendzich, 2009), but a reconstruction count does not establish copying or legal infringement.

The underlying mathematical problem is established in combinatorics on words and sequence assembly. Karhumäki, Saarela and Zamboni (2013) introduced the relevant family of equivalence relations; Karhumäki et al. (2017) investigated class cardinalities and singleton classes through de Bruijn graphs. Cassaigne et al. (2017) characterized equivalence through k-switching. Related work in sequence assembly addresses the ambiguity introduced by repeated substrings (Bresler et al., 2013). We use these results to examine melodic interval sequences at successive fragment lengths and compare them with randomized controls preserving increasingly detailed statistics.

The exploratory analyses suggested a scale-dependent crossover: original melodies had fewer compatible reconstructions at short fragment lengths, but more at larger lengths, than controls preserving bigrams. The present study examines whether this pattern recurs in a separate collection and whether matching repetition profiles attenuates it. The mathematical counting method is established; the focus is the empirical comparison across musical collections.

## 2. Methods

### 2.1. Observation and ambiguity

Represent a monophonic melody as a sequence of pitch classes p_0,...,p_n in Z/12Z. Define its interval word x_i=(p_(i+1)-p_i) mod 12. It determines the pitch-class sequence up to global transposition. Rhythm, register, polyphony and expressive performance are outside this representation.

For a word x of length n, let c_k(w) count occurrences of factor w of length k, and let s and t be the prefix and suffix of length k−1. The observation O_k(x) consists of the full factor multiset and these boundaries. Let F_k(x) denote the set of length-n words having this observation. For n≥k, this is the k-abelian equivalence class of x. Define

    N_k(x) = |F_k(x)|,
    H_k(x) = log2 N_k(x),
    k_min(x) = min {k : N_k(x)=1}.

H_k is log-cardinality; it equals entropy only under a uniform distribution over compatible words. The observations are nested because the order-(k+1) counts and boundaries determine the order-k counts and boundaries. The minimum can consequently be found by bisection. The model assumes noiseless, complete factor multisets, including exact multiplicities and boundaries.

### 2.2. Exact counting

For k≥2, form the directed multigraph with (k−1)-factors as vertices and k-factors as edges. A reconstruction is an Eulerian trail from s to t. Let m_uv denote edge multiplicity, d_v the outgoing degree, and tau_t the number of directed spanning arborescences toward t counting labelled parallel edges. The last-exit-tree form of the BEST theorem gives

    N_k = tau_t * product_v (d_v - 1 + indicator[v=t])! / product_(u,v) m_uv!.

The factorial denominator removes the labelling of indistinguishable repeated edges. The directed matrix-tree theorem evaluates tau_t. Determinants are evaluated with exact integer arithmetic; forced last-exit choices are contracted. The multinomial gives N_1. The same formula can be written

    N_k = (product_v d_v! / product_(u,v) m_uv!)
          * (tau_t / product_(v != t) d_v),
    H_k = L_k + G_k.

The first factor describes local exit orderings and the second describes their global compatibility. The latter is at most one; its logarithm G_k is non-positive. If F_j = sum_w log2(c_j(w)!), then L_k = F_(k−1) − F_k − log2(c_(k−1)(t)). Thus the strengthened profile introduced below fixes L_k without fixing G_k. For k=1, L_1=H_1 and G_1=0.

For the minimum, the implementation uses the established k-switching characterization: a nontrivial interchange of segments between matching (k−1)-contexts certifies non-uniqueness. It verifies the switch-based minimum against exact counts at k_min and k_min−1 for every validation melody. The counter was also compared with exhaustive enumeration of binary words through length nine for observations with and without known boundaries (16,388 comparisons, no discrepancy).

### 2.3. Corpus design

The exploratory data comprise 382 JSB chorales and 51 distinct tune IDs from a published subset of The Session. The highest pitch at each nonempty quarter-note instant is taken for Bach; The Session contributes one ABC transcription per tune ID. These are symbolic approximations rather than uniform full-score representations. All intervals are reduced modulo 12, with consecutive repeated notes retained.

Validation uses four ABC files from the Essen Folksong Collection as distributed by music21: altdeu10, ballad10, erk10 and kinder0 (Schaffrath, 1995). They contain 1,296 transcriptions. A restricted parser reads written monophonic pitch events with key signatures and bar-local accidentals, omits rests and durations, and does not expand repeats. Tied notes and unsupported notation are excluded. The minimum is 16 note events. Within each source file, the first eligible representative of a catalogue stem is retained, and exact interval-word duplicates across files are excluded. This yields 740 melodies (mean length 44.605 intervals).

| Collection | Available | Retained |
|---|---:|---:|
| altdeu10 | 313 | 223 |
| ballad10 | 107 | 31 |
| erk10 | 663 | 296 |
| kinder0 | 213 | 190 |
| Total | 1296 | 740 |

Exclusions: 474 catalogue-family variants, 65 transcriptions with ties, 7 short melodies and 10 exact duplicates. The four files are a convenience subset, not a random sample of the complete Essen database. An audit of complete interval words found no exact matches between the three corpora (including transpositions, removed by the interval representation). The 382 Bach records contain 344 distinct interval words; their exploratory summaries retain all 382 records, and thus are not summaries of independent compositions. Related but nonidentical tunes may occur across corpora. In an independent parser comparison, abcjs-basic 6.7.3 (Git blob 0631d3b91887d149458989f5b37b8f19c09dc725) reproduced all 33,748 written pitch-class events across the selected 740 Essen melodies, with no differences in note counts or interval words and no parser warnings. Its MIDI engine was applied after neutralizing repeat barlines, with note events sorted by their source positions. The comparison verifies the included Essen records, not excluded records or the earlier corpus parsers.

### 2.4. Matched controls

Each original is paired with twelve realizations of each control.

**Bigram control.** The complete interval-bigram multiset and endpoints are held fixed. An arborescence of last exits is sampled via loop-erased random walks, followed by random ordering of remaining exits. This produces the uniform distribution over compatible trails in the ideal random-number model, after identifying indistinguishable edges.

**Strengthened repetition-profile control.** In addition to bigrams and endpoints, hold fixed the histogram of factor multiplicities at every length and the multiplicity of the suffix at every length. For fixed n, the number of singleton factors is determined by the histogram of multiplicities at least two. A symmetric proposal uses interchanges of consecutive segments with matching endpoint symbols: either three positions with the same symbol, or two interleaved pairs of equal-symbol positions. A proposed change is accepted only if the strengthened profile is unchanged. Each chain starts at the original word, runs for 1,800 proposals, discards the first 600 and records states every 100 proposals. Twelve states are retained, including unchanged or repeated words. The proposal symmetry provides a uniform stationary distribution within a connected component in the ideal random-number model; neither irreducibility across the whole constrained space nor convergence is established.

The code verifies all control invariants, including equality of the local term L_k in the strengthened control for each evaluated order. Results are averaged first over controls within each melody, then across melodies. The xorshift32 seed is 261126 + 10007 i for melody index i (zero-based), with the bigram draws following the constrained chain.

### 2.5. Validation contrasts

The directions were fixed before computing the validation results (not formally preregistered): (H1) mean k_min is larger in the originals than in the bigram controls; (H2) the mean difference of H_k is negative at k=3 and 4 and positive at k=6 and 8; (H3) matching the strengthened profile attenuates the differences. A 75% attenuation threshold was adopted before computation. For H3 the attenuation measures are

    A_K = 1 - |mean(k_original - k_profile)| / |mean(k_original - k_bigram)|,
    A_H = 1 - sum_{k in {3,4,6,8}} |mean(H_original - H_profile)|
              / sum_{k in {3,4,6,8}} |mean(H_original - H_bigram)|.

These are aggregate measures: they are not averages of individual attenuation ratios and do not establish causal sufficiency. Orders 5, 7, 10 and 12 are additional descriptive comparisons. The validation uses 4,000 cluster bootstrap draws grouped by normalized song title (709 groups; seed 1162026), resampling entire groups and averaging the melodies within the resulting sample. The reported 95% percentile intervals are conditional on the observed controls and the approximate title grouping; they do not account for all tune-family dependence or Monte Carlo uncertainty. No adjustment for multiple contrasts is applied.

### 2.6. Graduated repetition-profile controls

An additional exploratory analysis on the same 740 melodies matches the bigram spectrum and boundaries and preserves factor-multiplicity histograms and suffix multiplicities through an upper order L, where L is 2, 3, 4, 6, 8 or the full word. This supplement was motivated by the strength of the full-profile control and is not an independent validation of a preregistered graded hypothesis. All levels use 1,800 switching proposals, discard 600 and retain twelve states 100 proposals apart. An independent bigram baseline uses twelve draws. Seeds are 410029 + 10007 i + 7919 j (melody index i and level index j, both zero-based) and 882113 + 10007 i for the new bigram baseline. The computation is split into four disjoint equal-sized batches by index modulo four, each with 185 melodies. All 740 melodies are retained, including chains that return the original. All retained constrained states are checked for their specified invariants. There are 62,160 control evaluations (seven conditions, twelve samples per melody) and 7,992,000 switching proposals. The full aggregate is computed as the mean of the four equally sized batch means. The raw melody-level records were not retained in the recorded experiment, so the supplementary pooled estimates are descriptive; no pooled bootstrap intervals are reported for them. The supplied code regenerates the melody-level results.

We report both signed differences and attenuation of their absolute magnitudes. For the ambiguity curve, we report attenuation over orders {3,4,6,8} and separately over the late orders {6,8}. Preserving the profile through L fixes the local term L_k for k≤L (k≥2) by construction. The late-order contrast at L=3 or 4 therefore tests orders beyond the matched profile. The choice of late-order contrast is part of the exploratory supplement. We do not interpret matching short substrings as preserving musicological phrase boundaries or rhythmic motifs.

## 3. Results

### 3.1. Minimum fragment length

| Corpus | n | Original | Bigram control | Profile control |
|---|---:|---:|---:|---:|
| Bach (exploratory) | 382 | 6.5864 | 5.6294 | 6.6440 |
| The Session (exploratory) | 51 | 11.0980 | 6.7108 | 11.4314 |
| Essen (validation) | 740 | 5.9838 | 5.2278 | 6.0679 |

The Essen difference is +0.756 intervals (95% cluster-bootstrap interval [0.597, 0.924]), or +14.46% relative to the bigram control. The profile-matched difference is −0.084 intervals [−0.132, −0.037], reversing sign. A_K is 88.87% [80.43%, 95.36%]. This supports H1 and the aggregate attenuation criterion, with a small residual in the opposite direction. The original exceeds the mean bigram control in 401 melodies, is lower in 278 and equal within numerical tolerance in 61.

### 3.2. Ambiguity across scales

| k | Original H | Bigram H | Profile H | Original − bigram (95% interval) | Original − profile |
|---:|---:|---:|---:|---:|---:|
| 3 | 11.9899 | 16.4014 | 11.8506 | −4.4115 [−4.8264, −4.0139] | +0.1393 |
| 4 | 3.2050 | 4.5891 | 3.1950 | −1.3841 [−1.6267, −1.1601] | +0.0100 |
| 5 | 1.0423 | 1.0406 | 1.0890 | +0.0017 [−0.1026, +0.0970] | −0.0467 |
| 6 | 0.4425 | 0.2470 | 0.4817 | +0.1954 [+0.1267, +0.2577] | −0.0392 |
| 7 | 0.2660 | 0.0695 | 0.2979 | +0.1965 [+0.1416, +0.2533] | −0.0319 |
| 8 | 0.1497 | 0.0218 | 0.1705 | +0.1279 [+0.0920, +0.1674] | −0.0208 |
| 10 | 0.0739 | 0.0033 | 0.0808 | +0.0706 [+0.0485, +0.0946] | −0.0070 |
| 12 | 0.0437 | 0.0004 | 0.0463 | +0.0433 [+0.0272, +0.0624] | −0.0026 |

The pooled Essen data support H2. The sum of absolute mean differences at the four specified orders decreases by 96.58% [95.35%, 97.45%], supporting H3. The residuals are small but not uniformly zero. The four source subsets all have larger mean k_min than their bigram controls; the smaller ballad subset has a negative rather than positive difference at k=6 (−0.0023 bits), so the crossover at the fixed orders is not universal across subsets.

### 3.3. Control diagnostics

The constrained chains produce a different retained state in 713 of 740 melodies, with mean normalized Hamming distance 0.6013 from the original (bigram control: 0.7390). Among 850,007 nontrivial proposals, 177,935 are accepted (20.93%). There are 7,383 distinct non-original retained candidates summed within melodies. The minimum changes in at least one retained state for 341 melodies and the measured ambiguity curve changes for 664. The mean control minimum in the first and second six retained states is 6.0752 and 6.0606. Restricting descriptively to the 690 melodies with mean Hamming distance at least 0.2 gives minima 5.9449, 5.1699 and 6.0357, respectively. These checks show substantial movement but are not evidence of convergence to the full constrained distribution.

### 3.4. Graduated controls

The original mean minimum is 5.9838 intervals; the new independent bigram baseline is 5.2304 (difference +0.7534). This baseline uses different random seeds from Table 1. The following results use the same 740 melodies.

| Control | Mean minimum | Original − control | Minimum attenuation | H attenuation (3,4,6,8) | Late H attenuation (6,8) | Mean Hamming distance |
|---|---:|---:|---:|---:|---:|---:|
| L=2 | 5.2270 | +0.7568 | -0.4% | 0.1% | 2.4% | 0.728 |
| L=3 | 5.9434 | +0.0404 | 94.6% | 69.0% | -13.7% | 0.682 |
| L=4 | 6.2350 | -0.2512 | 66.7% | 90.4% | -27.0% | 0.650 |
| L=6 | 6.1288 | -0.1450 | 80.7% | 95.7% | 74.8% | 0.621 |
| L=8 | 6.0678 | -0.0840 | 88.8% | 96.4% | 79.9% | 0.606 |
| All orders | 6.0663 | -0.0825 | 89.0% | 96.7% | 80.9% | 0.601 |

At L=3, the minimum contrast falls to +0.0404 intervals (94.6% attenuation), whereas the absolute summed late-order contrast increases by 13.7%. At L=4 the minimum contrast reverses sign (−0.2512), and the absolute late-order contrast increases by 27.0%. Attenuation is not monotone. At L=6 the summed late contrast is reduced by 74.8%; at L=8 and the full profile it is reduced by approximately 80%. Part of this reduction is expected because the local term at matched orders is fixed. The original and L=3 mean differences at k=6 and 8 are particularly informative: the signed differences are +0.1919 and +0.1253 against the bigram baseline, but −0.3371 and −0.0236 against L=3 controls. A small mean minimum difference is therefore insufficient evidence for matched ambiguity curves. It is also distinct from individual reconstruction uniqueness. L=3 describes patterns of four pitch-class events, not a sufficient fragment length for each melody.

| k | Original H | Bigram H | L=2 | L=3 | L=4 | L=6 | L=8 | All |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 11.9899 | 16.3813 | 16.3903 | 11.7635 | 11.8327 | 11.8313 | 11.8465 | 11.8510 |
| 4 | 3.2050 | 4.5782 | 4.5692 | 4.5041 | 3.1808 | 3.1849 | 3.1954 | 3.2020 |
| 5 | 1.0423 | 1.0361 | 1.0400 | 1.8142 | 1.4488 | 1.0845 | 1.0962 | 1.1062 |
| 6 | 0.4425 | 0.2505 | 0.2576 | 0.7795 | 0.7275 | 0.4741 | 0.4818 | 0.4835 |
| 7 | 0.2660 | 0.0719 | 0.0752 | 0.3664 | 0.4458 | 0.3134 | 0.2928 | 0.2954 |
| 8 | 0.1497 | 0.0244 | 0.0249 | 0.1733 | 0.2674 | 0.1980 | 0.1742 | 0.1693 |
| 10 | 0.0739 | 0.0037 | 0.0030 | 0.0413 | 0.1044 | 0.0995 | 0.0886 | 0.0812 |
| 12 | 0.0437 | 0.0005 | 0.0005 | 0.0122 | 0.0439 | 0.0544 | 0.0472 | 0.0460 |

The same qualitative minimum-length pattern (strong attenuation at L=3 and a negative contrast at L=4) occurs in each of the four computational batches, although the signed residual at L=3 is negative in one. The mean Hamming distance declines as the control becomes more restrictive (0.728 at L=2, 0.682 at L=3, 0.601 at the full profile). At least 711 melodies have a nonoriginal retained state at every level. Mean acceptance rates across equal-sized batches range from 95.1% to 21.0% of nontrivial proposals; these are averages of batch acceptance rates, not pooled proposal-level rates.

### 3.5. Chain-length sensitivity

A systematic subset of 37 melodies (indices 0,20,...,720) was evaluated at L=3,4,6 and all orders with the standard chains and with 7,200 proposals and new seed base 510029. The number of retained samples is unchanged. The subset original mean minimum is 5.5405 and the bigram mean is 5.3288; its baseline contrast is smaller than that of the full dataset.

| Level | 1,800 proposals | 7,200 proposals |
|---|---:|---:|
| 3 | 5.7432 | 5.8041 |
| 4 | 5.8514 | 5.8986 |
| 6 | 5.9707 | 5.8153 |
| All | 5.6959 | 5.8559 |

The short- and long-chain means differ by up to 0.160 intervals; the longest-chain results do not establish convergence or uniform sampling. Both runs reproduce the divergence between short-order and late-order residual contrasts, but numerical attenuation can be unstable on small subsets with weak baseline contrasts. The sensitivity run changes duration and seed together and therefore does not isolate either effect. No formal equivalence claim is made.

## 4. Discussion

The validation confirms the direction of the original comparisons in a larger separate collection. In particular, the original sequences have lower ambiguity at short orders and higher ambiguity near the point where uniqueness is reached. The two tendencies coexist in aggregate; they do not imply that every melody has a crossover. A control matching the repetition profile greatly attenuates both contrasts. The observation is consistent with the importance of repeated substrings and their arrangement in the underlying reconstruction problem.

Equal profiles do not determine reconstructibility: the binary words 0000101 and 0001001 have equal endpoints, bigram counts and factor-multiplicity histograms at every length, but require lengths three and four for uniqueness. Even with suffix multiplicities held fixed, 0101111 and 0111011 exhibit the same distinction. These examples illustrate the dependence of the global term on graph organization; no novelty of the examples or the BEST decomposition is asserted. The corresponding finite counts can be checked by enumeration. The empirical finding concerns the average contrasts for the chosen musical representations, not a universal characterization of music.

The graduated controls suggest that short repetition statistics can be sufficient to approximate a corpus mean of the minimum length under this sampling scheme, while longer repetition statistics are needed to approximate the entire curve at the examined late orders. They cannot isolate a causal contribution of musical phrases. The observed nonmonotonicity and overshoot also caution against interpreting a single attenuation number as a general measure of structure.

Important limitations are the loss of rhythm, register and polyphony, dependence between tune variants, 38 duplicate interval-word records within the exploratory Bach corpus, restricted ABC inclusion rules, a convenience subset of Essen, and unknown mixing of the profile-preserving chain. The abcjs comparison addresses pitch extraction for the included Essen data; it does not establish the correctness of all earlier data processing. The exactness of the individual cardinalities does not make the empirical estimates exact. Controls are conditional on different levels of information; matching the full repetition profile can preserve much of the structure governing the outcome. The observed attenuation should therefore not be interpreted as proof of a unique causal mechanism or as a formal equivalence test. The old and validation corpora differ in length and preprocessing, so their raw minimum fragment lengths are not directly measures of comparative musical complexity.

### Exhaustive follow-up on repetition organization

An exploratory comparison of strict interleaving between distinct repeated factors (four non-overlapping occurrences) suggested fewer crossings in the original Essen words than in sampled full-profile controls at factor lengths four and five. However, the analysis inspected several definitions, lengths and representations after observing the data; within-metric confidence intervals cannot establish a confirmatory result. A follow-up test required negative contrasts at both orders in the exact control. On the tractable subset of 36 words with bigram classes of size 2–10,000, we enumerated 97,328 compatible words, retaining 15,807 with matching complete repetition profiles and suffix multiplicities. Uniform exact control averages instead gave positive original-minus-control contrasts of 1.52 and 0.93 percentage points at orders four and five (20 and 14 eligible words). The mean minimum also reversed relative to the full-corpus sampled contrast (4.528 original versus 4.413 exact). Selection for tractability limits generalization and the comparison does not identify sampling bias independently of subset composition. Nevertheless, the proposed interleaving regularity was not supported. No causal explanation or musical regularity is claimed from the sampled residuals. See [exact-control protocol and results](EXACT_INTERLEAVING.md).

## 5. Conclusion

Exact k-abelian class cardinalities provide a scale-dependent measure of reconstruction ambiguity for symbolic interval sequences. Three musical collections display a pooled crossover relative to bigram-matched controls. In the independent Essen collection, matching repetition profiles reduces the aggregate differences in mean minimum length and in the ambiguity curve by 88.9% and 96.6%, respectively, under the implemented sampling scheme. Graduated controls show a substantial reduction of the mean minimum contrast even when repetition profiles are preserved only through three intervals, but the late-order ambiguity contrasts are not attenuated at that level. This distinction describes the observed contrasts under the implemented controls. The exact follow-up does not support a further claim that melodies organize repetitions with less interleaving; the constrained-control estimates should not be interpreted as uniform-null effects. The exploratory phase is closed, with standalone replication and author verification outstanding.

## Data and code availability

The code, recorded aggregates and reproduction instructions are available at https://github.com/sgarcia87/musical-reconstruction-ambiguity. The accompanying scripts check pinned source hashes, perform the original and graduated validations, and provide parser, cross-corpus overlap and exact interleaving audits. Recorded aggregates, batch summaries and the sensitivity results are supplied as JSON. The original corpus data and third-party parser bundle are obtained from their distributors and are not redistributed. The corpus experiments and independent ABC parser comparison were executed against pinned source contents in a JavaScript execution environment; the local standalone counter and parser self-tests pass. Full standalone replay is pending access to the source files. The graduated aggregates do not contain raw melody-level rows; these can be generated by the supplied script. Full standalone replication, bibliographic verification and source-license review remain pending.

## Generative AI disclosure

ChatGPT (GPT-6.2) and Claude (Opus 5.5, version reported by the author) were used for research assistance, experimental design and code generation, bibliography discovery, drafting and critical review. AI-generated code and interpretations require verification by the author, who is responsible for the submitted work. Human verification of the complete corpus calculations remains pending.

## References

- Bresler, G., Bresler, M., & Tse, D. (2013). Optimal assembly for high throughput shotgun sequencing. *BMC Bioinformatics*, 14(Suppl 5), S18. https://doi.org/10.1186/1471-2105-14-S5-S18
- Cassaigne, J., Karhumäki, J., Puzynina, S., & Whiteland, M. A. (2017). k-Abelian Equivalence and Rationality. *Fundamenta Informaticae*, 154(1–4). https://doi.org/10.3233/FI-2017-1553
- Karhumäki, J., Saarela, A., & Zamboni, L. Q. (2013). On a generalization of Abelian equivalence and complexity of infinite words. *Journal of Combinatorial Theory, Series A*, 120(8), 2189–2206. https://doi.org/10.1016/j.jcta.2013.08.008
- Karhumäki, J., Puzynina, S., Rao, M., & Whiteland, M. A. (2017). On cardinalities of k-abelian equivalence classes. *Theoretical Computer Science*, 658, 190–204. https://doi.org/10.1016/j.tcs.2016.06.010
- Schaffrath, H. (1995). *The Essen Folksong Collection in Kern Format* (D. Huron, ed.). Center for Computer Assisted Research in the Humanities. ABC distribution: music21 corpus, https://github.com/cuthbertLab/music21/tree/master/music21/corpus/essenFolksong
- JSB Chorales dataset: https://github.com/czhuang/JSB-Chorales-dataset (blob ff93746647d1f5af2f719d235329c294267f3088).
- Polifonia Project, folk_ngram_analysis: https://github.com/polifonia-project/folk_ngram_analysis (The Session subset, blob 9f172a30b41b48398d6aa0b0e48b40b94bf093dc).

- Downie, J. S. (1999). Music retrieval as text retrieval: Simple yet effective. https://experts.illinois.edu/en/publications/music-retrieval-as-text-retrieval-simple-yet-effective/
- Uitdenbogerd, A. L., & Zobel, J. (2002). Music ranking techniques evaluated. https://people.eng.unimelb.edu.au/jzobel/fulltext/acsc02uz.pdf
- Müllensiefen, D. (2009). FANTASTIC: Feature ANalysis Technology Accessing STatistics (In a Corpus). Technical report v1.5. https://www.doc.gold.ac.uk/isms/m4s/FANTASTIC_docs.pdf
- Pearce, M. T. (2018). Statistical learning and probabilistic prediction in music cognition: mechanisms of stylistic enculturation. *Annals of the New York Academy of Sciences*, 1423, 378–395. https://doi.org/10.1111/nyas.13654
- Müllensiefen, D., & Pendzich, M. (2009). Court decisions on music plagiarism and the predictive value of similarity algorithms. https://doi.org/10.1177/102986490901300111
- abcjs-basic 6.7.3. https://api.github.com/repos/paulrosen/abcjs/git/blobs/0631d3b91887d149458989f5b37b8f19c09dc725 (pinned Git blob).
