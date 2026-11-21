from pathlib import Path
from datetime import datetime, timezone
import csv

R = Path(__file__).resolve().parent
BASE = R.parents[1]
OUT = BASE / 'deliverables'
now = datetime.now(timezone.utc).isoformat()
who = 'GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'

events = [
 ('R-20', 'targeted proof check', 'PASS complete root reading and rederivation: five-row motif signs; all eight second-order normal families; both Fourier completions and phase shifts; finite determinant nonvanishing; explicit q,K,X degree budgets; common-factor intersection and Schur Toeplitz minor; primitive-root count; bad-fiber and Vandermonde budgets; descending-degree independence; generic differential specialization; uniform padding inequality and M0=8000001.'),
 ('R-20', 'computation or formal certificate', 'PASS independent root check_r20_certificate.py: Ryser permanents and Berkowitz determinants independently derive the 6/9/6 second-order terms and eight forms; evaluation-basis finite-field interpolation verifies all72 certificate matrix entries, determinants16/15 and combined value22 modulo41. r20_certificate_check.json. This is finite corroboration of the displayed certificate, not extrapolation.'),
 ('R-21', 'targeted proof check', 'PASS complete root reading including final precision clarification: positive integer characteristic coefficient and AGM spectral bound; factorial Gaussian transport; compressed kernel normalization; row-weight block decomposition and Weyl alternant extraction; fixed-N coefficient and exact-elimination bit bounds; absolute error2^-p threshold; integer-rounding distinction and fixed-height exponentially small spectral example.'),
 ('I-29', 'targeted proof check', 'PASS complete root reading: persistent active subspace and suffix complements; constant rank-r reset gauges; stable projected-segment row graph with last reset; coefficient-support accounting including initial passive row; sharp rc+w-1 monomial construction; Grassmann rank-preservation stage and K=2r(w-r)+w-1 sampling. Polynomial pair budget is not polynomial-size sampling in growing width.'),
 ('I-30', 'targeted proof check', 'PASS complete root reading: explicit rank-one endpoint update factors at nonzero constants; determinant-unit and all interval-rank preservation; nonzero univariate endpoints at individually transcendental centers; two-pair second-compound rank2 stage and four-pair rank1 stage; centered SV6, thirteen parameters, and stated finite grid.'),
 ('P-13', 'targeted proof check', 'PASS complete root reading of final general-K version: integer Lagrange denominators; common scaling closure; disjoint base-B parameter digits; Da_K<N_K including n=1; Eisenstein degree; coefficient and coordinate bit bounds; trace-dual basis; annihilator proof of exact coefficient-span recovery; width3 field degree(nD+1)^13 and two-rank specialization. Ordinary field trace, with no additional RH premise.'),
 ('I-31', 'targeted proof check', 'PASS complete independent root reading/rederivation: fixed-next-block projected cone VE is closed irreducible of unchanged dimension; row graph lifts equality; sequential deletion and 2ws-1 block budget; compatible constant gauges; higher-rank chunks and cone composition; rectangular endpoints stay in ground width; individually transcendental centers; local rank descent including empty chunks; homogeneous minor preservation and support detection; K recurrence, bound and Newton sampling. Original-coordinate claim only; polynomial-in-growing-width main gate remains open.')
]
with (R/'integration_06_check_events.tsv').open('w', newline='') as f:
    w = csv.writer(f, delimiter='\t', lineterminator='\n')
    w.writerow(['statement_id','date','who','type','outcome'])
    for identifier,kind,result in events:
        w.writerow([identifier,now,who,kind,result])

p=R/'intro.tex'; s=p.read_text()
old='R-15--R-19 give algebraic dimension growth and an unbounded range of genuine padding. G-10 makes the resulting degree threshold explicit. G-11 identifies rectangular outer highest weights and an explicit degree progression for these gaps, including $n=m+1$ for every $m\\geq8$ and each fixed ratio below $\\sqrt{5/3}$ eventually. G-13 bounds the first possible rectangular gap by a degree with logarithm $O(n^2\\log n)$. G-12 excludes that rectangular sector at and above $n=4m/3$. G-08--G-09 give explicit low-row exclusion bounds at larger padding.'
new='R-15--R-20 give algebraic dimension growth and an unbounded range of genuine padding. G-10 makes the resulting degree threshold explicit. G-11 identifies rectangular outer highest weights and an explicit degree progression for these gaps. R-20 proves such gaps for every integer $m\\geq8{,}000{,}001$ and $m<n<4m/3$; together with G-12, this is the exact eventual padding range for four-row outer rectangles. G-13 bounds the first possible rectangular gap by a degree with logarithm $O(n^2\\log n)$. R-20 also certifies four-row gaps beyond that boundary in its stated dimension range, where the weights must be nonrectangular. G-15 strengthens the necessary first-row condition to $\\lambda_1\\geq d(n-m)+4$, using a dominant third-jet map, and excludes full fourth-jet dominance by dimension. R-21 gives an exact orbit-multiplicity algorithm for each fixed ambient dimension, with numerical degree rather than bit-length complexity. G-08--G-09 give explicit low-row exclusion bounds at larger padding.'
assert old in s; s=s.replace(old,new)
old='The rank-profile construction I-21 now supplies an explicit polynomial-size hitting set for width at most three in one unknown variable order, in every characteristic with the stated field-node convention. It has a complete checked proof here; its mechanism is credited to a recent unrefereed preprint, whose broader claims are not assumed. The unresolved target is a bound polynomial jointly in the growing width, length and degree.'
new='The rank-profile construction I-21 and endpoint refinement I-30 supply an explicit six-pair interpolation hitting generator for width at most three in one unknown variable order, in every characteristic with the stated field-node convention. I-29 treats all words having one fixed singular interval rank. The full-matrix cone proof I-31 gives polynomial-size hitting sets for every fixed width and a pair budget controlled by the number of distinct interval ranks. Complete proofs are given here; the rank-profile and cone mechanisms are credited to a recent unrefereed preprint, whose broader affine-orbit claims are not assumed. The unresolved target is a bound polynomial jointly in the growing width, length and degree; even a polynomial pair budget does not by itself meet that sampling target.'
assert old in s; s=s.replace(old,new)
old='P-12 constructs such a point for the width-three class, together with an integer hitting curve and an exact trace-dual coefficient-span map, using I-21 and elementary algebraic number theory. No additional RH input is required for that construction.'
new='P-12 constructs such a point for the width-three class, together with an integer hitting curve and an exact trace-dual coefficient-span map. P-13 states the general centered-interpolation encoding and reduces the width-three field degree to $(nD+1)^{13}$ using I-30. It applies directly to the rank-spectrum construction I-31 with degree $(nD+1)^{2K_{\\mathcal R}+1}$. These constructions use elementary algebraic number theory and require no additional RH input.'
assert old in s; p.write_text(s.replace(old,new))

p=R/'open_gates.tex'; s=p.read_text()
s=s.replace('R-15--R-19 and G-10--G-11 now prove explicit rectangular multiplicity gaps in their specified linear-padding range. G-12 proves that this outer-rectangular sector is excluded for $n\\geq4m/3$. The unresolved asymptotic range and its higher-row or nonrectangular multiplicities remain separate.', 'R-20 and G-10--G-13 now prove explicit rectangular multiplicity gaps for every sufficiently large $m$ and every integer $m<n<4m/3$, while G-12 excludes this sector for $n\\geq4m/3$. R-20 also forces nonrectangular four-row gaps in its larger dimension-certified range. G-15 gives the sharp full-jet order and its necessary first-row boundary. R-21 computes exact orbit multiplicities for fixed ambient dimension, with an exponent that grows with that dimension. The unresolved asymptotic range and its higher-row multiplicities remain separate.')
s=s.replace('I-21 closes the width-at-most-three, one-unknown-order case by an explicit rank-preserving selector map, including arbitrarily many rank-two cuts. The remaining target is a hitting set whose size and construction time are polynomial jointly in length, degree and growing width.', 'I-30 closes the width-at-most-three, one-unknown-order case with six interpolation pairs, including arbitrarily many rank-two cuts. I-29 proves a polynomial pair budget when there is one allowed singular rank. I-31 proves a bound controlled by the number of allowed rank levels and polynomial-size sampling for every fixed width. Its recurrence is still $2^{O(w\\log w)}$ for all ranks, and sampling uses the pair count as an exponent. The remaining target is a hitting set whose size and construction time are polynomial jointly in length, degree and growing width.')
s=s.replace('P-12 constructs that point and an integer curve for the width-three class; the corresponding general-width construction remains open.', 'P-13 constructs that point and an integer curve for every class hit by the stated centered interpolation map, with degree $(nD+1)^{2K+1}$. This gives polynomial arithmetic budgets for width three and for each fixed width through I-31. The uniform polynomial-in-width arithmetic construction remains open.')
p.write_text(s)

p=R/'grothendieck.tex'; s=p.read_text(); marker='\\subsection{What the manuscript record does and does not establish}'
new=r'''
\paragraph{R-20. Second-order tangent sections and the exact eventual rectangle range.}
The permanent coefficient morphism has a family of differentials over
the one-parameter motif scheme. Row and column relations cancel its
constant and first-order normal terms. Dividing their polynomial
sections by the square of the parameter gives regular limiting sections
of the ambient coefficient bundle. The finite certificate proves a
nonzero minor after one residue-field specialization; the explicit
degree bounds and cyclotomic argument lift that nonvanishing to the
required characteristic-zero family. D-FGA records the resulting image
dimension, and the D-S3 Fourier characters separate its translated
motifs. The invariant quotient and Veronese construction of G-11 then
give the specified rectangular Schur classes. This transports the
actual proof, including its finite threshold, rather than treating a
dimension inequality as an unspecified positivity assertion.

\paragraph{R-21. Integral image ranks and fixed-rank character extraction.}
The orbit-coefficient homomorphism of free modules has an integral Gram
matrix. Its positive-rank characteristic coefficient is a nonzero
integer, giving the displayed analytic spectral separation. A bilinear
coefficient kernel presents the same image ranks without enumerating
the full tensor basis. The diagonalizable group of D-S3 splits that
kernel into weight blocks; the D-S6 Weyl-character identity extracts
each Schur multiplicity from their ranks. D-FGA identifies the ranks
with the degreewise coordinate-image modules. The algorithm is
polynomial only when the bundle rank is fixed and degree is measured
numerically. The metric estimate is ordinary linear algebra, not an
unproved arithmetic slope transfer.

\paragraph{I-29. A persistent active subbundle and one passive rank.}
On the preserved rank-profile chart, constant transition maps split
into an identity on a rank-$r$ active subbundle and invertible or zero
maps on a rank-$(w-r)$ complement. At the last zero map, the vanishing
higher minors give a row graph over the active summand. The stable
projection argument bounds the support filtration of its coefficient
image by $r(w-r)+w-1$. The Grassmannian dimension argument for rank
preservation adds $r(w-r)$ interpolation pairs. These are explicit
rank-stratum and filtration calculations in D-FGA and D-S3, valid with
arbitrarily many resets; the polynomial pair budget retains its
separate sampling exponent.

\paragraph{I-30. Endpoint sections extend to local automorphisms.}
A nonzero constant endpoint section has a split coordinate functional.
The displayed rank-one update extends the section to a bundle
automorphism on the principal open where its determinant is nonzero.
The determinant is a unit at the center. Thus all generic and constant
interval ranks are preserved after the endpoints are absorbed in the
word. In D-FGA this is an explicit trivialization on the required rank
chart, and in D-S3 it preserves the original coordinate support
filtration. The two width-three rank stages consequently use two and
four pairs, respectively.

\paragraph{I-31. Irreducible matrix cones and deletion of stable blocks.}
The closure of scalar multiples of a polynomial matrix image is an
irreducible affine cone in D-FGA. The rank-$s$ chart identifies the
image of its last block with the graph of a map over the first $s$
columns. Equality of two consecutive projected cones allows deletion:
an invertible right action gives a closed subcone of the same dimension,
which is equal to the irreducible cone. This geometric equality
preserves every homogeneous minor and composes under multiplication
on disjoint parameter schemes. Rank descent and split rectangular
endpoints yield the stated recurrence in the original rank-$w$ bundle.
No exponential compound bundle is introduced, but the recursive block
factor remains and prevents a uniform polynomial sampling conclusion.

\paragraph{P-13. A finite flat algebra encoding any centered generator.}
After clearing Lagrange denominators, distinct base-$B$ exponents embed
the bounded parameter monomials in a single polynomial variable. The
Eisenstein quotient by $T^{B^{2K+1}}-2$ is finite free over
$\mathbb Z$; its generic fiber is a separable field and the displayed
trace-dual basis recovers every coefficient coordinate. The
annihilator argument identifies the resulting image span with the
original coefficient-image module. D-FGA gives the finite algebra and
module interpretation, and D-S3 gives the tensor-coordinate transport.
This is the ordinary algebra trace, distinct from the Frobenius traces
of D-ET, and does not acquire a purity or RH hypothesis by analogy.

'''
assert marker in s and '\\paragraph{I-31.' not in s
p.write_text(s.replace(marker,new+marker))

p=BASE/'work/assemble.py'; s=p.read_text()
s=s.replace('A checked rank-profile construction yields polynomial hitting sets for width three in an unknown order and an explicit arithmetic point with trace-coordinate span recovery.', 'Checked rank-profile and matrix-cone constructions yield polynomial hitting sets for every fixed width in an unknown order, with a six-pair refinement at width three, and explicit arithmetic points with trace-coordinate span recovery.')
p.write_text(s)

p=OUT/'IMPLICATIONS.md'; s=p.read_text()
s=s.replace('R15–R19 give an algebraic lower bound', 'R15–R20 give algebraic lower bounds')
s=s.replace('including n=m+1 for every m>=8 and every fixed ratio 1<n/m<sqrt(5/3) eventually.', 'including n=m+1 for every m>=8. R20 extends the result to every integer m>=8,000,001 and m<n<4m/3, so this is the exact eventual range for four-row outer rectangles. Its dimension estimate also forces nonrectangular four-row gaps for each fixed ratio 4/3<n/m<3/sqrt(5), eventually.')
s=s.replace('I21 gives a complete checked polynomial hitting set for width at most three in one unknown variable order, over any characteristic with the explicit working-field convention.', 'I21 and its endpoint refinement I30 give a complete checked polynomial hitting set for width at most three in one unknown variable order, with six interpolation pairs, over any characteristic with the explicit working-field convention. I29 treats words with a single allowed singular interval rank. I31 uses full matrix cones to prove polynomial-size hitting sets for every fixed width, with a pair budget controlled by the number of distinct interval ranks.')
s=s.replace('The rank-profile mechanism is credited to the recent unrefereed Liu preprint, and only the independently proved specialization is used.', 'The rank-profile and cone mechanisms are credited to the recent unrefereed Liu preprint, and only the independently proved original-coordinate statements are used.')
s=s.replace('P12 now constructs the common algebraic point, integral hitting curve, and exact trace-dual span recovery for width three. Its field degree and coordinate descriptions are polynomial in length and total degree, with a large fixed exponent.', 'P12 and the general encoding P13 construct the common algebraic point, integral hitting curve, and exact trace-dual span recovery. The six-pair width-three map gives field degree (nD+1)^13. I31 gives the same construction for every fixed width with degree (nD+1)^(2K_R+1); its dependence on growing width is still too large.')
s=s.replace('The first-jet dominance is proved; second- and third-jet dominance remain explicit targets.', 'The first-jet dominance is proved; the second- and third-jet target was subsequently resolved by G15 below.')
s=s.replace('I28 gives a smaller proved width-three sampler with eight pairs; the general-width gate is unchanged by that constant improvement.', 'I28 first reduced the width-three sampler to eight pairs; I30 subsequently reduces it to six. These constant improvements do not discharge the general-width gate.')
s+='''

### Exact arithmetic ranks and the rank-spectrum construction

R21 gives an explicit least-positive-eigenvalue bound for an integral Gram matrix and a compressed coefficient kernel whose weight-block ranks recover orbit-closure multiplicities by Weyl extraction. For every fixed ambient dimension, its exact bit complexity is polynomial in the numerical degree and coefficient bit length. Its exponent depends on the ambient dimension, so it is not a uniform polynomial GCT algorithm. Integral entries can be rounded at absolute error below one half; the much finer bound in the theorem concerns direct spectral thresholding and is not asserted to be necessary for exact integer recovery.

I31 sets d_w=w²−1 and d_s=(2ws−1)(2 max_{t>s} d_t+1) over the allowed rank set R, and proves that centered SV_K hits the class for K=sum_{s in R}d_s. With L allowed rank levels, K<=2w²(4w²)^(L−1). A bounded L therefore gives polynomially many interpolation pairs in w, while the displayed finite grid still raises the degree-length budget to that pair count. For all rank levels the present proof has K=2^{O(w log w)}. It closes the original-coordinate fixed-width gate, with full proofs of stable-block deletion and cone-preserving restrictions, and leaves both uniform width control and efficient sampling as substantive remaining requirements.
'''
p.write_text(s)
with (OUT/'LEDGER.md').open('a') as f:
    f.write('\n\n## '+now+' — exact rectangle range, arithmetic ranks, and rank-spectrum compression\n\n')
    f.write('R20 closes the eventual four-row rectangular padding range: all integers m>=8000001 and m<n<4m/3 admit the explicit G11/G13 gaps, while G12 excludes the complementary threshold. Its larger dimension range forces nonrectangular gaps. Root independently derived and checked the finite R20 certificate. R21 adds exact fixed-ambient-dimension orbit-multiplicity computation and arithmetic spectral bounds. I29 handles one singular rank with a polynomial pair budget, I30 gives six pairs at width3, and P13 gives the corresponding field degree(nD+1)^13. I31 has now passed independent root and purity full proof reviews and closes the original-coordinate fixed-width construction using matrix cones. Its growing-width recurrence and sampling exponent remain insufficient for the main target. This is an ordinary progress entry, not the scheduled three-hour review.\n')
print(now)
