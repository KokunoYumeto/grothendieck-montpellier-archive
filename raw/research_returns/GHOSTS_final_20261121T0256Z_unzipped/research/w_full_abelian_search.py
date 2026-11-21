"""Exact finite abelian-cycle catalog. Geometry needed for exhaustiveness is separate."""
from pathlib import Path
source=(Path(__file__).resolve().parent/'t0_search.py').read_text().split('extra={}')[0]
exec(source)
def bar(q):return q[0]-q[1],-q[1]
def surface_z(h,inputs):
 M=[None]*4;M[inputs[0]]=((1,0),(0,0));M[inputs[1]]=((0,0),(1,0))
 for row,k in enumerate([j for j in range(4) if j not in inputs]):M[k]=(h[2*row],h[2*row+1])
 p12=det(M[0]+M[1]);p34=det(M[2]+M[3])
 return km(p12,bar(p34))
entries=[q for q in product(range(-2,3),repeat=2) if norm(q)<=5]
zeros={}
small_h=[]
for h in product(entries,repeat=4):
 T=sum(map(norm,h))
 if T>6:continue
 D=2*(1+T+norm(det(h)))
 if D<=14:small_h.append((D,h))
for inputs in combinations(range(4),2):
 for D,h in small_h:
  if surface_z(h,inputs)==(0,0):zeros[graph(h,inputs)]=(D,('coordinate_graph',inputs,h))
# Primitive two-minor exceptions: E_i x image(E -> E_j x E_k), norms3,4.
norm3=[q for q in product(range(-2,3),repeat=2) if norm(q)==3]
norm4=[q for q in product(range(-2,3),repeat=2) if norm(q)==4]
for free in range(4):
 for j,k in combinations([i for i in range(4) if i!=free],2):
  fixed=next(i for i in range(4) if i not in (free,j,k))
  for aa,bb in product(norm3,norm4):
   for a,b in ((aa,bb),(bb,aa)):
    bu,bv=cmforms(b,j);au,av=cmforms(a,k)
    curve=wedge(add(bu,scale(-1,au)),add(bv,scale(-1,av)))
    cl=wedge(curve,wedge(form(2*fixed),form(2*fixed+1)))
    vv=tuple(cl.get(x,0) for x in basis)
    zeros[vv]=(14,('two_minor',free,j,k,a,b))
print('Zero-Weil abelian surface counts:',Counter(x[0] for x in zeros.values()),flush=True)
weights=[1001**i for i in range(70)]
def encode(v):return sum(a*w for a,w in zip(v,weights))
maxcoeff=max(abs(x) for v in zeros for x in v)
print('Max zero surface coefficient:',maxcoeff,flush=True)
assert 2*11*maxcoeff+20<1000
groups={d:sorted({encode(v) for v,(D,_) in zeros.items() if D==2*d}) for d in range(1,8)}
dp={0:{0},**{d:set() for d in range(1,8)}}
for d in range(1,8):
 sums={0:{0}}
 for k in range(1,7//d+1):
  sums[k]={sum(xs) for xs in combinations_with_replacement(groups[d],k)}
 old=dp
 dp={n:set(old[n]) for n in range(8)}
 for n in range(1,8):
  for k in range(1,n//d+1):
   dp[n].update(a+b for a in old[n-k*d] for b in sums[k])
 print('After generator degree',2*d,'zero cycle counts:',[len(dp[n]) for n in range(8)],flush=True)
# Save only the finite catalog arithmetic for later search; there is no negative theorem here.
import pickle
with open(Path(__file__).with_suffix('.catalog'),'wb') as ff:pickle.dump((zeros,dp,weights),ff,protocol=5)
