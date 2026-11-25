#!/usr/bin/env python3
"""Independent direct-subset audit of the Z12 robust-query bound, stdlib only."""
from itertools import combinations
from collections import defaultdict, Counter
N = 12
def canon(A):
    return min(tuple(sorted((a+t)%N for a in A)) for t in range(N))
def counts(A,k):
    return Counter(canon(B) for B in combinations(A,k))
reps={canon(A) for k in range(N+1) for A in combinations(range(N),k)}
groups=defaultdict(list)
for A in sorted(reps):
    groups[(len(A),tuple(sorted(counts(A,2).items())))].append(A)
families=[g for g in groups.values() if len(g)>1]
pairs=[(a,b) for g in families for a,b in combinations(g,2)]
patterns={k:sorted({canon(A) for A in combinations(range(N),k)}) for k in (3,4)}
queries=[(k,p) for k,pp in patterns.items() for p in pp]
profiles={a:{k:counts(a,k) for k in patterns} for g in families for a in g}
diffs=[{(k,p) for k,p in queries if profiles[a][k][p]!=profiles[b][k][p]} for a,b in pairs]
q=[(3,canon(p)) for p in [(0,1,3),(0,3,4),(0,3,5),(0,4,5),(0,4,6),(0,5,6),(0,3,7)]]+[(4,canon((0,3,4,8)))]
witness=[s for (a,b),s in zip(pairs,diffs) if len(a)==3 and len(s)==2]+[s for s in diffs if all(k==4 for k,p in s)]
assert (len(reps),len(families),len(pairs),len(patterns[3]),len(patterns[4]),len(witness),min(map(len,diffs)))==(352,125,189,19,43,8,2)
assert len(set(q))==8 and all(set(q)&d for d in diffs)
assert all(not a&b for a,b in combinations(witness,2))
print("352 orbits; 125 ambiguous families; 189 pairs; 19+43 query types.")
print("8 disjoint lower-bound witnesses; 8-query universal separating list.")
print("Exact minimum 8h with repetitions; full distinct dictionary distance 2.")
