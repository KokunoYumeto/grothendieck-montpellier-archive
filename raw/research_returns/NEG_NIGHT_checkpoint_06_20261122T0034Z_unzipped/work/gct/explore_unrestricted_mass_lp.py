"""Exploratory unrestricted associativity mass relaxation, not a proof register.

All input-unit products are fixed. Every other table position is allowed.
For a proposed total added mass M, each off-diagonal quadratic monomial
xy is bounded above by M(x+y)/4 when total added mass is at most M.
A repeated variable square is bounded by M*x.
"""
from pathlib import Path
import json
import numpy as np
from scipy.sparse import coo_matrix
from scipy.optimize import linprog

src=json.loads(Path('work/gct/dimension_certificate_2744.json').read_text())
names=['mu','Sigma']+[f'g{i}_{w}' for i in (1,2) for w in ('1','12','2','21')]
ix={x:i for i,x in enumerate(names)}
n=len(names)
A=np.zeros((n,n,n),dtype=np.int64)
for row in src['constants']:
    a,b,c=map(ix.__getitem__,row['key'])
    A[a,b,c]=sum(abs(v) for v in row['trace_q'].values())
assert int(A.sum())==4443
variables=[(a,b,c) for a in range(1,n) for b in range(1,n) for c in range(n)]
vi={v:i for i,v in enumerate(variables)}
L=[];Q=[];deltas=[];locators=[]
def side(terms):
    base=0;lin={};quad={}
    for u,v in terms:
        au,av=int(A[u]),int(A[v]);base+=au*av
        if u in vi:lin[vi[u]]=lin.get(vi[u],0)+av
        if v in vi:lin[vi[v]]=lin.get(vi[v],0)+au
        if u in vi and v in vi:
            if u==v:quad[vi[u]]=quad.get(vi[u],0)+4
            else:
                quad[vi[u]]=quad.get(vi[u],0)+1
                quad[vi[v]]=quad.get(vi[v],0)+1
    return base,lin,quad
for a in range(1,n):
 for b in range(1,n):
  for c in range(1,n):
   for z in range(n):
    left=side([((a,b,y),(y,c,z)) for y in range(n)])
    right=side([((b,c,y),(a,y,z)) for y in range(n)])
    for direction,(big,small) in enumerate(((left,right),(right,left))):
        delta=big[0]-small[0]
        lin={k:4*(small[1].get(k,0)-big[1].get(k,0))
             for k in set(small[1])|set(big[1])}
        lin={k:v for k,v in lin.items() if v}
        if not lin and not small[2] and delta<=0:continue
        L.append(lin);Q.append(small[2]);deltas.append(4*delta)
        locators.append([a,b,c,z,direction])
rhs=np.array(deltas,dtype=float)
def solve(M):
    rr=[];cc=[];dd=[]
    for r,(l,q) in enumerate(zip(L,Q)):
        for c in set(l)|set(q):
            v=l.get(c,0)+M*q.get(c,0)
            if v:rr.append(r);cc.append(c);dd.append(-v)
    mat=coo_matrix((dd,(rr,cc)),shape=(len(L),len(variables))).tocsr()
    sol=linprog(np.ones(len(variables)),A_ub=mat,b_ub=-rhs,bounds=(0,None),method='highs')
    return sol

if __name__ == '__main__':
    print('variables',len(variables),'constraints',len(L),flush=True)
    results=[]
    for M in (0,100,250,500,1000,2000,4000,5486):
        sol=solve(M)
        r={'M':M,'status':int(sol.status),'minimum_added_mass_relaxation':None if sol.fun is None else float(sol.fun)}
        print(r,flush=True);results.append(r)
    Path('work/gct/unrestricted_mass_lp_exploration.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2),flush=True)
