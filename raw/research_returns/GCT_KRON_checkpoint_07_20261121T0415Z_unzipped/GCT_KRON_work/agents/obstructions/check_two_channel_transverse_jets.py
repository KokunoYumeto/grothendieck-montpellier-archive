"""Exact incidence and full-minor checks for O-027's two-channel pencil."""
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations, permutations
from math import comb
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

from test_permanent_transverse_endpoint import compositions, multiply_linear, rank_minor


def labels(n, i, j):
    R = 2*(n-1)
    result = []
    for channel in range(2):
        linear = [0]*R
        linear[2*i+channel] = 1
        if j < n-1:
            linear[2*j+channel] = 2
        result.append(linear)
    return result


def incidence(n):
    N, R = n-1, 2*(n-1)
    exponents = list(compositions(2, R))
    positions = {e: i for i, e in enumerate(exponents)}
    M = [[0]*(comb(n, 2)*2*R) for _ in range(N*len(exponents))]
    column = 0
    for i, j in combinations(range(n), 2):
        for linear in labels(n, i, j):
            for k in range(R):
                for h, coefficient in enumerate(linear):
                    if not coefficient:
                        continue
                    exponent = tuple(int(a == k)+int(a == h) for a in range(R))
                    monomial = positions[exponent]
                    M[i*len(exponents)+monomial][column] += coefficient
                    if j < N:
                        M[j*len(exponents)+monomial][column] -= coefficient
                column += 1
    return M


def matrix_pencil(n):
    r = 2*n
    A = [[[0]*r for _ in range(n)] for _ in range(n)]
    for i in range(n):
        A[i][i][0], A[i][i][1] = -i, 1
    for i, j in combinations(range(n), 2):
        first, second = labels(n, i, j)
        A[i][j] = [0, 0] + first
        A[j][i] = [0, 0] + second
    return A


def full_jacobian(n, determinant=False):
    A = matrix_pencil(n)
    r = 2*n
    target = [e for e in compositions(n, r) if sum(e[2:]) <= 2]
    positions = {e: i for i, e in enumerate(target)}
    J = [[0]*(n*n*r) for _ in target]
    for i in range(n):
        rows = [k for k in range(n) if k != i]
        for j in range(n):
            cols = [k for k in range(n) if k != j]
            cofactor = {}
            for order in permutations(range(n-1)):
                sign = (-1)**(i+j+sum(order[a]>order[b] for a in range(n-1) for b in range(a+1, n-1))) if determinant else 1
                term = {(0,)*r: sign}
                for row, place in zip(rows, order):
                    term = multiply_linear(term, A[row][cols[place]])
                for exponent, coefficient in term.items():
                    cofactor[exponent] = cofactor.get(exponent, 0) + coefficient
            for k in range(r):
                column = (n*i+j)*r+k
                for exponent, coefficient in cofactor.items():
                    shifted = list(exponent)
                    shifted[k] += 1
                    shifted = tuple(shifted)
                    if shifted in positions:
                        J[positions[shifted]][column] = coefficient
    return J


records = []
for n in range(2, 8):
    M = incidence(n)
    rank, _, residue = rank_minor(M, 1000003)
    assert rank == len(M)
    rank2, _, _ = rank_minor(M, 2)
    rank3, _, _ = rank_minor(M, 3)
    N = n-1
    expected2 = 3*comb(N, 2)+4*comb(N, 3)
    expected3 = comb(N, 3)
    assert len(M)-rank2 == expected2
    assert len(M)-rank3 == expected3
    record = {"type": "incidence", "n": n, "rank": rank,
              "defect_mod2": expected2, "defect_mod3": expected3}
    if n <= 5:
        S = smith_normal_form(sp.Matrix(M), domain=sp.ZZ)
        diagonal = [abs(int(S[i, i])) for i in range(S.rows)]
        assert all(x in (1, 2, 6) for x in diagonal)
        assert diagonal.count(2) == 3*comb(N, 2)+3*comb(N, 3)
        assert diagonal.count(6) == comb(N, 3)
        record["Smith_counts"] = {str(x): diagonal.count(x) for x in (1, 2, 6)}
    records.append(record)
    print(json.dumps(record), flush=True)

for n in range(2, 7):
    for determinant in (False, True):
        J = full_jacobian(n, determinant)
        rank, columns, residue = rank_minor(J, 1000003)
        assert rank == len(J) == 2*n**3-3*n**2+3*n
        record = {"type": "full coefficient Jacobian", "n": n,
                  "form": "determinant" if determinant else "permanent",
                  "rank": rank, "source_dimension": n*n*2*n,
                  "selected_columns": columns, "prime": 1000003,
                  "minor_residue": residue}
        records.append(record)
        print(json.dumps({k:v for k,v in record.items() if k != "selected_columns"}), flush=True)

result = {
    "date_utc": datetime.now(timezone.utc).isoformat(),
    "who_model_effort_run": "/root/saturation_obstructions; GPT-6 Astra Pro; effort not exposed; GCT_KRON_20261120",
    "method": "Explicit integer incidence matrices; exact Smith normal forms for n2..5; exact modular ranks and predicted characteristic2/3 defects for n2..7; full signed and unsigned permutation-minor derivatives of the displayed pencil for n2..6.",
    "records": records, "status": "PASS",
}
Path(__file__).with_name("two_channel_transverse_jet_certificate.json").write_text(json.dumps(result, indent=2) + "\n")
