#!/usr/bin/env python3
"""Exact integral block identities and arithmetic checks for the mixed theorem.

The formal block identity is symbolic, not an extrapolation from samples.
Finite checks supplement the geometry proved in A3_mixed_nonproduct_ranks.tex.
They do not establish existence of polarized surfaces or nodal curves.
"""
from pathlib import Path
from time import perf_counter
import json
import sympy as sp

started = perf_counter()
alpha, beta, epsilon = sp.symbols("alpha beta epsilon", nonzero=True)
J = sp.Matrix([[0, 1], [-1, 0]])
pairing = sp.diag(alpha * J, beta * J)
dual = sp.diag(-epsilon * beta * J, -epsilon * alpha * J)
D = epsilon * alpha * beta
assert pairing.T == -pairing
assert dual.T == -dual
assert pairing * dual == D * sp.eye(4)
assert dual * pairing == D * sp.eye(4)
assert sp.factor(pairing.det()) == alpha**2 * beta**2
assert sp.factor(dual.det()) == epsilon**4 * alpha**2 * beta**2
assert all(pairing[i, i] == dual[i, i] == 0 for i in range(4))

index_rows = []
for a in range(17):
    for b in range(17):
        valuation_D = a + b
        original_lengths = [a, a, b, b]
        dual_lengths = [valuation_D - a] * 2 + [valuation_D - b] * 2
        assert sum(original_lengths) == sum(dual_lengths) == 2 * valuation_D
        assert dual_lengths == [b, b, a, a]
        assert 2**valuation_D % 2**max(a, b) == 0
        assert (a == 0) == (b == valuation_D)
        assert (a == 0) == (dual_lengths[2:] == [0, 0])
        index_rows.append({
            "ordinary_index": a, "local_index": b, "D_valuation": valuation_D,
            "original_elementary_valuations": original_lengths,
            "dual_elementary_valuations": dual_lengths,
        })

norm_rows = []
union_rows = []
for degree in range(1, 65):
    for d in range(1, 33, 2):
        source_degree = degree * d * d
        nodes = 9 * (source_degree - 1)
        genus = 10 + nodes
        full_rank = 9 + nodes
        relative_rank = full_rank - 1
        assert genus == 9 * degree * d * d + 1
        assert relative_rank == 9 * degree * d * d - 1
        assert genus - full_rank == 1
        norm_rows.append([degree, d, source_degree, nodes, genus, relative_rank])
    for d in range(2, 33, 2):
        g1, g2 = 9 * degree + 1, 9 * degree * (d - 1)**2 + 1
        f1, f2 = g1 - 1, g2 - 1
        intersection = 18 * degree * (d - 1)
        genus = g1 + g2 + intersection - 1
        full_rank = f1 + f2 + intersection - 1
        relative_rank = full_rank - 1
        assert genus == 9 * degree * d * d + 1
        assert relative_rank == 9 * degree * d * d - 2
        assert genus - full_rank == 2
        union_rows.append([degree, d, intersection, genus, relative_rank])

out = {
    "status": "PASS",
    "scope": "Symbolic block identities and exact arithmetic supplements; no geometric existence inferred from samples",
    "symbolic_identity": "diag(alpha*J,beta*J)*diag(-epsilon*beta*J,-epsilon*alpha*J)=epsilon*alpha*beta*I4",
    "symbolic_determinants": ["alpha^2 beta^2", "epsilon^4 alpha^2 beta^2"],
    "index_cases": len(index_rows),
    "odd_norm_cases": len(norm_rows),
    "even_union_cases": len(union_rows),
    "index_rows": index_rows,
    "norm_rows": norm_rows,
    "union_rows": union_rows,
    "elapsed_seconds": perf_counter() - started,
}
Path(__file__).with_suffix(".output.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({k: v for k, v in out.items() if not k.endswith("_rows")}, indent=2))
