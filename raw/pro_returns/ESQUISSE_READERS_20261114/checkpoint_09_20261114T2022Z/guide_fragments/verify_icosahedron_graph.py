#!/usr/bin/env python3
"""Exact check for the twelve displayed vertices in guide section 4.

An ordered pair (a,b) denotes a+b*phi, where phi=(1+sqrt(5))/2 and
phi^2=phi+1. The three nonzero squared distances are 4, 4+4*phi and
8+4*phi, so an edge joins precisely the pairs at squared distance 4.
No floating-point arithmetic or group-classification result is used.

Writes ICOSAHEDRON_GRAPH_CHECK.tsv beside this script and prints its
calculation summary. This verifies only this concrete vertex graph.
"""
from collections import Counter, deque
import csv
from itertools import combinations
import json
from pathlib import Path


ZERO, ONE, PHI = (0, 0), (1, 0), (0, 1)


def neg(a):
    return -a[0], -a[1]


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    return (a[0] * b[0] + a[1] * b[1],
            a[0] * b[1] + a[1] * b[0] + a[1] * b[1])


def squared_distance(v, w):
    answer = ZERO
    for a, b in zip(v, w):
        difference = sub(a, b)
        answer = add(answer, mul(difference, difference))
    return answer


def label(value):
    return {ZERO: "0", ONE: "1", neg(ONE): "-1",
            PHI: "phi", neg(PHI): "-phi"}[value]


def main():
    vertices = []
    for a in [ONE, neg(ONE)]:
        for b in [PHI, neg(PHI)]:
            vertices.extend([(ZERO, a, b), (a, b, ZERO), (b, ZERO, a)])
    assert len(vertices) == len(set(vertices)) == 12
    names = {v: f"v{i:02d}" for i, v in enumerate(vertices, 1)}
    nonzero = {squared_distance(v, w) for v, w in combinations(vertices, 2)}
    assert nonzero == {(4, 0), (4, 4), (8, 4)}
    adjacency = {v: [w for w in vertices if squared_distance(v, w) == (4, 0)]
                 for v in vertices}
    assert all(len(neighbors) == 5 for neighbors in adjacency.values())
    rows = []
    for vertex in vertices:
        distance = {vertex: 0}
        queue = deque([vertex])
        while queue:
            current = queue.popleft()
            for neighbor in adjacency[current]:
                if neighbor not in distance:
                    distance[neighbor] = distance[current] + 1
                    queue.append(neighbor)
        antipode = tuple(neg(a) for a in vertex)
        assert Counter(distance.values()) == Counter({0: 1, 1: 5, 2: 5, 3: 1})
        assert [v for v in vertices if distance[v] == 3] == [antipode]
        cycle = (vertex[1], vertex[2], vertex[0])
        assert cycle in names and cycle != vertex
        assert {(v[1], v[2], v[0]) for v in adjacency[vertex]} == set(adjacency[cycle])
        rows.append({
            "vertex": names[vertex],
            "coordinates": "(" + ",".join(map(label, vertex)) + ")",
            "distance_0": names[vertex],
            "distance_1": ",".join(names[v] for v in vertices if distance[v] == 1),
            "distance_2": ",".join(names[v] for v in vertices if distance[v] == 2),
            "distance_3": names[antipode],
            "antipode": names[antipode],
            "coordinate_cycle": names[cycle],
        })
    output = Path(__file__).resolve().with_name("ICOSAHEDRON_GRAPH_CHECK.tsv")
    with output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({
        "field_relation": "phi^2=phi+1; phi=(1+sqrt(5))/2",
        "vertices": 12,
        "nonzero_squared_distances": ["4", "4+4*phi", "8+4*phi"],
        "edges_of_squared_length_4": sum(map(len, adjacency.values())) // 2,
        "distance_profile_from_every_vertex": {"0": 1, "1": 5, "2": 5, "3": 1},
        "unique_distance_3_vertex": "-v",
        "coordinate_cycle": "(x,y,z)->(y,z,x); edge-preserving, nonidentity, third power identity",
        "output": output.name,
        "consequence": "Every incidence automorphism preserves graph distance, hence carries the unique antipode of v to the unique antipode of its image: h(-v)=-h(v).",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
