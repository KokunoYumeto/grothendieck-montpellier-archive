#!/usr/bin/env python3
"""Independent finite checks and gate witnesses for even cycles with two leaves.

Standard library only. The exhaustive checks concern graph cover numbers and
positive upper-bound witnesses, not an enumeration of all Boolean circuits.
Run: python workbench/programs/c8_two_leaves_check.py --output-dir workbench/certificates
"""
import argparse
import hashlib
import json
from pathlib import Path


def graph(length, separation):
    assert length % 2 == 0 and length >= 6 and 0 < separation < length
    return [(v, (v + 1) % length) for v in range(length)] + [(0, length), (separation, length + 1)]


def edge_value(mask, edges):
    return any(((mask >> u) & 1) and ((mask >> v) & 1) for u, v in edges)


def evaluator(mask, n, gates, output):
    """Exact project semantics, with compact rows [op, *operand_indices]."""
    wires = [bool((mask >> i) & 1) for i in range(n)]
    for row in gates:
        values = [wires[i] if 0 <= i < len(wires) else False for i in row[1:]]
        if row[0] == "AND":
            result = all(values)
        elif row[0] == "OR":
            result = any(values)
        elif row[0] == "NOT":
            result = not (values[0] if values else False)
        else:
            raise ValueError(row[0])
        wires.append(result)
    return wires[output] if 0 <= output < len(wires) else False


def cover_stats(n, edges):
    masks = [(1 << u) | (1 << v) for u, v in edges]
    best = n + 1
    minimum = []
    for s in range(1 << n):
        size = s.bit_count()
        if size > best:
            continue
        if all(s & e for e in masks):
            if size < best:
                best, minimum = size, [s]
            else:
                minimum.append(s)
    return best, minimum


def cover_circuit(n, edges, cover):
    """Assign each edge to its smaller selected endpoint, then combine stars."""
    buckets = {v: [] for v in sorted(cover)}
    for u, v in edges:
        root = min(w for w in (u, v) if w in cover)
        buckets[root].append(v if root == u else u)
    gates = []

    def gate(op, a, b):
        gates.append([op, a, b])
        return n + len(gates) - 1

    def fold_or(wires):
        assert wires
        acc = wires[0]
        for w in wires[1:]:
            acc = gate("OR", acc, w)
        return acc

    stars = []
    for v, neighbors in buckets.items():
        assert neighbors, (v, edges, cover)
        stars.append(gate("AND", v, fold_or(neighbors)))
    return gates, fold_or(stars)


C8_GATES = [
    ["OR", 1, 7], ["OR", 10, 8], ["AND", 0, 11],
    ["OR", 1, 3], ["AND", 2, 13], ["OR", 4, 9], ["AND", 3, 15],
    ["OR", 4, 6], ["AND", 5, 17], ["AND", 6, 7],
    ["OR", 12, 14], ["OR", 16, 18], ["OR", 20, 21], ["OR", 22, 19],
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--max-cycle", type=int, default=12,
                        help="even upper limit for exhaustive cover/witness checks (default 12)")
    args = parser.parse_args()
    rows = []
    truth_rows = 0
    for length in range(6, args.max_cycle + 1, 2):
        k = length // 2
        for d in range(1, length):
            n = length + 2
            edges = graph(length, d)
            tau, minima = cover_stats(n, edges)
            expected_tau = k + (d % 2)
            assert tau == expected_tau, (length, d, tau, expected_tau)
            cover = set(range(0, length, 2)) | ({d} if d % 2 else set())
            gates, out = cover_circuit(n, edges, cover)
            size = 3 * k + 1 + (d % 2)
            assert len(gates) == size
            true = 0
            for x in range(1 << n):
                correct = edge_value(x, edges)
                assert evaluator(x, n, gates, out) == correct, (length, d, x)
                true += correct
            truth_rows += 1 << n
            rows.append({"cycle_length": length, "roots": [0, d],
                         "root_classes": "opposite" if d % 2 else "same",
                         "cover_number": tau, "minimum_cover_count": len(minima),
                         "witness_gate_count": len(gates), "truth_rows": 1 << n,
                         "true_rows": true})

    edges = graph(8, 3)
    true = 0
    for x in range(1 << 10):
        correct = edge_value(x, edges)
        assert evaluator(x, 10, C8_GATES, 23) == correct
        true += correct
    altered = [list(row) for row in C8_GATES]
    altered[0][0] = "AND"
    failures = [x for x in range(1 << 10) if evaluator(x, 10, altered, 23) != edge_value(x, edges)]
    assert failures, "Negative control unexpectedly passed"
    payload = json.dumps(C8_GATES, separators=(",", ":")).encode("ascii")
    witness = {
        "n": 10, "cycle_length": 8, "roots": [0, 3], "edges": edges,
        "gates": C8_GATES, "output": 23, "gate_count": 14,
        "gate_array_sha256": hashlib.sha256(payload).hexdigest(),
        "truth_rows": 1024, "true_rows": true, "false_rows": 1024 - true,
        "negative_control": {"change": "first OR changed to AND", "mismatch_count": len(failures),
                             "smallest_failing_input_mask": failures[0]},
        "domain": "positive witness; lower bound is a mathematical proof, not finite circuit enumeration",
    }
    report = {"status": "PASS", "graphs_checked": len(rows),
              "truth_rows_checked": truth_rows, "max_cycle_length": args.max_cycle,
              "graph_checks": rows}
    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        for name, data in (("c8_two_leaf_witness.json", witness), ("c8_even_cycle_checks.json", report)):
            (args.output_dir / name).write_text(json.dumps(data, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "graphs_checked": len(rows),
                      "truth_rows_checked": truth_rows, "c8_witness": witness}, sort_keys=True))


if __name__ == "__main__":
    main()
