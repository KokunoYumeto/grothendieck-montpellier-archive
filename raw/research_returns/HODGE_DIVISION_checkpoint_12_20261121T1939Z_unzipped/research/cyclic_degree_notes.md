> Historical unchecked draft, superseded by the fully checked HD-E8Q1–6 in research/e8_detector_degree.tex. Retained as work documentation.

# Quantitative branch-exponent transfer: active derivation

2026-11-21, root, GPT-6 Astra Pro, inherited effort not exposed.
This is a working derivation, not yet a checked theorem or an advertised bound.

## Fixed parameters

For the connected Gaussian E8 family, set G=1393459200 and
g=1+53G/24=3077222401. Let R=(2G+1)G!G^G, using the supplied
HECKE_DIV SQ3 integral Brauer coefficient-mass estimate, and L=2gR.
The total number of curve slots in the plus and conjugate-minus
Brauer determinant construction is at most L. A nonzero balanced
output determinant of rank6 has an even actual slot count.

Write H12(T) for the explicit Fermat-product Hodge-cycle spanning
bound being proved by sixfolds. All Fermat factors in the cyclic
supplier have total dimension at most L. The projective bundles
P(O^b plus O(-12)) have total dimension at most L as well.

Proposed safe constants:

    A = (4L)! [1000 g (G+1)(L+1)]^(4L)
    B = (4L+4) A^(2L+4)
    S = [26(L+1)]^L H12(L)
    D_source = (2G)^6 B^(4L+21) S.

Every expression is an integer. Before promotion, verify the exact
operation count and all projective-bundle multi-degree bounds.

## Cyclic incidence graph bound

Choose a very ample line bundle on the original curve C of degree6g.
For a cyclic intermediate C_i -> B_i, its faithful eigenspace rank
v_i is at most2g and equals deg K_Bi(D_i). On the source Y_i from
HD-FS1 use H_i=xi_i+x_i, where xi_i is the tautological pullback
from |K_Bi(D_i)| and x_i is the Fermat hyperplane. It is very ample:
Y_i=P(O^b plus O(-12)) and xi_i+x_i corresponds to the globally
generated positive summands O(1)^b plus O(13), which separate base
points and relative directions. This assertion needs a clean explicit
embedding proof or a standard projective-bundle very-ampleness citation.

The desired returning graph is an irreducible component of the finite
incidence scheme in C^v_i times Y_i where the section represented by
Y_i vanishes at the image in B_i of each of the v_i curve coordinates.
Each condition has line bundle pr_C^*q_i^*K_Bi(D_i) plus xi_i.
Its degree on its curve factor is at mostGv_i<=2Gg, so its numerical
class is bounded above by (G+1) times the total product polarization.
The incidence is finite flat over Y_i: a nonzero section on B_i has
a nonempty finite zero divisor, and the coordinates are independent.
Thus no excess-dimensional component enters this estimate.

For d_i=dimY_i and r_i the branch count, the bundle relation gives

    integral_Yi H_i^d_i
      =12 sum_(j=0)^(r_i-2) binom(d_i,j)12^(r_i-2-j)
      <=12*13^d_i.

For a product of such returning graphs with total curve slots l<=L
and total bundle dimension d<=L, the ambient product degree is at
most(2L)!(6g)^L12^L13^L. Intersecting all l incidence divisors
multiplies by at most(G+1)^L. Therefore every required graph has
degree at most(2L)![936g(G+1)]^L<A.

Unramified cyclic factors use projective spaces and satisfy the same
bound. Trivial Brauer characters use products of diagonals and point
classes on quotient-curve powers; pulling them to C gives components
of correspondences defined by equality in a quotient of degree<=G.
Their degrees are also below A. Spell this last bound out in final proof.

## Projective-bundle cycle bound

The full cohomology of a product Y is a direct sum of products of
xi_i^j_i with pullbacks from the corresponding product of Fermat
hypersurfaces. For a fixed monomial, use effective generic divisors
from the globally generated xi_i. Flat pullback and these intersections
preserve effectivity. Pushing powers of xi_i along the bundle uses
pi_*(xi_i^(b_i+k))=12^k x_i^k.

Expansion of the total product polarization, including all multinomial
coefficients, should give the safe bound [26(L+1)]^L times the
Fermat-product degree. This can also be derived coefficientwise by
bounding every multinomial coefficient by (L+1)^L and every remaining
12-power by12^L, with at most2^L terms. A final proof must account
for the number of weak compositions; the total coefficient sum is
already bounded by(13t)^L for t<=L factors, so [26(L+1)]^L is safe.

## Effective correspondence operations

Published Truong, Crelle758(2020), authorcopy arXiv1605.05049,
Lemma2.2 (authorp13) proves that on a smooth projective X of
dimensionk and degreeD, an intersection of integral effective cycles
of degreesd1,d2 is representable as positive minus negative integral
cycles, each degree<=kD^k d1d2. Root read the full cone proof.
Use the larger total-mass factor2(k+1)D^(k+1).

Every ambient product required here has dimension<=2L and degree<=A.
For a correspondence of degree<=A, first taking the product with
its target multiplies the cycle degree by at mostA; the intersection
cost is at most2(2L+1)A^(2L+1), and proper projection cannot increase
degree relative to the total product polarization. Hence B bounds
one entire correspondence operation on cycle mass.

The returning cyclic graph is one such operation. Algebraic character
projectors, Frobenius intertwiners, determinant alternation and matrix
units expand into finite linear combinations of coordinatewise deck
actions, permutations, point projectors and diagonals. Their scalar
coefficients do not enter detector degree: a nonzero final projection
of a linear combination has a nonzero projection from at least one
individual integral positive/negative component. No integral saturation
or coefficient division is being asserted.

Tentative operation count: at most L Kunneth projections, L group
endomorphisms, at mostL contractions/projections, six primitive
projectors, and two permutation/final projection operations, which
is at most4L+20. Need verify that tensor intertwiners really have
this expression with no extra operations depending on Brauer rank.

## Final map to the sixfold

Let e be the rational central E8 projector and p=e(1-s_1)/2.
Its denominator divides2G. On J(C), p is Rosati-self-adjoint and
idempotent. The homomorphism f=2Gp has image B of dimension6 and
f^*(Theta|B)<= (2G)^2 Theta. Compose six copies of f with Abel
maps and addition C^6->B. The Cauchy inequality for the sum of six
maps gives pullback theta_B <=(2G)^2 H_C^6 because degTheta|C=g
and degH_C=6g. Thus a three-cycle of degreeE on C^6 pushes to
one of theta_B-degree <=(2G)^6 E. This produces the proposed
D_source after the complete degree proof has passed review.

## Target lattice still separate

The natural source polarization has exponent dividing2G, hence
volume<= (2G)^6. For a general fixed target datum in the same
Gaussian determinant class3, one must explicitly charge a rational
Hermitian isometry between the source and target lattices. Merely
invoking Landherr or an unspecified isogeny does not give a numerical
bound. The task is active; no all-polarization D_source assertion is
being made in these notes.
