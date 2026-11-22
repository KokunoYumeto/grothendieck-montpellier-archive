"""Bounded exact factor diagnostic on the abstract exceptional p5 tensor."""
from pathlib import Path
from datetime import datetime,timezone
import json,time
OUT=Path(__file__).with_suffix('.output.json');assert not OUT.exists()
start=time.perf_counter()
source=Path(__file__).with_name('post_CP36_prime5_wall_diagnostic.output.json')
data=json.loads(source.read_text())['data']
Q={}
for e in data['Q']:
 y=tuple(e[2:]);Q[y]=Q.get(y,0)^1
Q={e:c for e,c in Q.items() if c}
def fm(a,b):
 r=0
 while b:
  if b&1:r^=a
  b>>=1;a<<=1
  if a&16:a^=19
 return r
def fp(a,n):
 r=1
 while n:
  if n&1:r=fm(r,a)
  a=fm(a,a);n//=2
 return r
z=fp(2,3);assert fp(z,5)==1 and z!=1
def mul(p,q):
 r={}
 for a,c in p.items():
  for b,d in q.items():
   e=tuple(x+y for x,y in zip(a,b));r[e]=r.get(e,0)^fm(c,d)
 return {e:c for e,c in r.items() if c}
rows=[]
for a in range(5):
 P={(0,)*5:1}
 for b in range(5):
  L={tuple(int(i==j) for i in range(5)):fp(z,(a*j*j+b*j)%5) for j in range(5)}
  P=mul(P,L)
 rows.append({'slope':a,'product_terms':len(P),'equals_Q':P==Q})
record={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,'exceptional_Q_terms':len(Q),'rows':rows,'scope':'Exact comparison only with the five Gaussian eigenbasis products at c1=c2=1 over explicit F16. No general factorization, actual Cartier realization, or geometric conclusion.'}
OUT.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
