#!/usr/bin/env python3
"""Finite geometric seed for the proper-completion cusp counterexample.

The infinite inverse-limit element is constructed in the accompanying proof.
This program verifies its actual A5 cover and the explicit integral fixed class.
"""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from time import perf_counter
import json
import numpy as np
import sympy as sp

started = perf_counter()
source = Path(__file__).with_name('build_A5_boundary_nilpotent.json')
if not source.exists():
    source = Path(__file__).resolve().parent.parent / 'build_A5_boundary_nilpotent.json'
raw = source.read_bytes()
assert sha256(raw).hexdigest() == 'ba0e10ed1fc1eb306fafdfbb2e77fe3ed38f17f5ba0f5593188f59203872b111'
data = json.loads(raw)
group = [tuple(h) for h in data['group']]
one = tuple(range(5))
x, y = tuple(data['x']), tuple(data['y'])

def mul(a, b):
    return tuple(a[b[i]] for i in range(5))

def inv(a):
    return tuple(a.index(i) for i in range(5))

def cyclic(a):
    out, h = [], one
    while h not in out:
        out.append(h)
        h = mul(h, a)
    assert h == one
    return set(out)

def cosets(I):
    remaining, out = set(group), []
    while remaining:
        g = min(remaining)
        c = frozenset(mul(g, i) for i in I)
        out.append(c)
        remaining -= c
    return out

def dot(A, B):
    bound = int(np.max(np.abs(A))) * int(np.max(np.abs(B))) * A.shape[1]
    assert bound < 2**63, bound
    return A @ B

assert len(group) == len(set(group)) == 60
assert all(mul(g, h) in set(group) for g in group for h in group)
generated, todo = {one}, [one]
while todo:
    g = todo.pop()
    for a in (x, y, inv(x), inv(y)):
        h = mul(g, a)
        if h not in generated:
            generated.add(h)
            todo.append(h)
assert generated == set(group)
z = inv(mul(x, y))
orders = [len(cyclic(a)) for a in (x, y, z)]
assert orders == [3, 5, 5]
H = cyclic(y)
normalizer = [g for g in group if {mul(mul(g,h),inv(g)) for h in H} == H]
assert len(normalizer) == 10
branch_cosets = [cosets(cyclic(a)) for a in (x, y, z)]
assert list(map(len, branch_cosets)) == [20, 12, 12]
fixed_by_h = []
for h in sorted(H - {one}):
    counts = [sum(frozenset(mul(h,g) for g in c) == c for c in cs)
              for cs in branch_cosets]
    assert counts == [0, 2, 2]
    fixed_by_h.append(counts)
two_g_minus_two = 60 * (-2 + sum(1-Fraction(1,d) for d in orders))
assert two_g_minus_two == 16
ramification = sum(map(sum, fixed_by_h))
assert ramification == 16
quotient_two_g_minus_two = (two_g_minus_two - ramification) / 5
assert quotient_two_g_minus_two == 0

Y = np.array(data['action_y'], dtype=np.int64)
E = np.array(data['E'], dtype=np.int64)
B = np.array(data['boundary_matrix'], dtype=np.int64)
I = np.eye(61, dtype=np.int64)
Q = 60*I-E
assert np.array_equal(dot(E,E), 60*E)
assert not np.any(dot(Q,B))
power, norm = I.copy(), np.zeros_like(I)
for j in range(5):
    norm += power
    power = dot(power,Y)
assert np.array_equal(power,I)
R = dot(norm,Q)
assert sp.Matrix(R.tolist()).rank() == 2
column = next(j for j in range(61) if np.any(R[:,j]))
assert column == 1
w = R[:,[column]]
q = Q[[0],:]
assert np.array_equal(dot(Y,w),w)
assert not np.any(dot(E,w))
assert not np.any(dot(q,B))
assert int(w[0,0]) == 9
assert int(dot(q,w)[0,0]) == 540
expected_w = [9,9,9,1,-12,1,1,9,9,1,18,-21,0,1,-12,1,-12,1,1,1,-12,1,-12,1,-21,1,-12,1,18,-21,9,0,1,-21,18,9,9,-12,1,1,1,18,1,-12,1,18,9,9,0,1,-12,-21,18,9,-12,1,-12,-21,18,9,0]
assert w[:,0].tolist() == expected_w

print('FROZEN_INPUT_SHA256', sha256(raw).hexdigest())
print('A5_GENERATED_ORDER',len(group),'INERTIA_ORDERS',orders,'CUSP_COUNTS',[20,12,12])
print('NORMALIZER_C5_ORDER',len(normalizer),'NONIDENTITY_FIXED_COUNTS',fixed_by_h)
print('COMPACT_GENUS',9,'CYCLIC_QUOTIENT_GENUS',1)
print('FIXED_PROPER_IMAGE_RANK',2,'FIRST_COLUMN',column,'FIRST_ENTRY',9)
print('Yw=w; Ew=0; qB=0; qw=540')
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'))
