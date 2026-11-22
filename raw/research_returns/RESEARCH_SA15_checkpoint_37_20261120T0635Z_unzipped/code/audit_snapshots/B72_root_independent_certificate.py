#!/usr/bin/env python3
"""Exact finite B72 supplement; no geometric existence is inferred."""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import datetime
import hashlib
import json
import time


def roots(points):
    hull = []
    for x, y in sorted(points):
        x, y = int(x), F(y)
        while len(hull) >= 2:
            x0, y0 = hull[-2]
            x1, y1 = hull[-1]
            if (y1-y0)*(x-x1) < (y-y1)*(x1-x0):
                break
            hull.pop()
        hull.append((x, y))
    answer = Counter()
    for (x0, y0), (x1, y1) in zip(hull, hull[1:]):
        valuation = (y0-y1)/(x1-x0)
        if valuation > 0:
            answer[valuation] += x1-x0
    return dict(answer)


def high_product_quotient(p, e, B):
    """Count actual high-quotient roots via the inverse polygon/product."""
    q = p*p
    a = e*(q-1)
    s = e*(p+1)
    alpha, beta = F(s-B), F(B, p)
    assert roots([(1, a), (p, (p-1)*B), (q, 0)]) == {
        alpha: p-1, beta: q-p}
    inverse = roots([(0, alpha), (1, a), (p, (p-1)*B), (q, 0)])
    quotient = Counter({p*beta: p-1})
    for z, multiplicity in inverse.items():
        assert z < alpha
        assert multiplicity*(p-1) % p == 0
        quotient[p*z] += multiplicity*(p-1)//p
    assert sum(quotient.values()) == q-1
    return dict(quotient)


def pair_orbit(p, c):
    N = p*p-1
    return tuple(sorted([c % N, p*c % N]))


def encode_roots(values):
    return [{"valuation": str(v), "multiplicity": m}
            for v, m in sorted(values.items(), reverse=True)]


def run():
    started = time.perf_counter()
    primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    counts = Counter()
    boundary_records = []
    for p in primes:
        q = p*p
        N = q-1
        e = 2*N
        s = e*(p+1)
        assert e % p and e > p and e < 2*q < p**3
        assert s % N == 0
        counts["boundary_indices"] += 1

        # Exact first-level break formula, across every prime parameter.
        seen_breaks = set()
        for C in range(1, p*e):
            if C % p:
                r = p*(s-C)-C
                assert r == p*s-(p+1)*C > 0
                assert r not in seen_breaks
                seen_breaks.add(r)
                counts["prime_parameter_breaks"] += 1

        # An explicitly bounded mixed-parameter range checks the direction
        # of the strict break comparison; no sufficiency is claimed.
        for Cdiv in range(p, 4*p+1, p):
            for Cpr in range(1, 4*p+1):
                if Cpr % p == 0:
                    continue
                rpr = p*s-(p+1)*Cpr
                upper_div = p*s-(p+1)*Cdiv
                assert (rpr < upper_div) == (Cpr > Cdiv)
                counts["bounded_mixed_break_directions"] += 1

        small = list(range(1, (e-1)//p+1))
        assert small == list(range(1, 2*p))
        for b1 in small:
            for b2 in small:
                if b1 >= b2 or (b2-b1) % (p-1):
                    continue
                if b1 >= 2:
                    assert q*b1 >= 2*q > e
                    assert p*b2 < e
                    gap = s-q*b1-p*b2
                    assert gap > q*(b2-b1) > 0
                    counts["separated_high_common_norm_pairs"] += 1
                elif b2 == p:
                    for c1 in range(p % (p+1), N, p+1):
                        c2 = (c1+p*(p-1)) % N
                        assert c2 == p*c1 % N
                        assert pair_orbit(p, c1) == pair_orbit(p, c2)
                        counts["harmless_frobenius_orbit_pairs"] += 1
                else:
                    assert b1 == 1 and b2 == 2*p-1
                    counts["new_mixed_second_quotient_pairs"] += 1

        b1, b2 = 1, 2*p-1
        B1, B2 = p*b1, p*b2
        D1, D2 = p*B1, p*B2
        assert B1 < e and B2 < e and D1 < e < D2
        first_roots = []
        second_roots = []
        second_parameters = []
        for B, D in [(B1, D1), (B2, D2)]:
            actual_first = high_product_quotient(p, e, B)
            assert actual_first == {F(s-D): p-1, F(D, p): q-p}
            first_roots.append(encode_roots(actual_first))
            C = p*D if D < e else s-D
            actual_second = high_product_quotient(p, e, D)
            assert actual_second == {F(s-C): p-1, F(C, p): q-p}
            second_roots.append(encode_roots(actual_second))
            second_parameters.append(C)
            counts["actual_double_quotient_root_records"] += 1
        Cdiv, Cpr = second_parameters
        assert Cdiv == p**3 and Cdiv % p == 0
        assert Cpr == 3*q-2*p-2 and Cpr % p
        assert 0 < Cdiv < p*e and 0 < Cpr < p*e
        assert Cdiv-Cpr == p*(p-1)*(p-2)+2 > 0
        rpr = p*s-(p+1)*Cpr
        upper_div = p*s-(p+1)*Cdiv
        assert rpr > upper_div
        assert s <= q*(p*b1+b2)
        counts["boundary_strict_break_contradictions"] += 1

        for c1 in range(p % (p+1), N, p+1):
            c2 = (c1+B2-B1) % N
            assert c2 % (p+1) == B2 % (p+1)
            assert (c1-c2) % (p-1) == 0
            assert (c1-B1-c2+B2) % N == 0
            high1, low1 = (p*c1-D1) % N, (c1+D1) % N
            high2, low2 = (p*c2-D2) % N, (c2+D2) % N
            assert (high1, low1) == (high2, low2)
            assert high1 != low1
            assert (low1-high1) % N == (p+1)*B1 % N
            assert pair_orbit(p, c1) != pair_orbit(p, c2)
            counts["marked_distinct_eigenvalue_records"] += 1

        # The general mixed-second-quotient inequality is checked on all
        # nonscalar small common-norm pairs of this boundary.
        for lo in small:
            for hi in small:
                if not (q*lo < e < q*hi):
                    continue
                if lo % (p-1) == 0 or (hi-lo) % (p-1):
                    continue
                second_div = p**3*lo
                second_pr = s-q*hi
                assert (second_pr > second_div) == (s > q*(p*lo+hi))
                counts["mixed_second_quotient_inequalities"] += 1

        prime_b = [b for b in range(1, e) if b % p]
        div_b = list(range(p, e, p))
        for b in prime_b:
            alpha = s-p*b
            assert alpha >= e+p and F(b, q).denominator == q
            for bdiv in div_b:
                lhs = q*(alpha-bdiv)
                rhs = b-bdiv
                assert lhs > p**3 and rhs < e < p**3
                counts["tame_mixed_point_field_inequalities"] += 1
        for bfirst in div_b:
            for bsecond in div_b:
                Bfirst, Bsecond = p*bfirst, p*bsecond
                if Bfirst > e or Bsecond > e:
                    large = max(Bfirst, Bsecond)
                    other = min(Bfirst, Bsecond)
                    assert (s-large) % p and (other//p) % p == 0
                    counts["tame_high_low_quotient_exclusions"] += 1
                else:
                    assert Bfirst == Bsecond == q
                    assert (2*q) % (p-1) == 2
                    counts["tame_small_exchanged_line_exclusions"] += 1
        counts["full_monodromy_lower_upper_thresholds"] += 1
        boundary_records.append({
            "p": p, "e": e, "b_pair": [b1, b2],
            "original_parameters": [B1, B2],
            "first_quotient_parameters": [D1, D2],
            "first_quotient_roots": first_roots,
            "second_quotient_parameters": second_parameters,
            "second_quotient_roots": second_roots,
            "prime_model_actual_break": rpr,
            "divisible_model_strict_upper_bound": upper_div,
            "required_inequality": "prime_actual_break < divisible_strict_upper_bound",
            "actual_inequality": "prime_actual_break > divisible_strict_upper_bound"
        })
    result = {
        "status": "PASS",
        "scope": "Finite exact Newton/product-root counts, marked characters and strict-break arithmetic only; the universal quotient/Galois proof is separate, and no existence is inferred.",
        "primes": primes, "counts": dict(sorted(counts.items())),
        "boundary_records": boundary_records,
        "elapsed_seconds": time.perf_counter()-started,
        "actual_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "program_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }
    Path(__file__).with_suffix(".output.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))
    return result


if __name__ == "__main__":
    run()
