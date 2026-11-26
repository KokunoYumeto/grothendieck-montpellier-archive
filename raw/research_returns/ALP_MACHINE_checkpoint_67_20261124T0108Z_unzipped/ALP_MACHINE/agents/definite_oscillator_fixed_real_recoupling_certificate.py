#!/usr/bin/env python3
"""Exact diagnostics for AM-DO-050; no automorphic computation."""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction as Q
from itertools import permutations, product
from math import factorial as fac, comb
from pathlib import Path
import hashlib
import json

ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def pmul(p, q):
    ans = defaultdict(int)
    for a, ca in p.items():
        for b, cb in q.items():
            ans[tuple(x + y for x, y in zip(a, b))] += ca * cb
    return {m: c for m, c in ans.items() if c}


def ppow(p, n, nv):
    ans = {(0,) * nv: 1}
    for _ in range(n):
        ans = pmul(ans, p)
    return ans


def var(i, n=8):
    m = [0] * n
    m[i] = 1
    return {tuple(m): 1}


def padd(p, q, scale=1):
    ans = defaultdict(int, p)
    for m, c in q.items():
        ans[m] += scale * c
    return {m: c for m, c in ans.items() if c}


def fisher(p, q):
    ans = Q(0)
    for m, c in p.items():
        if m in q:
            weight = 1
            for e in m:
                weight *= fac(e)
            ans += c * q[m] * weight
    return ans


def hook(lam):
    n = len(lam)
    a = 1
    b = 1
    for i in range(n):
        a *= fac(lam[i] + n - 1 - i)
        for j in range(i + 1, n):
            b *= lam[i] - lam[j] + j - i
    ans = Q(a, b)
    check(ans.denominator == 1, ("hook_integrality", lam))
    return ans.numerator


def gadd(z, w):
    return z[0] + w[0], z[1] + w[1]


def gmul(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def gscale(z, a):
    return z[0] * a, z[1] * a


def gconj(z):
    return z[0], -z[1]


def ginner(e, f):
    out = (Q(0), Q(0))
    for x, y in zip(e, f):
        out = gadd(out, gmul(x, gconj(y)))
    return out


def compact_projector_checks():
    # Signed permutation averaging is an exact finite 1-design on End(C^d).
    # It tests the linear-first Schur factor without floating-point roots.
    cases = []
    for d in range(1, 6):
        e = [(Q(i + 1, d + 1), Q(2 * i - 1, d + 2)) for i in range(d)]
        f = [(Q(3 - i, d + 3), Q(i + 2, d + 4)) for i in range(d)]
        out = [[(Q(0), Q(0)) for _ in range(d)] for _ in range(d)]
        count = 0
        for p in permutations(range(d)):
            for signs in product((-1, 1), repeat=d):
                ge = [gscale(e[p[i]], signs[i]) for i in range(d)]
                gf = [gscale(f[p[i]], signs[i]) for i in range(d)]
                count += 1
                for i in range(d):
                    for j in range(d):
                        out[i][j] = gadd(out[i][j], gmul(ge[i], gconj(gf[j])))
        trace = ginner(e, f)
        for i in range(d):
            for j in range(d):
                expected = gscale(trace, Q(1, d)) if i == j else (Q(0), Q(0))
                check(gscale(out[i][j], Q(1, count)) == expected,
                      ("Schur_linear_first", d, i, j))
        check(count == 2 ** d * fac(d), ("group_size", d))
        check(ginner([(Q(int(i == 0)), Q(0)) for i in range(d)],
                     [(Q(int(i == 0)), Q(0)) for i in range(d)]) == (Q(1), Q(0)),
              ("matched_extremal", d))
        if d > 1:
            check(ginner([(Q(int(i == 0)), Q(0)) for i in range(d)],
                         [(Q(int(i == 1)), Q(0)) for i in range(d)]) == (Q(0), Q(0)),
                  ("orthogonal_extremal", d))
        cases.append({"dimension": d, "averaging_group_order": count})
    return cases


def polynomial_checks():
    # x1,x2,z31,z32,z11,z12,z21,z22; old determinant uses last four.
    v = [var(i) for i in range(8)]
    radial = padd(pmul(v[0], v[2]), pmul(v[1], v[3]))
    det = padd(pmul(v[4], v[7]), pmul(v[5], v[6]), -1)
    cases = []
    for m in range(7):
        for ell in range(7):
            rp = ppow(radial, m, 8)
            dp = ppow(det, ell, 8)
            poly = pmul(rp, dp)
            hdet = fac(ell) * fac(ell + 1)
            hp = hook((m + ell, ell, 0))
            check(fisher(dp, dp) == hdet, ("det_norm", m, ell))
            check(fisher(rp, rp) == (m + 1) * fac(m) ** 2, ("radial_norm", m, ell))
            norm = (m + 1) * fac(m) ** 2 * hdet
            check(fisher(poly, poly) == norm, ("shuffle_norm", m, ell))
            check(hp == Q(fac(m + ell + 1) * fac(ell), m + 1), ("hook_closed", m, ell))
            kappa = Q(fac(m) * hdet, hp)
            check(kappa == Q(fac(m + 1) * fac(ell + 1), fac(m + ell + 1)),
                  ("branch_kappa", m, ell))
            summands = []
            reconstructed = {}
            for j in range(m + 1):
                xpart = pmul(ppow(v[0], j, 8), ppow(v[1], m - j, 8))
                zpart = pmul(pmul(ppow(v[2], j, 8), ppow(v[3], m - j, 8)), dp)
                term = pmul(xpart, zpart)
                expected = fac(j) * fac(m - j) * hdet
                check(fisher(zpart, zpart) == expected, ("terminal_branch_weight", m, ell, j))
                check(fisher(term, term) == fac(j) ** 2 * fac(m - j) ** 2 * hdet,
                      ("tensor_weight_norm", m, ell, j))
                reconstructed = padd(reconstructed, term, comb(m, j))
                summands.append(term)
            check(reconstructed == poly, ("literal_binomial_coev", m, ell))
            for i, term in enumerate(summands):
                for j, other in enumerate(summands):
                    if i != j:
                        check(fisher(term, other) == 0, ("orthogonal_weights", m, ell, i, j))
            # Funit = poly/(m!sqrt(Hdet)); Eunit = Funit/sqrt(m+1).
            f_norm2 = Q(norm, fac(m) ** 2 * hdet)
            e_norm2 = Q(norm, fac(m) ** 2 * hdet * (m + 1))
            check(f_norm2 == m + 1 and e_norm2 == 1, ("complete_coev_norms", m, ell))
            check(Q(e_norm2, f_norm2) == Q(1, m + 1), ("recoupling_abs", m, ell))
            if m and ell:
                check((m + ell, ell) != (ell, ell), ("non_top_branch", m, ell))
            cases.append({"m": m, "L": ell, "monomials": len(poly),
                          "kappa": str(kappa), "abs_z_squared": str(Q(1, m + 1))})
    return cases


def scale_checks():
    cases = []
    for dv, dh, n0, n1, h0, h1, dpbw, ubr2, kappa in product(
            (1, 2, 7), (1, 3, 5), (1, 6), (1, 10), (1, 2), (1, 6),
            (1, 13), (Q(1), Q(4, 9)), (Q(1), Q(5, 7))):
        z2 = Q(dv, dh)
        raw2 = z2 / dv ** 2 * Q(n0 * n1 * dpbw, h0 * h1) * ubr2 * kappa
        closed2 = Q(n0 * n1 * dpbw, dv * dh * h0 * h1) * ubr2 * kappa
        check(raw2 == closed2, "primitive_compact_scale")
        check(raw2 > 0, "nonzero_scale")
        check(raw2 * dv ** 2 == z2 * Q(n0 * n1 * dpbw, h0 * h1) * ubr2 * kappa,
              "complete_vs_matched")
        check(raw2 / dpbw == Q(n0 * n1, dv * dh * h0 * h1) * ubr2 * kappa,
              "isometric_PBW")
    for a, t, h in ((42, 1759, 1), (168, 1633, 4)):
        r = a + 1
        b = r + t
        nn = b + t
        c = nn + 1
        check(a * b + b * c == r * b + b * nn == 2 * b * b, "rank_balance")
        check(7 * h * (a * b + b * c) == 14 * h * b * b, "vacuum_balance")
        horizontal_c = 14 * h * (a * b + b * c)
        vertical_c = 14 * h * (a * b + b * nn)
        vertical_conj = 14 * h * b
        check(horizontal_c - vertical_c == vertical_conj, "CM_phase_balance")
        cases.append({"a": a, "b": b, "c": c, "r": r, "N": nn,
                      "h": h, "vacuum_det_exponent": 7 * h * b * b,
                      "CM_phase_exponent": vertical_conj})
    return cases


def main():
    compact = compact_projector_checks()
    polys = polynomial_checks()
    scales = scale_checks()
    report = {
        "finding": "AM-DO-050",
        "status": "PASS",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "assertions": ASSERTIONS,
        "scope": "Exact finite compact, Fischer, branch and scale diagnostics only; no automorphic-period claim.",
        "compact_projectors": compact,
        "polynomial_cases": polys,
        "actual_rank_balances": scales,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "assertions": ASSERTIONS,
                      "timestamp_utc": report["timestamp_utc"], "output": str(output)}))


if __name__ == "__main__":
    main()
