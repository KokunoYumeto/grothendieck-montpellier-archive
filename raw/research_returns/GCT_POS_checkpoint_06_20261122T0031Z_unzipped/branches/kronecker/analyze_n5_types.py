"""Exact support, lattice and infinitesimal data for the 77 modulus-16 types.

No claim about full finite stabilizers is made by this computation.
The last field is a determinant on the normal representation before any
possible residual finite quotient; it is not asserted to be a Hilbert residue.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

root = Path(__file__).resolve().parent
records = json.loads((root / "recursive_n5_m16_result.json").read_text())["feasible"]
z = sp.Symbol("z")
phi = z**8 + 1

def modular_rank(a, prime=1009):
    a = [[int(v) % prime for v in row] for row in a]
    m, n = len(a), len(a[0])
    r = 0
    pivots = []
    row_ids = list(range(m))
    for col in range(n):
        pivot = next((j for j in range(r, m) if a[j][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        row_ids[r], row_ids[pivot] = row_ids[pivot], row_ids[r]
        pivots.append([row_ids[r], col])
        scale = pow(a[r][col], -1, prime)
        a[r] = [(v * scale) % prime for v in a[r]]
        for j in range(r + 1, m):
            v = a[j][col]
            if v:
                a[j] = [(x - v * y) % prime for x, y in zip(a[j], a[r])]
        r += 1
        if r == m:
            break
    return r, pivots

def cyclotomic_product(exponents):
    answer = sp.Integer(1)
    counts = Counter(x % 16 for x in exponents if x % 16)
    for exponent, multiplicity in sorted(counts.items()):
        answer = sp.rem(answer * (1 - z**exponent)**multiplicity, phi, z)
    return answer

for number, record in enumerate(records, 1):
    weights = record["W"]
    if number == 1:
        # The three vectors in the repeated first-factor eigenspace are
        # e_0, e_1, e_0+e_1 in the order of the first three aggregate edges.
        support = []
        for edge_number, edge in enumerate(record["E"]):
            indices = [weights[j].index(edge[j]) for j in range(3)]
            if edge_number == 1:
                indices[0] = 1
            support.append(tuple(indices))
            if edge_number == 2:
                second = indices.copy()
                second[0] = 1
                support.append(tuple(second))
    else:
        support = [tuple(weights[j].index(edge[j]) for j in range(3)) for edge in record["E"]]
    incidence = sp.Matrix([[int(e[a] == i) for e in support] for a in range(3) for i in range(5)])
    smith = smith_normal_form(incidence, domain=sp.ZZ)
    diagonal = [abs(int(smith[j, j])) for j in range(min(smith.shape)) if smith[j, j]]
    support_set = set(support)
    lie = []
    for output_edge in product(range(5), repeat=3):
        row = []
        for a in range(3):
            for i in range(5):
                for j in range(5):
                    source_edge = list(output_edge)
                    source_edge[a] = j
                    row.append(int(output_edge[a] == i and tuple(source_edge) in support_set))
        lie.append(row)
    rank, pivots = modular_rank(lie)
    assert rank == 73
    assert len(diagonal) == 13 and diagonal == [1] * 12 + [16]
    numerator = cyclotomic_product(a - b for factor in weights for a in factor for b in factor)
    denominator = cyclotomic_product(sum(edge) for edge in product(*weights))
    normal = sp.rem(numerator * sp.invert(denominator, phi, z), phi, z)
    record.update({
        "index": number,
        "chosen_support": support,
        "smith_diagonal": diagonal,
        "GL_lie_rank_mod_1009": rank,
        "rank_pivots_mod_1009": pivots,
        "fixed_tensor_dimension": sum(sum(edge) % 16 == 0 for edge in product(*weights)),
        "fixed_GL_lie_dimension": sum(sum(c*c for c in Counter(factor).values()) for factor in weights),
        "normal_determinant_reciprocal_before_finite_quotient": str(normal),
    })
    print(number, "rank", rank, "smith", diagonal[-1], "normal", normal, flush=True)
(root / "n5_type_analysis.json").write_text(json.dumps(records, indent=2))
