"""Exploratory saturation of every two-weight support for E/U, dim(E/U)=2."""
from pathlib import Path
import sys,json,time
from itertools import combinations
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'pencil'))
import per5_prolongation_certificate as p
p.A_DIM=6
p.RECTANGLES=[((0,1),(0,1)),((0,1),(0,2)),((0,1),(1,2)),((0,2),(0,1)),((0,2),(0,2)),((0,2),(1,2))]
T=p.tensor();classes,image=p.weights();weights=[(w,b) for w,b in classes.items() if len(b)-(w in image)>0]
print('quotient weights',len(weights),'totaldimension',sum(len(b)-(w in image) for w,b in weights),flush=True)
poss=[(i,) for i,(w,b) in enumerate(weights) if len(b)-(w in image)>=2]+list(combinations(range(len(weights)),2))
remaining=[];allrec=[];start=time.time()
for num,inds in enumerate(poss):
 ws={weights[i][0] for i in inds}
 basis=[T[:,:,c].copy() for c in range(9) if tuple(-x for x in p.weight_var(*p.VARIABLES[c])) not in ws]
 for i in inds:
  for a,b in weights[i][1]:
   M=np.zeros((6,9),dtype=np.int64);M[a,b]=1;basis.append(M)
 dims={}
 for o in ['A','B']:
  M=p.prolongation_matrix(basis,o);rs,cs=p.pivots(M);dims[o]=int(M.shape[1]-len(rs))
  if dims[o]<11:break
 rec={'weights_indices':list(inds),'weights':[weights[i][0] for i in inds],'blocks':[weights[i][1] for i in inds],'max_extension_dim':len(basis),'prolongation_dimensions_upper':dims}
 allrec.append(rec)
 if all(dims.get(o,0)>=11 for o in ['A','B']):remaining.append(rec)
print('total supports',len(poss),'remaining',len(remaining),'seconds',time.time()-start,flush=True)
for rec in remaining:print(rec,flush=True)
Path(__file__).with_name('j6_prolongation_probe.json').write_text(json.dumps({'weights':[{'weight':w,'block':b} for w,b in weights],'all_records':allrec,'remaining':remaining},indent=2)+'\n')
