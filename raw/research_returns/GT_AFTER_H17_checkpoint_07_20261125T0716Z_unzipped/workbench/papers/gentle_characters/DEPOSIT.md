# Deposit sheet

## Title

Abelian quotients separating the gentle and full Grothendieck–Teichmüller groups

Subtitle: After Ihara and Harbater–Schneps

Authors: left blank for filing.

## Filing and review state

No external deposit or publication has been performed. The paper number and permanent work page are reserved for assignment by the owner. The mathematical check types and limitations are recorded in CHECK_EVENTS.tsv; no human check is claimed. Open mathematical questions are stated in the paper and QUESTIONS.tsv.

## Abstract

Drinfeld defined the Grothendieck–Teichmüller group by the cycle and pentagon relations, and Ihara's derivation algebra describes their infinitesimal counterparts. Harbater and Schneps identify the group defined by the two cycle relations with symmetric peripheral automorphisms; we use their description to construct its abelian quotients. We compute the indecomposable special derivations in weight sixteen: their dimension is thirty-eight, over both the rationals and the field with seventeen elements. The raw count of possible brackets overestimates their rank by one because of a Jacobi identity. We also give an exact weight-twelve pentagon certificate and a degree-seven integral witness to the independence of the infinitesimal pentagon. A precise linear-algebra formulation identifies the functionals relevant to characters: they annihilate the sum of the bracket space and the pentagon kernel. Using Brown's construction and the all-weight upper bound of OpenAI, with Willwacher's subsequent proof, and proving the required peripheral lifting and filtered group comparisons, we obtain thirty-eight independent characters of order seventeen and countably many independent characters of every finite $p$-power order for each prime $p\geq5$, all vanishing on the full pentagon group. A separate finite-cover construction gives countably many independent quadratic characters with the same vanishing property. We also extend the normalized elliptic-frame character to the whole gentle group and construct an element on which it is nonzero while the action on the third derived quotient is the identity. This character is therefore independent of all the metabelian quadratic characters. The mathematics and text were produced by GPT-6 Astra Pro (ChatGPT Pro mode); the computations were independently reimplemented and the proofs received separate checks by the same model; no human has checked this paper.

## Subject and keywords

Profinite groups; Grothendieck–Teichmüller theory; graded Lie algebras; finite characters.

gentle Grothendieck–Teichmüller group; pentagon; special derivations; Ihara bracket; peripheral lifting; beta characters; elliptic frames; weight sixteen.

## Method note

The mathematics and text were produced by GPT-6 Astra Pro (ChatGPT Pro mode). The finite Lie-space and pentagon calculations were independently implemented in this work; the precise proof-check events are listed at the [permanent records address](https://github.com/KokunoYumeto/mathematics-workbenches). The frame-character construction uses the normalized vanishing theorem of [1]; its extension to all multipliers and its nonzero full profinite witness are proved in Sections 12 and 13. The quadratic finite-cover construction and the deep-frame witness received separate statement-only reconstructions by GPT-6 Astra Pro; the effort setting is not exposed. The full peripheral lifting proof received complete targeted checks; its separate initial reconstruction was partial and is recorded as such. The cited monoid theorem records a proof by Claude Fable 5.2 and a check by Claude Opus 5.5, both at effort max. The cited H17 note records the same two models at effort max for its stated background checks. No human has checked this paper. The text is dedicated to the public domain under CC0 1.0. The associated [workbench address](https://github.com/KokunoYumeto/k-theory-and-galois-groups-workbench) is designated for the program *Gentle derivations and pentagon certificates*, its exact inputs and outputs, and the records.

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
| V. G. Drinfeld; Y. Ihara | GT equations, special derivations, and beta factorization. |
| D. Harbater; L. Schneps | Symmetric peripheral automorphism description, Main Theorem and §1.3. |
| V. A. Dolgushev; J. J. Guynee | Gentle GT terminology and the distinction between finite shadows and full inverse-limit elements. |
| F. Brown | Free odd-generator motivic injection, Theorem1.1. |
| OpenAI; T. Willwacher | The all-weight Deligne–Drinfeld upper bound and the subsequent proof used with Brown's theorem. |
| H. Furusho | Pentagon-to-hexagon implications and the full profinite beta formulation. |
| N. Markarian | Recent restricted pro-two tangent reconstruction, at its explicitly stated scope. |
| A. Garaialde Ocaña; J. González-Sánchez | The integral Lazard correspondence used for the top-weight character construction. |

## Editable project and records

The standalone project is this directory: main.tex, all its local inputs, BUILD.md, and main.pdf. Build with `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` using pdfLaTeX.

Intended workbench: <https://github.com/KokunoYumeto/k-theory-and-galois-groups-workbench>. Permanent-record registry: <https://github.com/KokunoYumeto/mathematics-workbenches>. Neither address has been modified by this work.
