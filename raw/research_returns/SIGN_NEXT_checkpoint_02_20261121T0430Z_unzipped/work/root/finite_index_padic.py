#!/usr/bin/env python3
"""Exact local Smith exponents for SN-15's finite matrices.

Elimination is in Z/p^cap: only unit pivots are inverted. If all
remaining entries are divisible by p, divide them and the modulus by p.
No exponent is accepted when the modulus is exhausted; retry at twice
the precision instead. The theorem bounds prime support by n.
"""
import argparse,json,math,time
from pathlib import Path
from finite_index_formula import bounded_matrix

def local_smith(mat,p,cap=16):
 original=[list(map(int,row)) for row in mat]
 while True:
  modulus=p**cap; A=[[x%modulus for x in row] for row in original]
  shift=0; vals=[]; trace=[]; retry=False
  while A:
   pivot=None
   for i,row in enumerate(A):
    for j,x in enumerate(row):
     if x%p:
      pivot=(i,j);break
    if pivot is not None:break
   if pivot is None:
    if modulus==p:
     retry=True;break
    assert all(x%p==0 for row in A for x in row)
    A=[[x//p for x in row] for row in A]
    modulus//=p;shift+=1
    trace.append({'divide_by_p':True,'remaining_rows':len(A),'shift':shift})
    continue
   i,j=pivot
   A[0],A[i]=A[i],A[0]
   for row in A:row[0],row[j]=row[j],row[0]
   unit=A[0][0]; inverse=pow(unit,-1,modulus)
   top=A[0]
   lower=[]
   for row in A[1:]:
    ratio=row[0]*inverse%modulus
    lower.append([(x-ratio*y)%modulus for x,y in zip(row[1:],top[1:])])
   trace.append({'pivot_row':i,'pivot_column':j,'pivot_unit':str(unit),
                 'modulus':str(modulus),'exponent':shift,'remaining_rows':len(A)})
   vals.append(shift);A=lower
  if not retry:
   assert vals==sorted(vals)
   return vals,cap,trace
  cap*=2

def calculate(n,proj):
 start=time.monotonic();M,rows,cols=bounded_matrix(n,proj)
 normal=[i for i,(v,k,l,t) in enumerate(rows) if t==0 or v-k-l+t==0]
 primes=[p for p in range(2,n+1) if all(p%d for d in range(2,math.isqrt(p)+1))]
 all_vals={p:[] for p in primes};cert=[]
 for sh in range(-n,n+1):
  ris=[i for i in normal if rows[i][1]-rows[i][2]==sh]
  cis=[j for j,(a,c,b) in enumerate(cols) if a-c==sh]
  B=[[int(M[i,j]) for j in cis] for i in ris]
  for p in primes:
   vals,cap,trace=local_smith(B,p)
   assert len(vals)==len(ris)
   all_vals[p].extend(vals)
   cert.append({'shift':sh,'prime':p,'precision':cap,'exponents':vals,'trace':trace})
 rank=len(normal);ds=[1]*rank
 for p,vs in all_vals.items():
  assert len(vs)==rank
  for i,v in enumerate(sorted(vs)):ds[i]*=p**v
 factors={str(p):sum(vs) for p,vs in all_vals.items() if sum(vs)}
 return {'n':n,'degree_projectors':proj,'rank':rank,'factorization':factors,
         'index':str(math.prod(ds)),'smith_factors':[str(d) for d in ds],
         'seconds':time.monotonic()-start,'local_certificates':cert}

def main():
 p=argparse.ArgumentParser();p.add_argument('--max-n',type=int,default=6);a=p.parse_args()
 out=Path(__file__).with_name('finite_index_padic_results.json');results=[]
 for n in range(1,a.max_n+1):
  for proj in [False,True]:
   r=calculate(n,proj);results.append(r)
   print({k:v for k,v in r.items() if k not in ['smith_factors','local_certificates']},flush=True)
   out.write_text(json.dumps(results,indent=2)+'\n')

if __name__=='__main__':main()
