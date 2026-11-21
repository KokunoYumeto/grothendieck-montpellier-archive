#!/usr/bin/env python3
"""Verify the stored theta13 certificate by independent symbolic reduction.

Reads coefficients from JSON; does not import producer code. Uses SymPy's
polynomials over F_2 and reduces by z^4+z+1. This validates the principal
norm identity and the evaluations; the divisor proof is in the notes.
"""
import json
from pathlib import Path
import sympy as sp

root = Path(__file__).resolve().parent
data = json.loads((root / 'theta13_direct.json').read_text())
x, z = sp.symbols('x z')


def decode(n):
    return sum(((n >> i) & 1) * z**i for i in range(4))


def reduce(expression):
    # Work over F_2[z,x] with a monic z-polynomial, avoiding any reuse of
    # the finite-field arithmetic in the producer.
    ideal = sp.groebner([z**4 + z + 1], z, x, modulus=2)
    return ideal.reduce(sp.expand(expression))[1]


a = sum(decode(c) * x**i for i, c in enumerate(data['A_coefficients_ascending']))
b = sum(decode(c) * x**i for i, c in enumerate(data['B_coefficients_ascending']))
r, s = [decode(c) for c in data['point_R']]
norm = a**2 + a*b*x**2 + b**2*(x**5+x)
assert reduce(norm - (x+r)**13) == 0
assert reduce(s**2+r**2*s+r**5+r) == 0
assert reduce((a+b*s).subs(x,r)) == 0
other = reduce((a+b*(s+r**2)).subs(x,r))
assert other == z**2+z
assert sp.degree(a,x)==6 and sp.degree(b,x)==4
assert sp.Poly(b,x).LC()==1
assert sp.Poly(z**4+z+1,z,modulus=2).is_irreducible
assert len({pow(2,i,13) for i in range(12)})==12
result = {
    'status':'PASS',
    'checks':['irreducible field modulus','point equation',
              'independent norm identity','vanishing at R',
              'nonvanishing at conjugate R','exact degree bounds',
              'primitive root 2 modulo 13'],
    'A_symbolic':str(a), 'B_symbolic':str(b),
    'norm_difference_reduced':0,
    'conjugate_value_symbolic':str(other),
    'producer_imported':False
}
(root/'theta13_independent_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
