"""Exact F2 graph check for the three-theta, K=F3^2 boundary.

The proof is uniform and written separately. This finite supplement checks
the precise degree-three dimensions, heart span and vertex-star vector.
"""
from pathlib import Path
import datetime,json,time
started=time.perf_counter()
K=[(a,b) for a in range(3) for b in range(3)]
zero=(0,0)
def add(x,y):return tuple((a+b)%3 for a,b in zip(x,y))
def neg(x):return tuple(-a%3 for a in x)
def sub(x,y):return add(x,neg(y))
def typ(x):return min(x,neg(x))
H=sorted({typ(x) for x in K if x!=zero})
edges=[]
for i in range(3):
 for h in H:
  for e in range(2):edges.append(('loop',i,h,e))
for i,j in [(0,1),(0,2),(1,2)]:
 for g in K:
  for e in range(2):edges.append(('cross',i,j,g,e))
index={e:i for i,e in enumerate(edges)}
def rank(vs):
 p={}
 for v in vs:
  while v:
   k=v.bit_length()-1
   if k in p:v^=p[k]
   else:p[k]=v;break
 return len(p)
def xor(vs):
 v=0
 for x in vs:v^=x
 return v
stars=[]
for i in range(3):
 stars.append(xor(1<<j for j,e in enumerate(edges) if e[0]=='cross' and i in e[1:3]))
assert xor(stars)==0 and rank(stars)==2
assert len(edges)==78
all_hearts=[]; cases=[]; type_constants=None
for r0 in K:
 for r1 in K:
  r=(r0,r1,neg(add(r0,r1)))
  selected=[]
  groups={h:[] for h in H}
  for j,e in enumerate(edges):
   if e[0]=='loop':groups[e[2]].append(1<<j)
   else:
    _,i,k,g,_=e
    q=sub(g,sub(r[k],r[i]))
    if q==zero:selected.append(1<<j)
    else:groups[typ(q)].append(1<<j)
  assert len(selected)==6
  T=[v for h in H for v in groups[h]]
  assert len(T)==72 and rank(T+stars)-2==72
  hearts=[]
  for h in H:
   assert len(groups[h])==18
   hearts.extend(groups[h][0]^v for v in groups[h][1:])
  assert rank(hearts+stars)-2==68
  all_hearts.extend(hearts)
  cases.append({'r':r,'T_dimension':72,'heart_dimension':68})
  if r==(zero,zero,zero):
   type_constants=[xor(groups[h]) for h in H]
   w=xor(1<<j for j,e in enumerate(edges) if e[0]=='cross' and 0 in e[1:3] and e[3]!=zero)
   for h in H:assert sum(bool(w&v) for v in groups[h])==8
   q01=xor(1<<index[('cross',0,1,zero,e)] for e in range(2))
   q02=xor(1<<index[('cross',0,2,zero,e)] for e in range(2))
   assert q01^q02^w==stars[0]
assert rank(all_hearts+stars)-2==75

# Restriction of the four type constants to each selected triangle:
# pair coordinates already agree, so only the triangle sum remains.
constraints=[]
for row in cases:
 r=row['r']; functional=0
 for j,v in enumerate(type_constants):
  parity=0
  for i,k in [(0,1),(0,2),(1,2)]:
   parity^=bool(v&(1<<index[('cross',i,k,sub(r[k],r[i]),0)]))
  if parity:functional|=1<<j
 constraints.append(functional)
assert rank(constraints)==4

result={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'runtime_seconds':time.perf_counter()-started,'field':'F2','kernel':'F3^2',
 'edge_count':78,'vertex_coboundary_rank':2,'graph_dimension':76,
 'number_of_sum_zero_shifts':len(cases),'each_partial_normalization_kernel_dimension':72,
 'each_four_type_heart_dimension':68,'all_hearts_span_dimension':75,
 'type_constant_triangle_constraints_rank':4,
 'unselected_vertex_star_ones_per_type':8,'unselected_vertex_star_zeroes_per_type':10,
 'scope':'Finite degree-three graph supplement only; no geometric monodromy conclusion is inferred from this computation.'}
out = Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work/outputs/root_degree_three_theta_graph_checks.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
