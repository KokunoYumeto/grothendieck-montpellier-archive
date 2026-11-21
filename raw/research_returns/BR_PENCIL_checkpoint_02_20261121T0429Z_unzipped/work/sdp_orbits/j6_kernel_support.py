from pathlib import Path
import sys,json
import sympy as s
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'pencil'))
import per5_prolongation_certificate as p
p.A_DIM=6
p.RECTANGLES=[((0,1),(0,1)),((0,1),(0,2)),((0,1),(1,2)),((0,2),(0,1)),((0,2),(0,2)),((0,2),(1,2))]
T=p.tensor();U=s.Matrix(54,9,lambda r,c:int(T[r//9,r%9,c]))
prior=json.loads(Path(__file__).with_name('j6_prolongation_probe.json').read_text())
records=[]
for rec in prior['remaining']:
 weights={tuple(w) for w in rec['weights']}
 basis=[T[:,:,c].copy() for c in range(9) if tuple(-x for x in p.weight_var(*p.VARIABLES[c])) not in weights]
 for block in rec['blocks']:
  for a,b in block:
   M=np.zeros((6,9),dtype=np.int64);M[a,b]=1;basis.append(M)
 EB=s.Matrix.hstack(*(s.Matrix(list(m.reshape(-1))) for m in basis))
 check={}
 for o in ['A','B']:
  if rec['prolongation_dimensions_upper'][o]!=11:continue
  M=s.Matrix(p.prolongation_matrix(basis,o));ker=M.nullspace();n=6 if o=='A' else 9
  assert len(ker)==11
  columns=[]
  for v in ker:
   for i in range(n):columns.append(EB*s.Matrix([v[j*n+i] for j in range(len(basis))]))
  support=U.row_join(s.Matrix.hstack(*columns))
  rank=support.rank();check[o]=rank
 print(rec['weights_indices'],'needed_E_dim',check,flush=True)
 records.append({'weights_indices':rec['weights_indices'],'needed_E_dimensions':check})
Path(__file__).with_name('j6_kernel_support_probe.json').write_text(json.dumps(records,indent=2)+'\n')
