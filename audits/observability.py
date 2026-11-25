#!/usr/bin/env python3
"""Q12 — observabilidad exacta y experimento PPR. Python 3.10+, biblioteca estándar.
Bit 0 = Do, filas CRT (n mod 3, n mod 4). PPR: hipercubo Q12 no dirigido,
transiciones uniformes entre 12 vecinos, restart 1-alpha en pares antipodales Q48.
Entropías log2; prior uniforme. La precisión PPR supone UNA muestra del campo.
"""
from collections import Counter
from itertools import combinations
from functools import lru_cache
from math import log2
import json
N=4096; MASK=N-1
ROWS=[[next(n for n in range(12) if n%3==i and n%4==j) for j in range(4)] for i in range(3)]
X=[tuple(1 if m>>i&1 else -1 for i in range(12)) for m in range(N)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def features(x):
 a=[[x[i] for i in row] for row in ROWS];s=tuple(map(sum,a));g=tuple(dot(a[i],a[j]) for i,j in combinations(range(3),2));b=sum(i*i for i in s);o=sum(i*i for i in g)
 ac=tuple(sum(x[i]*x[(i+d)%12] for i in range(12)) for d in range(1,7))
 return (sum(x),b,o,(b,o),s+g,ac,tuple(x[0]*i for i in x[1:]),x)
F=list(map(features,X));Q=[m for m in range(N) if F[m][3]==(0,0)];P=[m for m in Q if not m&1];assert len(Q)==48 and len(P)==24
assert all(m^MASK in Q for m in Q)
labels=['cardinalidad','balance','ortogonalidad','balance_ortogonalidad','sumas_gram','potencia_fourier','relaciones_referencia','signos']
def entropy(p):return -sum(x*log2(x) for x in p if x>0)
counts=[]
for i,n in enumerate(labels):
 row={'observacion':n}
 for k,S in [('Q12',range(N)),('Q48',Q)]:
  c=Counter(F[m][i] for m in S); row[k]={'clases':len(c),'mayor_clase':max(c.values()),'informacion_bits':entropy([v/len(S) for v in c.values()])}
 counts.append(row)
assert [r['Q12']['clases'] for r in counts]==[13,10,5,18,329,118,2048,4096]
assert [r['Q48']['clases'] for r in counts]==[1,1,1,1,1,2,24,48]
coord=[]
for k in range(1,8):
 sizes=[len({m&mask for m in Q}) for inds in combinations(range(12),k) for mask in [sum(1<<i for i in inds)]];coord.append({'k':k,'max_clases':max(sizes),'separadores':sizes.count(48)})
assert coord[-2]['max_clases']==40 and coord[-1]['separadores']==480
pairs=list(combinations(range(12),2))
def query_masks(states,relative):
 qs=pairs if relative else [(i,) for i in range(12)]
 return [sum(1<<j for j,s in enumerate(states) if (sum(s>>i&1 for i in q)%2)) for q in qs]
def fixed_relative(k):
 masks=query_masks(P,True)
 def search(start,groups,depth):
  if all(g.bit_count()==1 for g in groups):return []
  if depth==0 or any(g.bit_count()>2**depth for g in groups):return None
  for i in range(start,len(masks)-depth+1):
   m=masks[i];new=[]
   for g in groups:
    a=g&m;b=g^a
    if a:new.append(a)
    if b:new.append(b)
   if len(new)==len(groups):continue
   r=search(i+1,new,depth-1)
   if r is not None:return [i]+r
  return None
 r=search(0,[(1<<len(P))-1],k);return None if r is None else [pairs[i] for i in r]
assert fixed_relative(5) is None
rel6=fixed_relative(6);assert rel6 is not None

def adaptive(states,relative):
 masks=query_masks(states,relative);qs=pairs if relative else [(i,) for i in range(12)]
 @lru_cache(None)
 def best(c):
  if c.bit_count()<2:return (0,None)
  lower=(c.bit_count()-1).bit_length();ans=(99,None)
  for i,m in enumerate(masks):
   a=c&m;b=c^a
   if a and b:
    d=1+max(best(a)[0],best(b)[0])
    if d<ans[0]:ans=(d,i)
    if d==lower:break
  return ans
 def tree(c):
  d,i=best(c)
  if not d:return {'state':states[c.bit_length()-1]}
  a=c&masks[i];b=c^a
  return {'q':qs[i],'zero':tree(b),'one':tree(a),'depth':d}
 return tree((1<<len(states))-1)
T=adaptive(Q,False);R=adaptive(P,True);assert T['depth']==6 and R['depth']==5
# Map complement to orientation + relational coordinates (CNOT transformation).
def encode(m):return m if not m&1 else (m^MASK)|1
assert len({encode(m) for m in range(N)})==N
assert all(encode(m^MASK)==(encode(m)^1) for m in range(N))
# Walsh-Hadamard diagonalization of PPR, eigenvalues of transition 1-2k/12.
def fwht(a):
 a=a[:];h=1
 while h<len(a):
  for i in range(0,len(a),2*h):
   for j in range(i,i+h):u,v=a[j],a[j+h];a[j]=u+v;a[j+h]=u-v
  h*=2
 return a
ppr=[]
for alpha in (0,.5,.85,.95,.99,.999):
 kernel=[max(0,x/N) for x in fwht([(1-alpha)/(1-alpha*(1-2*m.bit_count()/12)) for m in range(N)])]
 fields=[[(kernel[m^q]+kernel[m^q^MASK])/2 for m in range(N)] for q in P]
 fields=[[x/s for x in f] for f in fields for s in [sum(f)]]
 h=[entropy(f) for f in fields];mean_h=sum(h)/24
 js=[entropy([(a+b)/2 for a,b in zip(fields[i],fields[j])])-(h[i]+h[j])/2 for i,j in combinations(range(24),2)]
 mix=[sum(col)/24 for col in zip(*fields)];I=entropy(mix)-mean_h
 ppr.append({'alpha':alpha,'C':1-sum(js)/len(js),'I_bits':I,'single_sample_accuracy':sum(map(max,zip(*fields)))/24})
assert ppr[-1]['C']>.999 and ppr[-1]['I_bits']<.002
print(json.dumps({'rows':ROWS,'Q48':Q,'observations':counts,'fixed_coordinate':coord,'fixed_relative_6':rel6,'adaptive_sign_tree':T,'adaptive_pair_tree':R,'ppr':ppr},ensure_ascii=False,indent=2))
