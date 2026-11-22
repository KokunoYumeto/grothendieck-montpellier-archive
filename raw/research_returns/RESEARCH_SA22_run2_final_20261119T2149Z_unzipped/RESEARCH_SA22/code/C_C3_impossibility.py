#!/usr/bin/env python3
"""Exact certificate for C:C3-coverage-obstruction.

Enumerate every reflection-compatible chain family at each label of C3.
The exact-kernel datum makes the indexing group a subgroup of C3; the
trivial subgroup is covered by making the other two families empty.
No randomized or floating-point mathematical calculation is used.
"""
import itertools
import json
import platform
import time
from datetime import datetime, timezone
from pathlib import Path


GROUP = range(3)
FULL = 7


def points(mask):
    return [x for x in GROUP if mask & (1 << x)]


def subset(a, b):
    return (a & b) == a


def is_chain(family):
    return all(subset(a, b) or subset(b, a) for a in family for b in family)


def translate(mask, shift):
    return sum(1 << ((x + shift) % 3) for x in points(mask))


def reflect(mask, label):
    return sum(1 << ((label - x) % 3) for x in points(mask))


def convolution(a, b):
    output = [0, 0, 0]
    for x in points(a):
        for y in points(b):
            output[(x + y) % 3] += 1
    return tuple(output)


def vector_convolution(a, b):
    return tuple(sum(a[x] * b[(z - x) % 3] for x in GROUP) for z in GROUP)


def in_chain_cone(vector, family):
    # Nonnegative integer vector belongs to a nested-indicator cone iff
    # all its nonempty positive superlevel sets occur in the chain.
    for level in set(vector) - {0}:
        mask = sum(1 << x for x in GROUP if vector[x] >= level)
        if mask not in family:
            return False
    return True


def candidate_families(label):
    symmetric = [mask for mask in range(8) if reflect(mask, label) == mask]
    families = []
    for count in range(len(symmetric) + 1):
        for family in itertools.combinations(symmetric, count):
            if is_chain(family):
                families.append(family)
    assert len(families) == 12
    return families


def convolution_closed(system):
    for h, k in itertools.product(GROUP, repeat=2):
        output_family = system[(h + k) % 3]
        for a, b in itertools.product(system[h], system[k]):
            if not in_chain_cone(convolution(a, b), output_family):
                return False
    return True


def aligned(system):
    for left, right in itertools.product(system, repeat=2):
        if not any(is_chain(left + tuple(translate(a, s) for a in right)) for s in GROUP):
            return False
    return True


def main():
    start = time.perf_counter()
    families = [candidate_families(label) for label in GROUP]
    counts = {
        "total_systems": 0,
        "systems_with_two_element_generator": 0,
        "convolution_closed_systems": 0,
        "convolution_closed_with_two_element_generator": 0,
        "all_printed_axioms_systems": 0,
        "all_printed_axioms_with_two_element_generator": 0,
    }
    for system in itertools.product(*families):
        counts["total_systems"] += 1
        has_pair = any(mask.bit_count() == 2 for family in system for mask in family)
        counts["systems_with_two_element_generator"] += has_pair
        if not convolution_closed(system):
            continue
        counts["convolution_closed_systems"] += 1
        counts["convolution_closed_with_two_element_generator"] += has_pair
        if aligned(system):
            counts["all_printed_axioms_systems"] += 1
            counts["all_printed_axioms_with_two_element_generator"] += has_pair
    assert counts["total_systems"] == 1728
    assert counts["convolution_closed_with_two_element_generator"] == 0
    assert counts["all_printed_axioms_with_two_element_generator"] == 0

    algebra = []
    for missing in GROUP:
        a = FULL ^ (1 << missing)
        vector = tuple(int(x in points(a)) for x in GROUP)
        square = convolution(a, a)
        cube = vector_convolution(square, vector)
        singleton = tuple(int(x == (2 * missing) % 3) for x in GROUP)
        singleton_cube = vector_convolution(vector_convolution(singleton, singleton), singleton)
        assert square == tuple(1 + int(x == (2 * missing) % 3) for x in GROUP)
        assert cube == (2, 3, 3)
        assert singleton_cube == (1, 0, 0)
        algebra.append({"missing": missing, "square": square, "cube": cube,
                        "singleton_cube": singleton_cube})

    output = {
        "theorem": "C:C3-coverage-obstruction",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "arithmetic": "exact integers and finite set masks",
        "scope": "All chain and reflection families on C3 with rho=id; empty families and empty sets allowed.",
        "families_per_label": [len(f) for f in families],
        "counts": counts,
        "convolution_identities": algebra,
        "assertions_passed": True,
        "runtime_seconds": time.perf_counter() - start,
    }
    destination = Path(__file__).resolve().parent.parent / "logs" / "C_C3_impossibility.json"
    destination.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
