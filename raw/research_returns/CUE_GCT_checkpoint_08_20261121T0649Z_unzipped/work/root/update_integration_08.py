from pathlib import Path
from datetime import datetime, timezone
import csv,json

R=Path(__file__).resolve().parent
OUT=R.parents[1]/'deliverables'
now=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'
p=R/'findings.tex';s=p.read_text();assert '\\label{G-17}' not in s
p.write_text(s+'\n'+(R/'g17_fragment.tex').read_text())
with (R/'questions.tsv').open('a') as f:
 f.write('G-Q18\tPrompt Q1/Q2; G17 partial-flag invariant quotient\tFor a dimension-certified padded pair, which rational four-row partition directions contain a positive stretched multiplicity gap?\tPROVED G-17: for nu partition ns, some positive stretch j has a gap iff nu4>0 and nu1>(n-m)s. Explicit first-stretch bound and every-term progression in the affirmative case; every stretch excluded on the two complementary faces.\n')
events=[
 ('G-17','targeted proof check','PASS complete independent root reading/rederivation: extremal Cartan component and coordinate ring; partial-flag dimension and eta0 case; Veronese-Segre degree pairing; exact single-label Hom extraction; positive theta witness and all moment components; tensor-power projective stabilizer; invariant dimensions; finite kernel; independent End(V*) parameter degree versus contragredient group-action degree; cumulative and progression bounds; equality faces, four-variable inheritance and G15 compatibility.'),
 ('I-32','targeted proof check','PASS complete independent root reading/rederivation: recursive seed resets and exact scalar; both paired unipotent identities; all partial intervals, single halves and empty singular set; common-center rank=min singular rank and generic equality; exact iff coordinate-cone criterion; inclusion among actual final rank1 local tests; one-pair dense detection. Exponential zero-coordinate compression bound is refuted, without a dense-sampling lower bound.'),
 ('I-33','targeted proof check','PASS complete independent root reading/rederivation: divisor multiplicity domination for the characteristic prime; root-of-unity orbit intersection count for all other primes; remaining monomial relation and coordinate variants; two-product coefficient span; elementary central-binomial prime bound and sieve cost; n64 disjoint subset-sum counterexample; width2 rank-one concatenation; scalar Lagrange product-closure repair and field-size convention. Known class complexity is explicitly credited rather than claimed as new.')
]
with (R/'integration_08_check_events.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['statement_id','date','who','type','outcome'])
 for identifier,kind,result in events:w.writerow([identifier,now,who,kind,result])
p=R/'grothendieck.tex';s=p.read_text();marker='\\subsection{What the manuscript record does and does not establish}'
new=r'''
\paragraph{G-17. Partial flags classify the stretched directions.}
For a partition direction $\nu\vdash ns$, subtract its last row to
obtain the polynomial highest weight $\eta$. The orbit of its extremal
line is the partial flag scheme embedded by the exterior-power Schur
construction. Its degree-$d$ coordinate module is the Cartan component
$S_{d\eta}V$, as follows directly by dualizing the orbit span of the
extremal tensor power. Pairing this cone with the $s$th Veronese of the
coefficient scheme makes the D-S3 invariant functor extract exactly
the multiplicity at $d\nu$, in original coordinate degree $sd$.
Positive Fermat coefficients balance the moment map precisely in the
strict region $\nu_4>0$, $\nu_1>(n-m)s$. D-FGA gives the quotient
dimension comparison and its effective Hilbert bounds. The two
excluded faces follow from the earlier ideal containments, so this
is an exact stretched-direction criterion, with its dimension
hypothesis retained. D-S6 records every exterior, symmetric and Schur
operation used in the construction.

\paragraph{I-32. A common-center rank chart with exponential deletion cost.}
Each singular factor is lifted to two univariate bundle maps whose
product depends only on the difference of their coordinates. On the
diagonal center those differences vanish, and every partial interval
is a product of nested projections between invertible boundary maps.
Thus all interval ranks are already correct on that D-FGA chart.
Nevertheless a homogeneous matrix-coordinate section is the product
of all paired differences. A coordinate subspace meets its nonvanishing
locus only if it retains one coordinate from every pair. This gives
the exact exponential threshold for preserving the image cone, while
a dense D-S3 interpolation map keeps the same section nonzero. The
obstruction concerns this coordinate-deletion criterion only.

\paragraph{I-33. Divisors on the one-dimensional torus and compatible weights.}
The prime-weight substitutions are integral cocharacters of the
split torus in D-S3. Pulling back the rational ratio of two products
gives divisors on the multiplicative line. Distinct prime root orbits
can overlap in at most one point, while the inseparable case is
controlled by integer divisor multiplicities. This forces any lost
ratio to be a character, which the coordinate variants separate.
The subset-sum example identifies the exact failure of closure under
products for the raw family. Interpolating its finite evaluation set
by one affine curve repairs scalar product closure because the
coordinate ring of the line is a domain. D-FGA places this curve and
the coefficient-image restriction; no purity theorem is needed.

'''
assert marker in s;p.write_text(s.replace(marker,new+marker))
p=R/'intro.tex';s=p.read_text()
s=s.replace('An auxiliary dual line removes the rectangular stability restriction.', 'An auxiliary dual line removes the rectangular stability restriction. More generally, G-17 classifies every four-row stretched direction under the same dimension hypothesis: for $\\nu\\vdash ns$, some stretch has a positive gap exactly when $\\nu_4>0$ and $\\nu_1>(n-m)s$. It gives effective first-stretch and progression bounds through a partial-flag construction.')
s=s.replace('The unresolved target is a bound polynomial jointly in the growing width, length and degree; even a polynomial pair budget does not by itself meet that sampling target.', 'I-32 refutes a polynomial coordinate-cone deletion bound even at a common center with every interval rank preserved. I-33 instead gives explicit small prime-cocharacter families for two dense products, their exact limitation, and a scalar product-closure repair. The unresolved target is a bound polynomial jointly in the growing width, length and degree; even a polynomial pair budget does not by itself meet that sampling target.')
p.write_text(s)
p=R/'open_gates.tex';s=p.read_text()
s=s.replace('G-15 gives the sharp full-jet order and its necessary first-row boundary.', 'G-17 classifies every four-row stretched direction for the dimension-certified pairs by the two strict inequalities in its statement. G-15 gives the sharp full-jet order and its necessary first-row boundary.')
s=s.replace('Its recurrence is still $2^{O(w\\log w)}$ for all ranks, and sampling uses the pair count as an exponent.', 'Its recurrence is still $2^{O(w\\log w)}$ for all ranks, and sampling uses the pair count as an exponent. I-32 proves that polynomial exact coordinate-cone compression at every preserved common center is impossible. I-33 supplies a dense prime-cocharacter repair for two-product factors and their products, leaving general matrix cancellation outside its divisor argument.')
p.write_text(s)
with (OUT/'IMPLICATIONS.md').open('a') as f:
 f.write('''

### Exact four-row stretched-direction criterion

G17 extends G16 to every rational direction in the four-row partition simplex. For a pair satisfying dim(P_m4)+3>2n²+2, fix nu partition ns. Some positive stretch j has a padded-permanent multiplicity exceeding the determinant multiplicity exactly when nu4>0 and nu1>(n−m)s. If a condition fails, every stretch is excluded. If both hold, the theorem supplies an effective first-stretch bound and an explicit progression of successful stretches. The auxiliary partial-flag cone extracts just the selected Schur component and has an explicit stable point. This classifies stretched directions for the certified pairs; it does not decide positivity at an arbitrary individual stretch or extend the underlying dimension range.

### A refuted compression gate and a dense sampling construction

I32 proves that exponential dependence on width is necessary for preserving the entire matrix image cone by retaining original coordinates at every preserved common center. Its exact minimum is 3·2^(w−2)−2 positions, even though all interval ranks are already correct. One dense interpolation pair detects the displayed scalar, so the counterexample directs the next construction toward weaker invariants or dense sampling rather than establishing a general PIT lower bound. I33 gives n+1 polynomial-magnitude prime cocharacters for differences of two dense products, over every characteristic. It supplies an exact width-two counterexample to the raw family's product closure, then repairs that failure by a single interpolating curve. The restricted class already has polynomial PIT in the literature; the new proof and explicit family do not settle general growing-width cancellation.
''')
with (OUT/'LEDGER.md').open('a') as f:
 f.write('\n\n## '+now+' — stretched directions classified and coordinate deletion ruled out\n\n')
 f.write('G-Q18 is PROVED by G17: the exact four-row stretched-direction criterion in every dimension-certified padded pair is nu4>0 and nu1>(n-m)s. Root checked the entire proof, including Cartan coordinate rings, stable points and quantitative bounds. I32 refutes polynomial full-cone coordinate deletion at every rank-preserved common center, with an exact exponential threshold. I33 proves a small prime-cocharacter family and its scalar product repair in a known restricted PIT class; this is not counted as a solution of the general matrix gate. This is an ordinary progress entry, not a scheduled review.\n')
p=R.parents[1]/'work/qa/visual_review_03.json';data=json.loads(p.read_text());data['reviewed_utc']=now;p.write_text(json.dumps(data,indent=2)+'\n')
print(now)
