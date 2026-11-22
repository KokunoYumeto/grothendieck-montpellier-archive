# Tabulate e3_constants.json by a, with VIII's form and the Tate-type test of the user's prediction
import json,os
from collections import defaultdict
here=os.path.dirname(os.path.abspath(__file__))
R=json.load(open(os.path.join(here,'e3_constants.json')))
tab=defaultdict(lambda: defaultdict(int))
for r in R:
    a=r['a']; t=tab[a]; t['n']+=1; t['sign'+('+' if r['sign']>0 else '-')]+=1
    ok=r['laurent'] and r['bar'] and r['nonneg'] and r['unimodal']; t['VIII form ok']+=ok
    if r['laurent']:
        tate = r['nonneg'] and r['step']==2 or (r['nonneg'] and len(r['coeffs'])==1)
        t['f = v^-d P(v^2), P in N[q]']+=bool(tate)
        par=(r['lo']%2); t['f weight parity even' if par==0 else 'f weight parity odd']+=1
        # parity of c itself: a + parity(f)
        t['c exponents parity even' if (a+par)%2==0 else 'c exponents parity odd']+=1
for a in sorted(tab): print('a =',a,dict(tab[a]))
bad=[r for r in R if not (r['laurent'] and r['bar'] and r['nonneg'] and r['unimodal'])]
print('failures:',len(bad))
for r in bad[:20]: print(r['b'],r['bp'],r['bpp'],r['c'])
