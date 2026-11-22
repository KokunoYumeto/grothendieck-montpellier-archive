"""Exact finite B68 supplement, checking every t in the stated sector
for six primes. It does not prove the all-prime theorem by enumeration.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from datetime import datetime, timezone
import json, time, itertools, traceback

def polygon(points):
    hull = []
    for x, y in sorted(points):
        while len(hull) >= 2:
            x0, y0 = hull[-2]
            x1, y1 = hull[-1]
            if F(y1-y0, x1-x0) >= F(y-y1, x-x1):
                hull.pop()
            else:
                break
        hull.append((x, y))
    return [(F(y0-y1, x1-x0), x1-x0)
            for (x0, y0), (x1, y1) in zip(hull, hull[1:]) if y0 > y1]

def main():
    start = time.perf_counter()
    counts, summaries = Counter(), []
    primes = (5, 7, 11, 13, 17, 19)
    for p in primes:
        N, q = p*p-1, p*p
        for t in range(2, p):
            e, s = t*(p-1), t*N
            a = e*N
            assert p < e < p*p and e % p and e % 2 == 0
            assert s == e*(p+1) and s % p and s % N == 0
            assert F(e, p) < p-1
            local = Counter()
            def high(B):
                return p*B if B < e else s-B
            def orbit(c):
                return tuple(sorted({c % N, p*c % N}))
            for B in range(1, p*e, 2):
                alpha, beta, uval = F(s-B), F(B, p), (p-1)*B
                assert alpha > beta
                assert polygon([(0, a), (p-1, uval), (N, 0)]) == [
                    (alpha, p-1), (beta, q-p)]
                assert polygon([(0, beta), (1, a), (p, uval), (q, 0)]) == [
                    (F(B, p**3), q)]
                inverse = polygon([(0, alpha), (1, a), (p, uval), (q, 0)])
                if B < e:
                    assert inverse == [(F(s-p*B, p), p), (beta, q-p)]
                else:
                    assert inverse == [(alpha/q, q)]
                quotient = Counter({F(B): p-1})
                for value, number in inverse:
                    assert value < alpha and number*(p-1) % p == 0
                    quotient[p*value] += number*(p-1)//p
                Bnext = high(B)
                assert quotient == Counter({F(s-Bnext): p-1, F(Bnext, p): q-p})
                assert 0 < Bnext < p*e and Bnext % 2
                tangent = [c for c in range(1, N, p-1) if (B-c) % (p+1) == 0]
                assert len(tangent) == 2
                for c in tangent:
                    cp = p*c % N
                    assert cp % (p-1) == 1
                    assert (Bnext-cp) % (p+1) == 0
                    assert orbit(cp) == orbit(c)
                    assert (c+s-B) % N == (c-B) % N
                    local["tangent_weights"] += 1
                local["Newton_high_quotient_records"] += 1
                if B % p == 0:
                    Blow = B//p
                    assert alpha+(p-1)*beta == s-Blow
                    assert p*beta/q == F(Blow, p)
                    for c in tangent:
                        assert (Blow-p*c) % (p+1) == 0
                    local["low_quotient_records"] += 1
            # Common-high-line small-parameter modular uniqueness.
            small = [b for b in range(1, e) if p*b < e]
            assert all(0 < b < p-1 for b in small)
            for b1, b2 in itertools.product(small, repeat=2):
                if (b1-b2) % (p-1) == 0:
                    assert b1 == b2
                local["wild_small_congruences"] += 1
            large_images = []
            for b in range(1, e):
                B = p*b
                if B < e:
                    assert high(B) % p == 0
                else:
                    assert high(B) % p
                    large_images.append(high(B))
                local["wild_divisible_quotients"] += 1
            assert len(large_images) == len(set(large_images))
            ks = [k for k in range(1, e) if p*k < e]
            for k in ks:
                B2 = p*p*k
                assert B2 > e and high(B2) % p
                assert (B2//p) % p == 0
                for b in range(1, e):
                    if b % p == 0:
                        continue
                    alpha = s-p*b
                    assert alpha >= e+p
                    assert p*p*(alpha-p*k) > p**3 > b-p*k
                    B1 = p*b
                    if B1 < e:
                        assert high(B1) % p == 0
                    else:
                        assert high(B1) % p and high(B1) != high(B2)
                    local["tame_mixed_divisibility"] += 1
            for k1, k2 in itertools.product(ks, repeat=2):
                B1, B2 = p*p*k1, p*p*k2
                assert high(B1) % p and (B2//p) % p == 0
                if high(B1) == high(B2):
                    assert k1 == k2
                local["tame_two_divisible"] += 1
            # Actual-target unweighted [p] recurrence, for every possible
            # norm-one tame degree, not an estimate on the two source models.
            square = []
            for m in range(1, p+2):
                if (p+1) % m:
                    continue
                aa = e*m
                q1 = min(aa+1, p+1, p*p)
                q2 = min(aa+q1, p*q1+1, p*p*q1)
                assert q1 >= p+1
                assert F(aa, p-1) <= N
                assert q2 >= F(aa, p-1)
                square.append({"m": m, "a": aa, "q1": q1, "q2": q2,
                               "threshold": str(F(aa, p-1))})
                local["square_target_bounds"] += 1
            # Both full-monodromy thresholds: actual p² failure exists and
            # actual p³ mixed comparison is forbidden.
            assert e > p and e <= p**3 and e % (p-1) == 0
            local["lower_and_mixed_thresholds"] += 1
            counts.update(local)
            summaries.append({"p": p, "t": t, "e": e, "s": s,
                              "counts": dict(local), "square_bounds": square})
    assert [x["e"] for x in summaries if x["p"] == 5] == [8, 12, 16]
    return {
        "status": "PASS", "actual_utc": datetime.now(timezone.utc).isoformat(),
        "runtime_seconds": time.perf_counter()-start, "primes": primes,
        "sectors_checked": len(summaries), "counts": dict(counts),
        "per_sector": summaries,
        "scope": "Finite exact Newton polygons and actual quotient multiplicities, tangent congruences, common-point-field inequalities and actual-target bounds. The all-prime theorem relies on the complete proof and B67, not this finite test."
    }

if __name__ == "__main__":
    try:
        result = main()
    except Exception:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        source = Path(__file__)
        source.with_name(source.stem+".failed."+stamp+".py").write_bytes(source.read_bytes())
        source.with_name(source.stem+".failed."+stamp+".txt").write_text(traceback.format_exc())
        raise
    Path(__file__).with_suffix(".output.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k != "per_sector"}, indent=2))
