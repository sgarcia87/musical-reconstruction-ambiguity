#!/usr/bin/env node
// RGO XVII: exact finite ordinal observability. Node 18+, no dependencies.
function run(){
  const comb=(a,k)=>k===0?[[]]:a.flatMap((x,i)=>comb(a.slice(i+1),k-1).map(t=>[x,...t]));
  const perm=a=>a.length===0?[[]]:a.flatMap((x,i)=>perm(a.slice(0,i).concat(a.slice(i+1))).map(p=>[x,...p]));
  function pop(x){let n=0;for(;x;x&=x-1)n++;return n}
  function bpop(x){let n=0;for(;x;x&=x-1n)n++;return n}
  const out=[];
  for(let n=3;n<=6;n++){
    let labels=Array.from({length:n},(_,i)=>i),Q=comb(labels,3),P=perm(labels).filter(p=>p[0]<p.at(-1)),N=P.length,m=Q.length;
    let S=P.map(p=>Q.map(t=>[...t].sort((a,b)=>p.indexOf(a)-p.indexOf(b))[1]));
    let differences=new Set(),single=new Set(),minDistance=m;
    for(let i=0;i<N;i++)for(let j=i+1;j<N;j++){let d=0;for(let k=0;k<m;k++)if(S[i][k]!==S[j][k])d|=1<<k;if(!d)throw Error("Collision");differences.add(d);if(i===0)single.add(d);minDistance=Math.min(minDistance,pop(d));}
    const minimal=ds=>{let r=[];for(const d of [...ds].sort((a,b)=>pop(a)-pop(b)||a-b))if(!r.some(x=>(x&d)===x))r.push(d);return r};
    const masks=minimal(differences),sMasks=minimal(single);
    function fixed(h,dm,lower=0){let tested=0;for(let k=lower;k<=m;k++){
      // Enumerate masks with k bits using Gosper's hack; m<=20.
      let x=(1<<k)-1;const limit=1<<m;
      while(x<limit){tested++;if(dm.every(d=>pop(d&x)>=h))return {count:k,queries:Q.filter((_,j)=>x&(1<<j)),tested};if(!x)break;let u=x&-x,v=x+u;x=v+(((v^x)/u)>>>2);}
    }return null}
    const fixedRows=[];
    for(let h=1;h<=minDistance;h++){let f=fixed(h,masks,Math.ceil(h*n*(n-1)/6));if(!f)throw Error("No fixed protocol");fixedRows.push({h,...f})}
    const cert=fixed(1,sMasks,1);
    // Minimax adaptive search by remaining depth, exact on finite candidate sets.
    const masksBig=Q.map((q,j)=>q.map(a=>S.reduce((s,row,i)=>row[j]===a?s|(1n<<BigInt(i)):s,0n)));
    const full=(1n<<BigInt(N))-1n,memo=new Map(),policy=new Map();
    function solve(B,d){
      let k=bpop(B);if(k<=1)return true;if(!d||k>3**d)return false;
      let key=B.toString(36)+"/"+d;if(memo.has(key))return memo.get(key);
      const opts=masksBig.map((ms,j)=>({j,parts:ms.map(x=>x&B)})).map(o=>({...o,counts:o.parts.map(bpop)})).filter(o=>Math.max(...o.counts)<k&&Math.max(...o.counts)<=3**(d-1)).sort((a,b)=>Math.max(...a.counts)-Math.max(...b.counts)||a.counts.reduce((s,x)=>s+x*x,0)-b.counts.reduce((s,x)=>s+x*x,0)||a.j-b.j);
      for(const o of opts)if([...o.parts].sort((a,b)=>bpop(b)-bpop(a)).every(C=>solve(C,d-1))){memo.set(key,true);policy.set(key,o.j);return true}memo.set(key,false);return false
    }
    const trials=[];let depth=Math.ceil(Math.log(N)/Math.log(3)-1e-12);
    while(true){const success=solve(full,depth);trials.push({depth,success});if(success)break;depth++;}
    let costs=[];
    for(let i=0;i<N;i++){let B=full,d=depth,cost=0;while(bpop(B)>1){const j=policy.get(B.toString(36)+"/"+d);if(j===undefined)throw Error("Incomplete policy");B&=masksBig[j][Q[j].indexOf(S[i][j])];d--;cost++;}if(B!==(1n<<BigInt(i)))throw Error("Wrong reconstruction");costs.push(cost);}
    function greedy(B){let k=bpop(B);let opts=masksBig.map((ms,j)=>{let counts=ms.map(x=>bpop(x&B));return {j,gain:counts.reduce((s,x)=>x?s-(x/k)*Math.log2(x/k):s,0),max:Math.max(...counts)}}).filter(o=>o.max<k).sort((a,b)=>b.gain-a.gain||a.max-b.max||a.j-b.j);return opts[0]?.j}
    // Prior: the first triple has middle element 1. True state spans all U.
    const prior=masksBig[0][Q[0].indexOf(1)];
    let summary={valid:bpop(prior),invalid:N-bpop(prior),priorOnlyReject:0,priorOnlyFalseUnique:0,validCorrect:0,wrongWithResidualU:0,auditReject:0,auditMaxExtra:0,auditMeanExtra:0};
    for(let i=0;i<N;i++){let U=full,C=prior,steps=0;while(bpop(C)>1){let j=greedy(C);if(j===undefined)throw Error("No split");const z=masksBig[j][Q[j].indexOf(S[i][j])];U&=z;C&=z;steps++}let wrong=(prior&(1n<<BigInt(i)))===0n;
      if(wrong){if(!C)summary.priorOnlyReject++;else{summary.priorOnlyFalseUnique++;if(bpop(U)>1)summary.wrongWithResidualU++;}}
      else if(C===(1n<<BigInt(i)))summary.validCorrect++;
      if(wrong){let extra=0;while(C&&bpop(U)>1){let j=greedy(U);if(j===undefined)throw Error("No audit split");let z=masksBig[j][Q[j].indexOf(S[i][j])];U&=z;C&=z;extra++;}if(!C)summary.auditReject++;summary.auditMaxExtra=Math.max(summary.auditMaxExtra,extra);summary.auditMeanExtra+=extra/summary.invalid;}
    }
    if(summary.auditReject!==summary.invalid||summary.validCorrect!==summary.valid||minDistance!==n-2)throw Error("Invariant failed");
    out.push({n,candidates:N,allQueries:m,minimumDistance:minDistance,distinctDifferenceMasks:differences.size,minimalMasks:masks.length,fixed:fixedRows,certificate:cert,adaptive:{depth,trials,mean:costs.reduce((a,b)=>a+b,0)/N,max:Math.max(...costs),verified:N},prior:summary});
  }return {phase:"XVII",protocol:"Strict total orders modulo reversal, noiseless three-outcome median-of-three oracle; fixed lists without repetition; Hamming distance; exact enumeration; ideal wrong-prior stress test, no empirical language claim.",rows:out}
}
console.log(JSON.stringify(run(),null,2));
