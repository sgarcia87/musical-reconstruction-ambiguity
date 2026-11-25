#!/usr/bin/env python3
"""RGO X: Q48/GF(4), binary homometry, minimum phase queries and quantum transfer.
All counts and algebra are exact. Python >=3.10; SymPy only for optional Z12 order audit.
python rgo_fase10_audit.py > rgo_fase10_results.json
"""
from itertools import combinations, combinations_with_replacement, product
from collections import Counter
from functools import lru_cache
from math import gcd, prod
import json

parity = lambda x: x.bit_count() & 1
P = list(combinations(range(4),2))
ROWS = [[next(n for n in range(12) if n%3==r and n%4==c) for c in range(4)] for r in range(3)]

def encode(r,a,b):
    m=0
    for j,c in enumerate((a,b,a^b)):
        u,v=c&1,c>>1
        for k,z in enumerate((r[j],r[j]^u,r[j]^v,r[j]^u^v)):
            m |= z << ROWS[j][k]
    return m

def decode(m):
    x=[[m>>i&1 for i in row] for row in ROWS]
    r=tuple(row[0] for row in x)
    a,b,c=[(row[0]^row[1]) | ((row[0]^row[2])<<1) for row in x]
    return r,a,b,c

L={encode(r,a,b) for r in product(range(2),repeat=3) for a,b in product(range(4),repeat=2)}
R={encode(r,0,0) for r in product(range(2),repeat=3)}
Q={encode(r,a,b) for r in product(range(2),repeat=3) for a,b in product(range(4),repeat=2) if a and b and a!=b}
Qdirect=set()
for m in range(4096):
    x=[[2*(m>>i&1)-1 for i in row] for row in ROWS]
    if all(sum(row)==0 for row in x) and all(sum(u*v for u,v in zip(a,b))==0 for a,b in combinations(x,2)):Qdirect.add(m)
assert Q==Qdirect and len(Q)==48 and len(L)==128 and len(R)==8
assert all(a^b in L for a,b in product(L,repeat=2))
assert all(a^b in Q for a,b in product(Q,R))
# Same GF(4) field tables and coordinate map as Cubo64.
M2=[0,2,3,1];M3=[0,3,1,2]
def cube(x,y,z):return x^M2[y]^M3[z],x^M3[y]^M2[z]
assert {p for p in product(range(4),repeat=3) if cube(*p)==(0,0)}=={(d,d,d) for d in range(4)}
plane=[(a,b,a^b) for a,b in product(range(4),repeat=2)]
assert len({cube(*p) for p in plane})==16
triads=[p for p in plane if all(p)]
axes={cube(*p) for p in triads}
assert axes=={(a,0) for a in range(1,4)}|{(0,a) for a in range(1,4)}
labels=sorted(2*(4*u+v)+1 for u,v in axes)
cube_set=[p for p in product(range(4),repeat=3) if cube(*p) in axes]
assert len(cube_set)==24
# Walsh, no numerical rounding.
def walsh(A,n):
    w=[int(i in A) for i in range(1<<n)]
    h=1
    while h<len(w):
        for i in range(0,len(w),2*h):
            for j in range(i,i+h):
                a,b=w[j],w[j+h];w[j],w[j+h]=a+b,a-b
        h*=2
    return tuple(w)
W=walsh(Q,12)
ann=lambda S:{k for k in range(4096) if all(parity(k&s)==0 for s in S)}
assert {k for k,w in enumerate(W) if w}==ann(R)
assert {k for k,w in enumerate(W) if abs(w)==48}==ann(L)
D={a|(b<<2) for a,b in product(range(4),repeat=2) if a and b and a!=b}
assert D=={6,7,9,11,13,14}
wd=walsh(D,4);mag=tuple(map(abs,wd))
assert mag==(6,)+(2,)*15
# All 6-element subsets on the quotient; reduction proof in note avoids 2^4096 search.
sets=[]
for a in combinations(range(16),6):
    if tuple(map(abs,walsh(set(a),4)))==mag:sets.append(frozenset(a))
canon=lambda a:min(tuple(sorted(x^t for x in a)) for t in range(16))
reps=sorted({canon(a) for a in sets});ws=[walsh(set(a),4) for a in reps]
assert len(sets)==448 and len(reps)==28
assert all(len({tuple(sorted(x^t for x in a)) for t in range(16)})==16 for a in reps)
# Each of these indicators is bent (Walsh of 1-2f has magnitude 4 everywhere)
# and quadratic. Recover its dual via W_{1-2f}(k)/4 = (-1)^g(k).
def dual(w):return tuple(0 if k==0 else int(w[k]>0) for k in range(16))
def polar(g,a,b):return g[a]^g[b]^g[a^b]^g[0]
def form(w):
    g=dual(w)
    return sum(polar(g,1<<i,1<<j)<<k for k,(i,j) in enumerate(P))
forms=[form(w) for w in ws]
assert len(set(forms))==28
for w in ws:
    g=dual(w)
    assert all(g[x]==(g[0]^sum(g[1<<i]*(x>>i&1) for i in range(4))%2^sum(polar(g,1<<i,1<<j)*(x>>i&1)*(x>>j&1) for i,j in P)%2) for x in range(16))
    # 2-copy coherence products are invariant under translations; exact rational expectation = +/-1/96.
    # Normalized Fourier amplitude w[k]/(4*sqrt(6)). 2*w[a]*w[b]*w[a^b]*w[0]/(4^4*6^2).
    assert all(abs(2*w[a]*w[b]*w[a^b]*w[0])==96 for a,b in combinations(range(1,16),2))
    for t in range(16):
        wt=tuple((-1)**parity(t&k)*v for k,v in enumerate(w))
        assert all(wt[a]*wt[b]*wt[a^b]*wt[0]==w[a]*w[b]*w[a^b]*w[0] for a,b in combinations(range(1,16),2))
# Fixed and adaptive observation minima. A triple (a,b,a xor b) reveals one linear form bit, with fixed offset.
diffs={a^b for a,b in combinations(forms,2)}
assert diffs==set(range(1,64)) # any rank-deficient linear observation collides
queries={}
for a,b in combinations(range(1,16),2):
    c=a^b
    if c<b:continue
    q=sum((((a>>i&1)*(b>>j&1))^((a>>j&1)*(b>>i&1)))<<k for k,(i,j) in enumerate(P))
    sig=sum(int(w[a]*w[b]*w[c]<0)<<k for k,w in enumerate(ws))
    assert sig==sum((1^parity(q&f))<<k for k,f in enumerate(forms))
    queries[q]=(a,b,sig)
assert len(queries)==35
for q in queries:assert q
fixed=[(1<<i,1<<j) for i,j in P]
assert len({tuple(int(w[a]*w[b]*w[a^b]<0) for a,b in fixed) for w in ws})==28
masks=sorted(queries.values())
@lru_cache(None)
def tree(state,depth):
    n=state.bit_count()
    if n==1:return {'class':(state&-state).bit_length()-1}
    if n==0 or n>2**depth:return None
    for a,b,m in masks:
        s0,s1=state&~m,state&m
        if not s0 or not s1 or max(s0.bit_count(),s1.bit_count())>2**(depth-1):continue
        t0=tree(s0,depth-1)
        if t0 is None:continue
        t1=tree(s1,depth-1)
        if t1 is not None:return {'a':a,'b':b,'positive':t0,'negative':t1}
    return None
T=tree((1<<28)-1,5)
assert T is not None
paths=[]
for i,w in enumerate(ws):
    t=T;depth=0
    while 'class' not in t:
        a,b=t['a'],t['b'];t=t['negative' if w[a]*w[b]*w[a^b]<0 else 'positive'];depth+=1
    assert t['class']==i and depth<=5;paths.append(depth)
# General formula for a punctured union of complementary m-dimensional subspaces.
axis_spectra=[]
for m in range(1,5):
    q=1<<m; A=set(range(1,q))|{a<<m for a in range(1,q)}
    hist=Counter(walsh(A,2*m));expected=Counter()
    expected[2*(q-1)]+=1;expected[q-2]+=2*(q-1);expected[-2]+=(q-1)**2
    assert hist==expected;axis_spectra.append(dict(m=m,q=q,spectrum=dict(sorted(hist.items()))))
# Z12 minimal relation order for real signals with specified spectral support and DC.
# exact cyclotomic arithmetic (z^4=z^2-1), plus Smith normal form.
def z12_order():
    from sympy import Matrix, ZZ
    from sympy.matrices.normalforms import smith_normal_form
    Z=[(1,0,0,0)]
    for _ in range(11):
        a,b,c,d=Z[-1];Z.append((-d,a,b+d,c))
    supports=Counter()
    for m in range(4096):
        a=[i for i in range(12) if m>>i&1]
        supports[tuple(k for k in range(12) if any(sum(Z[k*j%12][v] for j in a) for v in range(4)))]+=1
    out=[];hist=Counter()
    for support,count in sorted(supports.items()):
        S=[k for k in support if k];V=[k for k in S if k<=6];n=len(V);period=12//gcd(12,*S)
        rows=set()
        if 6 in V:rows.add(tuple(2*int(k==6) for k in V))
        def e(k):return tuple((int(k==i)-int(k==12-i)) if i!=6 else int(k==6) for i in V)
        if not n:r=1
        else:
            for r in range(2,13):
                for a in combinations_with_replacement(S,r):
                    if sum(a)%12==0:
                        v=tuple(sum(e(k)[i] for k in a) for i in range(n))
                        if any(v):rows.add(v)
                if rows:
                    diag=smith_normal_form(Matrix(list(rows)),domain=ZZ)
                    ds=[abs(int(diag[i,i])) for i in range(min(diag.shape)) if diag[i,i]]
                    if len(ds)==n and prod(ds)==period:break
            else:raise AssertionError('unresolved support')
        hist[r]+=count;out.append(dict(support=support,count=count,period=period,min_order=r))
    assert hist==Counter({1:2,2:2,3:3830,4:262})
    return {'histogram':dict(sorted(hist.items())),'support_details':out}
# General Boolean support: full subspace and a sparse circuit attaining order d+1.
def rank2(rows):
    basis={}
    for x in rows:
        while x:
            i=x.bit_length()-1
            if i in basis:x^=basis[i]
            else:basis[i]=x;break
    return len(basis)
S=[i for i in range(1,4096) if W[i]]
idx={s:i for i,s in enumerate(S)}
rank=rank2(S);triples=[]
for a,b in combinations(S,2):
    c=a^b
    if c>b and c in idx:triples.append((1<<idx[a])|(1<<idx[b])|(1<<idx[c]))
assert rank==9 and rank2(triples)==len(S)-rank==502
out=dict(q48=dict(size=len(Q),L_dimension=7,R_dimension=3,quotient_dimension=4,quotient_points=sorted(D),walsh_histogram=dict(sorted(Counter(W).items())),full_real_ambiguity_bits=len(S)-rank),cubo64=dict(plane_size=len(plane),diagonal_kernel_size=4,nonzero_axis_points=sorted(axes),odd_labels=labels,preimage_size=len(cube_set)),homometry=dict(weight6_quotient_sets=len(sets),translation_classes=len(reps),total_binary_homometric_sets_in_Q12=(4096//len(L))*len(sets),translation_orbit_size=4096//len(R),dual_forms=sorted(forms),all_nonzero_form_differences=len(diffs),fixed_minimum=6,adaptive_minimum=5,adaptive_depth_histogram=dict(sorted(Counter(paths).items())),cubic_query_count=len(queries),class_representatives=reps,adaptive_tree=T),quantum=dict(logical_qubits=4,fixed_zero_qubits=5,plus_qubits=3,walsh_probability_DC='3/8',walsh_probability_nonzero='1/24',two_copy_observable_expectation='±1/96',one_copy_uniform_translation_twirl_identical=True),general_axis_spectra=axis_spectra,z12=z12_order())
print(json.dumps(out,indent=2,ensure_ascii=False))
