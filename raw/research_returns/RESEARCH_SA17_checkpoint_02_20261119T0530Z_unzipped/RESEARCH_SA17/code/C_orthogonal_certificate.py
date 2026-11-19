#!/usr/bin/env python3
"""Exact checks for the standard-O_m obstruction and indecomposable identities.

The representation of dimension p+4 is H(V2) orthogonally summed with the
regular permutation representation.  The tensor-square Jordan decomposition
is obtained from its actual matrix.  Adams operations on its summands are
computed from exterior-power matrices, so no asserted Green-ring identity is
used as input.  All arithmetic is integral or modulo the displayed prime.
"""
import json
from time import perf_counter
import numpy as np
from C_finite_certificates import (jblock, jordan_counts, exterior, blockdiag,
                                   det_mod)

def check(p):
    start = perf_counter()
    unit = np.zeros(p, dtype=np.int64); unit[0] = 1
    table = np.zeros((p,p,p), dtype=np.int64)
    for i in range(1,p+1):
        for j in range(1,p+1):
            table[i-1,j-1] = jordan_counts(np.kron(jblock(i,p),jblock(j,p)),p)
    def mul(x,y):
        return np.einsum('i,j,ijk->k',x,y,table)
    def adams_matrix(t,n):
        lam = [unit] + [np.array(jordan_counts(exterior(t,i,p),p),dtype=np.int64)
                        for i in range(1,min(n,len(t))+1)]
        lam += [np.zeros(p,dtype=np.int64) for _ in range(n+1-len(lam))]
        psi = [np.zeros(p,dtype=np.int64)]
        for a in range(1,n+1):
            val = (-1)**(a-1)*a*lam[a]
            for i in range(1,a):
                val = val + (-1)**(i-1)*mul(lam[i],psi[a-i])
            psi.append(val)
        return psi[n]
    psi_basis=np.array([adams_matrix(jblock(j,p),p) for j in range(1,p+1)])
    x=np.eye(p,dtype=np.int64)[1]; z=np.eye(p,dtype=np.int64)[p-1]
    u=np.eye(p,dtype=np.int64)[p-2]
    assert np.array_equal(mul(u,u),unit+(p-2)*z)
    assert np.array_equal(psi_basis[1],2*(z-u))
    assert np.array_equal(psi_basis[p-1],p*unit)
    assert np.array_equal(psi_basis[2],3*unit)
    a=jblock(2,p); ainv=np.array([[1,-1],[0,1]],dtype=np.int64)%p
    h=np.block([[np.zeros((2,2),dtype=np.int64),np.eye(2,dtype=np.int64)],
                [np.eye(2,dtype=np.int64),np.zeros((2,2),dtype=np.int64)]])
    perm=np.zeros((p,p),dtype=np.int64)
    for i in range(p): perm[(i+1)%p,i]=1
    w=blockdiag(a,ainv.T,perm); form=blockdiag(h,np.eye(p,dtype=np.int64))
    assert det_mod(form,p) and np.array_equal(w.T@form@w%p,form%p)
    ww=np.kron(w,w)%p
    tensor_form=np.kron(form,form)%p
    assert np.array_equal(ww.T@tensor_form@ww%p,tensor_form)
    wc=np.array(jordan_counts(w,p)); wwc=np.array(jordan_counts(ww,p))
    psiw=wc@psi_basis; psiww=wwc@psi_basis
    defect=mul(psiw,psiw)-psiww
    expected=8*p*(z-u-unit)
    assert np.array_equal(defect,expected)
    # A direct exterior computation of W itself is also small when p=3.
    if p==3: assert np.array_equal(adams_matrix(w,p),psiw)
    return dict(prime=p,standard_dimension=p+4,tensor_square_dimension=(p+4)**2,
                basis=[f'V{j}' for j in range(1,p+1)],
                psi_p_on_Jordan_basis=psi_basis.tolist(),
                W_Jordan_counts=wc.tolist(),W_tensor_W_Jordan_counts=wwc.tolist(),
                psi_p_W=psiw.tolist(),psi_p_W_tensor_W=psiww.tolist(),
                multiplicativity_defect=defect.tolist(),
                invariant_forms_checked=True,
                largest_exterior_matrix_dimension=max(
                    __import__('math').comb(7 if p==3 else p,i) for i in range((7 if p==3 else p)+1)),
                runtime_seconds=round(perf_counter()-start,6))

if __name__=='__main__':
    print(json.dumps({'checks':[check(p) for p in [3,5,7]]},indent=2))
