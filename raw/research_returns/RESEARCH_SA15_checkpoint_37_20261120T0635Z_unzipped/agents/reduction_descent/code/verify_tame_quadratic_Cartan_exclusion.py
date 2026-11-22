#!/usr/bin/env python3
"""Exact finite supplement to B102; actual-field proof is separate."""
import hashlib
import itertools
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter

import sympy as sp


def mul(a, b, modulus):
    return tuple(sum(a[2*i+k] * b[2*k+j] for k in range(2)) % modulus
                 for i in range(2) for j in range(2))


def power(a, n, modulus):
    result = (1, 0, 0, 1)
    while n:
        if n & 1:
            result = mul(result, a, modulus)
        a = mul(a, a, modulus)
        n //= 2
    return result


def first_binomial_degree(k, p):
    return next(j for j in range(1, k + 1) if math.comb(k, j) % p)


def main():
    started = perf_counter()
    counts = dict(symbolic_identities=0, primes=0, character_rows=0,
                  quadratic_rows=0, inverse_polygon_checks=0,
                  literal_matrix_powers=0, literal_displacement_checks=0,
                  commutator_planes=0, fixed_expansion_cases=0,
                  direct_binomial_checks=0)
    p, a, b, A1, A2 = sp.symbols('p a b A1 A2')
    q = p**2
    J = A1 + (p-1)*a
    identities = [
        (A1+p*b)-(J+b)-(p-1)*(b-a),
        (q*q*A1-J)-((q*q-1)*A1-(p-1)*a),
        (q*q-1)*(p*A2-A2)-(p-1)*(q-1)*A2
          -(p-1)*q*(q-1)*A2,
        p*(p-1)*(p+2)/2-(p+2)*p*(p-1)/2,
        (p+1)*p*(p-1)-p*p*(p-1)/2-p*(p-1)*(p+2)/2,
        p*(p-1)*(p*p-1)-p*(p-1)*(p+2)/2
          -p*(p-1)*(2*p*p-p-4)/2,
    ]
    for expression in identities:
        assert sp.expand(expression) == 0
        counts['symbolic_identities'] += 1

    prime_list = [n for n in range(5, 102) if sp.isprime(n)]
    quadratic_samples = []
    for P in prime_list:
        counts['primes'] += 1
        Q, N, e = P*P, P*P-1, P*(P-1)
        for k in range(1, P-1):
            counts['character_rows'] += 1
            if (2*k) % (P-1) == 0:
                assert k == (P-1)//2
        if P % 4 != 3:
            continue
        k = (P-1)//2
        B = Q*k
        alpha = (P+1)*e-B
        beta = B//P
        assert alpha == (P+2)*beta > P*beta
        assert alpha % P == beta % P == 0
        assert (alpha//P) % P and (beta//P) % P
        assert B > e and alpha < e*N
        assert (P-1)*B*Q > (Q-P)*alpha
        # Each subsequent, smaller target also has its p-vertex above chord.
        for numerator, denominator in [(alpha, 1), (alpha, Q),
                                       (beta, 1), (beta, Q)]:
            assert (P-1)*B*Q*denominator > (Q-P)*numerator
            assert e*N*Q*denominator > (Q-1)*numerator
            counts['inverse_polygon_checks'] += 1
        assert Q*Q*alpha < e*N*Q*Q
        assert (Q*Q-1)*(alpha-beta) > (P-1)*(Q-1)*beta
        counts['quadratic_rows'] += 1
        quadratic_samples.append(dict(p=P, B=B, A1=alpha, A2=beta))

    # Literal p-th powers in the actual modulus, including arbitrary second digits.
    for P in [5, 7, 11]:
        modulus = P**3
        for C in itertools.product(range(P), repeat=4):
            g = tuple(((1+P if i in (0, 3) else 0)+P*P*C[i]) % modulus
                      for i in range(4))
            gp = power(g, P, modulus)
            assert gp == (1+P*P, 0, 0, 1+P*P)
            assert power(gp, P, modulus) == (1, 0, 0, 1)
            assert gp != (1, 0, 0, 1)
            counts['literal_matrix_powers'] += 1
            # P(g-I)e1 = P² e1 and (g^p-I)e1=P²e1 as actual Z/p³ vectors.
            assert (P*(g[0]-1)) % modulus == P*P
            assert (P*g[2]) % modulus == 0
            assert (gp[0]-1, gp[2]) == (P*P, 0)
            counts['literal_displacement_checks'] += 1
        for d1, d2, u, v in itertools.product(range(1, P), repeat=4):
            # An off-diagonal commutator belongs to the same off-line iff D scalar.
            comm12, comm21 = (d1-d2)*u % P, (d2-d1)*v % P
            dependence = (comm12*v-comm21*u) % P == 0
            assert dependence == (d1 == d2)
            counts['commutator_planes'] += 1

    # Direct binomial coefficients, not a p-adic-order formula, check the
    # competing first changes in finitely many fixed-coordinate expansions.
    for P in [5, 7, 11]:
        Q = P*P
        for multiple in range(1, 4):
            second = P*multiple
            first = (P+2)*second
            first_j = {k:first_binomial_degree(k, P)
                       for k in range(first, first+4*P+1)}
            counts['direct_binomial_checks'] += len(first_j)
            for low_break in range(1, 4*P+1):
                if not low_break <= (Q-1)*second:
                    continue
                assert first+P*low_break < Q*first
                ordinary = first+(P-1)*low_break
                if ordinary % P == 0:
                    continue
                for terminal_break in [low_break+1, low_break+P, Q*first]:
                    assert ordinary+terminal_break < first+P*terminal_break
                    for k, degree in first_j.items():
                        if k > first and k % P == 0:
                            assert k+degree*low_break > first+P*low_break
                            assert k+degree*terminal_break > ordinary+terminal_break
                    counts['fixed_expansion_cases'] += 1

    result = dict(status='PASS', actual_utc=datetime.now(timezone.utc).isoformat(),
                  runtime_seconds=perf_counter()-started, counts=counts,
                  quadratic_parameter_samples=quadratic_samples,
                  scope='Finite exact supplement only. It does not construct any formal group, '
                        'prove a Galois field realization, or replace the uniform actual-field proof.',
                  program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    destination = Path(__file__).with_suffix('.output.json')
    destination.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
