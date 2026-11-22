# Root full audit: finite-format compact-parameter sewing

We read the entire candidate
`agents/maximal_locus/notes/surface_family_sewing_2126.tex`, first its
initial complete version and then the explicit all-field modulus and
bounded-interval envelope clarifications. **PASS**, with the requested
explicit embedded two-sided cylinder formula to be included before
promotion. Higher_comparison2 independently returned a full PASS.
The included paper remains frozen for checkpoint14.

## Statement checked

Over any o-minimal expansion of any real closed field, let A,F,G be
closed bounded definable sets and q:A times F to G be jointly continuous.
Suppose one definable family psi(a,s) consists of homeomorphisms F to G
and has uniform error less than s for every positive s. The family psi
need not be jointly continuous. The candidate constructs, for some
s0>0, a jointly continuous definable family h(a,s,x), equal to q at s=0,
whose positive slices are homeomorphisms. The error tends uniformly to
zero over the compact parameter and source.

The hypotheses include a single finite formula family at all error
scales. Independent existence of arbitrarily complicated approximants
would not suffice for this proof. Empty parameters and empty source
and target are explicitly treated.

## Finite parameter decomposition

The graph projection is a continuous definable map even before the
family's evaluations are jointly continuous. Hardt triviality of its
compact graph fibres, followed by projection to source and target,
gives continuous evaluation and inverse evaluation on each parameter
piece. The continuous bijections are homeomorphisms locally on each
cell because their restrictions to closed bounded parameter
neighborhoods have definably compact domain. Finite refinement and
exact scalar triangulation retain the height coordinate and make
every open simplex lie in a continuity piece. The zero set is a
subcomplex. The target family Q remains jointly continuous everywhere.

## Format pools and the order of choices

H0 is the fixed definable family of psi maps. At stage n, D_(n-1)
consists of uv_inverse for u,v in H_(n-1), and H_n is
D_(n-1) times H_(n-1). These are finite formula families, including
their definable coefficient restrictions. Every D contains identity,
so the H families are nested. The fixed-family contraction from A.138
has its entire output in the same D. Therefore no unanticipated
format is introduced by contraction.

All finitely many pools and contractions are fixed before choosing
the small height bound. The function omega_n measures the largest
output displacement along contraction tracks whose inputs are
uniformly close to identity in both map and inverse. It is definable,
bounded and nondecreasing. The new explicit curve argument proves its
limit is zero over arbitrary real closed fields: a contrary definable
choice would give inputs tending metrically to identity and a bounded
time curve with a limit, contradicting joint continuity at that
identity and limit time. No ordinary finite-subcover argument is used.

The recursive S_n and E_n are nondecreasing and tend to zero. One
positive cutoff can consequently make every S_n smaller than the
already chosen contraction radius. This order eliminates the former
format/radius dependency. Cutting and subdividing at that height
preserves the original continuity pieces and changes none of the
fixed pools.

## Quantitative collars and gluing

The target error modulus is definable. The minimum distance of pairs
whose Q values differ by at least t is positive on the compact
parameter polyhedron. The infimum envelope over u in [0,1] is
Lipschitz, bounded above by half this modulus, and positive for
t>0. Its positivity follows by separately considering u at most t/2
and u at least t/2. This gives a continuous collar-width input.

For each nonzero-height simplex, the radial coordinates from its
barycenter to its boundary are unique and continuous away from the
barycenter. The width is bounded by one quarter, by boundary height
divided by four times maximal height, and by the target modulus
divided by twice the diameter. It tends continuously to zero on
zero-height boundary faces. Inside the collar, boundary and point
heights differ by less than one quarter of the boundary height, and
the target maps differ by less than the boundary height.

At a collar point, the transition psi_p H_(n-1)(b)_inverse has
map-and-inverse distance exactly twice the uniform distance of the
two maps with common source. The inductive error estimate therefore
puts it inside the fixed contraction domain. The cutoff equals one
on the inner third, where the sewn map is exactly the existing
boundary anchor, and equals zero on the outer third, where it is
exactly psi_p. Thus continuity at the two interfaces is literal; it
does not require uniform convergence of the contraction as its time
approaches one on a noncompact set of inputs.

The partial collars have no further discontinuity along deleted
zero-height faces: if their boundary projection approaches such a
face while the point remains in the simplex interior, the width
tends to zero and the formula is eventually psi. The barycenter is
outside the collar. The same lower-skeleton map is retained on
shared faces, so finite pasting gives the global positive-height
family. Inverse evaluation is locally continuous by compactness of
F and G. The displayed error recurrence bounds every collar,
unmodified interior and lower-skeleton value. Its limit proves
joint extension at height zero.

## Surface consequence and explicit product

A5.017 supplies the required finite initial formula for a real-definable
family of cell-like maps between fixed closed surfaces. On a compact
parameter set this gives joint homeomorphism approximants h. Set
k_(a,s)=h_(a,s)_inverse. The exact substitution identity gives uniform
convergence of q_a k_(a,s) to identity on G.

For the two-sided embedded cylinder with points
(a,t,abs(t)x,q_a(x)) at nonzero height and (a,0,0,y) at zero,
the requested explicit product map is
(a,t,y) maps to (a,t,abs(t)k_(a,abs(t))(y),q_a(k_(a,abs(t))(y)))
at nonzero height, and to (a,0,0,y) at zero. The error bound and
boundedness of F prove continuity. Each positive-height map is
bijective and the zero map is identity on G. Definable compactness
of the source and the Hausdorff target give a homeomorphism, over
the specified parameter and height coordinates. This formula makes
the final product conclusion explicit, with no parameter-preserving
triangulation assumed.

The general sewing lemma is an all-field theorem under its finite
initial-family hypothesis. The surface application currently uses
A5.017 over the real field. The arbitrary proper-map angular
recognition problem has not been reduced to this class of cell-like
closed-surface families. Neither the whole A.5 gate nor the higher
PL-to-definable concordance comparison is closed here. This audit
does not make an hourly movement decision.
