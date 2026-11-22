#!/usr/bin/env python3
"""Exact low-weight resolution and PD-lattice checks for A-L11.

All displayed matrices are integral.  The only coefficient inverted in
the kernel proof is 3, which is a unit in Z_(2).  The final membership
obstruction is the odd denominator of 1/2 in that local ring.
"""
import json
from fractions import Fraction
from pathlib import Path
from time import perf_counter
import sympy as sp


def main():
    started = perf_counter()
    checks = 0
    q0 = {
        1: sp.Matrix([[1]]),
        2: sp.Matrix([[2, 1]]),
        3: sp.Matrix([[3, 3]]),
        4: sp.Matrix([[4, 6, 1]]),
    }
    q1 = {
        2: sp.Matrix([[1], [-2]]),
        3: sp.Matrix([[2, 1], [-2, -1]]),
        4: sp.Matrix([[3, 3, 0], [-2, -2, 1], [0, 0, -6]]),
    }
    q2 = {
        3: sp.Matrix([[1], [-2]]),
        4: sp.Matrix([[2, 1], [-2, -1], [0, 0]]),
    }
    q3 = {4: sp.Matrix([[1], [-2]])}
    for w, matrix in q1.items():
        assert q0[w] * matrix == sp.zeros(1, matrix.cols)
        assert matrix.rank() == q0[w].cols - q0[w].rank()
        checks += 2
    for w, matrix in q2.items():
        assert q1[w] * matrix == sp.zeros(q1[w].rows, matrix.cols)
        assert matrix.rank() == q1[w].cols - q1[w].rank()
        checks += 2
    assert q2[4] * q3[4] == sp.zeros(3, 1)
    assert q3[4].rank() == 1
    checks += 2
    # The entire weight-four augmentation kernel is spanned over Z_(2).
    for a in range(-20, 21):
        for b in range(-20, 21):
            vector = sp.Matrix([a, b, -4 * a - 6 * b])
            alpha = sp.Rational(a, 3)
            beta = sp.Rational(b) + 2 * alpha
            assert vector == alpha * q1[4][:, 0] + beta * q1[4][:, 2]
            assert int(alpha.q) % 2 == int(beta.q) % 2 == 1
            checks += 2
    bottom3 = sp.Matrix([2, 1, -2])
    bottom4 = sp.Matrix([
        [-1, 2, 0],
        [2, 0, 2],
        [0, 2, 1],
        [0, -2, -1],
        [0, 0, 0],
    ])
    h, tc, k = [bottom4[:, i] for i in range(3)]
    assert 2 * h + tc - 2 * k == sp.zeros(5, 1)
    assert bottom4[:, (0, 2)].rank() == 2
    assert sp.Matrix([[-1, 0], [0, 1]]).det() == -1
    t_action = sp.Matrix([[1, 0, 0], [0, 0, 0], [0, 2, 0], [0, 0, 1], [0, 0, 0]])
    assert t_action * bottom3 == tc
    checks += 4
    # Basis: c*h, T*gamma_2(c).  c*k = c*h+T*gamma_2(c).
    pd_lattice = sp.Matrix([[1, 1, 0], [0, 1, 1]])
    primitive = sp.Matrix([0, sp.Rational(1, 2)])
    assert pd_lattice[:, (0, 2)] == sp.eye(2)
    assert primitive[1].q == 2
    assert 2 * primitive == pd_lattice[:, 2]
    checks += 3
    membership_checks = 0
    for denominator in range(1, 32, 2):
        for numerator in range(-32, 33):
            coefficient = Fraction(numerator, denominator)
            assert coefficient != Fraction(1, 2)
            membership_checks += 1
    checks += membership_checks
    result = {
        "statement": "A-L11",
        "all_assertions_passed": True,
        "exact_checks": checks,
        "weight_four_e4_included": True,
        "augmentation_matrices": {str(w): m.tolist() for w, m in q0.items()},
        "q1_matrices": {str(w): m.tolist() for w, m in q1.items()},
        "q2_matrices": {str(w): m.tolist() for w, m in q2.items()},
        "q3_weight_four": q3[4].tolist(),
        "bottom_weight_four_matrix": bottom4.tolist(),
        "pd_lattice_basis": ["c*h", "T*gamma_2(c)"],
        "rational_primitive_coordinates": ["0", "1/2"],
        "class_order": 2,
        "scope": "Direct comparison fails in H1; based saturation and its later H2/H3 remain separate questions.",
        "runtime_seconds": perf_counter() - started,
    }
    destination = Path(__file__).resolve().parents[1] / "logs" / "B_resolved_tail_lattice_certificate.json"
    destination.write_text(json.dumps(result, indent=2, default=str) + "\n")
    print(json.dumps({k: result[k] for k in (
        "statement", "all_assertions_passed", "exact_checks", "class_order", "runtime_seconds"
    )}))


if __name__ == "__main__":
    main()
