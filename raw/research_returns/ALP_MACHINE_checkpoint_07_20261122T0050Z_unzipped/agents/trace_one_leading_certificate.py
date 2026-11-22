"""Exact coordinate/valuation checks for ALP-LIFT-08; geometry proved in text."""
from fractions import Fraction
from pathlib import Path
import json
import sympy as sp

v1,v2,v3,alpha,iota,lam,beta=sp.symbols('v1 v2 v3 alpha iota lam beta')
q=v1*v3-v2**2
Q=lambda u:sp.expand(u[0]*u[2]-u[1]**2)
u2=[alpha**i/iota*v for i,v in enumerate([v1,v2,v3],1)]
u7=[lam/beta*v1,lam/beta*(v1+lam*v2),lam/beta*(v1+2*lam*v2+lam**2*v3)]
assert sp.simplify(Q(u2)-alpha**4/iota**2*q)==0
assert sp.simplify(Q(u7)-lam**4/beta**2*q)==0
assert sp.Matrix([[v1,v2],[v2,v3]]).det()==q
assert sp.Poly(q,v1,v2,v3,modulus=2).coeff_monomial(v1*v3)==1
c2=4*Fraction(2,7)
c7=4*Fraction(1,6)-2*Fraction(7,12)
assert c2==Fraction(2,7)+Fraction(6,7)==Fraction(8,7)
assert c7==Fraction(1,6)-Fraction(2,3)==Fraction(-1,2)
out={
 'statement':'ALP-LIFT-08',
 'kind':'exact polynomial and rational-valuation certificate; not a formal geometry proof',
 'cup_product_determinant':str(q),
 'primitive_mod_2':True,
 'dyadic_quadratic_scaling':'alpha^4/iota^2',
 'septadic_quadratic_scaling':'lambda^4/beta^2=lambda^-3',
 'dyadic_content':str(c2),
 'septadic_content':str(c7),
 'independent_determinant_frame_sums_agree':True,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
