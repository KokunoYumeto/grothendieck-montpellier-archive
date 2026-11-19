"""Independent lexicographic check of the compressed C.3af section data.

Only the immutable selected coefficient tuple is shared with the owner.
We use a different monomial order and retain all twelve exact unit bases.
"""
from pathlib import Path
from itertools import combinations
from datetime import datetime, timezone
import json, time
import sympy as sp
root=Path(__file__).resolve().parents[1]
start=time.perf_counter()
source=root.parent/'cycles'/'output/test_quartic_obstruction_rank.json'
c=json.loads(source.read_text())['trials'][0]['coefficients_i_j_k']
w=sp.Matrix(sp.symbols('w0:4'))
matrices=[sp.Matrix(4,4,lambda i,j:c[i][j][k]) for k in range(3)]
columns=[a*w for a in matrices]
determinants=[int(a.det()) for a in matrices]
assert determinants==[-36,4,200]
F=sum(v**4 for v in w)
checks=[]
for a,b in combinations(range(3),2):
 minors=[]
 for i,j in combinations(range(4),2):
  minors.append(sp.det(sp.Matrix([[columns[a][i],columns[b][i]],
                                  [columns[a][j],columns[b][j]]])))
 for chart in range(4):
  variables=[w[i] for i in range(4) if i!=chart]
  ideal=sp.groebner([g.subs(w[chart],1) for g in [F]+minors],
                   *variables,modulus=101,order='lex')
  expressions=[p.as_expr() for p in ideal.polys]
  assert expressions==[sp.Integer(1)]
  checks.append(dict(pair=[a,b],chart=chart,basis=[str(v) for v in expressions]))
record=dict(utc=datetime.now(timezone.utc).isoformat(),
 prime=101,order='lex',column_determinants=determinants,
 all_12_charts_empty=True,checks=checks,
 runtime_seconds=round(time.perf_counter()-start,6),
 scope='Finite certificate only. The all-s tensor independence and obstruction diagonal map are separately audited in the accompanying review.')
(root/'output/audit_quartic_column_pairs.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
