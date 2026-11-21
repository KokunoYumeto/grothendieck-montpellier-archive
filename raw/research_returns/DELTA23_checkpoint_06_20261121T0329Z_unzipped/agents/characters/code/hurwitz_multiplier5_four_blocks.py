#!/usr/bin/env python3
"""All local orthogonal lifts of the multiplier5 canonical detector actions."""
from pathlib import Path
import contextlib
import importlib.util
import io
import itertools
import json
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup
from hurwitz_multiplier5_detector import power
from hurwitz_mixed72_partial import orbits

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[1]
PENT = HERE.parent / "pentagon"
FIVE = HERE.parent / "five_level_six"
spec = importlib.util.spec_from_file_location("orth112", HERE / "code/hurwitz_orthogonal112.py")
orth = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(orth)


def run():
    data = np.load(PENT / "hurwitz_cubic216_four_13.npz")
    A, B, C = data["generators"]
    block = np.load(PENT / "hurwitz_cubic216_four_13_block0.npz")["block_map"]
    trans = np.load(FIVE / "hurwitz_block_correlations.npz")["transversals"]
    det = {int(v): int(w) for v, w in zip(data["detector_subset"], data["detector_map"])}
    src = np.load(HERE / "records/hurwitz_multiplier5_detector.npz")
    As, Bs, Fs, Ts = (src[k] for k in ["A", "B", "F", "W"])
    bs = [7, 8, 10, 11]
    subset = np.flatnonzero(np.isin(block, bs))
    loc = np.full(1344, -1, dtype=int)
    loc[subset] = np.arange(448)
    aa, bb = loc[A[subset]], loc[B[subset]]
    ss, dd = aa[bb[aa]], aa[bb]
    sii, di = np.argsort(ss), np.argsort(dd)
    xx, yy = aa[aa], bb[bb]
    zz = np.argsort(xx[yy])
    joint = PermutationGroup([Permutation(np.r_[xx, 448+As[As]].tolist()),
                              Permutation(np.r_[yy, 448+Bs[Bs]].tolist())])
    derived = joint.derived_subgroup()
    assert int(joint.order()) == 5832 and int(derived.order()) == 1944
    flookup = {f.tobytes(): i for i, f in enumerate(Fs)}
    lifts = [[] for _ in Fs]
    for g in derived.generate_schreier_sims():
        p = np.array(g.array_form)
        q = (p[448:]-448).astype(Fs.dtype)
        if q.tobytes() not in flookup:
            continue
        f = p[:448]
        if not np.array_equal(ss[f[sii]], np.argsort(f)):
            continue
        f1 = dd[f[di]]
        f2 = dd[f1[di]]
        for m in [2, 3]:
            if not np.array_equal(f2[power(zz, m)[f1[power(yy, m)[f[power(xx, m)]]]]], np.arange(448)):
                break
        else:
            lifts[flookup[q.tobytes()]].append(f)
    assert all(len(v) <= 1 for v in lifts)
    F448 = np.array([v[0] if v else np.arange(448) for v in lifts])

    orbit108 = next(o for o in orbits([A, B]) if len(o) == 108)
    nine = {j: set(det[int(v)] for v in orbit108 if block[v] == j) for j in bs}
    points = {j: trans[j][orth.base] for j in bs}
    labels = {j: np.array([det.get(int(v), -1) for v in points[j]]) for j in bs}
    coords, Q = orth.coords, orth.Q
    cindex = {tuple(v): i for i, v in enumerate(coords)}
    mixed = np.load(PENT / "hurwitz_global_conjugators.npz")["mixed72_V_1"][1]
    vmixed = loc[mixed[subset]]
    rows, saved = [], {"subset": subset, "F448": F448,
                       "first448_pass_indices": np.array([i for i, v in enumerate(lifts) if v])}
    for no, theta in enumerate(Ts):
        if not lifts[no]:
            rows.append({"detector_index": no, "no_first448_gentle_lift": True,
                         "four_block_covariance_lifts": 0, "centralizing_mixed_V": 0})
            continue
        target_blocks = {j: next(k for k in bs if {int(theta[t]) for t in nine[j]} == nine[k]) for j in bs}
        options = {}
        for j in bs:
            k = target_blocks[j]
            sj, tk = labels[j], labels[k]
            ids = []
            for q in np.flatnonzero(sj >= 0):
                if orth.rank(coords[ids+[int(q)]]) > len(ids):
                    ids.append(int(q))
                if len(ids) == 6:
                    break
            base = coords[ids].T
            bi = orth.inverse(base)
            gram = base.T@Q@base % 3
            choices = []
            for h, q in enumerate(ids):
                images = np.flatnonzero(tk == theta[sj[q]])
                assert len(images) == 3
                choices.append([coords[t]*s % 3 for t in images for s in ([1] if h == 0 else [1, 2])])
            found = []
            for mu in [1, 2]:
                def search(columns):
                    h = len(columns)
                    if h == 6:
                        yield np.array(columns).T
                        return
                    for v in choices[h]:
                        if all(int(u@Q@v % 3) == int(mu*gram[t, h] % 3) for t, u in enumerate(columns)):
                            yield from search(columns+[v])
                for w in search([]):
                    M = w@bi % 3
                    if orth.rank(M) != 6:
                        continue
                    assert np.array_equal(M.T@Q@M % 3, mu*Q % 3)
                    p = np.array([cindex[orth.proj(M@v)] for v in coords])
                    if any(tk[p[q]] != theta[sj[q]] for q in np.flatnonzero(sj >= 0)):
                        continue
                    found.append(p)
            options[j] = found
            saved[f"local_{no}_{j}"] = np.array(found)
        all_lifts, commuting = [], []
        f = F448[no]
        bnew = np.argsort(f)[power(bb, 5)[f]]
        for choice in itertools.product(*(range(len(options[j])) for j in bs)):
            global_map = np.full(1344, -1, dtype=int)
            for j, q in zip(bs, choice):
                global_map[points[j]] = points[target_blocks[j]][options[j][q]]
            w = loc[global_map[subset]]
            if not np.array_equal(w[aa], power(aa, 5)[w]):
                continue
            if not np.array_equal(w[bb], bnew[w]):
                continue
            all_lifts.append(w)
            if np.array_equal(w[vmixed], vmixed[w]):
                commuting.append(w)
        rows.append({"detector_index": no, "block_permutation": target_blocks,
                     "local_option_counts": [len(options[j]) for j in bs],
                     "four_block_covariance_lifts": len(all_lifts),
                     "centralizing_mixed_V": len(commuting)})
        saved[f"W448_{no}"] = np.array(all_lifts)
        saved[f"commuting_W448_{no}"] = np.array(commuting)
        print(rows[-1], flush=True)
    out = {"multiplier_mod12": 5, "cases": rows,
           "detector_candidates": len(Ts),
           "with_four_block_lift": sum(r["four_block_covariance_lifts"] > 0 for r in rows),
           "with_commuting_lift": sum(r["centralizing_mixed_V"] > 0 for r in rows),
           "scope": "Exhaustive local PGO lifts and B3 covariance on448points; not a full1344 arithmetic action."}
    (HERE / "records/hurwitz_multiplier5_four_blocks.json").write_text(json.dumps(out, indent=2) + "\n")
    np.savez_compressed(HERE / "records/hurwitz_multiplier5_four_blocks.npz", **saved)
    print(json.dumps({k: v for k, v in out.items() if k != "cases"}, indent=2), flush=True)


if __name__ == "__main__":
    run()
