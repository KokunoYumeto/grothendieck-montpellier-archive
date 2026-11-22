#!/usr/bin/env python3
"""Exact finite check of the multiplier/outer action in BMO17, section 3.3.1.

No character tables or author arithmetic are imported.  We enumerate kernels of
all characters of C4^2 x C3, then simultaneous outer orbits of (kernel, cyclic
outer subgroup).  The two order-four kernel orbits are deliberately unnamed:
the source's centralization prose disagrees with its displayed action on these
labels, whereas its complete 36-extension list is unaffected.
"""
import hashlib
import itertools
import json
import pathlib
import time

start = time.perf_counter()
M = tuple(itertools.product(range(4), range(4), range(3)))
index = {x: i for i, x in enumerate(M)}
identity = tuple(range(len(M)))


def permutation(fun):
    return tuple(index[fun(*x)] for x in M)


def mul(g, h):
    return tuple(g[h[i]] for i in range(len(M)))


def power(g, n):
    z = identity
    for _ in range(n):
        z = mul(z, g)
    return z


def inverse(g):
    h = [0] * len(g)
    for i, j in enumerate(g):
        h[j] = i
    return tuple(h)


# BMO: 6 sends a->b^3,b->c^3; 2_2 fixes a and swaps b,c;
# c=(ab)^-1.  The rotation fixes C3, each outer reflection inverts it.
R = permutation(lambda x, y, z: (y % 4, (3*x+y) % 4, z))
S = permutation(lambda x, y, z: ((x+3*y) % 4, 3*y % 4, -z % 3))
assert power(R, 6) == identity and power(R, 3) != identity
assert power(S, 2) == identity
assert mul(mul(S, R), S) == inverse(R)
A = set()
for i in range(6):
    A.add(power(R, i))
    A.add(mul(power(R, i), S))
assert len(A) == 12
assert all(mul(g, h) in A for g in A for h in A)


def cyclic(g):
    result, h = set(), identity
    while h not in result:
        result.add(h)
        h = mul(h, g)
    assert h == identity
    return frozenset(result)


cyclic_subgroups = {cyclic(g) for g in A}
assert sorted(map(len, cyclic_subgroups)) == [1] + [2]*7 + [3, 6]

# Every irreducible image has cyclic center, so its kernel on M is the kernel
# of one character.  Values are represented as exponents modulo twelve.
kernels = {
    frozenset(i for i, (x, y, z) in enumerate(M)
              if (3*(p*x+q*y)+4*r*z) % 12 == 0)
    for p in range(4) for q in range(4) for r in range(3)
}
assert len(kernels) == 20


def image_kernel(g, K):
    return frozenset(g[i] for i in K)


def conjugate(g, H):
    gi = inverse(g)
    return frozenset(mul(mul(g, h), gi) for h in H)


remaining = set(kernels)
kernel_orbits = []
while remaining:
    K = min(remaining, key=lambda k: (len(k), sorted(k)))
    orbit = {image_kernel(g, K) for g in A}
    assert orbit <= remaining
    remaining -= orbit
    stabilizer = {g for g in A if image_kernel(g, K) == K}
    kernel_orbits.append((K, orbit, stabilizer))
assert len(kernel_orbits) == 8
assert sorted((48//len(K), len(O), len(N)) for K, O, N in kernel_orbits) == [
    (1, 1, 12), (2, 3, 4), (3, 1, 12), (4, 3, 4),
    (4, 3, 4), (6, 3, 4), (12, 3, 4), (12, 3, 4)]

pairs = {(K, H) for K in kernels for H in cyclic_subgroups
         if all(image_kernel(g, K) == K for g in H)}
pair_orbits = []
while pairs:
    K, H = min(pairs, key=lambda kh: (
        48//len(kh[0]), sorted(kh[0]), len(kh[1]), sorted(kh[1])))
    orbit = {(image_kernel(g, K), conjugate(g, H)) for g in A}
    assert orbit <= pairs
    pairs -= orbit
    pair_orbits.append({
        "center_order": 48//len(K), "outer_cyclic_order": len(H),
        "orbit_size": len(orbit), "kernel_indices": sorted(K),
    })
assert len(pair_orbits) == 36
profile = {}
for row in pair_orbits:
    key = f"{row['center_order']}:{row['outer_cyclic_order']}"
    profile[key] = profile.get(key, 0) + 1
assert profile == {
    "1:1": 1, "1:2": 3, "1:3": 1, "1:6": 1,
    "2:1": 1, "2:2": 3,
    "3:1": 1, "3:2": 3, "3:3": 1, "3:6": 1,
    "4:1": 2, "4:2": 6,
    "6:1": 1, "6:2": 3,
    "12:1": 2, "12:2": 6,
}

# Inspect the source's labeling issue explicitly, without using the disputed
# sentence in the proof or in any representation-table identification.
Ka = frozenset(index[(x, 0, z)] for x in range(4) for z in range(3))
Kab2 = frozenset(index[(x, 2*x % 4, z)] for x in range(4) for z in range(3))


def trivial_on_quotient(g, K):
    for i, (x, y, z) in enumerate(M):
        X, Y, Z = M[g[i]]
        if index[((X-x) % 4, (Y-y) % 4, (Z-z) % 3)] not in K:
            return False
    return True


assert not trivial_on_quotient(S, Ka)
assert trivial_on_quotient(S, Kab2)
result = {
    "status": "PASS", "elapsed_seconds": round(time.perf_counter()-start, 6),
    "multiplier_order": 48, "outer_order": 12,
    "character_kernels": 20, "kernel_orbits": 8,
    "cyclic_outer_subgroups": 10, "bicyclic_pair_orbits": 36,
    "profile": profile, "pair_orbits": pair_orbits,
    "source_label_warning": (
        "The displayed 2_2 action in BMO section3.3.1 inverts M4/<a> and "
        "centralizes M4/<ab^2>; the next prose calls these the other way. "
        "Only the unordered pair of order4 covers and Lemma3.1's full list "
        "are used; completeness does not depend on this disputed label."
    ),
    "scope": "Finite multiplier-action enumeration only; no character-table or eigenvalue scan.",
}
out = pathlib.Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k: v for k, v in result.items() if k != 'pair_orbits'}, indent=2))
