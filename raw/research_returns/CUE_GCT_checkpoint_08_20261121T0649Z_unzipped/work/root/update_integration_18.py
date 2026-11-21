"""Integrate checked higher-row asymptotics and the Borel isolation budget."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json

R=Path(__file__).resolve().parent
W=R.parent
OUT=W.parent/'deliverables'
now=datetime.now(timezone.utc).isoformat()
guard=R/'integration_18_check_events.tsv'
assert not guard.exists()
who='GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'
hashes={
 'P-17':('purity/P17_balanced_cubic_rank.tex','ba2c04ce09afbda22f3a183f8c3691e1cfbe909f50d046de9226749426b89297'),
 'I-40':('isolation/I40_borel_weight_budget.tex','d35eda616dd6af5e4c6d17012f8383d4e08a7c949d7c6e27a7a2608cd6563266'),
 'R-28':('rectangular/r28_fragment.tex','0c0349405b10d25a523f488e3400fdda392ee111c430eeda9b613c8a6753473b'),
 'G-22':('root/g22_fragment.tex','6b95183839d25a3dc2937478519fa3bbb8451c4a7234f562a15631575f3e8cb2'),
 'G-23':('root/g23_fragment.tex','421a759a42556e2108fb94b0e24ac069cdc1fb0e800f4da02eaacc307bbb17e8'),
}
for identifier,(path,digest) in hashes.items():
 assert hashlib.sha256((W/path).read_bytes()).hexdigest()==digest,(identifier,'changed proof')

p=R/'findings.tex';s=p.read_text()
assert '[G-22:' not in s and '[G-23:' not in s
s+='\n\n'+(R/'g22_fragment.tex').read_text()+'\n\n'+(R/'g23_fragment.tex').read_text()
p.write_text(s)

p=R/'grothendieck.tex';s=p.read_text()
marker='\\subsection{What the manuscript record does and does not establish}'
addition=r'''
\paragraph{R-28 and G-22. Added tangent bundles and Fourier-frame stability.}
The determinant differential has an independent cofactor subbundle
of rank $n^2$ on a nonempty quaternary parameter open. Each added
variable contributes a copy in a separate multidegree. The resulting
rank $(r-2)n^2+2$ equals the parameter dimension minus the dimension
of the generically finite-stabilizer left--right special-linear
orbit. The permanent padding map is generically injective after
projectivization: the irreducible nonlinear factor and padding
line are recovered uniquely. D-S3 identifies the group actions,
and D-FGA and EGA~IV$_3$, 13.1.3, identify these rank opens and
fiber-dimension calculations.

In G-22, the partial Fourier matrix is a frame in a rank-$r$
locally free representation, after scalar extension to $\mathbb C$.
Its rank-one Hermitian moments sum to the required diagonal
weight. The ordered tensor and the extremal flag line have
zero total traceless moment and finite projective stabilizer.
Multiplication of the linear sections and the outer symmetric
power preserve the minimum weight for every cocharacter, since
the corresponding initial sections have nonzero products in a
symmetric algebra. The Hilbert--Mumford criterion therefore
transports stability to the multiplied section. This is a
cocharacter and initial-term dictionary in D-S3; it does not
assert equality of the two Hermitian moment maps. The Schur
and exterior tensor operations belong to D-S6, V~2.1--2.2.1,
V~3.2 and V~3.10, with the precise representation-ring convention
already fixed above. The square roots give a complex existence
witness, not an integral point or an effective arithmetic sampler.

The cyclic product-plus-power family is an irreducible parameter
scheme. Nonzero coefficient minors impose the finite projective
Lie-stabilizer condition. Irreducibility of a form is open because
the reducible locus is a finite union of proper projective
multiplication images. An explicit Eisenstein section and the
coefficient calculation of its stabilizer show these opens are
nonempty. Their intersection with the stable open remains nonempty.
Varying the padding line avoids the fixed loci of the finite
automorphism group and leaves only the central group scheme
$\mu_r$ upstairs. Its character on the enhanced representation
is $r\nu_r$ and is trivial. Thus distinct nonzero scalar multiples
have distinct closed orbits. Invariant separation makes the
nonzero evaluation degrees have gcd one; the numerical-semigroup
argument gives every degree from $\beta^2$. Proper projective
images use D-Proper, and the character and stabilizer statements
use D-S3. All these orbit assertions are over characteristic zero.

\paragraph{G-23. Exact growth of enhanced invariant coordinate algebras.}
The Cartan cone attached to the flag weight has degree-$j$
coordinate module $S_{j\eta}V$. The diagonal Segre--Veronese
algebra is therefore
$\mathbb C[Y]_{sj}\otimes S_{j\eta}V$; taking invariants
extracts the single label $j\nu$. The stable quotient dimensions
are $u=(r-2)n^2+r_\eta-r^2+3$ and
$v=rm^2-2m+r+r_\eta-r^2+2$. This is a dimension computation
on two projective invariant schemes, not an equality of their
coordinate modules in $K_0$.

The explicit standard Veronese has $E=rT\beta!$.
Its positive leading Hilbert coefficients, combined with
nonzero sections in all sufficiently large original degrees,
give the ratio $\kappa j^{v-u}(1+O(j^{-1}))$ through every
integer stretch. The character-ring reduction cannot remove
the difference $v-u$; its nonvanishing is a separate elementary
congruence argument. D-FGA and EGA~II, 2.5.2, place the graded
coordinate algebras and projectivizations. The coefficient-degree
bound on the action and the parameter-degree bound on the orbit
map remain distinct. The construction proves the eventual sign
in the stated strict cone with $4\le r\le m$; boundary faces,
more rows, and effective positive extraction at individual
finite degrees remain outside this conclusion.

\paragraph{P-17. Exterior decoders, coefficient-rank strata, and odd weights.}
On the integral node scheme obtained by inverting all node
differences, the three-row Vandermonde matrix is a split
surjection and its kernel $K$ is locally free of rank $n-3$.
The cubic coefficient decoder is a diagonal isomorphism with
unit Vandermonde factors. Its balanced-ideal part is
$\bigwedge^3 K$, by the explicitly cited ideal theorem.
The coefficient-cut rank bounds are determinantal closed
conditions. The three-block contradiction, the support-at-least-four
property, and the leading exterior projections are valid in
every residue characteristic on this node scheme. The two end
kernel subbundles have intersection ranks zero and one at
$n=9$ and $n=10$, yielding respectively the incompatible wedge
degrees and the forced common exterior divisor in the proof.

For an invariant multilinear tensor, each Schmidt support is
an $\mathrm{SL}_2$ subrepresentation on its fixed-rank chart.
At an odd cut its split-torus characters are nonzero odd
integers. The Weyl element pairs opposite character spaces,+so their total rank is even, including over characteristic two.
With rank at most three this forces rank two at every odd cut,
and each affine core factors through a rank-two bundle.
The two-pair theorem I-37 then applies. Translation and reversal
are the two unipotent operations on the multihomogenization;
the closed coefficient-rank degeneration to the leading
translation term gives the eight-variable closure. The exact
torus reference is SGA~3, I~4.7.3; exterior and symmetric
operations use D-S6, and the rank-stratum formulation uses
D-FGA. No division by two or semisimplicity in positive
characteristic is used.

\paragraph{I-40. Determinant characters of Borel-stable support bundles.}
For the homogeneous common-translation-invariant tensor, the
two support bundles at a cut are Borel-stable, although they
need not be $\mathrm{SL}_2$-stable. Their determinant lines
are upper-unipotent fixed lines inside exterior powers of
full rational $\mathrm{SL}_2$ representations. The standard
dominant-character fact cited from Jantzen, Lecture~I,
pp.~2--3, gives nonnegative integer weights $\delta_i,\delta_i'$.
The nonsingular coefficient pairing of total weight $m=n-2D$
gives $\delta_i+\delta_i'=r_i m$. This is an equality in the
character lattice of the split torus, not a congruence in
the residue field.

The support inclusions $L_i\to L_{i-1}\otimes V$ give
equivariant affine core maps. Their unipotent covariance
makes every nonzero square determinant constant in the local
variable. Its constant term is then invertible, and its
torus covariance gives the exact increment
$\delta_i-\delta_{i-1}=r_i$ across a full-rank square core.
Telescoping the determinant-line character proves the
full-width run bound $n-2D$. Constant absorption preserves
it because a removed singular map cannot leave the next
full-width map invertible. At width three, weights zero and
one put the word in I-37 and I-38 respectively. The cubic
closure of P-17 then makes a nine-variable quartic annihilator
translation invariant of weight one and gives the contradiction.

This restatement uses the determinant exterior operation in
D-S6, the split torus and Borel group schemes in D-S3, and
the coefficient-rank charts in D-FGA. The rational evaluation
map is regular after inverting the node-pole differences.
Its generic two-simple-pole chart is dense in the balanced
degree-two rational family even in characteristic two.
Clearing the squarefree coordinate denominator and using the
explicit selector and Newton-simplex grids gives the finite
sample count in I-40, with its working-field and extension-input
conditions retained.

'''
addition=addition.replace('spaces,\\+so','spaces,\nso')
assert marker in s
p.write_text(s.replace(marker,addition+marker))

events=[
 ('G-22','targeted proof check','PASS complete root derivation and final reading: Fourier frame norms and moments, full-spark minors, m=r padding frame, ordered finite stabilizer, every-cocharacter minimum-weight identity under both symmetrizations, ray-type condition, exact Cartan extraction and quotient dimensions. Independent rectangular whole-proof PASS separately recorded.'),
 ('G-23','targeted proof check','PASS complete root derivation and final reading: exact growing-r dimensions, generic padding recovery, integer Derksen bound, p versus L, generator count, E grouping, gcd-one occurrence, every-residue Hilbert sandwich, both explicit sign thresholds, all-integer ratio, complete parity/mod4/nonresidue proof of no equality, exact integer threshold and rectangular square completion. Independent purity whole-proof PASS separately recorded; one typographic quad corrected.'),
 ('R-28','targeted proof check','PASS full root proof reading/rederivation at original hash36b154...; then reread widened common-free-point scope3<=r<=m at final hash0c0349... . R23 four-variable cyclic cofactor proof reopened; all new-variable blocks, left-right stabilizer, padding dimension, explicit cyclic Eisenstein and finite Lie stabilizer, common opens, padding-line freeness, central no-scaling and gcd-one occurrence checked. Dimension clauses remainr>=4.'),
 ('I-40','targeted proof check','PASS entire root reading/rederivation of six parts and convention audit at hashd35eda...: exact tensor convention, Borel support stability, determinant lines, both-side integer budget, inclusion-derived covariance, determinant constancy and +r increment, run bound through constant absorption, arbitrary slopes via I37/I38, all-characteristic nine-variable closure, dense partial-fraction chart, selector degrees and Newton-simplex sample count. Primary Jantzen pp2–3 also freshly read.'),
 ('G-B15','used and rechecked in this run','Primary Mukai Theorem7.4 printedp212, its ray-type linear formulation(7.3)p213, and displayed proof pp218–219 reopened and read for G22; the criterion is used as established background. No new proof of its earlier valuation prerequisites claimed.'),
 ('G-B13','used and rechecked in this run','Primary Derksen2001 printedp956 Theorem1.1 and Proposition1.2 reopened and read; r² parameters, dimensionr²−1, equationdegree r and actiondegree L give sigma<=rL^(r²−1), then beta=ceil(3r²b/8)L^(2(r²−1)).'),
 ('I-B09','used and rechecked in this run','Primary Jantzen LectureI pp2–3 freshly opened and read: Frobenius reciprocity with both maps and lower-Borel SL2 induction equals Sym^d(V*) for d>=0 and zero for d<0, before any characteristic-zero simplicity assertion. Upper-line convention verified by dualizing and Weyl conjugation; direct Bruhat audit also fully read.'),
]
with guard.open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['statement_id','date','who','type','outcome'])
 for ident,kind,outcome in events:w.writerow([ident,now,who,kind,outcome])
(R/'integration_18_review_hashes.json').write_text(json.dumps({'checked_utc':now,'who':who,'proofs':{k:{'path':v[0],'sha256':v[1]} for k,v in hashes.items()},'status':'All complete proof readings PASS; external primary inputs separately scoped'},indent=2)+'\n')

p=R/'intro.tex';s=p.read_text()
needle='\n\nOn isolation,'
addition=r'''

The higher-row construction G-22 uses an ordered Fourier frame and
cocharacter minimum weights to provide a common stable tensor in
every strict direction with $r\le m$. R-28 removes its scalar-orbit
period and gives $\dim\mathcal D_{n,r}=(r-2)n^2+2$.
For $m\ge17$ and $4\le r\le m$, G-23 consequently proves
\[
 \frac{m_{j\nu}(\ell^{n-m}\operatorname{per}_m)}
      {m_{j\nu}(\det_n)}
 =\kappa_\nu j^{rm^2-(r-2)n^2-2m+r-1}(1+O(j^{-1})).
\]
Both multiplicities are positive at every sufficiently large integer
stretch, and the exponent is never zero. Its sign, with explicit
bounds for both alternatives, gives the exact eventual comparison
in every stated strict direction. Every rectangle with
$m<n<rm/(r-1)$ lies in the positive range. Boundary faces and
individual finite degrees retain their separate scope.
'''
assert needle in s
s=s.replace(needle,addition+needle,1)
needle='The precise conditional matrix-invariant consequence remains I-08.'
assert needle in s
s=s.replace(needle,'P-17 gives characteristic-free coefficient-cut obstructions, including every balanced two-pair cubic annihilator through ten variables. I-40 bounds full-width invertible runs of a homogeneous translation-invariant tensor by its integer weight $n-2D$. At weight one this gives isolated invertible factors and closes the complete balanced two-pair width-three problem through nine variables, with an explicit finite rational sampler. The ordinary unweighted centered map is not identified with that balanced map for every nine-variable polynomial. '+needle)
p.write_text(s)

p=R/'open_gates.tex';s=p.read_text()
s=s.replace('Individual higher-row multiplicities, changing directions, finite-degree comparisons on the eventual opposite side, and the superlinear-padding GCT regime remain unresolved.','G-22, R-28 and G-23 now determine the eventual sign in every strict direction with $4\\le r\\le m$ for $m\\ge17$, with both occurrences at all sufficiently large integer stretches and no integer equality case. More than $m$ rows, the first-row boundary face in higher rank, individual finite degrees, changing directions, and the superlinear-padding GCT regime remain unresolved.')
s=s.replace('Consecutive invertible runs of length at least two, nonlinear singular factors, and the growing-width question remain open.','I-40 supplies a determinant-character run bound for homogeneous translation-invariant tensors and closes weights zero and one through I-37/I-38. Together with P-17 it proves the balanced two-pair theorem through nine variables, including an explicit grid. The next balanced small case is a translation-invariant ten-variable quartic of weight two. Longer runs in unrestricted words, nonlinear singular factors, and the growing-width question remain open.')
start=s.index('\\subsection{Updated sharp gates after')
s=s[:start]+r'''\subsection{Updated gates after the higher-row and determinant-weight refinements}
R-27 closes the uniform quaternary dimension and specified Tor gate.
G-23 extends the exact eventual sign to every strict direction with
$4\le r\le m$, using G-22 and R-28. The higher-rank boundary face,
more than $m$ rows, finite-degree extraction and changing directions
remain open. A boundary degeneration to $(r-1)$ variables is the
next rectangular comparison under investigation; no result of that
attempt is asserted in this paragraph.

P-17 and I-40 close the balanced two-pair width-three question
through nine variables and all cubic annihilators through ten.
The determinant-character budget preserves the original affine-core
structure omitted by the failed abstract Hessian test of I-39.
At weight two it permits two consecutive invertible cores, so the
translation-invariant ten-variable quartic is the next small case.
General mixed words, nonlinear singular factors and uniform
polynomial dependence on growing width remain separate gates.
'''
p.write_text(s)

p=W/'assemble.py';s=p.read_text()
s=s.replace('Invariant quotients give the exact eventual four-row rectangular range; enhanced tensors classify all four-row stretched directions and give the exact eventual multiplicity sign, with explicit stretch bounds and a sharp uniform rectangular threshold.','Invariant quotients give the exact eventual four-row rectangular range. Fourier frames and common free tensors extend the exact eventual sign to every strict direction through $m$ rows for sizes at least seventeen, with explicit stretch bounds and no integer dimension-equality case.')
s=s.replace('two centered pairs for affine singular-factor words, and explicit arithmetic points with trace-coordinate span recovery.','two centered pairs for affine singular-factor words, and explicit arithmetic points with trace-coordinate span recovery. An all-characteristic determinant-weight budget and coefficient-cut arguments prove the complete balanced two-pair width-three result through nine variables.')
p.write_text(s)

p=R/'sources.md';s=p.read_text()
s=s.replace('For G19, Definition5.20 and Corollary5.21, printedp170, and the character discussion in Proposition5.19, printedp168, were reopened and checked.','For G19, Definition5.20 and Corollary5.21, printedp170, and the character discussion in Proposition5.19, printedp168, were reopened and checked. For G22, Theorem7.4, printedp212, its linear ray-type formulation equation(7.3), p213, and its displayed proof pp218–219 were freshly read. This supplies the stable one-parameter-subgroup minimum-weight criterion; the Fourier frame and multiplication step are proved in G22.')
p.write_text(s)

p=R/'questions.tsv'
with p.open(newline='') as f: reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
new=[
 ('G-Q26','G22; Mukai7.4 printedp212','Can common stable enhanced tensors be constructed for every strict partition direction in more than four rows?','PROVED G22 for n>m>=r>=2: Fourier-frame ordered moments plus preservation of every cocharacter minimum weight under multiplication; m=r uses the padding line as the final projective-frame line.'),
 ('G-Q27','G23; R28; G21','What is the exact eventual multiplicity sign for strict directions with4<=r<=m?','PROVED G23 for m>=17: both multiplicities positive for every j>=beta², ratio kappa*j^[r m²−(r−2)n²−2m+r−1], exponent neverzero, exact floor boundary and explicit every-integer thresholds for both signs. First-row boundary, r>m and finite earlier degrees remain separate.'),
 ('G-Q28','G23 rectangular corollary; next boundary degeneration','Does the strict higher-row rectangular range exhaust eventual positive gaps including its boundary?','PROVED INSIDE STRICT RANGE by G23 for m>=17,4<=r<=m: m<n<r m/(r−1). OPEN at the equality boundary in this entry; the proposed next gate is restriction of invariant functions to the (r−1)-variable degeneration. Above the boundary the padding one-parameter subgroup gives zero permanent rectangles.'),
]
existing={row['id'] for row in rows}
for ident,source,question,state in new:
 assert ident not in existing
 rows.append(dict(zip(fields,[ident,source,question,state])))
with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)

with (OUT/'LEDGER.md').open('a') as f:
 f.write('\n\n## '+now+' — higher-row phase and determinant-weight isolation\n\n')
 f.write('G22 and R28 give common stable projectively free points in every strict direction withr<=m, and R28 gives exact determinant image dimensions. G23 closes the eventual sign gate throughmrows for m>=17, including a proof that the integer exponents cannot tie. P17 and I40 close the complete balanced two-pair width-three question through nine variables; all cubic annihilators are excluded through ten. Complete root and independent-agent proof readings passed, with exact source and hash scopes. These are dated results; the next actual scheduled review remains05:49:46UTC. Packaging is not counted as movement.\n')
with (OUT/'IMPLICATIONS.md').open('a') as f:
 f.write('''\n\n### Higher-row strict directions and a preserved affine isolation invariant\n\nFor n>m>=17 and4<=r<=m, every fixed partition direction nu ofsize ns with nu_r>0 and nu_1>(n−m)s has both multiplicities positive at every sufficiently large integer stretch. Their ratio has exponent r m²−(r−2)n²−2m+r−1. G23 proves that this integer never vanishes and gives explicit thresholds for either sign. G22 constructs the common stable tensor by an ordered Fourier frame and exact one-parameter initial weights; R28 removes all projective symmetries by a cyclic product-plus-power family and a generic padding line. This extends the asymptotic comparison beyond four rows, but does not give a polynomial positive extraction algorithm, decide every finite degree, or prove a superlinear-padding lower bound.\n\nP17 excludes balanced two-pair multilinear width-three annihilators through eight variables and all cubic annihilators through ten. I40 then closes nine variables by retaining the Borel character of each coefficient-support determinant line. Each square full-rank affine core consumes its whole rank from a total character budget; weight one permits only isolated full-rank cores and falls under I38. The exact finite balanced grid has at most(n+1)² binom(D+3,3) points with the stated working-field size. The next small balanced case is a translation-invariant ten-variable quartic of weight two. No joint polynomial bound in growing width follows.\n\nThe Grothendieck transport uses split torus character lattices, Borel-stable support bundles, determinant exterior operations, cocharacter initial terms, Cartan cone coordinate algebras and projective invariant quotients. These are exact dictionaries to the listed SGA3, SGA6, EGA and FGA locators; they do not identify complex moment-map witnesses with integral arithmetic points or supply missing original archive scans.\n''')
print(now)
