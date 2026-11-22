#!/usr/bin/env python3
"""Independent exact arithmetic for the whole D-OL01--03 peer audit.

No author checker or arithmetic output is imported. Source formulas are
transcribed from the published propositions and checked symbolically.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,time
import sympy as s

start=time.perf_counter()
base=Path(__file__).resolve().parent
proof=base.parents[1]/'imprimitive/orthogonal_levels/orthogonal_level_section.tex'
assert proof.exists()
sigma=F(1,10**29); level_cutoff=10**30; degree_constant=2*10**29
assert F(1,6507*2**21*10**18)>7*sigma
assert sigma*degree_constant==2 and level_cutoff//5==degree_constant

m,d,L,z=s.symbols('m d L z')
E=lambda x:x*x/8-x/4-2
source_exponents={
 'odd_spin':m*(m+1)/2-2,
 'even_spin':m*(m-1)/2-2,
 'odd_SO_failure':m*m/2-1,
 'even_SO_failure':m*(m-1)/2-2,
}
gaps={k:s.expand(v-E(2*m+(1 if k.startswith('odd') else 0))) for k,v in source_exponents.items()}
assert gaps=={'odd_spin':m/2+s.Rational(1,8),'even_spin':0,'odd_SO_failure':s.Rational(9,8),'even_SO_failure':0}

# Uniform large-d polynomial, then make positivity coefficientwise at L>=10.
expr=s.expand(E(2*L+z)-s.Rational(1,5)*L*(2*L+z))
assert s.expand(expr-(L*L/10-L/2-2+(3*L/10-s.Rational(1,4))*z+z*z/8))==0
translated=s.Poly(s.expand(expr.subs(L,10+m)),m,z)
assert all(c>0 for c in translated.coeffs())

# Independent verification of the ceiling bound used in the level proof.
k_upper=d/6+s.Rational(2,3)
assert s.expand(d-2*k_upper-2-3*d/5-(d-50)/15)==0
pairs=0
for dim in range(50,301):
 for ell in range(1,dim//2+1):
  k=1+(ell-1)//3
  assert 3*(k-1)<ell<=3*k
  assert k*(dim-2*k-2)>=F(dim*ell,5)
  pairs+=1
for ell in (level_cutoff,level_cutoff+1,level_cutoff+2):
 for dim in (2*ell,2*ell+1,3*ell):
  k=1+(ell-1)//3
  assert F(dim*ell,5)>=degree_constant*dim
  assert k*(dim-2*k-2)>=degree_constant*dim

# Trace -> moving rank -> arbitrary normalizer -> actual source budget.
ratio=F(1,4)
support=(1-ratio)/4
assert support==F(3,16)<F(1,4)
ceiling=6/(12*support-2)
assert ceiling==24

out={'status':'PASS','scope':'independent exact arithmetic and polynomial identities; no group or classification reconstruction','proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'sigma':str(sigma),'degree_constant':degree_constant,'level_cutoff':level_cutoff,'spin_dimension_cutoff':2*level_cutoff,'source_exponent_gaps':{k:str(v) for k,v in gaps.items()},'positive_shifted_polynomial':str(translated.as_expr()),'finite_boundary_pairs':pairs,'normalizer_support':str(support),'source_degree_ceiling':str(ceiling),'elapsed_seconds':time.perf_counter()-start}
(base/'audit_orthogonal_levels.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
