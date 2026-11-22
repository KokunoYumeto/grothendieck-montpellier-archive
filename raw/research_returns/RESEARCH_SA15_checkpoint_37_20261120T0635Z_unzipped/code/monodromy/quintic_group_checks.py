#!/usr/bin/env python3
"""Exact finite checks used in the characteristic-two quintic proof.

This checks incidence linear ranks, maximal subgroup order obstructions,
the orbit calculations for the full stabilizer and its complement, and
the elementary cocycle equations.  It does not claim to recompute the
published maximal subgroup classification or to infer monodromy from
isolated Frobenius matrices.
"""
import json
import time
from pathlib import Path

started = time.perf_counter()

def binary_rank(rows):
    pivots = {}
    for r in rows:
        while r:
            j = r.bit_length() - 1
            if j in pivots:
                r ^= pivots[j]
            else:
                pivots[j] = r
                break
    return len(pivots)

monomials = [(a,b,5-a-b) for a in range(6) for b in range(6-a)]

# On Q: X=s^2, Y=st, Z=t^2, the five odd exponents of s must vanish.
smooth_equations = []
for exponent in [1,3,5,7,9]:
    row = sum(1 << j for j,(a,b,c) in enumerate(monomials)
              if 2*a+b == exponent)
    smooth_equations.append(row)
smooth_rank = binary_rank(smooth_equations)
assert smooth_rank == 5

# On Q=XY=0, P=[0:0:1], restrictions must be X times a quadratic square
# and Y times a quadratic square.  The forbidden monomials are Z^5,
# X^2 Z^3, X^4 Z, Y^2 Z^3, Y^4 Z.
forbidden = {(0,0,5),(2,0,3),(4,0,1),(0,2,3),(0,4,1)}
reducible_equations = [1 << monomials.index(a) for a in forbidden]
reducible_rank = binary_rank(reducible_equations)
assert reducible_rank == 5

# Six-dimensional representation with distinguished fixed v=e_0.
def transvection(x, i, j):
    return x ^ (((x >> j) & 1) << i)

complement_generators = [(i,j) for i in range(1,6)
                         for j in range(1,6) if i != j]
stabilizer_generators = complement_generators + [(0,j) for j in range(1,6)]

def orbits(gens):
    unseen = set(range(64))
    out = []
    while unseen:
        start = min(unseen)
        orbit = {start}
        todo = [start]
        while todo:
            x = todo.pop()
            for i,j in gens:
                y = transvection(x,i,j)
                if y not in orbit:
                    orbit.add(y)
                    todo.append(y)
        unseen.difference_update(orbit)
        out.append(sorted(orbit))
    return out

complement_orbits = orbits(complement_generators)
stabilizer_orbits = orbits(stabilizer_generators)
assert sorted(map(len,complement_orbits)) == [1,1,31,31]
assert sorted(map(len,stabilizer_orbits)) == [1,1,62]

gl5_order = 1
for i in range(5):
    gl5_order *= 32 - 2**i
stabilizer_order = 32 * gl5_order
assert gl5_order == 9999360 and stabilizer_order == 319979520
maximal_subgroup_orders = [10321920,10321920,9999360,2064384,2064384,4960]
order_checks = [{"order":a,"divisible_by_31":a%31 == 0,
                 "divisible_by_7":a%7 == 0,
                 "index":stabilizer_order//a}
                for a in maximal_subgroup_orders]
assert [x['order'] for x in order_checks
        if x['divisible_by_31'] and x['divisible_by_7']] == [gl5_order]

# Linear cocycle constraints for all elementary transvections in GL_m(2).
# Unknowns are coordinates of c(t_ij).  The order-two, commuting, and
# Steinberg conjugation relations suffice to leave exactly m dimensions,
# all supplied by coboundaries.  No group presentation assumption is used
# for the upper bound: every cocycle must obey these relations.
def cocycle_relation_dimension(m):
    pairs = [(i,j) for i in range(m) for j in range(m) if i != j]
    pos = {(i,j,k): m*h+k for h,(i,j) in enumerate(pairs) for k in range(m)}
    rows = []
    def formal(i,j):
        return [1 << pos[i,j,k] for k in range(m)]
    def act(v, i,j):
        w = v[:]
        w[i] ^= w[j]
        return w
    def word_cocycle(word):
        ans = [0]*m
        preceding = []
        for pair in word:
            vec = formal(*pair)
            for a,b in reversed(preceding):
                vec = act(vec,a,b)
            ans = [a^b for a,b in zip(ans,vec)]
            preceding.append(pair)
        return ans
    def relation(left,right):
        rows.extend(a^b for a,b in zip(word_cocycle(left),word_cocycle(right)))
    for i,j in pairs:
        relation([(i,j),(i,j)], [])
    for i,j in pairs:
        for k,l in pairs:
            if j != k and i != l:
                relation([(i,j),(k,l)], [(k,l),(i,j)])
    for i in range(m):
        for j in range(m):
            for k in range(m):
                if len({i,j,k}) == 3:
                    relation([(i,j),(j,k),(i,j)],[(j,k),(i,k)])
    unknowns = m*m*(m-1)
    return {"dimension":m,"unknowns":unknowns,
            "relation_rank":binary_rank(rows),
            "solution_dimension":unknowns-binary_rank(rows)}

cocycle_checks = [cocycle_relation_dimension(m) for m in [4,5,6]]
assert all(c['solution_dimension'] == c['dimension'] for c in cocycle_checks)

result = {
    "monomials_degree5":monomials,
    "smooth_conic":{"constraint_rank":smooth_rank,"affine_quintic_fibre_dimension":21-smooth_rank,
                    "conic_parameter_dimension":5,"total_projective_incidence_dimension":20},
    "reduced_reducible_conic":{"constraint_rank":reducible_rank,
                    "affine_quintic_fibre_dimension":21-reducible_rank,
                    "conic_parameter_dimension":4,"total_projective_incidence_dimension":19},
    "GL5_order":gl5_order,"stabilizer_order":stabilizer_order,
    "maximal_subgroup_order_checks":order_checks,
    "complement_orbits":complement_orbits,
    "stabilizer_orbits":stabilizer_orbits,
    "cocycle_checks":cocycle_checks,
    "elapsed_seconds":time.perf_counter()-started,
    "scope":"Exact elementary checks only. Maximal subgroup classification is the cited Basheer-Moori Table 1 / ATLAS input. Geometric monodromy proof is in quintic_exact.tex."
}
output = Path(__file__).resolve().parents[1]/'outputs'/'quintic_group_checks.json'
output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
