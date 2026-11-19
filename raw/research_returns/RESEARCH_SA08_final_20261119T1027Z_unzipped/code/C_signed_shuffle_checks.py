#!/usr/bin/env python3
"""Exact finite certificate for the signed Lyndon PD basis used in C24.

This checks triangularity over Z, with every parity on alphabets of size
two through length eight and size three through length five. It does not
replace the general Lyndon-factorization and signed-count proof.
"""
from collections import Counter
from functools import lru_cache
from itertools import product
from math import factorial
import json
import time
from pathlib import Path


def lyndon_factors(word):
    result = []
    i = 0
    while i < len(word):
        j, k = i + 1, i
        while j < len(word) and word[k] <= word[j]:
            k = i if word[k] < word[j] else k + 1
            j += 1
        size = j - k
        while i <= k:
            result.append(word[i:i + size])
            i += size
    return result


def run_case(alphabet_size, max_length, parities):
    @lru_cache(None)
    def parity(word):
        return sum(parities[a] for a in word) % 2

    @lru_cache(None)
    def shuffle(left, right):
        if not left:
            return ((right, 1),)
        if not right:
            return ((left, 1),)
        out = Counter()
        for word, coefficient in shuffle(left[1:], right):
            out[(left[0],) + word] += coefficient
        sign = -1 if parity(left) * parities[right[0]] else 1
        for word, coefficient in shuffle(left, right[1:]):
            out[(right[0],) + word] += sign * coefficient
        return tuple((word, c) for word, c in out.items() if c)

    def multiply(left, right):
        out = Counter()
        for a, ca in left.items():
            for b, cb in right.items():
                for word, c in shuffle(a, b):
                    out[word] += ca * cb * c
        return {word: c for word, c in out.items() if c}

    @lru_cache(None)
    def divided_power(generator, exponent):
        assert parity(generator) == 0
        expansion = {(): 1}
        for _ in range(exponent):
            expansion = multiply(expansion, {generator: 1})
        divisor = factorial(exponent)
        assert all(c % divisor == 0 for c in expansion.values())
        return tuple((word, c // divisor) for word, c in expansion.items())

    count = 0
    odd_square_checks = set()
    largest_support = 0
    for length in range(max_length + 1):
        for word in product(range(alphabet_size), repeat=length):
            factors = lyndon_factors(word)
            assert tuple(a for factor in factors for a in factor) == word
            assert all(factors[j] >= factors[j + 1]
                       for j in range(len(factors) - 1))
            expansion = {(): 1}
            for factor, multiplicity in Counter(factors).items():
                if parity(factor) == 0:
                    block = dict(divided_power(factor, multiplicity))
                else:
                    pairs, remainder = divmod(multiplicity, 2)
                    block = dict(divided_power(factor + factor, pairs))
                    if remainder:
                        block = multiply(block, {factor: 1})
                    if 2 * len(factor) <= max_length:
                        assert not dict(shuffle(factor, factor))
                        odd_square_checks.add(factor)
                expansion = multiply(expansion, block)
            assert expansion.get(word) == 1, (parities, word, expansion)
            assert all(term <= word for term in expansion), (parities, word)
            count += 1
            largest_support = max(largest_support, len(expansion))
    return {
        "alphabet_size": alphabet_size,
        "max_length": max_length,
        "parities": list(parities),
        "triangular_columns": count,
        "odd_square_checks": len(odd_square_checks),
        "largest_column_support": largest_support,
        "status": "PASS",
    }


def main():
    started = time.perf_counter()
    cases = []
    for alphabet_size, max_length in ((2, 8), (3, 5)):
        for parities in product((0, 1), repeat=alphabet_size):
            cases.append(run_case(alphabet_size, max_length, parities))
    receipt = {
        "statement": "C24 signed Lyndon PD/exterior triangular basis",
        "integer_arithmetic": True,
        "cases": cases,
        "total_triangular_columns": sum(c["triangular_columns"] for c in cases),
        "runtime_seconds": time.perf_counter() - started,
        "status": "PASS",
    }
    path = Path(__file__).resolve().parents[1] / "logs/C_signed_shuffle_checks.json"
    path.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({k: v for k, v in receipt.items() if k != "cases"}, indent=2))


if __name__ == "__main__":
    main()
