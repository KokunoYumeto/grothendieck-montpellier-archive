"""Exploratory quotient ranks for both local 2x3 identities.

This file deliberately makes no uniform-rank claim.
"""
import json
from pathlib import Path

# Importing the checker re-runs its small exact checks; its own output is
# unchanged and retained separately.
from check_simultaneous_chords import field_for, product_coefficients, rank_columns


def linear_mul(coefficients, c, p):
    out = [0] * (len(coefficients) + 1)
    for i, a in enumerate(coefficients):
        out[i] = (out[i] + a) % p
        out[i + 1] = (out[i + 1] - c * a) % p
    return out


results = []
for m in [6, 8, 10, 12, 14]:
    p, zeta = field_for(m)
    roots = [pow(zeta, i, p) for i in range(m)]
    for c, d in [(0, 0), (0, roots[2]), (roots[1], roots[2]), (2, 3)]:
        failures, successes, boundary = [], 0, []
        for k in range(2, m - 1):
            a = product_coefficients(range(k, m), roots, p)
            b = product_coefficients(range(k - 1), roots, p)
            ta = linear_mul(product_coefficients(range(k + 1, m), roots, p), c, p)
            tb = linear_mul(product_coefficients([0] + list(range(2, k)), roots, p), d, p)
            sa = linear_mul(product_coefficients([1] + list(range(k + 2, m)), roots, p), c, p)
            sb = linear_mul(product_coefficients(range(2, k + 1), roots, p), d, p)
            for t in range(2, m - 1):
                pairs = [(r, t - r) for r in range(m - k + 1) if 0 <= t - r <= k]
                cols = [
                    [a[r] * (b[s] if s < len(b) else 0) % p for r, s in pairs],
                    [a[r] * (b[s - 1] if 1 <= s <= len(b) else 0) % p for r, s in pairs],
                    [ta[r] * tb[s] % p for r, s in pairs],
                    [sa[r] * sb[s] % p for r, s in pairs],
                ]
                normal = rank_columns(cols, p) - rank_columns(cols[:2], p)
                if 3 <= k <= m - 3 and 3 <= t <= m - 3:
                    if normal == 2:
                        successes += 1
                    else:
                        failures.append([k, t, normal])
                else:
                    boundary.append(normal)
        results.append({"m": m, "prime": p, "c": c, "d": d,
                        "interior_rank_two_count": successes,
                        "interior_failures": failures,
                        "boundary_min_rank": min(boundary),
                        "boundary_max_rank": max(boundary)})
path = Path(__file__).with_name('two_normal_family_exploration.json')
path.write_text(json.dumps(results, indent=2) + '\n')
for result in results:
    print(json.dumps(result))
