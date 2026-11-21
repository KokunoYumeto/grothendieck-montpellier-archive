"""Finite mechanism checks for lower labels b_ji=v_i; no all-size claim."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
from structured_residue_tensor import kernel_basis, residue_matrix, quadratic_jacobian, rank_tool


def main():
    prime, rank_minor, results = 1000003, rank_tool(), []
    for m in [3, 4, 5]:
        parameters = list(range(1, m+1))
        edges, _ = kernel_basis(parameters, prime)
        matrices = [residue_matrix(parameters, i, prime) for i in range(m)]
        embedding = []
        for i, j in edges:
            row = [0]*(2*m-1)
            if i < j:
                row[i], row[j] = 1, 2
            else:
                row[m+j] = 1
            embedding.append(row)
        jacobian = quadratic_jacobian(matrices, embedding, prime)
        rank, pivots, residue = rank_minor(jacobian, prime)
        row = {"m": m, "rank": rank, "dimension": len(jacobian),
               "determinant_mod_prime": residue}
        results.append(row)
        print(row, flush=True)
    source = Path(__file__)
    result = {
        "date_utc": datetime.now(timezone.utc).isoformat(),
        "reviewer": "/root/verify_new_jets; GPT-6 Astra Pro; effort not exposed",
        "run": "GCT_KRON_20261120", "prime": prime,
        "script_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "scope": "Exploratory finite checks of a uniform embedding in the proved residue reduction; arbitrary-size nonvanishing remains open.",
        "results": results,
    }
    source.with_name("residue_simplified_embedding_certificate.json").write_text(json.dumps(result, indent=2)+"\n")


if __name__ == "__main__":
    main()
