#!/usr/bin/env python3
"""Exploratory bounded-Hessian test for lambda_2<=18 at n=23.

No theorem is asserted until a separate stdlib reconstruction passes.
All floating products below are sums of bounded integers below2^53.
"""
from collections import deque, defaultdict
from math import comb, factorial
from pathlib import Path
from time import monotonic
import json
import numpy as np
from probe_relative_second_jets import setup, linear_data, direction, second_jet
from check_binary_jets import rank_packed

P=101;N=23;S=18;LOW=968;R=91
OUT=Path('work/root/results/det23_quadratic_relative_jets')

def sparse_reduce(value,rows):
    value=dict(value)
    for pivot,row in sorted(rows.items()):
        c=value.get(pivot,0)
        if c:
            for key,x in row.items():
                y=(value.get(key,0)-c*x)%P
                if y:value[key]=y
                else:value.pop(key,None)
    return value

def module(j,k,r,coordinates):
    offset={17:0,18:len(coordinates[17])}
    index={d:{a:i+offset[d] for i,a in enumerate(coordinates[d])} for d in (17,18)}
    labels={i:a for d in (17,18) for a,i in index[d].items()}
    def key(a,b):
        x,y=index[j][tuple(a)],index[k][tuple(b)]
        return tuple(sorted((x,y))) if j==k else (x,y)
    highest={}
    for t in range(r+1):
        z=key((j-t,t,0),(k-r+t,r-t,0))
        highest[z]=(highest.get(z,0)+(-1)**t*comb(r,t))%P
    highest={z:x for z,x in highest.items() if x}
    pending=deque([(highest,())]);blocks=defaultdict(dict);basis=[]
    while pending:
        original,word=pending.popleft()
        if not original:continue
        a,b=next(iter(original));weight=tuple(x+y for x,y in zip(labels[a],labels[b]))
        reduced=sparse_reduce(original,blocks[weight])
        if not reduced:continue
        lead=min(reduced);inverse=pow(reduced[lead],-1,P)
        blocks[weight][lead]={z:x*inverse%P for z,x in reduced.items()}
        basis.append(dict(type=[j,k,r],word=list(word),terms=[[*z,x] for z,x in sorted(original.items())]))
        for root in (0,1):
            lowered={}
            for (a,b),coefficient in original.items():
                aa,bb=list(labels[a]),list(labels[b])
                for side in (0,1):
                    alpha=aa if side==0 else bb
                    c=alpha[root]
                    if not c:continue
                    changed=list(alpha);changed[root]-=1;changed[root+1]+=1
                    z=key(changed,bb) if side==0 else key(aa,changed)
                    lowered[z]=(lowered.get(z,0)+c*coefficient)%P
            pending.append(({z:x for z,x in lowered.items() if x},word+(root,)))
    expected=(j+k-2*r+1)*(j+k-r+2)*(r+1)//2
    assert len(basis)==expected,(j,k,r,len(basis),expected)
    return basis

def tangent_directions(jac,reduced,pivots):
    vectors=[];basis={};state=20261123
    while len(vectors)<R:
        v,state=direction(reduced,pivots,P,state)
        z=(jac[LOW:]@v)%P
        for pivot,row in sorted(basis.items()):
            z=(z-int(z[pivot])*row)%P
        support=np.flatnonzero(z)
        if not len(support):continue
        pivot=int(support[0]);basis[pivot]=z*pow(int(z[pivot]),-1,P)%P
        vectors.append(v)
    return np.array(vectors)

def mixed_second(matrices,coordinates,maps,base,vectors):
    variations=vectors.reshape(R,3,N,N).astype(np.float64)
    matrices=[a.astype(np.float64) for a in matrices]
    eye=np.eye(N,dtype=np.float64)
    first=np.zeros((R,1,N,N),dtype=np.float64)
    pair=np.triu_indices(R);answer=[]
    for degree in range(1,S+1):
        size=len(coordinates[degree])
        h=np.zeros((R,R,size),dtype=np.int64)
        nextfirst=np.zeros((R,size,N,N),dtype=np.float64) if degree<S else None
        for k,(dest,source) in enumerate(maps[degree]):
            # tr(V_s Q'_t): exact integer dot products <=529*100^2.
            q=first[:,source].transpose(0,1,3,2).reshape(R*len(source),N*N)
            traces=(variations[:,k].reshape(R,N*N)@q.T).astype(np.int64).reshape(R,R,len(source))%P
            h[:,:,dest]+=traces
            if degree<S:
                left=matrices[k]@first[:,source]
                right=variations[:,k,None]@base[degree-1][None,source].astype(np.float64)
                nextfirst[:,dest]+=left+right
        h=h%P
        assert np.array_equal(h,h.transpose(1,0,2))
        answer.extend((h[pair[0],pair[1],:].T*pow(2,-1,P)%P).astype(np.uint8))
        if degree<S:
            trace=np.trace(nextfirst,axis1=2,axis2=3).astype(np.int64)*pow(degree,-1,P)%P
            first=(trace[:,:,None,None]*eye-nextfirst)%P
        print(json.dumps(dict(stage='mixed_derivatives',degree=degree)),flush=True)
    return np.array(answer,dtype=np.uint8),pair

def normalized_tangents(jac,vectors,coordinates,matrices):
    high=(jac[LOW:]@vectors.T%P).T.copy()
    cursor=0;inverse=pow(factorial(N)%P,-1,P)
    for degree in (17,18):
        for alpha in coordinates[degree]:
            scale=factorial(N-degree)*inverse
            for a in alpha:scale*=factorial(a)
            high[:,cursor]=high[:,cursor]*(scale%P)%P;cursor+=1
    ell=[int(np.trace(a))*pow(N,-1,P)%P for a in matrices]
    index={a:i for i,a in enumerate(coordinates[17])};offset=len(index)
    for t,alpha in enumerate(coordinates[18]):
        for k in range(3):
            if alpha[k]:
                beta=list(alpha);beta[k]-=1
                high[:,offset+t]-=alpha[k]*ell[k]*high[:,index[tuple(beta)]]
    return high%P

def main():
    start=monotonic();OUT.mkdir(parents=True,exist_ok=True)
    matrices,coordinates,maps,base,jac=setup(N,S,P,20261122)
    reduced,pivots,normal,rank=linear_data(jac,LOW,P)
    assert rank==1059 and len(normal)==270
    vectors=tangent_directions(jac,reduced,pivots)
    assert not np.any(jac[:LOW]@vectors.T%P)
    np.savez_compressed(OUT/'linear_data.npz',jacobian=jac.astype(np.uint8),normal=normal.astype(np.uint8),directions=vectors.astype(np.uint8))
    print(json.dumps(dict(stage='linear',shape=jac.shape,normal_dimension=len(normal),seconds=monotonic()-start)),flush=True)
    mixed,pair=mixed_second(matrices,coordinates,maps,base,vectors)
    # Independently compare selected diagonal directions with the older full recurrence.
    for s in (0,17,90):
        column=next(t for t,(i,j) in enumerate(zip(*pair)) if i==s and j==s)
        assert np.array_equal(mixed[:,column],second_jet(matrices,coordinates,maps,base,vectors[s],P))
    np.save(OUT/'mixed_second_coefficients.npy',mixed)
    normalpart=(normal.astype(np.float64)@mixed.astype(np.float64)).astype(np.int64)%P
    high=normalized_tangents(jac,vectors,coordinates,matrices).astype(np.float64)
    basis=[]
    for t in ((17,17,16),(17,18,17),(18,18,18)):
        block=module(*t,coordinates);basis.extend(block)
        print(json.dumps(dict(stage='quadratic_module',type=t,dimension=len(block))),flush=True)
    assert len(basis)==1060
    (OUT/'quadratic_basis.json').write_text(json.dumps(basis,separators=(',',':'))+'\n')
    qrows=[]
    for record in basis:
        terms=np.array(record['terms'],dtype=np.int64)
        value=((high[:,terms[:,0]]*terms[:,2])@high[:,terms[:,1]].T).astype(np.int64)%P
        symmetric=(value+value.T)*pow(2,-1,P)%P
        qrows.append(symmetric[pair])
    matrix=np.concatenate((normalpart,np.array(qrows)),axis=0).astype(np.uint8)
    np.save(OUT/'combined_matrix.npy',matrix)
    print(json.dumps(dict(stage='rank_start',shape=matrix.shape,seconds=monotonic()-start)),flush=True)
    rr,columns,minor=rank_packed([bytes(row) for row in matrix],P)
    result=dict(status='EXPLORATORY',shape=list(matrix.shape),rank=rr,full_row_rank=rr==len(matrix),minor=minor,pivot_columns=columns,seconds=monotonic()-start)
    (OUT/'status.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='pivot_columns'}),flush=True)

if __name__=='__main__':main()
