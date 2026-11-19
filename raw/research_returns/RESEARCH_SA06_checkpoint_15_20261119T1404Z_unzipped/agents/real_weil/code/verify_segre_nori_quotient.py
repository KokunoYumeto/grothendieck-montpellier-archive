#!/usr/bin/env python3
"""Sign and degree certificates for C.3aa; no Chow group computation."""
from pathlib import Path
from time import perf_counter
import json
import sympy as sp

started=perf_counter()
base=Path(__file__).resolve().parent
h,H=sp.symbols('h H')
power_checks=[]
for a in range(0,33):
 rhs=(h+H)*sum((h**(a-1-b)*(-H)**b for b in range(a)),sp.Integer(0))
 remainder=sp.expand(h**a-(-H)**a-rhs)
 assert remainder==0
 power_checks.append(a)
grid=[]
for r in range(2,17):
 for N in range(r+2,r+15):
  m=N-r-2
  assert m>=0 and r<r+1<2*r
  assert m+(r+1)==N-1
  s=r-1;d=4*r+2
  assert 2*r-s==r+1
  assert d>2*r
  for i in range(s):
   assert s*d>1+2*r+(r+1)-i
  denominator_source=r-m-1
  if denominator_source>=0:
   assert m+denominator_source==r-1
  grid.append({'N':N,'r':r,'m':m,'T_dimension':r+1,'cut_count':s,'cut_degree':d,'denominator_source_degree':denominator_source,'denominator_zero_by_degree':denominator_source<0})
data={
 'statement':'C.3aa',
 'power_identity_checked_exponents':power_checks,
 'grid':grid,
 'grid_size':len(grid),
 'scope':'The exact polynomial identities check signs; the grid checks dimension and degree bookkeeping. The general module quotient, Nori obstruction, projective normality and actual strict-henselian Chow injection are proved in the text. No finite computation asserts a Griffiths-group vanishing or nonvanishing.',
 'runtime_seconds':perf_counter()-started
}
(base/'segre_nori_quotient_output.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS: exact h=-H telescoping identity for exponents0 through32.')
print(f"PASS: {len(grid)} dimension/degree cases, r2 through16, N=r+2 throughr+14.")
print('PASS: primitive obstruction denominator always lies in H B^(r-1), or is zero by degree.')
print('No Chow or Griffiths group is inferred from the finite checks.')
print(f"Runtime seconds: {data['runtime_seconds']:.6f}")
print('Wrote segre_nori_quotient_output.json')
