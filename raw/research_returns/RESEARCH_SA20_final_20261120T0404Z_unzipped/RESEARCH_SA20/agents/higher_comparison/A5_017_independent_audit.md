# A5.017 independent audit: one finite format for surface approximants

19 November 2026, 21:22 UTC. We write as GPT-6 Astra (OpenAI,
ChatGPT Pro mode), agent `/root/higher_comparison2`, with inherited
effort configuration. Root and maximal_locus2 control promotion.

**PASS** for the complete version of
`agents/maximal_locus/notes/uniform_surface_approximants_2104.tex`
identified by hash
`74c3532dc66cb5aa2786a68fa8e5a1cb6ab05b912fbf3cd9550d2c9c11383520`.
We read the entire proof, including explicit empty cases and the
source ambient dimension D in every certificate format. The statement
asserts one definable family of individually accurate homeomorphisms.
It does not assert joint continuity in the parameter or error variable.

## Original source independently reopened

Masahiro Shiota, *PL and Differential Topology in o-minimal Structure*,
arXiv:1002.1508v3, 17 February 2010, full original at
<https://arxiv.org/pdf/1002.1508>. We reopened Section 2, printed p. 5,
and Theorem 2.2(1), printed p. 6. Retrieval record:
`turn401273978view0`. The section works over a real closed field in a
fixed o-minimal expansion. The theorem supplies a definable source
homeomorphism making the given continuous scalar function PL, with
no change of target coordinate. This is the exact all-model input
needed by the certificate compactness argument.

The individual surface and finite collar inputs are the already
audited A5.016. We reread its height-leveling Lemma 1 and its mapping
cylinder extraction to check the new uniform-format dependence.

## Certificate and logical compactness checks

For each index i, the finite abstract complex, ambient dimension D,
and graph formula are fixed syntactic data. Coordinates, graph
parameters, and vertex heights form finite tuples of field variables.
The stated realization, graph bijection, continuity and inverse
continuity, and affine-height identities are all first-order. A graph
formula for a particular triangulation may use a and additional
parameters; these can all be entries of its existential coefficient
tuple. Thus the certificate list captures every triangulation supplied
by the scalar theorem in an elementary extension.

The parameter hypotheses needed at this stage are continuous
surjectivity and closed bounded mapping cylinders, which transfer.
Cell-likeness is not transferred. O-minimality persists under elementary
equivalence because uniform one-variable fibre bounds, together with
their interval descriptions, are first-order schemes true in the
original o-minimal structure. Hence the scalar theorem applies in the
elementary extension produced by compactness.

If no finite list of certificate formats covered A, the type excluding
all of them would be finitely satisfiable with the elementary diagram.
Its realization would contradict the scalar theorem. This reasoning
works for an arbitrary set of formulas; countability or effective
enumerability is unnecessary. It proves existence of a finite list,
without providing an algorithm or numerical complexity bound.

## Finite geometric choices

Definable choice selects one of the finitely many certificate formats
and its coefficients. Passing to the standard abstract realization
removes the moving geometric coordinates. The zero-vertex patterns
are finite and definable, so only finitely many pairs (K,L) occur.
The real cell-like argument is now applied only to pairs that occur
for real parameters. A5.016 then makes K a PL three-manifold and L
a union of its boundary components. Choosing one fixed collar for
each of these finitely many pairs is legitimate and introduces no
unbounded parameter-dependent collar complexity.

A fixed refinement making the collar simplicial and lying over the
original simplices works for every height function that is affine on
that original complex. Additional vertex heights are fixed affine
combinations of the original ones. Their zero pattern is determined
by the original zero pattern, because all heights are nonnegative.
The complement of the open collar is a fixed compact polyhedron
disjoint from L, so the height has a positive definable minimum there.
The chosen epsilon can therefore meet every required positive bound
in one definable formula.

For each mixed face, the zero-face and positive-face barycentres
give the displayed rational point at height epsilon. Since the
positive barycentre height is greater than epsilon, this point lies
in the relative interior. The finite descending stellar order is
fixed. Paired stars retain the same combinatorics and nondegenerate
simplices for every parameter in the part. Their affine maps are
therefore one definable family obtained by finite linear algebra.

The coordinate extraction and inversion from A5.016 are definable
for this family. For each fixed a they give actual homeomorphisms
and uniform convergence to q_a. Compactness of F makes the error
maximum definable. The final relation asking for error below eta
has nonempty fibres, so definable choice gives the asserted one
formula psi(a,eta,x). No continuity of that final choice is used.

## Transition identity and scope

For homeomorphisms u,v:F->G, substituting y=v(x) gives
`sup_G |uv^-1(y)-y| = sup_F |u(x)-v(x)|`. Substituting y=u(x)
gives the same quantity for the inverse transition. Therefore the
stated map-and-inverse metric control is exact even when the common
limit q_a is noninjective; no inverse of q_a is required.

This proof supplies the finite initial family needed by a separate
sewing argument. It does not supply that sewing argument, a joint
homeomorphism family, or any closure of the original A.5 row. Root
and maximal_locus2 were informed of the complete PASS in chat before
the source-freeze deadline.
