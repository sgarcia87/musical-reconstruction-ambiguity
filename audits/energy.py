#!/usr/bin/env python3
"""Enumeración Q12 y barreras; --quantum añade diagonalización dispersa (NumPy/SciPy)."""
from collections import Counter, deque
from itertools import combinations
import argparse, json
N=4096; MASK=N-1
ROWS=[[next(n for n in range(12) if n%3==i and n%4==j) for j in range(4)] for i in range(3)]
def evaluate(m):
    a=[[1 if m>>n&1 else -1 for n in r] for r in ROWS]
    b=sum(sum(r)**2 for r in a)
    o=sum(sum(x*y for x,y in zip(r,s))**2 for r,s in combinations(a,2))
    return b,o,b+o
F=list(map(evaluate,range(N))); H=[v[2] for v in F]; Q=[m for m in range(N) if H[m]==0]
assert len(Q)==48
D=[min((m^q).bit_count() for q in Q) for m in range(N)]
def neighbors(m):return [m^(1<<i) for i in range(12)]
mins=[m for m in range(N) if all(H[m]<H[n] for n in neighbors(m))]; traps=[m for m in mins if H[m]>0]
assert len(mins)==240 and len(traps)==192
assert all(F[m]==(12,0,12) and D[m]==3 and min(H[n] for n in neighbors(m))==16 for m in traps)
assert all(H[m]==H[m^MASK] and D[m]==D[m^MASK] for m in range(N))
# Reachability at threshold 16; proves the minimum barrier for all traps.
parent={m:None for m in Q}; queue=deque(Q)
while queue:
    m=queue.popleft()
    for n in neighbors(m):
        if H[n]<=16 and n not in parent:parent[n]=m;queue.append(n)
assert all(m in parent for m in traps)
path=[]; m=traps[0]
while m is not None:path.append({'mask':m,'H':H[m]});m=parent[m]
out=dict(rows=ROWS,energy_histogram=dict(sorted(Counter(H).items())),distance_histogram=dict(sorted(Counter(D).items())),Q48=Q,strict_local_minima=len(mins),non_global_minima=len(traps),trap_barrier=4,example_path=path,cardinality_means=[sum(D[m] for m in range(N) if m.bit_count()==k)/sum(m.bit_count()==k for m in range(N)) for k in range(13)])
p=argparse.ArgumentParser();p.add_argument('--quantum',action='store_true');args=p.parse_args()
if args.quantum:
    import numpy as np
    from scipy.sparse import coo_matrix,diags
    from scipy.sparse.linalg import eigsh
    i=np.repeat(np.arange(N),12);j=(i^(1<<np.tile(np.arange(12),N)))
    adjacency=coo_matrix((np.ones(len(i)),(i,j)),shape=(N,N)).tocsr()
    res=[]
    for gamma in (.5,1,3,6,12):
        mat=diags(H,dtype=float)-gamma*adjacency
        e,v=eigsh(mat,k=1,which='SA',v0=np.ones(N)/np.sqrt(N),tol=1e-10)
        psi=v[:,0];res.append(dict(gamma=gamma,E0=float(e[0]),Q48_probability=float(np.sum(psi[Q]**2)),residual=float(np.linalg.norm(mat@psi-e[0]*psi))))
    out['quantum']=res
print(json.dumps(out,indent=2))
