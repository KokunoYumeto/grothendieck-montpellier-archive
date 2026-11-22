#!/usr/bin/env python3
"""Finite checks accompanying the proofs; never substitutes for them.

The Artin--Schreier orbit target retains one more exponent than the source.
Truncating both at the same exponent would falsely erase the obstruction.
The A5 computation checks the abstract group example in the supplied reading.
All arithmetic is exact; there are no external package dependencies.
"""
from itertools import permutations
from pathlib import Path
import csv
import json


def rank_mod(matrix, p):
    a = [list(row) for row in matrix]
    rows, cols = len(a), len(a[0]) if a else 0
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        z = pow(a[rank][col] % p, -1, p)
        a[rank] = [(x*z) % p for x in a[rank]]
        for i in range(rows):
            if i != rank and a[i][col] % p:
                z = a[i][col] % p
                a[i] = [(x-z*y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def as_checks():
    records = []
    for p in (2, 3):
        for last_source in range(10):
            # F(e_r)-e_r = e_{r+1}-e_r, with coefficients in F_p.
            cols, rows = last_source+1, last_source+2
            matrix = [[0]*cols for _ in range(rows)]
            for col in range(cols):
                matrix[col][col] = p-1
                matrix[col+1][col] = 1
            augmented = [row+[int(i == 0)] for i, row in enumerate(matrix)]
            r = rank_mod(matrix, p)
            ra = rank_mod(augmented, p)
            assert r == cols and ra == cols+1
            records.append({"p": p, "last_source_exponent": last_source,
                            "source_dimension": cols, "target_dimension": rows,
                            "rank": r, "augmented_rank_for_e0": ra,
                            "e0_in_image": False})
    return records


def compose(a, b):
    return tuple(a[b[i]] for i in range(5))


def inverse(a):
    result = [0]*5
    for i, ai in enumerate(a):
        result[ai] = i
    return tuple(result)


def even(a):
    return sum(a[i] > a[j] for i in range(5) for j in range(i+1, 5)) % 2 == 0


def a5_checks():
    group = {a for a in permutations(range(5)) if even(a)}
    identity = tuple(range(5))
    commutators = {compose(compose(compose(a, b), inverse(a)), inverse(b))
                   for a in group for b in group}
    generated = {identity}
    frontier = [identity]
    while frontier:
        x = frontier.pop()
        for c in commutators:
            y = compose(x, c)
            if y not in generated:
                generated.add(y)
                frontier.append(y)
    assert len(group) == 60 and generated == group
    return {"order": len(group), "distinct_commutators": len(commutators),
            "commutator_subgroup_order": len(generated), "perfect": True,
            "finite_tuple_pigeonhole_bound": "For d generators, 60^d possible coordinate tuples."}


def multiplicative_orders():
    rows = []
    for n in range(1, 9):
        modulus = 3**n
        power, f = 2 % modulus, 1
        while power != 1:
            power = (power*2) % modulus
            f += 1
        assert f == 2*3**(n-1)
        rows.append({"n": n, "scalar_order": modulus,
                     "ord_3n_2": f, "field_dimension_of_Vn": n,
                     "F2_dimension_of_Vn": n*f,
                     "generator_lower_bound": n})
    return rows


def main():
    out = Path(__file__).resolve().parents[1] / "output"
    out.mkdir(exist_ok=True)
    for name, rows in (("artin_schreier_orbits.csv", as_checks()),
                       ("metabelian_factors.csv", multiplicative_orders())):
        with (out/name).open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    result = {"artin_schreier": "20 exact rank checks passed; target overflow retained",
              "a5": a5_checks(),
              "metabelian": "Orders checked n=1,...,8; full non-generation proof is symbolic",
              "scope": "Finite computations corroborate but do not replace the infinite proofs."}
    (out/"checks.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
