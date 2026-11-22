"""Universal multiplication cofactor for cyclic alternating Heisenberg tensors.
M_s(k,j)=c_(2(k-j))*s_(2k-j), c_-a=c_a,c_0=0.
This is a different matrix from the alternating dual contraction.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,time,resource
started=time.perf_counter()

def compute(n):
 m=(n-1)//2;bits=5;maskexp=(1<<bits)-1
 entries={}
 for k in range(1,n):
  for j in range(1,n):
   d=(2*(k-j))%n;d=min(d,n-d)
   if d:entries[k,j]=(1<<(bits*(d-1)),1<<(bits*((2*k-j)%n)))
 coeffs={};count=0
 def expand(row,cols,cm=0,sm=0):
  nonlocal count
  if row==n:
   terms=coeffs.setdefault(sm,set())
   if cm in terms:terms.remove(cm)
   else:terms.add(cm)
   count+=1;return
  for j in cols:
   if row==j:continue
   dc,ds=entries[row,j]
   expand(row+1,cols-{j},cm+dc,sm+ds)
 expand(1,set(range(1,n)))
 coeffs={s:cs for s,cs in coeffs.items() if cs}
 def support(c):return sum(1<<i for i in range(m) if c>>(bits*i)&maskexp)
 def unpack(c,l):return [(c>>(bits*i))&maskexp for i in range(l)]
 # Euler gives the deleted-column factor s0 in this cofactor.
 assert all(s&maskexp for s in coeffs)
 remaining=set(range(1,1<<m));witnesses={}
 for s,terms in sorted(coeffs.items(),key=lambda z:(len(z[1]),z[0])):
  data=[(support(c),c) for c in sorted(terms)]
  for mask in tuple(sorted(remaining)):
   alive=[c for cm,c in data if cm&~mask==0]
   if len(alive)==1:
    witnesses[mask]={'support_mask':mask,'nonzero_distances':[i+1 for i in range(m) if mask>>i&1],'s_monomial':unpack(s,n),'surviving_c_monomial':unpack(alive[0],m),'full_unrestricted_c_coefficient':[unpack(c,m) for c in sorted(terms)]}
    remaining.remove(mask)
  if not remaining:break
 return {'n':n,'determinant_terms_before_cancellation':count,'nonzero_s_coefficient_count':len(coeffs),'polynomial_term_count':sum(map(len,coeffs.values())),'support_count':(1<<m)-1,'monomial_witnesses':[witnesses[s] for s in sorted(witnesses)],'uncovered_supports':sorted(remaining),'small_full_coefficients':[{'s':unpack(s,n),'c':[unpack(c,m) for c in sorted(cs)]} for s,cs in sorted(coeffs.items())] if n<=7 else None}

rows=[]
for n in (3,5,7,11):
 row=compute(n);rows.append(row)
 print(json.dumps({'finished_n':n,'terms':row['polynomial_term_count'],'uncovered_supports':row['uncovered_supports'],'elapsed':time.perf_counter()-started}),flush=True)
result={'status':'PASS' if all(not r['uncovered_supports'] for r in rows) else 'PARTIAL','actual_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-started,'results':rows,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Exact characteristic-two determinant of M_s with row0/column0 deleted. Every support witness is a coefficient surviving as one nonzero c-monomial. This certifies generic multiplication rank n-1 for covered supports, independently of dual rank. No full geometric monodromy conclusion.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='results'}))
