"""Exact finite algebra used in C-RD10; the noetherian ring proof is in TeX."""
import json
import time
from pathlib import Path
import sympy as s

started = time.perf_counter()
t, X, Y, d, u, r, a, b = s.symbols("t X Y d u r a b")
x, y = t**2 - 1, t * (t**2 - 1)
node = s.expand(y**2 - x**2 * (x + 1))
assert node == 0
disc = s.factor(-16 * (4 * (d**2)**3 + 27 * (d**3)**2))
assert disc == -496 * d**6
generic = s.expand((t**3 * Y)**2 - (t**2 * X)**3
                   - (t**2)**2 * (t**2 * X) - (t**2)**3)
assert s.expand(generic - t**6 * (Y**2 - X**3 - X - 1)) == 0
transform = s.Poly(s.expand(
    (u**3 * Y + u**2 * a * X + b)**2
    - (u**2 * X + r)**3 - d**2 * (u**2 * X + r) - d**3
    - u**6 * (Y**2 - X**3 - X - 1)), X, Y)
coefficients = {str(m): str(c) for m, c in transform.terms()}
assert transform.coeff_monomial(X * Y) == 2 * a * u**5
assert transform.coeff_monomial(Y) == 2 * b * u**3
assert transform.coeff_monomial(X**2).subs({a: 0}) == -3 * r * u**4
residual = s.factor(transform.as_expr().subs({a: 0, b: 0, r: 0}))
assert s.expand(residual - X * (u**6 - d**2 * u**2) - u**6 + d**3) == 0
output = {
    "node_normalization_identity": str(node),
    "normalization_branches": [[1, 0, 0], [-1, 0, 0]],
    "twist_discriminant": str(disc),
    "generic_isomorphism_identity": str(s.factor(generic)),
    "general_weierstrass_change_coefficients": coefficients,
    "after_forced_translation_vanishing": str(residual),
    "forced_scaling": "u^4=d^2 and u^6=d^3 imply u^2=d; d=t^2 implies u=+t or -t",
    "nonregular_scaling_certificate": "Every node-local fraction has equal residues at t=1,-1; t has residues 1,-1",
    "seconds": time.perf_counter() - started,
}
path = Path(__file__).with_suffix(".output.json")
path.write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps(output, indent=2))
