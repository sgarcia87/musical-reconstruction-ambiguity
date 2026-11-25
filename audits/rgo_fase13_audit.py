#!/usr/bin/env python3
"""RGO XIII: exploratory external scalar betweenness benchmark.
Python >=3.10; pip install numpy scipy. Download inputs or place the original
8 Cue_Target_Pairs.*.html files and ordering_gold_standard.csv in --data.
USF associations are separate from Wilkinson/Oates scalar judgments.
No IA_m graph, ordering labels in propagation, or tuning. Membership is used
only in the explicitly labelled candidate restrictions and ablation.
"""
import argparse, json, hashlib, itertools, urllib.request
from pathlib import Path
from collections import defaultdict
import numpy as np
from scipy.sparse import coo_matrix, diags

PARTS=['A-B','C','D-F','G-K','L-O','P-R','S','T-Z']
BASE='https://raw.githubusercontent.com/teonbrooks/free_association/master/src/'
GOLD='https://raw.githubusercontent.com/Coral-Lab/scales/master/ordering/ordering_gold_standard.csv'
METHODS=['diffraction','min','sum','reverse','direct','cos','degree','random']
EPS=1e-12

def load(root):
    root.mkdir(parents=True,exist_ok=True)
    def read(name,url):
        p=root/name
        if not p.exists():
            with urllib.request.urlopen(url,timeout=60) as f:p.write_bytes(f.read())
        b=p.read_bytes()
        hashes[name]=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
        return b.decode('utf-8',errors='replace')
    hashes={}; edges=defaultdict(float); cues=set(); counts={}
    for part in PARTS:
        name=f'Cue_Target_Pairs.{part}.html'; counts[part]=0
        for line in read(name,BASE+name).splitlines():
            v=[x.strip() for x in line.split(',')]
            if len(v)<30 or v[2] not in ('YES','NO'):continue
            try:w=float(v[5])
            except ValueError:continue
            if not np.isfinite(w) or w<=0:continue
            a,b=v[0].lower(),v[1].lower()
            if not a or not b:continue
            edges[a,b]+=w;cues.add(a);counts[part]+=1
    groups=defaultdict(list)
    for line in read('ordering_gold_standard.csv',GOLD).strip().splitlines():
        w,g,v=line.split(',');groups[g].append((float(v),w))
    groups={g:[w for _,w in sorted(v)] for g,v in groups.items()}
    return edges,cues,groups,hashes,counts

def run(edges,cues,groups):
    names=sorted(set(itertools.chain.from_iterable(edges))); ix={w:i for i,w in enumerate(names)}; n=len(names)
    groupof={w:g for g,ls in groups.items() for w in ls}
    pool=[ix[w] for w in groupof if w in ix]; cueids={ix[w] for w in cues if w in ix}
    e=list(edges.items()); keep=[((a,b),w) for (a,b),w in e if not(a in groupof and groupof[a]==groupof.get(b))]
    out={'graph':{'nodes':n,'edges':len(e),'cues':len(cues),'removed':len(e)-len(keep),'missing':[w for w in groupof if w not in ix],'noncue':[w for w in groupof if w not in cues]}}
    def matrices(es):
        a,b,w=zip(*[(ix[a],ix[b],w) for (a,b),w in es])
        return coo_matrix((w,(a,b)),shape=(n,n)).tocsr()
    def pprs(mat):
        sums=np.asarray(mat.sum(axis=1)).ravel(); dangling=sums==0
        tr=(diags(np.divide(1,sums,out=np.zeros_like(sums),where=~dangling))@mat).T.tocsr()
        result={}
        for src in pool:
            p=np.zeros(n);p[src]=1
            for it in range(250):
                q=.85*(tr@p);q[src]+=.15+.85*p[dangling].sum()
                err=np.abs(q-p).sum();p=q
                if err<1e-11:break
            result[src]=p
        return result
    def top(scores,cand,valid):
        s=scores[cand]; winners=cand[np.abs(s-s.max())<EPS]
        return float(np.mean(np.isin(winners,valid))),winners
    def auc(scores,valid,neg):
        d=scores[valid,None]-scores[neg][None,:]
        return float(np.mean(np.where(np.abs(d)<EPS,.5,d>0)))
    for key,ee in [('intact',e),('masked',keep)]:
        M=matrices(ee); p=pprs(M); q=pprs(M.T.tocsr()); deg=np.asarray(M.sum(axis=0)).ravel()
        norms=np.sqrt(np.asarray(M.multiply(M).sum(axis=1)).ravel()); rows={'within':[],'pool':[]}; select=defaultdict(int); examples=[]
        for group,ls in groups.items():
            a=[ix[w] for w in ls if w in ix]
            for i in range(len(a)):
                for j in range(i+2,len(a)):
                    x,y=a[i],a[j]
                    if x not in cueids or y not in cueids:continue
                    good=np.array(a[i+1:j],dtype=int); gset=set(good)
                    u,v=p[x],p[y]; ru,rv=q[x],q[y]; mid=M.getrow(x)+M.getrow(y)
                    dots=(M@mid.T).toarray().ravel(); den=norms*np.sqrt(mid.multiply(mid).sum()); cos=np.divide(dots,den,out=np.zeros_like(dots),where=den>0)
                    sc={'diffraction':u+v-.6*np.abs(u-v),'min':np.minimum(u,v),'sum':u+v,'reverse':ru+rv-.6*np.abs(ru-rv),'direct':mid.toarray().ravel(),'cos':cos,'degree':deg}
                    for scenario,cc in [('within',a),('pool',pool)]:
                        cand=np.array([c for c in cc if c not in (x,y)],dtype=int);neg=np.array([c for c in cand if c not in gset],dtype=int)
                        if not len(neg):continue
                        row={'group':group,'a':names[x],'b':names[y],'valid':[names[t] for t in good],'methods':{}}
                        for method,s in sc.items():
                            t,win=top(s,cand,good);row['methods'][method]={'top':t,'auc':auc(s,good,neg),'winner':[names[w] for w in win]}
                        row['methods']['random']={'top':len(good)/len(cand),'auc':.5};rows[scenario].append(row)
                        if scenario!='pool':continue
                        fwd=sorted(cand,key=lambda c:(-sc['diffraction'][c],c));rev=sorted(cand,key=lambda c:(-sc['reverse'][c],c));f,r=fwd[0],rev[0];fc,rc=f in gset,r in gset
                        select['n']+=1;select['agree']+=int(f==r);select['agreeCorrect']+=int(f==r and fc);select['bothWrong']+=int(not fc and not rc)
                        def stable(seq):
                            c,d=seq[:2];s=sc['diffraction'];return s[c]>0 and s[c]>=1.35*s[d] and abs(u[c]-v[c])/(u[c]+v[c] or 1)<=.8
                        if stable(fwd):select['stable']+=1;select['stableCorrect']+=int(fc)
                        wrong=[c for c in fwd if c not in gset]
                        if len(wrong)>=2:select['wrongPriorN']+=1;select['wrongPriorStable']+=int(stable(wrong))
                        allcand=np.array([c for c in range(n) if c not in (x,y)])
                        for m in ('diffraction','min','reverse'):select['full_'+m]+=top(sc[m],allcand,good)[0]
                        if f==r and not fc:examples.append([names[x],names[y],[names[c] for c in good],names[f]])
        summary={}
        for scenario,rr in rows.items():
            by=defaultdict(list)
            for row in rr:by[row['group']].append(row)
            summary[scenario]={'n':len(rr),'methods':{m:{k:float(np.mean([row['methods'][m][k] for row in rr])) for k in ('top','auc')}|{'macro_'+k:float(np.mean([np.mean([row['methods'][m][k] for row in v]) for v in by.values()])) for k in ('top','auc')} for m in METHODS},'queries':rr}
        out[key]=summary|{'perspective_and_prior':dict(select),'agreement_errors':examples}
    return out

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--data',type=Path,default=Path('rgo13_data'));args=parser.parse_args()
    edges,cues,groups,hashes,counts=load(args.data);out=run(edges,cues,groups);out['hashes']=hashes;out['source_counts']=counts;print(json.dumps(out,ensure_ascii=False,indent=2))
