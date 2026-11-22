# C.3bp exact source and scope audit

The final proof is `C3_SNC_mixed_Albanese.tex`, equations MA.1–MA.12. The unchanged audited draft is preserved in `output/C3_SNC_mixed_Albanese_audited_draft.tex`.

## New primary input actually read

The Stacks Project, Section 48.27, Tag 0FVU, <https://stacks.math.columbia.edu/tag/0FVU>: Lemma 48.27.1(5),(7), Lemma 48.27.5(4), Remark 48.27.6, with the relevant complete proofs. This gives smooth proper Serre duality and the canonical sheaf used in MA.6. The bibliography key is the existing `D_Stacks0FVU` in `agents/real_weil/C3an_references.bib`; no duplicate entry was created. Parent and both peers independently reread this exact primary section.

At each smooth cut Y of dimension n>=2, H¹(Y,L^-b) is dual to H^(n-1)(Y,omega_Y tensor L^b). Serre vanishing applies at that particular stage because n-1>0. There is no Kodaira-vanishing claim, characteristic restriction, or standard-conjecture input.

## Exact inputs reused from C.3bo

- Milne, J. S. (2021, June 12). *Jacobian Varieties*, official author version, <https://www.jmilne.org/math/xnotes/JVs.pdf>. Lemma 6.9 and its complete proof, Remark 6.10(c), author p.23, were actually visually inspected for C.3bo. The minus sign is retained unchanged. The local PDF and p.23 PNG are retained in `sources/`; key `D_MilneJacobians2021` already records the exact new readings. No second visual reread is claimed for this extension.
- Stacks Tag 01XO, Lemma 30.17.1, full Serre-vanishing statement/proof; key `frC3azStacksSerre`.
- Stacks Tag 0B5V, Lemma 30.17.2, including its forward proof of finite pullback ampleness; key `frC3beStacksFiniteAmple`.
- Stacks Tag 0FH7, the prescribed-point Bertini construction in the **proof** of Lemma 45.8.3; the lemma statement itself is a divisibility assertion. Key `frC3azStacksBertini`.
- Stacks Lemma 30.17.5, nilpotent invariance of ampleness, key `rootStacks2026NilpotentAmple`, already checked in C.3bm.

C.3bn supplies the exact point comparison and equality of actual ordinary cycle-family relations with actual proper perfect-family endpoint relations. It is used in its stated resolved algebraizable positive-characteristic scope. Perfect pushforward from a component into singular E is not assumed; the family is first pushed into the fixed regular Z times its proper parameter.

## Limited computational reuse

MA.9 has the same formal block expansion as AM.8. The existing 25-entry C.3bo polynomial certificate is reused without a rerun. It verifies matrix algebra only. No finite computation certifies mixed intersection theory, Picard restriction, actual family lifting, or resolution existence.

## Scope

The intrinsic isogeny is valid in every characteristic under the explicitly supplied projective SNC and negative ample combination hypotheses. The ordinary top-quotient identification is only in C.3bn's characteristic-p resolved algebraizable scope, with SNC additionally imposed. No existence theorem for high-dimensional resolutions, no vanishing of component Albanese kernels, no unrestricted proper-family gluing theorem, and no originality or priority claim is made.
