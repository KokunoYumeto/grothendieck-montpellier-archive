"""Exact small-input certificates for C025 and C026.

Checks arithmetic trace coordinates, AS fiber multiplicities, and the exact
point-count identities. It does not verify sheaf cohomology or general
smoothness, geometric integrality, or complexity-class conclusions.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
import json
import random

from finite_checks_smooth import Field


def solve_binary(rows, right, n):
    work = [rows[i] | (((right >> i) & 1) << n) for i in range(n)]
    for j in range(n):
        i = next(i for i in range(j, n) if (work[i] >> j) & 1)
        work[i], work[j] = work[j], work[i]
        for i in range(n):
            if i != j and ((work[i] >> j) & 1):
                work[i] ^= work[j]
    return sum(((work[i] >> n) & 1) << i for i in range(n))


def satisfies(clauses, assignment):
    return all(any(bool(assignment[abs(literal)-1]) == (literal > 0)
                   for literal in clause) for clause in clauses)


def polynomial_indicator(clauses, coordinates, n):
    sat = 1
    for clause in clauses:
        violation = 1
        for literal in clause:
            x = coordinates[abs(literal)-1]
            violation *= (1 ^ x) if literal > 0 else x
        sat *= 1 ^ violation
    for x in coordinates[n:]:
        sat *= 1 ^ x
    return 1 ^ sat


def make_cases():
    cases = []
    clauses = [(1,), (-1,), (2,), (-2,), (1,2), (1,-2), (-1,2), (-1,-2)]
    for mask in range(1 << len(clauses)):
        cases.append((2, [clause for j, clause in enumerate(clauses) if mask >> j & 1]))
    for n in range(1,6):
        cases.extend([(n, []), (n, [()]), (n, [(1,)]), (n, [(1,-1)])])
    randomizer = random.Random(20261121)
    for n in range(1,6):
        for _ in range(8):
            cs = []
            for _ in range(randomizer.randrange(1,7)):
                scope = randomizer.sample(range(1,n+1), min(n, randomizer.randrange(1,4)))
                cs.append(tuple(i if randomizer.randrange(2) else -i for i in scope))
            cases.append((n, cs))
    return cases


def run():
    fields = {}
    field = Field(1)
    while field.degree <= 8:
        field.mul = lru_cache(maxsize=None)(field.mul)
        fields[field.degree] = field
        if field.degree == 8:
            break
        field = field.extend()

    data = {}
    coordinate_tests = 0
    for b, field in fields.items():
        rows = [sum(field.trace(field.mul(1 << i, 1 << j)) << j
                    for j in range(b)) for i in range(b)]
        dual = [solve_binary(rows, 1 << i, b) for i in range(b)]
        for i, beta in enumerate(dual):
            assert all(field.trace(field.mul(beta, 1 << j)) == int(i == j)
                       for j in range(b))
        coordinates = []
        for x in range(field.size):
            cs = tuple(field.trace(field.mul(beta, x)) for beta in dual)
            assert cs == tuple((x >> i) & 1 for i in range(b))
            coordinate_tests += b
            coordinates.append(cs)
        lam = next(1 << i for i in range(b) if field.trace(1 << i))
        fibers = [0] * field.size
        for y in range(field.size):
            fibers[field.mul(y,y) ^ y] += 1
        assert all(fibers[a] == (2 if field.trace(a) == 0 else 0)
                   for a in range(field.size))
        data[b] = field, coordinates, lam, fibers

    affine_cases = curve_cases = field_points = 0
    max_degree = 0
    for n, clauses in make_cases():
        truth = sum(satisfies(clauses, a) for a in product((0,1), repeat=n))
        # C025 uses the same n input coordinates, with no Boolean equations.
        count = 0
        d_affine = 6 * len(clauses) + 3
        for a in product((0,1), repeat=n):
            p = polynomial_indicator(clauses, a, n)
            f = p ^ (a[0] ** d_affine) ^ a[0]
            count += sum((t*t ^ t ^ f) == 0 for t in (0,1))
        assert count == 2 * truth
        affine_cases += 1

        b = 1
        while b < n:
            b *= 2
        field, coords, lam, fibers = data[b]
        d = (3 * len(clauses) + b + 1) * field.size + 1
        assert d & 1
        assert d > (3 * len(clauses) + b) * field.size // 2
        max_degree = max(max_degree, d)
        count = 1  # unique smooth rational point at infinity, proved in text
        accepted = 0
        for x in range(field.size):
            p = polynomial_indicator(clauses, coords[x], n)
            vanishing = field.power(x, field.size) ^ x
            f = field.mul(lam,p) ^ field.mul(vanishing, field.power(x,d-field.size))
            assert field.trace(f) == p
            count += fibers[f]
            accepted += p == 0
            field_points += 1
        assert accepted == truth
        assert count == 1 + 2 * truth
        assert ((count - 1) // 2) % 2 == truth % 2
        curve_cases += 1

    out = {'findings': ['NN-C025','NN-C026'], 'status': 'all assertions passed',
           'affine_formula_cases': affine_cases, 'curve_formula_cases': curve_cases,
           'trace_coordinate_tests': coordinate_tests, 'curve_field_points': field_points,
           'field_degrees': sorted(data), 'largest_binary_encoded_curve_degree': max_degree,
           'limits': 'Arithmetic and point-count checks only. The infinity point, smoothness, geometric integrality, Cech cohomology, zeta formula and complexity implications are proved in text, not certified by this program.'}
    Path(__file__).with_name('FINITE_CHECK_ARTIN_SCHREIER_RESULTS.json').write_text(
        json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    run()
