# Whole-proof review of K-026

Date: 2026-11-21. Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro;
effort not exposed; run GCT_POS.

**PASS.** Read all of `CYCLIC_FIXED_COMPONENT_REDUCTION.tex`, both
proposition K-026a and phase lemma K-026b. The complete inherited P-F30
proof and the effective-freeness of the chain were previously whole-proof
checked in this continuation; their hypotheses are explicitly retained.

## Component reduction

The determinant character on GL_n cubed modulo the scalar kernel has
exactly the effective SL_n cubed image as kernel. At a free closed orbit,
its stabilizer therefore injects into C-star. A nonzero homogeneous
invariant makes its character image finite, hence cyclic. The lift of
the chosen grading element is unique and has order exactly M.

The scalar kernel is a torus, so its M-power map is surjective. Adjusting
a lift by this central torus gives an honest order-dividing-M triple.
The resulting finite list of spectral classes gives a finite constructible
partition. Over an effectively free quotient point every orbit in the
fibre is closed: any nonclosed orbit would have a closed boundary orbit
of strictly smaller dimension, whereas this fibre's unique closed orbit
already has the full effective group dimension. This supplies an explicit
justification for using fixed-space images to define the partition.

On an irreducible component one class is generically constant. Cyclic
stability forces this class to be invariant under permutation. The three
spectra are scalar translates. Division of their total translation by
three modulo the dyadic order gives a product-one scalar adjustment making
all spectra identical. The resulting determinant has order M because its
cube has order M. Complete P-F30 then forces precisely the cubic chain.

The product of the three diagonal special-linear tori supplies actual
three-mode balancing. Its first three equations force the initial masses
to one-half; the succeeding equations give the unique positive recurrence.
The homogeneous version proves column independence. Thus all coefficients
are present and lie in one complex diagonal-torus orbit. The corresponding
quotient is the chain grading orbit. Its closure contains the putative
component, so maximal irreducibility gives equality. The remaining S3
orbits have sizes three or six, as stated.

## Phase lemma and scope

The tangent determinant is the determinant of the tensor representation
divided by the adjoint determinant, hence xi^(n^2). Removing fixed tangent
directions changes neither determinant. Complex conjugation of each
nontrivial factor gives (1-lambda^-1)=-lambda^-1(1-lambda), proving the
phase formula with sign (-1)^(D-d). The statement supplies a real phase
line only; it does not imply a common sign.

Both missing hypotheses are accurately stated: a fixed component might
miss the effectively free locus, and a free curve with larger inertia
may have density with a power of three in the denominator. A three-cycle
of components therefore need not contribute a three-divisible local term.
No exact primitive-M pole is concluded.

Two requested clarifications were sent to the author: name the product
of the three diagonal tori explicitly, and include the closed-fibre
justification of constructibility above. Neither is a substantive gap.
