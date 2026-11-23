"""Exact monomial certificates for the explicit HD-I18 tuples.

This finite calculation checks the displayed identities on 54 parameter
choices.  Universal generation and the geometric jet proof are separate
arguments in two_full_fiber_components.tex.
"""
from pathlib import Path
import json

TABLE = [(3, 1, 1, 2), (3, 3, 1, 1),
         (4, 1, 1, 3), (4, 2, 2, 3), (4, 4, 1, 2),
         (6, 1, 1, 5), (6, 2, 2, 5), (6, 3, 1, 1), (6, 6, 1, 4)]


def run(d, e, n, m, u, v):
    ident = (tuple(range(m)), (0,) * m)

    def mul(x, y):
        px, cx = x
        py, cy = y
        return (tuple(px[py[j]] for j in range(m)),
                tuple((cy[j] + cx[py[j]]) % d for j in range(m)))

    def inverse(x):
        p, c = x
        q = [0] * m
        for j, k in enumerate(p):
            q[k] = j
        return (tuple(q), tuple((-c[q[j]]) % d for j in range(m)))

    def power(x, j):
        ans = ident
        for _ in range(j):
            ans = mul(ans, x)
        return ans

    def swap(a, b, color=0):
        p, c = list(range(m)), [0] * m
        p[a], p[b] = b, a
        c[a], c[b] = color % d, -color % d
        return tuple(p), tuple(c)

    def cycles(x):
        p, c = x
        seen, out = set(), []
        for start in range(m):
            if start in seen:
                continue
            j, length, color = start, 0, 0
            while j not in seen:
                seen.add(j)
                length += 1
                color += c[j]
                j = p[j]
            out.append((length, color % d))
        return out

    a = m - 2
    p, c = list(range(m)), [0] * m
    for j in range(a - 1):
        p[j] = j + 1
    p[a - 1], c[a - 1] = 0, 1
    c[m - 2], c[m - 1] = u, v
    A = tuple(p), tuple(c)
    B = inverse(A)
    s, t, w, sp = swap(0, 1), swap(0, m - 2), swap(0, m - 1), swap(0, 1, 1)
    tup = [A, B, s, s, t, t, w, w, sp, sp] + [s, s] * (n - 4)
    assert len(tup) == 2 * n + 2
    product = ident
    for x in tup:
        assert sum(x[1]) % e == 0
        product = mul(product, x)
    assert product == ident
    assert all(mul(x, x) == ident for x in (s, t, w, sp))

    for j in range(a - 1):
        Aj = power(A, j)
        assert mul(mul(Aj, s), inverse(Aj)) == swap(j, j + 1)
    aug = mul(sp, s)
    assert aug == (tuple(range(m)), ((d - 1), 1) + (0,) * (m - 2))
    plain_cycle = (A[0], (0,) * m)
    diag = mul(A, inverse(plain_cycle))
    assert diag[0] == ident[0]
    assert sum(diag[1]) % d == e % d

    all_cycles = [cycles(x) for x in tup]
    assert all(color != 0 for cyc in all_cycles[:2] for _, color in cyc)
    assert sorted(all_cycles[0]) == sorted([(a, 1), (1, u), (1, v)])
    assert sorted(all_cycles[1]) == sorted([(a, d - 1), (1, d - u), (1, d - v)])
    deficits = [sum(length - 1 for length, _ in cyc) for cyc in all_cycles]
    codims = [sum(length - 1 + (color != 0) for length, color in cyc)
              for cyc in all_cycles]
    assert codims[:2] == [m, m] and codims[2:] == [1] * (2 * n)
    genus = 1 - m + sum(deficits) // 2
    assert sum(deficits) % 2 == 0 and genus == n - 2
    visible = [color for cyc in all_cycles for _, color in cyc if color]
    assert len(visible) == 6 and sum(visible) == 3 * d
    assert genus - 1 + sum(visible) // d == n
    assert sum(codims) - 2 * m == 2 * n
    N, jet_length = sum(codims) - len(tup), 2 * m
    J_rank = 2 * m - genus - 2
    forget_rank = 2 * n + genus - 1 - N + J_rank
    assert N == 2 * m - 2 and N - J_rank == genus
    assert forget_rank == 2 * n - 1
    assert jet_length > 2 * m - 2 * genus + 1
    return {"d": d, "e": e, "n": n, "m": m, "genus": genus,
            "first_cycle_colors": all_cycles[0], "visible_branch_count": 6,
            "jet_length": jet_length, "constraint_count": N,
            "jet_rank": J_rank, "forget_and_period_rank": forget_rank}


results = []
for d, e, u, v in TABLE:
    for n in (5, 8, 13):
        least = (n * n - 2 * n + 4) // 2
        for m in (least, least + 1):
            results.append(run(d, e, n, m, u, v))
assert len(results) == 54
out = {"check": "PASS", "cases": results,
       "scope": "Exact monomial products, explicit generating-word identities, cycle colors, genus/signature and rank arithmetic; universal geometric proof is separate."}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
print("PASS: 54 exact tuples; all colors, generating-word identities, balanced signatures and rank formulas")
