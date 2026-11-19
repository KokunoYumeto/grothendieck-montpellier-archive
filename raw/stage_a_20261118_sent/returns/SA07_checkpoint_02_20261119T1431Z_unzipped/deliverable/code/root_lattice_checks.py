"""Exact finite root-lattice checks for B15-01, scan 171.

The opening of the E6 exercise is missing; identifying its root system as E6
is this run's reconstruction. All arithmetic below is integral or modulo p.
Group orders are computed by SymPy's exact permutation-group algorithm.
"""
import json
from collections import deque
from itertools import product
import sympy as s
from sympy.combinatorics import Permutation, PermutationGroup

def root_data(arms, prime):
    n=1+sum(arms)
    C=s.eye(n)*2
    nxt=1
    for length in arms:
        prev=0
        for j in range(length):
            C[prev,nxt]=C[nxt,prev]=-1
            prev=nxt;nxt+=1
    def reflect(v,i):
        w=list(v)
        w[i]-=sum(int(C[i,j])*v[j] for j in range(n))
        return tuple(w)
    basis=[tuple(int(i==j) for j in range(n)) for i in range(n)]
    roots=set(basis); todo=deque(basis)
    while todo:
        r=todo.popleft()
        for i in range(n):
            v=reflect(r,i)
            if v not in roots: roots.add(v);todo.append(v)
    roots=sorted(roots); lookup={r:i for i,r in enumerate(roots)}
    perms=[Permutation([lookup[reflect(r,i)] for r in roots]) for i in range(n)]
    W=PermutationGroup(perms)
    minus=Permutation([lookup[tuple(-x for x in r)] for r in roots])
    radical=[v for v in product(range(prime),repeat=n)
             if all(sum(int(C[i,j])*v[j] for j in range(n))%prime==0 for i in range(n))]
    assert len(radical)==prime
    def coset(v):
        return min(tuple((v[j]+r[j])%prime for j in range(n)) for r in radical)
    image=sorted(set(map(coset,roots)))
    imlookup={r:i for i,r in enumerate(image)}
    representative={coset(r):r for r in roots}
    quotient=PermutationGroup([Permutation([imlookup[coset(reflect(representative[r],i))]
        for r in image]) for i in range(n)])
    def quadratic(v):
        return int((s.Matrix(v).T*C*s.Matrix(v))[0]//2)%prime
    sphere=None
    if prime==3:
        # q descends because the bilinear radical is also q-isotropic in odd characteristic.
        universe={coset(v) for v in product(range(prime),repeat=n)}
        sphere={v for v in universe if quadratic(v)==1}
        assert sphere==set(image)
    result={"rank":n,"Cartan_matrix":list(map(list,C.tolist())),"determinant":int(C.det()),
        "root_count":len(roots),"quotient_characteristic":prime,
        "radical_mod_p":[list(v) for v in radical],"root_images":len(image),
        "W_order_on_roots":int(W.order()),"W_image_order_on_quotient":int(quotient.order()),
        "kernel_size":int(W.order()//quotient.order()),"minus_identity_in_W":bool(W.contains(minus)),
        "group_generated_with_minus_identity":int(PermutationGroup(perms+[minus]).order())}
    if sphere is not None: result["norm_one_vectors_in_quotient"]=len(sphere)
    return result

E6=root_data([2,2,1],3)
E7=root_data([3,2,1],2)
assert E6["root_count"]==72 and E6["W_order_on_roots"]==51840
assert E6["W_image_order_on_quotient"]==51840 and not E6["minus_identity_in_W"]
assert E7["root_count"]==126 and E7["W_order_on_roots"]==2903040
assert E7["W_image_order_on_quotient"]==1451520 and E7["kernel_size"]==2
print(json.dumps({"E6_reconstruction":E6,"E7":E7},indent=2,default=int))
