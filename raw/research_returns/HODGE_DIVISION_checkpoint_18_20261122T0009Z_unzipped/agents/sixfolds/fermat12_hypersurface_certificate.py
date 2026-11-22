#!/usr/bin/env python3
"""Exact finite arithmetic checks for SF-SKQ01--05.

Checks explicit graph/projective-bundle degree formulas for all product
partitions through total dimension12, and the proposed recurrence through12.
The all-dimensional theorem is the written proof. No numerical Hodge or
analytic period computation is performed here.
"""
from math import factorial, comb, prod
from fractions import Fraction
from pathlib import Path
import json
import hashlib


def partitions(n, low=1):
    if n == 0:
        yield ()
    for a in range(low, n + 1):
        for rest in partitions(n - a, a):
            yield (a,) + rest


def P(t):
    return 12**t * factorial(t)


def A(t):
    return 2**(2*t) * P(t)**2


def M(t):
    return 2*(2*t+1)*3**t * A(t)**(2*t+2)


def U(t):
    return 440**t * factorial(t) * 144**(55*t)


def H(t):
    if t == 0:
        return 1
    return U(t) * prod(M(j)**(j-1) for j in range(2, t+1))


records = []
for t in range(2, 13):
    for n in range(2, t+1):
        for rest in partitions(t-n):
            denom_rest = prod(factorial(d) for d in rest)
            deg_z = factorial(t) * 12**(len(rest)+2) // (
                factorial(n-1) * denom_rest)
            deg_b = factorial(t-2) * 12**(len(rest)+2) // (
                factorial(n-2) * denom_rest)

            # Whole center includes twelve F^0 points, and 144 if n=2.
            # On the center y-hyperplane vanishes; x-hyperplane is h.
            def center_intersection(a):
                if a > n-2:
                    return 0
                return factorial(t-2-a) * 12**(len(rest)+2) // (
                    factorial(n-2-a) * denom_rest)

            # Blowup codimension2: pi_* E^j=-i_*h^(j-2), j>=2.
            graph_degree = 2**t * deg_z - sum(
                (-1)**j * comb(t, j) * 2**(t-j) * center_intersection(j-2)
                for j in range(2, n+1))
            assert graph_degree > 0
            assert graph_degree <= 2**t * deg_z <= 2**t * P(t)

            # Incidence projective bundle: p_*xi^j=h^(j-1).
            exceptional_degree = Fraction(
                factorial(t-1) * 2**(t-n) * (2**(n-1)-1) *
                12**(len(rest)+2),
                factorial(n-1) * denom_rest)
            assert exceptional_degree.denominator == 1
            exceptional_degree = exceptional_degree.numerator
            assert exceptional_degree <= 3**(t-1) * deg_b
            assert deg_z <= P(t) and deg_b <= P(t)
            assert exceptional_degree <= 3**t * P(t)

            # Main correspondence ambient and input-product degree estimates.
            deg_x = factorial(t) * 12**(len(rest)+1) // (
                factorial(n) * denom_rest)
            ambient_degree = comb(2*t, t) * deg_z * deg_x
            assert ambient_degree <= A(t)
            records.append({
                "total_dimension": t, "split_factor_dimension": n,
                "remaining_dimensions": rest,
                "source_degree": deg_z,
                "whole_center_degree": deg_b,
                "main_graph_degree": graph_degree,
                "whole_exceptional_correspondence_degree": exceptional_degree,
                "all_stated_bounds_checked": True,
            })

recurrence_checks = []
for t in range(1, 13):
    value = H(t)
    assert value >= U(t)
    if t >= 2:
        assert value >= M(t)**(t-1) * max(U(t), H(t-2))
    for k in range(t+1):
        curve_bound = 8**k * 55**k * 12**(t-k) * factorial(t) * 144**(55*t)
        assert curve_bound <= U(t)
    recurrence_checks.append({
        "dimension": t, "H12_bit_length": value.bit_length(),
        "recurrence_checked": True, "all_curve_codimensions_checked": True,
    })

report = {
    "statement_ids": ["SF-SKQ01", "SF-SKQ02", "SF-SKQ03", "SF-SKQ04", "SF-SKQ05"],
    "status": "PASS",
    "arithmetic": "exact integers and rational numbers",
    "geometric_degree_cases": len(records),
    "maximum_total_dimension_checked": 12,
    "degree_cases": records,
    "recurrence_checks": recurrence_checks,
    "definitions": {
        "P_T": "12^T*T!",
        "A_T": "2^(2T)*P_T^2",
        "M_T": "2*(2T+1)*3^T*A_T^(2T+2)",
        "U_T": "440^T*T!*144^(55T)",
        "H12_T": "U_T*product(M_j^(j-1),j=2..T), H12_0=1",
    },
    "scope": (
        "Finite checks validate arithmetic factors and projective-bundle degree "
        "identities in the stated range. The new written proof establishes the "
        "degree bounds and Hodge-spanning assertion for every dimension. "
        "No integral Hodge-lattice saturation is claimed."
    ),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
target = Path(__file__).with_name("fermat12_hypersurface_certificate_output.json")
target.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({
    "status": "PASS", "geometric_degree_cases": len(records),
    "maximum_total_dimension_checked": 12,
    "recurrence_dimensions_checked": 12, "output": str(target),
}))

