"""Exact finite checks for ALP-LIFT-07; no numerical theta approximation.

The geometric determinant-of-cohomology and good-model assertions are
proved in finite_theta_null_normalization.md, not inferred from this script.
"""
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import json
import sympy as sp


def add(*vectors):
    return tuple(sum(xs) % 2 for xs in zip(*vectors))


def parity(c):
    m, n = c[:3], c[3:]
    return sum(a*b for a, b in zip(m, n)) % 2


# Adjacent cycles in the ordered integral basis a0,a1,a2,b0,b1,b2.
gamma = [
    (1,0,0,0,0,0), (0,0,0,1,1,0),
    (0,1,0,0,0,0), (0,0,0,0,1,1),
    (0,0,1,0,0,0), (0,0,0,0,0,1),
]
table = [(0,0,0,1,0,0)]
for g in gamma:
    table.append(add(table[-1], g))
expected = [
    (0,0,0,1,0,0), (1,0,0,1,0,0), (1,0,0,0,1,0),
    (1,1,0,0,1,0), (1,1,0,0,0,1), (1,1,1,0,0,1),
    (1,1,1,0,0,0),
]
assert table == expected
assert add(*table) == (0,)*6
solutions = [c for c in product(range(2), repeat=6)
             if parity(c) == 0 and all(parity(add(c,t)) == 1 for t in table)]
K = (1,0,1,1,1,1)
assert solutions == [K]
assert add(table[1],table[3],table[5]) == K
triple_chars = {
    S: add(K, *(table[a] for a in S))
    for S in combinations(range(7), 3)
}
assert len(set(triple_chars.values())) == 35
assert all(parity(c) == 0 and c != K for c in triple_chars.values())
assert [S for S,c in triple_chars.items() if c == (0,)*6] == [(1,3,5)]

# Rational-function differentiation reduced by X^7=Y^2+Y.
X,Y,T = sp.symbols('X Y T')
t = X**3/Y
dYdX = 7*X**6/(2*Y+1)
dt = sp.diff(t,X)+sp.diff(t,Y)*dYdX
claimed = -X**2*(Y+4)/(Y*(2*Y+1))
numerator = sp.together(dt-claimed).as_numer_denom()[0]
assert sp.rem(numerator, X**7-Y**2-Y, X) == 0
for i in (1,2,3):
    eta_dt = -Y*X**(i-3)/(Y+4)
    fi = sp.cancel(t*eta_dt)
    assert sp.simplify(fi.subs(Y,sp.Rational(-1,2))+sp.Rational(2,7)*X**i) == 0

# The exact generic Vandermonde determinant and valuation arithmetic.
x0,x1,x2 = sp.symbols('x0 x1 x2')
xs = (x0,x1,x2)
evaluation = sp.Matrix([[-sp.Rational(2,7)*x**i for x in xs] for i in (1,2,3)])
vandermonde = (x1-x0)*(x2-x0)*(x2-x1)
factorized = (-sp.Rational(2,7))**3*x0*x1*x2*vandermonde
assert sp.factor(evaluation.det()-factorized) == 0
split_valuation = Fraction(3)-Fraction(6,7)-Fraction(6,7)
target_evaluation_valuation = Fraction(3,7)
integral_valuation = split_valuation-target_evaluation_valuation
assert (split_valuation,integral_valuation) == (Fraction(9,7),Fraction(6,7))

cyclotomic = sp.cyclotomic_poly(7,T)
bezout = T**5+2*T**4+3*T**3+4*T**2+5*T+6
assert sp.expand((T-1)*bezout-cyclotomic+7) == 0
assert sp.rem((T-1)*(T**5+T**3+T)-1,cyclotomic,T,domain=sp.GF(2)) == 0

result = {
    'statement':'ALP-LIFT-07',
    'kind':'exact rational, polynomial, and F2 finite certificate; not a formalized geometry proof',
    'branch_halfperiods_m_then_n':table,
    'unique_even_K_with_seven_odd_twists':K,
    'distinct_nonsingular_even_triple_characteristics':len(triple_chars),
    'zero_characteristic_triple':[1,3,5],
    'parameter_differentiation_exact':True,
    'split_evaluation_determinant_exact':True,
    'split_evaluation_v2':str(split_valuation),
    'target_evaluation_v2':str(target_evaluation_valuation),
    'integral_restriction_determinant_v2':str(integral_valuation),
    'cyclotomic_inverse_on_2torsion_exact':True,
}
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
