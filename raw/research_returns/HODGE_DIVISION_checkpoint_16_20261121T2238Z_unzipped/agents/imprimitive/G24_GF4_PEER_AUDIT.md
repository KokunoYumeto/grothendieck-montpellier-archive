# Independent whole-proof audit of G24 and the F4 extension

Run HODGE_DIVISION; 2026-11-21, approximately 11:48–11:57 UTC.
Reader: `/root/imprimitive`, GPT-6 Astra Pro, effort inherited/not exposed.

**Outcome: PASS for the complete mathematical proofs in the current
`g24/g24_section.tex` and `gf4/gf4_section.tex`, with the finite group
enumerations and full parabolic matrices taken from their exact reconstruction
certificates, whose independent reruns are owned by the root agent.** This is
a mathematical proof check, not a proof-assistant formalization. The separate
small-matrix certificate `audit_g24_gf4_integral.py` does not import any sibling
implementation and independently verifies the integral field actions and the
other identities specified below.

## Integral source factors

For G24 I checked the positive form, reflection formula, irreducibility
argument from the connected root graph, character-field trace, Schur-index-one
realization, doubled tuple, genus 673, and the two Chevalley–Weil multiplicities
3. The primitive idempotent is the central pair projector followed by the
rank-one projector `(1-s1)/2`. The coefficient 3 in the central projector
means that `2|G|=672` is a valid clearing integer; one must not reuse the
even-dimensional denominator `|G|`. Rosati symmetry follows from the central
projector and the orthogonal involution projector commuting.

The integral operator `(1-s1)R1R2R3` preserves the selected abelian factor:
the right-hand group element preserves the central block, and the left-hand
projection sends that block into the one-copy factor. Its restriction is
tau on one complex root line and conjugate tau on the other. Thus it defines
an actual integral endomorphism on the abelian subvariety. No assertion that
the entire displayed representation lattice is the homology lattice is used.
My independent exact arithmetic verifies the displayed product matrix, its
trace, all six root norms, and `<v1,g0 v1>=tau`.

For GF4 the order proof is valid without a classification premise. The
stabilizer of a coordinate short root is exactly B3, and the reflection
action is transitive on 24 short roots, yielding order 1152. The additional
involution normalizes root lines because Phi interchanges short roots and
long roots up to the stated factors. It is nonreal, so its coset is disjoint
from W and the extension has order 2304. My exact arithmetic independently
checks the length interchange for all 48 roots, the Hermitian involution,
the four displayed words for the simple reflections, and the field operator
`(1-s_e1)P12 z` acting as t on e1. It also checks trace `-t`.

The natural rank-four representation is absolutely irreducible already on
B4 and has character field Q(sqrt(-2)). The coefficient 4 in its central
projector makes `|G|e` integral. The field operator preserves the one-copy
factor by the same block-projection argument. Ten rank-one involutions and
two rank-two involutions give Chevalley–Weil `-4+(10+4)/2=3`, while their
inertia orders all equal two and give genus 4609. The distinction is handled
correctly.

For both groups the dual-lattice identity `Lambda_A^#=e Lambda` is correct:
the integral lattice intersection defining Lambda_A is primitive, any
integral functional on it extends to the unimodular ambient lattice, and
self-adjointness projects its representing vector. The clearing integer
therefore kills the polarization discriminant group. All six elementary
divisors divide that integer, proving the stated volume divisibilities.

## Parabolic matrices, period rank, and actual polarization

The cocycle relation and coboundaries have the required dimensions. GF4
correctly uses a fourteen-dimensional coefficient space for its two
rank-two inertia elements. The same `u_i/2` term applies throughout the
negative eigenspace. The nine intervals are nested or disjoint, are distinct
stable partitions, and form a maximal boundary stratum of Mbar_(0,12).
Their monodromy products equal one because they are unions of doubled pairs.

I checked the interpretation of the reported exact matrices and all principal
minor tables. Nonnegative principal minors certify each Hermitian matrix is
positive semidefinite; the strictly positive leading minors of their sums
make every positive weighted sum positive definite. Thus the logarithm sum
has K-rank three for all positive return powers. The stated determinant
norms are independently checked: 87808 for G24, and 32768/27 for GF4.

The geometric/logarithmic argument is the same full proof audited earlier
for G34, with rank three replacing four. Finite marking and Kummer covers
give one common orientation sign and positive integer multiples of the
algebraic logarithms. On the diagonal degeneration, the weight-zero graded
piece has type (0,0), so the limiting Hodge plane is transverse to the common
image I. The nine blocks then identify with nine independent complex tangent
vectors. Holomorphic extension of the untwisted period map makes the actual
interior derivative tend to those vectors; its determinant is nonzero nearby.
This proves period rank nine, rather than merely a boundary parameter count.

Splitness uses the genuine polarized logarithm: its square is zero and it
is skew-adjoint, hence its image is isotropic. The K-rank-three image is
maximal. There is no need to identify the auxiliary algebraic form S with
the actual cup product.

## Suppliers, quantitative extraction, and target lattices

I reread the cited supplied HECKE_DIV proofs SQ3–SQ6, in addition to the
previous whole-proof audit of the Schoen repair and Brauer transfer. The
only required branch feature is inertia of order two. Rank-two involutions
therefore introduce no new supplier problem. The primitive branch exponents
are m/2 and occur in pairs, or the cover is etale. The repair treats both the
original center and the exceptional divisor. All primitive determinant
embeddings are supplied, and the disconnected orthogonal parity coordinates
are retained in the character group.

The integer-lattice path-and-Cramer bound for coefficient mass is independent
of the selected representation dimension. The orbit-sum integral supplier
bound and its product bound are likewise unchanged. Retaining the supplier
on curve powers means that the contracting divisor degree is `ell/2+3` for
a sixfold. The binomial coefficient is consequently `binom(c,3)` and the
last intersection is `int_A theta_A^6`. This is exactly the adaptation made
in both new sections.

In the original SQ6 nef estimate one uses `g(C)-1 <= 4|G|`. Here the stronger
equality `g(C)-1=2|G|` holds. Hence the displayed `5|G|` bound for a pulled-back
theta divisor on each quotient curve and the resulting `40|G|` bound remain
valid. The argument extracts an effective integral cycle from a finite
spanning collection; it correctly requires no control of the scalar
coefficients in a complex divisor-polynomial presentation.

I checked the new target Hermitian normalizations directly. For tau²+tau+2=0,
`h(x,y)=E(x,tau y)-bar(tau)E(x,y)` is conjugate-linear first and linear second,
is integral over O_K, and its tau coefficient is E. For t²=-2,
`h(x,y)=E(x,ty)+tE(x,y)` has the analogous properties. In an O_K basis each
satisfies `det E=(det h)^2`; signature (3,3) gives `det h=-Delta`.

The Euclidean estimates 11/16 and 3/4 prove the needed PID property. A
primitive isotropic submodule is a direct summand. In a basis with Gram
matrix `[0 B; B* D]`, the substitutions `X=(B*)^{-1}D/2`, `w'=w-vX`,
`u=w'B^{-1}` give the standard hyperbolic form. Their forward and inverse
denominators divide `2Delta`: `det B=b` has norm Delta, and the combined
off-diagonal denominator is `2b bar(b)`. Combining source and target gives
the stated clearing integer `4Delta_A Delta`. The polarization pullback is
its square, and the three-cycle degree multiplier is its sixth power.

The analytic-open image is Zariski dense in the target component. The
accepted bounded-cycle closedness theorem then extends the unchanged bound
to the whole component. The nonmaximal-order lattice
`f O_K Lambda` lies between `f Lambda` and Lambda, has index at most f^12,
and changes the pulled-back polarization volume by exactly that index.
Projection formula preserves the pushed cycle degree. The final conductor
dependence and restriction to split determinant are correct.

## Scope of this check

The new proofs are checked conditional on their explicitly cited published
inputs (Riemann existence, Chevalley–Weil, the geometric braid comparison,
Schmid, Schoen with the written repair, and Milne's invariant theorem) and
the accepted bounded-cycle theorem. I did not independently reprove those
deep theorems. The exact group enumeration and the full quotient-cocycle
matrices have separate reconstruction certificates and root reruns; my
small-matrix script is not presented as a second enumeration of them.
