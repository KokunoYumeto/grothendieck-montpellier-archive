"""Exact exploratory prime-five wall diagnostic; no geometric promotion."""
from pathlib import Path
from functools import lru_cache
from itertools import permutations
from datetime import datetime, timezone
import json,time,traceback

OUT=Path(__file__).with_suffix('.output.json')
assert not OUT.exists(), 'Preserve prior output before rerun'
start=time.perf_counter();NV=7;ONE=frozenset({(0,)*NV});ZERO=frozenset()
def var(i):
 e=[0]*NV;e[i]=1;return frozenset({tuple(e)})
def add(*ps):
 r=set()
 for p in ps:r.symmetric_difference_update(p)
 return frozenset(r)
def mul(p,q):
 r=set()
 for a in p:
  for b in q:
   e=tuple(x+y for x,y in zip(a,b))
   if e in r:r.remove(e)
   else:r.add(e)
 return frozenset(r)
def power(p,n):
 r=ONE
 while n:
  if n&1:r=mul(r,p)
  p=mul(p,p);n//=2
 return r
def det(M):
 n=len(M);r=ZERO
 for perm in permutations(range(n)):
  t=ONE
  for i,j in enumerate(perm):t=mul(t,M[i][j])
  r=add(r,t)
 return r
def divide_var(p,j):
 assert all(e[j]>0 for e in p)
 return frozenset(tuple(v-int(i==j) for i,v in enumerate(e)) for e in p)
def pp(p):return [list(e) for e in sorted(p)]
def group_y(p):
 d={}
 for e in p:d.setdefault(e[2:],set()).add(e[:2])
 return d
def cmul(p,q):
 r=set()
 for a in p:
  for b in q:
   e=(a[0]+b[0],a[1]+b[1])
   if e in r:r.remove(e)
   else:r.add(e)
 return r
def specialize_c1_one(p):
 r=0
 for a,b in p:r^=1<<b
 return r
def prem(a,b):
 while a and a.bit_length()>=b.bit_length():a^=b<<(a.bit_length()-b.bit_length())
 return a
def pgcd(a,b):
 while b:a,b=b,prem(a,b)
 return a

try:
 c=[ZERO,var(0),var(1)];y=[var(i+2) for i in range(5)]
 dist=lambda z:min(z%5,(-z)%5)
 B=[[ZERO if i==j else mul(c[dist(i-j)],y[(3*(i+j))%5]) for j in range(5)] for i in range(5)]
 @lru_cache(None)
 def pf(vertices):
  if not vertices:return ONE
  i=vertices[0];r=ZERO
  for j in vertices[1:]:r=add(r,mul(B[i][j],pf(tuple(v for v in vertices if v not in (i,j)))))
  return r
 sigma=[pf(tuple(i for i in range(5) if i!=j)) for j in range(5)]
 M=[[ZERO if k==j else mul(c[dist(2*(k-j))],y[(2*k-j)%5]) for j in range(5)] for k in range(5)]
 tau=[]
 for j in range(5):
  cofactor=det([[M[r][s] for s in range(1,5)] for r in range(5) if r!=j])
  tau.append(divide_var(cofactor,2))
 for i in range(5):
  for j in range(5):
   cofactor=det([[M[r][s] for s in range(5) if s!=i] for r in range(5) if r!=j])
   assert cofactor==mul(y[i],tau[j])
 @lru_cache(None)
 def spow(j,n):return power(sigma[j],n)
 def compose(p):
  out=ZERO
  for e in p:
   t=frozenset({e[:2]+(0,)*5})
   for j,n in enumerate(e[2:]):t=mul(t,spow(j,n))
   out=add(out,t)
  return out
 composed=[compose(t) for t in tau]
 exceptional=[divide_var(t,j+2) for j,t in enumerate(composed)]
 assert all(f==exceptional[0] for f in exceptional)
 E=exceptional[0]
 Q=add(*(mul(y[i],power(sigma[i],2)) for i in range(5)))
 assert Q and E
 qg,eg=group_y(Q),group_y(E)
 pivot=next(k for k,v in sorted(qg.items()) if v=={(4,0)})
 equations=[];g=0
 for mon in sorted(set(qg)|set(eg)):
  coeff=cmul(eg.get(mon,set()),qg[pivot])^cmul(qg.get(mon,set()),eg.get(pivot,set()))
  value=specialize_c1_one(coeff)
  if value:equations.append({'y_monomial':list(mon),'coefficient_c1_c2':sorted(map(list,coeff)),'c1_one_binary':value});g=pgcd(g,value)
 e_gcd=0
 for coeff in eg.values():e_gcd=pgcd(e_gcd,specialize_c1_one(coeff))
 data={'variable_order':['c1','c2','y0','y1','y2','y3','y4'],
       'sigma':[pp(p) for p in sigma],'inverse_tau':[pp(p) for p in tau],
       'Q':pp(Q),'inverse_composition_exceptional_E':pp(E),
       'Q_terms':len(Q),'E_terms':len(E),'Q_E_proportionality_pivot_y':list(pivot),
       'nonzero_coefficient_equations':equations,
       'c1_one_proportionality_gcd_binary':g,
       'c1_one_E_coefficient_gcd_binary':e_gcd,
       'checked_all_25_adjugate_entries':True,'checked_all_five_inverse_compositions':True}
 status='PASS';error=None
except Exception:
 status='FAIL';error=traceback.format_exc();data={}
record={'status':status,'actual_utc':datetime.now(timezone.utc).isoformat(),
 'runtime_seconds':time.perf_counter()-start,'data':data,'error':error,
 'scope':'Exploratory exact universal p5 polynomial identities and proportionality locus only. No wall, local inertia, primitive full image, or fixed principal-degree assertion is promoted by this run.'}
OUT.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='data'},indent=2))
if status=='PASS':print(json.dumps({k:v for k,v in data.items() if k in ['Q_terms','E_terms','c1_one_proportionality_gcd_binary','c1_one_E_coefficient_gcd_binary']},indent=2))
if status!='PASS':raise SystemExit(1)
