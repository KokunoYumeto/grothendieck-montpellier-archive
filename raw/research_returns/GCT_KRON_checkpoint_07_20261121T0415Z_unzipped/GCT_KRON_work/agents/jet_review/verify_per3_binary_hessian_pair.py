"""Independent exact coefficient derivatives for the binary Hessian pair.

This rebuilds the cubic symbolically from its six monomials, differentiates
that expression twice, and evaluates the Hessian determinant directly.
To obtain each derivative of its determinant, use the four-point formula
for a polynomial of degree at most four in one matrix entry:
    p'(0) = (8(p(1)-p(-1))-(p(2)-p(-2)))/12.
Each entry occurs in exactly four positions of the cubic Hessian, so the
degree bound follows directly from the determinant permutation expansion.
No Hessian inverse or Jacobi trace formula is used.
"""
from datetime import datetime, timezone
from itertools import permutations
from pathlib import Path
import hashlib
import json

import sympy as sp


def main():
    source = Path(__file__)
    certificate_path = source.with_name("per3_binary_hessian_pair_certificate.json")
    original = json.loads(certificate_path.read_text())
    best = original["best"]
    left, right = best["left_matrix_flat"], best["right_matrix_flat"]
    x = sp.symbols("x0:9")
    cubic = sum(sp.prod(x[3*i+p[i]] for i in range(3)) for p in permutations(range(3)))
    gradient = [sp.diff(cubic, v) for v in x]
    hessian = sp.hessian(cubic, x)
    coefficient_matrices = [hessian.diff(v) for v in x]
    assert all(sum(int(c != 0) for c in matrix) == 4 for matrix in coefficient_matrices)
    cubic_rows, hessian_rows = [], []
    full_values = []
    for t in range(10):
        point = [a+t*b for a, b in zip(left, right)]
        substitutions = dict(zip(x, point))
        matrix = hessian.subs(substitutions)
        f_gradient = [int(v.subs(substitutions)) for v in gradient]
        if t < 4:
            cubic_rows.append(f_gradient+[t*v for v in f_gradient])
        h_gradient = []
        for coefficient in coefficient_matrices:
            values = {u: int((matrix+u*coefficient).det(method="domain-ge"))
                      for u in [-2, -1, 1, 2]}
            numerator = 8*(values[1]-values[-1])-(values[2]-values[-2])
            assert numerator % 12 == 0
            h_gradient.append(numerator//12)
        hessian_rows.append(h_gradient+[t*v for v in h_gradient])
        full_values.append({"t": t, "F": int(cubic.subs(substitutions)),
                            "H": int(matrix.det(method="domain-ge"))})
        print({"t": t, "columns_verified": 18}, flush=True)
    matrix = cubic_rows+hessian_rows
    prime = original["prime"]
    assert [[v % prime for v in row] for row in matrix] == [
        [v % prime for v in row] for row in best["Jacobian_mod_prime"]]
    columns = best["selected_columns"]
    minor = sp.Matrix([[row[c] for c in columns] for row in matrix])
    determinant = int(minor.det(method="domain-ge"))
    assert determinant != 0
    assert determinant % prime == best["selected_minor_mod_prime"]
    result = {
        "date_utc": datetime.now(timezone.utc).isoformat(),
        "reviewer": "/root/verify_new_jets; GPT-6 Astra Pro; effort not exposed",
        "run": "GCT_KRON_20261120",
        "method": "Symbolic six-term cubic differentiation; direct integer Hessian determinants; exact four-point derivative formula for degree-at-most-four entry dependence; integer selected-minor determinant.",
        "script_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "primary_certificate_sha256": hashlib.sha256(certificate_path.read_bytes()).hexdigest(),
        "all_252_Jacobian_entries_agree_mod_prime": True,
        "Jacobian_integer": matrix, "values_integer": full_values,
        "selected_columns": columns, "selected_minor_integer": determinant,
        "prime": prime, "selected_minor_mod_prime": determinant % prime,
        "status": "PASS",
    }
    target = source.with_name("per3_binary_hessian_pair_independent_certificate.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print({"determinant": determinant, "residue": determinant % prime}, flush=True)
    print(target, flush=True)


if __name__ == "__main__":
    main()
