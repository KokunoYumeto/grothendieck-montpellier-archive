#!/usr/bin/env python3
"""Rejected-route certificate: constant symmetrizers of elliptic Cartier pencils.
No monodromy conclusion is drawn.  The degree-three one-factor pencil
is symmetrizable, but the next four tested pole bounds are not.
"""
import json
from pathlib import Path
src=Path(__file__).with_name('ordinary_abelian_surface.py')
ns={'__file__':str(src)}
exec(src.read_text().split("u,v,w,z=sp.symbols('u v w z')")[0],ns)
out=[]
for m in [3,6,9,12,15]:
 B=[(i,0) for i in range(m//2+1)]+[(i,1) for i in range((m-3)//2+1)]
 bi={x:i for i,x in enumerate(B)}
 Ms=[[[bi[z] for z in ns['cartier'](ns['mul']({a},{b}))] for b in B] for a in B]
 rows=[]
 for M in Ms:
  for i in range(m):
   for j in range(i):
    z=0
    for k in M[j]:z^=1<<(i*m+k)
    for k in M[i]:z^=1<<(j*m+k)
    rows.append(z)
 piv={}
 for z in rows:
  while z:
   k=z.bit_length()-1
   if k in piv:z^=piv[k]
   else:piv[k]=z;break
 free=[i for i in range(m*m) if i not in piv];basis=[]
 for j in free:
  z=1<<j
  for k in sorted(piv):
   if (z&piv[k]).bit_count()%2:z^=1<<k
  assert all((z&r).bit_count()%2==0 for r in rows)
  basis.append(z)
 ranks=[]
 for z in basis:
  cols=[sum(((z>>(i*m+j))&1)<<i for i in range(m)) for j in range(m)]
  ranks.append(ns['rank'](cols))
 out.append({'pole_degree':m,'unknown_matrix_size':m,
  'linear_equation_rank':len(piv),'symmetrizer_dimension':len(free),
  'basis_matrices_encoded_row_major':basis,'basis_matrix_ranks':ranks})
dest=Path(__file__).resolve().parents[1]/'outputs'/'cartier_symmetrizer_probe.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
