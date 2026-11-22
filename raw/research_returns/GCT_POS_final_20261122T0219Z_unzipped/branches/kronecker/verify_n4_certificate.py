"""Exact checker. Does not import SciPy or trust floating point feasibility."""
from itertools import combinations_with_replacement,product
from collections import Counter
from fractions import Fraction
from pathlib import Path
import json
p=Path(__file__).resolve().parent
obj=json.loads((p/'dyadic_n4_exact_certificate.json').read_text())
M=8;n=4

def key(A,B,C):
 d=(sum(A)+sum(B)+sum(C))%8
 u=next(k for k in (1,3,5,7) if k*d%8==1)
 out=[]
 for e in product(set(A),set(B),set(C)):
  if sum(e)%8:continue
  out.append(tuple(sorted(tuple(sorted((u*(v-e[j]))%8 for v in X)) for j,X in enumerate((A,B,C)))))
 return min(out)

def encoded(x):return tuple(tuple(v) for v in x)
cert={encoded(r['spectra']):('positive',r) for r in obj['records']}
cert.update({encoded(r['spectra']):('negative',r) for r in obj['exclusions']})
assert len(cert)==2285
positive=negative=0
for K,(kind,r) in cert.items():
 sets=[sorted(set(X)) for X in K]; mult=[Counter(X) for X in K]
 E=[e for e in product(*sets) if sum(e)%8==0]
 rows=[(j,v) for j in range(3) for v in sets[j]]
 if kind=='positive':
  assert r['aggregate_support']==[list(e) for e in E]
  vals=list(map(Fraction,r['aggregate_positive_masses']))
  assert len(vals)==len(E) and all(t>0 for t in vals)
  assert all(sum(vals[k] for k,e in enumerate(E) if e[j]==v)==mult[j][v] for j,v in rows)
  positive+=1
 else:
  assert r['rows']==[list(x) for x in rows]
  y=list(map(Fraction,r['dual']));yd=dict(zip(rows,y))
  assert all(sum(yd[j,e[j]] for j in range(3))>=0 for e in E)
  assert sum(yd[j,v]*mult[j][v] for j,v in rows)<0
  negative+=1
S=[X for X in combinations_with_replacement(range(8),4) if X[0]==0]
covered=set(); examined=0
for A,B,C in combinations_with_replacement(S,3):
 if (sum(A)+sum(B)+sum(C))%2==0:continue
 E=[e for e in product(set(A),set(B),set(C)) if sum(e)%8==0]
 if any(set(e[j] for e in E)!=set(X) for j,X in enumerate((A,B,C))):continue
 K=key(A,B,C);assert K in cert
 covered.add(K);examined+=1
assert covered==set(cert)
print(json.dumps({'result':'PASS','covered_multiset_triples':examined,'spectral_orbits':len(covered),'positive_certificates':positive,'Farkas_certificates':negative},indent=2))
