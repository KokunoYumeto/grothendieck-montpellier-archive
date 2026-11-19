"""Exact finite checks for the formal Brauer countermodel.

This checks formal diagram algebras, not Chow cycles of a K3 surface.
The general proof is in part_c/c1_brauer_bv_obstruction.md.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product
from math import factorial
import json
from pathlib import Path


def matchings(vertices):
    vertices = tuple(vertices)
    if not vertices:
        yield ()
        return
    x = vertices[0]
    for y in vertices[1:]:
        rest = tuple(z for z in vertices[1:] if z != y)
        for p in matchings(rest):
            yield tuple(sorted(((x, y),) + p))


def components(size, edges):
    parent = list(range(size))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for x, y in edges:
        x, y = find(x), find(y)
        parent[y] = x
    out = defaultdict(list)
    for x in range(size):
        out[find(x)].append(x)
    return list(out.values())


def compose(a, b, m, delta):
    """Diagram a after b; layers are input, middle, output."""
    edges = list(b) + [(x + m, y + m) for x, y in a]
    pairs, loops = [], 0
    for comp in components(3 * m, edges):
        boundary = [x if x < m else x - m for x in comp if x < m or x >= 2 * m]
        if not boundary:
            loops += 1
        else:
            assert len(boundary) == 2
            pairs.append(tuple(sorted(boundary)))
    return tuple(sorted(pairs)), delta ** loops


def multiply(a, b, m, delta):
    out = defaultdict(Fraction)
    for p, cp in a.items():
        for q, cq in b.items():
            r, scalar = compose(p, q, m, delta)
            out[r] += cp * cq * scalar
    return {p: c for p, c in out.items() if c}


def sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))


def antisymmetrizer(m):
    return {
        tuple(sorted((i, m + p[i]) for i in range(m))): Fraction(sign(p), factorial(m))
        for p in permutations(range(m))
    }


def partial_trace(diagram, m, delta):
    edges = list(diagram) + [(m - 1, 2 * m - 1)]
    retained = list(range(m - 1)) + list(range(m, 2 * m - 1))
    renumber = {v: i for i, v in enumerate(retained)}
    pairs, loops = [], 0
    for comp in components(2 * m, edges):
        boundary = [renumber[x] for x in comp if x in renumber]
        if not boundary:
            loops += 1
        else:
            assert len(boundary) == 2
            pairs.append(tuple(sorted(boundary)))
    return tuple(sorted(pairs)), delta ** loops


def trace_linear(element, m, delta):
    out = defaultdict(Fraction)
    for p, c in element.items():
        q, s = partial_trace(p, m, delta)
        out[q] += c * s
    return {p: c for p, c in out.items() if c}


checks = []
for m in (2, 3, 4):
    delta = m - 1
    a = antisymmetrizer(m)
    identity = tuple((i, m + i) for i in range(m))
    assert a[identity] == Fraction(1, factorial(m)) != 0
    assert multiply(a, a, m, delta) == a
    assert trace_linear(a, m, delta) == {}
    for test_delta in (0, 1, 2, 3, 5):
        expected = {
            p: c * Fraction(test_delta - m + 1, m)
            for p, c in antisymmetrizer(m - 1).items()
            if c * Fraction(test_delta - m + 1, m)
        }
        assert trace_linear(a, m, test_delta) == expected
    checks.append({
        "m": m, "delta": delta, "nonzero_terms": len(a),
        "identity_coefficient": str(a[identity]), "idempotent": True,
        "partial_trace_zero_at_delta_m_minus_1": True,
        "partial_trace_formula_test_parameters": [0, 1, 2, 3, 5],
    })

# Entire small Brauer algebra: associativity, including cups/caps and loops.
m, delta = 3, 2
basis = list(matchings(range(2 * m)))
associativity_count = 0
for a, b, c in product(basis, repeat=3):
    ab, sab = compose(a, b, m, delta)
    left, sl = compose(ab, c, m, delta)
    bc, sbc = compose(b, c, m, delta)
    right, sr = compose(a, bc, m, delta)
    assert left == right and sab * sl == sbc * sr
    associativity_count += 1

# The BV expression has three unit/point terms and three paired-W terms.
# Delta_ij o_k contains each unit/point term twice; subtraction leaves once.
small = defaultdict(int)
for pair in ((0, 1), (0, 2), (1, 2)):
    k = next(x for x in range(3) if x not in pair)
    i, j = pair
    small[("unit", i)] += 1
    small[("unit", j)] += 1
    small[("paired_W", pair)] += 1
    small[("unit", k)] -= 1
expected = {("unit", i): 1 for i in range(3)}
expected.update({("paired_W", p): 1 for p in ((0, 1), (0, 2), (1, 2))})
assert dict(small) == expected

result = {
    "scope": "Formal rational Brauer-category countermodel only; no geometric K3 counterexample.",
    "antisymmetrizer_checks": checks,
    "brauer_B3_parameter_2_basis_size": len(basis),
    "complete_associativity_checks": associativity_count,
    "BV_small_diagonal_component_identity": True,
    "general_parameter": "d=22 gives the formal K3 Frobenius data and a nonzero a_23; nonvanishing is proved by its identity-diagram coefficient 1/23!, not enumerated.",
}
out = Path(__file__).with_name("check_brauer_bv_obstruction_output.json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
