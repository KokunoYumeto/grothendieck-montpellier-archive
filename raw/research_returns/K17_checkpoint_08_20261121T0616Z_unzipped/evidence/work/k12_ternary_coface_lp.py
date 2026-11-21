"""Discover fixed-reflection cofaces; save only exact rational minimum certificates."""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
from math import lcm
import json,numpy as np,sympy as sp
from scipy.optimize import linprog
ns={};exec(Path('work/k12_survivor_certificate.py').read_text().split('INTEGER_GRAM =')[0],ns)
forms=json.loads(Path('work/k12_ternary_glue_form_data.json').read_text());search=json.loads(Path('work/k12_ternary_coface_search.json').read_text())
tri=np.triu_indices(10);fac=np.where(tri[0]==tri[1],1,2)
def qr(v):
 v=np.asarray(v,dtype=np.int64);return v[...,tri[0]]*v[...,tri[1]]*fac
def canon(v):
 v=tuple(map(int,v));return v if next(x for x in v if x)>0 else tuple(-x for x in v)
def shorts(Q,bound):
 C=np.linalg.cholesky(Q).T;v=np.zeros(10,dtype=np.int64);out=[]
 def rec(i,budget):
  if i<0:
   if np.any(v):out.append(tuple(v))
   return
  shift=(C[i,i+1:]@v[i+1:])/C[i,i];radius=np.sqrt(max(0,budget))/C[i,i]
  for x in range(int(np.ceil(-shift-radius-1e-8)),int(np.floor(-shift+radius+1e-8))+1):
   v[i]=x;left=budget-(C[i,i]*(x+shift))**2
   if left>=-1e-8:rec(i-1,left)
 rec(9,bound);return out
out=[]
for f,s in zip(forms,search):
 W=np.asarray(f['minimum_vectors'],dtype=np.int64);Q0=np.asarray(f['integer_gram'],dtype=float)/f['gram_denominator'];initial=shorts(Q0,2.25);done=None;attempts=[]
 for ci,candidate in enumerate(s['candidates'][:40]):
  w=np.asarray(candidate['vector'],dtype=np.int64);target=np.vstack([W,w]);T={canon(v)for v in target};eq=qr(target)
  if np.linalg.matrix_rank(eq)!=14:continue
  E=np.c_[eq,np.zeros(14)];beq=np.ones(14);seen=set();vecs=[];pds=[]
  def add(v,pd=False):
   if not any(v):return
   v=canon(v)
   if not pd and v in T:return
   key=(v,pd)
   if key in seen:return
   seen.add(key);vecs.append(v);pds.append(pd)
  for v in initial:add(v)
  for i in range(10):
   v=[0]*10;v[i]=1;add(v)
  for i,j in combinations(range(10),2):
   for sign in [-1,1]:
    v=[0]*10;v[i]=1;v[j]=sign;add(v)
  status='iteration_limit'
  for it in range(80):
   A=np.c_[-qr(vecs),np.asarray([sum(x*x for x in v)if pd else 1 for v,pd in zip(vecs,pds)])]
   bb=np.asarray([0 if pd else -1 for pd in pds]);cost=np.r_[np.zeros(55),-1.]
   res=linprog(cost,A_ub=A,b_ub=bb,A_eq=E,b_eq=beq,bounds=[(None,None)]*55+[(0,1)],method='highs')
   if not res.success:status='infeasible';break
   eps=res.x[-1]
   if eps<1e-7:status='zero_margin';break
   Q=np.zeros((10,10));Q[tri]=res.x[:55];Q=Q+Q.T-np.diag(np.diag(Q));eig,U=np.linalg.eigh(Q)
   if eig[0]<1e-5:
    for j,t in enumerate(eig):
     if t<1e-5:add(np.rint(U[:,j]*100).astype(int),True)
    continue
   bad={canon(v)for v in shorts(Q,1+eps/4)}-T
   if bad:
    before=len(vecs)
    for v in bad:add(v)
    assert len(vecs)>before;continue
   EE=sp.Matrix(eq.tolist());piv=EE.rref()[1];free=[j for j in range(55)if j not in piv];inv=EE[:,piv].inv()
   for den in [3600,36000]:
    x=[None]*55
    for j in free:x[j]=sp.Rational(round(res.x[j]*den),den)
    sol=inv*(sp.ones(14,1)-EE[:,free]*sp.Matrix([x[j]for j in free]))
    for j,t in zip(piv,sol):x[j]=t
    q=[[F(0)for j in range(10)]for i in range(10)]
    for (i,j),t in zip(zip(*tri),x):q[i][j]=q[j][i]=F(int(t.p),int(t.q))
    try:sv,nodes,diag=ns['exact_short_vectors'](q,F(1))
    except AssertionError:continue
    if {canon(v)for v in sv}!=T:continue
    assert all(ns['gram_value'](q,v)==1 for v in target)
    d=lcm(*(t.denominator for row in q for t in row));H=[[int(t*d)for t in row]for row in q]
    done={'record':f['record'],'orbit':f['orbit'],'new_vector':w.tolist(),'minimum_vectors':target.tolist(),'integer_gram':H,'gram_denominator':d,'nodes':nodes,'quadratic_rank':ns['matrix_rank'](eq.tolist()),'facet_reflections':candidate['facet_reflections'],'relative_facets':[i for i,b in enumerate(f['gale_columns'])if not any(b)],'candidate_index':ci,'iterations':it}
    assert done['quadratic_rank']==14
    status='EXACT';break
   if done:break
   status='rationalization_failed';break
  attempts.append({'candidate':ci,'status':status})
  if done:break
 if done is None:done={'record':f['record'],'orbit':f['orbit'],'unfilled':True,'attempts':attempts}
 out.append(done);Path('work/k12_ternary_coface_exact_data.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in done.items()if k in('record','orbit','unfilled','nodes','gram_denominator','candidate_index','new_vector')}),flush=True)
