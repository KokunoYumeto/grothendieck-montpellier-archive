#!/usr/bin/env python3
"""Independent exact cross-ratio check of the parent's plumbing example.

This uses an explicit global coordinate on every plumbed fibre, independent
of the Kodaira--Spencer/Serre-duality residue calculation.
"""
import json
import platform
import time
from datetime import datetime, timezone
from pathlib import Path
import sympy as sp


def main():
    start = time.perf_counter()
    t = sp.symbols("t")
    R, A, B, C = sp.Rational(3, 2), sp.Rational(420, 569), sp.Rational(3, 4), sp.Integer(10)
    epsilon = sp.Rational(1, 100)
    t0 = (1 - epsilon) / (1 + epsilon)
    phi = lambda z: (z - R) ** 2
    scale = t / t0
    moving_a, moving_b, fixed_c = phi(scale * A), phi(scale * B), phi(C)
    crossratio = sp.factor((moving_a - fixed_c) / (moving_b - fixed_c))
    derivative = sp.factor(sp.diff(crossratio, t))
    second = sp.factor(sp.diff(crossratio, t, 2))
    derivative_at_zero = sp.simplify(derivative.subs(t, 0))
    derivative_at_t0 = sp.simplify(derivative.subs(t, t0))
    second_at_t0 = sp.simplify(second.subs(t, t0))
    roots = {
        "crossratio_zero": sp.solve(sp.together(crossratio).as_numer_denom()[0], t),
        "crossratio_pole": sp.solve(sp.together(crossratio).as_numer_denom()[1], t),
        "crossratio_one": sp.solve(sp.together(crossratio - 1).as_numer_denom()[0], t),
        "critical_parameters": sp.solve(sp.together(derivative).as_numer_denom()[0], t),
    }
    checks = {
        "normalization_parameter": t0 == sp.Rational(99, 101),
        "annular_scale_radius": (1 - epsilon) / t0 == 1 + epsilon,
        "phi_injective_on_enlarged_disc": 1 + epsilon < R,
        "retained_first_marks": 0 < A < 1 - epsilon and 0 < B < 1 - epsilon and A != B,
        "fixed_external_mark_outside": abs(C) > 1 + epsilon and abs(2 * R - C) > 1 + epsilon,
        "critical_at_t0": derivative_at_t0 == 0,
        "simple_critical_point": second_at_t0 != 0,
        "unramified_at_nodal_parameter": derivative_at_zero != 0,
        "zero_values_outside_closed_unit_disc": all(abs(z) > 1 for z in roots["crossratio_zero"]),
        "poles_outside_closed_unit_disc": all(abs(z) > 1 for z in roots["crossratio_pole"]),
        "one_values_only_at_zero_in_unit_disc": all(z == 0 or abs(z) > 1 for z in roots["crossratio_one"]),
    }
    assert all(checks.values()), checks
    output = {
        "statement": "A:hinich-explicit, independent cross-ratio verification",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "arithmetic": "exact rational functions",
        "t0": str(t0),
        "moving_a": str(sp.factor(moving_a)),
        "moving_b": str(sp.factor(moving_b)),
        "fixed_c": str(fixed_c),
        "crossratio": str(crossratio),
        "derivative": str(derivative),
        "crossratio_at_t0": str(sp.factor(crossratio.subs(t, t0))),
        "derivative_at_zero": str(derivative_at_zero),
        "derivative_at_t0": str(derivative_at_t0),
        "second_derivative_at_t0": str(second_at_t0),
        "roots": {key: list(map(str, value)) for key, value in roots.items()},
        "checks": {key: bool(value) for key, value in checks.items()},
        "check_count": len(checks),
        "runtime_seconds": time.perf_counter() - start,
    }
    destination = Path(__file__).resolve().parent.parent / "logs" / "C_plumbing_crossratio.json"
    destination.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
