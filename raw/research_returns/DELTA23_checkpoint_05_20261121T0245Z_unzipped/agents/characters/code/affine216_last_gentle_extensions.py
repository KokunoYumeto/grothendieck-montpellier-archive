#!/usr/bin/env python3
"""All finite S3 two/three-cycle extensions of the common-word last fibers."""
from pathlib import Path
import itertools
import json
import sys
import numpy as np

HERE = Path(__file__).resolve().parents[1]
FIVE = HERE.parent / "five_level_six"
STEM = HERE / "records/affine216_last_gentle_extensions"


def run():
    stem = STEM
    invt = np.load(HERE / "records/affine216_marked_pair_kernels.npz")
    meta = json.loads((HERE / "records/affine216_marked_pair_kernels.json").read_text())
    mt, iv, pk, nielsen = (invt[k] for k in ["multiplication", "inverse", "pair_kernel", "nielsen"])
    elements = invt["elements"]
    one = next(i for i, a in enumerate(elements) if tuple(a) == (0, 0, 1, 0, 0, 1))
    fibers = np.load(HERE / "records/affine216_last_meridian_fibers.npz")
    known_kids = list(map(int, fibers["kernel_ids"]))
    if "--all-fibers" in sys.argv:
        source = json.loads((HERE / "records/affine216_last_meridian_fibers.json").read_text())
        rows = []
        for row in source["cases"]:
            i, j, phase = row["candidate"], row["fiber_index"], row["deck_phase"]
            choices = [fibers[f"fiber_{i}_{j}_{phase}_{k}"] for k in known_kids]
            rows.extend([i, j, phase, *values] for values in itertools.product(*choices))
        table = np.array(rows, dtype=np.int16)
        stem = STEM.with_name(STEM.name + "_all")
    else:
        incoming = np.load(FIVE / "affine216_last_commonword.npz")
        print("input keys", [(k, incoming[k].shape) for k in incoming.files], flush=True)
        table = next(incoming[k] for k in incoming.files if incoming[k].ndim == 2 and incoming[k].shape[1] == 11)

    def members(a, b):
        out, seen = [one], {one}
        for g in out:
            for h in (a, b):
                q = int(mt[g, h])
                if q not in seen:
                    seen.add(q)
                    out.append(q)
        return np.array(out, dtype=np.int16)

    mapping_cache = {}
    def mapping(a, b):
        key = (a, b)
        if key not in mapping_cache:
            kid = int(pk[a, b])
            canonical = invt[f"kernel_{kid}_members"]
            mapped = members(a, b)
            assert len(mapped) == len(canonical)
            fwd = np.full(216, -1, dtype=np.int16)
            back = np.full(216, -1, dtype=np.int16)
            fwd[canonical] = mapped
            back[mapped] = canonical
            mapping_cache[key] = kid, fwd, back
        return mapping_cache[key]

    orbits = []
    seen = set()
    for k in known_kids:
        if k in seen:
            continue
        todo = [k]
        for j in todo:
            for z in nielsen[j]:
                if int(z) not in todo:
                    todo.append(int(z))
        todo.sort()
        orbits.append(todo)
        seen.update(todo)

    cache = {}
    saved = {"known_kernel_ids": np.array(known_kids), "input_assignments": table}
    cache_rows = []
    def extensions(orbit, known):
        signature = tuple((k, known[k]) for k in orbit if k in known)
        key = tuple(orbit), signature
        if key in cache:
            return cache[key]
        base = next(k for k in orbit if k in known)
        a, b = meta["kernels"][base]["pair"]
        z = int(iv[mt[a, b]])
        directed = [(a, b), (b, z), (z, a), (b, a), (z, b), (a, z)]
        maps = [mapping(*p) for p in directed]
        assert {q[0] for q in maps} == set(orbit)
        g0 = known[base]
        derived = fibers[f"kernel_{base}_derived"]
        found = []
        for g1 in derived:
            g2 = int(iv[mt[g1, g0]])
            values = [g0, int(g1), g2, int(iv[g0]), int(iv[g1]), int(iv[g2])]
            assignment = {}
            valid = True
            for (kid, _, back), value in zip(maps, values):
                q = int(back[value])
                assert q >= 0
                if kid in assignment and assignment[kid] != q:
                    valid = False
                    break
                assignment[kid] = q
            if not valid or any(assignment[k] != v for k, v in signature):
                continue
            def evaluate(x, y):
                kid, fwd, _ = mapping(x, y)
                q = int(fwd[assignment[kid]])
                assert q >= 0
                return q
            # Check all canonical orientations, including every reflected
            # kernel.  Their marked isomorphisms carry these equalities to
            # every representation with the same F2 kernel.
            for kid in orbit:
                x, y = meta["kernels"][kid]["pair"]
                zz = int(iv[mt[x, y]])
                fxy = evaluate(x, y)
                fyx = evaluate(y, x)
                fyz = evaluate(y, zz)
                fzx = evaluate(zz, x)
                if mt[fyx, fxy] != one or mt[mt[fzx, fyz], fxy] != one:
                    valid = False
                    break
                negative = one
                for q in (fzx, int(iv[zz]), fyz, int(iv[y]), fxy, int(iv[x])):
                    negative = int(mt[negative, q])
                if negative != one:
                    valid = False
                    break
            if valid:
                found.append(tuple(assignment[k] for k in orbit))
        found = sorted(set(found))
        cid = len(cache_rows)
        row = {"cache_index": cid, "orbit": orbit, "given": signature, "extension_count": len(found)}
        cache_rows.append(row)
        saved[f"orbit_{cid}_kernels"] = np.array(orbit)
        saved[f"orbit_{cid}_assignments"] = np.array(found, dtype=np.int16).reshape(-1, len(orbit))
        cache[key] = cid
        return cid

    cases = []
    passing = []
    for ordinal, row in enumerate(table):
        known = dict(zip(known_kids, map(int, row[3:])))
        indices = [extensions(orbit, known) for orbit in orbits]
        counts = [cache_rows[j]["extension_count"] for j in indices]
        passed = all(counts)
        cases.append({"input_index": ordinal, "label": list(map(int, row[:3])),
                      "orbit_cache_indices": indices, "extension_counts": counts, "passes": passed})
        if passed:
            passing.append(ordinal)
    saved["passing_input_indices"] = np.array(passing)
    saved["case_orbit_cache_indices"] = np.array([r["orbit_cache_indices"] for r in cases])
    out = {
        "statement": "D23.C34 S3 continuation",
        "orbits": orbits,
        "input_assignments": len(table),
        "passing_assignments": len(passing),
        "passing_raw_labels": sorted({tuple(cases[j]["label"]) for j in passing}),
        "cache": cache_rows,
        "cases": cases,
        "scope": "Complete finite two/three/m=-1 cycle extensions by marked-kernel graphs; cross-orbit common word is an additional test.",
    }
    stem.with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
    np.savez_compressed(stem.with_suffix(".npz"), **saved)
    print(json.dumps({k: v for k, v in out.items() if k not in ["cases", "cache", "passing_raw_labels"]}, indent=2), flush=True)
    print("cache counts", [(r["orbit"], r["given"], r["extension_count"]) for r in cache_rows], flush=True)


if __name__ == "__main__":
    run()
