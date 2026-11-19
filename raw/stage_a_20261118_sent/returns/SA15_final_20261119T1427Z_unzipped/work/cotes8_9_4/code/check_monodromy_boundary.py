"""Permutation monodromy boundary, n=1 only; not a higher-dimensional refutation."""
from pathlib import Path
from itertools import permutations,product
import json
W=Path(__file__).resolve().parents[1]
# QuotientF3^3/<(1,1,1)> in basis[e1],[e2], with[e3]=−[e1]−[e2].
v=[(1,0),(0,1),(2,2)]
H=set()
for s in permutations(range(3)):
    a,b=v[s[0]],v[s[1]]
    H.add(((a[0],b[0]),(a[1],b[1])))
G={((a,b),(c,d)) for a,b,c,d in product(range(3),repeat=4) if(a*d-b*c)%3}
assert len(H)==6 and len(G)==48 and H<G
out={'X':'P1','p':3,'degree':3,'vanishing_module':'F3^3/F3 diagonal',
'permutation_quotient_image_order':len(H),'GL2_F3_order':len(G),'quotient_matrices':sorted(H),
'conclusion':'n=1 fullGL assertion fails; no conclusion about the manuscript n>=2 question'}
(W/'outputs/monodromy_boundary.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
