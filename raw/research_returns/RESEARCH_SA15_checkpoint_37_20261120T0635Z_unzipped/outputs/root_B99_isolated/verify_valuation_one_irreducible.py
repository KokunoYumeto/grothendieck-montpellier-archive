#!/usr/bin/env python3
"""Exact B99 supplement. No field, group, or BT realization is inferred."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
import json
import time
import traceback
import sympy as s

OUT = Path(__file__).with_suffix(".output.json")
assert not OUT.exists(), "Preserve the exact prior executed output before a rerun"
start = time.perf_counter()
counts = {}


def vp(n, p):
    a = 0
    while n and n % p == 0:
        a += 1
        n //= p
    return a


def prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))


def run():
    p, t, a, b, A, D = s.symbols("p t a b A D")
    q, N = p**2, p**2 - 1
    e = t*p*(p-1)
    c1 = t*N*(p-1)
    c2 = t*(q*q-1)*(p-1)
    a0 = (q*e-e)/p
    j0 = q*e-a0
    lower = t*p-1+t*p*2*p*p*(p-1)-p*p*(t*p*p-1)
    d2min = t*(p*p-p-2+1/p)
    identities = [
        ("point_p_squared_value", e/q, t*(p-1)/p),
        ("point_p_cubed_value", e/q**2, t*(p-1)/p**3),
        ("minimum_break_threshold", a0, t*N*(p-1)),
        ("critical_ordinary_degree", j0, e+(p-1)*a0),
        ("critical_degree_residue", j0+t,
         t*p*(p**3-2*p*p+p+1)),
        ("critical_terminal_above_threshold",
         q*q*e-j0-(q*q*e-e)/p, (p-1)*(q*q*e-q*e)/p),
        ("low_break_ordinary_advantage",
         A+p*b-(A+(p-1)*a+b), (p-1)*(b-a)),
        ("high_break_ordinary_advantage",
         e+p*b-(q*e-a+b), (p-1)*(b-a)+p*(a-a0)),
        ("two_break_last_upper",
         (D-A-(p-1)*a+(p-1)*a)/p, (D-A)/p),
        ("different_actual_towers", lower,
         (p-1)*(t*p*(p*p-p-1)+p+1)),
        ("different_upper_sum", lower/(p-1)-(p+1),
         t*p*(p*p-p-1)),
        ("second_upper_endpoint",
         (t*p*(p*p-p-1)-t*(p-1))/p, d2min),
        ("trace_zero_gap", p**3*(t*N*N-c1)-p*c2,
         t*p*N*(p-1)*(p**3-p*p-1)),
        ("traceful_gap", q*(N*d2min-c1)-c2,
         t*N*(p**4-3*p**3+1)),
        ("second_above_first", N*d2min-c1,
         t*N*(p*p-2*p-1+1/p)),
    ]
    for name, lhs, rhs in identities:
        assert s.cancel(lhs-rhs) == 0, name
    counts["symbolic_identities"] = len(identities)

    primes = [x for x in range(5, 24) if prime(x)]
    sectors = []
    derivative_terms = divisible_indices = profiles = 0
    numerator_checks = ordinary_checks = boundary_checks = 0
    two_break_checks = rational_checks = conductor_checks = 0
    cyclotomic_elements = noncoprime_t_N = 0
    minimum_traceful = minimum_traceless = None
    for pp in primes:
        qq, nn = pp*pp, pp*pp-1
        t_values = sorted(set([1, 2, 3, pp-1, pp+1, 2*(pp-1), nn, nn+1]))
        for tt in t_values:
            if tt % pp == 0:
                continue
            ee = tt*pp*(pp-1)
            cc1, cc2 = tt*nn*(pp-1), tt*(qq*qq-1)*(pp-1)
            deg = tt*pp
            lead = tt*pp*pp-1
            assert vp(ee, pp) == 1
            assert F(ee, qq).denominator == pp
            assert F(ee, qq*qq).denominator == pp**3
            assert F(ee, qq)*qq == ee and F(ee, qq*qq)*qq*qq == ee
            numerator_checks += 4
            residues = {lead % deg}
            low_profile = [lead]
            varied_profile = [lead]
            for i in range(1, deg):
                # The coefficient valuation is measured in K_1;
                # both v_K(i) and v_K(a_i) are multiples of tp.
                assert (i-1) % deg not in residues
                residues.add((i-1) % deg)
                for va in (1, 2, pp+1):
                    value = ee*vp(i, pp)+deg*va+i-1
                    assert value % deg == i-1
                    assert value != lead
                    derivative_terms += 1
                low_profile.append(ee*vp(i, pp)+deg+i-1)
                varied_profile.append(ee*vp(i, pp)+deg*(1+i % 3)+i-1)
                divisible_indices += int(i % pp == 0)
            assert residues == set(range(deg))
            for values in (low_profile, varied_profile):
                assert len(set(values)) == len(values)
                assert min(values) <= lead
                assert min(values) >= deg-1
                profiles += 1

            aa0 = cc1
            jj0 = qq*ee-aa0
            assert jj0 == ee+(pp-1)*aa0
            assert jj0 % pp == (-tt) % pp != 0
            bb = qq*qq*ee-jj0
            assert bb > aa0
            assert F(bb)-F(qq*qq*ee-ee, pp) == F((pp-1)*(qq*qq*ee-qq*ee), pp) > 0
            boundary_checks += 3
            # Include exhaustive first-break samples in the small sectors,
            # and all critical neighbours in every (possibly large) sector.
            samples = {1, aa0-1, aa0, aa0+1, aa0+pp, qq*ee-ee-1}
            if pp == 5 and tt <= 3:
                samples.update(range(1, qq*ee-ee))
            for aa in sorted(x for x in samples if x > 0):
                if aa < aa0:
                    jj = ee+(pp-1)*aa
                    for delta in (1, pp, aa0+1):
                        last = aa+delta
                        assert ee+pp*last-(jj+last) == (pp-1)*delta > 0
                        ordinary_checks += 1
                elif aa > aa0:
                    jj = qq*ee-aa
                    if jj < ee or jj % pp == 0:
                        continue
                    for delta in (1, pp, aa0+1):
                        last = aa+delta
                        assert ee+pp*last-(jj+last) == (pp-1)*delta+pp*(aa-aa0) > 0
                        ordinary_checks += 1
            # Both possible degree-q point extensions, with all small a
            # and all boundary neighbours in every other sector.
            for DD in (qq*ee, qq*qq*ee):
                cut = (DD-ee)//pp
                firsts = {1, cut-1, cut//2}
                if pp == 5 and tt <= 3 and DD == qq*ee:
                    firsts.update(range(1, cut))
                for aa in sorted(x for x in firsts if 0 < x < cut):
                    jj = ee+(pp-1)*aa
                    if jj % pp == 0:
                        continue
                    last = DD-jj
                    assert last > aa
                    assert F(last+(pp-1)*aa, pp) == F(DD-ee, pp)
                    assert ee+pp*last > jj+last == DD
                    two_break_checks += 1

            actual_sum = 0
            for k in range(1, pp*pp):
                actual_sum += pp if k % pp else pp*pp
                cyclotomic_elements += 1
            assert actual_sum == 2*pp*pp*(pp-1)
            low = deg-1+deg*actual_sum-pp*pp*lead
            assert low == (pp-1)*(tt*pp*(pp*pp-pp-1)+pp+1)
            for den in (1, pp, pp*pp):
                # Full unscaled numerator range and the scaled endpoints.
                first_values = {F(tt*n, den) for n in range(1, (pp-1)*den+1)}
                for delta1 in first_values:
                    delta2 = (tt*pp*(pp*pp-pp-1)-delta1)/pp
                    last_lower = pp*delta2-(pp-1)*delta1
                    df = (pp*pp-1)*(delta1+1)+(pp-1)*(last_lower-delta1)
                    assert df == low
                    assert delta2 >= tt*(F(pp*pp-pp-2)+F(1, pp))
                    second = nn*delta2
                    assert second > cc1
                    gap = qq*(second-cc1)-cc2
                    expected = tt*nn*(pp**4-3*pp**3+1)
                    assert gap >= expected > 0
                    minimum_traceful = expected if minimum_traceful is None else min(minimum_traceful, expected)
                    for rr in (3, 4):
                        assert pp**rr*(second-cc1) > pp**(rr-2)*cc2
                        conductor_checks += 1
                    rational_checks += 1
            zero_gap = pp**3*(tt*nn*nn-cc1)-pp*cc2
            assert zero_gap == tt*pp*nn*(pp-1)*(pp**3-pp*pp-1) > 0
            minimum_traceless = zero_gap if minimum_traceless is None else min(minimum_traceless, zero_gap)
            import math
            noncoprime_t_N += int(math.gcd(tt, nn) > 1)
            sectors.append({"p": pp, "t": tt, "e": ee,
                            "c1": cc1, "c2": cc2,
                            "critical_degree": jj0,
                            "trace_zero_gap": zero_gap,
                            "traceful_minimum_gap": expected})
    counts.update({
        "primes": len(primes), "sectors": len(sectors),
        "point_denominator_checks": numerator_checks,
        "derivative_monomials": derivative_terms,
        "p_divisible_derivative_indices": divisible_indices,
        "distinct_derivative_profiles": profiles,
        "critical_boundary_checks": boundary_checks,
        "fixed_ordinary_term_inequalities": ordinary_checks,
        "two_break_Herbrand_checks": two_break_checks,
        "cyclotomic_elements": cyclotomic_elements,
        "rational_upper_break_pairs": rational_checks,
        "terminal_conductor_comparisons": conductor_checks,
        "sectors_not_coprime_to_N": noncoprime_t_N
    })
    return {"symbolic_identity_names": [x[0] for x in identities],
            "rows": sectors, "minimum_traceful_gap": minimum_traceful,
            "minimum_traceless_gap": minimum_traceless,
            "scope": "Exact symbolic identities and finite arithmetic only. Actual field existence, normality, coefficient expansions, and character-spanning are proved in the text; no realization or least-index conclusion is inferred from this checker."}


try:
    result = run()
    record = {"status": "PASS", "actual_utc": datetime.now(timezone.utc).isoformat(),
              "runtime_seconds": time.perf_counter()-start, "counts": counts, **result}
except Exception:
    record = {"status": "FAIL", "actual_utc": datetime.now(timezone.utc).isoformat(),
              "runtime_seconds": time.perf_counter()-start, "counts": counts,
              "traceback": traceback.format_exc()}
OUT.write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps({k: record[k] for k in ("status", "actual_utc", "runtime_seconds", "counts")}, indent=2))
if record["status"] != "PASS":
    print(record["traceback"])
    raise SystemExit(1)
