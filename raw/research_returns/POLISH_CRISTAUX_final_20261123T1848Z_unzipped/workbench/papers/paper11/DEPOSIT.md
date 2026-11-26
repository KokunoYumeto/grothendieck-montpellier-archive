# Deposit sheet

Status: local reviewable manuscript; no deposit or publication has been made. The author line is empty, and no permanent work number or commit has been allocated. Complete proofs, the author’s full expert and newcomer readings, all-page visual inspection, primary-source checks, original reruns, and a different exact arithmetic implementation are complete. Separate proof-unseen reconstructions of both even thin-system assertions have been frozen and compared in full, including the stronger supersingular assertion for every even degree at least six. The rectangular main theorem also has a complete separate reconstruction, relative to its two explicitly permitted companion results, and all 569 lines have been compared in full. The final fresh-copy build is clean, and the updated checking note has been read and visually inspected; all other page images are identical to the fully reviewed version. No human verification or publication is claimed.

## Title

Grothendieck’s generic Frobenius ranks on products of elliptic curves, after Cartier and Tate

## Abstract

Grothendieck's crystalline-cohomology notes ask how the generic stable Frobenius rank of hypersurface sections depends on their degree. We determine that rank in every positive degree for every cubed product polarization on a product of two elliptic curves in characteristic two. The answer depends only on the two elliptic 2-ranks and on two parities. It includes every ordinary elliptic curve and every power of two in the polarization degrees. We also determine the rank in bidegree (m,3) for every even m ≥ 6 when the second factor is supersingular. Cartier's operator gives the upper bounds, and Tate's residue duality supplies the matching lower bounds from explicit kernel–cokernel pairings. Cubic sections and nodal images under one-factor étale isogenies transfer these ranks to the required rectangular systems. A separate supersingular bundle calculation gives another uniform sparse family. These are complete linear-system results, with an explicit restriction-surjectivity qualification for ambient hypersurfaces. The mathematics and text were produced and checked by GPT-6 Astra Pro with the scopes stated at the end; no human has checked the mathematics.

## Subject and keywords

Arithmetic algebraic geometry; algebraic curves; elliptic curves; abelian surfaces; positive characteristic.

Generic p-rank; Cartier operator; characteristic two; product polarization; residue duality; Frobenius pushforward; stable rank; nodal curve; étale isogeny.

## Exact mathematical scope

Let the two elliptic 2-ranks be f₁,f₂ in {0,1}, and let ε(t) equal one for even t and zero for odd t. For every positive a,b,d, the geometric generic relative stable rank in the complete system of bidegree (3ad,3bd) is

`9abd² − 1 − (1 − f₂)ε(ad) − (1 − f₁)ε(bd)`.

The genus is 9abd²+1 and the relative coherent dimension is 9abd²−1. The ordinary elliptic parameter is unrestricted. The theorem concerns all 2-adic valuations of the two degrees. The same formula holds for ambient hypersurfaces when restriction is surjective; the stated sufficient range is d ≥ max(1, reg(I_A)−1).

The second main theorem proves the ordinary–supersingular thin system in every even first degree m ≥ 6, including degrees not divisible by three. Its full curve rank is 3m−1 and its relative rank is 3m−2. For two supersingular factors, the thin theorem covers every even m ≥ 6, with genus 3m+1 and full and relative rank 3m−2. An explicit section in every such degree is proved by a kernel-bundle calculation and two residue functionals. The uniform sparse section is proved geometrically for m=2q with q divisible by six.

No assertion is made about all inseparable polarizations on nonproduct surfaces, complete Newton polygons, all two-torsion group schemes, or monodromy groups. The positive-ordinary-index, zero-local-index determinant problem on a nonproduct mixed surface remains outside the proved scope.

## Literature and exact credit

Grothendieck’s question is cited at cote 4, §8.5.8, archive sheets 7–8, PDF images 8–9, from the original Montpellier scan. Cartier theory, as presented by Illusie (1979), supplies the local trace formula, its multiplicativity, and the differential obstruction. Tate (1968), Theorems 2–3, pp. 155–156, and §4/Theorem 5, pp. 157–159, supplies the residue interpretation of duality that makes the ordinary thin-case determinant explicit. These roles motivate the title’s attribution.

Oda (1969), Propositions 3.18 and 3.22–3.24, pp. 89 and 99–101, supplies the coherent/Dieudonné p-rank interpretation. The ordinary splitting is known from Oda (1971), Corollary 1.7, pp. 53–54; the paper proves the rank-two instance and the additional endomorphism calculations directly. Finite-isogeny facts and the elliptic normal forms are cited to exact locations in Edixhoven, van der Geer, and Moonen. The regularity range is a direct application of the Stacks Project, Definition 33.35.7 and Lemma 33.35.10.

The fixed-system rectangular formula, parameter-uniform residue determinant, explicit sparse-family bundle calculation, and simplified cubic witness were not identified as exact prior statements by the bounded search recorded separately. This is not a priority claim. Chang and coauthors (2026), Theorem 1.1, p. 2, concerns p-rank strata of double covers of a fixed elliptic curve in characteristic greater than two; its parameter space and hypotheses differ. Zou (2026) is cited as recent AI-assisted neighboring work on Frobenius and crystalline slopes, without importing a theorem from it.

## Note on method

The mathematics and text were produced by GPT-6 Astra Pro in ChatGPT Pro mode. The author froze a partial statement-led reconstruction before comparing the rectangular proofs, with earlier exposure to companion rank proofs and a finite seed disclosed. It is not a pristine independent reproof. Complete targeted proof checks, a separate full expert reading, a full newcomer reading, and all-page visual inspection were then performed. A separate GPT-6 Astra Pro expert read of the complete manuscript found no mathematical defect. Reasoning-effort metadata is not exposed.

Six original programs were read and rerun from isolated working copies, with generated outputs preserved separately. A new standard-library Python implementation reconstructs monomial Cartier operators and computes universal parameter minors by division-free subset expansion. It also independently checks the residue and sparse-bundle local identities. Finite high-degree tests are explicitly distinguished from the infinite geometric proof. The two even thin-system assertions now have complete separate proof-unseen reconstructions and full parent comparison. The supersingular reconstruction also proves the broader all-even range. A second exact arithmetic implementation checks these new sections over the four-element field, using inverse Frobenius on vector coefficients. These finite tests corroborate the uniform proofs. The rectangular main theorem also has a complete separate reconstruction, using only the permitted ordinary arbitrary-ample theorem and the degree-one principal-polarization theorem as companion inputs. Its complete nodal-image, parity, perfect-field and ambient-scope arguments passed root comparison. None of the older sparse witnesses receives independent-reproof credit merely from the main theorem.

No human has checked the mathematics. The new text and code are dedicated to the public domain under CC0 1.0.

## The eight opening requirements

| Requirement | Location and content |
| --- | --- |
| 1. Title and attribution | The title names Grothendieck’s generic Frobenius-rank question, the product scope, and the Cartier–Tate inputs. |
| 2. Abstract | The first sentence starts from Grothendieck’s notes; the abstract states the all-degree and parameter-uniform scope, the two main inputs, and the production/checking/no-human qualification. |
| 3. Main theorems in full and in words | Section 1, Theorems 1.1–1.2, defines the field, curves, line bundles, relative rank and parities. The following prose explains each elliptic-type case, with a worked bidegree-(6,3) table. |
| 4. Mathematical purpose | Section 1 explains the unit-root contribution and why the two factor degrees and ordinary/supersingular types matter to Grothendieck’s degree question. |
| 5. Split credit | The title, abstract and “Sources and context” paragraph distinguish Grothendieck’s question, Cartier theory, Tate’s residue duality, Oda’s known splitting and p-rank description, and the fixed-system arguments proved here. |
| 6. Earlier and recent context | Section 1 cites exact primary locations, compares Chang et al. (2026) by parameter space and characteristic, and discusses Zou’s AI-assisted neighboring work at its actual scope. The bounded search is expressly not a priority claim. |
| 7. Scope | Theorem 1.1 distinguishes complete systems and ambient hypersurfaces. The final numbered section, “Scope beyond product polarizations,” defines the mixed indices and identifies the nonproduct determinant problem left outside the result. |
| 8. Mechanism before proofs | “Why the proof works” explains the parity kernels, ordinary residue determinant, supersingular kernel–cokernel residue pairing and the separate two-point bundle modification, one-factor norm transfer, and two-even nodal union. |

Every numbered body section and the appendix begins with its mathematical purpose. The appendix makes both finite rank certificates explicit.

## Authors whose work the paper carries

Alexander Grothendieck; Pierre Cartier; John Tate; Luc Illusie; Tadao Oda; Bas Edixhoven; Gerard van der Geer; Ben Moonen; the Stacks Project authors. Contextual work: Kevin Chang, Dušan Dragutinović, Steven Groen, Yuxin Lin, Natalia Pacheco-Tallaj, Deepesh Singhal, and Haitao Zou.

No correspondence has been sent.

## Rights and destinations

CC0 1.0 applies to the new text and code. Third-party sources are cited and linked, and no copies are included in this workbench directory. Their URLs, SHA-256 hashes, exact pages and read scopes are recorded separately.

Workbench: https://github.com/KokunoYumeto/schemes-and-moduli-workbench

Permanent records: https://github.com/KokunoYumeto/mathematics-workbenches

Before a deposit, allocate permanent identifiers and freeze the source/PDF manifest and commit according to the workbench format. The separate main-proof dependencies and comparisons are already recorded. This sheet authorizes no publication.
