import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';
const here=path.dirname(fileURLToPath(import.meta.url));
const arg=(name,def)=>{let i=process.argv.indexOf(name);return i<0?def:process.argv[i+1]};
const root=path.resolve(arg('--data','essen_data')),lib=path.resolve(arg('--library','abcjs-basic-min.js'));
const sha='0631d3b91887d149458989f5b37b8f19c09dc725';
const bytes=await fs.readFile(lib);
if(createHash('sha1').update('blob '+bytes.length+'\0').update(bytes).digest('hex')!==sha)throw Error('abcjs blob hash mismatch');
const api=new Function('var module={exports:{}},exports=module.exports,window={},self=window;'+bytes.toString('utf8')+'\nreturn module.exports')();
const selected=JSON.parse(execFileSync(process.execPath,[path.join(here,'graded_essen.mjs'),'--data',root,'--export-pitches'],{encoding:'utf8',maxBuffer:8*1024*1024}));
const names=['altdeu10','ballad10','erk10','kinder0'],raw={};
for(let n of names){let s=await fs.readFile(path.join(root,n+'.abc'),'utf8');raw[n]=new Map(s.split(/(?=^X:)/m).filter(t=>t.startsWith('X:')).map(t=>[t.split(/\r?\n/)[0].slice(2).trim(),t]));}
const word=a=>a.slice(1).map((x,i)=>(x-a[i]+12)%12).join(',');
let agree=0,noteCount=0,intervalAgree=0,notes=0,warnings=0,errors=[],byCollection={};
for(let r of selected){let R=byCollection[r.collection]??={total:0,exact:0,intervalExact:0,noteCount:0};R.total++;notes+=r.a.length;let lines=raw[r.collection].get(r.x).split(/\r?\n/),idx=lines.findIndex(x=>/^K:/.test(x));let body=lines.slice(idx+1).map(l=>l.split('%')[0]).join('\n').replace(/:\|:|\|:|:\||::/g,'|').replace(/:/g,'');let abc=lines.slice(0,idx+1).join('\n')+'\n'+body;try{let t=api.parseOnly(abc)[0];if(t.warnings?.length)warnings++;let a=t.setUpAudio({}).tracks.flat().filter(e=>e.cmd==='note').sort((x,y)=>x.startChar-y.startChar).map(e=>(e.pitch%12+12)%12);if(a.length===r.a.length){noteCount++;R.noteCount++}if(word(a)===word(r.a)){intervalAgree++;R.intervalExact++}if(JSON.stringify(a)===JSON.stringify(r.a)){agree++;R.exact++}else errors.push({collection:r.collection,x:r.x,id:r.id,n:r.a.length,m:a.length,diff:a.findIndex((v,j)=>v!==r.a[j])})}catch(e){errors.push({collection:r.collection,x:r.x,error:String(e)})}}
console.log(JSON.stringify({abcjs:api.signature,blob:sha,n:selected.length,notes,agree,noteCount,intervalAgree,warnings,byCollection,errors},null,2));
if(errors.length||agree!==selected.length)process.exitCode=1;
