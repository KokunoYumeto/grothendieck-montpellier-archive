#!/usr/bin/env python3
from pathlib import Path
from itertools import product
import json,math,time
import numpy as np
from scipy.optimize import linprog
import sympy as s
start=time.perf_counter()
vals=[0,4,8,12,16,24,32]
def col(v):
 a,b,c,d=v;V=2*b*b+c*c+2*d*d
 return [1,a,a*a+2*b*b-c*c-2*d*d,a*a-2*b*b+c*c-2*d*d,a*a-2*b*b-c*c+2*d*d,a**3-a*V+4*b*c*d,a**4-2*a*a*V+16*a*b*c*d+4*b**4+c**4+4*d**4-4*b*b*c*c-8*b*b*d*d-4*c*c*d*d]
reps=[]
for a in (-14,14):
 for b,c,d0 in product(vals,repeat=3):
  if b==c==d0==0:continue
  for sg in (-1,1) if b*c*d0 else (1,):
   reps.append((a,b,c,sg*d0))
force=(-14,16,24,16);fw=s.Rational(1,4)
T_exact=s.Matrix([31,-14,-212,-196,-196,-1976,-19976])-fw*s.Matrix(col(force))
T=np.array(list(T_exact),dtype=float)
M=np.array([col(v) for v in reps],dtype=float).T
scale=np.array([1,14,1000,1000,1000,10000,1000000],dtype=float)
r=linprog(np.zeros(len(reps)),A_eq=M/scale[:,None],b_eq=T/scale,bounds=(0,None),method='highs')
out={'float_success':bool(r.success),'message':r.message,'candidate_count':len(reps)}
if r.success:
 ids=np.flatnonzero(r.x>1e-8).tolist();MM=s.Matrix.hstack(*[s.Matrix(col(reps[i])) for i in ids]);TT=T_exact
 sol=MM.inv()*TT if MM.rows==MM.cols else MM.gauss_jordan_solve(TT)[0]
 assert all(w.is_Rational and w>0 for w in sol)
 assert MM*sol==TT
 out['exact_support']=[{'rep':reps[i],'orbit_total_weight':str(w)} for i,w in zip(ids,sol)]
 out['exact_support'].append({'rep':force,'orbit_total_weight':str(fw)})
 out['exact_rank']=MM.rank();out['result']='PASS_EXACT_POSITIVE_CHARACTER'
else:out['result']='NO_FLOAT_WITNESS'
out['seconds']=time.perf_counter()-start
Path(__file__).with_name('rm_two_slope_search_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
