import json,random,time,math,numpy as np
from functools import lru_cache
from itertools import combinations,product
from pathlib import Path
from statistics import mean,median
from collections import defaultdict,Counter

def implicit(w,k,cap=300000):
 n=len(w);d=2**(k-1);m=[0]*(2*d);s=int(w[:k-1],2);t=int(w[-k+1:],2)
 for i in range(n-k+1):m[int(w[i:i+k],2)]+=1
 m=tuple(m);visited=0
 def edges(v,r):
  for b in (0,1):
   e=2*v+b
   if r[e]:yield b,e%(d),r[:e]+(r[e]-1,)+r[e+1:]
 @lru_cache(None)
 def C(v,r):
  nonlocal visited
  visited+=1
  if visited>cap:raise OverflowError
  return sum(C(u,z) for b,u,z in edges(v,r)) if any(r) else int(v==t)
 N=C(s,m);p=[0]*n;J=[[0]*n for _ in range(n)];pre=list(map(int,w[:k-1]));layer={(s,m):(1,pre)};peak=1
 for j,b in enumerate(pre):
  p[j]=N*b
  for i in range(j):J[i][j]=N*pre[i]*b
 for j in range(k-1,n):
  nxt={}
  for (v,r),(a,vec) in layer.items():
   for b,u,z in edges(v,r):
    c=C(u,z)
    if not c:continue
    if b:
     p[j]+=a*c
     for i,x in enumerate(vec):J[i][j]+=x*c
    q=(u,z);vv=vec+[a*b]
    if q in nxt:
     aa,xx=nxt[q];nxt[q]=(aa+a,[x+y for x,y in zip(xx,vv)])
    else:nxt[q]=(a,vv)
  layer=nxt;peak=max(peak,len(layer))
 assert sum(a for a,_ in layer.values())==N
 C.cache_clear()
 return N,[*p,*[p[i]+p[j]-2*J[i][j] for i,j in combinations(range(n),2)]],visited,peak

def explicit(ws):
 a=np.array([list(map(int,w)) for w in ws],dtype=np.int64);n=a.shape[1];p=a.sum(0);J=a.T@a
 return [*map(int,p),*[int(p[i]+p[j]-2*J[i,j]) for i,j in combinations(range(n),2)]]

def graph(w,k):
 d=2**(k-1);m=[0]*(2*d)
 for i in range(len(w)-k+1):m[int(w[i:i+k],2)]+=1
 return m,int(w[:k-1],2),int(w[-k+1:],2),d

def bridge(w,k):
 n=len(w);m,s,t,d=graph(w,k);P=np.zeros((d,d));T=n-k+1
 for v in range(d):
  z=sum(m[2*v:2*v+2])
  if z:
   for b in (0,1):P[v,(2*v+b)%d]+=m[2*v+b]/z
 A=[np.eye(d)]
 for _ in range(T):A.append(A[-1]@P)
 norm=A[T][s,t];bits=np.arange(d)%2;a=[];r=[]
 for i in range(n):
  u=i-k+2;a.append(int(w[i]) if u<=0 else (A[u][s]*bits)@A[T-u][:,t]/norm)
 for i,j in combinations(range(n),2):
  u=i-k+2;v=j-k+2;c=a[i]*a[j] if u<=0 else ((A[u][s]*bits)@A[v-u]*bits)@A[T-v][:,t]/norm
  r.append(a[i]+a[j]-2*c)
 return np.array(a+r)

def sample(w,k,rng):
 m,s,t,d=graph(w,k);out={v:[(2*v+b)%d for b in (0,1) for _ in range(m[2*v+b])] for v in range(d) if sum(m[2*v:2*v+2])};tree={t};last={}
 for v in out:
  u=v
  while u not in tree:last[u]=rng.randrange(len(out[u]));u=out[u][last[u]]
  u=v
  while u not in tree:tree.add(u);u=out[u][last[u]]
 for v,a in out.items():
  if v==t:rng.shuffle(a)
  else:x=a.pop(last[v]);rng.shuffle(a);a.append(x)
  a.reverse()
 v=s;ans=w[:k-1]
 for _ in range(len(w)-k+1):v=out[v].pop();ans+=str(v%2)
 assert graph(ans,k)==(m,s,t,d)
 return ans

def entropy(p):
 p=np.clip(np.asarray(p,dtype=float),0,1);a=(p>0)&(p<1);o=np.zeros_like(p);q=p[a];o[a]=-q*np.log2(q)-(1-q)*np.log2(1-q);return o

def evaluate(w,k,ws=None,seed=1):
 t=time.perf_counter();N,C,states,peak=implicit(w,k);dt=time.perf_counter()-t
 if ws is not None:assert N==len(ws) and C==explicit(ws)
 true=np.array([c/N for c in C]);H=entropy(true);n=len(w);rng=random.Random(seed)
 t=time.perf_counter();bp=bridge(w,k);bt=time.perf_counter()-t;q=int(np.argmax(entropy(bp)))
 t=time.perf_counter();sp=np.array(explicit([sample(w,k,rng) for _ in range(64)]))/64;st=time.perf_counter()-t;sq=int(np.argmax(entropy(sp)))
 allowed=list(range(k-1,n-k+1))+[n+i for i,(a,b) in enumerate(combinations(range(n),2)) if k-1<=a<n-k+1 or k-1<=b<n-k+1]
 return dict(n=n,k=k,N=str(N),states=states,peak=peak,exact_s=dt,bridge_s=bt,sample_s=st,opt=float(max(H)),bridge=float(H[q]),sample=float(H[sq]),random=float(H[allowed].mean()),bridge_error=float(np.mean(abs(bp-true))),sample_error=float(np.mean(abs(sp-true))),bridge_constant=bool(H[q]<1e-14),sample_constant=bool(H[sq]<1e-14))

def summary(rows):
 keys=['opt','bridge','sample','random','bridge_error','sample_error','exact_s','bridge_s','sample_s','states','peak']
 return dict(n=len(rows),**{k:mean(r[k] for r in rows) for k in keys},bridge_opt=sum(abs(r['bridge']-r['opt'])<1e-12 for r in rows),sample_opt=sum(abs(r['sample']-r['opt'])<1e-12 for r in rows),bridge_constant=sum(r['bridge_constant'] for r in rows),sample_constant=sum(r['sample_constant'] for r in rows),max_candidates=max(int(r['N']) for r in rows),median_candidates=median(int(r['N']) for r in rows))
if __name__=='__main__':
 small=[]
 for n,k in [(8,2),(8,3),(10,2),(10,3),(12,2),(12,3)]:
  fibers=defaultdict(list)
  for w in map(''.join,product('01',repeat=n)):
   sig=(w[:k-1],w[-k+1:],tuple(sorted(Counter(w[i:i+k] for i in range(n-k+1)).items())))
   fibers[sig].append(w)
  for ws in fibers.values():
   if 2<=len(ws)<=32:small.append(evaluate(ws[0],k,ws,1000+len(small)))
 print('SMALL',summary(small),flush=True)
 rng=random.Random(20261126);large=[];fail=[];summaries=[]
 for n,k,rep in [(32,2,12),(64,2,12),(128,2,6),(24,3,8),(32,3,6),(48,3,4)]:
  rows=[]
  for i in range(rep):
   w=''.join(rng.choice('01') for _ in range(n))
   try:rows.append(evaluate(w,k,seed=50000+n*100+i))
   except OverflowError:fail.append((n,k,i))
  large+=rows;v=summary(rows) if rows else None;summaries.append([n,k,v]);print(n,k,v,'failures',len(fail),flush=True)
 json.dump(dict(small=small,large=large,failures=fail,summaries=summaries),open(Path(__file__).parent/'results.json','w'),indent=2)
