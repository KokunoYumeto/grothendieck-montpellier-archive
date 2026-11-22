"""Construct R-NEW003's denominator and check its character convention.

This does not evaluate all 3196 numerator coefficients. Their finite
definition is in branches/root/h4_finite_rational.tex. The optional
prefix computation here is only a convention/arithmetic check.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import json
import sympy as sp
from symmetric_character import partitions, centralizer_size, character

ROOT = Path(__file__).resolve().parents[1]
t = sp.Symbol('t')

def multiply(a,b):
    out = [0]*(len(a)+len(b)-1)
    for j,x in enumerate(a):
        if x:
            for k,y in enumerate(b):
                if y:
                    out[j+k] += x*y
    return out

denominator = [1]
factors = []
for m in range(1,25):
    if m == 16:
        continue
    exponent = 1 if m == 8 else 19
    polynomial = 1-t if m == 1 else sp.cyclotomic_poly(m,t)
    coefficients = [int(x) for x in reversed(sp.Poly(polynomial,t).all_coeffs())]
    factors.append({'order':m,'exponent':exponent,'polynomial':str(polynomial)})
    for _ in range(exponent):
        denominator = multiply(denominator,coefficients)
assert len(denominator) == 3197 and denominator[0] == 1

perms = list(permutations(range(4)))
signs = [(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4)) for p in perms]

def vandermonde_character(s,cycles):
    target = (s+3,s+2,s+1,s)
    weights = {(0,0,0,0):1}
    for r in cycles:
        nxt = defaultdict(int)
        for weight,value in weights.items():
            for i in range(4):
                new = list(weight); new[i] += r
                if new[i] <= target[i]:
                    nxt[tuple(new)] += value
        weights = nxt
    result = 0
    for p,sign in zip(perms,signs):
        needed = tuple(target[i]-(3-p[i]) for i in range(4))
        if min(needed) >= 0:
            result += sign*weights.get(needed,0)
    return result

values = []
class_checks = 0
for s in range(5):
    value = Fraction(0)
    for rho in partitions(4*s):
        c = vandermonde_character(s,rho)
        assert c == character((s,s,s,s),rho)
        value += Fraction(c**3,centralizer_size(rho))
        class_checks += 1
    assert value.denominator == 1
    values.append(int(value))
assert values == [1,0,1,1,5]
known = json.loads((ROOT/'certificates'/'k4_small_values.json').read_text())['values']
prefix = [sum(denominator[j-s]*v for s,v in enumerate(known[:j+1]))
          for j in range(len(known))]
result = {'statement':'R-NEW003','degree':3196,'constant_term':1,
          'factors':factors,'coefficients_low_to_high':denominator,
          'numerator_prefix_through_s12':prefix,
          'character_convention_checks':class_checks,
          'independent_prefix_s0_through_s4':values,
          'scope':'Explicit denominator and convention check; full finite numerator not expanded.'}
(ROOT/'certificates'/'H4_denominator.json').write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k not in ('factors','coefficients_low_to_high')}))
