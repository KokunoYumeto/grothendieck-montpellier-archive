# K70-03 — mathematical notes

Written after the transcription freeze of **2026-11-18T00:07:21+00:00**. These notes use only the supplied scans and the frozen transcription. They do not alter a reading. A proposed slip or convention change based on doubtful, cancelled, or overwritten ink is rated **low** confidence. The fuller reading register, including spelling, abbreviations and correction states, is in `K70-03_doubts.md`.

## What the pages do

**Scans 33–34 — parameters and involution conditions.** Matrix (16) and formulas (17)–(20) describe transformations with coefficients written u and v/nu, impose a reflection condition, and reduce the parameters to lambda and mu. Scan 34 computes squares, records conditions for those squares to be the identity, and contrasts “Cas général” with the n-polyhedral case. The overwritten matrix on 33 is the least secure part of this unit.

**Scans 35–36 — two-variable calculations and orders.** Scan 35 writes two affine transformations, computes powers of an upper triangular homogeneous matrix, separates cases, and then examines an orbit to distinguish an affine transformation from its homogeneous part. Scan 36 states order conclusions, treats exceptional cases, and calculates the second transformation’s characteristic polynomial and eigenvalues amid substantial cancellation. The eigenvalue glyph is read eta with gamma as an alternative; the case revisions remain tentative.

**Scan 37 — higher-index formulas.** A bracketed list gives the first, intermediate and last transformations, followed by an eigenvalue-multiplicity statement and a question-marked comparison of orders. This is a short synthesis rather than a proof on the sheet.

**Scan 39 — cover.** The cover labels the following material “étude locale” of n-polyhedra and n-cards and calls it a “vieille rédaction”. A previous title is cancelled and a pencil page count is uncertain.

**Scans 40–41 — local constructions at a facet.** The notes recall a presentation of G_n and describe i-facets as a quotient of the underlying set E. They then consider the quotient E^−(i), its connected pieces, and the flags associated with a fixed facet. A “bord” construction is named, followed by the dual quotient E^+(i). Both the freeness/cartographic assertions and the dual construction carry qualifications.

**Scan 42 — intervals of types.** The quotient E(i,j) removes the generators outside an interval; the remaining generators are said to give a (j−i−2)-card. Its components are related to flags of type (i,j), and its h-facets to flags of type (i,i+h+1,j). The cases j=i+2 and j=i+3 lead to a trivial-looking case and a polygonal numerical invariant. The bottom relates these interval constructions to the preceding minus and plus constructions, with several cancellations.

**Scan 43 — numerical invariants and generator products.** A list of local invariants is followed by the claim, for a regular object, that the parameters p_0 through p_{n−1} are orders of adjacent generator products. A margin limits the asserted validity at least to incidence geometries. The sheet starts an argument using the action on E^−(2) and an orbit equation, but does not complete a general proof here.

**Scans 44 and 46 — geometric realization through flags.** Scan 44 defines a realization by a map from repères to maximal affine flags, constrained so that applying sigma_i preserves the j-component for i≠j. It then factors the component maps through the facet sets. Scan 46 discusses incidence geometries and extends the formulation to arbitrary type subsets and compatibility with their inclusions, ending with an interpretation as homomorphisms of flag geometries.

**Scan 45 — cancelled equivariant draft.** The whole upside-down draft is crossed out. It pairs a homomorphism from Aut(Pi) to Aff(E) with maps on repères and facets, labelled as G-homomorphisms, and records a flag-preservation condition. It is a cancelled formulation; no assertion that the author adopted it is made.

**Scans 47–48 — induced realizations.** A cancelled interval-card construction precedes a live discussion at a facet f_i with E_i=varphi_i(f_i). The text calls a realization in E_i “induite”, then starts the dual construction. Scan 48 identifies the relevant vertices with two-step flags and passes from affine subspaces containing E_i to lines in the quotient E/V_i, where V_i is the translation space of E_i.

## Statements left without proof

- **Scan 33, following (18):** “sigma_i est une réflexion ssi” the relations are consequences of the i-th one, followed by “Ceci signifie” and (19). The intervening words are doubtful in the transcription. The equivalence is asserted without a separate proof on this sheet; reading-dependent interpretation is **low** confidence.
- **Scan 37, eigenvalues:** “1 de multiplicité n−1” and the eigenvalue read eta_i. No justification of the multiplicity is written here. The interpretation of the underlying space is not supplied by these pages; **low** confidence for any dimensional inference.
- **Scan 40, local action:** “et sauf erreur c’est un” followed by the doubtful description of the local object, then “opèrent sans pts fixes dans E^−(i)”. The fixed-point assertion is stated with the author’s qualification; **low** confidence where the rewritten phrase is involved.
- **Scan 41, dual construction:** “On trouve une moquette” with inserted “de (n−i−1)-cartes” and “(sauf erreur)”. The associated facet description is given, but the cartographic claim is not proved here.
- **Scan 42:** “Sans doute il opère cartographiquement”. This is an expressly qualified assertion, followed by the resulting component and facet descriptions.
- **Scan 43:** “Supposons Pi régulier, je dis que”, followed by p_0 as the order of sigma_0 sigma_1, p_1 as the order of sigma_1 sigma_2, and so on to p_{n−1}. An argument begins under “En effet”; the general claim is not completed on this page. The p/rho and nu/v readings make a formal identification based on those names **low** confidence.
- **Scan 46:** “La donnée de varphi_R satisfaisant (2) équivaut à la donnée des applications (4) satisfaisant la condition de fonctorialité précédente”. Compatibility is described but no independent proof of the equivalence is written.
- **Scan 47, live paragraph:** “On trouve alors” with inserted “en termes de varphi”, then “une réalisation géom. canoniq. (dite ``induite'')”. The abbreviation “canoniq.” and the boundary decorations are doubtful, so a stronger claim about canonicity is **low** confidence.
- **Scan 48:** “les E_{i+1} correspondent à des droites de” E-bar=E/V_i. The correspondence is stated without a further proof or an explicit line-incidence condition on this sheet.

## Questions and conjectures

- **Scan 35:** “sigma_0^n(0)=?” is an explicit computational question, followed by an attempted answer in the iterates below.
- **Scan 37:** “ordre de sigma_i ?= ordre de eta_i in k^* si eta_i ne 1”. The question mark is authorial. The eta/gamma distinction is instead a reading doubt; interpretation depending on that choice is **low** confidence.
- **Scan 40:** “sauf erreur” qualifies the local-object/fixed-point discussion. The associated rewritten wording is uncertain; **low** confidence for a more specific conjectural formulation.
- **Scan 41:** “(sauf erreur)” qualifies the moquette of (n−i−1)-cards.
- **Scan 42:** “Sans doute il opère cartographiquement” is a qualified expectation, not a fully proved statement on the sheet.
- **Scan 43, margin:** “vrai tout au moins dans le cas des géométries d’incidences (``polyèdres''...)” restricts the assurance attached to the adjacent order claim.
- **Scan 47:** “Légèrement moins évidente” marks difficulty of the induced dual construction. It is not an explicit question or conjecture; it is included here only to distinguish that qualification from a proved result.

## Slips

The suggestions below are separate from the frozen readings. “Possible” means that shorthand, a different ambient space, or the state of a revision may explain the discrepancy.

| Scan / place | Frozen reading, as written | Suggested form or clarification | Reason / confidence |
|---|---|---|---|
| 33, (18), first row | `u_{i2} x_{i+2}`, alternative `x_{i+1}`; `Sigma_2`, alternative `Sigma_i` | Possibly `u_{i2} x_{i+1}` and `Sigma_i` | The neighboring terms and (17) favor those forms, but the local ink is 2-like. **Low**. |
| 34, reduced X_i | `lambda_i x_i + lambda_i(1-lambda_i)x_{i+1}` | Add `(1-lambda_i)mu_i Sigma_i` | This term survives expansion of the preceding line. **High** for the discrepancy between the two displayed expressions. |
| 34, reduced X_{i+1} | Coefficient 1 on `x_{i+1}` and positive `(1-lambda_i)mu_i Sigma_i` | Coefficient `lambda_i+(1-lambda_i)^2` and negative `(1-lambda_i)mu_i Sigma_i` | Direct expansion of the preceding expression gives these, but the surrounding outer terms are cancelled. **Low** for the intended revised expression. |
| 35, nth matrix power | `eta_n^{n-1}`, alternative `eta_0^{n-1}` | Probably `eta_0^{n-1}` | The same matrix with eta_0 is being powered. Doubtful index: **low**. |
| 35, bottom iterates | Powers 2, 3 and n give a scalar expression after `sigma_0^m(x,0)` | Possibly write a pair with second coordinate 0, or specify that only the first coordinate is displayed | The preceding first iterate is a pair. This may simply be shorthand. **Low**. |
| 36, exceptional cases | `alpha_0=1`, `sigma_0=id`; then `alpha_0 ne 1` | Recheck 1 versus 0 and the affine map versus its homogeneous part; no single correction asserted | The preceding affine formula has constant first coordinate contribution 1, whereas the homogeneous identity condition was alpha_0=0. Nearby revisions and the eigenvalue reading prevent a firm reconstruction. **Low**. |
| 36, final exception | `sauf si delta=1` after the live eigenvalue is named eta_1 | Possibly `eta_1=1` | Delta was used in the cancelled rewriting. **Low**. |
| 37, eigenvalue multiplicity | `1 de multiplicité n-1`, followed by eta_i | Possibly n if the full homogeneous space has n+1 independent coordinates | An implicit restriction could instead explain n−1. No space convention is inferred from these sheets. **Low**. |
| 40, local action | `G_n^+(i) ≃ G_{i-1}` | Possibly `G_n^-(i)` | The page’s minus subgroup is generated by sigma_0,...,sigma_{i−1}; its plus subgroup is used in forming the quotient. The rewritten/qualified passage is **low** confidence. |
| 42, quotient notation | `E/G^-(i) × G^+(j)` | Possibly group the denominator as `E/(G^-(i) × G^+(j))` | The generator quotient immediately before it suggests that grouping. This may be omitted grouping notation, not an error. **Medium**. |
| 42, special case | `polygône` | Standard spelling would be `polygone` | The visible circumflex is retained; this is a spelling observation, not a modernization of the text. **Medium**. |
| 42, final plus construction | `Pi^+(f^i)`, alternatives `Pi^+(f_i)` and `Pi^+(f′)` | Possibly `Pi^+(f_i)` | Neighboring facets use lower i, but this mark sits high. **Low**. |
| 44, bottom connective | `Il revient au =`, uncertain inserted words, then `à dire` | Possibly the idiom “Il revient au même de dire” | This is a reading question, not an established slip: two actual parallel strokes and the unclear note are retained. **Low**. |
| 46, target of (4) | `Drap aff_{...}(Pi)` | Probably `Drap aff_{...}(E)` | The realization targets on 44 and the final line on 46 are affine flags of E, while this target clearly says Pi. **Medium**. |
| 46, last paragraph | `on peut donc les interpréter` with inserted `les varphi_R` before “comme” | Possibly suppress one “les” phrase editorially; no such deletion supplied in the transcript | The insertion leaves duplicated wording. The correction state does not authorize normalizing it. **Low**. |
| 47, cancelled component set | `D_j(Pi)` | Possibly `D_{ij}(Pi)` | The interval construction has two endpoints, but the enlarged subscript shows only j. Cancelled material: **low**. |
| 48, affine flag component | `dont la i-composante est f_i` | Probably `E_i` | The next couple is `(E_i subset E_{i+1})`, and scan 47 defines E_i as the image of f_i. **High**. |

## Pointers

None identifiable as an external mathematical citation: these sheets give no explicit paper, person, other cote or dated text to consult. The uncertain cancelled cover heading “Th. des Topos” / “Th. de Topos” on scan 39 may name an earlier folder or text, but identifying it further would exceed the evidence (**low** confidence). “(vieille rédaction)” labels the current cover material. Internal references include (2), (3), and (4) in the realization discussion; they are not external pointers.

## Remarks of the model

- **Model remark — low confidence:** Scans 40–43 and 47 reuse the pattern of removing generators outside a type interval. This suggests a common organizing construction for the lower, upper and intermediate local objects. The confidence is limited because the scan-47 formulation is cancelled and some boundary notation is doubtful; no assertion of a final adopted convention follows from it.
- **Model remark — low confidence:** The contrast between the affine map and its homogeneous part appears central to the revisions in 35–36. It may explain some of the identity/order language, but the alpha-case and eigenvalue revisions do not allow a secure repaired argument.
- **Model remark — medium confidence:** Scan 48’s lines in E/V_i presumably retain the incidence condition coming from E_{i+1} containing E_i; in an affine reading this would mean passing through the image of E_i. The sheet does not spell that out, so it is an inferred clarification, not a correction to the transcription.
- **Model reading question — low confidence, scan 43, cancelled lower formula:** The frozen reading includes a raised `a|o` on d in the cancelled nu(Pi(d_{i,i+3})) fragment. The loop could belong to a cancellation flourish instead of an additional letter. It remains in the frozen text as a doubt; no change was made during these notes.
- **Model reading question — low confidence, scan 47, live lower diagram:** The frozen connector is `-|left arrow|right arrow`. “Image rec.” makes a rightward map mathematically natural, but the insertion curve and thick trace prevent deciding the arrowhead from the crop. The textual construction must not be used to erase that reading uncertainty.

No proof, external source, or continuation beyond these scans was used. The hash comparison after completion of these notes is recorded in `progress.log`.
