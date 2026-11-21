from itertools import product
from functools import lru_cache

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
 a,b=x;c,d=y
 return (a*c-b*d,a*d+b*c-b*d)
def conj(x):return (x[0]-x[1],-x[1])
def norm(x):return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
def tr(x):return 2*x[0]-x[1]
Z=(0,0)
U=[(a,b) for a in range(-2,3) for b in range(-2,3) if norm((a,b))==1]
S3=[(a,b) for a in range(-3,4) for b in range(-3,4) if norm((a,b))==3]
E6=[(a,b) for a in range(-3,4) for b in range(-3,4) if norm((a,b))<=6]

def psd(H):
 a,b,c,x,y,z=H
 if min(a,b,c)<0:return False
 if a*b<norm(x) or a*c<norm(y) or b*c<norm(z):return False
 return a*b*c-a*norm(z)-b*norm(y)-c*norm(x)+tr(mul(mul(x,z),conj(y)))>=0

def gram(v):return (norm(v[0]),norm(v[1]),norm(v[2]),mul(v[0],conj(v[1])),mul(v[0],conj(v[2])),mul(v[1],conj(v[2])))
def diff(H,G):return tuple(H[i]-G[i] if i<3 else sub(H[i],G[i]) for i in range(6))
rows=set()
for v in product([Z]+U+S3,[Z]+U,[Z]+U):
 if v==(Z,Z,Z):continue
 rows.add(gram(v))
rows=sorted(rows,key=lambda H:(-sum(H[:3]),H))
print('row Gram candidates',len(rows),flush=True)
@lru_cache(None)
def decomp(H):
 if H[:3]==(0,0,0):return ()
 for G in rows:
  if any(G[i]>H[i] for i in range(3)):continue
  M=diff(H,G)
  if psd(M):
   ans=decomp(M)
   if ans is not None:return (G,)+ans
 return None
for diag in [(2,2,2),(3,2,2)]:
 counts=[0,0];bad=[]
 for x,y,z in product(E6,E6,E6):
  H=diag+(x,y,z)
  if not psd(H):continue
  counts[0]+=1
  D=decomp(H)
  if D is None:bad.append(H)
  else:counts[1]+=1
 print('diag',diag,'psd',counts[0],'decomposable',counts[1],'bad',len(bad),'cache',decomp.cache_info(),flush=True)
 print('bad examples',bad[:20],flush=True)
