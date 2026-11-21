#!/usr/bin/env python3
"""All marked F2 kernels in E0, without a large direct-product enumeration.

Rooted deterministic Cayley labels identify two marked finite quotients
exactly.  Ambient AGL2(3) conjugacy is only an initial acceleration and is
not substituted for equality of kernels of nongenerating marked pairs.
"""
from pathlib import Path
from collections import Counter
import itertools
import json
import time
import numpy as np

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[1]
PENT = HERE.parent / "pentagon"
STEM = HERE / "records/affine216_marked_pair_kernels"


def multiply(a, b):
    u, v, A, B, C, D = a
    x, y, E, F, G, H = b
    return (
        (u+A*x+B*y) % 3, (v+C*x+D*y) % 3,
        (A*E+B*G) % 3, (A*F+B*H) % 3,
        (C*E+D*G) % 3, (C*F+D*H) % 3,
    )


def inverse(a):
    u, v, A, B, C, D = a
    di = pow((A*D-B*C) % 3, -1, 3)
    E, F, G, H = (di*D) % 3, (-di*B) % 3, (-di*C) % 3, (di*A) % 3
    return ((-E*u-F*v) % 3, (-G*u-H*v) % 3, E, F, G, H)


def run():
    start = time.monotonic()
    elems = [tuple(map(int, a)) for a in np.load(ROOT / "records/hurwitz_product_fixed_cover.npz")["group_elements"]]
    index = {a: i for i, a in enumerate(elems)}
    one = index[(0, 0, 1, 0, 0, 1)]
    mt = np.array([[index[multiply(a, b)] for b in elems] for a in elems], dtype=np.int16)
    iv = np.array([index[inverse(a)] for a in elems], dtype=np.int16)
    ambient = []
    for u, v, A, B, C, D in itertools.product(range(3), repeat=6):
        if (A*D-B*C) % 3:
            ambient.append((u, v, A, B, C, D))
    assert len(ambient) == 432
    autos = np.array([[index[multiply(multiply(g, a), inverse(g))] for a in elems] for g in ambient], dtype=np.int16)
    assert len({a.tobytes() for a in autos}) == 432

    def marked_cayley(a, b):
        todo = [one]
        loc = {one: 0}
        for g in todo:
            for h in (a, b):
                q = int(mt[g, h])
                if q not in loc:
                    loc[q] = len(todo)
                    todo.append(q)
        perms = np.array([[loc[int(mt[g, h])] for g in todo] for h in (a, b)], dtype=np.int16)
        return perms, np.array(todo, dtype=np.int16)

    pair_orbit = np.full((216, 216), -1, dtype=np.int16)
    pair_kernel = np.full((216, 216), -1, dtype=np.int16)
    orbit_rows, kernel_rows = [], []
    kernel_lookup = {}
    saved = {"elements": np.array(elems), "multiplication": mt, "inverse": iv, "ambient_automorphisms": autos}
    for a in range(216):
        for b in range(216):
            if pair_orbit[a, b] >= 0:
                continue
            orbit = np.unique(np.stack([autos[:, a], autos[:, b]], axis=1), axis=0)
            assert np.all(pair_orbit[orbit[:, 0], orbit[:, 1]] < 0)
            cayley, members = marked_cayley(a, b)
            k = cayley.tobytes()
            if k not in kernel_lookup:
                kid = len(kernel_rows)
                kernel_lookup[k] = kid
                kernel_rows.append({"kernel": kid, "pair": [a, b], "group_order": len(members)})
                saved[f"kernel_{kid}_cayley"] = cayley
                saved[f"kernel_{kid}_members"] = members
            kid = kernel_lookup[k]
            oid = len(orbit_rows)
            pair_orbit[orbit[:, 0], orbit[:, 1]] = oid
            pair_kernel[orbit[:, 0], orbit[:, 1]] = kid
            orbit_rows.append({"orbit": oid, "pair": [a, b], "orbit_size": len(orbit), "group_order": len(members), "kernel": kid})
    assert np.all(pair_orbit >= 0) and np.all(pair_kernel >= 0)

    # Kernel equalities are preserved by Nielsen transformations.  Check
    # every representative of an ambient orbit, not merely one per kernel.
    s3 = np.full((len(kernel_rows), 3), -1, dtype=np.int16)
    for row in orbit_rows:
        a, b = row["pair"]
        z = int(iv[mt[a, b]])
        values = [int(pair_kernel[b, a]), int(pair_kernel[b, z]), int(pair_kernel[a, z])]
        kid = row["kernel"]
        if s3[kid, 0] < 0:
            s3[kid] = values
        else:
            assert np.array_equal(s3[kid], values)
    swap, cycle, reflection = s3.T
    ident = np.arange(len(kernel_rows))
    assert np.array_equal(swap[swap], ident)
    assert np.array_equal(cycle[cycle[cycle]], ident)
    assert np.array_equal(reflection[reflection], ident)
    assert np.array_equal(swap[cycle[swap]], cycle[cycle])
    for row in kernel_rows:
        row["swap_kernel"], row["cycle_kernel"], row["reflection_kernel"] = map(int, s3[row["kernel"]])

    data = np.load(PENT / "hurwitz_cubic216_four_13.npz")
    tuples = np.array([[index[tuple(map(int, a))] for a in row] for row in data["tuple_elements"]], dtype=np.int16)
    products = np.full(1344, one, dtype=np.int16)
    prefix_pairs = np.empty((1344, 4, 2), dtype=np.int16)
    prefix_kernels = np.empty((1344, 4), dtype=np.int16)
    for j in range(4):
        products = mt[products, tuples[:, j]]
        prefix_pairs[:, j, 0] = iv[products]
        prefix_pairs[:, j, 1] = tuples[:, j]
        prefix_kernels[:, j] = pair_kernel[iv[products], tuples[:, j]]
    needed = sorted(map(int, set(prefix_kernels[:, 3])))
    for kid in needed:
        kernel_rows[kid]["last_pair_count"] = int(np.sum(prefix_kernels[:, 3] == kid))

    # The exact marked source of the cubic216 detector.
    cubic = [index[(0, 0, 2, 1, 0, 2)], index[(1, 0, 2, 0, 2, 2)]]
    cubic_kernel = int(pair_kernel[tuple(cubic)])
    saved.update(pair_orbit=pair_orbit, pair_kernel=pair_kernel, nielsen=s3, tuples=tuples,
                 prefix_pairs=prefix_pairs, prefix_kernels=prefix_kernels, cubic_pair=np.array(cubic))
    out = {
        "statement": "D23.C34 inventory",
        "target_order": 216,
        "ambient_automorphism_order": 432,
        "marked_pairs": 216**2,
        "ambient_pair_orbits": len(orbit_rows),
        "distinct_marked_kernels": len(kernel_rows),
        "generating_pair_orbits": sum(r["group_order"] == 216 for r in orbit_rows),
        "generating_marked_kernels": sum(r["group_order"] == 216 for r in kernel_rows),
        "generating_pairs": sum(r["orbit_size"] for r in orbit_rows if r["group_order"] == 216),
        "kernel_order_histogram": dict(sorted(Counter(r["group_order"] for r in kernel_rows).items())),
        "last_pair_kernel_ids": needed,
        "last_pair_kernels": [kernel_rows[k] for k in needed],
        "cubic_detector_kernel": cubic_kernel,
        "cubic_detector_pair": cubic,
        "orbits": orbit_rows,
        "kernels": kernel_rows,
        "elapsed_seconds": time.monotonic() - start,
        "result": "PASS",
        "scope": "Exact marked finite-kernel inventory and relevant tuple-pair lookup; no GT residue assignment or lifting assertion.",
    }
    STEM.with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
    np.savez_compressed(STEM.with_suffix(".npz"), **saved)
    print(json.dumps({k: v for k, v in out.items() if k not in ["orbits", "kernels"]}, indent=2), flush=True)


if __name__ == "__main__":
    run()
