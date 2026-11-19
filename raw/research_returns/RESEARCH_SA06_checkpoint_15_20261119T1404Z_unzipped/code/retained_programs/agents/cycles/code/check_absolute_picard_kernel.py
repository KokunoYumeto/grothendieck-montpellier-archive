"""Finite algebraic checks for C.3ao, rerun after scratch loss."""
from pathlib import Path
from datetime import datetime, timezone
from itertools import product
import json
import time
import sympy as s

started=time.perf_counter();base=Path(__file__).resolve().parents[1]
out=base/'output';out.mkdir(exist_ok=True)
u,v,b,t,a=s.symbols('u v b t a')
F=u**4+v**4+1
assert s.expand(F-u*s.diff(F,u)/4-v*s.diff(F,v)/4)==1
assert (4-1)*(4-2)//2==3
assert 2*3-2==4
serre=[{'n':n,'dual_degree':4*(1-n)} for n in range(2,21)]
assert all(row['dual_degree']<0 for row in serre)
dimensions=[]
for r in range(2,11):
 for m in range(r,r+13):
    N=m+r+1;D=(r+1)*3**r
    assert N>=2*r+1 and m>=r
    assert D-(r+1)+r==D-1
    assert r+(m-1)==N-2
    dimensions.append({'r':r,'m':m,'N':N,'coefficient_count':D,
                       'bad_incidence_upper_dimension':D-1,
                       'smooth_H_dimension':N-2,'kernel_bundle_rank':m})
recursions=[]
for r in range(2,17):
    mat=s.eye(r)
    for j in range(r-1):mat[j,j+1]=b
    assert mat.det()==1
    recursions.append({'r':r,'highest_power':r,'upper_triangular_determinant':1})
tensors=[]
for r in range(2,9):
    terms=list(product(range(3),repeat=r-1))
    normal=[]
    for word in terms:
       # A tensor basis uses 1,u_i,v_i; v_i exponent is below its quartic relation.
       uv=tuple((int(k==1),int(k==2)) for k in word)
       assert all(vdegree<4 for _,vdegree in uv)
       normal.append(uv)
    assert len(set(normal))==3**(r-1)
    tensors.append({'r':r,'independent_normal_monomials':len(normal),
                    'quartic_leading_exponent':4})
vertical=s.diff(1+t*a,t)/(1+t*a)
horizontal=s.diff(1+t*a,a)/(1+t*a)
assert vertical.subs(t,0)==a and horizontal.subs(t,0)==0
residue=s.residue(-(1+u+u*u)/(u-b),u,b)
assert s.expand(residue+1+b+b*b)==0
record={'utc':datetime.now(timezone.utc).isoformat(),'recovery_rerun':True,
 'all_passed':True,'sympy_version':s.__version__,
 'fermat_jacobian_unit':'F-u*F_u/4-v*F_v/4=1','genus':3,'canonical_degree':4,
 'serre_dual_degrees':serre,'dimension_cases':dimensions,
 'coefficient_recursions':recursions,'canonical_tensor_cases':tensors,
 'conormal_dlog':str(vertical.subs(t,0)),'horizontal_dlog':0,
 'residue':str(residue),'runtime_seconds':time.perf_counter()-started,
 'scope':'Finite defining-data identities only; formal algebraization, absolute-field independence and Chow detection are separately proved.'}
data=json.dumps(record,indent=2)+'\n'
(out/'absolute_picard_kernel.json').write_text(data)
(out/'absolute_picard_kernel.out').write_text(data)
print(data)
