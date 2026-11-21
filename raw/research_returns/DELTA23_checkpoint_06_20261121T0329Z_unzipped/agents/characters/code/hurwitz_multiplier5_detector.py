#!/usr/bin/env python3
"""Complete necessary multiplier-5 actions on the canonical degree36 detector."""
from pathlib import Path
import json
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup
from hurwitz_mixed72_partial import propagate

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[1]
PENT = HERE.parent / "pentagon"


def power(p, n):
    if n < 0:
        return power(np.argsort(p), -n)
    ans = np.arange(len(p))
    while n:
        if n & 1:
            ans = ans[p]
        p = p[p]
        n //= 2
    return ans


def run():
    A, B = np.load(PENT / "hurwitz_cubic216_order6_triple_9.npz")["generators"]
    x, y = A[A], B[B]
    z = np.argsort(x[y])
    D, S = A[B], A[B[A]]
    Di, Si = np.argsort(D), np.argsort(S)
    I = np.arange(36)
    assert np.array_equal(power(D, 3), I) and np.array_equal(S[S], I)
    assert np.array_equal(D[x[Di]], y) and np.array_equal(D[y[Di]], z)
    assert np.array_equal(S[x[Si]], y) and np.array_equal(S[y[Si]], x)
    G = PermutationGroup([Permutation(x.tolist()), Permutation(y.tolist())])
    H = G.derived_subgroup()
    assert int(G.order()) == 1944 and int(H.order()) == 648
    known = json.loads((ROOT / "records/hurwitz36_gt_stability.json").read_text())
    theta = np.array(next(r["conjugator_example"] for r in known["candidates"]
                          if r["label"] == [0, 1] and r["simultaneous_conjugators"] == 1))
    A5, B5 = power(A, 5), power(B, 5)
    rows, fs, ws = [], [], []
    count_duality = count_cycles = count_covariance = 0
    for ordinal, f0 in enumerate(H.generate_schreier_sims()):
        f = np.array(f0.array_form)
        fi = np.argsort(f)
        dual = np.array_equal(S[f[Si]], fi)
        count_duality += dual
        if not dual:
            continue
        f1 = D[f[Di]]
        f2 = D[f1[Di]]
        cycles = []
        for m in [2, 3]:
            q = f2[power(z, m)[f1[power(y, m)[f[power(x, m)]]]]]
            cycles.append(np.array_equal(q, I))
        if not all(cycles):
            continue
        count_cycles += 1
        newB = fi[B5[f]]
        maps = []
        for dst in range(36):
            w = propagate([A, B], [A5, newB], [(0, dst)])
            if w is not None:
                maps.append(w)
        if maps:
            count_covariance += 1
            assert len(maps) == 1
            w = maps[0]
            assert np.array_equal(w[A], A5[w])
            assert np.array_equal(w[B], newB[w])
            fs.append(f)
            ws.append(w)
            rows.append({
                "derived_index": ordinal,
                "two_cycle": True,
                "three_cycle_m2": True,
                "three_cycle_m3": True,
                "simultaneous_conjugators": len(maps),
                "commutes_with_mixed_theta": np.array_equal(w[theta], theta[w]),
                "W_order": int(Permutation(w.tolist()).order()),
            })
    # Stabilizer-chain generator order can vary between fresh processes.
    # Use literal permutation arrays to give downstream detector labels
    # a stable, reproducible ordering.
    order = sorted(range(len(fs)), key=lambda i: tuple(map(int, fs[i])))
    rows = [rows[i] for i in order]
    fs = [fs[i] for i in order]
    ws = [ws[i] for i in order]
    out = {
        "multiplier_mod12": 5,
        "first_derived_order": 648,
        "duality_values": int(count_duality),
        "both_cycle_values": count_cycles,
        "covariance_values": count_covariance,
        "commuting_with_mixed_theta": sum(r["commutes_with_mixed_theta"] for r in rows),
        "cases": rows,
        "scope": "Complete necessary detector values and actions for actual multiplier5; no chosen arithmetic f or full1344 lift asserted.",
    }
    (HERE / "records/hurwitz_multiplier5_detector.json").write_text(json.dumps(out, indent=2) + "\n")
    np.savez_compressed(HERE / "records/hurwitz_multiplier5_detector.npz",
                        A=A, B=B, F=np.array(fs), W=np.array(ws), mixed_theta=theta)
    print(json.dumps(out, indent=2), flush=True)


if __name__ == "__main__":
    run()
