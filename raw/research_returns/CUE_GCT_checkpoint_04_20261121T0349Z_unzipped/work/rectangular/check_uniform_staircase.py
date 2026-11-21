"""Bounded exact checks supplementing the uniform R22 proof.

These checks enumerate local permutations and binary coefficient formulas;
they do not compute or extrapolate growing permanent-pencil Jacobian ranks.
"""
from itertools import permutations
from pathlib import Path
import json


def prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, int(n ** .5) + 1))


def field(m):
    p = m + 1
    while not prime(p):
        p += m
    factors = [d for d in range(2, m + 1) if m % d == 0 and prime(d)]
    for a in range(2, p):
        q = pow(a, (p - 1) // m, p)
        if all(pow(q, m // d, p) != 1 for d in factors):
            return p, q
    raise AssertionError('primitive root not found')


def mul(a, b, p):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % p
    return c


def product(roots, p):
    a = [1]
    for root in roots:
        a = mul(a, [1, -root % p], p)
    return a


def evaluate(a, z, p):
    return sum(c * pow(z, len(a) - 1 - i, p)
               for i, c in enumerate(a)) % p


def solve(columns, target, p):
    n = len(columns)
    a = [[columns[j][i] % p for j in range(n)] + [target[i] % p]
         for i in range(n)]
    for j in range(n):
        i = next(i for i in range(j, n) if a[i][j])
        a[i], a[j] = a[j], a[i]
        inv = pow(a[j][j], -1, p)
        a[j] = [v * inv % p for v in a[j]]
        for i in range(n):
            if i != j:
                v = a[i][j]
                a[i] = [(x - v * y) % p for x, y in zip(a[i], a[j])]
    return [a[i][-1] for i in range(n)]


def local_permutation_checks(r):
    counts = {'r': r, 'minors': r + 1, 'zero_one_chord': 0,
              'endpoint_two_chord': 0, 'no_forward': 0,
              'top_two_chord_terms': 0}
    for missing in range(r + 1):
        columns = [j for j in range(r + 1) if j != missing]
        top = set()
        for permutation in permutations(columns):
            extra = [(i, j) for i, j in enumerate(permutation)
                     if j not in (i, i + 1)]
            inversions = sum(permutation[i] > permutation[j]
                             for i in range(r) for j in range(i + 1, r))
            parity = (inversions + sum(j - i - 1 if j > i + 1 else i - j
                                      for i, j in extra)) % 2
            if len(extra) <= 1:
                assert parity == 0
                counts['zero_one_chord'] += 1
            if missing in (0, r) and len(extra) == 2:
                assert parity == 0
                counts['endpoint_two_chord'] += 1
            if not any(j > i + 1 for i, j in extra):
                assert parity == 0
                counts['no_forward'] += 1
            l_degree = sum(j == i or j > i + 1
                           for i, j in enumerate(permutation))
            if len(extra) == 2 and parity and l_degree == 1:
                top.add(tuple(extra))
        expected = {((missing - 1, h + 1), (h, 0))
                    for h in range(missing, r)} if 0 < missing < r else set()
        assert top == expected, (r, missing, top, expected)
        counts['top_two_chord_terms'] += len(top)
    return counts


def row_transform_by_x_power(a, xy, zw, b, q, K, p):
    bases = []
    for j in range(1, a + 2):
        roots = [K * pow(q, u, p) % p for u in range(j, a + 1)]
        roots += [pow(q, u, p) for u in range(1, j)]
        bases.append(product(roots, p))
    coeff = solve(bases, xy, p)
    out = {}
    for j, c in enumerate(coeff, 1):
        shifted = [v * pow(q, -j * i, p) % p for i, v in enumerate(zw)]
        roots = [pow(q, u, p) for u in range(b - j, b - 1)]
        roots += [K * pow(q, u, p) % p for u in range(-1, a - j)]
        out[j] = [c * v % p for v in mul(shifted, product(roots, p), p)]
    return out


def specialization_check(b, k):
    m = 8 * b
    p, q = field(m)
    K = pow(q, k, p)
    r = b - 1
    for i in range(r - 2):
        xy = [1, -q % p]
        zw = product([pow(q, u, p) for u in range(1, r + 1)
                      if u != i + 2], p) + [0]
        zw = [-v % p for v in zw]
        actual = row_transform_by_x_power(1, xy, zw, b, q, K, p)
        expected = product([pow(q, u, p) for u in range(-1, r)
                            if u != i], p) + [0]
        expected = [-v % p for v in expected]
        assert all(v == 0 for v in actual[1])
        assert actual[2] == expected
        for h in range(r):
            value = evaluate(expected, pow(q, h, p), p)
            assert (value != 0) == (h == i)
    p2 = [1, -pow(q, 2, p) % p]
    uzw = [-v % p for v in product([pow(q, u, p)
                                    for u in range(1, r)], p) + [0]]
    vxy = mul([1, -pow(q, r, p) % p], p2, p)
    vzw = product([pow(q, u, p) for u in range(1, r - 1)], p) + [0]
    U = row_transform_by_x_power(1, p2, uzw, b, q, K, p)
    V = row_transform_by_x_power(2, vxy, vzw, b, q, K, p)
    A, B = pow(q, r - 2, p), pow(q, r - 1, p)
    ueA = {j: evaluate(f, A, p) for j, f in U.items()}
    ueB = {j: evaluate(f, B, p) for j, f in U.items()}
    veA = {j: evaluate(f, A, p) for j, f in V.items()}
    veB = {j: evaluate(f, B, p) for j, f in V.items()}
    assert ueA[1] == ueB[2] == veB[2] == veB[3] == veA[3] == 0
    lhs = (ueA[1] * veB[1] - veA[1] * ueB[1]) % p
    alpha = (q - 1) * pow(K - 1, -1, p) % p
    c1 = (1 - pow(q, r - 1, p)) * (1 - q) % p
    c1 = c1 * pow((1 - K) * (1 - K * q) % p, -1, p) % p
    rhs = alpha * c1 * A * B % p
    for u in range(r - 1):
        rhs = rhs * (B - pow(q, u, p)) % p
    for u in range(r - 2):
        rhs = rhs * (A - pow(q, u, p)) % p
    for v in [B - K * pow(q, -1, p), A - K * pow(q, -1, p), A - K]:
        rhs = rhs * v % p
    assert lhs == rhs and rhs != 0, (b, k, p, lhs, rhs)
    return {'b': b, 'm': m, 'k': k, 'p': p, 'q': q,
            'last_minor_X2': rhs, 'passed': True}


def main():
    local = [local_permutation_checks(r) for r in range(2, 8)]
    binary = [specialization_check(b, k) for b in range(3, 11)
              for k in sorted({2 * b - 1, 4 * b, 6 * b + 1})]
    result = {'scope': 'bounded local permutation and exact binary coefficient checks; no growing Jacobian computation',
              'local': local, 'binary': binary, 'passed': True}
    Path(__file__).with_name('uniform_staircase_check.json').write_text(
        json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
