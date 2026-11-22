#!/usr/bin/env python3
"""Exact supplements to D-OL12--13; the universal proof is in the TeX."""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
from collections import Counter
import datetime
import hashlib
import json
import time
import re
import sympy as sp

started = time.perf_counter()
base = Path(__file__).resolve().parent
proof = base/'orthogonal_odd_nonselfdual_section.tex'
text = proof.read_text()
assert text.count(r'\[') == text.count(r'\]')
assert not [ord(c) for c in text if ord(c)<32 and c not in '\n\t\r']
tags = re.findall(r'\\tag\{([^}]+)\}', text)
assert tags == ['OO.'+str(j) for j in range(1, 16)]

# Exact universal endpoint arithmetic. Monotonicity in q and N is proved
# in the text; the endpoint checks use integers, not decimal evaluation.
fixed_bound = (F(1, 5)+F(1, 5**9))/(1-F(1, 5**9)-F(1, 5**19))
assert fixed_bound < F(1, 4)
delta = (1-F(19, 20)**9)/2
assert F(1, 6) < delta < F(3, 16) < F(1, 4)
ceiling = 6/(12*delta-2)
assert 27 < ceiling < 28
assert F(1135-2, 2) == F(1133, 2)
assert (1135-1)//2 == 567 == 7*9**2
assert 1135-2 > 567
field_fixed = F(1, 2**18)/(1-F(1, 4**9)-F(1, 4**19))
assert field_fixed < F(1, 4)
assert F(1, 2)*F(3, 4)*F(1, 2) == F(3, 16)

# An exact signed-pair witness over Z, valid after reduction to every odd
# characteristic. Natural dimension9 has four hyperbolic planes and a
# norm-one line. Minus reflection in that line is in Omega: it is the
# product of eight reflections, with determinant and spinor norm one.
n = 9
I = sp.eye(n)
B = sp.zeros(n)
pairs = [(0, 8), (1, 2), (3, 4), (5, 6)]
for i, j in pairs:
    B[i, j] = B[j, i] = 1
B[7, 7] = 2
g = -sp.eye(n)
g[7, 7] = 1
assert g.T*B*g == B and g*g == I and g.det() == 1
product_reflections = I
norm_product = 1
for i, j in pairs:
    for sign in (1, -1):
        v = sp.zeros(n, 1)
        v[i], v[j] = 1, sign
        norm = (v.T*B*v)[0]/2
        R = I - v*(v.T*B)/norm
        assert R.T*B*R == B and R*R == I and R.det() == -1
        product_reflections = product_reflections*R
        norm_product *= norm
assert product_reflections == g and norm_product == 1

BW = B[1:8, 1:8]
gw = g[1:8, 1:8]
A = -gw
assert (A-sp.eye(7)).rank() == 1
v = sp.Matrix(sp.symbols('v0:7'))
def line_radical(w):
    u = sp.eye(9)
    u[0, 1:8] = -w.T*BW
    u[1:8, 8] = w
    u[0, 8] = -(w.T*BW*w)[0]/2
    return u
U = line_radical(v)
assert (U.T*B*U-B).applyfunc(sp.expand) == sp.zeros(9)
assert (g*U*g-line_radical(A*v)).applyfunc(sp.expand) == sp.zeros(9)

# Complete small norm-level counts independently verify the displayed
# rank-one example. The universal count is the elementary hyperbolic-plane
# recurrence in the proof, not an inference from these examples.
counts = []
vectors_checked = 0
for q in (3, 5, 7, 11, 13):
    for s in (1, 2, 3):
        N = 2*s+1
        if q**N > 100000:
            continue
        total, fixed = Counter(), Counter()
        for w in product(range(q), repeat=N):
            if not any(w):
                continue
            t = (sum(w[2*j]*w[2*j+1] for j in range(s))+w[-1]**2) % q
            total[t] += 1
            if w[-1] == 0:
                fixed[t] += 1
        vectors_checked += q**N
        for t in range(q):
            if t == 0:
                expect_total = q**(2*s)-1
                expect_fixed = q**(2*s-1)+(q-1)*q**(s-1)-1
            else:
                chi = 1 if pow(t, (q-1)//2, q) == 1 else -1
                expect_total = q**(2*s)+chi*q**s
                expect_fixed = q**(2*s-1)-q**(s-1)
            assert total[t] == expect_total and fixed[t] == expect_fixed
        counts.append({'q':q, 'W_dimension':N,
                       'vectors_including_zero':q**N,
                       'singular_total':total[0], 'singular_fixed':fixed[0],
                       'singular_fraction':str(F(fixed[0],total[0]))})

# This proposed q3 rank-one fixed-fraction strengthening is explicitly
# false. Here N23,d25, so the witness is already in the radical range.
q, s = 3, 11
q3_fraction = F(q**(2*s-1)+(q-1)*q**(s-1)-1, q**(2*s)-1)
assert q3_fraction > F(1, 3) > F(1, 4)
assert 2*s+3 == 25 and (25-1)//2 % 2 == 0

# Exact algebraic identities underlying the monotonic exponent bounds.
k, ell = sp.symbols('k ell', integer=True, positive=True)
assert sp.expand((2*k+1)-1-k) == k
NN = sp.Symbol('NN', integer=True)
assert sp.expand((NN-20)*(ell-1)+19*(ell-2)
                 -(-18-(ell-NN*(ell-1)))) == 0

out = {
    'status':'PASS',
    'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
    'runtime_seconds':time.perf_counter()-started,
    'rank_one_uniform_fixed_fraction_upper_bound':str(fixed_bound),
    'uniform_projective_support':str(delta),
    'exact_source_degree_ceiling':str(ceiling),
    'natural_dimension_threshold':1135,
    'spin_restricted_support_threshold':567,
    'signed_hyperbolic_pair_witness':{
        'natural_dimension':9,'reflection_count':8,
        'determinant':1,'spinor_norm_representative':1,
        'weight_action_moving_rank':1,
        'symbolic_radical_conjugation':'PASS'},
    'complete_norm_level_counts':counts,
    'vectors_checked_including_zero':vectors_checked,
    'q3_tested_false_strengthening':{
        'natural_dimension':25,'W_dimension':23,
        'singular_fixed_fraction':str(q3_fraction),
        'proposed_bound':'1/4','outcome':'REFUTED: actual fraction exceeds 1/3'},
    'scope':'Exact arithmetic, symbolic identities and finite witnesses. Universal representation and source proofs are written separately.',
    'failures_before_pass':[]
}
(base/'orthogonal_odd_nonselfdual_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
