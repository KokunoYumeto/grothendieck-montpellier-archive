# Deposit sheet

## Title

The arithmetic quotient of the profinite Grothendieck–Teichmüller group

Subtitle: Invariant characters after Ihara, Enriquez, Nakamura and Schneps

Authors: left blank for filing.

## Filing and review state

No external deposit or publication has been performed. The paper number and permanent work page are reserved for assignment by the owner. The mathematical check types and limitations are recorded in CHECK_EVENTS.tsv; no human check is claimed. Open mathematical questions are stated in the paper and QUESTIONS.tsv.

## Abstract

Ihara extended the Kummer cocycles to the profinite Grothendieck–Teichmüller group, Enriquez proved their distribution relations, and Nakamura and Schneps related the cocycle of two to the Teichmüller tower. Starting from the established normalized–Galois decomposition, we identify the arithmetic quotient and the relative abelian obstruction to equality with the Galois group. We compute the entire invariant Galois character target at every prime by explicit corrected cup products. At prime two, finite cyclic-cover homology lifts every target character to full GT, proving that the quadratic restriction map is surjective with an explicit linear section. The quadratic character space and its arithmetic restriction image both have countably infinite dimension. Using Willwacher's characteristic-two free generators, we prove that the full group and its Galois subgroup have the same dyadic free-group action, with image the free pro-two product of a group of order two and $\mathbf Z_2$. Every integral leading Lie lattice is attained arithmetically. Simultaneously removing this action, all rational Kummer coordinates, the entire coefficient-two cubic CM image and all the chosen corrected cup-product characters preserves the full relative abelian quotient. For its maximal pro-two quotient one can further remove every single-prime word action and both odd-primary CM images. An exact real-unit square-class criterion then determines further arithmetic CM images and permits their simultaneous removal, while preserving the relative obstruction and original character kernel. The local determinant is governed by the cyclotomic relative class number. Global Frobenius elements fill the local deficits at degrees twenty-nine and one hundred thirteen, including the finite signs; at degree one hundred sixty-three an explicit unit identity proves an arithmetic index of four. The latter full image has two possibilities, separated by a fixed finite-word test; the larger one would give a quotient of order twelve. An odd-inertia argument eliminates the conjugation obstruction for every collection of CM scalar kernels, including the infinite collection. Their full and arithmetic images are exact products even when individual images remain unknown. Extending an intrinsic invariant relative character is therefore equivalent to the vanishing of its relative central extension class. The quadratic restriction image is completely determined; its relative kernel remains open. The corrected adelic modular frames have exactly their joint Galois image. We determine its overlap with rational radicals, prove the normalized harmonic and cubic comparisons, and compute the exact joint odd CM image. At every odd coefficient prime, all arithmetic target characters survive the common kernel of the rational, single-prime, CM and finite-abelian-cover homology realizations; these realizations therefore do not provide the missing odd-prime lifts. We also construct explicit relative quadratic characters whose vanishing is undecided. The mathematics and text were produced by GPT-6 Astra Pro (ChatGPT Pro mode), with independent same-model re-proofs and targeted checks; no human has checked them.

## Subject and keywords

Arithmetic fundamental groups; profinite groups; Galois representations; complex multiplication.

Grothendieck–Teichmüller group; invariant characters; Kummer cocycles; cyclotomic abelianization; Magnus coefficients; CM reciprocity; modular frames; Teichmüller tower.

## Method note

The mathematics and text were produced by GPT-6 Astra Pro (ChatGPT Pro mode). Separate same-model workers reconstructed main statements before reading their authored proofs; complete comparisons then checked the written arguments, conventions and cited hypotheses. The accompanying statement-level records distinguish complete reconstructions, partial attempts, proof-informed checks and independently implemented calculations. They also disclose permitted background results, source pointers and normalization hints. Earlier partial attempts have not been relabelled after later successful checks. The exact cubic frame identity and its finite-character consequences have complete fresh independent reconstructions. The frame proof includes the full profinite topology, identification of the descended parameter, based signs and final central correction; its general nonzero-Kummer variant is not asserted. The full harmonic beta comparison and its residue-character assertion also have a complete fresh independent reconstruction, accepted after a full comparison with the authored proof. The earlier harmonic attempt remains partial at the geometric comparison. The exact scope of each check is recorded with its statement and file digest. Finite computations use exact arithmetic and explicit reconstruction programs. They support the stated finite calculations; they do not replace the arguments passing to full profinite groups or infinite products. The three stipulated background results are cited rather than reproved. Current independent workers used the same model, with effort setting not exposed. The cited background notes record checks by Claude Fable 5.2 and Claude Opus 5.5 at effort max. No human has checked this paper. The text and original programs are dedicated to the public domain under CC0 1.0. The workbench is <https://github.com/KokunoYumeto/k-theory-and-galois-groups-workbench>; the permanent records are at <https://github.com/KokunoYumeto/mathematics-workbenches>.

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
