"""Finite Artinian-pair check of the nine primitive-rank cubic lattice types."""
from pathlib import Path
from itertools import product,combinations
from time import perf_counter
import numpy as np
import json
exec(Path('code/C_finish_modp2_Bockstein.py').read_text().split('def homology(')[0])
start=perf_counter();p=3

def key(B):
 R,_=rr(np.array(B,dtype=np.int64).T,p)
 rows=[tuple(int(x) for x in row) for row in R if any(row)]
 return tuple(rows)
def basis(K,n):return np.array(K,dtype=np.int64).reshape((-1,n)).T

def subspaces(n):
 ans={()}
 vectors=[v for v in product(range(p),repeat=n) if any(v)]
 for r in range(1,n+1):
  for piv in combinations(range(n),r):
   cells=[(i,j) for i in range(r) for j in range(n) if j not in piv and j>piv[i]]
   for values in product(range(p),repeat=len(cells)):
    B=np.zeros((r,n),dtype=np.int64)
    for i,j in enumerate(piv):B[i,j]=1
    for (i,j),x in zip(cells,values):B[i,j]=x
    ans.add(key(B.T))
 return sorted(ans,key=lambda z:(len(z),z))

def contained(A,B):return rank(np.column_stack((A,B)),p)==B.shape[1]
rows=[];totalorbits=indecomp=0
for size in (1,2,3):
 for support in combinations(range(3),size):
  subs=subspaces(size);alpha=np.diag([0,1,2])[list(support)][:,list(support)]
  pairs=[]
  for uk in subs:
   U=basis(uk,size)
   if any(not np.any(U[i]) for i in range(size)):continue
   for vk in subs:
    V=basis(vk,size)
    if not contained(U,V) or not contained(alpha@U%p,V):continue
    # Rank of all diagonal nil basis changes into Hom(U,E/V).
    # Here a nonzero target occurs only for the regular rank(1,1,1) pair.
    target=U.shape[1]*(size-V.shape[1])
    gauge=[]
    for i in range(size):
     H=np.zeros((size,size),dtype=np.int64);H[i,i]=1
     gauge.append((H@U).reshape(-1))
    # Quotient by maps with all columns in V.
    rel=[]
    for j in range(U.shape[1]):
     for h in range(V.shape[1]):
      Z=np.zeros_like(U);Z[:,j]=V[:,h];rel.append(Z.reshape(-1))
    base=np.column_stack(rel) if rel else np.zeros((size*U.shape[1],0),dtype=np.int64)
    allm=np.column_stack([base]+[v[:,None] for v in gauge])
    assert rank(allm,p)-rank(base,p)==target
    pairs.append((uk,vk))
  seen=set();orbits=[]
  for pair in pairs:
   if pair in seen:continue
   orb=set()
   for units in product((1,2),repeat=size):
    D=np.diag(units);orb.add((key(D@basis(pair[0],size)%p),key(D@basis(pair[1],size)%p)))
   seen|=orb;orbits.append(pair)
  primitive=[]
  for uk,vk in orbits:
   U,V=basis(uk,size),basis(vk,size)
   split=False
   for cutsize in range(1,size):
    for cut in combinations(range(size),cutsize):
     D=np.diag([int(i in cut) for i in range(size)])
     if contained(D@U,U) and contained(D@V,V):split=True
   if not split:primitive.append((uk,vk))
  totalorbits+=len(orbits);indecomp+=len(primitive)
  rows.append({'support':support,'admissible_pairs':len(pairs),'torus_orbits':len(orbits),
               'indecomposable_orbits':len(primitive),'primitive_pairs':primitive})
assert indecomp==9
# Full 27-element conductor quotient algebra in (F3[pi]/pi²)^3.
D=[np.array([a,a,a],dtype=np.int64) for a in range(3)]
R=[(v, np.array([b,b+c,b-c],dtype=np.int64)%3) for v in D for b,c in product(range(3),repeat=2)]
Rkeys={(tuple(a),tuple(b)) for a,b in R}
for a,b in R:
 for c,d in R:
  assert (tuple((a*c)%3),tuple((a*d+b*c)%3)) in Rkeys
report={'status':'PASS','scope':'All Artinian-pair subspaces with each normalization-branch rank at most1; all diagonal residue-unit orbits and nil-gauge graph-map ranks; exact9 indecomposable primitive-rank orbits, plus all729 products in the conductor quotient. Arbitrary-rank completeness is the written rejection/three-subspace proof.','runs':rows,'total_orbits':totalorbits,'indecomposable_orbits':indecomp,'conductor_quotient_products':len(R)**2,'runtime_seconds':round(perf_counter()-start,6)}
Path('logs/C_finish_C3_lattices.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
