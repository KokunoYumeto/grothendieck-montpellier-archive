"""Integrate the uniform Jacobi bound and affine singular two-pair theorem."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

R=Path(__file__).resolve().parent
W=R.parent
OUT=W.parent/'deliverables'
now=datetime.now(timezone.utc).isoformat()
guard=R/'integration_15_check_events.tsv'
assert not guard.exists()
who='GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'

p=R/'grothendieck.tex'
s=p.read_text()
marker='\\subsection{What the manuscript record does and does not establish}'
assert marker in s
addition=r'''
\paragraph{R-26. Characterwise determinantal opens and a linear derived defect.}
The Jacobi parameters form an integral affine scheme; restricting
to nonzero diagonal and edge parameters gives an integral torus
chart. The finite cyclic action on the ternary variables decomposes
the coefficient bundle over characteristic zero into its character
subbundles. In each ordinary character, eight specified normal
sections have a nonzero determinant on a nonempty open chart.
The seventeen finite cores certify those opens by reduction modulo
$101$; their denominators are invertible at the stated certificates.
These are exact algebraic determinants, not approximate ranks.

The cut argument takes place over a Laurent-series field: divide
the second weight component by its path product, replace each cut
edge by a parameter times a chosen nonzero constant, and specialize
the resulting regular normalized matrix at parameter zero. Equal
outer cut orders allow its path-product ratio to have any specified
nonzero limit. Inserting isolated vertices multiplies the indicated
component sections by the common coordinate $x$, an injective map
of the coefficient modules. The two insertion rules therefore
transport each certified determinantal open to all required sizes.
The exceptional character sections are independent by the
coprimeness of consecutive continuants. Irreducibility of the
parameter scheme makes the finite intersection of all these opens
nonempty. This is the scheme-theoretic content of the construction;
it does not assert that one literal zero-edge pencil realizes all
the normalized certificates simultaneously.

Apply the R-25 normal-direction injection and the D-Tor dictionary
of R-23. The dimension of the degree-$m$ first derived tensor
homology is at most $6(m-18)$ for $m\ge18$. Thus the exact remaining
failure of the restricted linear strand is bounded linearly.
D-S3 places the character action, D-FGA places the coefficient
rank opens and orbit-image dimensions, and D-Tor (SGA~6, III~1.5--1.6
and I~5.1--5.4) places the derived restriction. The consequence is a
characteristic-zero bound; the use of modular certificates alone
does not give the whole statement in every positive characteristic.
Combining these dimension bounds with the flag quotients of
G-17/G-18 gives the exact rectangular padding range already for
$m\ge14$, as detailed in R-26. No new positivity conjecture is
substituted for those proved quotient comparisons.

\paragraph{I-37. Rank-two active bundles and the second coefficient form.}
The rational centered two-pole family defines a morphism from an
open parameter scheme to the coordinate affine space. Its one-pole
subfamily is dominant on each coordinate pair. An irreducible
multilinear section can be considered separately because its
irreducible factors use disjoint coordinate sets; specializing the
other coordinates preserves the affine singular factorization.
On the nonzero minor charts, every strict internal product has
rank two. A rank-one internal product would have a polynomial
column--row factorization over the coordinate UFD, and would split
the irreducible scalar into two nonconstant factors.

Exterior squares and the pairwise dominant pullback preserve these
rank-two charts, by I-36. Compatible bases split each intermediate
rank-three bundle into a persistent active rank-two summand and
a passive line, with constant transition $\operatorname{diag}(1,1,0)$.
The affine singular condition makes the linear passive self-entry
zero. If the original section vanished on the two-pole image,
simple-pole residues would annihilate all first coefficient forms
at the one-pole center. Translation along its nonzero common
slope vector annihilates the contraction of the second coefficient
form with that vector. In the compatible bases this form has only
adjacent off-diagonal entries. Induction along the ordered path
then makes each of them zero in every characteristic. Every
possible active-to-passive-to-active output transition consequently
has a zero product, forcing the whole section to be zero.

This restates the complete contradiction in bundle-map language.
The second coefficient form is extracted formally from multilinear
polynomials, so division by two is never used. D-S6, V~2.1--2.2.1,
places the exterior-square maps; D-S3 places the changes of frame;
D-FGA places the rank strata and nonvanishing charts. The final
diagonal node rescaling identifies the rational family with
ordinary centered Lagrange interpolation. Its five parameter
coordinates yield the exact grid count in I-37. Invertible
variable-dependent transitions can propagate the passive line,
so the tridiagonal argument does not extend to that unresolved
mixed-rank case.

'''
p.write_text(s.replace(marker,addition+marker))

events=[
('R-26','targeted proof check','PASS complete root proof reading/rederivation: all cofactor and second-derivative formulas; eight normalized columns; rational cut limits and adjustable reduced path ratio; both insertion maps including tight gap4 endpoints and repeated cut positions; exhaustive coverage of character indices; exceptional homogeneous continuant identities, coprimeness and degree arguments; common irreducible open intersection; integer parameter grid; R25 increment and linear Tor defect; exact padded range. Separate copies of specialization points are not confused with one common cut pencil.'),
('R-26','computation or formal certificate','PASS independent reconstruction of all17 finite core coefficient matrices by direct enumeration of path matchings, and all selected minors by modular fraction-free Bareiss with row-swap signs. The full matrices agree with the author continuant computation. See check_r26_cores.py and r26_core_checks.json. This computation alone does not establish the uniform insertion theorem.'),
('I-37','targeted proof check','PASS complete root proof reading and independent rederivation: arbitrary-slope pair dominance; residue extraction and Hc=0 in every characteristic; disjoint-variable irreducible factor specialization; UFD polynomial outer factorization; preservation of rank2 internal intervals; nonzero endpoint projections; compatible gauges and simultaneous endpoint shears even with one interior factor; derivative constraints; tridiagonal Hessian and all endpoint/interior path cases; diagonal node rescaling and exact five-parameter sampling. Scope is affine singular variable factors, not arbitrary mixed rank3 words.'),
('R-26','used and rechecked in this run','PASS rectangular consequence: for m≥18, 2(m−1)^2+53−16m^2/9=(2/9)(m−9)^2+37>0. For m14,15,16,17 the exact c values680,816,969,1124 exceed2n_max^2−1=647,721,881,967 with n_max18,19,21,22. G11/G17 supply gaps for m<n<4m/3 and G12 excludes n≥4m/3. Threshold14 is sufficient, not asserted optimal.')]
with guard.open('w',newline='') as f:
    writer=csv.writer(f,delimiter='\t',lineterminator='\n')
    writer.writerow(['statement_id','date','who','type','outcome'])
    for identifier,kind,outcome in events:
        writer.writerow([identifier,now,who,kind,outcome])

p=R/'intro.tex'
s=p.read_text()
needle='a uniform ternary rank condition is the next exact-dimension gate.'
assert needle in s
s=s.replace(needle,'R-26 proves the uniform bound $0\\le\\epsilon_m\\le6(m-18)$ for $m\\ge18$, using characterwise Jacobi continuants and finite core insertions. It yields $c_m\\ge4m^2-8m+110$ and all padded pairs with $n^2\\le2(m-1)^2+53$. The exact four-row rectangular range $m<n<4m/3$ consequently holds already for every $m\\ge14$. Uniform vanishing of the remaining defect is still open.')
needle='The precise conditional matrix-invariant consequence remains I-08.'
s=s.replace(needle,'I-37 reduces this to two centered pairs for the affine singular-factor subclass, in every characteristic and unknown order, by an irreducible-factor reduction and a tridiagonal second-coefficient argument. Mixed variable-dependent rank-two and rank-three factors remain outside that refinement. '+needle)
p.write_text(s)

p=R/'open_gates.tex'
s=p.read_text()
s += r'''

\subsection{Updated sharp gates after R-26 and I-37}
For the four-variable permanent image, R-26 bounds the single
Tor defect by $6(m-18)$ for every $m\ge18$. The dimension-certified
positive range reaches $n^2\le2(m-1)^2+53$, leaving only a bounded
distance in $n$ from the dimension ceiling. The exact four-row
rectangular padding range is established for every $m\ge14$.
Uniform zero defect for $m\ge19$ remains open; the border route
needs six additional normal directions beyond the Jacobi bound.

For centered two-pair width-three isolation, I-37 now closes the
affine singular-factor class. P-14 already treats rank-one or
full-rank factors. The remaining common two-pair target includes
arbitrary mixtures of rank-two and variable-dependent rank-three
affine factors, and nonlinear singular factors. No polynomial
sampling bound jointly in growing width, length and degree follows
from this specified width-three improvement.
'''
p.write_text(s)

p=W/'assemble.py'
s=p.read_text()
s=s.replace('A uniform staircase construction gives quaternary permanent-image dimension $4m^2-O(m^{3/2})$, reaching every fixed padding ratio below $\\sqrt2$.','A Jacobi-continuant construction gives quaternary permanent-image dimension $4m^2-O(m)$, bounding its exact homological defect linearly and reaching within a constant additive distance of the four-variable dimension ceiling.')
s=s.replace('with a six-pair refinement at width three, and explicit arithmetic points','with a six-pair refinement at width three and two centered pairs for affine singular-factor words, and explicit arithmetic points')
p.write_text(s)

with (OUT/'IMPLICATIONS.md').open('a') as f:
    f.write('''

### Linear defect and a constant remaining padding strip

R26 replaces the earlier O(m^(3/2)) permanent-image defect bound by the uniform exact inequality 0≤epsilon_m≤6(m−18), m≥18. Its proof uses seventeen independently verified finite character cores, algebraically valid normalized cut limits, exact vertex insertions, and the R25 border increment. Consequently c_m≥4m²−8m+110 and every integer pair m<n with n²≤2(m−1)²+53 is dimension-certified for the G17/G18 strict-direction conclusions. The remaining uncertainty near the four-variable dimension ceiling has bounded additive width in n. Combining the bound with the exact small-size certificates proves the exact four-row rectangular padding range m<n<4m/3 for every m≥14, with G12 excluding its complement. This sufficient threshold is not claimed optimal. The whole main asymptotic GCT separation and polynomial positive extraction are still open.

### Two centered pairs for affine singular width-three words

I37 proves centeredSV2 for all nonzero multilinear width-three words whose variable-dependent factors are affine and generically singular, in arbitrary unknown order and every characteristic. The exact grid has (D+1)((n−1)D+1)^2 binom(D+2,2) points. Its key argument splits an irreducible scalar across no rank-one interior interval, preserves all rank-two intervals at a one-pole center, and then forces every adjacent passive excursion to vanish if two-pole annihilation were assumed. The rational arithmetic encoding P13 therefore has degree at most(nD+1)^5 on this class. The earlier singular-factor result I36 still applies to arbitrary individual degree with exponent11, while unrestricted width three retains exponent13. Variable-dependent full-rank factors can transmit the passive state and remain a concrete obstruction to extending this new proof. The general growing-width polynomial PIT and associated matrix-invariant normalization targets remain unresolved.
''')

with (OUT/'LEDGER.md').open('a') as f:
    f.write('\n\n## '+now+' — uniform linear defect and affine two-pair refinement\n\n')
    f.write('R26 and I37 have passed complete root proof readings. All17 R26 finite core matrices were independently regenerated by matching enumeration and their minors verified by modular Bareiss. R26 strictly reduces the main four-variable dimension gate from an O(m^(3/2)) defect to at most6(m−18), and lowers the proved eventual rectangular threshold to14. I37 closes the affine singular-factor centeredSV2 subclass; mixed affine rank3 transitions and higher individual degree remain open. This entry is a dated integration update, not a scheduled movement review.\n')

review={'checked_utc':now,'who':who,'status':'PASS','proofs':[]}
for rel in ['rectangular/r26_fragment.tex','isolation/I37_multilinear_singular_two_pairs.tex']:
    path=W/rel
    review['proofs'].append({'path':str(path.relative_to(W.parent)),
                            'sha256_at_reading':hashlib.sha256(path.read_bytes()).hexdigest()})
(R/'r26_i37_whole_proof_review.json').write_text(json.dumps(review,indent=2)+'\n')
print(now)
