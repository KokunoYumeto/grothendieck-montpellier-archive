#!/usr/bin/env python3
"""Exact exterior-algebra checks for SF-E801--E803.

These finite linear algebra checks verify the stated wedge ranks and common
annihilator.  They do not construct a sheaf, prove semiregularity, or certify a
geometric eightfold family.  The Grassmannian reconstruction and algebraic
subgroup argument are proved separately in eightfold_obstructions.md.
"""
from itertools import combinations
from pathlib import Path
import json
import sympy as S

DIM = 8

def basis(k):
    return [sum(1 << i for i in c) for c in combinations(range(DIM), k)]

def wedge(x, y):
    z = {}
    for a, x0 in x.items():
        for b, y0 in y.items():
            if a & b:
                continue
            parity = sum((b & ((1 << i) - 1)).bit_count()
                         for i in range(DIM) if a >> i & 1)
            z[a | b] = z.get(a | b, 0) + (-1)**parity * x0 * y0
    return {a:S.expand(c) for a,c in z.items() if c != 0}

def mat_wedge(v, degree):
    out = basis(degree + 4)
    cols = [wedge({a:1}, v) for a in basis(degree)]
    return S.Matrix([[c.get(b,0) for c in cols] for b in out])

vol_l = {15:1}
vol_m = {240:1}
secant = {15:1,240:1}
secant_map = mat_wedge(secant,2)
mixed = [(1 << i) | (1 << j) for i in range(4) for j in range(4,8)]
assert secant_map.rank() == 12
assert len(secant_map.nullspace()) == 16
assert all(not wedge({a:1},secant) for a in mixed)

# All degree-four vectors annihilated by all mixed bivectors.
four = basis(4)
six = basis(6)
blocks=[]
for a in mixed:
    cols=[wedge({a:1},{b:1}) for b in four]
    blocks.append(S.Matrix([[c.get(o,0) for c in cols] for o in six]))
common=S.Matrix.vstack(*blocks)
ns=common.nullspace()
assert len(ns)==2
assert all(all(v[i]==0 for i,b in enumerate(four) if b not in (15,240)) for v in ns)

# A product of two symplectic two-forms, one on each four-dimensional block.
w1={3:1,12:1}
w2={48:1,192:1}
product=wedge(w1,w2)
product_map=mat_wedge(product,2)
assert product_map.rank()==18
assert len(product_map.nullspace())==10
assert mat_wedge(product,1).rank()==8

primitive=[]
for block,w in [(range(4),w1),(range(4,8),w2)]:
    b2=[sum(1 << i for i in c) for c in combinations(block,2)]
    top=sum(1 << i for i in block)
    row=S.Matrix([[wedge({a:1},w).get(top,0) for a in b2]])
    ker=row.nullspace()
    assert len(ker)==5
    prim=[{a:v[i] for i,a in enumerate(b2) if v[i]} for v in ker]
    pairing=S.Matrix([[wedge(a,b).get(top,0) for b in prim] for a in prim])
    assert pairing.rank()==5
    assert all(not wedge(a,product) for a in prim)
    primitive.extend(prim)

two=basis(2)
primitive_matrix=S.Matrix([[p.get(a,0) for p in primitive] for a in two])
assert primitive_matrix.rank()==10
product_blocks=[]
for p in primitive:
    cols=[wedge(p,{b:1}) for b in four]
    product_blocks.append(S.Matrix([[c.get(o,0) for c in cols] for o in six]))
product_common=S.Matrix.vstack(*product_blocks)
product_ann=product_common.nullspace()
assert len(product_ann)==1
pv=S.Matrix([product.get(b,0) for b in four])
assert S.Matrix.hstack(product_ann[0],pv).rank()==1

out={
    "status":"PASS",
    "coefficient_field":"rational numbers; exact SymPy integer/rational linear algebra",
    "secant_wedge_rank":12,
    "secant_kernel_dimension":16,
    "common_mixed_annihilator_dimension":2,
    "common_mixed_annihilator_support":["Lambda^4 L","Lambda^4 M"],
    "product_wedge_degree_one_rank":8,
    "product_wedge_degree_two_rank":18,
    "product_kernel_dimension":10,
    "primitive_block_dimensions":[5,5],
    "primitive_block_plucker_pairing_ranks":[5,5],
    "product_kernel_common_annihilator_dimension":1,
    "limits":"No sheaf existence or eightfold dominance is claimed by this computation."
}
path=Path(__file__).with_name('eightfold_kernel_certificate_output.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
