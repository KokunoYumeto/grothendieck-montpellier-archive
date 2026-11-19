#!/usr/bin/env python3
"""Exact algebra and rational bounds for the explicit collar supersolution.

No hyperbolic PDE is approximated. The continuous comparison proof is in
sections/part_a567_collar_explicit.tex. This script checks its finite algebra.
"""
from fractions import Fraction as F
import sympy as sp

y, t = sp.symbols('y t', real=True)
n = sp.symbols('n', positive=True, integer=True)
mode = sp.exp(-n*y)*(n-sp.tan(y))
assert sp.trigsimp(sp.diff(mode,y,2)-(n**2+2/sp.cos(y)**2)*mode) == 0
assert sp.diff(mode,y).subs(y,0) == -(n**2+1)
assert mode.subs(y,0) == n
eta = 1-10*t**3+15*t**4-6*t**5
assert sp.factor(sp.diff(eta,t)) == -30*t**2*(t-1)**2
assert sp.factor(sp.diff(eta,t,2)) == -60*t*(t-1)*(2*t-1)
for endpoint,value in [(0,1),(1,0)]:
    assert eta.subs(t,endpoint) == value
    assert sp.diff(eta,t).subs(t,endpoint) == 0
    assert sp.diff(eta,t,2).subs(t,endpoint) == 0
assert abs(sp.diff(eta,t).subs(t,sp.Rational(1,2))) == sp.Rational(15,8)
for critical in sp.solve(sp.diff(eta,t,3),t):
    assert sp.simplify(sp.diff(eta,t,2).subs(t,critical)**2) == sp.Rational(100,3)
assert sp.Rational(100,3) < 36

# Graph curvature from the connection in dr^2 + cosh(r)^2 ds^2.
c,h,p,pp = sp.symbols('c h p pp', real=True)
c = sp.Symbol('c',positive=True)
E = c*c+p*p
radial_acceleration = pp-c*h
longitudinal_acceleration = 2*h*p/c
curvature = (-c*radial_acceleration+p*c*longitudinal_acceleration)/E**sp.Rational(3,2)
expected = (h*(c*c+2*p*p)-c*pp)/E**sp.Rational(3,2)
assert sp.simplify(curvature-expected) == 0
q = p/c
normalized = ((h/c)*(1+2*q*q)-pp/(c*c))/(1+q*q)**sp.Rational(3,2)
assert sp.simplify(normalized-expected) == 0

N = 10**4
eps = F(1,10**14)
b = F(1,100)
height = 2*b
tan_upper = height/(1-height*height/2)
sec2_upper = 1/(1-height*height/2)**2
assert tan_upper == F(100,4999)
assert tan_upper < F(2,81) < F(1,40)
assert sec2_upper < 2
assert F(15,8)/b < 200
assert F(100,3)/b**4 < 60000**2
assert F(3,2)*eps < b
H_residual_upper = -4000+60000*F(1,40)+2*200*2
assert H_residual_upper == -1700
residual_coefficient = 60000*(N+F(1,40))+400*(N*N+N*F(1,40)+2)
assert residual_coefficient == 40600102300
assert N*b == 100
assert residual_coefficient < 2**100
assert 2*H_residual_upper+F(1,2) < 0

# The estimates use only the fixed integer N, not an asymptotic assertion.
assert N*N+N+2 <= 2*N*N
assert N**3+2*N*N+5*N+1 <= 4*N**3
assert 2+2*N**3 <= 3*N**3
assert 4+N*N <= 2*N*N
normal_error_upper = 5*eps*N**3+F(1,4)*eps**2*N**4
assert normal_error_upper < 10*eps*N**3
curvature_coefficient = F(9,8)+F(15,8)*N*N+F(3,16)*N**4
assert curvature_coefficient <= N**4
boundary_error_fraction = 10*eps*N**3+eps**2*N**4
assert boundary_error_fraction == F(1,10)+F(1,10**12)
assert boundary_error_fraction < 1
assert N*eps/2 < F(1,10)
negative_upper = 4000-F(9,20)*(N-1)
assert negative_upper == -F(9991,20) < 0

print('Exact separated-mode equation and boundary derivative: PASS')
print('Quintic cutoff endpoint and derivative bounds: PASS')
print('Exact signed graph-curvature identity: PASS')
print('Fixed parameters: n=10000, epsilon=1/100000000000000')
print('Conformal collar tan bound:',tan_upper,'< 2/81')
print('L(H) upper bound:',H_residual_upper)
print('Cutoff residual coefficient:',residual_coefficient,'< 2^100')
print('Relative boundary error:',boundary_error_fraction,'< 1')
print('Certified value upper bound for u:',negative_upper*eps)
print('All symbolic identities and exact rational inequalities passed.')
