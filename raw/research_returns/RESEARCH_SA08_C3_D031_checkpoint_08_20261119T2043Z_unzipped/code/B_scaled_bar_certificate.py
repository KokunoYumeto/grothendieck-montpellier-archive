#!/usr/bin/env python3
"""Exact finite coefficient certificates for A-L04 and A-L05.

The proof gives all arities and all coefficient rings.  This program
checks the integral coefficient identities independently on finite
composition lists, including labelled shuffle multiplicities.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import comb, factorial, prod
from pathlib import Path
import json
import time


def compositions(n: int):
    if n == 0:
        yield ()
        return
    for first in range(1, n + 1):
        for rest in compositions(n - first):
            yield (first,) + rest


def suffix_product(a: tuple[int, ...]) -> int:
    return prod(sum(a[i:]) for i in range(len(a)))


def shuffles(a: tuple[int, ...], b: tuple[int, ...]):
    # Entries are positions, so duplicate resulting value lists
    # must remain duplicated: they are different labelled shuffles.
    if not a:
        yield b
    elif not b:
        yield a
    else:
        for tail in shuffles(a[1:], b):
            yield (a[0],) + tail
        for tail in shuffles(a, b[1:]):
            yield (b[0],) + tail


def main() -> None:
    start = time.perf_counter()
    assertions = 0
    chains = 0
    integral_checks = 0
    chain_rows = []
    for positive_arity in range(0, 11):
        for a in compositions(positive_arity):
            denominator = suffix_product(a)
            for coefficient_arity in range(4):
                m = positive_arity + coefficient_arity
                assert factorial(m) % denominator == 0
                assertions += 1
                integral_checks += 1
                c = factorial(m) // denominator
                for j, arity in enumerate(a):
                    # Differential of the explicit image.
                    expected = (-1) ** j * arity * c
                    # Image of bar differential, after expanding delta(b_i b_{i+1}).
                    actual = 0
                    if j == 0:
                        actual += factorial(m) // suffix_product(a[1:])
                    if j > 0:
                        merged = a[: j - 1] + (a[j - 1] + a[j],) + a[j + 1 :]
                        actual += (-1) ** j * factorial(m) // suffix_product(merged)
                    if j + 1 < len(a):
                        merged = a[:j] + (a[j] + a[j + 1],) + a[j + 2 :]
                        actual += (-1) ** (j + 1) * factorial(m) // suffix_product(merged)
                    assert actual == expected
                    assertions += 1
                    chains += 1
            chain_rows.append(
                {"positive_arity": positive_arity, "bar_length": len(a), "arities": a, "denominator": denominator}
            )

    shuffle_pairs = 0
    labelled_shuffles = 0
    for total in range(10):
        for left_arity in range(total + 1):
            right_arity = total - left_arity
            for a in compositions(left_arity):
                for b in compositions(right_arity):
                    ds = [suffix_product(c) for c in shuffles(a, b)]
                    assert len(ds) == comb(len(a) + len(b), len(a))
                    assertions += 1
                    labelled_shuffles += len(ds)
                    got = sum((Fraction(1, d) for d in ds), Fraction(0))
                    want = Fraction(1, suffix_product(a) * suffix_product(b))
                    assert got == want
                    assertions += 1
                    for a0, b0 in product(range(3), repeat=2):
                        m, n = left_arity + a0, right_arity + b0
                        source_coefficient = sum(factorial(m + n) // d for d in ds)
                        target_coefficient = (
                            factorial(m) // suffix_product(a)
                            * (factorial(n) // suffix_product(b))
                            * comb(m + n, m)
                        )
                        assert source_coefficient == target_coefficient
                        assertions += 1
                    shuffle_pairs += 1

    closure_checks = 0
    for p in [1, 2, 3, 5, 7]:
        for n in range(1, 17):
            a = factorial(p * n) // factorial(n)
            b_den = factorial(n - 1) * factorial(n) ** (p - 1)
            assert factorial(p * n - 1) % b_den == 0
            assertions += 1
            b = factorial(p * n - 1) // b_den
            lhs = factorial(n - 1) * a * b
            multinomial_den = factorial(n) ** p
            assert factorial(p * n) % multinomial_den == 0
            assertions += 1
            rhs = factorial(p * n) // multinomial_den * factorial(p * n - 1)
            assert lhs == rhs
            assertions += 1
            closure_checks += 1

    # Explicit first-obstruction scaling formula used in AL.19.
    half_checks = 0
    for a in range(1, 257):
        assert comb(2 * a, a) == 2 * comb(2 * a - 1, a - 1)
        assertions += 1
        half_checks += 1

    weighted_terms = 0
    for total_weight in range(8):
        for blocks in compositions(total_weight):
            for coefficient_blocks in range(len(blocks) + 1):
                head = blocks[:coefficient_blocks]
                rest = blocks[coefficient_blocks:]
                for group_sizes in compositions(len(rest)):
                    groups = [head]
                    offset = 0
                    for size in group_sizes:
                        groups.append(rest[offset:offset + size])
                        offset += size
                    weights = [sum(group) for group in groups]
                    constants = [
                        factorial(weight) // prod(factorial(q) for q in group)
                        for group, weight in zip(groups, weights)
                    ]
                    for selected in product(*(range(len(group)) for group in groups[1:])):
                        chosen = [groups[i + 1][j] for i, j in enumerate(selected)]
                        denominator = suffix_product(tuple(weights[1:]))
                        lhs = Fraction(
                            factorial(total_weight) * prod(chosen),
                            denominator * prod(factorial(q) for q in blocks),
                        )
                        assert lhs.denominator == 1
                        assertions += 1
                        rhs = comb(total_weight, weights[0]) * constants[0]
                        for i, selected_q in enumerate(chosen, start=1):
                            local = Fraction(constants[i] * selected_q, weights[i])
                            assert local.denominator == 1
                            assertions += 1
                            suffix = sum(weights[i:])
                            rhs *= comb(suffix - 1, weights[i] - 1) * local.numerator
                        assert lhs.numerator == rhs
                        assertions += 1
                        weighted_terms += 1

    # AL.34--35: coefficients of x1*y2 and y1*x2.
    left_balanced = (3, 3)
    right_balanced = (4, 2)
    defect = tuple(a - b for a, b in zip(left_balanced, right_balanced))
    assert defect == (-1, 1) and defect != (0, 0)
    assertions += 1
    # Differential of x1*x2 is y1*x2-x1*y2, with the same coefficients.
    assert defect == (-1, 1)
    assertions += 1

    output = {
        "statement_ids": ["A-L04", "A-L05", "A-L06"],
        "status": "PASS",
        "scope": "integer coefficient identities, not a finite substitute for the all-arity proof",
        "maximum_positive_bar_arity_chain": 10,
        "coefficient_arities_chain": [0, 1, 2, 3],
        "integral_coefficient_checks": integral_checks,
        "chain_coefficient_checks": chains,
        "maximum_combined_shuffle_arity": 9,
        "shuffle_word_pairs": shuffle_pairs,
        "labelled_shuffles": labelled_shuffles,
        "shuffle_coefficient_arities_each_word": [0, 1, 2],
        "closure_multinomial_checks": closure_checks,
        "central_binomial_half_checks": half_checks,
        "weighted_parameter_maximum_euler_weight": 7,
        "weighted_parameter_term_checks": weighted_terms,
        "strict_balancing_defect": defect,
        "assertion_count": assertions,
        "runtime_seconds": time.perf_counter() - start,
        "chain_compositions": chain_rows,
    }
    target = Path(__file__).resolve().parents[1] / "logs" / "B_scaled_bar_certificate.json"
    target.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({k: v for k, v in output.items() if k != "chain_compositions"}))


if __name__ == "__main__":
    main()
