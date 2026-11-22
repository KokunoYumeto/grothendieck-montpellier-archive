#!/usr/bin/env python3
"""Independent finite supplements to OL04--05; no author helper is imported.

The all-dimensional orbit, commutant and source arguments are checked in the
companion report.  This independently checks a small orbit example without
enumerating either group, and tests the actual stabilizer symmetry directly.
"""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import hashlib, json, time

started = time.perf_counter()
base = Path(__file__).resolve().parent
proof = base.parents[1] / 'imprimitive/orthogonal_lowlevels/orthogonal_lowlevel_section.tex'
digest = hashlib.sha256(proof.read_bytes()).hexdigest()
assert digest == '2f40c6daf6ead0f9cad0aa0ac77f1fb9699b55396c215cc3c24c3f34cd9894e7'

# Interleaved hyperbolic coordinates differ from the author's x/y blocks.
vectors = [tuple((v >> k) & 1 for k in range(6)) for v in range(64)]
def quad(v):
    x = vectors[v]
    return sum(x[k]*x[k+1] for k in (0,2,4)) % 2
def polar(v,w):
    return quad(v^w)^quad(v)^quad(w)
roots = [v for v in range(64) if quad(v)]
symmetries = [[x ^ (v if polar(x,v) else 0) for x in range(64)] for v in roots]
assert len(roots) == 28
for s in symmetries:
    assert all(s[s[x]] == x and quad(s[x]) == quad(x) for x in range(64))
anchor = symmetries[0]
even_generators = [[anchor[s[x]] for x in range(64)] for s in symmetries[1:]]

def orbit_partition(generators):
    # Union-find on 64^2 states; no closure or claimed group order is used.
    parent = list(range(4096))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for g in generators:
        for x in range(64):
            for y in range(64):
                a,b = find(64*x+y),find(64*g[x]+g[y])
                if a != b:
                    parent[max(a,b)] = min(a,b)
    return [find(a) for a in range(4096)]
whole_orbits = orbit_partition(symmetries)
even_orbits = orbit_partition(even_generators)
assert whole_orbits == even_orbits
orbit_sizes = sorted(Counter(whole_orbits).values())
assert len(orbit_sizes) == 15

# Every span of at most two vectors is fixed pointwise by an odd symmetry.
# This directly checks the stabilizer-surjectivity conclusion in this model.
spans = {tuple(sorted({0,x,y,x^y})) for x in range(64) for y in range(64)}
for span in spans:
    candidate = next(v for v in roots if all(polar(v,r)==0 for r in span))
    s = symmetries[roots.index(candidate)]
    assert all(s[r] == r for r in span)
    assert sum(s[x] != x for x in range(64)) == 32
assert len(spans) == 715

binary_cases = 0
for p in (3,5,7,11,13,17,19,23):
    for a in range(1,p):
        for b in range(1,p):
            represented = {(a*x*x+b*y*y)%p for x in range(p) for y in range(p)}
            assert represented == set(range(p))
            binary_cases += 1

J = 10**30
assert 4*(J-1)+2 == 4*J-2 and 4*(J-1)+1 == 4*J-3
delta = (1-Fraction(9,16))/4
assert delta == Fraction(7,64)
assert 6/(1+10*delta-2) == 64
assert 16**6*15 > 64
prime_powers = sorted({p**k for p in (2,3,5,7,11,13) for k in range(1,5) if p**k < 16})
assert prime_powers == [2,3,4,5,7,8,9,11,13]

out = {
    'status':'PASS', 'proof_sha256':digest,
    'scope':'Independent exact finite supplement, not a replacement for the universal proof',
    'pair_states':4096, 'symmetry_generators':28, 'even_product_generators':27,
    'pair_orbits':15, 'orbit_sizes':orbit_sizes,
    'stabilizer_symmetry_spans':len(spans),
    'binary_forms':binary_cases, 'support':str(delta),
    'degree_ceiling':64, 'remaining_prime_powers':prime_powers,
    'seconds':time.perf_counter()-started,
}
base.joinpath('audit_orthogonal_lowlevels.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
