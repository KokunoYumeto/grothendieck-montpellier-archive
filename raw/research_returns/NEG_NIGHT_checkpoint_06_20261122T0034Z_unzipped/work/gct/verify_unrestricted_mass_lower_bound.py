"""Independent exact verifier for the unrestricted 61-pair lower bound.

Uses the original supplied trace table, not the LP builder or its floating
solutions. No optimization library is imported. The certificate consists
only of nonnegative integer weights for explicitly reconstructed necessary
associativity inequalities.
"""
from pathlib import Path
import json
from collections import defaultdict
import sympy as sp

names=['mu','Sigma']+[f'g{i}_{w}' for i in (1,2) for w in ('1','12','2','21')]
index={s:i for i,s in enumerate(names)}
v=sp.Symbol('v')
absolute={}
source=json.loads(Path('sources/OURS_E4_scripts/e3_constants.json').read_text())
for entry in source:
    key=tuple(index[entry[k]] for k in ('b','bp','bpp'))
    expr=sp.Poly(sp.expand(sp.sympify(entry['c'],locals={'v':v})*v**64),v)
    assert all((e[0]-64)%2==0 for e,_ in expr.terms())
    assert all(c.is_Integer for _,c in expr.terms())
    absolute[key]=sum(abs(int(c)) for _,c in expr.terms())
assert sum(absolute.values())==4443
for a in range(10):
    for z in range(10):
        assert absolute.get((0,a,z),0)==int(a==z)
        assert absolute.get((a,0,z),0)==int(a==z)
variables={(a,b,z) for a in range(1,10) for b in range(1,10) for z in range(10)}
assert len(variables)==810
certificate=json.loads(Path('work/gct/unrestricted_mass_lower_bound_certificate.json').read_text())
M=certificate['budget_added_mass']
assert M==120
weighted=defaultdict(int)
rhs=0
locators=set()

def reconstruct(terms):
    base=0
    linear=defaultdict(int)
    quadratic_bound=defaultdict(int)
    for u,w in terms:
        au,aw=absolute.get(u,0),absolute.get(w,0)
        base+=au*aw
        if u in variables:linear[u]+=aw
        if w in variables:linear[w]+=au
        if u in variables and w in variables:
            if u==w:
                quadratic_bound[u]+=4
            else:
                quadratic_bound[u]+=1
                quadratic_bound[w]+=1
    return base,linear,quadratic_bound

for row in certificate['weights']:
    weight=row['multiplier']
    assert isinstance(weight,int) and weight>0
    loc=tuple(row['locator'])
    assert loc not in locators
    locators.add(loc)
    a,b,c,z,direction=loc
    assert 1<=a<10 and 1<=b<10 and 1<=c<10 and 0<=z<10
    assert direction in (0,1)
    left=reconstruct([((a,b,y),(y,c,z)) for y in range(10)])
    right=reconstruct([((b,c,y),(a,y,z)) for y in range(10)])
    if direction==1:left,right=right,left
    rhs+=4*weight*(left[0]-right[0])
    for key in set(left[1])|set(right[1])|set(right[2]):
        coefficient=4*(right[1].get(key,0)-left[1].get(key,0))+M*right[2].get(key,0)
        weighted[key]+=weight*coefficient

maximum=max(weighted.get(key,0) for key in variables)
assert len(locators)==74
assert max(row['multiplier'] for row in certificate['weights'])==565
assert rhs==certificate['weighted_rhs']==12209088
assert maximum==certificate['maximum_weighted_coefficient']==101136
assert rhs-M*maximum==certificate['strict_gap']==72768
assert rhs>M*maximum
assert certificate['cancelling_pair_lower_bound']==61
assert certificate['ordinary_dimension_mass_lower_bound']==4565
print(json.dumps({
    'trace_positions':len(source),
    'free_unrestricted_positions':len(variables),
    'weighted_associativity_inequalities':len(locators),
    'weighted_rhs':rhs,
    'maximum_weighted_coefficient':maximum,
    'budget_times_maximum':M*maximum,
    'strict_gap':rhs-M*maximum,
    'proved_pair_lower_bound':61,
    'arithmetic':'exact integers; no optimization solver in verifier'
},indent=2))
