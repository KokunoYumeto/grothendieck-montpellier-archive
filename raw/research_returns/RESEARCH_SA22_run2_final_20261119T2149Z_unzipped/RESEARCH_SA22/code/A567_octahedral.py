#!/usr/bin/env python3
"""Exhaustive certificate in PGL_2(F_5); Python standard library only."""
from itertools import product, combinations
from time import perf_counter
import json
start=perf_counter()
p=5
points=list(range(p))+[None]
def normalize(a):
    c=next(x for x in a if x%p)
    s=pow(c,-1,p)
    return tuple(x*s%p for x in a)
def multiply(A,B):
    a,b,c,d=A; e,f,g,h=B
    return normalize((a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h))
def act(A,z):
    a,b,c,d=A
    if z is None: return None if c==0 else a*pow(c,-1,p)%p
    n=(a*z+b)%p; q=(c*z+d)%p
    return None if q==0 else n*pow(q,-1,p)%p
G=sorted({normalize(A) for A in product(range(p),repeat=4) if (A[0]*A[3]-A[1]*A[2])%p})
I=normalize((1,0,0,1))
inv={A:next(B for B in G if multiply(A,B)==I) for A in G}
fixed={A:frozenset(z for z in points if act(A,z)==z) for A in G}
invol=[A for A in G if A!=I and multiply(A,A)==I]
kleins=set()
for A,B in combinations(invol,2):
    if multiply(A,B)==multiply(B,A):
        V=frozenset([I,A,B,multiply(A,B)])
        if len(V)==4: kleins.add(V)
full=[V for V in kleins if frozenset().union(*(fixed[A] for A in V if A!=I))==frozenset(points)]
normals=[]
for V in full:
    N=[A for A in G if frozenset(multiply(multiply(A,B),inv[A]) for B in V)==V]
    normals.append(N)
assert len(G)==120
assert len(full)==5
assert [len(N) for N in normals]==[24]*5
assert all(len(fixed[A])==2 for V in full for A in V if A!=I)
assert len({frozenset(N) for N in normals})==5
cert={"field":"F5","P1_points":["infinity" if z is None else z for z in points],
"PGL2_order":len(G),"involutions":len(invol),"klein_groups_total":len(kleins),
"klein_groups_with_octahedral_ramification":len(full),"normalizer_orders":[len(N) for N in normals],
"five_Klein_groups":[[list(A) for A in sorted(V)] for V in sorted(full,key=lambda V:sorted(V))],
"seconds":perf_counter()-start}
print(json.dumps(cert,indent=2))
