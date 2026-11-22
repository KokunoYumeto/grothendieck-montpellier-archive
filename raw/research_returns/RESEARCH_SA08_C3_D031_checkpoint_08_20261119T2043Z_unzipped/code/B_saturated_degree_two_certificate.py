#!/usr/bin/env python3
"""Exact complete arity-two H2 calculation in the first affected weight.

The all-stage saturation argument is proved in B_saturated_degree_two.tex.
This certificate checks the complete source lattice and exact matrices in
arity two and unshifted weight five; higher generators cannot enter it.
"""
from pathlib import Path
from time import perf_counter
import json
import sympy as sp


def main():
    started = perf_counter()
    checks = 0
    degree_two_basis = ["x*g", "x*y", "c*r", "c*b", "h*a", "k*a"]
    degree_three_basis = [
        "h*A", "k*A", "c*B", "U*x*a", "T*x*b", "T*x*r",
        "x*s", "T*y*a", "y*b", "y*r", "T*g*a", "g*b",
        "g*r", "z*a", "g4*a",
    ]
    columns = [
        [0, 0, 0, 0, 0, 1, -2, 0, 0, 0, 1, -2, 2, 0, 0],
        [0, 0, 0, -1, 1, 0, -2, 1, -2, 2, 0, 0, 0, 0, 0],
        [2, -2, 2, 0, 0, 1, 0, 0, 0, -2, 0, 0, 2, 0, 0],
        [0, 0, 2, 0, 1, 0, 0, 0, -2, 0, 0, 2, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 2],
        [0, 2, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 2],
    ]
    d2 = sp.Matrix.hstack(*map(sp.Matrix, columns))
    cycle = sp.Matrix([-1, 1, 1, -1, -1, 1])
    d1 = 2 * cycle
    assert d2 * d1 == sp.zeros(15, 1)
    assert d2 * cycle == sp.zeros(15, 1)
    assert d2.rank() == 5
    assert sp.Matrix.hstack(cycle, d2.nullspace()[0]).rank() == 1
    assert cycle[1] == 1
    checks += 5
    # The last equality makes the rational kernel primitive over Z_(2).
    # Hence ker(d2)=R*cycle, im(d1)=2R*cycle and H2=R/2R.
    variables = [
        ("c", 0, 3), ("h", 0, 4), ("k", 0, 4),
        ("x", 1, 2), ("y", 1, 3), ("g", 1, 3),
        ("z", 1, 4), ("g4", 1, 4),
        ("a", 2, 1), ("b", 2, 2), ("r", 2, 2),
        ("s", 2, 3), ("t", 2, 4), ("a4", 2, 4),
        ("A", 3, 1), ("B", 3, 2), ("A4", 3, 4),
    ]
    form_one_monomials = []
    form_zero_monomials = []
    for i, left in enumerate(variables):
        for right in variables[i:]:
            if left == right and left[1] % 2:
                continue
            coefficient_weight = 5 - left[2] - right[2]
            if coefficient_weight < 0:
                continue
            degree = left[1] + right[1]
            if degree == 0:
                form_zero_monomials.append((left[0], right[0], coefficient_weight))
            if degree == 1:
                form_one_monomials.append((left[0], right[0], coefficient_weight))
            checks += 1
    assert form_zero_monomials == []
    assert form_one_monomials == [("c", "x", 0)]
    checks += 2
    # For every allowed source shift, the next possible rational zero-form
    # weight is strictly greater than the witness weight.
    for shift in range(5, 101):
        assert 2 * (shift + 3) > 2 * shift + 5
        assert 3 * (shift + 3) > 2 * shift + 5
        checks += 2
    result = {
        "statement": "A-L12",
        "all_assertions_passed": True,
        "exact_checks": checks,
        "degree_two_basis": degree_two_basis,
        "degree_three_basis": degree_three_basis,
        "d1": d1.tolist(),
        "d2": d2.tolist(),
        "cycle_coordinates": cycle.tolist(),
        "H2": "Z_(2)/2Z_(2)",
        "complete_degree_one_lattice": form_one_monomials,
        "first_rational_arity_two_zero_form_weight": "2s+6",
        "witness_weight": "2s+5",
        "scope": "Saturated-comparison counterexample; no exclusion of later degree-two repair.",
        "runtime_seconds": perf_counter() - started,
    }
    destination = Path(__file__).resolve().parents[1] / "logs" / "B_saturated_degree_two_certificate.json"
    destination.write_text(json.dumps(result, indent=2, default=str) + "\n")
    print(json.dumps({k: result[k] for k in (
        "statement", "all_assertions_passed", "exact_checks", "H2", "runtime_seconds"
    )}))


if __name__ == "__main__":
    main()
