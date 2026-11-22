#!/usr/bin/env python3
import json
from time import perf_counter
from pathlib import Path

t0 = perf_counter()
p, ell, r = 2, 3, 8
g = (p-1)*(p*r-2)//2
degN = (r*(p-1)-2)//ell
terms = []
for i in range(3):
    exponents = [9+2*i+3*j for j in range(7-i)]
    dims = [degN*c+1-g for c in exponents]
    assert all(degN*c-2 > 2*g-2 for c in exponents)
    terms.append({'i':i,'exponents':exponents,'dimensions':dims,'sum':sum(dims)})
assert g == 7 and degN == 2
assert [x['sum'] for x in terms] == [210,186,160]
assert sum(x['sum'] for x in terms) == 556
out = {'p':p,'ell':ell,'curve':'y^2-y=x^15','genus':g,'degN':degN,
       'power':9,'terms':terms,'h0_Q9':556,'root_cover_degree':'9^556',
       'trace_degree_mod_p':pow(9,556,p),'H1_Q_inverse':1,
       'runtime_seconds':round(perf_counter()-t0,6)}
target=Path(__file__).with_name('check_root_cover_input_output.json')
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
