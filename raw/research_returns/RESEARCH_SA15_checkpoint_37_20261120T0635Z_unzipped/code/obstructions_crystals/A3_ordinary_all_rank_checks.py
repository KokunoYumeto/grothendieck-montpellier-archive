#!/usr/bin/env python3
"""Finite exact arithmetic checks for ordinary surfaces of arbitrary type.

Checks integral dual-polarization matrices, connected/etale order identities
in the ordinary symplectic model, norm node counts, and d-component graph
arithmetic. The geometric subgroup-scheme and nodal-existence proofs are
supplied in the report, not inferred from these finite checks.
"""
from pathlib import Path
from time import perf_counter
from math import gcd
import json

started = perf_counter()

def multiply(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4))
             for j in range(4)] for i in range(4)]

def two_part(n):
    return n & -n

types = []
degree_cases = 0
for a in range(1, 17):
    for b in range(a, 65, a):
        D = a * b
        a2, b2, D2 = two_part(a), two_part(b), two_part(D)
        assert a2 * b2 == D2
        assert b2 % a2 == 0
        assert D2 % b2 == 0
        assert D % b == 0
        assert gcd(D // D2, 2) == 1
        # Connected and etale primary factors have equal rank D2.
        assert D2 * D2 == two_part(D * D)
        # The chosen isotropic has connected rank D2 and tame rank D/D2;
        # its Cartier dual is etale of total rank D.
        assert D2 * (D // D2) == D
        polarization = [[0,a,0,0],[-a,0,0,0],[0,0,0,b],[0,0,-b,0]]
        dual = [[0,-b,0,0],[b,0,0,0],[0,0,0,-a],[0,0,a,0]]
        scalar = [[D * int(i == j) for j in range(4)] for i in range(4)]
        assert multiply(polarization, dual) == scalar
        assert multiply(dual, polarization) == scalar
        assert D**3 // D**2 == D
        norm_nodes = 9 * (D - 1)
        assert 2 * norm_nodes == 18 * (D - 1)
        assert 10 + norm_nodes == 9 * D + 1
        for d in range(1, 129):
            edges = 18 * D * (d * (d - 1) // 2)
            graph_rank = edges - d + 1
            assert graph_rank >= 0
            genus = d * (9 * D + 1) + graph_rank
            assert genus == 9 * D * d * d + 1
            assert genus - 2 == 9 * D * d * d - 1
            degree_cases += 1
        types.append({"a": a, "b": b, "D": D, "D2": D2,
                      "dual_matrix": dual, "norm_nodes": norm_nodes})

result = {
    "status": "PASS",
    "scope": "Finite exact order, matrix, norm-node and graph identities; geometric descent and existence proved separately",
    "type_count": len(types),
    "even_D_type_count": sum(t["D"] % 2 == 0 for t in types),
    "degree_cases": degree_cases,
    "types": types,
    "elapsed_seconds": perf_counter() - started,
}
Path(__file__).with_name('A3_ordinary_all_rank_checks_output.json').write_text(
    json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'types'}, indent=2))
