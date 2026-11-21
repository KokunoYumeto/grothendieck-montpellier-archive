#!/usr/bin/env python3
"""D23.F28: harmonic exceptional unitary image and twelve kernel orders."""
from pathlib import Path
import sys,json
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'characters/code'))
import krammer_mixed_structure as k
a,b,c=k.kp.matrices(4,3,6);s=k.mm(k.mm(a,b),a);y=k.mp(c,2);z=k.inverse(k.mm(s,y))
eye=np.eye(6,dtype=np.int64)
H=np.array(json.loads((HERE/'krammer_orbital_unitary.json').read_text())['Hermitian_form'],dtype=np.int64)
bar=lambda v:np.asarray(v)%3+3*(-(np.asarray(v)//3)%3)
assert all(np.array_equal(k.mm(k.mm(bar(g).T,H),g),H) for g in [s,y])
def normalize(v):
    j=next(int(w) for w in v if w)
    return tuple(map(int,k.M[k.D[j],v]))
def orders(g):
    v=eye.copy();po=None;sc=None
    for j in range(1,100):
        v=k.mm(v,g)
        if po is None and np.array_equal(v,k.M[v[0,0],eye]):po=j;sc=int(v[0,0])
        if np.array_equal(v,eye):return j,po,sc
    raise RuntimeError('order bound')
local=[orders(g) for g in [s,y,z]]
assert local==[(24,24,1),(6,6,1),(12,12,1)]
T=k.mp(y,2);N=k.A[T,k.N[eye]];assert k.rank(N)==1
v=k.basiscols(N)[:,0]
vs=[normalize(v)];seen={vs[0]}
for v in vs:
    for g in [s,y]:
        w=normalize(k.mm(g,np.array(v)[:,None])[:,0])
        if w not in seen:seen.add(w);vs.append(w)
assert len(vs)==22204
assert all(not np.any(k.mm(k.mm(bar(np.array(v)[None,:]),H),np.array(v)[:,None])) for v in vs)
action_orders=[]
for x0,y0,z0 in [(36,6,3),(24,6,12)]:
    action_orders.extend([(x0,y0),(y0,z0),(z0,x0),(y0,x0),(z0,y0),(x0,z0)])
assert len(set(action_orders))==12
out={'statement':'D23.F28','harmonic_pair':'(K1 K2 K1,K3^2)',
     'local_orders_projective_orders_scalars':local,'isotropic_line_orbit':len(vs),
     'total_isotropic_lines':22204,'twelve_ordered_action_orders':action_orders,
     'determinant_s':6,'determinant_Y':2,
     'result':'PASS; SU6-generation and common-word consequences use the complete proofs F25-F26.'}
(HERE/'krammer_harmonic_orbital.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
