#!/usr/bin/env python3
"""Q12: prueba exploratoria sobre JSB Chorales (cuadrícula de negras).
Uso: python q12_corpus_audit.py [jsb-chorales-quarter.json]
Si no se indica un archivo, intenta descargarlo. Solo biblioteca estándar.
Fuente: https://github.com/czhuang/JSB-Chorales-dataset
Blob analizado: ff93746647d1f5af2f719d235329c294267f3088
"""
import sys,json,hashlib,urllib.request
from itertools import product
from collections import Counter
URL='https://raw.githubusercontent.com/czhuang/JSB-Chorales-dataset/master/jsb-chorales-quarter.json'
def mask(ns):
    m=0
    for n in ns:m|=1<<(n%12)
    return m
def orbit(ns):return {mask(e*n+t for n in ns) for e in (-1,1) for t in range(12)}
R={'6-Z37':(0,1,2,3,4,8),'6-Z4':(0,1,2,4,5,6),'6-Z48':(0,1,2,5,7,9),'6-Z26':(0,1,3,5,7,8)}
labels={m:k for k,ns in R.items() for m in orbit(ns)}
rows=[[n for c in range(4) for n in range(12) if n%3==r and n%4==c] for r in range(3)]
bal=set(); Q=set()
for m in range(4096):
    v=[[1 if m>>n&1 else -1 for n in row] for row in rows]
    if all(sum(a)==0 for a in v):
        bal.add(m)
        if all(sum(x*y for x,y in zip(v[i],v[j]))==0 for i,j in ((0,1),(0,2),(1,2))):Q.add(m)
assert len(Q)==48 and len(bal)==216 and Q==set(labels)
D={s^(1<<i) for s in orbit((0,2,4,5,7,9,11)) for i in range(12) if s>>i&1}
assert len(D)==72 and len(D&Q)==12
seed=42
def rand():
    global seed
    seed=(1664525*seed+1013904223)%2**32
    return seed/2**32
def audit(data):
    global seed
    seed=42
    result=[]
    for w in (1,2,4,8,16):
        total=six=diat=balanced=hits=pieces6=pieceshits=0
        cls=Counter(); pieces=[]; split={}
        for key,songs in data.items():
            st=Counter();split[key]=st
            for song in songs:
                ms=[mask(ns) for ns in song];c=Counter()
                for i in range(len(ms)-w+1):
                    m=0
                    for j in range(i,i+w):m|=ms[j]
                    total+=1;st['total']+=1
                    if m.bit_count()!=6:continue
                    six+=1;st['six']+=1;c[m]+=1
                    diat+=m in D;balanced+=m in bal
                    if m in Q:hits+=1;st['hits']+=1;cls[labels[m]]+=1
                if c:
                    pieces.append(c);pieces6+=1;pieceshits+=any(m in Q for m in c)
        out=dict(w=w,total=total,six=six,diatonic=diat,balanced=balanced,hits=hits,classes=dict(cls),pieces6=pieces6,pieceshits=pieceshits,split=split)
        if w in (4,8):
            sims=[]
            for _ in range(199):
                h=0
                for c in pieces:
                    p=list(range(12))
                    for i in range(11,0,-1):
                        j=int(rand()*(i+1));p[i],p[j]=p[j],p[i]
                    for m,n in c.items():
                        v=sum(1<<p[i] for i in range(12) if m>>i&1)
                        if v in Q:h+=n
                sims.append(h)
            sims.sort()
            out['null']=dict(reps=len(sims),mean=sum(sims)/len(sims),range=[sims[4],sims[194]],p_upper=(1+sum(h>=hits for h in sims))/200)
        result.append(out)
    return result
if __name__=='__main__':
    raw=open(sys.argv[1],'rb').read() if len(sys.argv)>1 else urllib.request.urlopen(URL,timeout=60).read()
    print('Git blob SHA1:',hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest())
    print(json.dumps(audit(json.loads(raw)),indent=2,ensure_ascii=False))
