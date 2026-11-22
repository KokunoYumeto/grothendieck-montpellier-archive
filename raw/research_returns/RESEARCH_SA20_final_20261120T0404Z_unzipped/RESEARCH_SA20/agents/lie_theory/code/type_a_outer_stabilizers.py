#!/usr/bin/env python3
from itertools import permutations,product
from math import gcd,factorial
from datetime import datetime,timezone
from time import perf_counter
import json
from pathlib import Path
start=perf_counter();print('Started UTC',datetime.now(timezone.utc).isoformat())
reports=[]
for n in [3,4,5]:
 units=[a for a in range(n) if gcd(a,n)==1]
 P=list(permutations(range(n)));unseen=set(product(P,P));reps=[];fixed=[]
 def orbit(p,q):
  return {(tuple((a*t+x)%n for t in p),tuple((pow(a,-1,n)*t+y)%n for t in q)) for a in units for x in range(n) for y in range(n)}
 while unseen:
  p,q=min(unseen);o=orbit(p,q);assert len(o)==n*n*len(units)
  unseen.difference_update(o);reps.append((p,q))
  tau=(p[::-1],tuple((-t)%n for t in q[::-1]))
  if tau in o:fixed.append((p,q))
 expected=factorial(n)**2//(n*n*len(units));assert len(reps)==expected
 # A separate computation counts affine maps of precisely the reversal cycle type.
 def reversal_type(a,b):
  f=[(a*t+b)%n for t in range(n)]
  return all(f[f[t]]==t for t in range(n)) and sum(f[t]==t for t in range(n))==n%2
 pairs=sum(reversal_type(a,x) and reversal_type((-pow(a,-1,n))%n,(-y)%n) for a in units for x in range(n) for y in range(n))
 centralizer=2**(n//2)*factorial(n//2)
 assert len(fixed)*n*n*len(units)==pairs*centralizer**2
 print('A'+str(n-1),'all pairs',len(P)**2,'pair normalizer',n*n*len(units),'inner classes',len(reps),'Aut=C2',len(fixed),'Aut=1',len(reps)-len(fixed))
 reports.append({'n':n,'inner_classes':len(reps),'outer_fixed':len(fixed),'trivial_automorphism':len(reps)-len(fixed),'class_representatives':reps,'C2_representatives':fixed,'affine_involution_pairs':pairs})
out=Path(__file__).resolve().parents[1]/'logs';(out/'type_a_outer_stabilizers.json').write_text(json.dumps(reports,indent=2))
print('PASS: exhaustive orbit enumeration agrees with independent affine-involution count')
print('Elapsed seconds',perf_counter()-start)
