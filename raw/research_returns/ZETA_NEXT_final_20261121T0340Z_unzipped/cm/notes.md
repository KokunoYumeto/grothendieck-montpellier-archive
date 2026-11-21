# CM consequences branch — completion notes

Date: 21 November 2026 (Europe/Berlin). Agent: `/root/cm_effectivity`, GPT-6 Astra Pro, inherited reasoning effort; numerical runtime effort setting is not exposed.

## Status

NC01–NC04 are proved relative to the stipulated Alpöge theorem and the explicit root-branch residue result NX02. A whole-proof targeted reread found no gap. The parent is asked to independently check the same-field maximal-order replacement and central order index argument in NC04.

The root communicated the final residue input

κ_E > 1 / [173 [E:Q]! log D_E],

and κ_E > 1/[173 log D_E] when E is normal. Root owns the verification of this input from Stark; my branch uses its exact constant and independently checks its algebraic consequences. Stark Lemma 9 was visually verified by root from original pp. 145–146; its coefficient 16g! is also read directly in Wei Prop5.4, p.21.

## Findings

- **NC01:** Relative class-number formula plus Louboutin's explicit residue upper bound cancels regulators. It gives an explicit lower bound c_g D_E^(1/4)/(log D_E)^g for h_E/h_F and hence h_E. Explicit c_g and epsilon conversion are in the paper, including a discriminant cutoff for h_E <= H. For normal E, multiply c_g by (2g)!.
- **NC02:** Wei Prop5.3, Stark Lemma9, averaged Colmez, and a concrete universal height lower bound give h_F(A) <= a_g log D_E+b_g with a_g=2^(g−1)(75/2+16g!), b_g=4g(2^g−1). The height normalization is explicitly reconciled: h_Wei=h_F+(g/2)log π. The period theorem's displayed positive bound 16h_F+49g implies h_Wei >−4g.
- **NC03:** Count integral ideals by N² ζ_E(2)<2^(2g)N² and use fully explicit Gaudron–Rémond. This gives a deliberately coarse explicit exponent 1/(16384g³), including an explicit multiplicative constant.
- **NC04:** A same-base-field maximal-order replacement (Rémond 2017 Thm1.1) and direct-factor theorem (Thm1.2) handle all special points. Maximal factors supply effective field-discriminant bounds and logarithmic heights. A degree-N isogeny B→A gives N O_center⊂ZEnd(A), yielding the explicit all-CM exponent 1/(28672g⁴).

## Approaches tried and resolved

1. Direct numerical substitution into Tsimerman's statement would leave unspecified isogeny constants. Resolved by using Gaudron–Rémond, **Polarisations et isogénies**, Duke163(2014), Thm1.4 (p2060), constants p2058. The similarly numbered theorem in the CMH paper is elliptic only; this locator ambiguity was corrected during source checking.
2. Individual Colmez would leave a separate conjectural input. Resolved by averaging over all 2^g types and using the uniform lower height bound; the arithmetic is Wei's Prop5.3 with explicit coefficients.
3. A generic reduction of nonmaximal orders through isogenies whose field extension depends on the conductor could be circular. Resolved by Rémond's 2017 theorem, which works over the same base field. Then explicit GR controls a new isogeny using the height of the maximal-order variety.
4. Original Tsimerman's theorem for all points reduces via a torus/class-group image argument. The present quantitative proof instead uses maximal-order replacement, primitive bounds, and a central order index. This produces constants directly and needs no unexplained effective refinement of the torus theorem.
5. A local partial-paper PDF compile was attempted and failed before reading TeX: `pdflatex.fmt` is absent, and fmtutil reports no configured formats. This is a build-environment limitation; the requested output is LaTeX. Parent may use another engine. No compiled PDF is claimed.

## Source checks

- Louboutin CJM53(2001), Theorem1(1), p1195: upper residue bound; Eq(21), p1200: relative class-number formula. Eq(21)'s square root was visually checked in a rendered page.
- Wei arXiv:2111.00617v1, p8 (height), pp19–20 (Theorem5.2 and Proposition5.3), p21 (Stark Lemma9 threshold). Page20 equations were visually checked.
- Yuan–Zhang Annals187(2018), p534 (normalization) and Thm1.1 p535 (averaged identity) checked directly from the published paper.
- Gaudron–Rémond CMH89(2014), Thm1.1 p345 and §2.3 pp351–352: original-height lower bound and normalization.
- Gaudron–Rémond Duke163(2014), constants p2058 and Thm1.4 p2060: verified from author PDF and rendered constants page.
- Tsimerman Annals187(2018), §2.2/Prop2.2 p382 (CM ideal classes); Lemma4.1 p384 (bounded definition extension); Thm4.2/5.2 p385 (targets).
- Rémond Rev Mat Iberoam33(2017), author preprint pp1–2: fixed-base-field convention and Thm1.1/1.2. Read proof of Thm1.1 in Prop2.3 p6 and exact statement of Thm1.2; these are cited known results, not claimed independently re-proved.

## Programme scope

The supplied SA06 intake does not assign a cote-and-scan to B.4a–B.4e, so no such locator is fabricated. The exact locator in INTAKE_ZETA_TWO §5.4 is cote15 scan70 for SA06 A.8a only. Related A.8c has an undefined ring R and no separate cote/scan locator supplied; sharper quadratic bounds remain ZETA_TWO IA02/IA03. Cote60 scans3–9 and SGA6 ExpV §2/(7.1.1) concern the determinant/λ-ring framework carried through ZETA_TWO ZT08, not the new numerical inequalities.

The new lower class-number bound makes bounded-class-number discriminant finiteness effective. It is not an upper bound for the sufficient lift power in SA06 B.4e. Root NX04 independently supplies an unconditional elementary upper class-number bound for that direction. Full RH for general nonabelian Artin factors, the non-CM L-functions, and the individual Colmez identity are not consequences of this argument.

## Computational audit

`constant_audit.py` evaluates constants in log scale for g=1,...,8 and verifies rational exponent identities. Its finite sampling of the calculus maxima is a numerical check, while the paper gives the exact calculus proof. This is **not** a formal certificate.


## Follow-up review and AO scope

2026-11-21T04:16:41+01:00 — Read NX01–NX04 in full and wrote normal_review.md; no mathematical defect found. Exact closure exponent verified against original Stark p143. Added a scoped paragraph to findings.tex: NC04 makes the requested orbit input effective; the original 2018 full-AO proof also uses counting and family-reduction steps. For Y(1)^n, Binyamini2020 explicitly gives the effective replacement after Dirichlet GRH removes the exceptional quadratic field. This is a proof-scope statement, not a claim that no broader effective AO result exists. Binyamini2022 ForumMathPi10 e6 Thm7 §7.2 independently says its sole ineffective constant for modular powers comes from Siegel; inspected but not needed as an added citation.

2026-11-21T04:22:15+01:00 — Added and reread the complete NC01 proof after quadratic strengthening: exponent1/2−epsilon retained for g=1, without changing uniform orbit constants. Completed targeted whole-proof challenge of NX-L02, documented in lambda_L2_review.md; no remaining gap found after noetherian-comparison clarification and flatness explanation.

2026-11-21T04:31:40+01:00 — Final wording check completed: NC04 keeps separate centre field factors for separate simple isogeny components even when fields are isomorphic; the polarized-field compositum preserves s_g; cote15 scan70 is attributed only to A.8a after rereading INTAKE_ZETA_TWO §5.4. All mathematical constants are unchanged. Final local NX-L02 clarifications checked and proof-block hash matched; see lambda_L2_review.md supplement.
