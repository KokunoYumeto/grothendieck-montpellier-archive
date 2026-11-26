#!/usr/bin/env python3
"""Exact finite checks accompanying Symmetric-lattice checks.

These computations verify the displayed polynomial identities. They do
not replace the ring-theoretic or representation-theoretic proofs.
Python 3, standard library only. CC0 1.0.
"""
from collections import Counter
from itertools import combinations
import json

# Split Green ring basis (1,y,x), y^2=1+x, xy=2x, x^2=3x.
one, y, x = (1, 0, 0), (0, 1, 0), (0, 0, 1)
zero = (0, 0, 0)
def add(a, b): return tuple(u+v for u,v in zip(a,b))
def neg(a): return tuple(-u for u in a)
def scale(n, a): return tuple(n*u for u in a)
def mul(a, b):
    a0, ay, ax = a; b0, by, bx = b
    return (a0*b0+ay*by, a0*by+ay*b0,
            a0*bx+ax*b0+ay*by+2*(ay*bx+ax*by)+3*ax*bx)
def power(a, n):
    r=one
    for _ in range(n): r=mul(r,a)
    return r
def convolution(a,b):
    r=[zero]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): r[i+j]=add(r[i+j],mul(u,v))
    return r
def exterior(a):
    assert min(a)>=0
    r=[one]
    for n,s in zip(a,([one,one],[one,y,one],[one,x,x,one])):
        for _ in range(n): r=convolution(r,s)
    return r
def psi3(a):
    e=exterior(a)+[zero]*3
    return add(add(power(a,3),scale(-3,mul(a,e[2]))),scale(3,e[3]))

assert psi3(x)==scale(3,one)
assert psi3(y)==add(scale(2,x),scale(-2,y))
a=add(x,scale(2,y)); e=exterior(a)
assert e[2]==add(scale(6,x),scale(3,one))
assert e[3]==e[4]==add(add(scale(10,x),scale(2,y)),one)
assert e[5]==e[2] and e[6]==a
q=add(add(add(add(mul(power(e[1],2),e[4]),scale(-2,mul(e[2],e[4]))),
                     neg(mul(e[1],e[5]))),e[6]),power(e[3],2))
lhs=exterior(e[2])[3]
assert lhs==(7,0,441) and q==(3,-4,445)
assert add(lhs,neg(q))==(4,4,-4)

# Verify the universal e_3[e_2] polynomial in six variables exactly.
N=6
def epoly(k):
    return Counter({tuple(int(i in I) for i in range(N)):1
                    for I in combinations(range(N),k)})
def pmul(a,b):
    r=Counter()
    for i,ci in a.items():
        for j,cj in b.items():r[tuple(u+v for u,v in zip(i,j))]+=ci*cj
    return r
def psum(*terms):
    r=Counter()
    for coefficient,a in terms:
        for i,ci in a.items():r[i]+=coefficient*ci
    return {i:c for i,c in r.items() if c}
E=[epoly(k) for k in range(7)]
universal=psum((1,pmul(pmul(E[1],E[1]),E[4])),(-2,pmul(E[2],E[4])),
               (-1,pmul(E[1],E[5])),(1,E[6]),(1,pmul(E[3],E[3])))
edges=list(combinations(range(N),2)); actual=Counter()
for chosen in combinations(edges,3):
    exponent=[0]*N
    for edge in chosen:
        for v in edge:exponent[v]+=1
    actual[tuple(exponent)]+=1
assert dict(actual)==universal
partition_coefficients={}
for exponent,coefficient in actual.items():
    partition=tuple(sorted((e for e in exponent if e),reverse=True))
    if partition in partition_coefficients:
        assert partition_coefficients[partition]==coefficient
    partition_coefficients[partition]=coefficient
assert partition_coefficients=={(3,1,1,1):1,(2,2,1,1):2,(2,2,2):1,
                                (2,1,1,1,1):6,(1,1,1,1,1,1):15}

# Binomial trace coefficients for sample prime characteristics.
from math import comb
trace_checks={}
for p in (2,3,5,7,11,13,17,19):
    coefficients=[sum(comb(a,j) for a in range(1,p) if a>=j)%p
                  for j in range(1,p)]
    assert coefficients==[0]*(p-2)+[1]
    trace_checks[str(p)]=coefficients

result={"status":"PASS", "arithmetic":"exact integers",
        "green_ring_basis":["1","y","x"],
        "iterate_left":lhs,"iterate_right":q,"iterate_defect":add(lhs,neg(q)),
        "universal_coefficients":{str(k):v for k,v in sorted(partition_coefficients.items())},
        "trace_checks":trace_checks,
        "scope":"Finite identities only; general proofs are in the paper."}
print(json.dumps(result,indent=2))
