#!/usr/bin/env python3
"""Exploratory exact-integer profile relaxation, not a tensor construction.

The floating MILP proposes a binary vector. Any returned vector is rounded
and every integer row is checked exactly; an infeasible/timeout solver status
alone is not a proof. Rank coverage is encoded by the exact nine possible
minimal patterns, avoiding exponentially ill-scaled rank coefficients.
"""
from pathlib import Path
from fractions import Fraction
import sys,json,itertools,time
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix

config=json.loads(Path(sys.argv[1]).read_text())
D=config['dimension'];m=6;A=3;n=m*D;M=2**(D-1)
assert D==4
variables=[];lookup={};rows=[]
def var(key):
    if key not in lookup:lookup[key]=len(variables);variables.append(key)
    return lookup[key]
def x(a,s,k):return var(('threshold',a,s,k))
def y(s,p):return var(('pattern',s,p))
def row(label,terms,b):
    c={}
    for j,v in terms:c[j]=c.get(j,0)+v
    rows.append((label,{j:v for j,v in c.items() if v},b))
for a in range(A):
    for s in range(M):
        for k in range(1,n+1):x(a,s,k)
patterns=sorted(set(itertools.permutations((n,0,0)))|
                set(itertools.permutations((n-1,n-1,0)))|
                set(itertools.permutations((n-1,n-2,n-2))))
linear_budget=(53*D*M-1)//12
square_budget=(2809*D*D*M-1)//144
for a in range(A):
    row(['mean',a],[(x(a,s,k),1) for s in range(M) for k in range(1,n+1)],linear_budget)
    row(['square',a],[(x(a,s,k),2*k-1) for s in range(M) for k in range(1,n+1)],square_budget)
    for s in range(M):
        for k in range(1,n):row(['monotone',a,s,k],[(x(a,s,k+1),1),(x(a,s,k),-1)],0)
        for t in range(M):
            h=(s^t).bit_count();h=min(h,D-h)
            if h:
                for k in range(12*h+1,n+1):
                    row(['lipschitz',a,s,t,k],[(x(a,s,k),1),(x(a,t,k-12*h),-1)],0)
for s in range(M):
    row(['cover',s],[(y(s,p),-1) for p in range(len(patterns))],-1)
    for p,pattern in enumerate(patterns):
        for a,k in enumerate(pattern):
            if k:row(['pattern',s,p,a],[(y(s,p),1),(x(a,s,k),-1)],0)
rr=[];cc=[];vv=[]
for i,(_,c,_) in enumerate(rows):
    for j,v in c.items():rr.append(i);cc.append(j);vv.append(v)
matrix=coo_matrix((vv,(rr,cc)),shape=(len(rows),len(variables))).tocsc()
start=time.monotonic()
res=milp(np.zeros(len(variables)),integrality=np.ones(len(variables)),
         bounds=Bounds(np.zeros(len(variables)),np.ones(len(variables))),
         constraints=LinearConstraint(matrix,np.full(len(rows),-np.inf),np.array([r[2] for r in rows])),
         options={'time_limit':config.get('seconds',30),'mip_rel_gap':0})
out={'config':config,'status':int(res.status),'message':str(res.message),
     'elapsed_seconds':time.monotonic()-start,'variables':len(variables),'rows':len(rows),
     'linear_budget':linear_budget,'square_budget':square_budget,
     'scope':'Necessary profile constraints only. Feasible profiles are not tensors or layouts; infeasible solver status is not an exact certificate.'}
if res.x is not None:
    v=np.rint(res.x).astype(int).tolist()
    failures=[label for label,c,b in rows if sum(v[j]*a for j,a in c.items())>b]
    out['exact_integer_rows_pass']=not failures
    out['violated_rows']=failures
    if not failures:
        profiles=[[sum(v[x(a,s,k)] for k in range(1,n+1)) for s in range(M)] for a in range(A)]
        assert all(sum(2**profiles[a][s] for a in range(A))>=2**n for s in range(M))
        out['profiles']=profiles
        out['sums']=[sum(p) for p in profiles]
        out['square_sums']=[sum(k*k for k in p) for p in profiles]
Path(sys.argv[2]).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
