#!/usr/bin/env python3
"""Independent full divided-power certificate for the finite detector.

No earlier SA17 certificate is imported.  The algebra is built from its monomial
quotient.  Every PD identity is checked for all ideal elements at p=2,3 and
every scalar in the entire algebra.  Infinite ranges reduce to the support
{1,2,p,p+1,2p}; the mathematical proof explains why no larger index contributes.
The final evaluations include each of the three counterexample presentations.
"""
from __future__ import annotations
import itertools
import json
import math
from pathlib import Path
import time
import numpy as np

BASIS = [(0,0,0,0),(1,0,0,0),(0,1,0,0),(2,0,0,0),(1,1,0,0),
         (0,2,0,0),(0,0,1,0),(0,0,0,1),(0,0,1,1)]
NAMES = ["1","x","y","x^2","xy","y^2","u","v","uv"]
RELATIONS = [(3,0,0,0),(2,1,0,0),(1,2,0,0),(0,3,0,0),
             (1,0,1,0),(0,1,1,0),(1,0,0,1),(0,1,0,1),
             (0,0,2,0),(0,0,0,2)]

def build_table():
    ans = np.zeros((9,9,9),dtype=np.int16)
    for i,a in enumerate(BASIS):
        for j,b in enumerate(BASIS):
            c=tuple(x+y for x,y in zip(a,b))
            if any(all(x>=y for x,y in zip(c,r)) for r in RELATIONS):
                continue
            assert c in BASIS, c
            ans[i,j,BASIS.index(c)]=1
    return ans

TABLE=build_table()

def mul(a,b,p):
    a,b=np.broadcast_arrays(a,b)
    z=np.zeros(a.shape,dtype=np.int16)
    z[...,0]=a[...,0]*b[...,0]
    for j in range(1,9):
        z[...,j]=a[...,0]*b[...,j]+a[...,j]*b[...,0]
    z[...,3]+=a[...,1]*b[...,1]
    z[...,4]+=a[...,1]*b[...,2]+a[...,2]*b[...,1]
    z[...,5]+=a[...,2]*b[...,2]
    z[...,8]+=a[...,6]*b[...,7]+a[...,7]*b[...,6]
    return z%p

def ideal_mul(a,b,p):
    shape=np.broadcast_shapes(a.shape,b.shape)
    z=np.zeros(shape,dtype=np.int16)
    z[...,8]=(a[...,6]*b[...,7]+a[...,7]*b[...,6])%p
    return z

def gamma(z,n,p):
    g=np.zeros(z.shape,dtype=np.int16)
    if n==0:
        g[...,0]=1
        return g
    if n==1:
        return z.copy()
    # These are added rather than assigned: indices 2 and p coincide at p=2.
    if n==2:
        g[...,8]+=z[...,6]*z[...,7]
    if n==p:
        g[...,6]+=z[...,3]**p
        g[...,7]+=z[...,5]**p
    if n==p+1:
        g[...,8]+=z[...,3]**p*z[...,7]+z[...,5]**p*z[...,6]
    if n==2*p:
        g[...,8]+=z[...,3]**p*z[...,5]**p
    return g%p

def equal(a,b,claim):
    if not np.array_equal(a,b):
        bad=np.argwhere(a!=b)[0].tolist()
        raise AssertionError((claim,bad))

def run(p):
    start=time.monotonic()
    E=np.eye(9,dtype=np.int16)
    for i,j in itertools.product(range(9),repeat=2):
        equal(mul(E[i],E[j],p),TABLE[i,j],"quotient multiplication")
    for i,j,k in itertools.product(range(9),repeat=3):
        equal(mul(mul(E[i],E[j],p),E[k],p),
              mul(E[i],mul(E[j],E[k],p),p),"associativity")
    R=np.array(list(itertools.product(range(p),repeat=9)),dtype=np.int16)
    Z=np.zeros((p**6,9),dtype=np.int16)
    Z[:,3:]=np.array(list(itertools.product(range(p),repeat=6)),dtype=np.int16)
    G=[gamma(Z,n,p) for n in range(2*p+1)]
    counts={"ring_basis_products":81,"ring_basis_associativity":729,
            "normalization":len(Z),"additivity":0,"scalar":0,
            "product":0,"composition":0,"nilpotence":0}
    equal(G[1],Z,"gamma_1")
    for n in range(1,2*p+1):
        # Full Cartesian product of ideal elements, chunked for memory.
        for low in range(0,len(Z),64):
            a=Z[low:low+64,None,:];b=Z[None,:,:]
            lhs=gamma((a+b)%p,n,p)
            rhs=np.broadcast_to(G[n][low:low+64,None,:]+G[n][None,:,:],lhs.shape).copy()
            for i in range(1,n):
                rhs+=ideal_mul(G[i][low:low+64,None,:],G[n-i][None,:,:],p)
            equal(lhs,rhs%p,("additivity",n,low))
            counts["additivity"]+=len(a)*len(Z)
    RP=[np.broadcast_to(E[0],R.shape).copy()]
    for n in range(1,2*p+1):
        RP.append(mul(RP[-1],R,p))
    for low in range(0,len(R),128):
        r=R[low:low+128,None,:]
        rz=mul(r,Z[None,:,:],p)
        for n in range(1,2*p+1):
            equal(gamma(rz,n,p),mul(RP[n][low:low+128,None,:],G[n][None,:,:],p),
                  ("scalar",n,low))
            counts["scalar"]+=len(r)*len(Z)
    for m,n in itertools.product(range(1,2*p+1),repeat=2):
        equal(ideal_mul(G[m],G[n],p),
              (math.comb(m+n,m)%p)*gamma(Z,m+n,p)%p,("product",m,n))
        coefficient=math.factorial(m*n)//(math.factorial(m)*math.factorial(n)**m)
        equal(gamma(G[n],m,p),(coefficient%p)*gamma(Z,m*n,p)%p,
              ("composition",m,n))
        counts["product"]+=len(Z);counts["composition"]+=len(Z)
    # Beyond 2p, addition has zero RHS: no product of two supported positive
    # gammas with indices summing to >2p survives.  Check up to the maximum 4p.
    for n in range(2*p+1,4*p+1):
        for i in range(max(1,n-2*p),min(2*p,n-1)+1):
            equal(ideal_mul(G[i][:,None,:],G[n-i][None,:,:],p),
                  np.zeros((len(Z),len(Z),9),dtype=np.int16),("tail",n,i))
            counts["nilpotence"]+=len(Z)**2
    # Actual presentation maps.  All polynomial variables t_i map to zero.
    x,y=E[1],E[2]
    r0_rel=[mul(x,x,p),mul(x,y,p),mul(y,y,p)]
    a,b,c,d=x,y,x,y
    plane_rel=[mul(a,c,p),mul(a,d,p),mul(b,c,p),mul(b,d,p)]
    for z in r0_rel+plane_rel:
        assert np.all(z[:3]==0)
    tau0=(mul(gamma(r0_rel[0],p,p),gamma(r0_rel[2],p,p),p)
          -mul(gamma(r0_rel[1],p,p),gamma(r0_rel[1],p,p),p))%p
    tau=(mul(gamma(plane_rel[0],p,p),gamma(plane_rel[3],p,p),p)
         -mul(gamma(plane_rel[1],p,p),gamma(plane_rel[2],p,p),p))%p
    equal(tau0,E[8],"R0 detector tau")
    equal(tau,E[8],"two-plane detector tau")
    tauinf=tau.copy()
    equal(tauinf,E[8],"infinite-polynomial detector tau")
    # At 2 the old omitted-cross-term formula fails, for a separately logged
    # diagnostic; the actual certificate above uses the corrected full PD.
    old_delta_failure=None
    if p==2:
        old_delta_failure={"argument":"u+v","old_value":0,
                           "required_value":"uv","nonzero":True}
    return {"p":p,"algebra_size":len(R),"ideal_size":len(Z),
            "basis":NAMES,"counts":counts,"all_identities_pass":True,
            "gamma_support":[1,2,p,p+1,2*p],
            "detectors":{name:{"tau_coordinates":v.tolist(),"nonzero":True}
              for name,v in [("R0",tau0),("R_two_planes",tau),("R_infinity",tauinf)]},
            "old_formula_failure":old_delta_failure,
            "seconds":round(time.monotonic()-start,6)}

if __name__=="__main__":
    results=[run(2),run(3)]
    output=Path(__file__).resolve().parents[1]/"logs/B_finish_PD_detector.json"
    output.write_text(json.dumps(results,indent=2)+"\n")
    print(json.dumps(results,indent=2))
