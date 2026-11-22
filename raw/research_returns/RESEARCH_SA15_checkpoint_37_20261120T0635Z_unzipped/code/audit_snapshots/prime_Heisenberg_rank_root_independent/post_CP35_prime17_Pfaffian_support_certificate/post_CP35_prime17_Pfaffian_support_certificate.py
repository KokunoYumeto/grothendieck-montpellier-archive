"""Universal N=17 maximal-Pfaffian support certificate in characteristic two.
Packed four-bit exponents are sufficient because total degree is eight.
The output supplies an exact monomial coefficient for every covered support.
"""
from pathlib import Path
from datetime import datetime,timezone
from collections import defaultdict
import json,time,resource
started=time.perf_counter(); n=17;m=8;inv2=9
edges={}
for i in range(1,n):
 for j in range(i+1,n):
  d=(j-i)%n;d=min(d,n-d)
  edges[i,j]=(1<<(4*(d-1)),1<<(4*(((i+j)*inv2)%n)))
coeffs={}; matching_count=0

def enumerate_pairs(items,cm=0,ym=0):
 global matching_count
 if not items:
  terms=coeffs.setdefault(ym,set())
  if cm in terms:terms.remove(cm)
  else:terms.add(cm)
  matching_count+=1
  return
 i=items[0]
 for q in range(1,len(items)):
  j=items[q];dc,dy=edges[i,j]
  enumerate_pairs(items[1:q]+items[q+1:],cm+dc,ym+dy)

enumerate_pairs(tuple(range(1,n)))
assert matching_count==2027025
coefficient_time=time.perf_counter()-started
coeffs={y:cs for y,cs in coeffs.items() if cs}

def support(c):return sum(1<<i for i in range(m) if c>>(4*i)&15)
def unpack(c,length):return [(c>>(4*i))&15 for i in range(length)]
remaining=set(range(1,1<<m));witnesses={}
# Short coefficients first.  Every test is a literal coefficient restriction.
for y,terms in sorted(coeffs.items(),key=lambda z:(len(z[1]),z[0])):
 data=[(support(c),c) for c in sorted(terms)]
 for mask in tuple(sorted(remaining)):
  alive=[c for cm,c in data if cm&~mask==0]
  if len(alive)==1:
   witnesses[mask]={'support_mask':mask,'nonzero_distances':[i+1 for i in range(m) if mask>>i&1],'y_monomial':unpack(y,n),'surviving_c_monomial':unpack(alive[0],m),'full_unrestricted_c_coefficient':[unpack(c,m) for c in sorted(terms)]}
   remaining.remove(mask)
 if not remaining:break
result={'status':'PASS' if not remaining else 'PARTIAL-SUPPORT-CERTIFICATE','actual_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-started,'coefficient_reconstruction_seconds':coefficient_time,'prime':n,'cofactor_deleted_index':0,'matching_count':matching_count,'nonzero_y_coefficient_count':len(coeffs),'full_polynomial_term_count':sum(map(len,coeffs.values())),'support_count':255,'monomial_witness_count':len(witnesses),'monomial_witnesses':[witnesses[s] for s in sorted(witnesses)],'uncovered_supports':sorted(remaining),'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Every recorded coefficient is reconstructed from all15!! perfect matchings over F2. On its exact nonempty coefficient support, the restricted coefficient is a single nonzero monomial. A complete support list proves generic dual rank16 for every nonzero alternating Heisenberg parameter over any characteristic-two field; no multiplication-rank conclusion.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='monomial_witnesses'}))
