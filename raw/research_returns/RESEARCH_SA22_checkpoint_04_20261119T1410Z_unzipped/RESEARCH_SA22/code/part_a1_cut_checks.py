#!/usr/bin/env python3
"""Exact finite arithmetic in the explicit non-toric analytic welding."""
from fractions import Fraction as F
from pathlib import Path
import json
import csv

root = Path(__file__).resolve().parents[1]
epsilon = F(1, 2)
derivative_maximum = -1 + epsilon
derivative_minimum = -1 - epsilon
assert derivative_minimum < derivative_maximum < 0
assert derivative_maximum != derivative_minimum
result = {
    "epsilon": str(epsilon),
    "angular_derivative_at_zero": str(derivative_maximum),
    "angular_derivative_at_pi": str(derivative_minimum),
    "angular_derivative_range": [str(derivative_minimum), str(derivative_maximum)],
    "orientation_reversing_diffeomorphism": True,
    "constant_toric_derivative": False,
    "all_assertions_passed": True,
}
text = json.dumps(result, indent=2) + "\n"
for suffix in ("json", "txt"):
    (root / "code" / ("part_a1_cut_checks_output." + suffix)).write_text(text)
print(text, end="")
with (root / "checks" / "part_a1_cut_results.csv").open("w", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(["id", "statement", "status", "where_proved", "depends_on", "manuscript_pages", "notes"])
    writer.writerow(["A1-nontoric-cut", "Arbitrary analytic cuts do not canonically yield pointed-cap antiisomorphisms", "Refuted", "sections/part_a1_cut_choice.tex", "Analytic collar welding; Schwarz lemma; uniqueness of hyperbolic bordered metric", "67/074-075", "Explicit h(theta)=-theta+(1/2)sin(theta); four-punctured sphere; geodesic interpretation repaired separately"])
