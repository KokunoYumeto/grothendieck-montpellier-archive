#!/usr/bin/env python3
"""Exact certificate for the proved AT18 modulo-two variation identity.

The free graded-commutative F2 algebra is reduced by T^2=TC=0.
Odd squares vanish. No cohomology or infinite-stage claim is inferred
from this finite symbolic verification.
"""
from collections import Counter
from pathlib import Path
import json
import time

START = time.perf_counter()
DEG = {
    "T": 0, "C": 0, "H": 0, "g": 1, "x": 1,
    "r": 2, "a": 2, "E": 3, "eta": 3, "z": 4,
    "alpha": 0, "beta": 0, "rho": 1, "chi": 1, "nu": 2,
    "dalpha": 1, "dbeta": 1, "drho": 2, "dchi": 2, "dnu": 3,
}
ORDER = {v: i for i, v in enumerate(DEG)}
ZERO = frozenset()

def canonical(m):
    c = Counter(m)
    if c["T"] >= 2 or (c["T"] and c["C"]):
        return None
    if any(DEG[v] % 2 and n >= 2 for v, n in c.items()):
        return None
    return tuple(sorted(m, key=ORDER.get))

def add(*ps):
    out = set()
    for p in ps:
        out.symmetric_difference_update(p)
    return frozenset(out)

def var(v):
    return frozenset({(v,)})

def mul(p, q):
    out = set()
    for a in p:
        for b in q:
            m = canonical(a+b)
            if m is None:
                continue
            if m in out:
                out.remove(m)
            else:
                out.add(m)
    return frozenset(out)

def prod(*ps):
    out = frozenset({()})
    for p in ps:
        out = mul(out, p)
    return out

V = {v: var(v) for v in DEG}
D = {v: ZERO for v in DEG}
for src, dst in (("C","x"),("H","g"),("g","r"),("x","a"),
                 ("r","E"),("a","eta"),("E","z")):
    D[src] = prod(V["T"], V[dst])
for v in ("alpha","beta","rho","chi","nu"):
    D[v] = V["d"+v]

def diff(p):
    out = ZERO
    for m in p:
        for i, v in enumerate(m):
            rest = frozenset({m[:i]+m[i+1:]})
            out = add(out, mul(rest, D[v]))
    return out

checks = 0
for v in DEG:
    assert not diff(D[v]), v
    checks += 1
assert not diff(prod(V["T"], V["C"]))
checks += 1
delta = {
    "C": prod(V["T"],V["beta"]),
    "H": prod(V["T"],V["alpha"]),
    "g": add(V["dalpha"],prod(V["T"],V["rho"])),
    "x": add(V["dbeta"],prod(V["T"],V["chi"])),
    "r": add(V["drho"],prod(V["T"],V["nu"])),
    "a": V["dchi"],
}
B = add(prod(V["a"],V["H"]), prod(V["C"],V["r"]),
        prod(V["g"],V["x"]))
NEW = {v: add(V[v],delta[v]) for v in delta}
Bnew = add(prod(NEW["a"],NEW["H"]), prod(NEW["C"],NEW["r"]),
           prod(NEW["g"],NEW["x"]))
primitive = add(
    prod(V["chi"],V["H"]),prod(V["C"],V["rho"]),
    prod(V["g"],V["beta"]),prod(V["alpha"],V["x"]),
    prod(V["alpha"],V["dbeta"]),
    prod(V["T"],V["alpha"],V["chi"]),
    prod(V["T"],V["beta"],V["rho"]),
)
assert not add(Bnew,B,diff(primitive))
checks += 1
output = {
    "status": "passed",
    "statement": "AT18",
    "checks": checks,
    "scope": "Exact symbolic modulo-two homotopy identity and all displayed generator d-squares; no cohomology inference.",
    "identity": "B_new-B_old=d(chi H+C rho+g beta+alpha x+alpha d beta+T alpha chi+T beta rho)",
    "relations": ["T^2=0", "TC=0", "odd squares=0"],
    "runtime_seconds": time.perf_counter()-START,
}
dest = Path(__file__).resolve().parents[1]/"logs"/"A_integral_period_check.json"
dest.write_text(json.dumps(output,indent=2)+"\n")
print(json.dumps(output))
