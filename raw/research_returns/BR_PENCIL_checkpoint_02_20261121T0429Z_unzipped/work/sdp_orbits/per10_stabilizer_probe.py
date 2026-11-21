#!/usr/bin/env python3
"""Exploration only: partial triangular stabilizer of the P20 permanent tensor.

The search records all continuous socle branches as unresolved.  It never
samples such a branch or promotes modular exclusions to a final certificate.
"""
from pathlib import Path
from collections import defaultdict
import sys,math,json
import numpy as np
from sympy import Matrix

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'work/pencil'))
from det7_prolongation import data,var_weight
import determinant_borel_extensions as ext


def make(S,full_unipotent=True):
    variables,T,blocks,image=data(S,1);a,m=len(S),len(variables)
    U=np.stack([T[:,:,c].reshape(-1) for c in range(m)],axis=1)
    coords=[];owners=[];starts={};pivots={}
    for i,(w,cs,d) in enumerate(blocks):
        starts[i]=len(coords)
        if w in image:
            pivot=cs[-1];c=image[w]
            assert U[pivot[0]*m+pivot[1],c] in (-1,1)
            pivots[c]=pivot[0]*m+pivot[1];cs=cs[:-1]
        for q,v in cs:coords.append(q*m+v);owners.append(i)
    for c in range(m):
        if c not in pivots:
            nz=np.flatnonzero(U[:,c]);assert len(nz)==1;pivots[c]=int(nz[0])
    X=np.eye(a*m,dtype=np.int64)[:,coords]
    Q=np.eye(a*m,dtype=np.int64)[coords,:].copy()
    for c,p in pivots.items():Q[:,p]-=U[coords,c]//int(U[p,c])
    assert not np.any(Q@U)
    assert np.array_equal(Q@X,np.eye((a-1)*m,dtype=np.int64))
    piv=[tuple(np.argwhere(T[h])[0]) for h in range(a)]
    groups=defaultdict(list)
    for u in range(m):
        for v in range(u+1,m):
            wt=tuple(x-y for x,y in zip(var_weight(variables[u]),var_weight(variables[v])))
            groups[wt].append((u,v))
    roots=[]
    for wt,positions in groups.items():
        residuals=[];representations=[]
        for u,v in positions:
            NB=np.zeros((m,m),dtype=np.int64);NB[u,v]=1
            NS=np.zeros((a,a),dtype=np.int64);res=[]
            for h,L in enumerate(T):
                Z=NB@L+L@NB.T
                for q,p in enumerate(piv):NS[q,h]=Z[p]//int(T[q][p])
                res.append(Z-sum((NS[q,h]*T[q] for q in range(a)),np.zeros((m,m),dtype=np.int64)))
            residuals.append(np.array(res).reshape(-1));representations.append(NS)
        D=Matrix(np.stack(residuals,axis=1).tolist())
        for vector in D.nullspace():
            den=math.lcm(*(int(v.q) for v in vector));coeff=[int(v*den) for v in vector]
            g=math.gcd(*coeff);coeff=[v//abs(g) for v in coeff]
            NB=np.zeros((m,m),dtype=np.int64);NS=np.zeros((a,a),dtype=np.int64)
            for c,(u,v),R in zip(coeff,positions,representations):NB[u,v]=c;NS+=c*R
            N=np.kron(-NS.T,np.eye(m,dtype=np.int64))+np.kron(np.eye(a,dtype=np.int64),NB)
            assert np.array_equal(N@U,-U@NB.T)
            roots.append({'weight':wt,'matrix':Q@N@X,'ambient':N,'variable_matrix':NB,'slice_matrix':NS})
    return {'S':S,'variables':variables,'T':T,'blocks':blocks,'image':image,
            'U':U,'Q':Q,'X':X,'coordinates':coords,'owners':owners,'starts':starts,'roots':roots}


def main():
    S=[0,1,2,3,4,6,7,8,9,10]
    ext.make=make
    out=ext.search(S,target=17,full_unipotent=True)
    out['family']='per';out['scope']='Exploration only; continuous branches remain unresolved.'
    Path(__file__).with_name('per10_stabilizer_probe.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
    print({k:v for k,v in out.items() if k not in ['continuous_branches','rigid_survivors','exclusions']},flush=True)

if __name__=='__main__':main()
