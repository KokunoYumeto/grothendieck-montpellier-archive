# K17: orthogonal join and the first nonsimplicial endpoint

Date: 2026-11-21 UTC. Researcher: `/root/vandiver_k`, GPT-6 Astra Pro.
Reasoning effort: not exposed.

Status: complete restricted proofs, self-read in full; independent audit
requested. No vanishing of the outstanding Steinberg groups or of K12 is
asserted. These results refine the possible chain-level obstruction.

## 1. Orthogonal join is an actual map on cellular coinvariants

Let `C_d(N;R)` be the oriented cellular chain coinvariants of the relative
projective perfect-cone (Voronoi) complex for `GL_N(Z)`. Its relative
subcomplex consists of the cones whose vectors do not span the ambient
rational vector space. Here `R=Z[1/13!]` is enough for all ranks under
discussion. The chain-map construction below itself is defined over Z;
the orientation cancellations use that 2 is invertible.

For a full-rank perfect cone `tau` in `Sym^2(R^N)`, put

    J(tau) = cone(tau, e_(N+1)e_(N+1)^t).

This is a perfect cone: if Q has minimum one and precisely the ray pairs
of tau as minima, then `Q perpendicular 1` has exactly those pairs and
the new coordinate pair as minima. A vector with both components nonzero
has norm at least two. Its projectivization is the cone on the projective
cell tau and has dimension one greater.

Use the cone-span orientation convention of DEKM, section 1.2.1,
equations (1)--(2), printed p.4: orient J(tau) by appending the new
quadratic ray to an oriented basis of the span of tau. If rho is a
facet of tau, the oriented basis of J(rho), followed by an old missing
ray, differs from the ordered basis used for J(tau) by moving that
missing ray across the new coordinate ray. Its incidence is therefore
the negative of the old incidence. The additional base facet tau has
rank N in the rank-(N+1) ambient lattice and is zero in the relative
complex. A face of tau already in the old relative boundary remains in
the new relative boundary after J. Thus, with this explicit convention,

    boundary J = -J boundary.

This is a degree-one chain map from the conventional suspended complex.
If one instead sets `J_tilde_d=(-1)^d J_d`, then
`boundary J_tilde = J_tilde boundary`. The latter is the ordinary
right-cone convention on oriented projective triangulations. These are
two degreewise orientation choices for the same geometric operation;
all boundary and homology conclusions below are independent of them.
The cone-span incidence argument works for nonsimplicial cells as well.

It descends to coinvariants: `g` in `GL_N(Z)` extends to `g perpendicular
1`, and sends the oriented join to the corresponding oriented join.
In particular an orientation-reversing stabilizer in the source extends
to one in the target. The construction is made on the actual cellular
chains before passing to coinvariants, so no stabilizer-index or transfer
factor appears. After taking orbits, equivalent facets are simply summed
with their ordinary oriented incidences, on both sides of the identity.

Consequences:

1. If an explicit chain b satisfies `boundary b = tau`, then
   `boundary (-J(b)) = J(tau)` with coefficient one. This justifies
   lifting the exact coface that kills the rank-nine survivor to rank ten.
2. J sends cycles to cycles and boundaries to boundaries, inducing a map
   of homology with the cellular degree shifted by one. Under the usual
   Voronoi/Steinberg shift, this keeps the Steinberg homological degree
   unchanged.
3. `J^2=0` in the oriented coinvariant complex when 2 is a unit: swapping
   the two new coordinate axes fixes every old ray and transposes the two
   new independent quadratic rays, reversing orientation.

An **integrally split coloop** is a primitive minimum vector v such that
all the other minimum rays span a hyperplane W and

    L = (L intersect W) direct_sum Z v.

Its cell is an orthogonal join up to integral equivalence. The given
witness form need not be orthogonal: restricting it to `L intersect W`
and taking its orthogonal sum with the unit rank-one form produces the
same minimum set. A rational coloop need not split integrally. If all
minimum vectors generate L, however, every rational coloop does split,
by collecting the integral coefficients of that vector.

**Limitation.** These facts do not define a contracting homotopy on all
coloop cells. In particular, a cycle in the image subcomplex of J need
not lift to a cycle before applying J: its lifted boundary may lie in
the kernel of J. Vanishing of lower-rank homology therefore does not,
without an additional argument controlling this kernel, eliminate every
cycle supported on coloop cells. The statement proved here is the actual
chain map and the lifting of already-known explicit boundaries.

## 2. Structure at excess five

### Proposition K17-K12-EXCESS5

Let L be a well-rounded lattice of rank `N>=6`, and suppose that the
perfect cone sigma of all its minimum pairs is nonsimplicial and has
perfection rank `r=N+5`. Then there is a rational subspace W of dimension
six such that:

- the minimum rays in W span a nonsimplicial perfect cone of dimension
  eleven;
- outside W there are exactly `N-6` minimum pairs;
- their images form a basis of `L_Q/W`, and each is a rational coloop.

If `N>=8` and the minimum vectors generate L, then sigma has an integral
orientation-reversing stabilizer. In particular, every nonsimplicial
rank-eight, projective degree-twelve cell whose minima generate its
ambient lattice vanishes in oriented coinvariants over R.

### Proof

Choose a minimal nontrivial linear dependence (a circuit) among the
distinct rank-one minimum rays. Let k be the number of rays in its
support, W their vector span, and m its vector dimension. A circuit has
quadratic rank `k-1`. Splitting its relation into its positive and
negative parts gives equality of two positive semidefinite sums. The
kernels of these sums show that both sign supports span W. Each support
has at least m vectors, hence

    k >= 2m.

Let `sigma_W` consist of all the minimum rays of L lying in W, and let
`r_W` be its quadratic dimension. This is a genuine perfect cone for
the lattice `L intersect W`, because the circuit spans W and the
restriction of the original witness form has exactly those minima.
It is also a face of sigma: a positive semidefinite linear functional
whose kernel is W exposes precisely these rays. It is nonsimplicial,
since it contains the chosen circuit among its extremal rays. Rank-one
positive semidefinite rays with distinct underlying lines are extremal
in any cone generated by rank-one positive semidefinite matrices.

Choose `N-m` original minimum vectors with independent images modulo W.
Their projected rank-one forms are linearly independent, giving

    r >= r_W + N-m,       r_W >= k-1 >= 2m-1.

Since `r=N+5`, we obtain `m<=6` and `r_W<=m+5<=11`.
The cited theorem of Dutour Sikiric--Hulek--Schuermann, Theorem 1.1(ii),
says that the only nonsimplicial perfect cone of dimension at most ten
is the D4 cone. That exception has vector span four and quadratic
dimension ten. It cannot occur here, because it would give
`10=r_W<=m+5=9`. Consequently `r_W=11`; then
`11<=m+5` forces `m=6`. This also forces `k=12` for the selected circuit,
although the argument does not claim that these are all the rays in W.

Choose minimum vectors `v_1,...,v_t` whose images form a basis modulo W,
where `t=N-6`. There is equality

    dim span(sigma) = 11+t.

The classes of `v_i v_i^t` therefore form a basis of the quotient of
the quadratic span by `span(sigma_W)`. Write the vector space as
`W direct_sum U` and use the images of the v_i as a basis of U.
For another minimum vector v outside W, its quadratic form is a linear
combination of the `v_i v_i^t` modulo a form supported on W. If the
U-coordinates of v are `a_1,...,a_t`, comparison of the U-by-U blocks
gives a diagonal matrix on the right. Thus `a_i a_j=0` for `i!=j`, so
only one coordinate is nonzero, say `a_j=a`. The coefficient of
`v_j v_j^t` is then `a^2`. Comparison of the W-by-U blocks shows that
the W-component of v is a times the W-component of v_j. Hence
`v=a v_j`. Their equal minimum norms give `a=+1` or `-1`.

It follows that the only minimum pairs outside W are those of
`v_1,...,v_t`. Each is a rational coloop.

Finally suppose all minima generate L. If M is the sublattice generated
by the minima in W, the complete list just proved gives

    L = M direct_sum Z v_1 direct_sum ... direct_sum Z v_t,
    M = L intersect W.

For `N>=8` there are at least two of the v_i. Interchanging v_1 and v_2
and fixing M and the other v_i is an integral lattice automorphism.
It fixes the entire eleven-dimensional quadratic span of sigma_W and
transposes two of the independent outside quadratic rays. Its
determinant on the quadratic span is minus one, hence it reverses the
projective cell orientation. The oriented coinvariant is zero after
inverting two. This proves the proposition.

### Scope and unresolved part

At rank eight, cone dimension thirteen, the new conclusion removes the
nonsimplicial cases with minimum-generated ambient lattice. It does not
remove simplicial cells. Nor does it remove a nonsimplicial case with
nontrivial ambient glue: a rational transposition of the two outside
coloops need not preserve that overlattice. We have not classified those
glue systems, enumerated all rank-eight cones of dimension thirteen, or
computed the incoming or outgoing boundary matrices for that endpoint.

## 3. Source and actual reading record

M. Dutour Sikiric, K. Hulek, A. Schuermann, *Smoothness and singularities
of the perfect form and the second Voronoi compactification of A_g*,
Algebraic Geometry 2 (2015), 642--653, DOI 10.14231/AG-2015-027.

Primary PDF: https://content.algebraicgeometry.nl/2015-5/2015-5-027.pdf

Theorem 1.1(ii) is on printed p.644. Its full printed proof is on p.646,
using the previously enumerated cones in rank at most seven and the
paper's Lemma 3.1 for the remaining cases. The definition of perfect
cones and the dimension convention were reread on pp.643--645. This
note invokes that source theorem as known background; its external
computer classification has not been rerun.

Local files: `work/k12_source_data/dshs_smoothness_2015.pdf` and `.txt`.
Fresh web retrieval in this task: `turn176302988view0`.

The exact incidence signs and the absence of a target-stabilizer
multiplier were also checked by reading DEKM section 1.2.1 in full,
printed p.4, equations (1)--(2), and section 1.2.2, Proposition 1.3,
printed p.5, in `work/k12_source_data/dekm_author_current.txt`.

The earlier full minimal-circuit proof at excess at most four is in
`work/k12_simplicial_circuit_candidate.md` and has independent complete
audits. Section 2 above gives its additional equality-case argument in
full, rather than treating the new rank-eight reduction as already
contained in that earlier audit.
