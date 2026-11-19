"""Exact auxiliary checks for E10; no numerical approximation."""
from math import comb
from pathlib import Path
import json

a,b=-1,0
discriminant=-16*(4*a**3+27*b**2)
assert discriminant==64 and discriminant%3!=0
points={}
for p in (3,5):
 affine=[(x,y) for x in range(p) for y in range(p) if (y*y-x**3+x)%p==0]
 points[str(p)]={"affine_points":affine,"projective_count":len(affine)+1,"trace":p-len(affine)}
assert points['3']['projective_count']==4
# C(dx/y) = (1/y) C((x^3-x)dx) at p=3.  Cartier selects degree 2 mod 3.
f={3:1,1:-1}
cartier={ (degree-2)//3:coef%3 for degree,coef in f.items() if degree%3==2 }
assert cartier=={}
# The exact identity used before applying Cartier is y^2=x^3-x.
# Verify the Laurent coefficient integrality detector for positive and negative exponents.
checked=0
for p in (2,3,5,7):
 for s in range(-500,501):
  if not s:continue
  v=0;n=abs(s)
  while n%p==0:v+=1;n//=p
  n=p**v
  binomial=comb(s,n) if s>=0 else (-1)**n*comb(n-s-1,n)
  assert binomial%p!=0,(p,s,n,binomial)
  checked+=1
result={"discriminant":discriminant,"good_reduction_at_3":True,"point_counts":points,
        "Cartier_of_invariant_differential_at_3":cartier,
        "generalized_binomial_unit_checks":checked,
        "scope":"Exact finite checks of arithmetic and coefficient identities; geometric site comparisons are proved separately."}
output=Path(__file__).with_name('E10_checks_output.json')
output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
