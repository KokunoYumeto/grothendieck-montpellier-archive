"""Bounded exact window synthesis on minimum-cover circuits for linear incidence graphs.

Run with python 612_constructions.py. Circuit values are truth-table integers.
"""
import itertools
import json
import random
import time
from functools import lru_cache
from pathlib import Path


def op(kind, a, b):
    return a & b if kind == "&" else a | b


def eval_circuit(inputs, gates, override=None):
    values = inputs.copy()
    for kind, a, b in gates:
        i = len(values)
        values.append(override[1] if override and override[0] == i else op(kind, values[a], values[b]))
    return values


def cases(n, edges):
    sets = [a for a in range(1 << n) if all(not ((a >> i) & (a >> j) & 1) for i, j in edges)]
    s = set(sets)
    maximal = [a for a in sets if all((a | 1 << i) not in s for i in range(n) if not a >> i & 1)]
    positive = [(1 << i) | (1 << j) for i, j in edges]
    return positive + maximal, (1 << len(positive)) - 1


def test_inputs(n, assignments):
    return [sum(1 << j for j, a in enumerate(assignments) if a >> i & 1) for i in range(n)]


def minimum_covers(n, edges):
    for k in range(n + 1):
        covers = [tuple(t) for t in itertools.combinations(range(n), k)
                  if all(i in t or j in t for i, j in edges)]
        if covers:
            return covers


@lru_cache(None)
def all_trees(leaves):
    if len(leaves) == 1:
        return (leaves[0],)
    trees = []
    for k in range(1, len(leaves)):
        for part in itertools.combinations(leaves[1:], k - 1):
            l = (leaves[0],) + part
            r = tuple(v for v in leaves if v not in l)
            trees.extend((a, b) for a in all_trees(l) for b in all_trees(r))
    return tuple(trees)


def random_tree(leaves, rng):
    t = list(leaves)
    while len(t) > 1:
        a = t.pop(rng.randrange(len(t)))
        b = t.pop(rng.randrange(len(t)))
        t.append((a, b))
    return t[0]


def star_circuit(n, cover, neighbor_trees, output_tree):
    gates = []

    def append(kind, a, b):
        gates.append((kind, a, b))
        return n + len(gates) - 1

    def build(tree, leaf):
        if isinstance(tree, int):
            return leaf[tree]
        return append("|", build(tree[0], leaf), build(tree[1], leaf))
    stars = [append("&", v, build(t, range(n))) for v, t in zip(cover, neighbor_trees)]
    build(output_tree, stars)
    return gates


def make_stars(n, edges, exhaustive, seed=612):
    rng = random.Random(seed)
    for cover in minimum_covers(n, edges):
        leaves = {i: [] for i in cover}
        for a, b in edges:
            # The sampled families use a bipartition as a minimum cover.
            if a in leaves:
                leaves[a].append(b)
            else:
                leaves[b].append(a)
        if any(not l for l in leaves.values()):
            raise ValueError("redundant canonical centre")
        all_neighbors = [tuple(sorted(leaves[i])) for i in cover]
        if exhaustive:
            for neighborhood in itertools.product(*(all_trees(l) for l in all_neighbors)):
                for output in all_trees(tuple(range(len(cover)))):
                    yield star_circuit(n, cover, neighborhood, output)
        else:
            for _ in range(4):
                neighborhood = [random_tree(l, rng) for l in all_neighbors]
                yield star_circuit(n, cover, neighborhood, random_tree(range(len(cover)), rng))


def windows(n, gates, root, limit):
    stack, seen = [frozenset([root])], set()
    while stack:
        removed = stack.pop()
        if removed in seen:
            continue
        seen.add(removed)
        yield removed
        if len(removed) == limit:
            continue
        for w in removed:
            for i in gates[w - n][1:]:
                if i >= n and i not in removed:
                    stack.append(removed | {i})


def replacements(bases, positive, negative, budget):
    care = positive | negative
    levels = [{v & care: i for i, v in bases}]
    if positive in levels[0]:
        return levels[0][positive]
    seen = set(levels[0])
    for size in range(1, budget + 1):
        new = {}
        for a_size in range((size - 1) // 2 + 1):
            b_size = size - 1 - a_size
            for kind in ("&", "|"):
                if size == budget:
                    # The final AND needs two supersets of the positive tests;
                    # the final OR needs two subsets of those tests.
                    def compatible(item):
                        w = item[0]
                        return (w & positive) == positive if kind == "&" else not (w & negative)
                    left = filter(compatible, levels[a_size].items())
                    right = list(filter(compatible, levels[b_size].items()))
                else:
                    left, right = levels[a_size].items(), levels[b_size].items()
                for x, ex in left:
                    for y, ey in right:
                        z = op(kind, x, y)
                        if z == positive:
                            return kind, ex, ey
                        if size < budget and z not in seen and z not in new:
                            new[z] = kind, ex, ey
        seen.update(new)
        levels.append(new)
    return None


def materialize(n, gates, removed, root, expression):
    new = []
    saved = {}

    def emit(expr):
        if isinstance(expr, int):
            return wire(expr)
        kind, a, b = expr
        a1, b1 = emit(a), emit(b)
        new.append((kind, a1, b1))
        return n + len(new) - 1

    def wire(i):
        if i < n:
            return i
        if i not in saved:
            if i == root:
                saved[i] = emit(expression)
            else:
                assert i not in removed
                saved[i] = emit(gates[i - n])
        return saved[i]

    output = wire(n + len(gates) - 1)
    return new, output


def run(name, n, edges, exhaustive, deadline):
    started = time.perf_counter()
    tests, target = cases(n, edges)
    all_points = (1 << len(tests)) - 1
    inputs = test_inputs(n, tests)
    full = test_inputs(n, range(1 << n))
    full_target = 0
    for a, b in edges:
        full_target |= full[a] & full[b]
    neighbors = [{b if a == v else a for a, b in edges if v in (a, b)} for v in range(n)]
    assert all(len(neighbors[a] & neighbors[b]) <= 1 for a in range(n) for b in range(a))
    count = 0
    nwin = [0] * 5
    misses = set()
    seen_circuits = set()
    witness = None
    timed_out = False
    covers = minimum_covers(n, edges)
    optimum = len(edges) + len(covers[0]) - 1
    for gates in make_stars(n, edges, exhaustive):
        frozen = tuple(gates)
        if frozen in seen_circuits:
            continue
        seen_circuits.add(frozen)
        assert len(gates) == optimum
        values = eval_circuit(inputs, gates)
        assert values[-1] == target
        assert eval_circuit(full, gates)[-1] == full_target
        count += 1
        for root in range(n, n + len(gates)):
            f0 = eval_circuit(inputs, gates, (root, 0))[-1]
            f1 = eval_circuit(inputs, gates, (root, all_points))[-1]
            pos, neg = target & ~f0, f1 & ~target
            below = {root}
            for i, (_, a, b) in enumerate(gates, start=n):
                if a in below or b in below:
                    below.add(i)
            for removed in windows(n, gates, root, 4):
                if time.perf_counter() > deadline:
                    timed_out = True
                    break
                budget = len(removed) - 1
                nwin[len(removed)] += 1
                pool = [(i, v) for i, v in enumerate(values) if i not in removed | below]
                key = (pos, neg, tuple(sorted({v & (pos | neg) for _, v in pool})), budget)
                if key in misses:
                    continue
                solution = replacements(pool, pos, neg, budget)
                if solution is None:
                    misses.add(key)
                else:
                    new, output = materialize(n, gates, removed, root, solution)
                    assert len(new) < optimum and eval_circuit(full, new)[output] == full_target
                    witness = {"gates": new, "output": output}
                    break
            if timed_out or witness:
                break
        if timed_out or witness:
            break
    return {"name": name, "n": n, "edges": edges, "cover_number": len(covers[0]),
            "minimum_covers": covers, "threshold": optimum, "maximal_independent_sets": len(tests)-len(edges),
            "distinct_seed_circuits_visited": count, "windows_of_sizes_1_to_4": nwin[1:],
            "distinct_negative_searches": len(misses), "full_truth_table_rows": 1 << n,
            "smaller_circuit": witness, "exhaustive_seed_trees": exhaustive, "timeout": timed_out,
            "seconds": round(time.perf_counter()-started, 3)}


if __name__ == "__main__":
    t0 = time.perf_counter()
    theta = [(0, 2+i) for i in range(3)] + [(2+i, 5+i) for i in range(3)] + [(1, 5+i) for i in range(3)]
    fano_lines = [(i, (i+1) % 7, (i+3) % 7) for i in range(7)]
    out = [run("three length-three paths between two terminals", 8, theta, True, t0+40)]
    for m in [5, 6, 7]:
        edges = [(p, 7+i) for i, line in enumerate(fano_lines[:m]) for p in line]
        out.append(run(f"{m} cyclic Fano lines", 7+m, edges, False, time.perf_counter()+20))
    dst = Path(__file__).with_suffix(".json")
    dst.write_text(json.dumps({"seconds": round(time.perf_counter()-t0,3), "results":out}, indent=2), "utf-8")
    for r in out:
        print(r["name"], r["distinct_seed_circuits_visited"], r["windows_of_sizes_1_to_4"],
              r["seconds"], r["timeout"], r["smaller_circuit"])
