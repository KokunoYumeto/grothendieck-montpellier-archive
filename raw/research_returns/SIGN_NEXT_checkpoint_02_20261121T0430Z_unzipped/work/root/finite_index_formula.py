#!/usr/bin/env python3
"""Exact all-rank bounded PBW matrices for actual exterior order indices.

Independent construction from subset intersection counts, not word closure.
Run `python finite_index_formula.py --max-n 4` from any directory.
For larger ranks use finite_index_padic.py; it avoids coefficient swell.
"""
from pathlib import Path
import argparse,json,math,time
from sympy import Matrix,ZZ,factorint
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form

def rows(n):
 return [(v,k,l,t) for v in range(n+1) for k in range(v+1)
         for l in range(v+1) for t in range(max(0,k+l-v),min(k,l)+1)]

def bounded_matrix(n,projectors=False):
 rr=rows(n)
 cc=[(a,c,b) for a in range(n+1) for c in range(n+1) for b in range(2*n+1)]
 data=[]
 for v,k,l,t in rr:
  row=[]
  for a,c,b in cc:
   s=l-c
   if s<0 or s>t or k!=s+a: x=0
   else:
    x=math.factorial(a)*math.factorial(c)*math.comb(t,s)
    x*=int(b==n-v+2*l) if projectors else (v-2*s)**b
   row.append(x)
  data.append(row)
 return Matrix(data),rr,cc

def calculate(n,projectors=False):
 start=time.monotonic()
 M,rr,cc=bounded_matrix(n,projectors)
 normal=[i for i,(v,k,l,t) in enumerate(rr) if t==0 or v-k-l+t==0]
 blocks=[];local_ds=[]
 for shift in range(-n,n+1):
  ris=[i for i in normal if rr[i][1]-rr[i][2]==shift]
  cis=[j for j,(a,c,b) in enumerate(cc) if a-c==shift]
  B=M[ris,cis]
  H=hermite_normal_form(B)
  S=smith_normal_form(H,domain=ZZ)
  ds_block=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]
  assert len(ds_block)==len(ris)
  local_ds.extend(ds_block)
  blocks.append({'shift':shift,'rows':ris,'columns':cis,
                 'smith_factors':[str(d) for d in ds_block],
                 'hnf_basis':[[str(x) for x in H.row(i)] for i in range(H.rows)]})
 primes=[p for p in range(2,n+1) if all(p%d for d in range(2,math.isqrt(p)+1))]
 ds=[1]*len(local_ds)
 for p in primes:
  vals=[]
  for x in local_ds:
   e=0
   while x%p==0:x//=p;e+=1
   vals.append(e)
  for i,e in enumerate(sorted(vals)):ds[i]*=p**e
 assert math.prod(ds)==math.prod(local_ds), 'Unexpected prime above n'
 assert len(ds)==(n+1)*(n+2)*(2*n+3)//6
 assert all(ds[i+1]%ds[i]==0 for i in range(len(ds)-1))
 idx=math.prod(ds)
 return {'n':n,'degree_projectors':projectors,'rows':len(rr),'generators':len(cc),
         'rank':len(ds),'index':str(idx),'factorization':{str(p):int(e) for p,e in factorint(idx).items()},
         'normal_rows':len(normal),'smith_factors':[str(d) for d in ds],
         'seconds':time.monotonic()-start,'block_certificates':blocks}

def main():
 p=argparse.ArgumentParser();p.add_argument('--max-n',type=int,default=4);p.add_argument('--min-n',type=int,default=1);a=p.parse_args()
 out=Path(__file__).with_name('finite_index_formula_results.json')
 results=[]
 for n in range(a.min_n,a.max_n+1):
  for proj in [False,True]:
   r=calculate(n,proj);results.append(r)
   print({k:v for k,v in r.items() if k not in ['smith_factors','block_certificates']},flush=True)
   out.write_text(json.dumps(results,indent=2)+'\n')

if __name__=='__main__':main()
