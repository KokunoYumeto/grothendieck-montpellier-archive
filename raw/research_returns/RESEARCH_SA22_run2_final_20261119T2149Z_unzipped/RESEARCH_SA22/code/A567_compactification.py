#!/usr/bin/env python3
"""Exact finite checks for the product log-model proof; no numeric approximation.
The universal compactification-invariance argument is in A:canonical-log-model-product.
"""
import json
import math
import time
from pathlib import Path

started = time.perf_counter()
canonical_bidegree = (-2, -2)
boundary_bidegree = (3, 3)
log_bidegree = tuple(a+b for a, b in zip(canonical_bidegree, boundary_bidegree))
assert log_bidegree == (1, 1)
# In variables x0,x1,y0,y1, the four Segre generators x_i*y_j.
generators = {(i,j): tuple(int(k == i) for k in range(2)) + tuple(int(k == j) for k in range(2))
              for i in range(2) for j in range(2)}
lhs = tuple(a+b for a,b in zip(generators[(0,0)],generators[(1,1)]))
rhs = tuple(a+b for a,b in zip(generators[(0,1)],generators[(1,0)]))
assert lhs == rhs == (1, 1, 1, 1)
hilbert = []
for m in range(9):
    product_dim = (m+1)**2
    quadric_dim = math.comb(m+3,3) - (math.comb(m+1,3) if m >= 2 else 0)
    assert product_dim == quadric_dim
    hilbert.append({'degree':m,'bidegree_section_dimension':product_dim,'quadric_ring_dimension':quadric_dim})
blowups = [{'branches_at_center':r,'canonical_exceptional_coefficient':1,
            'reduced_boundary_exceptional_correction':1-r,
            'log_discrepancy':2-r} for r in (1,2)]
result = {'certificate':'exact integer and monomial arithmetic',
          'canonical_bidegree':canonical_bidegree,'boundary_bidegree':boundary_bidegree,
          'log_canonical_bidegree':log_bidegree,
          'Segre_monomial_relation_exponents':{'z00_z11':lhs,'z01_z10':rhs},
          'boundary_blowup_cases':blowups,'Hilbert_dimension_checks':hilbert,
          'runtime_seconds':time.perf_counter()-started}
output = Path(__file__).resolve().parents[1]/'logs'/'A567_compactification.json'
output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
