"""Symbolic finite checks for R-07 and the S4 instance of R-09.

These supplement, and do not replace, the written general proofs.
"""
from pathlib import Path
from math import comb
import json
import sympy as sp

b = sp.symbols("b0:9")
checked = []
for j in range(2, 9):
    q = sp.cancel(b[0] ** (j - 1) * sum(
        comb(j, i) * b[i] * (-b[1] / b[0]) ** (j - i)
        for i in range(j + 1)
    ))
    poly = sp.Poly(q, *b)
    assert sp.denom(q) == 1
    raised = sp.expand(sum(i * b[i - 1] * sp.diff(q, b[i]) for i in range(1, 9)))
    assert raised == 0
    assert sp.expand(q.subs({b[0]: 1, b[1]: 0}) - b[j]) == 0
    for exponents, coefficient in poly.terms():
        assert sum(exponents) == j
        assert sum(i * exponents[i] for i in range(9)) == j
    checked.append(j)


def partitions_bounded(q, max_part, max_parts):
    counts = [[0] * (q + 1) for _ in range(max_parts + 1)]
    counts[0][0] = 1
    for part in range(1, max_part + 1):
        for number in range(1, max_parts + 1):
            for weight in range(part, q + 1):
                counts[number][weight] += counts[number - 1][weight - part]
    return sum(counts[k][q] for k in range(max_parts + 1))


def partitions_without_ones(q, n):
    counts = [0] * (q + 1)
    counts[0] = 1
    for part in range(2, n + 1):
        for k in range(part, q + 1):
            counts[k] += counts[k - part]
    return counts[q]


cases = 0
for n in range(2, 9):
    for d in range(11):
        for q in range(d + 1):
            wq = partitions_bounded(q, n, d)
            wm = partitions_bounded(q - 1, n, d) if q else 0
            assert wq - wm == partitions_without_ones(q, n)
            cases += 1

assert partitions_without_ones(4, 4) == 2
q4 = b[0]**3*b[4] - 4*b[0]**2*b[1]*b[3] + 6*b[0]*b[1]**2*b[2] - 3*b[1]**4
q2sq = (b[0]*b[2] - b[1]**2)**2
assert q4.subs({b[0]: 1, b[1]: 0}) == b[4]
assert q2sq.subs({b[0]: 1, b[1]: 0}) == b[2]**2

fourth_moment = (1 * 2**4 + 6 * 0**4 + 3 * 2**4 + 8 * (-1)**4 + 6 * 0**4) // 24
assert fourth_moment == 3
result = {
    "Q_j_symbolic_checks": checked,
    "weight_difference_checks": cases,
    "two_independent_witnesses_for_n_d_q_4": ["Q4", "Q2^2"],
    "R09_S4_fourth_moment": fourth_moment,
    "R09_length_cutoff_sums_for_n_d_2": [1, 2, 2, 3],
    "all_assertions_passed": True,
}
Path(__file__).with_name("centered_witness_results.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
