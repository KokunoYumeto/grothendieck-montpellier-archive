# Independent complete review of normal-base K1 family lifting

**PASS, in the exact fixed-local-base scope. No main-gate movement.**

Reviewer: GPT-6 Astra Pro (OpenAI), `/root/cycles_continuation`, research run RESEARCH_SA06; reasoning effort is not separately exposed.

The entire file `../frobenius/C3_normal_base_K1_family_RESEARCH.md`, including NK.1–NK.10, the point-kernel refinement NK.9a, the scalar-extension limitation and all source-scope declarations, was read and reconstructed. Reviewed SHA256: `72496a0cbf47d83d3796cd7ff3a6e186b5268830e31c0bc9f96337c7341b38a4`.

## Integral rank and determinant

The incidence dimension argument is valid for a generated bundle of rank at least two on the closed smooth integral curve. A nonzero vector in the complement of the incidence image lifts through the coefficient field. Properness over the local base makes the actual zero locus empty, since every nonempty closed subset of that base contains the closed point. The resulting subbundle has locally free quotient, so induction gives the claimed line filtration. The ample-line-bundle hypothesis supplies the vector-bundle description of perfect K0.

For either high-twist section of a line bundle, the fibrewise effective-Cartier criterion applies at every closed-fibre point. The complement of the resulting open locus is again proper over the local base and misses its closed point, hence is empty. The divisors are finite because their closed fibres are finite. Their coordinate rings are semilocal; a rank-one projective module over a semilocal ring is free. Consequently all line twists on their supported perfect classes are trivial.

I checked the twists in NK.3 explicitly. The Cartier sequence gives `[L]-1=[L] [O_D]` for the zero divisor of a section of L. The semilocal restriction makes this `[O_D]`. Subtract for L=M H^n and L=H^n, then multiply by H^(-n); the finite-support twists again disappear. This is exactly the displayed difference `[M]-1=[O_D+]-[O_D-]`. Multiplying by another line difference gives zero by the projection formula. There is no use of purity for a nonperfect coherent sheaf.

Line generation and the square-zero augmentation ideal then make Pic(B) isomorphic to the rank-zero subgroup. Expanding the gamma series of a sum and difference of line elements proves the vanishing of F_gamma^2 integrally. The claimed Adams polynomial follows on the two explicit summands. Neither step assumes a rational eigenspace decomposition on arbitrary K-groups.

## Normal modification, exact sequence and endpoints

For the proper birational map over a normal domain, regular functions lie in the fraction field and belong to every height-one valuation ring; equivalently their finite algebra of global functions is integral over the normal base. This proves g_*O=O. Tensoring the finite affine Cech equalizer over the coefficient field proves the same assertion after the fixed product with P. The elementary projection formula then proves Picard injectivity. Rank and determinant on the source alone suffice for K0 injectivity; no corresponding description of K0 of the regular modification is used.

I reread the entire `C3_fixed_family_negative_K.tex`, including the KST pro-exact sequence, GH nilpotent invariance after inverting p and TT finite-cover descent. Its every-degree fixed-product exact sequence gives NK.8 under precisely the displayed hypotheses. Source K0 injectivity kills the connecting obstruction, and the parameter K1 contribution is the restriction of its actual pullback to Z×P. Thus the whole prescribed K1 class lifts after inverting p, in every dimension covered by these hypotheses.

For a point, exactness applied to the pair (a,0) gives an element of K1(R) whose residue is zero. This verifies NK.9a, including its reverse containment. It does not say that every unit image has zero restriction. Commutative local K1 is the unit group, on which Adams psi^2 acts by multiplication by 2. If the exceptional endpoint is exactly u beta and beta has weight two, the endpoint discrepancy of an arbitrary lift is therefore killed by psi^2-2. The desired product has eigenvalue 8. The coefficient 1/6 in NK.10 is correct, and its application to the actual family gives the literal desired endpoint difference.

## Primary reading and retained boundary

On 19 November 2026 I freshly opened and read the complete printed proofs of Stacks Lemma31.19.9 (Tag062Y), Lemma37.44.2 (Tag02UP) and Lemma37.44.1 (Tag02LS). These supply respectively the local Cartier criterion and the finiteness argument. Their citations are:

- The Stacks Project Authors. (2026). *Relative effective Cartier divisors*, Lemma31.19.9. https://stacks.math.columbia.edu/tag/062Y
- The Stacks Project Authors. (2026). *Applications of Zariski's Main Theorem, I*, Lemmas37.44.1–37.44.2. https://stacks.math.columbia.edu/tag/02LS and https://stacks.math.columbia.edu/tag/02UP

The complete elementary rank-one semilocal argument from the earlier WP audit is reused. That audit also records Tag02M9 as a statement with proof hints, not a printed full proof. The previously completed AE/WP, FF and HK source audits supply the exact generation, perfect-pushforward, localization and operation inputs here. I do not claim a fresh rereading of all KST, GH, TT or Weibel sources in this audit.

The base R remains local and the parameter remains the actual fixed proper curve. R tensor k(u) need not be local. A class on an etale neighbourhood is not automatically extendible to a finite closure; the localization boundary and its trace have not been shown zero. These limitations are correctly retained by the owner. NK.10 also requires the exact exceptional endpoint, rather than merely its component projections. Accordingly this is a complete auxiliary PASS and does not by itself shrink UK.7.

Saved: 2026-11-19T20:10:15.596423+00:00

## Complete final TeX transfer review

At 2026-11-19T20:22:02.734268+00:00 the entire final C.3bv TeX was read, SHA256 `7aa938a79c885b669f2df35f5671aeea8bae3191d4c2c37892abc2c86b766336`. All hypotheses and NK.1–NK.10/NK.9a are faithfully retained. The Cartier identity now displays all twists explicitly; the semilocal triviality and source-unit arguments are expanded without strengthening the conclusion. The TT citation correctly names Corollary3.9 and Proposition3.10. The whole-product lift, residue-zero kernel, conditional exact endpoint, nonlocal-base limitation and unchanged UK.7 scope all pass. No visual-QA claim is made by this reviewer; the owner is inspecting its standalone pages.
