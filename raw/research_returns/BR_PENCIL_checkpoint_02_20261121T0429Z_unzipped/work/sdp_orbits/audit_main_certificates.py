"""Independent verification of root's j=5 coordinate Koszul certificate.
Orbit coverage uses BFS in seven generators, not the generator's full group table.
Matrices/minors are rebuilt here; no import of the generating implementation.
"""
from pathlib import Path
from itertools import combinations
import math,json,time,sys
import numpy as np

ROOT=Path(__file__).resolve().parents[1]/'root'
J=int(sys.argv[1]) if len(sys.argv)>1 else 5
DATA=json.loads((ROOT/f'j{J}.json').read_text())
P=1000003
assert P>1 and all(P%d for d in range(2,math.isqrt(P)+1))
PAIRS=list(combinations(range(4),2))
R=[(x,y) for x in PAIRS for y in PAIRS]
RI={r:i for i,r in enumerate(R)}
# Adjacent row/column transpositions, and transpose, generate the full group.
gens=[]
for axis in [0,1]:
 for z in range(3):
  trans=list(range(4));trans[z],trans[z+1]=trans[z+1],trans[z]
  mp=[]
  for row,col in R:
   pair=[row,col];pair[axis]=tuple(sorted(trans[v] for v in pair[axis]))
   mp.append(RI[tuple(pair)])
  gens.append(mp)
gens.append([RI[(col,row)] for row,col in R])
seen=set(); checked=0; minb={'det':99,'per':99}; minors=0; smallest_minor=None

def detmod(M,p):
 M=np.array(M,dtype=np.int64,copy=True)%p
 n=M.shape[0];assert M.shape==(n,n)
 determinant=1
 for c in range(n):
  piv=next((i for i in range(c,n) if M[i,c]),None)
  if piv is None:return 0
  if piv!=c:
   M[[piv,c]]=M[[c,piv]];determinant=-determinant
  val=int(M[c,c]);determinant=determinant*val%p
  inv=pow(val,p-2,p)
  # Keep unnormalized pivot row. Vectorized row eliminations with bounded int64 products.
  fac=(M[c+1:,c]*inv)%p
  M[c+1:,c:]=(M[c+1:,c:]-fac[:,None]*M[c,c:])%p
 return determinant%p

def matrix_for(subset,sgn,p,support):
 j=len(subset);m=len(support);ix={x:i for i,x in enumerate(support)}
 source=list(combinations(range(j),p));target=list(combinations(range(j),p+1));dest={x:i for i,x in enumerate(target)}
 M=np.zeros((len(target)*m,len(source)*m),dtype=np.int64)
 for a,rect in enumerate(subset):
  (r,s),(c,d)=R[rect]
  entries=[(4*r+c,4*s+d,1),(4*s+d,4*r+c,1),(4*r+d,4*s+c,sgn),(4*s+c,4*r+d,sgn)]
  for col,I in enumerate(source):
   if a in I:continue
   J=tuple(sorted(I+(a,)));row=dest[J];sign=1 if sum(i<a for i in I)%2==0 else -1
   for x,y,v in entries:M[row*m+ix[x],col*m+ix[y]]=sign*v
 return M

start=time.time()
for rec in DATA['records']:
 subset=tuple(rec['subset']);assert len(set(subset))==J and tuple(sorted(subset))==subset
 assert subset not in seen
 orb={subset};front=[subset]
 while front:
  cur=front.pop()
  for mp in gens:
   nxt=tuple(sorted(mp[i] for i in cur))
   if nxt not in orb:orb.add(nxt);front.append(nxt)
 assert len(orb)==rec['orbit_size']
 assert not seen.intersection(orb)
 seen.update(orb)
 support=sorted({4*x+y for i in subset for x in R[i][0] for y in R[i][1]})
 assert support==rec['support'] and len(support)==rec['support_bound']
 for family,sgn in [('det',-1),('per',1)]:
  lower=max(J,len(support))
  for cert in rec['families'][family]['koszul']:
   p=cert['p'];assert cert['prime']==P
   M=matrix_for(subset,sgn,p,support)
   assert list(M.shape)==cert['shape']
   rows=cert['rows'];cols=cert['cols'];r=cert['rank_mod_p']
   assert len(rows)==len(set(rows))==len(cols)==len(set(cols))==r
   minor=M[np.ix_(rows,cols)]
   determinant=detmod(minor,P)
   assert determinant!=0
   assert determinant==cert['pivot_product_mod_p']
   cost=math.comb(J-1,p);assert cost==cert['pure_cost']
   bound=(r+cost-1)//cost;assert bound==cert['bound']
   lower=max(lower,bound);minors+=1
  assert lower==rec['families'][family]['lower_bound']
  minb[family]=min(minb[family],lower)
 checked+=1
assert len(seen)==math.comb(36,J)==DATA['number_of_subsets']==DATA['orbit_sum']
assert checked==DATA['number_of_orbits']
assert minb==DATA['minimum_certified']
out={'j':J,'result':'PASS','independent_orbit_BFS':True,'orbits_verified':checked,'subsets_covered':len(seen),'certified_minors_verified':minors,'prime_trial_division':P,'minimum_bounds':minb,'seconds':time.time()-start}
Path(__file__).with_name('main_certificate_audit.json' if J==5 else f'main_j{J}_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
