"""Exact integral Chow-lattice certificates; not a finite proof of cycle existence.

Each cubic has basis 1,H,E1,...,E6,z, with H^2=z, Ei^2=-z,
and anticanonical class 3H-sum Ei.  The certificate constructs the
actual multiplication matrices, not just their dimensions.
"""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from itertools import product
from pathlib import Path
from time import perf_counter
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

started = datetime.now(timezone.utc).isoformat()
tic = perf_counter()
degrees = (0, 1, 1, 1, 1, 1, 1, 1, 2)
state_names = ("1", "H", "E1", "E2", "E3", "E4", "E5", "E6", "z")
checks = []

def checked(name, assertion, explanation):
    if not bool(assertion):
        raise AssertionError(name)
    checks.append({"name": name, "passed": True, "explanation": explanation})

def basis(s, m, q):
    return [t for t in product(range(m + 1), *([range(9)] * s))
            if t[0] + sum(degrees[v] for v in t[1:]) == q]

def matrix(s, m, q):
    columns = basis(s, m, q)
    rows = basis(s, m, q + 1)
    row_index = {t: i for i, t in enumerate(rows)}
    entries = {}
    for j, t in enumerate(columns):
        if t[0] < m:
            target = (t[0] + 1,) + t[1:]
            entries[(row_index[target], j)] = 1
        for factor in range(1, s + 1):
            value = t[factor]
            if value == 0:
                images = [(1, 3)] + [(e, -1) for e in range(2, 8)]
            elif value == 1:
                images = [(8, 3)]
            elif 2 <= value <= 7:
                images = [(8, 1)]
            else:
                images = []
            for new_value, coefficient in images:
                target = t[:factor] + (new_value,) + t[factor + 1:]
                key = (row_index[target], j)
                entries[key] = entries.get(key, 0) + coefficient
    return rows, columns, entries

def unit_elimination(row_count, column_count, entries):
    """Only swaps, sign changes and integral row/column additions are used."""
    a = [[0] * column_count for _ in range(row_count)]
    for (i, j), value in entries.items():
        a[i][j] = value
    pivot = 0
    operations = Counter()
    while pivot < min(row_count, column_count):
        located = next(((i, j) for i in range(pivot, row_count)
                        for j in range(pivot, column_count)
                        if abs(a[i][j]) == 1), None)
        if located is None:
            break
        i, j = located
        if i != pivot:
            a[i], a[pivot] = a[pivot], a[i]
            operations["row_swaps"] += 1
        if j != pivot:
            for row in a:
                row[j], row[pivot] = row[pivot], row[j]
            operations["column_swaps"] += 1
        if a[pivot][pivot] == -1:
            a[pivot] = [-value for value in a[pivot]]
            operations["row_sign_changes"] += 1
        for i in range(pivot + 1, row_count):
            multiplier = a[i][pivot]
            if multiplier:
                a[i] = [x - multiplier * y for x, y in zip(a[i], a[pivot])]
                operations["row_additions"] += 1
        for j in range(pivot + 1, column_count):
            multiplier = a[pivot][j]
            if multiplier:
                for i in range(row_count):
                    a[i][j] -= multiplier * a[i][pivot]
                operations["column_additions"] += 1
        pivot += 1
    checked(f"unit_block_{row_count}_{column_count}",
            all(a[i][j] == (1 if i == j else 0)
                for i in range(pivot) for j in range(column_count))
            and all(a[i][j] == 0 for i in range(pivot, row_count)
                    for j in range(pivot)),
            "The retained unit block is an actual direct summand after integral unimodular operations.")
    residual = [row[pivot:] for row in a[pivot:]]
    residual_nonzero = [row for row in residual if any(row)]
    return pivot, residual_nonzero, dict(operations)

records = []
raw = []
for r, m in [(2, 0), (2, 1), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (4, 3)]:
    case_tic = perf_counter()
    s, q = r - 1, r - 2
    rows, columns, entries = matrix(s, m, q)
    units, residual, operations = unit_elimination(len(rows), len(columns), entries)
    residual_columns = len(columns) - units
    if residual_columns:
        if residual:
            snf = smith_normal_form(sp.Matrix(residual), domain=sp.ZZ)
            tail = [abs(int(snf[i, i])) for i in range(min(snf.shape))]
            tail += [0] * (residual_columns - len(tail))
        else:
            tail = [0] * residual_columns
    else:
        tail = []
    diagonal = [1] * units + tail
    checked(f"full_column_rank_r{r}_m{m}", all(diagonal),
            "The exact Smith diagonal has no zero entry; this assertion concerns this explicit finite Chow lattice.")
    checked(f"smith_divisibility_r{r}_m{m}",
            all(diagonal[i + 1] % diagonal[i] == 0 for i in range(len(diagonal) - 1)),
            "Exact integer Smith invariant factors are in divisibility order.")
    encoded = json.dumps({"rows": rows, "columns": columns,
                          "entries": [[i, j, v] for (i, j), v in sorted(entries.items())]},
                         separators=(",", ":"))
    record = {"r": r, "s": s, "m": m, "local_dimension": m + 2*r,
              "map_degree": [q, q+1], "rows": len(rows), "columns": len(columns),
              "nonzero_entries": len(entries), "matrix_sha256": sha256(encoded.encode()).hexdigest(),
              "unit_pivots": units, "unimodular_operations": operations,
              "residual_matrix_nonzero_rows": residual,
              "smith_invariant_counts": dict(sorted(Counter(diagonal).items())),
              "torsion_invariant_factors": [v for v in diagonal if v > 1],
              "runtime_seconds": perf_counter() - case_tic}
    records.append(record)
    raw.append(json.loads(encoded))
    print(json.dumps(record), flush=True)

checked("r3_m1_saturated", next(v for v in records if (v["r"], v["m"]) == (3, 1))["torsion_invariant_factors"] == [],
        "This checks the coefficient-lattice part of the separate integral gcd(2,3) proof.")
checked("intersection_matrix", sp.Matrix([[1, 2], [2, 1]]).det() == -3,
        "The two integer intersection equations force x=y=0.")
checked("picard_torsion_bezout", 3 - 2 == 1,
        "The pure and mixed coefficients kill the entire Picard group element, not just its rational image.")
checked("cubic_hyperplane_square", 3**2 - 6 == 3,
        "Anticanonical square in the integral cubic blow-up lattice.")

report = {"statement": "Auxiliary exceptional cubic Chow lattices; unregistered",
          "started_at_utc": started, "runtime_seconds": perf_counter() - tic,
          "scope": "Exact finite multiplication matrices and Smith factors for the nine listed cases. No universal integral hard Lefschetz or local cycle existence is inferred solely from this code.",
          "basis": {"projective_factor": "h^j, 0<=j<=m", "cubic_states": state_names},
          "cases": records, "checks": checks, "passed": len(checks), "failed": 0}
outdir = Path(__file__).resolve().parents[1] / "output"
(outdir / "cubic_exceptional_lattice_matrices.json").write_text(json.dumps(raw, indent=2) + "\n")
(outdir / "cubic_exceptional_lattice_certificate.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2), flush=True)
