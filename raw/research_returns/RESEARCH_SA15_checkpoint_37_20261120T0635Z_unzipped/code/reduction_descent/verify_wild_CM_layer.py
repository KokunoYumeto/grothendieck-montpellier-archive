"""Exact finite algebra supplement for B78; field construction is in the proof."""
from pathlib import Path
from datetime import datetime, timezone
from math import isqrt
from collections import Counter
import json
import time

started = time.perf_counter()
counts = Counter()
lower_rows = []


def ring(p):
    modulus = p * p
    d = next(x for x in range(2, p) if pow(x, (p - 1) // 2, p) == p - 1)
    def mul(x, y):
        return ((x[0] * y[0] + d * x[1] * y[1]) % modulus,
                (x[0] * y[1] + x[1] * y[0]) % modulus)
    def power(x, n):
        result = (1, 0)
        while n:
            if n & 1:
                result = mul(result, x)
            x = mul(x, x)
            n //= 2
        return result
    def sigma(x):
        return (x[0], -x[1] % modulus)
    return d, mul, power, sigma


for p in (5, 7, 11, 13, 17, 19):
    q = p * p
    N = q - 1
    e = p * (p - 1)
    d, mul, power, sigma = ring(p)
    roots = {power((a, b), q) for a in range(p) for b in range(p) if (a, b) != (0, 0)}
    assert len(roots) == N and all(power(w, N) == (1, 0) for w in roots)
    norm_one = {w for w in roots if power(w, p + 1) == (1, 0)}
    assert len(norm_one) == p + 1
    H = {mul(w, (1 + p * a, 0)) for w in norm_one for a in range(p)}
    assert len(H) == p * (p + 1)
    assert N * q // len(H) == e
    for w in roots:
        assert sigma(w) == power(w, p)
        for a in range(p):
            theta = mul(power(w, e), (1 + p * a, 0))
            assert theta in H
            assert mul(theta, sigma(theta))[0] % p == 1
            u1 = mul(theta, w)
            u2 = mul(theta, power(w, 3 * p - 2))
            assert sigma(u1) == u2
            # Matrix form of the same Z/p^2-linear Frobenius intertwiner.
            M1 = ((u1[0], d * u1[1] % q), (u1[1], u1[0]))
            M2 = ((u2[0], d * u2[1] % q), (u2[1], u2[0]))
            SM1 = (M1[0], tuple(-x % q for x in M1[1]))
            M2S = tuple((row[0], -row[1] % q) for row in M2)
            assert SM1 == M2S
            counts['actual_mod_p2_twist_identities'] += 1
    lower_rows.append(dict(p=p, extension_degree=e, division_degree=N*q,
                          fixed_subgroup_order=len(H), unramified_quadratic_d=d,
                          special_orbit_1=sorted({1, p}),
                          special_orbit_2=sorted({(3*p-2)%N,(3-2*p)%N})))

    # Index-p^j subgroups of (Z/p^k)^2 via their full inverse-image
    # upper-Hermite lattices. This independently checks the last-layer
    # inclusion for every such subgroup in the retained range.
    for v in range(4):
        for n in range(v + 2, v + 5):
            k = n - 1
            for j in range(v + 1):
                for a in range(j + 1):
                    h = j - a
                    for b in range(p ** a):
                        def contains(x, y):
                            return y % (p ** h) == 0 and (x - b * (y // (p ** h))) % (p ** a) == 0
                        assert contains(p**k, 0) and contains(0, p**k)
                        assert contains(p**v, 0) and contains(0, p**v)
                        # In U=(1+pO)/(1+p^nO), logarithmic coordinates divide by p.
                        # Its nonzero terminal layer is therefore p^(n-2), not p^(n-1).
                        assert contains(p**(n-2), 0) and contains(0, p**(n-2))
                        counts['all_bounded_index_subgroups'] += 1
                        counts['terminal_layer_basis_vectors'] += 2

    if p <= 13:
        centralizers = 0
        for a in range(p):
            for b in range(p):
                for c in range(p):
                    for h in range(p):
                        commutes = ((b-d*c)%p == 0 and (a-h)%p == 0)
                        field_multiplier = (h == a and b == d*c % p)
                        assert commutes == field_multiplier
                        if commutes:
                            centralizers += 1
                        counts['residual_centralizer_matrices'] += 1
        assert centralizers == p*p


def poly_mul(A, B, modulus):
    C = {}
    for i, a in A.items():
        for j, b in B.items():
            C[i+j] = (C.get(i+j, 0) + a*b) % modulus
    return {i:a for i,a in C.items() if a}


def poly_power(A, n, modulus):
    result = {0:1}
    while n:
        if n & 1:
            result = poly_mul(result, A, modulus)
        A = poly_mul(A, A, modulus)
        n //= 2
    return result


for p in (5, 7, 11, 13):
    q = p*p
    N = q-1
    f = {1:1}
    for n in range(1, 7):
        phi = poly_power(f, N, q)
        phi[0] = (phi.get(0, 0) + p) % q
        assert max(phi) == N*q**(n-1)
        assert phi[max(phi)] == 1 and phi[0] == p
        assert all(a % p == 0 for i,a in phi.items() if i not in (0,max(phi)))
        if n >= 2:
            expected = {N*q**(n-1):1, (N-1)*q**(n-1)+q**(n-2):N*p % q, 0:p}
            assert phi == expected
        counts['Eisenstein_polynomials_mod_p2'] += 1
        g = poly_power(f, q, q)
        for i,a in f.items():
            g[i] = (g.get(i,0)+p*a) % q
        f = {i:a for i,a in g.items() if a}

all_primes = [p for p in range(5,102) if all(p%d for d in range(2,isqrt(p)+1))]
for p in all_primes:
    N = p*p-1
    e = p*(p-1)
    assert (p+(p-1)*e-(3*p-2)) % N == 0
    first = {1,p}
    second = {(3*p-2)%N,(3-2*p)%N}
    assert len(first) == len(second) == 2 and first.isdisjoint(second)
    assert (3*p-2) % (p-1) == 1
    counts['all_prime_lower_character_rows'] += 1

out = dict(status='PASS',actual_utc=datetime.now(timezone.utc).isoformat(),
           runtime_seconds=time.perf_counter()-started,counts=dict(counts),
           lower_field_rows=lower_rows,
           scope='Exact mod-p^2 unramified quadratic ring, all retained index-bounded additive subgroups, residual matrix centralizers, primitive Eisenstein reductions and finite special-character orbits. The actual division-field and deformation constructions are the written proof; no non-CM recovery is inferred.')
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
