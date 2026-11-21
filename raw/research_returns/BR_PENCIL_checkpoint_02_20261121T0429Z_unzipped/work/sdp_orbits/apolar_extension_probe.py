from pathlib import Path
import sys,json
from itertools import combinations
import numpy as np
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'root'))
from coordinate_koszul import slices,koszul

for name,subset in [('j5per',[0,1,3,6,7]),('j6per',[0,1,3,6,7,9])]:
 supp,ms=slices(subset,1);T=np.array(ms);a,b,c=T.shape
 K=s.Matrix(koszul(ms,1));r=K.rank();print(name,'K',K.shape,'rank',r,flush=True)
 left=K.T.nullspace();L=s.Matrix.vstack(*(x.T for x in left));pairs=list(combinations(range(a),2));pi={p:i for i,p in enumerate(pairs)}
 checks=[]
 for i in range(a):
  Z=s.zeros(len(pairs)*b,a*b)
  for j in range(a):
   if i==j:continue
   p=tuple(sorted((i,j)));sgn=1 if i<j else -1
   for v in range(b):Z[pi[p]*b+v,j*b+v]=sgn
  checks.append(L*Z)
 H=s.Matrix.vstack(*checks)
 space=H.nullspace();print(' extension space dimension',len(space),flush=True)
 out={'case':name,'existing_K_rank':r,'allowed_extension_dimension':len(space),'vectors':[[str(x) for x in v] for v in space]}
 Path(__file__).with_name(name+'_apolar_linear.json').write_text(json.dumps(out,indent=2)+'\n')
