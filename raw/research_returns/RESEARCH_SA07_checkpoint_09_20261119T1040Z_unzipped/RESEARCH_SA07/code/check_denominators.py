"""Exact local-series checks for A.4.22; no transcendence inference from numerics."""
from math import comb
from fractions import Fraction
import sympy as s

t = s.symbols('t')
R = s.sqrt(1+4*t**4)
x = (1+R)/(2*t**2)
assert s.simplify(t**2*x**2-x-t**2) == 0
assert s.simplify(-t*s.diff(x,t)/(2*x)-1/R) == 0
assert s.simplify(x/R-(1+1/R)/(2*t**2)) == 0
print('CM curve y^2=4x^3-4x: x=(1+sqrt(1+4t^4))/(2t^2), omega=dt/sqrt(1+4t^4).')

Z = 1/t - sum(s.Rational((-1)**n*comb(2*n,n),2*(4*n-1))*t**(4*n-1) for n in range(1,7))
assert s.series(s.diff(Z,t)+x/R,t,0,23).removeO() == 0
print('zeta(u(t)) through degree23:',s.expand(Z))

def vp(n,p):
    ans=0
    while n and n%p==0:
        n//=p
        ans+=1
    return ans

for r in range(5):
    n=(3**(2*r+1)+1)//4
    assert 4*n-1 == 3**(2*r+1)
    b=comb(2*n,n)
    assert vp(b,3) == r
    c=Fraction((-1)**(n+1)*b,2*(4*n-1))
    value=vp(c.numerator,3)-vp(c.denominator,3)
    assert value == -r-1
    print(f'r={r}, n={n}, exponent={4*n-1}, v3(binomial)={r}, v3(coefficient)={value}')
print('Infinite proof: n=1+2*sum(3^(2j+1),j=0..r-1), so n+n has exactly r base-three carries.')
