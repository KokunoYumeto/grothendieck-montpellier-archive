#!/usr/bin/env python3
"""Actual integral Cayley-graph homology and a boundary-moving nilpotent."""
from collections import deque
from functools import reduce
from math import gcd,lcm
from pathlib import Path
from time import perf_counter
import json
import numpy as np
import sympy as sp

started=perf_counter()
one=tuple(range(5));x=(1,2,0,3,4);y=(1,2,3,4,0)
def mul(a,b):return tuple(a[b[i]] for i in range(5))
def inv(a):return tuple(a.index(i) for i in range(5))
def order(a):
    u=one
    for n in range(1,61):
        u=mul(u,a)
        if u==one:return n
    raise AssertionError(a)
z=inv(mul(x,y));assert [order(t) for t in (x,y,z)]==[3,5,5]

group=[one];index={one:0};parent={};todo=deque([one])
while todo:
    h=todo.popleft()
    for j,t in enumerate((x,y)):
        ht=mul(h,t)
        if ht not in index:
            index[ht]=len(group);group.append(ht);todo.append(ht);parent[ht]=(h,j)
assert len(group)==60
edge=lambda h,j:2*index[h]+j
tree={edge(h,j) for h,j in parent.values()}
non_tree=[i for i in range(120) if i not in tree]
assert len(tree)==59 and len(non_tree)==61
paths={one:np.zeros(120,dtype=np.int64)};words={one:()}
for h in group[1:]:
    p,j=parent[h];v=paths[p].copy();v[edge(p,j)]+=1;paths[h]=v;words[h]=words[p]+(j,)
C=np.zeros((120,61),dtype=np.int64)
boundary=np.zeros((60,120),dtype=np.int64)
for h in group:
    for j,t in enumerate((x,y)):
        e=edge(h,j);boundary[index[mul(h,t)],e]+=1;boundary[index[h],e]-=1
for k,e in enumerate(non_tree):
    h=group[e//2];j=e%2
    C[:,k]=paths[h]-paths[mul(h,(x,y)[j])];C[e,k]+=1
assert np.array_equal(C[non_tree,:],np.eye(61,dtype=np.int64))
assert not np.any(boundary@C)

def action(h):
    image=np.zeros_like(C)
    for g in group:
        for j in (0,1):image[edge(mul(h,g),j),:]=C[edge(g,j),:]
    A=image[non_tree,:]
    assert np.array_equal(C@A,image)
    return A
actions={h:action(h) for h in group}
for a,b in ((x,y),(y,x),(x,x),(y,y)):
    assert np.array_equal(actions[a]@actions[b],actions[mul(a,b)])

def standard(h):
    A=np.zeros((4,4),dtype=np.int64)
    for j in range(4):
        if h[j]<4:A[h[j],j]+=1
        if h[4]<4:A[h[4],j]-=1
    return A
V={h:standard(h) for h in group}

cusps=[];B=[];F=[];u=np.array([1,1,1,-3],dtype=np.int64)
assert np.array_equal(V[x]@u,u)
for kind,t,word in [('x',x,[(0,1)]),('y',y,[(1,1)]),('z',z,[(1,-1),(0,-1)])]:
    seen=set()
    for h in group:
        if h in seen:continue
        orbit=[];g=h
        for _ in range(order(t)):orbit.append(g);seen.add(g);g=mul(g,t)
        assert g==h
        cycle=np.zeros(120,dtype=np.int64)
        for start in orbit:
            g=start
            for j,sign in word:
                a=(x,y)[j]
                if sign==1:cycle[edge(g,j)]+=1;g=mul(g,a)
                else:g=mul(g,inv(a));cycle[edge(g,j)]-=1
        assert not np.any(boundary@cycle)
        b=cycle[non_tree];assert np.array_equal(C@b,cycle)
        B.append(b);F.append(V[h]@u if kind=='x' else np.zeros(4,dtype=np.int64))
        cusps.append(dict(kind=kind,representative=index[h],orbit=[index[g] for g in orbit]))
B=np.stack(B,axis=1);F=np.stack(F,axis=1)
assert B.shape==(61,44) and F.shape==(4,44)
assert not np.any(B@np.ones(44,dtype=np.int64))
assert not np.any(F@np.ones(44,dtype=np.int64))
Bsym=sp.Matrix(B.tolist());_,bcols=Bsym.rref();bcols=list(bcols)
assert len(bcols)==43
Bb=B[:,bcols];_,brows=sp.Matrix(Bb.T.tolist()).rref();brows=list(brows)
square=sp.Matrix(Bb[brows,:].tolist());sinv=square.inv()
den=lcm(*[int(sp.denom(a)) for a in sinv]);assert den==1
left=np.zeros((43,61),dtype=np.int64);left[:,brows]=np.array(sinv.tolist(),dtype=np.int64)
assert np.array_equal(left@Bb,np.eye(43,dtype=np.int64))
P0=Bb@left;T0=F[:,bcols]@left
assert np.array_equal(P0@B,B) and np.array_equal(T0@B,F)

def dot(A,B):
    bound=int(np.max(np.abs(A)))*int(np.max(np.abs(B)))*A.shape[1]
    assert bound<2**63
    return A@B

E=sum((dot(dot(actions[h],P0),actions[inv(h)]) for h in group),np.zeros((61,61),dtype=np.int64))
assert np.array_equal(dot(E,E),60*E)
assert np.array_equal(dot(E,B),60*B)
for h in (x,y):assert np.array_equal(dot(E,actions[h]),dot(actions[h],E))
Q=60*np.eye(61,dtype=np.int64)-E
for j in range(61):
    averaged=sum((np.outer(actions[h][:,j],V[inv(h)][0,:]) for h in group),np.zeros((61,4),dtype=np.int64))
    S=dot(Q,averaged)
    if np.any(S):break
else:raise AssertionError('No proper standard representation found')
assert sp.Matrix(S.tolist()).rank()==4
T=dot(T0,E)
for h in (x,y):
    assert np.array_equal(dot(actions[h],S),dot(S,V[h]))
    assert np.array_equal(dot(T,actions[h]),dot(V[h],T))
Nraw=dot(S,T);divisor=reduce(gcd,(abs(int(a)) for a in Nraw.flat if a))
N=Nraw//divisor
assert not np.any(dot(N,N))
assert not np.any(dot(E,N))
assert np.array_equal(dot(N,E),60*N)
for h in (x,y):assert np.array_equal(dot(N,actions[h]),dot(actions[h],N))
assert sp.Matrix(N.tolist()).rank()==4
nb=dot(N,B[:,[0]])[:,0];assert np.any(nb)
k=next(i for i,a in enumerate(nb) if a)
q=Q[k,:].copy();qdiv=reduce(gcd,(abs(int(a)) for a in q if a));q//=qdiv
assert not np.any(dot(q.reshape((1,61)),B))
detected=int(dot(q.reshape((1,61)),nb.reshape((61,1)))[0,0]);assert detected!=0
gamma=np.eye(61,dtype=np.int64)+60*N;ginv=np.eye(61,dtype=np.int64)-60*N
assert np.array_equal(dot(gamma,ginv),np.eye(61,dtype=np.int64))
assert np.array_equal(dot(ginv,gamma),np.eye(61,dtype=np.int64))
base_exponents=np.stack([C[0::2,:].sum(axis=0),C[1::2,:].sum(axis=0)])
assert not np.any(dot(base_exponents,N))
base_minor=base_exponents[:,[1,6]]
assert np.array_equal(base_minor,np.array([[2,1],[-1,-1]],dtype=np.int64))
assert int(base_minor[0,0])*int(base_minor[1,1])-int(base_minor[0,1])*int(base_minor[1,0])==-1
assert np.array_equal(dot(base_exponents,gamma),base_exponents)
base_loop_words=[]
for j0 in (1,6):
    e=non_tree[j0];h=group[e//2];t=(x,y)[e%2];ht=mul(h,t)
    word=tuple(i+1 for i in words[h])+(e%2+1,)+tuple(-i-1 for i in reversed(words[ht]))
    image=one;exponents=[0,0]
    for symbol in word:
        generator=(x,y)[abs(symbol)-1]
        image=mul(image,generator if symbol>0 else inv(generator))
        exponents[abs(symbol)-1]+=1 if symbol>0 else -1
    assert image==one and exponents==base_exponents[:,j0].tolist()
    base_loop_words.append(word)

# Actual character projections onto the absolutely irreducible standard V.
chi=lambda h:sum(h[i]==i for i in range(5))-1
affine_numerator=sum(chi(h)*int(np.trace(actions[h])) for h in group)
peripheral_numerator=sum(chi(h)*int(np.trace(dot(E,actions[h]))) for h in group)
assert affine_numerator%60==0 and peripheral_numerator%3600==0
affine=affine_numerator//60;peripheral=peripheral_numerator//3600
assert (affine,peripheral,affine-peripheral)==(4,2,2)

# Literal factor set for the BFS section w_h of F2 -> A5.
# c(h,k) is the cycle of w_h w_k w_(hk)^-1. The two untrans-
# lated tree paths have zero non-tree coordinates, so only h.path(k)
# contributes to its displayed coordinates.
cocycle=np.zeros((60,60,61),dtype=np.int64)
for h in group:
    for k0 in group:
        shifted=np.zeros(120,dtype=np.int64)
        for g in group:
            for j0 in (0,1):shifted[edge(mul(h,g),j0)]=paths[k0][edge(g,j0)]
        cycle=paths[h]+shifted-paths[mul(h,k0)]
        c=cycle[non_tree]
        assert np.array_equal(C@c,cycle)
        cocycle[index[h],index[k0],:]=c
beta_b=cocycle.sum(axis=1)
eta=dot(N,beta_b.T).T
for h in group:
    hj=index[h];hproducts=[index[mul(h,k0)] for k0 in group]
    coboundary=dot(actions[h],beta_b.T).T-beta_b[hproducts,:]+beta_b[hj,:]
    assert np.array_equal(coboundary,60*cocycle[hj,:,:])
    corrected=dot(actions[h],eta.T).T-eta[hproducts,:]+eta[hj,:]
    assert np.array_equal(corrected,60*dot(N,cocycle[hj,:,:].T).T)
print('GROUP_ORDER',len(group),'BRANCH_ORDERS',[order(t) for t in (x,y,z)],flush=True)
print('CUSP_COUNTS',[sum(c['kind']==t for c in cusps) for t in ('x','y','z')],flush=True)
print('AFFINE_RANK',61,'PERIPHERAL_RANK',43,'PROPER_RANK',18,'GENUS',9,flush=True)
print('STANDARD_MULTIPLICITIES',affine,peripheral,affine-peripheral,flush=True)
print('PROPER_INTERTWINER_SEED_CYCLE',j,'N_DIVISOR',divisor,'N_RANK',4,'N_MAX_ENTRY',int(np.max(np.abs(N))),flush=True)
print('BOUNDARY_CLASS_INDEX',0,'IMAGE',nb.tolist(),flush=True)
print('PROPER_DETECTOR_ROW',q.tolist(),'VALUE',detected,flush=True)
print('N_SQUARED_ZERO; H_EQUIVARIANT; INTEGRAL_GAMMA_INVERSE; BOUNDARY_NOT_PRESERVED',flush=True)
print('BASE_HOMOLOGY_AN_ZERO; SURJECTIVE_MINOR',base_minor.tolist(),'DETERMINANT',-1,'LOOP_WORDS',base_loop_words,flush=True)
print('EXPLICIT_SECTION_FACTOR_SET: delta_b=60*c and delta_eta=60*N*c for all3600pairs; eta=N*b.',flush=True)
data=dict(group=group,x=x,y=y,z=z,tree_words=[words[h] for h in group],cusps=cusps,non_tree_edges=non_tree,cycle_basis=C.tolist(),boundary_matrix=B.tolist(),
          boundary_to_standard=F.tolist(),action_x=actions[x].tolist(),action_y=actions[y].tolist(),
          boundary_basis_columns=bcols,boundary_basis_rows=brows,projection_P0=P0.tolist(),boundary_map_T0=T0.tolist(),
          E=E.tolist(),standard_seed=j,averaged_standard_map=averaged.tolist(),S=S.tolist(),T=T.tolist(),N=N.tolist(),N_raw_divisor=divisor,
          boundary_index=0,boundary_image=nb.tolist(),proper_detector=q.tolist(),detected_value=detected,
          affine_standard_multiplicity=affine,peripheral_standard_multiplicity=peripheral,
          beta_b=beta_b.tolist(),extension_correction_eta=eta.tolist(),
          base_exponent_map=base_exponents.tolist(),base_minor_columns=[1,6],base_loop_words=base_loop_words)
Path(__file__).with_suffix('.json').write_text(json.dumps(data,separators=(',',':'))+'\n')
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'),flush=True)
