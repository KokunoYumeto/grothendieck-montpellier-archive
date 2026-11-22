#!/usr/bin/env python3
"""Exact Bockstein certificate for C:Bockstein_parity / flat_nilpotent_kernel.

All arithmetic is integer modulo four or binary; no floating point is used.
The invariant is constructed from ker/im of T-1, not from classification of
involutions. Exhaustive scope: all matrices of ranks 1 and 2 over Z/4 and all
upper triangular extensions with endpoint ranks (1,1), (1,2), (2,1).
"""
from itertools import product
from functools import lru_cache
from pathlib import Path
from time import perf_counter
import json
import numpy as np

START = perf_counter()

def binary(v):
    return sum((int(a) & 1) << j for j, a in enumerate(v))

def vector(v, n):
    return np.array([(v >> j) & 1 for j in range(n)], dtype=np.int64)

def span_basis(vectors):
    basis, space = [], {0}
    for v in vectors:
        if v not in space:
            basis.append(v)
            space |= {x ^ v for x in tuple(space)}
    return basis

def span_coordinates(basis):
    answer = {0: 0}
    for j, v in enumerate(basis):
        answer.update({x ^ v: c | (1 << j) for x, c in tuple(answer.items())})
    return answer

def rank_binary(a):
    return len(span_basis(binary(a[:, j]) for j in range(a.shape[1])))

@lru_cache(None)
def homology_data(entries, n):
    t = np.array(entries, dtype=np.int64).reshape(n, n) % 4
    assert np.array_equal(t @ t % 4, np.eye(n, dtype=np.int64) % 4)
    d = (t - np.eye(n, dtype=np.int64)) % 4
    db = d % 2
    assert not np.any(db @ db % 2)
    boundaries = span_basis(binary(db[:, j]) for j in range(n))
    cycles = [v for v in range(1 << n) if not np.any(db @ vector(v, n) % 2)]
    basis = list(boundaries)
    for v in cycles:
        if v not in span_coordinates(basis):
            basis.append(v)
    h_basis = basis[len(boundaries):]
    coordinates = span_coordinates(basis)
    h = len(h_basis)
    N = np.zeros((h, h), dtype=np.int64)
    for j, v in enumerate(h_basis):
        twice = d @ vector(v, n) % 4
        assert not np.any(twice % 2)
        w = binary(twice // 2)
        assert w in coordinates
        c = coordinates[w] >> len(boundaries)
        N[:, j] = vector(c, h)
    fN = (N @ N + N + np.eye(h, dtype=np.int64)) % 2
    power = np.eye(h, dtype=np.int64)
    for _ in range(max(1, h)):
        power = power @ fN % 2
    primary_dim = h - rank_binary(power)
    assert primary_dim % 2 == 0
    return {
        'D_mod2': db.tolist(), 'boundary_dimension': len(boundaries),
        'H_dimension': h, 'H_basis_bits': h_basis, 'N': N.tolist(),
        'f_primary_dimension': primary_dim, 'chi': (primary_dim // 2) % 2,
        '_basis': basis, '_coordinates': coordinates,
    }

def data(t):
    return homology_data(tuple(int(x) for x in t.flat), len(t))

def h_map(source, target, linear):
    """Induced binary map in the explicitly selected quotient bases."""
    s, t = data(source), data(target)
    out = np.zeros((t['H_dimension'], s['H_dimension']), dtype=np.int64)
    b = t['boundary_dimension']
    for j, v in enumerate(s['H_basis_bits']):
        image = binary(linear @ vector(v, len(source)) % 2)
        c = t['_coordinates'][image] >> b
        out[:, j] = vector(c, t['H_dimension'])
    return out

def verify_extension(a, b, X):
    r, s = len(a), len(b)
    e = np.block([[a, X], [np.zeros((s, r), dtype=np.int64), b]]) % 4
    if not np.array_equal(e @ e % 4, np.eye(r + s, dtype=np.int64)):
        return False
    da, de, db = data(a), data(e), data(b)
    assert de['chi'] == da['chi'] ^ db['chi']
    inc = np.vstack([np.eye(r, dtype=np.int64), np.zeros((s, r), dtype=np.int64)])
    proj = np.hstack([np.zeros((s, r), dtype=np.int64), np.eye(s, dtype=np.int64)])
    hi, hp, hd = h_map(a, e, inc), h_map(e, b, proj), h_map(b, a, X)
    na = np.array(da['N'], dtype=np.int64).reshape(da['H_dimension'], da['H_dimension'])
    ne = np.array(de['N'], dtype=np.int64).reshape(de['H_dimension'], de['H_dimension'])
    nb = np.array(db['N'], dtype=np.int64).reshape(db['H_dimension'], db['H_dimension'])
    assert not np.any((ne @ hi - hi @ na) % 2)
    assert not np.any((nb @ hp - hp @ ne) % 2)
    assert not np.any((na @ hd - hd @ (nb + np.eye(len(nb), dtype=np.int64))) % 2)
    assert rank_binary(hi) + rank_binary(hd) == da['H_dimension']
    assert rank_binary(hp) + rank_binary(hi) == de['H_dimension']
    assert rank_binary(hd) + rank_binary(hp) == db['H_dimension']
    return True

involutions = {}
counts = {}
for n in (1, 2):
    group = []
    for entries in product(range(4), repeat=n*n):
        t = np.array(entries, dtype=np.int64).reshape(n, n)
        if np.array_equal(t @ t % 4, np.eye(n, dtype=np.int64)):
            group.append(t)
            q = data(t)
            # Check every cycle lift and every changed lift, including boundaries.
            D = (t - np.eye(n, dtype=np.int64)) % 4
            bound = q['boundary_dimension']
            coords = q['_coordinates']
            N = np.array(q['N'], dtype=np.int64).reshape(q['H_dimension'], q['H_dimension'])
            for v, vc in coords.items():
                vvec = vector(v, n)
                expected = binary(N @ vector(vc >> bound, q['H_dimension']) % 2)
                for u in range(1 << n):
                    lift = vvec + 2 * vector(u, n)
                    twice = D @ lift % 4
                    assert not np.any(twice % 2)
                    actual = coords[binary(twice // 2)] >> bound
                    assert actual == expected
    involutions[n] = group
    counts[n] = {'all_matrices_tested': 4 ** (n*n), 'involutions': len(group),
                 'chi_one': sum(data(t)['chi'] for t in group)}

extension_counts = {}
for r, s in ((1, 1), (1, 2), (2, 1)):
    tested = valid = 0
    for a in involutions[r]:
        for b in involutions[s]:
            for entries in product(range(4), repeat=r*s):
                X = np.array(entries, dtype=np.int64).reshape(r, s)
                tested += 1
                valid += verify_extension(a, b, X)
    extension_counts[f'{r}+{s}'] = {'block_matrices_tested': tested, 'admissible_extensions': valid}

T = np.array([[1, 2], [2, 3]], dtype=np.int64)
J = np.array([[0, 1], [-1, 0]], dtype=np.int64)
assert not np.any((J @ T + T @ J) % 4)
assert verify_extension((-T) % 4, T, np.eye(2, dtype=np.int64))
trivial = np.array([[1]], dtype=np.int64)
sign = np.array([[3]], dtype=np.int64)
regular = np.array([[0, 1], [1, 0]], dtype=np.int64)
assert data(T)['chi'] == 1
assert data(trivial)['chi'] == data(sign)['chi'] == data(regular)['chi'] == 0

# Integral coefficient check over Z[epsilon]/epsilon^2, not only the quotient.
T0 = np.array([[1, 0], [0, -1]], dtype=np.int64)
T1 = np.array([[0, 1], [1, 0]], dtype=np.int64)
assert np.array_equal(T0 @ T0, np.eye(2, dtype=np.int64))
assert not np.any(T0 @ T1 + T1 @ T0)
assert not np.any(J @ T0 + T0 @ J)
assert not np.any(J @ T1 + T1 @ J)

def public(d):
    return {k: v for k, v in d.items() if not k.startswith('_')}

def pmul(a, b):
    c = 0
    while b:
        if b & 1:
            c ^= a
        a <<= 1
        b >>= 1
    return c

def pmod(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a

def pgcd(a, b):
    while b:
        a, b = b, pmod(a, b)
    return a

def irreducible_power_two_degree(q):
    d = q.bit_length() - 1
    assert d and not (d & (d - 1))
    x, h = pmod(2, q), pmod(2, q)
    for j in range(1, d + 1):
        h = pmod(pmul(h, h), q)
        if d > 1 and j == d // 2 and pgcd(h ^ x, q) != 1:
            return False
    return h == x

def composition_artin_schreier(q):
    result, power = 0, 1
    while q:
        if q & 1:
            result ^= power
        q >>= 1
        power = pmul(power, 6)  # t^2+t
    return result

def matrix_poly(poly, N):
    n = len(N)
    out = np.zeros((n, n), dtype=np.int64)
    power = np.eye(n, dtype=np.int64)
    while poly:
        if poly & 1:
            out ^= power
        poly >>= 1
        power = power @ N % 2
    return out

family = []
for d in (1, 2, 4):
    q = next(q for q in range(1 << d, 1 << (d + 1))
             if (q & 1) and ((q >> (d - 1)) & 1)
             and irreducible_power_two_degree(q))
    f = composition_artin_schreier(q)
    assert irreducible_power_two_degree(f)
    B = np.zeros((d, d), dtype=np.int64)
    for j in range(d - 1):
        B[j + 1, j] = 1
    B[:, d - 1] = vector(q, d)
    I = np.eye(d, dtype=np.int64)
    Z = np.zeros((d, d), dtype=np.int64)
    Tb = np.block([[I, 2*B], [2*I, -I]]) % 4
    Nb = np.block([[Z, B], [I, I]]) % 2
    Db = data(Tb)
    assert Db['H_dimension'] == 2*d
    assert np.array_equal(np.array(Db['N']), Nb)
    assert not np.any(matrix_poly(f, Nb))
    Jb = np.block([[Z, B], [-I, Z]])
    assert not np.any((Jb @ Tb + Tb @ Jb) % 4)
    family.append({'d': d, 'q_bits': q, 'f_bits': f, 'N': Nb.tolist()})
parity_matrix = []
for row in family:
    N = np.array(row['N'], dtype=np.int64)
    parities = []
    for column in family:
        f = column['f_bits']
        fN = matrix_poly(f, N)
        power = np.eye(len(N), dtype=np.int64)
        for _ in range(len(N)):
            power = power @ fN % 2
        dimension = len(N) - rank_binary(power)
        degree = f.bit_length() - 1
        assert dimension % degree == 0
        parities.append((dimension // degree) % 2)
    parity_matrix.append(parities)
assert parity_matrix == np.eye(3, dtype=np.int64).tolist()

result = {
    'status': 'all passed', 'exact_arithmetic': 'Z/4 and F2; binary Gaussian span enumeration',
    'exhaustive_involutions': counts, 'exhaustive_extension_checks': extension_counts,
    'witness': {'T': T.tolist(), **public(data(T))},
    'trivial_chi': data(trivial)['chi'], 'sign_chi': data(sign)['chi'],
    'regular_chi': data(regular)['chi'], 'rank_four_order_two_sequence_verified': True,
    'integral_dual_number_T_squared_and_sign_conjugation_verified': True,
    'infinite_family_first_three': family, 'family_parity_matrix': parity_matrix,
    'seconds': round(perf_counter() - START, 6),
}
output = Path(__file__).resolve().parents[1] / 'logs' / 'C_finish_bockstein.json'
output.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
