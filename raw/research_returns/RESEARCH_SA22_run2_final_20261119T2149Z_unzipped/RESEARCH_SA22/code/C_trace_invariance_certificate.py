"""Exact F2 centralizer certificate requested for the trace-splitting audit.

Enumerate the16 matrices in End(F2^2), check commutation with the two
specified invertible matrices, and show that every simultaneous centralizer
element is scalar with trace zero. This finite certificate is additional
to, and does not rerun, the preserved35-assertion scope certificate.
"""
from datetime import datetime, timezone
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
from time import perf_counter


def main():
    started_at = datetime.now(timezone.utc).isoformat()
    started = perf_counter()
    checks = 0

    def verify(condition, description):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(description)

    def multiply(a, b):
        return tuple(sum(a[2 * i + k] * b[2 * k + j] for k in range(2)) % 2
                     for i in range(2) for j in range(2))

    determinant = lambda a: (a[0] * a[3] - a[1] * a[2]) % 2
    trace = lambda a: (a[0] + a[3]) % 2
    swap = (0, 1, 1, 0)
    unipotent = (1, 1, 0, 1)
    verify(determinant(swap) == 1, "swap invertible overF2")
    verify(determinant(unipotent) == 1, "unipotent invertible overF2")
    rows = []
    centralizer = []
    for matrix in product(range(2), repeat=4):
        commute_swap = multiply(matrix, swap) == multiply(swap, matrix)
        commute_unipotent = multiply(matrix, unipotent) == multiply(unipotent, matrix)
        scalar = matrix[1] == matrix[2] == 0 and matrix[0] == matrix[3]
        verify((commute_swap and commute_unipotent) == scalar,
               "simultaneous centralizer is precisely scalar")
        if commute_swap and commute_unipotent:
            centralizer.append(matrix)
        rows.append({"matrix": matrix, "commutes_with_swap": commute_swap,
                     "commutes_with_unipotent": commute_unipotent,
                     "is_scalar": scalar, "trace": trace(matrix)})
    verify(len(centralizer) == 2, "exact centralizer size")
    for matrix in centralizer:
        verify(trace(matrix) == 0, "centralizer has trace zero")
    verify(not any(row["trace"] == 1 and row["commutes_with_swap"]
                   and row["commutes_with_unipotent"] for row in rows),
           "no change-of-basis-invariant trace-one lift")

    source = Path(__file__).resolve()
    result = {
        "status": "PASS",
        "execution_mode": "standalone exact finite certificate; one actual run",
        "source_program": "code/" + source.name,
        "source_sha256": sha256(source.read_bytes()).hexdigest(),
        "started_at_utc": started_at,
        "finished_at_utc": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": perf_counter() - started,
        "checks_count": checks,
        "matrix_cases_count": len(rows),
        "scope": "All16 F2 matrices and the two explicitly displayed invertible matrices only; general trace-sequence proof is written separately.",
        "swap_matrix": swap, "unipotent_matrix": unipotent,
        "simultaneous_centralizer": centralizer,
        "matrix_cases": rows,
    }
    output = source.parents[1] / "logs" / "C_trace_invariance_certificate.json"
    if output.exists():
        raise FileExistsError("Preserve the existing certificate; no optional rerun is intended")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in (
        "status", "started_at_utc", "finished_at_utc", "elapsed_seconds",
        "checks_count", "matrix_cases_count", "source_sha256")}, indent=2))


if __name__ == "__main__":
    main()
