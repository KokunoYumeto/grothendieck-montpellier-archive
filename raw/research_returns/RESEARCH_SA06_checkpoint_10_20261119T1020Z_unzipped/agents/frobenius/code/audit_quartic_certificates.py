"""Independent exact checks of the cycles agent's selected four sections.

Input data are read only.  We assemble the dual multiplication matrix by
columns, use SymPy's finite-field DomainMatrix rank, and check base loci
with lexicographic (rather than the original grevlex) Groebner bases.
"""
from pathlib import Path
from itertools import product
import json
import time
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import GF

start = time.perf_counter()
own = Path(__file__).resolve().parents[1]
cycles = own.parent / "cycles"
data = json.loads((cycles / "output/test_quartic_obstruction_rank.json").read_text())
assert data["trials"][0]["rank_mod_101"] == 57
c = data["trials"][0]["coefficients_i_j_k"]
source = [e for e in product(range(3), repeat=4) if sum(e) == 4]
target = [e for e in product(range(3), repeat=4) if sum(e) == 3]
position = {e: n for n, e in enumerate(target)}
matrix = sp.zeros(4*len(target), 3*len(source))
for k in range(3):
    for col, b in enumerate(source):
        for j in range(4):
            if b[j] == 0:
                continue
            a = list(b)
            a[j] -= 1
            row = position[tuple(a)]
            for i in range(4):
                matrix[16*i+row, 19*k+col] += c[i][j][k]
rank = DomainMatrix.from_Matrix(matrix).convert_to(GF(101)).rank()
assert rank == 57
minor = int(DomainMatrix.from_Matrix(matrix[:57, :]).convert_to(GF(101)).det()) % 101
assert minor == 47

w = sp.symbols("w0:4")
z = sp.symbols("z0:3")
sections = [sum(c[i][j][k]*w[j]*z[k]
                for j in range(4) for k in range(3)) for i in range(4)]
equations = [sum(x**4 for x in w), sum(x**4 for x in z)] + sections
charts = []
for j, k in product(range(4), range(3)):
    substitution = {w[j]: 1, z[k]: 1}
    variables = [v for v in w+z if v not in substitution]
    basis = sp.groebner([e.subs(substitution) for e in equations],
                        *variables, modulus=101, order="lex")
    unit = len(basis.polys) == 1 and basis.polys[0].as_expr() == 1
    assert unit
    charts.append({"w": j, "z": k, "lex_basis": [str(p.as_expr()) for p in basis.polys]})
result = {
    "matrix_shape": list(matrix.shape),
    "rank_mod_101_independent_DomainMatrix": rank,
    "first_57_rows_minor_mod_101": minor,
    "charts": charts,
    "all_geometric_chart_base_loci_empty": True,
    "runtime_seconds": time.perf_counter()-start,
    "scope": "Exact rank and basepoint-freeness certificates only; cycle deformation and restriction statements require separate proof.",
}
(own / "output/audit_quartic_certificates.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
