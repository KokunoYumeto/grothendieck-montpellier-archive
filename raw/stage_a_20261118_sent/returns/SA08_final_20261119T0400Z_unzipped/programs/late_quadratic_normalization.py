"""Exact quadratic Gamma normalization for the standard simplex quotient Psi.

This is a computation of a manuscript assertion, not a new research direction.
For Psi_2 with basis e1,e2, the three faces have coefficient rows(-1,1),
(0,1),(1,0) in Psi_1=k e. On Gamma² the corresponding row is(a²,2ab,b²).
"""
import json
from pathlib import Path
from sympy import Matrix
faces=[(-1,1),(0,1),(1,0)]
gamma_rows=[Matrix([[a*a,2*a*b,b*b]]) for a,b in faces]
constraints=gamma_rows[1].col_join(gamma_rows[2])
kernel=constraints.nullspace()
assert kernel==[Matrix([0,1,0])]
boundary=gamma_rows[0]*kernel[0]
assert boundary==Matrix([-2])
sym_rows=[Matrix([[a*a,a*b,b*b]]) for a,b in faces]
assert sym_rows[0]*kernel[0]==Matrix([-1])
out={
 'source':'136/239, D154–170; cross-check rootC958 at346',
 'Gamma2_face_rows':[[int(v) for v in x] for x in gamma_rows],
 'normalized_degree2_basis':[[int(v) for v in x] for x in kernel],
 'normalized_boundary_2_to_1':int(boundary[0]),
 'higher_normalized_terms':'zero: every degree-two monomial has support in at most2 positive vertex indices; the kernels of d1,...,dn require support containing all n indices',
 'over_any_commutative_k':{'H2':'kernel(2:k→k)','H1':'k/2k','other_positive_degrees':0},
 'over_Z':{'H2':0,'H1':'Z/2'},
 'over_Q':{'H2':0,'H1':0},
 'Sym2_boundary':-1,
 'conclusion':'An ordinary K(k,2) identification is false. For k=Q, weight2 is acyclic, so all-p nonflasqueness requires a different notation/hypothesis. The unsure Pi/K name remains undecided.'
}
P=Path('/workspace/scratch/7feb9690b71f/SA08_work/logs/late_quadratic_normalization.json')
P.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
