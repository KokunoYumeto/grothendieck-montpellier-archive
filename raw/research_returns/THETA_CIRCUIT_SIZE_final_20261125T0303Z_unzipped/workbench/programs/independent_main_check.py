"""Independent finite checks of the concrete main.tex objects; no lower-bound search."""

from itertools import combinations

N = 12
EDGES = ((0, 1), (0, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1),
         (0, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 1))
GATES = (("or", 1, 2), ("or", 12, 7), ("and", 0, 13),
         ("or", 6, 11), ("and", 1, 15), ("or", 2, 4),
         ("and", 3, 17), ("or", 4, 6), ("and", 5, 19),
         ("or", 7, 9), ("and", 8, 21), ("or", 9, 11),
         ("and", 10, 23), ("or", 14, 16), ("or", 18, 20),
         ("or", 22, 24), ("or", 25, 26), ("or", 28, 27))


def edge_value(mask):
    return any((mask >> a) & (mask >> b) & 1 for a, b in EDGES)


def circuit_value(mask, mutate=False):
    wires = [bool((mask >> i) & 1) for i in range(N)]
    for k, (op, a, b) in enumerate(GATES):
        if mutate and k == 0:
            op = "and"
        wires.append(wires[a] and wires[b] if op == "and" else wires[a] or wires[b])
    return wires[29]


if __name__ == "__main__":
    masks = range(1 << N)
    true_count = sum(map(edge_value, masks))
    mismatch = sum(circuit_value(m) != edge_value(m) for m in masks)
    mutant_mismatch = sum(circuit_value(m, True) != edge_value(m) for m in masks)
    maximal_independent = [m for m in masks if not edge_value(m)
                           and all(edge_value(m | (1 << v))
                                   for v in range(N) if not (m >> v) & 1)]
    covers = []
    for size in range(N + 1):
        covers = [c for c in combinations(range(N), size)
                  if all(a in c or b in c for a, b in EDGES)]
        if covers:
            break
    matching = ((0, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 1))
    assert len({v for edge in matching for v in edge}) == N
    assert all(edge in EDGES or edge[::-1] in EDGES for edge in matching)
    assert (true_count, (1 << N) - true_count, len(maximal_independent),
            mismatch, mutant_mismatch) == (3799, 297, 27, 0, 65)
    assert covers == [(0, 1, 3, 5, 8, 10)]
    print({"truth_rows": 1 << N, "true": true_count,
           "false": (1 << N) - true_count,
           "maximal_independent_sets": len(maximal_independent),
           "witness_mismatches": mismatch,
           "mutation_mismatches": mutant_mismatch,
           "minimum_covers": covers, "matching_size": len(matching)})
