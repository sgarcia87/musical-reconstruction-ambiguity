#!/usr/bin/env python3
"""Reproduce temporal observability tests with JSB-Chorales quarter-note JSON.
Usage: python audits/temporal_corpus.py [jsb-chorales-quarter.json]
If no path, fetch the public dataset from the original GitHub repo.
Uses exact integer arithmetic for Fourier zeros, and connectivity only.
Local orbit labels are assumed known up to pitch transposition, NOT inferred
from magnitude alone. Reconstructs pitch-class windows, not original audio.
"""
import json, sys, hashlib, urllib.request
from collections import Counter
from math import gcd, lcm, log2
URL='https://raw.githubusercontent.com/czhuang/JSB-Chorales-dataset/master/jsb-chorales-quarter.json'
Z=[(1,0,0,0)]
for _ in range(11):
    a,b,c,d=Z[-1];Z.append((-d,a,b+d,c))
orders=[12//gcd(k,12) for k in range(12)]
levels=[2,4,3]
primes=[2,2,3]
def support(m):
    s=0
    for k in range(1,12):
        vals=[Z[k*j%12] for j in range(12) if m>>j&1]
        if any(sum(v[q] for v in vals) for q in range(4)): s|=1<<k
    return s
S=list(map(support,range(4096)))
P=[lcm(*(orders[k] for k in range(1,12) if s>>k&1)) for s in S]
LM=[sum(1<<k for k in range(1,12) if orders[k]%l==0) for l in levels]
class DS:
    def __init__(self,seq,l):
        self.p=list(range(len(seq)));self.c=sum(P[m]%l==0 for m in seq)
    def root(self,i):
        while self.p[i]!=i:self.p[i]=self.p[self.p[i]];i=self.p[i]
        return i
    def join(self,i,j):
        a,b=self.root(i),self.root(j)
        if a!=b:self.p[a]=b;self.c-=1

def graph(seq,mode):
    ds=[DS(seq,l) for l in levels]
    n=len(seq)
    if mode in ('adjacent','F1'):
        for i in range(n-1):
            s=S[seq[i]]&S[seq[i+1]]
            if mode=='F1':s&=2
            for j,d in enumerate(ds):
                if s&LM[j]:d.join(i,i+1)
    elif mode in ('all','anchor'):
        # All same-frequency clique edges can be replaced with a star.
        for k in ([1] if mode=='anchor' else range(1,12)):
            vs=[i for i,m in enumerate(seq) if S[m]>>k&1]
            for j,d in enumerate(ds):
                if orders[k]%levels[j]==0:
                    for v in vs[1:]:d.join(vs[0],v)
    else:raise ValueError(mode)
    return ds

def repair(seq):
    ds=graph(seq,'adjacent');n=len(seq)
    lower=max(0,*(d.c-1 for d in ds));chosen=[]
    while any(d.c>1 for d in ds):
        best=None
        for lag in range(2,n):
            for i in range(n-lag):
                j=i+lag;s=S[seq[i]]&S[seq[j]]
                qs=[q for q,d in enumerate(ds) if s&LM[q] and d.root(i)!=d.root(j)]
                if qs and (best is None or len(qs)>len(best[2])):best=(i,j,qs)
                if best and len(best[2])==3:break
            if best and len(best[2])==3:break
        if best is None:break
        i,j,qs=best
        for q in qs:ds[q].join(i,j)
        chosen.append((i,j))
    return lower,chosen,all(d.c<=1 for d in ds)

def mask(notes):return sum(1<<i for i in {n%12 for n in notes})
def windows(song,w):
    ms=list(map(mask,song));out=[]
    for i in range(len(ms)-w+1):
        m=0
        for a in ms[i:i+w]:m|=a
        out.append(m)
    return out

def audit(data):
    results=[]
    for w in (1,2,4,8):
        o=dict(w=w,pieces=0,windows=0,nonzeroF1=0,period12=0,splits={})
        for mode in ('adjacent','all','F1','anchor'):o[mode]=dict(exact=0,meanAmbiguityBits=0.)
        o['repair']=dict(exact=0,additional_edges=0,lower_bound_sum=0,optimal_certified=0,max_edges=0,histogram=Counter())
        for split,songs in data.items():
            sp=dict(pieces=0,exactAdj=0,exactAll=0);o['splits'][split]=sp
            for song in songs:
                seq=windows(song,w)
                if not seq:continue
                o['pieces']+=1;sp['pieces']+=1;o['windows']+=len(seq)
                o['nonzeroF1']+=sum(bool(S[m]&2) for m in seq);o['period12']+=sum(P[m]==12 for m in seq)
                for mode in ('adjacent','all','F1','anchor'):
                    ds=graph(seq,mode);amb=sum(max(0,d.c-1)*log2(p) for d,p in zip(ds,primes))
                    o[mode]['meanAmbiguityBits']+=amb
                    if amb==0:
                        o[mode]['exact']+=1
                        if mode=='adjacent':sp['exactAdj']+=1
                        if mode=='all':sp['exactAll']+=1
                lo,edges,exact=repair(seq);k=len(edges);r=o['repair'];r['exact']+=exact;r['additional_edges']+=k;r['lower_bound_sum']+=lo;r['optimal_certified']+=exact and k==lo;r['max_edges']=max(r['max_edges'],k);r['histogram'][k]+=1
        for mode in ('adjacent','all','F1','anchor'):o[mode]['meanAmbiguityBits']/=o['pieces'] or 1
        results.append(o)
    return results
if __name__=='__main__':
    raw=open(sys.argv[1],'rb').read() if len(sys.argv)>1 else urllib.request.urlopen(URL,timeout=60).read()
    sha=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    print(json.dumps(dict(git_blob_sha1=sha,results=audit(json.loads(raw))),indent=2))
