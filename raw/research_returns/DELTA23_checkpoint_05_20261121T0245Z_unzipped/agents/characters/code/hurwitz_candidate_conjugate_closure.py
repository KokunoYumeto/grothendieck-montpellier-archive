#!/usr/bin/env python3
"""Actual-source closure under h and c h c^-1, with a3 parity."""
from pathlib import Path
from collections import deque
import json
import numpy as np

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[1]
PENT = HERE.parent / "pentagon"


def key(v, u, parity):
    return bytes([parity]) + v.astype(np.int16).tobytes() + u.astype(np.int16).tobytes()


def run():
    raw = np.load(PENT / "hurwitz_raw_pentagon45.npz")
    mixed = np.load(ROOT / "records/hurwitz_pentagon45_fibers.npz")
    vs = np.load(PENT / "hurwitz_global_conjugators.npz")["mixed72_V_1"]
    W = np.load(HERE / "records/hurwitz_complex_conjugation_probe.npz")["intertwiners"][0]
    Wi = np.argsort(W)
    items = []
    for k, (i, j) in enumerate(raw["labels"]):
        if np.array_equal(raw["pentagon_defects"][k], np.arange(8064)):
            v, r = vs[i], mixed[f"R_{i}"][j]
            items.append((int(i), int(j), v, np.argsort(r)[v]))
    assert len(items) == 18
    lookup = {key(v, u, 1): (i, j) for i, j, v, u in items}
    identity = np.arange(1344)
    rows = []
    saved = {}
    for i, j, v, u in items:
        cv, cu = W[v[Wi]], W[u[Wi]]
        gens = [(v, u), (cv, cu), (np.argsort(v), np.argsort(u)), (np.argsort(cv), np.argsort(cu))]
        labels = ["h", "chc", "h^-1", "chc^-1"]
        seen = {key(identity, identity, 0)}
        queue = deque([(identity, identity, 0, [])])
        odd = {}
        all_states = []
        failure = None
        while queue and failure is None:
            a, b, p, word = queue.popleft()
            all_states.append((a, b, p))
            if p:
                label = lookup.get(key(a, b, p))
                if label is None:
                    failure = {"word": word, "odd_length": len(word)}
                    break
                odd.setdefault(label, word)
            for (g, h), token in zip(gens, labels):
                aa, bb, pp = a[g], b[h], 1 - p
                k = key(aa, bb, pp)
                if k not in seen:
                    seen.add(k)
                    queue.append((aa, bb, pp, word + [token]))
        row = {
            "source": [i, j],
            "complex_conjugate": lookup[key(cv, cu, 1)],
            "closed": failure is None,
            "states_explored": len(all_states),
            "odd_targets": [{"label": label, "word": word} for label, word in sorted(odd.items())],
            "failure": failure,
        }
        if failure is None:
            row["graded_group_order"] = len(seen)
            assert len(seen) == len(all_states)
            # A finite set closed under the listed inverses is the entire
            # subgroup, not a bounded word search.
            row["even_count"] = sum(1 for _, _, p in all_states if p == 0)
            row["odd_count"] = sum(1 for _, _, p in all_states if p == 1)
            saved[f"V_{i}_{j}"] = np.stack([a for a, _, _ in all_states])
            saved[f"U_{i}_{j}"] = np.stack([b for _, b, _ in all_states])
            saved[f"parity_{i}_{j}"] = np.array([p for _, _, p in all_states])
        rows.append(row)
        print(json.dumps(row), flush=True)
    out = {
        "statement": "D23.C33",
        "cases": rows,
        "all_odd_words_retained": all(row["closed"] for row in rows),
        "exclusions": [row["source"] for row in rows if not row["closed"]],
        "scope": "Complete graded subgroup closure for h and its actual complex conjugate; no lift of any finite state is asserted.",
    }
    (HERE / "records/hurwitz_candidate_conjugate_closure.json").write_text(json.dumps(out, indent=2) + "\n")
    np.savez_compressed(HERE / "records/hurwitz_candidate_conjugate_closure.npz", **saved)
    print(json.dumps({k: v for k, v in out.items() if k != "cases"}, indent=2), flush=True)


if __name__ == "__main__":
    run()
