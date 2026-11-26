import json,random,math
from audit import evaluate,summary,graph
from pathlib import Path
rng=random.Random(314159);rows=[]
for name,p,stay in [('biased',.85,None),('persistent',.5,.94),('alternating',.5,.08)]:
 for n in (64,128):
  group=[]
  for i in range(12):
   if stay is None:w=''.join('1' if rng.random()<p else '0' for _ in range(n))
   else:
    a=[rng.choice('01')]
    for j in range(n-1):a.append(a[-1] if rng.random()<stay else str(1-int(a[-1])))
    w=''.join(a)
   r=evaluate(w,2,seed=91000+len(rows));m,s,t,d=graph(w,2)
   # independent binary run-count formula: each symbol's loop edges are distributed among its runs.
   runs=[int(s==0)+m[2],int(s==1)+m[1]]
   count=math.prod(math.comb(m[3*b]+runs[b]-1,runs[b]-1) if runs[b] else int(m[3*b]==0) for b in range(2))
   assert count==int(r['N'])
   if count==1:continue
   r.update(kind=name,word=w);rows.append(r);group.append(r)
  if group:print(name,n,summary(group),flush=True)
json.dump(rows,open(Path(__file__).parent/'stress.json','w'),indent=2)
