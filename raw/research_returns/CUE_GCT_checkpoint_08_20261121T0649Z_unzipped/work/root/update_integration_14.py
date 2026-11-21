"""Integrate the checked maximal-minor preservation and singular-word refinement."""
from pathlib import Path
from datetime import datetime, timezone
import csv

R=Path(__file__).resolve().parent;W=R.parent;OUT=W.parent/'deliverables'
now=datetime.now(timezone.utc).isoformat()
guard=R/'integration_14_check_events.tsv';assert not guard.exists()
who='GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'
p=R/'grothendieck.tex';s=p.read_text()
marker='\\subsection{What the manuscript record does and does not establish}'
assert marker in s
new=r'''
\paragraph{I-36. Pairwise dominant pullback and rank-one exterior maps.}
The centered one-pair morphism is dominant on every coordinate
pair: its determinant over the selector function field is the
difference of two Lagrange basis sections and is nonzero.
Hence its pullback is injective on each such bivariate
coordinate algebra. On a rank-one bundle-map chart, a pivot
writes the map as a column and a row divided by a nonzero
univariate section. Clearing the pivots turns an interval
contraction into a product of univariate endpoint sections
and adjacent bivariate sections. Each survives the same
pullback, and their product survives in the parameter domain.

For factors of rank at most $r$, the $r$th exterior map is
zero or rank one. Functoriality of exterior powers, equivalently
Cauchy--Binet, identifies its interval entries with the
original maximal minors. The first paragraph therefore
preserves each nonzero such section. D-S6, V~2.1--2.2.1,
places the exterior-power construction, D-S3 places its
coordinate action, and D-FGA places the resulting determinantal
rank opens. In width three with singular factors this supplies
the rank-two-preserving center. The four residual interpolation
pairs from I-30 preserve the remaining local rank-one tests,
giving five pairs in total. This proof uses actual nonzero
minors throughout; no numerical rank or purity argument is
substituted for the exact pullback assertion. Arbitrary
variable-dependent invertible width-three factors remain
outside this five-pair refinement.

'''
p.write_text(s.replace(marker,new+marker))
with guard.open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 w.writerow(['statement_id','date','who','type','outcome'])
 w.writerow(['I-36',now,who,'targeted proof check',
 'PASS entire root reading/rederivation: pairwise Lagrange determinant in all characteristics; pivot-cleared rank1 interval product has only univariate and adjacent bivariate factors; Cauchy–Binet and compound rank1 preserve every nonzero maximal minor; original singular-factor scope, parameter transcendence and endpoint absorption; exact I29/I30 four-pair completion with old minors retained at zero new amplitudes; five-pair grid and extension conventions. I30 full statement/proof was reopened. No claim for arbitrary invertible variable factors or centeredSV2.'])
p=R/'intro.tex';s=p.read_text()
needle='The precise conditional matrix-invariant consequence remains I-08.'
assert needle in s
s=s.replace(needle,'I-36 proves a pairwise-dominant maximal-minor preservation lemma and improves the bound to five pairs when every variable-dependent width-three factor is singular. '+needle)
p.write_text(s)
p=R/'open_gates.tex';s=p.read_text()
needle='I-30 closes the width-at-most-three, one-unknown-order case with six interpolation pairs, including arbitrarily many rank-two cuts.'
assert needle in s
s=s.replace(needle,needle+' I-36 improves this to five pairs for the class with singular variable-dependent factors, through one-pair preservation of all nonzero maximal interval minors.')
p.write_text(s)
with (OUT/'IMPLICATIONS.md').open('a') as f:
 f.write('''

### One pair preserves maximal minors of singular-factor words

I36 proves that a centered one-pair interpolation map is dominant on every coordinate pair. Exterior powers turn the maximal minors of a word of generic-rank-at-most-r factors into a rank-one matrix word; after exact pivot clearing, its contractions factor into univariate and adjacent bivariate polynomials. They all survive that same map. This supplies the complete rank-two-preservation stage for width-three words with singular variable-dependent factors. Adding the already checked four-pair rank-one completion gives centeredSV5, with exact evaluation bound (D+1)((n−1)D+1)^5 binom(D+5,5), in every characteristic with the stated working-field convention. The bound for unrestricted width three remains six pairs, and the proposed two-pair bound remains open. The integer arithmetic encoding P13 consequently has exponent11 on this singular-factor rational subclass, by direct substitution K=5 in its proved formula; the general width-three exponent remains13.
''')
with (OUT/'LEDGER.md').open('a') as f:
 f.write('\n\n## '+now+' — maximal-minor preservation and five-pair singular-factor subclass\n\n')
 f.write('I36 proves one-pair preservation of every nonzero maximal interval minor when all factor ranks are bounded by that minor size. In width three, this reduces the singular-factor class from six pairs to five after the existing rank-one completion. Root and purity read and rederived the entire proof, including the dependency hypotheses. This is a specified-class refinement; the unrestricted centeredSV2 and growing-width main gates are unchanged. This is not a scheduled review.\n')
print(now)
