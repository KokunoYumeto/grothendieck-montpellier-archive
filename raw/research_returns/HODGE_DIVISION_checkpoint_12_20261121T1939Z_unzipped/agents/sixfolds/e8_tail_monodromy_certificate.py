#!/usr/bin/env python3
"""Exact braid monodromy on the two-dimensional E8 tail factor.

Input: the sibling's certified eight-branch tuple and its parabolic quotient.
This script checks explicit returning braid words and their quotient action.
It does not claim rank nine for the original twelve-branch period map.
"""
from pathlib import Path
import sys
import json
import hashlib

HERE = Path(__file__).resolve().parent
SIBLING = HERE.parent / "imprimitive"
sys.path.insert(0, str(SIBLING / "g31_rerun"))
import gaussian_exact as M

INPUT = SIBLING / "e8_search" / "tuple_certificate.json"
data = json.loads(INPUT.read_text())


def decode(a):
    return [[M.F(x[0], x[1]) for x in row] for row in a]


simple = [M.mat(a) for a in data["simple_reflections"]]
tail = simple[:6] + [decode(data["h"]), decode(data["g"])]
I = M.eye(8)
P = decode(data["tail_parabolic"]["quotient_basis"])
G = decode(data["tail_parabolic"]["cup_gram"])

blocks = []
offset = 0
for g in tail:
    a = M.sub(I, g)
    cols = M.rref(a)[1]
    U = M.tr([M.tr(a)[j] for j in cols])
    dim = len(cols)
    blocks.append(M.mul(U, P[offset:offset + dim]))
    offset += dim
assert offset == len(P)
C = [row for block in blocks for row in block]
B = [row for g in tail for row in M.sub(I, g)]
E = [r + s for r, s in zip(B, C)]
rows = M.rref(M.tr(E))[1]
assert len(rows) == 10
left = M.inv([E[j] for j in rows])


def project(cocycles):
    coordinates = M.mul(left, [cocycles[j] for j in rows])
    assert M.mul(E, coordinates) == cocycles
    return coordinates[8:]


def braid_step(tuple_, cocycles, i):
    """Left cocycles: delta(gh)=delta(g)+g delta(h).

    Hurwitz (g,h)->(h,h^-1 g h);
    (v,w)->(w,h^-1(v+(g-I)w)).
    """
    gs = [a for a in tuple_]
    vs = [row[:] for row in cocycles]
    g, h = gs[i], gs[i + 1]
    hi = M.inv(h)
    v = vs[8 * i:8 * (i + 1)]
    w = vs[8 * (i + 1):8 * (i + 2)]
    gs[i] = h
    gs[i + 1] = M.mul(hi, M.mul(g, h))
    vs[8 * i:8 * (i + 1)] = w
    vs[8 * (i + 1):8 * (i + 2)] = M.mul(
        hi, M.add(v, M.mul(M.sub(g, I), w)))
    return gs, vs


loops = []
monodromies = []
for i in range(len(tail) - 1):
    gs = tail
    vs = C
    for power in range(1, 193):
        gs, vs = braid_step(gs, vs, i)
        if gs == tail:
            T = project(vs)
            assert M.mul(M.star(T), M.mul(G, T)) == G
            loops.append({
                "braid_generator": i + 1, "returning_power": power,
                "matrix": M.serialize(T), "identity": T == M.eye(2),
                "trace": (T[0][0] + T[1][1]).pair(),
                "determinant": M.det(T).pair(),
            })
            monodromies.append(T)
            break
    else:
        raise AssertionError("No return found in the explicit finite bound")

hyperbolic = None
for i, a in enumerate(monodromies):
    for j, b in enumerate(monodromies):
        c = M.mul(a, b)
        trace = c[0][0] + c[1][1]
        det = M.det(c)
        if det == M.ONE and not trace.b and abs(trace.a) > 2:
            hyperbolic = {
                "loop_indices": [i, j], "matrix": M.serialize(c),
                "trace": trace.pair(), "determinant": det.pair(),
                "infinite_order_reason": "real trace of absolute value >2 and determinant1",
            }
            break
    if hyperbolic:
        break

report = {
    "status": "PASS" if hyperbolic else "CHECKED_LOOPS_NO_INFINITE_ORDER_WITNESS",
    "input_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
    "coefficient_field": "Q(i)",
    "cocycle_convention": "left: delta(gh)=delta(g)+g delta(h)",
    "tail_dimension": 2,
    "tail_signature": [1, 1],
    "loops": loops,
    "infinite_order_witness": hyperbolic,
    "scope": (
        "Returning braid actions are exact. An infinite-order witness would "
        "prove the residual period map nonconstant, hence generic rank1; "
        "it does not prove rank9 for the full sixfold period map."
    ),
}
output = HERE / "e8_tail_monodromy_certificate_output.json"
output.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({
    "status": report["status"],
    "loops": [{k: v for k, v in row.items() if k != "matrix"} for row in loops],
    "infinite_order_witness": hyperbolic,
    "output": str(output),
}))
