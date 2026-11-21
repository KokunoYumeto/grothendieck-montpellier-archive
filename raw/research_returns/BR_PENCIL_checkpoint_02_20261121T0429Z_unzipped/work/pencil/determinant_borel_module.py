#!/usr/bin/env python3
"""Integral Borel action on (A tensor B)/T(C*) for a determinant ideal.

The six adjacent row/column root operators generate the unipotent radical.
The quotient basis uses one unit pivot in every image-weight block.
"""
from pathlib import Path
from collections import defaultdict
from itertools import combinations
import json,argparse,time,math
import numpy as np
from sympy import Matrix
from det7_prolongation import data,RECTS,quad_weight,var_weight,prolong,rank

def make(S,full_unipotent=False):
    variables,T,blocks,image=data(S,-1);a,m=len(S),len(variables)
    vindex={v:i for i,v in enumerate(variables)};sindex={q:i for i,q in enumerate(S)}
    allindex={q:i for i,q in enumerate(RECTS)}
    U=np.stack([T[:,:,c].reshape(-1) for c in range(m)],axis=1)
    coords=[];owners=[];starts={};pivots={}
    for i,(w,cs,d) in enumerate(blocks):
        starts[i]=len(coords)
        if w in image:
            pivot=cs[-1];c=image[w];assert U[pivot[0]*m+pivot[1],c] in (-1,1)
            pivots[c]=pivot[0]*m+pivot[1];cs=cs[:-1]
        for q,v in cs:coords.append(q*m+v);owners.append(i)
    # Blocks whose quotient dimension is zero still have their image pivot.
    for c in range(m):
        if c not in pivots:
            nonzero=np.flatnonzero(U[:,c]);assert len(nonzero)==1
            pivots[c]=int(nonzero[0])
    X=np.eye(a*m,dtype=np.int64)[:,coords]
    Q=np.eye(a*m,dtype=np.int64)[coords,:].copy()
    for c,p in pivots.items():Q[:,p]-=U[coords,c]//int(U[p,c])
    assert not np.any(Q@U) and np.array_equal(Q@X,np.eye((a-1)*m,dtype=np.int64))
    roots=[]
    for axis in [0,1]:
        for u in range(3):
            v=u+1;NS=np.zeros((a,a),dtype=np.int64);NB=np.zeros((m,m),dtype=np.int64)
            for h,q in enumerate(S):
                pair=RECTS[q][axis]
                if v not in pair or u in pair:continue
                unsorted=tuple(u if z==v else z for z in pair)
                sg=1 if unsorted[0]<unsorted[1] else -1
                lowered=list(RECTS[q]);lowered[axis]=tuple(sorted(unsorted));target=allindex[tuple(lowered)]
                assert target in sindex,('not an ideal',S,q,target)
                NS[sindex[target],h]=sg
            for c,z in enumerate(variables):
                rc=list(divmod(z,4))
                if rc[axis]!=v:continue
                rc[axis]=u;target=4*rc[0]+rc[1]
                assert target in vindex
                NB[vindex[target],c]=1
            N=np.kron(-NS.T,np.eye(m,dtype=np.int64))+np.kron(np.eye(a,dtype=np.int64),NB)
            assert np.array_equal(N@U,-U@NB.T)
            quotient=Q@N@X
            roots.append({'axis':axis,'lower':u,'upper':v,'matrix':quotient,'ambient':N})
    if full_unipotent:
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

def socle(M):
    answer=[]
    for i,(w,cs,d) in enumerate(M['blocks']):
        start=M['starts'][i];cols=list(range(start,start+d))
        E=Matrix.vstack(*(Matrix(g['matrix'][:,cols].tolist()) for g in M['roots']))
        K=E.nullspace()
        if K:answer.append({'block':i,'weight':w,'dimension':len(K),'basis':[list(v) for v in K]})
    return answer

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--subset',type=int,nargs='+',required=True);args=pa.parse_args()
    M=make(args.subset);a=len(args.subset);m=len(M['variables']);ans=socle(M)
    print('dimensions',a,m,'quotient',len(M['coordinates']),'blocks',len(M['blocks']),flush=True)
    print('socle',ans,flush=True)
    if 17-m==1:
        for r in ans:
            assert r['dimension']==1
            i=r['block'];_,cs,d=M['blocks'][i];coords=cs[:-1] if M['blocks'][i][0] in M['image'] else cs
            v=np.zeros((a,m),dtype=np.int64)
            for c,(h,b) in zip(r['basis'][0],coords):v[h,b]=int(c)
            E=[M['T'][:,:,c] for c in range(m)]+[v]
            print('candidate',i,'coordinate',np.argwhere(v).tolist(),[(o,rank(prolong(E,o))[0],prolong(E,o).shape[1]) for o in ['A','B']],flush=True)

if __name__=='__main__':main()
