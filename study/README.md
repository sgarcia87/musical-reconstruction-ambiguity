# Reconstruction ambiguity in folk songs and chorales

Research-note draft and reproduction materials. Node.js 18+; Python 3 for the optional synthetic verification. Run commands from this directory (`cd study`).

## Included results

- `MANUSCRIPT.md`: revised English manuscript, including musical literature, complete graduated-control analysis, parser audit, sensitivity and disclosure draft.
- `results/results_essen.json`: recorded aggregates of the original Essen validation.
- `results/graded_results_740.json`: recorded aggregates for all four disjoint batches, 740 melodies, six levels plus a new bigram control. The four batches correspond to indices modulo four. Means are equally weighted. Raw per-melody outputs were not retained. No new pooled bootstrap interval is asserted.
- `results/graded_sensitivity_37.json`: sensitivity at four levels on the same 37 melodies, two lengths and seeds.
- `results/parser_audit.json` and `results/overlap_audit.json`: recorded comparisons with abcjs and cross-corpus exact word overlap.
- `results/repeticiones.json` and `ESTUDIO_FRAGMENTOS.md`: exploratory results and protocol.

## Reproduce

    node validate_essen.mjs --self-test
    node graded_essen.mjs --self-test
    node auditoria_repeticiones.mjs --self-test
    python verify_repetition_profiles.py

    node auditoria_repeticiones.mjs --data ./rgo_data --fragments > fragments_full.json
    node auditoria_repeticiones.mjs --data ./rgo_data > exploratory_full.json
    node validate_essen.mjs --data ./essen_data > essen_full.json
    node graded_essen.mjs --data ./essen_data --full > graded_full.json

Alternatively run the graduated analysis as four separate batches (`--offset 0`, `--offset 1`, `--offset 2`, `--offset 3`, omitting `--full`). Each returns 185 rows; the pooled mean is the average of the four batch means. A full local run also outputs the pooled bootstrap interval.

    node graded_essen.mjs --data ./essen_data --stride 20 > sensitivity_short.json
    node graded_essen.mjs --data ./essen_data --stride 20 --steps 7200 --seed 510029 > sensitivity_long.json

The sensitivity commands calculate all six levels; the recorded sensitivity comparison reports levels 3,4,6 and all orders, using identical seeds for those level indices.

The source scripts download data if absent and verify the pinned Git blob hashes. If network access is unavailable, retrieve the following blobs using the GitHub REST Git blob endpoint and decode the base64 content exactly. Keep the original bytes and filenames. The data and abcjs bundle are not redistributed.

| Repository | Name | Blob SHA-1 |
|---|---|---|
| cuthbertLab/music21 | altdeu10.abc | 49e3860475f6a2d626830519171bf4b9b88e8c3d |
| cuthbertLab/music21 | ballad10.abc | de0a705e52e72d7ddbff6fe4fcfaf60d0416d4d4 |
| cuthbertLab/music21 | erk10.abc | 3d9e66a5acade62ed4b6249c716dc20ec47d76e5 |
| cuthbertLab/music21 | kinder0.abc | 97a520bdbdd5f97370995f760d393abdd347a8d1 |
| czhuang/JSB-Chorales-dataset | jsb-chorales-quarter.json | ff93746647d1f5af2f719d235329c294267f3088 |
| polifonia-project/folk_ngram_analysis | thesession_subset_metadata_with_tune_family_annotation.csv | 9f172a30b41b48398d6aa0b0e48b40b94bf093dc |
| paulrosen/abcjs | abcjs-basic-min.js (6.7.3) | 0631d3b91887d149458989f5b37b8f19c09dc725 |

Place the ABC files in `essen_data`, the two exploratory data files in `rgo_data`, and the ABCJS bundle in the working directory. Then:

    node audit_abcjs.mjs --data ./essen_data --library ./abcjs-basic-min.js > parser_replay.json
    node audit_overlap.mjs --data ./essen_data --old-data ./rgo_data > overlap_replay.json

## Verification status

The recorded corpus computations and abcjs comparison used the pinned repository contents. The counter and ABC parser self-tests return 16,388 exact counter checks and two parser checks. The results are recorded aggregates; the scripts regenerate individual melody rows. Full standalone replay remains pending. Neither convergence of the MCMC chains nor publication priority has been certified. Source licenses, bibliographic records and the full standalone computations remain to be verified. 
