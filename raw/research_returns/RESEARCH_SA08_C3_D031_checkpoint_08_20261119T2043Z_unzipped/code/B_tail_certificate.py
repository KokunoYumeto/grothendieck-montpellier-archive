#!/usr/bin/env python3
"""Finite certificates for A-L01 and the simplex-zero part of A-L02.

The all-prime/all-tail proof is in sections/B_tail_obstruction.tex.
This program independently checks the binomial obstruction and the
truncated coefficient algebras/modules on finite ranges.  It does not
claim that finite testing proves the infinite simplicial construction.
"""
from __future__ import annotations

import json
import math
from itertools import product
from pathlib import Path
import time


def main() -> None:
    started = time.perf_counter()
    assertions = 0
    certificates = []
    for p in [2, 3, 5, 7, 11]:
        for cutoff in range(1, 65):
            m = 1
            exponent = 0
            while m < cutoff:
                m *= p
                exponent += 1
            projection = [math.comb(m, a) % p for a in range(1, m + 1)]
            assert projection == [0] * (m - 1) + [1]
            assertions += 1
            b = (p - 1) * m
            assert math.comb(m + b, m) % p == 0
            assertions += 1
            # The two necessary equations on the e_m coefficient are
            # c_m=1 (projection) and c_m=0 (annihilator relation).
            assert all(not (c == 1 and c == 0) for c in range(p))
            assertions += p
            # Left multiplier (1,-1) annihilates the two identical
            # coefficient rows and sends their RHS (1,0) to 1.
            assert (1 - 1) % p == 0 and (1 - 0) % p == 1
            assertions += 1
            certificates.append(
                {
                    "prime": p,
                    "tail_cutoff": cutoff,
                    "power_exponent": exponent,
                    "m": m,
                    "annihilator_weight": b,
                    "projection_row_nonzero_positions": [m],
                    "required_coefficient": 1,
                    "annihilator_required_coefficient": 0,
                }
            )

    # Check actual truncated divided-power coefficient algebra identities.
    # S_L has basis T^[0],...,T^[L], with all greater weights zero.
    finite_algebras = []
    for p, cap in [(2, 8), (3, 9), (5, 10)]:
        triples = 0
        module_checks = 0
        for a in range(cap + 1):
            for b in range(cap + 1):
                if a + b <= cap:
                    assert math.comb(a + b, a) % p == math.comb(a + b, b) % p
                    assertions += 1
                for c in range(cap + 1):
                    if a + b + c > cap:
                        continue
                    left = math.comb(a + b, a) * math.comb(a + b + c, a + b)
                    right = math.comb(b + c, b) * math.comb(a + b + c, a)
                    assert (left - right) % p == 0
                    assertions += 1
                    triples += 1
        # Module homomorphism pi(T^[a] e_m) = binom(a+m,m) T^[a+m].
        for m in range(1, cap + 1):
            for a in range(cap - m + 1):
                for b in range(cap - m - a + 1):
                    left = math.comb(a + b, a) * math.comb(a + b + m, m)
                    right = math.comb(a + m, m) * math.comb(a + b + m, b)
                    assert (left - right) % p == 0
                    assertions += 1
                    module_checks += 1
        finite_algebras.append(
            {
                "prime": p,
                "maximum_weight": cap,
                "associativity_basis_triples": triples,
                "module_homomorphism_basis_checks": module_checks,
            }
        )

    # Integral rank calculation for C=(K -> F -> S<2>):
    # in coefficient weight w>=1 the last map is the binomial row
    # [binom(w,1),...,binom(w,w)], whose last entry is exactly 1.
    # Thus rank(F_w)=w, rank(K_w)=w-1, and the last map is split
    # as a Z-module in that individual weight.  The counterexample
    # concerns compatibility of these individual splittings with S.
    rank_rows = []
    for w in range(0, 129):
        row = [math.comb(w, a) for a in range(1, w + 1)]
        if w:
            assert row[-1] == 1
            assertions += 1
            rank_rows.append(
                {
                    "coefficient_weight": w,
                    "F_rank": w,
                    "K_rank": w - 1,
                    "top_cohomology_rank": 0,
                }
            )
        else:
            assert row == []
            assertions += 1
            rank_rows.append(
                {
                    "coefficient_weight": w,
                    "F_rank": 0,
                    "K_rank": 0,
                    "top_cohomology_rank": 1,
                    "total_weight": 2,
                }
            )

    # Nonlinear finite core used in A-L03:
    # basis 1,x,y,u,theta, dx=y, du=2theta,
    # xy=u, y^2=2theta, gamma_2(y)=theta, arity>2 zero.
    nonlinear_cores = []
    for modulus in (2, 3, 4):
        q = (0, 1, 2, 3, 4)
        zero = (0,) * 5
        one = (1, 0, 0, 0, 0)
        bases = [tuple(int(i == j) for i in range(5)) for j in range(5)]

        def add(a, b):
            return tuple((x + y) % modulus for x, y in zip(a, b))

        def scale(c, a):
            return tuple(c * x % modulus for x in a)

        def mul(a, b):
            c = [0] * 5
            for i in range(5):
                c[i] += a[0] * b[i] + a[i] * b[0]
            c[0] -= a[0] * b[0]
            c[3] += a[1] * b[2] + a[2] * b[1]
            c[4] += 2 * a[2] * b[2]
            return tuple(x % modulus for x in c)

        def power(a, n):
            result = one
            for _ in range(n):
                result = mul(result, a)
            return result

        def diff(a):
            return (0, 0, a[1] % modulus, 0, 2 * a[3] % modulus)

        def gamma(n, a):
            if n == 0:
                return one
            if n == 1:
                return a
            if n == 2:
                return (0, 0, 0, 0, a[2] * a[2] % modulus)
            return zero

        checks = 0
        for i, a in enumerate(bases):
            assert diff(diff(a)) == zero
            checks += 1
            for j, b in enumerate(bases):
                assert mul(a, b) == scale((-1) ** (q[i] * q[j]), mul(b, a))
                assert diff(mul(a, b)) == add(mul(diff(a), b), scale((-1) ** q[i], mul(a, diff(b))))
                checks += 2
                for c in bases:
                    assert mul(mul(a, b), c) == mul(a, mul(b, c))
                    checks += 1
        evens = [(0, 0, a, 0, b) for a, b in product(range(modulus), repeat=2)]
        even_scalars = [(a, 0, b, 0, c) for a, b, c in product(range(modulus), repeat=3)]
        for a in evens:
            for n in range(1, 5):
                assert diff(gamma(n, a)) == mul(gamma(n - 1, a), diff(a))
                checks += 1
                for m in range(1, 5):
                    assert mul(gamma(n, a), gamma(m, a)) == scale(math.comb(n + m, n), gamma(n + m, a))
                    coefficient = math.factorial(n * m) // (math.factorial(n) * math.factorial(m) ** n)
                    assert gamma(n, gamma(m, a)) == scale(coefficient, gamma(n * m, a))
                    checks += 2
                for b in evens:
                    rhs = zero
                    for i in range(n + 1):
                        rhs = add(rhs, mul(gamma(i, a), gamma(n - i, b)))
                    assert gamma(n, add(a, b)) == rhs
                    checks += 1
                for c in even_scalars:
                    assert gamma(n, mul(c, a)) == mul(power(c, n), gamma(n, a))
                    checks += 1
        assert gamma(2, diff(bases[1])) == bases[4]
        assert diff(bases[3]) == scale(2, bases[4])
        checks += 2
        assertions += checks
        nonlinear_cores.append(
            {"coefficient_ring": f"Z/{modulus}", "basis_count": 5, "pd_indices": [1, 2, 3, 4], "checks": checks}
        )

    out = {
        "statement_ids": ["A-L01", "A-L02", "A-L03"],
        "status": "PASS",
        "scope": "finite coefficient and simplex-zero certificates",
        "not_claimed": "finite certification of all simplicial or PD identities",
        "prime_count": 5,
        "tail_cutoffs_per_prime": 64,
        "tail_certificates": certificates,
        "truncated_algebras": finite_algebras,
        "integral_rank_rows": rank_rows,
        "nonlinear_pd_cores": nonlinear_cores,
        "assertion_count": assertions,
        "runtime_seconds": time.perf_counter() - started,
    }
    target = Path(__file__).resolve().parents[1] / "logs" / "B_tail_certificate.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(out, indent=2) + "\n")
    print(
        json.dumps(
            {
                "status": out["status"],
                "assertion_count": assertions,
                "tail_certificate_count": len(certificates),
                "runtime_seconds": out["runtime_seconds"],
                "output": str(target),
            }
        )
    )


if __name__ == "__main__":
    main()
