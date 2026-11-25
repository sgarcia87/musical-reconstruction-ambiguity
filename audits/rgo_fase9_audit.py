#!/usr/bin/env python3
"""RGO phase IX: exact phase constraints on Z_12 and the Walsh cube.
Run with Python 3.10+ and SymPy: python rgo_fase9_audit.py > rgo_fase9_results.json
Fourier coefficients are in Z[z]/(z^4-z^2+1), z=exp(-2*pi*i/12).
The ambient phase analysis allows arbitrary real signals with the given spectral
magnitudes and positive DC, not just binary indicators. Walsh sign counts
likewise allow arbitrary real normalized amplitudes, not only Q48 indicators.
"""
from itertools import combinations, combinations_with_replacement
from collections import Counter, defaultdict
from math import gcd, prod
import json
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

N=12; M=1<<N; MASK=M-1
Z=[(1,0,0,0)]
for _ in range(11):
    a,b,c,d=Z[-1]; Z.append((-d,a,b+d,c))
ZERO=(0,0,0,0)
def mul(a,b):
    v=[0]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b): v[i+j]+=x*y
    for i in range(6,3,-1):
        v[i-2]+=v[i];v[i-4]-=v[i]
    return tuple(v[:4])
def bits(m):return [i for i in range(12) if m>>i&1]
def mask(ns):return sum(1<<i for i in set(ns))
def rot(m,t):return ((m<<t)|(m>>(12-t)))&MASK
def canon(m):return min(rot(m,t) for t in range(12))
def dft(m):
    a=bits(m)
    return tuple(tuple(sum(Z[k*j%12][q] for j in a) for q in range(4)) for k in range(12))

def constraints(S):
    # Realness identifies k and -k; F0 is fixed; F6 must be real.
    variables=[k for k in S if 1<=k<=6]; n=len(variables)
    def e(k):
        v=[0]*n
        if k:v[variables.index(min(k,12-k))]=1 if k<=6 else -1
        return v
    fixed=[tuple(2*v for v in e(6))] if 6 in variables else []
    triples={}
    for a,b in combinations_with_replacement(S,2):
        c=(a+b)%12
        if c not in S:continue
        r=tuple(x+y-z for x,y,z in zip(e(a),e(b),e(c)))
        if 6 in variables:r=tuple(v%2 if k==6 else v for k,v in zip(variables,r))
        if not any(r):continue
        first=next((v for v,k in zip(r,variables) if v and k!=6),1)
        if first<0:r=tuple((-v)%2 if k==6 else -v for k,v in zip(variables,r))
        triples.setdefault(r,(a,b,c))
    return variables,fixed,triples

def kernel(n,rows):
    if not n:return 0,1,[]
    if not rows:return n,1,[]
    D=smith_normal_form(Matrix(rows),domain=ZZ)
    diag=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
    return n-len(diag),prod(diag),diag

def rank2(rows):
    basis={}
    for x in rows:
        while x:
            i=x.bit_length()-1
            if i in basis:x^=basis[i]
            else:basis[i]=x;break
    return len(basis)

def main():
    F=[dft(m) for m in range(M)]
    supports=[tuple(k for k,a in enumerate(f) if a!=ZERO) for f in F]
    rows=[[next(k for k in range(12) if k%3==i and k%4==j) for j in range(4)] for i in range(3)]
    Q=[]
    for m in range(M):
        a=[[2*(m>>k&1)-1 for k in row] for row in rows]
        if all(sum(r)==0 for r in a) and all(sum(x*y for x,y in zip(r,s))==0 for r,s in combinations(a,2)):Q.append(m)
    assert len(Q)==48 and len({supports[m] for m in Q})==1
    Qsupport=supports[Q[0]]; summaries=[]; q_min=None
    for S,count in sorted(Counter(supports).items()):
        vs,fix,trip=constraints(S); n=len(vs);free,tors,diag=kernel(n,fix+list(trip));period=12//gcd(12,*S)
        unique=free==0 and tors==period
        summaries.append(dict(support=S,indicator_count=count,period=period,variables=vs,distinct_cubic_rows=len(trip),free_phase_dimensions=free,smith_diagonal=diag,torus_kernel_components=tors,ambient_identifiable_up_to_translation=unique))
        if S==Qsupport:
            for t in range(n-len(fix),len(trip)+1):
                solutions=[[trip[r] for r in rs] for rs in combinations(trip,t) if kernel(n,fix+list(rs))[:2]==(0,period)]
                if solutions:q_min=dict(terms=t,number_of_minimal_row_sets=len(solutions),examples=solutions);break
    assert q_min['terms']==4 and q_min['number_of_minimal_row_sets']==8
    identifiable=sum(s['indicator_count'] for s in summaries if s['ambient_identifiable_up_to_translation'])
    assert identifiable==3834
    # Exact full triple correlations on binary indicators, up to translation.
    reps=sorted({canon(m) for m in range(M)}); groups=defaultdict(list)
    for a in reps:
        rr=[rot(a,t) for t in range(12)]
        sig=tuple((a&rr[i]&rr[j]).bit_count() for i in range(12) for j in range(i,12))
        groups[sig].append(a)
    ambiguous=[v for v in groups.values() if len(v)>1]
    assert len(reps)==352 and len(groups)==351 and ambiguous==[[315,441]]
    a,b=ambiguous[0];quartic=[]
    for m in (a,b):quartic.append(mul(mul(mul(F[m][1],F[m][1]),F[m][1]),F[m][9]))
    assert quartic==[(-8,0,0,-24),(-8,0,0,24)] # z^3=-i
    # Walsh indicator of the 48 states on the additive Boolean cube.
    w=[0]*M
    for q in Q:w[q]=1
    h=1
    while h<M:
        for i in range(0,M,2*h):
            for j in range(i,i+h):
                a0,b0=w[j],w[j+h];w[j],w[j+h]=a0+b0,a0-b0
        h*=2
    s=[i for i in range(1,M) if w[i]];ix={k:i for i,k in enumerate(s)}
    tr=[]
    for a0,b0 in combinations(s,2):
        c=a0^b0
        if c>b0 and c in ix:tr.append((1<<ix[a0])^(1<<ix[b0])^(1<<ix[c]))
    d=rank2(s);r=rank2(tr)
    stabilizer=[m for m in range(M) if all((m&k).bit_count()%2==0 for k in s)]
    row_flips={0}
    for row in rows:row_flips|={m^mask(row) for m in row_flips}
    assert set(stabilizer)==row_flips and d==9 and len(s)==511 and r==502
    assert sum(x*x for x in w)==M*len(Q)
    out=dict(z12=dict(translation_classes=len(reps),full_triple_classes=len(groups),ambiguous_pair=[bits(a),bits(b)],quartic_coefficients=quartic,quartic_complex=['-8+24i','-8-24i'],ambient_identifiable_count=identifiable,ambient_ambiguous_count=M-identifiable,support_types=len(summaries),support_analysis=summaries,Q48_support=Qsupport,Q48_minimal_complex_cubic_constraints=q_min),walsh=dict(Q48_size=len(Q),coefficient_histogram=dict(sorted(Counter(w).items())),support_size=len(s)+1,support_span_dimension=d,translation_stabilizer=stabilizer,nonconstant_sign_variables=len(s),distinct_triple_constraints=len(tr),GF2_rank=r,sign_ambiguity_bits_mod_translation=len(s)-d,remaining_bits_after_full_bispectrum=len(s)-r-d))
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
