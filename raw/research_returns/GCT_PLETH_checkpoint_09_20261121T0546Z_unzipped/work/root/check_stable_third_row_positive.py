"""G039 finite cycle/JT, original plethysm, and literal matrix checks."""
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
import sys,json
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'rectangular'))
from verify_rectangular import partitions,z,character
from verify_outer4_chambers import actual
from check_stable_hook_positive import trace_data,coin_witnesses
from check_stable_second_row_positive import coinvariant_cycle
import stable_hook_positive as H
import stable_third_row_positive as P

@lru_cache(None)
def actual_module(m,a,nu):
 value=Fraction()
 for rho in partitions(m):
  h,_=trace_data(rho,a+1)
  value+=Fraction(character(nu,rho)*(h[a]*h[3]-h[a+1]*h[2]),z(rho))
 assert value.denominator==1
 return int(value)
def independent_numerator(m,nu):
 N=m*(m-1)//2;A=[Fraction() for _ in range(N+4)]
 c2=Fraction();c21=Fraction();cw=Fraction()
 for rho in partitions(m):
  h,_=trace_data(rho,3);factor=Fraction(character(nu,rho),z(rho))
  c2+=factor*h[2];c21+=factor*(h[2]*h[1]-h[3]);cw+=factor*(h[2]*h[2]-h[3]*h[1]-h[2])
  for j,v in enumerate(coinvariant_cycle(rho)):
   A[j+3]+=factor*h[3]*v;A[j+2]-=factor*h[2]*v
 assert all(v.denominator==1 for v in (c2,c21,cw))
 c2,c21,cw=map(int,(c2,c21,cw))
 for shift,c,weights in ((2,c2,(4,)+tuple(range(3,m+1))),(3,c21,tuple(range(2,m+1))),(4,cw,tuple(range(2,m+1)))):
  A[shift]+=c
  for w in weights:A[shift+w]-=c
 assert all(v.denominator==1 for v in A)
 return H.trim([int(v) for v in A]),(c2,c21,cw)
def main():
 receipt={'statement':'G-039','free_numerator_comparisons':0,'module_coefficients':0,'support_checks':0,'original_plethysms':0,'polytope_cases':0,'literal_witnesses':0,'max_variables':0,'max_pieces':0}
 for m in range(3,11):
  for nu in partitions(m):
   if m>=4:
    F,c=P.free_numerator(nu);want,wc=independent_numerator(m,nu)
    assert list(F)==want and c==wc,(m,nu,F,want,c,wc)
    receipt['free_numerator_comparisons']+=1
   for a in range(3,20):
    got=P.module_coefficient(m,a,nu);want=actual_module(m,a,nu)
    assert got==want,(m,a,nu,got,want)
    assert P.module_support(m,a,nu)==bool(want),(m,a,nu,got,'support')
    receipt['module_coefficients']+=1;receipt['support_checks']+=1
  print('module',m,receipt['module_coefficients'],flush=True)
 for m in range(3,6):
  for a in range(3,6):
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
   for a in range(3,11):
    polys=P.module_polytopes(m,a,nu);count=0
    for poly in polys:
     tag=poly['tag'];receipt['max_variables']=max(receipt['max_variables'],poly['variable_count'])
     if tag['kind'] in ('free','free_rank_two'):
      target=(a+3 if m>=4 else a-3)-tag['degree']
      for coins in coin_witnesses(tuple(range(2,m+1)),target):
       for j in range(tag['multiplicity']):
        w={'generator':j,**{f'c{i}':coins[i-2] for i in range(2,m+1)}}
        assert H.valid_witness(poly,w),(m,a,nu,tag,w)
        count+=1
     else:
      weights=tag['weights'];k=len(weights);D=a+3-tag['shift']
      for bit in ((0,1) if tag['extra_bit'] else (0,)):
       for beta in coin_witnesses(weights,D-2*bit):
        supp=[j for j,v in enumerate(beta) if v]
        if not supp:continue
        i=supp[0]
        for j in supp[1:]:
         for gen in range(tag['multiplicity']):
          w={'generator':gen,**{f'z{l}':int(l==i) for l in range(k)},**{f'y{l}':int(l==j) for l in range(k)},**{f'b{l}':beta[l] for l in range(k)}}
          if tag['extra_bit']:w['quadratic_remainder']=bit
          assert H.valid_witness(poly,w),(m,a,nu,tag,w)
          count+=1
    assert count==actual_module(m,a,nu),(m,a,nu,count)
    receipt['polytope_cases']+=1;receipt['literal_witnesses']+=count
    receipt['max_pieces']=max(receipt['max_pieces'],len(polys))
  print('matrices',m,receipt['polytope_cases'],receipt['literal_witnesses'],flush=True)
 receipt['large_degree_examples']=[{'m':7,'a':10**30,'nu':nu,'coefficient':P.module_coefficient(7,10**30,nu)} for nu in ((7,),(6,1),(5,1,1),(3,2,2))]
 receipt['outcome']='PASS'
 (HERE/'STABLE_THIRD_ROW_POSITIVE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
 print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
