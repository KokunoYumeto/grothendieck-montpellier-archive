"""Exact modular test of the r=2m+2 transverse-order-two endpoint."""
from itertools import permutations
from pathlib import Path
from datetime import datetime, timezone
from random import Random
import json


def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total-first, length-1):
                yield (first,) + rest


def multiply_linear(poly, linear, cap=2):
    out = {}
    for exponent, coefficient in poly.items():
        for index, scalar in enumerate(linear):
            if not scalar or (index >= 2 and sum(exponent[2:]) == cap):
                continue
            updated = list(exponent)
            updated[index] += 1
            updated = tuple(updated)
            out[updated] = out.get(updated, 0) + coefficient*scalar
    return out


def cofactor(A, omitted_row, omitted_col):
    m, r = len(A), len(A[0][0])
    rows = [i for i in range(m) if i != omitted_row]
    cols = [j for j in range(m) if j != omitted_col]
    total = {}
    for perm in permutations(cols):
        term = {(0,)*r: 1}
        for i, j in zip(rows, perm):
            term = multiply_linear(term, A[i][j])
        for exponent, coefficient in term.items():
            total[exponent] = total.get(exponent, 0) + coefficient
    return total


def jacobian(A):
    m, r = len(A), len(A[0][0])
    targets = [e for e in compositions(m, r) if sum(e[2:]) <= 2]
    positions = {e: i for i, e in enumerate(targets)}
    J = [[0]*(m*m*r) for _ in targets]
    for i in range(m):
        for j in range(m):
            cof = cofactor(A, i, j)
            for k in range(r):
                for exponent, coefficient in cof.items():
                    updated = list(exponent)
                    updated[k] += 1
                    updated = tuple(updated)
                    if updated in positions:
                        J[positions[updated]][(m*i+j)*r+k] = coefficient
    return targets, J


def rank_minor(J, prime):
    A = [[x % prime for x in row] for row in J]
    rank, determinant, sign, pivots = 0, 1, 1, []
    for col in range(len(A[0])):
        pivot_row = next((i for i in range(rank, len(A)) if A[i][col]), None)
        if pivot_row is None:
            continue
        if pivot_row != rank:
            A[rank], A[pivot_row] = A[pivot_row], A[rank]
            sign *= -1
        pivot = A[rank][col]
        determinant = determinant*pivot % prime
        inverse = pow(pivot, -1, prime)
        A[rank] = [x*inverse % prime for x in A[rank]]
        for i in range(rank+1, len(A)):
            scalar = A[i][col]
            if scalar:
                A[i] = [(a-scalar*b) % prime for a, b in zip(A[i], A[rank])]
        pivots.append(col)
        rank += 1
        if rank == len(A):
            break
    return rank, pivots, sign*determinant % prime


if __name__ == "__main__":
    m, r, prime = 3, 8, 1000003
    random = Random(20261121)
    trials = []
    for trial in range(5):
        pencil = [[[random.randint(-3, 3) for _ in range(r)] for _ in range(m)] for _ in range(m)]
        targets, J = jacobian(pencil)
        rank, cols, residue = rank_minor(J, prime)
        trials.append({"trial": trial, "rank": rank})
        print(trials[-1], flush=True)
        if rank == len(targets):
            break
    result = {
        "date_utc": datetime.now(timezone.utc).isoformat(),
        "who_model_effort_run": "/root/saturation_obstructions; GPT-6 Astra Pro; effort not exposed; GCT_KRON_20261120",
        "m": m, "r": r, "target_dimension": len(targets),
        "source_dimension": m*m*r, "prime": prime, "trials": trials,
        "pencil_coefficients": pencil, "target_monomials": targets,
        "Jacobian": J, "selected_columns": cols, "selected_minor_mod_prime": residue,
        "status": "FULL RANK" if rank == len(targets) else "RANK DEFICIENT",
    }
    path = Path(__file__).with_name("permanent_transverse_endpoint_certificate.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(str(path), flush=True)
