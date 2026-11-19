#!/usr/bin/env python3
"""Necessary finite graph congruences for the correlated type-(1,2) cone.

This is an exploratory test, not a geometric obstruction or a sufficiency
theorem. The exact block forms and all tested linear systems are retained.
"""
from itertools import product
from pathlib import Path
from time import perf_counter
from datetime import datetime, timezone
import json
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

START = perf_counter()
L = sp.Matrix([[1,0,1,0], [1,0,0,0],
               [0,1,0,1], [0,0,0,1],
               [2,1,1,1], [0,0,1,1]])
R = sp.Matrix([[-1,-1,-1,0,1,0],[-1,1,0,-1,0,1]])
assert R*L == sp.zeros(2,4)
assert abs(L[:4,:].det()) == 1
forms = [(L[2*s:2*s+2,:].T*L[2*s:2*s+2,:]) for s in range(3)]

def test_odd_level(modulus):
    tic=perf_counter()
    verts=list(product(range(modulus), repeat=2))
    vid={v:i for i,v in enumerate(verts)}
    edges=[]
    labels=[v for v in product(range(modulus), repeat=2) if any(v)]
    for s in range(3):
        Rs=R[:,2*s:2*s+2]
        for u in verts:
            for lab in labels:
                step=Rs*sp.Matrix(lab)
                v=tuple((u[i]+int(step[i]))%modulus for i in range(2))
                rev=tuple((-x)%modulus for x in lab)
                if (u,lab) > (v,rev):
                    continue
                edges.append((s,u,v,lab))
    # Conservation of the embedding L^t p at every vertex, and the three
    # two-dimensional Gram matrices equal to the identity (odd level).
    nr=4*len(verts)+9
    A=sp.zeros(nr,len(edges))
    rhs=sp.zeros(nr,1)
    for s in range(3):
        rhs[4*len(verts)+3*s]=1
        rhs[4*len(verts)+3*s+2]=1
    for j,(s,u,v,lab) in enumerate(edges):
        q=L[2*s:2*s+2,:].T*sp.Matrix(lab)
        for i in range(4):
            A[4*vid[u]+i,j]-=int(q[i])
            A[4*vid[v]+i,j]+=int(q[i])
        a,b=lab
        base=4*len(verts)+3*s
        A[base,j]=a*a
        A[base+1,j]=a*b
        A[base+2,j]=b*b
    A=A.applyfunc(lambda x:int(x)%modulus)
    # A x = rhs (mod m) iff rhs is in the integral column lattice of [A,mI].
    H=hermite_normal_form(A.row_join(modulus*sp.eye(nr)),D=modulus**nr)
    sol=H.inv()*rhs
    feasible=all(x.q==1 for x in sol)
    cert=None
    if not feasible:
        ii=next(i for i,x in enumerate(sol) if x.q!=1)
        invrow=H.inv()[ii,:]
        w=[int(modulus*x)%modulus for x in invrow]
        assert all(x.q==1 for x in modulus*invrow)
        assert all(int(x)%modulus==0 for x in sp.Matrix([w])*A)
        obstruction=int((sp.Matrix([w])*rhs)[0])%modulus
        assert obstruction
        cert={"dual_weights":w,"rhs_pairing_modulus":obstruction,
              "vertex_weights":[[list(v),w[4*vid[v]:4*vid[v]+4]] for v in verts],
              "gram_weights":[w[4*len(verts)+3*s:4*len(verts)+3*s+3] for s in range(3)],
              "all_columns_pair_to_zero":True}
    return {"modulus":modulus,"level":"odd, normalized to 1",
            "vertices":len(verts),"edges":len(edges),"equations":nr,
            "congruences_feasible":feasible,
            "dual_infeasibility_certificate":cert,
            "cokernel_invariant_diagonal":[int(H[i,i]) for i in range(nr)],
            "runtime_seconds":perf_counter()-tic}

out={"started_utc":datetime.now(timezone.utc).isoformat(),
     "scope":"Necessary finite graph congruences only; no geometric conclusion",
     "L":L.tolist(),"R":R.tolist(),"forms":[Q.tolist() for Q in forms],
     "tests":[test_odd_level(2),test_odd_level(4)]}
out["runtime_seconds"]=perf_counter()-START
path=Path(__file__).resolve().parents[1]/"output"/"check_correlated_monodromy.json"
path.write_text(json.dumps(out,indent=2,default=int)+"\n")
print(json.dumps(out,indent=2,default=int))
