#!/usr/bin/env node
// Node >=18. Independent ordinal evidence pilot. No training on the evaluation ranks.
import fs from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
function pilot(corpus, goldCSV, halfCSV) {
  function comb(xs,k){if(!k)return [[]];return xs.flatMap((x,i)=>comb(xs.slice(i+1),k-1).map(t=>[x,...t]));}
  function perm(xs){if(xs.length===0)return [[]];return xs.flatMap((x,i)=>perm(xs.slice(0,i).concat(xs.slice(i+1))).map(t=>[x,...t]));}
  const gold=new Map();for(const line of goldCSV.trim().split(/\r?\n/)){const [w,s,r]=line.split(",");if(!gold.has(s))gold.set(s,[]);gold.get(s).push({w,r:+r});}
  const half=halfCSV.trim().split(/\r?\n/).slice(1).map(l=>l.split("\t")).filter(x=>x[1]==="demelo"&&x[2]==="EN").map(x=>({id:x[0],words:x.slice(3).flatMap((v,r)=>v.split("||").map(w=>({w:w.trim().toLowerCase(),r})).filter(x=>x.w))}));
  const patternEdges=new Map(), sourceTriples=new Map(), sourcePairs=new Map();
  const patterns=[["but not",["but","not"]],["if not",["if","not"]],["or even",["or","even"]],["and even",["and","even"]],[", even",[",","even"]],["and almost",["and","almost"]],["or perhaps even",["or","perhaps","even"]]];
  const splitCounts=[];
  for(const data of corpus){let sentences=0,tokens=0,hits=0;const byPattern={};for(const block of data.trim().split(/\r?\n\r?\n/)){const lines=block.split(/\r?\n/), id=lines.find(l=>l.startsWith("# sent_id = "))?.slice(12);const words=lines.filter(l=>/^\d+\t/.test(l)).map(l=>{let v=l.split("\t");return {w:v[1].toLowerCase(),lemma:v[2].toLowerCase(),pos:v[3],form:v[5]};});if(!words.length)continue;sentences++;tokens+=words.length;
    for(let i=0;i<words.length;i++){const a=words[i];if(a.pos!=="ADJ"||a.form.includes("Degree=Cmp")||a.form.includes("Degree=Sup"))continue;for(const [p,seq]of patterns){let start=i+1;if(words[start]?.w===","&&seq[0]!==",")start++;if(!seq.every((x,j)=>words[start+j]?.w===x))continue;const b=words[start+seq.length];if(!b||b.pos!=="ADJ"||a.lemma===b.lemma||b.form.includes("Degree=Cmp")||b.form.includes("Degree=Sup"))continue;const k=a.lemma+"\t"+b.lemma;if(!patternEdges.has(k))patternEdges.set(k,[]);patternEdges.get(k).push({pattern:p,id});hits++;byPattern[p]=(byPattern[p]||0)+1;}
    }
  }splitCounts.push({sentences,tokens,hits,byPattern});}
  for(const s of half){let rs=new Map(s.words.map(x=>[x.w,x.r]));const words=[...rs.keys()].sort();for(const t of comb(words,3)){let order=[...t].sort((a,b)=>rs.get(a)-rs.get(b));if(rs.get(order[0])===rs.get(order[1])||rs.get(order[1])===rs.get(order[2]))continue;const k=t.join("\t");if(!sourceTriples.has(k))sourceTriples.set(k,new Map());const m=sourceTriples.get(k);if(!m.has(order[1]))m.set(order[1],[]);m.get(order[1]).push(s.id);}
  }
  const rows=[];
  for(const [id,ts]of gold){const words=ts.map(x=>x.w).sort(),ref=ts.map(x=>x.w),qs=comb(words,3),P=perm(words).filter(x=>x[0]<x.at(-1));let constraints=[],conflicts=[],pat=[];
    for(const t of qs){const m=sourceTriples.get(t.join("\t"));if(m?.size===1){const [mid,scales]=[...m][0];constraints.push({triple:t,mid,scales});}else if(m?.size>1)conflicts.push({triple:t,mids:[...m.keys()]});}
    for(const a of words)for(const b of words){const hits=patternEdges.get(a+"\t"+b);if(hits)pat.push({a,b,hits});}
    const mid=(p,t)=>[...t].sort((a,b)=>p.indexOf(a)-p.indexOf(b))[1],fit=P.filter(p=>constraints.every(c=>mid(p,c.triple)===c.mid)),certified=[];
    if(fit.length)for(const t of qs){const ms=new Set(fit.map(p=>mid(p,t)));if(ms.size===1){const pred=[...ms][0];certified.push({triple:t,pred,correct:pred===mid(ref,t),direct:constraints.some(c=>c.triple.join("\t")===t.join("\t"))});}}
    const leaveOneOut=constraints.map(c=>{const kept=constraints.filter(x=>x!==c),rest=P.filter(p=>kept.every(x=>mid(p,x.triple)===x.mid));const ms=new Set(rest.map(p=>mid(p,c.triple)));return {triple:c.triple,determined:ms.size===1,correct:ms.size===1&&[...ms][0]===mid(ref,c.triple)};});
    rows.push({id,words,orders:P.length,compatible:fit.length,patternMatches:pat,observations:constraints,conflicts,certified,leaveOneOut});}
  return {corpus:{splits:splitCounts,uniqueDirectedPairs:patternEdges.size,matchedScalePairs:rows.reduce((s,r)=>s+r.patternMatches.length,0),matches:rows.flatMap(r=>r.patternMatches.map(x=>({scale:r.id,...x})))},ordinalTransfer:{sourceScales:half.length,sourceUniqueTriples:sourceTriples.size,rows,observed:rows.reduce((s,r)=>s+r.observations.length,0),certified:rows.reduce((s,r)=>s+r.certified.length,0),correct:rows.reduce((s,r)=>s+r.certified.filter(x=>x.correct).length,0),inferred:rows.reduce((s,r)=>s+r.certified.filter(x=>!x.direct).length,0),inferredCorrect:rows.reduce((s,r)=>s+r.certified.filter(x=>!x.direct&&x.correct).length,0),leaveOneOut:rows.reduce((s,r)=>s+r.leaveOneOut.filter(x=>x.determined).length,0)}};
}
const sources=[["UniversalDependencies/UD_English-EWT","master","en_ewt-ud-dev.conllu","dcd6281e66995543249cacf98789cbe664a42ca0"],["UniversalDependencies/UD_English-EWT","master","en_ewt-ud-test.conllu","de059e15c875a44adf2a738ac2a6ed2d6bdd2c73"],["UniversalDependencies/UD_English-EWT","master","en_ewt-ud-train.conllu","e6202c973502063a42e7a1f114d5ae7a61f75ba8"],["Coral-Lab/scales","master","ordering/ordering_gold_standard.csv","dc5ecb8805270be3fd135a2c1ff926b03926078d"],["ainagari/scalar_adjs","master","multilingual_data/all_translations.csv","a281181b88078bfd858e77b2eda2cf36eaca94f8"]];
const arg=process.argv.indexOf('--data'),root=arg<0?'rgo_data':process.argv[arg+1];
await fs.mkdir(root,{recursive:true});
const data=await Promise.all(sources.map(async ([repo,ref,p,sha])=>{const f=path.join(root,path.basename(p));let b;try{b=await fs.readFile(f)}catch(e){if(e.code!=='ENOENT')throw e;const r=await fetch('https://raw.githubusercontent.com/'+repo+'/'+ref+'/'+p);if(!r.ok)throw Error(r.status+' '+p);b=Buffer.from(await r.arrayBuffer());await fs.writeFile(f,b);}const hash=createHash('sha1').update('blob '+b.length+'\0').update(b).digest('hex');if(hash!==sha)throw Error('Source blob mismatch: '+p+' '+hash);return b.toString('utf8')}));
console.log(JSON.stringify({sources,...pilot(data.slice(0,3),data[3],data[4])},null,2));
