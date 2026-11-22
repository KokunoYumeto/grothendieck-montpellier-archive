"""Exact n=58 certificate for the constructed higher-lift point in K-029.

The same-component assertion is proved geometrically in the manuscript.
This script checks the critical direct sum, its two stabilizer spectra,
the prefix/cluster identification, and the complete fixed-space counts.
No global Hilbert residue is inferred.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
raw = json.loads((ROOT / 'amplifying_gadget_q8.json').read_text())
gadget = [tuple(e) for e in raw['support']]
boundary = tuple(raw['boundary'])
support = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]
masses = [Fraction(1, 2)] * 4
selected = (0, 0, 0)
n = 2
for k in range(1, 9):
    index = support.index(selected)
    r = masses.pop(index)
    support.pop(index)
    maps = []
    for a in range(3):
        other = [j for j in range(8) if j != boundary[a]]
        maps.append({boundary[a]: selected[a],
                     **{j: n+b for b, j in enumerate(other)}})
    added = [tuple(maps[a][e[a]] for a in range(3)) for e in gadget]
    support.extend(added)
    masses.extend((x+y*r)/256 for x, y in
                  zip(raw['intercept_numerators'], raw['slope_numerators']))
    selected = added[4]
    n += 7
    if k == 7:
        prefix_support = list(support)
        prefix_masses = list(masses)
        prefix_selected = selected
        m = n

assert (m, n) == (51, 58)
assert len(prefix_support) == 3*m-2
assert all(x > 0 for x in prefix_masses)
for a in range(3):
    assert all(sum(x for e, x in zip(prefix_support, prefix_masses)
                   if e[a] == j) == 1 for j in range(m))
    pairs = [tuple(e[b] for b in range(3) if b != a)
             for e in prefix_support]
    assert len(set(pairs)) == len(pairs)

record = next(r for r in json.loads((ROOT / 'lower_fixed_loci_checks.json').read_text())['receipts']
              if r['n'] == 58)
M = 1 << 57
assert record['modulus'] == M
W = [[w % M for w in factor] for factor in record['weights']]
assert gcd(sum(map(sum, W)), M) == 1
assert all(sum(W[a][e[a]] for a in range(3)) % M == 0 for e in support)
assert all(sum(W[a][e[a]] for a in range(3)) % M == 0
           for e in prefix_support)
sigma = [W[a][prefix_selected[a]] for a in range(3)]
assert sum(sigma) % M == 0
assert all(all(w == sigma[a] for w in W[a][m:]) for a in range(3))
prefix_character = sum(sum(factor[:m]) for factor in W) % M
assert gcd(prefix_character, M) == 1

small = {
    (0, 0, 0): sp.sqrt(sp.Rational(2, 3)),
    (0, 1, 2): -1/sp.sqrt(6),
    (1, 1, 2): 1/sp.sqrt(2),
    (0, 2, 1): -1/sp.sqrt(6),
    (1, 2, 1): -1/sp.sqrt(2),
    (2, 0, 2): 1/sp.sqrt(3),
    (2, 1, 1): 1/sp.sqrt(3),
    (2, 2, 0): 1/sp.sqrt(3),
}
for a in range(3):
    marginal = sp.zeros(3)
    for e, x in small.items():
        for f, y in small.items():
            if all(e[b] == f[b] for b in range(3) if b != a):
                marginal[e[a], f[a]] += x*sp.conjugate(y)
    assert marginal.applyfunc(sp.simplify) == sp.eye(3)

vsmall = [[0, 0, 1], [0, 1, 2], [0, 1, 2]]
assert all(sum(vsmall[a][e[a]] for a in range(3)) % 3 == 0 for e in small)
v = [[0]*m + vsmall[a] + [0]*(n-m-3) for a in range(3)]
assert sum(map(sum, v)) % 3 == 1
combined_modulus = 3*M
combined = [[(3*W[a][j]+M*v[a][j]) % combined_modulus
             for j in range(n)] for a in range(3)]
direct_support = prefix_support + [tuple(m+j for j in e) for e in small]
direct_support += [(j, j, j) for j in range(m+3, n)]
assert len(direct_support) == 163
assert all(sum(W[a][e[a]] for a in range(3)) % M == 0
           for e in direct_support)
assert all(sum(combined[a][e[a]] for a in range(3)) % combined_modulus == 0
           for e in direct_support)
character = sum(map(sum, combined)) % combined_modulus
assert gcd(character, combined_modulus) == 1

fixed_v = sum(sum(e) % M == 0 for e in product(*W))
fixed_sl = sum(sum(c*c for c in Counter(factor).values()) for factor in W)-3
assert (fixed_v, fixed_sl, fixed_v-fixed_sl) == (697, 339, 358)

receipt = {
    'status': 'PASS', 'finding': 'K-029', 'n': n, 'prefix_n': m,
    'cluster_size': 8, 'M': M, 'higher_order': combined_modulus,
    'prefix_selected_edge': prefix_selected,
    'prefix_character_exponent_mod_M': prefix_character,
    'higher_character_exponent': character,
    'higher_character_gcd': gcd(character, combined_modulus),
    'complete_fixed_counts': {'V': fixed_v, 'SL': fixed_sl, 'quotient': 358},
    'prefix_support': prefix_support,
    'prefix_masses': [str(x) for x in prefix_masses],
    'small_block_coefficients': {','.join(map(str, e)): str(x)
                                 for e, x in small.items()},
    'direct_sum_support': direct_support,
    'dyadic_spectra': W,
    'higher_lift_spectra': combined,
    'checks': ['positive prefix masses with every margin one',
               'prefix free support, hence zero off-diagonal moments',
               'exact symbolic 3-block identity marginals',
               'new coordinates collapse onto selected old edge weights',
               'complete dyadic fixed-space counts',
               'all direct-sum coordinates fixed by both displayed elements',
               'determinant-product character primitive of order 3*M'],
    'scope': 'The component-incidence proof is in AMPLIFIED_COLLISION_COMPONENTS.tex; no global pole assertion.'
}
(ROOT / 'amplified_collision_component_checks.json').write_text(json.dumps(receipt, indent=2)+'\n')
print('PASS K-029 n58: critical direct sum in the same fixed vector space; primitive character 3*2^57; complete fixed dimensions 697-339=358.')
