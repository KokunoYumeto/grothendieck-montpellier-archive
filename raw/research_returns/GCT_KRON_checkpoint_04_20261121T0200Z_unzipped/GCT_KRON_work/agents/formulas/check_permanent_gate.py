#!/usr/bin/env python3
"""Exact supplementary checks for F-009; the all-size proof is in further_gates.tex."""
import itertools
import json
from pathlib import Path
from time import perf_counter

import sympy as sp


def subset_matrix(entries, padding):
    m = len(entries)
    size = (1 << m) - 1
    full = size
    matrix = sp.zeros(size)
    for mask in range(full):
        row = mask.bit_count()
        for col in range(m):
            if mask & (1 << col):
                continue
            nxt = mask | (1 << col)
            target = 0 if nxt == full else nxt
            edge = entries[row][col]
            if mask == 0:
                edge *= (-1) ** (m - 1)
            matrix[mask, target] += edge
    for vertex in range(1, size):
        matrix[vertex, vertex] += padding
    return matrix


def permanent(entries):
    m = len(entries)
    return sum(sp.prod(entries[i][sigma[i]] for i in range(m))
               for sigma in itertools.permutations(range(m)))


def run():
    started = perf_counter()
    results = []
    padding = sp.Symbol("L")
    for m in (2, 3):
        symbols = sp.symbols(f"x0:{m*m}")
        entries = [list(symbols[i*m:(i+1)*m]) for i in range(m)]
        mat = subset_matrix(entries, padding)
        residual = sp.expand(mat.det(method="domain-ge")
                             - padding ** (mat.rows-m) * permanent(entries))
        assert residual == 0
        results.append({"m": m, "matrix_size": mat.rows,
                        "independent_symbolic_residual": "0"})

    integer_checks = 0
    for m in (4, 5, 6):
        entries = [[((7*i + 11*j + i*j + m) % 13) - 6
                    for j in range(m)] for i in range(m)]
        pval = permanent(entries)
        for value in (0, 1, -2):
            mat = subset_matrix(entries, value)
            assert mat.det(method="domain-ge") == value ** (mat.rows-m) * pval
            integer_checks += 1
        results.append({"m": m, "matrix_size": mat.rows,
                        "exact_integer_evaluations": 3})

    threshold_rows = []
    for m in range(2, 191):
        threshold_rows.append({"m": m, "subset_size": str(2**m-1),
                               "minimum_ip_size": str(3*m**4+1),
                               "minimum_bip_size": str(m**25),
                               "ip_containment_from_grenet": 2**m-1 <= 3*m**4+1,
                               "bip_containment_from_grenet": 2**m-1 <= m**25})
    assert [row["m"] for row in threshold_rows if row["ip_containment_from_grenet"]] == list(range(2, 19))
    assert [row["m"] for row in threshold_rows if row["bip_containment_from_grenet"]] == list(range(2, 190))
    endpoint_checks = {
        "2^18 <= 3*18^4": 2**18 <= 3*18**4,
        "2^189 <= 189^25": 2**189 <= 189**25,
        "2^19-1 > 3*19^4+1": 2**19-1 > 3*19**4+1,
        "2^190-1 > 190^25": 2**190-1 > 190**25,
        "20^4 < 2*19^4": 20**4 < 2*19**4,
        "191^25 < 2*190^25": 191**25 < 2*190**25,
    }
    assert all(endpoint_checks.values())
    certificate = {
        "finding": "F-009",
        "symbolic_cases": 2,
        "integer_evaluations": integer_checks,
        "matrix_results": results,
        "endpoint_checks": endpoint_checks,
        "threshold_rows": threshold_rows,
        "elapsed_seconds": round(perf_counter()-started, 2),
    }
    output = Path(__file__).with_name("permanent_gate_certificate.json")
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({key: certificate[key] for key in
                      ("finding", "symbolic_cases", "integer_evaluations", "endpoint_checks", "elapsed_seconds")}))


if __name__ == "__main__":
    run()
