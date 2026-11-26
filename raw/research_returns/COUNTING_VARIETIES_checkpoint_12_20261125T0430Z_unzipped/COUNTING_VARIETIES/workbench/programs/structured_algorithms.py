#!/usr/bin/env python3
"""Exact independent checks for the structured-count algorithms.

Run from the deliverable directory:
    python3 workbench/programs/structured_algorithms.py

This original standard-library program imports only our structured_verify.py.
Small exhaustive tests supplement proofs; they do not prove asymptotic claims.
"""
from itertools import product, combinations
from fractions import Fraction
from random import Random
import json
from structured_verify import FiniteField, rref


def parity(x):
    return x.bit_count() & 1


def walsh_add(a, b, p=3):
    out = dict(a)
    for m, c in b.items():
        out[m] = (out.get(m, 0) + c) % p
    return {m: c for m, c in out.items() if c}


def walsh_mul(a, b, p=3):
    out = {}
    for m, c in a.items():
        for n, d in b.items():
            out[m ^ n] = (out.get(m ^ n, 0) + c*d) % p
    return {m: c for m, c in out.items() if c}


def value(f, x, p=3):
    return sum(c * (-1 if parity(m & x) else 1)
               for m, c in f.items()) % p


def transform(values, n, p=3):
    factor = pow(2**n, -1, p)
    return {m: c for m in range(1 << n)
            if (c := factor*sum(v*(-1 if parity(m & x) else 1)
                                for x, v in enumerate(values)) % p)}


def restrict_bit(f, bit, setting, p=3):
    out = {}
    for m, c in f.items():
        n = m & ~(1 << bit)
        if setting and (m >> bit & 1):
            c = -c
        out[n] = (out.get(n, 0) + c) % p
    return {m: c for m, c in out.items() if c}


def witness(f, n):
    if not f:
        return None
    x = 0
    for bit in range(n):
        zero = restrict_bit(f, bit, 0)
        if zero:
            f = zero
        else:
            x |= 1 << bit
            f = restrict_bit(f, bit, 1)
            assert f
    return x


def reversible_registers():
    rng = Random(14207)
    programs = words = residues = 0
    for m in range(1, 19):
        n = 5
        for trial in range(4):
            stages = []
            f = {0: trial % 3} if trial % 3 else {}
            initial = trial % 3
            for _ in range(m):
                mask, bias = rng.randrange(1 << n), rng.randrange(2)
                s0, s1 = rng.choice((1, 2)), rng.choice((1, 2))
                c0, c1 = rng.randrange(3), rng.randrange(3)
                stages.append((mask, bias, s0, s1, c0, c1))
                # An affine bit b has (-1)^b=(-1)^bias chi_mask.
                sign = -1 if bias else 1
                slope = walsh_add({0: (s0+s1)*2 % 3},
                                  {mask: (s0-s1)*2*sign % 3})
                shift = walsh_add({0: (c0+c1)*2 % 3},
                                  {mask: (c0-c1)*2*sign % 3})
                f = walsh_add(walsh_mul(slope, f), shift)
            assert len(set(f) | {0}) <= m+1
            direct = []
            for x in range(1 << n):
                z = initial
                for mask, bias, s0, s1, c0, c1 in stages:
                    b = parity(mask & x) ^ bias
                    z = ((s1 if b else s0)*z + (c1 if b else c0)) % 3
                assert value(f, x) == z
                direct.append(z)
                words += 1
            for accepted in range(8):
                hv = [(accepted >> z) & 1 for z in range(3)]
                # h(z)=A+Bz+Cz^2 by direct interpolation over F_3.
                a = hv[0]
                b = (hv[1]-hv[2])*2 % 3
                c = ((hv[1]+hv[2])*2-a) % 3
                indicator = walsh_add({0: a},
                            walsh_add({i: b*v % 3 for i, v in f.items()},
                                      {i: c*v % 3 for i, v in walsh_mul(f, f).items()}))
                expected = [hv[z] for z in direct]
                assert [value(indicator, x) for x in range(1 << n)] == expected
                assert 2**n*indicator.get(0, 0) % 3 == sum(expected) % 3
                w = witness(indicator, n)
                assert (w is None) == (sum(expected) == 0)
                if w is not None:
                    assert expected[w]
                if sum(expected) and sum(expected) % 3 == 0:
                    residues += 1
            programs += 1
    return {'programs': programs, 'direct_word_checks': words,
            'nonempty_acceptance_sets_of_zero_residue': residues}


def solve_binary(equations, variables):
    pivots = {}
    for row, rhs in equations:
        word = row | (rhs << variables)
        while word & ((1 << variables)-1):
            pivot = (word & -word).bit_length()-1
            if pivot in pivots:
                word ^= pivots[pivot]
            else:
                pivots[pivot] = word
                break
        else:
            if word >> variables:
                return None
    solution = 0
    for pivot in sorted(pivots, reverse=True):
        word = pivots[pivot]
        if (word >> variables) ^ parity(word & solution):
            solution |= 1 << pivot
    return solution


def selector(syndromes, g, degree):
    masks = [m for m in range(1 << g) if m.bit_count() <= degree]
    rows = []
    for y in set(syndromes) | {0}:
        rows.append((sum(1 << j for j, m in enumerate(masks) if m & y == m),
                     int(y == 0)))
    answer = solve_binary(rows, len(masks))
    return None if answer is None else [m for j, m in enumerate(masks) if answer >> j & 1]


def affine(form, word):
    return parity(form[0] & word) ^ form[1]


def gate_defect(gate, word):
    a, b, c = [affine(form, word) for form in gate]
    return c ^ (a & b)


def partition(words, gates):
    """Exhaustive small-domain version of the affine slicing certificate."""
    if not words:
        return []
    for gate in gates:
        a, b, c = gate
        for eps in (0, 1):
            cells = {}
            for w in words:
                key = (affine(a, w), affine(c, w) ^ (eps & affine(b, w)))
                cells.setdefault(key, []).append(w)
            forbidden = cells.get((eps, 1), [])
            if not forbidden:
                continue
            if len(forbidden) == len(words):
                return []
            out = []
            for key, cell in cells.items():
                if key != (eps, 1):
                    out += partition(cell, gates)
            return out
    return [words]


def grouped_gates():
    rng = Random(230912)
    cases = found = 0
    for trial in range(60):
        n, g, block = 5, 3, 1+trial % 2
        gates = [tuple((rng.randrange(1 << n), rng.randrange(2)) for _ in range(3))
                 for _ in range(g*block)]
        syndromes = []
        for x in range(1 << n):
            syndromes.append(sum(int(any(gate_defect(h, x) for h in
                                         gates[i*block:(i+1)*block])) << i
                                 for i in range(g)))
        for degree in (1, 2):
            h = selector(syndromes, g, degree)
            if h is not None:
                for y in syndromes:
                    assert sum((m & y) == m for m in h) % 2 == int(y == 0)
                leaves = partition(list(range(1 << n)), gates)
                covered = [x for leaf in leaves for x in leaf]
                assert len(set(covered)) == len(covered) == syndromes.count(0)
                assert set(covered) == {x for x, y in enumerate(syndromes) if y == 0}
                assert len(leaves) <= 3**(2*block*degree)
                found += 1
            cases += 1
    chains = []
    for g in range(1, 7):
        syndromes = list(range(1 << g))
        assert selector(syndromes, g, g-1) is None
        assert selector(syndromes, g, g) is not None
        chains.append(g)
    return {'selector_problems': cases, 'verified_affine_partitions': found,
            'chain_minimum_degrees': chains}


def rational_solve(matrix, vector):
    n = len(vector)
    a = [[Fraction(x) for x in row]+[Fraction(y)] for row, y in zip(matrix, vector)]
    pivots, r = [], 0
    for j in range(n):
        k = next((i for i in range(r, n) if a[i][j]), None)
        if k is None:
            continue
        a[r], a[k] = a[k], a[r]
        scale = a[r][j]
        a[r] = [x/scale for x in a[r]]
        for i in range(n):
            if i != r:
                scale = a[i][j]
                a[i] = [x-scale*y for x, y in zip(a[i], a[r])]
        pivots.append(j)
        r += 1
    assert all(any(row[:n]) or not row[n] for row in a)
    answer = [Fraction(0)]*n
    for i, j in enumerate(pivots):
        answer[j] = a[i][-1]
    return answer


def moment_windows():
    rng = Random(92101)
    for trial in range(60):
        g = 4
        population = [rng.randrange(7) for _ in range(1 << g)]
        bounds = []
        for upper in (False, True):
            weights = [Fraction(1)-Fraction(y.bit_count(), g if upper else 1)
                       for y in range(1 << g)]
            matrix = [[sum(population[y]*weights[y] for y in range(1 << g)
                           if y >> i & 1 and y >> j & 1) for j in range(g)] for i in range(g)]
            vector = [-sum(population[y]*weights[y] for y in range(1 << g) if y >> i & 1)
                      for i in range(g)]
            h = rational_solve(matrix, vector)
            opt = sum(population[y]*weights[y]*(1+sum(h[i] for i in range(g) if y >> i & 1))**2
                      for y in range(1 << g))
            bounds.append(opt)
        assert bounds[0] <= population[0] <= bounds[1]
    for degree in (1, 2, 3):
        g = 2*degree+2
        for mask in range((1 << g)-1):
            totals = [sum(1 for y in range(1 << g) if parity(y) == b and y & mask == mask)
                      for b in (0, 1)]
            assert totals[0] == totals[1]
    return {'rational_windows': 60, 'indistinguishable_parity_dimensions': [4, 6, 8]}


def specialize_private(f, n, z):
    out = {}
    for mask, c in f.items():
        a, b = mask & ((1 << n)-1), mask >> n
        out[a] = (out.get(a, 0) + c*(-1 if parity(b & z) else 1)) % 3
    return {m: c for m, c in out.items() if c}


def trace_and_cap():
    rng = Random(90518)
    n, t, cap = 3, 3, 2
    detectors = bounded = 0
    for trial in range(40):
        table = [0]*(1 << (n+t))
        for x in range(1 << n):
            allowed = rng.sample(range(1 << t), rng.randrange(cap+1 if trial < 20 else 9))
            for z in allowed:
                table[x+(z << n)] = rng.choice((1, 2))
        f = transform(table, n+t)
        population = [sum(table[x+(z << n)] != 0 for z in range(1 << t)) for x in range(1 << n)]
        rows = {}
        for mask, c in f.items():
            rows.setdefault(mask >> n, {})[mask & ((1 << n)-1)] = c
        trace = {}
        for row in rows.values():
            trace = walsh_add(trace, {m: 2**t*c % 3 for m, c in walsh_mul(row, row).items()})
        defect = walsh_mul(f, walsh_add({0: 1}, {m: -c % 3 for m, c in walsh_mul(trace, trace).items()}))
        detects = all(h == 0 or h % 3 for h in population)
        assert (not defect) == detects
        detectors += detects
        fibre_functions = [specialize_private(f, n, z) for z in range(1 << t)]
        certificates = []
        for subset in combinations(fibre_functions, cap+1):
            term = {0: 1}
            for row in subset:
                term = walsh_mul(term, row)
            certificates.append(term)
        is_bounded = max(population) <= cap
        assert all(not c for c in certificates) == is_bounded
        if is_bounded:
            empty = {0: 1}
            for j in range(1, cap+1):
                for subset in combinations(fibre_functions, j):
                    term = {0: (-1)**j % 3}
                    for row in subset:
                        term = walsh_mul(term, walsh_mul(row, row))
                    empty = walsh_add(empty, term)
            assert [value(empty, x) for x in range(1 << n)] == [int(h == 0) for h in population]
            bounded += 1
    return {'families': 40, 'trace_detecting_families': detectors,
            'cap_two_families_and_empty_indicators': bounded}


def exact_register_reduction():
    results = []
    for pin in (0, 1):
        n = 5  # a,b,z,s,t
        forms = [([1, 1, -2, -1, 0], 0), ([0, 0, 1, 1, 1], -1),
                 ([0, 0, 1, 0, 0], -pin)]
        k = n//2+1
        base, count, population = 4**k, 0, 0
        for bits in product((0, 1), repeat=n):
            vals = [(sum(a*b for a, b in zip(coeff, bits))+constant) % 3
                    for coeff, constant in forms]
            count += all(v == 0 for v in vals)
            distribution = [1, 0, 0]
            for v in vals:
                for _ in range(k):
                    for h in (1, 2):
                        new = [0, 0, 0]
                        for residue, ways in enumerate(distribution):
                            new[residue] += ways
                            new[(residue+h*v) % 3] += ways
                        distribution = new
            assert distribution[1] == distribution[2]
            population += distribution[0]
        total = 2**(n+2*k*len(forms))
        decoded = (3*population-total)//(2*base**len(forms))
        assert decoded == count == (3 if pin == 0 else 1)
        results.append({'AND_output': pin, 'count': count, 'register_population': population,
                        'metric_decoding': decoded})
    return results


def arrangement_polynomial(k, forms, n):
    coefficients = [0]*(n+1)
    for mask in range(1 << len(forms)):
        rows = [list(a)+[k.sub(0, c)] for i, (a, c) in enumerate(forms) if mask >> i & 1]
        reduced, pivots = rref(rows, k)
        if n in pivots:
            continue
        coefficients[n-len(pivots)] += (-1)**mask.bit_count()
    return coefficients


def arrangements():
    records = []
    for p, d in ((3, 1), (2, 2)):
        k = FiniteField(p, d)
        eta = next(x for x in range(k.q) if x not in (0, 1))
        forms = []
        for variable in range(3):
            for c in range(k.q):
                if c not in (0, 1):
                    a = [0, 0, 0]
                    a[variable] = 1
                    forms.append((a, k.sub(0, c)))
        forms += [([0, 1, eta], k.sub(0, 1)),
                  ([1, k.sub(0, eta), 1], k.sub(0, 1)), ([0, 0, 1], 0)]
        coefficients = arrangement_polynomial(k, forms, 3)
        expected = [-12, 14, -6, 1] if k.q == 3 else [-37, 30, -9, 1]
        assert coefficients == expected
        count = 0
        for word in product(range(k.q), repeat=3):
            okay = True
            for a, c in forms:
                v = c
                for x, y in zip(a, word):
                    v = k.add(v, k.mul(x, y))
                okay &= bool(v)
            count += okay
        assert count == sum(c*k.q**i for i, c in enumerate(coefficients)) == 3
        records.append({'q': k.q, 'coefficients_constant_first': coefficients, 'points': count,
                        'quadratic_extension_points': sum(c*k.q**(2*i) for i, c in enumerate(coefficients))})
    assert records[1]['quadratic_extension_points'] == 2235
    return records


def main():
    print(json.dumps({'grouped_gates': grouped_gates(), 'moment_windows': moment_windows(),
          'reversible_registers': reversible_registers(), 'trace_and_cap': trace_and_cap(),
          'exact_count_metric_reduction': exact_register_reduction(),
          'arrangement_inclusion_exclusion': arrangements()}, indent=2))


if __name__ == '__main__':
    main()
