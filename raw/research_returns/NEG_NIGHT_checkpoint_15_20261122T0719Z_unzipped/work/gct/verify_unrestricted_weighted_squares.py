"""Exact certificate verifier for the unrestricted shared-quadratic bound.
No optimizer, floating arithmetic, or exploratory matrix builder is used.
Source dimensions and every associator/budget coefficient are reconstructed
from the original table, with all810 nonunit-input positions free.
"""
from pathlib import Path
from collections import Counter,defaultdict
from itertools import product
import json,sys
import sympy as sp

names=['mu','Sigma']+[f'g{i}_{w}' for i in (1,2) for w in ('1','12','2','21')]
indices={s:i for i,s in enumerate(names)};v=sp.Symbol('v');A={}
for row in json.loads(Path('sources/OURS_E4_scripts/e3_constants.json').read_text()):
 key=tuple(indices[row[k]] for k in ('b','bp','bpp'))
 p=sp.Poly(sp.expand(sp.sympify(row['c'],locals={'v':v})*v**64),v)
 assert all(co.is_Integer and (e[0]-64)%2==0 for e,co in p.terms())
 A[key]=sum(abs(int(co)) for e,co in p.terms())
assert len(A)==132 and sum(A.values())==4443
for a,z in product(range(10),repeat=2):
 assert A.get((0,a,z),0)==A.get((a,0,z),0)==int(a==z)
free=list(product(range(1,10),range(1,10),range(10)))
position={key:i for i,key in enumerate(free)}
assert len(free)==810
assert all(A.get(key,0)%2==0 for key in free)
assert all(A.get(key,0)==0 for key in free if key[2]==0)

def associator(loc):
 a,b,c,z=loc
 assert all(isinstance(x,int) for x in loc)
 assert 1<=a<10 and 1<=b<10 and 1<=c<10 and 0<=z<10
 constant=0;linear=defaultdict(int);quadratic=defaultdict(int)
 for y in range(10):
  for sign,left,right in [(1,(a,b,y),(y,c,z)),(-1,(b,c,y),(a,y,z))]:
   dl,dr=A.get(left,0),A.get(right,0)
   constant+=sign*dl*dr
   il,ir=position.get(left),position.get(right)
   if il is not None:linear[il]+=sign*dr
   if ir is not None:linear[ir]+=sign*dl
   if il is not None and ir is not None:quadratic[tuple(sorted((il,ir)))]+=sign
 return -constant,{i:c for i,c in linear.items() if c},{ij:c for ij,c in quadratic.items() if c}

# The verifier uses the full7290-equation moment graph, even when the
# finder used a smaller subgraph. Extra terms in a budget row enter with
# negative sign and remain valid nonnegative-product terms.
Q={(i,i) for i in range(810)}
for loc in product(range(1,10),range(1,10),range(1,10),range(10)):
 Q.update(associator(loc)[2])
assert len(Q)==112302
incident=[set() for _ in range(810)]
for ij in Q:
 for i in set(ij):incident[i].add(ij)

def verify(certificate,require_contradiction=True):
 M=certificate['budget_added_mass'];assert isinstance(M,int) and M>0 and M%2==0
 linear=defaultdict(int);quadratic=defaultdict(int);rhs=0
 seen=set()
 for row in certificate['equalities']:
  loc=tuple(row['locator']);weight=row['multiplier']
  assert isinstance(weight,int) and weight!=0 and loc not in seen;seen.add(loc)
  b,le,qu=associator(loc);rhs+=weight*b
  for i,co in le.items():linear[i]+=weight*co
  for ij,co in qu.items():quadratic[ij]+=weight*co
 eq_count=len(seen);seen=set()
 for row in certificate['nonnegative_bounds']:
  loc=tuple(row['locator']);weight=row['multiplier']
  assert isinstance(weight,int) and weight>0 and loc not in seen;seen.add(loc)
  if loc[0]=='diagonal':
   assert len(loc)==2 and isinstance(loc[1],int) and 0<=loc[1]<810
   i=loc[1];linear[i]-=2*weight;quadratic[i,i]+=weight
  elif loc[0]=='unit_diagonal':
   assert len(loc)==2 and isinstance(loc[1],int) and 0<=loc[1]<810 and free[loc[1]][2]==0
   i=loc[1];linear[i]-=4*weight;quadratic[i,i]+=weight
  elif loc[0]=='difference':
   assert len(loc)==3 and all(isinstance(i,int) for i in loc[1:])
   _,i,j=loc;assert 0<=i<810 and 0<=j<810 and i!=j and tuple(sorted((i,j))) in Q
   linear[i]-=2*weight;linear[j]+=2*weight
   quadratic[i,i]+=weight;quadratic[j,j]+=weight;quadratic[tuple(sorted((i,j)))]-=2*weight
  elif loc[0]=='weighted_difference':
   assert len(loc)==6 and all(isinstance(x,int) for x in loc[1:])
   _,i,j,a,b,sign=loc
   assert 0<=i<j<810 and (i,j) in Q and a>0 and b>0 and sign in (-1,1)
   linear[i]-=2*sign*a*weight;linear[j]+=2*sign*b*weight
   quadratic[i,i]+=a*a*weight;quadratic[j,j]+=b*b*weight;quadratic[i,j]-=2*a*b*weight
  elif loc[0]=='pair':
   assert len(loc)==3 and all(isinstance(i,int) for i in loc[1:])
   _,i,j=loc;assert 0<=i<j<810 and (i,j) in Q
   linear[i]+=M*weight;linear[j]+=M*weight;quadratic[i,j]-=4*weight
  elif loc[0]=='budget':
   assert len(loc)==2 and isinstance(loc[1],int) and 0<=loc[1]<810
   i=loc[1];linear[i]+=M*weight
   for ij in incident[i]:quadratic[ij]-=weight
  else:raise AssertionError(loc)
 # Drop negative product coefficients, then bound positive remainders
 # using EiEj<=M(Ei+Ej)/4 and Ei^2<=M Ei. Clear denominator4.
 corrected={i:4*linear[i] for i in range(810)}
 positive=0;positive_diagonal=0
 for (i,j),co in quadratic.items():
  if co<=0:continue
  positive+=1
  if i==j:corrected[i]+=4*M*co;positive_diagonal+=1
  else:corrected[i]+=M*co;corrected[j]+=M*co
 maximum=max(corrected.values())
 assert maximum>=0, 'The total-budget upper bound requires a nonnegative maximum'
 gap=4*rhs-M*maximum
 out={'source_positions':132,'free_unrestricted_positions':810,'moment_pairs':len(Q),'weighted_equalities':eq_count,'weighted_nonnegative_bounds':len(seen),'positive_quadratic_remainders':positive,'positive_diagonal_remainders':positive_diagonal,'budget_added_mass':M,'four_times_weighted_rhs':4*rhs,'maximum_corrected_coefficient':maximum,'budget_times_maximum':M*maximum,'strict_gap':gap,'proved_pair_lower_bound':M//2+1 if gap>0 else None,'arithmetic':'exact integers from original source; no optimizer in verifier'}
 if require_contradiction:assert gap>0
 if 'expected' in certificate:assert out==certificate['expected']
 return out

if __name__=='__main__':
 path=Path(sys.argv[1]) if len(sys.argv)>1 else Path('work/gct/unrestricted_weighted_squares_110_certificate.json')
 print(json.dumps(verify(json.loads(path.read_text())),indent=2))
