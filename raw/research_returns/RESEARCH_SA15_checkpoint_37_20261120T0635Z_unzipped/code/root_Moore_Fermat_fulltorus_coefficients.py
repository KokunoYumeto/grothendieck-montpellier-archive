"""Exact full-torus coefficient analysis of D_c(x) modulo sum(x_i^3).

Exploratory certificate only. All polynomial construction and data are retained.
No geometric conclusion or finite-field extrapolation is asserted.
"""
from pathlib import Path
from itertools import product, permutations
from collections import defaultdict, Counter
from functools import lru_cache
from datetime import datetime, timezone
import hashlib, json, time
start=time.perf_counter();w=Path(__file__).resolve().parents[1]
pts=list(product(range(3),repeat=2));idx={v:i for i,v in enumerate(pts)}
plus=[[idx[((a[0]+b[0])%3,(a[1]+b[1])%3)] for b in pts] for a in pts]
minus=[[idx[((a[0]-b[0])%3,(a[1]-b[1])%3)] for b in pts] for a in pts]
entries=[[(1<<(36+4*minus[i][j]))+(1<<(4*plus[i][j])) for j in range(9)] for i in range(9)]
terms=set()
for perm in permutations(range(9)):
 t=sum(entries[i][j] for i,j in enumerate(perm))
 if t in terms:terms.remove(t)
 else:terms.add(t)
coeff=defaultdict(set)
for t in terms:coeff[t&((1<<36)-1)].add(t>>36)
assert len(terms)==55296 and len(coeff)==2080
decode=lambda x:tuple((x>>(4*i))&15 for i in range(9))
encode=lambda es:sum(e<<(4*i) for i,e in enumerate(es))
def mul(a,b):
 result=set()
 for u in a:
  for v in b:
   t=u+v
   if t in result:result.remove(t)
   else:result.add(t)
 return result
S={3<<(4*i) for i in range(1,9)}
powers=[{0}]
for j in range(3):powers.append(mul(powers[-1],S))
@lru_cache(None)
def remainder(x):
 q,r=divmod(x&15,3)
 rest=x-(x&15)+r
 return {rest+t for t in powers[q]}
reduced=defaultdict(set)
for x,cs in coeff.items():
 for xr in remainder(x):reduced[xr].symmetric_difference_update(cs)
reduced={x:cs for x,cs in reduced.items() if cs}
assert len(reduced)==1085 and sum(map(len,reduced.values()))==47349
normal=defaultdict(list)
for x,cs in sorted(reduced.items()):
 es=[decode(c) for c in sorted(cs)]
 common=tuple(min(e[i] for e in es) for i in range(9))
 residual=tuple(sorted(tuple(e[i]-common[i] for i in range(9)) for e in es))
 normal[residual].append({'x_exponents':decode(x),'removed_c_monomial':common})
cube=[];small=[];records=[]
for es,locators in sorted(normal.items(),key=lambda v:(len(v[0]),v[0])):
 item={'terms':es,'locators':locators}
 records.append(item)
 if all(all(e%3==0 for e in mon) for mon in es):
  cube.append({'z_terms':[tuple(e//3 for e in mon) for mon in es],'locators':locators})
 if len(es)<=8:small.append(item)
table=w/'outputs/root_Moore_Fermat_fulltorus_normalized_coefficients.json'
assert not table.exists()
table.write_text(json.dumps(records,separators=(',',':'))+'\n')
out={
 'status':'EXACT_EXPLORATORY_FULL_TORUS_COEFFICIENTS',
 'actual_utc':datetime.now(timezone.utc).isoformat(),
 'runtime_seconds':time.perf_counter()-start,
 'counts':{'universal_permutations':362880,'universal_monomials':len(terms),
  'remainder_coefficients':len(reduced),'remainder_monomials':sum(map(len,reduced.values())),
  'distinct_coefficients_after_dividing_monomial':len(normal),
  'pure_cube_polynomials':len(cube),'at_most_eight_terms':len(small)},
 'term_count_histogram':dict(sorted(Counter(map(len,normal)).items())),
 'pure_cube_coefficients':cube,
 'small_coefficients':small,
 'normalized_table':str(table.relative_to(w)),
 'normalized_table_sha256':hashlib.sha256(table.read_bytes()).hexdigest(),
 'scope':'Exact characteristic-two coefficient conditions on the full c-coordinate torus. Dividing a c-monomial is legitimate only there. No solution classification or Cartier/Hasse conclusion follows from this data alone.'
}
dest=Path(__file__).with_suffix('.output.json');assert not dest.exists()
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','actual_utc','runtime_seconds','counts','term_count_histogram')},indent=2))
print('PURE CUBE CONDITIONS')
for item in cube:
 print(json.dumps({'z_terms':item['z_terms'],'first_locator':item['locators'][0]}))
