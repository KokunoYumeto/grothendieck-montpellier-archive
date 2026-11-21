from pathlib import Path
from datetime import datetime, timezone
import csv

R=Path(__file__).resolve().parent
OUT=R.parents[1]/'deliverables'
now=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'
p=R/'findings.tex';s=p.read_text();assert '\\label{G-15}' not in s
p.write_text(s+'\n'+(R/'g15_fragment.tex').read_text())
p=R/'questions.tsv'
with p.open(newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
for row in rows:
    if row['id']=='G-Q15':
        row['state']='PROVED G-15: explicit sl2 pencil has surjective third-jet differential in every size; lambda1<=d(n-m)+3 excludes a positive four-row gap. A rectangular gap requires d(4m-3n)>=16. No general strong Lefschetz assumption remains.'
rows.append({'id':'G-Q16','source_and_locator':'Prompt Q1/Q2; G15 and G06 dimension bound','question':'Can the full fourth-jet map of quaternary determinant images also be dominant?','state':'REFUTED for every m>=4 by G-15: its target dimension exceeds 2m²+2; order3 is maximal for full-jet dominance.'})
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['id','source_and_locator','question','state'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)

events=[
 ('G-15','targeted proof check','PASS complete root reading including final inverse-power version: harmonic covariants from symmetrized sl2 powers; nonzero value on H by the dense semisimple locus; orthogonal-polynomial diagonal induction and uniform trace normalization; positive tridiagonal Jacobi matrix and exact resolvent cofactor; isotypic projection of cofactor multiples; both parity cases and boundary spins; maximal jet order; G14 coefficient-weight transfer and rectangular divisibility refinement.'),
 ('G-15','computation or formal certificate','PASS independent actual-pencil cofactor computation for m2 through18 modulo1000003: tridiagonal continuants expanded in four variables, multiplied by all four variables and truncated modulo t^4; every coefficient matrix has full third-jet rank. check_sl2_jets.py and sl2_jet_checks.json. Finite corroboration, not a proof for untested sizes.'),
 ('I-27','targeted proof check','PASS complete root reading: carry-free deficits in [-2,2] force active bits individually coherent; coordinate-face classification; number of tested elements and gauge-independent equality; invertible width2 witness; raw magnitude qualification; dense-map scope limitation.'),
 ('I-28','targeted proof check','PASS complete root reading: nonzero left constant starts the nested image chain at a point; induction justifies removing non-growth parameters; nonzero right constant gives a proper Grassmannian hyperplane and its one-dimension saving; endpoints fit in r(w-r); common transcendental center meets endpoint hypotheses; two-pair rank2 stage and retained six-pair rank1 stage yield the eight-pair sampler.'),
 ('I-B08','used and rechecked in this run','Root independently opened arXiv1309.5668 primary full version and read Definition1.1 p3, Theorem4.1 pp21-22 and Corollary4.3 p22, including factorization use of every-order promise and additive SV composition. Confirmed field size and exact 1+2 floor(2 log2 w) pair count. Subsidiary condenser proofs not certified.'),
 ('G-B17','used and rechecked in this run','Root inspected indexed passages from the actual Fulton-Harris book scans: section11.2 Exercise11.11 p151 and Exercise11.14 p153. Publisher record confirms first edition1991, GTM129 and DOI. Full book retrieval exceeded web-tool size and local download was canceled; no whole-book or visual-page review claimed.')
]
with (R/'integration_05_check_events.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['statement_id','date','who','type','outcome'])
    for identifier,kind,result in events:w.writerow([identifier,now,who,kind,result])

p=R/'sources.md';s=p.read_text();s+='''

## G-B17 — The sl2 tensor and harmonic decompositions

Fulton, W., & Harris, J. (1991). *Representation theory: A first course* (Graduate Texts in Mathematics, Vol. 129). Springer. https://doi.org/10.1007/978-1-4612-0979-9

Exact locators: section11.2, Exercise11.11, printed p.151 (Clebsch–Gordan); Exercise11.14, printed p.153 (symmetric powers of the three-dimensional adjoint representation). The exact exercise statements were inspected in indexed passages from the primary book scans hosted by university mathematics departments. The publisher record lists the first-edition print publication in1991; its current electronic record also displays later reprint/digital dates. G15 supplies the specialized harmonic covariants and finite Jacobi calculation itself. Full-PDF web retrieval was too large; the attempted local full-book retrieval was canceled. No complete-book reading is claimed.

Primary scan locators: https://websites.math.leidenuniv.nl/edixhoven/teaching/2019-2020/CIMPA/Fulton-Harris.pdf and https://www-fourier.univ-grenoble-alpes.fr/~panchish/ETE%20LAMA%202018-AP/lecturesZETAS2018/Fulton%20Harris_Representation%20theory%20first%20course.pdf . Publisher metadata: https://link.springer.com/book/10.1007/978-1-4612-0979-9 .
''';p.write_text(s)

p=R/'grothendieck.tex';s=p.read_text();marker='\\subsection{What the manuscript record does and does not establish}'
new=r'''
\paragraph{G-15. Harmonic covariants make the third-jet morphism dominant.}
The $\mathrm{SL}_2$ representation-ring decomposition of the endomorphism
bundle and the symmetric algebra of its adjoint bundle gives the covariants
$T_l$ in D-S3/D-S6. Their scalar coefficients in the adjugate are determined
by a finite trace pairing and its Jacobi matrix. The strictly positive
squared norm in the proof is an ordinary Hermitian linear-algebra fact,
not a weight-purity assertion. Linear multiples of these cofactor sections
surject onto the quotient by the fourth power of the padding-coordinate
ideal. Thus the differential minor gives dominance of the corresponding
third-jet morphism in D-FGA, while dimension excludes the next full jet.
The D-S6 exterior-column weight bound transfers dominance to containment
of the specified isotypic ideal submodules. This closes the precise
higher-jet gate stated conditionally in G-14.

\paragraph{I-27. A Boolean face in the cocharacter lattice.}
The Pl\"ucker ideal of the D-FGA Grassmann cone supplies integral linear
equations in the diagonal cocharacter lattice of D-S3. Under the actual
base-six code embedding, bounded integer deficits cannot carry between
digits. Its intersection with that lattice condition is consequently a
coordinate face of the seed cube. The induced original-bundle characters
then agree on two untested basis directions. The displayed rank-two
unipotent representation detects this equality as exact vanishing of a
nonzero section. No statement about arbitrary decoders follows.

\paragraph{I-28. A hyperplane dimension drop pays for the final parameter.}
The left endpoint defines a curve through its nonzero constant point of
the Grassmannian. Including it in the nested projective-image chain uses
the same dimension budget as the internal bundle automorphisms. If the
constant right functional vanishes on the final image, that image lies
in a proper hyperplane section and loses at least one dimension; this
pays for retaining the right endpoint parameter. D-FGA therefore gives
the sharper $r(w-r)$ support existence statement with both endpoints
included. Its width-three specialization has eight SV pairs, and the
finite flat trace construction of P-12 uses the corresponding seventeen
parameters when sharpened by this result.

''';assert marker in s;p.write_text(s.replace(marker,new+marker))

with (OUT/'LEDGER.md').open('a') as f:
    f.write('\n\n## '+now+' — third-jet gate closed\n\n')
    f.write('G-Q15 changes from OPEN to PROVED by G15: a uniform explicit sl2 pencil dominates the full third jet. G-Q16 is refuted for the fourth and higher full jets by dimension. The multiplicity boundary is lambda1>=d(n-m)+4, with d(4m-3n)>=16 for rectangles. Root read the full proof and independently checked actual cofactor ranks for sizes2–18. I27 closes the filtered-code repair by a carry-free cocharacter argument, and I28 sharpens the width-three generator from ten to eight pairs using the endpoint hyperplane argument. This is an ordinary progress entry, not the scheduled three-hour review.\n')
with (OUT/'IMPLICATIONS.md').open('a') as f:
    f.write('\n\n### Third jets and the strengthened obstruction boundary\n\n')
    f.write('G15 resolves the higher-jet target left open in G14. The full third-jet map of quaternary degree-m determinant images is dominant for every m; for m>=4 no fourth full jet can be dominant. Consequently every positive four-row padded-form multiplicity gap has lambda1>=d(n-m)+4. If its outer shape is rectangular, divisibility forces d(4m-3n)>=16. The proof uses explicit sl2 covariants and a positive Jacobi inverse-power norm, with no additional RH or general Lefschetz assumption. I27 rules out the specified coherent-seed filtering repair. I28 gives a smaller proved width-three sampler with eight pairs; the general-width gate is unchanged by that constant improvement.\n')
print(now)
