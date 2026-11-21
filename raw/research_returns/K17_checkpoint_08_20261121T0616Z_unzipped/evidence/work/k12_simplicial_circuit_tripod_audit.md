# Independent audit: low perfection excess and simpliciality

Agent: /root/tripod_integral. Model: GPT-6 Astra Pro. Reasoning effort not exposed.
Date: 2026-11-21 UTC. Verdict: PASS for the full proposition in
`work/k12_simplicial_circuit_candidate.md`, including the added
rank-one extremality clarification.

I read the entire candidate and reconstructed each linear-algebra,
lattice-face and dimension step. The statement is that a lattice
whose minima span rank N has linearly independent minimal rank-one
forms whenever their span dimension r satisfies r−N≤4. The result
does not assert basicness of the original larger cone.

The primary input was freshly opened and read:
M. Dutour Sikirić, K. Hulek, A. Schürmann, *Smoothness and singularities
of the perfect form and the second Voronoi compactification of A_g*,
Algebraic Geometry 2(5) (2015), 642–653,
https://content.algebraicgeometry.nl/2015-5/2015-5-027.pdf,
DOI 10.14231/AG-2015-027; retrieval ref `turn185397310view0`.
Theorem 1.1(i), p.644, concerns every perfect cone of linear-hull
dimension at most nine, in any lattice rank. The beginning of §2,
p.645, explicitly defines this dimension and identifies the cones
with complete minimal-vector systems. I read that material and the
complete printed proof of (i), pp.645–646. Its background enumeration
and computational checks are cited as published inputs, not rerun.

For a minimal quadratic circuit with k rays, every coefficient in its
unique dependence is nonzero. Both signs occur because the forms are
nonzero positive semidefinite. Equality of the two positive sums
makes their images the same space W. The image of a positive sum
of these forms is exactly the span of its supporting vectors, since
its kernel is their common perpendicular. Thus each sign supports
at least m=dim W vectors and k≥2m.

The cone on all minimal vectors in W is a face: the functional
q↦trace(Pq), where P projects onto W-perpendicular, is nonnegative
on all rank-one generators and vanishes exactly on those in W.
W is rational. Its saturated intersection lattice with the original
lattice has the same minimum, and its complete minimal-vector set
is exactly the original minima lying in W. Thus this face is a
perfect cone to which the cited theorem applies.

Its span has dimension r_W≥k−1. Pick N−m original minima whose
images form a basis modulo W. Their projected rank-one forms are
independent (in basis coordinates they are diagonal elementary
forms), while every form supported on W projects to zero. Therefore
r≥r_W+N−m. Combining these inequalities gives m≤(r−N)+1 and
r_W≤(r−N)+m≤9 for r−N≤4.

The face is therefore simplicial. The selected distinct minimal pairs
give distinct extremal rays in it: a positive sum of rank-one positive
semidefinite forms has rank one only when every supporting vector is
on the same line. The circuit is consequently a dependence among
distinct extremal rays, contradicting simpliciality. This closes the
argument; merely lying inside a simplicial cone would not have been
enough without this extremal-ray observation.

For projective degree twelve the quadratic span has dimension thirteen.
Rank nine gives excess four and rank ten gives excess three. Both
target cells are therefore simplicial with exactly thirteen minimal
pairs. Combining this with the two separately audited index-two
orientation lemmas removes every rank-ten target cell of maximal
index at most two, including both the minimum-generated and the
proper generated-sublattice cases. It leaves larger-index cells and
the remaining rank-nine cases untreated. No full K12 vanishing
follows from this audit alone.
