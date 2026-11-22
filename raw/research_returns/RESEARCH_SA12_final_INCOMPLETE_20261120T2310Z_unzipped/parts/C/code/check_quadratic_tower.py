#!/usr/bin/env python3
"""Exact finite certificates for the quadratic-step A.2 construction.

We check the finite groups for r=1,2,3, exhaustively on the indicated
sets, and the seed field Q(sqrt(-35)).  Chebotarev, class field theory,
and the infinite tower are proved in the accompanying TeX, not inferred
from this finite computation.
"""
from collections import deque
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
from time import perf_counter

START = perf_counter()
CHECKS = 0


def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def certify_rank(r):
    q = 1 << r
    vectors = range(q)
    masks = range(1 << q)
    target = list(product(vectors, vectors, range(2)))
    ident = (0, 0, 0)
    tau = (0, 0, 1)

    def mul(a, b):
        x, y, e = a
        u, v, f = b
        return (x ^ (v if e else u), y ^ (u if e else v), e ^ f)

    def inv(a):
        x, y, e = a
        return (y, x, e) if e else a

    def phi(mask):
        parity = mask.bit_count() % 2
        total = 0
        for g in vectors:
            if (mask >> g) & 1:
                total ^= g
        return parity, total

    phi_values = [phi(m) for m in masks]

    def translate(mask, v):
        return sum(((mask >> g) & 1) << (g ^ v) for g in vectors)

    def source_mul(a, b):
        m, v = a
        n, w = b
        return m ^ translate(n, v), v ^ w

    def mapping(a):
        m, v = a
        b, u = phi_values[m]
        return mul((u, u, b), (v, 0, 0))

    # Linearity and equivariance of the module quotient, for every pair.
    for m in masks:
        b, u = phi_values[m]
        for n in masks:
            c, w = phi_values[n]
            check(phi_values[m ^ n] == (b ^ c, u ^ w), "linearity")
        for v in vectors:
            check(phi_values[translate(m, v)] == (b, u ^ (v if b else 0)),
                  "equivariance")
    check(len(set(phi_values)) == 2 * q, "module quotient surjective")

    # Verify the induced group map on every element and every generator.
    source = list(product(masks, vectors))
    generators = [(1 << g, 0) for g in vectors]
    generators += [(0, 1 << j) for j in range(r)]
    images = {mapping(a) for a in source}
    check(images == set(target), "group quotient surjective")
    for a in source:
        check(mapping(a)[0] ^ mapping(a)[1] == a[1], "old quotient")
        for g in generators:
            check(mapping(source_mul(g, a)) == mul(mapping(g), mapping(a)),
                  "homomorphism on all elements and generators")
    seen = {(0, 0)}
    queue = deque(seen)
    while queue:
        a = queue.popleft()
        for g in generators:
            b = source_mul(g, a)
            if b not in seen:
                seen.add(b)
                queue.append(b)
    check(len(seen) == len(source), "the tested generators generate")

    # Compute transfer from the coset definition, independently of formula.
    def transfer(a):
        result = ident
        for e in range(2):
            rep = tau if e else ident
            newrep = tau if e ^ a[2] else ident
            factor = mul(mul(rep, a), inv(newrep))
            check(factor[2] == 0, "transfer factor lies in H")
            result = mul(result, factor)
        return result

    transfers = {}
    for a in target:
        check(mul(a, inv(a)) == ident == mul(inv(a), a), "inverse")
        check(mul(ident, a) == a == mul(a, ident), "identity")
        x, y, e = a
        transfers[a] = transfer(a)
        check(transfers[a] == (x ^ y, x ^ y, 0), "transfer formula")
        v = x ^ y
        if v:
            check((mul(a, a) == (v, v, 0)) == bool(e),
                  "nonzero old Frobenius forces new inertness")
    for a in target:
        for b in target:
            check(transfers[mul(a, b)] == mul(transfers[a], transfers[b]),
                  "transfer is a homomorphism")

    # Every possible local Frobenius pattern and new-prime inertia image.
    inertia_images = []
    for g in vectors:
        c = mapping((1 << g, 0))
        conj = mul(mul((g, 0, 0), tau), (g, 0, 0))
        check(c == conj == (g, g, 1), "inertia is complement conjugate")
        check(mul(c, c) == ident and c[2] == 1, "inertia intersects H trivially")
        inertia_images.append(c)
        for v in vectors:
            if v:
                check(phi_values[(1 << g) ^ (1 << (g ^ v))] == (0, v),
                      "old degree-two local Frobenius")
    check(len({(v, v, 0) for v in vectors}) == q, "diagonal transfer injective")
    check(sum(a[2] == 0 for a in target) == q * q, "new class quotient rank doubles")
    return {
        "r": r,
        "source_order": len(source),
        "wreath_order": len(target),
        "module_quotient_order": 2 * q,
        "unramified_class_quotient_order": q * q,
        "all_source_elements_and_generator_products_checked": len(source) * len(generators),
        "all_target_transfer_products_checked": len(target) ** 2,
        "inertia_complements": inertia_images,
    }


def certify_seed():
    check(1 - 4 * 9 == -35, "seed discriminant")
    check(all(35 % (p * p) for p in (2, 3, 5)), "35 squarefree")
    check(-35 % 4 == 1, "maximal quadratic integer basis")
    check(4 * 35 < 16 * 9, "Minkowski bound less than four using pi greater than three")
    roots2 = [x for x in range(2) if (x*x - x + 9) % 2 == 0]
    roots3 = [x for x in range(3) if (x*x - x + 9) % 3 == 0]
    check(roots2 == [], "two is inert")
    check(roots3 == [0, 1], "three splits with distinct roots")
    check(9 == 3**2 and 1 % 3 != 0, "norm w and unit at conjugate prime")
    check(Fraction(35, 4) > 3, "nonzero y excludes norm three")
    check(all(x*x != 3 for x in range(-2, 3)), "y zero excludes norm three")
    for x, y in product(range(-7, 8), repeat=2):
        check(x*x + x*y + 9*y*y == (Fraction(x) + Fraction(y, 2))**2
              + Fraction(35, 4)*y*y, "completed-square identity")
    forms = []
    for a in range(1, 4):
        for b in range(-a, a + 1):
            if (b*b + 35) % (4*a):
                continue
            c = (b*b + 35) // (4*a)
            if c < a or ((abs(b) == a or a == c) and b < 0):
                continue
            forms.append((a, b, c))
    check(forms == [(1, 1, 9), (3, 1, 3)], "independent reduced-form certificate")
    return {
        "field": "Q(sqrt(-35))",
        "integer_polynomial": "w^2-w+9",
        "discriminant": -35,
        "roots_mod_2": roots2,
        "roots_mod_3": roots3,
        "reduced_forms": forms,
        "class_group": "C2",
        "dyadic_prime_principal": True,
        "class_group_after_inverting_2": "C2",
        "proof_scope": "The exact identities certify the explicit Minkowski/norm proof in the TeX.",
    }


report = {
    "status": "passed",
    "groups": [certify_rank(r) for r in (1, 2, 3)],
    "seed": certify_seed(),
}
report["assertions_passed"] = CHECKS
report["elapsed_seconds"] = perf_counter() - START
report["scope"] = "Finite group and seed-field checks only; the infinite arithmetic construction is proved in the accompanying manuscript."
destination = Path(__file__).resolve().parents[1] / "output" / "quadratic_tower_certificate.json"
destination.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
