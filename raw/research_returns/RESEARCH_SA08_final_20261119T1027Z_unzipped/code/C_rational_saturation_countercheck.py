"""C35 finite simplex-two certificate over Z, then Z_(2).
Basis: T^[a] U^[b] V^[c] times dU^e dV^f. All coefficients exact.
"""
from math import comb
from pathlib import Path
import json,time
start=time.monotonic();ROOT=Path(__file__).resolve().parents[1]
def add(a,b):
 out=dict(a)
 for m,c in b.items():out[m]=out.get(m,0)+c
 return {m:c for m,c in out.items() if c}
def mul(a,b):
 out={}
 for (i,j,l,e,f),c in a.items():
  for (I,J,L,E,F),C in b.items():
   if e+E>1 or f+F>1:continue
   m=(i+I,j+J,l+L,e+E,f+F)
   v=c*C*comb(i+I,i)*comb(j+J,j)*comb(l+L,l)*(-1)**(f*E)
   out[m]=out.get(m,0)+v
 return {m:c for m,c in out.items() if c}
def d(a):
 out={}
 for (i,j,l,e,f),c in a.items():
  if j and not e:out=add(out,{(i,j-1,l,1,f):c})
  if l and not f:out=add(out,{(i,j,l-1,e,1):c*(-1)**e})
 return out
x1={(0,1,0,1,0):1};x2={(0,0,1,0,1):1}
assert d(x1)==d(x2)=={}
c=mul(x1,x2)
assert c=={(0,1,1,1,1):1} and d(c)=={}
assert mul(x2,x1)=={m:-v for m,v in c.items()}
basis=[(a,b,2-a-b,1,1) for a in range(3) for b in range(3-a)]
assert len(basis)==6 and (0,1,1,1,1) in basis
vec=[c.get(m,0) for m in basis]
assert any(v%2 for v in vec)
# Exhaustive differential and Leibniz checks in the finite weight <=4 window.
mon=[]
for a in range(5):
 for b in range(5-a):
  for l in range(5-a-b):
   for e in range(2):
    for f in range(2):
     if a+b+l+e+f<=4:mon.append((a,b,l,e,f))
count=0
for m in mon:
 assert d(d({m:1}))=={}
 for n in mon:
  if sum(m)+sum(n)>4:continue
  lhs=d(mul({m:1},{n:1}))
  rhs=add(mul(d({m:1}),{n:1}),{r:(-1)**(m[3]+m[4])*v for r,v in mul({m:1},d({n:1})).items()})
  assert lhs==rhs;count+=1
out={'statement':'C35','all_checks_passed':True,'monomials':len(mon),'Leibniz_pairs':count,
 'weight4_form2_basis':[list(m) for m in basis],'product_vector':vec,
 'obstruction':'Coordinate UV dU dV requires 2*v=1 in Z_(2), impossible.',
 'seconds':time.monotonic()-start}
(ROOT/'logs/C_rational_saturation_countercheck.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
