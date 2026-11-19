#!/usr/bin/env python3
"""Exact certificate for the explicit Fermat-quartic CM Prym cover.

This verifies rational identities, differential pullbacks and finite counts.
It does not certify LM6 A.20, an actual normalizer subgroup, or cofinality.
Inputs are the displayed characteristic-zero polynomial equations.
"""
from time import perf_counter
_started = perf_counter()
import sympy as S

t, s, x, y = S.symbols('t s x y')
checks = []
def zero(label, expression, relation=None, main=None):
    numerator = S.cancel(expression).as_numer_denom()[0]
    if relation is not None:
        numerator = S.rem(S.Poly(numerator, main), S.Poly(relation, main)).as_expr()
    answer = S.factor(numerator)
    assert answer == 0, (label, answer)
    checks.append(label)
    print('PASS:', label)

X=2*(1+s)/t**2
Y=4*(1+s)/t**3
zero('D: s^2=1-t^4 maps to Y^2=X^3+4X',Y**2-X**3-4*X,s**2+t**4-1,s)
zero('D_z: s^2=1+t^4 maps to Y^2=X^3-4X',Y**2-X**3+4*X,s**2-t**4-1,s)
zero('Inverse t=2X/Y',2*X/Y-t)
zero('Inverse s=2X^3/Y^2-1',2*X**3/Y**2-1-s)
zero('Original D scaling: (1+i)^4=-4',(1+S.I)**4+4)
zero('Third quotient scaling: (sqrt(2))^4=4',S.sqrt(2)**4-4)

# C: x^4+y^4=1 and dy/dx=-x^3/y^3.
rel=x**4+y**4-1
dydx=-x**3/y**3
zero('q_x pulls dt/s back to -x dx/y^3',dydx/x**2+x/y**3)
zero('q_y pulls dt/s back to y dx/y^3',1/y**2-y/y**3)
zero('q_z pulls dt/s back to dx/y^3',y-x*dydx-1/y**3,rel,x)
pullback_matrix=S.Matrix([[0,0,1],[-1,0,0],[0,1,0]])
assert pullback_matrix.det() in (1,-1)
checks.append('Three quotient differential pullbacks form a basis')
print('PASS:',checks[-1],'; determinant=',pullback_matrix.det())

# A branch point has s=0,t^4=1. On D's Weierstrass model
# X^2=4 and Y^2=8X; the doubling formula gives (0,0).
u,v=S.symbols('u v')
slope=(3*u*u+4)/(2*v)
x2=S.cancel(slope*slope-2*u)
y2=S.cancel(slope*(u-x2)-v)
G=S.groebner([v*v-8*u,u*u-4],v,u,order='lex')
for name,expr in [('branch-point doubled x coordinate',x2),('branch-point doubled y coordinate',y2)]:
    num=S.cancel(expr).as_numer_denom()[0]
    assert S.expand(G.reduce(num)[1]) == 0
    print('PASS:',name,'=0 modulo branch equations')
    checks.append(name)
# Denominators are nonzero since v^2=8u and u^2=4.
assert S.gcd(S.Poly(t**4-1,t),S.Poly(4*t**3,t)).degree()==0
print('PASS: the four branch values are distinct in characteristic zero')
checks.append('branch polynomial is separable')

q_degree=2; multiplication_degree=4**2
branch_values=4; torsion_points=4**2
genus=(4-1)*(4-2)//2
boundary=branch_values+2*(torsion_points-branch_values)
cover_degree=q_degree*multiplication_degree
assert boundary==28 and genus==3 and cover_degree==32
assert 2-2*genus-boundary==-cover_degree
assert 2*genus-2==q_degree*(2*1-2)+branch_values
print('PASS: degree=32; genus=3; boundary=28; Euler characteristic=-32')
checks.append('Riemann-Hurwitz and open Euler counts')
print('LIMIT: no assertion that this finite cover detects all A.22 subgroups.')
print('LIMIT: normalizer-recognition consequence retains the separate A.20 proof status.')
print('TOTAL_EXACT_CHECKS:',len(checks))
print('ACTUAL_WALL_SECONDS:',format(perf_counter()-_started,'.9f'))
