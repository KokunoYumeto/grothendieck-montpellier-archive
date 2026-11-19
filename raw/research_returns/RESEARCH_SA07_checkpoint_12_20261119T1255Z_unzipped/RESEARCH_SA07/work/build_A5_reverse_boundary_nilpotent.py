#!/usr/bin/env python3
"""Exact reverse boundary shear, reconstructed from the frozen A5 input JSON.

The profinite parameter is symbolic: a_2=0 and a_l=1 for every odd l.
All finite matrices and the extension correction are integral and checked here.
"""
from functools import reduce
from hashlib import sha256
from math import gcd
from pathlib import Path
from time import perf_counter
import json
import numpy as np
import sympy as sp

started=perf_counter()
source=Path(__file__).with_name('build_A5_boundary_nilpotent.json')
raw=source.read_bytes(); data=json.loads(raw)
assert sha256(raw).hexdigest()=='ba0e10ed1fc1eb306fafdfbb2e77fe3ed38f17f5ba0f5593188f59203872b111'
group=[tuple(h) for h in data['group']]; idx={h:i for i,h in enumerate(group)}
one=tuple(range(5)); x=tuple(data['x']); y=tuple(data['y'])
def mul(a,b):return tuple(a[b[i]] for i in range(5))
def inv(a):return tuple(a.index(i) for i in range(5))
def dot(A,B):
    bound=int(np.max(np.abs(A)))*int(np.max(np.abs(B)))*A.shape[1]
    assert bound<2**63, bound
    return A@B
C=np.array(data['cycle_basis'],dtype=np.int64)
non_tree=data['non_tree_edges']; B=np.array(data['boundary_matrix'],dtype=np.int64)
S=np.array(data['S'],dtype=np.int64); T=np.array(data['T'],dtype=np.int64)
E=np.array(data['E'],dtype=np.int64); q=np.array(data['proper_detector'],dtype=np.int64).reshape(1,61)
A=np.array(data['base_exponent_map'],dtype=np.int64)
def action(h):
    image=np.zeros_like(C)
    for g in group:
        for j in (0,1):image[2*idx[mul(h,g)]+j,:]=C[2*idx[g]+j,:]
    result=image[non_tree,:]
    assert np.array_equal(dot(C,result),image)
    return result
def standard(h):
    result=np.zeros((4,4),dtype=np.int64)
    for j in range(4):
        if h[j]<4:result[h[j],j]+=1
        if h[4]<4:result[h[4],j]-=1
    return result
rho={h:action(h) for h in group}; V={h:standard(h) for h in group}
assert np.array_equal(rho[x],np.array(data['action_x']))
assert np.array_equal(rho[y],np.array(data['action_y']))
b=B[:,[0]]; tb=dot(T,b)
ell_idx=next(i for i in range(4) if tb[i,0]); ell=np.zeros((1,4),dtype=np.int64);ell[0,ell_idx]=1
qs=dot(q,S); v_idx=next(i for i in range(4) if qs[0,i]); v0=np.zeros((4,1),dtype=np.int64);v0[v_idx,0]=1
R=sum((dot(dot(rho[h],b),dot(ell,V[inv(h)])) for h in group),np.zeros((61,4),dtype=np.int64))
U=sum((dot(dot(V[h],v0),dot(q,rho[inv(h)])) for h in group),np.zeros((4,61),dtype=np.int64))
rscalar=15*int(tb[ell_idx,0]); uscalar=15*int(qs[0,v_idx])
assert rscalar and uscalar
assert np.array_equal(dot(T,R),rscalar*np.eye(4,dtype=np.int64))
assert np.array_equal(dot(U,S),uscalar*np.eye(4,dtype=np.int64))
assert not np.any(dot(U,B))
assert np.array_equal(dot(E,R),60*R)
for h in (x,y):
    assert np.array_equal(dot(rho[h],R),dot(R,V[h]))
    assert np.array_equal(dot(U,rho[h]),dot(V[h],U))
Nraw=dot(R,U); divisor=reduce(gcd,(abs(int(n)) for n in Nraw.flat if n));N=Nraw//divisor
assert reduce(gcd,(abs(int(n)) for n in N.flat if n))==1
assert not np.any(dot(N,N))
assert not np.any(dot(N,B))
assert not np.any(dot(A,N))
assert np.array_equal(dot(E,N),60*N)
assert not np.any(dot(N,E))
assert sp.Matrix(N.tolist()).rank()==4
for h in (x,y):assert np.array_equal(dot(N,rho[h]),dot(rho[h],N))
# Integral membership in the actual boundary lattice, not only its Q-span.
bcols=data['boundary_basis_columns']; brows=data['boundary_basis_rows'];Bb=B[:,bcols]
square=sp.Matrix(Bb[brows,:].tolist()); square_inverse=square.inv()
assert all(sp.denom(z)==1 for z in square_inverse)
left=np.zeros((43,61),dtype=np.int64);left[:,brows]=np.array(square_inverse.tolist(),dtype=np.int64)
boundary_coordinates=dot(left,N)
assert np.array_equal(dot(Bb,boundary_coordinates),N)
beta_b=np.array(data['beta_b'],dtype=np.int64)
eta_coeff=dot(N,beta_b.T).T
assert not np.any(dot(N,eta_coeff.T))
assert not np.any(dot(A,eta_coeff.T))
# Recover the actual section factor set from delta(beta_b)=60*c.
for h in group:
    products=[idx[mul(h,k)] for k in group]
    cob=dot(rho[h],beta_b.T).T-beta_b[products,:]+beta_b[idx[h],:]
    assert not np.any(cob%60)
    c=cob//60
    corrected=dot(rho[h],eta_coeff.T).T-eta_coeff[products,:]+eta_coeff[idx[h],:]
    assert np.array_equal(corrected,60*dot(N,c.T).T)
i,j=next((i,j) for i in range(61) for j in range(61) if N[i,j])
payload=dict(source_sha256=sha256(raw).hexdigest(),R=R.tolist(),U=U.tolist(),N_reverse=N.tolist(),
    boundary_coordinates=boundary_coordinates.tolist(),extension_eta_coefficient=eta_coeff.tolist(),
    ell_index=ell_idx,v_index=v_idx,T_R_scalar=rscalar,U_S_scalar=uscalar,primitive_divisor=divisor,
    witness_row=i,witness_column=j,witness_N_entry=int(N[i,j]),
    profinite_parameter='a_2=0; a_l=1 for every odd prime l')
Path(__file__).with_suffix('.json').write_text(json.dumps(payload,separators=(',',':'))+'\n')
print('FROZEN_INPUT_SHA256',payload['source_sha256'])
print('STANDARD_SEEDS',ell_idx,v_idx,'T_R_SCALAR',rscalar,'U_S_SCALAR',uscalar)
print('N_REVERSE_DIVISOR',divisor,'RANK',4,'MAX_ENTRY',int(np.max(np.abs(N))))
print('N2=0; N(B)=0; im(N) subset B INTEGRALLY; A*N=0; E*N=60*N; N*E=0')
print('H_EQUIVARIANCE_CHECKED_ON_GENERATORS; delta(eta_coefficient)=60*N*c FOR_ALL_3600_PAIRS')
print('NONINTEGRAL_SHEAR_WITNESS',i,j,int(N[i,j]),'WITH_a_2=0_AND_a_ODD=1')
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'))
