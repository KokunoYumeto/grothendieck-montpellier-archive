"""Finite exact corroboration of the carry-free coherent-seed lemma."""
from itertools import combinations, product
from pathlib import Path
import json


def exchange_rows(w, r, bases):
    ix = {b: i for i, b in enumerate(bases)}
    rows = []
    for common in combinations(range(w), r - 2):
        remaining = [i for i in range(w) if i not in common]
        for a, b, c, d in combinations(remaining, 4):
            def loc(x, y):
                return ix[tuple(sorted(common + (x, y)))]
            pairings = [(loc(a, b), loc(c, d)),
                        (loc(a, c), loc(b, d)),
                        (loc(a, d), loc(b, c))]
            for other in pairings[1:]:
                row = [0] * len(bases)
                for j in pairings[0]:
                    row[j] += 1
                for j in other:
                    row[j] -= 1
                rows.append(row)
    return rows


out = []
for w, r in [(4, 2), (5, 2), (5, 3), (6, 3)]:
    bases = list(combinations(range(w), r))
    ell = (len(bases) - 1).bit_length()
    code = [tuple((i >> (ell - j - 1)) & 1 for j in range(ell))
            for i in range(len(bases))]
    exchanges = exchange_rows(w, r, bases)

    def coherent(values):
        return all(sum(a * b for a, b in zip(row, values)) == 0
                   for row in exchanges)

    good = [coherent([c[j] for c in code]) for j in range(ell)]
    good_seeds = []
    for seed in product([0, 1], repeat=ell):
        weights = [sum(6 ** (ell - j - 1) * seed[j] * c[j]
                       for j in range(ell)) for c in code]
        test = coherent(weights)
        expected = all(not seed[j] or good[j] for j in range(ell))
        assert test == expected
        if test:
            good_seeds.append(seed)

    tested = set()
    for j, is_good in enumerate(good):
        if not is_good:
            continue
        values = [c[j] for c in code]
        if len(set(values)) == 1:
            continue
        witnesses = [u for u in range(w)
                     if values == [int(u in b) for b in bases]
                     or values == [int(u not in b) for b in bases]]
        assert len(witnesses) == 1
        tested.add(witnesses[0])

    untested = [u for u in range(w) if u not in tested]
    collision = None
    if len(untested) >= 2:
        u, v = untested[:2]
        common = tuple(i for i in range(w) if i not in [u, v])[:r - 1]
        a = bases.index(tuple(sorted(common + (u,))))
        b = bases.index(tuple(sorted(common + (v,))))
        for seed in good_seeds:
            wa = sum(6 ** (ell - j - 1) * seed[j] * code[a][j]
                     for j in range(ell))
            wb = sum(6 ** (ell - j - 1) * seed[j] * code[b][j]
                     for j in range(ell))
            assert wa == wb
        collision = [bases[a], bases[b]]
    out.append(dict(w=w, r=r, ell=ell, coherent_bits=good,
                    coherent_seed_count=len(good_seeds),
                    tested_elements=sorted(tested), collision=collision,
                    exact_coordinate_face=True))

result = dict(instances=out,
              scope="Exact finite checks; the general proof is I-27.")
Path(__file__).with_name("I27_computation_checks.json").write_text(
    json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
