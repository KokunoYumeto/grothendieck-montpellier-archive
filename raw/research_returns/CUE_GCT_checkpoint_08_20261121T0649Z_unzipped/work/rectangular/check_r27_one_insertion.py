"""Bounded author audit of the R27 central insertion, not its uniform proof.

Reconstruct all three projected jets at size18 and compare them with the
x/y/z row embedding of the saved size17 core.  Arithmetic is exact mod101.
"""
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from check_jacobi_repair import build


def main():
    directory = Path(__file__).resolve().parent / 'border_ternary'
    old = np.load(directory / 'jacobi_boundary_repair_m17.npz')
    data = json.loads((directory / 'jacobi_boundary_repair_m17.json').read_text())
    prime = 101
    alpha, delta = data['alpha'], data['delta_with_zero_cut']
    alpha = alpha[:9] + [1] + alpha[9:]
    delta = delta[:8] + [0, 0] + delta[9:]
    m = 18
    base = np.array([[1, 0, 0], [0, 1, 0], [1, 0, 0], [0, 0, 1]])
    change = np.array(data['change'])
    allowed = set(range(6)) | set(range(m - 5, m))
    labels = ([0, 1, -1]
              + [s for i in range(m) for s in [i, i + 1, i - 1]]
              + [s for i in range(m) for s in [-i, -i + 1, -i - 1]]
              + list(range(m)) + [-i for i in range(m)])
    columns = [i for i, character in enumerate(labels) if character % m in allowed]
    unit_delta = [x if x else 1 for x in delta]
    product = 1
    for value in unit_delta:
        product = product * value % prime

    values = []
    for epsilon in range(4):
        forms = (base + epsilon * change) % prime
        matrix, monomials = build(m, alpha, delta, forms, prime)
        unit_matrix, _ = build(m, alpha, unit_delta, forms, prime)
        weights = np.array([b - c for a, b, c in monomials])
        rows = [i for i, weight in enumerate(weights) if weight % m in allowed]
        negative = [i for i, weight in enumerate(weights)
                    if -m - 5 <= weight <= -m + 5]
        matrix[negative] = unit_matrix[negative] * pow(product, -1, prime) % prime
        values.append(matrix[np.ix_(rows, columns)])

    weights1 = [-11 * pow(6, -1, prime) % prime, 3,
                -3 * pow(2, -1, prime) % prime, pow(3, -1, prime)]
    weights2 = [1, -5 * pow(2, -1, prime) % prime, 2,
                -pow(2, -1, prime) % prime]
    jets = [values[0],
            sum(w * value for w, value in zip(weights1, values)) % prime,
            sum(w * value for w, value in zip(weights2, values)) % prime]
    lookup = {monomials[i]: j for j, i in enumerate(rows)}
    checks = []
    for order, jet in enumerate(jets):
        expected = np.zeros_like(jet)
        for i, (x, y, z) in enumerate(old['monomials']):
            weight = y - z
            if -5 <= weight <= 5:
                target = (x + 1, y, z)
            elif weight >= 12:
                target = (x, y + 1, z)
            elif weight <= -12:
                target = (x, y, z + 1)
            else:
                raise AssertionError((x, y, z))
            expected[lookup[target]] = old['C' + str(order)][i]
        assert np.array_equal(expected, jet)
        checks.append({'order': order, 'shape': list(jet.shape),
                       'all_entries_match': True, 'entries': int(jet.size)})
    result = {
        'checked_utc': datetime.now(timezone.utc).isoformat(),
        'scope': ('Author check of one central insertion m17 to m18, including '
                  'all three projected jet matrices; uniform iteration remains '
                  'a mathematical argument'),
        'prime': prime, 'old_shape': list(old['C0'].shape),
        'new_shape': list(jets[0].shape), 'checks': checks,
    }
    (directory / 'r27_one_insertion_check.json').write_text(
        json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
