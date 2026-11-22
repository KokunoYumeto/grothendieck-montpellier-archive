#!/usr/bin/env python3
"""Exact B101 arithmetic. No formal-group existence is inferred by enumeration."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from math import gcd
import json
import time
import traceback
import sympy as s

OUT = Path(__file__).with_suffix(".output.json")
assert not OUT.exists(), "Retain old executed output before rerunning"
start = time.perf_counter()
counts = {}


def prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5)+1))


def vp(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def choose_A(e, p, k, N):
    if e < p**(k+1):
        return 1
    A = e//p**(k+1)+1
    return A+1 if A % N == 0 else A


def run():
    p, e, A, r, w = s.symbols("p e A r w")
    q, N = p*p, p*p-1
    U = w*A
    b = e*N/r-(p-1)*U
    J = r*U+b*(r-1)/(p-1)
    identities = [
        ("last_q_branch_gap", b-(q-p)*U/q, N/r*(e-r*U/p)),
        ("first_p_branch_gap", (q-p)*U-b, N/r*(r*U-e)),
        ("terminal_Eisenstein_degree", b+(p-1)*J, e*N),
        ("strict_p_coefficient_cutoff", e*N-J, (p-2)*J+b),
        ("one_more_p_iteration", p*J+b,
         p*r*U+b*(p*r-1)/(p-1)),
        ("exact_family_parameter",
         b.subs({e:2*r*(p-1), w:q, A:1}), (p-1)*(p*p-2)),
        ("upper_surplus", 2*r*p*p-1-2*r*N, 2*r-1),
        ("mixed_upper_gap", r*p**3-2*r*(p-1), r*(p**3-2*p+2)),
    ]
    for name, lhs, rhs in identities:
        assert s.cancel(lhs-rhs) == 0, name
    counts["symbolic_identities"] = len(identities)
    primes = [p for p in range(5, 44) if prime(p)]
    arcs = q_steps = p_steps = final_steps = cutoff_checks = 0
    weight_checks = character_checks = skipped_divisible_A = 0
    nonfaithful = exact_family = recurrence_checks = endpoint_checks = 0
    examples = []
    for pp in primes:
        qq, nn = pp*pp, pp*pp-1
        for vv in range(0, 9):
            ppv = pp**vv
            for hh in range(1, 7):
                n = hh+vv+1
                k = 2*n-3-vv
                assert hh >= 1 and n >= vv+2 and k == 2*hh+vv-1
                base = ppv*(pp-1)
                first = pp**k//base+1
                ts = set(range(first, first+8))
                # Explicitly force floor(x0)+1 near N and 2N.
                for multiple in (1, 2):
                    center = (multiple*nn-1)*pp**(k+1)//base
                    ts.update(range(max(1, center-2), center+4))
                for tt in sorted(ts):
                    if tt % pp == 0:
                        continue
                    ee = base*tt
                    if ee <= pp**k:
                        continue
                    assert vp(ee, pp) == vv
                    aa = choose_A(ee, pp, k, nn)
                    assert F(ee, pp**(k+1)) < aa < F(ee, pp**k)
                    assert aa % nn != 0
                    skipped_divisible_A += int(ee >= pp**(k+1) and (ee//pp**(k+1)+1) % nn == 0)
                    UU = qq**hh*aa
                    bb = ee*nn//ppv-(pp-1)*UU
                    dd = ee*nn
                    assert bb-(qq-pp)*qq**(hh-1)*aa == F(nn, ppv)*(ee-pp**k*aa) > 0
                    assert (qq-pp)*UU-bb == F(nn, ppv)*(pp**(k+1)*aa-ee) > 0
                    orders = [aa]
                    for j in range(1, n):
                        current = orders[-1]
                        candidates = [bb+pp*current, qq*current]
                        expected = qq*current if j <= hh else bb+pp*current
                        assert min(candidates) == expected
                        assert candidates[0] != candidates[1]
                        assert expected > current
                        indices = range(pp+1, qq) if pp <= 7 and vv <= 2 and hh <= 3 else (pp+1, qq-1)
                        for degree in indices:
                            assert bb+degree*current > expected
                            weight_checks += 1
                        assert (qq+1)*current > expected
                        weight_checks += 1
                        orders.append(expected)
                        if j <= hh:
                            assert expected == qq**j*aa
                            q_steps += 1
                        else:
                            rr = j-hh
                            assert expected == pp**rr*UU+bb*((pp**rr-1)//(pp-1))
                            p_steps += 1
                    assert len(orders) == n
                    Jlast = orders[-1]
                    assert Jlast == ppv*UU+bb*((ppv-1)//(pp-1))
                    assert bb+(pp-1)*Jlast == dd < nn*Jlast
                    assert dd > Jlast and all(0 < z < dd for z in orders)
                    assert (bb+(pp-1)*aa) % nn == 0
                    final_steps += 1
                    for z in orders:
                        assert dd+z > Jlast
                        cutoff_checks += 1
                    assert sorted([aa % nn, pp*aa % nn]) != sorted([0, (pp+1)*aa % nn])
                    assert (pp-1) % (nn//gcd((pp+1)*aa, nn)) == 0
                    character_checks += 2
                    nonfaithful += int(gcd(aa, nn) > 1)
                    arcs += 1
            # Entire exact family v=0,...,8 with actual upper recurrence.
            ee = 2*ppv*(pp-1)
            nnlevel = vv+2
            assert ee > pp**(2*nnlevel-3-vv)
            aa = choose_A(ee, pp, 2*nnlevel-3-vv, nn)
            assert aa == 1
            bb = ee*nn//ppv-(pp-1)*qq
            assert bb == (pp-1)*(pp*pp-2)
            absolute = ee*nn
            seq = [1]
            for j in range(vv+2):
                first = absolute+seq[-1]
                second = pp*seq[-1]+pp-1
                assert first >= second
                seq.append(min(first, second))
                assert seq[-1] == 2*pp**(j+1)-1
                recurrence_checks += 1
            assert seq[-1]-F(absolute, pp-1) == 2*ppv-1 > 0
            assert ee < pp**(vv+3)
            exact_family += 1
            examples.append({"p":pp, "v":vv, "e":ee,
                             "counterexample_actual_level_exponent":vv+2,
                             "recovery_actual_level_exponent":vv+3,
                             "least_manuscript_index":vv+2,
                             "A":1, "b":bb, "upper_sequence":seq,
                             "upper_surplus":2*ppv-1})
            # Equality at the strict threshold leaves a tied q/p branch
            # for A=1; it is intentionally excluded by the proof.
            for hh in range(1, 7):
                kval = 2*hh+vv-1
                ee0 = pp**kval
                U0 = qq**hh
                b0 = ee0*nn//ppv-(pp-1)*U0
                assert b0 == (qq-pp)*qq**(hh-1)
                endpoint_checks += 1

    # Sparse exact logarithm and uniform weight through the largest
    # finite n used above; this supplements the infinite induction.
    log_terms = 0
    for pp in primes:
        nn = pp*pp-1
        logs = [{0:F(1)}]
        for j in range(1, 16):
            nxt = {a+pp**(j-1): c/pp for a,c in logs[-1].items()}
            if j >= 2:
                for a,c in logs[-2].items():
                    nxt[a] = nxt.get(a, F(0))+c/pp
            logs.append(nxt)
            for a,c in nxt.items():
                assert ((pp-1)*a-(pp**j-1)) % nn == 0
                assert (c*pp**j).denominator == 1
                log_terms += 1
    counts.update({"primes":len(primes), "arc_cases":arcs,
                   "q_branch_iterations":q_steps, "p_branch_iterations":p_steps,
                   "terminal_Eisenstein_checks":final_steps,
                   "intermediate_and_tail_weights":weight_checks,
                   "p_coefficient_cutoffs":cutoff_checks,
                   "character_checks":character_checks,
                   "avoided_divisible_A_choices":skipped_divisible_A,
                   "nonfaithful_special_actions":nonfaithful,
                   "exact_family_members":exact_family,
                   "actual_target_recurrence_steps":recurrence_checks,
                   "strict_endpoint_ties":endpoint_checks,
                   "logarithm_monomials":log_terms})
    return {"symbolic_identity_names":[x[0] for x in identities],
            "exact_family":examples,
            "finite_scope":"Primes5..43; v=0..8; h=1..6, hence n=h+v+1. All prime-to-p t in eight-value first-threshold windows and six-value windows near the first two excluded multiples of A. All intermediate degrees for p<=7,v<=2,h<=3, monotone endpoints otherwise. Exact logarithms through j15.",
            "not_inferred":"These checks do not infer integral formal groups, fields, descent, actual quotients or compatible cocycles. Those are constructed in the full proof. Equality at the necessary bound is excluded, not assigned a branch."}


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
