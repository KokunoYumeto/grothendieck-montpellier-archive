"""Exact dominance certificates for permanent pencils in four variables.

No floating-point arithmetic.  A nonzero maximal Jacobian minor modulo
a prime certifies that the same integer minor is nonzero in characteristic
zero.  The n=4 derivative columns are also checked by exact finite
differences of the independently expanded permanent coefficient map.
"""
from itertools import permutations
from random import Random
from pathlib import Path
import json


def compositions(total, parts=4):
    if parts == 1:
        return [(total,)]
    return [(a,)+tail for a in range(total, -1, -1)
            for tail in compositions(total-a, parts-1)]


def multiply_linear(poly, coefficients):
    out = {}
    for alpha, value in poly.items():
        for k, c in enumerate(coefficients):
            if not c:
                continue
            beta = list(alpha)
            beta[k] += 1
            beta = tuple(beta)
            out[beta] = out.get(beta, 0)+value*c
    return {alpha: value for alpha, value in out.items() if value}


def permanent_coefficients(pencil):
    n = len(pencil)
    out = {}
    for sigma in permutations(range(n)):
        term = {(0, 0, 0, 0): 1}
        for i, j in enumerate(sigma):
            term = multiply_linear(term, pencil[i][j])
        for alpha, value in term.items():
            out[alpha] = out.get(alpha, 0)+value
    return out


def jacobian(pencil):
    n = len(pencil)
    exponents = compositions(n)
    columns = []
    column_parameters = []
    for i in range(n):
        for j in range(n):
            minor = [[pencil[a][b] for b in range(n) if b != j]
                     for a in range(n) if a != i]
            cof = permanent_coefficients(minor)
            for k in range(4):
                column_parameters.append((i, j, k))
                column = []
                for alpha in exponents:
                    beta = list(alpha)
                    beta[k] -= 1
                    column.append(cof.get(tuple(beta), 0) if beta[k] >= 0 else 0)
                columns.append(column)
    rows = [list(row) for row in zip(*columns)]
    return exponents, column_parameters, rows


def pivot_columns_mod(matrix, prime):
    a = [[x % prime for x in row] for row in matrix]
    pivots = []
    i = 0
    for j in range(len(a[0])):
        pivot = next((k for k in range(i, len(a)) if a[k][j]), None)
        if pivot is None:
            continue
        a[i], a[pivot] = a[pivot], a[i]
        inv = pow(a[i][j], -1, prime)
        a[i] = [(x*inv) % prime for x in a[i]]
        for k in range(i+1, len(a)):
            factor = a[k][j]
            if factor:
                a[k] = [(x-factor*y) % prime for x, y in zip(a[k], a[i])]
        pivots.append(j)
        i += 1
        if i == len(a):
            break
    return pivots


def determinant_mod(matrix, prime):
    a = [[x % prime for x in row] for row in matrix]
    result = 1
    for i in range(len(a)):
        k = next((j for j in range(i, len(a)) if a[j][i]), None)
        if k is None:
            return 0
        if i != k:
            a[i], a[k] = a[k], a[i]
            result = -result
        result = (result*a[i][i]) % prime
        inverse = pow(a[i][i], -1, prime)
        for j in range(i+1, len(a)):
            factor = a[j][i]*inverse % prime
            for h in range(i+1, len(a)):
                a[j][h] = (a[j][h]-factor*a[i][h]) % prime
            a[j][i] = 0
    return result % prime


def determinant_bareiss(matrix):
    a = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for i in range(len(a)-1):
        k = next((j for j in range(i, len(a)) if a[j][i]), None)
        if k is None:
            return 0
        if i != k:
            a[i], a[k] = a[k], a[i]
            sign = -sign
        pivot = a[i][i]
        for j in range(i+1, len(a)):
            for h in range(i+1, len(a)):
                numerator = a[j][h]*pivot-a[j][i]*a[i][h]
                assert numerator % previous == 0
                a[j][h] = numerator//previous
            a[j][i] = 0
        previous = pivot
    return sign*a[-1][-1]


def certify(n, seed, prime=101, maximum_attempts=20):
    rng = Random(seed)
    for attempt in range(maximum_attempts):
        pencil = [[[rng.randrange(-2, 3) for k in range(4)]
                   for j in range(n)] for i in range(n)]
        rows, parameters, jac = jacobian(pencil)
        pivots = pivot_columns_mod(jac, prime)
        if len(pivots) == len(rows):
            break
    else:
        raise AssertionError("No full-rank pencil found in deterministic search")
    minor = [[row[j] for j in pivots] for row in jac]
    det_mod = determinant_mod(minor, prime)
    det_integer = determinant_bareiss(minor)
    assert det_integer != 0 and det_integer % prime == det_mod != 0
    coeffs = permanent_coefficients(pencil)
    check_columns = range(len(parameters)) if n == 4 else range(0, len(parameters), 9)
    for column in check_columns:
        i, j, k = parameters[column]
        pencil[i][j][k] += 1
        shifted = permanent_coefficients(pencil)
        pencil[i][j][k] -= 1
        assert all(shifted.get(alpha, 0)-coeffs.get(alpha, 0) == jac[row][column]
                   for row, alpha in enumerate(rows))
    record = {
        "n": n, "variable_count": 4, "seed": seed, "attempt_zero_based": attempt,
        "prime": prime,
        "pencil_coefficients_i_j_k": pencil,
        "variables": ["x1", "x2", "x3", "x4"],
        "row_monomial_exponents": rows,
        "column_parameters_zero_based": parameters,
        "selected_columns_zero_based": pivots,
        "selected_parameters_one_based": [[x+1 for x in parameters[j]] for j in pivots],
        "jacobian_integer": jac,
        "minor_integer": minor,
        "rank_mod_prime": len(pivots),
        "minor_determinant_mod_prime": det_mod,
        "minor_determinant_integer": str(det_integer),
        "permanent_coefficients": [coeffs.get(alpha, 0) for alpha in rows],
        "exact_finite_difference_columns_checked_zero_based": list(check_columns),
        "finite_difference_check_passed": True,
        "arithmetic": "integers; modular elimination; fraction-free Bareiss determinant",
    }
    output = Path(__file__).with_name(f"permanent_{n}_four_variable_certificate.json")
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"n": n, "rank": len(pivots), "prime": prime,
                      "determinant_mod_prime": det_mod,
                      "integer_determinant": str(det_integer),
                      "attempt_zero_based": attempt,
                      "finite_difference_columns_checked": len(list(check_columns)),
                      "output": str(output)}), flush=True)
    return record


if __name__ == "__main__":
    certify(4, 20261121)
    certify(5, 20261122)
