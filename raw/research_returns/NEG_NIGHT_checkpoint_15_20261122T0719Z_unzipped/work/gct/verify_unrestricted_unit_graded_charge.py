"""Exact source congruence check for the all-position unit ideal lemma.
The ideal argument is in g037_unit_graded_charge.tex; this script verifies
only its finite original-source interface, not a bounded-degree search.
"""
from pathlib import Path
from itertools import product
import json
import sympy as sp

v=sp.Symbol('v')
names=['mu','Sigma']+[f'g{i}_{w}' for i in (1,2) for w in ('1','12','2','21')]
idx={name:i for i,name in enumerate(names)}
trace={}
for row in json.loads(Path('sources/OURS_E4_scripts/e3_constants.json').read_text()):
    key=tuple(idx[row[z]] for z in ('b','bp','bpp'))
    assert key not in trace
    poly=sp.Poly(sp.expand(sp.sympify(row['c'],locals={'v':v})*v**64),v)
    coeff={}
    for (e,),c in poly.terms():
        assert c.is_Integer and (e-64)%2==0
        coeff[(e-64)//2]=int(c)
    assert coeff and any(coeff.values())
    trace[key]=coeff
assert len(trace)==132
for a,z in product(range(10),repeat=2):
    wanted={0:1} if a==z else {}
    assert trace.get((0,a,z),{})==trace.get((a,0,z),{})==wanted

checked=nonzero=zero_unit=0
for a,b,z in product(range(1,10),range(1,10),range(10)):
    coeff=trace.get((a,b,z),{})
    assert all(sum(c for e,c in coeff.items() if e%2==j)%2==0 for j in (0,1))
    checked+=1;nonzero+=bool(coeff)
    if z==0:
        assert not coeff
        zero_unit+=1
assert (checked,nonzero,zero_unit)==(810,113,81)
result={'source_positions':132,'normalized_unit_positions':19,
        'all_nonunit_input_positions_checked':checked,
        'nonzero_nonunit_input_source_positions':nonzero,
        'zero_unit_output_positions':zero_unit,
        'congruence':'every nonunit-input trace lies in (2,(q+1)^2)',
        'method':'exact integer coefficient parity by grading degree modulo2'}
Path('work/gct/unrestricted_unit_graded_charge_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
