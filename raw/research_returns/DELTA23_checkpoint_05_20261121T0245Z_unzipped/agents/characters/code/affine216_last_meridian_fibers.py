#!/usr/bin/env python3
"""Exact last-meridian word fibers for all 18x6 raw Hurwitz actions.

Conditional only on the independently derived formula
  kappa_h(P)=P,
  kappa_h(t4)=f(P^-1,t4)^-1 t4 f(P^-1,t4).
The inverse of the stored actual-covariance permutation is precomposition
by kappa_h. All marked-kernel correlations within the 36 last-entry pairs
are imposed; correlations between distinct kernels remain separate.
"""
from pathlib import Path
import json
import time
import numpy as np

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[1]
PENT = HERE.parent / "pentagon"
STEM = HERE / "records/affine216_last_meridian_fibers"


def run():
    start = time.monotonic()
    inventory = np.load(HERE / "records/affine216_marked_pair_kernels.npz")
    metadata = json.loads((HERE / "records/affine216_marked_pair_kernels.json").read_text())
    mt, iv = inventory["multiplication"], inventory["inverse"]
    elems = inventory["elements"]
    index = {tuple(map(int, a)): i for i, a in enumerate(elems)}
    one = index[(0, 0, 1, 0, 0, 1)]
    raw = np.load(ROOT / "records/hurwitz_product_fixed_cover.npz")
    assert np.array_equal(raw["group_elements"], elems)
    tuples = raw["tuples"]
    product = index[tuple(map(int, raw["product"]))]
    a = int(iv[product])
    bs = np.unique(tuples[:, 3])
    assert len(bs) == 36
    kids = sorted({int(inventory["pair_kernel"][a, b]) for b in bs})
    assert kids == metadata["last_pair_kernel_ids"]
    values = np.load(PENT / "hurwitz_raw_survivor_covariance.npz")
    deck = raw["deck"]
    identity = np.arange(8064)

    def cayley_members(x, y):
        todo, seen = [one], {one}
        for g in todo:
            for h in (x, y):
                q = int(mt[g, h])
                if q not in seen:
                    seen.add(q)
                    todo.append(q)
        return np.array(todo, dtype=np.int16)

    def derived_members(x, y, members):
        comm = int(mt[mt[mt[x, y], iv[x]], iv[y]])
        normals = np.unique(mt[mt[members, comm], iv[members]])
        todo, seen = [one], {one}
        for g in todo:
            for h in normals:
                q = int(mt[g, h])
                if q not in seen:
                    seen.add(q)
                    todo.append(q)
        return np.array(sorted(todo), dtype=np.int16)

    saved = {"last_inputs": np.array([a, *bs]), "kernel_ids": np.array(kids)}
    models = {}
    for kid in kids:
        x, y = metadata["kernels"][kid]["pair"]
        members = inventory[f"kernel_{kid}_members"]
        assert np.array_equal(members, cayley_members(x, y))
        derived = derived_members(x, y, members)
        positions = {int(g): i for i, g in enumerate(members)}
        positions = np.array([positions[int(g)] for g in derived])
        these = np.array([b for b in bs if inventory["pair_kernel"][a, b] == kid], dtype=np.int16)
        images = []
        for b in these:
            mapped = cayley_members(a, int(b))
            assert len(mapped) == len(members)
            value = mapped[positions]
            images.append(mt[mt[iv[value], b], value])
        predicted = np.stack(images, axis=1)
        models[kid] = (these, derived, predicted)
        saved[f"kernel_{kid}_last_entries"] = these
        saved[f"kernel_{kid}_derived"] = derived
        saved[f"kernel_{kid}_predicted_conjugates"] = predicted

    rows = []
    for key in values.files:
        if not key.startswith("V_"):
            continue
        i, j = map(int, key.split("_")[1:])
        v = values[key]
        dpow = identity.copy()
        for phase in range(6):
            vv = dpow[v]
            vi = np.argsort(vv)
            desired = tuples[vi, 3]
            target = {}
            for b in bs:
                out = np.unique(desired[tuples[:, 3] == b])
                assert len(out) == 1, "Stored action must preserve the last-entry partition."
                target[int(b)] = int(out[0])
            counts = {}
            for kid, (these, derived, predicted) in models.items():
                want = np.array([target[int(b)] for b in these])
                allowed = derived[np.all(predicted == want[None, :], axis=1)]
                counts[kid] = len(allowed)
                saved[f"fiber_{i}_{j}_{phase}_{kid}"] = allowed
            row = {"candidate": i, "fiber_index": j, "deck_phase": phase,
                   "kernel_fiber_sizes": counts, "passes": all(counts.values())}
            rows.append(row)
            dpow = deck[dpow]
        print(i, j, [(r["deck_phase"], r["passes"], list(r["kernel_fiber_sizes"].values())) for r in rows[-6:]], flush=True)
    assert len(rows) == 108
    out = {
        "statement": "D23.C34 finite probe",
        "source_formula": "kappa(P)=P and kappa(t4)=f(P^-1,t4)^-1 t4 f(P^-1,t4)",
        "stored_action_orientation": "inverse raw V is precomposition by kappa",
        "last_entry_count": len(bs),
        "relevant_kernel_ids": kids,
        "cases": rows,
        "passing_raw_phases": sum(r["passes"] for r in rows),
        "passing_base_pairs": sorted({(r["candidate"], r["fiber_index"]) for r in rows if r["passes"]}),
        "elapsed_seconds": time.monotonic() - start,
        "scope": "Exact derived-value fibers with all same-kernel correlations; no inter-kernel common-word or actual lifting assertion.",
    }
    STEM.with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
    np.savez_compressed(STEM.with_suffix(".npz"), **saved)
    print(json.dumps({k: v for k, v in out.items() if k != "cases"}, indent=2), flush=True)


if __name__ == "__main__":
    run()
