#!/usr/bin/env python3
"""Reconstruct the new 112-point block as a projective F3 quadratic space.
Coordinates come from the four affine elements' unique fixed points.
"""
from pathlib import Path
import itertools,json,numpy as np
HERE=Path(__file__).resolve().parents[1];PENT=HERE.parent/'pentagon';FIVE=HERE.parent/'five_level_six'
def rref(A):
    A=np.array(A,dtype=np.int64,copy=True)%3;row=0;piv=[]
    for col in range(A.shape[1]):
        nz=np.flatnonzero(A[row:,col])
        if not len(nz):continue
        j=row+int(nz[0]);A[[row,j]]=A[[j,row]];A[row]=A[row]*int(A[row,col])%3
        for k in range(A.shape[0]):
            if k!=row and A[k,col]:A[k]=(A[k]-A[k,col]*A[row])%3
        piv.append(col);row+=1
        if row==A.shape[0]:break
    return A,piv
def rank(A):return len(rref(A)[1])
def inverse(A):
    n=len(A);B,p=rref(np.c_[A,np.eye(n,dtype=int)])
    assert p[:n]==list(range(n))
    return B[:,n:]
def nullspace(A):
    R,p=rref(A);free=[i for i in range(R.shape[1])if i not in p];out=[]
    for f in free:
        v=np.zeros(R.shape[1],dtype=int);v[f]=1
        for j,k in enumerate(p):v[k]=-R[j,f]%3
        out.append(v)
    return np.array(out)
def determinant(A):
    A=np.array(A,dtype=int,copy=True)%3;ans=1
    for i in range(len(A)):
        nz=np.flatnonzero(A[i:,i]);assert len(nz)
        j=i+int(nz[0])
        if i!=j:A[[i,j]]=A[[j,i]];ans=-ans
        d=int(A[i,i]);ans=ans*d%3;A[i]=A[i]*d%3
        for j in range(i+1,len(A)):A[j]=(A[j]-A[j,i]*A[i])%3
    return ans%3
def proj(v):
    v=np.array(v,dtype=int)%3;nz=np.flatnonzero(v);assert len(nz)
    return tuple((v*int(v[nz[0]]))%3)
SL=[np.array(v,dtype=int).reshape(2,2)for v in itertools.product(range(3),repeat=4)
    if (v[0]*v[3]-v[1]*v[2])%3==1]
raw=np.load(PENT/'hurwitz_cubic216_four_13.npz')
stab=np.load(FIVE/'hurwitz_block_stabilizer.npz');base=stab['base']
tuples=raw['tuple_elements'][base];standard=tuples[0,:,2:].reshape(4,2,2)
coordinates=[];transporters=[]
for tup in tuples:
    mats=tup[:,2:].reshape(4,2,2);fixed=[]
    for elt,A in zip(tup,mats):fixed.append(inverse(np.eye(2,dtype=int)-A)@elt[:2]%3)
    Bs=[B for B in SL if all(np.array_equal(B@A@inverse(B)%3,T)for A,T in zip(mats,standard))]
    assert len(Bs)==2 and np.array_equal(Bs[0],-Bs[1]%3)
    vec=np.concatenate([Bs[0]@(q-fixed[3])%3 for q in fixed[:3]])
    coordinates.append(proj(vec));transporters.append(Bs[0])
coords=np.array(coordinates,dtype=int);assert len(set(coordinates))==112 and rank(coords)==6
monomials=[(i,j)for i in range(6)for j in range(i,6)]
N=nullspace(np.array([[v[i]*v[j]%3 for i,j in monomials]for v in coords]))
assert len(N)==1
coeff=N[0];Q=np.zeros((6,6),dtype=int)
for a,(i,j)in zip(coeff,monomials):
    if i==j:Q[i,j]=a
    else:Q[i,j]=Q[j,i]=2*a%3
Q=Q*int(Q.flat[np.flatnonzero(Q)[0]])%3
assert rank(Q)==6 and determinant(Q)==1
assert np.all(np.einsum('bi,ij,bj->b',coords,Q,coords)%3==0)
allproj=sorted({proj(v)for v in itertools.product(range(3),repeat=6)if any(v)})
singular={v for v in allproj if np.array(v)@Q@np.array(v)%3==0}
assert singular==set(coordinates) and len(singular)==112
ids=[]
for i,v in enumerate(coords):
    if rank(coords[ids+[i]])>len(ids):ids.append(i)
    if len(ids)==6:break
V=coords[ids].T;Vi=inverse(V)
def lift_permutation(p):
    W=coords[p[ids]].T;candidates=[]
    for signs in itertools.product([1,2],repeat=5):
        M=W@np.diag((1,)+signs)@Vi%3
        if rank(M)!=6:continue
        if all(proj(M@v)==tuple(coords[int(j)])for v,j in zip(coords,p)):
            candidates.append(M)
    assert len(candidates)==1
    M=candidates[0];T=M.T@Q@M%3
    scalar=next(a for a in [1,2]if np.array_equal(T,a*Q%3))
    return M,scalar
matrices=[];multipliers=[];dets=[]
for p in stab['stabilizer']:
    M,mu=lift_permutation(p);matrices.append(M);multipliers.append(mu);dets.append(determinant(M))
assert set(multipliers)=={1} and set(dets)=={1}
assert np.array_equal(lift_permutation(np.arange(112))[0],np.eye(6,dtype=int))
symbasis=[]
for i,j in monomials:
    E=np.zeros((6,6),dtype=int);E[i,j]=E[j,i]=1;symbasis.append(E)
constraints=[]
for M in matrices:
    constraints.append(np.array([(M.T@E@M-E).reshape(-1)%3 for E in symbasis]).T)
invariants=nullspace(np.vstack(constraints))
assert len(invariants)==1
np.savez_compressed(HERE/'records/hurwitz_orthogonal112.npz',base=base,coordinates=coords,
                    quadratic_form=Q,matrices=np.array(matrices),transporters=np.array(transporters))
out={'statement':'D23.C23','coordinate_construction':'SL2-normalized fixed-point differences (q1-q4,q2-q4,q3-q4), modulo sign',
     'base_linear_tuple':standard.tolist(),'point_count':112,'ambient_dimension':6,
     'quadratic_form':Q.tolist(),'quadratic_space_dimension':1,'form_rank':6,'form_determinant':1,
     'projective_singular_count':112,'all_points_are_exact_singular_locus':True,
     'invariant_symmetric_form_space_dimension':1,
     'stabilizer_generator_multipliers':multipliers,'stabilizer_generator_determinants':dets,
     'stabilizer_matrices':[M.tolist()for M in matrices],
     'projective_action_matches_all112_points':True,'result':'PASS'}
(HERE/'records/hurwitz_orthogonal112.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
