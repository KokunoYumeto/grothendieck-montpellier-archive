"""Recursive finite-lift spectral feasibility with exact certificates.
Only primitive determinant character at each modulus is covered by this version.
"""
from itertools import product,combinations_with_replacement
from collections import Counter
from fractions import Fraction
from pathlib import Path
import json,time,sys
import numpy as np
from scipy.optimize import linprog
p=Path(__file__).resolve().parent
n=int(sys.argv[1]); maxM=int(sys.argv[2]);start=time.time()

def canon(W,M):
 d=sum(map(sum,W))%M
 if d%2==0:return None
 u=pow(d,-1,M)
 Ws=[tuple((a*u)%M for a in X) for X in W]
 out=[]
 for e in product(*[sorted(set(X)) for X in Ws]):
  if sum(e)%M:continue
  out.append(tuple(sorted(tuple(sorted((a-e[j])%M for a in X)) for j,X in enumerate(Ws))))
 return min(out) if out else None

def covered(W,M):
 sets=[set(X) for X in W]
 E=[e for e in product(*sets) if sum(e)%M==0]
 return all({e[j] for e in E}==sets[j] for j in range(3))

def refine(X,M):
 c=Counter(X);items=sorted(c.items());res=[]
 for ks in product(*[range(m+1) for r,m in items]):
  vals=[]
  for (r,m),k in zip(items,ks):vals.extend([r]*(m-k)+[r+M]*k)
  res.append(tuple(sorted(vals)))
 return res

def solve(W,M):
 sets=[sorted(set(X)) for X in W];mult=[Counter(X) for X in W]
 E=[e for e in product(*sets) if sum(e)%M==0];rows=[(j,v) for j in range(3) for v in sets[j]]
 mat=[[int(e[j]==v) for e in E] for j,v in rows];rhs=[mult[j][v] for j,v in rows]
 ae=np.array(mat,dtype=float);be=np.array(rhs,dtype=float)
 d=linprog(be,A_ub=-ae.T,b_ub=np.zeros(len(E)),bounds=[(-1,1)]*len(rows),method='highs')
 assert d.success
 if d.fun < -1e-8:
  y=[Fraction(float(a)).limit_denominator(10**6) for a in d.x]
  assert all(sum(y[i]*mat[i][j] for i in range(len(rows)))>=0 for j in range(len(E)))
  assert sum(y[i]*rhs[i] for i in range(len(rows)))<0
  return {'W':W,'y':[str(a) for a in y]}
 c=np.zeros(len(E)+1);c[-1]=-1
 r=linprog(c,A_ub=np.c_[-np.eye(len(E)),np.ones(len(E))],b_ub=np.zeros(len(E)),A_eq=np.c_[ae,np.zeros(len(rows))],b_eq=be,bounds=[(0,None)]*(len(E)+1),method='highs')
 assert r.success
 x=[Fraction(float(a)).limit_denominator(10**6) for a in r.x[:-1]]
 assert all(a>=0 for a in x)
 assert all(sum(x[j]*mat[i][j] for j in range(len(E)))==rhs[i] for i in range(len(rows)))
 return {'W':W,'E':E,'x':[str(a) for a in x],'strict':all(a>0 for a in x)}

previous=None;levels=[];M=2
while M<=maxM:
 seen=set();raw=0
 if previous is None:
  spectra=[(0,)*(n-k)+(1,)*k for k in range(n)]
  candidates=combinations_with_replacement(spectra,3)
 else:
  def generate():
   for W in previous:
    yield from product(*[refine(X,M//2) for X in W])
  candidates=generate()
 for W in candidates:
  raw+=1
  if sum(map(sum,W))%2==0 or not covered(W,M):continue
  K=canon(W,M)
  if K is not None:seen.add(K)
 print('GENERATED',n,M,'raw',raw,'orbits',len(seen),'time',round(time.time()-start,2),flush=True)
 good=[];counts=Counter();fp=(p/f'recursive_n{n}_m{M}_certificates.jsonl').open('w')
 for i,W in enumerate(sorted(seen)):
  r=solve(W,M);fp.write(json.dumps(r,separators=(',',':'))+'\n')
  if 'x' in r:good.append(r);counts['feasible']+=1
  else:counts['infeasible']+=1
  if i%5000==0:print('FILTER',n,M,i,'/',len(seen),dict(counts),'time',round(time.time()-start,2),flush=True)
 fp.close()
 obj={'n':n,'M':M,'scope':'primitive determinant character and eigenvalues in mu_M','raw_refinements':raw,'orbits':len(seen),'counts':dict(counts),'feasible':good,'elapsed':time.time()-start}
 (p/f'recursive_n{n}_m{M}_result.json').write_text(json.dumps(obj,indent=2))
 print('DONE',n,M,dict(counts),'time',round(time.time()-start,2),flush=True)
 levels.append(obj);previous=[r['W'] for r in good]
 if not previous:break
 M*=2
(p/f'recursive_n{n}_summary.json').write_text(json.dumps(levels,indent=2))
