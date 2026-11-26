#!/usr/bin/env python3
"""Independent finite graph checks for the reader and positive-bound audit.

No SAT solver, external files, or nonstandard packages are required.
This verifies graph facts, not absence of arbitrary 17-gate circuits.
Run from any directory; --output writes the complete compact witness data.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

N = 12
PATHS = ((0, 1), (0, 2, 3, 4, 5, 6, 1), (0, 7, 8, 9, 10, 11, 1))
EDGES = tuple((min(a, b), max(a, b)) for path in PATHS for a, b in zip(path, path[1:]))
ADJ = tuple(frozenset(b if a == v else a for a, b in EDGES if v in (a, b)) for v in range(N))
ODD = (2, 4, 6, 7, 9, 11)
EVEN = (3, 5, 8, 10)


def value(mask):
    return any(mask & (1 << a) and mask & (1 << b) for a, b in EDGES)


def verts(mask):
    return [v for v in range(N) if mask & (1 << v)]


def check():
    covers = [s for s in range(1 << N) if all(s & ((1 << a) | (1 << b)) for a, b in EDGES)]
    tau = min(s.bit_count() for s in covers)
    minimum = [s for s in covers if s.bit_count() == tau]
    expected = sum(1 << v for v in (0, 1, 3, 5, 8, 10))
    assert tau == 6 and minimum == [expected]
    matching = ((0, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 1))
    assert len({v for e in matching for v in e}) == 12
    assert all(tuple(sorted(e)) in EDGES for e in matching)
    assert all(len(ADJ[v]) >= 2 for v in range(N))
    assert not any(a in ADJ[b] and b in ADJ[c] and c in ADJ[a]
                   for a, b, c in itertools.combinations(range(N), 3))
    assert all(len(ADJ[v] & ADJ[w]) <= 1 for v, w in itertools.combinations(range(N), 2))

    alternates = []
    for u, v in EDGES:
        witnesses = [(a, b) for a in sorted(ADJ[u] - {v}) for b in sorted(ADJ[v] - {u})
                     if b not in ADJ[a]]
        assert witnesses
        alternates.append([u, v, *witnesses[0]])

    distinguish = []
    for v in range(N):
        for w in range(N):
            if v == w:
                continue
            z = next(z for z in sorted(ADJ[v]) if z not in ADJ[w])
            assert not value((1 << w) | (1 << z))
            assert value((1 << v) | (1 << w) | (1 << z))
            distinguish.append([v, w, z])

    # An odd OR reader cannot have a distinct primary as its other operand.
    # Even readers additionally need the analogous controlling-zero check.
    primary_obstructions = []
    for v in ODD + EVEN:
        for w in range(N):
            if v == w:
                continue
            for b in ((1,) if v in ODD else (0, 1)):
                witnesses = [s for s in range(1 << N)
                             if not (s >> v) & 1 and ((s >> w) & 1) == b
                             and not value(s) and value(s | (1 << v))]
                assert witnesses, (v, w, b)
                primary_obstructions.append([v, w, b, min(witnesses, key=lambda s: (s.bit_count(), s))])

    hub_sensitivities = []
    for v in range(2, 12):
        for a, b in ((0, 0), (0, 1), (1, 0)):
            witnesses = [s for s in range(1 << N)
                         if ((s >> 0) & 1) == a and ((s >> 1) & 1) == b
                         and not ((s >> v) & 1) and not value(s) and value(s | (1 << v))]
            assert witnesses, (v, a, b)
            hub_sensitivities.append([v, a, b, min(witnesses, key=lambda s: (s.bit_count(), s))])

    return {
        "domain": "graph facts and reader sensitivity witnesses only",
        "n": N, "edges": EDGES, "tau": tau,
        "unique_minimum_cover": verts(expected), "matching": matching,
        "alternate_independent_neighbors": alternates,
        "singleton_cut_distinguishing_neighbors": distinguish,
        "primary_reader_obstructions": primary_obstructions,
        "interior_hub_sensitivities": hub_sensitivities,
        "hub_zero_neighbor_eligibility_under_unique_cover": {
            "eligible": [1], "ineligible": [2, 7], "required_consumptions": 3,
            "available_under_17_positive_gates": 2,
        },
        "checks": {
            "edge_count": len(EDGES), "minimum_degree": min(map(len, ADJ)),
            "no_triangle": True, "no_four_cycle": True,
            "minimum_covers_count": len(minimum),
            "alternate_pairs_checked": len(alternates),
            "singleton_cut_pairs_checked": len(distinguish),
            "primary_reader_pairs_values_checked": len(primary_obstructions),
            "interior_hub_patterns_checked": len(hub_sensitivities),
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = check()
    payload = (json.dumps(data, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(payload)
    print(json.dumps({"status": "PASS", **data["checks"],
                      "certificate_sha256": hashlib.sha256(payload).hexdigest()}, sort_keys=True))
