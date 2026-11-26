#!/usr/bin/env python3
"""Independently verify branch_graph.json using sets rather than bit operations.

The verifier does not import the generator. It reconstructs every reachable
layer exactly, checks all graph hypotheses, and checks that the designated
matching covers all twelve vertices. It additionally checks on every residual
vertex subset and every active twin group that at most one surviving matching
edge can be removed. This last test is a finite control of the general matching
lemma, whose proof is in the research note and the paper.
"""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path

EXPECTED_EDGES = {(0,1),(0,2),(2,3),(3,4),(4,5),(5,6),(1,6),
                  (0,7),(7,8),(8,9),(9,10),(10,11),(1,11)}


def decode(mask: int, n: int) -> frozenset[int]:
    assert 0 <= mask < 2 ** n
    return frozenset(v for v in range(n) if (mask // (2 ** v)) % 2)


def verify(path: Path) -> dict:
    obj = json.loads(path.read_text())
    n = obj["n"]
    assert n == 12
    universe = frozenset(range(n))
    edges = {tuple(sorted(e)) for e in obj["edges"]}
    assert edges == EXPECTED_EDGES
    assert len(edges) == len(obj["edges"])
    neighbors = {v: frozenset(w for a, b in edges for w in
                             ([b] if a == v else [a] if b == v else []))
                 for v in universe}
    assert all(len(neighbors[v]) >= 2 for v in universe)
    assert all(len(neighbors[u] & neighbors[v]) <= 1
               for u, v in itertools.combinations(universe, 2))
    assert [len(neighbors[v]) for v in range(n)] == obj["degrees"]
    assert [sum(2 ** w for w in neighbors[v]) for v in range(n)] == obj["adjacency_masks"]
    assert obj["max_common_neighbors_of_distinct_vertices"] == 1
    matching = {frozenset(e) for e in obj["perfect_matching"]}
    assert len(matching) == 6
    assert all(tuple(sorted(e)) in edges for e in matching)
    assert sum(map(len, matching)) == len(frozenset().union(*matching)) == n
    for i, j, u, v in obj["alternate_neighbor_witnesses"]:
        assert tuple(sorted((i, j))) in edges
        assert u in neighbors[i] and v in neighbors[j]
        assert u != j and v != i and v not in neighbors[u]
    assert {tuple(sorted(w[:2])) for w in obj["alternate_neighbor_witnesses"]} == edges

    def close(deleted: frozenset[int]) -> frozenset[int]:
        return deleted | frozenset(v for v in universe if not neighbors[v] - deleted)

    def classes(deleted: frozenset[int]) -> set[frozenset[int]]:
        groups = {}
        for v in universe - deleted:
            residual = neighbors[v] - deleted
            if residual:
                groups.setdefault(residual, set()).add(v)
        return {frozenset(group) for group in groups.values()}

    seen = {close(frozenset())}
    for depth, encoded in enumerate(obj["layers"]):
        claimed = {decode(mask, n) for mask in encoded}
        assert len(claimed) == len(encoded) == obj["layer_sizes"][depth]
        assert claimed == seen, ("frontier mismatch", depth)
        assert (universe in seen) == (depth == obj["first_full_depth"])
        seen = seen | {close(deleted | group)
                       for deleted in seen for group in classes(deleted)}
    assert obj["first_full_depth"] == 6
    assert obj["layer_sizes"] == [1,13,79,283,642,939,999]

    checked = 0
    for mask in range(2 ** n):
        deleted = decode(mask, n)
        surviving = {e for e in matching if not e & deleted}
        for group in classes(deleted):
            destroyed = {e for e in surviving if e & group}
            assert len(destroyed) <= 1, (deleted, group, destroyed)
            assert all(not e <= close(deleted | group)
                       for e in surviving - destroyed)
            checked += 1
    return {"status": "verified", "vertices": n, "edges": len(edges),
            "perfect_matching_size": len(matching),
            "first_full_depth": 6,
            "layer_sizes": obj["layer_sizes"],
            "residual_class_matching_checks": checked,
            "circuit_exhaustion_claimed": False}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path,
                        default=Path(__file__).resolve().parents[1] / "certificates/branch_graph.json")
    args = parser.parse_args()
    print(json.dumps(verify(args.certificate), sort_keys=True))


if __name__ == "__main__":
    main()
