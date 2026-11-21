#!/usr/bin/env python3
"""Local chain identities and exact parameter bound for unit gluing.

This checks displayed matrices and integers, not the derived descent gate.
"""
from pathlib import Path
import json
import sympy as s

x,y,b1,b2,c1,c2=s.symbols('x y b1 b2 c1 c2')
v=s.Matrix([-y,x]);w=s.Matrix([[x,y]])
b=s.Matrix([[b1,b2]]);c=s.Matrix([[c1,c2]])
tb=(b*v)[0];tc=(c*v)[0]
d1=v*w;d2=v
Db=[v*b,tb*s.eye(2),s.Matrix([[tb]])]
Dc=[v*c,tc*s.eye(2),s.Matrix([[tc]])]
assert d1*d2==s.zeros(2,1)
assert s.simplify(Db[0]*d1-d1*Db[1])==s.zeros(2)
assert s.simplify(Db[1]*d2-d2*Db[2])==s.zeros(2,1)
jb=s.Matrix([b2,-b1]);h0=jb*c;hm1=tc*b
assert s.simplify(d1*h0-Db[0]*Dc[0])==s.zeros(2)
assert s.simplify(d2*hm1+h0*d1-Db[1]*Dc[1])==s.zeros(2)
assert s.simplify(hm1*d2-Db[2]*Dc[2])==s.zeros(1)

U=s.diag(s.Matrix([[1,1],[1,-1]]),s.Matrix([[1,1],[1,-1]]))
S=s.diag(1,1,-1,-1)
Delta=8*s.eye(4)-6*U-8*S+6*U*S
t=s.symbols('t')
det=s.factor((Delta-t*s.eye(4)).det())
assert s.expand(det-t*t*((16-t)**2-288))==0
dims=[int(-det.subs(t,3*a)) for a in (1,2,3)]
assert dims==[1071,6768,19359]
lower=dims[2]-2*dims[1]
assert lower==5823
# Euler consistency of the sheaf Ext formulas.  Let delta=D^4/24.
z=s.symbols('z')
chiS=lambda a:a**4-2*(a-1)**4+(a-2)**4
euler=2*chiS(-1)-4*chiS(1)+2*chiS(3)
assert euler==192
out={'result':'PASS','generic_chain_lift':True,
     'generic_product_nullhomotopy':True,
     'difference_matrix':str(Delta),'determinant':str(det),
     'index_three_dimensions':dims,'non_tensor_parameter_lower_bound':lower,
     'Ext_sheaf_Euler_coefficient_D4_over24':euler,
     'limits':'The End/Ext classifications, actual gluing, and index-theorem use are written proofs. No cyclic derived trace, spectral-sequence compatibility, finite action or semiregularity is computed or asserted.'}
Path(__file__).with_name('rm_unit_gluing_certificate_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
