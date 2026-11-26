#!/usr/bin/env node
// RGO XVIII — JSB Chorales, symbolic retrieval and temporal observability.
// Node >=18, no dependencies. No GitHub writes. Original data not bundled.
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
const URL='https://raw.githubusercontent.com/czhuang/JSB-Chorales-dataset/master/jsb-chorales-quarter.json';
const SHA='ff93746647d1f5af2f719d235329c294267f3088';
const gcd=(a,b)=>b?gcd(b,a%b):a,lcm=(a,b)=>a*b/gcd(a,b);
const rot=(m,s)=>((m<<s)|(m>>(12-s)))&4095;
const pc=new Uint8Array(4096),canon=new Uint16Array(4096),offset=new Uint8Array(4096),period=new Uint8Array(4096),support=new Uint16Array(4096),power=new Array(4096);
const z=[[1,0,0,0]];for(let i=1;i<12;i++){let [a,b,c,d]=z[i-1];z.push([-d,a,b+d,c])}
for(let m=0;m<4096;m++){
 if(m)pc[m]=pc[m>>1]+(m&1);
 let best=m,p=12;for(let s=1;s<12;s++){const r=rot(m,s);if(r<best)best=r;if(r===m&&p===12)p=s}
 canon[m]=best;period[m]=p;for(let s=0;s<p;s++)if(rot(best,s)===m){offset[m]=s;break}
 let bits=0;for(let k=1;k<12;k++){let v=[0,0,0,0];for(let n=0;n<12;n++)if(m&(1<<n))for(let j=0;j<4;j++)v[j]+=z[k*n%12][j];if(v.some(Boolean))bits|=1<<k}
 support[m]=bits;
}
for(let m=0;m<4096;m++)power[m]=Array.from({length:7},(_,s)=>pc[m&rot(m,s)]).join('.');
const ds=new Uint8Array(4096);for(let bits=0;bits<4096;bits++){let d=1;for(let k=1;k<12;k++)if(bits&(1<<k))d=lcm(d,12/gcd(12,k));ds[bits]=d}
const phase=(a,b)=>{let d=ds[support[a]&support[b]];return canon[a]+':'+canon[b]+':'+d+':'+((offset[b]-offset[a]+12)%d)};
const joint=(a,b)=>{let d=gcd(period[a],period[b]);return canon[a]+':'+canon[b]+':'+d+':'+((offset[b]-offset[a]+12)%d)};
const triple=(a,b,c)=>{let best=Infinity;for(let s=0;s<12;s++){let x=rot(a,s)*16777216+rot(b,s)*4096+rot(c,s);if(x<best)best=x}return String(best)};
const collapse=a=>a.filter((m,i)=>!i||m!==a[i-1]);
const mask=a=>a.reduce((s,n)=>s|1<<((n%12+12)%12),0);
const uniq=a=>{let best=null;for(let s=0;s<12;s++){let x=a.map(m=>rot(m,s)).join(',');if(best===null||x<best)best=x}return best};
const cross=(a,b)=>Array.from({length:12},(_,s)=>pc[a&rot(b,s)]);
function audit(data){
 const refs=[];for(const split of ['train','valid','test'])data[split].forEach((notes,i)=>refs.push({id:split+'-'+i,notes,seq:collapse(notes.map(mask)),split}));
 const targets=refs.map((r,i)=>i).filter(i=>refs[i].split==='test');
 let pairTotal=0,pairStrict=0,phaseLostExamples=[];
 for(let r of refs)for(let j=1;j<r.seq.length;j++){const a=r.seq[j-1],b=r.seq[j],d=ds[support[a]&support[b]],g=gcd(period[a],period[b]);pairTotal++;if(d<g){pairStrict++;if(phaseLostExamples.length<5)phaseLostExamples.push({id:r.id,index:j-1,a,b,d,g})}}
 function collisions(fn){const m=new Map();for(let r of refs){let k=fn(r.seq);m.set(k,(m.get(k)||0)+1)}return {distinct:m.size,nonunique:[...m.values()].filter(x=>x>1).reduce((s,x)=>s+x,0)}}
 const exact={globalOrbit:collisions(uniq),localPower:collisions(a=>a.map(m=>power[m]).join('|')),localShape:collisions(a=>a.map(m=>canon[m]).join(',')),phasePath:collisions(a=>a.map((m,i)=>i?phase(a[i-1],m):String(canon[m])).join('|')),pairPath:collisions(a=>a.map((m,i)=>i?joint(a[i-1],m):String(canon[m])).join('|')),adjacentPairs:pairTotal,phaseLessThanPairOrbit:pairStrict,phaseLostExamples};
 const a=3,b=1365,b1=rot(b,1);
 exact.counterexample={a,b,b1,phase1:phase(a,b),phase2:phase(a,b1),pair1:joint(a,b),pair2:joint(a,b1),correlation1:cross(a,b),correlation2:cross(a,b1),globallySame:uniq([a,b])===uniq([a,b1])};
 const methods=['power_bag','shape_bag','self_similarity','pair_orbit','triple_orbit','phase_adjacent','phase_multilag','pair_multilag','chroma_alignment'];
 function add(m,k){m.set(k,(m.get(k)||0)+1)}
 function features(a){
  const f=Array.from({length:8},()=>new Map()),h=new Float64Array(12);
  for(const m of a){add(f[0],power[m]);add(f[1],canon[m]);for(let j=0;j<12;j++)if(m&(1<<j))h[j]++}
  for(const lag of [1,2,4,8])for(let i=lag;i<a.length;i++){let x=a[i-lag],y=a[i],u=pc[x|y],v=u?pc[x&y]/u:1;add(f[2],lag+':'+Math.min(4,Math.floor(v*5)))}
  for(let i=1;i<a.length;i++){add(f[3],joint(a[i-1],a[i]));add(f[5],phase(a[i-1],a[i]))}
  for(let i=2;i<a.length;i++)add(f[4],triple(a[i-2],a[i-1],a[i]));
  for(const lag of [1,2,4])for(let i=lag;i<a.length;i++){add(f[6],lag+'|'+phase(a[i-lag],a[i]));add(f[7],lag+'|'+joint(a[i-lag],a[i]))}
  return {f,h,a};
 }
 const R=refs.map(r=>features(r.seq)),df=Array.from({length:8},()=>new Map());
 for(const r of R)r.f.forEach((m,j)=>{for(const k of m.keys())add(df[j],k)});
 function weight(f){return f.map((m,j)=>{let out=new Map(),norm=0;for(const [k,c]of m){let w=(1+Math.log(c))*(1+Math.log((1+R.length)/(1+(df[j].get(k)||0))));out.set(k,w);norm+=w*w}norm=Math.sqrt(norm)||1;for(const [k,v]of out)out.set(k,v/norm);return out})}
 for(const r of R)r.w=weight(r.f);
 function cosine(a,b){if(a.size>b.size)[a,b]=[b,a];let s=0;for(const [k,v]of a)s+=v*(b.get(k)||0);return s}
 // OTI + simple Smith-Waterman-like local alignment, not Serrà's full method.
 function align(q,r){let sh=0,best=-Infinity;for(let s=0;s<12;s++){let v=0;for(let i=0;i<12;i++)v+=q.h[i]*r.h[(i+s)%12];if(v>best){best=v;sh=s}}
  const a=q.a,b=r.a;let row=new Float64Array(b.length+1),prev=new Float64Array(b.length+1),mx=0;
  for(let i=0;i<a.length;i++){const x=rot(a[i],sh);row[0]=0;for(let j=1;j<=b.length;j++){const y=b[j-1],u=pc[x|y],sim=u?pc[x&y]/u:1;const v=Math.max(0,prev[j-1]+2*sim-1,prev[j]-.5,row[j-1]-.5);row[j]=v;if(v>mx)mx=v}let tmp=prev;prev=row;row=tmp}
  return mx/Math.max(1,a.length);
 }
 function rng(seed){let s=seed>>>0;return ()=>{s=(Math.imul(s,1664525)+1013904223)>>>0;return s/4294967296}}
 const conditions=[['transpose_register',1,0,0],['variable_duration',1,0,0],['crop50',.5,0,0],['edit20',1,.2,.1],['crop50_edit20',.5,.2,.1],['crop25_edit20',.25,.2,.1]];
 function transform(r,ri,c,ci){const rand=rng(17001+ri*1091+ci*101),shift=1+Math.floor(rand()*11);let a=collapse(r.notes.map(notes=>mask(notes.map(n=>n+shift+12*(Math.floor(rand()*3)-1)))));
  const [name,frac,noise,del]=c;
  if(name==='variable_duration'){let v=[];for(const m of a){let k=1+Math.floor(rand()*4);for(let j=0;j<k;j++)v.push(m)}a=collapse(v)}
  if(frac<1){let k=Math.max(3,Math.floor(a.length*frac)),start=Math.floor(rand()*(a.length-k+1));a=a.slice(start,start+k)}
  let corrupted=0,dropped=0,b=[];for(let m of a){if(del&&rand()<del){dropped++;continue}if(noise&&rand()<noise){m^=1<<Math.floor(rand()*12);corrupted++}b.push(m)}
  if(b.length<3)b=a.slice(0,3);
  return {a:collapse(b),shift,corrupted,dropped};
 }
 function rank(scores,i){const x=scores[i];let better=0,equal=0;for(const s of scores){if(s>x+1e-10)better++;else if(Math.abs(s-x)<=1e-10)equal++}
  let rr=0;for(let k=1;k<=equal;k++)rr+=1/(better+k);return {top1:better===0?1/equal:0,top5:Math.max(0,Math.min(equal,5-better))/equal,mrr:rr/equal,rank:better+(equal+1)/2}}
 const results=[];
 for(let ci=0;ci<conditions.length;ci++){
  const c=conditions[ci],acc=Object.fromEntries(methods.map(m=>[m,{top1:0,top5:0,mrr:0,rank:0}]));
  let lengths=0,edits=0,drops=0;
  for(const i of targets){const t=transform(refs[i],i,c,ci),q=features(t.a);q.w=weight(q.f);lengths+=t.a.length;edits+=t.corrupted;drops+=t.dropped;let scores=methods.map(()=>[]);
   for(const r of R){for(let j=0;j<8;j++)scores[j].push(cosine(q.w[j],r.w[j]));scores[8].push(align(q,r))}
   methods.forEach((m,j)=>{let v=rank(scores[j],i);for(let k of Object.keys(v))acc[m][k]+=v[k]});
  }
  for(const a of Object.values(acc))for(let k of Object.keys(a))a[k]/=targets.length;
  results.push({condition:c[0],queries:targets.length,meanLength:lengths/targets.length,corrupted:edits,dropped:drops,methods:acc});
 }
 const controls={independent:{n:0,localShapesSame:0,phasePathSame:0,pairPathSame:0,globalOrbitSame:0},block:{n:0,localShapesSame:0,phasePathSame:0,pairPathSame:0,globalOrbitSame:0}};
 const path=(s,fn)=>s.map((m,i)=>i?fn(s[i-1],m):String(canon[m])).join('|');
 for(const i of targets)for(const mode of ['independent','block']){const a=refs[i].seq,r=rng(88000+i),s=1+Math.floor(r()*11);let b=a.map((m,j)=>rot(m,mode==='independent'?Math.floor(r()*12):j>=Math.floor(a.length/2)?s:0));const o=controls[mode];o.n++;o.localShapesSame+=+(a.map(m=>canon[m]).join(',')===b.map(m=>canon[m]).join(','));o.phasePathSame+=+(path(a,phase)===path(b,phase));o.pairPathSame+=+(path(a,joint)===path(b,joint));o.globalOrbitSame+=+(uniq(a)===uniq(b))}
 return {dataset:'JSB Chorales quarter-note; all transformations synthetic',referenceCount:refs.length,testCount:targets.length,exact,controls,results};
}
function temporalAudit(data){
 const levels=[2,4,3],weights=[1,1,Math.log2(3)];
 class DSU{constructor(seq,l){this.p=seq.map((_,i)=>i);this.c=seq.filter(m=>period[m]%l===0).length}root(i){while(this.p[i]!==i){this.p[i]=this.p[this.p[i]];i=this.p[i]}return i}join(i,j){let a=this.root(i),b=this.root(j);if(a!==b){this.p[a]=b;this.c--}}}
 const amb=sets=>sets.reduce((a,s,i)=>a+Math.max(0,s.c-1)*weights[i],0);
 const mods={phase:(a,b)=>ds[support[a]&support[b]],joint:(a,b)=>gcd(period[a],period[b])};
 function compute(a,kind,lags){const sets=levels.map(l=>new DSU(a,l)),f=mods[kind];for(let lag of lags)for(let i=lag;i<a.length;i++){const j=i-lag,d=f(a[i],a[j]);for(let k=0;k<3;k++)if(d%levels[k]===0)sets[k].join(i,j)}return sets}
 function repair(a,kind,sets){const f=mods[kind],lower=Math.max(0,...sets.map(s=>s.c-1)),chosen=[];while(amb(sets)>1e-12){let best=null;for(let j=1;j<a.length;j++)for(let i=0;i<j;i++){let d=f(a[i],a[j]),k=levels.map((l,k)=>d%l===0&&sets[k].root(i)!==sets[k].root(j)?k:-1).filter(k=>k>=0),gain=k.reduce((s,i)=>s+weights[i],0);if(gain>0&&(!best||gain>best.gain+1e-12))best={i,j,k,gain}}
  if(!best)break;for(const k of best.k)sets[k].join(best.i,best.j);chosen.push([best.i,best.j]);}return {lower,chosen,exact:amb(sets)<1e-12}}
 const all=Object.entries(data).flatMap(([split,songs])=>songs.map((song,i)=>({id:split+'-'+i,a:song.map(mask)})));
 const results=[];
 for(const window of ['collapsed',1,2,4,8]){let o={window,pieces:0,frames:0,phaseAdj:{exact:0,bits:0},jointAdj:{exact:0,bits:0},phaseLags:{exact:0,bits:0},jointLags:{exact:0,bits:0},phaseRepair:{exact:0,added:0,optimal:0,max:0},jointRepair:{exact:0,added:0,optimal:0,max:0},jointStronger:0};
  for(const {a:raw}of all){let a;if(window==='collapsed')a=collapse(raw);else{a=[];for(let i=0;i+window<=raw.length;i++){let x=0;for(let j=0;j<window;j++)x|=raw[i+j];a.push(x)}}
   if(!a.length)continue;o.pieces++;o.frames+=a.length;let p=compute(a,'phase',[1]),j=compute(a,'joint',[1]);const pb=amb(p),jb=amb(j);o.jointStronger+=+(pb>jb+1e-12);
   for(const [key,bits]of [['phaseAdj',pb],['jointAdj',jb],['phaseLags',amb(compute(a,'phase',[1,2,4]))],['jointLags',amb(compute(a,'joint',[1,2,4]))]]){o[key].exact+=+(bits<1e-12);o[key].bits+=bits}
   for(const [key,kind,sets]of [['phaseRepair','phase',p],['jointRepair','joint',j]]){const t=repair(a,kind,sets),q=o[key],k=t.chosen.length;q.exact+=+t.exact;q.added+=k;q.optimal+=+(t.exact&&k===t.lower);q.max=Math.max(q.max,k)}
  }
  for(const k of ['phaseAdj','jointAdj','phaseLags','jointLags'])o[k].bits/=o.pieces;results.push(o)}
 return results;
}
function selfTest(){
 const assert=(x,msg)=>{if(!x)throw Error(msg)};
 for(let a=0;a<4096;a++){assert(12%period[a]===0,'invalid period');assert(rot(canon[a],offset[a])===a,'invalid representative');assert(ds[support[a]]===period[a],'period support mismatch')}
 const a=3,b=1365,b1=rot(b,1);assert(JSON.stringify(cross(a,b))===JSON.stringify(cross(a,b1)),'cross counterexample');assert(phase(a,b)===phase(a,b1)&&joint(a,b)!==joint(a,b1),'different relative information');
 let seed=987654321;const rand=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed};
 for(let i=0;i<10000;i++){const a=rand()%4096,b=rand()%4096,s=rand()%12,t=rand()%12;const d=ds[support[a]&support[b]],g=gcd(period[a],period[b]);assert(g%d===0,'phase modulus');assert(phase(a,b)===phase(rot(a,s),rot(b,s)),'phase invariance');assert(joint(a,b)===joint(rot(a,s),rot(b,s)),'pair invariance');assert((phase(a,b)===phase(a,rot(b,t)))===(JSON.stringify(cross(a,b))===JSON.stringify(cross(a,rot(b,t)))),'cross equivalence');assert((joint(a,b)===joint(a,rot(b,t)))===(uniq([a,b])===uniq([a,rot(b,t)])),'pair equivalence')}
 const tiny={train:[[[60,64,67],[62,65,69],[59,62,67],[60,64,67],[60,64,67],[62,65,69],[64,67,71],[60,64,67]]],valid:[[[60],[62],[63],[65],[66],[67],[69],[72]]],test:[[[60,63,67],[65,68,72],[67,70,74],[60,63,67],[60,63,67],[62,65,69],[63,67,70],[60,63,67]]]};
 const r=audit(tiny);assert(r.referenceCount===3&&r.testCount===1&&r.results.length===6,'retrieval smoke');assert(temporalAudit(tiny).length===5,'temporal smoke');
 console.log('PASS: 4096 period identities; 10000 pair checks; retrieval and temporal smoke tests.');
}
if(process.argv.includes('--self-test'))selfTest();else{
 const arg=process.argv[2];let bytes;if(arg)bytes=await fs.readFile(arg);else{const res=await fetch(URL);if(!res.ok)throw Error('HTTP '+res.status);bytes=Buffer.from(await res.arrayBuffer())}
 const sha=createHash('sha1').update('blob '+bytes.length+'\0').update(bytes).digest('hex');if(sha!==SHA)throw Error('Source version mismatch: '+sha);
 const data=JSON.parse(bytes.toString('utf8'));if(data.train.length!==229||data.valid.length!==76||data.test.length!==77)throw Error('Unexpected corpus split');
 console.log(JSON.stringify({phase:'XVIII',source:URL,git_blob_sha1:sha,retrieval:audit(data),temporal:temporalAudit(data)},null,2));
}
