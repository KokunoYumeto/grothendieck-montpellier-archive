"""Exact modular Jacobian for the binary pair (per_3, det Hess(per_3))."""
from datetime import datetime, timezone
from itertools import permutations
from pathlib import Path
from random import Random
import hashlib
import json


TRIPLES = [tuple(3*i+p[i] for i in range(3)) for p in permutations(range(3))]


def cubic_jet(point):
    value = 0
    gradient = [0]*9
    hessian = [[0]*9 for _ in range(9)]
    for triple in TRIPLES:
        a, b, c = triple
        value += point[a]*point[b]*point[c]
        for i in range(3):
            gradient[triple[i]] += point[triple[(i+1)%3]]*point[triple[(i+2)%3]]
            for j in range(i+1, 3):
                k = 3-i-j
                hessian[triple[i]][triple[j]] += point[triple[k]]
                hessian[triple[j]][triple[i]] += point[triple[k]]
    return value, gradient, hessian


def determinant_inverse_mod(matrix, prime):
    n = len(matrix)
    rows = [[v % prime for v in row]+[int(i == j) for j in range(n)]
            for i, row in enumerate(matrix)]
    determinant = 1
    for col in range(n):
        pivot_row = next((i for i in range(col, n) if rows[i][col]), None)
        if pivot_row is None:
            return 0, None
        if pivot_row != col:
            rows[col], rows[pivot_row] = rows[pivot_row], rows[col]
            determinant = -determinant
        pivot = rows[col][col]
        determinant = determinant*pivot % prime
        inverse = pow(pivot, -1, prime)
        rows[col] = [v*inverse % prime for v in rows[col]]
        for i in range(n):
            if i != col and rows[i][col]:
                scalar = rows[i][col]
                rows[i] = [(a-scalar*b) % prime for a, b in zip(rows[i], rows[col])]
    return determinant % prime, [row[n:] for row in rows]


def rank_minor(matrix, prime):
    rows = [[v % prime for v in row] for row in matrix]
    rank, determinant, pivots = 0, 1, []
    for col in range(len(rows[0])):
        pivot_row = next((i for i in range(rank, len(rows)) if rows[i][col]), None)
        if pivot_row is None:
            continue
        if pivot_row != rank:
            rows[rank], rows[pivot_row] = rows[pivot_row], rows[rank]
            determinant = -determinant
        pivot = rows[rank][col]
        determinant = determinant*pivot % prime
        inverse = pow(pivot, -1, prime)
        rows[rank] = [v*inverse % prime for v in rows[rank]]
        for i in range(rank+1, len(rows)):
            scalar = rows[i][col]
            if scalar:
                rows[i] = [(a-scalar*b) % prime for a, b in zip(rows[i], rows[rank])]
        pivots.append(col)
        rank += 1
        if rank == len(rows):
            break
    return rank, pivots, determinant % prime


def pair_jacobian_mod(left, right, prime):
    cubic_rows, hessian_rows, evaluations = [], [], []
    for t in range(10):
        point = [a+t*b for a, b in zip(left, right)]
        value, gradient, hessian = cubic_jet(point)
        determinant, inverse = determinant_inverse_mod(hessian, prime)
        if inverse is None:
            return None
        h_gradient = [0]*9
        for triple in TRIPLES:
            for i in range(3):
                a, b = triple[(i+1)%3], triple[(i+2)%3]
                h_gradient[triple[i]] += 2*determinant*inverse[a][b]
        h_gradient = [v % prime for v in h_gradient]
        if t < 4:
            cubic_rows.append(gradient+[t*v for v in gradient])
        hessian_rows.append(h_gradient+[t*v % prime for v in h_gradient])
        evaluations.append({"t": t, "F": value % prime, "H": determinant})
    return cubic_rows+hessian_rows, evaluations


def main():
    prime = 1000003
    random = Random(270526)
    trials, best = [], None
    for trial in range(6):
        left = [random.randint(-4, 4) for _ in range(9)]
        right = [random.randint(-4, 4) for _ in range(9)]
        result = pair_jacobian_mod(left, right, prime)
        if result is None:
            trials.append({"trial": trial, "singular_evaluation": True})
            continue
        matrix, evaluations = result
        rank, columns, residue = rank_minor(matrix, prime)
        trials.append({"trial": trial, "rank": rank})
        print(trials[-1], flush=True)
        if best is None or rank > best["rank"]:
            best = {"left_matrix_flat": left, "right_matrix_flat": right,
                    "rank": rank, "selected_columns": columns,
                    "selected_minor_mod_prime": residue,
                    "Jacobian_mod_prime": matrix, "evaluations": evaluations}
        if rank == 14:
            break
    source = Path(__file__)
    certificate = {
        "date_utc": datetime.now(timezone.utc).isoformat(),
        "reviewer": "/root/verify_new_jets; GPT-6 Astra Pro; effort not exposed",
        "run": "GCT_KRON_20261120", "prime": prime,
        "method": "Differentiate the six permanent monomials; use exact modular Hessian inverse and Jacobi determinant differentiation. Rows are F(1,t), t=0..3, followed by H(1,t), t=0..9. Columns are nine A entries then nine B entries.",
        "script_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "trials": trials, "best": best,
        "status": "FULL RANK" if best and best["rank"] == 14 else "RANK DEFICIENT",
    }
    path = source.with_name("per3_binary_hessian_pair_certificate.json")
    path.write_text(json.dumps(certificate, indent=2)+"\n")
    print(path, flush=True)


if __name__ == "__main__":
    main()
