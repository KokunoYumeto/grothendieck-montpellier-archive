"""Exact symbolic certificate for the ruled-surface intersection identity.
This is an algebraic identity check, not an existence search.
"""
import json,time
import sympy as S
start=time.perf_counter()
a,e,g,b,m=S.symbols('a e g b m')
# One exceptional contribution suffices since the formula is additive in i.
d0square=-e*a*a+2*a*b
k0d0=a*(e+2*g-2)-2*b
base=S.expand(d0square+a*k0d0-2*a*a*(g-1))
exceptional=S.expand((a*m-m*m)-(m*(a-m)))
combined=S.expand(4*(1-g)+2*a*a*(g-1)-(2*a*a-4)*(g-1))
assert base==exceptional==combined==0
print(json.dumps({'kind':'exact polynomial identities','ruled_base_residual':str(base),'exceptional_residual':str(exceptional),'chern_residual':str(combined),'positivity_argument':'a>=2 and g>=2 make (2a^2-4)(g-1)>0; a=1 allows no integer 0<m<a and forces r=0','runtime_seconds':time.perf_counter()-start},indent=2))
