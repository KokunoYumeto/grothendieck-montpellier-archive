# PL maps form a closed subfamily in every fixed definable format

19 November 2026, 20:43 UTC. We write this separate working note as
GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent
`/root/higher_comparison2`, with inherited effort configuration.
It is a method limitation, not a promoted theorem or original-gate
movement. Included sources, bibliography, CSV and check TSV remain frozen.

## Statement

Let K be the underlying set of a fixed finite linear simplicial complex
over a real closed field R. Assume K is closed and bounded. Let
`f_a:K -> R^q`, for `a in A`, be one definable family of continuous
maps in a fixed o-minimal expansion of R. No continuity in a is assumed.
Equip the family of actual maps with the uniform metric, quotienting
duplicate graph parameters if desired.

Then the following assertions hold.

1. The parameter set on which f_a is PL is definable.
2. There is an ordinary finite integer N, depending on the family and
   the fixed domain complex, such that every PL graph in the family has
   a finite polyhedral presentation and a triangulation of complexity
   at most N. Vertices and coefficients may lie in R.
3. The subfamily of PL maps is closed for the uniform metric, relative
   to the given family. Consequently, if f_a is not PL, there is a
   positive epsilon such that no PL member of this same family has
   uniform distance less than epsilon from f_a.

These statements hold for all RCFs, with no ordinary sequential
compactness assumption. They also hold for any definable subfamily
specified by marked homeomorphism conditions. For homeomorphisms of K,
closedness holds in the stronger map-and-inverse metric used in A.138.

## Original inputs opened

We opened the complete author-uploaded original of Michel Coste,
*An Introduction to O-minimal Geometry* (November 1999), at
<https://www.researchgate.net/publication/228392940_An_introduction_to_O-minimal_geometry>.
The page identifies the full text as uploaded by Michel Coste; it is
the original notes, not a secondary statement or abstract. Relevant
locators are Theorem 3.1, p. 25 (definable choice); Theorem 3.4,
pp. 26–27 (closed bounded sets and definable curve limits);
Theorem 3.9, pp. 28–29 (definable components); and Theorem 3.12,
pp. 30–31 (a uniform finite bound on fibre components).
The arbitrary-real-closed-field convention is in Section 1.3,
pp. 9–10. Retrieval records are `turn290178368view0`,
`turn375284005view1` and `turn419925358view0`.

The author's direct OMIN.pdf endpoint timed out twice. We used the
already public full author upload and did not bypass access controls.
The elementary polyhedral arguments below are supplied in full.

## 1. A first-order local-affineness criterion

For every simplex sigma of the fixed domain complex, including its
lower-dimensional faces, use affine coordinates on its affine hull.
If sigma has positive dimension, let U_(a,sigma) be the set of points
x in the relative interior of sigma for which there are an affine map
L and a positive r such that

`f_a(y)=L(y)` whenever `y in relint(sigma)` and `|y-x|<r`.

This is a first-order definition: the coefficients of L and r are
finitely many field variables. Thus U is a definable family of relatively
open subsets of the simplex interiors. The affine germ at a point of U
is unique, because two affine functions agreeing on a nonempty open
subset of an affine space agree everywhere on that affine space.
Its coefficient tuple is locally constant on U. It is therefore
constant on every definably connected component of U. Theorem 3.12
uniformly bounds the number of those components. Zero-dimensional
simplices impose no condition: every map on one point is affine.

We claim that f_a is PL if and only if U_(a,sigma) is dense in sigma
for every positive-dimensional simplex sigma. Necessity follows by
intersecting a finite PL subdivision with sigma. Outside its lower
dimensional faces, the restriction is locally affine.

For sufficiency, fix sigma and suppose U is dense. Write its finitely
many components as U_1,...,U_b and their affine formulas as L_1,...,L_b.
Continuity of f_a implies f_a=L_i on the closure of U_i in sigma.
Those finitely many closures cover sigma. Hence, at every point of
sigma, f_a agrees with at least one of the finitely many L_i.

Subdivide sigma by all nonidentically-zero scalar affine equations
arising from the coordinates of L_i-L_j. Include the face hyperplanes
of sigma. On the relative interior C of each resulting convex
polyhedral cell, any two L_i and L_j either agree everywhere or
disagree everywhere. Since f_a is continuous and selects one of these
finitely many affine values, the choice of the equivalence class of
that value is locally constant on C: near a point, different values
remain separated. Convexity makes C definably connected, so the choice
is constant. Thus f_a is affine on C, and continuity extends that
formula to the closure of C. This proves that f_a has a finite
polyhedral graph on sigma. Taking all domain simplices proves that
its full graph is a finite polyhedron, equivalently that f_a is PL.

Density is first-order, for example by quantifying a point of the
simplex and a positive radius. The conjunction over the finitely many
domain simplices therefore defines exactly the PL parameter locus.
No quantification over an unspecified number of pieces is used.

## 2. Uniform polyhedral complexity

Theorem 3.12 supplies one bound b for the number of components of all
the U_(a,sigma), after taking the maximum over the fixed finite set of
simplices. For each sigma the arrangement above uses at most
`q*b*(b-1)/2` additional hyperplanes, besides its fixed face planes.
The ambient dimension and number of these hyperplanes are fixed.
There are uniformly finitely many sign cells, faces and vertices.
Each closed cell is a bounded convex polytope; its graph under its
affine formula is a convex polytope with the same vertex bound.

One can refine the finitely many graph polytopes by all their faces
and intersections, then triangulate the resulting finite polytopal
complex by its face barycentres. The number of faces, intersections,
and barycentric flags is bounded by a finite function of the preceding
uniform bounds and the fixed ambient dimension. This gives one finite
bound N on the number of graph vertices and simplices for all PL
members. No numerical efficiency claim is made.

In particular, there are only finitely many abstract simplicial
complexes that can occur as one such bounded presentation. For each
of these finitely many combinatorial types, being a realization in
R^(dim ambient K + q), being the graph of f_a, and having the prescribed
simplex intersections are first-order conditions on its vertices.
Alternatively, for the closure argument it suffices to use a fixed
number of convex-hull slots with repeated vertices and degenerate
simplices allowed. This avoids imposing any nondegeneracy on limits.

## 3. Closedness by definable vertex limits

Suppose f_0 is a member of the family in the uniform closure of its PL
subfamily. For every sufficiently small positive t, there is a PL
member f_(a(t)) with `sup_K |f_(a(t))-f_0|<t`. Definable choice selects
a(t), a bounded-complexity graph presentation, and its vertex tuple.
All of this choice is made in one first-order relation; it need not
initially be continuous. Since the combinatorial type takes only
finitely many values, o-minimality makes it constant after restricting
to some interval `0<t<t_0`. Thus we may label its finitely many vertices
v_1(t),...,v_N(t), allowing repetitions if necessary.

Every vertex lies in the graph of f_(a(t)). The domain K is bounded,
and the uniform t-bound puts every image coordinate in a fixed bounded
box around the compact image of f_0. Hence all vertex coordinates are
bounded definable one-variable functions. Monotonicity gives a limit
for each coordinate as t tends to zero from above; equivalently one
may first restrict to an interval where all coordinates are continuous
and apply Theorem 3.4. Write the vertex limits as v_i(0).

Let Q(t) be the union of the finitely many graph simplices, and let
Q(0) be the union of the convex hulls of the corresponding limiting
vertices. Simplices may collapse or meet more at t=0; Q(0) is still a
finite polyhedron. For two finite lists of vertices, the Hausdorff
distance between their convex hulls is at most the maximum of the
paired vertex distances: use the same barycentric coefficients in
the two convex combinations. The same estimate holds for the finite
unions. Consequently Q(t) tends to Q(0) in Hausdorff distance.

On the other hand, Q(t) is the graph of f_(a(t)), and the uniform
function bound gives Hausdorff distance less than t from the graph
of f_0, pairing points with the same domain coordinate. Thus Q(0)
equals the graph of f_0. Both sets are closed and bounded; the triangle
inequality gives zero mutual distance, which yields equality. Therefore
f_0 has a finite polyhedral graph and is PL.

This proves closedness using only definable choices and limits of
finitely many bounded definable coordinate functions. In particular,
it does not select a subsequence in a non-Archimedean field.

## 4. Consequence for approximation routes

There is no jointly definable family of PL maps on K that converges
uniformly, as a positive scalar parameter tends to zero, to a non-PL
continuous map. This holds already over the real field. The family
itself would be one finite format, and the preceding closedness proof
would force its limit to be PL. In particular there is no such
definable PL approximation family converging to x squared on [0,1].

This does not contradict real-field PL density: a sequence of finer
and finer arbitrary finite PL subdivisions need not be a definable
one-parameter family. Nor does it obstruct a definable isotopy ending
at a PL map. The isotopy `(1-s)*x^2+s*x` is an explicit example; its
members are non-PL for s<1 and PL at s=1. Closedness is compatible with
that direction of degeneration.

For the higher comparison gate, A.138 supplies contractions within
each fixed format. The present result shows why one cannot keep a
single such format while demanding arbitrary-error PL approximation
of a non-PL member. A proof must supply coherent straightening by
another mechanism, or control a genuinely changing collection of
formats. No failure of the full PL-to-definable weak-homotopy comparison
is asserted.

## 5. An explicit fixed-format higher obstruction over the reals

Let C be the boundary of the square `[-1,1]^2`, and let
`A_(c,s)=[[c,-s],[s,c]]`, where `c^2+s^2=1`. Define

`h_(c,s)(x) = A_(c,s) x / ||A_(c,s) x||_infinity`, for x in C.

These form a single semialgebraic family of actual homeomorphisms of C.
Positive homogeneity verifies the composition law and gives the inverse
by replacing s with -s. The parameter map from the unit circle to this
homeomorphism family is continuous, injective and onto; compactness
makes it a homeomorphism for the uniform map-and-inverse metric. Thus
the family has the homotopy type of a circle.

Its PL members are exactly the four quarter-turns. If c=0 or s=0,
the map is the corresponding linear rotation of the square. If cs is
nonzero, restrict to the edge x=(1,t). On any open interval of strict
coordinate dominance, the nonconstant target-edge coordinate is a
fractional linear function `(gamma+delta*t)/(alpha+beta*t)`, where
beta is either c or -s and `alpha*delta-beta*gamma` is nonzero.
Its second derivative is

`-2*beta*(alpha*delta-beta*gamma)/(alpha+beta*t)^3`,

which is nowhere zero on that interval. It cannot be affine on any
subinterval there, so the square homeomorphism cannot be finite PL.
Such a strict-dominance interval always exists; equality of the two
absolute coordinates occurs only at finitely many points of the edge.

Every member of the family is semialgebraically isotopic within the
family to the identity, because the parameter circle is definably
path connected. Yet the inclusion of the four PL points into the
whole family is not surjective on pi_1: the circle has pi_1 equal to
Z and the four-point space has trivial based pi_1. Thus even complete
pointwise isotopy to PL plus fixed-format local contractions does not
give a higher straightening that stays inside that fixed format.

This last example is solely a counterexample to a format-preserving
inference. The full PL homeomorphism space contains paths and loops
that leave this particular rotation family. It is not a counterexample
to the original higher comparison.
