"""Discovery only: LP with integer quadratic cuts; final result requires exact certificate."""
import json
from pathlib import Path
from itertools import product
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
import sympy as sp
BASE=Path(__file__).parent
seed=json.loads((BASE/'k12_survivor_certificate.json').read_text())
V=np.array(seed['vectors'],dtype=int);Q0=np.array(seed['integer_gram'],dtype=float)/36
w=np.array([0,0,0,0,0,0,0,1,1]);target=np.vstack([V,w]);tri=np.triu_indices(9); fac=np.where(tri[0]==tri[1],1,2)
def qr(v):
 v=np.array(v,dtype=np.int64)
 return v[...,tri[0]]*v[...,tri[1]]*fac
def canon(v):
 v=tuple(int(x) for x in v)
 return v if next(x for x in v if x)>0 else tuple(-x for x in v)
def short_float(q,bound):
 R=np.linalg.cholesky(q).T; z=np.zeros(9,dtype=int);out=[]
 def visit(i,rem):
  if i<0:
   if np.any(z):out.append(tuple(z))
   return
  shift=R[i,i+1:]@z[i+1:]/R[i,i]
  radius=np.sqrt(max(0,rem))/R[i,i]
  for a in range(int(np.ceil(-shift-radius-1e-8)),int(np.floor(-shift+radius+1e-8))+1):
   z[i]=a;res=rem-(R[i,i]*(a+shift))**2
   if res>=-1e-8:visit(i-1,res)
 visit(8,bound)
 return out
T={canon(v) for v in target}
seen={tuple(z) for z in product((-1,0,1),repeat=9) if any(z) and next(x for x in z if x)>0 and tuple(z) not in T}
rows=[qr(v) for v in seen];rhs=[-1.01]*len(rows)
cuts=[];eq=qr(target);qflat=Q0[tri]
Aeq=np.hstack([eq,np.zeros((len(eq),45))]);beq=np.ones(len(eq))
base_abs=np.vstack([np.hstack([np.eye(45),-np.eye(45)]),np.hstack([-np.eye(45),-np.eye(45)])]);base_rhs=np.r_[qflat,-qflat]
cost=np.r_[np.zeros(45),np.ones(45)]
for it in range(60):
 A=np.vstack([np.hstack([-np.array(rows),np.zeros((len(rows),45))]),base_abs]);b=np.r_[rhs,base_rhs]
 res=linprog(cost,A_ub=A,b_ub=b,A_eq=Aeq,b_eq=beq,bounds=[(None,None)]*45+[(0,None)]*45,method='highs')
 if not res.success:
  print('infeasible',it,res.message,flush=True);break
 q=np.zeros((9,9));q[tri]=res.x[:45];q=q+q.T-np.diag(np.diag(q))
 eig,vec=np.linalg.eigh(q);print('iter',it,'min_eigen',eig[0],'L1',res.fun,'rows',len(rows),flush=True)
 if eig[0]<.001:
  for j in range(9):
   if eig[j]>=.002:continue
   v=np.rint(vec[:,j]*100).astype(int)
   rows.append(qr(v));rhs.append(-.002*float(v@v));cuts.append(v.tolist())
  continue
 short=short_float(q,1.0099999);bad={canon(v) for v in short}-T
 if bad:
  print('bad',len(bad),flush=True)
  for v in sorted(bad):
   assert v not in seen;seen.add(v);rows.append(qr(v));rhs.append(-1.01)
  continue
 # Rationalize free variables and solve exact equalities.
 E=sp.Matrix(eq.tolist());piv=E.rref()[1];free=[i for i in range(45) if i not in piv]
 for den in [3600,36000,360000]:
  x=[None]*45
  for j in free:x[j]=sp.Rational(round(res.x[j]*den),den)
  b0=sp.ones(13,1)-E[:,free]*sp.Matrix([x[j] for j in free])
  solved=E[:,piv].inv()*b0
  for j,t in zip(piv,solved):x[j]=t
  qrational=[[Fraction(0) for _ in range(9)]for _ in range(9)]
  for (i,j),t in zip(zip(*tri),x):qrational[i][j]=qrational[j][i]=Fraction(int(t.p),int(t.q))
  # Load only exact enumeration functions, avoiding unrelated original execution.
  ns={};src=(BASE/'k12_survivor_certificate.py').read_text().split('INTEGER_GRAM =')[0];exec(src,ns)
  try: sv,nodes,diag=ns['exact_short_vectors'](qrational,Fraction(1))
  except AssertionError:continue
  ss={canon(v)for v in sv}
  if ss==T and all(ns['gram_value'](qrational,v)==1 for v in target):
   out={'scope':'Exact positive-definite and complete-minimum candidate; boundary witness still to package','target':target.tolist(),'gram_rational':[[str(t)for t in row]for row in qrational],'short_vectors':[list(v)for v in sv],'nodes':nodes,'diagonal':[str(x)for x in diag],'minimum_pairs':len(T),'quadratic_rank':ns['matrix_rank'](eq.tolist())}
   (BASE/'k12_coface_tripod_candidate.json').write_text(json.dumps(out,indent=2)+'\n')
   print('EXACT CANDIDATE FOUND',nodes,'nodes',flush=True);raise SystemExit(0)
 print('rationalization failed',flush=True);break
