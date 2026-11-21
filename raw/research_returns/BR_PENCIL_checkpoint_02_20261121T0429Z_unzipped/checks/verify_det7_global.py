#!/usr/bin/env python3
"""Independently check the 25 Borel ideals and all non-prolongation det7 minors.

The separate P-09/P-12/P-14/P-15 proofs/certificates are explicit dependencies.
This program never imports the search or certificate-generation routines.
"""
from itertools import combinations
from pathlib import Path
from collections import Counter
import json,math
import numpy as np
PAIRS=list(combinations(range(4),2))
RECTS=[(I,J) for I in PAIRS for J in PAIRS]

def detmod(matrix,p):
 a=np.array(matrix,dtype=np.int64,copy=True)%p
 n=a.shape[0];assert a.shape==(n,n);value=1
 for k in range(n):
  nz=np.flatnonzero(a[k:,k])
  if not len(nz):return 0
  j=k+int(nz[0])
  if j!=k:a[[j,k]]=a[[k,j]];value=-value
  pivot=int(a[k,k]);value=value*pivot%p
  a[k,k:]=a[k,k:]*pow(pivot,-1,p)%p
  ids=np.flatnonzero(a[k+1:,k])+k+1
  if len(ids):a[ids,k:]=(a[ids,k:]-a[ids,k,None]*a[k,k:])%p
 return value%p

def all_ideals(size):
 def below(q,z):
  I,J=RECTS[q];K,L=RECTS[z]
  return all(a<=b for a,b in zip(I,K)) and all(a<=b for a,b in zip(J,L))
 lower=[sum(1<<q for q in range(36) if q!=z and below(q,z)) for z in range(36)]
 layer={0}
 for _ in range(size):
  layer={mask|(1<<z) for mask in layer for z in range(36) if not(mask>>z&1) and lower[z]&mask==lower[z]}
 return {tuple(z for z in range(36) if mask>>z&1) for mask in layer}

def tensor(S):
 support=sorted({4*r+c for z in S for r in RECTS[z][0] for c in RECTS[z][1]})
 pos={v:i for i,v in enumerate(support)};T={}
 for h,z in enumerate(S):
  (r,s),(c,d)=RECTS[z]
  a,b,x,y=[pos[v] for v in [4*r+c,4*r+d,4*s+c,4*s+d]]
  for u,v,value in [(a,y,1),(y,a,1),(b,x,-1),(x,b,-1)]:T[h,u,v]=value
 return support,T

def koszul_minor(S,support,T,along,p,rows,cols):
 m=len(support);j=len(S);d=j if along=='A' else m
 src=list(combinations(range(d),p));dst=list(combinations(range(d),p+1))
 def entry(row,col):
  if along=='A':
   J,u=dst[row//m],row%m;I,v=src[col//m],col%m
   if not set(I)<=set(J):return 0
   h=next(x for x in J if x not in I)
   return (-1)**sum(i<h for i in I)*T.get((h,u,v),0)
  J,h=dst[row//j],row%j;I,v=src[col//m],col%m
  if not set(I)<=set(J):return 0
  u=next(x for x in J if x not in I)
  return (-1)**sum(i<u for i in I)*T.get((h,u,v),0)
 return [[entry(row,col) for col in cols] for row in rows]

def main():
 path=Path(__file__).with_name('det7_global_certificate.json');data=json.loads(path.read_text());prime=data['prime']
 assert prime==1000003 and all(prime%d for d in range(2,math.isqrt(prime)+1))
 ideals=all_ideals(7);assert len(ideals)==25
 actual=[tuple(r['subset']) for r in data['records']];assert len(set(actual))==25 and set(actual)==ideals
 expected={}
 reps={'P-09':[[0,1,3,6,7,9,12],[0,1,3,6,7,12,13]],'P-12':[[0,1,2,3,6,7,8],[0,1,2,3,4,6,12]],'P-14':[[0,1,2,3,6,7,9],[0,1,2,3,6,7,18]],'P-15':[[0,1,3,6,7,9,18]]}
 for label,subsets in reps.items():
  for S in subsets:
   expected[tuple(S)]=label;expected[tuple(sorted((q%6)*6+q//6 for q in S))]=label
 counts=Counter();minor_count=0
 for rec in data['records']:
  S=rec['subset'];support,T=tensor(S);m=len(support);assert support==rec['support'];kind=rec['type'];counts[kind]+=1
  if kind=='support':
   assert m>=14
   pairs=[next((h,u) for h in range(7) for u in range(m) if T.get((h,u,v))) for v in range(m)]
   assert len(set(pairs))==m
   minor=[[T.get((h,u,v),0) for v in range(m)] for h,u in pairs]
   assert detmod(minor,prime) in (1,prime-1);minor_count+=1
  elif kind=='A_koszul':
   p=rec['p'];cost=math.comb(6,p);assert cost==rec['cost']
   rows,cols=rec['rows'],rec['cols'];n=rec['minor_order']
   assert len(set(rows))==len(set(cols))==n>13*cost
   value=detmod(koszul_minor(S,support,T,'A',p,rows,cols),prime)
   assert value==rec['determinant_mod_p']!=0;minor_count+=1
  elif kind=='B_koszul':
   p=rec['p'];cost=math.comb(m-1,p);assert cost==rec['cost']
   src=list(combinations(range(m),p));dst=list(combinations(range(m),p+1))
   weights=[32**(v//4)+32**(4+v%4) for v in support]
   aw=[sum(32**i for i in RECTS[z][0])+sum(32**(4+i) for i in RECTS[z][1]) for z in S]
   # The displayed tensor respects the grading; distinct numerical weights
   # are honest torus-character separations for these bounded digit ranges.
   assert all(weights[u]+weights[v]==aw[h] for h,u,v in T)
   seen_rows=set();seen_cols=set();seen_weights=set();total=0
   for c in rec['blocks']:
    rows,cols,n,w=c['rows'],c['cols'],c['size'],c['weight']
    assert len(set(rows))==len(set(cols))==n
    assert not(seen_rows&set(rows)) and not(seen_cols&set(cols)) and w not in seen_weights
    assert all(sum(weights[u] for u in dst[row//7])-aw[row%7]==w for row in rows)
    assert all(sum(weights[u] for u in src[col//m])-weights[col%m]==w for col in cols)
    value=detmod(koszul_minor(S,support,T,'B',p,rows,cols),prime)
    assert value==c['determinant_mod_p']!=0
    seen_rows.update(rows);seen_cols.update(cols);seen_weights.add(w);total+=n;minor_count+=1
   assert total==rec['rank_lower_bound']>13*cost
  else:
   assert kind=='prolongation' and rec['finding']==expected[tuple(S)]
  assert rec['lower_bound']>=14
 out={'status':'PASS','Borel_ideals_covered':25,'case_types':dict(counts),'exact_modular_minors_verified':minor_count,'prolongation_dependencies':['P-09','P-12','P-14','P-15'],'scope':'Coverage and Koszul/support certificates verified here; listed prolongation proofs are checked separately.'}
 path.with_name('det7_global_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
