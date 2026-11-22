"""Certify the selected four bilinear sections have no projective base point."""
from pathlib import Path
from itertools import product
import json
import time
import sympy as sp

start = time.perf_counter()
base = Path(__file__).resolve().parents[1]
data = json.loads((base / "output" / "test_quartic_obstruction_rank.json").read_text())
coeff = data["trials"][0]["coefficients_i_j_k"]
w = sp.symbols("w0:4")
z = sp.symbols("z0:3")
sections = [sum(coeff[i][j][k]*w[j]*z[k] for j in range(4) for k in range(3))
            for i in range(4)]
equations = [sum(x**4 for x in w), sum(x**4 for x in z)] + sections
records = []
for j, k in product(range(4), range(3)):
    chart_start = time.perf_counter()
    sub = {w[j]: 1, z[k]: 1}
    variables = [x for x in w+z if x not in sub]
    ideal = sp.groebner([f.subs(sub) for f in equations], *variables,
                        modulus=101, order="grevlex")
    empty = len(ideal.polys) == 1 and ideal.polys[0].as_expr() == 1
    row = {"chart_w": j, "chart_z": k, "unit_ideal_mod_101": empty,
           "groebner_basis": [str(f.as_expr()) for f in ideal.polys],
           "runtime_seconds": time.perf_counter()-chart_start}
    records.append(row)
    print(json.dumps({key: val for key,val in row.items() if key != "groebner_basis"}), flush=True)
    assert empty, f"This integer tuple has a base point in chart {(j,k)}"
record = {"coefficient_source": "test_quartic_obstruction_rank.json, first trial",
          "prime": 101, "sections": [str(s) for s in sections], "charts": records,
          "basepoint_free_mod_101": all(r["unit_ideal_mod_101"] for r in records),
          "runtime_seconds": time.perf_counter()-start,
          "geometric_inference": "The common-zero scheme is projective over Z. Empty geometric fibre at101 implies empty characteristic-zero fibre, since a nonempty generic fibre would have closed image containing all Spec Z."}
(base / "output" / "check_quartic_sections_basepoints.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps({key:val for key,val in record.items() if key not in ("charts","sections")},indent=2))
