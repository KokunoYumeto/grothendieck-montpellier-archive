#!/usr/bin/env python3
"""Exhaustive simultaneous-conjugacy test in the unique degree36 Hurwitz orbit."""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
ROOT=Path(__file__).resolve().parents[2];AG=ROOT/'work/agents/pentagon'
start=time.monotonic()
A,B=np.load(AG/'hurwitz_cubic216_order6_triple_9.npz')['generators'].astype(np.int16)
I=np.arange(36,dtype=np.int16);J=np.arange(9,dtype=np.int16)
mul=lambda a,b:a[b]
inv=lambda a:np.argsort(a).astype(np.int16)
x,y=A[A],B[B];D=A[B];S=A[B[A]]
assert np.array_equal(D[D[D]],I) and np.array_equal(S[S],I)
det=json.loads((AG/'cubic_detector_216.json').read_text())
def aff(a):
 return np.array([3*((a[0]*(v//3)+a[1]*(v%3)+a[2])%3)+(a[3]*(v//3)+a[4]*(v%3)+a[5])%3 for v in range(9)],dtype=np.int16)
tx,ty=aff(det['x']),aff(det['y'])
G=[(I,J)];lookup={I.tobytes():0}
for p,q in G:
 for a,b in [(x,tx),(y,ty)]:
  pp,qq=a[p],b[q];key=pp.tobytes()
  if key in lookup:assert np.array_equal(G[lookup[key]][1],qq)
  else:lookup[key]=len(G);G.append((pp,qq))
assert len(G)==1944
PG=PermutationGroup([Permutation(x.tolist()),Permutation(y.tolist())]);der=PG.derived_subgroup()
assert der.order()==648
ids=[lookup[np.array(p.array_form,dtype=np.int16).tobytes()] for p in der.generate_schreier_sims()]
label={aff(r['f_matrix']).tobytes():(r['rho'],r['a3']) for r in det['six_actual_gentle_residues']}
Dinv=inv(D);Sinv=inv(S);xi,yi=inv(x),inv(y);z=inv(x[y]);zi=inv(z)
assert np.array_equal(D[x[Dinv]],y) and np.array_equal(D[y[Dinv]],z)
assert np.array_equal(S[x[Sinv]],y) and np.array_equal(S[y[Sinv]],x)
def conjugators(old,new):
 answers=[]
 for dst in range(36):
  p=np.full(36,-1,dtype=np.int16);pre=np.full(36,-1,dtype=np.int16);p[0]=dst;pre[dst]=0;todo=[0];ok=True
  for v in todo:
   for a,b in zip(old,new):
    u,w=int(a[v]),int(b[p[v]])
    if p[u]>=0:
     if p[u]!=w:ok=False;break
    elif pre[w]>=0:ok=False;break
    else:p[u]=w;pre[w]=u;todo.append(u)
   if not ok:break
  if ok:
   assert len(todo)==36 and np.all(p>=0)
   assert all(np.array_equal(p[a],b[p])for a,b in zip(old,new))
   answers.append(p.tolist())
 return answers
rows=[]
for k in ids:
 f,t=G[k]
 if t.tobytes()not in label:continue
 fi=inv(f);f1=D[f[Dinv]];f2=D[f1[Dinv]]
 tests={
 'two_cycle':np.array_equal(S[f[Sinv]],fi),
 'three_cycle_1':np.array_equal(f2[f1[f]],I),
 'three_cycle_minus1':np.array_equal(f2[zi[f1[yi[f[xi]]]]],I)}
 bnew=fi[B[f]]
 cs=conjugators((A,B),(A,bnew))
 row={'group_index':k,'label':list(label[t.tobytes()]),'tests':tests,'simultaneous_conjugators':len(cs),'f':f.tolist()}
 if cs:row['conjugator_example']=cs[0]
 rows.append(row)
summary=[]
for rho in range(3):
 for bit in range(2):
  rr=[r for r in rows if r['label']==[rho,bit]]
  summary.append({'rho':rho,'a3':bit,'candidate_count':len(rr),'cycles_pass':sum(all(r['tests'].values())for r in rr),'conjugacy_pass':sum(r['simultaneous_conjugators']>0 for r in rr),'both_pass':sum(all(r['tests'].values())and r['simultaneous_conjugators']>0 for r in rr)})
out={'scope':'Unique degree36 Hurwitz orbit: finite necessary test; its fullGT kernel stability proved separately via Hurwitz functoriality.','pure_order':len(G),'derived_order':len(ids),'summary':summary,'candidates':rows,'elapsed_seconds':time.monotonic()-start}
(ROOT/'work/records/hurwitz36_gt_stability.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='candidates'},indent=2))
