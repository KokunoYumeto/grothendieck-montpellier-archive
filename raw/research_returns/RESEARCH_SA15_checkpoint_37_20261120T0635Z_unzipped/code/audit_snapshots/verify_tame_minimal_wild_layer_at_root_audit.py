"""Exact arithmetic supplement to B55; no formal group is instantiated."""
from fractions import Fraction
from pathlib import Path
import datetime
import json
import math
import time

started = time.perf_counter()
primes = [n for n in range(5, 102)
          if all(n % d for d in range(2, math.isqrt(n) + 1))]
valuation_cases = 0
minimal_cases = 0
field_elements = 0
scalar_candidates = 0
pair_cases = 0
p5 = {}

for p in primes:
    q, N = p*p, p*p-1
    for t in range(1, N+1):
        if N % t:
            continue
        for r in range(5):
            A = Fraction(t * p**r, (p+1)*p*p)
            valuation_cases += 1
            if A.denominator == 1:
                assert r >= 2
                if r == 2:
                    minimal_cases += 1
                    assert A == Fraction(t, p+1)
                    assert A.numerator % p
                    b = (q-1)*A
                    assert A+b == q*A
                    # Every higher Teichmuller degree has strictly higher error.
                    for j in range(A.numerator+1, A.numerator+33):
                        assert j+b > A+b
    n = next(a for a in range(2, p) if pow(a, (p-1)//2, p) == p-1)

    def mul(x, y):
        a, b = x
        c, d = y
        return ((a*c+n*b*d) % p, (a*d+b*c) % p)

    def power(x, exponent):
        out = (1, 0)
        while exponent:
            if exponent & 1:
                out = mul(out, x)
            x = mul(x, x)
            exponent >>= 1
        return out

    elements = [(a, b) for a in range(p) for b in range(p)]
    for x in elements:
        field_elements += 1
        assert power(x, q) == x
        assert power(x, p) == (x[0], (-x[1]) % p)
    for beta in elements:
        scalar_candidates += 1
        witness = (1, 0) if beta != (1, 0) else (0, 1)
        assert mul(beta, witness) != power(witness, p)

    # Actual normalized orientations, not only unordered abstract type names.
    cs = list(range(1, N, p-1))
    for c1 in cs:
        c2 = (p*c1+(p-1)**2) % N
        type1 = {c1 % N, p*c1 % N}
        type2 = {c2 % N, p*c2 % N}
        alpha1, alpha2 = (c1+p-1) % N, (c2+p-1) % N
        if alpha1 % (p+1) == 0:
            continue
        if type1 != type2:
            pair_cases += 1
            assert alpha2 == p*alpha1 % N
            assert alpha1 != alpha2
            assert math.gcd(math.gcd(N, c1), c2) == 1
    if p == 5:
        p5 = {
            'joint_good_degree': N,
            'minimal_wild_order_excluded': q,
            'remaining_wild_orders': [p**3, p**4],
            'primitive_coordinate_valuation_in_minimal_case': p-1,
            'common_lower_break_in_minimal_case': N*(p-1),
        }

result = {
    'status': 'PASS',
    'actual_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope': ('Finite valuation, finite-field and normalized-character arithmetic only; '
              'no Barsotti-Tate model or torsion-congruent pair is constructed.'),
    'primes': primes,
    'valuation_cases': valuation_cases,
    'minimal_integral_cases': minimal_cases,
    'field_elements_checked': field_elements,
    'scalar_frobenius_candidates_excluded': scalar_candidates,
    'distinct_type_orientation_pairs': pair_cases,
    'p5': p5,
    'runtime_seconds': time.perf_counter()-started,
}
dest = Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work/outputs/root_b55_exact_arithmetic.json')
dest.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
