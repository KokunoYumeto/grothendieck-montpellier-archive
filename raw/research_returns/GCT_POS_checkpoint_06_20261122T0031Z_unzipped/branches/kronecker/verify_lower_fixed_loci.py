"""Exact finite checks for K-021; no floating point or search input.

Small cases use retained exact generator spectra, while n=58 is rebuilt
from the gadget and solved over the rational numbers.  Full tensor
weight counts, not a lower bound from a partial support, are checked.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
from math import gcd
import json
from sympy import Matrix

root = Path(__file__).resolve().parent
raw = json.loads((root / 'amplifying_gadget_q8.json').read_text())
gadget = [tuple(edge) for edge in raw['support']]
boundary = tuple(raw['boundary'])
assert gadget[4] == (7, 5, 5)
assert [sum(edge[a] == gadget[4][a] for edge in gadget) for a in range(3)] == [3, 2, 3]


def count_at(weights, modulus):
    fixed_v = sum(sum(edge) % modulus == 0 for edge in product(*weights))
    fixed_sl = sum(sum(multiplicity ** 2 for multiplicity in Counter(value % modulus for value in factor).values())
                   for factor in weights) - 3
    return fixed_v, fixed_sl, fixed_v - fixed_sl


receipts = []
records = json.loads((root / 'amplifier_spectral_diagnostics_output4.json').read_text())
for record in records:
    k = record['k']
    for levels in range(1, k):
        modulus = 2 * 256 ** (k - levels)
        r = 1 + 7 * levels
        m = 2 + 7 * (k - levels)
        counts = count_at(record['W'], modulus)
        expected = (r ** 3 + 5 * r + 3 * m - 8,
                    3 * r ** 2 + 3 * m - 6,
                    343 * levels ** 3 + 14 * levels + 1)
        assert counts == expected
        for factor in record['W']:
            assert sorted(Counter(value % modulus for value in factor).values()) == [1] * (m - 1) + [r]
        receipts.append({'k': k, 'n': record['n'], 'levels': levels,
                         'modulus': modulus, 'counts': counts})

support = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]
masses = [Fraction(1, 2)] * 4
selected = (0, 0, 0)
n = 2
for k in range(1, 9):
    selected_index = support.index(selected)
    mass = masses.pop(selected_index)
    support.pop(selected_index)
    maps = []
    for a in range(3):
        others = [value for value in range(8) if value != boundary[a]]
        maps.append({boundary[a]: selected[a], **{value: n + j for j, value in enumerate(others)}})
    added = [tuple(maps[a][edge[a]] for a in range(3)) for edge in gadget]
    support.extend(added)
    masses.extend((x + y * mass) / 256 for x, y in zip(raw['intercept_numerators'], raw['slope_numerators']))
    selected = added[4]
    n += 7

assert n == 58 and len(support) == 172
period = 2 * 256 ** 8
rows = [row for row in range(3 * n) if row not in (2 * n - 1, 3 * n - 1)]
incidence = Matrix([[int(edge[a] == i) for edge in support] for a in range(3) for i in range(n)])
minor = incidence[rows, :]
rhs = Matrix([period if edge == selected else 0 for edge in support])
solution = minor.T.inv() * rhs
assert all(value.q == 1 for value in solution)
flat = [0] * (3 * n)
for row, value in zip(rows, solution):
    flat[row] = int(value) % period
weights = [flat[a * n:(a + 1) * n] for a in range(3)]
assert gcd(sum(flat), period) == 1
assert all(sum(weights[a][edge[a]] for a in range(3)) % period == 0 for edge in support)
assert all(len(set(factor)) == n for factor in weights)
modulus = 2 ** (n - 1)
counts = count_at(weights, modulus)
r = 8
m = 51
assert counts == (r ** 3 + 5 * r + 3 * m - 8, 3 * r ** 2 + 3 * m - 6, 358)
for factor in weights:
    assert sorted(Counter(value % modulus for value in factor).values()) == [1] * 50 + [8]
receipts.append({'k': 8, 'n': 58, 'levels': 1, 'modulus': modulus,
                 'period': period, 'character_exponent': sum(flat) % period,
                 'counts': counts, 'weights': weights})
(root / 'lower_fixed_loci_checks.json').write_text(json.dumps({'status': 'PASS', 'receipts': receipts}, indent=2))
print('PASS K-021: six small complete collapse counts and exact n58 generator; target order 2^57 fixed dimensions V=697, SL=339, quotient=358.')
