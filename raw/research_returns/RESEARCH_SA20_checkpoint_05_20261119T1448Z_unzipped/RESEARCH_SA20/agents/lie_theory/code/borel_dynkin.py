#!/usr/bin/env python3
"""Complete root-span test for all-positive weighted Dynkin diagrams.

For d_i in {1,2}, g(0) is the Cartan subalgebra.  If beta,gamma have d-height
two and beta != gamma, beta-gamma has d-height zero and is not a root.
Consequently d is an sl2 characteristic iff its Cartan element lies in the
span of the coroots of the degree-two roots.  This is exact rational linear
algebra and is necessary AND sufficient, not a random rank experiment.
"""
from pathlib import Path
from itertools import product
import json, time
import numpy as np
import sympy as sp
from coxeter_normalizers import cartan

OUT=Path(__file__).resolve().parents[1]/'logs'

def compute(kind):
    start=time.perf_counter(); A=cartan(kind);n=len(A)
    ident=np.eye(n,dtype=int);S=[]
    for i in range(n):
        s=ident.copy();s[i]-=A[i];S.append(s)
    roots={tuple(map(int,ident[:,i])) for i in range(n)};todo=list(roots)
    for r in todo:
        for s in S:
            q=tuple(map(int,s@r))
            if q not in roots:roots.add(q);todo.append(q)
    pos=sorted(r for r in roots if min(r)>=0)
    d=[sp.Rational(1)]*n
    for i in range(n-1):
        if A[i,i+1]:d[i+1]=d[i]*sp.Rational(int(A[i,i+1]),int(A[i+1,i]))
    G=sp.diag(*d)*sp.Matrix(A)
    assert G==G.T
    inv=sp.Matrix(A).T.inv();accepted=[];rejected=[]
    for diagram in product([1,2],repeat=n):
        H=inv*sp.Matrix(diagram)
        degree2=[r for r in pos if sum(x*y for x,y in zip(r,diagram))==2]
        cols=[]
        for r in degree2:
            rv=sp.Matrix(r);dr=(rv.T*G*rv)[0]/2
            cols.append(sp.Matrix([r[i]*d[i]/dr for i in range(n)]))
        M=sp.Matrix.hstack(*cols) if cols else sp.zeros(n,0)
        ok=M.rank()==M.row_join(H).rank()
        rec={'diagram':diagram,'degree_two_roots':degree2,
             'cartan_coroot_coordinates':[str(x) for x in H]}
        if ok:
            sol,parameters=M.gauss_jordan_solve(H)
            sol=sol.subs({s:0 for s in parameters})
            rec['f_coefficients']=[str(x) for x in sol]
            assert M*sol==H
            accepted.append(rec)
        else:
            # A rational linear functional annihilating the candidate coroots
            # but not H is a compact independently checkable exclusion.
            witness=next(z for z in M.T.nullspace() if (z.T*H)[0]!=0)
            rec['exclusion_covector']=[str(x) for x in witness]
            rec['value_on_h']=str((witness.T*H)[0])
            rejected.append(rec)
    ans={'type':kind,'cartan':A.tolist(),'checked':2**n,'accepted':accepted,
         'rejected':rejected,'seconds':time.perf_counter()-start}
    print(kind,'checked',2**n,'accepted',[x['diagram'] for x in accepted],
          'seconds',round(ans['seconds'],4),flush=True)
    (OUT/f'borel_dynkin_{kind}.json').write_text(json.dumps(ans,indent=2))
    return ans

if __name__=='__main__':
    for kind in ['G2','F4','E6','E7','E8']:compute(kind)
