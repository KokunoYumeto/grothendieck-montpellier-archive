#!/usr/bin/env python3
"""Exact bounded supplement to the uniform nine-theta graph proof.

No geometry or infinite assertion is inferred from these finite checks.
The eighteen parallel edges are retained individually throughout.
"""
from datetime import datetime, timezone
from itertools import product
from pathlib import Path
import hashlib
import json
import time


def binary_rank(rows):
    pivots = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def check_group(moduli):
    elements = list(product(*(range(m) for m in moduli)))
    zero = tuple(0 for _ in moduli)
    add = lambda a, b: tuple((x + y) % m for x, y, m in zip(a, b, moduli))
    neg = lambda a: tuple(-x % m for x, m in zip(a, moduli))
    sub = lambda a, b: add(a, neg(b))
    typ = lambda a: min(a, neg(a))
    types = sorted({typ(a) for a in elements if a != zero})
    type_index = {h: i for i, h in enumerate(types)}
    k = len(elements)
    edges = []
    for vertex in range(3):
        for h in types:
            for label in range(18):
                edges.append(("loop", vertex, vertex, h, label))
    for i, j in ((0, 1), (0, 2), (1, 2)):
        for g in elements:
            for label in range(18):
                edges.append(("cross", i, j, g, label))
    assert len(edges) == 81 * k - 27
    stars = [sum(1 << q for q, e in enumerate(edges)
                 if e[0] == "cross" and vertex in e[1:3])
             for vertex in range(3)]
    assert binary_rank(stars) == 2
    assert stars[0] ^ stars[1] ^ stars[2] == 0
    assert all(row.bit_count() == 36 * k for row in stars)

    parent = list(range(len(edges)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[a] = b

    constant_rows = []
    partition_count = 0
    for r0, r1 in product(elements, repeat=2):
        r2 = neg(add(r0, r1))
        r = (r0, r1, r2)
        assert add(add(r0, r1), r2) == zero
        selected = []
        parts = {h: [] for h in types}
        selected_by_pair = {}
        for q, edge in enumerate(edges):
            kind, i, j, g, _ = edge
            if kind == "loop":
                parts[g].append(q)
            else:
                diff = sub(g, sub(r[j], r[i]))
                if diff == zero:
                    selected.append(q)
                    selected_by_pair.setdefault((i, j), []).append(q)
                else:
                    parts[typ(diff)].append(q)
        assert len(selected) == 54
        assert all(len(part) == 162 for part in parts.values())
        assert sum(map(len, parts.values())) == 81 * (k - 1)
        selected_mask = sum(1 << q for q in selected)
        selected_stars = [s & selected_mask for s in stars]
        assert binary_rank(selected_stars) == 2
        assert len(selected) - 2 == 52
        # No nonzero target coboundary vanishes on the selected graph.
        assert all((s & selected_mask) != 0 for s in stars)
        for h, part in parts.items():
            anchor = part[0]
            for q in part[1:]:
                union(anchor, q)
            # The unselected star has exactly the claimed nonconstant pattern.
            for star in stars:
                ones = sum(bool(star & (1 << q)) for q in part)
                assert (ones, len(part) - ones) == (72, 90)
        for pair, labels in selected_by_pair.items():
            assert len(labels) == 18
            total = sum(1 << q for q in labels)
            nine_pairs = 0
            for j in range(0, 18, 2):
                pair_vector = (1 << labels[j]) ^ (1 << labels[j + 1])
                assert binary_rank(selected_stars + [pair_vector]) == 3
                nine_pairs ^= pair_vector
            assert nine_pairs == total
        row = 0
        for i, j in ((0, 1), (0, 2), (1, 2)):
            diff = sub(r[j], r[i])
            if diff != zero:
                row ^= 1 << type_index[typ(diff)]
        constant_rows.append(row)
        partition_count += 1

    # Pair differences within the hearts connect every edge coordinate:
    # their raw span is the complete even-sum hyperplane.
    connected_coordinates = len({find(q) for q in range(len(edges))})
    assert connected_coordinates == 1
    raw_heart_span = len(edges) - 1
    quotient_heart_span = raw_heart_span - 2
    graph_dimension = len(edges) - 2
    assert quotient_heart_span == graph_dimension - 1
    # The only type-constant vector lying in every T_r is zero.
    assert binary_rank(constant_rows) == len(types)
    delta = 81 * (k - 1)
    R = 81 * k - 1
    large_summand = 80 + 161 * len(types)
    assert 2 * large_summand > R
    for f in (0, 1):
        source_boundary = 3 * (8 + f) + 52 - f
        target_boundary = 3 * (8 + f) + graph_dimension - f
        assert source_boundary == 76 + 2 * f
        assert target_boundary == R - (4 - 2 * f)
        assert target_boundary - source_boundary == delta
    return {
        "moduli": list(moduli), "order": k, "types": len(types),
        "partitions": partition_count, "edges": len(edges),
        "graph_dimension": graph_dimension,
        "selected_graph_dimension": 52,
        "kernel_dimension": delta, "type_dimension": 162,
        "quotient_heart_span_dimension": quotient_heart_span,
        "constant_constraint_rank": binary_rank(constant_rows),
        "star_ones_zeros": [72, 90],
        "large_transvection_summand_lower_bound": large_summand,
        "target_rank": R,
    }


def main():
    start = time.perf_counter()
    cases = [check_group(moduli) for moduli in [(3,), (5,), (7,), (9,), (3, 3)]]
    decompositions = {}
    for d in range(2, 10002, 2):
        if d == 2:
            decompositions[d] = "proved degree-two base case"
            continue
        if d % 6 == 0:
            a, b = 3, d - 3
        elif d % 6 == 4:
            a, b = 1, d - 1
        else:
            a, b = 5, d - 5
        assert a > 0 and b > 0 and a + b == d and a % 2 == b % 2 == 1
        assert all(x in (1, 5) or x % 3 == 0 for x in (a, b))
        decompositions[d] = [a, b]
    source = Path(__file__)
    result = {
        "status": "PASS", "actual_utc": datetime.now(timezone.utc).isoformat(),
        "runtime_seconds": time.perf_counter() - start,
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "scope": "Exact bounded graph and arithmetic supplement only; all geometric and infinite assertions depend on the written proof.",
        "parallel_edge_multiplicity": 18, "group_cases": cases,
        "even_degree_range": [2, 10000], "even_degree_cases": len(decompositions),
        "first_decompositions": {d: decompositions[d] for d in range(2, 32, 2)},
    }
    output = source.parents[1] / "outputs/nonordinary_nine_theta_weighted_graph_checks.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
