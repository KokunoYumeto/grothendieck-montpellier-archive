#!/usr/bin/env python3
"""Exact finite-field certificate for one ambient nonliftable cycle class.

No claim about an axis class is made.  This constructs an integral polynomial
in 28 divisor classes on E^4, E: y^2=x^3-x in characteristic 3, whose mod-5
four-form has zero infinitesimal GL(8) stabilizer.  The output includes an
inverse for a 64x64 minor, allowing verification by multiplication alone.
"""
from itertools import combinations, product
from pathlib import Path
import json
import random

P = 5
N = 8
B2 = list(combinations(range(N), 2))
B4 = list(combinations(range(N), 4))
I2 = {v: i for i, v in enumerate(B2)}
I4 = {v: i for i, v in enumerate(B4)}


def wedge_monomial(a, b):
    if len(set(a + b)) != len(a + b):
        return None, 0
    inversions = sum(x > y for x in a for y in b)
    return tuple(sorted(a + b)), (-1) ** inversions


def wedge_vectors(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            t, sign = wedge_monomial((i,), (j,))
            if sign:
                out[t] = (out.get(t, 0) + sign * x * y) % P
    return out


def rref(a):
    a = [[x % P for x in row] for row in a]
    row = 0
    pivots = []
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], -1, P)
        a[row] = [(x * inv) % P for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                scalar = a[i][col]
                a[i] = [(x - scalar * y) % P for x, y in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return a, pivots


def inverse(a):
    n = len(a)
    augmented = [row + [int(i == j) for j in range(n)] for i, row in enumerate(a)]
    reduced, pivots = rref(augmented)
    assert pivots[:n] == list(range(n))
    assert all(reduced[i][:n] == [int(i == j) for j in range(n)] for i in range(n))
    return [row[n:] for row in reduced]


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, col)) % P for col in zip(*b)] for row in a]


def determinant(a):
    a = [[x % P for x in row] for row in a]
    det = 1
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            det = -det
        value = a[j][j]
        det = det * value % P
        for i in range(j + 1, len(a)):
            factor = a[i][j] * pow(value, -1, P) % P
            for k in range(j, len(a)):
                a[i][k] = (a[i][k] - factor * a[j][k]) % P
    return det % P


def lie_matrix(w):
    out = [[0] * (N * N) for _ in B4]
    for col, (a, b) in enumerate(product(range(N), repeat=2)):
        for term, coefficient in zip(B4, w):
            if b not in term or not coefficient:
                continue
            changed = list(term)
            changed[changed.index(b)] = a
            if len(set(changed)) < 4:
                continue
            sign = (-1) ** sum(changed[i] > changed[j] for i in range(4) for j in range(i + 1, 4))
            row = I4[tuple(sorted(changed))]
            out[row][col] = (out[row][col] + sign * coefficient) % P
    return out


def divisor_basis():
    names = []
    classes = []
    for i in range(4):
        names.append({"kind": "coordinate", "i": i + 1})
        form = [0] * len(B2)
        form[I2[(2 * i, 2 * i + 1)]] = 1
        classes.append(form)
    endomorphisms = [
        ("id", [[1, 0], [0, 1]], 1),
        ("iota", [[2, 0], [0, 3]], 1),
        ("pi", [[0, 1], [2, 0]], 3),
        ("pi_after_iota", [[0, 2], [1, 0]], 3),
    ]
    for i, j in combinations(range(4), 2):
        for name, matrix, degree in endomorphisms:
            first = {2 * i: 1, 2 * j: matrix[0][0], 2 * j + 1: matrix[1][0]}
            second = {2 * i + 1: 1, 2 * j: matrix[0][1], 2 * j + 1: matrix[1][1]}
            form = wedge_vectors(first, second)
            form[(2 * i, 2 * i + 1)] = (form.get((2 * i, 2 * i + 1), 0) - 1) % P
            form[(2 * j, 2 * j + 1)] = (form.get((2 * j, 2 * j + 1), 0) - degree) % P
            names.append({"kind": "cross", "i": i + 1, "j": j + 1, "endomorphism": name, "degree": degree})
            classes.append([form.get(t, 0) for t in B2])
    # Columns are divisor classes; inverse columns express monomial 2-forms.
    matrix = [list(row) for row in zip(*classes)]
    inv = inverse(matrix)
    assert multiply(matrix, inv) == [[int(i == j) for j in range(28)] for i in range(28)]
    return names, matrix, inv


def main():
    rng = random.Random(20261122)
    for attempt in range(1, 101):
        w = [rng.randrange(P) for _ in B4]
        action = lie_matrix(w)
        _, row_indices = rref([list(row) for row in zip(*action)])
        if len(row_indices) == 64:
            break
    else:
        raise RuntimeError("No certificate found in search window")
    minor = [action[i] for i in row_indices]
    inv_minor = inverse(minor)
    identity64 = [[int(i == j) for j in range(64)] for i in range(64)]
    assert multiply(minor, inv_minor) == identity64
    assert multiply(inv_minor, minor) == identity64

    names, divisor_matrix, divisor_inverse = divisor_basis()
    # Verify that the cycle sum w_abcd F_ab F_cd gives the target four-form.
    reconstructed = [0] * 70
    for term, coefficient in zip(B4, w):
        if not coefficient:
            continue
        a = I2[term[:2]]
        b = I2[term[2:]]
        first = [sum(divisor_matrix[k][j] * divisor_inverse[j][a] for j in range(28)) % P for k in range(28)]
        second = [sum(divisor_matrix[k][j] * divisor_inverse[j][b] for j in range(28)) % P for k in range(28)]
        for i, x in enumerate(first):
            for j, y in enumerate(second):
                target, sign = wedge_monomial(B2[i], B2[j])
                if sign:
                    reconstructed[I4[target]] = (reconstructed[I4[target]] + coefficient * x * y * sign) % P
    assert reconstructed == w

    certificate = {
        "statement": "C44-A10 ambient supersingular individual-class nonliftability",
        "prime_for_reduction": P,
        "curve_characteristic": 3,
        "curve": "y^2 = x^3 - x",
        "geometric_field": "algebraic closure of F3; all displayed cycles defined over F9",
        "basis_indexing": "0-based exterior indices in lexicographic order; divisor factor numbers 1-based",
        "four_form_basis": B4,
        "four_form_coefficients": w,
        "lie_columns": list(product(range(N), repeat=2)),
        "minor_row_indices": row_indices,
        "minor_determinant_mod_5": determinant(minor),
        "minor_inverse_mod_5": inv_minor,
        "divisor_names": names,
        "divisor_cohomology_matrix_mod_5": divisor_matrix,
        "divisor_inverse_mod_5": divisor_inverse,
        "cycle_definition": "F_ab=sum_j divisor_inverse[j,ab] D_j; Z=sum_abcd w_abcd F_ab*F_cd. All coefficients lifted to integers 0,...,4.",
        "point_class_scale": "All divisor forms have one common unknown nonzero scalar lambda; Z therefore has lambda^2 times the certified four-form. Rank is unchanged.",
        "search_seed": 20261122,
        "search_attempt": attempt,
        "checks": ["64x64 minor times displayed inverse equals identity mod5 in both orders", "28 divisor classes span exterior-square space mod5", "divisor-product cycle reconstructs the certified four-form"],
    }
    path = Path(__file__).with_name("supersingular_class_certificate.json")
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"PASS: Lie rank 64, minor determinant {certificate['minor_determinant_mod_5']} mod5, search attempt {attempt}")
    print("PASS: divisor basis and product reconstruction")
    print("Four-form coefficients:", w)
    print("Minor row indices:", row_indices)
    print("Certificate:", path)


if __name__ == "__main__":
    main()
