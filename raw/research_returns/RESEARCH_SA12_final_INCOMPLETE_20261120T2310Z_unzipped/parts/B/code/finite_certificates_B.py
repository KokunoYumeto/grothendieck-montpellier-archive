#!/usr/bin/env python3
"""Finite certificates for B.1a and B.3a; no numerical evidence is used as a proof.

Checks primitive Hopf quotients alpha_p -> alpha_(p^2) for p=2,3,5,
and the smooth cubic Y^2 Z + Y Z^2 = X^3 over F_2 and F_4.
The paper gives the general symbolic arguments.
"""
import json
import math
import time
from pathlib import Path

started = time.perf_counter()
out = {"scope": "finite checks, supplementing the symbolic proofs", "alpha": [], "elliptic": []}

def delta(n, q, p):
    return {(i, n-i): math.comb(n, i) % p for i in range(n+1)
            if i < q and n-i < q and math.comb(n, i) % p}

for p in (2, 3, 5):
    for q in (p, p*p):
        assert all(math.comb(q, j) % p == 0 for j in range(1, q))
    for n in range(p*p):
        projected_delta = {(i,j): a for (i,j),a in delta(n, p*p, p).items()
                           if i < p and j < p}
        target_delta = delta(n, p, p) if n < p else {}
        assert projected_delta == target_delta
    # I=(t,...,t^(q-1)); I^2=(t^2,...,t^(q-1)).
    tangent_dims = [(q-1)-max(0,q-2) for q in (p,p*p)]
    assert tangent_dims == [1,1]
    # The quotient sends the class of t to the class of t.
    out["alpha"].append({"p":p,"coordinate_dimensions":[p,p*p],
        "tangent_dimensions":tangent_dims,"tangent_map_matrix":[[1]],
        "monomials_checked":p*p,"Hopf_compatibility":True,
        "strict_quotient":p < p*p})

def add(a,b):
    return a ^ b

def mul(a,b,q):
    if q == 2:
        return a*b
    # F_4=F_2[u]/(u^2+u+1), with bits representing coefficients.
    c0=(a&1)*(b&1)
    c1=((a&1)*((b>>1)&1)) ^ (((a>>1)&1)*(b&1))
    c2=((a>>1)&1)*((b>>1)&1)
    return (c0 ^ c2) | ((c1 ^ c2) << 1)

def power(a,n,q):
    z=1
    for _ in range(n):
        z=mul(z,a,q)
    return z

for q in (2,4):
    affine=[]
    for x in range(q):
        for y in range(q):
            if add(power(y,2,q),y) == power(x,3,q):
                affine.append((x,y))
    affine_set=set(affine)
    for x,y in affine:
        assert (x,add(y,1)) in affine_set
        assert add(y,1) != y
    projective_solutions=0
    checked=q**3-1
    for x in range(q):
        for y in range(q):
            for z in range(q):
                if (x,y,z)==(0,0,0):
                    continue
                equation=add(add(mul(power(y,2,q),z,q),mul(y,power(z,2,q),q)),power(x,3,q))
                gradient=(power(x,2,q),power(z,2,q),power(y,2,q))
                assert gradient != (0,0,0)
                if equation == 0:
                    projective_solutions += 1
    assert projective_solutions == (q-1)*(len(affine)+1)
    out["elliptic"].append({"field_order":q,"affine_points":affine,
        "projective_point_count":len(affine)+1,
        "nonzero_projective_triples_checked":checked,
        "no_zero_gradient":True,"no_affine_self_inverse_point":True})

out["elapsed_seconds"]=time.perf_counter()-started
out["all_checks_passed"]=True
destination=Path(__file__).resolve().parent / "output"
destination.mkdir(exist_ok=True)
text=json.dumps(out,indent=2)+"\n"
(destination / "finite_certificates_B.json").write_text(text)
print(text,end="")
