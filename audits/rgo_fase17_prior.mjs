#!/usr/bin/env node
// RGO XVII — prior fragility on exact ternary oracle; no dependencies.
function priorAudit(){
  function perms(a){if(a.length<2)return [a];return a.flatMap((x,i)=>perms(a.slice(0,i).concat(a.slice(i+1))).map(p=>[x,...p]))}
  function comb(a,k){if(!k)return [[]];return a.flatMap((v,i)=>comb(a.slice(i+1),k-1).map(t=>[v,...t]))}
  const out=[];
  for(let n=4;n<=8;n++){
    const V=Array.from({length:n},(_,i)=>i),Q=comb(V,3),P=perms(V).filter(p=>p[0]<p.at(-1));
    const S=P.map(p=>{const pos=Array(n);p.forEach((w,i)=>pos[w]=i);return Q.map(t=>t.slice().sort((a,b)=>pos[a]-pos[b])[1])});
    const prior=P.map((p,i)=>p[0]===0||p.at(-1)===0?i:-1).filter(i=>i>=0),U=P.map((_,i)=>i),ps=new Set(prior);
    let stats={n,universe:U.length,priorSize:prior.length,trueInside:prior.length,trueOutside:U.length-prior.length,conditionalReject:0,conditionalWrongUnique:0,conditionalCorrectUnique:0,conditionalQueriesMean:0,validationReject:0,validationCorrect:0,validationQueriesAdditionalMean:0,validationQueriesAdditionalWorst:0};
    function partition(ids,q){const a=[[],[],[]];for(const i of ids)a[Q[q].indexOf(S[i][q])].push(i);return a}
    function pick(ids){let best=null;for(let q=0;q<Q.length;q++){const g=partition(ids,q),sizes=g.map(a=>a.length),max=Math.max(...sizes),cost=sizes.reduce((s,x)=>s+(x?x*Math.log2(x):0),0);if(max===ids.length)continue;if(!best||max<best.max||max===best.max&&cost<best.cost-1e-10)best={q,max,cost,g};}if(!best)throw Error("Unseparated");return best}
    function validation(global,local,depth){if(!local.length){stats.validationReject+=global.length;stats.validationQueriesAdditionalMean+=depth*global.length;stats.validationQueriesAdditionalWorst=Math.max(stats.validationQueriesAdditionalWorst,depth);return}
      if(global.length===1){if(!ps.has(global[0]))throw Error("Wrong global survivor");stats.validationCorrect++;stats.validationQueriesAdditionalMean+=depth;stats.validationQueriesAdditionalWorst=Math.max(stats.validationQueriesAdditionalWorst,depth);return}
      let {q,g}=pick(global),l=partition(local,q);for(let j=0;j<3;j++)if(g[j].length)validation(g[j],l[j],depth+1)}
    function conditional(global,local,depth){if(local.length<=1){stats.conditionalQueriesMean+=depth*global.length;
        if(local.length===0)stats.conditionalReject+=global.length;else {if(!global.includes(local[0]))throw Error("Wrong local support");stats.conditionalCorrectUnique++;stats.conditionalWrongUnique+=global.length-1;}
        validation(global,local,0);return}
      const {q,g}=pick(local),u=partition(global,q);for(let j=0;j<3;j++)if(u[j].length)conditional(u[j],g[j],depth+1)}
    conditional(U,prior,0);stats.conditionalQueriesMean/=U.length;stats.validationQueriesAdditionalMean/=U.length;
    if(stats.conditionalWrongUnique+stats.conditionalReject!==stats.trueOutside||stats.conditionalCorrectUnique!==stats.trueInside||stats.validationReject!==stats.trueOutside||stats.validationCorrect!==stats.trueInside)throw Error("Incorrect counts");
    out.push(stats);
  }
  return {protocol:"Synthetic exact oracle. Prior is fixed independently of truth: element 0 must be an endpoint. All orders up to reversal tested. Conditional observer splits the prior fiber until singleton/empty. Validator continues to split the full universe fiber until prior empty or full fiber unique. Both choose minimum largest branch then entropy. No empirical semantic claim.",results:out};
}
console.log(JSON.stringify(priorAudit(),null,2));
