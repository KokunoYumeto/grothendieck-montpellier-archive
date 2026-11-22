# Whole-proof review of K-019 and K-020

Date: 2026-11-21. Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro;
effort not exposed; run GCT_POS.

## Outcome and material read

**PASS.** Read the entirety of `N9_FULL_STABILIZER.tex` and
`AMPLIFIER_FULL_STABILIZERS.tex`, both finite verifier scripts, the current
K-018 proof, and the full K-012 and K-016 criteria. K-018 and the finite-group
criteria already had separate whole-proof reviews; their relevant hypotheses
and applications were checked again here. The local conormal convention was
compared with P-F23 and the explicit pullback convention in P-F60/P-F65.

Executed both finite verifiers unchanged. They passed: the gadget has Lie rank
190, both required coverage conditions, 22 complete zero-weight edges, and
exactly one antipodal pair in the second factor; the dimension-nine tensor has
Lie rank 241 and fixed quotient tangent dimensions 1 and 4 at orders 512 and
256. This is a replay of the supplied scripts, not independently authored
arithmetic. Their integer operations reduced modulo 10007 have no machine
integer overflow in these calculations. Root separately checked the main
finite arithmetic.

## K-019

The positive margin-one representative is critical and concise. Independence
of the 25 incidence columns makes every nonzero choice of coefficients
diagonally equivalent, so the coefficient-one Lie-rank certificate applies
to the critical representative. Rank 241 leaves exactly the unavoidable
two-dimensional scalar Lie algebra.

The displayed simple spectra make the centralizer diagonal. The exact
diagonal group and primitive determinant character from K-018 therefore
satisfy K-012; its antipodal-free factor hypothesis is met. This proves the
full group, rather than only its diagonal subgroup. Faithfulness of the
determinant character implies that the determinant-one stabilizer is precisely
the ineffective scalar subgroup. Luna's slice theorem gives the stated smooth
effective quotient and tangent quotient.

Exactness of finite-group invariants yields dimensions `25-24=1` and
`30-26=4`. The latter includes the additional two dimensions in the adjoint
centralizer caused by the second-factor collision modulo 256. Smoothness of
fixed schemes in characteristic zero gives an actual local four-dimensional
fixed component at order 256. Thus the claimed failure of the universal
one-dimensional-component pattern is justified.

The complete order-512 fixed tensor space, strict positive unique margin
solution, diagonal transitivity, and orbit-stabilizer grading computation
give the asserted single dense grading orbit and density-one curve. The
moving-normal factor uses the source pullback convention, so its displayed
eigenvalues are correct; it is only a local contribution.

## K-020: the Lie gluing argument

For an output with one new coordinate and two strictly old coordinates,
only variation of an old edge can contribute; freeness gives at most one
source for each fixed pair, and coverage forces every old-to-new matrix
entry to vanish. The reversed argument uses one strictly old coordinate and
two new coordinates, killing the opposite off-block entries. In particular
each boundary line is preserved, and both old and gadget spaces are invariant.

The remaining variations intersect only in the three-boundary tensor line.
No contribution reaches that line because the old selected edge was removed
and neither support has an edge containing two boundary coordinates.
Hence the variations vanish separately. The gadget's scalar Lie algebra
forces the boundary scalar sum to vanish; restoring the removed old edge
then invokes the old scalar Lie algebra. The scalar values agree on each
boundary line, proving exactly the global two-dimensional scalar algebra.

The induction starts with the separately certified dimension-nine tensor,
not with a falsely assumed minimal Lie stabilizer for the dimension-two
parity tensor. Output 755 uses three new coordinates, its coverage is checked,
and every old coordinate remains covered after deletion because its removed
mass is strictly less than its margin. The recurrence maps the stated interval
strictly into itself and preserves an odd numerator.

## K-020: the finite stabilizer and curve

The boundary character has exact order 256: the unique rational incidence
expression uses `u/256`, with an odd entry, and zero old coefficients.
Consequently the restriction of a primitive new generator is a primitive
gadget generator modulo scalars. Reducing all weights modulo the old period
collapses the gadget block onto the deleted edge and yields a primitive old
generator; the determinant congruence and odd total exponent ensure
primitivity.

A possible new zero-weight edge must collapse to an old support edge. The
deleted edge case is handled by the complete gadget support. Any other old
edge meets the deleted edge in at most one coordinate, so a changed gadget
coordinate contributes a single nonzero eigenvalue difference. This excludes
all spurious edges. The same reduction proves simple spectra and confines
all antipodal pairs to the refined gadget block. Thus K-016 applies in either
parity at every subsequent stage, giving the full stabilizer
`S x mu_(2*256^k)`.

The smooth quotient, fixed tangent dimension one, and density-one grading
curve then follow as in K-019. No classification of other fixed components
or global Hilbert-series pole is asserted or obtained by this proof.

