#!/usr/bin/env python3
"""Normalized coordinate certificate for the contractible parameter A-L07."""
from __future__ import annotations
from itertools import combinations_with_replacement
from pathlib import Path
import json
import time


def main() -> None:
    start = time.perf_counter()
    normalized = {}
    assertions = 0
    for n in range(9):
        pairs = list(combinations_with_replacement(range(n + 1), 2))
        survivors = [pair for pair in pairs if all(i in pair for i in range(1, n + 1))]
        expected = {0: [(0, 0)], 1: [(0, 1), (1, 1)], 2: [(1, 2)]}.get(n, [])
        assert survivors == expected
        assertions += 1
        normalized[str(n)] = {"coordinate_count": len(pairs), "normalized_basis": survivors}
    # Chain basis: degree0 a=00; degree1 b=01,c=11; degree2 d=12.
    d = {"a": {}, "b": {}, "c": {"a": 1}, "d": {"b": 1}}
    h = {"a": {"c": 1}, "b": {"d": 1}, "c": {}, "d": {}}

    def linear(op, vector):
        result = {}
        for key, value in vector.items():
            for target, coefficient in op[key].items():
                result[target] = result.get(target, 0) + value * coefficient
        return {k: v for k, v in result.items() if v}

    for key in "abcd":
        basis = {key: 1}
        assert linear(d, linear(d, basis)) == {}
        assertions += 1
        dh = linear(d, linear(h, basis))
        hd = linear(h, linear(d, basis))
        result = dict(dh)
        for target, value in hd.items():
            result[target] = result.get(target, 0) + value
        assert {k: v for k, v in result.items() if v} == basis
        assertions += 1
    # Inclusion of the normalized identity disk D2: top d, bottom b.
    assert d["d"] == {"b": 1} and d["b"] == {}
    assertions += 1
    # The normalized top indicator has coordinate12 equal1, and is idempotent.
    pairs2 = list(combinations_with_replacement(range(3), 2))
    indicator = tuple(int(pair == (1, 2)) for pair in pairs2)
    assert indicator[pairs2.index((1, 2))] == 1
    assert tuple(c * c for c in indicator) == indicator
    assertions += 2
    result = {
        "statement_id": "A-L07",
        "status": "PASS",
        "scope": "normalized coordinate complex and contraction; the all-n support proof is in the paper",
        "normalized_degrees_checked": [0, 8],
        "normalized_components": normalized,
        "differential": d,
        "contraction": h,
        "top_indicator": indicator,
        "assertion_count": assertions,
        "runtime_seconds": time.perf_counter() - start,
    }
    target = Path(__file__).resolve().parents[1] / "logs" / "B_pair_parameter_certificate.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "assertion_count": assertions, "runtime_seconds": result["runtime_seconds"], "output": str(target)}))


if __name__ == "__main__":
    main()
