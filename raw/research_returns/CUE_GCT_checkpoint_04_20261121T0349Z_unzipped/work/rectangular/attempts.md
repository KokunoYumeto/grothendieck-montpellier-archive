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

