"""Integrate nonrectangular boundary extension and weight-three closure."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json
R=Path(__file__).resolve().parent;W=R.parent;O=W.parent/'deliverables'
guard=R/'integration_23_check_events.tsv';assert not guard.exists()
now=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro; /root; effort not exposed; CUE_GCT_20261121_R1'
hashes={
 'rectangular/r32_fragment.tex':'964362d2ebce7d19fab7d99c45d0ebf3e47cdce03a01ee6716f475b14dd50f3d',
 'isolation/I43_weight_three_connectors.tex':'7e47c4d369d318104f3908dd85e9086d1fab3a528808ec3d94c6bea4f1bf06be',
 'root/g27_fragment.tex':'d627bfa4381ed5e8eb3bf15a2bb4fefdb1697b74899a55a44f28ffbb6130bda4'}
for rel,h in hashes.items():assert hashlib.sha256((W/rel).read_bytes()).hexdigest()==h
for rel,needle in [('rectangular/findings.tex','R-32:'),('isolation/findings.tex','I-43.')]:assert needle in (W/rel).read_text()
p=R/'findings.tex';s=p.read_text();assert '[G-27:' not in s;p.write_text(s+'\n\n'+(R/'g27_fragment.tex').read_text())
audits={
 'R32':('rectangular/r32_fragment.tex','Complete proof read. The orthogonal block sizes lie between2 andd−1; each normalized rational moment list has trace d. The two unit product moments give the full prescribed moment. Distinct mixed bidegrees and independent partials force finite complex projective stabilizer of the sum. The common enhanced tensor has zero special-linear moment, and its finite projective stabilizer implies stability. A nontrivial auxiliary flag avoids the finite polynomial automorphism group; the central exponent ds−|eta|=r nu_r gives no-scaling. Rectangles receive only stability and quotient dimension, exactly as stated.'),
 'I43':('isolation/I43_weight_three_connectors.tex','Complete proof read and every new connector calculation rederived. At determinant weight0 the u² wedge coefficient survives, or primitive affine row factorization gives the exact simple-pole factor. At weight1 the Grassmann orbit line gives stable two/four-planes. Four distinct paired torus characters and the physical unipotent exclude q>1 without semisimplicity, forcing weights(1,1,−1). Common-covector rank-one updates make the compound affine; a unique internal pole evaluates its coefficient at an invertible linear transform of t,z. All pivots, interval contractions and endpoints use the same parameters. I42 applies at run bound3, and the P19/translation-leading/reversal induction closes all n≤11. Root freshly read the complete primary Grassmann Lemma3 proof.'),
 'G27':('root/g27_fragment.tex','Complete author proof reread. R32 gives period one only for the nonrectangular determinant algebra A; the possibly rectangular tail algebra B needs merely stability for its dimension. Both row ranges, exact dimensions, u−v≥m²−m−2, v lower bound, common beta/E/p bounds and the degreewise Pieri injection check. If g is the gcd of B generator degrees, all multiples g beyond beta² occur. For a nonzero B_j, g divides t and2E−t, so the upper multiplication exists despite period. The A lower multiplier uses its actual no-scaling point. The standard-Veronese Hilbert bounds and strict integer threshold check. The later proof-introduction sentence is a formatting-only change from1c3a8c...; all mathematical text is unchanged.')}
for name,(rel,body) in audits.items():
 (R/f'independent_review_{name}_root.md').write_text(f'# Complete root proof reading: {name}\n\nActual record: {now}\n\nWho: {who}.\n\nSHA256: {hashes[rel]}\n\nOutcome: PASS. {body}\n')

p=R/'grothendieck.tex';s=p.read_text();marker='\\subsection{What the manuscript record does and does not establish}'
addition=r'''
\paragraph{R-32 and G-27. Unpadded stable quotients and a one-sided degree semigroup.}
The same two-product parameter morphism, without a padding
line, meets every prescribed positive moment direction when
each factor block has rank at most $d-1$. Its enhanced tensor
is stable. A nonzero flag weight allows a generic flag section
to remove the remaining finite projective stabilizer. The
central character then vanishes on the special linear center.
For a rectangular label the flag is a point, so only stability
and the quotient dimension are retained. This is the D-S3
stabilizer and cocharacter construction with the D-S6 Schur
line and D-FGA enhanced coordinate scheme; no integral
moment-map assertion is made.

G-27 uses two such schemes, in ranks $r$ and $r-1$. The upper
comparison needs no degree-period-one property on the lower
scheme. If $g$ is the gcd of its homogeneous generator
degrees, every sufficiently large multiple of $g$ is present.
Whenever its degree-$j$ piece is nonzero, a nonzero multiplier
places that piece inside a suitable degree of the standard
Veronese. The determinant algebra, used for a lower bound,
does have period one. Thus the projective Hilbert comparison
works at every original degree without identifying the two
semigroups. These are the graded-domain and Proj constructions
of D-FGA and EGA~II, 2.5.2. Together with the Pieri tail
dictionary of G-26, they classify every fixed nonrectangular
direction through $2m-1$ rows. The finite degree thresholds
are effective bounds, not polynomial-size algorithms.

\paragraph{I-43. A Pl\"ucker line constrains actual adjacent support bundles.}
A determinant-weight-one line in the third exterior power
generates a standard rank-two $\mathrm{SL}_2$ module. Its
projectivization lies in the Grassmannian, whose line
description gives an invariant rank-two subspace inside an
invariant rank-four space. The exact known Grassmann input
is I-B10, Lemma~3, p.~4. The actual preceding coefficient
support has rank at most three. Its split-torus characters
and the physical unipotent action exclude a larger pair
of opposite weights in that invariant two-plane, leaving
weights $(1,1,-1)$ on the rank-three support.

No splitting of these module extensions is needed in a
positive-characteristic fiber. The normalized core updates
have a common covector, so their second exterior map is
affine in the internal variables. A single node pole detects
each nonzero coefficient while the two anchor evaluations
remain independent. The determinant-weight-zero case uses
one divided-square anchor and an arbitrary opposite affine
anchor. These identities hold on the actual coefficient
rank charts over the same rational parameter field. The
preserved two-dimensional contractions compose, including
the endpoint projections, before applying the I-42 reset
argument. D-S3 locates the group scheme and characters,
D-S6 the exterior/divided operations, and D-FGA the
Grassmann and determinantal charts. The result is valid on
every field fiber with distinct nodes: all weights at most
three and, using P-19, every multilinear input on at most
eleven variables are hit by the balanced two-pair sampler.

'''
assert marker in s;p.write_text(s.replace(marker,addition+marker))

p=R/'intro.tex';s=p.read_text()
s=s.replace('Thus every fixed direction through $m$ rows is classified eventually; boundary faces beyond $m$ rows and individual finite degrees retain their separate scope.','Thus every fixed direction through $m$ rows is classified eventually. R-32 and G-27 additionally classify every fixed nonrectangular direction through $2m-1$ rows, allowing a degree period in the lower comparison algebra. Rectangular directions beyond $m$ rows, the next boundary row and individual finite degrees retain their separate scope.',1)
s=s.replace('it supplies positive saturated-run classes with explicit remaining rank gates. The precise conditional matrix-invariant consequence remains I-08.','it supplies positive saturated-run classes. I-43 closes every weight-three connector: a Grassmann orbit line and the actual adjacent support bound force a rank-one update pattern, while the weight-zero anchor case is handled directly. Shared-parameter contractions then give the complete balanced two-pair theorem through eleven variables in every characteristic. Weight four and the unrestricted higher-degree case remain open. The precise conditional matrix-invariant consequence remains I-08.',1)
p.write_text(s)
p=R/'open_gates.tex';s=p.read_text()
s=s.replace('the nonrectangular first-row boundary face beyond $m$ rows','the nonrectangular first-row boundary face from $2m$ rows onward')
s=s.replace('The next unrestricted balanced small case has eleven variables.','I-43 closes weight three and the complete balanced theorem through eleven variables. The next unrestricted balanced small case has twelve variables.')
start=s.index('\\subsection{Updated gates after the complete boundary comparison}')
s=s[:start]+r'''\subsection{Updated gates after nonrectangular boundary and weight-three closure}
R-27 closes the uniform quaternary dimension and specified Tor gate.
R-29/R-30 and G-25 give the exact strict-direction sign through
$2m$ rows. G-26 classifies every fixed direction through $m$
rows. R-32 and G-27 extend the complete nonrectangular
classification through $2m-1$ rows: the lower tail algebra
may have a degree period, because the comparison requires
only its upper Hilbert bound. Rectangular directions beyond
$m$ rows, the $2m$-row nonrectangular boundary, strict
directions beyond $2m$ rows, changing directions and efficient
finite-degree extraction remain open. R-31 excludes the
unchanged two-product no-scaling strategy in specified
$2m+1$-row directions, with no vanishing claim on the full cones.

P-19 proves the unrestricted cubic theorem in every variable
count and characteristic. I-43 closes all determinant weights
at most three and the complete balanced two-pair theorem
through eleven variables. Its Grassmann-line and unique-pole
arguments preserve all contractions and endpoints over the
same parameters before using the I-42 reset criterion.
The next general weight is four and the next unrestricted
variable count is twelve. Longer constrained connectors,+nonlinear singular factors, shared-seed synchronization and
uniform polynomial dependence on growing width remain open.
'''.replace('connectors,\\+nonlinear','connectors,\nnonlinear')
p.write_text(s)

p=W/'assemble.py';s=p.read_text()
s=s.replace('including the full first-row equality face. Graph isolation','including the full first-row equality face; separate unpadded quotients extend the nonrectangular classification through $2m-1$ rows. Graph isolation',1)
s=s.replace('An all-characteristic determinant-weight budget and coefficient-cut arguments prove the complete balanced two-pair width-three result through ten variables.','An all-characteristic determinant-weight budget, Grassmann-line connectors and coefficient-cut arguments prove the complete balanced two-pair width-three result through eleven variables.',1)
p.write_text(s)
p=R/'questions.tsv'
with p.open(newline='') as f:rr=csv.DictReader(f,delimiter='\t');fields=rr.fieldnames;rows=list(rr)
for row in rows:
 if row['id']=='G-Q30':row['state']+=' Subsequent G27 extends the complete nonrectangular classification through2m−1 rows; rectangular labels beyondm remain separate.'
rows.append(dict(zip(fields,['G-Q31','G27; R32; G26 Pieri tail bound and G18 semigroups','Can nonrectangular boundary directions beyondm rows be compared at every large integer even when the lower tail algebra has a period?','PROVED G27 for m>=17,m<r<=2m−1: unpadded A has period one, stable B may have arbitrary gcd g. Each nonzero B_j injects into B_E(k+2) because g divides its residue and all large multiples g occur. Exact u>v and the explicit same-form threshold give strict determinant dominance on/below the face. All fixed nonrectangular directions through2m−1 are classified eventually.'])))
with p.open('w',newline='') as f:ww=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n');ww.writeheader();ww.writerows(rows)

with guard.open('w',newline='') as f:
 wr=csv.writer(f,delimiter='\t',lineterminator='\n');wr.writerow(['statement_id','date','who','type','outcome'])
 for name,(_,body) in audits.items():wr.writerow([name[0]+'-'+name[1:],now,who,'targeted proof check','PASS whole-proof reading. '+body])
 wr.writerow(['I-B10',now,who,'used and rechecked in this run','Fresh primary author PDF read of Ghorpade–Patil–Pillai Lemma3, printedp4, including its full proof and arbitrary-field convention atp3. Exact use: a Grassmann line has fixed codimension-one intersection and one-larger span.'])
(R/'integration_23_review_hashes.json').write_text(json.dumps({'checked_utc':now,'who':who,'status':'PASS complete proof readings','hashes':hashes},indent=2)+'\n')
with (O/'LEDGER.md').open('a') as f:f.write(f'\n\n## {now} — nonrectangular classification through2m−1 and balanced n≤11\n\nR32 supplies common stable unpadded points, and period one for every nonrectangular direction in its row range. G27 uses these to extend the first-row boundary comparison through2m−1 rows: the lower tail algebra is allowed an arbitrary degree period, handled by a one-sided semigroup multiplier. I43 uses a Grassmann line and actual adjacent support to close weight3 over every characteristic, and P19 then gives the complete n≤11 balanced theorem. All three full proofs passed root and independent specialist readings; exact hashes and the formatting-only G27 transition are recorded.\n')
with (O/'IMPLICATIONS.md').open('a') as f:f.write('''\n\n### Nonrectangular directions and weight-three tensors\n\nR32 and G27 extend the complete eventual nonrectangular classification through2m−1 rows for m≥17. A nonrectangular auxiliary flag provides period one on the determinant comparison algebra. The lower tail algebra may remain periodic: every nonzero residue has a large complementary degree, which is enough for the upper Hilbert bound. This closes additional equality and below-face directions without assuming generic rectangular freeness or equality of two degree semigroups.\n\nI43 proves the balanced two-pair sampler for every homogeneous translation-invariant multilinear width-three tensor of weight n−2D≤3. A Grassmann-line input restricts its actual adjacent support enough to make the middle compound affine, and all connector and endpoint tests use one shared parameter field. Combined with the full cubic theorem, this proves the sampler for every multilinear width-three input on at most11 variables. The next general weight4 and growing-width PIT questions remain distinct.\n''')
print(now)
