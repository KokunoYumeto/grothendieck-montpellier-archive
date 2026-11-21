# THETA3-C23 independent whole-proof review

**Result: PASS, after the stated local-deformation precision edits.**

Reviewer: GPT-6 Astra Pro, independent sub-run `/root/theta_032`, 2026-11-21. The inherited effort label is not exposed. This is a mathematical proof and source-scope check, not a formal verification certificate.

I read the entire revised `paper_C23.tex`. The proof starts with explicit good-model hypotheses at the fixed prime. It does not replace them with a spreading-out assertion.

## Integral extension and exact cycle

The Neron mapping property extends maps from the smooth model and homomorphisms of the auxiliary abelian varieties. The Picard restriction argument is correct for the smooth proper models with geometrically connected fibres used here: regularity makes closed generic divisors Cartier, and the only vertical prime divisor is the integral special fibre, which is principal. Thus the generic line bundles extend uniquely up to isomorphism. Normalizing each line bundle on the product removes its two pure Kunneth components; the original sum is unchanged because its class was already purely mixed. The dual-variety universal property and zero-preserving rigidity produce actual Poincare correspondences.

The cycle formula has relative dimension g-n after 2n first-Chern operations on a variety of relative dimension n+g. Proper pushforward has codimension n. On the generic fibre, the projection formula gives the exact A6 cycle and retains its sign and nonzero scalar. Refined special-fibre Gysin commutes with the specified Chern operations and proper pushforward. Smooth proper base change preserves its nonzero prime-to-p cohomology class. No integrality of the algebraic coefficients, or constancy of the divisor-generated subalgebra across specialization, is inferred.

## KR comparison

The revised text fixes an ambient deformation over A, works in the nilpotent-p divided-power deformation category, and labels the CM eigenspace by subscript zero. Under those conventions the Grothendieck-Messing obstruction is the stated map between two rank-one modules. Its vanishing is the lifting criterion. A homomorphism extending on an entire constant family has zero obstruction, so that homomorphism alone cannot define the desired proper special divisor in a varying unitary moduli problem.

For flat closed subschemes in a common flat ambient space, the ideal is saturated with respect to the uniformizer. Equality after inverting the uniformizer therefore implies integral equality. If the divisors are Cartier, their local equations differ by units and their two-term perfect complexes, hence the derived tensor products, agree. The example (t) versus (pi*t), evaluated along t=pi, correctly gives lengths one and two even for regular-sequence intersections; the second divisor has a vertical component and is not flat.

A full-rank unitary KR cycle has empty horizontal part by the signature argument in Li-Zhang Lemma 2.10.1. Derived pullback, tensor product and proper pushforward preserve generic vanishing. They cannot turn that vertical object into the A6 class with nonzero generic cohomology. A horizontal stage plus a separately identified vertical intersection is therefore required for this kind of comparison.

## Primary source checks

- Kudla-Rapoport I, Proposition 3.5 and equations (3.2)-(3.3), author-preprint pp.15-16: full relevant proof read.
- Li-Zhang, Lemma 2.10.1, p.15: full signature proof read; section 11.2, pp.75-76: model scope read.
- Stacks Project, Tags 0AG0, 02TA, 0B73, and the relevant portions of 02T7 and 0AYA: factoriality, proper-pushforward Gysin compatibility and Chern/Gysin compatibility checked.
- Milne, *Abelian Varieties*, v2.00 (2008), Remark 8.7(c), p.37, and Corollary 16.2(a), p.67: exact universal property and zero-preserving rigidity statements read on the official PDF.
- Conrad, *Minimal models for elliptic curves*, Definition 5.1 and Example 5.3, p.13: previously read in this same run for C19.

The original external theorems remain cited background; their complete foundational proofs are not claimed to have been re-proved here.

## Checked subsequent additions

I also read the entire balanced-biextension addition, its explicit CM polarization/idempotent representative construction, and the full Artinian-local line-bundle-lift refinement. All pass at their stated scope. I visually read the original SGA7 I Expose VIII sections3.1-3.2, printed254-255, and Expose VII Corollary2.9.4/Example2.9.5, printed174-175. The latter source explicitly identifies birigidified line bundles on a product of abelian schemes with biextensions, so the lifting refinement does not need to assume the addition laws separately. Order-linearity is then forced by the independently checked nilpotent rigidity argument. The explicit representatives use the conjugate-dual target action; the actual tautological PEL action and signature are still a separate match.
