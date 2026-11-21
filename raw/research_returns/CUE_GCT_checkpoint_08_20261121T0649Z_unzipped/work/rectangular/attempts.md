# Rectangular and Haar approach ledger

Run CUE_GCT-20261121, agent `/root/rectangular_bridge`, 2026-11-21.

## A. Direct scalar CUE positivity

The finite moment is a rectangular GL dimension. Treating that dimension
as an individual rectangular Kronecker coefficient fails: R-03 gives
dimension 20 and a relevant coefficient zero. Next construction: retain
all spectral parameters and perform tensor-subgroup restriction (R-01).

## B. Apparent mismatch of rectangle positions

Initially the Bump–Gamburd rectangle occupied the outer Schur label,
while GCT puts two rectangles in the inner labels. Kronecker symmetry
resolves this exactly. R-01 uses `s_(d^n)(X Y)` and projects onto
`s_lambda(X) det(Y)^d`; it reaches every relevant rectangular coefficient.
This is genuine gate movement beyond an analogy of shapes.

## C. Swaps and tableaux

The exact unitary swap formula can be pulled back along the product
alphabet. Weyl coefficient extraction gives a finite alternating
tableau-marginal formula. The individual swap terms have poles and
mixed signs; no termwise positive rule results. Next construction:
orthogonal invariant projectors and their squared entries (R-02),
followed by explicit structured witnesses (R-07).

## D. Rains power splitting

Cycle-index plethysm needs a joint law of powers of one Haar matrix.
Independent Rains marginals give the wrong moment already on U(2):
the true value is 2 and the independent value is zero (R-04).
Next construction: retain the full wreath-product symmetrizer;
it gives an exact sum of squares but still factorial size.

## E. Weingarten and orbit boundary

Connected-stabilizer multiplicities and full determinant-orbit
multiplicities differ (R-03, S4 example); orbit and closure likewise
must be separated. R-05 goes directly to a covariance whose kernel
is the orbit-closure ideal, thereby resolving the boundary distinction
at the level of an exact finite-rank criterion.

## F. Removing signed integration

Gaussian orthogonality converts the covariance to a factorially
weighted coefficient Gram matrix. R-06 gives integral Schur-projector
matrices, explicit entry bounds, and a finite interpolation grid.
These certificates are exact but their displayed sizes are exponential
or factorial. The unresolved task is structural compression or explicit
nonzero-minor control, not nonnegativity of the matrix.

## G. Explicit left-right invariants

Centering the coefficients of a binary determinant pencil gives
highest-weight polynomials Q_j. Their products give a positive basis in
the stable two-row range. Factoring binary forms shows that these
witnesses, and indeed all two-row ambient highest-weight vectors,
survive on the determinant orbit closure (R-07). Thus two-row
multiplicity obstructions are rigorously excluded. The root develops
the next ternary and fixed-variable stages; those are not duplicated here.

## H. Exact ratios rather than an unspecified Molien integral

R-09 projects a two-sided CUE inverse-determinant ratio to obtain the
sum of squares of precisely the GCT rectangular coefficients, with
monotone length cutoffs. In the stable unitary dimension range,
Bump–Gamburd's ratios theorem evaluates the inner integral as one
fourfold tensor Molien denominator. This gives exact identities and
bounds, but not efficient evaluation of the remaining projection.

## I. Arithmetic hypotheses

No R result depends on RH, Dirichlet GRH, or Masullo's claim. Their
truth changes which analytic zero-statistic results are unconditional,
not the Schur-transform identities or rank sizes proved here.
CFKRS's arithmetic moment recipe still requires its own off-diagonal
estimates. No statement that RH logically cannot ever help is claimed;
the missing comparison or compression theorem is simply not supplied.

## J. Complete small-height and small-degree sectors

GCT IV's exact two-row generating function closes the height-two
rectangular gate, including the symmetric/exterior split (R-10).
Beauville's cubic-surface theorem, together with the elementary quadric
normal form, excludes four-row multiplicity obstructions for all
degree-at-most-three padded forms (R-11). These use established results
with their precise hypotheses; no general canonical-basis conjecture
is promoted to a theorem.

## K. Finite projection dominance and a genuine-padding dimension test

Exact permanent-pencil Jacobians prove quaternary dominance for per4
and per5 (R-12), then for every size through16 (R-13). The row/column
torus makes dominance impossible starting at17. Different exact DP,
Ryser derivative, and minor-elimination algorithms checked the saved
matrices. The quartic determinant divisor produces explicit infinite
multiplicity-deficit-one families. Factoring out a padding linear form
adds exactly three dimensions to a generic quaternary permanent image,
giving R-14's rigorous finite padded ranges and its general criterion.

## L. One chord fails; two chords cross the unpadded dimension gate

Single-chord searches on the cyclic pencil produced no rank increase.
Two interacting chords did. The proof does not infer this for all sizes
from those computations: R-15 exhibits an exact cofactor identity and a
partial-fraction obstruction modulo the entire base Jacobian space.
It proves a strict permanent/determinant projection dimension inequality
for every n>=4, and hence four-row multiplicity gaps in large degree.

## M. Simultaneous directions and actual growing padding

Adding separately achieved rank increments would have been invalid.
Fixed dense cores and several sparse chord patterns were explored only
to identify structure. The decisive construction uses disjoint row
pairs, so the local 2x3 cofactor factorization remains exact with all
blocks present. At roots of unity, the limiting new vectors separate
by bidegree and cyclic Fourier character. An initial endpoint-only
argument gave a weaker quadratic surplus; a three-consecutive-index
Toeplitz determinant, identified with a nonzero Schur specialization,
establishes every needed character. Vandermonde then proves simultaneous
quotient independence. R-16 gives c_m>=2m^2+2+h_m(m-3), crossing n=m+1
for every m>=12 and, with R-14, every m>=8. It also proves every fixed
padding ratio below sqrt(5)/2 eventually. The proof is uniform and
does not extrapolate the sparse-core numerical ranks.

## Current rectangular gate

The exact Haar/Gaussian and coefficient/minor bridges R-01–R-09 remain
valid for all labels. Known height-two rules and low-row determinant
survival remove several potential obstruction sectors. R-12–R-16 now
prove actual four-row multiplicity gaps, including an unbounded genuine
padding range; root's G-10 supplies a very large effective coordinate
degree threshold. General efficient positivity, polynomial-size witness
extraction, maximal permanent-projection rank, and a separation at
arbitrarily growing padding ratios remain separate gates.


## N. A second exact family improves the uniform range

The optional fully overlapping cyclic-band deformation would destroy the
2x3 row-support factorization. Before introducing that error, both exact
local permanent relations were examined. Changing p_a to ell_(a+1)
retains row disjointness and makes their two normal families independent.
For generic unrelated chord forms some isolated Fourier modes failed;
the specialized forms reduce the test to four binary cubics with a
character-independent evaluation determinant. A4x4 Toeplitz/Schur
determinant then gives two independent classes in every interior mode.
R-18 proves dimension>=3m^2-O(m) and fixed padding ratios below sqrt(3/2),
with the explicit rectangular labels and degree progression from G-11.
No overlapping-band rank formula or maximal generic-fiber assertion is
needed. R-17 separately records the exact determinant dimension and
concrete pairs where the proved four-row gaps must be nonrectangular.

## O. Row and column identities coexist in a three-row motif

Spacing centers by three allows the R-18 row pair and a transposed column pair to coexist with all other motifs. A third chord with diagonal factor ell_a gives four independent normal classes per interior mode. The crucial six-dimensional test reduces to four quintics divisible by two specified linear factors and two further quintics whose evaluation determinant at those roots is nonzero and independent of the character. R-19 therefore proves dimension>=(10/3)m^2-O(m), extending the explicit rectangular padding range to every fixed ratio below sqrt(5/3).

A naive extension by adjoining more complete 2x3 blocks is blocked by exact support constraints. For row pair R_i one needs p_i=q_i=1 and p_(i+1)=q_(i-1)=0; for column pair C_i one needs p_(i-1)=q_i=1 and p_(i-2)=q_(i+1)=0. Thus adding overlapping full pairs does not automatically retain the identities. The next b=4/5 attempt must establish a larger-block identity or control the extra terms. No asymptotic rank claim is inferred from a finite band-pattern computation.

## P. A larger staircase and a finite algebraic certificate close the rectangular sector

Simply adding more nearest-neighbor forward/backward chords leaves only four normal classes per Fourier character, even for larger blocks; arbitrary choices of the corresponding binary forms did not remove that limitation. A full staircase preserves a four-row support and a transposed four-column support inside one five-row motif. The signed determinant minors agree with permanent minors through first order; the second-order defect gives four row and four column families. Taking highest bidegrees for all-(z,w) chords lost a class at b5. Mixed (x,y)/(z,w) chord forms give all eight.

The uniform proof does not extrapolate those exploratory ranks. It gives an explicit twelve-chord motif and eight displayed degree-five forms. Each Fourier problem reduces to a fixed6x6 rational matrix. Two exact finite-field determinants16 and15 prove that their cleared product is a nonzero integer polynomial; its degree bounds control every sufficiently large root-of-unity specialization after choosing a primitive root. At most300 bidegrees and80 characters per good bidegree are lost. A coprime-factor intersection proves joint row/column independence, and ordinary Vandermonde systems recover all translated families despite the missing modes. The original polynomial limits are independent by descending highest bidegree, so all surplus ranks occur at one generic epsilon.

R-20 proves dimension>=(18/5)m^2-O(m) with the explicit threshold m>=8000001. The margin18/5>32/9 yields rectangular multiplicity gaps for every integer m<n<4m/3 above that threshold. G12 supplies the opposite exclusion at and above4m/3, making the eventual rectangular boundary exact within this sector. The same dimension bound also gives necessarily nonrectangular gaps in an asymptotic strip above4m/3. General efficient multiplicity positivity, maximal permanent projection dimension, and arbitrary growing padding ratios remain separate problems.

## Q. Return to the Gaussian arithmetic gate

The integer Gram model gives a quantitative spectral gap, but the gap can be exponentially small in matrix dimension even at entry height2. This explains why integrality alone does not make a direct spectral test uniformly efficient. For integer coefficients, absolute error below1/2 also allows exact entry rounding, so the finer spectral precision is sufficient for thresholding rather than necessary for exact recovery.

A useful compression works when ambient dimension is fixed. The bilinear kernel of the tensor orbit map can be expanded directly using the n! beta! symmetric-tensor normalization; its MxM coefficient Gram avoids N^D output rows. Weight-block ranks and the signed Weyl denominator compute each multiplicity in polynomial bit complexity in numerical nd at fixed N. This does not replace the entire permanent-pencil image by a single quaternary orbit, and the exponent grows with N. Alpoge note step13 names Bost's slope inequality but supplies no constants for these specific matrices; no unsupported transfer is made.

## R. Uniform typed staircases and the dimension ceiling

A nearest-neighbor extension left the normalized row and column spaces too small even when its binary factors varied. A row-star construction with weighted chord orders could isolate desired products on one side, but its transposed star required incompatible order inequalities on shared backward edges. These were obstructions to those constructions, not impossibility results for all motifs.

The successful arbitrary-b construction keeps the complete staircase support, assigns every additional forward edge an (x,y) form and every backward edge a (z,w) form, and examines the second-order permanent-minus-signed-determinant defect. Upper-Hessenberg matchings cancel. A column-multiset comparison forces every surviving top-degree pair, giving an explicit triangular sum for arbitrary block size.

An explicit row specialization reduces the normal quotient to diagonal root evaluations and one nonzero 2x2 coefficient. Transpose plus index reversal preserves the typed parameter domain and proves column nonvanishing. Joint independence then follows from the coprime common-factor intersection, not from adding separate row and column ranks.

The first plan selected a fixed motif before specializing q and would have required a phi(m) root-order bound and O(b^2) lost bidegrees. The stronger quantifier order fixes m,q first: the local proof works for each interior k, so a single finite integer grid avoids the product over all those k. The row/column determinants have joint Laurent width2b in the character variable, leaving at most2b bad characters per bidegree. This gives dimension4m^2-O(m^(3/2)) after choosing b proportional to sqrt(m), and every fixed padding ratio below sqrt2. The dimension upper bound shows sqrt2 is the asymptotic ceiling of this comparison method. Exact generic-fiber dimension, polynomial-time multiplicity evaluation, and superlinear padding remain unresolved by this argument.

## S. The exact generic-section homology gate

After R22 reached every fixed padding ratio below sqrt2, the next target was exact generic four-variable dimension. The primary ELSW paper does give the full-variable linear strand: at the permanent gradient ideal there are exactly2m−2 linear syzygies. The subpermanent ideal must not be confused with the apolar ideal, whose syzygies are studied in a different paper.

A generic linear restriction is not automatically exact on this resolution. R23 identifies the precise obstruction as the degree-m part of Tor1(R/J_m,S); it is exactly the deficit from4m^2−2m+2. The cyclic pencil proves that all gradient generators and all old torus relations remain independent generically, so lower-degree Tor1 does vanish. Existing complete dominance results force positive degree-m defects for m3..16, providing explicit counterexamples to unrestricted transfer within the same family.

The proposed full regular-sequence shortcut fails before any subtle computation: the singular-locus codimension is at least5, so depth(R/J_m) is less than the number m^2−4 of linear forms imposed. This does not rule out degree-specific Tor vanishing for m>=17. No suitable vanishing theorem has yet been established or imported. R23 records the exact needed statement and distinguishes it from both a full resolution theorem and a numerical rank conjecture.


## T. Exact size17 rank and a limitation of mixed disjoint motifs

The first size outside the dominant range attains the torus parameter bound: an explicit integer pencil has an1124x1124 evaluation-Jacobian minor88 modulo101. R24 records this finite equality, not an extrapolation. The determinant was checked by separate elimination recurrences, and all1317840 entries by a distinct Ryser implementation. A constructive induction remains the stronger next target.

Simply mixing disjoint R22 block sizes cannot improve its error order if each block uses the same full interior window. Let h blocks have sizes b_i and S=sum b_i<=m. Even granting perfect independence and no character losses, their surplus is at most sum(2b_i-2)(m-4b_i+3)=2mS-2mh-8 sum b_i^2+14S-6h. Cauchy and AM-GM give 2mh+8S^2/h>=8S sqrt(m), so the full rank obtainable from that accounting is at most2m^2+2+(2m-8sqrt(m)+14)S<=4m^2-8m^(3/2)+14m+2. This audits this specific full-window disjoint-block route; it is not a bound on arbitrary motifs, boundary modes, or overlapping/higher-order deformations.

## U. A bordered induction isolates a ternary rank problem

A naive block border yields only6m−1 off-diagonal directions after restriction to its new linear variable. Exact cancellations with upper-left variations produce2m additional Hessian-contraction columns at orderepsilon³. R25 proves that a ternary space generated by8m+3 columns, with one universal scaling relation, supplies the full8m+2 dimension increment. Dense m17 reaches that target and certifies maximal c18. This is not a uniform induction theorem.

Exploratory exact ranks localize the remaining problem. At cyclic ternary data, the first-column space P*E plus(Gv)*E plus(G^Tu)*E has ranks4m+5 at m11 and17; all2m Hessian columns survive independently. One step-two chord raises the first rank by4 at m11, a paired chord by5, and the full step-two band reaches6m+2. The same band gives full8m+2 at m17. Exact degree-bounded interpolation of the epsilon coefficient and kernel/cokernel elimination show the first-order normal map already has full dimension2m−3 at m11 and17. These finite tests motivate, but do not prove, a uniform signed-adjugate defect argument.

### Current uniform-border approaches (still unproved)

The cycle cofactor matrix is the transpose adjugate of the signed cycle matrix. This explains2m−3 extra first-column syzygies. Adding every step-two chord produces a diagonal first-order cofactor defect; exact finite kernel/cokernel calculations at m11 and17 show that this first-order map supplies all missing directions. A fully equivariant specialization under weights(0,1,0) has an ambient-character capacity obstruction; balanced weights(0,1,2) avoid it and reach full rank at m11. The one-path q-Vandermonde formula was derived algebraically and independently rederived by root. The direct two-arc Hessian formula has a polynomial-time coefficient evaluator, checked against728 DP entries at m11. A proposed common degree-five polynomial normalization for its Hessians failed the exact m41 coefficient test, so no such formula is claimed.

An alternative open Jacobi pencil has diagonal alpha_i*x, upper beta_i*y, lower gamma_i*z. At m11, even restricting u,v to their two endpoints preserves the full ternary criterion rank. This gives explicit path/continuant formulas and a second uniform route. The special endpoint monomials(u0,uL,v0,vL)=(x,y,x,z) give rank84 rather than90 at m11; the generic endpoint forms give90. These calculations remain route diagnostics, not a uniform dimension statement.

## V. Finite continuant cores give the uniform linear defect

The balanced-root Fourier route produced exact one-path identities, but the simplest shared polynomial normalization for the Hessians failed. The open Jacobi endpoint construction avoids those sums. Its monomial endpoints preserve a cyclic character grading. In every ordinary character, all long path products collapse after rational normalization to one outer-edge ratio K. Paired outer zero edges permit insertion of two isolated diagonal-x vertices with K unchanged; a central cut inserts one vertex in only the longer component. These are exact polynomial identities in the continuants, with valid limits from nonzero edges.

Seventeen finite cores cover all ordinary characters after these insertions. Different characters may use different cut limits: a finite intersection of their nonempty minor-open sets supplies one common generic Jacobi pencil. Root and author independently proved the exceptional character lower bounds6/7/7 using a single changed diagonal and coprime consecutive continuants. R26 therefore proves dimC>=8m-4 uniformly, not by extrapolating the finite ranks. The inherited border induction yields epsilon_m<=6(m-18), improving the previous O(m^(3/2)) defect to O(m) and bringing sufficient padding to within a constant ofsqrt2*m. The unresolved maximal-rank problem is now the possible removal of six lost directions per border step.


## W. A second-order endpoint repair closes the exact dimension gate

The monomial Jacobi base loses six directions from the maximal ternary criterion. Perturbing only its four endpoint forms initially looked like a first-order repair, but exact kernel/cokernel calculations showed first gain4 and corrected second gain2. The seven base relations lie in characters0,+1,-1. A complete boundary projection to characters0,±1,...,±5 has91 columns and base rank84; retaining every column in each block is essential.

A central-cut size17 computation gives Toeplitz ranks84,172,262. A naive use of these lower bounds at a limit is insufficient: two order-two pivots can change into orders one and three, destroying the claimed second-order continuation. The repaired proof derives a universal general-endpoint K11 identity. Its first derivative is in the base span, witnessed by explicit pure extreme monomials from the r2/r3 continuants and one nonzero Delta. Its transpose and scaling supply three independent first-order lifts, hence a generic upper bound4 for the first normal. This makes the Toeplitz lower bounds stable enough to recover two second normals.

The same finite boundary matrix propagates by inserting an isolated diagonal-x vertex at a central cut. On retained central, positive extreme, and negative extreme rows the normalized coefficient maps are multiplication byx,y,z respectively. Short and long branches can overlap in discarded intermediate weights, but not in the retained windows; this distinction removes the initially overly strong separation condition at size17. Negative long paths are divided by the entire lower-edge product before taking cut limits. Complete-character support confines first corrections to±3 and second corrected images to±5, so the projected gains are gains modulo all full base columns.

Thus R27 proves dimC=8m+2 for everym>=17 and the exact four-variable dimension formula by R25/R24. The former Tor vanishing gate is closed; full regular-sequence exactness remains false, and exact multiplicity algorithms or superlinear padding conclusions do not follow from this dimension theorem.


## X. Higher rows: the scalar period needs a common irreducible family

G21's variable-extension dimension suggests higher-row quotient comparisons, but finite projective stabilizers and scalar-orbit periods are separate requirements. The ordered Fourier-frame tensor gives the stable common product point in G22; its polynomial product can still have permutations of its factors. A first route used generic unordered point configurations, with an a1 case reducible to Gale-dual configurations on P1. That route is unnecessary.

The simpler common family is q=prod L_j+epsilon h^m, represented by a diagonal-plus-cycle matrix for both determinant and permanent after a single cycle-sign change. It contains the stable product point at epsilon0. The explicit monomial-plus-power specialization x1...x_(r−1)xr^(m−r+1)+epsilon(Σxi)^m is irreducible by Eisenstein after replacing xr by the sum coordinate, and has finite projective stabilizer by pure-power coefficient comparison followed by independent off-diagonal root monomials. Stable, irreducible and finite-stabilizer conditions are separate nonempty opens on one irreducible parameter space, so they coexist. A generic padding line then removes all remaining projective automorphisms because the nonlinear irreducible factor is distinguishable even when the padding exponent is1.

This proves the all-integer invariant-degree property throughr=m andr3, while exact determinant image dimensions extend through unused-variable cofactor blocks. The strict first-row condition is retained: equality can retain an(r−1)-variable multiplicity problem, so the four-row excluded-boundary assertion must not be transferred automatically. Root is developing the separate exact phase and rectangular-boundary arguments.


## Y. Beyond m rows: normalize products before taking an orthogonal sum

A product of m linear forms is concise in at most m variables, and its stabilizer obstructs simply repeating the earlier full-spark construction above that range. The successful extension separates the desired moment matrix into two orthogonal blocks, each of dimension at most m-1. An ordered Fourier tensor gives a stable product-plus-flag point, but its polynomial product does not have an additive factor moment. Reverse Kempf–Ness followed by a unitary normalization of the auxiliary partial flag instead proves that a polynomial product itself can attain every positive rational spectrum in that block.

A weighted sum of two such unit products has the exact full moment matrix because its pure block spaces are orthogonal. For degree at least3 the two mixed bidegrees are distinct, so derivative conciseness forces both off-diagonal infinitesimal blocks to vanish; finite block stabilizers then make the entire projective stabilizer finite. Every-1PS minimum weights, not a product-moment identity, transfer stability through padding.

The shared determinant/permanent family must be enlarged to all sums of two products. In that irreducible parameter space the two-block point supplies stable and finite-stabilizer opens, while the three-variable Eisenstein polynomial x1^m+x2^(m-1)x3 supplies a separate irreducible open even when r>m. Their intersection and a generic padding line give a common no-scaling point. This proves the strict row extension to r<=2m-2 and its all-integer occurrence property, without an effective bit-complexity claim for the normalization or an assertion on the equality face.


## Z. The endpoint product torus can be handled through compact stabilizers

Extending the product moment lemma to exactly m variables does not make the complex stabilizer finite: a product of a basis always has a torus. A finite symmetrization map transfers closedness from the ordered cone and gives polystability, but it does not solve this separate problem. The successful endpoint argument uses a nonconstant spectrum. The Fourier basis and a proper standard auxiliary flag have only scalar common symmetries, because a circulant matrix preserving a proper consecutive interval is scalar. The normalized polynomial product then has finite UNITARY projective stabilizer: every unitary symmetry commutes with its moment matrix and preserves its flag.

A small rational two-eigenvalue tilt of the padding line produces a positive residual moment whose two exceptional eigenvalues can be put in separate blocks. Both blocks now have nonconstant spectra even at size m. Their weighted sum has finite compact stabilizer, and the full ordered padded tensor has zero moment. Only at this point is the cited compact-real-form stabilizer theorem used to deduce complex finiteness.

At r=2m the generic two-product q itself has an unavoidable torus, so the previous finite-q plus generic-padding argument cannot be reused. Explicit padded forms nevertheless have finite projective stabilizer. A generic nontrivial auxiliary flag removes that finite group. This completes all strict directions through2m rows. An independent padding variable can make the same family concise in2m+1 variables, so the endpoint theorem is not stated as a universal family ceiling. The direct rank-deficient moment continuation has a special nearrectangular degeneracy and is being treated separately.


## AA. The next row has an actual period obstruction for the unchanged family

Adding an independent padding variable makes a two-product form concise in2m+1 variables, so a simple factor-span count did not rule out the next row. A rank-deficient residual moment construction fails in the nearrectangular case: its positive spectrum has only one exceptional eigenvalue, leaving one orthogonal product block balanced and untouched by padding or flag.

The stronger R31 audit applies to the entire common two-product family. Generic factor coordinates put F into z^a(prod x_i+prod y_i). A transposition of x1,x2, compensated by their auxiliary-covector coefficients, fixes both F and that covector but has determinant minus one. Its SL normalization scales the enhanced tensor by(-1)^b. For oddm and the explicit strict direction s=2m+1,b=m, all odd-degree invariants vanish identically on this common subcone. Closed-orbit separation then precludes any stable no-scaling point anywhere in it.

This does not propagate vanishing to either full coordinate ring. It shows that the unchanged common-family period-one method is insufficient. Richer common pencils or separate stable points for the two cones may avoid it. Merely proving that a generic projected form has finite automorphism group would not supply the missing stability; a possible normal-slice route still requires explicit balanced weights and a valid local argument.


## AB. The unpadded comparison avoids a false period-one requirement below the face

The first-row equality reduction can lead to an unpadded tail whose largest part is not greater than its outer degree, so inserting another smaller padded permanent does not always supply a strict witness. R32 removes that detour. The R29 two-block products already prescribe the moment of a degree-d unpadded form through2d-2 variables and have finite complex projective stabilizer. This gives stable enhanced algebras for every positive full-row direction. A nontrivial auxiliary flag removes scalar periods; rectangular directions do not receive that conclusion.

For an algebra used only as an upper Hilbert bound, period one is unnecessary. Root G27 uses the gcd of its nonzero homogeneous generator degrees: each occurring residue embeds into a larger standard-Veronese degree by multiplication by a sufficiently large occurring multiple of that gcd. The upper comparison therefore remains valid for rectangular tails, while the determinant lower algebra uses R32's nonrectangular no-scaling point. This distinguishes stability, dimension, and scalar period rather than treating them as one condition.


## AC. A lower quotient upper bound needs generic finite stabilizers, not stability

G21's exact generic kernel is particularly useful away from the special stable witnesses. On the common open where a projected permanent pencil has maximal coefficient rank, a full-support coefficient matrix, and every Pluecker coordinate nonzero, its kernel consists precisely of the2m-2 row-column diagonal gauge variations. Any projective variable Lie symmetry, after subtracting a scalar, must therefore come from a diagonal operator preserving that generic coefficient subspace. All Pluecker coordinates force all subset weight sums equal, hence every coordinate weight equal; the zero permanent character makes that scalar zero.

This proves generic finite complex projective stabilizer for every4<=q<m^2. It does not prove a closed orbit or stable point. For a lower algebra needed only as an upper Hilbert bound, the dominant invariant quotient already suffices: its generic fiber contains a full-dimensional generic group orbit, giving the needed quotient-dimension upper bound. Root G28 combines this with a genuinely stable no-scaling determinant witness and treats lower quotient dimensions0/1 separately.
