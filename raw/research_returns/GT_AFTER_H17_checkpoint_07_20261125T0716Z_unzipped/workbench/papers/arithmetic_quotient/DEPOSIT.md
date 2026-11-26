# Deposit sheet

## Title

The arithmetic quotient of the profinite Grothendieck–Teichmüller group

Subtitle: Invariant characters after Ihara, Enriquez, Nakamura and Schneps

Authors: left blank for filing.

## Filing and review state

No external deposit or publication has been performed. The paper number and permanent work page are reserved for assignment by the owner. The mathematical check types and limitations are recorded in CHECK_EVENTS.tsv; no human check is claimed. Open mathematical questions are stated in the paper and QUESTIONS.tsv.

## Abstract

Ihara extended the Kummer cocycles to the profinite Grothendieck–Teichmüller group, Enriquez proved their distribution relations, and Nakamura and Schneps related the cocycle of two to the Teichmüller tower. Starting from the established decomposition into normalized and Galois elements, we identify the arithmetic quotient and the obstruction to extending invariant characters. Dividing the integral Kummer cocycles by two gives independent invariant quadratic characters with quartic Kummer restrictions; the invariant space and its restriction image both have countably infinite dimension. We then remove all rational Kummer coordinates and compute successive exact two-adic monodromy images through weight ten, already attained by the Galois subgroup. Their common kernel has no Magnus term below degree eleven. An integral beta measure gives exact arithmetic images in every odd weight and removes the entire dyadic metabelian multiplier. Combining these reductions and removing a primitive mixed degree-eleven coordinate gives a smaller group carrying the same relative abelian obstruction. We determine which of the resulting quadratic characters extend through the earlier normalizations. The full restriction image and relative kernel remain open. The two corrected adelic modular frames have exactly their joint Galois image, giving the quotient associated with the maximal abelian extensions of the Gaussian and Eisenstein fields. We determine its overlap with rational radicals and settle the complete prime-two and exceptional prime-three compatibility. Furusho's nonabelian dyadic identities prove the normalized harmonic comparison. Finite-subgroup centralizers, genus-zero rigidity and the exact cubic distribution relation prove the normalized cubic comparison. The remaining conditions are explicit tame tests. A finite-cover determinant gives another explicit relative character whose nonvanishing is undecided. We also compute a local Brauer invariant and the Hecke conductors at the quartic Kummer layer. The mathematics and text were produced by GPT-6 Astra Pro (ChatGPT Pro mode), with independent same-model re-proofs and targeted checks; no human has checked them.

## Subject and keywords

Arithmetic fundamental groups; profinite groups; Galois representations; complex multiplication.

Grothendieck–Teichmüller group; invariant characters; Kummer cocycles; cyclotomic abelianization; Magnus coefficients; CM reciprocity; modular frames; Teichmüller tower.

## Method note

The mathematics and text were produced by GPT-6 Astra Pro (ChatGPT Pro mode). The quotient, character extension, parity, dimension, simultaneous rational-radical normalization, normalized congruence, individual-frame comparison and conductor arguments received independent same-model re-proofs. The cubic and weight-five divisibilities, exact arithmetic images and further normalizations received separate statement-only re-proofs, including integral coefficient calculations, as well as targeted checks. The prime-two compatibility, exact radical–CM intersection, and exceptional-three division field and relative character also received complete independent same-model re-proofs. The weight-eight exact image and further normalization received a complete statement-only re-proof by the same model; its sharper extension threshold received a second complete statement-only proof using complex conjugation. For weight seven, the initial independent reconstruction proved a weaker upper bound; a subsequent complete targeted check verified the exact bound and the printed full-pentagon certificate by a separate implementation. The finite relative comparison characters received a complete separate statement-only re-proof, followed by a targeted comparison. The normalized dyadic harmonic comparison received a complete separate statement-only re-proof. The exact weight-nine normalization received a complete separate statement-only re-proof, using an integral measure for the upper bound and a separate leading-space calculation. The weight-ten normalization and its extension threshold received a complete separate statement-only re-proof, with a different arithmetic witness and leading-space certificate. The uniform dyadic normalization received a complete proof-informed reconstruction and targeted check, followed by a complete separate statement-only re-proof; the existence of a measure approach had been announced, but its argument had not been disclosed. The primitive mixed degree-eleven reduction received a complete targeted proof check and a separate coefficient recomputation; its statement-only check is pending. The cubic comparison received a complete targeted proof and primary-source check; a separate statement-only attempt recovered its algebraic reduction but did not complete the geometric comparison. The finite CM tests, adelic CM comparison and finite-cover character arguments received targeted proof checks and, where indicated, exact coefficient verification. Each check is recorded with its scope; the effort setting of the same-model checks is not exposed. The cited background note records checks by Claude Fable 5.2 and Claude Opus 5.5 at effort max. These are AI checks; no human has checked this paper. The text and original programs are dedicated to the public domain under CC0 1.0. The workbench is <https://github.com/KokunoYumeto/k-theory-and-galois-groups-workbench>; the permanent records are at <https://github.com/KokunoYumeto/mathematics-workbenches>.

## Location of the eight opening requirements

| Requirement | Location |
| --- | --- |
| 1. Field-recognizable title and credit | Title and subtitle, first page. |
| 2. Abstract: source, theorem, granted inputs, significance, production and checks | Abstract, first page; final sentence states AI production and absence of human checking. |
| 3. Main theorem statements and their meaning | Section1, The question and the results; the displayed theorem statements and following explanatory paragraphs. |
| 4. Why the result matters | Opening of Section1 and the explanatory paragraphs after the main statements. |
| 5. Exact division of credit | Section1 credit and scope discussion, with exact source locators and a separate statement of the present contribution. |
| 6. Earlier and neighboring work | Section1 comparison paragraphs; source statements and dates in the bibliography. |
| 7. Scope and open questions | Section1, alongside the claims; the final questions/scope section gives the remaining obstruction. |
| 8. Proof overview before proofs | Section2, Proof overview. |

## Authors and work carried forward

This table identifies mathematical debts for the owner's filing and correspondence. It is not a record of notifications or endorsements.

| Authors | Work used or carried forward |
| --- | --- |
| V. G. Drinfeld; Y. Ihara | Defining GT relations, Galois inclusion, integral Kummer and beta characters. |
| B. Enriquez | Full distribution relations, Theorem8.1 and Remark8.6. |
| H. Nakamura; L. Schneps; A. Hatcher; P. Lochak | Normalized tower relations and actions; Lochak2025 Theorem5.10 and closing questions. |
| G. W. Anderson; H. Furusho | Arithmetic gamma multiplication and its precise beta formulation; the dyadic comparison. |
| P. Moree; P. Stevenhagen | The rational-radical affine Galois description and its quadratic entanglement. |
| J. S. Milne; M. Papikian | CM ray-class reciprocity, conductor–discriminant formula, and Galois-compatible Tate uniformization. |
| W. Herfort; L. Ribes | Centralizers in profinite free products. |
| I. Marin | Classical degree-three and degree-five Soulé-character extensions through rigidity. |
| A. Schmidt; K. Wingberg | The precise solvable inverse-Galois theorem used for the arithmetic target. |

## Editable project and records

The standalone project is this directory: main.tex, all its local inputs, BUILD.md, and main.pdf. Build with `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` using pdfLaTeX.

Intended workbench: <https://github.com/KokunoYumeto/k-theory-and-galois-groups-workbench>. Permanent-record registry: <https://github.com/KokunoYumeto/mathematics-workbenches>. Neither address has been modified by this work.
