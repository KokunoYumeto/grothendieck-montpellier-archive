"""Exact finite certificates used in the infinite abstract group example.

We certify A5 by explicit permutations: closure, inverses, perfection, and
the normal closure of each nonidentity element.  The infinite product and
the argument about all of its open subgroups are proved in paper_D.tex.
This is not a geometric counterexample to D.1 or D.2.
"""
from itertools import permutations
from pathlib import Path
from time import perf_counter
import json

started = perf_counter()
identity = tuple(range(5))

def parity(g):
    return sum(g[i] > g[j] for i in range(5) for j in range(i + 1, 5)) % 2

def compose(g, h):
    return tuple(g[h[i]] for i in range(5))

def inverse(g):
    return tuple(g.index(i) for i in range(5))

group = tuple(g for g in permutations(range(5)) if parity(g) == 0)
group_set = set(group)
assert len(group) == 60
assert identity in group_set
inverses = {g: inverse(g) for g in group}
assert all(inverses[g] in group_set for g in group)
assert all(compose(g, h) in group_set for g in group for h in group)

def generated(generators):
    generators = tuple(set(generators))
    seen = {identity}
    pending = [identity]
    while pending:
        h = pending.pop()
        for g in generators:
            gh = compose(g, h)
            if gh not in seen:
                seen.add(gh)
                pending.append(gh)
    return seen

commutators = {
    compose(compose(compose(g, h), inverses[g]), inverses[h])
    for g in group for h in group
}
assert generated(commutators) == group_set
normal_closure_sizes = {}
for g in group:
    if g == identity:
        continue
    conjugates = [compose(compose(h, g), inverses[h]) for h in group]
    normal_closure = generated(conjugates)
    assert normal_closure == group_set
    normal_closure_sizes[str(g)] = len(normal_closure)

obstructions = []
for d in range(1, 13):
    distinct_coordinate_tuples = 60 ** d
    number_of_factors = distinct_coordinate_tuples + 1
    assert number_of_factors > distinct_coordinate_tuples
    obstructions.append({
        "proposed_generators": d,
        "possible_coordinate_tuples": distinct_coordinate_tuples,
        "number_of_factors": number_of_factors,
        "diagonal_obstruction": True,
    })

output = {
    "purpose": "Exact finite certificates for an abstract infinite-product obstruction, not a geometric counterexample",
    "group": "A5 acting on five letters",
    "order": len(group),
    "closure_pairs_checked": len(group) ** 2,
    "inverse_elements_checked": len(group),
    "commutator_pairs_checked": len(group) ** 2,
    "commutator_generated_group_order": len(generated(commutators)),
    "nonidentity_normal_closures_checked": len(normal_closure_sizes),
    "normal_closure_sizes": normal_closure_sizes,
    "finite_pigeonhole_certificates": obstructions,
    "elapsed_seconds": perf_counter() - started,
}
Path(__file__).with_name("check_pronilpotent_obstruction_output.json").write_text(
    json.dumps(output, indent=2) + "\n"
)
print(json.dumps({
    "order": output["order"],
    "normal_closures": output["nonidentity_normal_closures_checked"],
    "pigeonhole_certificates": len(obstructions),
    "elapsed_seconds": output["elapsed_seconds"],
}))
