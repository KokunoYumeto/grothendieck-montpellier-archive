"""Exact finite polynomial checks for the characteristic-two swap local model.

This checks only the displayed finite algebra and intersection identities.
It does not certify the geometric contraction, completion, or fundamental group.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
root=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def check(value):
 global checks
 assert value
 checks+=1
zero=frozenset();one=frozenset({(0,0)});u=frozenset({(1,0)});v=frozenset({(0,1)})
def add(a,b):return a^b
def mul(a,b):
 out=set()
 for i,j in a:
  for k,l in b:
   t=(i+k,j+l)
   if t in out:out.remove(t)
   else:out.add(t)
 return frozenset(out)
def aadd(a,b):return(add(a[0],b[0]),add(a[1],b[1]))
def amul(a,b):
 return(add(mul(a[0],b[0]),mul(mul(a[1],b[1]),v)),
        add(add(mul(a[0],b[1]),mul(a[1],b[0])),mul(mul(a[1],b[1]),u)))
def sigma(a):return(add(a[0],mul(a[1],u)),a[1])
az=(zero,zero);aone=(one,zero);x=(zero,one)
check(aadd(aadd(amul(x,x),(zero,u)),(v,zero))==az)
check(sigma(sigma(x))==x)
check(aadd(x,sigma(x))==(u,zero))
check(amul(x,sigma(x))==(v,zero))
coeff=[frozenset(t for i,t in enumerate([(0,0),(1,0),(0,1)]) if bits&(1<<i)) for bits in range(8)]
elements=[(a,b) for a in coeff for b in coeff]
for a in elements:
 check(sigma(sigma(a))==a)
 check((sigma(a)==a)==(a[1]==zero))
 for b in elements:
  check(sigma(amul(a,b))==amul(sigma(a),sigma(b)))
  check(amul(a,b)==amul(b,a))
# The residue polynomial X^2+v has no square root in F2(v): v has odd v-order.
check(next(iter(v))[1]%2==1)
# Formal discriminant of T^2+uT+v in characteristic two is u^2.
check(mul(u,u)==frozenset({(2,0)}))
# Intersection identities and positivity over a finite, stated genus range.
for g in range(2,258):
 delta2=2-2*g;d2=1-g;hd=2*g-2;h2=4*(g-1)**2
 check(delta2==2*d2)
 check(hd+2*d2==0)
 check(h2+4*hd+4*d2==4*g*(g-1))
 check(4*g*(g-1)>0 and d2<0)
record={'utc':datetime.now(timezone.utc).isoformat(),'actor':'GPT-6 Astra Pro; /root; SA12 run1; effort setting not independently exposed',
 'type':'computation or formal certificate','status':'PASS','assertions':checks,
 'scope':'Universal identities in the exact polynomial algebra F2[u,v][x]/(x²+ux+v), all64 coefficient pairs with coefficients in span{1,u,v}, all4096 pair products, and intersection arithmetic for genera2 through257.',
 'excluded_scope':'No computational verification of existence of the curves, semiampleness, Stein contraction, completion connectedness, DVR geometry, or full wild-inertia image; these have separate proofs.',
 'seconds':time.perf_counter()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'code/output/wild_swap_local_certificate_root.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
