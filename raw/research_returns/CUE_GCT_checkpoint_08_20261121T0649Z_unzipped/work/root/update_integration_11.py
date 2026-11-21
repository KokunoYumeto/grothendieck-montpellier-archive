"""Add the checked homological dictionary and the one-pair counterexample."""
from pathlib import Path
from datetime import datetime, timezone
import csv

R=Path(__file__).resolve().parent; W=R.parent; OUT=W.parent/'deliverables'
now=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'
p=R/'grothendieck.tex';s=p.read_text()
marker='\\paragraph{D-FGA: images, quotients, and projective parameter spaces.}'
framework=r'''
\paragraph{D-Tor: derived restriction and its obstruction groups.}
SGA~6, Expos\'e~III, Definition~1.5 defines Tor independence of two
schemes over a base by vanishing of their positive Tor sheaves; in
the affine case it is exactly the assertion that derived tensor
product agrees with ordinary tensor product. Notation~1.6 specifies
the relative derived tensor product. Expos\'e~I, Proposition~5.1
and Definition~5.2 give the flat-amplitude criterion, and paragraph~5.4
identifies it with ordinary finite flat-resolution length for a
module. These exact passages were read in the electronic French
primary-text transcription. III~1.5 refers to EGA~III, section~6.5,
for local hyper-Tor; that reference is corroborated here through
SGA~6, without a new whole-section reading of EGA~III.

'''
assert marker in s and '\\paragraph{D-Tor:' not in s
s=s.replace(marker,framework+marker)
marker='\\subsection{What the manuscript record does and does not establish}'
new=r'''
\paragraph{R-23. A single graded part of a derived intersection.}
Let $Z=\operatorname{Spec}(R/J_m)$ be the permanent Jacobian scheme,
and let $L=\operatorname{Spec}S$ be a general four-plane in
$\operatorname{Spec}R$. Their D-Tor derived fiber product has
coordinate complex $(R/J_m)\otimes_R^{\mathbf L}S$.
Its first homology in internal degree $m$ is precisely the dimension
defect $\epsilon_m$. The known full-variable linear resolution gives
the preceding map, and the cyclic coefficient calculation proves
that its $2m-2$ old syzygies remain independent while no new constant
relation appears. The degree-$m$ differential then gives
$c_m=4m^2-2m+2-\epsilon_m$. This is an equality of dimensions of
explicit cohomology groups, not an inference from an alternating
$K_0$ class. The low-size positive defects prove failure of the
unqualified restriction argument. The depth bound rules out a full
regular-sequence justification but leaves the single graded
vanishing question open. D-FGA places the associated generic rank
stratum, and D-S6 distinguishes its actual homology from its
Euler characteristic.

\paragraph{P-15. A nonzero section killed by a dense interpolation morphism.}
The displayed quadratic is a rational coefficient tensor with
minimum tensor-train width three: its three balanced flattenings
have ranks $3,4,4$. The upper-triangular bundle-map factorization
keeps every interval on the invertibility open set. Nevertheless
its pullback under the specified centered Lagrange morphism is
zero. The identities in the three linear coordinates $S,U,V$
prove this directly; the harmonic cross-ratio identity supplies
the separately stated rational-evaluation examples. D-FGA records
the nonzero section and its zero pullback, while D-S3 records the
coordinate choices. The example is over $\mathbb Q(\mathrm i)$
for the fourth-root Lagrange nodes, and uses rational abscissas
for the other convention. No scalar change of coordinates is
silently omitted in comparing these two maps.

'''
assert marker in s;p.write_text(s.replace(marker,new+marker))

events=[
 ('R-23','targeted proof check','PASS complete root proof reading/rederivation: ELSW dimension2m−2 at kappa=m−1; actual row/column syzygies; independence after cyclic restriction; all m² cyclic cofactors independent by exact character support; degree-m tensor-resolution homology equals differential-kernel quotient; no Tor1 belowm; explicit low-size and cyclic defects; R22 bound; depth-versus-section-length obstruction. No vanishing for m>=17 is asserted.'),
 ('R-B16','used and rechecked in this run','Opened author ELSW PDF and inspected Theorem1.1 printedp2, section4.1 Example4.1 and Theorem4.3 printedp11. Specialized the exact linear-first-syzygy count and inspected the Laplace-difference basis. Source statement use, not certification of the whole minimal-resolution proof. Refs turn116356836view0,turn101465360view0–1.'),
 ('R-B17','used and rechecked in this run','Opened BCMV arXiv2402.17839v2 and inspected Theorem4.23 printedp17 and its immediate proof, and Theorem4.14 printedp14 (attributed there to von zurGathen). These bound the height of the gradient ideal; no conjectural exact codimension is used. Refs turn116356836view1,turn101465360view2.'),
 ('G-B03','used and rechecked in this run','Read electronic French SGA6 primary-text transcription: ExposeIII Definition1.5 and Notation1.6, plus ExposeI Proposition5.1/Definition5.2/paragraph5.4. Exact affine derived-tensor/Tor-independence and flat-resolution conventions support the R23 dictionary. EGAIII6.5 is corroborated only through the explicit SGA6 reference; no original EGA scan rereading claimed. Refs turn784128622view0–1,turn270082121view0–1.')
]
with (R/'integration_11_check_events.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['statement_id','date','who','type','outcome'])
 for identifier,kind,result in events:w.writerow([identifier,now,who,kind,result])

p=R/'sources.md';s=p.read_text()
needle='A separate 24-page PDF found during retrieval was an incomplete front-matter excerpt and was not treated as the full volume.'
assert needle in s
s=s.replace(needle,needle+' For R23, additionally read Exposé III, Definition1.5 and Notation1.6 at https://grothendiecksga.com/read/sga6/fr/III-1.html , and Exposé I, Proposition5.1, Definition5.2 and paragraph5.4 at https://grothendiecksga.com/read/sga6/fr/I-5.html . These are electronic French primary-text transcriptions. III1.5 explicitly refers to EGAIII6.5; that reference is corroborated through SGA6 only.')
p.write_text(s)

p=R/'open_gates.tex';s=p.read_text()
needle='Exact image dimension, individual finite-degree or changing-direction comparisons beyond that range, and the superlinear-padding GCT regime remain separate gates.'
assert needle in s
s=s.replace(needle,'R-23 expresses the exact image-dimension defect as $\\dim\\operatorname{Tor}_1^R(R/J_m,S)_m$ after a general four-variable restriction; its vanishing for $m\\geq17$ is the next specific homological gate. Individual finite-degree or changing-direction comparisons beyond that range, and the superlinear-padding GCT regime, remain separate gates.')
needle='General intermediate-rank matrix cancellation remains outside these divisor and product arguments.'
s=s.replace(needle,needle+' P-15 refutes a node-uniform one-pair generator already at width three with invertible factors. It does not decide the two-pair rank-two-reset case or the growing-width question.')
p.write_text(s)

with (OUT/'IMPLICATIONS.md').open('a') as f:
 f.write('''

### The exact remaining dimension defect is homological

R23 proves c_m=4m²−2m+2−epsilon_m, where epsilon_m is the degree-m dimension of Tor_1^R(R/J_m,S), J_m is the permanent gradient ideal, and S is a general four-variable linear restriction. All lower-degree Tor_1 pieces vanish generically. The complete full-variable linear-syzygy theorem supplies exactly2m−2 relations, which remain independent on the section; every additional differential relation is measured by this one Tor piece. R13 gives positive exact defects for sizes3 through16, so simply restricting the known full-variable resolution would be invalid. A full regular-sequence argument is also obstructed by the known gradient-ideal height. The required degree-m vanishing for m>=17 remains unproved.

P15 closes a tested simplification negatively: one ordinary centered interpolation pair fails for an explicit minimum-width-three polynomial at four fourth-root Lagrange nodes, even though every transition factor and interval product is invertible. The same quadratic gives balanced rational-evaluation counterexamples at harmonic rational nodes, including a subset of the standard integer grid. The paper separates those coordinate conventions. These counterexamples leave the proved six-pair width-three map and the general-width target intact.
''')
with (OUT/'LEDGER.md').open('a') as f:
 f.write('\n\n## '+now+' — exact derived-restriction gate and one-pair counterexample\n\n')
 f.write('R23 identifies the permanent four-variable dimension defect with one degree-m Tor_1 group and proves all earlier Tor_1 degrees vanish generically. The old linear syzygies are explicitly controlled; unrestricted exactness after restriction is refuted by the positive defects for sizes3–16. Root checked the whole proof and exact primary-source locators. P15 refutes the tested one-pair width-three strengthening for the specified node conventions, with full root and isolation reviews. The latter closes a simplification attempt but is not counted as movement on the polynomial-in-width target. This is not the scheduled review.\n')

attempts=R/'attempts.md'
if not attempts.exists(): attempts.write_text('# Root research attempts\n\nRun CUE_GCT_20261121_R1. Actual deductions and failed transfer steps are recorded separately from proof status.\n')
with attempts.open('a') as f:
 f.write('''

## Extending low-degree rational-evaluation ideal bounds by factor width

The attempted inference that multiplying by an auxiliary polynomial cannot lower a coefficient-cut rank is false. Over every field, for r>=1, g(x,y)=sum_{j=0}^r x^j y^j has coefficient-matrix rank r+1, whereas (1−xy)g=1−x^(r+1)y^(r+1) has rank2. Thus the HMM low-degree hypotheses cannot be removed merely by factoring an ideal element and assigning the factor the width of the product. This is a counterexample to that particular inference, not an obstruction to every ideal-based method. P15 separately tests and refutes a one-pair width-three conjecture for stated node choices.

## The period-removal step for stretched multiplicities

The initial G18 draft moved the auxiliary partial flag to avoid the finite projective stabilizer, which covered nonrectangular directions only. The successful replacement varies the padding line while fixing the smooth Fermat factor. Unique factorization makes the generic padded form projectively free; this includes a trivial auxiliary representation and therefore rectangular directions. The final proof supersedes the initial restricted draft, with full independent checks and explicit common-degree semigroup bounds.

## Exact generic permanent dimension after the uniform staircase

R22 reaches leading dimension4m² with an explicit O(m^(3/2)) error. The next route uses the known full-variable linear syzygies. Assuming they stay the complete syzygy space after restriction would be wrong; R23 identifies the additional graded Tor_1 term and gives actual positive defects in sizes3–16. A full regular-sequence argument is impossible by the gradient-ideal height. The remaining specific task is the degree-m Tor vanishing or a sharper quantitative bound for m>=17.
''')
print(now)
