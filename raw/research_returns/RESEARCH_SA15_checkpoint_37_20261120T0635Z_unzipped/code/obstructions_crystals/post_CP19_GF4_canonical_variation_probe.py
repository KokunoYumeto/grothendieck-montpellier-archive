#!/usr/bin/env python3
"""Typed semilinear GF4 diagnostic. No general symmetry theorem is inferred."""
from pathlib import Path
import ast,json,random
from time import perf_counter
started=perf_counter()
p=Path(__file__).with_name('post_CP19_canonical_cup_variation_probe.py')
nodes=[]
for node in ast.parse(p.read_text()).body:
 if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='records' for t in node.targets):break
 if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='started' for t in node.targets):continue
 nodes.append(node)
ns={'__file__':str(p.resolve())};exec(compile(ast.Module(body=nodes,type_ignores=[]),str(p),'exec'),ns)
N=18;B=36
mul=[[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]]
sq=lambda a:mul[a][a]
def vec(bits,n):return [(bits>>j)&1 for j in range(n)]
def add(a,b):return [x^y for x,y in zip(a,b)]
def scale(a,c):return [mul[c][x] for x in a]
def dot(a,b):
 z=0
 for x,y in zip(a,b):z^=mul[x][y]
 return z
def action(cols,v):
 z=[0]*len(cols[0])
 for col,c in zip(cols,v):
  if c:z=add(z,scale(col,c))
 return z
def echelon(cols):
 piv={};indices=[]
 for j,c in enumerate(cols):
  v=c[:]
  for r in sorted(piv):
   if v[r]:v=add(v,scale(piv[r],v[r]))
  q=next((i for i,x in enumerate(v) if x),None)
  if q is not None:
   v=scale(v,sq(v[q]));piv[q]=v;indices.append(j)
 return indices
rank=lambda cols:len(echelon(cols))
def solver(cols):
 piv={}
 for j,c in enumerate(cols):
  v=c[:];q=[0]*len(cols);q[j]=1
  for r in sorted(piv):
   if v[r]:
    a=v[r];v=add(v,scale(piv[r][0],a));q=add(q,scale(piv[r][1],a))
  r=next((i for i,x in enumerate(v) if x),None)
  if r is not None:
   a=sq(v[r]);piv[r]=(scale(v,a),scale(q,a))
 def solve(v):
  v=v[:];q=[0]*len(cols)
  for r in sorted(piv):
   if v[r]:
    a=v[r];v=add(v,scale(piv[r][0],a));q=add(q,scale(piv[r][1],a))
  if any(v):raise ValueError('outside column image')
  return q
 return solve

def nullspace(rows,n):
 # kernel of the row matrix, via homogeneous reduction
 a=[r[:] for r in rows];piv=[];r=0
 for j in range(n):
  z=next((h for h in range(r,len(a)) if a[h][j]),None)
  if z is None:continue
  a[r],a[z]=a[z],a[r];a[r]=scale(a[r],sq(a[r][j]))
  for h in range(len(a)):
   if h!=r and a[h][j]:a[h]=add(a[h],scale(a[r],a[h][j]))
  piv.append(j);r+=1
 out=[]
 for j in range(n):
  if j in piv:continue
  v=[0]*n;v[j]=1
  for h,k in enumerate(piv):v[k]=a[h][j]
  out.append(v)
 return out
smallco=[[vec(c,N) for c in row] for row in ns['smallcoeff']]
bigco=[[vec(c,B) for c in row] for row in ns['ns']['coefficients']]
pull=[vec(c,B) for c in ns['pull']];trace=[vec(c,N) for c in ns['trace']]
sp=solver(pull);st=solver(trace)
def mat(s,co,n):
 out=[[0]*n for _ in range(n)]
 for a,m in zip(s,co):
  if a:out=[add(c,scale(d,a)) for c,d in zip(out,m)]
 return out

def rootv(x):return [sq(a) for a in x]
def det(v):return mul[v[0]][v[3]]^mul[v[1]][v[2]]
toral=[vec(ns['smalltoral'](1<<j),N) for j in range(N)]
rng=random.Random(202611191734);records=[]
for trial in range(100):
 s=[rng.randrange(4) for _ in range(N)];M=mat(s,smallco,N)
 ix=echelon(M)
 if len(ix)!=N-2:continue
 R1=action(toral,s);R=[add(s,R1),R1]
 im=[rootv(M[j]) for j in ix]
 if rank(R+im)!=N:continue
 proj=solver(R+im)
 K=[[proj([int(j==h) for j in range(N)])[i] for h in range(N)] for i in range(2)]
 assert all(dot(K[i],R[j])==int(i==j) for i in range(2) for j in range(2))
 assert all(dot(k,c)==0 for k in K for c in im)
 PK=[[dot(k,tr) for tr in trace] for k in K]
 S=action(pull,s);MA=mat(S,bigco,B)
 q=[st(r) for r in R];vi=[sp(rootv(action(MA,x))) for x in q]
 alpha=[proj(x)[:2] for x in vi];corrected=[];sm=solver(M)
 for x,y,ar in zip(q,vi,alpha):
  z=add(y,action(R,ar));w=sm(rootv(z));corrected.append(add(x,action(pull,w)))
 assert all(action(trace,x)==r for x,r in zip(corrected,R))
 assert all(rootv(action(MA,x))==action(pull,action(R,ar)) for x,ar in zip(corrected,alpha))
 variations=[]
 for Mt in bigco:
  # Linearized coherent domain uses squares of actual semilinear kernel vectors.
  cols=[[dot(rootv(k),action(Mt,qj)) for k in PK] for qj in corrected]
  variations.append(cols[0]+cols[1])
 annih=nullspace(variations,4)
 combos=[[0]*4]
 for a in annih:combos=[add(x,scale(a,c)) for x in combos for c in range(4)]
 records.append({'trial':trial,'source_coefficients':s,'alpha_cup_root_columns':alpha,'variation_dimension':rank(variations),'annihilator_basis':annih,'annihilator_has_invertible':any(det(x)!=0 for x in combos),'all_trace_zero':all(x[0]==x[3] for x in variations),'all_variations':variations})
 if len(records)>=12:break
out={'status':'COMPLETED_TYPED_FINITE_DIAGNOSTIC','scope':'GF4 semilinear kernel, actual Cartier square root and linearized first variation; no universal conclusion','field_polynomial':'t^2+t+1','records':records,'elapsed_seconds':perf_counter()-started}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'samples':len(records),'dims':[r['variation_dimension'] for r in records],'trace_zero':[r['all_trace_zero'] for r in records],'invertible_annihilator':[r['annihilator_has_invertible'] for r in records],'annihilators':[r['annihilator_basis'] for r in records],'elapsed_seconds':out['elapsed_seconds']},indent=2))
