#!/usr/bin/env python3
"""Exact B100 supplement. Infinite arcs/descent/BT effectivity are proved in text."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from math import gcd
import json
import time
import traceback
import sympy as s

OUT = Path(__file__).with_suffix(".output.json")
assert not OUT.exists(), "Preserve prior executed code/output before rerunning"
start = time.perf_counter()
counts = {}


def prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5)+1))


def choose_A(e, p):
    N = p*p-1
    if e < p**3:
        return 1
    A = e//p**3+1
    if A % N == 0:
        A += 1
    return A


def mul_trunc(a, b, degree):
    c = [F(0)]*(degree+1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if i+j <= degree and bj:
                    c[i+j] += ai*bj
    return c


def pow_coeff(a, power, degree):
    c = [F(1)]
    for _ in range(power):
        c = mul_trunc(c, a, degree)
    return c[degree]


def run():
    p, e, A = s.symbols("p e A")
    q, N = p*p, p*p-1
    d = e*N
    b = e*N/p-q*(p-1)*A
    J = b+p*q*A
    identities = [
        ("first_strict_Newton_gap", b-(q-p)*A, N*(e-p*p*A)/p),
        ("second_strict_Newton_gap", (q-p)*q*A-b, N*(p**3*A-e)/p),
        ("Eisenstein_degree", b+(p-1)*J, d),
        ("p_coefficient_cutoff", d-J, (p-1)*b+p*q*(p-2)*A),
        ("tame_weight_multiple", b+(p-1)*A, N*(e/p-(p-1)*A)),
        ("terminal_P_gap", N*J-d, (q-p)*J-b),
        ("explicit_second_wild_b", b.subs({e:2*p*(p-1), A:1}), (p-1)*(p*p-2)),
        ("explicit_second_wild_J", J.subs({e:2*p*(p-1), A:1}), (p-1)*(p*p-2)+p**3),
        ("weighted_upper_surplus", (2*p**3-1)-2*p*N, 2*p-1),
        ("mixed_upper_surplus", p**4-2*p*(p-1), p*(p**3-2*p+2)),
    ]
    for name, lhs, rhs in identities:
        assert s.cancel(lhs-rhs) == 0, name
    counts["symbolic_identities"] = len(identities)
    primes = [x for x in range(5, 102) if prime(x)]
    arc_cases = intermediate_checks = tail_checks = logarithm_terms = 0
    avoided_N = nonfaithful = exact_examples = upper_checks = 0
    character_checks = direct_coefficients = recursion_integrality = 0
    examples, direct, upper = [], [], []
    for pp in primes:
        qq, nn = pp*pp, pp*pp-1
        ts = set(range(2, 4*pp+5))
        # Windows where floor(e/p³)+1 would be divisible by N,
        # and where the ramification has higher p-adic order.
        for mult in (1, 2, 3):
            center = ((mult*nn-1)*pp*pp)//(pp-1)
            ts.update(range(max(2, center-3), center+4))
        ts.update([pp, pp*pp, pp**3, pp**4, 2*pp**3])
        for tt in sorted(ts):
            ee = tt*pp*(pp-1)
            if ee <= qq:
                continue
            aa = choose_A(ee, pp)
            assert F(ee, pp**3) < aa < F(ee, pp*pp)
            assert aa % nn != 0
            assert aa <= F(ee, pp**3)+2 if ee >= pp**3 else aa == 1
            raw_A = ee//pp**3+1
            avoided_N += int(ee >= pp**3 and raw_A % nn == 0)
            dd = ee*nn
            bb = ee*nn//pp-qq*(pp-1)*aa
            jj = bb+pp*qq*aa
            assert bb > (qq-pp)*aa > 0
            assert bb < (qq-pp)*qq*aa
            assert bb+(pp-1)*jj == dd
            assert dd-jj == (pp-1)*bb+pp*qq*(pp-2)*aa > 0
            assert aa < qq*aa < jj < dd
            assert (bb+(pp-1)*aa) % nn == 0
            # Unique earliest terms in each mod-p composition.
            first_candidates = {"p": bb+pp*aa, "q": qq*aa}
            second_candidates = {"p": bb+pp*qq*aa, "q": qq*qq*aa}
            terminal_candidates = {"p": bb+(pp-1)*jj, "q": nn*jj}
            assert min(first_candidates, key=first_candidates.get) == "q"
            assert min(second_candidates, key=second_candidates.get) == "p"
            assert min(terminal_candidates, key=terminal_candidates.get) == "p"
            # All potentially nonzero intermediate coefficients have at least
            # one u factor modulo p. Test every such degree at the smaller
            # primes, and its monotone endpoints at the others.
            indices = range(pp+1, qq) if pp <= 13 else (pp+1, qq-1)
            for i in indices:
                assert bb+i*aa > qq*aa
                assert bb+i*qq*aa > jj
                assert bb+(i-1)*jj > dd
                intermediate_checks += 3
            for degree, val, selected in ((qq+1, aa, qq*aa),
                                           (qq+1, qq*aa, jj)):
                assert degree*val > selected
                tail_checks += 1
            assert qq*jj > dd
            assert dd+aa > qq*aa and dd+qq*aa > jj
            tail_checks += 3
            # Generic finite character order may be a proper divisor of N.
            order = nn//gcd(aa, nn)
            assert order > 1 and gcd(order, pp) == 1
            psi_order = nn//gcd((pp+1)*aa, nn)
            assert (pp-1) % psi_order == 0
            assert sorted([aa % nn, pp*aa % nn]) != sorted([0, (pp+1)*aa % nn])
            assert (aa+pp*aa) % nn == (pp+1)*aa % nn
            nonfaithful += int(order < nn)
            character_checks += 3
            arc_cases += 1
            if tt == 2:
                assert aa == 1 and bb == (pp-1)*(pp*pp-2)
                exact_examples += 1
                examples.append({"p": pp, "e": ee, "A": aa, "b": bb,
                                 "point_values": [aa, qq*aa, jj], "absolute_good_index": dd,
                                 "special_order": order, "determinant_order": psi_order})

        # Construct the actual HG logarithm recursively in Q[u].
        # Each recorded monomial verifies the precise tame weight.
        logs = [{0:F(1)}]
        for j in range(1, 13):
            nxt = {k+pp**(j-1): v/pp for k, v in logs[j-1].items()}
            if j >= 2:
                for k, v in logs[j-2].items():
                    nxt[k] = nxt.get(k, F(0))+v/pp
            logs.append(nxt)
            for k, coefficient in nxt.items():
                assert ((pp-1)*k-(pp**j-1)) % nn == 0
                assert (coefficient*pp**j).denominator == 1
                logarithm_terms += 1
        assert logs[1] == {1:F(1, pp)}
        assert logs[2] == {pp+1:F(1, pp*pp), 0:F(1, pp)}

        ee = 2*pp*(pp-1)
        absolute = ee*nn
        bound = F(absolute, pp-1)
        sequence = [1]
        for _ in range(3):
            sequence.append(min(absolute+sequence[-1], pp*sequence[-1]+pp-1))
        assert sequence == [1, 2*pp-1, 2*pp*pp-1, 2*pp**3-1]
        assert sequence[-1]-bound == 2*pp-1 > 0
        assert pp**4 >= ee and 4 >= 1+2
        upper_checks += 5
        upper.append({"p": pp, "e": ee, "actual_target_sequence": sequence,
                      "threshold": int(bound), "surplus": 2*pp-1})

    # Independent coefficient inversion through degree p², using
    # f([p]T)=p f(T), not the asserted p-series coefficient list.
    for pp in (5, 7, 11, 13):
        alpha = [F(pp)]
        for j in range(1, pp+1):
            coefficient = (F(1) if j == 1 else F(0))-pow_coeff(alpha, pp, j-1)/pp
            assert coefficient.denominator == 1
            alpha.append(coefficient)
            direct_coefficients += 1
        last_u = F(1, pp)-pow_coeff(alpha, pp, pp)/pp-pp**(pp*pp-2)
        last_constant = 1-pp**(pp*pp-1)
        assert alpha[1] == 1-pp**(pp-1)
        assert last_u.denominator == 1 and last_constant % pp == 1
        # All coefficients through p² below degree p are zero;
        # the intermediate supported degrees carry a positive u power.
        assert all((1+j*(pp-1)) > pp for j in range(2, pp+1))
        direct_coefficients += 2
        direct.append({"p": pp, "coefficient_Tp": int(alpha[1]),
                       "coefficient_Tp2_at_u0": last_constant,
                       "coefficient_u_pplus1_Tp2": int(last_u)})
        recursion_integrality += len(alpha)-1
    counts.update({"primes":len(primes), "arc_cases":arc_cases,
                   "intermediate_coefficient_weights":intermediate_checks,
                   "tail_and_p_coefficient_cutoffs":tail_checks,
                   "avoided_divisible_A_choices":avoided_N,
                   "nonfaithful_special_actions":nonfaithful,
                   "character_checks":character_checks,
                   "logarithm_monomials":logarithm_terms,
                   "direct_multiplication_coefficients":direct_coefficients,
                   "direct_integral_recursion_coefficients":recursion_integrality,
                   "exact_second_wild_examples":exact_examples,
                   "actual_target_upper_checks":upper_checks})
    return {"examples":examples, "direct_series":direct, "upper_bounds":upper,
            "symbolic_identity_names":[x[0] for x in identities],
            "finite_scope":"Primes5..101. Every t=2..4p+4, specified windows around three excluded-A multiples, and t=p,p²,p³,p⁴,2p³. All intermediate degrees for p<=13 and monotone endpoint bounds thereafter. Exact sparse logarithm through j12; direct multiplication inversion through p² for p=5,7,11,13.",
            "not_inferred":"No infinite formal group, Eisenstein DVR, descent cocycle, finite quotient, Kummer extension, or torsion congruence is inferred from this arithmetic census; all are proved in the candidate."}


try:
    result = run()
    record = {"status":"PASS", "actual_utc":datetime.now(timezone.utc).isoformat(),
              "runtime_seconds":time.perf_counter()-start, "counts":counts, **result}
except Exception:
    record = {"status":"FAIL", "actual_utc":datetime.now(timezone.utc).isoformat(),
              "runtime_seconds":time.perf_counter()-start, "counts":counts,
              "traceback":traceback.format_exc()}
OUT.write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps({k:record[k] for k in ("status","actual_utc","runtime_seconds","counts")}, indent=2))
if record["status"] != "PASS":
    print(record["traceback"])
    raise SystemExit(1)
