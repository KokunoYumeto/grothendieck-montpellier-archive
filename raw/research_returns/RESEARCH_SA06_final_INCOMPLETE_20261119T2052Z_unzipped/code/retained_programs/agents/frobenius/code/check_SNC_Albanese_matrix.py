"""Exact symbolic check of the two-vertex weighted matrix identity.
This checks the displayed block algebra, not geometric isogeny or families.
"""
from pathlib import Path
from datetime import datetime,timezone
import sympy as sp
import time,json
t=time.perf_counter()
a,b=sp.symbols('a b')
r=sp.Matrix(2,2,sp.symbols('r0:4'))
s=sp.Matrix(2,3,sp.symbols('s0:6'))
x,y,z=sp.symbols('x y z')
q=sp.Matrix([[x,y],[y,z]])
n1=sp.Matrix([[sp.Symbol('u0'),sp.Symbol('u1')],[sp.Symbol('u1'),sp.Symbol('u2')]])
v=sp.symbols('v0:6')
n2=sp.Matrix([[v[0],v[1],v[2]],[v[1],v[3],v[4]],[v[2],v[4],v[5]]])
lam=(-n1).row_join(-r.T*q*s).col_join((-s.T*q*r).row_join(-n2))
T=sp.diag(a,a,b,b,b)
diag=sp.diag(*[]) if False else sp.diag(a*(-a*n1-b*r.T*q*r),b*(-b*n2-a*s.T*q*s))
d=r.row_join(-s)
rhs=diag+a*b*d.T*q*d
dif=(T.T*lam*T-rhs).applyfunc(sp.expand)
assert dif==sp.zeros(5)
out={'completed_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-t,
     'checked_scalar_polynomial_entries':25,
     'component_dimensions':[2,3],'edge_jacobian_dimension':2,
     'all_zero':True,
     'scope':'Exact generic block-matrix AM.8 check only; no geometric or proper-family conclusion is tested.'}
base=Path(__file__).resolve().parents[1]
(base/'output/SNC_Albanese_matrix_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

