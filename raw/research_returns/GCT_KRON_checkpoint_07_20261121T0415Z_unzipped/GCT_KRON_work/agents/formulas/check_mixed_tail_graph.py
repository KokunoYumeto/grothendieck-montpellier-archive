"""Exact supplementary certificates for the mixed graph in F-017.

The proof is the saved all-parameter cycle argument. These checks target
overlapping suffix labels, coefficient-edge variable absorption, and S<m.
"""
from datetime import datetime, timezone
from itertools import product
from math import comb
from pathlib import Path
import json
import sympy as sp


def indices(number, degree):
    return [a for a in product(range(degree + 1), repeat=number)
            if sum(a) <= degree]


def monomial(variables, exponent):
    return sp.prod(x ** a for x, a in zip(variables, exponent))


def construct(m, p, q, R, u, v, L, variables, coefficients):
    s = u + v + 1
    left = [(a, g) for a in indices(p, m) for g in indices(R, u)]
    right = [(a, g) for a in indices(q, m) for g in indices(R, v)]
    root_left, root_right = ((0,) * p, (0,) * R), ((0,) * q, (0,) * R)
    ids = {('L', root_left): 0, ('R', root_right): 0}
    for side, vertices, root in [('L', left, root_left), ('R', right, root_right)]:
        for vertex in vertices:
            if vertex != root:
                ids[(side, vertex)] = len(set(ids.values()))
    size = len(left) + len(right) - 1
    matrix = sp.zeros(size)
    for j in range(1, size):
        matrix[j, j] = L
    z, y = variables[:p + q], variables[p + q:]
    for side, vertices, root, own_z in [
            ('L', left, root_left, z[:p]), ('R', right, root_right, z[p:])]:
        local_variables = own_z + y
        number_early = len(own_z)
        for vertex in vertices:
            if vertex == root:
                continue
            exponent = vertex[0] + vertex[1]
            last = max(j for j, a in enumerate(exponent) if a)
            parent = list(exponent)
            parent[last] -= 1
            parent = (tuple(parent[:number_early]), tuple(parent[number_early:]))
            a, b = ids[(side, parent)], ids[(side, vertex)]
            if side == 'R':
                a, b = b, a
            matrix[a, b] += -local_variables[last]
    expected = 0
    for (alpha, gamma), coefficient in coefficients.items():
        assert sum(alpha) + sum(gamma) <= m and sum(gamma) <= s
        remainder = list(gamma)
        if any(gamma):
            j = next(i for i, value in enumerate(gamma) if value)
            remainder[j] -= 1
            edge = coefficient * y[j]
        else:
            edge = coefficient * L
        ga = [0] * R
        allowance = u
        for j, value in enumerate(remainder):
            ga[j] = min(value, allowance)
            allowance -= ga[j]
        gb = [value - a for value, a in zip(remainder, ga)]
        assert sum(ga) <= u and sum(gb) <= v
        origin = (alpha[:p], tuple(ga))
        target = (alpha[p:], tuple(gb))
        matrix[ids[('L', origin)], ids[('R', target)]] += edge
        degree = sum(alpha) + sum(gamma)
        assert size >= degree
        expected += coefficient * monomial(z, alpha) * monomial(y, gamma) * L ** (size - degree)
    assert size == comb(m + p, p) * comb(R + u, u) + comb(m + q, q) * comb(R + v, v) - 1
    return matrix, sp.expand(expected)


def support(m, p, q, R, u, v):
    return [(a, g) for a in indices(p + q, m)
            for g in indices(R, u + v + 1) if sum(a) + sum(g) <= m]


symbolic = []
for parameters in [(3, 1, 0, 1, 0, 1), (2, 1, 1, 1, 0, 0), (5, 0, 0, 2, 0, 0)]:
    m, p, q, R, u, v = parameters
    L = sp.Symbol('L')
    variables = sp.symbols(f'x0:{p + q + R}')
    terms = support(*parameters)
    coefficients = dict(zip(terms, sp.symbols(f'c0:{len(terms)}')))
    matrix, expected = construct(*parameters, L, variables, coefficients)
    residual = sp.expand(matrix.det() - expected)
    assert residual == 0
    symbolic.append({'parameters_m_p_q_R_u_v': parameters,
                     'size': matrix.rows, 'coefficients': len(terms), 'residual': str(residual)})

integer = []
for parameters in [(4, 1, 1, 2, 1, 1), (5, 1, 0, 3, 1, 2), (7, 0, 0, 2, 1, 1)]:
    m, p, q, R, u, v = parameters
    terms = support(*parameters)
    coefficients = {term: (11 * j + 3) % 23 - 11 for j, term in enumerate(terms)}
    variables = tuple((j + 1) * (-1 if j % 2 else 1) for j in range(p + q + R))
    for L in (0, 1, -2):
        matrix, expected = construct(*parameters, L, variables, coefficients)
        determinant = matrix.det(method='domain-ge')
        assert determinant == expected
        integer.append({'parameters_m_p_q_R_u_v': parameters, 'size': matrix.rows,
                        'L': L, 'determinant': str(determinant)})

ratios = []
for u in range(13):
    a = 25 - 2 * u
    ratio = sp.Rational(comb(a + 2, 2), 2 ** a) * sp.Rational(u + 1, 2 ** u)
    assert ratio <= sp.Rational(55, 512)
    ratios.append({'u': u, 'a': a, 'exact_ratio': str(ratio)})

result = {'finding': 'F-017', 'date_utc': datetime.now(timezone.utc).isoformat(),
          'model': 'GPT-6 Astra Pro', 'effort': 'not exposed', 'run': 'GCT_KRON_20261120',
          'symbolic_identities': symbolic, 'integer_identities': integer,
          'BIP_budget_ratios': ratios, 'status': 'PASS'}
destination = Path(__file__).with_name('mixed_tail_graph_certificate.json')
destination.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'symbolic_identities': len(symbolic),
                  'integer_identities': len(integer), 'BIP_ratios': len(ratios),
                  'certificate': str(destination)}))
