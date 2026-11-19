#!/usr/bin/env python3
"""Exact genus/graph/norm identities for the ordinary arbitrary-embedding proof.

The finite arithmetic checks do not replace the geometric jet, descent,
Bertini, or all-parameter proofs in the accompanying text.
"""
from pathlib import Path
from time import perf_counter
import json
start=perf_counter()
rows=[]
for n in range(3,257):
    indecomposable_edges=n*(n-1)
    indecomposable_graph=indecomposable_edges-n+1
    product_edges=n*n
    product_graph=product_edges-2*n+1
    assert 2*n+indecomposable_graph == n*n+1
    assert 2*n+product_graph == n*n+1
    assert indecomposable_graph == product_graph == (n-1)**2
    for D in range(1,129):
        norm_nodes=n*n*(D-1)
        genus=n*n+1+norm_nodes
        assert genus == D*n*n+1
        assert genus-2 == D*n*n-1
        assert 2*norm_nodes == (D-1)*(2*n*n)
    rows.append({'n':n,'theta_graph_rank':product_graph,
                 'principal_genus':n*n+1})
out={'status':'PASS','n_cases':len(rows),'degree_norm_cases':len(rows)*128,
     'scope':'Finite exact numerical identities; geometric arguments proved separately',
     'rows':rows,'elapsed_seconds':perf_counter()-start}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
