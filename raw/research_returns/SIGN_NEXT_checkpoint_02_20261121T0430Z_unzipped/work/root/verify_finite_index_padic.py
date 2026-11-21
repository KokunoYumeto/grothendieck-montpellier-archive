#!/usr/bin/env python3
"""Verify new n=5,6 local exponents by exact rational Schur elimination.

Unlike the producer this uses no modular arithmetic, precision cap,
unit-rank iteration, HNF, or Smith routine. It chooses an entry of
minimal p-adic valuation and takes its rational Schur complement.
All elimination ratios are p-integral, so each pivot valuation is
one local elementary divisor. Matrix entries use the reviewed SN-15
formula shared with the producer.
"""
from fractions import Fraction
from pathlib import Path
import json,time
from finite_index_formula import bounded_matrix

def val(x,p):
 if not x:return 10**9
 a,b=abs(x.numerator),x.denominator;e=0
 while a%p==0:a//=p;e+=1
 while b%p==0:b//=p;e-=1
 return e

def exact_schur(B,p):
 A=[[Fraction(int(x)) for x in row] for row in B];vs=[]
 while A:
  v,i,j=min((val(x,p),i,j) for i,row in enumerate(A) for j,x in enumerate(row))
  assert v<10**9
  A[0],A[i]=A[i],A[0]
  for row in A:row[0],row[j]=row[j],row[0]
  pivot=A[0][0];top=A[0]
  ratios=[row[0]/pivot for row in A[1:]]
  assert all(not r or val(r,p)>=0 for r in ratios)
  assert all(not x or val(x/pivot,p)>=0 for x in top[1:])
  A=[[x-r*y for x,y in zip(row[1:],top[1:])] for row,r in zip(A[1:],ratios)]
  vs.append(v)
 assert vs==sorted(vs)
 return vs

def main():
 base=Path(__file__).resolve().parent
 results=json.loads((base/'finite_index_padic_results.json').read_text());checks=[]
 for record in results:
  n=record['n'];proj=record['degree_projectors']
  if n not in (5,6):continue
  start=time.monotonic();M,rows,cols=bounded_matrix(n,proj)
  normal=[i for i,(v,k,l,t) in enumerate(rows) if t==0 or v-k-l+t==0]
  for cert in record['local_certificates']:
   sh,p=cert['shift'],cert['prime']
   ri=[i for i in normal if rows[i][1]-rows[i][2]==sh]
   ci=[j for j,(a,c,b) in enumerate(cols) if a-c==sh]
   got=exact_schur([[M[i,j] for j in ci] for i in ri],p)
   assert got==cert['exponents'],(n,proj,sh,p,got,cert['exponents'])
   checks.append({'n':n,'degree_projectors':proj,'shift':sh,'prime':p,'exponents':got,'passed':True})
  print({'n':n,'degree_projectors':proj,'passed':True,'seconds':time.monotonic()-start},flush=True)
 (base/'finite_index_independent_verification.json').write_text(json.dumps(checks,indent=2)+'\n')
 print('All',len(checks),'block-prime calculations agreed.',flush=True)

if __name__=='__main__':main()
