#!/usr/bin/env python3
"""Auditoría Q12 musical. Python 3.10+, sin dependencias externas.
Convención: Do=0, Do#=1,..., Si=11; filas módulo 3, columnas módulo 4.
Homología de Vietoris–Rips sobre F2, distancia Hamming.
"""
from itertools import combinations, product
from collections import Counter
from cmath import exp, pi
U=set(range(12))
rows=[[next(n for n in U if n%3==r and n%4==c) for c in range(4)] for r in range(3)]
H=[v for v in product((-1,1),repeat=4) if sum(v)==0]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
S=sorted({tuple(sorted(n for row,v in zip(rows,vs) for n,s in zip(row,v) if s==1)) for vs in product(H,repeat=3) if all(dot(a,b)==0 for a,b in combinations(vs,2))})
assert len(S)==48
R={'6-Z37':(0,1,2,3,4,8),'6-Z4':(0,1,2,4,5,6),'6-Z48':(0,1,2,5,7,9),'6-Z26':(0,1,3,5,7,8)}
def orbit(s):return {tuple(sorted((e*n+t)%12 for n in s)) for e in (-1,1) for t in range(12)}
label={s:k for k,r in R.items() for s in orbit(r)}
assert set(label)==set(S) and set(Counter(label.values()).values())=={12}
def iv(s):return tuple(sum(min((a-b)%12,(b-a)%12)==k for a,b in combinations(s,2)) for k in range(1,7))
profiles={iv(s) for s in R.values()}
assert {s for s in combinations(range(12),6) if iv(s) in profiles}==set(S)
print('Filas CRT:',rows,'Estados:',len(S))
for k,s in R.items():
 print(k,s,iv(s),'Potencia DFT k=1..6:',[round(abs(sum(exp(-2j*pi*j*n/12) for n in s))**2,6) for j in range(1,7)],'C:',label[tuple(sorted(U-set(s)))],'M5:',label[tuple(sorted(5*n%12 for n in s))])
X=[tuple(1 if n in s else -1 for n in range(12)) for s in S]
for i,j in product(range(12),repeat=2):
 assert sum(x[i]*x[j] for x in X)==(48 if i==j else -16 if i%3==j%3 else 0)
D=[[sum(a!=b for a,b in zip(x,y)) for y in X] for x in X]
print('Histograma por estado:',Counter(D[0]))
assert all(Counter(row)==Counter(D[0]) for row in D)
# Grafo de ortogonalidad: dos componentes K_{8,8,8}.
def components(nodes,adj):
 todo=set(nodes);out=[]
 while todo:
  stack=[todo.pop()];comp=set(stack)
  while stack:
   i=stack.pop();ns={j for j in todo if adj(i,j)};todo-=ns;comp|=ns;stack.extend(ns)
  out.append(comp)
 return out
comps=components(range(48),lambda i,j:D[i][j]==6)
assert sorted(map(len,comps))==[24,24]
for comp in comps:
 parts=components(comp,lambda i,j:D[i][j]!=6)
 assert sorted(map(len,parts))==[8,8,8]
 assert all(D[i][j]==6 for p,q in combinations(parts,2) for i in p for j in q)
print('Grafo ortogonal: 2 K(8,8,8). Operador de marco: 64 P, rango 9.')
# Distancia de conducción de voces L1 circular, asignación exacta DP.
def vl(a,b):
 dp={0:0}
 for x in a:
  new={}
  for mask,v in dp.items():
   for j,y in enumerate(b):
    if mask>>j&1:continue
    m=mask|1<<j;d=v+min((x-y)%12,(y-x)%12)
    new[m]=min(new.get(m,1000),d)
  dp=new
 return dp[(1<<len(b))-1]
E=[(i,j) for i,j in combinations(range(48),2) if vl(S[i],S[j])<=2]
assert len(E)==24 and all(vl(S[i],S[j])==2 for i,j in E)
print('Grafo voz L1 <=2:',len(E),'aristas; componentes:',Counter(map(len,components(range(48),lambda i,j:(min(i,j),max(i,j)) in E))))
# Comparación de tríadas y escalas, sin interpretar frecuencia en corpus.
for k,s in R.items():
 print(k,'triadas M,m,dim,aug:',[len({tuple(sorted((t+i)%12 for i in q)) for t in range(12) if {(t+i)%12 for i in q}<=set(s)}) for q in [(0,4,7),(0,3,7),(0,3,6),(0,4,8)]])
for name,scale in [('diatonica',(0,2,4,5,7,9,11)),('menor armonica',(0,2,3,5,7,8,11)),('menor melodica',(0,2,3,5,7,9,11)),('octatonica',(0,1,3,4,6,7,9,10)),('tonos',(0,2,4,6,8,10))]:
 allsubs={s for sc in orbit(scale) for s in combinations(sc,6)};matches=allsubs&set(S)
 print(name,'subconjuntos con T/I:',len(allsubs),'coincidencias:',len(matches),Counter(label[s] for s in matches))
# Rango exacto de matrices de frontera sobre F2 mediante enteros como bitsets.
def rank(cols):
 basis={}
 for v in cols:
  while v:
   p=v.bit_length()-1
   if p in basis:v^=basis[p]
   else:basis[p]=v;break
 return len(basis)
for t in (4,6):
 e=[s for s in combinations(range(48),2) if D[s[0]][s[1]]<=t]; EI={s:i for i,s in enumerate(e)}
 tr=[s for s in combinations(range(48),3) if all(x in EI for x in combinations(s,2))];TI={s:i for i,s in enumerate(tr)}
 q=[s for s in combinations(range(48),4) if all(x in TI for x in combinations(s,3))]
 r1=rank((1<<a)|(1<<b) for a,b in e);r2=rank(sum(1<<EI[x] for x in combinations(s,2)) for s in tr);r3=rank(sum(1<<TI[x] for x in combinations(s,3)) for s in q)
 b=(48-r1,len(e)-r1-r2,len(tr)-r2-r3);assert b==((1,13,6) if t==4 else (1,0,0))
 print('Rips',t,'simplices dimensiones 0..3:',(48,len(e),len(tr),len(q)),'Betti 0..2:',b)
# Para r=8 el grafo es K48 menos 24 pares antipodales: frontera del politopo cruzado de dim 24.
assert all(sum(d>8 for d in row)==1 for row in D)
print('Rips 8: esfera S^23. Rips 12: simplex completo. AUDITORIA OK')
