#!/usr/bin/env python3
"""Exact finite diagnostics for LIFT32. No global cusp/jet assertion."""
from itertools import product
from fractions import Fraction
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as sp

def ident(n): return tuple(int(i==j) for i in range(n) for j in range(n))
def mm(A,B,n,q):
    return tuple(sum(A[i*n+k]*B[k*n+j] for k in range(n))%q for i in range(n) for j in range(n))
def inv(A,n,q):
    B=[[A[i*n+j] for j in range(n)]+[int(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        p=next((i for i in range(j,n) if B[i][j]%q),None)
        if p is None:return None
        B[j],B[p]=B[p],B[j]; c=pow(B[j][j],-1,q); B[j]=[(c*x)%q for x in B[j]]
        for i in range(n):
            if i!=j:
                c=B[i][j]; B[i]=[(x-c*y)%q for x,y in zip(B[i],B[j])]
    return tuple(B[i][n+j] for i in range(n) for j in range(n))
def gl(n,q):
    return [A for A in product(range(q),repeat=n*n) if inv(A,n,q) is not None]
def embed(A,n):
    a=n-1
    return tuple(A[i*a+j] if i<a and j<a else int(i==j) for i in range(n) for j in range(n))
def unip(n,q):
    ix=[(i,j) for i in range(n) for j in range(i+1,n)]
    out=[]
    for vals in product(range(q),repeat=len(ix)):
        A=list(ident(n))
        for (i,j),v in zip(ix,vals):A[i*n+j]=v
        out.append(tuple(A))
    return out
def addz(x,y):return(x[0]+y[0],x[1]+y[1])
def conjz(x):return(x[0]-x[1],-x[1])
def normz(x):return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
def root(q,j):
    if q==2:return((-1)**(j%2),0)
    return ((1,0),(0,1),(-1,-1))[j%3]
def psi(A,n,q):return root(q,sum(A[i*n+i+1] for i in range(n-1)))
def induced_char(P,U,n,q):
    decomp={}; reps=[]
    for g in P:
        if g in decomp:continue
        j=len(reps);reps.append(g)
        for u in U:decomp[mm(u,g,n,q)]=(j,psi(u,n,q))
    vals={}
    for p in P:
        s=(0,0)
        for j,r in enumerate(reps):
            k,z=decomp[mm(r,p,n,q)]
            if k==j:s=addz(s,z)
        vals[p]=s
    return vals,len(reps)
mirabolic=[]
for n,q in ((2,3),(3,2),(3,3)):
    H=[embed(A,n) for A in gl(n-1,q)]
    P=[]
    for A in H:
        for col in product(range(q),repeat=n-1):
            B=list(A)
            for i,z in enumerate(col):B[i*n+n-1]=z
            P.append(tuple(B))
    U=unip(n,q); chars,d=induced_char(P,U,n,q)
    assert sum(normz(z) for z in chars.values())==len(P)
    Ua=[embed(A,n) for A in unip(n-1,q)]
    # Character restricted to H uses the inherited simple-root character.
    gg,dh=induced_char(H,Ua,n,q)
    assert d==dh
    assert all(chars[h]==gg[h] for h in H)
    mirabolic.append(dict(n=n,q=q,P_order=len(P),dimension=d,irreducible_norm=1,H_character_checks=len(H)))

def lines(n,q):
    out=[]
    for v in product(range(q),repeat=n):
        j=next((j for j,x in enumerate(v) if x),None)
        if j is None:continue
        if v[j]==1:out.append(v)
    return out
def mv(A,v,n,q):return tuple(sum(A[i*n+j]*v[j] for j in range(n))%q for i in range(n))
def canonical(v,q):
    z=next(x for x in v if x);c=pow(z,-1,q)
    return tuple(c*x%q for x in v)
def st_char(A,n,q,L,iv):
    fixedL=[l for l in L if canonical(mv(A,l,n,q),q)==l]
    if n==2:return len(fixedL)-1
    it=tuple(iv[j*n+i] for i in range(n) for j in range(n))
    fixedP=[v for v in L if canonical(mv(it,v,n,q),q)==v]
    flags=sum(sum(x*y for x,y in zip(l,v))%q==0 for l in fixedL for v in fixedP)
    return flags-len(fixedL)-len(fixedP)+1

restrictions=[]
for n,q in ((2,3),(3,2)):
    G=gl(n,q); GI={g:inv(g,n,q) for g in G}; L=lines(n,q)
    chars={g:st_char(g,n,q,L,GI[g]) for g in G}; d=chars[ident(n)]
    assert sum(x*x for x in chars.values())==len(G)
    U=unip(n,q)
    Wh=(0,0)
    for u in U:
        z=conjz(psi(u,n,q));Wh=addz(Wh,(z[0]*chars[u],z[1]*chars[u]))
    assert Wh==(len(U),0)
    # Exact central-idempotent convolution on every element.
    for x in G:
        z=sum(chars[mm(GI[y],x,n,q)]*chars[y] for y in G)
        assert d*z==len(G)*chars[x]
    H=[embed(A,n) for A in gl(n-1,q)]
    C=[tuple((c if i==n-1 else 1) if i==j else 0 for i in range(n) for j in range(n)) for c in range(1,q)]
    K=[mm(h,c,n,q) for h in H for c in C]; KI={k:GI[k] for k in K}
    Ua=[embed(A,n) for A in unip(n-1,q)]
    Z=[tuple(c if i==j else 0 for i in range(n) for j in range(n)) for c in range(1,q)]
    S=[mm(u,z,n,q) for u in Ua for z in Z]
    phase={}
    for u in Ua:
        s=psi(u,n,q)
        assert s[1]==0
        for z in Z:phase[mm(u,z,n,q)]=s[0]
    reps=[];decomp={}
    for k in K:
        if k in decomp:continue
        j=len(reps);reps.append(k)
        for s in S:decomp[mm(k,s,n,q)]=(j,phase[s])
    D=len(reps)
    W=sp.Matrix([[decomp[k][1] if decomp[k][0]==j else 0 for j in range(D)] for k in K])
    B=sp.Matrix([[sp.Rational(d,len(K))*sum(chars[mm(KI[h],x,n,q)]*W[i,j] for i,h in enumerate(K)) for j in range(D)] for x in G])
    grow={g:i for i,g in enumerate(G)}
    A=sp.Matrix([list(B[grow[r],:]) for r in reps])
    assert A.det()!=0
    Ai=A.inv();E=B*Ai
    assert sp.Matrix([list(E[grow[r],:]) for r in reps])==sp.eye(D)
    assert E.T*E/sp.Integer(len(G))==Ai/sp.Integer(D)
    # Full left-K equivariance of the canonical extension, not just H-type occurrence.
    for k in K:
        dom=sp.Matrix([[W[K.index(mm(KI[k],r,n,q)),j] for j in range(D)] for r in reps])
        lhs=sp.Matrix([list(E[grow[mm(KI[k],x,n,q)],:]) for x in G])
        assert lhs==E*dom
    wrong=0
    if q==3:
        # Same generic H data with the wrong scalar central sign is annihilated.
        dec2={};reps2=[]
        for k in K:
            if k in dec2:continue
            j=len(reps2);reps2.append(k)
            for z in Z:
                sign=1 if z==ident(n) else -1
                dec2[mm(k,z,n,q)]=(j,sign)
        for j in range(len(reps2)):
            for x in G:
                val=sum(chars[mm(KI[h],x,n,q)]*(dec2[h][1] if dec2[h][0]==j else 0) for h in K)
                assert val==0;wrong+=1
    restrictions.append(dict(n=n,q=q,G_order=len(G),H_order=len(H),K_order=len(K),Pi_dimension=d,compatible_dimension=D,
      compressed_characteristic_polynomial=str(A.charpoly().as_expr()),extension_norm_gram=str(Ai/D),
      idempotent_convolution_checks=len(G),equivariance_scalar_checks=len(K)*len(G)*D,
      incompatible_central_annihilation_checks=wrong))

out=dict(finding='ALP-LIFT-32',status='PASS',checked_at_utc=datetime.now(timezone.utc).isoformat(),
 scope='Exact finite mirabolic branching, central projector, compatible restriction, norm, and stabilizer-equivariance diagnostics. No global jet or arithmetic lattice claim.',
 mirabolic=mirabolic,restrictions=restrictions)
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
