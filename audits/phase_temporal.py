#!/usr/bin/env python3
"""Exact Fourier equivalence, bispectral Z-pair audit and temporal synchronization.
Python 3.10+ stdlib only. Fourier algebra in Z[z]/(z^4-z^2+1), z=exp(-2*pi*i/12).
Run: python audits/phase_temporal.py
"""
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, product
from math import gcd, lcm, prod
import json, random
N=12; M=1<<N; MASK=M-1
ZERO=(0,0,0,0); ONE=(1,0,0,0)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def mul(a,b):
    v=[0]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b): v[i+j]+=x*y
    for i in range(6,3,-1):
        v[i-2]+=v[i]; v[i-4]-=v[i]
    return tuple(v[:4])
Z=[ONE]
for _ in range(11): Z.append(mul(Z[-1],(0,1,0,0)))
assert mul(Z[-1],Z[1])==ONE

def conj(a):
    v=ZERO
    for i,c in enumerate(a): v=add(v,tuple(c*x for x in Z[-i%12]))
    return v
def real2(a):return add(a,conj(a))
def pow2(a):return mul(a,conj(a))
def bits(m):return tuple(i for i in range(N) if m>>i&1)
def mask(a):return sum(1<<i for i in set(a))
def rot(m,t):t%=12;return ((m<<t)|(m>>(12-t)))&MASK
def inv(m):return mask((-i)%12 for i in bits(m))
def canon(m):return min(rot(m,t) for t in range(12))

def dft(m):
    out=[]
    for k in range(12):
        a=ZERO
        for i in bits(m):a=add(a,Z[(k*i)%12])
        out.append(a)
    return tuple(out)
F=[dft(m) for m in range(M)]
C=[canon(m) for m in range(M)]; D=[min(C[m],C[inv(m)]) for m in range(M)]
R=sorted(set(C)); RD=sorted(set(D))
rows=[[next(i for i in range(12) if i%3==r and i%4==c) for c in range(4)] for r in range(3)]
def is_q(m):
    a=[[2*(m>>i&1)-1 for i in row] for row in rows]
    return all(sum(r)==0 for r in a) and all(sum(x*y for x,y in zip(r,s))==0 for r,s in combinations(a,2))
Q=[m for m in range(M) if is_q(m)]
QF=[m for m in range(M) if m.bit_count()==6 and F[m][4]==ZERO and pow2(F[m][3])==(4,0,0,0)]
assert Q==QF and len(Q)==48
# exact B_112 = F1^2 conj(F2). The expression is real in Q48.
reps={'6-Z37':[0,1,2,3,4,8],'6-Z4':[0,1,2,4,5,6],'6-Z48':[0,1,2,5,7,9],'6-Z26':[0,1,3,5,7,8]}
B=[mul(mul(f[1],f[1]),conj(f[2])) for f in F]
labels={}
for name,ns in reps.items():
    a=mask(ns);orbit={rot(a,t) for t in range(12)}
    assert len(orbit)==12 and D[a]==C[a] and inv(a) in orbit
    assert len({B[m] for m in orbit})==1 and B[a]==conj(B[a])
    labels.update({m:name for m in orbit})
assert set(labels)==set(Q) and len({B[m] for m in Q})==4
# z+z^-1 = sqrt(3); exact real values +/- (8 +/- 4 sqrt(3))
s3=add(Z[1],Z[11]); hi=add((8,0,0,0),tuple(4*x for x in s3));lo=add((8,0,0,0),tuple(-4*x for x in s3))
assert {B[m] for m in Q}=={hi,lo,tuple(-x for x in hi),tuple(-x for x in lo)}
family_table=[dict(name=name,notes=ns,B112_coefficients=B[mask(ns)],F1_coefficients=F[mask(ns)][1]) for name,ns in reps.items()]
# Identify all Z pairs; use real bispectrum (reflection invariant), with indices summing to 0.
power=[tuple(pow2(a) for a in f[:7]) for f in F]
groups=defaultdict(list)
for m in RD:groups[power[m]].append(m)
amb=[(a,b) for g in groups.values() for a,b in combinations(g,2)]
assert len(amb)==23 and all(len(g)<=2 for g in groups.values())
triples=sorted({min(t,tuple(sorted((-k)%12 for k in t))) for t in combinations_with_replacement(range(1,12),3) if sum(t)%12==0})
def bval(m,t):return real2(mul(mul(F[m][t[0]],F[m][t[1]]),F[m][t[2]]))
coverage=[sum(1<<i for i,(a,b) in enumerate(amb) if bval(a,t)!=bval(b,t)) for t in triples]
full=(1<<len(amb))-1
for n in range(1,len(triples)+1):
    solutions=[]
    for inds in combinations(range(len(triples)),n):
        v=0
        for j in inds:v|=coverage[j]
        if v==full:solutions.append([triples[j] for j in inds])
    if solutions:break
assert solutions
assert len({(power[m],tuple(bval(m,t) for t in solutions[0])) for m in RD})==224
# For rational pitch-class indicators, Galois conjugacy ensures that characters
# of the same order are either all nonzero or all zero. This order-based
# intersection is valid for the COMPLETE cross-spectrum measured here.
orders=[12//gcd(k,12) for k in range(12)]
support=[{orders[k] for k in range(1,12) if f[k]!=ZERO} for f in F]
period=[lcm(*s) if s else 1 for s in support]
assert all(period[m]==len({rot(m,t) for t in range(12)}) for m in range(M))
def common(a,b):return lcm(*(support[a]&support[b])) if support[a]&support[b] else 1
# Each ordered pair of local necklaces has gcd(p,q) global translation orbits;
# cross spectrum yields only lcm(shared character orders) distinct signatures.
pair_total=pair_distinct=pair_unambig=local_pairs_ambig=0; ambiguity=Counter(); examples=[]
for a in R:
    for b in R:
        g=gcd(period[a],period[b]);d=common(a,b)
        assert g%d==0
        pair_total+=g;pair_distinct+=d;ambiguity[g//d]+=g
        if g==d:pair_unambig+=g
        else:
            local_pairs_ambig+=1
            if a.bit_count()==3 and b.bit_count()==3:examples.append((a,b,g,d))
# Independent exact checks of pair count formula by actual correlations.
def cc(a,b):return tuple((a&rot(b,t)).bit_count() for t in range(12))
rng=random.Random(812)
for a,b in rng.sample(list(product(R,R)),1000):
    g=gcd(period[a],period[b]);d=common(a,b)
    assert len({cc(a,rot(b,t)) for t in range(g)})==d
# Temporal Q48 theorem: all ordered pairs, label + first cross coefficient.
pair_keys=set(); pair_orbits=set()
for a,b in product(Q,Q):
    pair_keys.add((labels[a],labels[b],mul(F[b][1],conj(F[a][1]))))
    pair_orbits.add(min((rot(a,t),rot(b,t)) for t in range(12)))
assert len(pair_keys)==len(pair_orbits)==192
# General ambiguity formula: nested connectivity at prime-power levels 2,4,3.
def component_count(vertices,edges):
    parent={v:v for v in vertices}
    def root(v):
        while parent[v]!=v:v=parent[v]
        return v
    for i,j in edges:parent[root(i)]=root(j)
    return len({root(v) for v in vertices})
def fiber(seq,edges):
    count={}
    for level in (2,4,3):
        v=[i for i,m in enumerate(seq) if period[m]%level==0]
        e=[(i,j) for i,j in edges if common(seq[i],seq[j])%level==0]
        count[level]=component_count(v,e) if v else 0
    return prod(p**max(0,count[l]-1) for l,p in [(2,2),(4,2),(3,3)]),count
# Verify formula by brute enumerating shift vectors, canonicalizing global rotation.
for _ in range(300):
    seq=rng.choices(R,k=3); edges=[e for e in combinations(range(3),2) if rng.random()<.65]
    predicted,_=fiber(seq,edges);valid=set()
    for shifts in product(*(range(period[m]) for m in seq)):
        if any((shifts[i]-shifts[j])%common(seq[i],seq[j]) for i,j in edges):continue
        x=tuple(rot(m,s) for m,s in zip(seq,shifts));valid.add(min(tuple(rot(m,t) for m in x) for t in range(12)))
    assert predicted==len(valid)
# Choose a simple counterexample.
ex=None
for a,b,g,d in examples:
    for t in range(1,g):
        if t%d==0 and cc(a,b)==cc(a,rot(b,t)):
            ex=dict(A=bits(a),B=bits(b),B_shift=bits(rot(b,t)),shift=t,periods=[period[a],period[b]],shared_order=d,correlation=cc(a,b),ambiguous_global_orbits=g//d);break
    if ex:break
if ex is None:
    for a,b in product(R,R):
        g=gcd(period[a],period[b]);d=common(a,b)
        if g>d:
            ex=dict(A=bits(a),B=bits(b),B_shift=bits(rot(b,d)),shift=d,periods=[period[a],period[b]],shared_order=d,correlation=cc(a,b),ambiguous_global_orbits=g//d);break
out=dict(Q48_count=len(Q),fourier_equivalence=True,family_table=family_table,TI_orbits=len(RD),T_orbits=len(R),Z_pairs=len(amb),nonzero_triples=triples,min_real_bispectrum_terms=len(solutions[0]),min_solution_count=len(solutions),example_min_solution=solutions[0],all_min_solutions=solutions,hexachord_Z_pairs=sum(a.bit_count()==6 for a,b in amb),F1_nonzero=sum(f[1]!=ZERO for f in F),F1_zero_periods=dict(Counter(period[m] for m in range(M) if F[m][1]==ZERO)),Q48_ordered_pair_orbits=len(pair_orbits),Q48_pair_keys=len(pair_keys),all_ordered_pair_orbits=pair_total,all_pair_distinct_signatures=pair_distinct,all_pair_unambiguously_recovered=pair_unambig,local_orbit_pairs_ambiguous=local_pairs_ambig,ambiguity_orbit_histogram=dict(sorted(ambiguity.items())),pair_counterexample=ex,random_triple_graph_checks=300)
print(json.dumps(out,indent=2))
