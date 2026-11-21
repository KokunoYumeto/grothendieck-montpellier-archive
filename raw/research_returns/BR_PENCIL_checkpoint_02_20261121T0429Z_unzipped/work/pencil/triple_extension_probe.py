#!/usr/bin/env python3
"""Joint AB/AC degree-(1,1,1) necessary condition for fixed extensions."""
from pathlib import Path
from collections import defaultdict
import json,argparse,time
import numpy as np
from sympy import Matrix,Rational
from determinant_borel_module import make
from determinant_borel_extensions import ambient_basis
from det7_prolongation import rank,var_weight,quad_weight
from bigraded_prolongation import primitive

def intersection(E,F,S,variables):
    a,b=E[0].shape;r=len(E);Earr=np.array(E)
    flatF=np.stack([x.reshape(-1) for x in F],axis=1)
    null=Matrix(flatF.T.tolist()).nullspace()
    ann=np.array([primitive(v) for v in null],dtype=np.int64).reshape(len(null),a,b)
    M=np.einsum('lak,sab->lbsk',ann,Earr).reshape(len(null)*b,r*b)
    aw=[tuple(-x for x in quad_weight(q)) for q in S];bw=[var_weight(v) for v in variables]
    eweights=[]
    for L in E:
        nz=np.argwhere(L);weights={tuple(x+y for x,y in zip(aw[int(i)],bw[int(j)])) for i,j in nz};assert len(weights)==1
        eweights.append(next(iter(weights)))
    groups=defaultdict(list)
    for s,w in enumerate(eweights):
        for k,v in enumerate(bw):groups[tuple(x+y for x,y in zip(w,v))].append(s*b+k)
    basis=[];usedrows=set()
    for w,cols in groups.items():
        rows=list(map(int,np.flatnonzero(np.any(M[:,cols],axis=1))))
        assert not usedrows.intersection(rows);usedrows.update(rows)
        block=Matrix(M[np.ix_(rows,cols)].tolist()) if rows else Matrix.zeros(0,len(cols))
        for v in block.nullspace():
            V=np.zeros(r*b,dtype=np.int64)
            V[cols]=primitive(v)
            assert not np.any(M@V)
            X=np.einsum('sab,sc->abc',Earr,V.reshape(r,b));basis.append(X)
    if basis:
        bc=np.stack(basis,axis=0).transpose(2,3,0,1).reshape(b*b,len(basis)*a)
        bc_rank=rank(bc)[0]
    else:bc_rank=0
    return {'intersection_dimension':len(basis),'BC_image_rank':bc_rank,
            'excluded':len(basis)<17 or (len(basis)==17 and bc_rank>17),'basis':basis}

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--support',type=int,required=True);args=pa.parse_args()
    here=Path(__file__).resolve().parent;source=json.loads((here/f'det10_borel_support{args.support}.json').read_text());out=[];t=time.time()
    for rec in source:
        if not rec['rigid_survivors']:continue
        M=make(rec['subset']);spaces=[]
        for sp in rec['rigid_survivors']:
            F=[() for _ in M['blocks']]
            for block in sp:F[block['block']]=tuple(tuple(Rational(x) for x in row) for row in block['basis'])
            spaces.append(ambient_basis(M,F))
        results=[]
        for i,E in enumerate(spaces):
            for j,F in enumerate(spaces[i:],i):
                r=intersection(E,F,rec['subset'],M['variables']);r.pop('basis');r.update(left=i,right=j);results.append(r)
                print(rec['subset'],i,j,r,'seconds',round(time.time()-t,2),flush=True)
        out.append({'subset':rec['subset'],'pairs':results})
        (here/f'det10_triple_support{args.support}.json').write_text(json.dumps(out,indent=2)+'\n')
    print('DONE',time.time()-t,flush=True)

if __name__=='__main__':main()
