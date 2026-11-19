"""Finite audits of the exact coefficient-adjoint proof; not its universal proof."""
from fractions import Fraction
from math import comb
import json
relations=0
for j in range(35):
 for n in range(j+1):
  for m in range(j-n+1):
   assert Fraction(comb(j-n,m),comb(j,n+m))==Fraction(comb(n+m,n),comb(j,n))
   relations+=1
transitions=0
for j in range(20):
 for h in range(j,30):
  for n in range(j+1):
   assert Fraction(comb(h-n,j-n),comb(j,n)*comb(h,j))==Fraction(1,comb(h,n))
   transitions+=1
units=0
for ell in [2,3,5,7]:
 for r in range(1,4):
  j=ell**r-1
  for n in range(j+1):
   assert comb(j,n)%ell!=0
   units+=1
print(json.dumps({'coefficient_presentation_relations':relations,'cofinal_transition_identities':transitions,'prime_local_binomial_units':units,'universal_proof':'work/early/proofs.md section15; work/late/proofs.md section5','scope':'Finite exact rational/binomial audits only'},indent=2))
