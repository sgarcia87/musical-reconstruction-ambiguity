# Musical Reconstruction Ambiguity

**Sergi Garcia Mecinas · 2026**

Exact combinatorial analysis of melodic reconstruction from interval fragments and repetition structures.

[Manuscript](study/MANUSCRIPT.md) · [Reproduction](study/README.md) · [Results](study/results/) · [Español](README.md)

**Status:** exploratory research closed; standalone replication and academic review pending.

The study counts compatible pitch-class interval words from complete multisets of consecutive fragments with known boundaries. The analysis covers 382 Bach chorales, 51 traditional tunes and 740 Essen folk melodies.

| Corpus | Original | Bigram control | Full-profile control |
|---|---:|---:|---:|
| Bach | 6.586 | 5.629 | 6.644 |
| The Session | 11.098 | 6.711 | 11.431 |
| Essen | 5.984 | 5.228 | 6.068 |

Mean minimum unique reconstruction length, in intervals. In a separate graduated-control experiment, preserving repetition statistics through length three attenuates the mean minimum-length contrast by 94.6%, while increasing the absolute late-order ambiguity contrasts (orders 6 and 8) by 13.7%. Longer profile constraints attenuate the late contrasts.

An independent abcjs parser comparison agrees on all 33,748 pitch events in the 740 included Essen melodies. Full standalone replay and pooled uncertainty estimates for the graduated experiment remain pending. No claim of algorithmic or mathematical priority is made.

The exploratory hypothesis of reduced repetition interleaving was not supported by exact enumeration of a tractable 36-melody subset: the contrasts reverse to +1.52 and +0.93 percentage points at orders 4 and 5. This does not isolate sampling bias from subset effects. See the [exact control](study/EXACT_INTERLEAVING.md).

[Historical research archive](https://github.com/sgarcia87/musical-reconstruction-ambiguity/tree/f0905323a98448229ff5504763987db97648f40b).
