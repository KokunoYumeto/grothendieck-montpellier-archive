#!/usr/bin/env python3
"""Finite certificates used in the degree-six and degree-seven proofs.

The geometric input and Hering's classification are proved/cited in the
accompanying TeX. These checks certify only the arithmetic exclusions.
"""
import json
import time
from pathlib import Path

started = time.perf_counter()

def order_mod(a, m):
    r = 1
    for j in range(1, m + 1):
        r = r*a % m
        if r == 1:
            return j
    raise AssertionError('not a unit')

def gl_order(n, q):
    ans = 1
    for i in range(n):
        ans *= q**n-q**i
    return ans

def semilinear_order(n, exponent):
    return exponent*gl_order(n, 2**exponent)

orbit = []
a = 1
while a not in orbit:
    orbit.append(a)
    a = 2*a % 31
inverse_orbit = sorted((-a) % 31 for a in orbit)
assert len(orbit) == 5 and set(orbit).isdisjoint(inverse_orbit)
assert order_mod(2,31**2) == 155
sextic = {
    'dimension':10,
    'order31_eigenvalue_degree':5,
    'order31_fixed_dimension':5,
    'GammaL5_4_fixed_dimension_must_be_even':True,
    'GammaL2_32_order':semilinear_order(2,5),
    'GammaL1_1024_order':semilinear_order(1,10),
    'required_prime_divisor':7,
}
assert sextic['GammaL2_32_order'] % 7 != 0
assert sextic['GammaL1_1024_order'] % 7 != 0
assert gl_order(5,2) % 7 == 0
septic = {
    'ambient_dimension':15,
    'quotient_dimension':14,
    'nonfixed_theta_orbit_size':2**15-2,
    'quotient_nonzero_orbit_size':2**14-1,
    'order31_fixed_dimension_before_quotient':10,
    'order31_fixed_dimension_after_quotient':9,
    'GammaL7_4_fixed_dimension_must_be_even':True,
    'GammaL2_128_order':semilinear_order(2,7),
    'GammaL1_16384_order':semilinear_order(1,14),
    'required_prime_divisor':11,
    'GL10_order_divisible_by_11':gl_order(10,2) % 11 == 0,
}
assert septic['GL10_order_divisible_by_11']
assert septic['GammaL2_128_order'] % 11 != 0
assert septic['GammaL1_16384_order'] % 11 != 0
assert 2*septic['quotient_nonzero_orbit_size'] == septic['nonfixed_theta_orbit_size']
result = {
    'multiplicative_order_2_mod_31':order_mod(2,31),
    'multiplicative_order_2_mod_961':order_mod(2,961),
    'primitive31_frobenius_orbit':orbit,
    'inverse_orbit':inverse_orbit,
    'nonreciprocal_irreducible_factor':True,
    'sextic':sextic,
    'septic':septic,
    'elapsed_seconds':time.perf_counter()-started,
    'scope':'Integer/order certificates, not a new computation of Hering classification or geometric monodromy.'
}
out=Path(__file__).resolve().parents[1]/'outputs'/'sextic_septic_group_checks.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
