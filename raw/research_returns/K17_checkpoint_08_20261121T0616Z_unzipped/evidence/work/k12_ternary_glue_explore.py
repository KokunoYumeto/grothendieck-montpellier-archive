"""Finite discovery check for index-three ambient glue, rank-ten excess three.

Published five Delta=1 rank-three polytope classes are a coverage input.
This exploratory script searches exact signed integral symmetries and the
Watson support obstruction; it does not test positivity of remaining cases.
"""
from itertools import product, combinations, permutations
from pathlib import Path
import ast,json,time

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def canon(v):
 v=tuple(v)
 return v if next(x for x in v if x)>0 else tuple(-x for x in v)
def mv(A,v):return tuple(dot(r,v)for r in A)
def parity(p):return sum(p[i]>p[j]for i in range(len(p))for j in range(i+1,len(p)))%2

MASKS=tuple(range(1,8));COLORS={m:tuple(c for c in range(3)if m>>c&1)for m in MASKS}
SHIFT={(m,t):sum(1<<((c+t)%3)for c in COLORS[m])for m in MASKS for t in range(3)}
SIGN={(m,e):sum(1<<((e*c)%3)for c in COLORS[m])for m in MASKS for e in [-1,1]}

def autos(B):
 pivot=next(p for p in combinations(range(len(B)),3)if abs(det(*(B[i]for i in p)))==1)
 a,b,c=(B[i]for i in pivot);D=det(a,b,c)
 inv=tuple(tuple(x//D for x in r)for r in (cross(b,c),cross(c,a),cross(a,b)))
 signed=B+[tuple(-x for x in b)for b in B];lookup={b:i for i,b in enumerate(B)}
 found={}
 for im in permutations(signed,3):
  if abs(det(*im))!=1:continue
  A=tuple(tuple(sum(im[k][i]*inv[k][j]for k in range(3))for j in range(3))for i in range(3))
  images=[mv(A,b)for b in B]
  if not all(canon(v)in lookup for v in images):continue
  perm=tuple(lookup[canon(v)]for v in images)
  signs=tuple(1 if v==canon(v)else -1 for v in images)
  found[A]=(perm,signs)
 return [(A,*v)for A,v in found.items()]

def odd_witness(state,B,group,shifts):
 sizes=[m.bit_count()for m in state];offset=[0]
 for n in sizes:offset.append(offset[-1]+n)
 for A,perm,signs in group:
  if any(sizes[j]!=sizes[perm[j]]for j in range(len(B))):continue
  signed=tuple(SIGN[state[j],signs[j]]for j in range(len(B)))
  for lam,values in shifts:
   if any(signed[j]!=SHIFT[state[perm[j]],values[perm[j]]]for j in range(len(B))):continue
   p=[]
   for j,m in enumerate(state):
    dest=perm[j];values_dest=COLORS[state[dest]]
    p.extend(offset[dest]+values_dest.index((signs[j]*c-values[dest])%3)for c in COLORS[m])
   if parity(p):return {'matrix':A,'lambda':lam,'permutation':p}
 return None

def support_witness(state,zweight,shifts):
 n=sum(m.bit_count()for m in state)
 for lam,values in shifts:
  w=n-sum(bool(SHIFT[m,t]&1)for m,t in zip(state,values))+zweight
  if w<=6:return {'lambda':lam,'support':w}
 return None

records=ast.literal_eval(Path('work/k12_source_data/delta_dim_3_delta_1.txt').read_text())
out=[];start=time.monotonic()
for index,vertices in enumerate(records):
 B=sorted(set(canon(v)for v in vertices));assert max(abs(det(*x))for x in combinations(B,3))==1
 group=autos(B);shifts=[(lam,tuple(dot(lam,b)%3 for b in B))for lam in product(range(3),repeat=3)]
 counts={'total':0,'odd':0,'support_impossible':0,'survivors':0};survivors=[]
 for state in product(MASKS,repeat=len(B)):
  n=sum(m.bit_count()for m in state);z=13-n
  if z not in (0,1,2):continue
  zero_weights=(0,)if z==0 else(0,1)if z==1 else(1,)
  # The symmetry test is independent of a normalized zero-column color.
  witness=odd_witness(state,B,group,shifts)
  for zw in zero_weights:
   counts['total']+=1
   if witness:counts['odd']+=1;continue
   sw=support_witness(state,zw,shifts)
   if sw:counts['support_impossible']+=1;continue
   counts['survivors']+=1;survivors.append({'state':state,'zero_count':z,'zero_weight':zw})
 item={'record':index+1,'B':B,'automorphism_count':len(group),'counts':counts,'survivors':survivors}
 out.append(item);print(json.dumps({k:v for k,v in item.items()if k not in('survivors','B')}),flush=True)
Path('work/k12_ternary_glue_explore.json').write_text(json.dumps({'records':out,'seconds':time.monotonic()-start,'coverage':'Published five Delta1 rank3 polytopes; symmetry/Watson checks only.'},indent=2)+'\n')
