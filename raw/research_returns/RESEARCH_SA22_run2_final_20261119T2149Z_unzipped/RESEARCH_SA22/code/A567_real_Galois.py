#!/usr/bin/env python3
"""Exact finite witness for the real-place Galois obstruction.

The mathematical proof identifies Gal(Q(cuberoot(2),zeta_3)/Q) with S_3.
This certificate checks the specified permutations, their orders, the
conjugation of complex conjugation, and its centralizer in that quotient.
It does not claim to enumerate the infinite absolute Galois group.
"""
import itertools
import json
from pathlib import Path
from time import perf_counter
import sympy as sp

started = perf_counter()

identity = (0, 1, 2)

def mul(p, q):
    """Composition p after q."""
    return tuple(p[q[i]] for i in range(3))

def inverse(p):
    return tuple(p.index(i) for i in range(3))

def order(p):
    out = identity
    for n in range(1, 7):
        out = mul(out, p)
        if out == identity:
            return n
    raise AssertionError("Not an S3 permutation")

group = list(itertools.permutations(range(3)))
# Labels are alpha, alpha*zeta_3, alpha*zeta_3^2.
c = (0, 2, 1)
sigma = (1, 2, 0)
conjugate = mul(mul(sigma, c), inverse(sigma))
commutator = mul(conjugate, inverse(c))
centralizer = [p for p in group if mul(p, c) == mul(c, p)]

assert len(group) == 6
assert order(c) == 2
assert order(sigma) == 3
assert conjugate != c
assert order(commutator) == 3
assert set(centralizer) == {identity, c}

# Check the exact symbolic elliptic family used to prove outer faithfulness.
j = sp.Symbol("j")
k = j / (j - 1728)
a, b = -3 * k, -2 * k
discriminant = sp.factor(-16 * (4 * a**3 + 27 * b**2))
j_invariant = sp.cancel(1728 * 4 * a**3 / (4 * a**3 + 27 * b**2))
assert j_invariant == j
assert sp.cancel(discriminant - 1728 * k**2 * (k - 1)) == 0

result = {
    "group": "S3 on alpha, alpha*zeta_3, alpha*zeta_3^2",
    "composition": "p*q means p after q",
    "order": len(group),
    "complex_conjugation": c,
    "sigma": sigma,
    "sigma_c_sigma_inverse": conjugate,
    "commutator_sigma_c": commutator,
    "commutator_order": order(commutator),
    "centralizer_of_c": centralizer,
    "elliptic_family": {
        "k": str(k),
        "a": str(a),
        "b": str(b),
        "discriminant": str(discriminant),
        "j_invariant": str(j_invariant),
        "excluded_values": [0, 1728],
    },
    "all_assertions_passed": True,
    "checks_count": 8,
    "elapsed_seconds": perf_counter() - started,
    "run_note": "Subsequent timed run; the first successful run was not timed",
    "scope": "All six permutations of S3, six finite-group assertions, and two exact rational-function assertions; no enumeration of the absolute Galois group",
}
path = Path(__file__).resolve().parents[1] / "logs" / "A567_real_Galois.json"
path.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
