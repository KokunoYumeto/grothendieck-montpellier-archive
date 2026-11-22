"""Exact exploratory remainder of the universal Moore determinant modulo sum x_i^3.

This tests a new local-Hasse route. It does not assert a Cartier theorem or
infer a full parameter classification from finite-field sampling.
"""
from pathlib import Path
from itertools import product,permutations
from collections import defaultdict,Counter
from functools import lru_cache
from datetime import datetime,timezone
import hashlib,json,time
start=time.perf_counter();w=Path(__file__).resolve().parents[1]
pts=list(product(range(3),repeat=2));idx={v:i for i,v in enumerate(pts)}
plus=[[idx[((a[0]+b[0])%3,(a[1]+b[1])%3)]for b in pts]for a in pts]
minus=[[idx[((a[0]-b[0])%3,(a[1]-b[1])%3)]for b in pts]for a in pts]
entries=[[(1<<(36+4*minus[i][j]))+(1<<(4*plus[i][j]))for j in range(9)]for i in range(9)]
terms=set()
for perm in permutations(range(9)):
 t=sum(entries[i][j]for i,j in enumerate(perm))
 if t in terms:terms.remove(t)
 else:terms.add(t)
coeff=defaultdict(set)
for t in terms:coeff[t&((1<<36)-1)].add(t>>36)
assert len(terms)==55296 and len(coeff)==2080
decode=lambda x:tuple((x>>(4*i))&15 for i in range(9))
encode=lambda es:sum(e<<(4*i)for i,e in enumerate(es))
def mul(a,b):
 result=set()
 for u in a:
  for v in b:
   t=u+v
   if t in result:result.remove(t)
   else:result.add(t)
 return result
S={3<<(4*i)for i in range(1,9)}
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
reduced={x:cs for x,cs in reduced.items()if cs}
assert all((x&15)<3 for x in reduced)
counts={'determinant_permutations':362880,'universal_monomials':len(terms),
 'universal_coefficients':len(coeff),'remainder_coefficients':len(reduced),
 'remainder_monomials':sum(map(len,reduced.values()))}
table=[]
for x,cs in reduced.items():
 table.append((x,[(c,sum(1<<i for i,e in enumerate(decode(c))if e))for c in cs]))
table.sort(key=lambda r:len(r[1]))
excluded=[];survivors=[]
for support in range(1,512):
 witness=None
 for x,cs in table:
  kept=[c for c,s in cs if s&~support==0]
  if len(kept)==1:
   witness={'x_exponents':decode(x),'c_exponents':decode(kept[0])};break
 if witness is None:survivors.append(support)
 else:excluded.append({'support':support,'witness':witness})
counts['single_monomial_excluded_supports']=len(excluded)
counts['surviving_supports']=len(survivors)
def restrict(support):
 result={}
 for x,cs in reduced.items():
  kept={c for c in cs if all(e==0 for i,e in enumerate(decode(c))if i not in support)}
  if kept:result[x]=kept
 return result
old=json.loads((w/'agents/obstructions_crystals/code/verify_Moore_singular_parameter_classification.output.json').read_text())
tests=[('two',set((1,2)),old['two_support_factor'])]
tests += [('four_'+str(i),set((1,2,3,6)),v)for i,v in enumerate(old['four_support_factors'])]
six=old['six_support_factors']
tests += [('six_product',set(range(3,9)),six['product_equality_cube']),
 ('six_sum',set(range(3,9)),six['sum_of_cubes_equality_cube'])]
tests += [('six_matching_'+str(i),set(range(3,9)),v)for i,v in enumerate(six['cyclic_matching_products'])]
factors=[]
for name,support,v in tests:
 target={encode(e)for e in v['c_terms']};rr=restrict(support)
 found=[decode(x)for x,cs in rr.items()if cs==target]
 factors.append({'name':name,'same_factor_is_actual_remainder_coefficient':bool(found),
 'coefficient_locators':found,'desired_c_terms':v['c_terms']})
r8=restrict(set(range(1,9)));pairs=[(1,2),(3,6),(4,8),(5,7)]
cube_factors=[]
for a,b in pairs:
 found=[]
 for x,cs in r8.items():
  if len(cs)!=2:continue
  es=[decode(c)for c in cs];common=tuple(min(es[0][i],es[1][i])for i in range(9))
  residual={tuple(e[i]-common[i]for i in range(9))for e in es}
  expected={tuple(3 if i==a else 0 for i in range(9)),tuple(3 if i==b else 0 for i in range(9))}
  if residual==expected:found.append({'x_exponents':decode(x),'common':common})
 cube_factors.append({'pair':[a,b],'found':found})
roots=[1,2,3];characters={tuple(sum(l*v for l,v in zip(ell,pts[a]))%3 for a,b in pairs)for ell in pts}
phases=[]
decoded={x:[decode(c)for c in cs]for x,cs in r8.items()}
for phase in product(range(3),repeat=4):
 nonzero=0;witness=None
 for x,cs in decoded.items():
  values={}
  for c in cs:
   d=tuple(c[a]+c[b]for a,b in pairs)
   exponent=sum(phase[j]*c[a]for j,(a,b)in enumerate(pairs))%3
   values[d]=values.get(d,0)^roots[exponent]
   if values[d]==0:del values[d]
  if values:
   nonzero+=1
   if len(values)==1 and witness is None:
    d,scalar=next(iter(values.items()));witness={'x_exponents':decode(x),'d_exponents':d,'F4_scalar':scalar}
 phases.append({'phase':phase,'character':phase in characters,'nonzero_remainder_coefficients':nonzero,'monomial_witness':witness})
counts['phase_choices_with_zero_remainder']=sum(r['nonzero_remainder_coefficients']==0 for r in phases)
counts['phase_choices_with_monomial_exclusion']=sum(r['monomial_witness']is not None for r in phases)
out={'status':'EXACT_EXPLORATORY_REMAINDER_COMPLETE','actual_utc':datetime.now(timezone.utc).isoformat(),
 'runtime_seconds':time.perf_counter()-start,'counts':counts,
 'surviving_support_counts':dict(Counter(s.bit_count()for s in survivors)),
 'surviving_supports':survivors,'excluded_supports':excluded,
 'original_proof_factors_after_reduction':factors,'eight_support_cube_factors':cube_factors,
 'eight_support_phase_results':phases,
 'remainder_table_sha256':hashlib.sha256(json.dumps({hex(x):sorted(map(hex,cs))for x,cs in sorted(reduced.items())},sort_keys=True).encode()).hexdigest(),
 'scope':'Universal exact polynomial division by monic Fermat polynomial sum x_i^3, with x0 eliminated. This is an exploratory algebraic probe; the determinant classification has not automatically been extended to this larger divisibility locus. No geometric or local-inertia conclusion is asserted.'}
dest=Path(__file__).with_suffix('.output.json');assert not dest.exists()
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k]for k in('status','actual_utc','runtime_seconds','counts','surviving_support_counts')},indent=2))
