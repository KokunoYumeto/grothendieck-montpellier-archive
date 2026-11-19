"""Check pairwise independent columns for the certified C.3ae matrices.

This is a proposed refinement of the section count, separate from the
already proved full-basis product construction.
"""
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations
import json
import time
import sympy as sp

started=time.perf_counter()
base=Path(__file__).resolve().parents[1]
coeff=json.loads((base/'output/test_quartic_obstruction_rank.json').read_text())['trials'][0]['coefficients_i_j_k']
w=sp.symbols('w0:4')
F=sum(x**4 for x in w)
B=sp.Matrix([[sum(coeff[i][j][k]*w[j] for j in range(4)) for k in range(3)] for i in range(4)])
charts=[]
for k,l in combinations(range(3),2):
    minors=[B[i,k]*B[j,l]-B[j,k]*B[i,l] for i,j in combinations(range(4),2)]
    for chart in range(4):
        before=time.perf_counter()
        variables=[w[j] for j in range(4) if j!=chart]
        polys=[p.subs(w[chart],1) for p in [F]+minors]
        gb=sp.groebner(polys,*variables,modulus=101,order='grevlex')
        basis=[str(p.as_expr()) for p in gb.polys]
        charts.append({'columns':[k,l],'chart_w':chart,'unit_ideal_mod101':basis==['1'],
                       'basis':basis,'runtime_seconds':time.perf_counter()-before})
record={'utc':datetime.now(timezone.utc).isoformat(),'prime':101,
        'coefficient_source':'test_quartic_obstruction_rank.json, first tuple',
        'column_matrices_det': [int(sp.Matrix([[coeff[i][j][k] for j in range(4)] for i in range(4)]).det()) for k in range(3)],
        'charts':charts,'all_pair_columns_independent':all(x['unit_ideal_mod101'] for x in charts),
        'runtime_seconds':time.perf_counter()-started,
        'scope':'Exact finite-field emptiness certificate; properness of each projective determinantal locus gives pairwise independence at every complex point of W. Tensor consequences require a separate proof.'}
(base/'output/check_quartic_column_pairs.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
