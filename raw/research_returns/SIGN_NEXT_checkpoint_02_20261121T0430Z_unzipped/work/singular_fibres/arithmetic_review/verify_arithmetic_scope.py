#!/usr/bin/env python3
"""Exact arithmetic checks for SF-Q6-01--04 and source identity for SF-Q6-07; not a Lean build.

The source-level implications are proved in the accompanying TeX notes.
This certificate verifies their concrete arithmetic and selected HC data.
"""
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
k, m, t, f = 8, 2, 15, 8
r = k + m - 1
N = [k + j * (t + 1) for j in range(m + 1)]
host_floor = 4 * t * r + 1
assert host_floor == 541
assert not host_floor < 11 and not host_floor < 7
assert host_floor < 571 and host_floor < 599

Delta, hh, uF, uL, b1 = 1, t + 3, 24, -1, 1
v = [Q((k - 2 - j) * 4 * Delta) for j in range(k - 1)]
u = [Q(uF) + Q(1, 2)] + [v[j] - Q(1, 2) - Delta for j in range(k - 2)] + [Q(uL) + Q(1, 2)]
b = [Q(b1 + j * 2 * hh) for j in range(m)]
e = [x + hh for x in b]
assert all(u[j] > v[j] > u[j+1] for j in range(k - 1))
assert -b[0] < u[-1]
assert all(e[j] - b[j] >= Q(t+3, 2) for j in range(m))
assert all(b[j+1] - e[j] >= Q(t+3, 2) for j in range(m-1))
bT_forced = -u[-1] - Q(k-1, 2)
assert bT_forced == -3

rankval_lhs = r + t
rankval_rhs_minimum = 8 * f * r + 4
assert (rankval_lhs, rankval_rhs_minimum) == (24, 580)
assert rankval_lhs < rankval_rhs_minimum
assert 3**4 == 81

# SF-Q6-04 is a conditional identity; this checks its concrete positive
# right hand side, not existence of the global realizing data.
T = 10**10
prime = 863
assert all(prime % d for d in range(2, int(prime**0.5) + 1))
assert prime > 2 * f * N[-1] + 1
denominator = prime**2 - 1
full_lower_bound = Q(48 * T * T, denominator) - 76800 * (T + 3000)
assert full_lower_bound > 0
conditional = {
    "scope": "Exact positivity of SF-Q6-04(b) conditional full expression; realization not asserted",
    "T": T, "p": prime, "p_squared_minus_one": denominator,
    "lower_bound_numerator": full_lower_bound.numerator,
    "lower_bound_denominator": full_lower_bound.denominator,
    "positive": True,
    "integer_floor_lower_bound": full_lower_bound.numerator // full_lower_bound.denominator,
}
(HERE / "conditional_full_bound_certificate.json").write_text(json.dumps(conditional, indent=2) + "\n")

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

report = {
    "scope": "exact rational/integer calculation supporting human source-level proofs; no Lean compilation",
    "ranks": {"k": k, "m": m, "t": t, "r": r, "f": f, "N": N},
    "SF-Q6-01": {"host_lower_bound": host_floor, "numBig_host": [11,7], "full_H0_host": [571,599], "numBig_host_impossible": True},
    "SF-Q6-02": {"u": [str(x) for x in u], "v": [str(x) for x in v], "b": [str(x) for x in b], "e": [str(x) for x in e], "hc_interlacing_checked": True, "forced_top_bT": str(bT_forced)},
    "SF-Q6-03": {"RankVal_left": rankval_lhs, "RankVal_right_minimum": rankval_rhs_minimum, "M3_fourth_power": 81},
    "SF-Q6-04": conditional,
    "source_notes_sha256": {p.name: sha(p) for p in [HERE / "no_global_numBig.tex", HERE / "actual_m2_jets_scope.tex", HERE / "asymptotic_rank_scope.tex", HERE / "true_stabilizer_and_full_local_bound.tex", HERE / "untwisted_model_obstruction.tex"]},
}
(HERE / "arithmetic_scope_certificate.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
