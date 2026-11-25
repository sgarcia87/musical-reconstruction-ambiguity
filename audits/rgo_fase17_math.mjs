#!/usr/bin/env node
// RGO XVII — exact ternary observation protocol, Node >=18, no dependencies.
function mathAudit(){
  function perms(a){if(a.length<2)return [a];return a.flatMap((x,i)=>perms(a.slice(0,i).concat(a.slice(i+1))).map(p=>[x,...p]))}
  function comb(a,k){if(k===0)return [[]];return a.flatMap((v,i)=>comb(a.slice(i+1),k-1).map(t=>[v,...t]))}
  function bits(v){let n=0;while(v){v&=v-1;n++}return n}
  const results=[];
  for(let n=3;n<=8;n++){
    const items=Array.from({length:n},(_,i)=>i),Q=comb(items,3),P=perms(items).filter(p=>p[0]<p.at(-1));
    const S=P.map(p=>{const r=Array(n);p.forEach((x,i)=>r[x]=i);return Q.map(t=>t.slice().sort((a,b)=>r[a]-r[b])[1])});
    const N=P.length;const lb=Math.ceil(Math.log(N)/Math.log(3)-1e-12);
    let fixed=null,certificate=null;
    if(n<=6){
      const masks=new Set();let minDistance=Q.length;
      for(let i=0;i<N;i++)for(let j=i+1;j<N;j++){let m=0;for(let q=0;q<Q.length;q++)if(S[i][q]!==S[j][q])m|=1<<q;masks.add(m);minDistance=Math.min(minDistance,bits(m))}
      if(minDistance!==n-2)throw Error("Distance mismatch");
      const minimal=[];for(const m of [...masks].sort((a,b)=>bits(a)-bits(b)||a-b)){if(!minimal.some(k=>(m&k)===k))minimal.push(m)}
      const pairLB=Math.ceil(n*Math.ceil((n-1)/2)/3);
      let found=null,tested={};
      function search(k,start,m){if(k===0){tested[depth]=(tested[depth]||0)+1;if(minimal.every(x=>x&m)){found=m;return true}return false}
        for(let i=start;i<=Q.length-k;i++)if(search(k-1,i+1,m|(1<<i)))return true;return false}
      let depth=pairLB;for(;depth<=Q.length;depth++)if(search(depth,0,0))break;
      if(found===null)throw Error("No fixed solution");
      fixed={minimum:depth,lowerBound:pairLB,witness:Q.filter((_,i)=>found&(1<<i)),tested,distinctDifferenceMasks:masks.size,minimalMasks:minimal.length,fullDictionaryMinDistance:minDistance};
      const truth=0;let cf=null;const cmasks=[];for(let j=1;j<N;j++){let m=0;for(let q=0;q<Q.length;q++)if(S[truth][q]!==S[j][q])m|=1<<q;cmasks.push(m)}
      function findCert(k,start,m){if(!k){if(cmasks.every(x=>x&m)){cf=m;return true}return false}for(let i=start;i<=Q.length-k;i++)if(findCert(k-1,i+1,m|1<<i))return true;return false}
      let k=1;for(;k<=n-2;k++)if(findCert(k,0,0))break;
      certificate={minimum:k,witness:Q.filter((_,i)=>cf&(1<<i)),truth:P[0]};
    }
    function greedy(ids,depth=0){
      if(ids.length===1)return {worst:depth,sum:depth,count:1};
      let best=null;for(let q=0;q<Q.length;q++){let groups=[[],[],[]];for(let i of ids)groups[Q[q].indexOf(S[i][q])].push(i);const sizes=groups.map(g=>g.length),max=Math.max(...sizes);if(max===ids.length)continue;const ent=sizes.reduce((s,x)=>s+(x?x*Math.log2(x):0),0);if(!best||max<best.max||max===best.max&&ent<best.ent-1e-10)best={groups,max,ent,q}}
      if(!best)throw Error("Unseparated");
      const branches=best.groups.filter(g=>g.length).map(g=>greedy(g,depth+1));
      return {worst:Math.max(...branches.map(x=>x.worst)),sum:branches.reduce((s,x)=>s+x.sum,0),count:branches.reduce((s,x)=>s+x.count,0)};
    }
    const g=greedy(Array.from({length:N},(_,i)=>i));
    let optimal=null;
    if(g.worst===lb)optimal=lb;
    else if(n<=6){
      const memo=new Map();
      function solve(ids,d){if(ids.length<=1)return true;if(ids.length>3**d||d===0)return false;let key=d+":"+ids.join(",");if(memo.has(key))return memo.get(key);let options=[];
        for(let q=0;q<Q.length;q++){let groups=[[],[],[]];for(let i of ids)groups[Q[q].indexOf(S[i][q])].push(i);let max=Math.max(...groups.map(g=>g.length));if(max<=3**(d-1)&&max<ids.length)options.push({max,groups})}
        options.sort((a,b)=>a.max-b.max);for(const o of options){if(o.groups.filter(g=>g.length).sort((a,b)=>b.length-a.length).every(g=>solve(g,d-1))){memo.set(key,true);return true}}memo.set(key,false);return false;
      }
      optimal=lb;for(;optimal<g.worst;optimal++)if(solve(Array.from({length:N},(_,i)=>i),optimal))break;
    }
    // Complete-dictionary Hamming distance theorem; direct check for n<=6.
    const adjacent=items.slice();[adjacent[0],adjacent[1]]=[adjacent[1],adjacent[0]];
    const sig=p=>Q.map(t=>t.slice().sort((a,b)=>p.indexOf(a)-p.indexOf(b))[1]);
    const aa=sig(items),bb=sig(adjacent),adjDist=aa.filter((x,i)=>x!==bb[i]).length;
    if(adjDist!==n-2)throw Error("adjacent distance");
    // Known truth adjacent-chain certificate n-2: independently verify.
    const chain=Array.from({length:n-2},(_,i)=>Q.findIndex(t=>t[0]===i&&t[1]===i+1&&t[2]===i+2));
    const chainFiber=S.filter(row=>chain.every(q=>row[q]===aa[q])).length;
    if(chainFiber!==1)throw Error("chain not unique");
    // Exclude truth with adjacent swapped alternative: all but n-2 observations agree.
    results.push({n,orders:N,queries:Q.length,entropyBits:Math.log2(N),adaptiveLowerBound:lb,greedyWorst:g.worst,greedyMean:g.sum/N,adaptiveMinimum:optimal,fixed,certificate,chainCertificateSize:n-2,chainFiber,fullMinDistance:n-2,adjacentSwapAgreements:Q.length-adjDist,detectErrors:n-3,correctErrors:Math.floor((n-3)/2)});
  }
  return {results};
}
console.log(JSON.stringify(mathAudit(),null,2));
