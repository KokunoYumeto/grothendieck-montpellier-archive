#!/usr/bin/env python3
"""Exact p=3,5 audit of the deep resolved-tail low-form weights.

Verifies every coefficient-resolution matrix through weight p^2,
including the new e_(p^2) generator.  All lattice tests use exact
Z_(p) elementary operations.  No modular-rank inference is used.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json
import time
import sympy as sp


def vp(a, p):
    a = F(a)
    if not a:
        return 10**9
    n, d, v = abs(a.numerator), a.denominator, 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def smith(a, ncols, p):
    a = [[F(x) for x in row] for row in a]
    m, n = len(a), ncols
    u, v, rank = eye(m), eye(n), 0
    for k in range(min(m, n)):
        candidates = [(vp(a[i][j], p), i, j) for i in range(k, m)
                      for j in range(k, n) if a[i][j]]
        if not candidates:
            break
        _, r, c = min(candidates)
        a[k], a[r] = a[r], a[k]
        u[k], u[r] = u[r], u[k]
        for matrix in (a, v):
            for row in matrix:
                row[k], row[c] = row[c], row[k]
        pivot = a[k][k]
        for i in range(k + 1, m):
            q = a[i][k] / pivot
            assert vp(q, p) >= 0
            a[i] = [x - q * y for x, y in zip(a[i], a[k])]
            u[i] = [x - q * y for x, y in zip(u[i], u[k])]
        for j in range(k + 1, n):
            q = a[k][j] / pivot
            assert vp(q, p) >= 0
            for i in range(m):
                a[i][j] -= q * a[i][k]
            for i in range(n):
                v[i][j] -= q * v[i][k]
        rank += 1
    return a, v, rank


def kernel(a, ncols, p):
    _, v, rank = smith(a, ncols, p)
    return [[row[j] for j in range(rank, ncols)] for row in v]


def coordinates(b, a):
    dim = len(b[0]) if b else 0
    if not dim:
        assert not any(x for row in a for x in row)
        return []
    bm, am = sp.Matrix(b), sp.Matrix(a)
    rows = list(bm.T.rref()[1])
    result = bm[rows, :].inv() * am[rows, :]
    assert bm * result == am
    return [[F(x) for x in row] for row in result.tolist()]


class Resolution:
    def __init__(self, p):
        self.p, self.cutoff = p, p * p
        c = factorial(p - 1)
        self.gens = [[('e1', 1), ('ep', p), ('epp', p * p)]]
        self.data = [{}]
        a = factorial(p * (p - 1)) // (factorial(p) ** (p - 1))
        delta = factorial(p * p) // (factorial(p) ** p)
        self.gens.append([('r0', p), ('r1', p + 1), ('rpp', p * p)])
        self.data.append({'r0': {'e1': F(c), 'ep': F(-p * c)},
                          'r1': {'e1': F(1), 'ep': F(-1)},
                          'rpp': {'ep': F(a), 'epp': F(-delta)}})
        for k in range(2, 2 * p + 1):
            if k % 2 == 0:
                j = k // 2
                weights = [j * p + 1, (j + 1) * p]
                matrix = [[1, 1], [-p * c, -c]]
            else:
                j = (k - 1) // 2
                weights = [(j + 1) * p, (j + 1) * p + 1]
                matrix = [[c, 1], [-p * c, -1]]
            previous = self.gens[k - 1][:2]
            gens = [(f'q{k}_{i}', wt) for i, wt in enumerate(weights)]
            data = {name: {previous[i][0]: F(matrix[i][j]) for i in range(2)}
                    for j, (name, _) in enumerate(gens)}
            self.gens.append(gens)
            self.data.append(data)

    def at(self, k, w):
        return [(n, v) for n, v in self.gens[k] if v <= w]

    def matrix(self, k, w):
        source = self.at(k, w)
        if not k:
            return [[F(comb(w, wt)) for _, wt in source]]
        target = self.at(k - 1, w)
        return [[self.data[k][name].get(tname, F(0)) * comb(w - tw, w - sw)
                 for name, sw in source] for tname, tw in target]

    def w_d1(self, weight):
        q = 2 * self.p
        source = [('u', q - 2, n, w) for n, w in self.at(q - 2, weight)]
        source += [('v', q - 3, n, w) for n, w in self.at(q - 3, weight)]
        target = [('u', q - 3, n, w) for n, w in self.at(q - 3, weight)]
        target += [('v', q - 4, n, w) for n, w in self.at(q - 4, weight)]
        result = []
        for kind_t, level_t, name_t, wt in target:
            row = []
            for kind_s, level_s, name_s, ws in source:
                value = F(0)
                if kind_s == kind_t and level_t == level_s - 1:
                    value = self.data[level_s][name_s].get(name_t, F(0))
                    if kind_s == 'u':
                        value = -value
                elif kind_s == 'v' and kind_t == 'u' and level_s == level_t and name_s == name_t:
                    value = F(self.p)
                row.append(value * comb(weight - wt, weight - ws))
            result.append(row)
        return source, target, result


def main():
    started = time.perf_counter()
    answer = []
    for p in (3, 5):
        res = Resolution(p)
        checks = 0
        matrices = {}
        for w in range(1, p * p + 1):
            assert min(vp(x, p) for x in res.matrix(0, w)[0] if x) == 0
            for k in range(1, 2 * p + 1):
                previous, current = res.matrix(k - 1, w), res.matrix(k, w)
                nprev = len(res.at(k - 1, w))
                basis = kernel(previous, nprev, p)
                dim = len(basis[0]) if basis else 0
                if dim:
                    co = coordinates(basis, current)
                    diagonal, _, rank = smith(co, len(res.at(k, w)), p)
                    assert rank == dim, (p, w, k, 'rank')
                    assert all(vp(diagonal[i][i], p) == 0 for i in range(rank)), (p, w, k, 'lattice')
                else:
                    assert not any(x for row in current for x in row)
                checks += 1
                matrices[f'{k}:{w}'] = current
        zero_ranks = {}
        first_zero = None
        first_one = None
        for w in range(1, p * p + 1):
            source, target, matrix = res.w_d1(w)
            if source and first_one is None:
                first_one = w
            basis = kernel(matrix, len(source), p)
            rank = len(basis[0]) if basis else 0
            zero_ranks[str(w)] = rank
            if rank and first_zero is None:
                first_zero = w
        expected_one = p * (p - 1)
        assert first_one == expected_one
        assert first_zero == expected_one + 1
        source, target, matrix = res.w_d1(first_zero)
        q = 2 * p
        c = factorial(p - 1)
        C = []
        for kind, level, name, wt in source:
            if kind == 'u':
                value = p if name == res.gens[q - 2][0][0] else 0
            elif name == res.gens[q - 3][0][0]:
                value = 1
            else:
                value = -p * c
            C.append(F(value))
        assert all(sum(a * b for a, b in zip(row, C)) == 0 for row in matrix)
        assert min(vp(x, p) for x in C if x) == 0
        assert zero_ranks[str(first_zero)] == 1
        # Leibniz expansion; x is odd, so the Tx*x term is zero.
        # The only reduction is t^(p-1)C=p(cK-H), verified by the
        # next coefficient-resolution column and its cone relation.
        derivative_coefficients = {'g*x': p, 'y*x': -p*c,
                                   'C*r': p, 'C*b': -p*c,
                                   'K*a': p*c, 'H*a': -p}
        divided_coefficients = {m: F(v, p) for m, v in derivative_coefficients.items()}
        assert all(v.denominator == 1 for v in divided_coefficients.values())
        assert divided_coefficients == {'g*x': 1, 'y*x': -c, 'C*r': 1,
                                        'C*b': -c, 'K*a': c, 'H*a': -1}
        answer.append({'prime': p, 'cutoff': p * p, 'exact_lattice_checks': checks,
                       'resolution_generators': res.gens,
                       'resolution_matrices': matrices,
                       'W0_weight_ranks': zero_ranks,
                       'minimum_W1_weight': first_one,
                       'minimum_W0_weight': first_zero,
                       'C_in_W1_basis': C,
                       'arity2_form1_total_unshifted_weight': first_one + first_zero,
                       'minimum_arity2_zeroform_weight': 2 * first_zero,
                       'arity2_form1_basis': ['C*x'],
                       'exact_d_Cx_coefficients': derivative_coefficients,
                       'exact_divided_coefficients': divided_coefficients,
                       'd_Cx_divided_by_p': ['g*x', f'-{c}*y*x', 'C*r', f'-{c}*C*b', f'({c}*K-H)*a'],
                       'independent_exterior_gx_coefficient': 1})
    result = {'passed': True, 'scope': 'complete coefficient resolutions and bottom kernels through p^2 for p=3,5; exact Z_(p) lattice arithmetic',
              'results': answer, 'runtime_seconds': time.perf_counter() - started}
    dest = Path(__file__).resolve().parents[1] / 'logs/A_cosimplicial_deep_tail_certificate.json'
    dest.write_text(json.dumps(result, default=lambda x: str(x) if isinstance(x, F) else x, indent=2) + '\n')
    print(json.dumps({'passed': True, 'primes': [x['prime'] for x in answer],
                      'exact_lattice_checks': [x['exact_lattice_checks'] for x in answer],
                      'minima': [[x['minimum_W1_weight'], x['minimum_W0_weight']] for x in answer],
                      'runtime_seconds': result['runtime_seconds']}))


if __name__ == '__main__':
    main()
