#!/usr/bin/env python3
"""Finite checks for cycle-audit examples; no claims about Chow groups are tested.

Run from any directory. The JSON output records exact input and scope.
The mathematical proofs, not these bounded checks, establish the infinite claims.
"""
from __future__ import annotations

import json
import platform
import time
from pathlib import Path

import sympy as sp


def main() -> None:
    started = time.perf_counter()
    matrix_checks = []
    for griffiths_rank in range(1, 7):
        mat = sp.eye(2 + griffiths_rank)
        mat[1, 0] = 1
        matrix_checks.append({
            "input_finite_Griffiths_rank": griffiths_rank,
            "matrix": [[int(v) for v in mat.row(i)] for i in range(mat.rows)],
            "determinant": int(mat.det()),
            "nullity": len(mat.nullspace()),
        })
        assert mat.det() == 1 and not mat.nullspace()

    def parity_cone(a: int, b: int) -> bool:
        return a >= abs(b) and (a - b) % 2 == 0

    def full_cone(a: int, b: int) -> bool:
        return a >= abs(b)

    def open_cone(a: int, b: int) -> bool:
        return (a, b) == (0, 0) or a > abs(b)

    radius = 12
    grid = [(a, b) for a in range(-radius, radius + 1)
            for b in range(-radius, radius + 1)]
    bad_generator_equivalence = []
    bad_polar = []
    bad_root_saturation = []
    for a, b in grid:
        via_generators = (a + b >= 0 and a - b >= 0
                          and (a + b) % 2 == 0 and (a - b) % 2 == 0)
        if parity_cone(a, b) != via_generators:
            bad_generator_equivalence.append([a, b])
        # Exact two-generator polar, not a sampled polar.
        if (a + b >= 0 and a - b >= 0) != full_cone(a, b):
            bad_polar.append([a, b])
        for n in range(1, 13):
            if open_cone(n * a, n * b) != open_cone(a, b):
                bad_root_saturation.append([a, b, n])
    assert not bad_generator_equivalence and not bad_polar
    assert not bad_root_saturation
    assert not parity_cone(1, 0) and full_cone(1, 0)
    assert parity_cone(2, 0)
    assert not open_cone(1, 1) and full_cone(1, 1)
    assert all(parity_cone(a, b) == parity_cone(a, -b) for a, b in grid)

    x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3")
    variables = (x0, x1, x2, x3)
    fermat = sum(x**4 for x in variables)
    gradient = [sp.diff(fermat, x) for x in variables]
    # Saturated projective Jacobian check: each coordinate chart has unit ideal.
    chart_checks = []
    for x in variables:
        gb = sp.groebner(gradient + [x - 1], *variables)
        is_unit_ideal = list(gb) == [1]
        chart_checks.append({"chart": f"{x}=1", "groebner_basis": list(map(str, gb)),
                             "unit_ideal": is_unit_ideal})
        assert is_unit_ideal

    elliptic_a, elliptic_b = -1, 0
    elliptic_discriminant = -16 * (4 * elliptic_a**3 + 27 * elliptic_b**2)
    assert elliptic_discriminant == 64
    elliptic_f5_points = [[x, y] for x in range(5) for y in range(5)
                          if (y*y - x*x*x + x) % 5 == 0]
    assert len(elliptic_f5_points) + 1 == 8
    assert elliptic_discriminant % 5 == 4
    isogeny_denominators = [{"dimension": g, "isogeny": "[2]",
                             "kernel_scheme_order": 2**(2 * g),
                             "kernel_scheme_exponent": 2,
                             "minimal_inverse_denominator": 2}
                            for g in range(1, 7)]

    # Formal coefficient checks for the proved geometric induction C.1f.
    # G marks an abstract vector-space summand; no Chow class is computed.
    t, g_marker = sp.symbols("t G")
    ambient = sum(t**j for j in range(5))
    finite_part = sum(t**j for j in range(4))
    griffiths_part = t**2
    induction_checks = []
    for i in range(1, 8):
        if i > 1:
            base = sp.expand(ambient * (1 + t))
            finite_part = sp.expand(base + t * finite_part)
            griffiths_part = sp.expand(t * griffiths_part)
            ambient = sp.expand(base * (1 + t))
        assert sp.degree(ambient, t) == 2 * i + 2
        assert sp.degree(finite_part, t) == 2 * i + 1
        assert griffiths_part == t**(i + 1)
        product_checks = []
        for extension in range(0, 7):
            n = 2 * i + 1 + extension
            p_factor = sum(t**j for j in range(extension + 1))
            total_finite = sp.expand(finite_part * p_factor)
            total_griffiths = sp.expand(griffiths_part * p_factor)
            source_g = int(total_griffiths.coeff(t, i))
            target_g = int(total_griffiths.coeff(t, n - i))
            assert source_g == 0 and target_g == 1
            product_checks.append({
                "n": n, "i": i, "projective_factor_dimension": extension,
                "source_finite_dimension": int(total_finite.coeff(t, i)),
                "target_finite_summand_dimension": int(total_finite.coeff(t, n - i)),
                "source_G_multiplicity": source_g,
                "target_G_multiplicity": target_g,
            })
        induction_checks.append({
            "i": i, "X_dimension": 2 * i + 1,
            "ambient_dimension": 2 * i + 2,
            "ambient_Tate_polynomial": str(ambient),
            "A_alg_formal_polynomial": str(finite_part + g_marker * griffiths_part),
            "sole_Griffiths_codimension": i + 1,
            "product_checks": product_checks,
        })

    # Local polynomial Rees-algebra elimination for two independent parameters.
    # The geometric proof separately uses regularity in each local ring.
    a, b, tau, u, v = sp.symbols("a b tau u v")
    rees_gb = sp.groebner([u-a*tau, v-b*tau], tau, u, v, a, b, order="lex")
    elimination = [q for q in rees_gb if not q.has(tau)]
    assert elimination == [-a*v + b*u]

    j_checks = []
    for i in range(1, 8):
        for extension in range(0, 7):
            n = 2 * i + extension
            j_part = sp.expand(t**(i + 1) * sum(t**j for j in range(extension + 1)))
            assert j_part.coeff(t, i) == 0
            assert j_part.coeff(t, n + 1 - i) == 1
            j_checks.append({"i": i, "n": n, "initial_K3_dimension": 2,
                             "base_dimension": 2 * i,
                             "ambient_dimension": 2 * i + 1,
                             "projective_factor_dimension": extension,
                             "Lefschetz_exponent": n - 2 * i + 1,
                             "source_J2_multiplicity": 0,
                             "target_J2_multiplicity": 1})

    out = {
        "run_identity": "GPT-6 Astra (OpenAI), cycles agent, 2026-11-19",
        "python_version": platform.python_version(),
        "sympy_version": sp.__version__,
        "scope": [
            "Exact finite linear-algebra models of the V x P1 Lefschetz calculation.",
            "Bounded lattice checks of explicitly proved cone formulae.",
            "Exact Jacobian-ideal chart calculation for the Fermat quartic over Q/C.",
            "Exact discriminant calculation for E: y^2=x^3-x.",
            "[2] group-scheme order versus exponent in dimensions 1 through 6.",
            "Formal blow-up/projective-bundle coefficient recurrence for i=1..7 and 49 (n,i) pairs.",
            "Rees-algebra elimination for the universal two-parameter ideal (a,b).",
            "K3-based algebraically-trivial-group shift: 49 pairs with zero source and nonzero target marker.",
            "No computation claims to prove nonzero Griffiths/Chow classes or a general conjecture."
        ],
        "lefschetz_matrix_checks": matrix_checks,
        "cone_checks": {
            "grid_radius": radius,
            "grid_point_count": len(grid),
            "root_multiplier_range": [1, 12],
            "bad_generator_equivalence": bad_generator_equivalence,
            "bad_polar_formula": bad_polar,
            "bad_open_cone_root_saturation": bad_root_saturation,
            "parity_witness": {"point": [1, 0], "in_original": False, "in_bipolar": True,
                               "twice_point_is_j": [2, 0]},
            "closure_witness": {"point": [1, 1], "in_open_cone": False, "in_bipolar": True}
        },
        "fermat_quartic": {"polynomial": str(fermat), "gradient": list(map(str, gradient)),
                            "projective_chart_checks": chart_checks},
        "elliptic_curve": {"equation": "y^2=x^3-x", "a": elliptic_a, "b": elliptic_b,
                            "discriminant": elliptic_discriminant,
                            "scope": "Smooth over characteristic zero; no use as a smooth model in characteristic 2."},
        "elliptic_F5": {"discriminant_mod5": elliptic_discriminant % 5,
                        "affine_points": elliptic_f5_points,
                        "projective_point_count": len(elliptic_f5_points) + 1,
                        "cohomology_claim": "H1 has dimension2 and diagonal acts as identity; this is not inferred from the point enumeration."},
        "isogeny_denominator_checks": isogeny_denominators,
        "iterated_blowup_checks": induction_checks,
        "local_Rees_algebra": {"input_ideal": ["u-a*tau", "v-b*tau"],
                               "elimination_relation": list(map(str, elimination))},
        "J_surjectivity_degree_checks": j_checks,
        "runtime_seconds": time.perf_counter() - started,
        "all_assertions_passed": True,
    }
    output = Path(__file__).resolve().parents[1] / "output" / "check_cycles.json"
    output.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
