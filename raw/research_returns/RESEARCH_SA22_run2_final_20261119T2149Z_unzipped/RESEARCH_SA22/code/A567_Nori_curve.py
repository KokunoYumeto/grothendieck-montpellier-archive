#!/usr/bin/env python3
"""Exact F_4 parameter and polynomial certificate for the Pauly example.

F_4 = F_2[a]/(a^2+a+1), encoded by two bits.  This checks only the
explicit algebraic substitutions.  Smoothness/ordinarity and the family
of F^4-trivial bundles use the opened, precisely cited source theorems.
"""
import json
from pathlib import Path
from time import perf_counter

started = perf_counter()

def add(u, v):
    return u ^ v

def mul(u, v):
    ans = 0
    while v:
        if v & 1:
            ans ^= u
        v >>= 1
        u <<= 1
        if u & 4:
            u ^= 7
    return ans

def psum(*polynomials):
    ans = [0] * max(map(len, polynomials))
    for p in polynomials:
        for i, c in enumerate(p):
            ans[i] ^= c
    while len(ans) > 1 and ans[-1] == 0:
        ans.pop()
    return ans

def pmul(p, q):
    ans = [0] * (len(p) + len(q) - 1)
    for i, c in enumerate(p):
        for j, d in enumerate(q):
            ans[i+j] ^= mul(c, d)
    return psum(ans)

a = b = 1
c = alpha = 2
condition = mul(a,a) ^ mul(b,b) ^ mul(c,c) ^ a ^ c
abc = mul(mul(a,b),c)
alpha_relation = mul(alpha,alpha) ^ alpha ^ 1
numerator = [c,c,a^b,a]
# x(x+1)*(x+1 + alpha/x + 1/(x+1))
partial_fraction_numerator = psum(pmul(pmul([0,1],[1,1]),[1,1]),
                                  pmul([alpha],[1,1]),[0,1])
assert condition == 0
assert abc != 0
assert alpha_relation == 0
assert numerator == partial_fraction_numerator
elapsed_seconds = perf_counter() - started
result = {
    "field": "F_2[alpha]/(alpha^2+alpha+1)",
    "encoding": {"0":0,"1":1,"alpha":2,"alpha+1":3},
    "parameters": {"a":a,"b":b,"c":c},
    "alpha_squared_plus_alpha_plus_one": alpha_relation,
    "a_squared_plus_b_squared_plus_c_squared_plus_a_plus_c": condition,
    "abc":abc,
    "numerator_coefficients_low_to_high":numerator,
    "partial_fraction_numerator_coefficients_low_to_high":partial_fraction_numerator,
    "checks_count":4,
    "elapsed_seconds":elapsed_seconds,
    "run_note":"Subsequent timed run; the first successful run was not timed",
    "proved_by_this_program":"Exact finite-field and polynomial substitutions only",
    "status":"PASS"
}
out = Path(__file__).resolve().parents[1] / "logs" / "A567_Nori_curve.json"
out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
