"""Exact finite supplement to B67, with genuinely nonminimal tame indices.

No BT group or congruent pair is constructed. The arbitrary-index theorem
is proved in the accompanying text, not inferred from these finite checks.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
from fractions import Fraction
import itertools, json, math, time, traceback

def main():
    started = time.perf_counter()
    counts = Counter()
    indices = []
    for p in (5, 7, 11, 13, 17, 19):
        q, N = p*p, p*p-1
        for t in range(1, 2*p+4):
            e = t*(p-1)
            if e % p == 0:
                continue
            b0 = N*e
            indices.append((p, e))
            for r in (2, 3, 4):
                A = e*p**(r-2)
                eF = e*N*p**r
                assert eF == N*q*A and eF > q*A
                assert A % p**(r-2) == 0 and A % p**(r-1) != 0
                eta_exp = pow(pow(p, r, N), -1, N)
                assert (eta_exp*A-e) % N == 0
                assert Fraction(e, q)*p**r == A
                counts["field_normalizations"] += 1
                # Independent binomial coefficients check the first ordinary
                # characteristic-p change for actual, nonminimal A.
                candidates = sorted({A+j for j in range(13)}
                                    | {p*(A//p+j) for j in range(1, 5)}
                                    | {q*(A//q+j) for j in range(1, 3)})
                for j in candidates:
                    power = 1
                    while j % (power*p) == 0:
                        power *= p
                    if power > q:
                        assert j > A and j+power > A+p**(r-2)
                        counts["higher_divisibility_later_terms"] += 1
                        continue
                    assert math.comb(j, power) % p == (j//power) % p
                    assert all(math.comb(j, k) % p == 0 for k in range(1, power))
                    counts["binomial_first_terms"] += 1
            cycloval = e*N//(p-1)
            assert e*N % (p-1) == 0 and cycloval % p
            assert p*cycloval-cycloval == b0
            assert q*e-e == b0
            counts["point_and_cyclotomic_breaks"] += 1
            # Check the plus-sign leading character and oriented Frobenius
            # relation, without assuming joint faithful degree N.
            for c in range(N):
                lam = (c+e) % N
                if lam % (p+1) == 0:
                    continue
                d = (p*c+(p-1)*e) % N
                assert (d+e) % N == p*lam % N
                assert d % (p-1) == c % (p-1)
                if {c, p*c % N} != {d, p*d % N}:
                    assert d != c
                    assert lam != p*lam % N
                    counts["different_oriented_characters"] += 1
                counts["irreducible_leading_characters"] += 1

            # Cubic wild image: exact compatibility of the first ordinary
            # coefficient, with c=b0 retained as an explicit edge case.
            A = p*e
            target = q*A
            anti = {N//2+j*N for j in range(min(e+3, 14))}
            anti |= {b0+N//2, b0+3*N//2}
            cartan = {j*N for j in range(1, 15)}
            cartan |= {b0, b0+N, b0+2*N}
            def signature(kind, b):
                if b == b0:
                    return None
                j = A+(p-1)*b if b < b0 else target-b
                if not A < j < target or j % p == 0:
                    return False
                return j, ("linear" if b < b0 or kind == "Cartan" else "Frobenius")
            valid = [(b, signature("anti", b)) for b in sorted(anti)
                     if signature("anti", b)]
            for b, sig in valid:
                assert b != b0
                counts["cubic_first_signatures"] += 1
                for b2, sig2 in valid:
                    if b2 > b:
                        assert sig != sig2
                        counts["cubic_two_anti_comparisons"] += 1
                possible_c = cartan | {p*b0-(p-1)*b}
                for c in possible_c:
                    if c <= 0:
                        continue
                    if c == b0:
                        compatible = sig[0] >= target-b0
                    else:
                        cs = signature("Cartan", c)
                        compatible = bool(cs) and cs == sig
                    expected = b < b0 and b % p and c == p*b0-(p-1)*b
                    assert compatible == bool(expected), (p, e, b, c, sig)
                    counts["cubic_Cartan_comparisons"] += 1

            # Full wild image: both anti-plane patterns and exact Herbrand
            # sums. These are conditional arithmetic patterns only.
            A = q*e
            target = q*A
            for b in range(N//2, b0, N):
                if b % p == 0:
                    continue
                K = A+N*b
                J = A+(q-p)*b
                c = target-K
                assert A < K < target and K % p
                assert J % p == 0 and J % q != 0
                assert c > b0 and c > b
                assert K+c == target < J+p*c
                assert J+p*c-(K+c) == (p-1)*(c-b)
                assert A+q*c-(K+c) == N*(c-b)
                assert q*b+c-b == q*b0
                counts["full_single_break_patterns"] += 1
            for b1 in range(N//2, min(b0, 12*N), N):
                if b1 % p == 0:
                    continue
                for jump in range(1, 10):
                    b2 = b1+jump*N
                    if b2 % p == 0:
                        continue
                    J = A+(q-p)*b1
                    K = J+(p-1)*b2
                    c = target-K
                    if c <= max(b0, b2):
                        continue
                    assert A+q*b1 == J+p*b1 < K+b1
                    assert J+p*b2 == K+b2 < A+q*b2
                    assert A+q*b1 < target and J+p*b2 < target
                    assert K+c == target < J+p*c
                    assert J % p == 0 and J % q != 0 and K % p
                    assert c % N == 0
                    assert q*b1+p*(b2-b1)+c-b2 == q*b0
                    counts["full_two_break_patterns"] += 1

    # General two-dimensional planes in cubic fields. Their root polynomial
    # need not have zero middle coefficient; the test deliberately retains it.
    for p in (5, 7, 11):
        cubic = next((c0, c1, c2)
                     for c0 in range(1, p) for c1 in range(p) for c2 in range(p)
                     if all((x**3+c2*x*x+c1*x+c0) % p for x in range(p)))
        zero, one = (0, 0, 0), (1, 0, 0)
        elements = list(itertools.product(range(p), repeat=3))
        def add(a, b):
            return tuple((a[i]+b[i]) % p for i in range(3))
        def sub(a, b):
            return tuple((a[i]-b[i]) % p for i in range(3))
        def scale(n, a):
            return tuple(n*x % p for x in a)
        def mul(a, b):
            v = [0]*5
            for i in range(3):
                for j in range(3):
                    v[i+j] = (v[i+j]+a[i]*b[j]) % p
            for j in (4, 3):
                for k, ck in enumerate(cubic):
                    v[j-3+k] = (v[j-3+k]-v[j]*ck) % p
            return tuple(v[:3])
        def power(a, n):
            out = one
            while n:
                if n & 1:
                    out = mul(out, a)
                a = mul(a, a)
                n //= 2
            return out
        xp = {x: power(x, p) for x in elements}
        xq = {x: xp[xp[x]] for x in elements}
        normals = [v for v in elements[1:] if next(x for x in v if x) == 1]
        assert len(normals) == p*p+p+1
        for normal in normals:
            D = [x for x in elements if sum(normal[i]*x[i] for i in range(3)) % p == 0]
            assert len(D) == p*p
            a = next(x for x in D if x != zero)
            line = {scale(n, a) for n in range(p)}
            b = next(x for x in D if x not in line)
            ap = power(a, p-1)
            yb = sub(xp[b], mul(ap, b))
            yp = power(yb, p-1)
            middle = scale(-1, add(power(ap, p), yp))
            linear = mul(yp, ap)
            assert yb != zero and linear != zero
            if middle != zero:
                counts["nonzero_middle_planes"] += 1
            Dset = set(D)
            for x in elements:
                result = add(xq[x], add(mul(middle, xp[x]), mul(linear, x)))
                assert (result == zero) == (x in Dset)
                counts["additive_root_tests"] += 1
            if p == 5:
                coeff = [one]
                for d in D:
                    out = [zero]*(len(coeff)+1)
                    for j, v in enumerate(coeff):
                        out[j] = sub(out[j], mul(d, v))
                        out[j+1] = add(out[j+1], v)
                    coeff = out
                expected = [zero]*(p*p+1)
                expected[1], expected[p], expected[p*p] = linear, middle, one
                assert coeff == expected
                counts["direct_polynomial_coefficients"] += len(coeff)
            counts["additive_planes"] += 1

    for p in (5, 7, 11, 13):
        ns = next(a for a in range(2, p) if pow(a, (p-1)//2, p) == p-1)
        for a, b in itertools.product(range(p), repeat=2):
            agree_one = (a, b) == (1, 0)
            agree_root = (b*ns % p, a) == (0, p-1)
            assert not (agree_one and agree_root)
            counts["scalar_Frobenius_candidates"] += 1
        # Low-break cardinality obstruction on an actual quadratic plane.
        powers = set()
        def qm(x, y):
            return ((x[0]*y[0]+ns*x[1]*y[1]) % p,
                    (x[0]*y[1]+x[1]*y[0]) % p)
        for x in itertools.product(range(p), repeat=2):
            if x == (0, 0):
                continue
            ans = (1, 0)
            for _ in range(p-1):
                ans = qm(ans, x)
            powers.add(ans)
            counts["low_break_plane_elements"] += 1
        assert len(powers) == p+1

    assert counts["full_two_break_patterns"] > 0
    assert counts["nonzero_middle_planes"] > 0
    return {
        "status": "PASS",
        "actual_utc": datetime.now(timezone.utc).isoformat(),
        "runtime_seconds": time.perf_counter()-started,
        "indices": indices,
        "counts": dict(counts),
        "scope": "Finite exact nonminimal-index normalization, binomial terms, conditional break arithmetic, arbitrary additive planes and Frobenius obstruction only; no group or pair existence is inferred."
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
    print(json.dumps({k: v for k, v in result.items() if k != "indices"}, indent=2))
