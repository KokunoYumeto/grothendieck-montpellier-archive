#!/usr/bin/env python3
"""Exact finite witness for SF-E850; no theorem inferred from a search.

The integer multiplication algebra has Hilbert function (1,4,3). A modular
rank witness for the commutator-Koszul differential gives the characteristic
zero upper bound a<=25. The written proof gives the matching25 independent
Hom(I,A) directions. This program uses no author's/peer's imported checker.
"""
from datetime import datetime, timezone
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
from time import perf_counter
import json

HERE = Path(__file__).resolve().parent
P = 101


def mm(a, b):
    out = [[0] * len(b[0]) for _ in a]
    for i, row in enumerate(a):
        for k, c in enumerate(row):
            if c:
                for j, d in enumerate(b[k]):
                    out[i][j] += c * d
    return out


def rank_witness(matrix, p=P):
    a = [[v % p for v in row] for row in matrix]
    n, m = len(a), len(a[0])
    labels = list(range(n))
    used_rows, used_cols, pivots = [], [], []
    rank = 0
    for col in range(m):
        k = next((i for i in range(rank, n) if a[i][col]), None)
        if k is None:
            continue
        a[rank], a[k] = a[k], a[rank]
        labels[rank], labels[k] = labels[k], labels[rank]
        pivot = a[rank][col]
        used_rows.append(labels[rank])
        used_cols.append(col)
        pivots.append(pivot)
        inv = pow(pivot, -1, p)
        a[rank] = [(v * inv) % p for v in a[rank]]
        row = a[rank]
        for i in range(rank + 1, n):
            c = a[i][col]
            if c:
                a[i] = [(u - c * v) % p for u, v in zip(a[i], row)]
        rank += 1
        if rank == n:
            break
    determinant = 1
    for d in pivots:
        determinant = determinant * d % p
    return {'rank': rank, 'rows': used_rows, 'columns': used_cols,
            'ordered_minor_determinant_mod101': determinant}


def det_mod(matrix, p=P):
    a = [[v % p for v in row] for row in matrix]
    n = len(a)
    ans = 1
    for j in range(n):
        k = next((i for i in range(j, n) if a[i][j]), None)
        if k is None:
            return 0
        if k != j:
            a[j], a[k] = a[k], a[j]
            ans = -ans
        v = a[j][j]
        ans = ans * v % p
        inv = pow(v, -1, p)
        for i in range(j + 1, n):
            c = a[i][j] * inv % p
            if c:
                for h in range(j, n):
                    a[i][h] = (a[i][h] - c * a[j][h]) % p
    return ans % p


def make_algebra():
    b = [
        [[int(i == j) for j in range(4)] for i in range(4)],
        [[(i + 1) * int(i == j) for j in range(4)] for i in range(4)],
        [[int(abs(i - j) == 1) for j in range(4)] for i in range(4)]
    ]
    table = [[[0] * 8 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        table[0][i][i] = 1
        table[i][0][i] = 1
    for i in range(4):
        for j in range(4):
            for k in range(3):
                table[i + 1][j + 1][k + 5] = b[k][i][j]
    return b, table


def multiply(table, u, v):
    out = [0] * 8
    for i, a in enumerate(u):
        for j, b in enumerate(v):
            if a and b:
                for k, c in enumerate(table[i][j]):
                    out[k] += a * b * c
    return out


def polynomial_relations():
    return [
        {(1, 0, 1, 0): 1},
        {(1, 0, 0, 1): 1},
        {(0, 1, 0, 1): 1},
        {(1, 1, 0, 0): 1, (0, 1, 1, 0): -1},
        {(0, 1, 1, 0): 1, (0, 0, 1, 1): -1},
        {(2, 0, 0, 0): 1, (0, 2, 0, 0): -2, (0, 0, 2, 0): 1},
        {(0, 2, 0, 0): 1, (0, 0, 2, 0): -2, (0, 0, 0, 2): 1},
    ]


def monomials(degree):
    return [v for v in product(range(degree + 1), repeat=4) if sum(v) == degree]


def main():
    start = datetime.now(timezone.utc).isoformat()
    t0 = perf_counter()
    b, table = make_algebra()
    basis = [[int(i == j) for j in range(8)] for i in range(8)]
    for i, j, k in product(range(8), repeat=3):
        assert multiply(table, table[i][j], basis[k]) == multiply(table, basis[i], table[j][k])
    assert all(table[i][j] == table[j][i] for i in range(8) for j in range(8))
    ms = [[[table[i + 1][j][h] for j in range(8)] for h in range(8)] for i in range(4)]
    for i, j in combinations(range(4), 2):
        assert mm(ms[i], ms[j]) == mm(ms[j], ms[i])

    qs = polynomial_relations()
    mons2, mons3 = monomials(2), monomials(3)
    quad_rows = [[f.get(v, 0) for v in mons2] for f in qs]
    assert rank_witness(quad_rows)['rank'] == 7
    for f in qs:
        value = [0] * 8
        for exponent, c in f.items():
            term = basis[0]
            for i, e in enumerate(exponent):
                for _ in range(e):
                    term = multiply(table, term, basis[i + 1])
            value = [v + c * w for v, w in zip(value, term)]
        assert value == [0] * 8
    cubic_rows = []
    for f in qs:
        for i in range(4):
            g = {}
            for exponent, c in f.items():
                new = list(exponent)
                new[i] += 1
                g[tuple(new)] = c
            cubic_rows.append([g.get(v, 0) for v in mons3])
    cubic = rank_witness(cubic_rows)
    assert cubic['rank'] == 20
    chosen = [[cubic_rows[i][j] for j in cubic['columns']] for i in cubic['rows']]
    assert det_mod(chosen) == cubic['ordered_minor_determinant_mod101'] != 0

    # Row-major vectorization: [M,F] has coefficients below.
    ds = []
    for m in ms:
        d = [[0] * 64 for _ in range(64)]
        for i, j, h in product(range(8), repeat=3):
            d[8 * i + j][8 * h + j] += m[i][h]
            d[8 * i + j][8 * i + h] -= m[h][j]
        ds.append(d)
    d0 = [row[:] for d in ds for row in d]
    d1 = [[0] * 256 for _ in range(384)]
    for pair, (i, j) in enumerate(combinations(range(4), 2)):
        for h in range(64):
            for k in range(64):
                d1[64 * pair + h][64 * j + k] += ds[i][h][k]
                d1[64 * pair + h][64 * i + k] -= ds[j][h][k]
    assert all(v == 0 for row in mm(d1, d0) for v in row)
    rank0, rank1 = rank_witness(d0), rank_witness(d1)
    assert rank0['rank'] == 56 and rank1['rank'] == 175
    minor = [[d1[i][j] for j in rank1['columns']] for i in rank1['rows']]
    assert det_mod(minor) == rank1['ordered_minor_determinant_mod101'] != 0
    # Socle: simultaneous kernels of the four multiplication matrices.
    socle_rank = rank_witness([row for m in ms for row in m])['rank']
    assert socle_rank == 5
    # The four infinitesimal translations on the seven minimal quadrics.
    translation = []
    for f in qs:
        for output in range(4):
            row = []
            for derivative in range(4):
                exponent = [0] * 4
                exponent[output] += 1
                exponent[derivative] += 1
                row.append(f.get(tuple(exponent), 0) * exponent[derivative])
            translation.append(row)
    assert rank_witness(translation)['rank'] == 4
    result = {
        'status': 'PASS', 'started_utc': start,
        'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'field': 'integer algebra; modular rank certificates over F101',
        'multiplication_matrices_of_quadratic_forms': b,
        'associativity_checks': 512, 'commuting_pairs': 6,
        'hilbert_function': [1, 4, 3], 'length': 8, 'socle_dimension': 3,
        'quadratic_relation_rank': 7, 'cubic_macaulay_rank': 20,
        'cubic_rank_witness': cubic,
        'commutator_differential_shapes': [[256, 64], [384, 256]],
        'rank_d0_mod101': rank0['rank'], 'rank_d1_mod101': rank1['rank'],
        'd1_minor_witness': rank1,
        'char0_Hom_I_A_upper_bound': 25,
        'written_proof_lower_bound': '21 degree-zero maps plus4 independent translations',
        'translation_rank': 4, 'Hom_I_A_exact_dimension': 25, 'delta': 1,
        'new_local_bound': '2q^2+8', 'global_invariant_kernel_bound': 4,
        'limitation': 'Finite witness only. Translation/hull tangent exactness, supported cone duality, and finite-action/global semiregularity conclusions are proved in the accompanying text. No universal lower bound on delta is asserted.',
        'seconds': perf_counter() - t0, 'finished_utc': datetime.now(timezone.utc).isoformat(),
    }
    out = HERE / 'rm_nonci_translation_certificate_output.json'
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('d1_minor_witness', 'cubic_rank_witness')}, indent=2))


if __name__ == '__main__':
    main()
