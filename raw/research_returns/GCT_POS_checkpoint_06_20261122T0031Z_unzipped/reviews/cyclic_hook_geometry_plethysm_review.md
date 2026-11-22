# Whole-proof review of K-023, K-024 and R-NEW-004

Date: 2026-11-21. Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro;
effort not exposed; run GCT_POS.

**PASS for the complete chain.** Read all of
`CYCLIC_TRACE_HOOK_IDENTITY.tex`, `HOOK_CHAIN_POLE.tex`,
`branches/root/hook_chain_lie.tex`, and the entire inherited P-F30 proof in
the standalone plethysm paper. The latter's graph-support chain and
finite-lift dependencies were already whole-proof checked in this run.
Read and replayed `branches/root/verify_hook_chain_lie.py`; its exact ranks
over Q are n^2 for n=2 through8.

## The trace identity

Schur–Weyl identifies the rectangular invariant multiplicity with the
diagonal symmetric-group invariants in the tensor cube of the rational
rectangular Specht representation, compatibly with the three-cycle. The
trace of the three-cycle composed with A tensor-cubed is trace(A^3), which
gives the character average over pi^3. Cubing one cycle gives one cycle
unless its length is divisible by3, in which case it gives three cycles of
one-third the length. The resulting exponential equals the character of
Sym(W direct-sum S_(2,1)W) with weights1 and3, since
`s_(2,1)=(p1^3-p3)/3`. Rectangular Schur extraction and division of total
weight by n give precisely the asserted auxiliary Hilbert function.

The coordinate-dual convention is handled by the simultaneous
contragredient automorphism and does not change the invariant trace.
The rational C3 decomposition gives dimension minus trace equal to three
times a nonnegative integer. This proves the integral coefficient
congruence, including degree zero, without any reduction-of-invariants
assumption. The named general Scharf identity is attribution; the needed
specialization is proved in full in K-023 itself.

## The all-dimensional Lie calculation

Independently reconstructed R4-1. Differentiating the single letter in
`[e_i,[e_i,e_(i+1)]]` gives its first term; differentiating either repeated
letter diagonally gives the factor2; replacing a repeated letter by its
successor gives the minus sign in the reversed repeated multidegree.
No other contribution has that multidegree.

The descending diagonal recurrence kills every diagonal entry. The repeated
multidegrees then restrict every later column to its first superdiagonal
and the displayed exceptional second-superdiagonal entry. The distinct
multidegrees kill the remote first-column entries and remaining
superdiagonal entries. In multidegree123 the two exact coefficients are
`y2-2*x31` and `y2+x31`, so the determinant-three system kills both in
characteristic zero. Multidegree134 kills the sole final exception; n2
and n3 are separately covered. All entries vanish. The small-rank exact
matrix replay checks these conventions and is not used as extrapolation.

## Closed orbit, full stabilizer and complete fixed locus

The positive masses satisfy all diagonal moment equations. Distinct chain
weights differ by no root, and the linear and cubic summands are
orthogonal, so all off-diagonal moments vanish. The critical representative
therefore has closed SL orbit. Its coefficients are diagonally equivalent
to the coefficient-one representative because the n support columns have
nonzero determinant.

The diagonal generator has simple spectrum, determinant of exact order
M=2^(n-1), and diagonal centralizer of order M. Finite-group character
column orthogonality forces all linear characters to be determinant powers
and all nonlinear characters to have trace zero at this generator. The
dyadic cyclotomic basis makes zero trace equivalent to antipodal pairing.
There is only one such pair in W, so every nonlinear constituent lies in
the final two-plane. The determinant kernel fixes the complementary lines,
acts on the two-plane in SL2, and fixes e_n. Every finite-order matrix with
these properties is identity. Thus the entire GL stabilizer is cyclic and
determinant-faithful, including n2.

For an arbitrary nonzero grading-fixed quotient point, the closed-orbit
property supplies an exact fixing GL element. Its semisimple cyclic closure
has finite determinant image, since a positive-degree invariant does not
vanish. Splitting its character module and taking the two-primary part
gives the required finite two-power lift without imposing an artificial
bound on its order. Nonvanishing of an invariant implies the rational-span
condition on the supported weights. Replacing each supported linear weight
e_i by3e_i preserves that span and exact invariance for a two-power element.
The full P-F30 theorem therefore forces precisely the hook chain and final
linear coordinate. Every coefficient is nonzero and all such vectors are
in one GL orbit.

The complete g-fixed representation has dimension n. Explicitly, any
hypothetical additional fixed weight could be adjoined to the known chain
support; its rational span still contains the all-ones vector, contradicting
P-F30. The trivial effective SL stabilizer gives quotient smoothness and
the tangent exact sequence; subtracting the n-1 fixed Lie directions gives
one fixed quotient tangent direction. Positive grading and inertia exactly
mu_M give a one-orbit curve closure, origin as its only boundary, and
normalized density one.

## The pole and the essential no-collision condition

The residue product uses the actual multiplicity2 of distinct-letter hook
weights. Every numerator and denominator factor is a nonzero dyadic
cyclotomic difference. The geometric-sum identity makes each a unit in
Z[zeta,1/2], hence at every prime over3. The unique component therefore
gives a genuine simple pole with three-adic unit residue.

If d has two-part at least M and d is not M, any nonzero mu_d-fixed point
would lie on the same orbit, contradicting its exact inertia mu_M.
Its fixed scheme is consequently supported at the origin. The finite-length
Koszul argument excludes the corresponding actual poles. In particular
there are no M*3^r poles in the auxiliary Hilbert series for r>0. This is
precisely the extra condition needed by PNEW-013: a unit residue by itself
would not survive reduction in the presence of colliding higher lifts.

No gap was found. A short explanatory sentence for the complete fixed-weight
count was requested and incorporated by the author. No characteristic-three
smoothness, base change of invariant rings, or claim about the exact
primitive-M pole of the tensor series is used.

## Parameter-notation addendum

The root's new source check distinguishes the unified rank parameter
`rank(x)=n^2+5n` in GCT VI section3.4 from the introductory parameter
`h=dim G prime+height(lambda)+height(pi)=n^4+O(n)`. PNEW-013 now uses
these distinct symbols correctly. The exponential denominator lower bound
outgrows every polynomial in both parameters; no mathematical conclusion
changes. Earlier wording calling n^2+5n h is superseded by this addendum.
