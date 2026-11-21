"""Integrate the fully checked all-stretch comparison and dense repairs once."""
from pathlib import Path
from datetime import datetime, timezone
import csv

R=Path(__file__).resolve().parent
OUT=R.parents[1]/'deliverables'
now=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'

p=R/'findings.tex'; s=p.read_text(); assert '\\label{G-18}' not in s
p.write_text(s+'\n'+(R/'g18_fragment.tex').read_text())
with (R/'questions.tsv').open('a') as f:
 f.write('G-Q19\tPrompt Q1/Q2; G18 padding-line stabilizer and degree semigroup\tCan the successful stretch progression be upgraded to every sufficiently large integer stretch, including rectangles?\tPROVED G-18: every strict four-row direction has both multiplicities positive for every j>=beta²; when c_m+3>2n²+2 the permanent multiplicity is larger for every j>=E(4u(pE)^(u-1)+1). Generic padding-line variation removes the finite projective stabilizer, including eta=0.\n')
 f.write('G-Q20\tPrompt Q1/Q2; G18 all-integer Hilbert asymptotics\tWhat determines eventual comparison in a fixed four-row direction, and can occurrence obstructions persist along that direction?\tPROVED G-18: ratio=kappa_nu*j^(c_m-2n²+1)(1+O(1/j)), kappa_nu>0; effective eventual determinant dominance if 2n²>4m²-2m+3, in particular n>=sqrt(2)m. Every fixed four-row direction has no occurrence obstruction at all sufficiently large stretches. Equality of quotient dimensions and individual finite-degree gaps remain separate comparisons.\n')

events=[
 ('G-18','targeted proof check','PASS complete root reading/rederivation of final all-direction proof: smooth irreducible Fermat factor; finite projective stabilizer and dual fixed-locus avoidance; common stable open under padding-line variation; unique factorization; central exponent 4nu4; closed-orbit separation and gcd1; semigroup conductor; injective all-residue sandwich; exact binomial ratio; both homogeneous parameter degrees; effective reverse comparison; Hilbert leading term and all-integer ratio; fixed-direction occurrence corollary and eta0 case.'),
 ('G-B15','used and rechecked in this run','Reopened Mukai2003 primary PDF and read Theorem5.3 including its two-step proof, printed pp161–162, Corollary5.4 p162, and Proposition5.15 p166 with its preceding argument. Distinct closed orbits are separated by invariants; stable locus is open. These precise assertions, with characteristic-zero reductivity, support G18. Retrievals turn349210535view0–2 and turn496942138view0.'),
 ('I-34','computation or formal certificate','PASS independent SymPy integer expansion, prime checks and coefficient flattening at2026-11-21T03:27:56.060099+00:00. Three-product prime curve vanishes and its freed-coordinate identity is exact. All eight one-coordinate cylinders of the four-product example vanish; a two-coordinate cylinder is nonzero. Flattening determinant1 proves rank4 in every characteristic. Files work/root/check_i34_examples.py and i34_example_check.json. An initial unnecessary symbolic factorization was canceled; exact expansion run completed.')
]
with (R/'integration_09_check_events.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n'); w.writerow(['statement_id','date','who','type','outcome'])
 for identifier,kind,result in events:w.writerow([identifier,now,who,kind,result])

p=R/'sources.md'; s=p.read_text()
needle='G11 supplies explicit stable points before applying the fiber-dimension deduction.'
replacement=needle+' For G18, Theorem5.3 and its complete two-step proof, printed pp.161–162, Corollary5.4, p.162, and Proposition5.15, p.166, were reopened and read. They give separation of distinct closed orbits by invariants and openness of the stable locus; the padding-line and effective semigroup arguments are proved in G18 itself.'
assert needle in s; p.write_text(s.replace(needle,replacement))

p=R/'grothendieck.tex'; s=p.read_text()
marker='\\subsection{What the manuscript record does and does not establish}'
new=r'''
\paragraph{G-18. Removing scalar orbit periods and comparing every large degree.}
The auxiliary Schur cone and its D-S6 Cartan coordinate modules remain
those of G-17. The smooth Fermat factor has finite projective stabilizer;
varying its padding line in a common stable open avoids every nontrivial
fixed locus. Unique factorization then gives a free projective orbit.
In the D-S3 central group scheme $\mu_4\subset\mathrm{SL}_4$, the
character exponent $ns-|\eta|=4\nu_4$ is trivial. Consequently two
distinct nonzero scalar multiples of the chosen tensor have distinct
closed orbits. Exact reductive invariants separate them, forcing the
degrees of common nonzero invariant sections to generate $\mathbb Z$.
The explicit numerical-semigroup argument gives sections in every
degree at least $\beta^2$. Multiplication by these sections is injective
in both quotient coordinate domains. D-FGA's standard Veronese and
Hilbert-function comparison can therefore be transported to every
integer degree, with the stated effective thresholds and common
asymptotic exponent. The rectangular central congruence is already
encoded by $ns=4\nu_4$. All stability, exact invariant-functor, and
quotient assertions here are in characteristic zero; an integral
model alone is not an assertion of the same behavior at every prime.

\paragraph{I-34. Local relation modules and coordinate cylinders.}
At one factor position, take the kernel of the univariate coefficient
map from the free module on product terms. A rank-one kernel with full
support is a circuit. The D-S3 prime cocharacters and the divisor
argument of I-33 force every canceled multiplicative ratio off this
position to be a character. A free coordinate separates its character
exponents, and the circuit property excludes every proper relation.
Higher local nullity is reduced by coefficient elimination. The result
gives the explicit bound on the number of free coordinate directions;
interpolation replaces the cylinders by integral cocharacters. In
D-FGA terms, the finite family preserves the coefficient-image module
after extension to the working field. The rank-four flattening example
defines a genuine nonzero tensor in the kernel of every one-coordinate
cylinder and identifies the precise failure of that smaller family.

\paragraph{P-14. Rank-one reset maps and scalar bridge sections.}
On a rank-one bundle-map chart, a nonzero pivot writes the map as a
column times a row divided by that pivot. Clearing all pivots splits
the scalar contraction into bridge sections. Invertible interior maps
and absorbed endpoint maps have identity constants over $F(t)$; the
ascending coefficient-row subspaces have at most $w-1$ strict growth
steps. One common interpolation morphism keeps every nonzero bridge
section nonzero, and their product remains nonzero in its coordinate
domain even when adjacent bridges share a reset variable. Constant
linear annihilators give exact coefficient-row preservation. This is
the D-FGA image-module criterion and the D-S3 dense substitution; no
equality of matrix image cones or purity statement is required. The
balanced rational-evaluation form follows from the stated partial
fractions and the same scalar-annihilator argument.

'''
assert marker in s; p.write_text(s.replace(marker,new+marker))

p=R/'intro.tex'; s=p.read_text()
needle='It gives effective first-stretch and progression bounds through a partial-flag construction.'
assert needle in s
s=s.replace(needle,needle+' G-18 strengthens this to every sufficiently large integer stretch, including rectangular directions. It gives an all-integer multiplicity ratio with exponent $\\dim\\mathcal P_{m,4}-2n^2+1$, an effective converse range, and eventual absence of occurrence obstructions along each fixed four-row direction.')
needle='I-33 instead gives explicit small prime-cocharacter families for two dense products, their exact limitation, and a scalar product-closure repair.'
assert needle in s
s=s.replace(needle,needle+' I-34 extends the prime family to bounded local nullity among separated products, with an exact three-versus-four-term cylinder distinction. P-14 uses scalar bridges to give $w-1$ interpolation pairs for factors of rank one or full rank, including one pair at width two.')
p.write_text(s)

p=R/'open_gates.tex'; s=p.read_text()
needle='G-17 classifies every four-row stretched direction for the dimension-certified pairs by the two strict inequalities in its statement.'
assert needle in s
s=s.replace(needle,needle+' G-18 makes the comparison valid at every sufficiently large integer stretch, computes its all-integer leading exponent, and gives effective eventual determinant dominance when $2n^2>4m^2-2m+3$. Every fixed four-row direction eventually has no occurrence obstruction; changing directions and individual finite-degree gaps remain outside that conclusion.')
needle='I-33 supplies a dense prime-cocharacter repair for two-product factors and their products, leaving general matrix cancellation outside its divisor argument.'
assert needle in s
s=s.replace(needle,'I-34 extends the prime-cocharacter repair to separated products with bounded local nullity and proves its exact one-coordinate limitation. P-14 replaces full image-cone preservation by scalar bridges for factors of rank one or full rank, reducing that case to $w-1$ pairs. General intermediate-rank matrix cancellation remains outside these divisor and product arguments.')
p.write_text(s)

with (OUT/'IMPLICATIONS.md').open('a') as f:
 f.write('''

### Every sufficiently large stretch, and an effective converse

G18 removes the progression restriction from G17, including rectangular directions. For every fixed nu partition ns with nu4>0 and nu1>(n−m)s, both orbit-closure multiplicities are positive at every stretch j>=beta². If c_m+3>2n²+2, the permanent multiplicity exceeds the determinant multiplicity for every j>=E(4u(pE)^(u−1)+1), with the quantities explicitly defined in G17. The proof varies the padding linear form to remove all projective automorphisms while staying in a common stable open. Separation of closed orbits then makes the degrees of nonzero common invariant sections relatively prime. An effective numerical-semigroup argument supplies every large degree, and multiplication transfers the standard-Veronese bounds to every residue.

For any fixed strict direction, the ratio of permanent to determinant multiplicities equals kappa_nu times j^(c_m−2n²+1)(1+O(1/j)), with kappa_nu>0. If 2n²>4m²−2m+3, in particular if n>=sqrt(2)m, determinant multiplicities eventually exceed the permanent multiplicities at every stretch, with a displayed effective threshold. Equality of dimensions still requires comparison of quotient degrees or lower Hilbert coefficients. This is a fixed-direction statement and does not establish orbit containment or settle finite-degree obstructions with changing labels.

Every fixed four-row direction eventually has no occurrence obstruction: the determinant multiplicity is eventually positive in the strict region, while the earlier containment arguments give the opposite weak multiplicity inequality on the two excluded faces at every stretch. The positive gaps proved here are therefore necessarily multiplicity obstructions after enough stretching.

### Weaker isolation conditions that survive dense substitution

I34 proves that a local coefficient-matrix nullity bounded by c in a sum of separated products is handled by changing at most max(1,c) coordinates of one prime cocharacter. The family jointly preserves coefficient spans over the working extension. All sums of at most three products need just one changed coordinate; a tensor-rank-four example is killed by every entire one-coordinate cylinder. Sampling still has an exponent depending on unbounded local nullity.

P14 proves that a scalar ROABP with every factor of rank one or full rank is hit by a common center plus w−1 interpolation pairs. A rank-one factorization splits the output, after clearing pivots, into nonzero scalar bridges; the same dense map preserves all bridges simultaneously. This covers every width-two ROABP with one pair, with established width-two PIT and rank-one splitting explicitly credited to AGKS. The construction preserves coefficient rows, while general intermediate-rank matrix contractions remain unresolved. The corresponding arithmetic point follows directly from P13 with K=w−1 over the rational coefficient model.
''')
with (OUT/'LEDGER.md').open('a') as f:
 f.write('\n\n## '+now+' — every-stretch comparison and weaker isolation gates\n\n')
 f.write('G-Q19 and G-Q20 are PROVED by G18 after complete root and independent purity proof readings. The exact direction criterion now yields gaps at every sufficiently large integer stretch, including rectangles; the all-integer ratio and an effective reverse dimension range are proved. Every fixed four-row direction eventually has no occurrence obstruction. I34 passes root/purity full proof checks and an independent root exact example computation; bounded local nullity gives the stated dense prime family. P14 passes root/isolation full proof checks and replaces full matrix-cone preservation by scalar bridge conditions for rank-one/full-rank factors. This is an ordinary progress entry, not the scheduled three-hour review.\n')
print(now)
