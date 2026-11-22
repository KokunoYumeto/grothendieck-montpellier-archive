"""Exact finite certificates for D:uniform-H1-obstruction.

We verify the explicit alternating-group generators in degrees 5--8 and
compute H^1 for A5 on its four-dimensional deleted permutation module over
F2, and for A5 x A5 on the outer tensor square.  The infinite-product and
all-module assertions are proved separately in the manuscript.
"""
from collections import deque
from itertools import permutations
from math import factorial
from pathlib import Path
from time import perf_counter
import json

started = perf_counter()
checks = 0


def check(condition):
    global checks
    checks += 1
    assert condition


def compose(g, h):
    return tuple(g[h[i]] for i in range(len(g)))


def cycle(n, entries):
    result = list(range(n))
    for a, b in zip(entries, entries[1:] + entries[:1]):
        result[a] = b
    return tuple(result)


def closure(identity, generators, multiply):
    seen = {identity}
    queue = deque([identity])
    while queue:
        h = queue.popleft()
        for g in generators:
            gh = multiply(g, h)
            if gh not in seen:
                seen.add(gh)
                queue.append(gh)
    return seen


generator_results = []
for n in range(5, 9):
    a = cycle(n, list(range(n)) if n % 2 else list(range(1, n)))
    b = cycle(n, [0, 1, 2])
    generated = closure(tuple(range(n)), (a, b), compose)
    check(len(generated) == factorial(n) // 2)
    for g in generated:
        check(sum(g[i] > g[j] for i in range(n)
                  for j in range(i + 1, n)) % 2 == 0)
    generator_results.append({"degree": n, "order": len(generated),
                              "generator_a": a, "generator_b": b})


def xor_all(values):
    result = 0
    for x in values:
        result ^= x
    return result


def bit_indices(x):
    while x:
        bit = x & -x
        yield bit.bit_length() - 1
        x ^= bit


def gf2_rank(rows):
    pivots = {}
    for row in rows:
        while row:
            leading = row.bit_length() - 1
            if leading not in pivots:
                pivots[leading] = row
                break
            row ^= pivots[leading]
    return len(pivots)


identity5 = tuple(range(5))
a5 = cycle(5, list(range(5)))
b5 = cycle(5, [0, 1, 2])
A5 = sorted(closure(identity5, (a5, b5), compose))
check(len(A5) == 60)


def deleted_action(g, v):
    # Basis e_i+e_4 for i=0,...,3 of sum-zero vectors in F2^5.
    v5 = v | ((v.bit_count() % 2) << 4)
    result = xor_all(1 << g[i] for i in bit_indices(v5))
    check(result.bit_count() % 2 == 0)
    return result & 15


action = {g: tuple(deleted_action(g, 1 << j) for j in range(4)) for g in A5}


def act(columns, v):
    return xor_all(columns[j] for j in bit_indices(v))


for g in A5:
    for h in A5:
        for j in range(4):
            check(act(action[g], action[h][j]) == action[compose(g, h)][j])

# Each nonzero vector generates the entire four-dimensional module.
for v in range(1, 16):
    check(gf2_rank(act(action[g], v) for g in A5) == 4)


def cayley_cohomology(identity, generators, multiply, columns, dimension,
                     expected_order):
    """Exact cocycles using all directed generator edges in the Cayley graph.

The unknowns are values on the generators.  A spanning tree expresses every
other value in these unknowns.  Every remaining edge imposes its cocycle
identity.  Thus the computed kernel is exactly Z^1, with no presentation
assumption.  All arithmetic is bitwise Gaussian elimination over F2.
"""
    d = dimension
    seeds = [tuple(1 << (i * d + j) for j in range(d))
             for i in range(len(generators))]
    row_supports = [[tuple(j for j in range(d) if matrix[j] >> k & 1)
                     for k in range(d)] for matrix in columns]
    values = {identity: (0,) * d}
    queue = deque([identity])
    equations = []
    edges = 0
    while queue:
        h = queue.popleft()
        for i, g in enumerate(generators):
            gh = multiply(g, h)
            candidate = tuple(seeds[i][k] ^ xor_all(values[h][j]
                              for j in row_supports[i][k]) for k in range(d))
            if gh not in values:
                values[gh] = candidate
                queue.append(gh)
            else:
                equations.extend(candidate[k] ^ values[gh][k] for k in range(d))
            edges += 1
    check(len(values) == expected_order)
    rank = gf2_rank(equations)
    z1 = len(generators) * d - rank
    # A coboundary has generator values (g-1)v.
    b1_columns = [xor_all((columns[i][j] ^ (1 << j)) << (i * d)
                          for i in range(len(generators))) for j in range(d)]
    b1 = gf2_rank(b1_columns)
    for equation in equations:
        for coboundary in b1_columns:
            check((equation & coboundary).bit_count() % 2 == 0)
    check(z1 >= b1)
    check(z1 - b1 <= d)
    return {"group_order": expected_order, "module_dimension": d,
            "generators": len(generators), "directed_edges": edges,
            "linear_constraints": len(equations), "constraint_rank": rank,
            "Z1_dimension": z1, "B1_dimension": b1,
            "H1_dimension": z1 - b1, "invariant_dimension": d - b1}


single = cayley_cohomology(identity5, (a5, b5), compose,
                          (action[a5], action[b5]), 4, 60)
check(single["H1_dimension"] == 0)

# Independent full bar-cocycle matrix for the A5 calculation.
index = {g: i for i, g in enumerate(A5)}
bar_rows = []
for g in A5:
    for h in A5:
        gh = compose(g, h)
        for k in range(4):
            row = (1 << (4 * index[gh] + k)) ^ (1 << (4 * index[g] + k))
            for j in range(4):
                if action[g][j] >> k & 1:
                    row ^= 1 << (4 * index[h] + j)
            bar_rows.append(row)
bar_z1 = 240 - gf2_rank(bar_rows)
check(bar_z1 == single["Z1_dimension"])


def pair_multiply(g, h):
    return compose(g[0], h[0]), compose(g[1], h[1])


def tensor_columns(g, h):
    result = []
    for i in range(4):
        for j in range(4):
            result.append(xor_all(1 << (4 * r + s)
                                  for r in bit_indices(action[g][i])
                                  for s in bit_indices(action[h][j])))
    return tuple(result)


pair_generators = ((a5, identity5), (b5, identity5),
                   (identity5, a5), (identity5, b5))
tensor = cayley_cohomology((identity5, identity5), pair_generators,
                          pair_multiply,
                          tuple(tensor_columns(g, h) for g, h in pair_generators),
                          16, 3600)
check(tensor["H1_dimension"] == 0)
check(tensor["invariant_dimension"] == 0)

output = {
    "purpose": "Finite auxiliary checks only; the all-module infinite-product claim is proved in the manuscript",
    "alternating_group_generators": generator_results,
    "A5_deleted_module_irreducible": True,
    "A5_deleted_module_H1": single,
    "independent_A5_bar_equations": len(bar_rows),
    "independent_A5_bar_Z1_dimension": bar_z1,
    "A5_squared_outer_tensor_H1": tensor,
    "assertions_passed": checks,
    "elapsed_seconds": perf_counter() - started,
}
destination = Path(__file__).with_name("check_uniform_h1_obstruction_output.json")
destination.write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps(output, indent=2))
