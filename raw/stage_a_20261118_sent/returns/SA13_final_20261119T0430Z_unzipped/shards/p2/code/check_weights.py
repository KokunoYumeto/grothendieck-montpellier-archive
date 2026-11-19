#!/usr/bin/env python3
"""Exact symbolic checks for the independent K34-12 audit, not a theorem prover."""
import json
from pathlib import Path
from math import comb
import sympy as s

p,q,r,d,Q=s.symbols('p q r d Q', integer=True)
cech=s.expand(q-r+1-q)
leray=s.expand(p+r+2*(q-r+1)-(p+2*q))
support=s.expand(p+r+2*(q-r+1)-2-(p+2*q-2))
assert cech==1-r and leray==2-r and support==2-r
gysin=s.Matrix([[1,1]])
assert gysin.rank()==1 and len(gysin.nullspace())==1
left_degree=2*(d-q)-p
right_degree=2*(d-(q-1))-(p+2)
assert s.simplify(left_degree-right_degree)==0
assert (d-q)+q==d and (d-(q-1))+(q-1)==d
F=s.diag(1,Q); N=s.Matrix([[0,1],[0,0]])
assert N*N==s.zeros(2)
assert s.simplify(F*N*F.inv()-N/Q)==s.zeros(2)
assert N.nullspace()==[s.Matrix([1,0])]
assert N.columnspace()==[s.Matrix([1,0])]
assert F*s.Matrix([1,0])==s.Matrix([1,0])
assert F*s.Matrix([0,1])==Q*s.Matrix([0,1])
rows=[]
for branches in range(1,7):
 for degree in range(branches+1):
  rows.append({'branches':branches,'degree':degree,
   'arithmetic_Rj_rank':comb(branches,degree),
   'geometric_nearby_rank':comb(branches-1,degree) if degree<=branches-1 else 0})
out={'status':'all assertions passed','cech_target_minus_source_weight':str(cech),
 'leray_target_minus_source_weight':str(leray),'support_target_minus_source_weight':str(support),
 'Gm_in_P1_d2':{'matrix':[[1,1]],'rank':1,'kernel_dimension':1,'cokernel_dimension':0},
 'duality_degrees':{'source':str(s.expand(left_degree)),'target':str(s.expand(right_degree)),'common_twist':'d'},
 'local_ranks':rows,'Tate_curve':{'F':[['1','0'],['0','Q']],'N':[[0,1],[0,0]],
  'FNF_inverse':'Q^(-1) N','invariants_eigenvalue':'1','coinvariants_eigenvalue':'Q',
  'invariants_weight':0,'coinvariants_weight':2,'cohomology_degree':1},
 'scope':'Exact linear algebra and index identities. The geometric inputs are separately cited and explained in weights_audit.md.'}
path=Path(__file__).resolve().parents[1]/'outputs'/'weights_computations.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'output':str(path)}))
