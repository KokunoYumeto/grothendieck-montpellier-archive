#!/usr/bin/env python3
"""Exact rational envelope for 4*C4 < 173; no floating-point acceptance test.

Uses log(x)=2*sum(z^(2k+1)/(2k+1)), z=(x-1)/(x+1),
the geometric upper bound for its tail, and the exponential Taylor
series with a geometric bound for its tail.  Euler's constant satisfies
gamma < H_n-log(n), since the latter decreases to gamma.
This is a numerical certificate, not a proof-assistant formalization.
"""
from fractions import Fraction as F

def log_interval(x, terms=12):
    z=(x-1)/(x+1)
    assert 0 < z < 1
    lower=2*sum((z**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))
    upper=lower+2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
    return lower,upper

def exp_upper(x, terms=32):
    term=F(1)
    total=term
    for k in range(1,terms+1):
        term*=x/F(k)
        total+=term
    first_tail=term*x/F(terms+1)
    assert x/F(terms+2)<1
    return total+first_tail/(1-x/F(terms+2))

l2,u2=log_interval(F(2))
l3,u3=log_interval(F(3))
l54,u54=log_interval(F(5,4))
harmonic=sum((F(1,k) for k in range(1,1001)),F(0))
gamma_upper=harmonic-3*(l54+3*l2)  # 1000=10^3, 10=(5/4)*2^3.
assert gamma_upper<F(289,500)
assert u2<F(347,500)
assert l3>F(549,500)
exponent_upper=F(21,8)+(F(289,500)+2*F(347,500))/(4*F(549,500))
assert exponent_upper<F(3073,1000)
exp_bound=exp_upper(F(3073,1000))
assert 8*exp_bound<173
sharper_exponent=F(21,8)+(gamma_upper+2*u2)/(4*l3)
assert 8*exp_upper(sharper_exponent)<F(864,5)
print('PASS: gamma < 289/500; log 2 < 347/500; log 3 > 549/500')
print('PASS: exponent of C4/2 < 3073/1000')
print('PASS: 4*C4 < 8*exp(3073/1000) < 173, certified by rational Taylor bounds')
print('PASS: sharper rational envelope also proves C4 < 43.2')
print('Rational envelope for 4*C4 (decimal for display only):',float(8*exp_bound))
