#!/usr/bin/env python3
"""Exact arithmetic certificate for the bordered landing obstruction.

This certifies the algebraic contradiction, not the analytic capping
theorem. The latter is proved in sections/part_a1_bordered.tex.
"""
from fractions import Fraction as F
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
half = F(1, 2)
a0 = a1 = ainf = F(1)
b0 = (a0 + a1 - ainf) / (2 * a0)
b1 = (a0 + a1 - ainf) / (2 * a1)
assert (b0, b1) == (half, half)

# For a candidate cusp pant, 2*b0*a0' = a0'+a1'-1/2
# and 2*b1*a1' = a0'+a1'-1/2.  Solve the two linear equations.
matrix = [[2 * b0 - 1, F(-1)], [F(-1), 2 * b1 - 1]]
rhs = [-half, -half]
det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
assert det != 0
ap0 = (rhs[0] * matrix[1][1] - matrix[0][1] * rhs[1]) / det
ap1 = (matrix[0][0] * rhs[1] - rhs[0] * matrix[1][0]) / det
assert (ap0, ap1) == (half, half)
assert (2 * ap0 - 1, 2 * ap1 - 1) == (F(0), F(0))

result = {
    "original_lambda_squared": ["1", "1", "1"],
    "original_a": [str(a0), str(a1), str(ainf)],
    "invariant_cap_jets_b": [str(b0), str(b1)],
    "candidate_cusp_a_infinity": str(half),
    "candidate_linear_system": {
        "matrix": [[str(x) for x in row] for row in matrix],
        "rhs": [str(x) for x in rhs],
        "determinant": str(det),
    },
    "unique_candidate_a": [str(ap0), str(ap1)],
    "candidate_lambda_squared": [str(2 * ap0 - 1), str(2 * ap1 - 1)],
    "contradiction": "Both retained nondegenerate caps would require zero geodesic boundary length.",
    "all_assertions_passed": True,
}
out = ROOT / "code" / "part_a1_bordered_checks_output.json"
out.write_text(json.dumps(result, indent=2) + "\n")
text = json.dumps(result, indent=2) + "\n"
(ROOT / "code" / "part_a1_bordered_checks_output.txt").write_text(text)
print(text, end="")

rows = [
    ["A1-bordered-landing", "The bordered external-only admissibility target is not preserved, already on the equal-length four-holed sphere", "Refuted", "sections/part_a1_bordered.tex Proposition A1-bordered-landing", "A2-schwarzian; cusp Schwarzian 1/(2q^2)", "67/065-066;67/074-076", "Exact two-jet contradiction; code/part_a1_bordered_checks_output.json"],
    ["A1-bordered-shadow-range", "Node tensors plus external shadows give an exact realanalytic model on the joint support-inequality domain", "Proved", "sections/part_a1_bordered.tex Theorem A1-bordered-shadow-range", "A2b-energy;A2b-recession;A2b-image;A4-grafting;A1-retained-discs", "67/074-079", "Paired edge variables occur twice, external leg variables once; fixed cusps and self-nodes included"],
    ["A1-bordered-shape-image", "The exact image with external disc domains retained is the graph of the jointly reconstructed external caps", "Proved", "sections/part_a1_bordered.tex Corollary A1-bordered-shape-image", "A1-bordered-shadow-range;A2b-regularity", "67/075-076", "External-only admissibility must be replaced by joint shape compatibility"],
]
with (ROOT / "checks" / "part_a1_bordered_results.csv").open("w", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(["id", "statement", "status", "where_proved", "depends_on", "manuscript_pages", "notes"])
    writer.writerows(rows)
