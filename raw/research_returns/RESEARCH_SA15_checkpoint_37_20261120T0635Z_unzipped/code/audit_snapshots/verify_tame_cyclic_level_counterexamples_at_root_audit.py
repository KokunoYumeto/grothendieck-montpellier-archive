"""Exact finite supplements for B62; no formal-group existence inferred here.

Checks arithmetic ranges/strict weights, specialized logarithm homogeneity,
direct multiplication-series coefficients through degree p^2 for four primes,
and characteristic-zero finite-character identities.  The theorem is the
symbolic proof in B_tame_cyclic_level_counterexamples.tex.
"""
from fractions import Fraction
from math import gcd, comb
from pathlib import Path
from datetime import datetime, timezone
import json
import time

start = time.perf_counter()


def isprime(n):
    return n >= 2 and all(n % d for d in range(2, int(n ** .5) + 1))


primes = [p for p in range(5, 102) if isprime(p)]
counts = dict(arithmetic_cases=0, iterate_weight_checks=0,
              logarithm_monomials=0, direct_series_coefficients=0,
              character_cases=0, first_threshold_cases=0)
examples = []

for p in primes:
    q, N = p * p, p * p - 1
    for n in range(2, 13):
        low, high = p ** (2 * n - 3), p ** (2 * n - 2)
        first = low + p - 2
        assert first % (p - 1) == 0
        assert first - (p - 1) <= low < first < high
        assert first % p == p - 2
        counts['first_threshold_cases'] += 1
        last = ((high - 1) // (p - 1)) * (p - 1)
        if n == 2:
            es = range(first, high, p - 1)
        else:
            middle = ((low + high) // (2 * (p - 1))) * (p - 1)
            es = sorted({first + j * (p - 1) for j in range(20)} |
                        {last - j * (p - 1) for j in range(20)} |
                        {middle + j * (p - 1) for j in range(-10, 10)})
        for e in es:
            if not (low < e < high):
                continue
            d = N * e
            b = d - (p - 1) * q ** (n - 1)
            assert b - (q - p) * q ** (n - 2) == N * (e - low) > 0
            assert b > 0 and d > q ** (n - 1)
            assert d < N * q ** (n - 1)
            assert (b + p - 1) % N == 0
            assert b + (p - 1) * q ** (n - 1) == d
            for j in range(1, n):
                w = q ** (j - 1)
                # The qth term is uniquely first in [p](X^w).
                assert q * w < b + p * w
                assert q * w < d + w
                # Each intermediate term is later than the pth term.
                assert b + (p + 1) * w > b + p * w
                assert (q + 1) * w > q * w
                counts['iterate_weight_checks'] += 1
            w = q ** (n - 1)
            assert b + (p - 1) * w < b + p * w
            assert b + (p - 1) * w < N * w
            counts['arithmetic_cases'] += 1
            if p in (5, 7) and n in (2, 3) and e == first:
                examples.append(dict(p=p, n=n, e=e, d=d, b=b,
                                     point_valuations=[q ** j for j in range(n)]))

    # Specialized HG recursion as sparse Q[u]-polynomials; exact denominators.
    logs = [{0: Fraction(1)}]
    for j in range(1, 13):
        nxt = {}
        for exponent, coefficient in logs[j - 1].items():
            nxt[exponent + p ** (j - 1)] = coefficient / p
        if j >= 2:
            for exponent, coefficient in logs[j - 2].items():
                nxt[exponent] = nxt.get(exponent, 0) + coefficient / p
        logs.append(nxt)
        for exponent, coefficient in nxt.items():
            assert ((p - 1) * exponent - (p ** j - 1)) % N == 0
            assert (coefficient * p ** j).denominator == 1
            counts['logarithm_monomials'] += 1
    assert logs[1] == {1: Fraction(1, p)}
    assert logs[2] == {p + 1: Fraction(1, p * p), 0: Fraction(1, p)}

    # Character exponents and determinant; a=zeta^-1.
    assert N // gcd(N, p + 1) == p - 1
    assert sorted([1 % N, p % N]) != sorted([0, (p + 1) % N])
    assert (1 + p) % N == (0 + p + 1) % N
    # The formal Laurent-polynomial trace identity has four distinct exponents.
    lhs = {0: -1, 1: 1, p: 1, p + 1: -1}
    rhs = {}
    for i, ai in ((1, 1), (0, -1)):
        for j, bj in ((p, 1), (0, -1)):
            rhs[i + j] = rhs.get(i + j, 0) - ai * bj
    assert lhs == rhs
    assert gcd(1, N) == gcd(p, N) == 1
    counts['character_cases'] += 1


def mul_trunc(A, B, degree):
    out = [Fraction(0) for _ in range(degree + 1)]
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            if i + j <= degree:
                out[i + j] += a * b
    return out


def power_coeff(A, power, degree):
    out = [Fraction(1)]
    for _ in range(power):
        out = mul_trunc(out, A, degree)
    return out[degree]


direct = []
for p in (5, 7, 11, 13):
    # Put S=u*T^(p-1).  Up to degree p^2, all terms below the
    # last one are alpha_j*u^j*T^(1+j*(p-1)).
    alpha = [Fraction(p)]
    for j in range(1, p + 1):
        value = (Fraction(1) if j == 1 else Fraction(0))
        value -= power_coeff(alpha, p, j - 1) / p
        assert value.denominator == 1
        alpha.append(value)
        counts['direct_series_coefficients'] += 1
    last_u = Fraction(1, p) - power_coeff(alpha, p, p) / p - p ** (p * p - 2)
    last_constant = 1 - p ** (p * p - 1)
    assert last_u.denominator == 1
    assert alpha[1] == 1 - p ** (p - 1)
    assert last_constant % p == 1
    counts['direct_series_coefficients'] += 1
    direct.append(dict(p=p, coefficient_Tp=int(alpha[1]),
                       coefficient_Tp2_at_u0=last_constant,
                       coefficient_u_pplus1_Tp2=int(last_u)))

elapsed = time.perf_counter() - start
result = dict(result='PASS', actual_utc=datetime.now(timezone.utc).isoformat(),
              elapsed_seconds=elapsed, counts=counts, examples=examples,
              direct_series=direct,
              finite_scope='Primes5..101; levels2..12; all admissible e for n2 and stated first/last/middle windows otherwise. Sparse logarithms through j12. Direct multiplication coefficients through p² for p5,7,11,13.',
              not_computed='No infinite formal group, DVR, Galois representation, Kummer lift, or character comparison is inferred from the finite range; these are proved symbolically in the TeX file.')
out = Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work/outputs/root_tame_cyclic_level_counterexamples.json')
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
