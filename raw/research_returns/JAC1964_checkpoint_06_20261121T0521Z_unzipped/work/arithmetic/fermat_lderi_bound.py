#!/usr/bin/env python3
"""Fermat rank-two CM L-prime(2): exact coefficients and a certified interval.

Run JAC1964-20261121; GPT-6 Astra Pro; effort setting not exposed.
This numerical check is supplementary to the elementary >7/20 proof.
Analytic input: the normalized CM theta series of chi=psi^3*mu,
conductor (1+i)^4, weight 4, level 64, root number -1.
"""
from flint import arb, ctx
from math import isqrt
import json
from pathlib import Path

ctx.prec = 160
cutoff = 20
coefficients = {}
for n in range(1, cutoff + 1):
    if n % 2 == 0:
        coefficients[n] = 0
        continue
    mu = 1 if n % 8 in (1, 7) else -1
    re = im = 0
    for a in range(-isqrt(n), isqrt(n) + 1):
        for b in range(-isqrt(n), isqrt(n) + 1):
            if a*a+b*b != n:
                continue
            # alpha=a+bi is the unique primary generator of its ideal:
            # alpha == 1 mod (2+2i).
            if (a-1+b) % 4 or (b-a+1) % 4:
                continue
            re += mu*(a*a*a-3*a*b*b)
            im += mu*(3*a*a*b-b*b*b)
    assert im == 0
    coefficients[n] = re
assert {n:a for n,a in coefficients.items() if a} == {1:1,5:-22,9:-27,13:18,17:-94}

c=arb.pi()/4
partial=arb(0)
for n,a in coefficients.items():
    x=c*n
    partial += 2*arb(a)/(n*n)*((-x).exp()-(-x).ei())
# |a_n| <= 2*n^2 and E1(x) <= exp(-x)/x.
tail=4*(1+1/(c*(cutoff+1)))*(-c*(cutoff+1)).exp()/(1-(-c).exp())
lower=partial-tail
upper=partial+tail
assert lower > arb('1.5071685')
assert upper < arb('1.5071697')
result = dict(cutoff=cutoff, nonzero_coefficients={n:a for n,a in coefficients.items() if a},
    partial_sum=str(partial), tail_upper_bound=str(tail),
    certified_lower=str(lower), certified_upper=str(upper),
    rational_interval=['1.5071685','1.5071697'],
    analytic_elementary_lower_bound='7/20',
    scope='Arithmetic interval check conditional only on the stated known CM identification and functional equation; no height identity asserted.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
