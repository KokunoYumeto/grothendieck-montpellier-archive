"""Integrate the fully checked R29/G25 row extension and I41 weight-two theorem."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json
R=Path(__file__).resolve().parent;W=R.parent;OUT=W.parent/'deliverables'
guard=R/'integration_20_check_events.tsv';assert not guard.exists()
now=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'
assert 'R-29: prescribed' in (W/'rectangular/findings.tex').read_text()
assert 'I-41. Weight-two' in (W/'isolation/findings.tex').read_text()
p=R/'findings.tex';s=p.read_text();assert '[G-25:' not in s
p.write_text(s+'\n\n'+(R/'g25_fragment.tex').read_text())

p=R/'grothendieck.tex';s=p.read_text();marker='\\subsection{What the manuscript record does and does not establish}'
s=s.replace('character spaces,+so','character spaces, so')
addition=r'''
\paragraph{R-29 and G-25. Two-product families and enlarged stable quotient schemes.}
Work over $\mathbb C$ with a rank-$r$ vector space split as two
summands of ranks at most $m-1$. The ordered linear-factor tensors,
their symmetric products, and the auxiliary Cartan flag cone are
formed by the tensor and Schur operations of D-S6. Minimum
cocharacter weights are preserved under multiplication in the
symmetric algebra. Kempf--Ness and unitary transitivity on the
complex partial flag variety give a product section with any
prescribed positive rational moment spectrum in each summand.
This analytic normalization is an existence argument on the
complex fiber; it does not assert an integral section or an
effective arithmetic change of basis.

The orthogonal sum of the two product sections has the required
moment spectrum. The Lie-stabilizer equations split by bidegree:
mixed blocks vanish by independence of directional derivatives,
and diagonal blocks are scalar. The affine scheme parametrizing
two products and a padding line contains the stable open, the
irreducible-form open, and the finite-projective-stabilizer open.
Their nonempty intersection and avoidance of finitely many fixed
line loci give a common stable section with only the central
projective stabilizer. Its central character is $r\nu_r$ and
is trivial on $\mu_r$. These are group-scheme and character-lattice
statements in D-S3 on the characteristic-zero fiber; proper
projective multiplication images use D-Proper.

The degree-$j$ Cartan coefficient algebra still extracts precisely
the label $j\nu$. Hence the projective invariant schemes have
the same dimensions $u,v$ as G-23 for $r\le2m-2$. G-25 checks
the only changed dimension lower bounds and carries across the
same standard Veronese, positive Hilbert leading terms and
gcd-one degree semigroup. The exact difference is unchanged.
For the new positive family $r=n=m+1$ it equals one, and the
label is $(3j,(2j)^{m-1},j)$ in degree $2j$.
D-FGA and EGA~II, 2.5.2, place these graded algebras and their
projectivizations. This comparison of actual invariant Hilbert
functions is stronger than exhibiting one equation copy, but
does not provide a general positive formula for individual
finite-degree multiplicities.

\paragraph{I-41. Saturated determinant weights, divided squares, and pole-rank charts.}
On the fixed-rank coefficient charts of I-40, a width-three run
of two invertible cores exhausts the determinant-character budget
at weight two. The bounding determinant lines have character zero
and are fixed by the whole split $\mathrm{SL}_2$. Their decomposable
exterior tensors determine invariant rank-three support bundles.
Single-coordinate contractions give neighboring invariant
rank-two bundles. Torus character parity and the Weyl involution
force weights $1,-1$: larger opposite weights would leave no
odd-rank invariant subbundle in their tensor product with the
standard bundle. This uses the integral character lattice of
SGA~3, I~4.7.3, rather than reduction of weights modulo the
residue characteristic.

The invariant rank-three subbundle in $V\otimes V$ is explicitly
spanned by $e_0e_0$, $e_0e_1+e_1e_0$, and $e_1e_1$.
It is the divided-square tensor submodule in every characteristic.
The proof retains its actual dual coefficient pairing; it neither
identifies it with its dual in characteristic two nor assumes
semisimplicity. Determinant and tensor operations use D-S6,
and the support charts use D-FGA. The character shifts make
the two middle affine maps upper unitriangular in compatible
weight bases. Their two-dimensional connector determinant has
the nonzero square coefficient $d_2d_3$.

Over the node scheme with all node differences inverted, the
one-pole rational evaluation is regular after also inverting
the node-pole differences. The unique double pole of that square
term proves nonvanishing of each saturated connector. Compound
rank-one factorization then preserves every required interval
rank. On the resulting compatible charts the second-coefficient
matrix has bandwidth three and annihilates the three sections
$1,h,h^2$. Their three-column Vandermonde determinants are units,
so the row induction and passive-path argument force the
contradiction in every characteristic. Translation and reversal
are root-group operations; their leading limits stay in the
closed determinantal width locus. They reduce the ten-variable
degrees to the weight-two and weight-zero cases. The balanced
finite interpolation grid is the same regular-open construction
as in I-40, with all field-size and extension conventions retained.

'''
assert marker in s;p.write_text(s.replace(marker,addition+marker))

p=R/'intro.tex';s=p.read_text()
s=s.replace('For $m\\ge17$ and $4\\le r\\le m$, G-23 consequently proves','For $m\\ge17$ and $4\\le r\\le2m-2$, G-23 and its R-29/G-25 extension consequently prove')
s=s.replace('Nonrectangular boundary faces and individual finite degrees retain their separate scope.','For the added rows $r>m$, the only positive parameter case is $r=n=m+1$: the explicit direction $(3,2^{m-1},1)$ has ratio $\\kappa j(1+O(j^{-1}))$ in degree $2j$. Nonrectangular boundary faces and individual finite degrees retain their separate scope.',1)
s=s.replace('The ordinary unweighted centered map is not identified with that balanced map for every nine-variable polynomial.','I-41 uses the saturated weight-two support spaces and their actual divided-square dual pairing to preserve the four-coordinate connectors. Its bandwidth-three argument closes the balanced theorem through ten variables, with the same finite grid. The ordinary unweighted centered map is not identified with that balanced map for every ten-variable polynomial.')
p.write_text(s)

p=R/'open_gates.tex';s=p.read_text()
s=s.replace('G-22, R-28 and G-23 now determine the eventual sign in every strict direction with $4\\le r\\le m$','G-22, R-28/R-29 and G-23/G-25 now determine the eventual sign in every strict direction with $4\\le r\\le2m-2$')
s=s.replace('More than $m$ rows, the nonrectangular','More than $2m-2$ rows, the nonrectangular')
s=s.replace('The next balanced small case is a translation-invariant ten-variable quartic of weight two.','I-41 closes the weight-two class and the complete balanced problem through ten variables by a nonzero connector square coefficient and a bandwidth-three argument. The next unrestricted balanced small case has eleven variables.')
start=s.index('\\subsection{Updated gates after the higher-row')
s=s[:start]+r'''\subsection{Updated gates after the two-product and weight-two refinements}
R-27 closes the uniform quaternary dimension and specified Tor gate.
R-29 and G-25 extend the exact strict-direction sign to
$4\le r\le2m-2$, with all G-23 constants retained. Among the
additional rows $r>m$, only $r=n=m+1$ has positive eventual sign,
with exponent one and the explicit degree-two direction
$(3,2^{m-1},1)$. G-24 retains its complete eventual rectangular
comparison through $m$ rows. More rows, nonrectangular equality
faces, finite-degree extraction and changing directions remain open.

P-17, I-40 and I-41 close the complete balanced two-pair width-three
question through ten variables. I-41 also covers every homogeneous
translation-invariant width-three tensor with $0\le n-2D\le2$.
At weight three, longer runs need not have the same bounding
invariant support spaces, and three tangent directions do not
alone kill bandwidth four. The unrestricted eleven-variable case,
general mixed words, nonlinear singular factors and uniform
polynomial dependence on growing width remain separate gates.
'''
p.write_text(s)

p=W/'assemble.py';s=p.read_text()
s=s.replace('extend the exact eventual sign to every strict direction through $m$ rows','extend the exact eventual sign to every strict direction through $2m-2$ rows')
s=s.replace('complete balanced two-pair width-three result through nine variables','complete balanced two-pair width-three result through ten variables')
p.write_text(s)

p=R/'questions.tsv'
with p.open(newline='') as f:rr=csv.DictReader(f,delimiter='\t');fields=rr.fieldnames;rows=list(rr)
for row in rows:
 if row['id']=='G-Q26': row['state']+=' R29 extends common stable no-scaling points to4<=r<=2m-2 by prescribed product spectra and an orthogonal two-product family.'
 if row['id']=='G-Q27':
  row['question']='What is the exact eventual multiplicity sign for strict directions through2m-2 rows?'
  row['source_and_locator']='G23/G25; R28/R29; G21'
  row['state']='PROVED G23/G25 for m>=17,4<=r<=2m-2: both multiplicities positive for every j>=beta², ratio kappa*j^[r m²−(r−2)n²−2m+r−1], exponent neverzero, exact floor boundary and explicit every-integer thresholds for both signs. Nonrectangular first-row equality faces, more rows, and finite earlier degrees remain separate.'
rows.append(dict(zip(fields,['G-Q29','R29 two-product family; G25 exact dimension exponent','Does extending beyondm rows give a new explicit genuinely padded positive multiplicity family?','PROVED G25: within m<r<=2m-2 the only positive parameter case is r=n=m+1. For everym>=17, s2 andnu=(3,2^(m−1),1) give ratio kappa*j and a positive gap at all sufficiently large degrees2j. All other new-row integer cases have eventual determinant dominance.'])))
with p.open('w',newline='') as f:ww=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n');ww.writeheader();ww.writerows(rows)

events=[
 ('R-29','targeted proof check','PASS complete root proof reading and rederivation; see independent_review_R29_root.md. Prescribed moments, reverse KN, partial-flag normalization, both mixed bidegrees, stabilizer, common opens, no scalar period and scope all checked.'),
 ('I-41','targeted proof check','PASS complete root proof reading and rederivation; see independent_review_I41_root.md. Actual divided-square dual pairing, constant gauges, determinant formula, pole rank, every endpoint, bandwidth-three and full n10 degree closure checked in every characteristic. Only dim TeX typo changed after reading.'),
 ('G-25','targeted proof check','PASS complete root derivation and whole-proof reading: all dependencies in the enlarged row range, replacement u/v lower bounds, unchanged action and parameter degrees and all constants, all-integer semigroup comparison, unique positive new parameter case and partition size/strictness. Independent rectangular whole read PASS separately recorded.'),
 ('G-B14','used and rechecked in this run','Losev Theorem4 p1, the full closed-orbit iff moment-zero criterion, used in both directions for R29; finite projective stabilizer is established separately. No product-moment additivity is inferred.'),
 ('I-B09','used and rechecked in this run','The all-characteristic dominant-character fact from Jantzen LectureI pp2–3 is used for factor weights in I41; zero-weight invariance and the standard two-dimensional module are additionally proved directly in I41.'),
]
with guard.open('w',newline='') as f:
 ww=csv.writer(f,delimiter='\t',lineterminator='\n');ww.writerow(['statement_id','date','who','type','outcome'])
 for ident,kind,outcome in events:ww.writerow([ident,now,who,kind,outcome])
hashes={rel:hashlib.sha256((W/rel).read_bytes()).hexdigest() for rel in ['rectangular/r29_fragment.tex','isolation/I41_weight_two_connectors.tex','root/g25_fragment.tex']}
(R/'integration_20_review_hashes.json').write_text(json.dumps({'checked_utc':now,'who':who,'status':'PASS complete proof readings','hashes':hashes},indent=2)+'\n')
with (OUT/'LEDGER.md').open('a') as f:
 f.write('\n\n## '+now+' — two-product stable directions and the weight-two connector\n\nR29 and G25 pass all complete proof readings and extend the exact strict-direction comparison through2m−2 rows. The new positive family r=n=m+1 has exponent1 and explicit nu=(3,2^(m−1),1). I41 passes author/root/purity complete readings and closes the balanced two-pair theorem through ten variables, plus all translation-invariant homogeneous weight≤2 inputs. These subclass isolation results are not counted as a general growing-width solution. Review3 already occurred at05:49:46UTC with movementYES and count0; the next actual review is06:49:46UTC.\n')
with (OUT/'IMPLICATIONS.md').open('a') as f:
 f.write('''\n\n### Strict directions through2m−2 rows and a degree-two direction with exponent one\n\nR29 supplies the common stable and projectively free point through2m−2 rows, using a prescribed-spectrum product lemma and an orthogonal sum of two products. G25 extends every exact sign and explicit constant of G23. Among the added rowsr>m, positive eventual gaps occur precisely atr=n=m+1. The partitionnu=(3,2^(m−1),1) withs2 is an explicit such direction for everym>=17; its ratio is asymptotic tokappa*j in degree2j. This is a comparison of total multiplicities. It does not assert every earlier degree or a superlinear-padding lower bound. G24 retains its exact eventual rectangular range throughm rows.\n\nI41 closes the homogeneous common-translation-invariant weight-two width-three case and then all balanced two-pair width-three inputs through ten variables, in every characteristic and unknown order. Its new connector has a nonzero square coefficient that survives one-pole evaluation; the three tangent directions kill the resulting bandwidth-three Hessian. The finite balanced grid remains(n+1)² binom(D+3,3). Arbitrary center slopes and ordinary unweighted centeredSV2 are not promoted to this entire class. The general growing-width polynomial sampler remains open.\n''')
print(now)
