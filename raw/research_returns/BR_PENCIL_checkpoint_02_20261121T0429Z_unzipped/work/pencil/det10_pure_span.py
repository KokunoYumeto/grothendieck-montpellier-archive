#!/usr/bin/env python3
"""Search exact rational pure points in fixed candidate extension spaces.

This is an upper-construction search. Failure of its finite sign grid proves
nothing about the full Segre intersection. Every found pure point is checked
by exact integer annihilator identities.
"""
from pathlib import Path
from itertools import combinations,product
import argparse,json,time,math
import numpy as np
from sympy import Matrix,Rational
from determinant_borel_module import make
from determinant_borel_extensions import ambient_basis
from det10_final_line_refine import decode
from bigraded_prolongation import primitive

def pure_span(M,F):
    E=ambient_basis(M,F);a,b=E[0].shape
    EB=Matrix.hstack(*(Matrix(x.reshape(-1).tolist()) for x in E));assert EB.rank()==17
    H=np.array([primitive(v) for v in EB.T.nullspace()],dtype=np.int64)
    Z=H.reshape(H.shape[0],a,b)
    allowed=np.any(np.array(E)!=0,axis=0)
    found=[];points=[];tests=0;dim=0
    for k in range(1,a+1):
        for I in combinations(range(a),k):
            J=np.flatnonzero(np.all(allowed[list(I),:],axis=0))
            if not len(J):continue
            for signs in product([-1,1],repeat=k-1):
                x=np.zeros(a,dtype=np.int64);x[list(I)]=[1]+list(signs)
                N=np.tensordot(Z,x,axes=(1,0))[:,J];N=N[np.any(N,axis=1)]
                R=Matrix(N.tolist()) if len(N) else Matrix.zeros(0,len(J));tests+=1
                for v in R.nullspace():
                    y=np.zeros(b,dtype=np.int64);y[J]=primitive(v)
                    z=np.outer(x,y).reshape(-1);assert not np.any(H@z)
                    V=Matrix.hstack(*(found+[Matrix(z.tolist())])) if found else Matrix(z.tolist())
                    if V.rank()>dim:
                        found.append(Matrix(z.tolist()));points.append({'a':x.tolist(),'b':y.tolist()});dim+=1
                        if dim==17:
                            coeff=V.inv_quick() if V.rows==V.cols else V.gauss_jordan_solve(EB)[0]
                            return {'rank':17,'points':points,'tests':tests,'coordinates':[[str(z) for z in coeff.row(i)] for i in range(coeff.rows)]}
    return {'rank':dim,'points':points,'tests':tests}

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--support',type=int,default=14);args=pa.parse_args();here=Path(__file__).resolve().parent
    records=json.loads((here/f'det10_borel_support{args.support}.json').read_text());out=[];start=time.time()
    for rec in records:
        if not rec['rigid_survivors']:continue
        M=make(rec['subset']);results=[]
        for i,sp in enumerate(rec['rigid_survivors']):
            result=pure_span(M,decode(M,sp));result['space']=sp;results.append(result)
            print(rec['subset'],'E',i,'pure-span rank',result['rank'],'tests',result['tests'],'seconds',round(time.time()-start,2),flush=True)
        out.append({'subset':rec['subset'],'results':results})
        (here/f'det10_pure_span_m{args.support}.json').write_text(json.dumps({'status':'EXPLORATION','records':out,'seconds':time.time()-start},indent=2)+'\n')

if __name__=='__main__':main()
