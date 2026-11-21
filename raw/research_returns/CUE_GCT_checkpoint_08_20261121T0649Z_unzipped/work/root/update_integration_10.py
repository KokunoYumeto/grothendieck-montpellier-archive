"""Integrate R22's checked uniform dimension bound and G17 bit lengths."""
from pathlib import Path
from datetime import datetime, timezone
import csv

R=Path(__file__).resolve().parent; W=R.parent; OUT=W.parent/'deliverables'
now=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'

corollary=(W/'rectangular/g17_bitlength_corollary.tex').read_text()
p=R/'g17_fragment.tex'; s=p.read_text(); assert '\\label{G17:bitlength}' not in s
p.write_text(s+corollary)
p=R/'findings.tex'; s=p.read_text(); marker='\\begin{theorem}[G-18:'
assert '\\label{G17:bitlength}' not in s and marker in s
p.write_text(s.replace(marker,corollary+'\n'+marker))

events=[
 ('R-22','targeted proof check','PASS complete independent root reading/rederivation, all nine sections: typed-position count and simultaneous row/column supports; endpoint permutation signs and forced top edge pair; row-form indices; both Fourier completions directly; basis invertibility; specialized diagonal evaluation columns and exact last X² minor including b3; reflection and bidegree/character alignment; coefficient interval, coprime intersection and Schur restriction; determinant exponent ranges; one integer grid over Q(q)(X); gcd(b,m) translation count; descending highest components; one-epsilon differential rank; all asymptotic and padding constants. Integer-grid wording is correctly restricted to untwisted motif parameters. No global Jacobian extrapolation was used.'),
 ('G-17','targeted proof check','PASS complete root reading/rederivation of quantitative bitlength corollary: weak compositions bound binom(N+s-1,s), six Weyl factors, L<=4ns,p<=2ns,u<=2n²; exact logarithmic bound for j_*; uniform O(n^5 log(s+1)+n²log n) and fixed-s O_s(n²log n); degree and highest-weight multiplication adds O(log(ns)) bits. This proves size of an existing witness, not efficient search or positivity certification.')
]
with (R/'integration_10_check_events.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['statement_id','date','who','type','outcome'])
 for identifier,kind,result in events:w.writerow([identifier,now,who,kind,result])

p=R/'grothendieck.tex'; s=p.read_text(); marker='\\subsection{What the manuscript record does and does not establish}'
new=r'''
\paragraph{R-22. Cyclic characters and one open differential-rank condition.}
The permanent coefficient morphism is an integral polynomial map of
affine schemes. R-22 works over a cyclotomic extension in characteristic
zero. The D-S3 diagonal torus restricts to $\mu_m$, whose characters
split the differential coefficient space. A single staircase parameter
space supplies both local row and column cofactor relations. Their
highest components define two subspaces with explicitly computed
coprime-factor intersection. The D-S6 Schur determinant is the nonzero
minor of coefficient restriction; its principal geometric specialization
is a Vandermonde determinant with distinct cyclotomic exponents.
The product of finitely many nonzero parameter polynomials defines one
nonempty open subset on which all bidegrees are simultaneously valid.
An integer grid contains a point of that open after the root of unity
is fixed; translated motifs use the prescribed cyclotomic twists.
The final D-FGA differential minor is nonzero in one common deformation,
so its image dimension is at least the stated bound. The proof can be
spread over the localization where these particular denominators and
minors remain nonzero; it does not assert the same rank in every residue
characteristic. Its quotient and highest-weight consequences use the
characteristic-zero dictionaries of G-10 and G-17--G-18.

\paragraph{The G-17 quantitative corollary.}
The rank of a symmetric power and the six-factor Schur-rank polynomial
bound the ambient bundle rank in the D-S6 construction. Together with
the polynomial action degree, these give the binary-length estimate
for the existing first successful quotient degree. This is an effective
bound on the degrees of sections in the D-FGA graded algebra; it is
separate from computing the section or deciding its multiplicity.

'''
assert marker in s;p.write_text(s.replace(marker,new+marker))

p=R/'intro.tex';s=p.read_text()
s=s.replace('R-15--R-20 give algebraic dimension growth and an unbounded range of genuine padding.', 'R-15--R-22 give algebraic dimension growth and an unbounded range of genuine padding. R-22 proves $4m^2-20m^{3/2}+2\\leq\\dim\\mathcal P_{m,4}\\leq4m^2-2m+2$ for $m\\geq99$, reaching every fixed padding ratio below $\\sqrt2$ with an explicit threshold.')
s=s.replace('R-20 proves such gaps for every integer $m\\geq8{,}000{,}001$ and $m<n<4m/3$; together with G-12, this is the exact eventual padding range for four-row outer rectangles.', 'R-20 first closes the eventual rectangular range, and R-22 lowers its uniform threshold to $m\\geq2025$: every integer $m<n<4m/3$ has such gaps, while G-12 excludes the complementary range. This is the exact eventual padding range for four-row outer rectangles.')
s=s.replace('R-20 also certifies four-row gaps beyond that boundary in its stated dimension range, where the weights must be nonrectangular.', 'R-22 certifies nonrectangular four-row gaps beyond that boundary throughout every fixed ratio below $\\sqrt2$, eventually.')
s=s.replace('It gives effective first-stretch and progression bounds through a partial-flag construction.', 'It gives effective first-stretch and progression bounds through a partial-flag construction. The first successful stretch has polynomial binary length in $n$ and $\\log(s+1)$, and logarithm $O_s(n^2\\log n)$ for fixed $s$.')
p.write_text(s)

p=R/'open_gates.tex';s=p.read_text()
s=s.replace('R-20 and G-10--G-13 now prove explicit rectangular multiplicity gaps for every sufficiently large $m$ and every integer $m<n<4m/3$, while G-12 excludes this sector for $n\\geq4m/3$. R-20 also forces nonrectangular four-row gaps in its larger dimension-certified range,', 'R-22 and G-10--G-13 prove explicit rectangular multiplicity gaps for every $m\\geq2025$ and every integer $m<n<4m/3$, while G-12 excludes this sector for $n\\geq4m/3$. R-22 proves $\\dim\\mathcal P_{m,4}=4m^2-O(m^{3/2})$, forcing nonrectangular four-row gaps for every fixed padding ratio below $\\sqrt2$, eventually,')
s=s.replace('The unresolved asymptotic range and its higher-row multiplicities remain separate.', 'The remaining dimension transition has width at most $O(\\sqrt m)$ below $\\sqrt2m$. Exact image dimension, individual finite-degree or changing-direction comparisons beyond that range, and the superlinear-padding GCT regime remain separate gates.')
p.write_text(s)

p=W/'assemble.py';s=p.read_text()
s=s.replace('Algebraic permanent-image dimensions and invariant quotients produce the exact eventual four-row rectangular padding range, and an enhanced tensor construction specifies nonrectangular highest weights throughout the dimension-certified range.', 'A uniform staircase construction gives quaternary permanent-image dimension $4m^2-O(m^{3/2})$, reaching every fixed padding ratio below $\\sqrt2$. Invariant quotients give the exact eventual four-row rectangular range; enhanced tensors classify all four-row stretched directions in the dimension-certified range and compare every sufficiently large stretch.')
p.write_text(s)

p=OUT/'IMPLICATIONS.md';s=p.read_text()
s=s.replace('R15–R20 give algebraic lower bounds', 'R15–R22 give algebraic lower bounds')
s=s.replace('R20 extends the result to every integer m>=8,000,001 and m<n<4m/3, so this is the exact eventual range for four-row outer rectangles. Its dimension estimate also forces nonrectangular four-row gaps for each fixed ratio 4/3<n/m<3/sqrt(5), eventually.', 'R22 lowers the uniform threshold to every integer m>=2025 and m<n<4m/3, giving the exact eventual range for four-row outer rectangles. Its dimension estimate reaches every fixed ratio n/m<sqrt(2), eventually, including the necessarily nonrectangular sector above4/3.')
s+='''

### The dimension bound reaches every fixed ratio below its ceiling

R22 proves 4m²−20m^(3/2)+2 <= dim(P_m4) <= 4m²−2m+2 for m>=99. Its arbitrary-size staircase uses one simultaneous pencil deformation. A common integer choice of the untwisted motif parameters works for all required bidegrees; coprime-factor intersections and exact Schur determinants prove the simultaneous row/column ranks. The proof does not add ranks from unrelated pencils or extrapolate a finite list of computations.

For every fixed 1<rho<sqrt(2), all integers m<n<=rho*m are dimension-certified once m>=max(99,ceil(100/(2−rho²)²)). In particular the exact eventual rectangular range m<n<4m/3 holds for every m>=2025. More finely, m>=169 and m<n<=sqrt(2)*m−4sqrt(m) suffice. G17–G18 then classify all four-row stretched directions and compare every sufficiently large stretch. The row/column torus ceiling forbids this dimension argument from passing n>=sqrt(2)*m, and G18 gives eventual determinant dominance along each fixed strict direction there. The unresolved dimension transition is confined to an O(sqrt(m)) strip below that ceiling. The unrestricted GCT regime with superlinear padding, changing directions, and efficient Schur-Gram minors remains open.

The additional G17 quantitative corollary bounds log2(j_*) by log2(u+1)+u*log2(p)+(2u+1)*log2(beta). This is O(n^5 log(s+1)+n²log n), and O_s(n²log n) for fixed s. The stretch, original coordinate degree and label entries thus have polynomial binary length in n and log(s+1). Their bounded description length is separate from an efficient algorithm finding or certifying the multiplicity gap.
'''
p.write_text(s)
with (OUT/'LEDGER.md').open('a') as f:
 f.write('\n\n## '+now+' — uniform four-variable dimension ceiling reached asymptotically\n\n')
 f.write('RQ-26 is PROVED by R22 after author and independent root/isolation whole-proof checks, plus an independent purity check of sections6–9. For m>=99, c_m>=4m²−20m^(3/2)+2; every fixed padding ratio below sqrt(2) is now covered with a stated threshold. The remaining dimension transition is at most O(sqrt(m)) below sqrt(2)m. R22 lowers the exact eventual rectangular boundary threshold to m>=2025. G17–G18 supply all strict directions and every sufficiently large stretch; the G17 first-stretch bitlength corollary is checked separately. This is an ordinary dated progress entry, not the scheduled review, which remains due at03:49:46UTC.\n')
print(now)
