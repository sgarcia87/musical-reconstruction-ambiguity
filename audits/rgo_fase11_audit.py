#!/usr/bin/env python3
"""RGO XI — combinatorial prior, phase identifiability and noisy observations.
Python >=3.10; numpy, sympy. Exact counts via spatial decks and independent
cyclotomic support + Hermite normal form (not the previous SNF code).
"""
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement
from math import gcd, factorial, log2
import json, math
import numpy as np
from sympy import Matrix, Poly, cyclotomic_poly, symbols
from sympy.matrices.normalforms import hermite_normal_form


def rotate(m,t,n):
    t%=n
    return ((m<<t)|(m>>(n-t)))&((1<<n)-1)
def orbit(m,n):return {rotate(m,t,n) for t in range(n)}
def notes(m,n):return [i for i in range(n) if m>>i&1]
def inv(m,n):return sum(1<<((-i)%n) for i in notes(m,n))
def reps(n):
    # Visit each rotation class just once.
    seen=set();r=[]
    for m in range(1<<n):
        if m not in seen:
            r.append(m);seen.update(orbit(m,n))
    return r

def patterns(n,k):
    # Every translation class of k distinct positions contains 0 in some translate.
    return sorted({min(orbit(1|sum(1<<i for i in c),n)) for c in combinations(range(1,n),k-1)})

def signature(m,pats,n):
    # Count translated patterns (including stabilizer multiplicity, as in correlation).
    return tuple(sum(m&rotate(p,t,n)==rotate(p,t,n) for t in range(n)) for p in pats)

def support_factory(n):
    # For integer coefficients, a character of order d vanishes iff Phi_d divides P.
    # Compute residues of X^j for each divisor d and use integer sums.
    x=symbols('x');ds=[d for d in range(2,n+1) if n%d==0];basis={}
    for d in ds:
        ph=Poly(cyclotomic_poly(d,x),x); deg=ph.degree();p=[int(ph.nth(i)) for i in range(deg)]
        v=[1]+[0]*(deg-1);vs=[]
        for j in range(n):
            vs.append(v);z=v[-1];v=[-z*p[0]]+[v[i-1]-z*p[i] for i in range(1,deg)]
        basis[d]=vs
    def s(m):
        a=notes(m,n);live={d for d,vs in basis.items() if any(sum(vs[j][i] for j in a) for i in range(len(vs[0])))}
        return tuple(k for k in range(1,n) if n//gcd(k,n) in live)
    return s


def ambient_orders(n,S,max_order=4):
    # Lattice in Z^m: realness, fixed DC, zero-sum monomials. HNF computes
    # index of row lattice. Full index equals order of translation group acting faithfully.
    v=[k for k in S if k<=n//2];m=len(v)
    if not m:return 1,0,1,1 # constant, with supplied spectrum and DC; aggregate with order 2
    period=n//gcd(n,*S)
    def e(k):return tuple(int(k==j)-int(k==(n-j)%n and k!=j) for j in v)
    rows=set()
    if n%2==0 and n//2 in v:rows.add(tuple(2*int(j==n//2) for j in v))
    free3=None; index3=None
    for r in range(2,max_order+1):
        for a in combinations_with_replacement(S,r):
            if sum(a)%n:continue
            u=tuple(map(sum,zip(*(e(k) for k in a))))
            if any(u):rows.add(u)
        if rows:
            h=hermite_normal_form(Matrix(list(rows)).T)
            rank=h.cols
            index=abs(int(h.det())) if rank==m else None
        else:rank=0;index=None
        if r==3:free3=m-rank;index3=index
        if index==period:
            if r==2:free3=0;index3=index
            return r,free3,index3,period
    return None,free3,index3,period


def binary_audit(n,ambient=True):
    rr=reps(n);w={m:len(orbit(m,n)) for m in rr}
    # Refine partitions in order; distinct-position decks + all lower orders
    # equivalent to full ordered correlation data for binary indicators.
    gr=defaultdict(list)
    for m in rr:gr[m.bit_count()].append(m)
    found={m:1 for g in gr.values() if len(g)==1 for m in g}
    by_order={1:gr};remaining=[g for g in gr.values() if len(g)>1]
    for k in range(2,5):
        pats=patterns(n,k);new=[]
        for g in remaining:
            parts=defaultdict(list)
            for m in g:parts[signature(m,pats,n)].append(m)
            for g2 in parts.values():
                if len(g2)==1:found[g2[0]]=k
                else:new.append(g2)
        remaining=new;by_order[k]=remaining
    assert len(found)+sum(map(len,remaining))==len(rr)
    hist=Counter();trans=Counter()
    for m in rr:hist[str(found.get(m,'>4'))]+=w[m]
    out=dict(n=n,translation_classes=len(rr),binary_orders=dict(hist),ambiguous_after_2=[g for g in by_order[2]],ambiguous_after_3=by_order[3],unresolved_after_4=remaining)
    if ambient:
        sf=support_factory(n);sc={m:sf(m) for m in rr};counts=Counter();support_results={}
        for s in sorted(set(sc.values())):support_results[s]=ambient_orders(n,s)
        joint=Counter();types=defaultdict(lambda:Counter());gaps=[]
        for m,s in sc.items():
            r,free,index,per=support_results[s];k=found.get(m,'>4');label=str(r) if r is not None else '>4'
            counts[label]+=w[m];joint[(str(k),label)]+=w[m];types[s][str(k)]+=w[m]
            if r==4 and k<=3:gaps.append(m)
        out.update(ambient_orders=dict(counts),joint=[{'binary_order':a,'ambient_order':b,'count':v} for (a,b),v in sorted(joint.items())],support_details=[dict(support=[0,*s] if s else [],count=sum(types[s].values()),min_real_order=r[0],free_dimensions_after_3=r[1],index_after_3=r[2],period=r[3],binary_orders=dict(types[s])) for s,r in support_results.items()],gap_classes=len(gaps))
    return out


def overlap(a,b,n):return [(a&rotate(b,t,n)).bit_count() for t in range(n)]
def moment_diff_numerator(a,b,n,k):return sum(v**k for v in overlap(a,a,n))+sum(v**k for v in overlap(b,b,n))-2*sum(v**k for v in overlap(a,b,n))

def noise_example(a,b,n):
    nums=[moment_diff_numerator(a,b,n,k) for k in range(1,5)]
    r=next(i for i,v in enumerate(nums,1) if v)
    lead=nums[r-1]/(n*factorial(r))
    # Weighted L2 distance between orbit-mixture densities, divided by Gaussian
    # density at zero mean. Evaluate positive Taylor series to avoid cancellation.
    coeff=[moment_diff_numerator(a,b,n,k)/(n*factorial(k)) for k in range(1,81)]
    assert all(v>=0 for v in coeff)
    curve=[]
    for sigma in (1,2,4,8,16,32):
        dist=sum(v/sigma**(2*k) for k,v in enumerate(coeff,1))
        curve.append(dict(sigma=sigma,weighted_L2=dist,scaled=dist*sigma**(2*r)))
    return dict(A=notes(a,n),B=notes(b,n),first_distinguishing_order=r,moment_squared_norms=[v/n for v in nums],leading_coefficient=lead,curve=curve)


def adaptive_audit(n,groups,seed=11026,trials=6000):
    # Conditional on exact 2-deck, choose one translated triple/quadruple count
    # per step; observe count + independent Gaussian noise, same noise per query.
    # Compare greedy posterior variance (expected spread proxy), fixed repeated
    # max-variance, fixed diversified (greedy minimize pairwise Gaussian
    # affinity sum), and informative uniform random.
    # All use exact same candidate list and Bayesian decoder, equal query counts.
    rng=np.random.default_rng(seed)
    pats=patterns(n,3)+patterns(n,4)
    groups=[g for g in groups if len(g)>1]
    # Only query features that differ inside the prior family; retain all others
    # for global fixed/random baselines (global count dictionary).
    values=[np.array([signature(m,pats,n) for m in g],float) for g in groups]
    # Normalize counts by pattern stabilizer so every measurement is a count of
    # DISTINCT translated patterns, same units even for symmetric patterns.
    norm=np.array([n/len(orbit(p,n)) for p in pats]);values=[v/norm for v in values]
    results=[]
    for sigma in (0.5,1.,2.):
        for steps in (1,3,6,12):
            scores={}
            # Equal weighting over classes; exact known family (not uniform over groups).
            gi=rng.choice(len(groups),size=trials,p=np.array([len(g) for g in groups])/sum(map(len,groups)))
            # Common truths and noise for comparisons.
            true=np.array([rng.integers(len(groups[g])) for g in gi]);noise=rng.normal(0,sigma,(trials,steps))
            for mode in ('adaptive','fixed','fixed_diverse','random'):
                success=0;entropy=0.;multi_success=0.;multi_n=0
                for g,V in enumerate(values):
                    ii=np.flatnonzero(gi==g)
                    if not len(ii):continue
                    ntr=len(ii);K=len(groups[g]);post=np.ones((ntr,K))/K;target=V[true[ii]]
                    usable=np.flatnonzero(np.ptp(V,axis=0)>0)
                    # Best fixed scalar variance per family; repeats permitted equally in all modes.
                    fixed=int(np.argmax(V.var(axis=0)))
                    # Predetermined schedule: choose the next feature that minimizes
                    # sum of Bhattacharyya affinities between the Gaussian likelihoods.
                    # This is a stronger nonadaptive baseline than repeating one feature.
                    pairs=list(combinations(range(K),2))
                    affinity=np.exp(-np.array([(V[a]-V[b])**2 for a,b in pairs])/(8*sigma*sigma))
                    weights=np.ones(len(pairs));schedule=[]
                    for _ in range(steps):
                        q=int(np.argmin(weights@affinity));schedule.append(q);weights*=affinity[:,q]
                    for t in range(steps):
                        if mode=='adaptive':
                            means=post@V;var=post@(V*V)-means*means;qs=var.argmax(axis=1)
                        elif mode=='fixed':qs=np.full(ntr,fixed)
                        elif mode=='fixed_diverse':qs=np.full(ntr,schedule[t])
                        else:qs=rng.choice(usable,size=ntr)
                        obs=target[np.arange(ntr),qs]+noise[ii,t];pred=V[:,qs].T
                        log=np.log(np.maximum(post,1e-300))-(pred-obs[:,None])**2/(2*sigma*sigma)
                        log-=log.max(axis=1,keepdims=True);post=np.exp(log);post/=post.sum(axis=1,keepdims=True)
                    # For MAP ties, fractional correct probability rather than arbitrary ordering.
                    mx=post.max(axis=1);ties=np.isclose(post,mx[:,None],rtol=1e-12,atol=1e-15)
                    correct=np.sum(ties[np.arange(ntr),true[ii]]/ties.sum(axis=1));success+=correct
                    if K>2:multi_success+=correct;multi_n+=ntr
                    entropy+=float(-np.sum(post*np.log2(np.maximum(post,1e-300))))
                scores[mode]=dict(accuracy=success/trials,posterior_entropy_bits=entropy/trials,multi_candidate_accuracy=multi_success/multi_n,multi_candidate_n=multi_n)
            results.append(dict(sigma=sigma,queries=steps,trials=trials,**scores))
    return dict(n=n,families=len(groups),classes=sum(map(len,groups)),family_size_hist=dict(Counter(map(len,groups))),feature_count=len(pats),results=results,seed=seed)


def robust_audit(n,groups):
    from functools import lru_cache
    pats=patterns(n,3)+patterns(n,4);pairs=[(a,b) for g in groups for a,b in combinations(g,2)]
    val={m:signature(m,pats,n) for g in groups for m in g}
    sep=[{i for i,(x,y) in enumerate(zip(val[a],val[b])) if x!=y} for a,b in pairs]
    # Lower-bound witness: seven disjoint sets of distinguishing queries,
    # from pairs of reflected trichords, plus one from the 3-deck collision.
    witness=[i for i,(a,b) in enumerate(pairs) if a.bit_count()==3 and len(sep[i])==2]
    witness += [pairs.index((315,441))]
    assert len(witness)==8
    assert all(not (sep[i]&sep[j]) for i,j in combinations(witness,2))
    def idx(ns):return pats.index(min(orbit(sum(1<<i for i in ns),n)))
    q1=[[0,1,3],[0,3,4],[0,3,5],[0,4,5],[0,4,6],[0,5,6],[0,3,7],[0,3,4,8]]
    q2=[[0,1,3],[0,2,3],[0,1,4],[0,3,4],[0,1,5],[0,2,5],[0,3,5],[0,4,5],[0,1,6],[0,2,6],[0,4,6],[0,5,6],[0,3,7],[0,4,7],[0,1,4,8],[0,3,4,8]]
    assert len(set(map(idx,q1)))==8 and min(len(s&set(map(idx,q1))) for s in sep)==1
    assert len(set(map(idx,q2)))==16 and min(len(s&set(map(idx,q2))) for s in sep)==2
    assert min(map(len,sep))==2
    stats=Counter();adaptive_example=None
    for g in groups:
        V=[val[m] for m in g]
        for k in range(1,4):
            fixed=next((inds for inds in combinations(range(len(pats)),k) if len({tuple(v[i] for i in inds) for v in V})==len(g)),None)
            if fixed is not None:break
        assert fixed is not None
        @lru_cache(None)
        def tree(state):
            if len(state)==1:return (0,{'candidate':state[0]})
            best=(100,None)
            for j,p in enumerate(pats):
                part=defaultdict(list)
                for i in state:part[V[i][j]].append(i)
                if len(part)<=1:continue
                sub={v:tree(tuple(ss)) for v,ss in part.items()}
                depth=1+max(r[0] for r in sub.values())
                if depth<best[0]:best=(depth,{'pattern':notes(p,n),'branches':{v:r[1] for v,r in sub.items()}})
            return best
        dep,t=tree(tuple(range(len(g))))
        stats[(len(g),k,dep)]+=1
        if dep<k:adaptive_example=dict(candidates=[notes(m,n) for m in g],fixed_min=k,adaptive_min=dep,tree=t,fixed_example=[notes(pats[i],n) for i in fixed])
    return dict(known_exact_2deck=True,features_by_order={'3':len(patterns(n,3)),'4':len(patterns(n,4))},pair_count=len(pairs),global_min_queries=8,global_min_queries_for_one_erasure=16,global_min_queries_for_one_arbitrary_error=24,arbitrary_error_requires_repetition=True,min_distance_full_distinct_dictionary=2,noiseless_fixed_patterns=q1,one_erasure_distinct_patterns=q2,lower_bound_witness=[{'A':notes(pairs[i][0],n),'B':notes(pairs[i][1],n),'separating_patterns':[notes(pats[j],n) for j in sorted(sep[i])]} for i in witness],fixed_adaptive_per_family=[dict(family_size=a,fixed=b,adaptive=c,families=v) for (a,b,c),v in sorted(stats.items())],adaptive_example=adaptive_example)


def main():
    # n <= 16 as a manageable complete census; 12 singled out for musical reading.
    audits=[binary_audit(n) for n in range(2,17)]
    z=audits[10];assert z['n']==12
    assert z['ambient_orders']=={'1':2,'2':2,'3':3830,'4':262},z['ambient_orders']
    assert z['ambiguous_after_3']==[[315,441]],z['ambiguous_after_3']
    assert not z['unresolved_after_4']
    # All binary T/I Z-related pairs, and direct comparison of unoriented trichord content.
    ti_reps=sorted({min(min(orbit(m,12)),min(orbit(inv(m,12),12))) for m in reps(12)})
    p2=patterns(12,2);p3=patterns(12,3)
    f=defaultdict(list)
    for m in ti_reps:f[(m.bit_count(),signature(m,p2,12))].append(m)
    zpair=[]
    for g in f.values():
        for a,b in combinations(g,2):
            ca,cb=signature(a,p3,12),signature(b,p3,12)
            dif=[]
            for p in p3:
                ip=min(orbit(inv(p,12),12))
                if p>ip:continue
                i=p3.index(p);j=p3.index(ip)
                # Counts of actual subsets (not translated-pattern multiplicity).
                v1=ca[i]*len(orbit(p,12))//12;v2=cb[i]*len(orbit(p,12))//12
                if j!=i:v1+=ca[j]*len(orbit(ip,12))//12;v2+=cb[j]*len(orbit(ip,12))//12
                if v1!=v2:dif.append(dict(trichord=notes(p,12),count_A=v1,count_B=v2))
            assert dif
            zpair.append(dict(A=notes(a,12),B=notes(b,12),cardinality=a.bit_count(),different_trichord_types=len(dif),example=dif[0]))
    assert len(zpair)==23 and sum(x['cardinality']==6 for x in zpair)==15
    noise=[noise_example(315,441,12),noise_example(sum(1<<i for i in [0,1,2,3,4,8]),sum(1<<i for i in [0,1,2,4,5,6]),12)]
    # Compare actual differences for every pair with the same 2-deck.
    cnt=Counter();leading=defaultdict(Counter)
    for g in z['ambiguous_after_2']:
        for a,b in combinations(g,2):
            k=next(k for k in (3,4) if moment_diff_numerator(a,b,12,k));cnt[k]+=1
            leading[k][str(moment_diff_numerator(a,b,12,k)/12)]+=1
    z['all_homometric_pair_first_distinguishing_order']=dict(cnt);z['first_moment_squared_norm_histogram']=dict(leading)
    out=dict(census=[{k:v for k,v in a.items() if k not in ('ambiguous_after_2','ambiguous_after_3','support_details','unresolved_after_4')} for a in audits],z12=z,z_pairs=zpair,noise_examples=noise,adaptive=adaptive_audit(12,z['ambiguous_after_2']),robust=robust_audit(12,z['ambiguous_after_2']))
    print(json.dumps(out,indent=2,ensure_ascii=False))
if __name__=='__main__':main()
