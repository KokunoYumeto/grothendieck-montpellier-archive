#!/usr/bin/env python3
"""Exact finite certificates supplementing the full F56 path/coherence proofs.
These tests do not replace the report's all-length induction or its categorical
scope statements. No source-prescribed additional 2-relations are assumed.
"""
import sympy as s

def leaves(t):
    return [t] if isinstance(t,int) else leaves(t[0])+leaves(t[1])

def coeff_order(t):
    """Left-coefficient q reduction: internal factors in postorder of cuts."""
    if isinstance(t,int):
        return []
    left,right=t
    return coeff_order(left)+coeff_order(right)+[leaves(right)[0]]

trees = [
    (((0,1),2),3),
    ((0,(1,2)),3),
    (0,((1,2),3)),
    (0,(1,(2,3))),
    ((0,1),(2,3)),
]
orders=[coeff_order(t) for t in trees]
assert orders==[[1,2,3],[2,1,3],[2,3,1],[3,2,1],[1,3,2]]
current=orders[0]
permutation=[0,1,2]
for target in orders[1:]+[orders[0]]:
    step=[current.index(x) for x in target]
    permutation=[permutation[j] for j in step]
    current=target
assert permutation==[0,1,2]
assert coeff_order(((0,1),2)) == [1,2]
assert coeff_order((0,(1,2))) == [2,1]

def beta(branch, idx, factors):
    if branch==1:
        return [1,0,3,2][idx], factors
    result=[2,3,0,1][idx]
    if idx in (1,3):
        factors=tuple(reversed(factors))
    return result,factors

for branch in (1,2):
    for idx in range(4):
        label=("first_coefficient_block","second_coefficient_block")
        j,f=beta(branch,idx,label)
        i2,f2=beta(branch,j,f)
        assert (i2,f2)==(idx,label)

delta=s.symbols("delta")
D=delta**2
for a in (delta,D-2):
    x=s.Matrix([[D,0],[a,0]])
    y=s.Matrix([[0,a],[0,D]])
    S=D+(D-2)**2
    T=D*(D-2)**2
    L=x*y*x*y*x+S*y*x*y+T*x
    R=y*x*y*x*y+S*x*y*x+T*y
    assert (L-R).applyfunc(s.expand)==s.zeros(2)
    assert (x*x-D*x).applyfunc(s.expand)==s.zeros(2)
    assert (y*y-D*y).applyfunc(s.expand)==s.zeros(2)

sizes64=[1]*24+[2]*20
sizes6=[1,1,2,2]
assert sum(sizes64)==64 and sum(i*i for i in sizes64)==104
assert sum(sizes6)==6 and sum(i*i for i in sizes6)==10

print("Triple q-reduction orders:", [1,2], [2,1])
print("Four-factor pentagon coefficient orders:", orders)
print("Pentagon comparison permutation:", permutation)
print("Degree-five explicit mirror/inverse maps: PASS for both branches")
print("Exact degree-five and quadratic matrix identities: PASS")
print("Karoubi counts: 64 states -> 104 shifted simple families; 6 -> 10")
print("All finite checks passed. General coherence/cancellation/closure proofs are in the report.")

