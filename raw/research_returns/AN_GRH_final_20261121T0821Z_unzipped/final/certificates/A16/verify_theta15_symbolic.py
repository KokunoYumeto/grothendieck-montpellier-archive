"""Independent symbolic certificate for an exact order-15 theta point.

Uses SymPy polynomial reduction over F2; imports no producer arithmetic.
All coefficients are given in F8=F2[z]/(z^3+z+1).
"""
from pathlib import Path
import json
from sympy import Poly, symbols

z,X=symbols('z X')
modulus=Poly(z**3+z+1,z,modulus=2)
assert modulus.is_irreducible
def coeff(n):return sum(((n>>i)&1)*z**i for i in range(3))
def reduce_poly(expression):
    p=Poly(expression,X,domain='EX')
    terms={}
    for (degree,),c in p.terms():
        r=Poly(c,z,modulus=2).rem(modulus).as_expr()
        if r!=0:terms[degree]=str(r)
    return terms
def reduce_field(expression):return Poly(expression,z,modulus=2).rem(modulus).as_expr()

av=[2,3,6,7,6,0,5,7]
bv=[1,3,4,6,7,1]
A=sum(coeff(a)*X**i for i,a in enumerate(av))
B=sum(coeff(b)*X**i for i,b in enumerate(bv))
h=X**2
f=X**5+(z+1)*X**3+X
r,s=z**2,z
assert reduce_field(s**2+r**2*s-f.subs(X,r))==0
norm=A**2+h*A*B+f*B**2
assert reduce_poly(norm+(X+r)**15)=={}
assert reduce_field(A.subs(X,r)+B.subs(X,r)*s)==0
other=reduce_field(A.subs(X,r)+B.subs(X,r)*(s+r**2))
assert other!=0
assert Poly(A,X).degree()==7 and Poly(B,X).degree()==5
assert reduce_field(r**4)==z and reduce_field(r**4+1)!=0
orbit=[];v=1
while v not in orbit:orbit.append(v);v=2*v%15
units=sorted(set(orbit+[-v%15 for v in orbit]))
assert units==[1,2,4,7,8,11,13,14]
# The short prime-degree comparison is checked directly over F2.
f5=X**5+X**4+X**3+X
A5=X+1
assert reduce_poly(A5**2+X**2*A5+f5+(X+1)**5)=={}
assert reduce_field(A5.subs(X,1))==0
result=dict(status='PASS',field_modulus=str(modulus.as_expr()),field_modulus_irreducible=True,
 curve='Y^2+X^2Y=X^5+(z+1)X^3+X',point={'X':'z^2','Y':'z'},
 A_coefficients_binary_ascending=av,B_coefficients_binary_ascending=bv,
 norm_identity='A^2+X^2*A*B+(X^5+(z+1)*X^3+X)*B^2=(X+z^2)^15',
 value_at_R=0,value_at_conjugate=str(other),
 pole_degrees={'A':14,'B_Y':15},r_fourth_power=str(reduce_field(r**4)),
 exact_order_argument='Order divides15 by divisor identity; order1 impossible in genus2; order3 excluded by l(3P)=l(2P)=2; order5 would force r^4=1 by the norm X coefficient.',
 two_orbit_mod15=orbit,generated_units_with_minus_one=units,
 prime_degree5_comparison_norm_verified=True,formal_verification=False)
Path(__file__).with_name('theta15_symbolic_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
