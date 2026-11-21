"""Independent cycle traces, original plethysms and literal G037 witnesses."""
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
import json,sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'rectangular'))
from verify_rectangular import partitions,z,character
from verify_outer4_chambers import actual
import stable_hook_positive as P

@lru_cache(None)
def trace_data(rho,N):
 h=[1]+[0]*N
 for j in rho:
  for k in range(j,N+1):h[k]+=h[k-j]
 h=[h[k]-(h[k-1] if k else 0) for k in range(N+1)]
 e=[1]
 for j in rho:e=P.mul(e,[1]+[0]*(j-1)+[(-1)**(j+1)])
 for k in range(1,len(e)):e[k]-=e[k-1]
 assert e[-1]==0
 return h,e[:-1]
def actual_module(m,a,r,nu):
 value=Fraction()
 for rho in partitions(m):
  h,e=trace_data(rho,a+r)
  tr=sum((-1)**j*h[a+j]*e[r-j] for j in range(r+1))
  value+=Fraction(character(nu,rho)*tr,z(rho))
 assert value.denominator==1
 return int(value)
def coin_witnesses(weights,D):
 if D<0:return
 if not weights:
  if D==0:yield ()
  return
 for k in range(D//weights[0]+1):
  for rest in coin_witnesses(weights[1:],D-weights[0]*k):yield(k,)+rest
@lru_cache(None)
def tableaux(nu):
 if not nu:return ({},)
 m=sum(nu);out=[]
 for i,a in enumerate(nu):
  if i+1<len(nu) and nu[i+1]==a:continue
  new=list(nu);new[i]-=1
  while new and not new[-1]:new.pop()
  for T in tableaux(tuple(new)):out.append({**T,(i+1,a):m})
 return tuple(out)
def witnesses(m,a,r,nu):
 D=a+r
 if nu==(m,):
  for beta in coin_witnesses(tuple(range(2,m+1)),D):
   supp=[j for j in range(2,m+1) if beta[j-2]]
   if not supp:continue
   i=supp[0]
   for chosen in combinations(supp[1:],r):
    yield {**{f'z{j}':int(j==i) for j in range(2,m+1)},**{f'y{j}':int(j in chosen) for j in range(2,m+1)},**{f'b{j}':beta[j-2] for j in range(2,m+1)}}
  return
 C=P.cells(nu);select=[c for c in C if c not in ((1,1),(2,1))]
 for T in tableaux(nu):
  rows={label:c[0] for c,label in T.items()};delta={j:int(rows[j+1]>rows[j]) for j in range(1,m)}
  comaj=sum((m-j)*delta[j] for j in delta)
  for chosen in combinations(select,r):
   left=D-comaj-sum(j-i+1 for i,j in chosen)
   for coins in coin_witnesses(tuple(range(2,m+1)),left):
    yield {**{f'X{c[0]}_{c[1]}_{j}':int(T[c]==j) for c in C for j in range(1,m+1)},**{f'd{j}':delta[j] for j in delta},**{f'Y{c[0]}_{c[1]}':int(c in chosen) for c in select},**{f'c{j}':coins[j-2] for j in range(2,m+1)}}
def main():
 receipt={'statement':'G-037','module_coefficients':0,'support_checks':0,'original_plethysm_coefficients':0,'polytope_cases':0,'literal_witnesses':0,'max_variables':0}
 for m in range(3,9):
  for nu in partitions(m):
   for r in range(m-1):
    for a in range(1,15):
     v=P.module_coefficient(m,a,r,nu);want=actual_module(m,a,r,nu)
     assert v==want,(m,a,r,nu,v,want)
     assert (v>0)==P.module_support(m,a,r,nu),(m,a,r,nu,v,'support')
     receipt['module_coefficients']+=1;receipt['support_checks']+=1
  print('module and support',m,receipt['module_coefficients'],flush=True)
 for m in range(3,6):
  for a in range(1,4 if m<5 else 3):
   for r in range(m-1):
    for t in (0,1):
     n=a+t
     for mu in partitions(m):
      lam,nu=P.physical(m,a,r,t,n,mu)
      v=P.coefficient(m,a,r,t,n,mu);want=actual(mu,n,lam)
      assert v==want,(m,a,r,t,n,mu,lam,v,want)
      receipt['original_plethysm_coefficients']+=1
  print('original plethysm',m,receipt['original_plethysm_coefficients'],flush=True)
 for m in range(3,7):
  for nu in partitions(m):
   for r in range(m-1):
    for a in range(1,6):
     data=P.module_polytope(m,a,r,nu);count=0
     for w in witnesses(m,a,r,nu):
      assert P.valid_witness(data,w),(m,a,r,nu,w)
      count+=1
     assert count==P.module_coefficient(m,a,r,nu),(m,a,r,nu,count)
     receipt['polytope_cases']+=1;receipt['literal_witnesses']+=count
     receipt['max_variables']=max(receipt['max_variables'],data['variable_count'])
  print('polytope',m,receipt['polytope_cases'],receipt['literal_witnesses'],flush=True)
 # Exercise parity extraction on a degree far beyond a linear coefficient scan.
 receipt['large_degree_example']={'m':7,'a':10**12,'r':2,'nu':[3,2,2],'coefficient':P.module_coefficient(7,10**12,2,(3,2,2))}
 receipt['outcome']='PASS'
 (HERE/'STABLE_HOOK_POSITIVE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
 print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
