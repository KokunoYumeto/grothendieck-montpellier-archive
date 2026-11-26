#!/usr/bin/env python3
"""Check all 12^4 polarized coefficient identities for the published array."""
from pathlib import Path
from itertools import product
import json
w = Path(__file__).resolve().parents[1]
data = json.loads((w/'inputs/rt_zhang_zhu_12_12_18.json').read_text())
table = data['table']
def pair(a, b):
    sa = -1 if a.startswith('-') else 1
    sb = -1 if b.startswith('-') else 1
    a, b = a.lstrip('-'), b.lstrip('-')
    if a in 'ABC' and b in 'ABC':
        value = data['gram_ABC']['ABC'.index(a)]['ABC'.index(b)]
    else:
        value = int(a == b)
    return sa*sb*value
failures=[]
for i,j,k,l in product(range(12),repeat=4):
    value = pair(table[i][j],table[k][l])+pair(table[i][l],table[k][j])
    expected = 2*int(i==k and j==l)
    if value != expected:
        failures.append({'indices':[i,j,k,l], 'actual':value, 'expected':expected})
out={'source':data['source'],'identities_checked':12**4,'failures':failures,
     'status':'PASS' if not failures else 'FAIL',
     'scope':'Only the explicit positive identity; no asymptotic amplification or real nonexistence is inferred.'}
(w/'outputs/rt_zhang_zhu_12_12_18_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'identities_checked':12**4,'failure_count':len(failures),'first_failures':failures[:4]}))
