#!/usr/bin/env python3
"""Independent exact check of the radial rank-profile Farkas certificates.

Reconstruct inequalities from their mathematical labels, without importing
the system generator, trusting stored row indices, or invoking an LP solver.
Layer-pair existence is verified by an intersection-size formula on the
full D-cube, independently of the generator's quotient-cube enumeration.
"""
import json
import hashlib
import math
import sys
from fractions import Fraction
from pathlib import Path


def check(path):
    data = json.loads(path.read_text())
    D, m = data["D"], data["m"]
    assert 2 <= D and 3 <= m
    M, n, layers = 2 ** (D - 1), m * D, D // 2 + 1
    weights = [math.comb(D, a) // (2 if 2 * a == D else 1)
               for a in range(layers)]
    assert sum(weights) == M
    totals = {}
    rhs = Fraction(0)
    count = 0

    def index(term, a, t):
        assert term in (0, 1) and 0 <= a < layers and 1 <= t <= n
        return (term * layers + a) * n + t - 1

    def exists(a, b, h):
        assert 0 <= a < layers and 0 <= b < layers
        return any(min(a + b - 2 * i, D - a - b + 2 * i) == h
                   for i in range(max(0, a + b - D), min(a, b) + 1))

    for entry in data["certificate"]:
        coeff = Fraction(entry["numerator"], entry["denominator"])
        assert coeff >= 0
        label = entry["label"]
        kind, tail = label[0], label[1:]
        terms, bound = [], 0
        if kind == "monotone":
            term, a, t = tail
            terms = [(index(term, a, t + 1), 1), (index(term, a, t), -1)]
        elif kind == "budget":
            term, = tail
            terms = [(index(term, a, t), weights[a])
                     for a in range(layers) for t in range(1, n + 1)]
            bound = (m - 1) * D * M - 1
        elif kind == "mixed":
            a, b, h, alternative = tail
            assert exists(a, b, h) and alternative in (0, 1)
            L = m * (D - h)
            terms = [(index(0, a, L - 1 + alternative), -1),
                     (index(1, b, L - alternative), -1)]
            bound = -1
        elif kind == "lipschitz":
            term, a, b, t = tail
            assert exists(a, b, 1) and 2 * m < t <= n
            terms = [(index(term, a, t), 1), (index(term, b, t - 2 * m), -1)]
        elif kind == "low_cut":
            assert not tail
            terms = [(index(0, 0, (m - 2) * D), 1)]
        elif kind == "exact_low_upper":
            t, = tail
            assert t == data["low_value"] and 0 <= t <= (m - 2) * D - 1
            terms = [(index(0, 0, t + 1), 1)]
        elif kind in ("exact_low_lower", "other_global_lower"):
            a, t = tail
            assert t == data["low_value"] and 1 <= t <= (m - 2) * D - 1
            assert a == 0 or data["global_min"]
            term = 0
            if kind == "other_global_lower":
                assert data["global_min"] and data["minimum_both"]
                term = 1
            terms = [(index(term, a, t), -1)]
            bound = -1
        elif kind in ("lower", "upper"):
            j, = tail
            assert 0 <= j < 2 * layers * n
            terms = [(j, 1 if kind == "upper" else -1)]
            bound = 1 if kind == "upper" else 0
        else:
            raise AssertionError(label)
        for j, v in terms:
            totals[j] = totals.get(j, Fraction(0)) + coeff * v
        rhs += coeff * bound
        count += 1
    assert all(v == 0 for v in totals.values())
    assert rhs == -1
    return {"file": str(path), "dimension": D, "width": m,
            "certificate_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "low_value": data.get("low_value"),
            "minimum_both": data.get("minimum_both", False),
            "certificate_entries": count,
            "all_coefficients_nonnegative": True,
            "all_used_layer_pairs_exist": True,
            "exact_variable_cancellation": True, "exact_rhs": str(rhs),
            "solver_used_by_verifier": False, "result": "PASS"}


if __name__ == "__main__":
    config = json.loads(Path(sys.argv[1]).read_text())
    result = {"checks": [check(Path(p)) for p in config["certificates"]]}
    Path(sys.argv[2]).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
