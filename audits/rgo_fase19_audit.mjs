#!/usr/bin/env node
// RGO XIX: exact small Vietoris-Rips persistence and music retrieval. Node >=18.
import fs from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
function audit(bachRaw,folkRaw) {
const pop=new Uint8Array(4096);for(let i=1;i<4096;i++)pop[i]=pop[i>>1]+(i&1);
const rot=(m,s)=>((m<<s)|(m>>(12-s)))&4095,mask=ns=>ns.reduce((x,n)=>x|1<<((n%12+12)%12),0);
const collapse=a=>a.filter((x,i)=>i===0||x!==a[i-1]);
const N=16, bins=16;
const pow=Array.from({length:4096},(_,m)=>Array.from({length:7},(_,k)=>pop[m&rot(m,k)]/12));
const euc=(x,y)=>Math.sqrt(x.reduce((s,a,i)=>s+(a-y[i])**2,0));
function points(a){let all=[];for(let i=0;i+3<=a.length;i++)all.push(a.slice(i,i+3));let n=Math.min(N,all.length);return Array.from({length:n},(_,i)=>all[Math.round(i*(all.length-1)/Math.max(1,n-1))]);}
function matrix(P,kind,time=false){const A=P.map(p=>p.flatMap(m=>pow[m]));return P.map((p,i)=>P.map((q,j)=>{let d;if(kind==="power")d=euc(A[i],A[j])/Math.sqrt(21);else{let min=Infinity;for(let s=0;s<12;s++)min=Math.min(min,p.reduce((a,m,k)=>a+pop[m^rot(q[k],s)],0));d=min/36}
return time?Math.hypot(d,0.25*Math.abs(i-j)/Math.max(1,P.length-1)):d;}))}
function barcode(D){
const n=D.length,edges=[],ix=Array.from({length:n},()=>Array(n).fill(-1));
for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)edges.push({i,j,d:D[i][j]});
edges.sort((a,b)=>a.d-b.d||a.i-b.i||a.j-b.j);
const parent=Array.from({length:n},(_,i)=>i),root=x=>{while(parent[x]!==x){parent[x]=parent[parent[x]];x=parent[x]}return x;};
let h0=[],h1=[],cycles=new Set();
edges.forEach((e,k)=>{ix[e.i][e.j]=ix[e.j][e.i]=k;let a=root(e.i),b=root(e.j);if(a!==b){parent[a]=b;h0.push([0,e.d])}else cycles.add(k);});
const tris=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)for(let k=j+1;k<n;k++){const a=ix[i][j],b=ix[i][k],c=ix[j][k];tris.push({max:Math.max(a,b,c),v:(1n<<BigInt(a))|(1n<<BigInt(b))|(1n<<BigInt(c))})}
tris.sort((a,b)=>a.max-b.max);
const piv=new Map();
for(const t of tris){let v=t.v;while(v){const k=v.toString(2).length-1;if(piv.has(k))v^=piv.get(k);else{piv.set(k,v);if(!cycles.has(k))throw Error("Triangle pivot not a cycle");const b=edges[k].d,d=edges[t.max].d;if(d-b>1e-10)h1.push([b,d]);cycles.delete(k);break}}}
if(cycles.size)throw Error("Unkilled H1 class in complete complex");
return {h0:h0.filter(p=>p[1]>1e-10),h1};
}
function pdSummary(B){let v=[];for(const key of ["h0","h1"]){const bars=B[key];for(let i=0;i<bins;i++){const lo=i*1.1/bins,hi=(i+1)*1.1/bins;v.push(bars.reduce((s,[b,d])=>s+Math.max(0,Math.min(hi,d)-Math.max(lo,b)),0)/(N-1)/(hi-lo));}v.push(bars.reduce((s,[b,d])=>s+d-b,0)/(N-1));v.push(Math.max(0,...bars.map(([b,d])=>d-b)));}return v;}
function hist(D){const v=Array(bins).fill(0);let n=0;for(let i=0;i<D.length;i++)for(let j=i+1;j<D.length;j++){v[Math.min(bins-1,Math.floor(D[i][j]/1.1*bins+1e-9))]++;n++;}return v.map(x=>x/Math.max(1,n))}
function ngram(a){let m=new Map();for(let i=2;i<a.length;i++){let best=Infinity;for(let s=0;s<12;s++)best=Math.min(best,rot(a[i-2],s)*16777216+rot(a[i-1],s)*4096+rot(a[i],s));m.set(best,(m.get(best)||0)+1)}const norm=Math.sqrt([...m.values()].reduce((s,x)=>s+x*x,0))||1;for(const [k,x]of m)m.set(k,x/norm);return m}
const dot=(a,b)=>{if(a.size>b.size)[a,b]=[b,a];let x=0;for(const [k,v]of a)x+=v*(b.get(k)||0);return x};
const methods=["power_hist","power_PH","joint_hist","joint_PH","time_joint_hist","time_joint_PH","joint_3gram","chroma_align"];
function feature(a){let P=points(a),D=matrix(P,"power"),J=matrix(P,"joint"),T=matrix(P,"joint",true);return {a,P,features:[hist(D),pdSummary(barcode(D)),hist(J),pdSummary(barcode(J)),hist(T),pdSummary(barcode(T))],ng:ngram(a)}}
function alignment(a,b){let best=0;for(let shift=0;shift<12;shift++){let prev=new Float64Array(b.length+1),cur=new Float64Array(b.length+1),mx=0;for(const m of a){let x=rot(m,shift);cur[0]=0;for(let j=1;j<=b.length;j++){let y=b[j-1],u=pop[x|y],sim=u?pop[x&y]/u:1;let v=Math.max(0,prev[j-1]+2*sim-1,prev[j]-.5,cur[j-1]-.5);cur[j]=v;mx=Math.max(mx,v)}let tmp=prev;prev=cur;cur=tmp}best=Math.max(best,mx)}return best/Math.max(1,Math.min(a.length,b.length));}
function scores(q,r,align=false){let s=q.features.map((v,i)=>-euc(v,r.features[i]));s.push(dot(q.ng,r.ng));if(align)s.push(alignment(q.a,r.a));return s;}
function ranks(ss,relevant){let pairs=ss.map((s,i)=>({s,r:relevant[i]})).sort((a,b)=>b.s-a.s);let first=0,ap=0,total=relevant.filter(Boolean).length,seen=0,k=0;while(k<pairs.length){let j=k+1;while(j<pairs.length&&Math.abs(pairs[j].s-pairs[k].s)<1e-10)j++;let n=j-k,h=pairs.slice(k,j).filter(p=>p.r).length;if(k===0)first=h/n;for(let a=1;a<=n;a++){let before=n>1?(a-1)*(h-1)/(n-1):0;if(h)ap+=(h/n)*(seen+1+before)/(k+a)}seen+=h;k=j}return {top1:first,ap:ap/total};}
function summary(queries,refs,eligible,relevant,doAlign=false){let out={},rows=[],chance=0;const use=methods.slice(0,doAlign?8:7);for(let m of use)out[m]={top1:0,ap:0};let count=0;for(let q of queries){const R=refs.filter(r=>eligible(q,r)),rel=R.map(r=>relevant(q,r));if(!rel.some(Boolean))continue;chance+=rel.filter(Boolean).length/rel.length;let S=use.map(()=>[]);for(let r of R)scores(q.f,r.f,doAlign).forEach((v,i)=>S[i].push(v));let row={id:q.id,family:q.family,methods:{}};for(let i=0;i<use.length;i++){let v=ranks(S[i],rel),m=use[i];out[m].top1+=v.top1;out[m].ap+=v.ap;row.methods[m]=v}rows.push(row);count++}
for(let m of use){out[m].top1/=count;out[m].ap/=count}return {count,chanceTop1:chance/count,methods:out,rows};}
const data=JSON.parse(bachRaw),refs=Object.entries(data).flatMap(([split,songs])=>songs.map((s,i)=>({id:split+"-"+i,split,a:collapse(s.map(mask))})));
for(let r of refs)r.f=feature(r.a);
function rng(seed){let s=seed>>>0;return ()=>{s=(Math.imul(s,1664525)+1013904223)>>>0;return s/4294967296}}
const B=[];let exactInvariant=0;
for(const cond of ["transposition","crop50","crop50_edit20"]){let qs=refs.filter(r=>r.split==="test").map((r,i)=>{let rand=rng(19000+i*101+(cond==="crop50_edit20"?77:0)),s=1+Math.floor(rand()*11),a=r.a.map(m=>rot(m,s));if(cond!=="transposition"){let len=Math.floor(a.length/2),start=Math.floor(rand()*(a.length-len+1));a=a.slice(start,start+len)}if(cond==="crop50_edit20"){a=a.filter(()=>rand()>=.1).map(m=>rand()<.2?m^(1<<Math.floor(rand()*12)):m);a=collapse(a)}const f=feature(a);if(cond==="transposition"){if(f.features.some((v,j)=>euc(v,r.f.features[j])>1e-9)||Math.abs(dot(f.ng,r.f.ng)-1)>1e-9)throw Error("transposition invariance");exactInvariant++}return {id:r.id,f}});B.push({condition:cond,...summary(qs,refs,()=>true,(q,r)=>q.id===r.id,false)})}
// Control: exact PH is invariant to relabelling the vertices; time augmented breaks many arbitrary permutations.
// Test square cycle with diagonals sqrt(2), and a simple transposition example.
let sq=barcode([[0,1,Math.SQRT2,1],[1,0,1,Math.SQRT2],[Math.SQRT2,1,0,1],[1,Math.SQRT2,1,0]]);
if(sq.h1.length!==1||Math.abs(sq.h1[0][0]-1)>1e-10||Math.abs(sq.h1[0][1]-Math.SQRT2)>1e-10)throw Error("square persistence");
let permCount=0,timeChanged=0,globalChanged=0;for(const r of refs.filter(x=>x.split==="test")){const P=r.f.P,idx=P.map((_,i)=>i),rr=rng(11+permCount);for(let i=idx.length-1;i>0;i--){let j=Math.floor(rr()*(i+1));[idx[i],idx[j]]=[idx[j],idx[i]];}let Q=idx.map(i=>P[i]);let old=matrix(P,"joint"),sh=matrix(Q,"joint");let sig=x=>pdSummary(barcode(x));if(euc(sig(old),sig(sh))>1e-9)throw Error("Unordered diagram mismatch");permCount++;timeChanged+=+(euc(sig(matrix(P,"joint",true)),sig(matrix(Q,"joint",true)))>1e-9);globalChanged+=+(P.map(x=>x.join(",")).join("|")!==Q.map(x=>x.join(",")).join("|"))}
function csv(s){let rows=[],row=[],cell="",q=false;for(let i=0;i<s.length;i++){let c=s[i];if(q){if(c==='"'&&s[i+1]==='"'){cell+='"';i++}else if(c==='"')q=false;else cell+=c}else if(c==='"')q=true;else if(c===","){row.push(cell);cell=""}else if(c==="\n"){row.push(cell.replace(/\r$/,""));rows.push(row);row=[];cell=""}else cell+=c}if(cell||row.length){row.push(cell);rows.push(row)}if(q)throw Error("unclosed CSV quote");return rows}
const signature={C:0,G:1,D:2,A:3,E:4,B:5,"F#":6,"C#":7,F:-1,Bb:-2,Eb:-3,Ab:-4,Db:-5,Gb:-6,Cb:-7};
const minor={A:"C",E:"G",B:"D","F#":"A","C#":"E","G#":"B",D:"F",G:"Bb",C:"Eb",F:"Ab",Bb:"Db",Eb:"Gb"};
const dor={D:"C",A:"G",E:"D",B:"A","F#":"E","C#":"B",G:"F",C:"Bb",F:"Eb",Bb:"Ab"};
const mix={G:"C",D:"G",A:"D",E:"A",B:"E",C:"F",F:"Bb",Bb:"Eb",Eb:"Ab"};
function parseABC(key,body){let km=key.trim().match(/^([A-G][#b]?)\s*(major|minor|dorian|mixolydian|maj|min|dor|mix)?$/i);if(!km)return {error:"unsupported_key"};let tonic=km[1][0].toUpperCase()+km[1].slice(1),mode=(km[2]||"major").toLowerCase();let major=mode.startsWith("min")?minor[tonic]:mode.startsWith("dor")?dor[tonic]:mode.startsWith("mix")?mix[tonic]:tonic;let sig=signature[major];if(sig===undefined)return {error:"unsupported_key"};
let bodyStart=body.match(/\bR:\S+\s+/);if(!bodyStart)return {error:"missing_R_header"};let a=body.slice(bodyStart.index+bodyStart[0].length).replace(/"[^"]*"/g,"").replace(/\{[^}]*\}/g,"").replace(/![^!]*!/g,"").replace(/\+[^+]*\+/g,"");
if(/\[(?![0-9|])/.test(a)||/(?:^|\s)[KMLQV]:/.test(a))return {error:"polyphony_or_inline_header"};
const keyAcc={},letters=sig>0?"FCGDAEB":"BEADGCF";for(let i=0;i<Math.abs(sig);i++)keyAcc[letters[i]]=Math.sign(sig);let acc={},ns=[];
const base={C:0,D:2,E:4,F:5,G:7,A:9,B:11};
const re=/\||(\^{1,2}|_{1,2}|=)?([A-Ga-g])([,']*)|[zZxX]/g;for(const m of a.matchAll(re)){if(m[0]==="|"){acc={};continue}if(!m[2])continue;let note=m[2],L=note.toUpperCase(),oct=(note===L?0:1)+[...(m[3]||"")].reduce((s,c)=>s+(c==="'"?1:-1),0),id=L+oct;if(m[1])acc[id]=m[1]==="="?0:(m[1][0]==="^"?1:-1)*m[1].length;let n=base[L]+12*oct+(acc[id]??keyAcc[L]??0);ns.push(1<<((n%12+12)%12))}return ns.length>=16?{a:ns}:{error:"too_short"};}
const table=csv(folkRaw),header=table.shift(),col=Object.fromEntries(header.map((h,i)=>[h,i])),excluded={},folk=[];
for(let r of table){if(r.length!==header.length){excluded.csv=(excluded.csv||0)+1;continue}const id=r[col.identifiers],tune=r[col.N].match(/tune id:\s*(\d+)/)?.[1],family=r[col.tune_family],x=parseABC(r[col.K],r[col.abc_score]);if(x.error||!tune||!family){let k=x.error||"metadata";excluded[k]=(excluded[k]||0)+1;continue}folk.push({id,tune,family,a:x.a})}
for(const r of folk)r.f=feature(r.a);
// Use only the fixed features for all queries, including every other eligible setting; same-ID and different-ID tasks are separated.
const F1=summary(folk,folk,(q,r)=>q.id!==r.id,(q,r)=>q.tune===r.tune,false),F2=summary(folk,folk,(q,r)=>q.tune!==r.tune,(q,r)=>q.family===r.family,false);
// strong alignment control only on deterministic first (lexicographic numeric) setting per tune id,
// all other distinct tune representatives as references; both endpoints are independent settings.
const reps=[...new Map(folk.slice().sort((a,b)=>Number(b.id)-Number(a.id)).map(r=>[r.tune,r])).values()].sort((a,b)=>Number(a.id)-Number(b.id));
const F3=summary(reps,reps,(q,r)=>q.tune!==r.tune,(q,r)=>q.family===r.family,true);
const meta={sourceRows:table.length,usable:folk.length,tuneIds:new Set(folk.map(x=>x.tune)).size,families:new Set(folk.map(x=>x.family)).size,excluded,settingsPerFamily:Object.fromEntries([...new Set(folk.map(x=>x.family))].sort().map(k=>[k,folk.filter(x=>x.family===k).length])),representatives:reps.length,parser:"Conservative subset ABC: pitch classes only, key signatures and explicit bar-local accidentals; skip chords/inline headers and unsupported keys, omit durations, grace notes, ornaments and rests, notate repeats as written (no expansion). No labels used in feature extraction."};
return {phase:"XIX",protocol:{sampledWindows:N,windowEvents:3,bins,metrics:"Normalized autocorrelation Euclidean pseudometric; joint Hamming quotient metric; latter plus 0.25 normalized time by Euclidean product. Exact Rips H0/H1 on <=16 points, positive finite bars (infinite H0 omitted), discretized integral Betti and lifetime summaries; same matrices' distance histograms, direct invariant trigram cosine, optional all-transposition local chroma alignment. Fixed rules, no tuning.",bach:"All 382 references, official 77 test pieces with deterministic synthetic changes; different random draws than XVIII.",folk:"Independently contributed symbolic settings, same tune IDs or annotated tune families, no self match. Different-tune family test excludes all same-ID settings. One representative per ID chosen by smallest numeric setting ID, separately aligned. No audio/timbre test."},selfTest:{squareH1:sq.h1,exactInvariant,shuffledPointClouds:permCount,changedWindowOrder:globalChanged,unorderedPHIdentical:permCount,timeAugmentedPHChanged:timeChanged},bach:B,folk:{meta,sameTune:F1,differentTuneSameFamily:F2,representatives:F3}};
}
const sources=[{"repo":"czhuang/JSB-Chorales-dataset","path":"jsb-chorales-quarter.json","ref":"master","sha":"ff93746647d1f5af2f719d235329c294267f3088"},{"repo":"polifonia-project/folk_ngram_analysis","path":"FoNN/SIATEC_comparison/data/thesession_subset_metadata_with_tune_family_annotation.csv","ref":"master","sha":"9f172a30b41b48398d6aa0b0e48b40b94bf093dc"}];
const i=process.argv.indexOf('--data'),root=i<0?'rgo_data':process.argv[i+1];await fs.mkdir(root,{recursive:true});
const raw=await Promise.all(sources.map(async s=>{let f=path.join(root,path.basename(s.path)),b;try{b=await fs.readFile(f)}catch(e){if(e.code!=='ENOENT')throw e;const r=await fetch('https://raw.githubusercontent.com/'+s.repo+'/'+s.ref+'/'+s.path);if(!r.ok)throw Error(r.status+' '+s.path);b=Buffer.from(await r.arrayBuffer());await fs.writeFile(f,b);}const sha=createHash('sha1').update('blob '+b.length+'\0').update(b).digest('hex');if(sha!==s.sha)throw Error('Source hash mismatch '+s.path);return b.toString('utf8')}));
console.log(JSON.stringify({sources,...audit(...raw)},null,2));
