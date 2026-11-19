#!/usr/bin/env python3
"""Independent finite check of A-012 at q=w=m=2 over F2 on sk_4 B(C2)."""
import itertools,json,time
from pathlib import Path
import sympy as sp
start=time.perf_counter();checks=0
verts=range(5)
cuts=list(itertools.combinations(range(1,5),2))
def z(i,j,k):return ((j-i)%2)*((k-j)%2)
for f in itertools.combinations(verts,4):
 assert sum(z(*f[:i],*f[i+1:]) for i in range(4))%2==0
 checks+=1
A=sp.Matrix([[int(c1<=j1<c2<=j2) for c1,c2 in cuts] for j1,j2 in cuts])
assert A.det()==1;checks+=1
rhs=sp.Matrix([z(0,j1,j2) for j1,j2 in cuts])
u=[int(x)%2 for x in A.inv()*rhs]
assert u==[1]*6;checks+=1
form={}
for coeff,(c1,c2) in zip(u,cuts):
 for i in range(c1,c2):
  for j in range(c2,5):
   mask=(1<<(i-1))|(1<<(j-1))
   form[mask]=(form.get(mask,0)+coeff)%2
form={m:a for m,a in form.items() if a}
assert form=={3:1,9:1,12:1};checks+=1
gamma={}
for (a,x),(b,y) in itertools.combinations(form.items(),2):
 if not a&b:gamma[a|b]=(gamma.get(a|b,0)+x*y)%2
assert gamma.get(15,0)==1;checks+=1
result={'statement':'A-012','finite_X':'sk_4 B(C2)','coefficient_ring':'F2',
 'q':2,'w':2,'m':2,'orientation_coordinate_matrix':[list(map(int,A.row(i))) for i in range(A.rows)],
 'ordinary_cocycle_values':[int(x) for x in rhs], 'degeneracy_coefficients_mod2':u,
 'lifted_2form_nonzero_masks':form,'divided_square_top_coefficient':gamma[15],
 'interpretation':'gamma2 of the weight2 class x^2 has nonzero degree4 component; no factorial cancellation used',
 'assertions_passed':checks,'elapsed_seconds':time.perf_counter()-start}
p=Path(__file__).resolve().parents[1]/'logs/D_A3_cocycle_check.json'
p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
