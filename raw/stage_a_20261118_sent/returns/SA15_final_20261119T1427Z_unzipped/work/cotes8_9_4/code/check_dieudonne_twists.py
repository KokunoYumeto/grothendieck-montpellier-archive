"""Nontrivial coefficient-twist certificate over W2(F9)=Z/9[a]/(a²−2)."""
from pathlib import Path
from itertools import product
import json
W=Path(__file__).resolve().parents[1]
def sigma(x):return(x[0],(-x[1])%9)
def add(x,y):return((x[0]+y[0])%9,(x[1]+y[1])%9)
def mul(x,y):return((x[0]*y[0]+2*x[1]*y[1])%9,(x[0]*y[1]+x[1]*y[0])%9)
def timesp(x):return mul((3,0),x)
E=list(product(range(9),repeat=2))
for a in E:
    for b in E:
        assert sigma(add(a,b))==add(sigma(a),sigma(b))
        assert sigma(mul(a,b))==mul(sigma(a),sigma(b))
    # z=bV is the only positive-V monomial contributing tophi(Fz).
    assert timesp(sigma(a))==sigma(timesp(a))
    # z=aF givesphi(zV)=pa andphi(Vz)=p sigma^-1(a).
    assert timesp(a)==sigma(timesp(sigma(a)))
assert sigma((0,1))==(0,8)
assert timesp((1,0))==(3,0)!=(0,0)
out={'ring':'Z/9[a]/(a²−2), unramifiedquadratic, sigma(a)=−a',
'coefficient_count':len(E),'ring_automorphism_pairs_checked':len(E)**2,
'F_and_V_coefficient_identities_checked':len(E),
'phi_FV':timesp((1,0)),'cancelled_zero_formula_false':True,
'scope':'Exactmonomial twist check, not a general dualizing-bimodule theorem.'}
(W/'outputs/dieudonne_twists.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
