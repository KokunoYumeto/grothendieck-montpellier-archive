#!/usr/bin/env python3
"""Exact candidate character, line-Ext graph, and brick-matrix edge capacities.
The construction proof, not this script alone, is required for the actual
extension object and its endomorphism algebra. Semiregularity is not claimed.
"""
from pathlib import Path
from math import comb,ceil,lcm
from functools import reduce
import json,time
import sympy as s
start=time.perf_counter();root=Path(__file__).resolve().parent;u=s.sqrt(2)
j=json.loads((root/'rm_two_slope_exact_input.json').read_text())
weights={}
for item in j['exact_support']:
 a,b,c,d=item['rep'];w=s.Rational(item['orbit_total_weight'])
 orbit=set([(a,b,c,d),(a,-b,c,-d),(a,b,-c,-d),(a,-b,-c,d)])
 for z in orbit:weights[z]=weights.get(z,0)+w/len(orbit)
def lam(v):
 a,b,c,d=v
 return [a+b*u+c+d*u,a+b*u-c-d*u,a-b*u+c-d*u,a-b*u-c+d*u]
def char(v):
 x=lam(v)
 return s.Matrix([s.expand(s.prod(x[k] for k in range(4) if mask>>k&1)) for mask in range(16)])
vq=s.zeros(16,1);vq[0]=1;vq[3]=vq[12]=-s.Rational(1,2);vq[15]=s.Rational(1,4)
G=2*char((10,0,0,0))-2*char((2,0,0,0))+char((-2,0,0,0))
assert all(s.expand(z)==0 for z in G+sum((w*char(v) for v,w in weights.items()),s.zeros(16,1))-32*vq)
assert sum(w for v,w in weights.items() if v[0]==14)==15
assert sum(w for v,w in weights.items() if v[0]==-14)==16
assert all(w>0 for w in weights.values())
r=reduce(lcm,(int(w.q) for w in weights.values()),1)
A=[{'name':'G','divisor':None,'weight':s.Integer(1),'multiplicity':r}]
B=[]
for v,w in sorted(weights.items()):
 item={'name':str(v),'divisor':v,'weight':w,'multiplicity':int(r*w)}
 (A if v[0]==14 else B).append(item)
def line_h1(v):
 a,b,c,d=v;idx=0;ker=0;chi=1
 for x,y in [(a+c,b+d),(a-c,b-d)]:
  if x==0 and y==0:ker+=2;continue
  det=x*x-2*y*y;assert det
  idx+=1 if det<0 else (0 if x>0 else 2);chi*=abs(det)
 return chi*comb(ker,1-idx) if 0<=1-idx<=ker else 0
def unit_ext_lower(v):
 eig=[14-x for x in lam(v)];dims=[]
 for shift in (4,12,16):
  vals=[x-shift for x in eig]
  if any(x==0 for x in vals):return 0
  if sum(bool(x<0) for x in vals)!=1:return 0
  dims.append(int(s.simplify(-s.prod(vals))))
 return max(0,2*dims[0]-2*dims[1])
# Cross Ext3 vanishing: line targets have index at most2; unit targets
# have H3(A-D)=0 and H4(A-3D)=0, hence H3(F tensor A)=0.
ext3_line_checks=[];ext3_unit_checks=[]
for a in A[1:]:
 for b in B:
  aa,bb,cc,dd=[x-y for x,y in zip(a['divisor'],b['divisor'])]
  idx=0
  for xx,yy in [(aa+cc,bb+dd),(aa-cc,bb-dd)]:
   det=xx*xx-2*yy*yy;assert det!=0
   idx+=1 if det<0 else (0 if xx>0 else 2)
  assert idx<=2
  ext3_line_checks.append(idx)
for b in B:
 vals=[10-z for z in lam(b['divisor'])]
 assert all(z!=0 for z in vals)
 idx=sum(bool(z<0) for z in vals);assert idx<=2
 # The other possible total-degree3 term is H4(A-3D); its first
 # Chern class has positive theta-degree (scalar coefficient16).
 ext3_unit_checks.append({'divisor':b['divisor'],'H3_first_term_index':idx,'H4_middle_term_theta_coefficient':16})
edges=[];adj={i:[] for i in range(len(A)+len(B))}
for ai,a in enumerate(A):
 for bi,b in enumerate(B):
  cap=unit_ext_lower(b['divisor']) if ai==0 else line_h1(tuple(x-y for x,y in zip(a['divisor'],b['divisor'])))
  need=int(ceil(max(a['weight']/b['weight'],b['weight']/a['weight'])))+2
  if cap>=need:
   e={'A':ai,'B':bi,'Ext1_dimension_or_lower_bound':cap,'matrix_arrows_needed':need}
   edges.append(e);adj[ai].append(len(A)+bi);adj[len(A)+bi].append(ai)
seen={0};queue=[0];tree=[]
while queue:
 v=queue.pop(0)
 for w in adj[v]:
  if w not in seen:
   seen.add(w);queue.append(w)
   ai=v if v<len(A) else w;bi=(w if w>=len(A) else v)-len(A)
   tree.append(next(e for e in edges if e['A']==ai and e['B']==bi))
connected=len(seen)==len(adj)
def serial(z):return {'name':z['name'],'divisor':z['divisor'],'weight':str(z['weight']),'multiplicity':z['multiplicity']}
out={'result':'PASS_CHARACTER_AND_CONNECTED_CAPACITY' if connected else 'PASS_CHARACTER_BUT_DISCONNECTED',
     'defect_rank':r,'total_rank':32*r,'A':[serial(z) for z in A],'B':[serial(z) for z in B],
     'all_weights_positive':True,'full16_coordinate_identity':True,'all_cross_Ext3_vanish':True,'cross_line_index_histogram':{str(k):ext3_line_checks.count(k) for k in range(3)},'cross_unit_checks':ext3_unit_checks,'qualified_edge_count':len(edges),
     'connected_vertex_count':len(seen),'total_vertex_count':len(adj),'spanning_tree':tree,
     'all_qualified_edges':edges,'runtime_seconds':time.perf_counter()-start,
     'limits':'The tree certifies sufficient dimensions for explicit rectangular injection/projection and Jordan-pair matrices. It does not by itself assert any Yoneda/formality statement or weak semiregularity.'}
(root/'rm_two_slope_coupling_certificate_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['result','defect_rank','total_rank','qualified_edge_count','connected_vertex_count','total_vertex_count','spanning_tree','runtime_seconds']},indent=2))
