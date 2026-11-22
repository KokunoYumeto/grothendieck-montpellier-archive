#!/usr/bin/env python3
"""Exact dual-number certificate for the formal parameter-division obstruction.

M(Q[epsilon]/epsilon^2) = R direct_sum Nil(R) has Q-basis
(1, epsilon, epsilon_in_second_summand). E is scalar epsilon and L is
the logarithm of the formal shear at parameter epsilon. Every E*U has
zero third row, while L does not, even before imposing R-linearity on U.
"""
import json
import platform
import time
from datetime import datetime, timezone
from pathlib import Path


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def main():
    start = time.perf_counter()
    zero = [[0] * 3 for _ in range(3)]
    scalar_epsilon = [[0, 0, 0], [1, 0, 0], [0, 0, 0]]
    logarithm = [[0, 0, 0], [0, 0, 0], [1, 0, 0]]
    assert multiply(scalar_epsilon, scalar_epsilon) == zero
    assert multiply(logarithm, logarithm) == zero
    assert multiply(scalar_epsilon, logarithm) == multiply(logarithm, scalar_epsilon) == zero
    images = []
    for i in range(3):
        for j in range(3):
            unit = [[int((row, col) == (i, j)) for col in range(3)] for row in range(3)]
            image = multiply(scalar_epsilon, unit)
            assert image[2] == [0, 0, 0]
            images.append(image)
    assert logarithm[2] != [0, 0, 0]
    output = {
        "theorem": "C:functor-separate-obstructions",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "arithmetic": "exact integer matrices",
        "scalar_epsilon_matrix": scalar_epsilon,
        "logarithm_matrix": logarithm,
        "matrix_units_checked": len(images),
        "square_zero_and_R_linearity": True,
        "linear_separating_functional": "third-row first-column entry",
        "functional_on_all_scalar_epsilon_times_matrix_units": [m[2][0] for m in images],
        "functional_on_logarithm": logarithm[2][0],
        "parameter_division_impossible": True,
        "runtime_seconds": time.perf_counter() - start,
    }
    destination = Path(__file__).resolve().parent.parent / "logs" / "C_functor_obstructions.json"
    destination.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
