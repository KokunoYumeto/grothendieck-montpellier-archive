"""Independent character, moment-kernel and literal G038 matrix checks."""
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
import sys,json
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'rectangular'))
from verify_rectangular import partitions,z,character
from verify_outer4_chambers import actual
import stable_second_row_positive as P
import stable_hook_positive as H
from check_stable_hook_positive import trace_data,coin_witnesses,witnesses

@lru_cache(None)
def actual_module(m,a,nu):
 total=Fraction()
 for rho in partitions(m):
  h,_=trace_data(rho,max(a+1,2))
  trace=h[a]*h[2]-h[a+1]*h[1]
  total+=Fraction(character(nu,rho)*trace,z(rho))
 assert total.denominator==1
 return int(total)
@lru_cache(None)
def coinvariant_cycle(rho):
 m=sum(rho);N=m*(m-1)//2
 out=[1]+[0]*N
 for i in range(1,m+1):
  for j in range(N,i-1,-1):out[j]-=out[j-i]
 for i in rho:
  for j in range(i,N+1):out[j]+=out[j-i]
 return out
def independent_free_numerator(m,nu):
 N=m*(m-1)//2;out=[Fraction() for _ in range(N+3)]
 for rho in partitions(m):
  w=rho.count(1)-1;w2=rho.count(1)+2*rho.count(2)-1
  s2=(w*w+w2)//2
  factor=Fraction(character(nu,rho),z(rho))
  for j,v in enumerate(coinvariant_cycle(rho)):
   out[j+2]+=factor*s2*v;out[j+1]-=factor*w*v
 d=1 if nu==(m-1,1) else 2 if nu==(m-2,1,1) else 0
 if d:
  out[d]+=1
  for j in range(2,m+1):out[d+j]-=1
 assert all(v.denominator==1 for v in out)
 return H.trim([int(v) for v in out]),d
def main():
 receipt={'statement':'G-038','free_numerator_comparisons':0,'module_coefficients':0,'support_checks':0,'original_plethysms':0,'polytope_cases':0,'literal_witnesses':0,'max_variables':0,'max_pieces':0}
 for m in range(3,11):
  for nu in partitions(m):
   f,d=P.free_numerator(nu);want,wd=independent_free_numerator(m,nu)
   assert list(f)==want and d==wd,(m,nu,f,want)
   receipt['free_numerator_comparisons']+=1
   for a in range(2,18):
    got=P.module_coefficient(m,a,nu);want=actual_module(m,a,nu)
    assert got==want,(m,a,nu,got,want)
    assert P.module_support(m,a,nu)==bool(want),(m,a,nu,got,'support')
    receipt['module_coefficients']+=1;receipt['support_checks']+=1
  print('character',m,receipt['module_coefficients'],flush=True)
 for m in range(3,6):
  for a in range(2,5):
   for t in (0,1):
    n=a+t
    for mu in partitions(m):
     lam,nu=P.physical(m,a,t,n,mu)
     got=P.coefficient(m,a,t,n,mu);want=actual(mu,n,lam)
     assert got==want,(m,a,t,n,mu,lam,got,want)
     receipt['original_plethysms']+=1
  print('original',m,receipt['original_plethysms'],flush=True)
 for m in range(3,7):
  for nu in partitions(m):
   for a in range(2,9):
    pieces=P.module_polytopes(m,a,nu);count=0
    for poly in pieces:
     receipt['max_variables']=max(receipt['max_variables'],poly['variable_count'])
     tag=poly['tag']
     if tag['kind']=='free':
      for coins in coin_witnesses(tuple(range(2,m+1)),a+2-tag['degree']):
       for j in range(tag['multiplicity']):
        w={'generator':j,**{f'c{i}':coins[i-2] for i in range(2,m+1)}}
        assert H.valid_witness(poly,w),(m,a,nu,tag,w)
        count+=1
     else:
      for w in witnesses(m,a+1-tag['shift'],1,(m,)):
       assert H.valid_witness(poly,w),(m,a,nu,tag,w)
       count+=1
    assert count==actual_module(m,a,nu),(m,a,nu,count)
    receipt['polytope_cases']+=1;receipt['literal_witnesses']+=count
    receipt['max_pieces']=max(receipt['max_pieces'],len(pieces))
  print('matrices',m,receipt['polytope_cases'],receipt['literal_witnesses'],flush=True)
 receipt['large_degree_examples']=[{'m':7,'a':10**30,'nu':nu,'coefficient':P.module_coefficient(7,10**30,nu)} for nu in ((7,),(6,1),(5,1,1),(3,2,2))]
 receipt['outcome']='PASS'
 (HERE/'STABLE_SECOND_ROW_POSITIVE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
 print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
