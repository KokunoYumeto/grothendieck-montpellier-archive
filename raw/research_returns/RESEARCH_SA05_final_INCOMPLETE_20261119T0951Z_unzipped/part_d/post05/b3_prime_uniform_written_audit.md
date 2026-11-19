# Independent audit of the integrated prime-uniform proof

Part D, 19 November 2026, 06:42 UTC. Read all of `sections/b3_prime_uniform.tex`, including its smooth-source lemma, arbitrary-base theorem and abelian-torsor corollary. The written proof passes. This is a separate actual read of the integrated text, after the earlier proof-note audits.

## Smooth source

For an open U of a smooth projective geometrically connected Y, the exact boundary sequence gives a finite-rank unit lattice N with finite Frobenius action. The equality H2(Gamma,N)=N_Gamma tensor Q/Z is correct for continuous cohomology of a discrete lattice; rational-coefficient higher cohomology vanishes by finite averaging. The invariant-to-coinvariant map has finite cokernel, so tensoring with Q/Z supplies all of H2 via arithmetic unit cups. Hilbert 90 lifts invariant unit classes.

The Picard calculation separates a quotient of Pic0(Y)(kbar) by a finite subgroup from a finitely generated lattice quotient. Lang's map is surjective on geometric points, and finite-field Galois cohomological dimension one kills H2 of the finite subgroup. Thus the H1 Picard term is one finite group. No spectral-sequence degeneration is assumed. Qin Theorem 5.2 gives the needed whole-prime-to-p geometric group, after the one-prime hypothesis is supplied by Tate and the unconditional divisor splitting.

For a generically finite proper alteration of degree d, Riou's finite-coefficient trace has composite d even when d is not invertible in the coefficient ring. Generic vanishing of a Kummer Pic/n lift proves its trace has zero Brauer image on the regular target, so trace descends to Br[n]. The projection formula identifies the trace of an arithmetic unit cup with the cup of the norm unit. Properness and normality make that norm a global unit. The resulting quotient is bounded by one integer. Its fixed-order torsion is finite because the cup image is divisible and Kummer gives finite Br[h].

Clarity requested and accepted by Part B: an alteration U may have a larger field of constants. Apply the open-projective argument over that constant field; restriction multiplies the arithmetic character by its degree, and multiplication by that degree on the divisible group D is surjective. Hence the cup image is unchanged.

## Arbitrary bases

The perfected h-cover kernel is finitely generated over Z[1/p] itself. One integral unit-lattice matrix and one integral valuation matrix control all primes simultaneously. The integers L, M and N are therefore fixed, not selected separately for each prime. For A=H2(Gm)[1/p] and the divisible cup subgroup C, the image of A/C in the altered Brauer quotient is annihilated by h=LMN. Its h-torsion is a quotient of the finite group Br(T)[h], because the subgroup being divided out is divisible. The kernel is a quotient of the finitely generated cover kernel. Hence A/C is finitely generated.

Localization cannot turn an element of infinite order into torsion. Quotienting by a torsion subgroup also has the exact torsion preimage used in the proof. This verifies that the torsion of A/C is Br(S)[p-prime]/C. Equality of global units yields equality of cup images and the whole prime-to-p relative Brauer conclusion in every relative dimension. No prime-uniform finite-cotype decomposition is assumed.

## Abelian torsors

Let B=A-dual. The zero section splits Rf_*Gm as Gm plus K with K in degrees at least one and H1(K)=Pic(B/S). The truncation Pic(B/S)[-1] to K injects H1(Pic(B/S)) into H2(K), because the next truncation has no hypercohomology in degree one. This is an actual subgroup of H2(B,Gm), in the kernel of the zero-section pullback. It therefore meets the image from the base trivially. Torsion inputs produce actual torsion Brauer classes, so the earlier singular-base torsion-lifting obstruction is absent.

Inversion acts by minus one on Pic0=A and by plus one on the quotient sheaf of algebraic-equivalence classes. Naturality kills the connecting image by two. On prime-to-p torsors the kernel is zero for p=2; otherwise it is bounded by the finite group H1(S,A[2]). This proves whole-prime-to-p torsor finiteness from the already proved relative Brauer conclusion. Relative Picard duality and the inversion identities are Part B's separately opened primary inputs; this audit does not falsely claim an additional primary-source opening.

Finally the existing actual Cech-cocycle descent proof has an integral Z[1/p] kernel bound. On a regular alteration the torsor group is torsion, and its localization is now one finite group by the first assertion. The extension argument gives finite generation over Z[1/p], including the bounded-p nilpotent comparison and finite open-cover step.

## Scope

This is stronger finiteness with the same unresolved surface-Tate gate. The independent irregularity-zero restriction is a different result and is recorded in `b3_irregularity_zero_surface_gate.tex`. Neither argument proves Tate for its remaining surface class.
