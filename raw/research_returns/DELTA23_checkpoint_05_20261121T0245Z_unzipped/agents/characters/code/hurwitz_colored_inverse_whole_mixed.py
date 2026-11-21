#!/usr/bin/env python3
"""Exact full colored-5376 mixed image and its marked S4 join.

Discard an orbit only when adding its marked generators leaves the image
order unchanged.  This is an exact kernel inclusion, so the final retained
union is faithful for the whole mixed image, independently of componentwise
absence of a quotient.
"""
from pathlib import Path
import json
import pickle
import sys
import time
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup

HERE = Path(__file__).resolve().parents[1]
PENT = HERE.parent / "pentagon"
STEM = HERE / "records/hurwitz_colored_inverse_whole_mixed"


def group(gens):
    return PermutationGroup([Permutation(g.tolist()) for g in gens])


def join(gens, other):
    if gens is None:
        return other.copy()
    return np.stack([np.r_[g, len(g) + h] for g, h in zip(gens, other)])


def run():
    start = time.monotonic()
    source = np.load(PENT / "hurwitz_colored_inverse_orbit_12.npz")
    A, B, C = source["generators"]
    s = A[B[A]]
    original = np.stack([C[C], s[s]])
    data = np.load(PENT / "hurwitz_colored_inverse_12_mixed.npz")
    inventory = json.loads(
        (PENT / "hurwitz_colored_inverse_12_mixed.json").read_text()
    )["cases"]
    n = len(A)
    all_points = np.concatenate([data[f"orbit_{r['mixed_orbit']}"] for r in inventory])
    assert np.array_equal(np.sort(all_points), np.arange(n))
    for row in inventory:
        k = row["mixed_orbit"]
        subset = data[f"orbit_{k}"]
        index = np.full(n, -1, dtype=np.int64)
        index[subset] = np.arange(len(subset))
        assert np.array_equal(index[original[:, subset]], data[f"pair_{k}"])

    # Large images first, preferring their smaller faithful actions.
    ordered = sorted(inventory, key=lambda r: (-r["order"], r["degree"], r["mixed_orbit"]))
    selected = []
    current = None
    current_order = 1
    history = []
    current_group = None
    if "--resume" in sys.argv and STEM.with_suffix(".json").exists():
        prior = json.loads(STEM.with_suffix(".json").read_text())
        selected = prior["selected_components"]
        history = prior["component_tests"]
        current_order = prior["image_order_so_far"]
        for k in selected:
            current = join(current, data[f"pair_{k}"])
    processed = {r["component"] for r in history}
    inventory_by_id = {r["mixed_orbit"]: r for r in inventory}
    for row in ordered:
        k = row["mixed_orbit"]
        if k in processed:
            continue
        factor = None
        if current is not None:
            for j in sorted(selected, key=lambda j: inventory_by_id[j]["degree"]):
                parent = inventory_by_id[j]
                if parent["order"] % row["order"]:
                    continue
                small = group(join(data[f"pair_{j}"], data[f"pair_{k}"]))
                small_order = int(small.order())
                if small_order == parent["order"]:
                    factor = (j, small_order)
                    break
        candidate = join(current, data[f"pair_{k}"])
        if factor is None:
            G = group(candidate)
            order = int(G.order())
        else:
            G = None
            order = current_order
        assert order % current_order == 0
        assert order % row["order"] == 0
        keep = order != current_order
        step = {
            "component": k,
            "degree": row["degree"],
            "previous_degree": 0 if current is None else len(current[0]),
            "previous_order": current_order,
            "joined_order": order,
            "retained": keep,
        }
        if factor is not None:
            step["factored_through_component"] = factor[0]
            step["two_component_join_order"] = factor[1]
        if keep:
            selected.append(k)
            current, current_order, current_group = candidate, order, G
        history.append(step)
        partial = {
            "statement": "D23.C32",
            "source_degree": n,
            "selected_components": selected,
            "faithful_degree_so_far": len(current[0]),
            "image_order_so_far": current_order,
            "completed_component_tests": len(history),
            "component_tests": history,
            "elapsed_seconds": time.monotonic() - start,
            "status": "IN_PROGRESS",
        }
        STEM.with_suffix(".json").write_text(json.dumps(partial, indent=2) + "\n")
        print(json.dumps(step), flush=True)

    # Every omitted coordinate factors through the final image: at its test
    # stage its kernel contained the retained kernel, which only shrank later.
    target = np.array([[1, 2, 0, 3], [1, 2, 3, 0]], dtype=np.int64)
    if current_group is None:
        current_group = group(current)
        assert int(current_group.order()) == current_order
    J = group(join(current, target))
    joined_order = int(J.order())
    assert joined_order % current_order == 0
    kernel_order = joined_order // current_order
    assert 24 % kernel_order == 0
    result = dict(partial)
    result.update({
        "faithful_degree": len(current[0]),
        "full_mixed_order": current_order,
        "joined_markedS4_order": joined_order,
        "projection_kernel_order": kernel_order,
        "retains_markedS4": kernel_order == 1,
        "common_marked_quotient_order": 24 // kernel_order,
        "elapsed_seconds": time.monotonic() - start,
        "status": "PASS",
        "scope": "Exact whole mixed marked image; all discarded orbit kernels certified by joined-order equality.",
    })
    subset = np.concatenate([data[f"orbit_{k}"] for k in selected])
    np.savez_compressed(STEM.with_suffix(".npz"), subset=subset, generators=current, target=target)
    STEM.with_name(STEM.name + "_state.pkl").write_bytes(
        pickle.dumps((current_group.args, current_group.__dict__))
    )
    STEM.with_name(STEM.name + "_joined_state.pkl").write_bytes(
        pickle.dumps((J.args, J.__dict__))
    )
    STEM.with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2), flush=True)


if __name__ == "__main__":
    run()
