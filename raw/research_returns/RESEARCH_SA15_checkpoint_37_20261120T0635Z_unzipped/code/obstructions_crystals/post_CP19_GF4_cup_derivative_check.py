#!/usr/bin/env python3
"""Independent dual-number evaluation of the candidate derivative identity.
Actual bilinear Cartier products are evaluated over GF4[epsilon]/epsilon^2;
no differentiated projection formula is used for the left hand side.
"""
from pathlib import Path
from time import perf_counter
import ast,json
started=perf_counter()
p=Path(__file__).with_name('post_CP19_GF4_canonical_variation_probe.py')
nodes=[]
for z in ast.parse(p.read_text()).body:
 if isinstance(z,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='rng' for x in z.targets):break
 if isinstance(z,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='started' for x in z.targets):continue
 nodes.append(z)
ns={'__file__':str(p.resolve())};exec(compile(ast.Module(body=nodes,type_ignores=[]),str(p),'exec'),ns)
for k in ['mul','sq','N','B','add','scale','dot','action','echelon','solver','smallco','bigco','pull','trace','sp','st','mat','rootv','toral']:globals()[k]=ns[k]
def dm(x,y):
 a,b=x&3,x>>2;c,d=y&3,y>>2
 return mul[a][c] | ((mul[a][d]^mul[b][c])<<2)
def ds(v,c):return [dm(x,c) for x in v]
def da(cols,v):
 z=[0]*len(cols[0])
 for c,k in zip(cols,v):
  if k:z=add(z,ds(c,k))
 return z
def dmat(s,co,n):
 out=[[0]*n for _ in range(n)]
 for a,m in zip(s,co):
  if a:out=[add(c,ds(d,a)) for c,d in zip(out,m)]
 return out
def dsolve(cols,v):
 # Unit-pivot elimination over the actual dual-number ring.
 n=len(cols);a=[[cols[j][i] for j in range(n)]+[v[i]] for i in range(n)]
 for j in range(n):
  h=next(i for i in range(j,n) if a[i][j]&3)
  a[j],a[h]=a[h],a[j];x=a[j][j];aa=x&3;bb=x>>2
  inv=sq(aa) | (mul[bb][aa]<<2) # inverse a^-1 + eps*b*a^-2; a^-2=a in GF4
  a[j]=ds(a[j],inv)
  assert a[j][j]==1
  for i in range(n):
   if i!=j and a[i][j]:a[i]=add(a[i],ds(a[j],a[i][j]))
 return [a[i][-1] for i in range(n)]
def split_dsolve_f2(solve,v):
 a=solve([x&3 for x in v]);b=solve([x>>2 for x in v])
 return [x|(y<<2) for x,y in zip(a,b)]
old=json.loads(p.with_suffix('.output.json').read_text())
checks=[]
for rec in old['records']:
 s=rec['source_coefficients'];u=rootv(s);ui=action(toral,u);rr=[add(u,ui),ui];R=[rootv(r) for r in rr]
 Mu=mat(u,smallco,N);ix=echelon(Mu)
 for j in range(N):
  v=[int(h==j) for h in range(N)];ud=[x|(y<<2) for x,y in zip(u,v)]
  ud1=da(toral,ud);rd=[add(ud,ud1),ud1]
  Mud=dmat(ud,smallco,N);base=R+[Mud[h] for h in ix]
  MA=dmat(da(pull,ud),bigco,B)
  Ac=[]
  for ri in rd:
   qi=split_dsolve_f2(st,ri)
   hu=split_dsolve_f2(sp,da(MA,qi))
   Ac.append(dsolve(base,hu)[:2])
  derivative=[x>>2 for col in Ac for x in col]
  target=st(v) # v^2=v for the coordinate directions used here
  D=[0]*4
  for c,m in zip(target,rec['all_variations']):
   if c:D=add(D,scale(m,c))
  expected=rootv(D)
  assert derivative==expected,(rec['trial'],j,derivative,expected)
  checks.append({'source_trial':rec['trial'],'root_coordinate_direction':j,'derivative':derivative,'root_variation':expected})
out={'status':'PASS','scope':'Exact dual-number check of the typed derivative identity at twelve GF4 product sources; no arbitrary-surface trace or determinant conclusion.','field':'GF4[epsilon]/epsilon^2','cases':len(checks),'records':checks,'elapsed_seconds':perf_counter()-started}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
