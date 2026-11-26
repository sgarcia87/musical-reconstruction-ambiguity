from adaptive import *
rng=random.Random(847);checks=0
for k in (2,3):
    fibers=defaultdict(list)
    for w in map(''.join,product('01',repeat=10)):fibers[fiberkey(w,k)].append(w)
    for ws in fibers.values():
        if len(ws)<2:continue
        w=rng.choice(ws);obs=[];v=ws
        for step in range(3):
            e=Engine(w,k,obs);m=e.local_marginals();assert m==explicit(v,list(m));checks+=len(m);e.close()
            if len(v)==1:break
            q=select(m,len(v));b=bit(w,q);obs.append((q,b));v=[s for s in v if bit(s,q)==b]
print(checks)
