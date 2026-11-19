#!/usr/bin/env python3
"""Finite certificate over (Z/9)[e]/(3e,e^3), including ring axioms.

The two-dimensional S3 representation is diag(1+e,(1+e)^2) on a
3-cycle and the swapping matrix on a transposition.  Its 3-cycle trace
is 2+e^2, outside the constant subring.  This representation is the
finite reduction of the local characteristic-zero counterexample.
"""
from itertools import product
import json
from time import perf_counter

start=perf_counter()
zero=(0,0,0); one=(1,0,0); eps=(0,1,0)
elements=list(product(range(9),range(3),range(3)))
def add(a,b): return ((a[0]+b[0])%9,(a[1]+b[1])%3,(a[2]+b[2])%3)
def mul(a,b):
    return ((a[0]*b[0])%9,(a[0]*b[1]+a[1]*b[0])%3,
            (a[0]*b[2]+a[1]*b[1]+a[2]*b[0])%3)
def matmul(a,b):
    return tuple(tuple(add(mul(a[i][0],b[0][j]),mul(a[i][1],b[1][j]))
                       for j in range(2)) for i in range(2))
identity=((one,zero),(zero,one))
def power(a,n):
    out=identity
    for _ in range(n): out=matmul(out,a)
    return out

for a,b,c in product(elements,repeat=3):
    assert add(add(a,b),c)==add(a,add(b,c))
    assert mul(mul(a,b),c)==mul(a,mul(b,c))
    assert mul(a,add(b,c))==add(mul(a,b),mul(a,c))
for a,b in product(elements,repeat=2):
    assert add(a,b)==add(b,a) and mul(a,b)==mul(b,a)
for a in elements:
    assert add(a,zero)==a and mul(a,one)==a
    assert add(a,((-a[0])%9,(-a[1])%3,(-a[2])%3))==zero

u=add(one,eps); u2=mul(u,u)
c=((u,zero),(zero,u2)); s=((zero,one),(one,zero))
assert power(c,3)==identity and power(s,2)==identity
assert matmul(matmul(s,c),s)==power(c,2)
matrices={(i,j):matmul(power(c,i),power(s,j)) for i in range(3) for j in range(2)}
assert len(set(matrices.values()))==6
for (i,j),(r,t) in product(matrices,repeat=2):
    idx=((i+(-1)**j*r)%3,(j+t)%2)
    assert matmul(matrices[i,j],matrices[r,t])==matrices[idx]
trace=add(c[0][0],c[1][1]); assert trace==(2,0,1)
assert trace not in {(i,0,0) for i in range(9)}
print(json.dumps(dict(ring='(Z/9)[epsilon]/(3epsilon,epsilon^3)',
    ring_elements=len(elements),ring_axiom_triples=len(elements)**3,
    group_order=6,group_product_pairs=36,
    epsilon=eps,character_u=u,three_cycle=c,transposition=s,
    trace_on_three_cycle=trace,trace_outside_constant_subring=True,
    runtime_seconds=round(perf_counter()-start,6)),indent=2))
