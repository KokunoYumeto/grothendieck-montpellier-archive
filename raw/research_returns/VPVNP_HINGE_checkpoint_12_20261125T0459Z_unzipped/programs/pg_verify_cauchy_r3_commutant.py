"""All-field obstruction to one local span{I,SWAP} term per crown matching.

Constructs coefficients directly from boundary epsilon entries, then checks
six retained-party symmetric-quotient identities and six integral unit minors.
Only Python integers and fractions are used. No numerical solver is needed.
"""
from pathlib import Path
from itertools import product, permutations
from fractions import Fraction
import json

ROOT = Path(__file__).resolve().parents[1]
PERMS = list(permutations(range(3)))
COEFFS = [-1, 1, 1, -1, -1, 1]


def slot(i, j):
    return [k for k in range(3) if k != i].index(j)


def epsilon(a, b):
    return 0 if a == b else (1 if a == 0 else -1)


def bit(x, position):
    return (x >> position) & 1


def crown_coefficient(boundary, sigma):
    value = 1
    for i in range(3):
        for ell in range(3):
            if i == ell:
                continue
            j = sigma[ell]
            value *= epsilon(bit(boundary[i], slot(i, ell)),
                             bit(boundary[3+j], slot(j, sigma[i])))
    return value


def target_coefficient(boundary):
    value = 1
    for side in (0, 3):
        for i in range(3):
            for j in range(i+1, 3):
                value *= epsilon(bit(boundary[side+i], slot(i, j)),
                                 bit(boundary[side+j], slot(j, i)))
    return value


BOUNDARIES = list(product(range(4), repeat=6))
SOURCES = [[crown_coefficient(x, sigma) for x in BOUNDARIES]
           for sigma in PERMS]
TARGET = [target_coefficient(x) for x in BOUNDARIES]


def symmetric_quotient_except(vector, retained):
    result = [0] * (4 * 3**5)
    for boundary, coefficient in zip(BOUNDARIES, vector):
        index = 0
        for party in range(6):
            if party == retained:
                index = 4 * index + boundary[party]
            else:
                index = 3 * index + [0, 1, 1, 2][boundary[party]]
        result[index] += coefficient
    return result


def retained_swap(vector, retained):
    dimensions = [4 if j == retained else 3 for j in range(6)]
    result = []
    for flat_index in range(len(vector)):
        remainder = flat_index
        boundary = [0] * 6
        for j in range(5, -1, -1):
            boundary[j] = remainder % dimensions[j]
            remainder //= dimensions[j]
        x = boundary[retained]
        boundary[retained] = (x >> 1) | ((x & 1) << 1)
        index = 0
        for dimension, coordinate in zip(dimensions, boundary):
            index = dimension * index + coordinate
        result.append(vector[index])
    return result


def determinant(matrix):
    matrix = [list(map(Fraction, row)) for row in matrix]
    result = Fraction(1)
    for j in range(len(matrix)):
        pivot = next(k for k in range(j, len(matrix)) if matrix[k][j])
        if pivot != j:
            matrix[j], matrix[pivot] = matrix[pivot], matrix[j]
            result = -result
        value = matrix[j][j]
        result *= value
        for k in range(j+1, len(matrix)):
            multiplier = matrix[k][j] / value
            matrix[k] = [a - multiplier*b
                         for a, b in zip(matrix[k], matrix[j])]
    return result


MINOR_ROWS = [
    [260, 266, 278, 284, 290, 302],
    [98, 104, 116, 122, 128, 140],
    [44, 50, 143, 149, 155, 248],
    [53, 86, 125, 158, 191, 230],
    [65, 89, 137, 161, 185, 233],
    [69, 93, 141, 165, 189, 237],
]
certificates = []
for retained in range(6):
    sources = [symmetric_quotient_except(x, retained) for x in SOURCES]
    target = symmetric_quotient_except(TARGET, retained)
    assert all(sum(c*x[j] for c, x in zip(COEFFS, sources)) == target[j]
               for j in range(len(target)))
    differences = [[a-b for a, b in zip(retained_swap(x, retained), x)]
                   for x in sources]
    rows = MINOR_ROWS[retained]
    matrix = [[x[j] for x in differences] for j in rows]
    det = determinant(matrix)
    assert det == (-1)**retained
    certificates.append({
        'retained_party': retained,
        'quotient_dimensions': [4 if j == retained else 3 for j in range(6)],
        'row_indices': rows, 'matrix': matrix, 'determinant': int(det),
        'checked_quotient_coordinates': len(target),
    })

failure_index = 95
bare_coefficient = sum(c*x[failure_index] for c, x in zip(COEFFS, SOURCES))
assert TARGET[failure_index] == 0 and bare_coefficient == 1
output = {
    'status': 'PASS integral retained-party identities and unit minors',
    'permutations': [list(x) for x in PERMS],
    'forced_coefficients': COEFFS, 'sectors': certificates,
    'bare_sum_failure': {
        'index': failure_index, 'boundary': BOUNDARIES[failure_index],
        'target_coefficient': 0, 'bare_sum_coefficient': 1,
    },
    'scope': 'Every field: no six-term lift with one product of local span{I,SWAP} maps per matching. Multiple terms per class and arbitrary local maps are not excluded.',
}
path = ROOT / 'outputs/pg_cauchy_r3_commutant_quotient.json'
temporary = path.with_suffix('.json.tmp')
temporary.write_text(json.dumps(output, indent=2) + '\n')
temporary.replace(path)
print(json.dumps({k:v for k,v in output.items() if k != 'sectors'}, indent=2))
