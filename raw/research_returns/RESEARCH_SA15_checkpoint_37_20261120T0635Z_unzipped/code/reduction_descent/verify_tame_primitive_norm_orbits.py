#!/usr/bin/env python3
"""Exact cyclic-character arithmetic for B51, not BT realization."""
from math import gcd, lcm
from pathlib import Path
from time import perf_counter
import json

started = perf_counter()
primes = [p for p in range(5, 102)
          if all(p % t for t in range(2, int(p ** 0.5) + 1))]
rows = []
fibre_count = pair_count = 0
for p in primes:
    possible = []
    for d in range(1, p + 2, 2):
        if (p + 1) % d:
            continue
        q = (p + 1) // d
        m = (p - 1) * q
        assert gcd(m, p + 1) == q
        norm_multiplier = (p + 1) // q
        all_primitive_fibres = []
        for h in range(1, p - 1):
            if gcd(h, p - 1) != 1:
                continue
            fibre = {c for c in range(m)
                     if (norm_multiplier * c - h) % (p - 1) == 0}
            assert len(fibre) == q
            orbits = {tuple(sorted({c, p * c % m})) for c in fibre}
            assert len(orbits) == q // 2
            assert all(len(o) == 2 for o in orbits)
            assert set().union(*(set(o) for o in orbits)) == fibre
            assert any(gcd(c, m) == 1 for c in fibre)
            orders = {o: m // gcd(o[0], m) for o in orbits}
            joint = set()
            ordered_orbits = sorted(orbits)
            for i, a in enumerate(ordered_orbits):
                for b in ordered_orbits[i + 1:]:
                    joint.add(lcm(orders[a], orders[b]))
                    pair_count += 1
            assert (m in joint) == (q >= 4)
            if q == 2:
                assert p % 4 == 1
                for c in fibre:
                    assert (p * c - c - m // 2) % m == 0
            fibre_count += 1
            all_primitive_fibres.append({"norm_exponent": h,
                "orbits": ordered_orbits, "joint_orders": sorted(joint)})
        if q >= 4:
            possible.append(m)
        rows.append({"p": p, "d": d, "q": q, "m": m,
                     "primitive_fibres": all_primitive_fibres})
    expected = sorted((p * p - 1) // d for d in range(1, p + 2, 2)
                      if (p + 1) % d == 0 and (p + 1) // d >= 4)
    assert sorted(possible) == expected

p5 = next(row for row in rows if row["p"] == 5 and row["m"] == 24)
f5 = next(f for f in p5["primitive_fibres"] if f["norm_exponent"] == 1)
assert f5["orbits"] == [(1, 5), (9, 21), (13, 17)]
orbits5 = {"A": (1, 5), "B": (9, 21), "C": (13, 17)}
twists = {name: next(other for other, values in orbits5.items()
                      if values == tuple(sorted((c + 12) % 24 for c in orbit)))
          for name, orbit in orbits5.items()}
assert twists == {"A": "C", "B": "B", "C": "A"}
pair_orbits = set()
for a, b in [("A", "B"), ("A", "C"), ("B", "C")]:
    pair_orbits.add(tuple(sorted({tuple(sorted((a, b))),
                                tuple(sorted((twists[a], twists[b])))})))
assert pair_orbits == {(("A", "B"), ("B", "C")), (("A", "C"),)}

summary = {str(p): sorted({r["m"] for r in rows
                           if r["p"] == p and r["q"] >= 4}) for p in primes}
assert summary["5"] == [24]
assert summary["7"] == [48]
assert summary["13"] == [168]
assert summary["17"] == [96, 288]
result = {"status": "PASS", "scope": "Finite cyclic character fibres and joint orders only; no Barsotti--Tate realization or torsion-isomorphism existence.",
          "primes": primes, "primitive_norm_fibres": fibre_count,
          "distinct_character_pairs": pair_count,
          "remaining_joint_degrees": summary,
          "p5_orbits": orbits5, "p5_quadratic_twist": twists,
          "p5_unordered_pair_orbits": sorted(pair_orbits),
          "elapsed_seconds": perf_counter() - started}
out = Path(__file__).with_suffix('.output.json')
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
