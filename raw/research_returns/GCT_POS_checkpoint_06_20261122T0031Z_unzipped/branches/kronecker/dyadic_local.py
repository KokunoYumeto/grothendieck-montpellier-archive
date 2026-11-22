import json,sympy as s
from collections import Counter
from pathlib import Path
p=Path(__file__).resolve().parent
z=s.Symbol('z');phi=z**4+1
obj=json.loads((p/'dyadic_n4_classification.json').read_text())
def mul(A,B): return s.rem(A*B,phi,z)
def prod(exps):
 r=s.Integer(1)
 for e in exps:
  if e%8:r=mul(r,1-z**(e%8))
 return r
for i,r in enumerate(obj['records']):
 A,B,C=r['spectra']
 num=prod([a-b for X in [A,B,C] for a in X for b in X if a!=b])
 den=prod([a+b+c for a in A for b in B for c in C if (a+b+c)%8])
 coeff=mul(num,s.invert(den,phi,z))
 r['local_coefficient']=str(coeff)
 r['local_complex']=str(s.N(coeff.subs(z,s.exp(s.pi*s.I/4)),20))
 print(i+1,'num',num,'den',den,'local',coeff,'complex',r['local_complex'])
(p/'dyadic_n4_local.json').write_text(json.dumps(obj,indent=2))
