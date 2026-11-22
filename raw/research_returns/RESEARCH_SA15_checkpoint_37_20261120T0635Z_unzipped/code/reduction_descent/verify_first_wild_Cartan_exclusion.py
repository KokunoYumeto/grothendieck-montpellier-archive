"""Exact finite supplement for B81. No actual group existence is inferred."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
from itertools import product
from math import comb, isqrt
import json, time
import sympy as sp

start = time.perf_counter()
counts = Counter()
rows = []
P, a, b = sp.symbols('p a b')
Q = P**2
AA = P*(P-1)
DD1, DD2 = Q*AA, Q**2*AA
a_zero = (Q-1)*(P-1)
j_zero = AA+(P-1)*a_zero
identities = [
    DD1-AA-P*a_zero,
    j_zero-(DD1-a_zero),
    a_zero-1-P*(P**2-P-1),
    j_zero-(P-1)-P*(P**3-2*P**2+P),
    AA+P*b-(AA+(P-1)*a+b)-(P-1)*(b-a),
    AA+P*b-(DD1-a+b)-((P-1)*(b-a)+P*(a-a_zero)),
    AA+P*b-(j_zero+b)-(P-1)*(b-a_zero),
    P*(DD2-j_zero)-(DD2-AA)-(P-1)*(DD2-DD1),
]
for expr in identities:
    assert sp.expand(expr) == 0, sp.factor(expr)
    counts['symbolic_identities'] += 1

primes = [p for p in range(5, 102) if all(p%d for d in range(2, isqrt(p)+1))]
for p in primes:
    q, N = p*p, p*p-1
    A = p*(p-1)
    D1, D2 = q*A, q*q*A
    a0 = N*(p-1)
    j0 = A+(p-1)*a0
    terminal_b = D2-j0
    assert (a0%p, j0%p) == (1, p-1)
    assert A < j0 < D1 < D2 < N*D2
    assert terminal_b > a0
    assert p*terminal_b-(D2-A) == (p-1)*(D2-D1) > 0
    assert A+p*terminal_b > D2
    assert j0+terminal_b == D2
    assert all(comb(A, k)%p == 0 for k in range(1, p))
    assert comb(A, p)%p == (A//p)%p != 0
    counts['initial_binomial_rows'] += 1
    for later_b in (a0+1, a0+p, 2*a0, terminal_b):
        assert A+p*later_b > D1
        assert j0+1+later_b > D1
        assert A+p*later_b-(j0+later_b) == (p-1)*(later_b-a0) > 0
        counts['vanishing_boundary_exclusions'] += 1
    rows.append({'p':p,'A':A,'D1':D1,'D2':D2,'a0':a0,'j0':j0,
                 'boundary_terminal_break':terminal_b})

    # Exhaustive first-break degrees at the three stated small primes.
    # The full uniform comparisons are the polynomial identities above.
    if p <= 11:
        for first_a in range(1, D1-A+1):
            if first_a == a0:
                continue
            j = A+(p-1)*first_a if first_a<a0 else D1-first_a
            if j < A or j%p == 0:
                counts['impossible_prime_degree_rows'] += 1
                continue
            assert j > A
            for later_b in sorted({first_a+1,first_a+p,first_a+q,D2-j}):
                assert later_b > first_a
                gap = A+p*later_b-(j+later_b)
                assert gap > 0
                if first_a<a0:
                    assert gap == (p-1)*(later_b-first_a)
                else:
                    assert gap == (p-1)*(later_b-first_a)+p*(first_a-a0)
                counts['later_terminal_comparisons'] += 1
            forced_b = D2-j
            assert j+forced_b == D2 and A+p*forced_b > D2
            counts['exhaustive_small_prime_first_breaks'] += 1

    nonsquare = next(x for x in range(2,p) if pow(x,(p-1)//2,p)==p-1)
    def mul(x,y,m):
        return ((x[0]*y[0]+nonsquare*x[1]*y[1])%m,
                (x[0]*y[1]+x[1]*y[0])%m)
    def power(x,n,m):
        z=(1,0)
        while n:
            if n&1:z=mul(z,x,m)
            x=mul(x,x,m);n//=2
        return z
    for scalar in product(range(p), repeat=2):
        matches = [mul(scalar,x,p)==power(x,p,p) for x in ((1,0),(0,1))]
        assert not all(matches)
        counts['Frobenius_not_scalar_tests'] += 1
    if p <= 11:
        modulus = p**3
        fibres = Counter()
        for x,y in product(range(p*p),repeat=2):
            unit=((1+p*x)%modulus,p*y%modulus)
            got=power(unit,p,modulus)
            want=((1+p*p*(x%p))%modulus,p*p*(y%p)%modulus)
            assert got == want
            assert power(unit,p*p,modulus) == (1,0)
            fibres[got] += 1
            counts['literal_Cartan_pth_powers'] += 1
        assert len(fibres)==q and set(fibres.values())=={q}
        counts['surjective_terminal_power_maps'] += 1

out = {
    'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
    'runtime_seconds':time.perf_counter()-start,'counts':dict(counts),
    'boundary_rows':rows,
    'scope':'Eight symbolic identities; all relevant first-break degrees for p5,7,11; '
            'literal pth powers in the full quadratic principal-unit groups at those primes; '
            'boundary degree, binomial and two-basis scalar/Frobenius tests for primes5..101. '
            'The actual coordinate, ramification and orientation proofs are separate. '
            'No formal-group existence, larger wild-image or reducible-residual assertion.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
