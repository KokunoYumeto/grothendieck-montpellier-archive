#!/usr/bin/env python3
"""Symbolic certificate for the normal-domain mixed-characteristic counterexample."""
from itertools import product
import json
import sympy as s
a,b,c=s.symbols('a b c');f=b*c-a*(2-a)
T=s.Matrix([[a-1,b],[c,1-a]]);P=T+s.eye(2)
assert all(s.expand(x)==0 for x in T*T-s.eye(2)-f*s.eye(2))
assert all(s.expand(x)==0 for x in P*P-2*P-f*s.eye(2))
assert s.expand(P.det()+f)==0
# The homogeneous reduction a^2+bc has no linear factor over F2.
linear=[x*a+y*b+z*c for x,y,z in product(range(2),repeat=3) if (x,y,z)!=(0,0,0)]
q=s.Poly(a*a+b*c,a,b,c,modulus=2)
assert not any(s.Poly(u*v,a,b,c,modulus=2)==q for u,v in product(linear,repeat=2))
print(json.dumps({'matrix_T':str(T),'relation_f':str(f),'T_squared_minus_identity':'f*I2','P_squared_minus_2P':'f*I2','det_P':'-f','mod2_defining_polynomial':'a^2+b*c','nonzero_linear_forms_checked':len(linear),'linear_factor_pairs_checked':len(linear)**2,'mod2_polynomial_irreducible':True},indent=2))
