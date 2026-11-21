#!/usr/bin/env python3
"""Exact evaluation of the supplied NumDatum numEx, not a Lean kernel run.

Source locators, relative to evidence/lean_source in the delivered package
(or ../lean_evidence in the original working directory):
  Formalism/LocalToGlobal/Divisibility/Numbers.lean
    eQ, sigPar, aPlus, aMinus, Dplus, Dminus, FTypeG, FRamD,
    FInert, FjP, suppP, Fo.
  Formalism/LocalToGlobal/Divisibility/NumbersLemmas.lean
    numEx, hostEx, hostEx_psQ, ex_FRamD, ex_FjP_d, ex_FjP_2, ex_FjP_q.
  Formalism/LocalRingCardinality/DataParams₂.lean
    Scale.X'', lpFeasible, lpF.
  Formalism/LocalRingCardinality/HostCls.lean
    primeClass_eq_splitK_iff', primeClass_eq_signal_iff',
    primeClass_eq_inert_iff_symbols.
  Formalism/LocalRingCardinality/SpanPowerMembership/
    ExampleRanksRankComplement.lean: R0.
    ExampleWeightMiddleEntries.lean: hcV, hcB, hcE.

The constant-input LP formula is proved in section_arithmetic_sl2.tex.
This script separately certifies its primal optimizer and summed-constraint
upper bound for the possible nontrivial orbit lengths 2 and 4 of this example.
It evaluates only the F contribution. No nonzero period, entry estimate,
error/gain datum, or comparison to a Wilson inclusion matrix is synthesized.
"""
from fractions import Fraction as Q
from math import exp, factorial, log
from pathlib import Path
import csv
import hashlib

OUT = Path(__file__).resolve().parent
SRC = OUT / "evidence" / "lean_source"
if not SRC.is_dir():
    SRC = OUT.parent / "lean_evidence"
FILES = [
    "Formalism/LocalToGlobal/Divisibility/Numbers.lean",
    "Formalism/LocalToGlobal/Divisibility/NumbersLemmas.lean",
    "Formalism/LocalToGlobal/Divisibility/NumbersLink.lean",
    "Formalism/LocalRingCardinality/DataParams₂.lean",
    "Formalism/LocalRingCardinality/HostCls.lean",
    "Formalism/LocalRingCardinality/SpanPowerMembership/ExampleRanksRankComplement.lean",
    "Formalism/LocalRingCardinality/SpanPowerMembership/ExampleWeightMiddleEntries.lean",
]
k, m, t, nV, n, card_A = 8, 2, 15, 24, 4, 4
card_RPl = 2 * card_A
hcV, hcB, hcE = [24, 20, 16, 12, 8, 4, 0], [91, 109], [100, 118]
g, q, d = [3697, 7393], 11, 7


def sig_par(i):
    return hcV[i] if i < k - 1 else -hcB[i - (k - 1)] if i - (k - 1) < m else 0


def a_plus(j, i):
    return Q(sig_par(i) + hcE[j - 1]) - Q(nV - 1 - 2 * i, 2) - Q(k + j - 1 - (m - j), 2)


def a_minus(j, c):
    return Q(hcB[j + c] if j + c < m else 0) - hcE[j - 1] - Q(t + 1 + 2 * c, 2)


rows = []
main = {}
for j in (1, 2):
    ap = [a_plus(j, i) for i in range(k + j - 1)]
    am = [a_minus(j, c) for c in range(m - j)]
    dp, dm = card_RPl * sum(ap), card_RPl * sum(am)
    fg = -(dp + dm) / 2
    fr = -Q(k - 1, 2) * card_A * hcE[j - 1]
    main[j] = (fg, fr)
    rows.append([j, hcE[j - 1], k + (j - 1) * (t + 1), k + j * (t + 1),
                 ",".join(map(str, ap)), ",".join(map(str, am)), dp, dm, fg, fr])
assert rows[0][4:6] == ["109,106,103,100,97,94,91,1", "1"]
assert rows[1][4:6] == ["126,123,120,117,114,111,108,18,1", ""]
assert main == {1: (Q(-2808), Q(-1400)), 2: (Q(-3352), Q(-1652))}

# A rational, rigorous cutoff certificate: 1 < 2^(1/300) < 101/100;
# exp(101/100) < 11/4 by a Taylor sum and geometric tail majorant.
# Also exp(1) > 1+1+1/2+1/6 = 8/3, hence X'' > 64/3 > 21.
x = Q(101, 100)
assert x ** 300 > 2
N = 12
exp_upper = sum(x ** r / factorial(r) for r in range(N + 1)) + (x ** (N + 1) / factorial(N + 1)) / (1 - x / (N + 2))
assert exp_upper < Q(11, 4)
assert Q(64, 3) > 21
# NumFacts.n2 requires Nm^2 <= b = exp(2^(1/100)). But 2^(1/100)<2
# and exp(2) = exp(1)^2 < 3^2, as exp(1)<exp(101/100)<11/4<3.
Nm = k + m * (t + 1)
assert Nm == 40 and Nm * Nm > 9
assert Q(0) < Q(1, 100) < 1 and exp_upper < 3
cutoff = 8 * exp(2 ** (1 / 300))  # display only, not the proof of the cutoff
assert 21 < cutoff < 22
primes = [2, 3, 5, 7, 11, 13, 17, 19]


def legendre(a, p):
    r = pow(a % p, (p - 1) // 2, p)
    return 0 if r == 0 else 1 if r == 1 else -1


def prime_class(p):
    if p == 2:
        return "ram2"
    if p == q:
        return "ramQ"
    if p == d:
        return "ramD"
    if legendre(-d, p) == 1:
        return "splitK"
    # hostEx_psQ identifies psAt with the quadratic character (-q/p).
    return "signal" if legendre(-q, p) == 1 else "inertClass"


lp_checks = 0
for p in [3, 5, 13, 17, 19]:
    assert prime_class(p) in ("signal", "inertClass")
    for e in hcE:
        A = Q((k - 1) * e)
        for orbit_len in [2, 4]:
            # All odd supported i obey p^i+1 >= p+1. Summing the
            # feasibility inequalities therefore bounds the objective by
            # orbit_len*A/(p+1); the following feasible point attains it.
            xs = [[Q(0) for _ in range(orbit_len)] for _ in range(orbit_len)]
            for s in range(orbit_len):
                xs[s][1] = A / (p + 1)
            for s in range(orbit_len):
                lhs = sum(p ** i * xs[s][i] for i in range(orbit_len))
                lhs += sum(xs[(s - i) % orbit_len][i] for i in range(orbit_len))
                assert lhs == A
            objective = sum(sum(row) for row in xs)
            assert objective == orbit_len * A / (p + 1)
            for i in range(orbit_len):
                if i % 2:
                    assert p ** i + 1 >= p + 1
            lp_value = Q(p, p * p - 1) * orbit_len * A - objective
            assert lp_value == orbit_len * A / (p * p - 1)
            lp_checks += 1


def f_j_p(j, p):
    if p in g:
        return main[j][0]
    cls = prime_class(p)
    if cls == "ramD":
        return main[j][1]
    if cls in ("signal", "inertClass") and p <= 21:
        return Q(card_RPl * (k - 1) * hcE[j - 1], p * p - 1)
    return Q(0)


local_rows = []
for p in primes + g:
    f1, f2 = f_j_p(1, p), f_j_p(2, p)
    local_rows.append([p, "distinguished" if p in g else prime_class(p), f1, f2, f1 + f2])
assert f_j_p(1, 7) == -1400
assert f_j_p(1, 2) == f_j_p(1, 11) == 0
fo_approx = sum(log(p) * float(f1 + f2) for p, cls, f1, f2, total in local_rows)


def write_tsv(name, header, data):
    with (OUT / name).open("w", newline="") as out:
        writer = csv.writer(out, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(data)


write_tsv("step10_m2_parameters.tsv",
          ["lift_j", "e_j", "source_rank", "target_rank", "a_plus", "a_minus", "Dplus", "Dminus", "FTypeG", "FRamD"], rows)
write_tsv("step10_m2_local_contributions.tsv", ["prime", "class", "F_1_p", "F_2_p", "sum_F_j_p"], local_rows)
write_tsv("step10_m2_source_hashes.tsv", ["path_relative_to_lean_evidence", "sha256"],
          [[name, hashlib.sha256((SRC / name).read_bytes()).hexdigest()] for name in FILES])
print("PASS: exact m=2 row sums, local coefficients and 20 LP certificates.")
print(f"Certified 21 < X'' < 22; approximation: {cutoff:.12f}")
print(f"Fo approximation (F contribution only): {fo_approx:.12f}")
print("Certified NumFacts.n2 incompatibility: Nm^2=1600, while b<9.")
for row in local_rows:
    print("\t".join(map(str, row)))
