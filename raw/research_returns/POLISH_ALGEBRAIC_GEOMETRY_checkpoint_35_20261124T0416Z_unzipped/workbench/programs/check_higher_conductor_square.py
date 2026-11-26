#!/usr/bin/env python3
"""Exact arithmetic corroboration; not a certificate of the geometric inputs.

Run: python workbench/programs/check_higher_conductor_square.py
Method: symbolic intersection substitution and exact rational boundary checks.
The proof itself derives the identities by hand; this program independently
substitutes the Euler formula into the intersection pairing and eliminates g.
"""
from fractions import Fraction
import json
from pathlib import Path
import sympy as s

p, a, d, c2, chiN = s.symbols('p a d c2 chiN')
m = p*a
chiX = chiN/p + (p-1)*a*((p+1)*a-3)*d/12
K2 = 12*chiX-c2
KY = (m-1)*d
square = K2-2*(m-2)*KY+(m-2)**2*d
assert s.expand(square-(12*chiN/p-c2-a*(a+p-3)*d)) == 0
q = a*(p-1)+3
num = (p-1)*a*a+(p*p-4*p+6)*a+p-3
assert s.expand(q*(a+p-3)-2*(p-3)-num) == 0
assert s.expand(num.subs(a,1)-((p-1)**2+1)) == 0
assert s.cancel(num.subs(p,3)/q.subs(p,3)-a) == 0
count = 4
for pp in (2,3,5,7,11,13,17,19,23,29,31):
    for aa in range(1,41):
        qq = aa*(pp-1)
        for bb in range(1,qq+3):
            assert bb*bb-(qq+3)*bb+2 < 0
            count += 1
        bb = qq+3
        for dd in (1,2,3,11,37):
            if pp == 2:
                for gg in (1,2,5,19):
                    assert -2*(gg-1)-aa*(aa-1)*dd <= 0
                    count += 1
            else:
                # Set the ramification inequality to its maximal g boundary.
                gminus1 = Fraction(pp*aa*dd,2*bb)
                upper = Fraction(4*(pp-3),pp)*gminus1-aa*(aa+pp-3)*dd
                nn = (pp-1)*aa*aa+(pp*pp-4*pp+6)*aa+pp-3
                assert upper == -Fraction(aa*dd*nn,bb)
                assert upper < 0
                count += 2
result = {'status':'PASS','assertions':count,
          'method':'Symbolic intersection-pairing substitution; exact rational extremal genus and fiber-degree checks',
          'scope':'Arithmetic only; no computational proof of normalization, ruledness, separability, cohomology or nefness'}
out = Path(__file__).resolve().parents[1]/'records/HIGHER_CONDUCTOR_SQUARE_ARITHMETIC.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
