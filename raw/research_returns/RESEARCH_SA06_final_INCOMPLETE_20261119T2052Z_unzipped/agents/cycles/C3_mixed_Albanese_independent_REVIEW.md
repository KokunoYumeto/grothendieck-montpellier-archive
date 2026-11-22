# Independent full audit of the mixed exceptional Albanese matrix

Completed **19 November 2026, 17:54:45 UTC**. Reviewer: GPT-6 Astra Pro, `/root/cycles`, run RESEARCH_SA06. Full mathematical/source **PASS** for `../frobenius/C3_SNC_mixed_Albanese_draft.tex`, MA.1–MA.12. No finite computation or wrapper was rerun by this reviewer.

The intrinsic isogeny statement is valid in every characteristic and every stated dimension d≥2. Its ordinary top-quotient application retains the SNC resolved positive-characteristic algebraizable scope of C.3bn. No higher-dimensional existence of resolution, removal of component Albanese kernels, or general vanishing of the residual quotient is inferred.

## Full proof check

The homomorphism associated with a one-cycle is algebraic: a finite signed representative by integral curves can be normalized, and each normalized smooth proper curve supplies Picard pullback and Albanese pushforward. These maps depend on the cycle class, and pointwise equality determines the abelian-variety homomorphism. The minus sign in mu=−kappa is the same curve-autoduality sign verified for C.3bo and does not acquire an extra dimension-dependent sign.

The mixed complete-intersection construction is correct. At each stage the ambient dimension is at least two. Serre duality turns H1(L^(−b)) into the dual of H^(n−1)(omega tensor L^b), and Serre vanishing kills this for a sufficiently high exponent chosen after the preceding cuts. Smooth connected high sections exist in every characteristic. Thus H1(O) restriction is injective at every step, and restriction of reduced Picard varieties has finite kernel even if the unreduced Picard schemes are nonsmooth. The final curve represents exactly the product of the chosen exponents times the mixed one-cycle. Its theta pullback gives a positive multiple of the displayed mixed homomorphism as a polarization. The n=1 convention is correct and agrees with the principal curve polarization.

For an arbitrary first divisor M, the construction as a difference of ample divisor classes proves symmetry without falsely calling M ample. The common H on E is used exactly where needed: its two restrictions coincide on each double stratum. The off-diagonal zero-cycle has c1(L_i|C) times H^(d−2), of codimension d−1 on the (d−1)-dimensional stratum. Its Albanese pushforward is dual to Picard restriction. I independently expanded the weighted identity: the diagonal double-stratum terms cancel and the edge-difference terms produce precisely the negative off-diagonal blocks. Higher strata add no terms to this pairwise intersection identity.

A common multiple of every diagonal and edge mixed polarization is represented by a product of theta line bundles pulled back from actual complete-intersection Jacobians. The diagonal maps already have finite kernel, so the total map is finite onto its image. Finite pullback makes the theta product ample. This proves the isogeny without Hodge theory, standard conjectures, or a separability assumption.

The all-dimensional degree matrix is also correctly typed. Its off-diagonal entry is the degree of H^(d−1) on the double stratum, and symmetry uses the global H. Multiplying by the positive exceptional weights gives strictly negative weighted row sums. The displayed quadratic identity proves negative definiteness and hence rational invertibility. It therefore removes every component-degree coordinate before the Albanese reduction.

The Picard input is an actual family. The normalized Poincare line bundle on E_i times a smooth proper curve is multiplied by the fixed H_i^(d−2), then properly pushed into the regular product Z times that same curve. This is a codimension-d cycle family with the required endpoint difference. C.3bn/AE.13, or the inverse rational Chern character on a finite smooth model, places its restriction in the actual perfect relation subgroup. No perfect pushforward from E_i directly into the singular E is assumed. Surjectivity on algebraically closed points of the proved isogeny supplies every component Albanese coordinate. The last subtraction by u in the common Picard-family subgroup separates the two denominator summands exactly, as in C.3bo.

## Exact source reads

Freshly opened and read the complete Stacks Project Section 48.27, Tag 0FVU, especially Lemma 48.27.1(5),(7), its proof, Lemma 48.27.5(4) and its proof, and Remark 48.27.6: https://stacks.math.columbia.edu/tag/0FVU. These give the smooth proper Serre duality and finite-dimensional perfect pairings used in the successive cuts.

The source reads completed immediately before this audit for C.3bo are reused with their exact scope: Milne *Jacobian Varieties*, official 12 June 2021 version, Proposition 6.1 pp.19–20 and the independently viewed page23 Lemma6.9/Remark6.10(c) sign; Stacks0B5V full finite-ampleness proof; 01XO Lemma30.17.1; and 0FH7's actual smooth connected prescribed-point section construction. No new opening of those same pages is claimed for this later receipt. The complete C.3bn/AE proof was independently audited earlier in this run; its endpoint comparison is used only within its certified scope.

No correction is requested.
