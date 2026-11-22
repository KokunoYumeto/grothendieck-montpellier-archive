"""Exact finite checks accompanying the Nagata double construction.

These checks verify only endpoint arithmetic, the idempotent identity,
and finite cyclic Mayer--Vietoris coefficient calculations. They do not
verify the infinite valuation intersection or the normalization argument;
those are established by the cited source and the written proof.
"""
from fractions import Fraction
from pathlib import Path
import json
from time import perf_counter

import sympy as sp


def main():
    started = perf_counter()
    alpha = sp.sqrt(2)
    values = {
        "a_at_alpha": 2 - alpha,
        "a_at_2alpha": 2 - 2 * alpha,
        "b_at_alpha": alpha - sp.Rational(7, 4),
        "b_at_2alpha": 2 * alpha - sp.Rational(7, 4),
    }
    signs = {key: int(sp.sign(value)) for key, value in values.items()}
    assert signs == {
        "a_at_alpha": 1,
        "a_at_2alpha": -1,
        "b_at_alpha": -1,
        "b_at_2alpha": 1,
    }
    # Rational square comparisons independently certify the radicals.
    assert Fraction(1) < Fraction(2) < Fraction(4)
    assert Fraction(2) < Fraction(49, 16)
    assert Fraction(49, 16) < Fraction(8)
    assert sp.simplify(values["a_at_alpha"] + values["b_at_alpha"]) == sp.Rational(1, 4)
    assert sp.simplify(values["a_at_2alpha"] + values["b_at_2alpha"]) == sp.Rational(1, 4)

    a, b = sp.symbols("a b")
    indicator = a / (a + b)
    identity = sp.factor(indicator**2 - indicator)
    assert sp.cancel(identity + a * b / (a + b)**2) == 0
    assert sp.simplify(indicator.subs(b, 0)) == 1
    assert sp.simplify(indicator.subs(a, 0)) == 0

    finite_checks = []
    for n in (2, 3, 4, 5, 7, 8, 11, 16):
        pairs = {(u, v) for u in range(n) for v in range(n)}
        connected_image = {(u - v) % n for u, v in pairs}
        two_part_image = {((u - v) % n, (u - v) % n) for u, v in pairs}
        assert len(connected_image) == n
        assert len(two_part_image) == n
        indicator_order = next(
            k for k in range(1, n + 1) if (k % n, 0) in two_part_image
        )
        assert indicator_order == n
        finite_checks.append({
            "n": n,
            "connected_overlap_cokernel_order": n // len(connected_image),
            "two_clopen_parts_cokernel_order": n * n // len(two_part_image),
            "indicator_class_order": indicator_order,
        })

    result = {
        "status": "PASS",
        "checks_count": 9 + 3 * len(finite_checks),
        "ordered_pairs_enumerated": sum(row["n"] ** 2 for row in finite_checks),
        "elapsed_seconds": perf_counter() - started,
        "scope": "Finite arithmetic and coefficient checks only; infinite ring proof is not a finite computation.",
        "exact_endpoint_values": {k: str(v) for k, v in values.items()},
        "endpoint_signs": signs,
        "product_value": "1/4",
        "idempotent_difference": str(identity),
        "finite_cyclic_checks": finite_checks,
    }
    destination = Path(__file__).resolve().parents[1] / "logs" / "C_Nagata_double_certificate.json"
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
