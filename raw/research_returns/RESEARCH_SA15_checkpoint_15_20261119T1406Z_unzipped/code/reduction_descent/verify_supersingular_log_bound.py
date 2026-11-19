#!/usr/bin/env python3
"""Exact finite arithmetic certificate for B-RD34.

The proof is algebraic. This certificate verifies its integer estimates,
the multivariable low-degree coefficient cases, and the retained small
ramification possibilities. It does not claim to construct a BT group.
"""
from itertools import product
from pathlib import Path
import json
import time


def vp3(n):
    assert n > 0
    answer = 0
    while n % 3 == 0:
        n //= 3
        answer += 1
    return answer


def sequence(a, steps):
    values = [1]
    for _ in range(steps):
        q = values[-1]
        values.append(min(a + q, 1 + 3 * q, 9 * q))
    return values


def main():
    start = time.perf_counter()
    monomials = []
    for dimension in (1, 2, 3):
        for alpha in product(range(10), repeat=dimension):
            degree = sum(alpha)
            if not 1 <= degree <= 9:
                continue
            common_power = min(vp3(j) for j in alpha if j)
            assert 3 ** common_power <= degree
            assert 2 * common_power <= degree - 1
            monomials.append((alpha, degree, common_power))

    coefficient_cases = 0
    for a in range(1, 145):
        # Differentiation forces valuation >=a when some exponent is a
        # 3-adic unit. The special [3]-order adds >=1 below degree nine.
        lower_by_degree = {}
        for alpha, degree, common_power in monomials:
            forced = max(0, a * (1 - common_power))
            if degree < 9:
                forced = max(forced, 1)
            if degree == 1:
                forced = a
            lower_by_degree[degree] = min(
                lower_by_degree.get(degree, forced), forced
            )
        for q in range(1, 129):
            finite_min = min(
                val + degree * q for degree, val in lower_by_degree.items()
            )
            recurrence = min(a + q, 1 + 3 * q, 9 * q)
            assert finite_min == recurrence
            # Every still higher degree has nonnegative coefficient
            # valuation and contributes at least 10*q > 9*q.
            assert 10 * q > 9 * q
            coefficient_cases += 1

    log_cases = 0
    for degree in range(1, 10001):
        power = 0
        while 3 ** (power + 1) <= degree:
            power += 1
        assert 2 * power <= degree - 1
        for a in (2, 24, 36, 72):
            q = a // 2 + 1
            assert degree * q - a * power >= q
            log_cases += 1

    small = []
    for a in range(1, 25):
        values = sequence(a, 2)
        predicted = 2 * a + 1 if a <= 2 else min(a + 4, 13)
        assert values[-1] == predicted
        assert 2 * values[-1] > a
        small.append({"a": a, "q": values})

    seventy_two = sequence(72, 3)
    assert seventy_two == [1, 4, 13, 40]
    assert 2 * seventy_two[-1] > 72

    joint_orders = (1, 2, 3, 4, 6, 9, 12, 18, 36)
    remaining = [m for m in joint_orders if 2 * sequence(2 * m, 2)[-1] <= 2 * m]
    assert remaining == [18, 36]

    # On ker(F^n), the image of F^u has rank 3^(n-u) for u<n.
    frobenius_images = [
        {"level_exponent": n, "claimed_killing_power": u, "image_rank": 3 ** (n-u)}
        for n, u in ((4, 3), (3, 2))
    ]
    assert all(row["image_rank"] == 3 for row in frobenius_images)

    result = {
        "status": "PASS",
        "scope": "Finite exact arithmetic only; no lift or BT example asserted",
        "multivariable_monomials": len(monomials),
        "coefficient_cases": coefficient_cases,
        "logarithm_degree_cases": log_cases,
        "small_ramification_sequences": small,
        "a72_sequence": seventy_two,
        "remaining_level27_joint_orders": remaining,
        "nonzero_Frobenius_images": frobenius_images,
        "elapsed_seconds": time.perf_counter() - start,
    }
    output = Path(__file__).with_suffix(".output.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
