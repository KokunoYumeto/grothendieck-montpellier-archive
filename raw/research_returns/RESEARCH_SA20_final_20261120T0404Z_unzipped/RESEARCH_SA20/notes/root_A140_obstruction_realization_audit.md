# Root audit of A.140

We read the complete numbered candidate in
`agents/singularities_duality/logs/A140_OPR_obstruction_realization_draft.tex`
and the independent audit. The mathematical argument passes, with the
source-notation correction and finite-certificate paragraph specified below
to be included in the promoted version.

## Exact original inputs and notation

Root opened and read the current original Orson–Powell–Randal-Williams
paper, `smoothing_pseudo_isotopies.pdf`, Sections 2.1 and 3.1, Theorem 2.3(D)
on printed page 6, and the definition of KS on page 9. In this audit we also
read the locally retained original text of Section 5.2, Definition 5.8 on
page 21, and the proof on page 22. The displayed Theorem 2.3(D) prints an
L^s_6 target, whereas Definition 5.8 explicitly defines I_2 using quadratic
L^q_6 and its assembly map. Our hypothesis is the vanishing of the **actual
map defined in Definition 5.8 and used in the proof**. We requested the
L^q notation and a note recording the printed discrepancy. We neither
identify symmetric and quadratic L-groups nor infer a stronger hypothesis.

The given PL four-manifold has a compatible smoothing by the exact
Kirby–Siebenmann Essay I page 39 existence assertion. This chooses one
structure only; no family of PL maps is converted into a smooth family.
The corrected GGHKP Theorem 1.5 was opened in its original published form:
it isotopes the whole TOP pseudo-isotopy to identity relative to the bottom
and the vertical boundary on a simply connected compact four-manifold.

## Class-level obstruction comparison

For N=B times I, W=N times I and
C=(N times {0}) union (boundary N times I), we checked that C to W is a
homotopy equivalence. The exact triple connecting map therefore identifies
H^3(boundary W,C;Z/2) with H^4(W,boundary W;Z/2). The standard lift on W
trivializes the PL-lift torsor. Changing its top boundary lift changes the
relative universal Kirby–Siebenmann obstruction by precisely this connecting
map. This is the actual universal-square construction, not merely a
comparison of vanishing conditions.

The OPR pullback convention uses F inverse relative to the A.137 pushforward
convention. The proved trivial action on relative cylinder H^3 and additivity
of kappa make their difference immaterial over Z/2. Suspending once more
and applying product Poincare duality gives KS_OPR(F)=PD_B(kappa(F)).
Common-collar normalization preserves both classes and supplies literal
boundary smooth/PL data where required.

## Realization and ordinary components

Theorem 2.3(D) starts with **block** pi_1. We checked that the proof never
treats a block simplex as an ordinary loop. A class in its image has an
endpoint diffeomorphism whose block smooth component is trivial. The
source's exact sequence gives a smooth pseudo-isotopy G from that endpoint
f to identity. The formula G'=G composed with (f inverse times I) has bottom
identity and top f inverse, so G' composed with F fixes both ends literally.
The OPR additive obstruction of G' is zero. This realizes exactly the
Poincare dual of the Bockstein kernel by both-end-fixed concordances.

A.137 then gives im(lambda_B) containing (L_B+J_B)/J_B. If H_1 with
Z_(2) coefficients has no two-torsion, the Bockstein is zero and this image
is the entire quotient. The endpoint-image subgroup is still retained.
No assertion is made for a nonzero assembly summand without another proof.

In the simply connected case, GGHKP makes the ordinary free-top component
group trivial. Together with realization this proves J_B=H^2(B;Z/2).
For every prescribed class choose a both-end-fixed F and an ordinary path
H_s from identity to F. Its top restriction gamma is an ordinary loop.
The exact formulas T_s(x,t)=(gamma_(st)(x),t) and Q_s=T_s inverse H_s keep
Q_s fixed on both ends. Its kappa is zero throughout, proving that the trace
of gamma realizes the prescribed class. Pointwise multiplication of loops
and trace additivity prove that eta_B is a homomorphism. The homotopy-fibre
exact sequence, equivalently the PL trace, proves vanishing on the PL pi_1
image. Thus the stated failure of automorphism pi_1 surjectivity follows.
It is not a claim about concordance pi_1, nor a smooth-isotopy conclusion.

## Complete finite base for the counterexample

Take the boundary of the standard tetrahedron, with vertices 0,1,2,3, in
each factor. This is a finite PL two-sphere: each of its four triangular
facets is the face missing one vertex. Triangulate each product of two
triangles by its six monotone (2,2) staircase paths, using the inherited
vertex orders. Encode a product vertex (i,j) as 4i+j. The constructions agree
on common faces, and each staircase simplex is the usual simplex obtained
by ordering the cumulative barycentric coordinates of the two factors.
Their interiors partition the product and their intersections are common
faces. Thus the resulting finite complex is PL-homeomorphic to S2 times S2,
not merely a homology imitation. The product is closed and oriented, and
its fundamental group is trivial by the product fundamental-group formula.
Its product cell structure has one zero-cell, two two-cells, and one four-cell,
with zero cellular differentials, giving H^2=(Z/2)^2.

The attached exact checker `code/check_A140_product_spheres.py` records all
96 maximal four-simplices in `logs/check_A140_product_spheres.json`.
It passed **1,465 checks with zero failures** in the observed runtime
**0.014848837003228255 seconds**. It verifies the tetrahedral factors, all
staircase paths and distinct facets, face vector (16,84,216,240,96), Euler
characteristic four, mod-two Betti numbers (1,0,2,0,1), every boundary-squared
identity, every codimension-one incidence, and all 556 nonmaximal simplex
links at the homology level. The link homology checks alone are not a proof
of the PL type; the explicit product triangulation proves that fact.
The program certifies the finite base and its cohomology. It does not
algorithmically construct or test the infinite homeomorphism-space classes
whose existence follows from the opened original theorems and this proof.

No original parent task is marked complete by this result. The scheduled
progress review will assess the reduction, rather than this audit assigning
an early stopping-count change.
