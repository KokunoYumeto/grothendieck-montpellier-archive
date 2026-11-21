from pathlib import Path
import hashlib,json
import sympy as S

def mul(a,b,mod,degree):
 out=0
 for i in range(degree):
  if b>>i&1:out^=a<<i
 for j in range(2*degree-2,degree-1,-1):
  if out>>j&1:out^=mod<<(j-degree)
 return out

def count(degree,mod):
 q=1<<degree
 mm=lambda a,b:mul(a,b,mod,degree)
 def pp(a,n):
  out=1
  while n:
   if n&1:out=mm(out,a)
   a=mm(a,a);n//=2
  return out
 u=next(a for a in range(q) if mm(a,a)^a^1==0)
 u2=mm(u,u)
 pts=[]
 for x in range(q):
  if x in (0,1):continue
  rhs=x^mm(u,pp(x,q-2))^mm(u2,pp(x^1,q-2))
  for y in range(q):
   if mm(y,y)^y==rhs:pts.append([x,y])
 return dict(q=q,modulus=mod,u=u,N=len(pts)+3,affine_unramified_points=pts)
counts=[count(2,7),count(4,19)]
assert [c['N'] for c in counts]==[3,15]
x,t=S.symbols('x t');P=x**4-2*x**3+x*x-8*x+16
H1=4*t**4+7*t**3+10*t*t+7*t+4;H2=16*t**4-8*t**3+t*t-8*t+16
res=S.resultant(P,S.expand(P.subs(x,t*x)),x)
assert S.expand(res-256*(t-1)**4*H1**2*H2)==0
for H,v in [(P,x),(H1,t),(H2,t)]:
 assert S.Poly(H,v,modulus=3).is_irreducible
 assert S.Poly(H,v).is_irreducible
assert S.expand(x*x*((x+4/x)**2-2*(x+4/x)-7)-P)==0
out=dict(counts=counts,P=str(P),ratio_resultant=str(S.factor(res)),real_quadratic='s^2-2s-7, discriminant32, fieldQ(sqrt2)',mod3_irreducible=True,scope='Independent direct point enumeration plus SymPy integer resultant and mod3 irreducibility; endomorphism conclusion requires the separate written Tate-centralizer argument.',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='counts'},indent=2))
