import sympy as s,json
from pathlib import Path
from itertools import product
p=Path(__file__).resolve().parent
obj=json.loads((p/'dyadic_n4_local.json').read_text())
x=s.symbols('x0:4')
for idx,rec in enumerate(obj['records']):
 sets=rec['spectra'];S=[tuple(sets[j].index(e[j]) for j in range(3)) for e in rec['aggregate_support']]
 T={e:1 for e in S}
 cols=[]
 for a in range(3):
  for i in range(4):
   for j in range(4):
    col=[]
    for e in product(range(4),repeat=3):
     f=list(e);f[a]=j
     col.append(T.get(tuple(f),0) if e[a]==i else 0)
    cols.append(s.Matrix(col))
 mat=s.Matrix.hstack(*cols);rank=mat.rank();ns=mat.nullspace()
 rec['GL_lie_rank']=rank;rec['GL_lie_stabilizer_dimension']=48-rank
 rec['determinant_slices']=[]
 for a in range(3):
  b,c=[j for j in range(3) if j!=a]
  Q=s.zeros(4)
  for e in S: Q[e[b],e[c]]+=x[e[a]]
  rec['determinant_slices'].append(str(s.factor(Q.det())))
 print(idx+1,'rank',rank,'kernel',48-rank,rec['determinant_slices'],flush=True)
(p/'dyadic_n4_stabilizers.json').write_text(json.dumps(obj,indent=2))
