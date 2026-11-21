#!/usr/bin/env python3
"""Enumerate small Borel-invariant extension quotients when weight lines are rigid.

Parameterized socle weights are recorded as unresolved branches, never sampled.
"""
from collections import Counter
from pathlib import Path
import json,argparse,time
import numpy as np
from sympy import Matrix,Rational
from determinant_borel_module import make
from det7_prolongation import prolong,rank

def canonical(rows,d):
    if not rows:return ()
    R,pivots=Matrix(rows).rref()
    return tuple(tuple(R.row(i)) for i in range(len(pivots)))

def quotient_matrices(rows,d):
    if not rows:return Matrix.eye(d),Matrix.eye(d)
    R=Matrix(rows);pivots=[next(j for j in range(d) if R[i,j]) for i in range(R.rows)]
    free=[j for j in range(d) if j not in pivots]
    X=Matrix.eye(d)[:,free];Q=Matrix.eye(d)[free,:]
    for k,p in enumerate(pivots):
        for i,j in enumerate(free):Q[i,p]-=R[k,j]
    assert Q*R.T==Matrix.zeros(len(free),len(rows)) and Q*X==Matrix.eye(len(free))
    return Q,X

def quiver(M):
    ans=[]
    for i,(w,cs,d) in enumerate(M['blocks']):
        start=M['starts'][i];cols=list(range(start,start+d));maps=[]
        for g in M['roots']:
            N=g['matrix'][:,cols]
            targets=sorted(set(M['owners'][int(r)] for r in np.flatnonzero(np.any(N,axis=1))))
            assert len(targets)<=1
            if targets:
                j=targets[0];s=M['starts'][j];dd=M['blocks'][j][2]
                maps.append((j,Matrix(N[s:s+dd,:].tolist())))
        ans.append(maps)
    return ans

def extensions(M,F,QV):
    quot=[quotient_matrices(F[i],d) for i,(w,cs,d) in enumerate(M['blocks'])]
    rigid=[];continuous=[]
    for i,(w,cs,d) in enumerate(M['blocks']):
        Q,X=quot[i]
        if not X.cols:continue
        equations=[]
        for j,N in QV[i]:
            E=quot[j][0]*N*X
            if E.rows:equations.append(E)
        H=Matrix.vstack(*equations) if equations else Matrix.zeros(0,X.cols)
        K=H.nullspace()
        if not K:continue
        lifts=[X*v for v in K]
        if len(K)>1:
            continuous.append({'block':i,'dimension':len(K),'basis':[list(v) for v in lifts]});continue
        G=list(F);G[i]=canonical(F[i]+(tuple(lifts[0]),),d);G=tuple(G)
        rigid.append(G)
    return rigid,continuous

def ambient_basis(M,F):
    a,m=M['T'].shape[:2];E=[M['T'][:,:,c].copy() for c in range(m)]
    for i,rows in enumerate(F):
        s=M['starts'][i];d=M['blocks'][i][2]
        for coeff in rows:
            v=M['X'][:,s:s+d]@np.array([int(x) for x in coeff],dtype=np.int64)
            assert all(x.q==1 if hasattr(x,'q') else True for x in coeff)
            E.append(v.reshape(a,m))
    return E

def serialize(F):
    return [{'block':i,'basis':[[str(x) for x in row] for row in rows]} for i,rows in enumerate(F) if rows]

def search(S,target=17,full_unipotent=False):
    start=time.time();M=make(S,full_unipotent=full_unipotent);QV=quiver(M);m=len(M['variables']);a=len(S);q=target-m
    states={tuple(() for _ in M['blocks'])};branches=[];exclusions=[];history=[]
    for level in range(1,q+1):
        new=set();cnt=Counter()
        for F in states:
            rigid,continuous=extensions(M,F,QV)
            for c in continuous:branches.append({'level':level,'parent':serialize(F),'branch':c})
            new.update(rigid);cnt['continuous_branches']+=len(continuous)
        remain=set()
        for F in new:
            E=ambient_basis(M,F);rs={o:rank(prolong(E,o))[0] for o in ['A','B']}
            if rs['A']>(a-1)*target or rs['B']>(m-1)*target:
                exclusions.append({'level':level,'space':serialize(F),'ranks':rs});cnt['excluded']+=1
            else:remain.add(F)
        history.append({'level':level,'rigid_extensions':len(new),'remaining':len(remain),**cnt})
        print(S,'m',m,'level',level,'rigid',len(new),'remain',len(remain),'branches',cnt['continuous_branches'],'seconds',round(time.time()-start,2),flush=True)
        states=remain
    output={'subset':S,'target_excluded':target,'variables':M['variables'],'quotient_dimension':q,'full_unipotent':full_unipotent,'unipotent_generators':len(M['roots']),
            'block_count':len(M['blocks']),'history':history,'continuous_branches':branches,
            'rigid_survivors':[serialize(F) for F in states],'exclusions':exclusions,
            'complete':not branches,'excluded':not branches and not states,'seconds':time.time()-start}
    return output

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--subset',type=int,nargs='+',required=True);pa.add_argument('--out',type=Path,required=True);pa.add_argument('--full',action='store_true');args=pa.parse_args()
    out=search(args.subset,full_unipotent=args.full)
    args.out.write_text(json.dumps(out,indent=2,default=str)+'\n')
    print({k:v for k,v in out.items() if k not in ['continuous_branches','rigid_survivors','exclusions']},flush=True)

if __name__=='__main__':main()
