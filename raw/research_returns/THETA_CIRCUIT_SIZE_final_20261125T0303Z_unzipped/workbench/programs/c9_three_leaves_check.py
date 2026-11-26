#!/usr/bin/env python3
"""Check odd-separated three-leaf cycles using only the standard library.

This enumerates graph covers and evaluates explicit witnesses. It is not a
search over all circuits. The C9 witness has an additional independent
scalar check and a deliberately changed negative control.
"""
import argparse
import hashlib
import json
from pathlib import Path


def graph(distances):
    assert all(d >= 3 and d % 2 for d in distances) and len(distances) == 3
    length = sum(distances)
    roots = [0, distances[0], distances[0] + distances[1]]
    edges = [(i, (i + 1) % length) for i in range(length)]
    edges += [(root, length + j) for j, root in enumerate(roots)]
    return length, roots, edges


def minimum_covers(n, edges):
    masks = [(1 << u) | (1 << v) for u, v in edges]
    best, minimum = n + 1, []
    for s in range(1 << n):
        size = s.bit_count()
        if size > best:
            continue
        if all(s & edge for edge in masks):
            if size < best:
                best, minimum = size, [s]
            else:
                minimum.append(s)
    return best, minimum


def input_tables(n):
    rows = 1 << n
    tables = []
    for i in range(n):
        block = 1 << i
        bits = ((1 << block) - 1) << block
        width = 2 * block
        while width < rows:
            bits |= bits << width
            width *= 2
        tables.append(bits)
    return tables


def bit_evaluate(n, gates, output):
    wires = input_tables(n)
    universe = (1 << (1 << n)) - 1
    for op, *indices in gates:
        values = [wires[i] if 0 <= i < len(wires) else 0 for i in indices]
        if op == "AND":
            value = universe
            for x in values:
                value &= x
        elif op == "OR":
            value = 0
            for x in values:
                value |= x
        elif op == "NOT":
            value = universe ^ (values[0] if values else 0)
        else:
            raise ValueError(op)
        wires.append(value)
    return wires[output] if 0 <= output < len(wires) else 0


def scalar_evaluate(mask, n, gates, output):
    values = [bool((mask >> v) & 1) for v in range(n)]
    for gate in gates:
        operands = [values[i] if 0 <= i < len(values) else False for i in gate[1:]]
        if gate[0] == "AND":
            result = all(operands)
        elif gate[0] == "OR":
            result = any(operands)
        elif gate[0] == "NOT":
            result = not (operands[0] if operands else False)
        else:
            raise ValueError(gate[0])
        values.append(result)
    return values[output] if 0 <= output < len(values) else False


def graph_value(mask, edges):
    return any((mask & (1 << u)) and (mask & (1 << v)) for u, v in edges)


def make_witness(length, roots, edges):
    n = length + 3
    cover = set(roots)
    for j, start in enumerate(roots):
        finish = roots[(j + 1) % 3]
        distance = (finish - start) % length
        cover.update((start + offset) % length for offset in range(2, distance, 2))
    assigned = {v: [] for v in sorted(cover)}
    for u, v in edges:
        root = min(w for w in (u, v) if w in cover)
        assigned[root].append(v if u == root else u)
    gates = []

    def gate(op, u, v):
        gates.append([op, u, v])
        return n + len(gates) - 1

    def disjoin(wires):
        result = wires[0]
        for v in wires[1:]:
            result = gate("OR", result, v)
        return result

    stars = []
    for root, neighbors in assigned.items():
        assert neighbors
        stars.append(gate("AND", root, disjoin(neighbors)))
    return sorted(cover), gates, disjoin(stars)


C9 = [
    ["OR", 1, 8], ["OR", 12, 9], ["AND", 0, 13],
    ["OR", 1, 3], ["AND", 2, 15], ["OR", 4, 10], ["AND", 3, 17],
    ["OR", 4, 6], ["AND", 5, 19], ["OR", 7, 11], ["AND", 6, 21],
    ["AND", 7, 8], ["OR", 14, 16], ["OR", 18, 20], ["OR", 22, 23],
    ["OR", 24, 25], ["OR", 27, 26],
]


def check(distances):
    length, roots, edges = graph(distances)
    n, k = length + 3, (length - 1) // 2
    tau, all_minima = minimum_covers(n, edges)
    assert tau == k + 2
    cycle_tau, cycle_minima = minimum_covers(length, edges[:length])
    assert cycle_tau == k + 1 and len(cycle_minima) == length
    selected_root_witnesses = []
    for s in cycle_minima:
        internal = [(u, v) for u, v in edges[:length] if (s >> u) & 1 and (s >> v) & 1]
        assert len(internal) == 1
        isolated_roots = [r for r in roots if (s >> r) & 1
                          and not ((s >> ((r - 1) % length)) & 1)
                          and not ((s >> ((r + 1) % length)) & 1)]
        assert isolated_roots, (distances, s)
        selected_root_witnesses.append({"minimum_cycle_cover_mask": s,
                                        "unique_selected_edge": internal[0],
                                        "isolated_selected_roots": isolated_roots})
    cover, gates, output = make_witness(length, roots, edges)
    assert len(cover) == tau and len(gates) == 3 * k + 5
    inputs = input_tables(n)
    expected = 0
    for u, v in edges:
        expected |= inputs[u] & inputs[v]
    assert bit_evaluate(n, gates, output) == expected
    return {"distances": distances, "cycle_length": length, "roots": roots, "n": n,
            "edges": edges, "cover_number": tau, "minimum_cover_count": len(all_minima),
            "minimum_cycle_covers": selected_root_witnesses, "cover": cover,
            "gates": gates, "gate_count": len(gates), "output": output,
            "truth_rows_checked": 1 << n, "true_rows": expected.bit_count(),
            "false_rows": (1 << n) - expected.bit_count()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    records = [check(ds) for ds in ((3, 3, 3), (3, 3, 5), (3, 5, 5), (5, 5, 5))]
    _, _, edges = graph((3, 3, 3))
    expected = bit_evaluate(12, records[0]["gates"], records[0]["output"])
    assert bit_evaluate(12, C9, 28) == expected
    for mask in range(4096):
        correct = graph_value(mask, edges)
        assert scalar_evaluate(mask, 12, C9, 28) == correct
        assert bool((expected >> mask) & 1) == correct
    altered = [row.copy() for row in C9]
    altered[0][0] = "AND"
    failures = [mask for mask in range(4096)
                if scalar_evaluate(mask, 12, altered, 28) != graph_value(mask, edges)]
    assert failures
    gates_bytes = json.dumps(C9, separators=(",", ":")).encode("ascii")
    report = {"status": "PASS", "domain": "graph covers, selected-root witnesses, and explicit circuit evaluation",
              "graphs_checked": len(records),
              "truth_rows_checked": sum(row["truth_rows_checked"] for row in records),
              "c9_scalar_rows_checked": 4096,
              "c9_printed_witness": {"n": 12, "gates": C9, "output": 28, "gate_count": 17,
                                     "gate_array_sha256": hashlib.sha256(gates_bytes).hexdigest(),
                                     "true_rows": expected.bit_count(), "false_rows": 4096 - expected.bit_count(),
                                     "negative_control": {"change": "first OR changed to AND",
                                                          "mismatch_count": len(failures),
                                                          "smallest_failing_mask": failures[0]}},
              "graphs": records}
    payload = (json.dumps(report, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(payload)
    print(json.dumps({"status": "PASS", "graphs_checked": len(records),
                      "truth_rows_checked": report["truth_rows_checked"],
                      "c9_printed_witness": report["c9_printed_witness"],
                      "certificate_sha256": hashlib.sha256(payload).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
