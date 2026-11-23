#!/usr/bin/env python3
"""HD-S36 exact simply-laced normalizer data.
GPT-6 Astra Pro, /root/sixfolds, inherited effort not exposed, 2026-11-21.
This reconstructs roots, diagrams and a literal longest-element word.
"""
from itertools import permutations
from pathlib import Path
from fractions import Fraction as F
import json
import sympy as sp
out={}
for r,expected in [(6,72),(7,126),(8,240)]:
 H=[[2*int(i==j) for j in range(r)] for i in range(r)]
 edges=[(0,2),(2,3),(3,4),(4,5),(5,6),(6,7),(1,3)]
 for i,j in edges:
  if max(i,j)<r:H[i][j]=H[j][i]=-1
 eye=[tuple(int(i==j) for i in range(r)) for j in range(r)]
 roots=list(eye);seen=set(roots)
 for v in roots:
  for j in range(r):
   w=list(v);w[j]-=sum(H[j][k]*v[k] for k in range(r));w=tuple(w)
   if w not in seen:seen.add(w);roots.append(w)
 assert len(roots)==expected
 assert all(sum(v[i]*H[i][j]*v[j] for i in range(r) for j in range(r))==2 for v in roots)
 assert all(all(x>=0 for x in v) or all(x<=0 for x in v) for v in roots)
 autos=[p for p in permutations(range(r)) if all(H[i][j]==H[p[i]][p[j]] for i in range(r) for j in range(r))]
 assert len(autos)==(2 if r==6 else 1)
 hs=sp.Matrix(H);rho=[F(x) for x in hs.inv()*sp.ones(r,1)]
 x=[-a for a in rho];w0=[list(row) for row in eye];word=[]
 while True:
  pair=[sum(H[j][k]*x[k] for k in range(r)) for j in range(r)]
  bad=[j for j in range(r) if pair[j]<0]
  if not bad:break
  j=bad[0];x[j]-=pair[j]
  newrow=[w0[j][k]-sum(H[j][l]*w0[l][k] for l in range(r)) for k in range(r)]
  w0[j]=newrow;word.append(j+1)
  assert len(word)<=expected//2
 assert x==rho and len(word)==expected//2
 P=[[-a for a in row] for row in w0]
 assert all(sum(row)==1 and set(row)<={0,1} for row in P)
 perm=tuple(next(j for j in range(r) if P[i][j]) for i in range(r))
 assert perm in autos
 if r==6:
  assert perm==(5,1,4,3,2,0)
  assert hs.det()==3
  y=hs.inv()[:,0]
  assert any(v.q==3 for v in y) and any((2*v).q==3 for v in y)
 else:assert perm==tuple(range(r))
 out[f'E{r}']={'rank':r,'root_count':len(roots),'Cartan_determinant':int(hs.det()),
   'all_root_coordinates_same_sign':True,'diagram_automorphisms':[[j+1 for j in p] for p in autos],
   'minus_longest_element_permutation':[j+1 for j in perm],
   'left_applied_simple_reflection_word':word,
   'word_matrix':w0,'Cartan_matrix':H}
out['status']='PASS'
out['scope']='Exact root/diagram matrices and words. The universal block, moduli, and Jacobian maps are proved in the accompanying HD-S36 text.'
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
