#!/usr/bin/env python3
"""Actual positive-rank free compensation with the E825 determinant exactly met.
This is not a semiregular seed. A nonzero global extension is certified by
an exact cohomological dimension lower bound, not by an Ext matrix rank.
"""
from pathlib import Path
from itertools import product
from functools import reduce
from math import lcm
import time,json
import sympy as s
from sympy.polys.matrices import DomainMatrix
start=time.perf_counter();root=Path(__file__).resolve().parent
u=s.sqrt(2);K=s.QQ.algebraic_field(u);signs=list(product((-1,1),repeat=4))
D=4;unit_twist=14;total_normalized_rank=32;q=s.Rational(1,2)
def coeff(v):return s.Matrix([s.prod(v[i] for i in range(4) if(mask>>i)&1) for mask in range(16)])
def mult(a,b):
 out=[s.S.Zero]*16
 for i in range(16):
  for j in range(16):
   if not i&j:out[i|j]+=a[i]*b[j]
 return s.Matrix([s.expand(x) for x in out])
def lam(v):
 a,b,c,d=v
 return [a+b*u+c+d*u,a+b*u-c-d*u,a-b*u+c-d*u,a-b*u-c+d*u]
def nearest(v):return int(s.floor(v+s.Rational(1,2)))
vq=s.zeros(16,1);vq[0]=1;vq[3]=vq[12]=-q;vq[15]=q*q
F=2*coeff([-D]*4)-2*coeff([-3*D]*4)+coeff([-4*D]*4)
G=mult(coeff([unit_twist]*4),F)
assert G==2*coeff([unit_twist-D]*4)-2*coeff([unit_twist-3*D]*4)+coeff([unit_twist-4*D]*4)
target=total_normalized_rank*vq-G
trials=[];found=None
for R in (8,16,32,64):
 divisors=[];columns=[]
 for eps in signs:
  v=[R*x for x in eps]
  div=[nearest(sum(v)/s.Integer(4)),nearest((v[0]+v[1]-v[2]-v[3])/(4*u)),nearest((v[0]-v[1]+v[2]-v[3])/s.Integer(4)),nearest((v[0]-v[1]-v[2]+v[3])/(4*u))]
  divisors.append(div);columns.append(coeff(lam(div)))
 M=s.Matrix.hstack(*columns)
 DM=DomainMatrix.from_Matrix(M).convert_to(K)
 DT=DomainMatrix.from_Matrix(target).convert_to(K)
 weights=[s.simplify(x) for x in (DM.inv()*DT).to_Matrix()]
 assert all(x.is_Rational for x in weights)
 assert all(s.simplify(x)==0 for x in M*s.Matrix(weights)-target)
 positive=all(x>0 for x in weights)
 trials.append({'scale':R,'positive':bool(positive),'minimum_weight':str(min(weights))})
 if not positive:continue
 r=reduce(lcm,(int(w.q) for w in weights),1)
 ns=[int(r*w) for w in weights];Rtot=total_normalized_rank*r
 assert sum(ns)==Rtot-r and min(ns)>0
 assert all(s.expand(x)==0 for x in r*G+M*s.Matrix(ns)-Rtot*vq)
 candidates=[]
 for div,n in zip(divisors,ns):
  eig=[unit_twist-z for z in lam(div)]
  dims=[];indices=[]
  for a in (1,3,4):
   vals=[z-a*D for z in eig]
   idx=sum(bool(z<0) for z in vals);indices.append(idx)
   val=s.simplify((-1)**idx*s.prod(vals));assert val.is_Integer
   dims.append(int(val))
  if indices==[1,1,1]:
   lower=2*dims[0]-2*dims[1]
   if lower>0:
    all_indices=[sum(bool(z-j*D<0) for z in eig) for j in range(6)]
    dual_indices=[sum(bool(4*D-z-j*D<0) for z in eig) for j in range(3)]
    assert all_indices==[1]*6 and dual_indices==[3]*3
    h1A=int(s.simplify(-s.prod(eig)))
    hull_lower=(h1A+4)//5
    candidates.append({'free_divisor':div,'multiplicity':n,'line_indices_for_resolution_terms':indices,'h1_line_dimensions':dims,'Ext1_lower_bound':lower,'difference_eigenvalues':[str(z) for z in eig],
                       'five_section_Koszul_indices':all_indices,'dual_surface_Koszul_indices':dual_indices,'h1_of_hull_difference':h1A,'nonzero_hull_parameter_rank_lower_bound':hull_lower})
 assert candidates
 found={'scale':R,'defect_rank':r,'free_rank':sum(ns),'total_rank':Rtot,'D_theta_coefficient':D,'unit_twist_theta_coefficient':unit_twist,'q':str(q),'normalized_total_rank_per_unit':total_normalized_rank,
        'defect_determinant_theta_coefficient':unit_twist*r,'required_7rD_over_2_theta_coefficient':int(s.Rational(7,2)*r*D),
        'summands':[{'coefficients':div,'multiplicity':n,'weight_per_unit':str(w)} for div,n,w in zip(divisors,ns,weights)],
        'unit_character_subset_coefficients':[str(x) for x in G],'balanced_subset_coefficients':[str(x) for x in vq],
        'nonzero_extension_candidates':candidates}
 break
assert found
out={'result':'PASS','runtime_seconds':time.perf_counter()-start,'trials':trials,'construction':found,
     'limits':'The starting sheaf is an actual direct sum of twisted unit modules and integral-divisor line bundles. A nonzero Ext1 guarantees a genuine nonsplit global coherent extension preserving the complete character, local form and defect determinant. Remaining direct summands, simplicity, finite action and semiregularity are not eliminated or asserted.'}
(root/'rm_positive_defect_compensation_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'result':'PASS','runtime_seconds':out['runtime_seconds'],'trials':trials,'defect_rank':found['defect_rank'],'total_rank':found['total_rank'],'extension_candidates':found['nonzero_extension_candidates']},indent=2))
