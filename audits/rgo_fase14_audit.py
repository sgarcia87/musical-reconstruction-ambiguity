#!/usr/bin/env python3
"""RGO XIV — semantic direction and profile geometry.
Requires numpy scipy. Original USF tables and Wilkinson/Oates CSV are downloaded
on demand or read from --data. Gold membership only defines evaluation pools and
an explicitly label-informed stress-test ablation. Gold rank defines endpoints
and test outcomes, never feature weights. No fitted hyperparameters.
"""
import argparse, json, hashlib, itertools, urllib.request
from pathlib import Path
from collections import defaultdict
import numpy as np
from scipy.sparse import coo_matrix, diags

PARTS=['A-B','C','D-F','G-K','L-O','P-R','S','T-Z']
BASE='https://raw.githubusercontent.com/teonbrooks/free_association/master/src/'
GOLD='https://raw.githubusercontent.com/Coral-Lab/scales/master/ordering/ordering_gold_standard.csv'
EPS=1e-12

def load(root):
    root.mkdir(parents=True,exist_ok=True); hashes={}; edges=defaultdict(float); cues=set(); counts={}
    def read(name,url):
        p=root/name
        if not p.exists():
            with urllib.request.urlopen(url,timeout=60) as f:p.write_bytes(f.read())
        b=p.read_bytes(); hashes[name]=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
        return b.decode('utf-8',errors='replace')
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
        w,g,v=line.split(',');groups[g].append((float(v),w.strip()))
    return edges,cues,{g:[w for _,w in sorted(v)] for g,v in groups.items()},hashes,counts

def geometry(ab,ax,bx):
    # All feature vectors used for geometry are nonzero and L2-normalized.
    d=np.maximum(2-2*ab,EPS);t=.5+(bx-ax)/d
    residual=np.maximum(0,2-2*ax-t*t*d)
    seg=-(residual+d*(t-np.clip(t,0,1))**2)
    return t,seg,ax+bx

def pprs(mat,srcs):
    sums=np.asarray(mat.sum(axis=1)).ravel(); dangling=sums==0
    tr=(diags(np.divide(1,sums,out=np.zeros_like(sums),where=~dangling))@mat).T.tocsr()
    result={}
    for src in srcs:
        p=np.zeros(mat.shape[0]);p[src]=1
        for it in range(300):
            q=.85*(tr@p);q[src]+=.15+.85*p[dangling].sum()
            err=np.abs(q-p).sum();p=q
            if err<1e-11:break
        result[src]=p
    return result

def normalize(mat):
    norms=np.sqrt(np.asarray(mat.multiply(mat).sum(axis=1)).ravel())
    return (diags(np.divide(1,norms,out=np.zeros_like(norms),where=norms>0))@mat).tocsr(),norms>0

def dense_normalized(p):
    return {i:v/(np.linalg.norm(v) or 1) for i,v in p.items()}

def evaluate(scores,cand,good):
    cand=np.asarray(cand,int);good=np.asarray(good,int)
    s=scores[cand];hits=np.isin(cand,good);pos=s[hits];neg=s[~hits]
    best=s.max();ties=np.abs(s-best)<EPS
    dif=pos[:,None]-neg[None,:]
    return dict(top=float(hits[ties].mean()),auc=float(np.mean(np.where(np.abs(dif)<EPS,.5,dif>0))),bestRank=int(min(1+np.sum(s>x+EPS) for x in pos)),winner=cand[ties].tolist())

def summary(rows):
    if not rows:return {'n':0,'summary':{}}
    by=defaultdict(list)
    for r in rows:by[r['g']].append(r)
    methods=rows[0]['methods']; out={}
    for m in methods:
        out[m]={k:float(np.mean([r['methods'][m][k] for r in rows])) for k in ('top','auc')}
        out[m].update({'macroTop':float(np.mean([np.mean([r['methods'][m]['top'] for r in rs]) for rs in by.values()])), 'macroAUC':float(np.mean([np.mean([r['methods'][m]['auc'] for r in rs]) for rs in by.values()])), 'top5Optimistic':sum(r['methods'][m].get('bestRank',100000)<=5 for r in rows)})
    return dict(n=len(rows),summary=out,queries=rows)

def order_stat(values):
    signs=np.array(values);return float(np.sum(signs>EPS)+.5*np.sum(np.abs(signs)<EPS)),int(len(signs)),int(np.sum(np.abs(signs)<EPS))

def run(edges,cues,groups):
    names=sorted(set(itertools.chain.from_iterable(edges))); ix={w:i for i,w in enumerate(names)};N=len(names)
    groupof={w:g for g,ls in groups.items() for w in ls};pool=[ix[w] for w in groupof if w in ix and w in cues]
    scales={g:[ix[w] for w in ls if w in ix and w in cues] for g,ls in groups.items()}
    e=list(edges.items());keep=[((a,b),w) for (a,b),w in e if not(a in groupof and groupof[a]==groupof.get(b))]
    result={'graph':dict(nodes=N,edges=len(e),removed=len(e)-len(keep),pool=len(pool)), 'conditions':{}}
    for condition,ee in [('intact',e),('masked',keep)]:
        a,b,w=zip(*[(ix[a],ix[b],w) for (a,b),w in ee]);M=coo_matrix((w,(a,b)),shape=(N,N)).tocsr()
        F,hasF=normalize(M);R,hasR=normalize(M.T.tocsr());assert all(hasF[pool]) and all(hasR[pool]),'Reference terms without nonzero profile: explicitly revise eligibility before use.'
        sf={i:(F@F.getrow(i).T).toarray().ravel() for i in pool};sr={i:(R@R.getrow(i).T).toarray().ravel() for i in pool}
        p=pprs(M,pool);q=pprs(M.T.tocsr(),pool);pf=dense_normalized(p);pr=dense_normalized(q)
        sm={};smr={}
        for i in pool:
            sm[i]=np.zeros(N);smr[i]=np.zeros(N)
            for j in pool:sm[i][j]=np.dot(pf[i],pf[j]);smr[i][j]=np.dot(pr[i],pr[j])
        axis_methods=['contrast','contrastReverse','pprProj','reverseProj','assocProj','assocRevProj'];axis_rows=[]
        for g,ls in scales.items():
            if len(ls)<3:continue
            a,b=ls[0],ls[-1];inner=np.array(ls[1:-1],int)
            vals={'contrast':np.divide(p[b]-p[a],p[b]+p[a],out=np.zeros(N),where=p[b]+p[a]>0),'contrastReverse':np.divide(q[b]-q[a],q[b]+q[a],out=np.zeros(N),where=q[b]+q[a]>0)}
            for key,S in [('pprProj',sm),('reverseProj',smr),('assocProj',sf),('assocRevProj',sr)]:vals[key]=geometry(S[a][b],S[a],S[b])[0]
            v={}
            for m in axis_methods:
                dif=[vals[m][y]-vals[m][x] for x,y in itertools.combinations(inner,2)];ok,n,ties=order_stat(dif)
                v[m]=dict(ok=ok,n=n,acc=ok/n if n else None,coords=vals[m][inner].tolist())
            axis_rows.append(dict(g=g,anchors=[names[a],names[b]],inner=[names[i] for i in inner],scores=v))
        axis_summary={}
        for m in axis_methods:
            rows=[r['scores'][m] for r in axis_rows if r['scores'][m]['n']];n=sum(r['n'] for r in rows)
            axis_summary[m]=dict(pairs=n,pairAcc=sum(r['ok'] for r in rows)/n if n else None,macro=float(np.mean([r['acc'] for r in rows])) if n else None,scales=len(rows))
        # Local anchors: every a < b with at least one intervening cue.
        scopes={'within':[],'pool':[],'fullJoint':[],'fullIncoming':[]};joint=np.flatnonzero(hasF&hasR).tolist();inc=np.flatnonzero(hasR).tolist()
        order={'out':defaultdict(list),'in':defaultdict(list)}
        for g,ls in scales.items():
            for i,j in itertools.combinations(range(len(ls)),2):
                if j-i<2:continue
                a,b=ls[i],ls[j];good=ls[i+1:j];x,y=p[a],p[b];d=x+y
                t,sg,mid=geometry(sm[a][b],sm[a],sm[b]);rt,rs,rm=geometry(smr[a][b],smr[a],smr[b]);ot,os,om=geometry(sf[a][b],sf[a],sf[b]);it,ins,inm=geometry(sr[a][b],sr[a],sr[b]);
                local={'diffraction':d-.6*np.abs(x-y),'min':np.minimum(x,y),'sum':d,'contrastMid':-np.abs(x-y)/np.where(d>0,d,1e-30),'pprMid':mid,'pprSegment':sg,'pprOrderOnly':np.minimum(t,1-t),'reverseSegment':rs,'assocSegment':os,'assocRevSegment':ins}
                direct={'inMid':inm,'inSeg':ins,'outMid':om,'outSeg':os,'inMin':np.minimum(sr[a],sr[b])}
                for scope,cc in [('within',ls),('pool',pool),('fullJoint',joint),('fullIncoming',inc)]:
                    cand=[c for c in cc if c not in (a,b)]
                    if not any(c in good for c in cand) or all(c in good for c in cand):continue
                    ss=local|direct if scope in ('within','pool') else (direct if scope=='fullJoint' else {k:direct[k] for k in ('inMid','inSeg','inMin')})
                    rr={m:evaluate(v,cand,good) for m,v in ss.items()};rr['random']={'top':sum(c in good for c in cand)/len(cand),'auc':.5}
                    for r in rr.values():
                        if 'winner'in r:r['winner']=[names[c] for c in r['winner'][:5]]
                    scopes[scope].append(dict(g=g,a=names[a],b=names[b],valid=[names[c] for c in good],methods=rr))
                for X,Y in itertools.combinations(good,2):
                    for m,S in [('out',sf),('in',sr)]:
                        delta=(S[b][Y]-S[a][Y])-(S[b][X]-S[a][X]);order[m][g,X,Y].append(delta)
        order_summary={}
        for m,r in order.items():
            allvals=[z for v in r.values() for z in v];ok,n,ties=order_stat(allvals);per=defaultdict(list)
            for (g,x,y),v in r.items():per[g].extend(v)
            varied=[v for v in r.values() if len(v)>=2]
            order_summary[m]=dict(n=n,correct=ok,ties=ties,acc=ok/n if n else None,macro=float(np.mean([order_stat(v)[0]/len(v) for v in per.values()])) if per else None,repeatPairs=len(varied),disagreementPairs=sum(any(x>EPS for x in v) and any(x<-EPS for x in v) for v in varied),consistentWrong=sum(all(x<-EPS for x in v) for v in varied))
        result['conditions'][condition]=dict(axis={'summary':axis_summary,'scales':axis_rows},order=order_summary,scopes={k:summary(v) for k,v in scopes.items()},candidate_counts={'pool':len(pool),'fullJoint':len(joint),'fullIncoming':len(inc)})
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--data',type=Path,default=Path('rgo13_data'));a=ap.parse_args();e,c,g,h,k=load(a.data);out=run(e,c,g);out['source_hashes']=h;out['source_counts']=k;print(json.dumps(out,ensure_ascii=False,indent=2))
