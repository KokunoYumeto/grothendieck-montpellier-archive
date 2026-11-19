"""Further exact checks identified during final claim-by-claim review."""
from fractions import Fraction as F
from itertools import permutations,combinations
from collections import defaultdict
from pathlib import Path
import json

out={}
def det(A):
 n=len(A);s=F(0)
 for p in permutations(range(n)):
  x=F((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))
  for i in range(n):x*=A[i][p[i]]
  s+=x
 return s
def inv(A):
 n=len(A);d=det(A);assert d
 return [[F((-1)**(i+j))*det([[A[r][c] for c in range(n) if c!=i] for r in range(n) if r!=j])/d for j in range(n)] for i in range(n)]
def mv(A,v):return [sum(x*y for x,y in zip(row,v)) for row in A]
def normalize(v):
 q=next(x for x in v if x)
 return [x/q for x in v]

A=[[F(x) for x in row] for row in [[1,2,3],[0,1,4],[5,6,0]]]
assert det(A)==1
a=F(7,3);b=F(-5,2)
normal=[[F(1),F(0),F(0)],[F(0),F(1),F(0)],[F(0),F(0),F(1)],[F(1),F(1),a],[b,F(1),F(1)]]
scales=[F(2),F(3),F(-4),F(5),F(7)]
points=[[z*s for z in mv(A,p)] for p,s in zip(normal,scales)]
B=[[points[j][i] for j in range(3)] for i in range(3)]
Binv=inv(B);u=mv(Binv,points[3]);v=mv(Binv,points[4])
t=[u[0],u[1],u[1]*v[2]/v[1]]
C=[[B[i][j]*t[j] for j in range(3)] for i in range(3)]
recovered=[normalize(mv(inv(C),p)) for p in points]
assert all(normalize(r)==normalize(p) for r,p in zip(recovered,normal))
assert u[2]*v[1]/(u[1]*v[2])==a
assert v[0]*u[1]/(u[0]*v[1])==b
out['GIT_chart_inverse']={'matrix':A,'independent_projective_scales':scales,'a':a,'b':b,'recovered_normal_forms':recovered,'claim':'Explicit two-sided normalization on the n=2,nu=2 unit chart. The tree proof establishes the general ring-valued chart.'}

# Generic polynomial difference identity used for each coordinate contraction.
def add(*xs):
 d=defaultdict(int)
 for x in xs:
  for m,c in x.items():d[m]+=c
 return {m:c for m,c in d.items() if c}
def scale(x,s):return {m:c*s for m,c in x.items() if c*s}
def mul(x,y):
 d=defaultdict(int)
 for m,c in x.items():
  for n,e in y.items():d[tuple(a+b for a,b in zip(m,n))]+=c*e
 return {m:c for m,c in d.items() if c}
checks=[]
for n in range(1,11):
 for aexp in range(n+1):
  target={(aexp,n-aexp,0):1}
  q={(aexp-1-j,n-aexp+j,j):1 for j in range(aexp)}
  rhs=add(mul({(1,0,0):1,(0,1,1):-1},q),{(0,n,aexp):1})
  assert rhs==target
 checks.append({'n':n,'number_of_minimal_monomial_generators':n+1,'identities_checked':n+1})
out['coherent_elimination']={'coordinate_identity':'u^a v^(n-a)=(u-vT)*sum_(j=0)^(a-1)u^(a-1-j)v^(n-a+j)T^j+v^nT^a','checks':checks,'general_proof':'research/root_proofs.md R11; not inferred from n<=10 tests'}

# A two-point topological example: exact irreducible closed-chain dimension.
def dimension(closed):
 nonempty=[x for x in closed if x]
 irr=[z for z in nonempty if not any(x!=z and y!=z and x|y==z for x in closed for y in closed)]
 best=0
 for n in range(1,len(irr)+1):
  for chain in permutations(irr,n):
   if all(chain[i]<chain[i+1] for i in range(n-1)):best=max(best,n-1)
 return best
E=frozenset();aa=frozenset({0});bb=frozenset({1});ab=frozenset({0,1})
disc=[E,aa,bb,ab];sier=[E,aa,ab]
assert all(z in disc for z in sier)
assert dimension(disc)==0 and dimension(sier)==1
out['continuous_image_dimension']={'source_closed_sets':[sorted(x) for x in disc],'target_closed_sets':[sorted(x) for x in sier],'identity_continuous':True,'source_dimension':dimension(disc),'target_dimension':dimension(sier)}

dest=Path(__file__).resolve().parents[1]/'outputs/root_extra_certificates.json'
dest.write_text(json.dumps(out,default=str,ensure_ascii=False,indent=2))
print(json.dumps({'groups':list(out),'all_assertions':'passed','output':str(dest)},indent=2))
