#!/usr/bin/env python3
"""Exact PGO seed transporters for A -> A^5, Z3 -> Z3^5.

This is a necessary finite relaxation; no arithmetic lift is asserted.
"""
from pathlib import Path
import contextlib, importlib.util, io, itertools, json
import numpy as np
from hurwitz_multiplier5_detector import power
HERE=Path(__file__).resolve().parents[1]
PENT=HERE.parent/'pentagon'; FIVE=HERE.parent/'five_level_six'
spec=importlib.util.spec_from_file_location('orth112',HERE/'code/hurwitz_orthogonal112.py')
ort=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(ort)
raw=np.load(PENT/'hurwitz_cubic216_four_13.npz'); A,B,C=raw['generators']; Z=power(A[B],3)
blocks=np.load(PENT/'hurwitz_cubic216_four_13_block0.npz'); bm=blocks['block_map']; qA=blocks['generators'][0]
qZ=power(qA[blocks['generators'][1]],3)
trans=np.load(FIVE/'hurwitz_block_correlations.npz')['transversals']
points=np.array([t[ort.base] for t in trans]); loc=np.full((12,1344),-1,dtype=int)
for j in range(12):loc[j,points[j]]=np.arange(112)

def local(p,j):
 q=loc[j,p[points[j]]]; assert np.all(q>=0);return q

def matpow(M,k):
 r=np.eye(6,dtype=int)
 for _ in range(k):r=r@M%3
 return r

def linear_equations(L,R):
 # N L = R N, row-major vectorization.
 E=np.eye(36,dtype=int).reshape(36,6,6)
 return np.array([(N@L-R@N).reshape(-1)%3 for N in E]).T

def run():
 out=[];save={}
 for j,targets,p in [(0,[0,9],A),(1,list(range(1,7)),power(A,3))]:
  src=[ort.lift_permutation(local(g,j))[0] for g in [p,power(Z,2)]]
  for k in targets:
   dst=[ort.lift_permutation(local(power(g,5),k))[0] for g in [p,power(Z,2)]]
   dims=[]
   for signs in itertools.product([1,2],repeat=2):
    N=ort.nullspace(np.vstack([linear_equations(s,t*e%3) for s,t,e in zip(src,dst,signs)]))
    dims.append([list(signs),len(N)])
    save[f'hom_{j}_{k}_{signs[0]}_{signs[1]}']=N.reshape(-1,6,6)
   row={'source_block':j,'target_block':k,'hom_dimensions':dims};out.append(row);print(row,flush=True)
 np.savez_compressed(HERE/'records/hurwitz_multiplier5_global_seeds_probe.npz',**save)
 (HERE/'records/hurwitz_multiplier5_global_seeds_probe.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
