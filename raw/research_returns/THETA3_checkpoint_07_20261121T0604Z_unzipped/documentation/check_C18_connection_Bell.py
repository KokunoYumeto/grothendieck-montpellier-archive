"""Finite exact checks supplementing the full THETA3-C18 proofs.

The displayed general Bell-weight inequality is proved in the paper; checking
finitely many primes and weights is not used as a proof of that assertion.
"""
from fractions import Fraction as F
import sympy as s


def vp_factorial(n, p):
    out = 0
    while n:
        n //= p
        out += n
    return out


for p in [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
    slope = F(p, p*p-1)
    for j in range(4, 20002, 2):
        assert (vp_factorial(j, p) - (j-2)//p + F(1, p-1)
                <= j*slope), (p, j)
    assert vp_factorial(p+1, p) + F(1, p-1) == (p+1)*slope
print("Bell-weight inequality: 13 primes, every even 4<=j<=20000 passed.")
print("Equality at j=p+1 passed for each tested prime.")

x, g2, g3 = s.symbols('x g2 g3')
y2 = 4*x**3-g2*x-g3
B = 9*x-g2/(2*x)-g3/x**2-(6*x*x-g2/2)**2/y2
numerator = (-5*g2*x**4-13*g3*x**3+g2*g2*x*x/4
             +3*g2*g3*x/2+g3*g3)
assert s.cancel(B-numerator/(x*x*y2)) == 0
print("Rational B numerator verified by exact symbolic simplification.")

t = s.symbols('t')
q = 1-s.Rational(5,12)*t**4+s.Rational(1411,2016)*t**8
Dt = 1+2*t**4-2*t**8
A = s.series(Dt*s.diff(q,t)/q, t, 0, 8).removeO()
assert A == -s.Rational(5,3)*t**3+s.Rational(11,7)*t**7
DA = s.series(Dt*s.diff(A,t), t, 0, 7).removeO()
assert DA == -5*t*t+t**6
print("Square-lattice connection expansion verified: A=-5t^3/3+11t^7/7; DA=-5t^2+t^6.")
