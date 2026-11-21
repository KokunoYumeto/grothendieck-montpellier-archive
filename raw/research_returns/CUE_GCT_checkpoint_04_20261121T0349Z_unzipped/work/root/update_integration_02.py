from pathlib import Path
from datetime import datetime, timezone
import csv
R=Path(__file__).resolve().parent
now=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'
rows=[
('R-16','targeted proof check','PASS complete root reading of simultaneous disjoint-row identities, exact bidegree space, root-of-unity coefficient obstruction, dual Jacobi–Trudi/Weyl alternant nonvanishing, character Vandermonde, deformation minor and padding arithmetic.'),
('I-21','targeted proof check','PASS complete root reading completed before this record: unit-rank profile lemma including last-zero reset, lowest homogeneous component truncation, two-stage rank preservation and original-coordinate width-three sampler; source provenance retained.'),
('P-12','targeted proof check','PASS complete root reading: common scalar clears Lagrange denominators without changing the class; injective base-B encoding; n=1 endpoint; Da<N; Eisenstein/discriminant; integer curve points and bit bounds; rational annihilator span proof and explicit trace-dual basis.'),
('G-10','targeted proof check','PASS complete root reading: projective rational-image degree including base components, Chardin prime/EGR hypothesis and all-degree bound, linear normalization lower bound, exact strict threshold and highest-weight inheritance.'),
('G-B11','used and rechecked in this run','Chardin1989 primary PDF and screenshot printed p306 inspected: central unnumbered all-degree theorem H_I(nu)<=degree(I) binom(nu+D,D), EGR homogeneous ideal; prime characteristic-zero case applies.'),
('G-B12','used and rechecked in this run','Sombra1997 author preprint section1 p5 and Proposition2.10 pp11–12 inspected. The cited displayed proposition is for everywhere regular maps; G10 proves its needed rational-map base-locus adaptation.'),
('G-B13','used and rechecked in this run','Derksen2001 primary author PDF Theorem1.1, Proposition1.2 and Example2.1 printed p956 inspected; q=4 yields beta=6 binom(n+3,3)n^30.'),
('G-B14','used and rechecked in this run','Losev2006 complete three-page primary preprint inspected; Theorem4 p1 is the Kempf–Ness closed-orbit criterion; p2 proof read. Used for concrete moment-map zero witnesses.'),
('G-B15','used and rechecked in this run','Mukai2003 primary book copy inspected at Theorem5.9 and Proposition5.10 pp164–165, Definition5.12 p165, Proposition5.15 and Theorem5.16 p166, Corollary5.17 p167; exactness, quotient surjectivity, stable open locus and orbit fibers checked.')]
p=R/'integration_02_check_events.tsv'
assert not p.exists()
with p.open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['statement_id','date','who','type','outcome'])
 for i,t,o in rows:w.writerow([i,now,who,t,o])
with (R/'sources.md').open('a') as f:f.write('''

## G-B11 — All-degree Hilbert upper bound

Chardin, M. (1989). Une majoration de la fonction de Hilbert et ses conséquences pour l’interpolation algébrique. *Bulletin de la Société Mathématique de France, 117*(3), 305–318. https://doi.org/10.24033/bsmf.2124

Primary PDF: https://www.numdam.org/article/BSMF_1989__117_3_305_0.pdf . Exact locator: central unnumbered theorem on printed p.306, with its definition of EGR and projective dimension D; proof continues on pp.307–310. The displayed all-degree bound was read and visually checked. G10/G11 apply it to reduced irreducible characteristic-zero projective varieties, without a Cohen–Macaulay hypothesis.

## G-B12 — Degree of an algebraic image

Sombra, M. (1997). Bounds for the Hilbert function of polynomial ideals and for the degrees in the Nullstellensatz. *Journal of Pure and Applied Algebra, 117–118*, 565–599. https://doi.org/10.1016/S0022-4049(97)00028-5

Primary author preprint: https://www.maia.ub.edu/~sombra/publications/hilbert/hilbert5.pdf . Exact locators in that preprint: §1, p.5, projective Bézout bounds on the sum of degrees of components; Proposition2.10, pp.11–12, degree bound for an everywhere regular polynomial map. G10 explicitly proves the rational-map version it needs, accounting for the base locus. No rational-map statement is attributed verbatim to Proposition2.10.

## G-B13 — Degree bounds for invariant generators

Derksen, H. (2001). Polynomial bounds for rings of invariants. *Proceedings of the American Mathematical Society, 129*(4), 955–963. https://doi.org/10.1090/S0002-9939-00-05698-7

Primary author copy: https://bpb-us-e1.wpmucdn.com/sites.northeastern.edu/dist/7/497/files/2020/12/A.I.a.7.pdf . Exact locators: Theorem1.1, Proposition1.2, and Example2.1, printed p.956. Example2.1 gives the symmetric-power generator-degree estimate used for quaternary forms. The Veronese generation bound and ensuing orbit-closure comparison in G11 are proved separately.

## G-B14 — Closed orbits from the moment map

Losev, I. V. (2006). *The Kempf–Ness theorem and invariant theory* [Preprint]. arXiv:math/0605756. https://arxiv.org/abs/math/0605756

Exact locator: Theorem4, p.1, with proof on p.2. The paper states that the general results are established background and gives proofs. The original source it cites is Kempf, G., & Ness, L. (1979), “The length of vectors in representation spaces,” *Lecture Notes in Mathematics, 732*, 233–243. The locator actually inspected and used here is Losev Theorem4; no separate inspection of the 1979 original is claimed.

## G-B15 — Stable affine quotient dimensions

Mukai, S. (2003). *An introduction to invariants and moduli* (W. M. Oxbury, Trans.; Cambridge Studies in Advanced Mathematics, Vol.81). Cambridge University Press.

Primary book copy inspected: https://www.math.ens.psl.eu/~benoist/refs/Mukai.pdf . Exact locators: Theorem5.9 (affine quotient surjectivity), Proposition5.10 and its proof (invariant closed subsets and exactness), printed pp.164–165; Definition5.12 (closed orbit and finite stabilizer), p.165; Proposition5.15 (open stable locus) and Theorem5.16 (separation), p.166; Corollary5.17 (geometric stable quotient), p.167. G11 supplies explicit stable points before applying the fiber-dimension deduction.
''')
p=R/'grothendieck.tex';s=p.read_text()
marker='\\subsection{What the manuscript record does and does not establish}'
assert marker in s
new=r'''
\subsection{Further rectangular, rank-profile, and arithmetic consequences}

\paragraph{R-16. Several normal directions on one deformation.}
The cyclic pencil lies on the coefficient affine scheme; disjoint row-pair modifications define one morphism from the affine line into that parameter scheme. The exact permanent identities produce polynomial sections of its differential-image sheaf away from zero. Their special-fiber classes are separated by characters of the finite diagonalizable group of $m$th roots of unity after adjoining $\zeta$ and inverting $m$. Dual Jacobi--Trudi is the Schur operation in D-S6, equivalently the exact cote~133 symmetric/exterior dictionary. A nonzero maximal minor makes the normal directions independent on a principal open. D-FGA and D-S3 therefore carry the dimension and padding proof; the characteristic-zero conclusion does not assert uniform good reduction at every prime.

\paragraph{G-10. Projective degree controls the first forced Hilbert gap.}
The pencil map induces a rational morphism of projective coefficient schemes. Pullback of general hyperplanes and the degree of their intersections bound the image degree, including components of the base locus. Chardin's bound then compares the graded dimensions with a polynomial subalgebra supplied by linear Noether normalization. These are D-FGA's projective, graded-module and Hilbert frameworks, with associated sheaves as in EGA~II, Proposition~2.5.2. The explicit bound is geometric effectivity; no small-size representation of every graded module is inferred.

\paragraph{G-11. Rectangular classes in a reductive quotient.}
Restriction from $\mathrm{GL}_4$ to $\mathrm{SL}_4$ sends precisely the determinant characters among polynomial irreducibles to the tensor unit. In D-S3 and D-S6, the degree-$d$ invariant module is therefore the rectangular multiplicity space. Explicit moment-map witnesses establish a nonempty stable open locus over $\mathbb C$; its quotient has dimension reduced by $15$, by the fiber-dimension statement already located in D-S3. The invariant rings are quotients because the group is linearly reductive in characteristic zero. The explicit Veronese is a standard graded coordinate algebra, so D-FGA applies again to its Proj, degree and Hilbert function. The analytic compact-group witness proves the stated characteristic-zero fact; it is not asserted to define a positive integral motive or to make reductive invariants exact over $\mathbb Z$.

\paragraph{G-12. A cocharacter degeneration and its invariant ideal.}
The homomorphism $t\mapsto\operatorname{diag}(t^3,t^{-1},t^{-1},t^{-1})$ is an integral cocharacter of $\mathrm{SL}_{4,\mathbb Z}$, as in D-S3. Its weight filtration extends the padded form over the affine line whenever $3(n-m)\geq m$. Strict inequality gives the zero special fiber; equality gives a ternary residual form with its padding factor. The ternary determinantal containment of G-05 then implies containment of invariant ideals in characteristic zero. In D-FGA this is the specialization of a morphism and the inclusion of its ideal of functions; in D-S6 it selects the determinant-character summands. It excludes precisely the specified rectangular sector.

\paragraph{I-21. Rank strata over local Artin bases.}
Every interval coefficient product is a map of free modules. The proof works over finite local Artin rings and requires a unit maximal minor, so the rank-two image and its complement split on the corresponding determinantal chart. Projection growth and its last-zero reset control the necessary coefficient supports. The two selector stages pull these finitely many rank conditions back to one nonempty open parameter locus. D-FGA supplies the determinantal and Grassmannian language, while D-S3 translates the coefficient supports to character gradings. This gives the explicit unknown-order width-three morphism; it does not assume that an arbitrary rank stratum over a nonreduced base splits without a unit minor.

\paragraph{P-12. A finite flat arithmetic evaluation and its trace dual.}
The algebra $\mathbb Z[T]/(T^N-2)$ is finite free of rank $N$. After inverting its discriminant it is finite \emph{\'etale}; over $\mathbb Q$ it is a field by Eisenstein. The integral coordinate polynomials $A_i$ define the evaluation morphism. Their bounded-degree pullback is injective on the specified ROABP class by I-21 and the explicit monomial encoding. The dual basis for the trace pairing extracts all rational coefficient rows, giving an actual span-preserving arithmetic realization. D-FGA describes the affine finite morphism and its kernel, D-S3 the coefficient lattice, and D-ET the finite \emph{\'etale} cover. Frobenius distribution and additional purity bounds are unnecessary for this construction.

'''
s=s.replace(marker,new+marker).replace('The integral controls G-01--G-09','The integral controls G-01--G-12')
p.write_text(s)
print(now)
