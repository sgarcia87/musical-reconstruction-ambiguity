#!/usr/bin/env python3
"""RGO phase VII — complete third-order invariants and conditional observability.
Python 3.10+, NumPy. Enumerates all binary states; exact integer invariants.
PPR is numerical, via Walsh-Hadamard transform. No audio or hardware data.
Usage: python rgo_fase7_audit.py > rgo_fase7_results.json
"""
import json
from collections import Counter, defaultdict
from itertools import combinations
import numpy as np

N=4096; MASK=N-1
m=np.arange(N, dtype=np.int64)
X=2*((m[:,None]>>np.arange(12))&1)-1
ROWS=np.array([[next(n for n in range(12) if n%3==i and n%4==j) for j in range(4)] for i in range(3)])
A=X[:,ROWS]
Q=np.flatnonzero((A.sum(2)==0).all(1)&(np.einsum('nik,njk->nij',A,A)[:,[0,0,1],[1,2,2]]==0).all(1))
perms=[[(s*i+t)%12 for i in range(12)] for s in (1,-1) for t in range(12)]
trans=np.array([sum(((m>>i)&1)<<p[i] for i in range(12)) for p in perms]); canon=trans.min(0); canonC=np.minimum(canon,MASK-trans.max(0))
R=np.unique(canon); groups=np.array([np.flatnonzero(canon[Q]==r) for r in np.unique(canon[Q])]); assert len(Q)==48 and len(R)==224 and len(np.unique(canonC))==122 and groups.shape==(4,12)
F=[]; keys=[]; degree_stats=[]
def bits(a):return tuple(i for i in range(12) if int(a)>>i&1)
def entropy(p, axis=-1):
    p=np.asarray(p); lp=np.zeros_like(p,dtype=float); np.log2(p,out=lp,where=p>0); return -np.sum(p*lp,axis=axis)
for d in range(1,5):
    for p in sorted({int(canon[sum(1<<i for i in a)]) for a in combinations(range(12),d)}):
        orb=np.unique(trans[:,p]); v=sum(np.prod(X[:,bits(q)],axis=1) for q in orb)
        F.append(v); keys.append((d,bits(p)))
    v=np.stack(F,axis=1); _,c=np.unique(v,axis=0,return_counts=True); _,cq=np.unique(v[Q],axis=0,return_counts=True)
    degree_stats.append(dict(degree=d,features=len(F),classes=len(c),Q48_classes=len(cq),bits_uniform_Q12=float(entropy(c/N)),bits_uniform_Q48=float(entropy(cq/48))))
F=np.stack(F,axis=1); assert [r['classes'] for r in degree_stats[:3]]==[13,201,224]
assert [r['Q48_classes'] for r in degree_stats[:3]]==[1,2,4]
for j in range(19): assert np.all(F[:,j]==F[canon,j])
assert np.unique(F[R,:19],axis=0).shape[0]==224
# Find ambiguous pairs of T/I orbits under first+second order, and the minimum number of extra triple observables.
f=F[R]; g=defaultdict(list)
for i,z in enumerate(f[:,:7]):g[tuple(z)].append(i)
amb=[(a,b) for q in g.values() for a,b in combinations(q,2)]
assert len(amb)==23 and max(map(len,g.values()))==2
for k in range(1,13):
    extra=[js for js in combinations(range(7,19),k) if all(any(f[a,j]!=f[b,j] for j in js) for a,b in amb)]
    if extra:break
assert k==3 and len(extra)==26
# Minimum arbitrary subset within the specified 19 elementary orbit sums, not among all possible encodings.
pairs=np.array(list(combinations(range(len(R)),2))); coverage=[]
for j in range(19):
    b=f[pairs[:,0],j]!=f[pairs[:,1],j];coverage.append(int.from_bytes(np.packbits(b,bitorder='little').tobytes(),'little'))
allp=(1<<len(pairs))-1
for k in range(1,20):
    n=0;first=None
    for js in combinations(range(19),k):
        c=0
        for j in js:c|=coverage[j]
        if c==allp:n+=1;first=first or js
    if n:break
assert k==8 and n==158
assert len(np.unique(F[:,first],axis=0))==224
# Even moments retain complement invariance; fourth order resolves all T/I/C orbits.
even=[i for i,k0 in enumerate(keys) if k0[0] in (2,4)]; assert len(np.unique(F[:,even],axis=0))==122 and np.all(F[:,even]==F[canonC][:,even])
# Two sign-valued triple moments classify the four Q48 families.
j1=keys.index((3,(0,1,2)));j2=keys.index((3,(0,1,3)))
reps=[('6-Z37',(0,1,2,3,4,8)),('6-Z4',(0,1,2,4,5,6)),('6-Z48',(0,1,2,5,7,9)),('6-Z26',(0,1,3,5,7,8))]
families=[]
for label,ns in reps:
    s=sum(1<<i for i in ns);a,b=F[s,[j1,j2]];assert s in Q and abs(a)==4 and abs(b)==8
    families.append(dict(label=label,notes=ns,T012=int(a),T013=int(b)))
assert len(np.unique(F[Q][:,[j1,j2]],axis=0))==4
assert np.all(F[:,[j1,j2]]==-F[m^MASK][:,[j1,j2]])
# PPR: starting state uniformly chosen from Q48. T = orbit family; X = exact start.
# Observation Y is one sample from the PPR field. Z=canonical orbit of Y.
C=np.unique(canon,return_inverse=True)[1];weight=np.array([int(i).bit_count() for i in m]);ix=np.triu_indices(48,1);within=canon[Q][ix[0]]==canon[Q][ix[1]]
ppr=[]
for alpha in (0,.5,.85,.95,.99,.999):
    kernel=(1-alpha)/(1-alpha*(1-2*weight/12));h=1
    while h<N:
        a=kernel.reshape(-1,2*h);u=a[:,:h].copy();v=a[:,h:].copy();a[:,:h]=u+v;a[:,h:]=u-v;h*=2
    kernel=np.maximum(kernel/N,0);kernel/=kernel.sum();p=kernel[m^Q[:,None]];t=p[groups].mean(1)
    IT=float(entropy(p.mean(0))-entropy(t).mean());IN=float(entropy(t).mean()-entropy(p).mean())
    z=np.array([np.bincount(C,weights=v) for v in p]);tz=z[groups].mean(1);IZ=float(entropy(tz.mean(0))-entropy(tz).mean());LZ=float(entropy(tz).mean()-entropy(z).mean())
    assert abs(IT-IZ)<1e-10 and abs(LZ)<1e-10
    js=entropy((p[ix[0]]+p[ix[1]])/2)-(entropy(p[ix[0]])+entropy(p[ix[1]]))/2
    assert np.allclose(z[groups],tz[:,None,:],atol=1e-12)
    ppr.append(dict(alpha=alpha,target_bits_raw=IT,nuisance_bits_raw=IN,target_bits_quotient=IZ,nuisance_bits_quotient=max(0,LZ),C_within_raw=float(1-js[within].mean()),C_between_raw=float(1-js[~within].mean()),C_within_quotient=1.0,accuracy_target_raw=float(t.max(0).sum()/4),accuracy_target_quotient=float(tz.max(0).sum()/4)))
print(json.dumps(dict(rows=ROWS.tolist(),Q48=Q.tolist(),orbits_TI=len(R),orbits_TI_complement=len(np.unique(canonC)),degree_stats=degree_stats[:3],ambiguous_pairs_second_order=len(amb),minimum_extra_triple=3,extra_triple_solutions=len(extra),example_extra_triple=[keys[j] for j in extra[0]],minimum_subset_19=k,minimum_subset_count=n,example_minimum_subset=[keys[j] for j in first],even_degree_2_4_classes=len(np.unique(F[:,even],axis=0)),families=families,ppr=ppr),indent=2,ensure_ascii=False))
