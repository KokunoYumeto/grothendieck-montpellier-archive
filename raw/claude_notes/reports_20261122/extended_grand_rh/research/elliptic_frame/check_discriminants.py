"""Optional independent maximal-order and rational resolvent checks with SymPy."""
import os
os.environ["SYMPY_GROUND_TYPES"]="python"

from sympy import Poly, Rational, Symbol, discriminant, expand
from sympy.polys.numberfields import round_two

x=Symbol("x")
z=Symbol("z")
a,b,c=-4,-3,Rational(-4,3)
resolvent=z**3-a*z**2-4*c*z+4*a*c-b*b
assert expand(resolvent.subs(z,x-Rational(4,3))) == x**3+Rational(269,27)
assert expand(3*resolvent.subs(z,x*x+a)) == 3*x**6-24*x**4+64*x*x-27
assert discriminant(3*x**4-12*x**2-9*x-4,x) == -(3**3)*(269**2)

# The quartic and sextic variables below are three times the pair/line coordinates.
fields={"A":(x**4-36*x*x-81*x-108,-1953747),
        "F":(x**3-269,-217083),
        "B":(x**6-72*x**4+1728*x*x-6561,424125260001)}
for name,(poly,expected) in fields.items():
    assert Poly(poly,x).is_irreducible
    _,disc=round_two(Poly(poly,x))
    assert disc==expected
    print(name,disc)
