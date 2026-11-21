"""Independent finite check of G033's actual rank-two triple trace.

The left side expands the three normal-slot polynomial and extracts its
Schur coefficients by the two-variable alternant.  The right side uses
only the two geometric-series factors for each literal selected cycle.
No polynomial certificate or representation evaluator is imported.
"""
from collections import defaultdict
from pathlib import Path
import hashlib
import json


def normal_character(eta, k):
    result = {(0, 0): 1}
    for ell in eta:
        factor = {(ell*i, ell*j): 1
                  for i in range(k) for j in range(k-i)}
        out = defaultdict(int)
        for (a, b), c in result.items():
            for (i, j), d in factor.items():
                out[a+i, b+j] += c*d
        result = dict(out)
    return result


def horizontal_strip_trace(poly, a, b, epsilon):
    total = 0
    for p in range(b, a+1):
        for q in range(b+1):
            coefficient = poly.get((p, q), 0)-poly.get((p+1, q-1), 0)
            total += coefficient*epsilon**(a+b-p-q)
    return total


def geometric_tail(eta, epsilon, degree):
    if degree < 0:
        return 0
    values = [1]+[0]*degree
    for ell in eta:
        for scalar in (1, epsilon**ell):
            for n in range(ell, degree+1):
                values[n] += scalar*values[n-ell]
    return values[degree]


def main():
    digest = hashlib.sha256()
    cases = 0
    nonzero_second = 0
    zero_second = 0
    for k in range(2, 13):
        for eta in ((1, 1, 1), (2, 1), (3,)):
            poly = normal_character(eta, k)
            for epsilon in (-1, 1):
                for t in range(k-1):
                    b = 3*k-3-t
                    assert b > 2*(k-1)
                    for x in range(2*k+1):
                        a = b+x
                        actual = horizontal_strip_trace(poly, a, b, epsilon)
                        second = geometric_tail(eta, epsilon, t-x-1)
                        predicted = epsilon**(x+k-1)*(
                            geometric_tail(eta, epsilon, t)-second)
                        assert actual == predicted, (k, eta, epsilon, t, x,
                                                     actual, predicted)
                        cases += 1
                        nonzero_second += second != 0
                        zero_second += second == 0
                        digest.update((repr((k, eta, epsilon, t, x, actual))+'\n').encode())
    receipt = {
        'statement': 'G033 ZW.4-ZW.7',
        'method': 'literal normal-polynomial expansion plus rank-two alternant '
                  'and horizontal-strip extraction versus independent geometric recurrence',
        'k_range': [2, 12],
        'selected_cycles': [[1, 1, 1], [2, 1], [3]],
        'complementary_eigenvalues': [-1, 1],
        't_range': '0 <= t <= k-2',
        'x_range': '0 <= x <= 2k',
        'cases': cases,
        'nonzero_second_boundary': nonzero_second,
        'zero_second_boundary': zero_second,
        'sha256': digest.hexdigest(),
        'result': 'PASS',
    }
    path = Path(__file__).with_name('TRIPLE_TAIL_IDENTITY_RECEIPT.json')
    path.write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
