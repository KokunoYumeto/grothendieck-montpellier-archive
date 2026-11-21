#!/usr/bin/env python3
"""Exact finite certificates for IF12; no Lean execution or numerical theta sum.

The analytic estimates (normal convergence, exp inequalities, and the lattice
tail bound) are proved in genuine_theta_noncommutator.tex.  This script checks
their instantiated integer/rational inequalities and independently verifies
the unitary gauge and ordinary-derivative heat normalization in finite models.
"""
from fractions import Fraction
from math import factorial
from pathlib import Path
import hashlib
import json
import sympy as sp

OUT = Path(__file__).resolve().parent
nu = (28,27,24,21,18,15,12,10)
alpha = (18,17,14,11,8,5,2,0)
ah = tuple(nu[k] - (nu[k+1] if k < 7 else 0) for k in range(8))
assert tuple(x + 10 for x in alpha) == nu
assert ah == (1,3,3,3,3,3,2,10)
degree = sum((h+1)*c for h,c in enumerate(ah))
assert degree == sum(nu) == 155
q = 24*8
T = 10**400
diag = [Fraction(1,4),Fraction(1,3)] + [Fraction(1,4)]*6
Q_at_a = Fraction(1)
minor = Fraction(1)
for h, c in enumerate(ah, start=1):
    minor *= diag[h-1]
    if h >= 2:
        Q_at_a *= minor**c
P_at_a = (diag[0]-diag[1])*Q_at_a
assert P_at_a == -Fraction(1,4**128 * 3**28)
assert abs(P_at_a) > Fraction(1,10**156)
M_bound = 2
for h,c in enumerate(ah, start=1):
    if h >= 2:
        M_bound *= factorial(h)**c
assert M_bound <= 2*factorial(8)**27 < 2*10**135
assert q*degree**2 == 4612800 < 10**7

# pi >= 3, exp(u)-1 <= 2u when 0<=u<=1, exp(T/2)>=T^2/8.
u_upper = Fraction(q*degree**2,24*T)
assert 0 < u_upper < 1
heat_error_bound = 2*M_bound*u_upper
tail_error_bound = Fraction(128*q*M_bound,T*T)
assert heat_error_bound < Fraction(4,10**258)
assert tail_error_bound < Fraction(5,10**661)
assert heat_error_bound + tail_error_bound < abs(P_at_a)/2
# Conditions for (1+4r)^q-1 <= 8qr, using r<=8/T^2.
assert Fraction(8,T*T) <= Fraction(1,2)
assert Fraction(32*q,T*T) <= 1
assert T >= 2*degree

# Exact unitary gauge for one Fourier summand.  z is complex; T,a,n real.
z = sp.Symbol('z')
t = sp.Symbol('t', positive=True)
a,n = sp.symbols('a n', real=True)
x = sp.I*t*a
conjx = -sp.I*t*a
original_exponent = (sp.pi*(z+x)**2/(2*t)
    - sp.pi*t*n*n + 2*sp.pi*sp.I*n*(z+x)
    - sp.pi*z*conjx/t - sp.pi*x*conjx/(2*t))
target_exponent = sp.pi*z*z/(2*t)-sp.pi*t*(n+a)**2+2*sp.pi*sp.I*(n+a)*z
assert sp.expand(original_exponent-target_exponent) == 0

# Direct truncated Taylor multiplication versus the heat differential formula.
# exp(k*x*z-s*k^2*z^2): k^{-d} d^d/dz^d at0 = exp(-s*d_x^2)x^d.
k,s,X = sp.symbols('k s X')
heat_checks = []
for d in range(13):
    linear = sum((k*X*z)**j/sp.factorial(j) for j in range(d+1))
    quadratic = sum((-s*k*k*z*z)**j/sp.factorial(j) for j in range(d//2+1))
    direct = sp.expand(linear*quadratic).coeff(z,d)*sp.factorial(d)/k**d
    heat = sum((-s)**j/sp.factorial(j)*sp.diff(X**d,X,2*j) for j in range(d//2+1))
    assert sp.expand(direct-heat) == 0
    heat_checks.append(d)

# Source half-period normalization: Gaussian odd theta after U_h has no
# remaining linear term in z. Its constant cancels in th0 = U_h sigma/U_h sigma(0).
h = -(1+sp.I*t)/2
conjh = -(1-sp.I*t)/2
odd_gauge = (sp.pi*(z+h)**2/(2*t) + sp.pi*sp.I*(sp.I*t)/4
    + sp.pi*sp.I*(z+h+sp.Rational(1,2))
    - sp.pi*z*conjh/t - sp.pi*h*conjh/(2*t))
assert sp.expand(odd_gauge-odd_gauge.subs(z,0)-sp.pi*z*z/(2*t)) == 0

def rational_record(x):
    return {'numerator':str(x.numerator),'denominator':str(x.denominator)}

record = {
 'scope':'exact integer/rational estimate checks and finite symbolic normalizations; no numerical theta summation, no Lean build',
 'python_sympy_version':sp.__version__,
 'nu':nu,'alpha':alpha,'column_multiplicities':ah,'degree':degree,'coordinates':q,
 'T_decimal':str(T),'T_power_of_10':400,
 'P_at_a':rational_record(P_at_a),
 'coefficient_l1_upper_bound':str(M_bound),
 'u_upper_pi_ge_3':rational_record(u_upper),
 'heat_error_upper':rational_record(heat_error_bound),
 'tail_error_upper':rational_record(tail_error_bound),
 'error_less_than_half_main_term':True,
 'unitary_gauge_exact':True,'half_period_th0_normalization_exact':True,
 'ordinary_derivative_heat_degrees':heat_checks,
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
(OUT/'genuine_theta_check.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({key:record[key] for key in (
 'scope','nu','column_multiplicities','degree','coordinates','T_power_of_10',
 'error_less_than_half_main_term','unitary_gauge_exact',
 'half_period_th0_normalization_exact','ordinary_derivative_heat_degrees')},indent=2))
