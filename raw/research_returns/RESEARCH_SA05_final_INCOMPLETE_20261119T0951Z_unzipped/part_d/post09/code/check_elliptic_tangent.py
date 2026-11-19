"""Exact polynomial certificate for the elliptic Milnor-completion example.

Point count and projective smoothness reuse Part B's retained certificate.
The infinite Tate-module/completion proof is not a finite computation.
"""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from time import perf_counter
import json
from sympy import Poly, symbols

started = perf_counter()
root = Path(__file__).resolve().parents[3]
out = Path(__file__).resolve().parents[1] / "output"
out.mkdir(parents=True, exist_ok=True)
x, y, X = symbols("x y X")
relation = y**2 + y + x**3

def zero(poly):
    return Poly(poly, X, y, x, modulus=2).is_zero

tangent_y = x**2 * X + y**2
substituted = tangent_y**2 + tangent_y + X**3
factor = (X + x)**2 * (X + x**4)
checks = {
    "tangent_passes_through_point_mod_curve":
        zero(y + x**3 + y**2 + relation),
    "tangent_cubic_minus_factor_is_curve_relation_squared":
        zero(substituted + factor + relation**2),
    "third_y_coordinate_minus_y_fourth_is_curve_relation_squared":
        zero(x**6 + y**2 + y**4 + relation**2),
    "frobenius_preserves_curve_mod_squared_relation":
        zero(y**4 + y**2 + x**6 + relation**2),
    "frobenius_squared_preserves_curve_mod_fourth_relation":
        zero(y**8 + y**4 + x**12 + relation**4),
    "doubling_coordinates_preserve_curve_mod_fourth_relation":
        zero((y**4 + 1)**2 + (y**4 + 1) + x**12 + relation**4),
    "negation_of_double_equals_frobenius_squared":
        zero((y**4 + 1) + 1 + y**4),
    "line_y_zero_has_triple_intersection_x_zero":
        zero(relation.subs(y, 0) + x**3),
}
assert all(checks.values())
retained = []
for relative in [
    "part_b/code/characteristic_brauer_counterexample.py",
    "part_b/output/characteristic_brauer_counterexample.txt",
]:
    path = root / relative
    data = path.read_bytes()
    retained.append({"path": relative, "sha256": sha256(data).hexdigest()})
result = {
    "created_utc": datetime.now(timezone.utc).isoformat(),
    "runtime_seconds": perf_counter() - started,
    "coefficient_field": "F_2",
    "curve_relation": "y^2+y+x^3",
    "tangent_line": "Y=x^2*X+y^2",
    "factor_mod_curve": "(X+x)^2*(X+x^4)",
    "double_point": ["x^4", "y^4+1"],
    "arithmetic_frobenius_squared": ["x^4", "y^4"],
    "checks": checks,
    "retained_point_and_smoothness_certificates": retained,
    "scope": "Eight exact symbolic checks; point count and smoothness reuse the listed existing certificate. Infinite completion and nonvanishing are proved in the note, not inferred from this program.",
}
(out / "elliptic_tangent_certificate.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
