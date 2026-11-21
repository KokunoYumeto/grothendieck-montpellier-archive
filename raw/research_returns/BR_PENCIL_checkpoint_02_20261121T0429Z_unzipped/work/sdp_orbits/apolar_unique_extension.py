from pathlib import Path
from itertools import combinations
import sys,json
import numpy as np
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'root'))
from coordinate_koszul import slices,koszul,modular_rank
supp,ms=slices([0,1,3,6,7],1);T=np.array(ms);a,b,c=T.shape
E=[T[:,:,k] for k in range(c)]
X=np.zeros((a,b),dtype=np.int64);X[2,0]=1;E.append(X)
# Tensor with slices E in third factor. Wedge in B: matrix slices map third-factor dual (E) to A.
EB=np.array(E)
bslices=[EB[:,:,j].T for j in range(b)]
K=koszul(bslices,1)
cer=modular_rank(K);print('B wedge E',K.shape,cer['rank_mod_p'],'threshold',8*10,flush=True)
# rank-one points of E: inspect symbolic E matrix
v=s.symbols('a b c d e f g h i x')
M=sum((v[k]*s.Matrix(E[k]) for k in range(10)),s.zeros(a,b))
print(M,flush=True)
out={'B_wedge_rank_mod_p':cer,'B_wedge_shape':list(K.shape),'E_symbolic':str(M),'extension':'c_2 tensor entry_a'}
Path(__file__).with_name('j5per_unique_E.json').write_text(json.dumps(out,indent=2)+'\n')
