# Whole-proof audit of SF-E801--E804

Run HODGE_DIVISION; 2026-11-21; reader `/root/imprimitive`,
GPT-6 Astra Pro, effort inherited/not exposed.

**PASS for SF-E801--E804 as read before the addition of E805.** This is
a mathematical whole-proof check. It does not claim an independent rerun
of the sibling's exterior-algebra script, and it does not claim a new
eightfold construction.

## Intrinsic kernel calculations

The Fock identification has the correct total degree: starting from a
holomorphic four-form, contraction lowers the holomorphic degree and
exterior multiplication raises the antiholomorphic degree, so a diagonal
character corresponds to exterior degree four in the eight-dimensional
HH1 space. Degree-two cap product therefore becomes the stated wedge map.

For a sum of two transverse volume forms, the two pure bivector summands
map injectively into different bidegrees; the mixed sixteen-dimensional
summand is exactly the kernel. Wedge multiplication by all mixed
bivectors kills only the two extreme components of a four-vector. The
tensor-product injectivity argument for intermediate bidegrees is valid
and does not allow cancellation between those bidegrees.

For the product of two nondegenerate two-vectors, the pure kernels have
dimension five each and the mixed map is an isomorphism of sixteen-
dimensional spaces. Thus the rank is eighteen. If a kernel vector is
the sum of two nonzero pure parts, its square has the nonzero mixed
tensor component twice their tensor product, so it is not decomposable.
Each pure kernel is a hyperplane orthogonal to a nonisotropic vector
in the nondegenerate six-dimensional exterior-square quadratic space.
Its Plucker quadric is therefore a smooth irreducible quadric threefold.
These are precisely the two connected components of the projective
decomposable locus. Every vector of each four-space lies in a Lagrangian
two-plane, so taking the span of the represented planes recovers that
four-space. The unordered pair is intrinsic.

## SF-E802

The rational imaginary-secant coefficients are both nonzero: a rational
number cannot cancel a nonzero purely imaginary one. The ample form
makes the two exponential supports transverse. The CY4 adjunction
turns injectivity of the full degree-two trace into surjectivity of
evaluation, so the trace image equals the twelve-dimensional character
contraction image. The Atiyah class of a direct sum is block diagonal;
off-diagonal Ext2 has zero trace and diagonal images must be independent.

The bivector wedge pairing is symmetric. Consequently the character-image
inclusion for a summand gives the reversed kernel inclusion needed for
the common-annihilator lemma. A summand character must lie in the same
secant plane; its rank and its degree-two component force its two
coordinates in the rational secant basis to be rational. Every nonzero
such character has contraction rank twelve, so two nonzero characters
cannot coexist in independent trace images. The coherent-sheaf
indecomposability consequence uses the nonzero effective leading support
cycle and is valid.

I read the supplied DEG_L S-21 statement and the relevant complete
identity-sector, invariant Serre-pairing and evaluation/trace argument.
Its hypotheses are retained in the equivariant version. I do not
independently reprove all of its cited categorical inputs here.

## SF-E803

On a surface the point ideal has self-Ext dimensions (1,4,1): the Euler
pairing is -2, simplicity gives one in degree zero, and Serre duality
gives one in degree two. Rank and point contraction give independent
two-dimensional pieces of the degree-one trace. Thus all needed factor
traces are injective. Kunneth puts the three product Ext2 summands in
distinct Hochschild bidegrees, giving dimensions 1+16+1=18 and no possible
cross cancellation. The product is simple, gluable, and has Euler pairing4.

Its two intrinsic four-spaces are the Lie algebras of the two surface
translation--tensor groups. For a derived equivalence, the induced HH1
map is the differential of the corresponding isomorphism of abelian
translation--tensor groups, and cap-product naturality transports the
kernel. I opened Orlov's primary author manuscript at
<https://homepage.mi-ras.ru/~orlov/papers/abelnew.pdf>, checked Theorem2.10
on page9 and Corollary2.13 on page12, and read the corollary proof.
Browser references: `turn305439632view0`, `turn633042038view0`,
`turn633042038view1`. This event is a statement/scope and corollary-proof
check, not a claim to have independently reproved the whole Orlov theorem.

For an isogeny f:Y->X, the pullback transport on HH1 is the differential
of the rational isogeny `(f^-1,hat f)`; pushforward is its inverse on
rational cohomology times a nonzero degree. A rational algebraic B-field
is a rational homomorphism shear. Clearing denominators preserves the
property that a subspace is an abelian-subvariety tangent space. Scalar
characters and shifts preserve the kernel as well.

For the genuine RM character, the same kernel recovery instead gives
the two real-field eigenspaces on the Lie algebra of Y times its dual.
The eigenvalues are real, so the underlying real tangent spaces remain
eigenspaces for the rational endomorphism. A positive-dimensional
abelian subgroup would contribute a nonzero rational homology vector
there. A rational matrix cannot have a nonzero rational eigenvector for
an irrational eigenvalue: one nonzero rational coordinate already
contradicts this. The argument is therefore a rational subgroup
obstruction, not an inference from a merely complex splitting.

## SF-E804

Twice applying left exact Hom to the finite heart filtrations bounds
End(E) by the sum of `m_i*m_j*dim Hom(F_i,F_j)`, hence by the sum of the
squared multiplicities under the stated orthogonality hypothesis.
Gluability and CY4 duality give `chi=2e0-2e1+e2`; the supplied secant
identities `e2=12` and `e1>=8` give exactly the claimed upper bound.
Euler bilinearity then contradicts the specified nonnegative mixed
pairings and diagonal pairings at least two. The conclusion is correctly
stated as a necessary obstruction, not an existence theorem.
