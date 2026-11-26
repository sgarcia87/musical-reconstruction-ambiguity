from collections import defaultdict, Counter
from itertools import product, combinations
from functools import lru_cache
from math import log2,ceil
import json,statistics,time

def signature(w,k):
    return w[:k-1],w[len(w)-k+1:],tuple(sorted(Counter(w[i:i+k] for i in range(len(w)-k+1)).items()))
def fibers(n,k):
    d=defaultdict(list)
    for w in map(''.join,product('01',repeat=n)):d[signature(w,k)].append(w)
    return list(d.values())

def optimize(words, relational=False, fixed=True):
    N=len(words); full=(1<<N)-1;n=len(words[0]); masks={}
    for j in range(n):
        mask=sum((w[j]=='1')<<i for i,w in enumerate(words))
        if mask not in (0,full): masks.setdefault(min(mask,full^mask),f'x{j+1}')
    if relational:
        for j,l in combinations(range(n),2):
            mask=sum((w[j]!=w[l])<<i for i,w in enumerate(words))
            if mask not in (0,full):masks.setdefault(min(mask,full^mask),f'x{j+1} XOR x{l+1}')
    qs=list(masks); Q=len(qs)
    def splits(s):
        seen=set()
        for q in qs:
            a=s&q;b=s^a
            if a and b:
                a,b=sorted((a,b))
                if a not in seen:seen.add(a);yield a,b,q
    @lru_cache(None)
    def opt(s):
        z=s.bit_count()
        if z<=1:return 0,0
        av=10**9;worst=10**9
        for a,b,q in splits(s):
            x,y=opt(a),opt(b)
            av=min(av,z+x[0]+y[0]);worst=min(worst,1+max(x[1],y[1]))
        return av,worst
    @lru_cache(None)
    def greedy(s):
        z=s.bit_count()
        if z<=1:return 0,0
        a,b,q=min(splits(s),key=lambda x:abs(x[0].bit_count()-x[1].bit_count()))
        x,y=greedy(a),greedy(b)
        return z+x[0]+y[0],1+max(x[1],y[1])
    @lru_cache(None)
    def look(s):
        z=s.bit_count()
        if z<=1:return 0,0
        a,b,q=min(splits(s),key=lambda x:greedy(x[0])[0]+greedy(x[1])[0])
        x,y=look(a),look(b)
        return z+x[0]+y[0],1+max(x[1],y[1])
    # expected cost of choosing uniformly among currently informative binary partitions
    @lru_cache(None)
    def rnd(s):
        z=s.bit_count()
        if z<=1:return 0.
        v=[rnd(a)+rnd(b) for a,b,q in splits(s)]
        return z+sum(v)/len(v)
    a,w=opt(full);g,gw=greedy(full);l,lw=look(full)
    result=dict(N=N,Q=Q,optimal=a/N,worst=w,greedy=g/N,greedyWorst=gw,rollout=l/N,rolloutWorst=lw,random=rnd(full)/N,bound=log2(N),integerBound=(ceil(log2(N))+1-2**ceil(log2(N))/N),states=opt.cache_info().currsize)
    if fixed:
        @lru_cache(None)
        def partition(t):
            if not t:return (full,)
            bit=t&-t;q=qs[bit.bit_length()-1];return tuple(a for s in partition(t^bit) for a in (s&q,s&~q) if a)
        @lru_cache(None)
        def fixedopt(t):
            p=partition(t);unresolved=sum(s.bit_count() for s in p if s.bit_count()>1)
            if not unresolved:return 0,0
            a=w=10**9
            for j in range(Q):
                if t>>j&1:continue
                if not any((s&qs[j]) and (s&~qs[j]) for s in p):continue
                x,y=fixedopt(t|1<<j);a=min(a,unresolved+x);w=min(w,1+y)
            return a,w
        v,u=fixedopt(0);result.update(fixed=v/N,fixedWorst=u)
    return result

def run():
    out=[]
    for n,k in [(8,2),(8,3),(10,2),(10,3),(12,2),(12,3)]:
        fs=fibers(n,k);sel=[w for w in fs if 2<=len(w)<=32]
        rows=[]
        for words in sel:
            a=optimize(words); b=optimize(words,True,False)
            rows.append(dict(words=words,position=a,relation=b))
        s=dict(n=n,k=k,allFibers=len(fs),ambiguous=sum(len(w)>1 for w in fs),excluded=sum(len(w)>32 for w in fs),rows=rows);out.append(s)
        def avg(key,model):return statistics.mean(r[model][key] for r in rows)
        print(n,k,len(rows),s['excluded'],{key:round(avg(key,'position'),4) for key in ['optimal','worst','greedy','rollout','random','fixed','fixedWorst','bound','integerBound']},'relation',round(avg('optimal','relation'),4),flush=True)
    return out
if __name__=='__main__':
    out=run();json.dump(out,open(__import__('pathlib').Path(__file__).resolve().parent/'results.json','w'),indent=2)
