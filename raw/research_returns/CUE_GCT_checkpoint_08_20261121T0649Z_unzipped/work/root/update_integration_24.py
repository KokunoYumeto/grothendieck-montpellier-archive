"""Integrate generic-stabilizer boundary comparison and bounded chain connectors."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json
R=Path(__file__).resolve().parent;W=R.parent;O=W.parent/'deliverables'
guard=R/'integration_24_check_events.tsv';assert not guard.exists()
now=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro; /root; effort not exposed; CUE_GCT_20261121_R1'
hashes={
 'rectangular/r33_fragment.tex':'34fc9cae09bbf7c2c58b7efa649a575de826636fa12439fbf2a64e5baca7aded',
 'root/g28_fragment.tex':'de5e7f1401fb8f65ec35c865e527482d2891fb75eb08b2914f3be61a592b4160',
 'isolation/I44_torus_chain_connectors.tex':'759c2fd7a18ecc3953c6c8e3f60bb7739786e03cd80319d8fe97db4ae9c75268'}
for rel,h in hashes.items():assert hashlib.sha256((W/rel).read_bytes()).hexdigest()==h
for rel,needle in [('rectangular/findings.tex','R-33:'),('isolation/findings.tex','I-44.')]:assert needle in (W/rel).read_text()
p=R/'findings.tex';s=p.read_text();assert '[G-28:' not in s;p.write_text(s+'\n\n'+(R/'g28_fragment.tex').read_text())
audits={
 'R33':('rectangular/r33_fragment.tex','Complete root proof reading of initial c74d38f mathematical text and final source clarification. The generic differential kernel equals the independent row-column zero-character gauge space on a nonempty parameter open. Every-Plucker nonvanishing intersects it. Subtracting c/m times the variable identity reduces a projective Lie symmetry to that kernel. All q-subset weight sums then agree, forcing every matrix-unit weight equal; the zero character makes it zero. Independence of the coefficient matrices gives zero projective Lie stabilizer. Its open locus gives finite generic projective stabilizer, and a quotient fiber contains the full-dimensional generic orbit, yielding only the upper dimension bound. Root freshly read Stacks tag0B2L(2), including its complete proof; EGA/SGA semicontinuity is retained only for its correct openness scope.'),
 'G28':('root/g28_fragment.tex','Complete author proof reread. R32 applies to A in rows≤2n−2 and provides nonrectangular period one. R33 applies to B at q=r−1<m² and gives only w≤v. The u−v lower bound needs merely n≥m+1,r≥m+1; the factorization (q−1)(m²−q−1) gives v>2. B=C is treated separately; at w1 its standard Veronese projective image is a reduced point. For every w≤v the image-degree and binomial upper bounds are monotone, so the arbitrary-period G27 multiplier proves the unchanged explicit threshold. Full nonrectangular classification through2m and the larger boundary-only range are correctly separated.'),
 'I44':('isolation/I44_torus_chain_connectors.tex','Complete root proof reading and rederivation. Checked all six two-row and four three-row subsets of the four possible anchor weights, repeated-weight exclusions, and the five surviving matrices. Recomputed G1/G2 exterior rows and the reverse B anchor through the actual antidiagonal pairing. The residual determinant has precisely the stated square and ordered cross coefficients. One-pole annihilation gives two independent row equations without a factor two, hence three neighbors per nonzero row. With at most five internal positions one type has at most two; the forced order makes B0 vanish and factors the connector into two nonzero linear forms. The simultaneous rank and endpoint argument, I42 characteristic split, factor-weight reduction and complete n12/n13 induction all check.')}
for name,(rel,body) in audits.items():
 (R/f'independent_review_{name}_root.md').write_text(f'# Complete root proof reading: {name}\n\nActual record: {now}\n\nWho: {who}.\n\nSHA256: {hashes[rel]}\n\nOutcome: PASS. {body}\n')

p=R/'grothendieck.tex';s=p.read_text();marker='\\subsection{What the manuscript record does and does not establish}'
addition=r'''
\paragraph{R-33 and G-28. A generic Pl\"ucker chart and a quotient upper bound.}
The maximal differential rank of the permanent coefficient
morphism identifies its generic tangent kernel with the
row-column diagonal gauge directions. On the Grassmann
open where every Pl\"ucker coordinate of the coefficient
matrix span is nonzero, any diagonal operator preserving
that span has equal sums on every fixed-size coordinate
subset. Exchanging one index forces all individual weights
equal. The zero gauge character makes the scalar zero.
Thus the generic projective stabilizer has zero Lie algebra
and is finite over $\mathbb C$.

These are the determinantal and Grassmann opens of D-FGA
and the torus character calculation of D-S3. Stabilizer
openness retains the precise SGA~3 VI$_B$, Proposition~4.1
and cited EGA~IV$_3$, Theorem~13.1.3 framework. The generic
fiber dimension equality is separately cited from the
Stacks Project, Lemma~33.20.4(2), tag~0B2L (R-B18), whose
complete primary proof was read. A fiber of the invariant
quotient contains the orbit through its generic point.
This gives only an upper bound on quotient dimension;
it asserts neither stability nor equality.

G-28 uses exactly that upper bound on the lower permanent
algebra. Its actual dimension may be smaller, or the ring
may contain only constants. The projective image degree and
Hilbert upper estimates decrease with that dimension, so
the G-27 comparison still holds. This closes all fixed
nonrectangular directions through $2m$ rows and extends
the boundary-only comparison to
$r\le\min\{2n-2,m^2\}$. The Schur tail, Proj and degree
semigroup constructions retain the D-S6/D-FGA interpretation
already given; generic freeness is not substituted for
the stable-point hypothesis needed for the upper determinant
algebra's period one.

\paragraph{I-44. Torus chains, anchor charts, and a residue-support condition.}
The normalized cores move between integer torus characters
differing by two. Unless the rank-three support is a chain
of three successive such characters, their updates have
a common image or covector, and the second exterior map
is affine. In the chain case, the actual preceding support
allows four weights. Minimal coefficient independence and
rank two leave precisely the five anchor charts displayed
in I-44. These statements use the D-S3 character grading
and D-FGA rank charts and hold on every characteristic fiber.

Two anchor types have a unique nonzero pole coefficient.
The third, paired with the actual reverse anchor, reduces
the second exterior map to an explicit quadratic. A square
coefficient gives a double pole. In the multilinear case,+the coefficient of $tz$ and the simple residues impose two
independent equations on each row. Every nonzero row would
therefore need at least three neighbors. With at most five
internal positions, one of the two coefficient types has
at most two entries, forcing an order that makes the
quadratic factor into nonzero linear forms. The evaluation
kernel cannot contain that product.

The resulting interval and endpoint assertions use a single
parameter field before invoking the reset-Hessian theorem.
The exterior operations belong to D-S6, without division
by two. The characteristic-two distinction occurs only in
the subsequent I-42 scalar Hessian step: four-core runs
are covered on every fiber, and five-core runs where two
is invertible. Factor weights then give the complete balanced
theorem through twelve variables in every characteristic
and thirteen away from two, with the stated finite grid.

'''.replace('case,\\+the','case,\nthe')
assert marker in s;p.write_text(s.replace(marker,addition+marker))

p=R/'intro.tex';s=p.read_text()
s=s.replace('R-32 and G-27 additionally classify every fixed nonrectangular direction through $2m-1$ rows, allowing a degree period in the lower comparison algebra. Rectangular directions beyond $m$ rows, the next boundary row and individual finite degrees retain their separate scope.','R-32/R-33 and G-27/G-28 additionally classify every fixed nonrectangular direction through $2m$ rows. The lower comparison algebra may have a degree period and need only satisfy a quotient-dimension upper bound. Boundary comparison extends further to $r\\le\\min\\{2n-2,m^2\\}$ for nonrectangular labels. Rectangular directions beyond $m$ rows, larger strict directions and individual finite degrees retain their separate scope.',1)
s=s.replace('Weight four and the unrestricted higher-degree case remain open. The precise conditional matrix-invariant consequence remains I-08.','I-44 classifies every chain anchor and preserves all interval ranks through five full-rank cores. The reset criterion yields weights at most four in every characteristic and at most five away from two; the complete balanced theorem follows through twelve variables, and thirteen away from two. Weight five in characteristic two and the next higher-degree cases remain open. The precise conditional matrix-invariant consequence remains I-08.',1)
p.write_text(s)
p=R/'open_gates.tex';s=p.read_text()
s=s.replace('the nonrectangular first-row boundary face from $2m$ rows onward','nonrectangular boundary faces beyond $r\\le\\min\\{2n-2,m^2\\}$')
s=s.replace('The next unrestricted balanced small case has twelve variables.','I-44 further closes the balanced theorem through twelve variables in every characteristic and thirteen away from two. The next unrestricted small cases are thirteen variables in characteristic two and fourteen otherwise.')
start=s.index('\\subsection{Updated gates after nonrectangular boundary and weight-three closure}')
s=s[:start]+r'''\subsection{Updated gates after the generic-stabilizer and chain-anchor arguments}
R-27 closes the uniform quaternary dimension and specified Tor gate.
R-29/R-30 and G-25 give the strict-direction sign through
$2m$ rows. G-26 classifies every fixed direction through
$m$ rows. R-32/R-33 and G-27/G-28 classify every fixed
nonrectangular direction through $2m$ rows, with a further
boundary-only range $r\le\min\{2n-2,m^2\}$.
Rectangular directions beyond $m$ rows, strict directions
past $2m$ rows, changing directions and efficient finite-degree
extraction remain open. R-31 excludes the unchanged two-product
no-scaling strategy in specified $2m+1$-row directions;
it imposes no vanishing on the full cones.

P-19 proves the cubic theorem in every variable count and
characteristic. I-44 preserves all one-pole interval ranks
through five full-rank cores by its complete torus-chain
anchor calculation. The I-42 scalar step then gives weights
at most four in every characteristic and at most five away
from two. The complete balanced two-pair theorem holds
through twelve variables, and thirteen away from two.
The characteristic-two weight-five gate consists of possible
saturated five-core runs whose ranks are now preserved but
whose reset Hessian needs an additional constraint.
At longer lengths the remaining two-anchor quadratic is
explicit; both internal coefficient types can have at least
three positions. Nonlinear singular factors, general
shared-seed synchronization and uniform polynomial dependence
on growing width remain open.
'''
p.write_text(s)
p=W/'assemble.py';s=p.read_text()
s=s.replace('extend the nonrectangular classification through $2m-1$ rows.','and a generic-stabilizer upper bound extend the nonrectangular classification through $2m$ rows.',1)
s=s.replace('through eleven variables. A smallest-counterexample','through twelve variables in every characteristic and thirteen away from two. A smallest-counterexample',1)
p.write_text(s)

p=R/'questions.tsv'
with p.open(newline='') as f:rr=csv.DictReader(f,delimiter='\t');fields=rr.fieldnames;rows=list(rr)
for row in rows:
 if row['id']=='G-Q31':row['state']+=' Subsequent R33/G28 remove the lower stability requirement and extend the complete nonrectangular classification through2m rows.'
rows.append(dict(zip(fields,['G-Q32','G28; R33; G27 semigroup/Hilbert comparison','Can generic finite stabilizers replace lower-cone stability and extend the boundary comparison?','PROVED G28 for m>=17,m<r<=min(2n−2,m²),nonrectangular on/below-face labels. R33 supplies only dimB<=v; actual dimension0/1 and all residues are handled explicitly. All fixed nonrectangular directions through2m are now classified eventually; rectangular labels beyondm and strict directions beyond2m remain separate.'])))
with p.open('w',newline='') as f:ww=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n');ww.writeheader();ww.writerows(rows)

with guard.open('w',newline='') as f:
 wr=csv.writer(f,delimiter='\t',lineterminator='\n');wr.writerow(['statement_id','date','who','type','outcome'])
 for name,(_,body) in audits.items():wr.writerow([name[0]+'-'+name[1:],now,who,'targeted proof check','PASS whole-proof reading. '+body])
 wr.writerow(['R-B18',now,who,'used and rechecked in this run','Fresh complete primary Stacks Lemma33.20.4(2), tag0B2L, statement and proof read. Used for generic fiber dimension, separately from the EGA/SGA semicontinuity locator.'])
(R/'integration_24_review_hashes.json').write_text(json.dumps({'checked_utc':now,'who':who,'status':'PASS complete proof readings','hashes':hashes},indent=2)+'\n')
with (O/'LEDGER.md').open('a') as f:f.write(f'\n\n## {now} — complete nonrectangular comparison through2m and chain-anchor closure\n\nR33 proves generic finite projective stabilizer of projected permanents in4<=q<m² from the exact tangent kernel and a full Plucker chart. G28 uses only its quotient-dimension upper bound, including possible constant or one-dimensional invariant rings, to extend the boundary range and complete every fixed nonrectangular comparison through2m rows. I44 proves the complete short-chain anchor calculation and one-pole rank preservation through five cores. The scalar theorem holds through four cores in every characteristic and five away from two, giving all multilinear n≤12 and n≤13 away from two. All full proofs have root and independent specialist PASS records.\n')
with (O/'IMPLICATIONS.md').open('a') as f:f.write('''\n\n### Generic stabilizers and all short torus-chain connectors\n\nR33/G28 remove the need for a lower stable point in the boundary comparison. The exact tangent kernel and nonzero Plucker coordinates force a generic projected permanent to have finite projective stabilizer whenever4<=q<m². Quotient fibers then give only an upper dimension bound, which suffices. The complete eventual nonrectangular classification reaches2m rows; on/below-face comparison extends to r<=min(2n−2,m²). Generic finite stabilizers are never identified with closed or stable orbits.\n\nI44 classifies every minimal singular anchor into a three-weight torus chain. A quadratic residue condition then proves one-pole rank preservation through five full-rank cores. Combined with the sharp reset criterion, this resolves all weights≤4 in every characteristic and≤5 outside characteristic2, and hence all multilinear width-three inputs on≤12 variables or≤13 outside characteristic2. General growing-width sampling and characteristic2 weight5 remain open.\n''')
print(now)
