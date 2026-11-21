"""Exact exploratory Hecke matrices on the proposed S13(Gamma0(3),chi-3) model.
Coverage and modular-form identities are separate proof obligations.
"""
from pathlib import Path
import math,json
import sympy as sp

N=55
def mul(a,b):
 c=[0]*(N+1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b[:N+1-i]):
    if y:c[i+j]+=x*y
 return c
def power(a,k):
 c=[1]+[0]*N
 while k:
  if k&1:c=mul(c,a)
  a=mul(a,a);k//=2
 return c
def eta_product(exponents,shift):
 a=[0]*shift+[1]+[0]*(N-shift)
 for scale,exponent in exponents:
  for t in range(scale,N+1,scale):
   b=[0]*(N+1)
   for k in range(N//t+1):
    if exponent>=0:
     if k>exponent:break
     v=(-1)**k*math.comb(exponent,k)
    else:v=math.comb(-exponent+k-1,k)
    b[k*t]=v
   a=mul(a,b)
 return a
def chi(d):return 0 if d%3==0 else (1 if d%3==1 else -1)
a=[1]+[6*sum(chi(d) for d in range(1,n+1) if n%d==0) for n in range(1,N+1)]
b=eta_product([(3,9),(1,-3)],1)
D=eta_product([(1,6),(3,6)],1)
basis=[mul(D,power(a,7)),mul(D,mul(power(a,4),b)),mul(D,mul(a,power(b,2)))]
leading=sp.Matrix([[f[n] for f in basis] for n in [1,2,3]])
assert leading.det()==1
results=[]
X=sp.Symbol('X')
u=json.loads((Path(__file__).resolve().parent/'u3_weight5_exact_exploration.json').read_text())
for p in [7,13]:
 cols=[]
 for f in basis:
  c=leading.inv()*sp.Matrix([f[p*n] for n in [1,2,3]])
  assert all(v.q==1 for v in c)
  # Check all independently available additional coefficients.
  for n in range(1,N//p+1):
   lhs=f[p*n]+(chi(p)*p**12*f[n//p] if n%p==0 else 0)
   assert lhs==sum(c[j]*basis[j][n] for j in range(3)),(p,n,lhs)
  cols.append(c)
 T=sp.Matrix.hstack(*cols)
 P=T.charpoly(X).as_poly()
 value=int(P.eval(p**12+1))
 ru=next(z for z in u['results'] if z['p']==p)
 total=value*ru['evaluation_difference']
 r={'p':p,'matrix':[[int(v) for v in row] for row in T.tolist()],'charpoly':str(P.as_expr()),'charpoly_coefficients':[int(v) for v in P.all_coeffs()],'evaluation_point':p**12+1,'evaluation':value,'combined_evaluation':total,'factorization':{str(k):int(v) for k,v in sp.factorint(abs(total)).items()}}
 results.append(r);print(r,flush=True)
g=math.gcd(*(r['combined_evaluation'] for r in results))
result={'status':'EXPLORATORY coverage not proved','weight':13,'level':3,'character':'chi_minus3','series_precision':N,'basis_first_terms':[f[:16] for f in basis],'results':results,'combined_gcd':g,'gcd_factorization':{str(k):int(v) for k,v in sp.factorint(g).items()}}
(Path(__file__).resolve().parent/'gl2_weight13_exact_exploration.json').write_text(json.dumps(result,indent=2))
print('COMBINED GCD',g,sp.factorint(g))
