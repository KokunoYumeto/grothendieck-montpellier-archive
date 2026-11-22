# Whole-proof review of K-028

Date: 2026-11-21. Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro;
effort not exposed; run GCT_POS.

**PASS.** Read the entire `PRIME_TO_THREE_STABILIZER_REDUCTION.tex`,
both proposition K-028a and corollary K-028b, including the equivariant
coherent localization induction. No gap was found.

## Primary slice input

Independently opened the primary Numdam PDF
https://www.numdam.org/item/MSMF_1973__33__81_0.pdf
and read all of Luna (1973), section III.1's preceding lemma, the slice
theorem, its complete proof and Remarks1–4, printed pp.96–98. Also read
section III.2 Corollaries3–4 and their proof on printed p.100.
The required subgroup assertion is explicitly Remark4 on p.98. The
theorem gives a saturated affine neighborhood. Applied to the effective
special-linear action, this proves openness of the locus with finite
stabilizer order prime to three. The ambient variety is the smooth
tensor representation and the chosen orbit is closed, as required.

## Finite stabilizer and conjugacy argument

On a dense open locus the effective kernel order q and the finitely many
class counts are constant. The stabilizer incidence is quasi-finite there;
its reduced finite fibres and their intersections with fixed semisimple
classes have constructible cardinalities. Passing to the quotient preserves
constructibility because these are orbit-invariant conditions.

The determinant-xi coset has exactly q elements, each of order dividing
Mq: its Mth power is in the kernel of order q. Finite conjugacy classes of
this bounded order are permuted by the three-cycle. If none of the occurring
classes were fixed, the sum of their constant multiplicities would be a
multiple of three, contrary to 3 not dividing q. This step chooses a stable
conjugacy class, not an unjustifiably fixed individual stabilizer element.

The scalar-kernel power map gives a lift of order dividing Mq. Since three
is invertible modulo Mq, its translated spectra can be made identical by
a product-one scalar adjustment. The determinant of A has order M; taking
the two-primary part of A is a power operation on the finite cyclic group,
preserves the fixing equation, and preserves that determinant order.
Complete P-F30 applies to this two-power lift, including rank-deficient and
arbitrary-lift cases. Product-torus balancing and the chain's independent
incidence columns force the chain product-linear orbit. Closure then gives
the assertion for the whole irreducible locally closed subvariety.

## Smaller exceptional support

The removed locus is closed and stable. The nonzero chain is an
open-and-closed piece of its complement, since its fixed germ is smooth
and one-dimensional and it has no higher three-primary inertia. The
remaining complement may be singular or have intersecting components;
the proof correctly uses dimension induction instead of disjointness.

Keeping the C3-equivariant coherent class is essential and is done.
An equivariant coherent extension is obtained inside the equivariant
quasicoherent pushforward by summing finitely many translated coherent
submodules; this does not multiply its restriction by three. At each
induction stage the generic component pieces occur in triples and their
restrictions are represented by induced equivariant classes. The residual
equivariant class is supported in a closed subset of smaller dimension.
Any stable irreducible residual component outside the chain would violate
K-028a, so the process continues until the remainder is supported on the
new exceptional set. Connected grading preserves the individual component
closures; all constructions retain grading.

Every extension support is contained in an original component whose
closure has no nonzero mu_(3M)-fixed point. Thus the no-collision integrality
lemma of K-027 applies at every lower-dimensional stage. Three translated
Hilbert series are identical and contribute a multiple of three after
localization. The chain and scalar Koszul denominator are unchanged.
This proves exactly the refined principal-part congruence, with no
inversion of an integral Grothendieck class and no all-n exact-M pole claim.
