#!/usr/bin/env python3
"""Independent literal Artin check of the first-strand cabling marking."""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE.parent / "five_level_six"))
from hurwitz_last_coordinate import same, inv, comm, z


def meridian(n, i):
    v = tuple(range(n, i, -1))
    return v + (i, i) + inv(v)


def y(i):
    return tuple(range(i-1, 1, -1)) + (1, 1) + tuple(range(2, i))


def run():
    rows = []
    t = (2, 1, 1, 2)
    assert same(t, inv(z(2)) + z(3), 3)
    assert same(comm(z(2), z(3)), (), 3)
    for n in [2, 3, 4, 5]:
        # Source A_{n+1}=<s1^2,s2,...,sn>; the cabled first generator is t.
        # Verify its annular Artin relation with the new s3.
        assert same(t + (3,) + t + (3,), (3,) + t + (3,) + t, n+2)
        for i in range(3, n+1):
            assert same(comm(t, (i+1,)), (), n+2)
        u = [meridian(n+1, i) for i in range(1, n+2)]
        targets = []
        for i in range(1, n+1):
            prefix = tuple(range(n+1, i+1, -1))
            image = prefix + (t if i == 1 else (i+1, i+1)) + inv(prefix)
            wanted = u[0] + u[1] if i == 1 else u[i]
            assert same(image, wanted, n+2)
            targets.append(image)
        # Delta sends every y_i to y_{i+1}; this is the exact associator
        # input equality in the remaining standard braid-action formulas.
        for i in range(2, n+1):
            image = tuple(range(i, 2, -1)) + t + tuple(range(3, i+1))
            assert same(image, y(i+1), n+2)
        rows.append({
            "source_free_rank": n,
            "target_free_rank": n+1,
            "delta_u1_equals_u1_u2": True,
            "remaining_meridians_shift_by_one": True,
            "all_y_inputs_shift_by_one": True,
            "annular_relations": True,
        })
    out = {
        "statement": "Independent certificate for D23.F42",
        "delta_sigma1_squared": [2, 1, 1, 2],
        "delta_sigma_i_for_i_at_least_2": "sigma_(i+1)",
        "y3_equals_z2_inverse_z3": True,
        "nested_full_twists_commute": True,
        "cases": rows,
        "result": "PASS",
        "scope": "Literal marking and braid identities; full-GT equivariance follows by substituting the standard braid action generatorwise.",
    }
    (HERE / "records/first_strand_cabling.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    run()
