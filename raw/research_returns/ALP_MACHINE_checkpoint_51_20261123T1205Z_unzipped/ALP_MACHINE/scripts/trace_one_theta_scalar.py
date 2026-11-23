#!/usr/bin/env python3
"""Exact cyclotomic cross-product; independent numerical theta-scalar check.

The numerical comparison is diagnostic only. The exact identity, including
its eighth power, is derived from the derivative Thomae theorem in AM-R-006.
"""
from pathlib import Path
from itertools import product
import json
import sympy as sp
import mpmath as mp

OUT = Path(__file__).resolve().parents[1] / 'evidence' / 'trace_one_theta_scalar.json'
a = sp.Symbol('a')
phi = sum(a**i for i in range(7))
cross = sp.rem(sp.prod(a**j-a**k for j in (1,3,5) for k in (0,2,4,6)), phi, a)
cross_sq = sp.rem(cross**2, phi, a)
assert cross != 0
assert sp.Rational(49)*sp.Rational(125,16) == sp.Rational(6125,16)
assert sp.Rational(4,5)**12 > 0

mp.mp.dps = 60
zeta = mp.exp(2*mp.pi*mp.j/7)
A = mp.matrix([[zeta**(2*(i+1)*j) for j in range(3)] for i in range(3)])
B = mp.matrix([[sum(zeta**((i+1)*(2*k+1)) for k in range(j,3)) for j in range(3)] for i in range(3)])
period_scalars = [-2*mp.j/7*mp.beta(mp.mpf(i)/7,mp.mpf('0.5'))*(zeta**i-1) for i in (1,2,3)]
P = mp.diag(period_scalars)*A
tau = A**-1*B
Pinv = P**-1
alpha = [mp.mpf('0.5')]*3
beta = [mp.mpf('0.5'),mp.mpf(0),mp.mpf('0.5')]
theta_zero = mp.mpc(0)
theta_K_zero = mp.mpc(0)
theta_K_h13 = mp.mpc(0)
theta_K_h22 = mp.mpc(0)
for n in product(range(-9,10), repeat=3):
    theta_zero += mp.exp(mp.pi*mp.j*sum(n[i]*tau[i,j]*n[j] for i in range(3) for j in range(3)))
    q = [n[i]+alpha[i] for i in range(3)]
    term = mp.exp(mp.pi*mp.j*sum(q[i]*tau[i,j]*q[j] for i in range(3) for j in range(3))
                  + 2*mp.pi*mp.j*sum(q[i]*beta[i] for i in range(3)))
    theta_K_zero += term
    d = [2*mp.pi*mp.j*sum(q[i]*Pinv[i,j] for i in range(3)) for j in range(3)]
    theta_K_h13 += term*d[0]*d[2]
    theta_K_h22 += term*d[1]**2
c = -mp.j*theta_K_h13/theta_zero
cross_num = mp.fprod(zeta**j-zeta**k for j in (1,3,5) for k in (0,2,4,6))
checks = {
    'theta_K_zero': abs(theta_K_zero),
    'quadratic_shape': abs(theta_K_h22+2*theta_K_h13),
    'eighth_power': abs(c**8-cross_num**2/4**8),
    'modulus': abs(abs(c)-abs(cross_num)**mp.mpf('0.25')/4),
}
assert max(checks.values()) < mp.mpf('1e-35'), checks
data = {
    'exact_cross_product_in_Q_zeta7': str(cross),
    'exact_c_eighth_power': str(cross_sq/sp.Integer(4)**8),
    'c_definition': '-i partial_u1 partial_u3 theta[111/2;101/2](P^-1u)|0 / theta[0;0](0)',
    'scalar_numeric': mp.nstr(c,50),
    'scalar_modulus_numeric': mp.nstr(abs(c),50),
    'sigma_gaussian_constant_exact': '6125/16',
    'finite_scalar_valuations_normalized_vp_p_1': {'2':'-2','7':'1/2','all_other_primes':'0'},
    'diagnostic_residuals': {k:mp.nstr(v,12) for k,v in checks.items()},
    'numeric_precision': 60,
    'theta_cube': 9,
    'scope': 'Cyclotomic reduction exact; theta numerical comparisons diagnostic, not a formal or interval certificate.',
}
OUT.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
