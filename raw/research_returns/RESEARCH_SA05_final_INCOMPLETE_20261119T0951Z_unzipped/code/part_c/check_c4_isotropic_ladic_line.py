"""A formal Q_5 linear-algebra obstruction, not a geometric degeneration."""
from fractions import Fraction as Q
from pathlib import Path
import json


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


one, imag, zero = (Q(1), Q(0)), (Q(0), Q(1)), (Q(0), Q(0))
v = (one, imag)
norm = add(mul(v[0], v[0]), mul(v[1], v[1]))
assert norm == zero
assert mul(imag, imag) == (Q(-1), Q(0))

# Hensel lifting selects the Q_5 embedding of Q(i) with i == 2 mod 5.
root, modulus = 2, 5
roots = [{"modulus": modulus, "root": root}]
for _ in range(5):
    candidates = [root + k * modulus for k in range(5)
                  if ((root + k * modulus) ** 2 + 1) % (5 * modulus) == 0]
    assert len(candidates) == 1
    root, modulus = candidates[0], 5 * modulus
    assert (root * root + 1) % modulus == 0
    assert (2 * root) % 5 != 0
    roots.append({"modulus": modulus, "root": root})

# F=2I scales the line and scales the negative-definite rational form by 4.
frobenius_line_image = tuple(mul((Q(2), Q(0)), x) for x in v)
assert frobenius_line_image == ((Q(2), Q(0)), (Q(0), Q(2)))
result = {
    "scope": "Formal linear algebra over Q_5; not a geometric counterexample.",
    "rational_form": "-x^2-y^2",
    "isotropic_line_over_Q_i": "span(1,i), i^2=-1",
    "exact_line_Gram_entry": [str(-norm[0]), str(-norm[1])],
    "hensel_roots": roots,
    "derivative_nonzero_mod_5": True,
    "frobenius": "2 I_2",
    "frobenius_preserves_line": True,
    "frobenius_similitude_factor": 4,
    "rational_line_impossible": "A nonzero rational vector has x^2+y^2>0 in R.",
}
Path(__file__).with_name("check_c4_isotropic_ladic_line_output.json").write_text(
    json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
