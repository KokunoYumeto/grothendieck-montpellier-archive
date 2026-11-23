#!/usr/bin/env python3
"""Exact finite diagnostics for AM-DO-068; not a proof of the adelic theorem."""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
from itertools import product, permutations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AGENTS = ROOT / "work" / "agents"
count = 0
groups = Counter()


def check(ok, group):
    global count
    count += 1
    groups[group] += 1
    if not ok:
        raise AssertionError((group, count))


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return list(map(list, zip(*a)))


def inv(a):
    n = len(a)
    z = [list(row) + unit for row, unit in zip(a, eye(n))]
    for j in range(n):
        k = next(i for i in range(j, n) if z[i][j])
        z[j], z[k] = z[k], z[j]
        c = z[j][j]
        z[j] = [x / c for x in z[j]]
        for i in range(n):
            if i != j:
                c = z[i][j]
                z[i] = [x - c * y for x, y in zip(z[i], z[j])]
    return [r[n:] for r in z]


def val(x, p):
    x = F(x)
    if x == 0:
        return 10**6
    a, b, v = abs(x.numerator), x.denominator, 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v


def integral(v, p):
    return all(val(x, p) >= 0 for x in v)


def primitive(v, p):
    return min(val(x, p) for x in v) == 0


def rank_two_primitive(a, p):
    return min(val(a[i][0] * a[j][1] - a[i][1] * a[j][0], p)
               for i in range(len(a)) for j in range(i + 1, len(a))) == 0


def integral_fourier_column(t1, t2, p):
    """Exact integral over F/O by a finite p-power-root character sum.

    It is called only after the first-column indicator. All domains are
    O-periodic. One nonzero first-column coordinate bounds every solution,
    so the displayed finite enumeration misses no admissible O-coset.
    """
    if not integral(t1, p):
        return False, None, 0
    i = min((i for i in range(len(t1)) if t1[i]),
            key=lambda i: val(t1[i], p))
    b = max(0, val(t1[i], p),
            val(t1[i], p) - val(t2[i], p) if t2[i] else 0)
    modulus = p**b
    admissible = []
    coeff = [0] * modulus
    for j in range(modulus):
        u = F(j, modulus)
        if integral([y + u * x for x, y in zip(t1, t2)], p):
            admissible.append(u)
            coeff[j] = 1
    if b == 0:
        nz = bool(admissible)
    else:
        stride = modulus // p
        # Phi_(p^b)=sum_{r=0}^{p-1} X^(r p^(b-1)).
        zero = all(len({coeff[j + r * stride] for r in range(p)}) == 1
                   for j in range(stride))
        nz = not zero
    return nz, admissible[0] if admissible else None, len(admissible)


def bf_tests():
    for p in (3, 5, 7):
        for rho in range(1, 6):
            for ds in product(range(-2, 3), repeat=rho):
                diagonal = all(d <= 0 for d in ds)
                # Explicit primitive-root sums on each simple root.
                roots = []
                for d in ds[:-1]:
                    if d >= 0:
                        roots.append(True)
                    else:
                        coeff = [1] * p**(-d)
                        stride = len(coeff) // p
                        roots.append(not all(
                            len({coeff[j+r*stride] for r in range(p)}) == 1
                            for j in range(stride)))
                second_coordinate = ds[-1] >= 0
                actual = diagonal and all(roots) and second_coordinate
                check(actual == all(d == 0 for d in ds),
                      "BF_exact_Fourier_and_y_orientation")
    # e_last^t u=e_last^t and the actual y*a last-column direction.
    for rho in range(1, 7):
        u = eye(rho)
        for i in range(rho):
            for j in range(i+1, rho):
                u[i][j] = F(i + 2*j + 1)
        last = [[F(i == rho-1) for i in range(rho)]]
        check(mm(last, u) == last, "BF_last_row_U_invariance")
        d = [[F(2**i if i == j else 0) for j in range(rho)]
             for i in range(rho)]
        check(mm(last, d)[0][-1] == 2**(rho-1),
              "BF_source_Levi_y_a")


def fb_tests():
    jmat = [[F(0), F(0), F(1)],
            [F(0), F(1), F(0)],
            [F(1), F(0), F(0)]]
    x = [[F(1), F(0)], [F(0), F(1)], [F(0), F(0)]]
    gram = [[F(0), F(0)], [F(0), F(1)]]
    cases, survivors, cancellations = 0, 0, 0
    for p in (3, 5):
        for perm in permutations(range(3)):
            pm = [[F(j == perm[i]) for j in range(3)] for i in range(3)]
            for ds in product((-1, 0, 1), repeat=3):
                dm = [[F(p)**ds[i] if i == j else F(0)
                       for j in range(3)] for i in range(3)]
                shears = [eye(3)]
                for i, j in ((0, 1), (1, 2), (2, 0)):
                    for c in (F(1), F(1, p)):
                        sh = eye(3)
                        sh[i][j] = c
                        shears.append(sh)
                for sh in shears:
                    hp = mm(mm(pm, dm), sh)
                    hm = mm(mm(jmat, tr(inv(hp))), jmat)
                    tp, tm = mm(inv(hp), x), mm(inv(hm), x)
                    cases += 1
                    check(mm(mm(tr(tm), jmat), tp) == gram,
                          "FB_actual_split_unitary_Gram")
                    results = []
                    for t in (tp, tm):
                        one = [r[0] for r in t]
                        two = [r[1] for r in t]
                        nz, shift, size = integral_fourier_column(one, two, p)
                        results.append((nz, shift))
                        if integral(one, p) and size and not nz:
                            cancellations += 1
                            check(not primitive(one, p),
                                  "FB_nonprimitive_Fourier_cancellation")
                    if not all(z[0] for z in results):
                        continue
                    survivors += 1
                    changed = []
                    for t, (_, shift) in zip((tp, tm), results):
                        tnew = [[r[0], r[1]+shift*r[0]] for r in t]
                        changed.append(tnew)
                        check(all(integral(r, p) for r in tnew),
                              "FB_integral_unipotent_column_choice")
                        check(primitive([r[0] for r in tnew], p),
                              "FB_primitive_isotropic_first_column")
                        check(rank_two_primitive(tnew, p),
                              "FB_whole_frame_direct_summand")
                    check(mm(mm(tr(changed[1]), jmat), changed[0]) == gram,
                          "FB_changed_Gram_and_unit_last_norm")
    check(cases == 2268, "FB_model_count")
    check(survivors > 50 and cancellations > 50, "FB_nonvacuity")
    return {"models": cases, "survivors": survivors,
            "nonprimitive_character_cancellations": cancellations}


def weyl_vector(m, a, b, vec):
    """rho(a,b) f(t)=exp(2pi i b(t+a/2)/m) f(t+a), phases mod 2m."""
    return {t: (vec[(t+a) % m] + 2*b*t + a*b) % (2*m)
            for t in range(m) if (t+a) % m in vec}


def literal_ann_tests():
    details = []
    for m, r in ((8, 4), (9, 3), (16, 8), (25, 5)):
        gamma = list(product(range(0, m, r), repeat=2))
        # Keep the actual doubled lifts: reducing their labels modulo m
        # would discard a central phase when m is odd.
        required = {(2*a, 2*b) for a, b in gamma}
        required |= {(a, 0) for a, b in gamma}
        required |= {(0, b) for a, b in gamma}
        vec = {t: 0 for t in range(0, m, r)}
        for a, b in required:
            check(weyl_vector(m, a, b, vec) == vec,
                  "literal_doubled_half_vacuum")
        ann = [(a, b) for a, b in product(range(m), repeat=2)
               if all((a*d-b*c) % m == 0 for c, d in required)]
        for a, b in ann:
            moved = weyl_vector(m, a, b, vec)
            for c, d in required:
                check(weyl_vector(m, c, d, moved) == moved,
                      "literal_Ann_preserves_both_vacuum_clauses")
        details.append({"modulus": m, "Gamma_step": r,
                        "Ann_size": len(ann)})
    return details


def finite_orbit_tests():
    p = 3
    def modmm(a, b):
        return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b))) % p
                           for j in range(len(b[0]))) for i in range(len(a)))
    def det3(a):
        return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
                -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
                +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])) % p
    x = ((1, 0), (0, 1), (0, 0))
    ident = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    kminus = ((2, 0, 0), (0, 1, 0), (0, 0, 1))
    kk = (ident, kminus)
    cc = {modmm(k, x) for k in kk}
    uu = [((1, u), (0, 1)) for u in range(p)]
    xu = [modmm(x, u) for u in uu]
    uc = [i for i, z in enumerate(xu) if z in cc]
    check(uc == [0], "K_first_character_kernel")
    gcount, support = 0, 0
    for entries in product(range(p), repeat=9):
        h = tuple(tuple(entries[3*i+j] for j in range(3)) for i in range(3))
        if not det3(h):
            continue
        gcount += 1
        # h^{-1} x u in C iff x u in h C; use no inverse.
        hc = {modmm(h, z) for z in cc}
        active = [j for j, z in enumerate(xu) if z in hc]
        rk = any(modmm(modmm(h, k), x) in xu for k in kk)
        check(bool(active) == rk, "finite_RK_orbit_support_equivalence")
        check(len(active) <= 1, "finite_orbit_no_character_cancellation")
        support += bool(active)
    check(gcount == 11232 and support > 0, "finite_G_orbit_nonvacuity")
    return {"GL3_F3_order": gcount, "support_cardinality": support,
            "K_order": 2, "U_C_order": 1}


def fingerprints():
    base = ROOT / "work" / "research" / "alpoge_source"
    paths = [
        base/"Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/TowerEx.lean",
        base/"Development/AbelianVarietyTheory/Definitions/LatticeFrames/KerBF.lean",
        base/"Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsThetaFam.lean",
        base/"Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/WittSmallGroupEmbeddingMemPointwiseStabilizerIso.lean",
        base/"Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/WittDecompSymplInclIsotropicInclAnisotropic.lean",
        base/"Formalism/LocalToGlobal/IndefiniteReal/LocalNewformFunction.lean",
        AGENTS/"definite_oscillator_refs/first2015_witt.pdf",
        AGENTS/"definite_oscillator_refs/hanzer2011_rank_one.pdf",
    ]
    out = {}
    for p in paths:
        check(p.is_file(), "retained_source_fingerprint")
        out[str(p.relative_to(ROOT))] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=AGENTS /
                    "definite_oscillator_finite_loc_certificate.json")
    args = ap.parse_args()
    bf_tests()
    fb = fb_tests()
    ann = literal_ann_tests()
    orbit = finite_orbit_tests()
    sources = fingerprints()
    report = {
        "finding": "AM-DO-068",
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "status": "PASS", "assertions": count, "groups": dict(groups),
        "BF_cases": "rho=1..5, valuations=-2..2, q=3,5,7",
        "FB": fb, "Ann": ann, "orbit": orbit,
        "source_sha256": sources,
        "scope": "Exact finite diagnostics only. No adelic construction, "
                 "Schwartz-density theorem, global period, integral cost, "
                 "or source Host/SizeData is certified by enumeration.",
    }
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("finding", "checked_at",
                                          "status", "assertions")}))


if __name__ == "__main__":
    main()
