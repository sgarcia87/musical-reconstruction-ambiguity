import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';
const here=path.dirname(fileURLToPath(import.meta.url));
const arg=(name,def)=>{let i=process.argv.indexOf(name);return i<0?def:process.argv[i+1]};
const e=path.resolve(arg('--data','essen_data')),old=path.resolve(arg('--old-data','rgo_data'));
const selected=JSON.parse(execFileSync(process.execPath,[path.join(here,'graded_essen.mjs'),'--data',e,'--export-pitches'],{encoding:'utf8',maxBuffer:8*1024*1024}));
async function read(name,sha){const b=await fs.readFile(path.join(old,name));if(createHash('sha1').update('blob '+b.length+'\0').update(b).digest('hex')!==sha)throw Error('source hash mismatch '+name);return b.toString('utf8')}
const Braw=await read('jsb-chorales-quarter.json','ff93746647d1f5af2f719d235329c294267f3088'),Fraw=await read('thesession_subset_metadata_with_tune_family_annotation.csv','9f172a30b41b48398d6aa0b0e48b40b94bf093dc');
const source=await fs.readFile(path.join(here,'auditoria_repeticiones.mjs'),'utf8'),parseFolk=new Function(source.slice(source.indexOf('function parseFolk'),source.indexOf('const fact=[1n]'))+'\nreturn parseFolk')();
const word=a=>a.slice(1).map((x,i)=>(x-a[i]+12)%12).join(',');
const E=selected.map(r=>word(r.a)),B=Object.values(JSON.parse(Braw)).flat().map(p=>word(p.filter(n=>n.length).map(n=>Math.max(...n)%12)));
const {folk}=parseFolk(Fraw),F=folk.sort((a,b)=>Number(a.id)-Number(b.id)).filter((r,i,A)=>A.findIndex(x=>x.tune===r.tune)===i).map(r=>word(r.a.map(m=>Math.log2(m))));
function overlap(a,b){let s=new Set(b);return a.filter(x=>s.has(x)).length}
console.log(JSON.stringify({counts:[E.length,B.length,F.length],unique:[new Set(E).size,new Set(B).size,new Set(F).size],EssenBach:overlap(E,B),EssenSession:overlap(E,F),BachSession:overlap(B,F)},null,2));
