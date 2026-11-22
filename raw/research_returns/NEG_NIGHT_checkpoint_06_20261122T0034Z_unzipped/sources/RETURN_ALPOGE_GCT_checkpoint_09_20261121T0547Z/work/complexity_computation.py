"""Finite sanity checks of the stated encodings, not formal certificates.

Run from the workspace root with Python 3.  No external package is required.
The ETH theorem itself and its asymptotic complexity are not executed or tested.
"""

import itertools
import json
import math
import random
from datetime import datetime, timezone
from pathlib import Path


def gate_checks():
    checked = 0
    for table in itertools.product((0, 1), repeat=4):
        forbidden = [(a, b, 1 - table[2 * a + b])
                     for a, b in itertools.product((0, 1), repeat=2)]
        # A clause forbidding t has literals x_i if t_i=0 and not x_i otherwise.
        for triple in itertools.product((0, 1), repeat=3):
            clause_values = [any(x != t for x, t in zip(triple, bad))
                             for bad in forbidden]
            assert all(clause_values) == (triple[2] == table[2 * triple[0] + triple[1]])
            checked += 1
    return checked


def chain_count(bits):
    d = len(bits)
    if not d:
        return 0
    total = 0
    for internal in itertools.product((0, 1), repeat=d - 1):
        states = (0,) + internal + (1,)
        total += all(states[j] + bits[j] == states[j + 1] for j in range(d))
    return total


def chain_checks():
    checked = 0
    for d in range(1, 9):
        for bits in itertools.product((0, 1), repeat=d):
            assert chain_count(bits) == int(sum(bits) == 1)
            checked += 1
    return checked


def permanent_by_permutations(a):
    return sum(math.prod(a[i][p[i]] for i in range(len(a)))
               for p in itertools.permutations(range(len(a))))


def permanent_by_chain_factors(a):
    n = len(a)
    edges = [(i, j) for i in range(n) for j in range(n) if a[i][j]]
    rows = [[k for k, (i, _) in enumerate(edges) if i == v] for v in range(n)]
    cols = [[k for k, (_, j) in enumerate(edges) if j == v] for v in range(n)]
    if any(not indices for indices in rows + cols):
        return 0
    total = 0
    # Each chain factor is itself contracted by the exhaustive chain_count above.
    factors = {d: {bits: chain_count(bits)
                   for bits in itertools.product((0, 1), repeat=d)}
               for d in {len(indices) for indices in rows + cols}}
    for bits in itertools.product((0, 1), repeat=len(edges)):
        count = math.prod(factors[len(indices)][tuple(bits[k] for k in indices)]
                          for indices in rows + cols)
        if count:
            total += count * math.prod(a[i][j] if bits[k] else 1
                                      for k, (i, j) in enumerate(edges))
    return total


def permanent_checks():
    matrices = []
    for n in (1, 2):
        for values in itertools.product((-1, 0, 1), repeat=n * n):
            matrices.append([list(values[n * i:n * (i + 1)]) for i in range(n)])
    rng = random.Random(20261120)
    for n, examples in ((3, 120), (4, 30)):
        for _ in range(examples):
            matrices.append([[rng.choice((-2, -1, 0, 0, 1, 2)) for _ in range(n)]
                             for _ in range(n)])
    for a in matrices:
        per = permanent_by_permutations(a)
        assert permanent_by_chain_factors(a) == per
        n = len(a)
        e = sum(x != 0 for row in a for x in row)
        max_weight = max(abs(x) for row in a for x in row)
        b = (max_weight - 1).bit_length() if max_weight else 0
        p = e + n * b + 2
        assert abs(per) <= 2 ** (e + n * b)
        residue = per % (2 ** p)
        signed = residue if residue < 2 ** (p - 1) else residue - 2 ** p
        assert signed == per
    return len(matrices)


def grid_checks():
    checked = 0
    for p, r, degree in ((2, 2, 1), (3, 2, 2), (5, 2, 2)):
        monomials = [exponents for exponents in itertools.product(range(degree + 1), repeat=r)
                     if sum(exponents) <= degree]
        points = list(itertools.product(range(p), repeat=r))
        evaluations = [[math.prod(pow(x, e, p) for x, e in zip(point, exponents)) % p
                        for exponents in monomials] for point in points]
        for coefficients in itertools.product(range(p), repeat=len(monomials)):
            nonzero_on_grid = any(sum(a * b for a, b in zip(coefficients, row)) % p
                                  for row in evaluations)
            assert bool(nonzero_on_grid) == any(coefficients)
            checked += 1
    # Degree restriction is essential: this nonzero formal polynomial vanishes everywhere.
    assert all((x ** 3 - x) % 3 == 0 for x in range(3))
    return checked


def shifted_ray_checks():
    checked = 0
    for s in range(121):
        coefficient = s // 3 + int(s % 2 == 0)
        lattice_count = sum(1 for z in (0, 1)
                            for t in range(-4, s + 2)
                            if 3 * t + 4 * z >= s and 2 * t + 4 * z <= s)
        assert lattice_count == coefficient
        checked += 1
    return checked


def main():
    checks = {
        "C-COUNT-01_all_binary_gate_tables": gate_checks(),
        "C-COUNT-02_exact_one_chains": chain_checks(),
        "C-COUNT-02_signed_permanent_instances": permanent_checks(),
        "C-PIT-01_bounded_degree_grid_polynomials": grid_checks(),
        "P-F1_shifted_ray_parameters": shifted_ray_checks(),
    }
    report = {
        "date_utc": datetime.now(timezone.utc).isoformat(),
        "model": "GPT-6 Astra Pro",
        "effort": "inherited/undisclosed",
        "run": "/root/complexity",
        "result": "PASS",
        "scope": "Finite exhaustive and seeded sanity checks only; no formal proof certificate or execution of the supplied ETH algorithm.",
        "checked_cases": checks,
    }
    output = Path(__file__).with_name("complexity_computation.json")
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
