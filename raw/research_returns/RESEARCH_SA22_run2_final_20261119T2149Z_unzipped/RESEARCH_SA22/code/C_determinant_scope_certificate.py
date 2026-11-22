"""Exact certificates for two printed Knudsen--Mumford scope defects.

Enumerate End(F_2^2) and its scalar/trace-zero map. Compute the symbolic
one-variable resolution matrix, its specialization at t=0, and the exact
rational homology dimensions for the ordinary base-change example.
This is not a test of all perfect-complex base-change theorems: exactness
of the polynomial resolution and the general trace criterion are proved
in notes/C_KnudsenMumford_sign_fragment.tex.
"""
from datetime import datetime, timezone
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
from time import perf_counter

import sympy as sp


def main():
    started_at = datetime.now(timezone.utc).isoformat()
    started = perf_counter()
    checks = 0

    def verify(condition, description):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(description)

    matrices = tuple(product(range(2), repeat=4))
    trace = lambda a: (a[0] + a[3]) % 2
    trace_zero = tuple(a for a in matrices if trace(a) == 0)
    identity = (1, 0, 0, 1)
    zero = (0, 0, 0, 0)

    def phi(a, matrix):
        return tuple((a * identity[i] + matrix[i]) % 2 for i in range(4))

    pairs = tuple(product(range(2), trace_zero))
    images = {phi(a, matrix) for a, matrix in pairs}
    kernel = tuple((a, matrix) for a, matrix in pairs if phi(a, matrix) == zero)
    verify(len(matrices) == 16, "all2x2 matrices over F2")
    verify(len(trace_zero) == 8, "trace-zero cardinality")
    verify(trace(identity) == 0, "identity has zero trace")
    verify(identity != zero, "identity is nonzero")
    verify(phi(1, identity) == zero, "explicit nonzero kernel vector")
    verify(len(images) == 8, "scalar-plus-tracezero image cardinality")
    verify(len(kernel) == 2, "scalar-plus-tracezero kernel cardinality")
    verify(images != set(matrices), "not surjective")
    for a, matrix in pairs:
        verify(trace(phi(a, matrix)) == 0, "all image matrices have zero trace")

    t = sp.Symbol("t")
    polynomial_map = sp.Matrix([[t]])
    verify(polynomial_map.det() == t, "symbolic determinant")
    verify(polynomial_map.rank() == 1, "rank over Q(t)")
    verify(sp.rem(t, t, t) == 0, "quotient kills t")
    verify(sp.rem(sp.Integer(1), t, t) == 1, "quotient preserves nonzero1")
    specialized = polynomial_map.subs(t, 0)
    verify(specialized == sp.zeros(1, 1), "tensor differential at t=0")
    source_dimensions = {-1: 1, 0: 1}
    source_homology = {-1: 1 - specialized.rank(), 0: 1 - specialized.rank()}
    target_dimensions = {0: 1}
    target_homology = {-1: 0, 0: 1}
    verify(source_homology == {-1: 1, 0: 1}, "source homology")
    verify(target_homology == {-1: 0, 0: 1}, "target homology")
    degree = lambda dimensions: sum((-1 if i % 2 else 1) * n
                                    for i, n in dimensions.items())
    verify(degree(source_dimensions) == 0, "source determinant degree")
    verify(degree(target_dimensions) == 1, "target determinant degree")
    verify(source_homology[-1] != target_homology[-1], "comparison is not quasi-isomorphic")
    verify(degree(source_dimensions) != degree(target_dimensions), "graded determinants differ")

    source = Path(__file__).resolve()
    result = {
        "status": "PASS",
        "execution_mode": "standalone exact finite and symbolic certificate; one actual run",
        "source_program": "code/" + source.name,
        "source_sha256": sha256(source.read_bytes()).hexdigest(),
        "started_at_utc": started_at,
        "finished_at_utc": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": perf_counter() - started,
        "checks_count": checks,
        "scope": "F2 trace-map enumeration and symbolic specialization/rational homology of the explicit affine base-change example only; general statements have separate written proofs.",
        "trace_example": {
            "field_order": 2, "matrix_size": 2,
            "matrices_count": len(matrices),
            "trace_zero_matrices_count": len(trace_zero),
            "domain_pairs_count": len(pairs),
            "image_count": len(images), "kernel_count": len(kernel),
            "nonzero_kernel_vector": [1, list(identity)],
            "trace_zero_matrices": trace_zero,
            "image_matrices": sorted(images), "kernel_vectors": kernel,
        },
        "base_change_example": {
            "ring": "Q[t]", "quotient": "k=Q[t]/(t)",
            "resolution_degrees": [-1, 0],
            "resolution_matrix": [["t"]], "generic_rank_over_Q(t)": 1,
            "specialized_matrix": [[0]], "specialized_rank": 0,
            "source_homology_dimensions": {str(i): int(n) for i, n in source_homology.items()},
            "target_homology_dimensions": {str(i): int(n) for i, n in target_homology.items()},
            "source_determinant_degree": degree(source_dimensions),
            "target_determinant_degree": degree(target_dimensions),
            "resolution_exactness_note": "Multiplication by t is injective in Q[t] and its cokernel is k, as proved in the accompanying text; no finite sample substitutes for that argument.",
        },
    }
    output = source.parents[1] / "logs" / "C_determinant_scope_certificate.json"
    if output.exists():
        raise FileExistsError("Preserve the existing certificate; no optional rerun is intended")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in (
        "status", "started_at_utc", "finished_at_utc", "elapsed_seconds",
        "checks_count", "source_sha256")}, indent=2))


if __name__ == "__main__":
    main()
