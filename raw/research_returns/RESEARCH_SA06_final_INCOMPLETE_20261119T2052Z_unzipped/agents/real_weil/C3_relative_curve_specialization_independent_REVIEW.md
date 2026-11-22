# Independent complete review of the relative-curve specialization countermodel

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode, run `/root/component_families`; effort setting not separately exposed. Mathematical review was completed during the checkpoint22 freeze; the full post-checkpoint text was reread after thaw on 19 November 2026. **PASS for the stated auxiliary relative-curve countermodel; no main-gate movement.**

Reviewed the entire `agents/cycles/notes/relative_curve_specialization_countermodel_1915.md`, including RC.1–RC.4, the marked proper K1 family, finite-extension descent, the relative vertical residue, all limitation/source paragraphs, and the post-checkpoint clarification receipt. Final reviewed SHA256: `b975ac4c788dbef3ecb90bdaf53052cf9ef939af2d4ee69efde8ff817a54f866`.

## 1. Ordinary proper relative families

The two displayed elliptic equations are smooth in their stated characteristics, including the odd-characteristic equation in characteristic three. The generic point q over the algebraic closure of the elliptic function field is nontorsion: all geometric points of each finite torsion group scheme are already algebraic over the algebraically closed constant field. Thus O(q−0) remains nonzero after tensoring the Picard group with Q.

For the actual fibre of K(A) to K({0,q}), the rank/determinant description of K0 of a smooth curve gives the surjection onto Pic(A)_Q with exactly the stated K1-image kernel. Clearing a denominator in the relative class itself makes its component restriction zero in integral K0(P), so its determinant is actually trivial on both marked parameter sections. This step would be insufficient if denominators were cleared only after taking determinants, but the final text explicitly clears them in the relative group.

Normalizing by the fibre at the base point gives a morphism f0 from the proper parameter curve to the elliptic Picard variety. The normalized Poincare property and the second marked trivialization imply f0^*N_q=O. A nonconstant morphism between the smooth proper curves is finite flat even if inseparable. The finite-flat determinant norm gives N_q raised to the positive degree as the trivial bundle, contradicting nontorsion. Therefore f0 is constant and every actual ordinary proper relative relation has zero component Picard image. Killing the entire component kernel as well leaves exactly Pic(A)_Q. The quotient is not merely a universal regular quotient, and no unproved identification with such a quotient is used.

## 2. The higher proper family and finite field of definition

The already audited marked-family lemma VE applies with the two marks and provides an actual K1 class on a fixed smooth proper curve with literal zero marked restrictions. Exactness of the relative fibre supplies an actual relative lift; no uniqueness of that lift is required.

All classes and equality witnesses involve finite-presentation data and descend through the filtered system of finite extensions of k0(u). After increasing the finite extension if necessary, the proper parameter, its two rational endpoints, the relative lift, and the endpoint relation are all defined there. Hence the descended class s_K is itself an actual element of the proper-relation subgroup over K. The final text explicitly includes this point and uses only that finite extension. It does not assume the existence of an unqualified residue map on the entire algebraic closure.

## 3. Relative residue and the nonzero target class

For the chosen extension of the u-adic valuation, the residue field is k0 because it is algebraically closed. The two ambient schemes A×R and {0,q}×R, their special fibres, and the vertical immersions satisfy regular purity. The vertical equation remains a nonzerodivisor after marked-section pullback, so Tor-independent base change identifies the map of support spectra with the actual map K(A) to K({0,q}). Taking its fibre yields the claimed relative residue target. No singular purity theorem has been substituted.

The line bundle is defined over the constant field, and the product boundary of the unit u is its valuation e. Projection to the component group therefore gives e([L]−1). Dividing by e over Q leaves the nonzero class L. All choices of the relative lift are immaterial to this component calculation: their changes lie in the component kernel, which is explicitly killed in the target. The ordinary proper relative subgroup has zero Picard image by the preceding complete argument. Thus the descended proper K1 relation has nonzero normalized residue in the full stated target quotient, and a normalized residue cannot descend from that proper K1 quotient.

## 4. Scope and source certification

This is an independent mathematical reconstruction of the entire typed proof. It reuses the previously fully audited VE marked-family result, regular vertical localization, filtered-colimit compatibility, Poincare representability, and elementary finite-flat norm identities. It does not claim a fresh full reading of all Thomason–Trobaugh or Weibel proofs during this audit. No numerical computation or TeX build was needed or performed.

The result excludes the proposed general formal specialization principle for this marked-curve relative K-functor. It neither embeds that functor as a retract of a negative exceptional SNC surface nor controls additional proper families on such a surface. Consequently it is not a counterexample to UK.7, to C.3bt, or to the main C.3 claim, and it does not reduce or move the main gate. No priority claim is made.
