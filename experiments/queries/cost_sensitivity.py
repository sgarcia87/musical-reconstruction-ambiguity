from functools import lru_cache
from itertools import combinations
from pathlib import Path
from statistics import mean
import json
ROOT=Path(__file__).resolve().parent

def weighted(words, costs=(4,5,6,8)):
    N=len(words); n=len(words[0]); full=(1<<N)-1; masks={}
    cols=[sum((w[j]=='1')<<i for i,w in enumerate(words)) for j in range(n)]
    for mask in cols:
        if mask not in (0,full):masks[min(mask,full^mask)]=4
    for a,b in combinations(cols,2):
        mask=a^b
        if mask not in (0,full):masks.setdefault(min(mask,full^mask),0)
    @lru_cache(None)
    def opt(s):
        z=s.bit_count()
        if z<=1:return (0,)*len(costs)
        choices={}
        for q,c in masks.items():
            a=s&q;b=s^a
            if a and b:
                a,b=sorted((a,b));choices[a,b]=max(c,choices.get((a,b),0))
        best=[10**12]*len(costs)
        for (a,b),c in choices.items():
            x,y=opt(a),opt(b)
            for j,d in enumerate(costs):best[j]=min(best[j],z*(c or d)+x[j]+y[j])
        return tuple(best)
    return [v/(4*N) for v in opt(full)]

if __name__=='__main__':
    rows=[r for g in json.loads((ROOT/'results.json').read_text()) for r in g['rows']]
    w=[]
    for r in rows:
        v=weighted(r['words']);assert abs(v[0]-r['relation']['optimal'])<1e-9;assert abs(v[-1]-r['position']['optimal'])<1e-9;w.append(v)
    base=[r['position']['optimal'] for r in rows]
    out={'costs':[1,1.25,1.5,2],'mean':[mean(v[j] for v in w) for j in range(4)],'improved':[sum(v[j]<b-1e-9 for b,v in zip(base,w)) for j in range(4)],'baseline':mean(base),'rows':w}
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2));(ROOT/'costs.json').write_text(json.dumps(out,indent=2))
