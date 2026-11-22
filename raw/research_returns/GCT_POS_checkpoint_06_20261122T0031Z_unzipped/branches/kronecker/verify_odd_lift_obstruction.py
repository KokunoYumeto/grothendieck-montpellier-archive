"""Exact dimension-three moment check and n26 determinant-character lift."""
from pathlib import Path
from math import gcd
import json
import sympy as sp

root = Path(__file__).resolve().parent
T = sp.MutableDenseNDimArray.zeros(3, 3, 3)
T[0, 0, 0] = sp.sqrt(sp.Rational(2, 3))
T[0, 1, 2] = -1 / sp.sqrt(6)
T[1, 1, 2] = 1 / sp.sqrt(2)
T[0, 2, 1] = -1 / sp.sqrt(6)
T[1, 2, 1] = -1 / sp.sqrt(2)
for b, c in ((0, 2), (1, 1), (2, 0)):
    T[2, b, c] = 1 / sp.sqrt(3)
for mode in range(3):
    marginal = sp.zeros(3)
    for i in range(3):
        for j in range(3):
            for a in range(3):
                for b in range(3):
                    left = [a, b]
                    right = [a, b]
                    left.insert(mode, i)
                    right.insert(mode, j)
                    marginal[i, j] += T[tuple(left)] * sp.conjugate(T[tuple(right)])
    assert marginal.applyfunc(sp.simplify) == sp.eye(3)
weights3 = [[0, 0, 1], [0, 1, 2], [0, 1, 2]]
for i in range(3):
    for j in range(3):
        for k in range(3):
            if T[i, j, k]:
                assert (weights3[0][i] + weights3[1][j] + weights3[2][k]) % 3 == 0
assert sum(map(sum, weights3)) % 3 == 1
record = next(row for row in json.loads((root / 'amplifier_spectral_diagnostics_output4.json').read_text()) if row['k'] == 3)
D = 2 ** 25
assert record['n'] == 23 and record['M'] == D
weights26 = [[3 * value for value in old] + [D * value for value in new]
             for old, new in zip(record['W'], weights3)]
exponent = sum(map(sum, weights26)) % (3 * D)
assert gcd(exponent, 3 * D) == 1
assert all(sum(weights26[a][edge[a]] for a in range(3)) % (3 * D) == 0 for edge in record['support'])
(root / 'odd_lift_obstruction_checks.json').write_text(json.dumps({
    'status': 'PASS', 'dimension3_marginals': 'three identity matrices',
    'dimension3_character_exponent_mod3': 1, 'dimension26_order': 3 * D,
    'dimension26_character_exponent': exponent, 'dimension26_spectra': weights26,
    'scope': 'Explicit critical point and stabilizer element; no full-stabilizer or global-pole assertion.'}, indent=2))
print('PASS K-025: exact n3 critical frame and primitive character3; n26 block lift primitive character 3*2^25.')
