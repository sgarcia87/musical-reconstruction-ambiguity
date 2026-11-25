#!/usr/bin/env python3
"""RGO XII: internal graph-consistency pilot, NOT semantic ground-truth evaluation.
Run with compact snapshot (included) or original red_fractal_sample.json.
No dependencies beyond Python 3.10+. Candidate priors deliberately use reference
labels to create matched stress-test cases; prediction/validation do not.
"""
import argparse, collections, hashlib, json, math, itertools
from pathlib import Path

def load(path):
    raw=Path(path).read_bytes(); g=json.loads(raw)
    if 'names' in g: return g
    names=[n['id'] for n in g['nodes']]; ix={s:i for i,s in enumerate(names)}
    types=['equilibrio','relacion_fuerte','dualidad','sintesis']
    edges=[[ix[e['source']],ix[e['target']],e.get('weight',1),types.index(e['tipo'])] for e in g['links'] if e.get('tipo') in types]
    cases=[[ix[v['entre'][0]],ix[v['entre'][1]],ix[n['id']],int(not ax.startswith('eje:descubierta:'))] for n in g['nodes'] for ax,v in n.get('roles',{}).items() if v.get('rol')=='equilibrio' and len(v.get('entre',[]))==2 and all(x in ix for x in v['entre']) and n['id'] not in v['entre']]
    return dict(names=names,edges=edges,cases=cases,sha=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest())

def ppr(n,edges,src,alpha=.85):
    out=[[] for _ in range(n)]
    for a,b,w,_ in edges:out[a].append((b,max(.05,min(5,w))))
    sums=[sum(w for _,w in x) for x in out]; p=[float(i==src) for i in range(n)]
    for _ in range(1000):
        z=[0.]*n;z[src]=1-alpha
        for i,p_i in enumerate(p):
            if sums[i]==0:z[src]+=alpha*p_i
            else:
                for j,w in out[i]:z[j]+=alpha*p_i*w/sums[i]
        if sum(abs(a-b) for a,b in zip(z,p))<1e-12:return z
        p=z
    raise RuntimeError('PPR convergence')

def js(a,b):
    def term(p,q):return p*math.log2(2*p/(p+q)) if p>0 else 0
    return .5*sum(term(x,y)+term(y,x) for x,y in zip(a,b))

def run(g):
    names=g['names'];N=len(names);edges=[tuple(e) for e in g['edges']];rows=[];truth=[]
    for a,b,t,manual in g['cases']:
        eligible=[i for i in range(N) if i not in (a,b)]; E=set(eligible)
        # Reserve ALL equilibrium edges from candidate nodes INTO either pole.
        held=[e for e in edges if e[3]==0 and e[0] in E and e[1] in (a,b)]
        train=[e for e in edges if e not in held]
        pa,pb=ppr(N,train,a),ppr(N,train,b)
        s={i:pa[i]+pb[i]-.6*abs(pa[i]-pb[i]) for i in eligible}
        balance={i:abs(pa[i]-pb[i])/(pa[i]+pb[i]) if pa[i]+pb[i]>0 else 1 for i in eligible}
        rank=sorted(eligible,key=lambda i:(-s[i],i))
        wrong=[i for i in rank if i!=t][:5];right=sorted([t]+wrong[:4],key=lambda i:(-s[i],i))
        # For simple baselines use an explicit tie-break by original node order.
        methods={'diffraction':s,'PPR_sum':{i:pa[i]+pb[i] for i in eligible},'PPR_min':{i:min(pa[i],pb[i]) for i in eligible},'direct_out_weight':{i:sum(e[2] for e in train if e[0] in (a,b) and e[1]==i) for i in eligible},'degree':{i:sum(e[0]==i or e[1]==i for e in train) for i in eligible}}
        base={k:min(eligible,key=lambda i:(-v[i],i))==t for k,v in methods.items()}
        # Stricter prediction split: ALSO reserve all equilibrium edges OUT of
        # either pole toward every candidate. Other edge types remain available.
        train2=[e for e in train if not(e[3]==0 and e[0] in (a,b) and e[1] in E)]
        qa,qb=ppr(N,train2,a),ppr(N,train2,b)
        methods2={'diffraction':{i:qa[i]+qb[i]-.6*abs(qa[i]-qb[i]) for i in eligible},'PPR_sum':{i:qa[i]+qb[i] for i in eligible},'PPR_min':{i:min(qa[i],qb[i]) for i in eligible},'direct_out_weight':{i:sum(e[2] for e in train2 if e[0] in (a,b) and e[1]==i) for i in eligible},'degree':{i:sum(e[0]==i or e[1]==i for e in train2) for i in eligible}}
        base2={k:min(eligible,key=lambda i:(-v[i],i))==t for k,v in methods2.items()}
        valedges={(e[0],e[1]) for e in held}
        def strong(es):return [i for i in eligible if (i,a) in es and (i,b) in es]
        valid=strong(valedges)
        def assess(P):
            top=P[0];ratio=s[top]/s[P[1]] if s[P[1]]>0 else None
            # Distinguish an unsupported prior from a ranking disagreement.
            status='inconclusive' if len(valid)!=1 else 'prior_rejected' if valid[0] not in P else 'corroborated' if valid[0]==top else 'ranking_disagreement'
            return dict(candidates=[names[i] for i in P],winner=names[top],correct=top==t,ratio=ratio,balance=balance[top],stable=(s[top]>0 and (ratio is None or ratio>=1.35) and balance[top]<=.8),mass=sum(s[i] for i in P)/sum(s.values()) if sum(s.values()) else 0,decision=status)
        rows.append(dict(poles=[names[a],names[b]],reference=names[t],nonautomatic=bool(manual),rank=rank.index(t)+1,baseline=base,strict_baseline=base2,validation_candidates=[names[i] for i in valid],held_edges=len(held),pole_similarity=1-js(pa,pb),valid_prior=assess(right),wrong_prior=assess(wrong)))
        truth.append((a,b,t,eligible,right,wrong,valedges))
    def aggregate(rr):
        return dict(n=len(rr),rank_accuracy={k:sum(r['baseline'][k] for r in rr) for k in rr[0]['baseline']},strict_rank_accuracy={k:sum(r['strict_baseline'][k] for r in rr) for k in rr[0]['strict_baseline']},wrong_stable=sum(r['wrong_prior']['stable'] for r in rr),valid_stable=sum(r['valid_prior']['stable'] for r in rr),valid_stable_wrong=sum(r['valid_prior']['stable'] and not r['valid_prior']['correct'] for r in rr),wrong_stable_rejected=sum(r['wrong_prior']['stable'] and r['wrong_prior']['decision']=='prior_rejected' for r in rr),valid_prior_status=dict(collections.Counter(r['valid_prior']['decision'] for r in rr)),wrong_prior_status=dict(collections.Counter(r['wrong_prior']['decision'] for r in rr)),unique_validator_correct=sum(r['validation_candidates']==[r['reference']] for r in rr))
    # In the independent-deletion model each held-out edge is kept with 1-p.
    # Exact expectation (not Monte Carlo): complete support for a candidate
    # requires two distinct retained edges; events disjoint across candidates.
    noise=[]
    for p in (0,.1,.25,.5,.75):
        q=(1-p)**2;acc=collections.Counter()
        for a,b,t,elig,right,wrong,es in truth:
            full=[i for i in elig if (i,a) in es and (i,b) in es]
            k=len(full);unique_each=q*(1-q)**(k-1) if k else 0
            acc['inconclusive']+=1-k*unique_each
            acc['unique_correct']+=unique_each*(t in full)
            acc['unique_incorrect']+=unique_each*(k-(t in full))
            acc['wrong_prior_rejected']+=unique_each*sum(i not in wrong for i in full)
            acc['valid_prior_false_alarm']+=unique_each*sum(i not in right for i in full)
        noise.append(dict(deletion_probability=p,**{k:v/len(truth) for k,v in acc.items()}))
    # Actual changes of seed pairs for a common annotated target.
    groups=collections.defaultdict(list)
    for a,b,t,_ in g['cases']: groups[t].append((a,b))
    group_rows=[]
    for t,ps in groups.items():
        if len(ps)<2:continue
        poles={v for p in ps for v in p};elig=[i for i in range(N) if i not in poles]
        assert t in elig
        held=[e for e in edges if e[3]==0 and e[0] in elig and e[1] in poles]
        train=[e for e in edges if e not in held];scores=[];fields=[]
        for a,b in ps:
            pa,pb=ppr(N,train,a),ppr(N,train,b)
            scores.append({i:pa[i]+pb[i]-.6*abs(pa[i]-pb[i]) for i in elig})
            fields.append([(x+y)/2 for x,y in zip(pa,pb)])
        order=sorted(elig,key=lambda i:(-sum(s[i] for s in scores),i))
        wrong=[i for i in order if i!=t][:5];right=[t]+wrong[:4]
        def winners(P):return [max(P,key=lambda i:(s[i],-i)) for s in scores]
        C=1-sum(js(a,b) for a,b in itertools.combinations(fields,2))/(len(ps)*(len(ps)-1)/2)
        vs={i:sum(any(e[0]==i and e[1]==a for e in held) and any(e[0]==i and e[1]==b for e in held) for a,b in ps) for i in elig}
        best=max(vs.values());val=[i for i,v in vs.items() if v==best and best>0]
        group_rows.append(dict(reference=names[t],perspectives=[[names[a],names[b]] for a,b in ps],coherence=C,valid_prior=[names[i] for i in right],wrong_prior=[names[i] for i in wrong],valid_winners=[names[i] for i in winners(right)],wrong_winners=[names[i] for i in winners(wrong)],validation_best=[names[i] for i in val],validation_pairs=best))
    # Shared-bias counterexample: replace two held-out equilibrium links for
    # tibio by two links for temperatura. First-view graph stays unchanged.
    e=next(r for r in rows if set(r['poles'])=={'calor','frío'})
    a,b,t,eligible,right,wrong,es=next(z for z in truth if set([names[z[0]],names[z[1]]])=={'calor','frío'})
    decoy=names.index('temperatura'); altered=(es-{(t,a),(t,b)})|{(decoy,a),(decoy,b)}
    val=[i for i in eligible if (i,a) in altered and (i,b) in altered]
    assert val==[decoy] and names[decoy]==e['wrong_prior']['winner'] and decoy in wrong
    shared=dict(poles=e['poles'],reference=e['reference'],wrong_winner=e['wrong_prior']['winner'],before=e['wrong_prior']['decision'],after='corroborated',altered_validation_candidates=[names[i] for i in val],perturbation='remove both held-out tibio-to-poles equilibrium edges; add both temperatura-to-poles edges',evidence_is_simulated=True)
    return dict(source=g.get('source'),source_git_blob_sha=g['sha'],nodes=N,structural_edges=len(edges),all=aggregate(rows),nonautomatic=aggregate([r for r in rows if r['nonautomatic']]),automatically_discovered=aggregate([r for r in rows if not r['nonautomatic']]),deletion_model=noise,shared_bias_example=shared,perspective_groups=group_rows,rows=rows)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('graph',nargs='?',default=str(Path(__file__).with_name('rgo_fase12_graph.json')));args=p.parse_args();print(json.dumps(run(load(args.graph)),ensure_ascii=False,indent=2,allow_nan=False))
