"""Test the induced first-order map at the one-charge residue embedding."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from structured_residue_tensor import kernel_basis, residue_matrix, quadratic_jacobian, rank_tool


def kernel_mod(matrix, prime):
    a = [[v % prime for v in row] for row in matrix]
    ncols, rank, pivots = len(a[0]), 0, []
    for col in range(ncols):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][col], -1, prime)
        a[rank] = [v*inverse % prime for v in a[rank]]
        for i in range(rank+1, len(a)):
            c = a[i][col]
            if c:
                a[i] = [(x-c*y) % prime for x, y in zip(a[i], a[rank])]
        pivots.append(col)
        rank += 1
        if rank == len(a):
            break
    free = [j for j in range(ncols) if j not in set(pivots)]
    basis = []
    for j in free:
        vector = [0]*ncols
        vector[j] = 1
        for i, pivot in reversed(list(enumerate(pivots))):
            vector[pivot] = -sum(a[i][k]*vector[k] for k in range(pivot+1, ncols)) % prime
        assert all(sum(x*y for x, y in zip(row, vector)) % prime == 0 for row in matrix)
        basis.append(vector)
    return basis


def main():
    prime, rank_minor, rows = 1000003, rank_tool(), []
    for m in [3, 4, 5]:
        a = list(range(1, m+1))
        edges, _ = kernel_basis(a, prime)
        matrices = [residue_matrix(a, i, prime) for i in range(m)]
        r = 2*m-1
        zero, charge = [], []
        for i, j in edges:
            b, c = [0]*r, [0]*r
            b[i] += 1
            b[j] += 1
            if i < m-1:
                b[m+i] += 1
            if j < m-1:
                b[m+j] -= 1
            c[m-1] = 1 if i < j else -1
            zero.append(b)
            charge.append(c)
        j0 = quadratic_jacobian(matrices, zero, prime)
        j1 = quadratic_jacobian(matrices, charge, prime)
        right = kernel_mod(j0, prime)
        left = kernel_mod(list(map(list, zip(*j0))), prime)
        images = [[sum(x*y for x, y in zip(row, vector)) % prime for row in j1]
                  for vector in right]
        induced = [[sum(x*y for x, y in zip(vector, image)) % prime
                    for image in images] for vector in left]
        rank = rank_minor(induced, prime)[0] if induced else 0
        row = {"m": m, "square_dimension": len(j0),
               "boundary_right_nullity": len(right),
               "boundary_left_nullity": len(left),
               "first_order_induced_matrix": induced,
               "first_order_induced_rank": rank}
        rows.append(row)
        print({k: v for k, v in row.items() if k != "first_order_induced_matrix"}, flush=True)
    source = Path(__file__)
    result = {
        "date_utc": datetime.now(timezone.utc).isoformat(),
        "reviewer": "/root/verify_new_jets; GPT-6 Astra Pro; effort not exposed",
        "run": "GCT_KRON_20261120", "prime": prime,
        "script_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "scope": "Finite tests of a specific induced deformation map; no arbitrary-size conclusion.",
        "results": rows,
    }
    source.with_name("residue_charge_lifting_certificate.json").write_text(json.dumps(result, indent=2)+"\n")


if __name__ == "__main__":
    main()
