#!/usr/bin/env python3
"""Independent integer coefficient check of the sign-normalized border table."""
import hashlib
import json
from collections import defaultdict
from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / "inputs/pg_singh_border_sign_normalized.json"
data = json.loads(path.read_text())
q, width = data["q"], data["rank_width"]
coefficient = defaultdict(int)
for first, second, realign in (("U", "V", False), ("G", "H", True)):
    for degree1, row1, inner1, value1 in data["tables"][first]:
        assert 0 <= row1 < q*q and 0 <= inner1 < width and value1 in (-1, 1)
        for degree2, row2, inner2, value2 in data["tables"][second]:
            if inner1 != inner2:
                continue
            if realign:
                x, u = divmod(row1, q)
                y, v = divmod(row2, q)
                row, column = q*x+y, q*u+v
            else:
                row, column = row1, row2
            coefficient[degree1+degree2, row, column] += value1*value2
checked = 0
leading = data["leading_degree"]
for degree in range(leading+1):
    for row in range(q*q):
        x, y = divmod(row, q)
        for column in range(q*q):
            u, v = divmod(column, q)
            expected = int(degree == leading and x == v and y == u)
            assert coefficient[degree, row, column] == expected, (degree, row, column)
            checked += 1
result = {
    "input_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    "integer_coordinates_checked_through_leading_degree": checked,
    "leading_degree": leading,
    "leading_coefficient": 1,
    "nonzero_coefficients_by_degree": {
        str(degree): sum(bool(value) for (d, _, _), value in coefficient.items() if d == degree)
        for degree in range(7)},
    "all_nonzero_integer_coefficients": [
        {"degree": degree, "row": row, "column": column, "coefficient": value}
        for (degree, row, column), value in sorted(coefficient.items()) if value],
    "status": "PASS over the integers, hence the border identity specializes to every field. No Lean execution."
}
(root / "outputs/ex_singh_sign_check.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({key: result[key] for key in (
    "integer_coordinates_checked_through_leading_degree", "leading_degree",
    "leading_coefficient", "nonzero_coefficients_by_degree", "status")}))
