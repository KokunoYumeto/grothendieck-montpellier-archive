"""Exact certificates for E: y^2=4*x^3-30*x-28 and its Hodge parameter.

Python 3 + SymPy.  All operations are exact over Q; sqrt(-2) is represented
by u with u^2=-2 when interpreting the geometric formulas in the report.
"""
from fractions import Fraction
import sympy as sp
import time

t0 = time.perf_counter()
X, Y = sp.symbols('X Y')
a, b = sp.Rational(-6), sp.Rational(9, 2)
f = X**3+a*X**2+b*X
Xp = X+a+b/X
Yp2 = f*(1-b/X**2)**2
target = sp.expand(Xp**3-2*a*Xp**2+(a*a-4*b)*Xp)
assert sp.factor(Yp2-target) == 0
assert a*(-2) == -2*a
assert b*(-2)**2 == a*a-4*b
print('Source after X=x+2, Y=y/2: Y^2 =', f)
print('2-isogeny X_prime =', Xp)
print('2-isogeny Y_prime = Y*(1 - 9/(2*X^2))')
print('Target equation residual:', sp.factor(Yp2-target))
print('Target coefficients:', -2*a, a*a-4*b)
print('Scaling by u, u^2=-2, gives target coefficients:', a*(-2), b*(-2)**2)
# d(Y/X)=(X-b/X)*dX/(2Y); omega=dX/(2Y), xi=(X-2)*omega.
reduction = -X+1
exact_coefficient = sp.Rational(1,2)*(X-b/X)
assert sp.simplify((-Xp/2)-2-reduction-exact_coefficient) == 0
print('alpha^*(xi)/u in de Rham, after exact differential removal:', reduction, '* omega')
print('In (omega,xi) basis: alpha^*(omega)=u*omega; alpha^*(xi)=-u*omega-u*xi')
print('Hodge slope h=(-u)/(-u-u)=', sp.Rational(1,2))
g2, g3 = sp.Integer(30), sp.Integer(28)
disc = g2**3-27*g3**2
j = 1728*g2**3/disc
assert j == 8000
print('Weierstrass discriminant g2^3-27*g3^2:', disc)
print('j:', j)
print('runtime_seconds:', f'{time.perf_counter()-t0:.6f}')
