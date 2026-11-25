#!/usr/bin/env node
// RGO XVII — independent paraphrase evidence, Node 18+, no dependencies.
import fs from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
function semanticAudit(raw,oldGold,newGold){
  const G=JSON.parse(raw);
  if(!Array.isArray(G.nodes)||!Array.isArray(G.links)||!G.directed)throw Error("Unexpected JJGraph format");
  // Extract evidence before opening any gold rankings. Fixed rule: modifiers that
  // conventionally increase degree, without using rankings to tune the list.
  const strong=new Set("very extremely exceedingly exceptionally extraordinarily intensely immensely remarkably unusually tremendously incredibly highly deeply profoundly really especially particularly utterly absolutely totally completely".split(" "));
  const vocab=new Set(G.nodes.map(n=>n.id.toLowerCase()));
  const all=new Map(), strict=new Map();
  function add(M,a,b,ad){const k=a+"\t"+b;if(!M.has(k))M.set(k,new Set());M.get(k).add(ad)}
  let validLinks=0;
  for(const e of G.links){if(e.rel!=="adv+jj->jj"||typeof e.adverb!=="string")continue;let a=G.nodes[e.source]?.id?.toLowerCase(),b=G.nodes[e.target]?.id?.toLowerCase(),ad=e.adverb.toLowerCase().trim();if(!a||!b||a===b||!ad)continue;validLinks++;add(all,a,b,ad);if(strong.has(ad))add(strict,a,b,ad)}
  const strict2=new Map([...strict].filter(([,s])=>s.size>=2));
  const wo=new Map();
  for(const l of oldGold.trim().split(/\r?\n/)){const [w,id,r]=l.split(",");if(!wo.has(id))wo.set(id,[]);wo.get(id).push({w:w.toLowerCase(),r:+r})}
  const previous=new Set([...wo.values()].flat().map(x=>x.w));
  const half=newGold.trim().split(/\r?\n/).slice(1).map(l=>l.split("\t")).filter(v=>v[1]==="demelo"&&v[2]==="EN").map(v=>({id:v[0],terms:v.slice(3).flatMap((s,r)=>s.split("||").map(w=>({w:w.trim().toLowerCase(),r})).filter(x=>x.w))}));
  function perms(a){if(a.length<2)return [a];return a.flatMap((x,i)=>perms(a.slice(0,i).concat(a.slice(i+1))).map(p=>[x,...p]))}
  function comb(a,k){if(k===0)return [[]];return a.flatMap((v,i)=>comb(a.slice(i+1),k-1).map(t=>[v,...t]))}
  function truthMiddle(t,rank){const a=t.slice().sort((a,b)=>rank.get(a)-rank.get(b));return rank.get(a[0])<rank.get(a[1])&&rank.get(a[1])<rank.get(a[2])?a[1]:null}
  function mid(p,t){const r=t.map(x=>p.indexOf(x));return t[r[0]>r[1]?(r[1]>r[2]?1:r[0]>r[2]?2:0):(r[0]>r[2]?0:r[1]>r[2]?2:1)]}
  function evalScale(scale,M,mode){
    const terms=scale.terms,words=[...new Set(terms.map(x=>x.w))].sort(),rank=new Map(terms.map(x=>[x.w,x.r]));
    if(words.length>8)throw Error("Scale above exact enumeration limit");
    const edges=[];for(const a of words)for(const b of words)if(M.has(a+"\t"+b))edges.push({a,b,adverbs:[...M.get(a+"\t"+b)].sort()});
    const eset=new Set(edges.map(e=>e.a+"\t"+e.b)),ts=comb(words,3),goldTs=ts.map(t=>({t,m:truthMiddle(t,rank)})).filter(x=>x.m!==null);
    // Intensity is directed on one half-scale, but not across antonym poles.
    // On bipolar scales only use unambiguous two-edge chains to propose a middle.
    const ternary=[];
    for(const t of ts){const ms=t.filter(b=>{let [a,c]=t.filter(w=>w!==b);return eset.has(a+"\t"+b)&&eset.has(b+"\t"+c)||eset.has(c+"\t"+b)&&eset.has(b+"\t"+a)});if(ms.length===1)ternary.push({t,m:ms[0]});}
    const orders=perms(words).filter(p=>mode==="directed"||p.length<2||p[0]<p.at(-1));
    const violations=orders.map(p=>mode==="directed"?edges.filter(e=>p.indexOf(e.a)>p.indexOf(e.b)).length:ternary.filter(e=>mid(p,e.t)!==e.m).length);
    const min=Math.min(...violations);
    const compatible=orders.filter((_,i)=>violations[i]===0),one=orders.filter((_,i)=>violations[i]<=1);
    const goldOrders=orders.filter(p=>{const asc=p.every((w,i)=>i===0||rank.get(p[i-1])<=rank.get(w));const desc=p.every((w,i)=>i===0||rank.get(p[i-1])>=rank.get(w));return mode==="directed"?asc:asc||desc});
    const goldKey=new Set(goldOrders.map(p=>p.join("\t")));
    function evaluate(F){let certain=[],ambiguous=0;for(const {t,m}of goldTs){if(!F.length)break;let mm=new Set(F.map(p=>mid(p,t)));if(mm.size===1){const pred=[...mm][0];certain.push({t,pred,reference:m,correct:pred===m})}else ambiguous++}
      return {orders:F.length,truthIncluded:F.some(p=>goldKey.has(p.join("\t"))),certified:certain.length,correct:certain.filter(x=>x.correct).length,wrong:certain.filter(x=>!x.correct),certain,ambiguous,examples:F.slice(0,2)}}
    // A forced middle from a uniform candidate posterior is only a conditional prediction.
    // For an unobserved scale it is generally unidentifiable.
    return {id:scale.id,words,coveredWords:words.filter(w=>vocab.has(w)).length,goldTriples:goldTs.length,edges,ternary,edgeStrictCorrect:edges.filter(e=>rank.get(e.a)<rank.get(e.b)).length,edgeStrictWrong:edges.filter(e=>rank.get(e.a)>rank.get(e.b)).length,edgeTied:edges.filter(e=>rank.get(e.a)===rank.get(e.b)).length,initialOrders:orders.length,minimumViolations:min,exact:evaluate(compatible),budget1:evaluate(one)};
  }
  function sum(rows){const r={scales:rows.length,scalesWithEdges:0,scalesWithTernary:0,strictTriples:0,edges:0,edgeCorrect:0,edgeWrong:0,edgeTied:0,constraints:0,incompatible:0,truthExcluded:0,unique:0,exactCertified:0,exactCorrect:0,oneCertified:0,oneCorrect:0,oneIncompatible:0,oneTruthExcluded:0,oneUnique:0};
    for(const x of rows){r.scalesWithEdges+=+(x.edges.length>0);r.scalesWithTernary+=+(x.ternary.length>0);r.strictTriples+=x.goldTriples;r.edges+=x.edges.length;r.edgeCorrect+=x.edgeStrictCorrect;r.edgeWrong+=x.edgeStrictWrong;r.edgeTied+=x.edgeTied;r.constraints+=x.ternary.length;r.incompatible+=+(x.exact.orders===0);r.truthExcluded+=+(!x.exact.truthIncluded);r.unique+=+(x.exact.orders===1);r.exactCertified+=x.exact.certified;r.exactCorrect+=x.exact.correct;r.oneCertified+=x.budget1.certified;r.oneCorrect+=x.budget1.correct;r.oneIncompatible+=+(x.budget1.orders===0);r.oneTruthExcluded+=+(!x.budget1.truthIncluded);r.oneUnique+=+(x.budget1.orders===1);}
    return r}
  const sets=[["all",all],["strict",strict],["strict2",strict2]];
  const runs={};
  for(const [name,M]of sets){
    const full=[...wo].map(([id,terms])=>evalScale({id,terms},M,"ternary"));
    const h=half.filter(s=>s.terms.length>=3).map(s=>evalScale(s,M,"directed"));
    const d=half.map(s=>({id:s.id,terms:s.terms.filter(x=>!previous.has(x.w))})).filter(s=>s.terms.length>=3&&new Set(s.terms.map(x=>x.r)).size>=3).map(s=>evalScale(s,M,"directed"));
    runs[name]={globalPairs:M.size,full:{summary:sum(full),rows:full},half:{summary:sum(h),rows:h},disjoint:{summary:sum(d),rows:d}};
  }
  return {graph:{nodes:G.nodes.length,links:G.links.length,validNonselfParaphrases:validLinks,distinctDirectedPairs:all.size,strictPairs:strict.size,strict2Pairs:strict2.size},intensifierList:[...strong].sort(),protocol:"Exploratory; gold membership supplied. All vs fixed conventional intensifier whitelist vs at least two different whitelisted modifiers (not necessarily independent). Half-scales directed; full bipolar scales use only unambiguous two-edge-chain middle constraints. All words retained, including absent words; strict gold triples only; weak gold ranks admit tied completions. Exact and absolute one-violation budgets. No ranking labels used to extract the graph.",runs};
}
const inputs=[["acocos/scalar-adj","jjgraph/jjgraph.json","master","ef174b3608e8177cefc69d1edef93978232f5ce6"],["Coral-Lab/scales","ordering/ordering_gold_standard.csv","master","dc5ecb8805270be3fd135a2c1ff926b03926078d"],["ainagari/scalar_adjs","multilingual_data/all_translations.csv","master","a281181b88078bfd858e77b2eda2cf36eaca94f8"]];
const i=process.argv.indexOf('--data'), root=i<0?'rgo_data':process.argv[i+1];
await fs.mkdir(root,{recursive:true});
const data=await Promise.all(inputs.map(async ([repo,p,ref,expected])=>{const f=path.join(root,path.basename(p));let b;try{b=await fs.readFile(f)}catch(e){if(e.code!=='ENOENT')throw e;const r=await fetch('https://raw.githubusercontent.com/'+repo+'/'+ref+'/'+p);if(!r.ok)throw Error(r.status+' '+p);b=Buffer.from(await r.arrayBuffer());await fs.writeFile(f,b);}const sha=createHash('sha1').update('blob '+b.length+'\0').update(b).digest('hex');if(sha!==expected)throw Error('Source hash mismatch: '+p+' '+sha);return b.toString('utf8')}));
console.log(JSON.stringify({phase:'XVII',sources:inputs.map(([repo,path,ref,blob])=>({repo,path,ref,blob})),...semanticAudit(...data)},null,2));
