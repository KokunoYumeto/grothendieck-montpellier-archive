"""Exact symbolic independent-row moment matrix for tail (4,4)."""
from pathlib import Path
from math import comb
from functools import lru_cache
from collections import defaultdict
import json
import sympy as sp
HERE=Path(__file__).resolve().parent
a=sp.symbols('a')
inds=[(p,d-p) for d in range(1,5) for p in range(d,-1,-1)]
W={t:sp.Symbol('w%d%d'%t) for t in inds}
U={t:sp.Symbol('u%d%d'%t) for t in inds if sum(t)>=2}
def central(p,q):
    return sp.expand(sum(comb(p,i)*comb(q,j)*(-W[1,0]/a)**(p-i)*
                         (-W[0,1]/a)**(q-j)*(a if i+j==0 else W[i,j])
                         for i in range(p+1) for j in range(q+1)))
def basis(M):
    A,B,C=M[2,0],M[1,1],M[0,2]
    P,Q,R,S=M[3,0],M[2,1],M[1,2],M[0,3]
    D,E,F,G,H=M[4,0],M[3,1],M[2,2],M[1,3],M[0,4]
    return [(A*C-B*B)**2,
            C*C*D-4*C*B*E+(2*A*C+4*B*B)*F-4*A*B*G+A*A*H,
            2*(C*(P*R-Q*Q)-B*(P*S-Q*R)+A*(Q*S-R*R)),
            2*(D*H-4*E*G+3*F*F)]
@lru_cache(None)
def set_partitions(N):
    if N==0:return ((),)
    ans=[]
    for pi in set_partitions(N-1):
        ans.append(pi+((N-1,),))
        for j in range(len(pi)):
            ans.append(pi[:j]+(pi[j]+(N-1,),)+pi[j+1:])
    return tuple(ans)
@lru_cache(None)
def expectation_pattern(pattern):
    ans=defaultdict(int)
    for pi in set_partitions(len(pattern)):
        blocks=tuple(sorted((sum(pattern[j][0] for j in B),
                             sum(pattern[j][1] for j in B)) for B in pi))
        if any(sum(b)==1 for b in blocks):continue
        ans[blocks]+=1
    return tuple(ans.items())
def main():
    centralM={t:central(*t) for t in U}
    q=[sp.Poly(sp.expand(f),list(W.values())) for f in basis(centralM)]
    F=[sp.expand(f) for f in basis(U)]
    fall={k:sp.prod(a-j for j in range(k)) for k in range(9)}
    matrix=[]
    full=[]
    for row,poly in enumerate(q):
        coefficients=defaultdict(lambda:0)
        for powers,coeff in poly.terms():
            pattern=tuple(t for t,e in zip(inds,powers) for _ in range(e))
            for blocks,num in expectation_pattern(pattern):
                coefficients[blocks]+=coeff*num*fall[len(blocks)]
        coefficients={blocks:sp.factor(c) for blocks,c in coefficients.items() if sp.factor(c)!=0}
        assert all(sum(t)<=4 for blocks in coefficients for t in blocks)
        result=sum(c*sp.prod(U[t] for t in blocks) for blocks,c in coefficients.items())
        picks=[((1,1),)*4,tuple(sorted(((0,2),(0,2),(4,0)))),
               tuple(sorted(((0,2),(3,0),(1,2)))),tuple(sorted(((4,0),(0,4))))]
        raw=[coefficients.get(picks[j],0)/([1,1,2,2][j]) for j in range(4)]
        assert sp.expand(result-sum(raw[j]*F[j] for j in range(4)))==0
        vals=[sp.factor(v/fall[3]) for v in raw]
        matrix.append(vals);full.append(result)
        print('row',row,[str(v) for v in vals],flush=True)
    C=sp.Matrix(matrix)
    print('DET',sp.factor(C.det()),flush=True)
    print('row counts',[(t,C.subs(a,t).rank()) for t in range(3,9)],flush=True)
    data=dict(matrix=[[str(v) for v in row] for row in matrix],
              determinant=str(sp.factor(C.det())),
              raw_monomial_counts=[len(poly.terms()) for poly in q],
              status='PASS exact full moment-polynomial reconstruction')
    (HERE/'DOUBLE_FOUR_MOMENT_MATRIX.json').write_text(json.dumps(data,indent=2)+'\n')
if __name__=='__main__':main()

