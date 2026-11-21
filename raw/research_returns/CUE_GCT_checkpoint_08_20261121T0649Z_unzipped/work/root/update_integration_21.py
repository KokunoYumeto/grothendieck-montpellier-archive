"""Integrate the checked endpoint, full boundary, and two isolation refinements."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json
R=Path(__file__).resolve().parent;W=R.parent;OUT=W.parent/'deliverables'
guard=R/'integration_21_check_events.tsv';assert not guard.exists()
now=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro; /root; effort not exposed; CUE_GCT_20261121_R1'
for rel,needle in [('rectangular/findings.tex','R-30: tilted'),('isolation/findings.tex','I-42.'),('purity/findings.tex','P-18.')]:assert needle in (W/rel).read_text()
p=R/'findings.tex';s=p.read_text();assert '[G-26:' not in s
p.write_text(s+'\n\n'+(R/'g25_endpoint_addendum.tex').read_text()+'\n\n'+(R/'g26_fragment.tex').read_text())

p=R/'grothendieck.tex';s=p.read_text();marker='\\subsection{What the manuscript record does and does not establish}'
addition=r'''
\paragraph{R-30 and the G-25 endpoint extension. Compact forms and auxiliary flags.}
At a block of rank $m$, the nonconstant torus character defines
a nontrivial partial flag. Its stabilizer intersects the Fourier
basis torus only in scalars: the corresponding circulant matrix
cannot preserve a proper consecutive coordinate subspace unless
every nonconstant cyclic coefficient vanishes. This produces a
stable ordered tensor even though its polynomial product alone
has a positive-dimensional complex stabilizer. After normalization,
the product has only a finite compact projective stabilizer.
The tilted padding line subtracts a positive rank-one Hermitian
operator from the desired moment matrix, with two explicitly
chosen rational positive eigenvalues. Both product blocks then
have nonconstant spectrum.

The full ordered padded tensor is the point at which the moment
vanishes. Losev's real-form stabilizer calculation applies there
and makes its complex stabilizer finite. The two-product parameter
scheme also has a nonempty open with finite padded-form stabilizer.
A generic section of the nontrivial partial flag orbit avoids
every fixed locus of that finite projective group. The resulting
enhanced point has no scalar period. This is a characteristic-zero
stable-quotient construction using D-S3 group stabilizers and
cocharacters, D-S6 tensor/Schur operations and D-FGA flag and
coordinate schemes; the Hermitian normalization is not transported
as an integral arithmetic algorithm. The exact G-25 quotient
comparison consequently extends to $r\le2m$ with unchanged
explicit constants.

\paragraph{G-26. A Pieri face of the bidegree pullback.}
The padding parameter morphism pulls a degree-$d$ coordinate
section back to bidegree $(ad,d)$ on the line and the permanent
cone. Its injectivity comes from dense image. In the representation
Grothendieck group its Schur components are governed by
$[\operatorname{Sym}^{ad}V^*]\,[S_\alpha V^*]$ and the
Pieri identity. The direct-sum multiplicity comparison is taken
over $\mathbb C$, where these representations are semisimple;
no integral direct-sum decomposition is inferred from a $K_0$
identity. When $\lambda_1=ad$, the horizontal strip must use
every column, so the unique surviving label is the tail of
$\lambda$. The zero-last-character coefficient subalgebra
identifies that tail multiplicity in one fewer variable.
These tensor and Schur identities belong to D-S6, with the exact
Pieri source locator retained in G-B20.

Two different enhanced invariant schemes now provide the
comparison: the determinant scheme in $r$ variables and the
tail permanent scheme in $r-1$ variables, or its full ternary
ambient bound at $r=4$. Their separate stable points have trivial
scalar period. Deleting the first flag part removes a nonnegative
number of strict weight comparisons, and the exact quotient
dimensions satisfy $u>v$ throughout the equality face with
$4\le r\le m$. The standard Veronese and the two separate
degree semigroups give strict comparison in every sufficiently
large original degree. D-FGA and EGA~II, 2.5.2, locate these
graded coordinate algebras and projectivizations. The argument
uses an injection and an upper bound, not a surjective lifting
of lower-dimensional sections to padded forms.

\paragraph{P-18. Three block characters and adjacent contraction degrees.}
The blockwise homogeneous coefficient tensor is graded by
three independent split tori. The three summands of its common
translation derivative have different block characters, hence
each is zero in every residue characteristic. At an extreme
block cut, the last-variable coefficient and the constant-prefix
coefficient occupy different degree blocks; their ranks add.
This forces two-dimensional extreme support bundles. The
prime rational-evaluation kernel makes every nonzero middle
coefficient map between those bundles invertible, and an
interior cut has two disjoint rank-two blocks. It cannot lie
in the width-three determinantal locus.

For a smallest unrestricted cubic, the exterior decoder of P-17
lives in $\bigwedge^3K$ over the node scheme. Decomposition by
left exterior degree makes the three contraction operators
connect only adjacent degree blocks. A zero block therefore
separates a smaller kernel element. Minimality and the P-17
rank lemma leave only adjacent occupied degrees at every
prefix; the ordered support is consequently trilinear on
three intervals with at most two shared boundary variables.
The degree-three interpolation grid has $20(n+1)^2$ points.
This dictionary uses the torus characters in D-S3, exterior
operations in D-S6 and determinantal charts in D-FGA. It neither
changes the variable order by a general linear coordinate map
nor asserts that setting a shared boundary variable to zero
preserves the balanced ideal.

\paragraph{I-42. Rank-one reset blocks and the special fiber at two.}
On the compatible rank charts of I-41, the mixed second
coefficients factor as $a_i b_j$ inside each reset block and
vanish across a strict internal reset. These are polynomial
rank-one equations; they retain more information than a
bandwidth condition alone. The three tangent sections
$1,h,h^2$ give a split rank-three evaluation map on any three
distinct nodes. The first nonzero row and the first future
nonzero coefficient reduce a hypothetical relation to at most
three Vandermonde columns when the reset distance is at most
five. At distance six the remaining relation yields exactly
the factor $2a_kb_\ell$. This also vanishes only trivially on
the open base where two is invertible.

The characteristic-two fiber is genuinely different: two
four-column kernels overlapping in one node give the sharp
seven-node abstract counterexample. Disjoint four-column
kernels give the eight-node example in every characteristic.
Neither is asserted to be the jet of an actual annihilating
ROABP. Use mixed coefficients, rather than division by two,
for this second-order statement. The fixed-rank and kernel
schemes belong to D-FGA, while the split characters and
divided-square anchors of saturated runs use D-S3 and D-S6
as in I-40/I-41. A saturated run exhausts the determinant
character budget, so the same anchor square coefficient
preserves its one-pole rank regardless of its length. The
sharp reset bounds then prove the stated irreducible classes
at weights three and four, and weight five away from two;
shorter nonsaturated runs retain their explicit rank gate.

'''
assert marker in s;p.write_text(s.replace(marker,addition+marker))

p=R/'intro.tex';s=p.read_text()
s=s.replace('$4\\le r\\le2m-2$','$4\\le r\\le2m$')
s=s.replace('Nonrectangular boundary faces and individual finite degrees retain their separate scope.','G-26 additionally settles every nonrectangular first-row equality face through $m$ rows: Pieri bounds its multiplicity by the tail partition in one fewer variable, and the determinant eventually dominates. Below that face the padded multiplicity is zero. Thus every fixed direction through $m$ rows is classified eventually; boundary faces beyond $m$ rows and individual finite degrees retain their separate scope.',1)
s=s.replace('The precise conditional matrix-invariant consequence remains I-08.','P-18 proves an arbitrary-length trilinear three-block class with $20(n+1)^2$ balanced samples and reduces the unrestricted cubic problem to at most two shared boundary variables. I-42 uses the actual rank-one reset structure to remove the Hessian step through four invertible factors in every characteristic, and five outside characteristic two; it supplies positive saturated-run classes with explicit remaining rank gates. The precise conditional matrix-invariant consequence remains I-08.',1)
p.write_text(s)

p=R/'open_gates.tex';s=p.read_text()
s=s.replace('$4\\le r\\le2m-2$','$4\\le r\\le2m$')
s=s.replace('More than $2m-2$ rows, the nonrectangular first-row boundary face in higher rank','More than $2m$ rows, the nonrectangular first-row boundary face beyond $m$ rows')
start=s.index('\\subsection{Updated gates after the two-product')
s=s[:start]+r'''\subsection{Updated gates after the complete boundary comparison}
R-27 closes the uniform quaternary dimension and specified Tor gate.
R-29/R-30 and G-25 extend the exact strict-direction sign through
$2m$ rows. G-26 closes every first-row equality face through
$m$ rows, with an all-degree Pieri upper bound and an explicit
eventual determinant-dominance threshold. Every fixed full-row
direction with $4\le r\le m$ is therefore classified: a positive
eventual gap requires both the strict padding inequality and
the positive G-23 dimension exponent. Boundary faces with more
than $m$ rows, strict directions beyond $2m$ rows, changing
directions and efficient finite-degree extraction remain open.

P-17, I-40 and I-41 close the complete balanced two-pair
width-three problem through ten variables. P-18 additionally
covers an arbitrary-length trilinear class and reduces a smallest
unrestricted cubic counterexample to at most two shared boundary
variables. I-42 proves that once ranks and endpoints survive,
the actual reset-Hessian structure is sufficient through four
invertible factors in all characteristics, and five away from
characteristic two. Saturated runs preserve their ranks and give
the stated higher-weight irreducible classes. At weight three
the remaining run-length gate is two, without a saturated
determinant budget. The unrestricted eleven-variable case,
nonlinear singular factors, shared-seed synchronization and
uniform polynomial dependence on growing width remain open.
'''
p.write_text(s)

p=W/'assemble.py';s=p.read_text()
s=s.replace('through $2m-2$ rows','through $2m$ rows')
s=s.replace('A lower-variable boundary comparison completes the exact eventual rectangular range through $m$ rows.','A Pieri tail bound and lower-variable boundary comparison classify every fixed direction through $m$ rows eventually, including the full first-row equality face.')
s=s.replace("    manuscript = ''.join(parts)\n", "    manuscript = ''.join(parts)\n    manuscript = manuscript.replace('\\n\\\\part{', '\\n\\\\clearpage\\\\part{')\n")
p.write_text(s)

p=R/'questions.tsv'
with p.open(newline='') as f:rr=csv.DictReader(f,delimiter='\t');fields=rr.fieldnames;rows=list(rr)
for row in rows:
 if row['id']=='G-Q26':row['state']+=' R30 closes the2m−1 and2m endpoints by tilted padding, compact stabilizers at moment zero, and generic auxiliary flags.'
 if row['id']=='G-Q27':
  row['question']='What is the exact eventual multiplicity sign for strict directions through2m rows?'
  row['source_and_locator']='G23/G25 including endpoint corollary; R28–R30; G21'
  row['state']='PROVED G23/G25 for m>=17,4<=r<=2m: both multiplicities positive for every j>=beta²; ratio exponent r m²−(r−2)n²−2m+r−1 neverzero; exact floor boundary and explicit every-integer thresholds. G26 separately closes first-row equality faces throughm rows. Larger-row boundary faces and individual earlier degrees remain separate.'
 if row['id']=='G-Q29':row['state']=row['state'].replace('m<r<=2m-2','m<r<=2m')
rows.append(dict(zip(fields,['G-Q30','G26; supplied Bump–Gamburd section2.1 equatione:pieri; G21–G25','Can every nonrectangular first-row padding-boundary direction throughm rows be compared eventually?','PROVED G26: all-degree padded multiplicity<=tail permanent multiplicity whenlambda1=ad, and zero below. For m>=17,4<=r<=m separate free stable quotients have u>v; explicit every-integer stretch bound gives determinant dominance on the equality face. Combined withG23, every fixed full-row direction in this range has an exact eventual sign.'])))
with p.open('w',newline='') as f:ww=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n');ww.writeheader();ww.writerows(rows)

p=R/'sources.md';s=p.read_text()
s+='''\n\n## G-B20 — Pieri on the first-row padding face\n\nBump, D., & Gamburd, A. (2006). On the averages of characteristic polynomials from classical groups. *Communications in Mathematical Physics, 265*, 227–274. https://doi.org/10.1007/s00220-006-1503-1\n\nExact inspected locator: supplied source acp20.tex, section2.1, equation label e:pieri, lines404–422, together with the horizontal-strip definition immediately before it. The source cites Macdonald equationI(5.16),p73 and Bump Theorem42.4; those two books were not independently reopened for this result. Root and isolation read the supplied primary statement. G26 uses the known Pieri rule, then proves its unique-tail consequence and the actual-coordinate-ring injection. No generic ambient-plethysm equality is asserted.\n\n### G-B14 additional stabilizer locator for R30\n\nLosev2006, proof of Theorem1, printedp2, equations(3)–(4) and the following sentence: at a moment-zero vector, the compact stabilizer Lie algebra is a real form of the complex stabilizer Lie algebra. Root freshly read the complete Theorem4 proof and this Theorem1 proof on the primary PDF. The real-form conclusion is applied only at the balanced full tensor inR30, never at an unbalanced block product.\n'''
p.write_text(s)

events=[
 ('R-30','targeted proof check','PASS complete root proof reading; independent_review_R30_root.md. Finala5f8e scope and full proof checked; primary Losev Theorem1 proof and Theorem4 reread.'),
 ('P-18','targeted proof check','PASS complete root proof reading; independent_review_P18_root.md. All-characteristic trilinear contradiction, minimal cubic contraction separation, exact two-boundary gate and finite grid.'),
 ('I-42','targeted proof check','PASS complete root proof reading and final clarification check; independent_review_I42_root.md. Sharp all-characteristic/away-from-two reset thresholds, abstract examples, endpoint shears and actual saturated-run consequence.'),
 ('G-25','targeted proof check','PASS complete endpoint addendum proof: R30 supplies the two endpoint hypotheses; explicit u/v lower bounds valid throughr2m; every constant and unique new-row positive case remain unchanged.'),
 ('G-26','targeted proof check','PASS complete root derivation and whole-proof reading: bidegree injection, unique Pieri tail, actual ring inheritance, two separate stable no-scaling points, ternary ambient surjection, exact dimensions and flag difference, common beta/E/p bounds and strict every-residue threshold. Independent isolation and rectangular full readings PASS.'),
 ('G-B20','used and rechecked in this run','Read supplied Bump–Gamburd section2.1 e:pieri and the preceding horizontal-strip definition in full; exact source scope and second-hand book locators recorded.'),
 ('G-B14','used and rechecked in this run','Fresh primary read of Losev Theorem4 proof and Theorem1 proof through equations3–4 onp2, including the real-form stabilizer conclusion; used at moment zero inR30.'),
]
with guard.open('w',newline='') as f:
 ww=csv.writer(f,delimiter='\t',lineterminator='\n');ww.writerow(['statement_id','date','who','type','outcome'])
 for ident,kind,outcome in events:ww.writerow([ident,now,who,kind,outcome])
rels=['rectangular/r30_fragment.tex','purity/P18_ordered_cubic_gate.tex','isolation/I42_reset_hessians.tex','root/g25_endpoint_addendum.tex','root/g26_fragment.tex']
(R/'integration_21_review_hashes.json').write_text(json.dumps({'checked_utc':now,'who':who,'status':'PASS complete proof readings','hashes':{rel:hashlib.sha256((W/rel).read_bytes()).hexdigest() for rel in rels}},indent=2)+'\n')
with (OUT/'LEDGER.md').open('a') as f:
 f.write('\n\n## '+now+' — complete fixed-direction boundary comparison and further rank structure\n\nR30 extends stable no-scaling witnesses through2m rows. G25 carries every strict-direction constant to those endpoints. G26 closes the entire first-row equality face throughm rows, not only rectangles, by an all-degree Pieri-tail bound and strict lower-variable Hilbert comparison. P18 supplies the arbitrary-length trilinear class and exact two-shared-variable cubic gate. I42 proves sharp reset-Hessian bounds and positive saturated-run classes; the general growing-width gate remains open. All complete proof readings are recorded. The next actual movement review remains06:49:46UTC.\n')
with (OUT/'IMPLICATIONS.md').open('a') as f:
 f.write('''\n\n### Every fixed direction throughm rows has an eventual classification\n\nG26 proves that on the equality face lambda1=ad, a padded multiplicity is at most the permanent multiplicity of the tail partition in one fewer variable. Below that face it vanishes. For n>m>=17 and4<=r<=m, the lower enhanced quotient has strictly smaller dimension than the determinant quotient, and separate no-scaling points give an explicit threshold valid at every integer stretch. Thus eventual positive gaps in every fixed full-row direction occur exactly when the padding inequality is strict and the G23 integer dimension exponent is positive. This closes nonrectangular equality faces in this range as well as rectangles. R30 and the G25 endpoint addendum extend the strict-direction classification through2m rows. They do not settle larger-row boundary faces, changing directions or the superlinear-padding complexity separation.\n\nP18 gives20(n+1)² balanced samples for an arbitrary-length trilinear three-block width-three class; a smallest unrestricted cubic counterexample has at most two shared boundary variables. I42 shows that the actual rank-one reset structure removes the Hessian obstruction through four invertible cores in all characteristics and five outside characteristic2. Its seven-/eight-node abstract examples show these thresholds are exact for that algebraic criterion; they are not polynomial annihilator counterexamples. Saturated determinant budgets supply the rank-preservation hypothesis for the stated irreducible higher-weight classes. The next weight-three gate is a shorter nonsaturated two-core connector.\n''')
print(now)
