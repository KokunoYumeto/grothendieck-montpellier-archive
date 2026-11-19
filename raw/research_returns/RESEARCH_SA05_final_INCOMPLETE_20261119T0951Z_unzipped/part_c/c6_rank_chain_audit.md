# Independent chain-level source audit for the conditional C6 rank route

Recorded 19 November 2026, 07:14 UTC, by /root/part_c.

We opened the complete primary PDF of Takeshi Saito, *Weight spectral sequences and independence of ell*, dated 9 June 2003, https://www.ms.u-tokyo.ac.jp/~t-saito/pp/wmr2r.pdf, and read the full Lemmas 2.4.1–2.4.2, Corollary 2.4.3 and Proposition 2.4.4 with proof, author pp. 33–36.

For a rational algebraic correspondence on the generic fibre, Lemma 2.4.2 chooses one vector-bundle resolution of the cycle closure on the regular semistable product blowup. The Chern characters of its restrictions define algebraic cycles on every stratum, independent of ell; the fixed factorial denominator is harmless with rational coefficients. Proposition 2.4.4 composes these cycles with the stratum pullback and pushforward maps and obtains the required common algebraic E1 blocks for every ell.

For the self-correspondence of codimension equal to the generic dimension, each block preserves the stratum cohomology degree and twist. The monodromy map shifts the spectral indices from $(p,i)$ to $(p+2,i-1)$, preserving the stratum index $p+2i$. Therefore the diagonal correspondence blocks commute with the E1 monodromy map exactly. Idempotence at E1 is unnecessary; the E2/abutment action is the supplied projector.

This source check supports Part D's conditional route from finite-field ranks of algebraic correspondences to ranks of all monodromy powers on homogeneous Chow summands. It is not yet a full written-proof audit of Part D's final reduction and is not an unconditional C6 theorem or a converse to the named finite-field conjecture.

## Complete written-proof audit, 07:18 UTC

We subsequently read every line of part_d/c6_rank_conjecture_reduction.tex. The full proof passes.

The block-image formula computes the induced cohomology-map rank because projection to the first target has image equal to the outgoing differential image, while its kernel is the image of cocycles plus incoming boundaries. Padding $H^j(Z)(t)$ by the top cohomology of $\mathbb P^{T-t}$ puts every summand of a common weight in a common cohomological degree and twist. Additional degree-zero projective-space factors equalize dimensions. Thus all block entries form one fixed rational algebraic correspondence on a finite disjoint union, and no algebraic projector onto a differential kernel is required.

We also read Saito's Corollary 1.2.6 and its preceding semistable-base-change construction. Its quantifier allows every finite extension containing one fixed initial extension, so choosing a Galois extension is justified. The projector transferred by the alteration is an algebraic idempotent because proper pushforward after pullback is multiplication by the generic degree.

The spectral-sequence rows have distinct pure weights, hence degenerate at E2. For a chosen Frobenius, generalized eigenspaces separate different weights even without Frobenius semisimplicity. The identity $FNF^{-1}=q^{-1}N$ sends the weight-$b$ primary space precisely to the weight-$(b-2)$ space. Therefore the sum of the ranks of the associated-graded $N^r e$ maps equals the actual rank of $N^r e$. This is stronger than a generic assertion about a filtration-preserving nilpotent, and the Frobenius relation is exactly what makes the step valid.

Once all monodromy operators vanish, the same semistable extension kills inertia on every realization. Saito's common alternating trace theorem, combined with the homogeneous algebraic projector, then gives common individual inertia traces. Averaging over the common finite inertia quotient gives invariant dimension equal to the entire rank, proving original-base unramifiedness.

The primary van Dobben de Bruyn PDF was independently opened: https://arxiv.org/pdf/1808.00119, published version. We read Theorem 1, Definition 4.1, Theorem 4.6, and the complete Theorem 5.1 proof, pp. 17–18. That proof identifies ranks using common Künneth cycles and exterior powers in even degree versus symmetric powers in odd degree. Finite disjoint unions are explicitly allowed as smooth projective schemes. The citation should include Theorem 5.1 for this directly used implication.

The conclusion remains conditional on the independent finite-field homological-equivalence conjecture. We do not assert its converse, do not extend the argument to nonalgebraic absolute-Hodge or motivated projectors, and do not treat this result as a complete resolution of the user's general C6 alternative.

## Later scope changes, recorded 07:57 UTC

The preceding paragraph records the scope of the algebraic proof at 07:18. The integrated version subsequently weakens Chow idempotence to homogeneous cohomological idempotence of a rational algebraic correspondence. The altered projector is then idempotent on cohomology and E2, which is all the proof needs; no equality of its square in the Chow correspondence ring is asserted.

A separate, fully written and independently audited construction now extends the sufficient finite-field rank hypothesis to André motivated projectors. It uses whole-product Lefschetz inverse expressions and finite graph constraints, and is recorded in c6_motivated_operator_independent_audit.md and part_d/c6_motivated_rank_reduction.tex. This is an additional argument, not an inference from the original algebraic correspondence theorem alone. The unconditional general C6 claim and a converse to the named finite-field rank conjecture remain unproved.
