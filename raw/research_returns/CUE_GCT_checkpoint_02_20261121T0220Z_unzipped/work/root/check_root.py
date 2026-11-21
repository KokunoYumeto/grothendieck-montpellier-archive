#!/usr/bin/env python3
"""Finite exact checks of G-01, G-03, and the explicit G-09 construction.

These computations supplement the written proofs; they are not formal proofs.
The determinantal construction is evaluated independently by modular Gaussian
elimination and direct sparse-polynomial evaluation, including zero padding.
"""
from collections import deque
from itertools import product
from math import comb, factorial
from pathlib import Path
import json
import random
import sympy as sp


def exponents(r, m):
    return sorted((a for a in product(range(m + 1), repeat=r) if sum(a) <= m),
                  key=lambda a: (sum(a), a))


def build(m, k, h=None):
    """Return vertices and labelled edges (constant or one variable)."""
    vertices, edges = set(), []
    def vertex(v):
        vertices.add(v)
        return v
    def edge(u, v, label):
        vertex(u); vertex(v)
        edges.append((u, v, label))
    left, right = {}, {}
    if k % 2:
        r = (k - 1) // 2
        for side, mapping in [('L', left), ('R', right)]:
            for a in exponents(r, m):
                mapping[a] = vertex((side, a))
                if sum(a):
                    j = max(i for i, e in enumerate(a) if e)
                    parent = list(a); parent[j] -= 1
                    u, v = (side, tuple(parent)), (side, a)
                    if side == 'R': u, v = v, u
                    edge(u, v, ('var', j + (r if side == 'R' else 0)))
        source, sink = left[(0,) * r], right[(0,) * r]
        for a, u in left.items():
            for b, v in right.items():
                if sum(a) + sum(b) <= m:
                    edge(u, v, ('coeff', a + b))
        expected = 2 * comb(m + r, r) - 1
    else:
        r = (k - 2) // 2
        assert r >= 1 and h is not None and 1 <= h <= m + 1
        Q, s0 = m // h, min(h - 1, m)
        for j in range(Q * h + 1):
            vertex(('Lz', j))
            if j: edge(('Lz', j - 1), ('Lz', j), ('var', 2 * r))
        for q in range(Q + 1):
            for a in exponents(r, m - q * h):
                v = ('Lz', q * h) if not sum(a) else ('Lx', q, a)
                left[q, a] = vertex(v)
                if sum(a):
                    j = max(i for i, e in enumerate(a) if e)
                    parent = list(a); parent[j] -= 1; parent = tuple(parent)
                    u = ('Lz', q * h) if not sum(parent) else ('Lx', q, parent)
                    edge(u, v, ('var', j))
        for s in range(s0 + 1):
            vertex(('Rz', s))
            if s: edge(('Rz', s), ('Rz', s - 1), ('var', 2 * r))
            for b in exponents(r, m - s):
                u = ('Rz', s) if not sum(b) else ('Ry', s, b)
                right[s, b] = vertex(u)
                if sum(b):
                    j = max(i for i, e in enumerate(b) if e)
                    parent = list(b); parent[j] -= 1; parent = tuple(parent)
                    v = ('Rz', s) if not sum(parent) else ('Ry', s, parent)
                    edge(u, v, ('var', r + j))
        source, sink = ('Lz', 0), ('Rz', 0)
        for (q, a), u in left.items():
            for (s, b), v in right.items():
                if sum(a) + sum(b) + q * h + s <= m:
                    edge(u, v, ('coeff', a + b + (q * h + s,)))
        expected = (sum(comb(m - q * h + r, r) for q in range(Q + 1))
                    + Q * (h - 1)
                    + sum(comb(m - s + r, r) for s in range(s0 + 1)) - 1)
    assert len(vertices) - 1 == expected
    # All coefficient exponents must occur once, including the constant term.
    support = [label[1] for _, _, label in edges if label[0] == 'coeff']
    assert len(support) == len(set(support)) == comb(m + k - 1, k - 1)
    assert set(support) == set(exponents(k - 1, m))
    adjacency, indegree = {v: [] for v in vertices}, {v: 0 for v in vertices}
    for u, v, label in edges:
        adjacency[u].append(v); indegree[v] += 1
    queue = deque(sorted((v for v in vertices if indegree[v] == 0), key=repr))
    order = []
    while queue:
        u = queue.popleft(); order.append(u)
        for v in adjacency[u]:
            indegree[v] -= 1
            if not indegree[v]: queue.append(v)
    assert len(order) == len(vertices) and order[0] == source and order[-1] == sink
    return order, edges, support, expected


def det_mod(A, prime):
    A = [[v % prime for v in row] for row in A]
    answer, n = 1, len(A)
    for j in range(n):
        pivot_row = next((i for i in range(j, n) if A[i][j]), None)
        if pivot_row is None: return 0
        if pivot_row != j:
            A[pivot_row], A[j] = A[j], A[pivot_row]; answer = -answer
        pivot = A[j][j]; answer = answer * pivot % prime
        inverse = pow(pivot, -1, prime)
        for i in range(j + 1, n):
            scale = A[i][j] * inverse % prime
            for c in range(j + 1, n):
                A[i][c] = (A[i][c] - scale * A[j][c]) % prime
    return answer % prime


def matrix(order, edges, values, coefficients, ell):
    index = {v: i for i, v in enumerate(order)}; size = len(order)
    # Homogenize constants before taking the cofactor; variable entries stay linear.
    A = [[ell if i == j else 0 for j in range(size)] for i in range(size)]
    for u, v, label in edges:
        value = values[label[1]] if label[0] == 'var' else coefficients[label[1]] * ell
        A[index[u]][index[v]] -= value
    M = [row[1:] for row in A[:-1]]
    if (size + 1) % 2:
        M[0] = [-value for value in M[0]]
    return M


def main():
    results = []
    E = (0, 1)
    pairs = list(product(E, repeat=2))
    fixed_pairs = sum((1-a, 1-b) == (a, b) for a, b in pairs)
    fixed_E = sum(1-a == a for a in E)
    assert fixed_pairs == 0 and 2 * 1 + fixed_E == 2
    results.append({'id': 'G-01', 'check': 'C2 fixed-point counterexample', 'left': 0, 'right': 2})
    for D in range(13):
        r = D + 1
        assert sum(comb(r, j) for j in range(0, r + 1, 2)) == 2 ** D
        for power in range(r):
            assert sum((-1)**j * comb(r, j) * j**power for j in range(r + 1)) == 0
        assert sum((-1)**j * comb(r, j) * j**r for j in range(r + 1)) == (-1)**r * factorial(r)
    results.append({'id': 'G-03', 'check': 'Rank, finite moments, first nonzero derivative', 'D': '0..12'})
    for m, k, h in [(1, 3, None), (1, 4, 1), (2, 4, 1)]:
        order, edges, support, B = build(m, k, h)
        variables = sp.symbols(f'x0:{k-1}'); ell = sp.Symbol('ell')
        coefficients = dict(zip(support, sp.symbols(f'c0:{len(support)}')))
        M = sp.Matrix(matrix(order, edges, variables, coefficients, ell))
        target = sum(coefficients[a] * sp.prod(x**e for x, e in zip(variables, a))
                     * ell**(B-sum(a)) for a in support)
        assert sp.expand(M.det(method='domain-ge') - target) == 0
        results.append({'id': 'G-09', 'check': 'Universal symbolic determinant identity', 'm': m, 'k': k, 'h': h, 'B': B})
    rng = random.Random(20261121)
    for m, k, h in [(3, 4, 2), (6, 4, 2), (10, 4, 3), (4, 5, None), (5, 6, 2), (4, 8, 2)]:
        order, edges, support, B = build(m, k, h)
        for trial in range(12):
            prime = (101, 103, 107)[trial % 3]
            values = [rng.randrange(prime) for _ in range(k-1)]
            coefficients = {a: rng.randrange(prime) for a in support}
            ell = 0 if trial == 0 else rng.randrange(1, prime)
            M = matrix(order, edges, values, coefficients, ell)
            target = sum(coefficients[a] * sp.prod(pow(x, e, prime) for x, e in zip(values, a))
                         * pow(ell, B-sum(a), prime) for a in support) % prime
            assert det_mod(M, prime) == target
        results.append({'id': 'G-09', 'check': '12 exact modular determinant evaluations', 'm': m, 'k': k, 'h': h, 'B': B, 'primes': [101, 103, 107]})
    out = Path(__file__).with_name('computation_results.json')
    out.write_text(json.dumps({'scope': 'Finite exact computations, not a general formal proof', 'results': results}, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'records': len(results), 'output': str(out)}))


if __name__ == '__main__':
    main()
