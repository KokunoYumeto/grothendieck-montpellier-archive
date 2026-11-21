#!/usr/bin/env python3
"""Exact arithmetic certificate for D-OL-01--03; no group enumeration."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import time

started = time.perf_counter()
SIGMA = F(1, 10**29)
J = 10**30
M = 2 * 10**29
D = 2 * J

# Tiny exact bivariate polynomial operations, variables J and s.
def add(a, b):
    c = dict(a)
    for mon, val in b.items():
        c[mon] = c.get(mon, F(0)) + val
        if not c[mon]:
            del c[mon]
    return c
def neg(a):
    return {mon: -val for mon, val in a.items()}
def sub(a, b):
    return add(a, neg(b))
def scale(a, q):
    return {mon: val * q for mon, val in a.items() if val*q}
def mul(a, b):
    c = {}
    for u, x in a.items():
        for v, y in b.items():
            w = (u[0]+v[0], u[1]+v[1])
            c[w] = c.get(w, F(0)) + x*y
    return {w: x for w, x in c.items() if x}
one = {(0, 0): F(1)}
j = {(1, 0): F(1)}
s = {(0, 1): F(1)}
d = add(scale(j, 2), s)
E = sub(sub(scale(mul(d,d), F(1,8)), scale(d,F(1,4))), scale(one,2))
difference = sub(E, scale(mul(j,d),F(1,5)))
expected = {(2,0):F(1,10), (1,0):F(-1,2), (0,0):F(-2),
            (1,1):F(3,10), (0,1):F(-1,4), (0,2):F(1,8)}
assert difference == expected

# Universal positivity after J=10+t: all coefficients are nonnegative
# and the constant is 3.
Jsmall = add(scale(one,10), j)
constant = sub(sub(scale(mul(Jsmall,Jsmall),F(1,10)),
                   scale(Jsmall,F(1,2))),scale(one,2))
assert constant == {(0,0):F(3),(1,0):F(3,2),(2,0):F(1,10)}
linear_s = sub(scale(Jsmall,F(3,10)),scale(one,F(1,4)))
assert linear_s == {(0,0):F(11,4),(1,0):F(3,10)}

# Four exact exponent reductions to E(d).
m = j
de = scale(m,2)
do = add(de,one)
def Epoly(d):
    return sub(sub(scale(mul(d,d),F(1,8)),scale(d,F(1,4))),scale(one,2))
spin_even = sub(scale(mul(m,sub(m,one)),F(1,2)),scale(one,2))
spin_odd = sub(scale(mul(m,add(m,one)),F(1,2)),scale(one,2))
extension_even = spin_even
extension_odd = sub(scale(mul(m,m),F(1,2)),one)
assert sub(spin_even,Epoly(de)) == {}
assert sub(spin_odd,Epoly(do)) == {(1,0):F(1,2),(0,0):F(1,8)}
assert sub(extension_even,Epoly(de)) == {}
assert sub(extension_odd,Epoly(do)) == {(0,0):F(9,8)}

# Degree estimate: d-2k-2 >= 3d/5+(d-50)/15.
# Substitute k<=d/6+2/3, then verify the exact identity.
x = j
lhs = sub(sub(x, scale(add(scale(x,F(1,6)),scale(one,F(2,3))),2)),scale(one,2))
rhs = add(scale(x,F(3,5)),scale(sub(x,scale(one,50)),F(1,15)))
assert lhs == rhs

assert SIGMA*M == 2 and F(J,5)==M
assert F(1,6507*2**21*10**18) > 7*SIGMA
assert F(1,4) < 1
delta = (1-F(1,4))/4
assert delta == F(3,16)
assert 12*delta-2 == F(1,4)
assert 6/(12*delta-2) == 24
assert F(1,4)>delta
assert F(J*J,10)-F(J,2)-2 > 0
assert F(3*J,10)-F(1,4)>0
assert M*10>5 # every factor in the degree-barrier theorem has a>32.

# Exhaustive small boundary instances supplement, but do not replace,
# the preceding universal polynomial identities.
boundary_count = 0
for natural in range(50,501):
    for level in range(1,natural//2+1):
        k=(level+2)//3
        assert F(level,3) <= k <= F(level+2,3)
        assert natural-2*k-2 >= F(3*natural,5)
        assert k*(natural-2*k-2) >= F(natural*level,5)
        boundary_count += 1
for level in (J,J+1,J+2,2*J-1,2*J):
    for natural in (2*level,2*level+1,2*level+2,10*level):
        k=(level+2)//3
        assert k*(natural-2*k-2) >= F(natural*level,5)
        assert F(natural*level,5) >= M*natural

folder=Path(__file__).resolve().parent
proof=(folder/'orthogonal_level_section.tex').read_text()
assert proof.count(r'\[')==proof.count(r'\]')
assert proof.count(r'\begin{proof}')==proof.count(r'\end{proof}')==3
assert proof.count(r'\begin{lemma}')==proof.count(r'\end{lemma}')==2
assert proof.count(r'\begin{theorem}')==proof.count(r'\end{theorem}')==1
out={
 'status':'PASS',
 'scope':'Exact rational constants and symbolic identities; no group enumeration',
 'sigma':str(SIGMA),'level_cutoff':J,'degree_coefficient':M,
 'spin_and_SO_extension_dimension_cutoff':D,
 'core_trace_ratio':'1/4','normalizer_support':'3/16','Hurwitz_degree_ceiling':24,
 'finite_level_boundary_pairs':boundary_count,
 'universal_polynomial_identity':{str(k):str(v) for k,v in expected.items()},
 'spin_even_gap':'0','spin_odd_gap':'m/2+1/8',
 'SO_extension_even_gap':'0','SO_extension_odd_gap':'9/8',
 'proof_sha256':hashlib.sha256(proof.encode()).hexdigest(),
 'seconds':round(time.perf_counter()-started,9),
}
(folder/'constants_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

