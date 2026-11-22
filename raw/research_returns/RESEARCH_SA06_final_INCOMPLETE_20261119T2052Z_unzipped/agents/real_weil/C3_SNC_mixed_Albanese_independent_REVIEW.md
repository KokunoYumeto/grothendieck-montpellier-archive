# Independent full review: mixed exceptional Albanese intersections

Completed 19 November 2026, 17:55:29 UTC. Reviewer: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; RESEARCH_SA06; run `/root/real_weil`; effort setting not exposed. This is an independent sibling-agent mathematical review, not a claim of a different model family.

**Outcome: PASS for the complete stated scope of MA.1–MA.12.** The audited input is `agents/frobenius/C3_SNC_mixed_Albanese_draft.tex`. No theorem number was assigned by this reviewer. No program or standalone/master build was rerun or certified in this receipt.

## Mathematical checks

1. The one-cycle definition of the Picard-to-Albanese homomorphism is algebraic: normalize each integral curve in a representative and use the Jacobian pullback/pushforward. Equality on algebraically closed points determines the resulting morphism of reduced abelian varieties. The sign is the already checked negative curve-autoduality sign of C.3bo; no sign is changed with dimension.

2. For a smooth projective variety of dimension at least two, Serre duality turns `H¹(L^{-b})` into the dual of `H^{n-1}(ω⊗L^b)`. Serre vanishing applies since `n-1>0`. Consequently successive high smooth connected ample sections induce Picard restrictions with finite kernel. This uses tangent injectivity only to obtain dimension-zero kernel, so no separability or smoothness of the unreduced Picard scheme is assumed. Restricting to the final curve gives a positive multiple of each mixed intersection map as the pullback of its principal polarization. The curve endpoint has no extra cut.

3. In MA.8 the diagonal self-intersection and off-diagonal restriction/pushforward have the same negative sign. The restriction of the globally chosen ample H agrees on both sides of every double stratum. Expanding `d_e^∨ν_e d_e` verifies MA.9 block by block: its diagonal edge terms cancel those from `a_i μ_{-D,H,…,H}`, leaving the required negative normal-bundle block; its off-diagonal terms are exactly the actual intersection blocks. Higher strata create no additional pairwise intersection terms.

4. After a common positive multiple, each summand is a theta pullback. The positive diagonal pieces already give a finite-kernel map to a product of Jacobians; adding the edge pieces preserves that property. Its pullback line bundle is ample, proving the isogeny in every characteristic, including inseparable cases. The argument does not invoke a Lefschetz standard conjecture.

5. The degree matrix is symmetric because H is global. Its off-diagonal entries are nonnegative, and its product with the positive coefficient vector of D is strictly negative by ampleness of −D on every component. The displayed weighted-square identity is exact and proves negative definiteness. Hence exceptional one-cycles span all component degree coordinates over Q.

6. A Poincaré line bundle on `E_i×P`, multiplied by the `d-2` fixed H classes, gives an actual codimension-d family after pushforward to the regular fixed product `Z×P`. C.3bn then places its exceptional restriction in `J_K^d(E)`. This does not use a perfect pushforward from a component into the singular E. The weighted isogeny is surjective on k-points, giving all component Albanese coordinates.

7. The last denominator equality was checked in both directions. Because U lies in both the exceptional image and the actual-family subgroup, an element `j+q` of the common Albanese kernel can be rewritten as `(j+u)+(q-u)` with the two summands separately in that kernel. Thus MA.3 is an isomorphism of the displayed quotients, not merely a surjection.

## Exact source review

Freshly opened and read the full relevant statements and proofs in the Stacks Project, Section 48.27, Tag 0FVU: Lemma 48.27.1(5),(7), Lemma 48.27.4, Lemma 48.27.5(4), and Remark 48.27.6. These give precisely the smooth proper duality used for the negative ample H¹ vanishing. URL: <https://stacks.math.columbia.edu/tag/0FVU>.

The official June 12, 2021 Milne *Jacobian Varieties*, Lemma 6.9 and Remark 6.10(c), author p.23, including its minus sign, was freshly visually and textually checked in the immediately preceding C.3bo review and is reused here. The exact source is <https://www.jmilne.org/math/xnotes/JVs.pdf>. That preceding review also opened the complete finite-ampleness and Serre statements at Stacks Tags 0B5V and 01XO, and the Bertini paragraph in the proof of Lemma 45.8.3, Tag 0FH7. No fresh reread of the whole C.3bn proof is claimed here; its certified endpoint/ordinary-family comparison is the explicit dependency.

## Scope retained

The intrinsic isogeny is valid in all characteristics under its smooth projective SNC and negative ample combination hypotheses. Its identification with the ordinary top quotient is asserted only in the resolved positive-characteristic algebraizable scope of C.3bn. The proof does not establish a resolution in dimensions where none has been supplied, does not extend its component argument to arbitrary non-SNC support, and does not kill component Albanese kernels or the remaining proper-family compatibility problem.
