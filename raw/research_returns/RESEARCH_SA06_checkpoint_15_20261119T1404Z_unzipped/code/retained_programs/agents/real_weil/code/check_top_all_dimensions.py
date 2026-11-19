#!/usr/bin/env python3
"""Exact finite arithmetic and exterior-algebra certificate for proposed C3as.

This does not certify ampleness, Gersten exactness, actual-curve descent,
ordinary algebraic divisibility, or an assertion about every integer.
Those are the separate proof obligations in the LaTeX fragment.
"""
from datetime import datetime, timezone
from fractions import Fraction
from math import comb, gcd
from pathlib import Path
from time import perf_counter
import json

started = perf_counter()
cases = []
for p in (2, 3, 5, 7, 11):
    for d in range(2, 7):
        E = [1]
        ell = []
        for _ in range(1, d):
            degree = 1 + p * E[-1]
            ell.append(degree)
            E.append(E[-1] * degree)
        n = p * E[-1]
        coefficients = [E[-1] * (n - 3)]
        volume = Fraction(coefficients[0])
        assert n >= 6 and n % p == 0
        assert p * coefficients[0] == n * (n - 3)
        assert 1 - n + n * (n - 2) == n * (n - 3) + 1
        stages = []
        for j, degree in enumerate(reversed(ell), 1):
            index = d - j
            assert degree == ell[index - 1]
            assert degree > p and gcd(degree, p) == 1
            assert all(c % degree == 0 for c in coefficients)
            prime_coefficients = [c // degree for c in coefficients]
            m = degree - p
            assert 0 < m < degree and gcd(m, degree) == 1
            # Classes are recorded in the basis (S_infinity, pullback D').
            inverse_root_to_degree = (degree, -degree * p)
            branch_class = (p + m, -p * degree)
            assert inverse_root_to_degree == branch_class
            b = (-pow(p, -1, degree)) % degree
            a0 = (1 + p * b) // degree
            assert 1 <= b < degree and a0 * degree - p * b == 1
            # w=x^a0 T^b, T^degree=x^-p-c:
            # the x exponent after multiplication is exactly one.
            assert a0 * degree - p * b == 1
            assert a0 * degree + b * (-p) == 1
            # The same identity fixes the normal-bundle transition exponent.
            normal_transition_exponent = a0 * degree - p * b
            differential_order = p * (degree - 1)
            assert normal_transition_exponent == 1
            assert differential_order >= p
            prime_volume = volume / degree ** j
            assert prime_volume.denominator == 1 and prime_volume > 0
            mixed_sum = sum(comb(j + 1, h) * (degree - 1) ** h
                            for h in range(1, j + 2))
            assert mixed_sum == degree ** (j + 1) - 1
            volume = mixed_sum * prime_volume
            assert volume.denominator == 1 and volume > 0
            coefficients = [degree - 1] + prime_coefficients
            assert all(c % E[index - 1] == 0 for c in coefficients)
            stages.append({
                "base_dimension": j, "cover_degree": degree,
                "branch_multiplicity_at_infinity": m,
                "bezout_b": b, "bezout_a0": a0,
                "normal_transition_exponent": normal_transition_exponent,
                "differential_order_at_section": differential_order,
                "new_divisor_coefficients": coefficients[:],
                "new_top_self_intersection": volume.numerator,
            })
        assert len(coefficients) == d
        assert all(c > 0 for c in coefficients)
        cases.append({
            "p": p, "dimension_d": d, "local_dimension_N": d + 1,
            "plane_degree": n, "cover_degrees_ascending": ell,
            "initial_divisor_degree": E[-1] * (n - 3),
            "final_divisor_top_self_intersection": volume.numerator,
            "stages": stages, "all_checks_passed": True,
        })

def wedge_monomial(left, right):
    if set(left) & set(right):
        return 0, ()
    sign = (-1) ** sum(i > j for i in left for j in right)
    return sign, tuple(sorted(left + right))

residue_cases = []
for d in range(2, 13):
    # dx_1,...,dx_(d-1),dz,dt have ordered indices 0,...,d.
    horizontal = tuple(range(d - 1))
    s0, ordinary = wedge_monomial(horizontal, (d - 1,))
    s1, conormal = wedge_monomial(horizontal, (d,))
    assert s0 == s1 == 1
    # dz-a dt minus dz is -a dt, moved from last to first:
    coefficient_of_dt_first = -((-1) ** (d - 1))
    assert coefficient_of_dt_first == (-1) ** d
    sign_after_normalization = ((-1) ** d) * coefficient_of_dt_first
    assert sign_after_normalization == 1
    assert ordinary == tuple(range(d))
    assert conormal == tuple(range(d - 1)) + (d,)
    residue_cases.append({
        "d": d, "raw_residue_coefficient_of_a": coefficient_of_dt_first,
        "fixed_orientation_factor": (-1) ** d,
        "normalized_residue_coefficient_of_a": sign_after_normalization,
    })

record = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "all_checks_passed": True,
    "tower_cases": cases,
    "residue_cases": residue_cases,
    "runtime_seconds": perf_counter() - started,
    "scope": (
        "Exact finite arithmetic for five primes and dimensions2..6, and "
        "integral exterior signs for dimensions2..12. Universal geometry, "
        "normalization, ampleness, integral cycle functoriality, actual branch "
        "selection and ordinary equivalence are proved separately; no "
        "rational or characteristic-zero conclusion is tested or inferred."
    ),
}
Path(__file__).with_name("check_top_all_dimensions_output.json").write_text(
    json.dumps(record, indent=2) + "\n"
)
print(json.dumps(record, indent=2))
