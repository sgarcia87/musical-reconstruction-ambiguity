import json,random
from adaptive import solve
from pathlib import Path
rng=random.Random(20261127);rows=[]
for n,k,rep in [(48,2,6),(64,2,6),(24,3,6)]:
 for i in range(rep):
  w=''.join(rng.choice('01') for _ in range(n))
  for mode in ['positions','local','sample']:
   z=solve(w,k,mode,9876+i);z['case']=i;rows.append(z);print(n,k,i,mode,z['queries'],z['peak'],round(z['seconds'],3),z['failed'],flush=True)
  json.dump(rows,open(Path(__file__).parent/'local_results.json','w'),indent=2)
