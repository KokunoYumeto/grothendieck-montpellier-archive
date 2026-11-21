"""Integrate G19 and the independently checked R24/R25/I35 dictionaries."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json

R = Path(__file__).resolve().parent
W = R.parent
OUT = W.parent/'deliverables'
now = datetime.now(timezone.utc).isoformat()
who = 'GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'
guard = R/'integration_12_check_events.tsv'
assert not guard.exists(), 'Integration12 has already run.'

p=R/'findings.tex'
s=p.read_text()
assert 'G-19: an explicit rectangular discriminant' not in s
p.write_text(s+'\n\\subsection{A specified rectangular discriminant copy}\n\n'+(R/'g19_fragment.tex').read_text())

p=R/'grothendieck.tex';s=p.read_text()
marker='\\paragraph{D-FGA: images, quotients, and projective parameter spaces.}'
assert marker in s
s=s.replace(marker, r'''\paragraph{D-Proper: closed images of projective incidence schemes.}
EGA~II, Definition~5.4.1, printed p.~100, defines properness
using separated finite type and universal closedness.
Theorem~5.5.3(i), printed p.~104, states that a projective
morphism is proper. The corresponding French primary-text
passages, including the displayed statements and the proof
following the latter, were read through the indexed original
PDF text. The complete PDF did not load in the web reader.
These locators justify the closed incidence images below;
they do not supply a computational bound for their equations.

'''+marker)
marker='\\subsection{What the manuscript record does and does not establish}'
assert marker in s
dictionary=r'''
\paragraph{R-24. The first zero of the graded derived-intersection defect.}
The specified integer Jacobian minor is a section of an exterior
power of the permanent coefficient-map differential. Its nonzero
residue modulo $101$ proves that its principal open locus has
nonempty characteristic-zero fiber. On that locus the image
dimension is $1124$, the exact D-S3 torus quotient bound.
R-23 then identifies $\epsilon_{17}=0$ as vanishing of the
indicated degree of the D-Tor first homology. This is one
explicit generic-fiber result; no complete Tor independence
or assertion in every residue characteristic follows. The
padded coefficient image and resulting highest weights use
the D-FGA and D-S6 dictionaries already proved in G-17--G-18.

\paragraph{R-25. A single family, canceled tangent sections, and induction.}
The bordered matrix is a morphism from an affine parameter scheme
times $\mathbb A^1_\varepsilon$ to the space of forms. Two
coordinated parameter variations cancel their order-one terms
exactly; division by $\varepsilon^3$ on the punctured parameter
line gives fixed Hessian sections in the same differential image.
Their restrictions to the hyperplane $\ell=0$ are the stated
ternary coefficient columns. The intersection of two nonempty
rank opens in the irreducible parameter space permits one matrix
with both required properties. A single minor with nonzero
constant term proves the dimension increment. This transports
the proof to D-FGA rank loci and tangent maps; it does not infer
rank from an alternating $K_0$ class. The finite integer minor
certifies the antecedent at $m=17$ and hence $c_{18}=1262$.
The uniform nonemptiness of those rank opens for all larger
sizes remains the specific geometric question.

\paragraph{I-35. Base loci on a Segre scheme and the seed diagonal.}
The two boundary vectors define a point of
$\mathbb P^{r-1}\times\mathbb P^{r-1}$, embedded as rank-one
functionals. Equality of their annihilator intersections is
equality of base loci of two linear systems on this Segre
scheme. The incidence dimension argument and D-Proper give
an existential subspace with the same base locus and at most
$2r-1$ generators. It need not be realized by an explicit
substitution on the original variables. For the generic matrix,
the Hankel curve realizes such a linear system, although the
matrix value has rank one. This is the known optimal test-space
dimension cited in P-B16, with the new bridge deduction stated
separately.

Independent seed sets give a product of parameter schemes.
At each replacement the other parameters belong to the
coefficient function field, so the extension-field contraction
hypothesis applies. Identifying those parameters afterward is
pullback along a diagonal; a nonzero section can become zero
under that pullback, as the explicit examples prove. Thus
base change of the coefficient field is distinct from seed
identification. Finally the multiplicative lift sends the
rank-$r$ idempotent corner into a one-dimensional endomorphism
corner; its fixed entry readout would have to be a multiplicative
character, contradicted by the two unipotent matrices. D-S3
places these actions, D-S6 places their exterior powers, and
D-FGA places their coefficient-image modules. No new purity
or representation-rank conclusion is inserted by this language.

\paragraph{G-19. A discriminant line and a specified Schur submodule.}
Over the integer coefficient scheme, the homogeneous form and
its partial derivatives define a closed incidence scheme with
projective point coordinates. Its projection is closed by
D-Proper. On the characteristic-zero fiber its reduced
discriminant equation is a section of coefficient degree
$D=k(m-1)^{k-1}$ and variable-change determinant weight
$\delta=m(m-1)^{k-1}$. Benoist's exact degree theorem and
primitive integer construction supply this line; D-S3 records
its character. The highest-weight inclusion into the plethysm
generates one $S_{(\delta^k)}V$ over $\mathbb C$, in the D-S6
Schur-functor language. Its restriction map to one orbit
coordinate ring is zero and to the other injective. This is
a statement about a specified submodule of the coefficient
algebra, not the rank of its entire isotypic multiplicity space.

The Haar identity is its compact complex realization; Gaussian
orthogonality is a positive norm of its integer pullback
coefficients. Neither norm is asserted to arise from a pure
arithmetic sheaf or motive. The explicit cubic Macaulay minor
defines an open localization where the graded Jacobian map
is onto, so the projective gradient-zero scheme is empty.
Its nonzero residue certifies the characteristic-zero smooth
fiber and hence the displayed discriminant nonvanishing.
Positive padding factors the section and forces a singular
intersection, so the discriminant pullback becomes zero.
This same geometric argument proves the stated limitation.
The row-minimality at size three is the D-S3 highest-weight
subalgebra argument applied to the dense D-FGA four-variable
determinant image. Cote~133, scan~028, supplies the Schur
operation viewpoint; scan~019's rank-versus-character warning
remains essential for the specified-copy distinction.

'''
p.write_text(s.replace(marker,dictionary+marker))

p=R/'sources.md';s=p.read_text()
s=s.replace('The original large PDF did not load in the web tool.',
'''The original large PDF did not load in the web tool. For G19 and I35, the indexed French original passages for Definition5.4.1, printedp100, and Theorem5.5.3(i), printedp104, including the latter's displayed proof, were read at https://geotoppos.org/divers/ega2.pdf . They give universal closedness and projective implies proper. A direct temporary download failed with HTTP403; no complete original-PDF reading is claimed.''')
s=s.replace('The padding-line and effective semigroup arguments are proved in G18 itself.',
'''The padding-line and effective semigroup arguments are proved in G18 itself.''')
needle='the padding-line and effective semigroup arguments are proved in G18 itself.'
assert needle in s
s=s.replace(needle,needle+' For G19, Definition5.20 and Corollary5.21, printedp170, and the character discussion in Proposition5.19, printedp168, were reopened and checked.')
s+='''

## G-B18 — Singular linear determinant sections

Alper, J., Bogart, T., & Velasco, M. (2017). A lower bound for the determinantal complexity of a hypersurface. *Foundations of Computational Mathematics, 17*(3), 829–836. https://doi.org/10.1007/s10208-015-9300-x

Primary author version: https://sites.math.washington.edu/~jarod/papers/determinantal-complexity.pdf . Exact locator used: Theorem1.7, printedp3, and its complete proof, printedp5. It states the characteristic-zero codimension bound for every linear determinant restriction and the generic equality; in at least five variables the corresponding projective hypersurface is always singular. G19 uses this known theorem, together with the permanent singular-locus bounds already cited as R-B17. The associated smooth-section and specified-module deduction is proved in G19. The published metadata and DOI were corroborated by the author-institution publication record. No latest or strongest determinantal-complexity claim is made.

## G-B19 — Degree and integral normalization of the discriminant

Benoist, O. (2012). Degrés d’homogénéité de l’ensemble des intersections complètes singulières. *Annales de l’Institut Fourier, 62*(3), 1189–1214. https://doi.org/10.5802/aif.2720

Primary author PDF: https://www.math.ens.psl.eu/~benoist/articles/degreic.pdf . Exact locators: Theorem1.3, equations(1.4)–(1.6), printedpp1190–1191, for coefficient and variable-change degrees; Theorem1.7, p1191, for the primitive integer equation and its characteristic-dependent reductions; Example1.8, p1192, for the hypersurface specialization. The coefficient degree is k(m−1)^(k−1), and the determinant character exponent is m(m−1)^(k−1). The second displayed formula in Example1.8 omits the factor d1 in that exponent; the primary equations(1.4),(1.6) and scalar dilation give the stated correct exponent. The example was independently checked visually. This is a source-formula correction, not a cote133 transcription claim. G19 only uses the primitive integer normalization and characteristic-zero hypersurface properties, without asserting a reduced discriminant in every finite characteristic. Bibliographic metadata was checked against the primary NUMDAM publisher archive: https://archive.numdam.org/articles/10.5802/aif.2720/ .
'''
p.write_text(s)

p=R/'questions.tsv'
with p.open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 w.writerows([
 ('G-Q21','PromptQ1/Q2; G19; Alper–Bogart–Velasco2017 Theorem1.7; Benoist2012 Theorem1.3',
  'Can one identify a concrete rectangular coefficient module with zero determinant energy and strictly positive permanent energy?',
  'PROVED G19 for unpadded equal size: restriction discriminant generates one S_(m(m−1)^(k−1))^k copy; exact Haar norm and positive integer Gaussian certificate. No total multiplicity inequality follows.'),
 ('G-Q22','PromptQ1/Q2; G19 positive-padding test',
  'Does this discriminant separator survive multiplication by a positive padding power?',
  'REFUTED G19 for this construction: every positively padded restriction has a repeated component or intersecting components and zero discriminant. This does not refute other higher-row separators.'),
 ('G-Q23','PromptQ1/Q2; G19 explicit per3 slice; R11 dense cubic-surface determinant image',
  'What is the least row length of a highest-weight equation separating per3 from the det3 orbit closure?',
  'PROVED G19: five rows are necessary and sufficient; a specified degree80 copy of weight(48^5) is nonzero on the explicit smooth permanent slice. The210x210 Macaulay minor is94mod101 with independent all-entry reconstruction; this is not a total multiplicity comparison.')])

events=[
 ('I-35','targeted proof check','PASS complete root reading, including final formulations: constant rank-one annihilator equality and rational clearing; Segre incidence construction; actual unipotent Hankel realization; field-extension composition with independent seeds and retained cuts; precisely bounded polynomial-map grid cost; same-seed counterexamples; multiplicative idempotent-corner obstruction in every characteristic. Known optimal dimension is explicitly cited as background.'),
 ('R-24','targeted proof check','PASS entire proof and all finite corollaries read: coefficient-map differential, characteristic-zero lift of integer minor, torus upper bound, epsilon17=0 by R23, padded n18..23 and specified nonrectangular direction. No untested-size extrapolation.'),
 ('R-25','targeted proof check','PASS entire conditional proof and finite corollary: factor1/2 in R, exact bordered permanent, third-order cancellation by allowable linear variations at the same pencil, intersection of open conditions, nonzero limit minor and8m+2 increment. Complete m17 certificate specification yields c18=1262 and stated padded range; universal hypothesis remains open.'),
 ('G-19','targeted proof check','PASS complete root proof and added cubic paragraphs: action/dual convention, singular-locus and Bertini hypotheses, discriminant highest-weight vector generating one copy, equivariant restriction kernels, Haar normalization, integer Gaussian norm, interpolation witness, positive-padding vanishing, exact Macaulay inference and row-minimality from R11. No total multiplicity gap is claimed.'),
 ('G-B18','used and rechecked in this run','Read primary author Theorem1.7 printedp3 and complete proof p5, including its linear-map and characteristic-zero hypotheses. Refs turn264349150view1 and earlier primary retrievals. This is a source-statement/dependency check, not a new proof of the cited theorem.'),
 ('G-B19','used and rechecked in this run','Read primary Benoist Theorem1.3 equations1.4–1.6, Theorem1.7 and Example1.8, pp1190–1192; checked scalar-character normalization and explicitly recorded example typo. Independent reviewer visually checked the example. Publisher metadata confirmed at primary NUMDAM archive turn889597862search2. No full-article proof certification claimed.'),
 ('G-B15','used and rechecked in this run','Reopened Mukai Definition5.20 and Corollary5.21 printedp170, plus Proposition5.19 printedp168, for the discriminant and determinant character. Scope is these exact source statements.'),
 ('G-B06','used and rechecked in this run','Read indexed French original EGAII Definition5.4.1 printedp100 and Theorem5.5.3(i) printedp104, including displayed proof after the latter. Proper projection is closed and projective morphisms are proper. Full PDF fetch was too large, temporary direct retrieval returned403. Exact primary refs turn719125137search0 and turn272574171search0; no complete-book inspection claimed.')
]
for identifier, filename in [('R-24','r24_certificate_check.json'),('R-25','border_m17_check.json')]:
 d=json.loads((R/filename).read_text())
 events.append((identifier,'computation or formal certificate',
  'PASS independent root finite check at '+d['checked_utc']+': '+d['scope']+' Complete result in work/root/'+filename+'.'))
events.append(('G-19','computation or formal certificate',
 'PASS root exact cubic polynomial/Macaulay construction at2026-11-21T04:01:19.073868+00:00, selected determinant94mod101 and full rank210. Independent isolation agent reconstructed all73500 entries and separately eliminated the minor at04:02:21.920730UTC; its event is separately credited. No discriminant expansion was computed.'))
with guard.open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 w.writerow(['statement_id','date','who','type','outcome'])
 for identifier,kind,outcome in events:w.writerow([identifier,now,who,kind,outcome])

p=R/'intro.tex';s=p.read_text()
needle='G-08--G-09 give explicit low-row exclusion bounds at larger padding.'
assert needle in s
s=s.replace(needle,needle+' R-23 expresses the exact quaternary permanent dimension defect as one graded Tor group. R-24 proves its vanishing at size17, and the checked conditional induction R-25 certifies size18; a uniform ternary rank condition is the next exact-dimension gate. G-19 gives a concrete rectangular discriminant copy with zero determinant energy and positive permanent energy in equal size, together with an explicit smooth cubic slice and its five-row minimality. This specified-copy equation does not compare total multiplicities and vanishes under positive padding.')
needle='The precise conditional matrix-invariant consequence remains I-08.'
s=s.replace(needle, 'I-35 weakens bridge preservation to equality of rank-one annihilator base loci, proves independent-seed composition, and isolates the missing synchronization condition with explicit counterexamples. '+needle)
p.write_text(s)

p=R/'open_gates.tex';s=p.read_text()
needle='its vanishing for $m\\geq17$ is the next specific homological gate.'
assert needle in s
s=s.replace(needle,'R-24 and R-25 prove its vanishing at sizes17 and18. R-25 reduces propagation to a full-rank ternary first- and second-derivative space; the remaining uniform hypothesis is for every $m\\geq18$, which would settle exact dimension at all larger sizes. G-19 gives a specified rectangular discriminant copy in equal size, but explicitly supplies neither a total multiplicity inequality nor a positive-padding separator.')
needle='The independent-variable theorem, rank-profile specialization, and arithmetic encoding do not yet supply the required uniform width dependence.'
assert needle in s
s=s.replace(needle,needle+' I-35 gives the strictly weaker rank-one-annihilator criterion and proves composition with independent seeds; the remaining bridge gate is an efficient common substitution preserving the actual restricted seed-dependent boundary functions. Arbitrary rational-boundary preservation and the stated rank-one multiplicative scalarization are refuted.')
p.write_text(s)

with (OUT/'IMPLICATIONS.md').open('a') as f:
 f.write('''

### Exact sizes17 and18, and a constructive induction gate

R24 proves c17=1124 and epsilon17=0. R25 gives a conditional induction with the exact increment8m+2, obtained from first- and second-derivative columns on a ternary section and coordinated third-order tangent cancellations in one bordered quaternary pencil. Its fully checked size17 antecedent proves c18=1262 and epsilon18=0. Thus the exact-dimension target is now a uniform rank condition for every m>=18; no extrapolation from the finite certificates is made. New padded dimension-certified pairs include(17,n),18<=n<=23, and(18,n),19<=n<=25. The endpoint directions(41r,17r,17r,17r) at(17,23), and(46r,18r,18r,18r) at(18,25), lie beyond the rectangular padding boundary and are covered by G17/G18.

### A concrete rectangular copy and its positive energy

G19 packages the classical smooth-section discriminant separator as one explicit rectangular highest-weight polynomial with exact Haar energy and an integer Gaussian expectation at least1 on the permanent, while both vanish on the determinant. Its cubic instance has degree80 and weight(48^5); the displayed five-variable permanent slice has a completely specified Macaulay smoothness certificate, reconstructed independently entry by entry. Four-row determinant-cubic equations vanish identically, so five rows are minimal for such a specified equation. This does not infer a gap between total multiplicities of that isomorphism type: the full isotypic restriction ranks remain separate data. The same discriminant vanishes on every positively padded form, so it does not supply an asymptotic GCT separation.

In Grothendieck's language, this is a determinant-character line on a coefficient scheme, a closed projective incidence image, and one Schur submodule with two different restriction maps. EGAII5.4.1 and5.5.3 supply the exact properness locators; the SGA3/SGA6 dictionary retains the full representation information rather than only its rank. The finite smoothness minor gives a principal open arithmetic certificate. No pure sheaf or motive is inferred from the positive compact norm.

### The remaining seed-composition requirement

I35 proves that scalar boundary preservation only needs equality of rank-one annihilator base loci. It can hold after generic matrix rank drops, and an existential2r−1-dimensional test space suffices. Independent seed sets compose over the rational function field of all other variables, with the displayed sampling exponent. Reusing seeds is a distinct diagonal pullback and can kill the result even when every separate block preserves its entire coefficient span. The explicit multiplicative-corner obstruction also rules out a lift that both makes a rank-r reset rank one and recovers an arbitrary matrix entry by one fixed linear readout. The unresolved constructive target is synchronization for the actual neighboring boundary functions, with budgets polynomial jointly in the original width and length.
''')
with (OUT/'LEDGER.md').open('a') as f:
 f.write('\n\n## '+now+' — finite exact dimensions and a checked induction reduction\n\n')
 f.write('R24 and R25 prove exact maximal quaternary permanent dimension at sizes17 and18. The open degree-m Tor question is reduced further to the explicit ternary derivative-rank antecedent of R25, still unproved uniformly for m>=18. Root independently checked the two selected minors and scaling relations; the author separately recomputed every matrix entry using Ryser formulas. G19 and its explicit cubic certificate are checked restricted results; they are not counted as a general total-multiplicity or positive-padding solution. I35 isolates the smaller boundary-annihilator and synchronization target without claiming an efficient shared-seed construction. This entry is not the scheduled hourly review.\n')

with (R/'attempts.md').open('a') as f:
 f.write('''

## Exact dimension: finite base, then a bordered induction

R24 certifies the first parameter-bound size17. A naive bordered argument using only first-derivative normal columns cannot yield the required increment8m+2. R25 repairs this by coordinated variations whose first-order terms cancel and whose surviving epsilon^3 terms give2m second-derivative columns in the same pencil differential. The independent open-condition argument avoids requiring a ternary pencil itself to attain the generic quaternary dimension. The size17 ternary certificate proves size18. Dense finite tests are not a uniform proof. The next attempt is a cyclic pencil with step-two chords and a first-order analysis of the extra signed-adjugate syzygies.

## A higher-row discriminant and the padding failure

The five-variable discriminant is a concrete rectangular highest-weight vector. Classical singular-section theorems make it vanish on every determinant restriction, while the permanent singular-locus bound supplies a smooth general section. G19 makes the compact and Gaussian norm implications explicit and provides a small cubic slice with an independently reconstructed certificate. The attempt does not compare full isotypic ranks, and positive padding makes every section reducible or nonreduced with singular intersection. The latter is the exact point where this otherwise explicit separator ceases to address the padded problem. Any continuation must use a different equation or remove padding intrinsically with a controlled equivariant construction.

## Unretrieved newer singular-locus claims are not inputs

Search surfaced the abstract of Ying Xie's September2026 preprint arXiv2609.27320, Dimensions of permanental varieties in arbitrary size, claiming an exact codimension result. Attempts to open its primary abstract, PDF, HTML, export endpoint and linked archive failed. No theorem locator or proof was inspected, and the claim is not used. G19 uses only the fully located BCMV bounds R-B17. Newer smooth-slice determinantal-complexity searches likewise did not replace the established cited inputs with unverified latest/best claims.
''')
print(now)
