#!/usr/bin/env python3
"""Exact finite certificate for D.HF.5--9.

This checks integer monomial exponents, finite colon-semigroup tests,
endpoint restriction matrices and the internal branch substitutions.
It does not prove descent, duality, cohomology, or family classification.
Use --output PATH for an independent audit run without replacing the
author's retained output.
"""
import argparse
import hashlib
import json
import time
from pathlib import Path

START = time.perf_counter()
ASSERTIONS = 0


def check(condition, description):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(description)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


ONE = (0, 0, 0)
U = (1, 0, 0)


def ideal_generators(a):
    return [ONE] if a == 0 else [U, (0, 0, a)]


def hom_generators(a, b):
    if a == b:
        return [ONE]
    if b > a:
        return [U, (0, 0, b - a)]
    return [ONE, (0, 1, -(a - b))]


def cover_exponents(n, monomial):
    u, v, w = monomial
    return n * u + w, n * v + w


def chart_exponents(n, i, monomial):
    u, v, w = monomial
    return (i + 1) * u + (n - i - 1) * v + w, i * u + (n - i) * v + w


def in_ring(n, exponents):
    x, y = exponents
    return x >= 0 and y >= 0 and (x - y) % n == 0


def in_monomial_module(n, exponents, generators):
    return any(in_ring(n, sub(exponents, cover_exponents(n, g))) for g in generators)


endpoint_cases = {}
for n in range(2, 51):
    for a in range(n):
        for b in range(n):
            gens = hom_generators(a, b)
            for h in gens:
                for g in ideal_generators(a):
                    check(in_monomial_module(n, cover_exponents(n, add(h, g)),
                                             ideal_generators(b)),
                          ("colon-generator inclusion", n, a, b, h, g))

            left_source = U if a else ONE
            left_target = U if b else ONE
            right_source = (0, 0, a) if a else ONE
            right_target = (0, 0, b) if b else ONE
            left_orders, right_orders = [], []
            constant_columns = []
            for h in gens:
                left = chart_exponents(n, 0, add(h, sub(left_source, left_target)))
                right = chart_exponents(n, n - 1, add(h, sub(right_source, right_target)))
                check(min(left) >= 0, ("regular left coefficient", n, a, b, h, left))
                check(min(right) >= 0, ("regular right coefficient", n, a, b, h, right))
                if left[1] == 0:
                    left_orders.append(left[0])
                if right[0] == 0:
                    right_orders.append(right[1])
                constant_columns.append((int(left == (0, 0)), int(right == (0, 0))))
                if a != b:
                    check(not (left[1] == 0 and right[0] == 0),
                          ("distinct-character generators have disjoint endpoint support",
                           n, a, b, h, left, right))
            check(bool(left_orders) and bool(right_orders), ("both endpoint images", n, a, b))
            if a == b:
                check(constant_columns == [(1, 1)], ("diagonal equal-constant condition", n, a))
                defect = 1
                case = "equal"
            else:
                defect = min(left_orders) + min(right_orders)
                case = ("source_trivial" if a == 0 else
                        "target_trivial" if b == 0 else
                        "increasing" if a < b else "decreasing")
            expected = 1 + int(a > 0 and b == 0) - int(a == 0 and b > 0)
            check(defect == expected, ("endpoint cokernel dimension", n, a, b, defect, expected))
            endpoint_cases[case] = endpoint_cases.get(case, 0) + 1

# Independent finite semigroup comparison of each colon with its generators.
semigroup_cases = 0
for n in range(2, 11):
    for a in range(n):
        for b in range(n):
            for x in range(-n, 2 * n + 1):
                for y in range(-n, 2 * n + 1):
                    if (x - y) % n:
                        continue
                    actual = all(in_monomial_module(n, add((x, y), cover_exponents(n, g)),
                                                     ideal_generators(b))
                                 for g in ideal_generators(a))
                    proposed = in_monomial_module(n, (x, y), hom_generators(a, b))
                    check(actual == proposed, ("colon semigroup equality", n, a, b, x, y))
                    semigroup_cases += 1

internal_cases = []
for m in range(1, 41):
    n, i = 3 * m, m - 1
    check(chart_exponents(n, i, U)[0] == m, ("internal u order", m))
    check(chart_exponents(n, i, (0, 1, 0))[0] == 2 * m, ("internal v order", m))
    check(chart_exponents(n, i, (0, 0, 1))[0] == 1, ("internal w parameter", m))
    for a in (m, 2 * m):
        quotient = chart_exponents(n, i, sub((0, 0, a), U))
        check(min(quotient) >= 0, ("u generates full ideal on the internal chart", m, a))
    orders = [chart_exponents(n, i, h)[0] for h in hom_generators(m, 2 * m)]
    check(orders == [m, m], ("internal image is exactly (w^m)", m, orders))
    item = {"m": m, "N": n, "framed_dimension": m}
    if m % 2:
        residue, period = 2 % n, 1
        while residue != 1:
            residue = (2 * residue) % n
            period += 1
            check(period <= n, ("finite prime-to-two multiplicative order", m, period))
        check(pow(2, period, n) == 1, ("fixed-characteristic Frobenius period", m, period))
        check((pow(2, period, n) * m - m) % n == 0, ("first periodic character", m))
        check((pow(2, period, n) * 2 * m - 2 * m) % n == 0, ("second periodic character", m))
        item["characteristic_two_period"] = period
    internal_cases.append(item)

# A finite multiplicity check of the closed dimension formula.
for n in range(2, 11):
    for seed in range(1, 11):
        r = [(seed + 2 * a) % 4 for a in range(n)]
        s = [(2 * seed + a) % 4 for a in range(n)]
        total = sum(r[a] * s[b] * (1 + int(a > 0 and b == 0) - int(a == 0 and b > 0))
                    for a in range(n) for b in range(n))
        rank_r, rank_s = sum(r), sum(s)
        formula = rank_r * rank_s + rank_r * s[0] - r[0] * rank_s
        check(total == formula, ("sum of rank-one defects", n, seed))
        check(0 <= total <= 2 * rank_r * rank_s, ("two-end rank bound", n, seed))

parser = argparse.ArgumentParser()
parser.add_argument("--output", type=Path,
                    default=Path(__file__).resolve().parents[1] / "output" / "RDP_Hom_framing.json")
args = parser.parse_args()
result = {
    "status": "PASS",
    "statement_labels": [
        "D:RDP-full-Hom-vanishing",
        "D:A-chain-two-end-Hom-bound",
        "D:A-chain-internal-framing-obstruction",
    ],
    "assertions": ASSERTIONS,
    "elapsed_seconds": time.perf_counter() - START,
    "endpoint_N_range": [2, 50],
    "endpoint_cases": endpoint_cases,
    "colon_semigroup_N_range": [2, 10],
    "colon_semigroup_cases": semigroup_cases,
    "internal_cases": internal_cases,
    "scope": "Finite exact integer/monomial certificate; geometric arguments remain in the proof.",
    "program_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
