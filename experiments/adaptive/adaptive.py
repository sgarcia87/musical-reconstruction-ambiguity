import math,random,time,json,sys
from collections import defaultdict,Counter
from functools import lru_cache
from itertools import product,combinations
from pathlib import Path
from statistics import mean
from first_query import graph

# Condition on unary observations and XOR edges. Components encode parity relative
# to a root; an unfixed component is stored only between its first and last visit.
def constraints(n,obs,w,k):
    adj=[[] for _ in range(n)]; fixed={i:int(w[i]) for i in set(range(k-1))|set(range(n-k+1,n))}
    for (i,j),b in obs:
        if j is None:
            if i in fixed: assert fixed[i]==b
            fixed[i]=b
        else: adj[i].append((j,b));adj[j].append((i,b))
    seen={};rules=[None]*n
    for i in range(n):
        if i in seen:continue
        stack=[i];seen[i]=0;comp=[]
        while stack:
            v=stack.pop();comp.append(v)
            for u,b in adj[v]:
                p=seen[v]^b
                if u in seen:assert seen[u]==p
                else:seen[u]=p;stack.append(u)
        vals={fixed[v]^seen[v] for v in comp if v in fixed};assert len(vals)<=1
        if vals:
            root=next(iter(vals))
            for v in comp:rules[v]=(0,root^seen[v],0)
        elif len(comp)==1:rules[i]=(1,0,0)
        else:
            mask=1<<i;end=max(comp)
            for v in comp:rules[v]=(2 if v==i else 3 if v==end else 4,seen[v],mask)
    return rules

class Limit(Exception):pass
class Engine:
    def __init__(self,w,k,obs=(),cap=100000):
        self.n=n=len(w);self.k=k;self.w=w;self.obs=obs;self.cap=cap;self.states=0
        m,s,t,d=graph(w,k);self.s=s;self.t=t;self.m=tuple(m);self.d=d;self.rules=constraints(n,obs,w,k)
        @lru_cache(None)
        def C(v,r,a):
            self.states+=1
            if self.states>cap:raise Limit()
            if not any(r):return int(v==t)
            return sum(C(*q) for b,q in self.edges(v,r,a))
        self.C=C
        self.start=(s,self.m,0)
        self.N=C(*self.start)
        assert self.N>0
    def edges(self,v,r,a):
        j=self.n-sum(r);kind,p,mask=self.rules[j]
        for b in (0,1):
            e=2*v+b
            if not r[e]:continue
            z=a
            if kind==0 and b!=p:continue
            if kind==2:
                if b^p:z|=mask
            if kind in (3,4):
                if b!=(int(bool(a&mask))^p):continue
                if kind==3:z&=~mask
            yield b,(e%self.d,r[:e]+(r[e]-1,)+r[e+1:],z)
    def marginals(self,relations=True):
        n=self.n;k=self.k;N=self.N;pre=list(map(int,self.w[:k-1]));p=[0]*n;J=[[0]*n for _ in range(n)] if relations else None
        layer={self.start:(1,pre if relations else [])}
        for j,b in enumerate(pre):
            p[j]=N*b
            if relations:
                for i in range(j):J[i][j]=N*pre[i]*b
        for j in range(k-1,n):
            nxt={}
            for st,(a,vec) in layer.items():
                for b,q in self.edges(*st):
                    c=self.C(*q)
                    if not c:continue
                    if b:
                        p[j]+=a*c
                        if relations:
                            for i,x in enumerate(vec):J[i][j]+=x*c
                    vv=vec+[a*b] if relations else []
                    if q in nxt:
                        aa,xx=nxt[q];nxt[q]=(aa+a,[x+y for x,y in zip(xx,vv)])
                    else:nxt[q]=(a,vv)
            layer=nxt
        assert sum(a for a,_ in layer.values())==N
        out={(i,None):v for i,v in enumerate(p)}
        if relations:out.update({(i,j):p[i]+p[j]-2*J[i][j] for i,j in combinations(range(n),2)})
        return out
    def local_marginals(self,band=3):
        n=self.n;k=self.k;N=self.N;pre=list(map(int,self.w[:k-1]));p=[0]*n;J={}
        layer={self.start:(1,pre[-band:])}
        for j,b in enumerate(pre):
            p[j]=N*b
            for i in range(max(0,j-band),j):J[i,j]=N*pre[i]*b
        for j in range(k-1,n):
            nxt={}
            for st,(a,vec) in layer.items():
                for b,q in self.edges(*st):
                    c=self.C(*q)
                    if not c:continue
                    if b:
                        p[j]+=a*c
                        for i,x in enumerate(vec,j-len(vec)):J[i,j]=J.get((i,j),0)+x*c
                    vv=(vec+[a*b])[-band:]
                    if q in nxt:
                        aa,xx=nxt[q];nxt[q]=(aa+a,[x+y for x,y in zip(xx,vv)])
                    else:nxt[q]=(a,vv)
            layer=nxt
        assert sum(a for a,_ in layer.values())==N
        out={(i,None):v for i,v in enumerate(p)}
        out.update({(i,j):p[i]+p[j]-2*J.get((i,j),0) for i in range(n) for j in range(i+1,min(n,i+band+1))})
        return out
    def sample(self,rng):
        st=self.start;ans=self.w[:self.k-1]
        while any(st[1]):
            u=rng.randrange(self.C(*st))
            for b,q in self.edges(*st):
                c=self.C(*q)
                if u<c:ans+=str(b);st=q;break
                u-=c
            else:raise AssertionError('sample')
        return ans
    def close(self):self.C.cache_clear()

def bit(w,q):i,j=q;return int(w[i]) if j is None else int(w[i])^int(w[j])
def select(m,N):return min(m,key=lambda q:abs(2*m[q]-N))
def explicit(ws,qs):return {q:sum(bit(w,q) for w in ws) for q in qs}
def fiberkey(w,k):return w[:k-1],w[-k+1:],tuple(sorted(Counter(w[i:i+k] for i in range(len(w)-k+1)).items()))
def H(p):return -p*math.log2(p)-(1-p)*math.log2(1-p) if 0<p<1 else 0.

def solve(w,k,mode,seed,ws=None,cap=100000):
    rng=random.Random(seed);obs=[];states=0;peak=0;t0=time.perf_counter();initial=None;remaining=ws;checked=0;fail=False
    while True:
        try:e=Engine(w,k,obs,cap)
        except Limit:fail=True;break
        N=e.N;states+=e.states;peak=max(peak,e.states)
        if initial is None:initial=N
        if remaining is not None:assert N==len(remaining)
        if N==1:
            assert e.sample(rng)==w;e.close();break
        qs=[(i,None) for i in range(len(w))]
        if mode!='positions':qs += [(i,j) for i,j in combinations(range(len(w)),2) if mode!='local' or j-i<=3]
        if mode=='sample':
            # exact posterior samples, no rejection; same conditional counting engine
            sam=[e.sample(rng) for _ in range(32)];m=explicit(sam,qs);q=select(m,len(sam))
            # if all 32 samples identical, find a distinguishing query exactly
            if m[q] in (0,len(sam)):
                m=e.marginals();q=select(m,N)
        else:
            m=e.local_marginals() if mode=='local' else e.marginals(mode!='positions');m={q:m[q] for q in qs};q=select(m,N)
            if remaining is not None:assert m==explicit(remaining,list(m));checked+=len(m)
        b=bit(w,q);obs.append((q,b));e.close()
        if remaining is not None:remaining=[v for v in remaining if bit(v,q)==b]
        if len(obs)>len(w):raise AssertionError('nonprogress')
    return dict(n=len(w),k=k,mode=mode,queries=len(obs),initial=str(initial),states=states,peak=peak,seconds=time.perf_counter()-t0,checks=checked,failed=fail)

if __name__=='__main__':
    rows=[];rng=random.Random(12345)
    for n,k in [(8,2),(8,3),(10,2),(10,3),(12,2),(12,3)]:
        fibers=defaultdict(list)
        for w in map(''.join,product('01',repeat=n)):fibers[fiberkey(w,k)].append(w)
        for ws in fibers.values():
            if 2<=len(ws)<=32:
                # One deterministic random truth per class, shared across methods.
                w=rng.choice(ws)
                for mode in ('positions','relations','sample'):rows.append(solve(w,k,mode,100+len(rows),ws))
        print('small',n,k,len(rows),flush=True)
    for n,k,rep in [(24,2,8),(32,2,8),(48,2,6)]:
        for i in range(rep):
            w=''.join(rng.choice('01') for _ in range(n))
            for mode in ('positions','relations','sample'):
                z=solve(w,k,mode,100+len(rows));rows.append(z);print('large',n,k,i,mode,z['queries'],z['peak'],round(z['seconds'],3),z['failed'],flush=True)
        json.dump(rows,open(Path(__file__).parent/'results.json','w'),indent=2)
    json.dump(rows,open(Path(__file__).parent/'results.json','w'),indent=2)
