"""Exploratory rank-nine coface discovery. Not a certificate."""
import json
from pathlib import Path
from itertools import product
import numpy as np
from scipy.optimize import linprog
from fractions import Fraction
import sympy as sp

BASE=Path(__file__).parent
seed=json.loads((BASE/'k12_survivor_certificate.json').read_text())
V=np.array(seed['vectors'],dtype=int)
Q0=np.array(seed['integer_gram'],dtype=float)/36
w=np.array([0,0,0,0,0,0,0,1,1])
target=np.vstack([V,w])
tri=np.triu_indices(9); fac=np.where(tri[0]==tri[1],1,2)
def rows(v):return v[:,tri[0]]*v[:,tri[1]]*fac
def canon(v):
 v=tuple(int(x) for x in v)
 return v if next(x for x in v if x)>0 else tuple(-x for x in v)
targetset={canon(v) for v in target}
cube=np.array([z for z in product((-1,0,1),repeat=9) if any(z) and next(x for x in z if x)>0 and tuple(z) not in targetset])
constraints=rows(cube).astype(float)
eq=rows(target).astype(float)
aub=np.column_stack([-constraints,np.ones(len(cube))]);aeq=np.column_stack([eq,np.zeros(len(target))])
res=linprog(np.r_[np.zeros(45),-1],A_ub=aub,b_ub=-np.ones(len(cube)),A_eq=aeq,b_eq=np.ones(len(target)),bounds=[(None,None)]*45+[(0,.03)],method='highs')
out={'success':res.success,'message':res.message,'w':w.tolist()}
if res.success:
 q=np.zeros((9,9));q[tri]=res.x[:45];q=q+q.T-np.diag(np.diag(q))
 out.update(slack=float(res.x[-1]),gram=q.tolist(),eigenvalues=np.linalg.eigvalsh(q).tolist())
else:
 if hasattr(res,'ineqlin') and res.ineqlin.marginals is not None: out['duals']=res.ineqlin.marginals.tolist()
(BASE/'k12_coface_tripod_search.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
