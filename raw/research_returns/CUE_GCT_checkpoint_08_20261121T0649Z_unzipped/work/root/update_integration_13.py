"""Transport and record the checked uncentered interpolation obstruction."""
from pathlib import Path
from datetime import datetime, timezone
import csv

R=Path(__file__).resolve().parent;W=R.parent;OUT=W.parent/'deliverables'
now=datetime.now(timezone.utc).isoformat()
guard=R/'integration_13_check_events.tsv'
assert not guard.exists()
who='GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'
p=R/'grothendieck.tex';s=p.read_text()
marker='\\subsection{What the manuscript record does and does not establish}'
assert marker in s
new=r'''
\paragraph{P-16. Reciprocal coordinates, residue functionals, and a necessary center.}
The four disjoint pole divisors lie on the projective line over
the explicitly bounded number field. Their residue functionals
annihilate polynomials of the stated degrees because of the
orders of vanishing at infinity. The displayed rational identity
then makes one nonzero width-three tensor section vanish on
the unbalanced evaluation image. Passing to the coordinate
torus and applying inversion exchanges numerator and denominator
degree. Multiplication by the full coordinate monomial extends
this pullback to the multilinear coefficient tensor; on each
rank-two variable factor it exchanges the two basis vectors.
Every coefficient flattening is consequently changed only by
row and column permutation. This is a direct equality of ranks
of bundle maps in D-FGA, with D-S3 supplying the torus inversion
and diagonal node rescaling; no rank-monotonicity assumption
about polynomial factors is made.

The simple-root discriminant of the node polynomial makes all
$A'(b)$ invertible in the working field, so the Lagrange and
unbalanced rational maps have the stated exact diagonal
identification. Clearing denominators extends the identity
from the dense torus chart to the whole defined evaluation
family. Adding the common center is a different affine
parameter morphism. Its nonvanishing follows from P-14 because
all displayed transition determinants are nonzero polynomials.
Thus the same section is zero on one image and nonzero on the
centered image. D-S6 places the coefficient tensor operations;
it does not identify these two pullback maps merely because
their target bundle ranks agree. The construction uses the
specified algebraic nodes, and supplies no counterexample
for an arbitrary preassigned node set.

'''
p.write_text(s.replace(marker,new+marker))

with guard.open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 w.writerow(['statement_id','date','who','type','outcome'])
 w.writerow(['P-16',now,who,'targeted proof check',
 'PASS complete root proof reading/rederivation: explicit pairwise-disjoint simple pole groups and degree72 field bound at18nodes; nonzero residues, exact rational identity and vanishing moments; dense-open denominator specialization; width3 word and all-order width2 exclusion via P14; coordinatewise reversal and flattening permutations; SV diagonal D_b=Aprime(b) with correct sign; full-rank reversed factors and P14 centering repair. Missing display delimiter corrected before integration. No balanced/centered counterexample or arbitrary-node claim.'])

p=R/'intro.tex';s=p.read_text()
needle='The precise conditional matrix-invariant consequence remains I-08.'
assert needle in s
s=s.replace(needle,'P-16 gives an explicit degree16, width-exactly-three obstruction to the uncentered two-pair map on eighteen specified algebraic nodes. Its transition factors are generically invertible, and P-14 proves that the centered two-pair map hits the same polynomial. '+needle)
p.write_text(s)
p=R/'open_gates.tex';s=p.read_text()
needle='It does not decide the two-pair rank-two-reset case or the growing-width question.'
assert needle in s
s=s.replace(needle,'P-16 refutes the uncentered two-pair map on eighteen specified algebraic nodes, even for generically invertible factors, while P-14 proves that centering repairs that example. The centered two-pair rank-two-reset case and the growing-width question remain open.')
p.write_text(s)

with (OUT/'IMPLICATIONS.md').open('a') as f:
 f.write('''

### Centering cannot be omitted from the two-pair refinement

P16 gives eighteen explicit algebraic nodes over a field of degree at most72 and a nonzero degree16 multilinear polynomial of minimum ROABP width three in every variable order, killed by ordinary uncentered SV2. The proof starts with four rational functions on disjoint pole sets satisfying one exact quadratic relation, then reverses the multilinear coefficient basis and applies the exact Lagrange diagonal rescaling. Every resulting transition factor is generically invertible. P14 therefore proves that the centered SV2 map hits the very same polynomial. This separates the two maps concretely and blocks an attempted removal of the center. It does not decide centered SV2 for rank-two resets, nor assert failure for arbitrary preassigned interpolation nodes. The construction also explains why an unbalanced rational-map reduction needs additional structure: its large-degree ideal elements can have width three.
''')
with (OUT/'LEDGER.md').open('a') as f:
 f.write('\n\n## '+now+' — uncentered two-pair simplification refuted\n\n')
 f.write('P16 closes the explicit uncentered-generator question on its specified algebraic nodes. Full root and isolation proof readings verify the residue relation, coefficient reversal, all-order width lower bound and P14 repair by centering. This is a reduction of an attempted simplification; it is not recorded as solving the centered rank-two-reset gate or the polynomial-in-width main target. This is not a scheduled hourly review.\n')
print(now)
