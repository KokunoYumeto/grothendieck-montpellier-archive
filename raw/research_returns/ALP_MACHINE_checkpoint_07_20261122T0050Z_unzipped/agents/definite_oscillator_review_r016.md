# Independent whole-proof review of AM-R-016

Reviewer: GPT-6 Astra Pro, ALP_MACHINE `/root/definite_oscillator`.
Inherited reasoning effort is not separately exposed. Completed
22 November 2026 UTC, after the author's whole rereading and the
explicit rank-zero `Pos`/`FJd` clarification.

**Verdict: PASS in the stated genuine analytic interpretation.**
I read the whole proof in `work/research/last_two_free_data_seesaws.md`
and checked its relevant recovered source declarations. The result
proves the final two free-data implications and therefore all indices
of that predicate when `m=2`. It does not identify the freely chosen
Schwartz input with a raw arithmetic row or furnish the complete D7
constructor.

## 1. Spaces and character labels

At indices `m-2,m-1,m`, the vertical spaces are respectively
`A plus (-L)`, `B`, and the codimension-one positive subspace H
of C. This agrees exactly with R014's dimensions and signs.
The three groups actually integrated in the seesaw identities,
`U(A)`, `U(B)`, and `U(H)`, are definite and have compact
automorphic quotients.

Since `m-2` is even and `m-1` is odd, the source `car`
inserts `eta^(-1)` on the first member of the penultimate
pair and the second member of the terminal pair. Thus the
two oriented pairs have characters

- `(mu eta^(-1),mu)` on `(A plus (-L),B)`;
- `(mu,mu eta^(-1))` on `(B,H)`.

The required auxiliary pair is `(B,-L)`, with the opposite
character `eta^(-1)`. Its character attached to B does not
affect the kernel at the identity of `U(-L)`. The standard
character-change formula therefore gives the same auxiliary
kernel space on both edges, even if the two characters mu
are different.

The target factorization uses
`(mu eta^(-1)) eta = mu`, while the source factorization
uses `mu eta^(-1)`. These are the character products in
the actual tensor rules. No character is attached to the
wrong member of the dual pair.

## 2. Conjugation and adjoint checks

Negating the target Hermitian form negates the symplectic
form. Complex conjugation changes the additive character to
its inverse, and inverts both splitting characters. This is
exactly `weil_conjTarget`, including its `splitFacO_inv`
calculation. It gives (R16.6).

For the adjoint exchange, write `z=tr(Y^* X)`. The exchanged
trace is `bar z`, and `bar xi=-xi`; hence the symplectic
form changes sign. The group actions exchange because
`(h X g^(-1))^*=g X^* h^(-1)`. After complex conjugation,
the character labels are exchanged, with no further
inversion. On determinant roots the scalar becomes
`alpha(y)^(-1) beta(x)`, the conjugate of the original
`beta(x)^(-1) alpha(y)`. The recovered adjoint-exchange
statement explicitly has characters `(chiT,chiS)`, which
confirms (R16.7).

I also checked the odd vacuum weights. If eta has half-angular
weight h, the auxiliary `(B,-L)` source vacuum has weight
`1/2+h`; the unbarred `(B,L)` and `(-L,B)` kernels have
weight `-1/2-h`. In the terminal tensor product these cancel
the change from rank c to rank c-1 and the inserted eta.
In the penultimate product they change the target vacuum
from the contribution a/2 to `(a-1)/2`, with the same
inserted eta. Thus the finite determinant-root check agrees
with the actual odd archimedean baseline.

With the polarizations and self-dual measures transported
as in the note, these are exact theta-distribution identities.
There is no discarded nonzero scalar. The rational sum is
carried bijectively by the rational adjoint map, and its
complex conjugate is exactly the conjugate theta sum.

## 3. Periods and compact Fubini

The source's rank-zero `per_zero` formula contains the
conjugate of `om(g,1) Phi0` evaluated at zero. Here Phi0 is
in the theta-function model; the value is the full auxiliary
theta kernel, not the value of an unevolved Schrödinger
test function. This matches (R16.5).

The `bB` declaration first conjugates the horizontal form,
then inserts it into the Hermitian first slot. Its resulting
integrand is bilinear in the displayed horizontal form and
the vertical form. Consequently both lower periods have
the `phi*F` convention of (R16.8) and (R16.12).

The orthogonal target decomposition gives (R16.9), and
integrating in B and H in either order proves (R16.10).
The orthogonal source decomposition gives (R16.11), and
integrating in A and B proves (R16.13). The same Haar
measures occur on both sides. The rank-zero unipotent
quotient is a singleton of volume one by the source's
normalization, so no hidden unipotent volume remains.

Only the compact restriction of the downward lift to
`U(A)` is integrated in the second identity. No premature
cuspidality or rapid-decay assertion on `U(A plus (-L))`
is required for that Fubini step. Its cusp membership for
selected data is subsequently supplied by the checked
R014/R015 lower-tower argument.

## 4. Free data, pure tensors, and literal quantifiers

At fixed finite support and level, theta sums on compact
automorphic charts are controlled uniformly by a Schwartz
seminorm and an absolutely summable lattice majorant.
Thus the displayed integrated periods are continuous
linear functionals in the Schwartz input. Finite-place
functions on a direct sum are finite sums of products.
At real places the polynomial-Gaussian Hermite functions
span a dense subspace in the Schwartz topology and are
finite under the compatible maximal compact groups.

One can verify that density without any representation
irreducibility assumption: apply powers of the positive
harmonic oscillator to a Schwartz function, use its
Hermite eigenvalues to obtain arbitrarily rapid decay
of the coefficients, and use the usual creation/annihilation
operators to control every polynomial-times-derivative
seminorm of the tail. Hence the Hermite expansion converges
in all Schwartz seminorms. The oscillator eigenspaces are
finite-dimensional and stable under the compatible compact
unitary action, proving the compact-finiteness used here.

The terminal step may replace the original horizontal
Schwartz input by a pure product where the same integrated
functional is nonzero. This is allowed by the literal
predicate: its conclusion requires a lower datum for the
same horizontal source form and the same upper vertical
form, not the recovery of the original horizontal kernel.
Nonvanishing on a dense finite-sum span implies nonvanishing
on one pure summand, so the required lower datum is itself
factorizable and compact-finite.

At the penultimate step the original horizontal input is
retained. Density is applied only to the auxiliary datum.
Conjugate-adjoint transport preserves pure tensors and
compact-finiteness. The tensor is finite under
`K_(A plus (-L))=U(A) times U(1)` and under the diagonal
`U(B)`, since a tensor product of two finite-dimensional
compact modules is finite-dimensional.

The added `Pos` clarification is necessary and sufficient:
at the identity B-to-B embedding the genuine rank-zero
position is the empty flag on a zero complement, and
`FJd` is the full Schwartz space of the fixed auxiliary
pair. Thus an arbitrary upper existential `PerNZ` is
exactly a nonzero (R16.5). At the lower codimension-one
step the complementary nonisotropic coordinate does
not appear in a rank-zero unipotent character, so the
period is the same ordinary restriction for each such
choice. I checked the clarification after it was saved.

For `m=2`, these are precisely the two indices `j<m`.
For larger m the proof says nothing about the earlier
positive-rank unfolding. It also gives no effective
bound on the selected finite level, coefficient height,
or norm. These restrictions are correctly retained.

## Source declarations directly read

All locators are in the recovered commit
`7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`.

- `Formalism/SharpRestriction/CuspSpanNormBounds/CayleySignature.lean`,
  `car`, `bB`, `PerNZ`, and the complete
  `ThetaUnfoldingFreeData` quantifiers, lines114–175.
- `Development/AbelianVarietyTheory/Proofs/TwistedOperators/LastSeesawPeriodNonvanishing.lean`,
  `per_zero`, lines58–94.
- `Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/WittSmallGroupEmbeddingMemPointwiseStabilizerIso.lean`,
  `fjSrcFun`, lines228–233.
- `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/IsWeilDatumConjNegHermitianSpaces.lean`,
  `splitFacO_inv`, `conjTarget_apply`, and the complete
  `weil_conjTarget` proof.
- The same directory,
  `ConjWeilDatumViaAdjointExchangedPairStatement.lean`,
  the complete exchanged-character statement;
  `ThetaTensorRuleOrthogonalSumSourceStatement.lean`,
  the complete source rule; and
  `ThetaTensorRuleTargetOrthogonalSum.lean`,
  `tensorTarget` and its character-product transport.

This review checks the cited mathematical realization and
source conventions. It does not claim that the entire
import graph was built or that every published/source
input was reproved in this review.

