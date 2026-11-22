#!/usr/bin/env python3
"""Exploratory exact Z_(2) resolution and arity-two PD lattices.

This script is a research probe.  It computes a complete weightwise
minimal graded free resolution of I_1 to the requested finite weight,
then the nonnegative resolved 2-cone W and its torsion-free arity-two
free relative PD algebra.  All matrix arithmetic is rational and all
lattice operations are over Z_(2), using exact valuation pivots.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import argparse
import json
import time
import sympy as sp


def val2(x):
    x = F(x)
    if not x:
        return 10**9
    n, d, out = abs(x.numerator), x.denominator, 0
    while n % 2 == 0:
        n //= 2
        out += 1
    while d % 2 == 0:
        d //= 2
        out -= 1
    return out


def fm(a):
    return [[F(x) for x in row] for row in a]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def mm(a, b, rows=None, cols=None):
    if not a:
        return []
    if not b:
        return [[] for _ in a]
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def inverse(a):
    if not a:
        return []
    return fm(sp.Matrix(a).inv().tolist())


def smith_dvr(a, ncols=None):
    """Return U,A_diag,V with U*A_original*V=A_diag, U,V unimodular Z_(2)."""
    a = fm(a)
    m = len(a)
    n = len(a[0]) if m else (ncols or 0)
    u, v = eye(m), eye(n)
    rank = 0
    for k in range(min(m, n)):
        candidates = [(val2(a[i][j]), i, j) for i in range(k, m)
                      for j in range(k, n) if a[i][j]]
        if not candidates:
            break
        _, r, c = min(candidates)
        if r != k:
            a[k], a[r] = a[r], a[k]
            u[k], u[r] = u[r], u[k]
        if c != k:
            for matrix in (a, v):
                for row in matrix:
                    row[k], row[c] = row[c], row[k]
        pivot = a[k][k]
        for i in range(k + 1, m):
            if a[i][k]:
                ratio = a[i][k] / pivot
                assert val2(ratio) >= 0
                a[i] = [x - ratio * y for x, y in zip(a[i], a[k])]
                u[i] = [x - ratio * y for x, y in zip(u[i], u[k])]
        for j in range(k + 1, n):
            if a[k][j]:
                ratio = a[k][j] / pivot
                assert val2(ratio) >= 0
                for i in range(m):
                    a[i][j] -= ratio * a[i][k]
                for i in range(n):
                    v[i][j] -= ratio * v[i][k]
        rank += 1
    return u, a, v, rank


def kernel_basis(a, ncols):
    _, diag, v, rank = smith_dvr(a, ncols)
    return [[row[j] for j in range(rank, ncols)] for row in v]


def coords(basis, columns):
    # Both arguments have ambient rows.  The basis has independent columns.
    if not basis or not basis[0]:
        assert not any(x for row in columns for x in row)
        return []
    b = sp.Matrix(basis)
    pivots = list(b.T.rref()[1])
    square = [[basis[i][j] for j in range(len(basis[0]))] for i in pivots]
    selected = [columns[i] for i in pivots]
    result = mm(inverse(square), selected)
    assert mm(basis, result) == columns
    return result


def mod2(x):
    x = F(x)
    assert val2(x) >= 0
    return x.numerator % 2  # the denominator is odd after reduction


def complement_mod2(columns, dimension):
    vectors = [list(c) for c in zip(*columns)] if columns and columns[0] else []
    pivots = {}
    def add(vector):
        v = [mod2(x) for x in vector]
        for i in sorted(pivots):
            if v[i]:
                v = [a ^ b for a, b in zip(v, pivots[i])]
        if not any(v):
            return False
        pivots[next(i for i, x in enumerate(v) if x)] = v
        return True
    for v in vectors:
        add(v)
    chosen = []
    for i in range(dimension):
        vector = [F(j == i) for j in range(dimension)]
        if add(vector):
            chosen.append(i)
    return chosen


class Resolution:
    def __init__(self, cutoff):
        self.cutoff = cutoff
        self.gens = [[], [], []]
        self.new_d = [{}, {}, {}]
        self.matrices = [{}, {}, {}]
        for level in range(3):
            for w in range(1, cutoff + 1):
                if level == 0:
                    basis = [[F(1)]]
                    existing = [[F(comb(w, g['weight'])) for g in self.gens[0]]]
                else:
                    prev = self.matrix(level - 1, w)
                    ntarget = len(self.at(level - 1, w))
                    basis = kernel_basis(prev, ntarget)
                    existing = self.matrix(level, w)
                dimension = len(basis[0]) if basis else 0
                existing_coords = coords(basis, existing) if dimension else []
                chosen = complement_mod2(existing_coords, dimension)
                for k in chosen:
                    gen = {'name': f'q{level}_{w}_{sum(g["weight"] == w for g in self.gens[level])}',
                           'weight': w}
                    vector = [row[k] for row in basis]
                    self.gens[level].append(gen)
                    if level == 0:
                        self.new_d[level][gen['name']] = {'unit': vector[0]}
                    else:
                        self.new_d[level][gen['name']] = {
                            g['name']: value for g, value in zip(self.at(level - 1, w), vector) if value}
                full = self.matrix(level, w)
                if dimension:
                    co = coords(basis, full)
                    assert not complement_mod2(co, dimension)
                self.matrices[level][w] = full

    def at(self, level, w):
        return [g for g in self.gens[level] if g['weight'] <= w]

    def matrix(self, level, w):
        sources = self.at(level, w)
        if level == 0:
            return [[self.new_d[0][g['name']]['unit'] * comb(w, g['weight']) for g in sources]]
        targets = self.at(level - 1, w)
        output = []
        for t in targets:
            row = []
            for g in sources:
                value = self.new_d[level][g['name']].get(t['name'], F(0))
                row.append(value * comb(w - t['weight'], w - g['weight']) if value else F(0))
            output.append(row)
        return output


class WComplex:
    def __init__(self, resolution):
        self.res = resolution
        self.cutoff = resolution.cutoff
        self.vars = []
        self.var_by_name = {}
        self.zero_lattice = {}
        self.linear = {}
        # Positive-degree generators are free over S.
        for degree, pairs in [(1, [(2, 'u'), (1, 'v')]),
                              (2, [(1, 'u'), (0, 'v')]), (3, [(0, 'u')])]:
            for level, kind in pairs:
                for g in resolution.gens[level]:
                    self.add_var({'name': kind + '_' + g['name'], 'degree': degree,
                                  'weight': g['weight'], 'level': level, 'kind': kind, 'd': {}})
        for v in self.vars:
            level, kind = v['level'], v['kind']
            if kind == 'u' and level > 0:
                v['d'] = {'u_' + t: -c for t, c in resolution.new_d[level][v['name'][2:]].items()}
            elif kind == 'v':
                v['d'] = {'u_' + v['name'][2:]: F(2)}
                if level > 0:
                    v['d'].update({'v_' + t: c for t, c in resolution.new_d[level][v['name'][2:]].items()})
        # Degree zero is the actual kernel inside W1.  Choose only a
        # rational graded S-basis; retain its full integral weight lattice.
        for weight in range(1, self.cutoff + 1):
            one = self.of_degree(1, weight)
            differential = self.linear_d(1, weight)
            integral = kernel_basis(differential, len(one))
            self.zero_lattice[weight] = integral
            old = self.zero_image_matrix(weight)
            old_rank = sp.Matrix(old).rank() if old and old[0] else 0
            current = [row[:] for row in old]
            for col in range(len(integral[0]) if integral else 0):
                candidate = [row[col] for row in integral]
                test = [row + [c] for row, c in zip(current, candidate)]
                rank = sp.Matrix(test).rank() if test else 0
                if rank > old_rank:
                    name = f'zero_{weight}_{sum(v["weight"] == weight for v in self.of_degree(0, weight))}'
                    self.add_var({'name': name, 'degree': 0, 'weight': weight,
                                  'd': {v['name']: c for v, c in zip(one, candidate) if c}})
                    current, old_rank = test, rank
            image = self.zero_image_matrix(weight)
            self.linear[0, weight] = coords(image, integral) if image and image[0] else []
        for degree in range(1, 4):
            for weight in range(1, self.cutoff + 1):
                self.linear[degree, weight] = eye(len(self.of_degree(degree, weight)))

    def add_var(self, v):
        self.var_by_name[v['name']] = v
        self.vars.append(v)

    def of_degree(self, degree, weight):
        return [v for v in self.vars if v['degree'] == degree and v['weight'] <= weight]

    def linear_d(self, degree, weight):
        sources, targets = self.of_degree(degree, weight), self.of_degree(degree + 1, weight)
        return [[v['d'].get(t['name'], F(0)) * comb(weight - t['weight'], weight - v['weight'])
                 if v['d'].get(t['name'], 0) else F(0) for v in sources] for t in targets]

    def zero_image_matrix(self, weight):
        return self.linear_d(0, weight)

    def lattice_vectors(self, degree, weight):
        vs = self.of_degree(degree, weight)
        matrix = self.linear.get((degree, weight), [])
        return [{v['name']: c for v, c in zip(vs, col) if c}
                for col in zip(*matrix)] if matrix and matrix[0] else []


class ArityTwo:
    def __init__(self, wcomplex, total):
        self.w = wcomplex
        self.total = total
        self.names = sorted(v['name'] for v in wcomplex.vars)
        self.order = {name: i for i, name in enumerate(self.names)}
        self.bases, self.index, self.lattices = {}, {}, {}
        for degree in range(7):
            basis = []
            for i, name in enumerate(self.names):
                a = wcomplex.var_by_name[name]
                for name2 in self.names[i:]:
                    b = wcomplex.var_by_name[name2]
                    if a['degree'] + b['degree'] != degree or a['weight'] + b['weight'] > total:
                        continue
                    if name == name2 and a['degree'] % 2:
                        continue
                    basis.append((name, name2))
            self.bases[degree] = basis
            self.index[degree] = {m: i for i, m in enumerate(basis)}
            columns = []
            for aweight in range(1, total):
                bweight = total - aweight
                if aweight > self.w.cutoff or bweight > self.w.cutoff:
                    continue
                for adegree in range(4):
                    bdegree = degree - adegree
                    if not 0 <= bdegree <= 3:
                        continue
                    for a in self.w.lattice_vectors(adegree, aweight):
                        for b in self.w.lattice_vectors(bdegree, bweight):
                            columns.append(self.product(a, aweight, b, bweight, degree))
            if degree in (0, 4):
                lin_degree = degree // 2
                for aw in range(1, total // 2 + 1):
                    for a in self.w.lattice_vectors(lin_degree, aw):
                        vector = self.product(a, aw, a, aw, degree)
                        # Multiply gamma_2(a) by the remaining coefficient.
                        for i, monomial in enumerate(basis):
                            genweight = sum(self.w.var_by_name[n]['weight'] for n in monomial)
                            old_coefficient = 2 * aw - genweight
                            vector[i] = vector[i] / 2 * comb(total - genweight, total - 2 * aw) if vector[i] else F(0)
                        columns.append(vector)
            matrix = [[col[i] for col in columns] for i in range(len(basis))]
            if basis:
                u, diagonal, _, rank = smith_dvr(matrix)
                assert rank == len(basis), (total, degree, rank, len(basis))
                ui = inverse(u)
                self.lattices[degree] = [[ui[i][j] * diagonal[j][j] for j in range(rank)] for i in range(rank)]
            else:
                self.lattices[degree] = []
        self.differentials = {}
        for degree in range(6):
            ambient = self.differential(degree)
            if self.bases[degree + 1]:
                actual = mm(inverse(self.lattices[degree + 1]), mm(ambient, self.lattices[degree]))
            else:
                actual = []
            assert all(val2(x) >= 0 for row in actual for x in row)
            self.differentials[degree] = actual
        for degree in range(5):
            if self.differentials[degree + 1] and self.differentials[degree]:
                square = mm(self.differentials[degree + 1], self.differentials[degree])
                assert not any(x for row in square for x in row)

    def product(self, left, lw, right, rw, degree):
        out = [F(0)] * len(self.bases[degree])
        for an, ac in left.items():
            a = self.w.var_by_name[an]
            for bn, bc in right.items():
                b = self.w.var_by_name[bn]
                if an == bn and a['degree'] % 2:
                    continue
                sign = 1
                aa, bb = an, bn
                if self.order[aa] > self.order[bb]:
                    aa, bb = bb, aa
                    sign = (-1) ** (a['degree'] * b['degree'])
                factor = 2 if an == bn else 1
                r1, r2 = lw - a['weight'], rw - b['weight']
                coefficient = ac * bc * sign * factor * comb(r1 + r2, r1)
                out[self.index[degree][aa, bb]] += coefficient
        return out

    def differential(self, degree):
        target = self.bases[degree + 1]
        output = [[F(0)] * len(self.bases[degree]) for _ in target]
        for col, (an, bn) in enumerate(self.bases[degree]):
            a, b = self.w.var_by_name[an], self.w.var_by_name[bn]
            weight = a['weight'] + b['weight']
            if an == bn:
                vector = self.product({an: F(1)}, a['weight'], a['d'], a['weight'], degree + 1)
            else:
                first = self.product(a['d'], a['weight'], {bn: F(1)}, b['weight'], degree + 1)
                second = self.product({an: F(1)}, a['weight'], b['d'], b['weight'], degree + 1)
                vector = [x + (-1) ** a['degree'] * y for x, y in zip(first, second)]
            for row, monomial in enumerate(target):
                tw = sum(self.w.var_by_name[name]['weight'] for name in monomial)
                if vector[row]:
                    vector[row] *= comb(self.total - tw, self.total - weight)
                output[row][col] = vector[row]
        return output

    def homology(self, degree):
        dimension = len(self.bases[degree])
        if not dimension:
            return []
        outgoing = self.differentials.get(degree, [])
        _, _, v, rank = smith_dvr(outgoing, dimension)
        incoming = self.differentials.get(degree - 1, [])
        if not incoming or not incoming[0]:
            return ['free'] * (dimension - rank)
        converted = mm(inverse(v), incoming)
        assert not any(x for row in converted[:rank] for x in row)
        relation = converted[rank:]
        _, diagonal, _, r = smith_dvr(relation)
        out = [val2(diagonal[i][i]) for i in range(r) if val2(diagonal[i][i]) > 0]
        out += ['free'] * (dimension - rank - r)
        return out


def serial(obj):
    if isinstance(obj, F):
        return str(obj)
    raise TypeError(type(obj))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-total', type=int, default=7)
    parser.add_argument('--output', default='A_cosimplicial_resolved_arity_probe.json')
    args = parser.parse_args()
    started = time.perf_counter()
    resolution = Resolution(args.max_total - 1)
    w = WComplex(resolution)
    print('resolution ranks', [len(x) for x in resolution.gens], 'W0 generators', len(w.of_degree(0, w.cutoff)), flush=True)
    results = []
    for total in range(2, args.max_total + 1):
        a = ArityTwo(w, total)
        result = {'unshifted_total_weight': total,
                  'dimensions': [len(a.bases[q]) for q in range(7)],
                  'cohomology_2_primary_exponents': {str(q): a.homology(q) for q in (1, 2, 3, 4)},
                  'bases': a.bases, 'lattice_bases': a.lattices,
                  'differential_matrices': a.differentials}
        results.append(result)
        print(total, result['dimensions'], result['cohomology_2_primary_exponents'], flush=True)
    output = {'status': 'completed exact exploratory calculation',
              'scope': 'one simplex, one K2 generator, zero twist, arity two; all computations over Z_(2)',
              'resolution_generators': resolution.gens,
              'resolution_differentials': resolution.new_d,
              'W_rational_generators': w.vars,
              'results': results, 'runtime_seconds': time.perf_counter() - started}
    destination = Path(__file__).resolve().parents[1] / 'logs' / args.output
    destination.write_text(json.dumps(output, default=serial, indent=2) + '\n')
    print('saved', destination.name, 'runtime', output['runtime_seconds'], flush=True)


if __name__ == '__main__':
    main()
