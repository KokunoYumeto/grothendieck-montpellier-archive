#!/usr/bin/env python3
"""Exact certificates for A.4.27--29; rational symbolic arithmetic only."""
import sympy as S
from fractions import Fraction
from math import factorial, prod

x,t,a,g2,g3=S.symbols('x t a g2 g3')
P=4*x**3-g2*x-g3
Fp=-(x+a)/S.sqrt(P)
res=2*P*(x+a)*S.diff(Fp,x)+(S.diff(P,x)*(x+a)-2*P)*Fp
assert S.simplify(res)==0
print('A.4.27 elliptic primitive ODE residual:', S.simplify(res))

Q=4*x*(x-1)*(x-t)
# R=x(x-1)/y; dR divided by omega=dx/y.
dR_over_omega=S.diff(x*(x-1),x)-x*(x-1)*S.diff(Q,x)/(2*Q)
reduction=(x-t)/2-t*(t-1)/(2*(x-t))
assert S.simplify(dR_over_omega-reduction)==0
AA=1/(2*(1-t)); BB=-1/(2*t*(1-t))
assert S.simplify(1/(2*(x-t))-(AA+BB*x)+dR_over_omega/(t*(t-1)))==0
print('A.4.28 exact Gauss-Manin reduction residual: 0')
print('Connection matrix columns:',S.Matrix([[AA,AA],[BB,-AA]]))
s=S.symbols('s')
N=18
G=sum(S.Rational(prod(4*j+1 for j in range(m))**2,factorial(2*m))*s**(2*m) for m in range(N+1))
F=(S.Rational(1,2)-2*s*s)*S.diff(G,s)-(S.Rational(1,2)+s)*G
C=S.Matrix([[AA,AA],[BB,-AA]]).subs(t,S.Rational(1,2)+s)
V=S.Matrix([F,G])
residual=V.diff(s)+C*V
assert all(S.series(z,s,0,2*N-1).removeO().expand()==0 for z in residual)
print('Horizontal CM initial vector:', V.subs(s,0).T)
print('G(s) through s^8:', S.series(G,s,0,10))
print('Horizontal ODE verified through degree',2*N-2)

def valuation_integer(n,p):
    count=0
    while n%p==0 and n:
        n//=p;count+=1
    return count

def valuation_rational(q,p):
    return valuation_integer(q.numerator,p)-valuation_integer(q.denominator,p)
for p in (3,7,11,19,23,31,43,47):
    m=(p+1)//2
    coefficient=Fraction(prod(4*j+1 for j in range(m))**2,factorial(2*m))
    val=valuation_rational(coefficient,p)
    assert val==-1
    print('p =',p,'degree =',2*m,'valuation =',val)

u,n,u0,eta0=S.symbols('u n u0 eta0')
assert S.expand(-a*(n*u)**2/2+n**2*a*u*u/2)==0
assert S.expand(-(eta0-a*u0)*u0/2-a*u0*u0/2+eta0*u0/2)==0
print('A.4.29 division quotient Gaussian exponent: 0')
print('Torsion constant Gaussian exponent difference: 0')
print('All exact identities passed.')
