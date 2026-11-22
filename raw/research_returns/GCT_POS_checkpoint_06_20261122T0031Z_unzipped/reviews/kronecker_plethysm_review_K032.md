# Complete peer mathematical proof review of K-032

Date: 2026-11-22. Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro;
effort not exposed; run GCT_POS.

**PASS.** Read all of `AMPLIFIED_COMPONENT_NORMALIZATION.tex`.
The complete spectra, positive masses, incidence independence and
effectively free point of K020–21/K029 are retained previously checked
inputs. This review independently reconstructs the normalization proof,
the exact coefficient formula and the leading-density deduction. It does
not claim another replay of the new finite coefficient verifier.

## Finite normalization

The centralizer representation is the already checked complete collapse:
one r³ tensor block, five vector blocks and3m−8 one-dimensional blocks.
The outside torus characters are retained, so the latter summands are
not incorrectly treated as full-centralizer invariants.

For a C_h-semistable fixed vector, its closed nonzero C_h orbit has a
moment-zero representative still in V^h. The full SL moment map is
h-fixed because h is unitary. Under the invariant Hermitian identification
it lies in the compact centralizer Lie algebra, and its projection there
is the zero C_h moment map. Thus the full moment map vanishes. This
proves the required nullcone equality; the reverse inclusion uses the
subgroup relation. No reductivity or smoothness claim about a quotient
is needed here.

Surjectivity of the affine quotient turns equality of nullcones into
sqrt(A_+B)=B_+. The quotient B/A_+B is finite dimensional. Lifting a
homogeneous basis and inducting on degree proves finite generation as
an A-module. This supplies the stated finite-restriction result directly,
rather than importing the general theorem as an unchecked step.

Over the effective-free quotient open, every SL orbit in a fibre is
closed: a nonclosed orbit would have a lower-dimensional closed boundary
orbit, impossible when that closed orbit already has maximum effective
group dimension. Two fixed representatives therefore differ by g in SL³.
The full effective stabilizer has injective determinant character, so
g^(-1)hg equals h modulo the scalar kernel. Every factor spectrum has
one unique eigenvalue of multiplicity r>1; a scalar preserving it must
be1. Hence g centralizes the actual h and the fibre consists of one
C_h orbit. A finite generically one-point morphism has function-field
degree1 in characteristic0. The invariant ring is normal, giving the
claimed normalization exactly.

## Graded coefficients

Characters of L/C_h are integral powers of the three full determinants.
The scalar action on homogeneous degree d forces all powers equal to
s=d/n, hence s is a nonnegative integer. Independent prefix incidence
columns give the unique degree vector: s times the mass vector, plus
s(r−1) on the selected edge. The sum is ns. The reduced denominator M
of rho forces M|s; this also suffices for every assigned degree to be
integral. No positivity of the resulting invariant multiplicity is
asserted merely from that integrality.

The tensor block has the ordinary three-factor Schur–Weyl decomposition.
The two vector powers in the first and third blocks decompose by Pieri
into two-row partitions with multiplicity1. Their complements in (s^r)
are exactly (s^(r−2),s−j,s rho+j); the middle complement is
(s^(r−1),s rho). The range j≤s(1−rho)/2 ensures these are partitions.
All three sizes are s(r−1+rho). The determinant multiplicities are1,
so summing the ordinary Kronecker coefficients gives precisely the
displayed formula, including degree0.

## Leading term and limitation

The normalization and component have dimension
r³−3r²+5r−2=343l³+14l+1. The finite birational quotient B/A is supported
in dimension at most d−1 and both rings are supported in M-divisible
degrees. Therefore it cannot affect the coefficient of (1−t^M)^(-d).
Hilbert–Serre gives the positive rational leading density e_l without
assuming degree-semigroup generation in degree1.

At a generic effective-free point the ambient quotient and fixed locus
are smooth. The moving quotient tangent representation gives exactly
the stated determinant ratio E_l in the already specified point-pullback
convention. Rank controls the top Hilbert coefficient of a coherent class
on an irreducible component, hence e_lE_l is its order-d contribution.
Every moving eigenvalue is a nontrivial dyadic root, making E_l a unit
at every prime over3. Cyclic permutation preserves both grading and
moving representation, so a triple contributes3e_lE_l and has valuation
1+v3(e_l).

Neither the density e_l nor its valuation is computed. The proof explicitly
retains the conductor and lower moving-class terms, which can contribute
to the simple Laurent coefficient. Thus this does not establish an
exact-M pole or a strict-index estimate. No such conclusion is inferred
by this review.
