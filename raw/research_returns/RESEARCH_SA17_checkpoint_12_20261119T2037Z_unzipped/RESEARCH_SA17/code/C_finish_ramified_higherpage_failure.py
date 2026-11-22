#!/usr/bin/env python3
"""Finite refutation of a proposed second-pi-page parity invariant.

This does not refute the C.1 question or any released theorem.  It tests the
unproved proposal that the translation-stable primary parity of the second
pi-Bockstein page is additive for all admissible involution extensions.

The exact ring is S = Z[pi]/(pi^2-2, pi^3), of order eight.  An element is
(a mod 4, b mod 2), representing a+b*pi.  All computations are exhaustive
integer or F_2 operations; no floating-point arithmetic or random search.
"""
from itertools import product
from pathlib import Path
import json
import time


ZERO = (0, 0)
ONE = (1, 0)
PI = (0, 1)
TWO = (2, 0)
ELEMENTS = tuple(product(range(4), range(2)))


def add(x, y):
    return ((x[0] + y[0]) % 4, (x[1] + y[1]) % 2)


def neg(x):
    return ((-x[0]) % 4, x[1])


def mul(x, y):
    return ((x[0] * y[0] + 2 * x[1] * y[1]) % 4,
            (x[0] * y[1] + x[1] * y[0]) % 2)


def residue(x):
    return x[0] % 2


def ident(n, zero=ZERO, one=ONE):
    return [[one if i == j else zero for j in range(n)] for i in range(n)]


def mm(a, b):
    c = [[ZERO for _ in range(len(b[0]))] for _ in a]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] = add(c[i][j], mul(a[i][k], b[k][j]))
    return c


def gf_rank(a):
    a = [list(row) for row in a]
    if not a:
        return 0
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def gf_mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % 2
             for j in range(len(b[0]))] for i in range(len(a))]


def gf_add(*matrices):
    return [[sum(a[i][j] for a in matrices) % 2
             for j in range(len(matrices[0][0]))]
            for i in range(len(matrices[0]))]


def gf_power(a, e):
    v = ident(len(a), 0, 1)
    for _ in range(e):
        v = gf_mm(v, a)
    return v


def f_primary_length(n_matrix):
    """f=z^2+z+1; ker f(N)^n is the full f-primary subspace."""
    n = len(n_matrix)
    f = gf_add(gf_mm(n_matrix, n_matrix), n_matrix, ident(n, 0, 1))
    dimension = n - gf_rank(gf_power(f, n))
    assert dimension % 2 == 0
    return dimension // 2


def build_extension(n_matrix):
    n = len(n_matrix)
    t = ident(n)
    for i in range(n):
        for j in range(n):
            t[i][j] = add(t[i][j], (2 * n_matrix[i][j], 0))
    e = ident(2 * n)
    for i in range(n):
        for j in range(n):
            e[i][j] = t[i][j]
            e[i][n + j] = PI if i == j else ZERO
    return t, e


def first_normalized_pi(t):
    # If T-I is in pi*S, its quotient by pi has residue equal to the
    # pi coefficient of T-I.  The ambiguity Ann(pi)=(pi^2) has zero residue.
    for i in range(len(t)):
        for j in range(len(t)):
            difference = add(t[i][j], neg(ONE if i == j else ZERO))
            assert residue(difference) == 0
    return [[entry[1] for entry in row] for row in t]


def second_operator_when_first_zero(t):
    result = []
    for i, row in enumerate(t):
        out = []
        for j, entry in enumerate(row):
            difference = add(entry, neg(ONE if i == j else ZERO))
            assert difference[1] == 0 and difference[0] % 2 == 0
            out.append((difference[0] // 2) % 2)
        result.append(out)
    return result


def run():
    start = time.perf_counter()
    assert mul(PI, PI) == TWO and mul(TWO, PI) == ZERO
    assert add(TWO, TWO) == ZERO and TWO != ZERO
    triples = 0
    for x, y, z in product(ELEMENTS, repeat=3):
        assert mul(mul(x, y), z) == mul(x, mul(y, z))
        assert mul(x, add(y, z)) == add(mul(x, y), mul(x, z))
        triples += 1
    assert {x for x in ELEMENTS if mul(TWO, x) == ZERO} == {
        x for x in ELEMENTS if residue(x) == 0}
    assert len({mul(TWO, x) for x in ELEMENTS}) == 2
    # Hence Ann(2) has four elements but (2) only two: ordinary mod4
    # division-by-two Bockstein hypotheses explicitly fail.

    # f has no root in F2 and f(z+1)=f(z), checked coefficientwise.
    assert all((z * z + z + 1) % 2 == 1 for z in (0, 1))
    translated_coefficients = [(1 + 1 + 1) % 2, (2 + 1) % 2, 1]
    assert translated_coefficients == [1, 1, 1]

    cases = []
    for n in (1, 2, 3):
        total = failure = 0
        for values in product((0, 1), repeat=n * n):
            n_matrix = [list(values[i * n:(i + 1) * n]) for i in range(n)]
            t, e = build_extension(n_matrix)
            assert mm(t, t) == ident(n)
            assert mm(e, e) == ident(2 * n)
            inclusion = [[ONE if i == j else ZERO for j in range(n)]
                         for i in range(2 * n)]
            projection = [[ONE if j == n + i else ZERO
                           for j in range(2 * n)] for i in range(n)]
            assert mm(e, inclusion) == mm(inclusion, t)
            assert mm(projection, e) == projection

            d_end = first_normalized_pi(t)
            d_middle = first_normalized_pi(e)
            assert gf_rank(d_end) == 0
            assert gf_mm(d_middle, d_middle) == [[0] * (2 * n) for _ in range(2 * n)]
            assert gf_rank(d_middle) == n
            assert 2 * n - 2 * gf_rank(d_middle) == 0
            assert second_operator_when_first_zero(t) == n_matrix

            endpoint_chi = f_primary_length(n_matrix) % 2
            # The other endpoint has second operator0; the middle's next
            # page is0 because its first normalized differential is acyclic.
            assert f_primary_length([[0] * n for _ in range(n)]) == 0
            total += 1
            failure += endpoint_chi
        cases.append({'endpoint_rank': n, 'exact_extensions': total,
                      'nonadditive_primary_parity_cases': failure,
                      'middle_second_page_dimension': 0})

    witness = [[0, 1], [1, 1]]
    t, e = build_extension(witness)
    assert gf_add(gf_mm(witness, witness), witness, ident(2, 0, 1)) == [[0, 0], [0, 0]]
    assert f_primary_length(witness) == 1
    return {
        'status': 'PASS: proposed second-pi-page primary parity is not additive',
        'refuted_proposal': 'Additivity on every admissible involution extension of translation-stable primary parity of the second pi-Bockstein page.',
        'not_refuted': 'The original C.1 question, nonvanishing for the e=2,n=3 node, and all released manuscript theorems.',
        'ring': 'Z[pi]/(pi^2-2, pi^3), eight elements (a mod4,b mod2)',
        'residue_field': 'F2, the smallest possible residue field',
        'ring_identity_triples': triples,
        'primary_polynomial': 'z^2+z+1, irreducible over F2 and translation invariant',
        'witness_second_operator': witness,
        'witness_endpoint_T': t,
        'witness_middle_E': e,
        'witness_parities': {'submodule': 1, 'quotient': 0, 'middle': 0},
        'families': cases,
        'total_exact_extensions': sum(c['exact_extensions'] for c in cases),
        'total_nonadditivity_witnesses': sum(c['nonadditive_primary_parity_cases'] for c in cases),
        'scope': 'Exact finite ring identities, involutions and split underlying extensions; first normalized pi differentials and endpoint second operators in this explicit family. No general higher Bockstein construction or node-class vanishing/nonvanishing theorem is asserted.',
        'runtime_seconds': time.perf_counter() - start,
    }


if __name__ == '__main__':
    output = run()
    path = Path(__file__).resolve().parents[1] / 'logs/C_finish_ramified_higherpage_failure.json'
    path.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps({key: output[key] for key in
                      ('status', 'ring_identity_triples', 'total_exact_extensions',
                       'total_nonadditivity_witnesses', 'runtime_seconds')}, indent=2))
