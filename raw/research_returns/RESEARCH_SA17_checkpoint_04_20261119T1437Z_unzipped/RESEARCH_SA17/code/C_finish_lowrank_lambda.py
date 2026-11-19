#!/usr/bin/env python3
"""Exact matrix certificates for the odd-characteristic O_3 and O_4 defects.

The representations, invariant forms, symmetric powers, tensor products,
Jordan multiplicities and exterior-power Adams operators are constructed
independently.  No claimed closed formula for Adams operations is input.
"""
from itertools import product
from math import factorial
from time import perf_counter
import json
import numpy as np
from C_finite_certificates import jblock, jordan_counts, exterior, blockdiag, det_mod

def compositions(d, m):
    if m == 1:
        yield (d,)
    else:
        for a in range(d+1):
            for tail in compositions(d-a,m-1):
                yield (a,)+tail

def symmetric(t, d, p):
    """Matrix on degree-d monomials in the standard basis, over F_p."""
    m=len(t); basis=list(compositions(d,m)); index={a:i for i,a in enumerate(basis)}
    out=np.zeros((len(basis),len(basis)),dtype=np.int64)
    zero=(0,)*m
    for col,a in enumerate(basis):
        poly={zero:1}
        for j,exponent in enumerate(a):
            for _ in range(exponent):
                nxt={}
                for b,c in poly.items():
                    for i in range(m):
                        if t[i,j]:
                            bb=list(b);bb[i]+=1;bb=tuple(bb)
                            nxt[bb]=(nxt.get(bb,0)+c*int(t[i,j]))%p
                poly={b:c for b,c in nxt.items() if c}
        for b,c in poly.items():out[index[b],col]=c
    return out,basis

def inverse(t,p):
    n=len(t);a=np.concatenate((t.copy()%p,np.eye(n,dtype=np.int64)),axis=1)
    for j in range(n):
        h=j+int(np.flatnonzero(a[j:,j])[0]);a[[j,h]]=a[[h,j]]
        a[j]=a[j]*pow(int(a[j,j]),-1,p)%p
        for i in range(n):
            if i!=j and a[i,j]:a[i]=(a[i]-a[i,j]*a[j])%p
    return a[:,n:]

def symmetric_monomial_form(basis, dual, signs, p):
    """Induced form from a monomial Gram matrix, normalized symmetrization."""
    d=sum(basis[0]);index={a:i for i,a in enumerate(basis)}
    form=np.zeros((len(basis),len(basis)),dtype=np.int64)
    denominator=pow(factorial(d),-1,p)
    for i,a in enumerate(basis):
        b=[0]*len(a);v=denominator
        for j,r in enumerate(a):
            b[dual[j]]=r;v=v*factorial(r)*pow(signs[j],r,p)%p
        form[i,index[tuple(b)]]=v
    return form

def hyperbolic(t,p):
    n=len(t);zero=np.zeros((n,n),dtype=np.int64);one=np.eye(n,dtype=np.int64)
    return blockdiag(t,inverse(t,p).T),np.block([[zero,one],[one,zero]])

def green_data(p):
    unit=np.eye(p,dtype=np.int64)[0]
    table=np.zeros((p,p,p),dtype=np.int64)
    for i in range(1,p+1):
        for j in range(1,p+1):
            table[i-1,j-1]=jordan_counts(np.kron(jblock(i,p),jblock(j,p)),p)
    def mul(v,w):return np.einsum('i,j,ijk->k',v,w,table)
    def adams(t,n):
        lam=[unit]+[np.array(jordan_counts(exterior(t,r,p),p))
                    for r in range(1,min(len(t),n)+1)]
        lam += [np.zeros(p,dtype=np.int64) for _ in range(n+1-len(lam))]
        psi=[np.zeros(p,dtype=np.int64)]
        for a in range(1,n+1):
            v=(-1)**(a-1)*a*lam[a]
            for r in range(1,a):v=v+(-1)**(r-1)*mul(lam[r],psi[a-r])
            psi.append(v)
        return psi[n]
    ops=np.array([adams(jblock(j,p),p) for j in range(1,p+1)])
    return mul,ops

def check_rep(t,q,p):
    assert np.array_equal(q,q.T)
    assert det_mod(q,p)
    assert np.array_equal(t.T@q@t%p,q%p)
    assert np.array_equal(np.linalg.matrix_power(t,p)%p,np.eye(len(t),dtype=np.int64))

def run(p,mul,ops,rank):
    start=perf_counter();u=jblock(2,p)
    if rank==3:
        w,wb=symmetric(u,2*p-2,p)
        a,qa=hyperbolic(w,p)
        b,bb=symmetric(u,p-1,p)
        qb=symmetric_monomial_form(bb,[1,0],[1,-1],p)
        expected_ac=np.zeros(p,dtype=np.int64);expected_ac[p-2]=2;expected_ac[p-1]=2
        expected_bc=np.zeros(p,dtype=np.int64);expected_bc[p-1]=1
        coefficient=2*p*(p-1)
    else:
        a,qa=hyperbolic(u,p)
        b,bb=symmetric(a,p-1,p)
        qb=symmetric_monomial_form(bb,[2,3,0,1],[1,1,1,1],p)
        expected_ac=np.zeros(p,dtype=np.int64);expected_ac[1]=2
        expected_bc=None;coefficient=None
    check_rep(a,qa,p);check_rep(b,qb,p)
    ac=np.array(jordan_counts(a,p));bc=np.array(jordan_counts(b,p))
    assert np.array_equal(ac,expected_ac)
    if expected_bc is not None:assert np.array_equal(bc,expected_bc)
    tensor=np.kron(a,b)%p
    tc=np.array(jordan_counts(tensor,p))
    assert np.array_equal(tc,mul(ac,bc))
    pa=ac@ops;pb=bc@ops;pt=tc@ops
    defect=mul(pa,pb)-pt
    unit=np.eye(p,dtype=np.int64)[0];z=np.eye(p,dtype=np.int64)[-1];v=np.eye(p,dtype=np.int64)[-2]
    if rank==4:
        assert bc[-1]>0
        coefficient=4*p*int(bc[-1])
    assert np.array_equal(defect,coefficient*(z-v-unit))
    return dict(prime=p,orthogonal_rank=rank,A_dimension=len(a),B_dimension=len(b),
                tensor_dimension=len(tensor),A_Jordan_counts=ac.tolist(),B_Jordan_counts=bc.tolist(),
                tensor_Jordan_counts=tc.tolist(),psi_p_A=pa.tolist(),psi_p_B=pb.tolist(),
                psi_p_tensor=pt.tolist(),defect=defect.tolist(),coefficient=coefficient,
                invariant_nondegenerate_forms_verified=True,runtime_seconds=round(perf_counter()-start,6))

def main():
    start=perf_counter();checks=[];adams=[]
    for p in (3,5,7):
        mul,ops=green_data(p)
        adams.append(dict(prime=p,psi_p_on_Jordan_basis=ops.tolist()))
        checks.extend(run(p,mul,ops,r) for r in (3,4))
    print(json.dumps(dict(checks=checks,adams=adams,total_runtime_seconds=round(perf_counter()-start,6)),indent=2))

if __name__=='__main__':main()
