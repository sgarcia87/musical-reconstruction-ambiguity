#!/usr/bin/env python3
"""Distance-to-Q48 audit on quarter-note grids. Usage: python bach_distance.py [dataset.json].
Replicates the exploratory analysis; no cadence annotations or independent window assumption.
"""
import json,sys,urllib.request,hashlib
from collections import Counter,defaultdict
from itertools import combinations
from bach_hexachords import Q,mask,URL
N=4096
E=[min((m^q).bit_count() for q in Q) for m in range(N)]
scales=[mask([n+t for n in (0,2,4,5,7,9,11)]) for t in range(12)]
K=[m.bit_count() for m in range(N)]
M=[min((m&~s).bit_count() for s in scales) for m in range(N)]
groups=defaultdict(list); by_k=defaultdict(list)
for m in range(N):groups[K[m],M[m]].append(E[m]);by_k[K[m]].append(E[m])
mean=lambda a:sum(a)/len(a)
baseline={k:mean(v) for k,v in by_k.items()}; tonal={k:mean(v) for k,v in groups.items()}
seed=7123
def rand():
    global seed
    seed=(1664525*seed+1013904223)&0xffffffff
    return seed/2**32

def audit(data,reps=199):
    global seed
    seed=7123;out=[]
    for w in (2,4,8):
        pieces=[];total=0;sum_e=0;sum_z=0;sum_t=0
        for split,songs in data.items():
            for s in songs:
                ms=list(map(mask,s));a=[]
                for i in range(len(ms)-w+1):
                    m=0
                    for n in ms[i:i+w]:m|=n
                    a.append(m);total+=1;sum_e+=E[m];sum_z+=E[m]-baseline[K[m]];sum_t+=E[m]-tonal[K[m],M[m]]
                if len(a)<2:continue
                z=[E[m]-baseline[K[m]] for m in a]
                pieces.append((a,z,Counter(a)))
        observed=mean([mean(z) for _,z,_ in pieces]);end=mean([z[-1]-mean(z[:-1]) for _,z,_ in pieces]);sims=[];end_sims=[]
        for _ in range(reps):
            vals=[];ends=[]
            for a,z,c in pieces:
                p=list(range(12))
                for i in range(11,0,-1):
                    j=int(rand()*(i+1));p[i],p[j]=p[j],p[i]
                val=0
                for m,n in c.items():
                    mm=sum(1<<p[i] for i in range(12) if m>>i&1)
                    val+=n*(E[mm]-baseline[K[m]])
                vals.append(val/len(a))
                j=int(rand()*len(z));ends.append(z[j]-(sum(z)-z[j])/(len(z)-1))
            sims.append(mean(vals));end_sims.append(mean(ends))
        out.append(dict(window=w,total=total,pieces=len(pieces),mean_E=sum_e/total,mean_cardinality_control=sum_z/total,mean_diatonic_control=sum_t/total,per_piece_residual=observed,permutation_mean=mean(sims),p_lower=(1+sum(x<=observed for x in sims))/(1+reps),last_vs_rest=end,last_vs_random_p_upper=(1+sum(x>=end for x in end_sims))/(1+reps)))
    return out
if __name__=='__main__':
    raw=open(sys.argv[1],'rb').read() if len(sys.argv)>1 else urllib.request.urlopen(URL,timeout=60).read()
    print('Git blob SHA1:',hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),file=sys.stderr)
    print(json.dumps(audit(json.loads(raw)),indent=2))
