"""Exact corroboration of STEP7-01; proof is in step7_deeper.md."""
from itertools import combinations
from math import comb
from pathlib import Path
import json


def determinant_integer(a):
    n = len(a)
    if n == 0:
        return 1
    a = [list(row) for row in a]
    sign, divisor = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            p = next((p for p in range(k + 1, n) if a[p][k]), None)
            if p is None:
                return 0
            a[k], a[p] = a[p], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                assert numerator % divisor == 0
                a[i][j] = numerator // divisor
        for i in range(k + 1, n):
            a[i][k] = 0
        divisor = pivot
    return sign * a[-1][-1]


by_size = []
for k in range(7):
    count = 0
    values = set(range(2 * k))
    for us in combinations(values, k):
        u = sorted(us, reverse=True)
        lam = sorted(values - set(us), reverse=True)
        a = [[int(ui > lj) for lj in lam] for ui in u]
        d = determinant_integer(a)
        interlace = all(lam[i] < u[i] for i in range(k)) and all(
            u[i + 1] < lam[i] for i in range(k - 1)
        )
        assert d == int(interlace), (u, lam, a, d)
        count += 1
    assert count == comb(2 * k, k)
    by_size.append({"k": k, "strict_order_patterns": count, "outcome": "pass"})

# The cross-equality endpoint must remain excluded from the strict equivalence.
u, lam = [2, 1], [1, 0]
a = [[int(ui > lj) for lj in lam] for ui in u]
assert determinant_integer(a) == 1 and not u[1] < lam[0]

result = {
    "statement_id": "STEP7-01",
    "method": "exact integer Bareiss determinants over all strict merge-order patterns for k=0,...,6",
    "total_patterns": sum(x["strict_order_patterns"] for x in by_size),
    "by_size": by_size,
    "cross_equality_counterexample": {"u": u, "lambda": lam, "matrix": a, "determinant": 1},
    "scope": "finite corroboration, not a formal certificate or replacement for the proof",
}
Path(__file__).with_name("check_step7_threshold_results.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
