# Grothendieck source crosswalk and check provenance

Run BR_PENCIL-20261121-R1/fields_literature; 2026-11-21. Investigator GPT-6 Astra Pro (ChatGPT Pro mode), inherited effort, no separate numeric setting exposed. Published statements below are background foundations for modern deductions. They are not represented as original statements of tensor-complexity bounds.

## Published locators newly checked from facsimiles

PDF leaves are one-based counts in the exact linked facsimiles, not viewer labels. The indicated image pages were actually rendered and viewed; OCR was not the only check. Reference binaries are a temporary cache, not required deliverables.

| Background ID | Work and exact statement | Printed page | PDF leaf | Mathematical use |
|---|---|---:|---:|---|
| G-EGA-P1 | Grothendieck–Dieudonné, EGAII, Definition5.4.1 and Proposition5.4.2(i)–(iv) | 100 | 97 | Properness entails universal closedness; stability under closed immersion, composition and base change |
| G-EGA-P2 | Same, Theorem5.5.3(i) | 104 | 101 | Projective morphisms are proper |
| G-FGA-Q1 | Grothendieck, *Techniques de construction et théorèmes d'existence en géométrie algébrique IV: les schémas de Hilbert*, Séminaire Bourbaki, exposé221, Théorème3.1 | 259 | 12 | Representability of Quot for projective schemes with the stated noetherian hypotheses; projective pieces |
| G-FGA-Q2 | Same, Théorème3.2 | 260 | 13 | Fixed-Hilbert-polynomial Quot scheme is projective |
| G-FGA-H | Same, specialization Hilb=Quot(O_X) immediately after Proposition3.8; Remarks3.9 | 265–266 | 18–19 | Hilbert parameter spaces and universal/base-change construction; retain the limiting span by a graph closure when necessary |
| G-SGA3 | Demazure–Grothendieck et al., *Schémas en groupes*, SGA3, ExposéI, §§4.5–4.6, including Definition4.6.1 | 29 | 42 | GL_n=Spec Z[T_ij,det(T)^{-1}], module functors and locally free tensor representations |
| G-SGA6-L | Berthelot–Grothendieck–Illusie et al., *Théorie des intersections et théorème de Riemann–Roch*, SGA6, ExposéV, Definition2.1, Examples2.2(b), Lemma2.2.1 and continuation | 314–316 | 321–323 | lambda operations from exterior powers; filtration of an exterior power of a locally split extension |
| G-SGA6-R | Same, representation-ring example at end of Examples2.2(b), before §2.3 | 317 | 324 | K_0 of representations in finite projective modules as a lambda ring |
| G-SGA6-G1 | Same, Proposition3.2(ii) | 325 | 332 | Relation between lambda and gamma operations |
| G-SGA6-G2 | Same, §3.10, equation(3.10.1) | 331 | 338 | Gamma filtration by products of positive operations on augmentation-zero elements |

Primary facsimiles:

- FGA: [NUMDAM SB_1960-1961__6__249_0.pdf](https://www.numdam.org/article/SB_1960-1961__6__249_0.pdf). Exposé pages249–276. Catalog reprint/erratum dates should not be mistaken for the talk's date.
- SGA3I: [SLMath/MSRI facsimile sga3-1.pdf](https://library.slmath.org/nonmsri/sga/sga/pdf/sga3-1.pdf).
- SGA6: [SLMath/MSRI facsimile sga6.pdf](https://library.slmath.org/nonmsri/sga/sga/pdf/sga6.pdf).

## EGA properness

The required exact locators are EGAII, Definition5.4.1 and Proposition5.4.2, printed p.100, PDF leaf97; Theorem5.5.3(i), printed p.104, leaf101. Source: [NUMDAM PMIHES_1961__8__5_0.pdf](https://www.numdam.org/article/PMIHES_1961__8__5_0.pdf), *Éléments de géométrie algébrique II*, IHÉS8 (1961),5–222, DOI10.1007/BF02699291. Definition5.4.1 supplies universal closedness as part of properness, Proposition5.4.2 supplies stability facts, and Theorem5.5.3(i) gives projective implies proper.

Fresh verification completed on2026-11-21: the whole219-leaf NUMDAM PDF was downloaded, leaves97 and101 were rendered, and both images were viewed. The statement numbers and printed pages match the predecessor's locators. The proof of5.5.3(i) is also on leaf101; the background result is used and rechecked, not claimed as independently reproved.

## Locators carried from the supplied predecessor

These are exact locators reported and inspected in GCT_GINEQ. This agent has read the predecessor's statements and dictionary but has not newly opened all these full facsimiles. Retain that provenance if cited.

| Work | Locator | Printed page / recorded PDF leaf | Present use |
|---|---|---|---|
| EGAI, NUMDAM PMIHES_1960__4__5_0 | §9.5, Propositions9.5.1 and9.5.4, Corollary9.5.2, Definition9.5.3 | 176–177 / 175–176 | Scheme-theoretic image/orbit-closure foundations; kernel commutes with flat base change, not arbitrary reduction modulo a prime |
| SGA4 | ExposéVII, §1.2 | Not asserted here | Étale-site foundation only |
| Deligne, *La conjecture de Weil II* | Definition1.2.2 | 153 / 17 in predecessor's IAS facsimile | Purity terminology only; no rank lower bound follows from a constant stalk |
| Grothendieck, *Résumé de la théorie métrique des produits tensoriels topologiques* | §1 no.1, Definition1 and Theorem1; Theorem2 and duality corollary | 8 /8; 8' /9 | Analytic tensor norms/duality, where the SDP/orbit agent explicitly uses them |
| Same *Résumé* | §4 no.2, Theorems1–2; Corollary1 after Theorem3, inequality(8); §4 no.3 proof opening | 59–60 /60–61;61 /62;62 /63 | Grothendieck inequality foundations, not the norm-free residual-border-rank proof |

The *Résumé* facsimile recorded in the predecessor is the1996 USP reprint, DOI10.11606/resimeusp.v2i4.74836. Do not copy leaf locators to another PDF without verifying its pagination.

## Archive identifiers: verified and unverified

The [CSG published-works catalogue](https://csg.igrothendieck.org/published-works/) was opened and its relevant entries read:

- CSG17 identifies the published *Résumé*. The catalogue gives the1953 São Paulo volume8,pp.1–79 and the1996 USP reprint,pp.401–480.
- CSG44 identifies the published Hilbert-schemes exposé221,pp.249–276; it also lists the1962 erratum,p.302.

These are published-work catalogue identifiers. They are not Montpellier unpublished-manuscript cotes. The [Montpellier archive page](https://grothendieck.umontpellier.fr/archives-grothendieck/) was consulted, but no manuscript cote and scan specifically carrying the modern residual-pencil theorem was established. The honest entry for such a manuscript locator is “not established; published foundations as above.” No inference from the name of a framework creates a manuscript source, and no invented cote or scan should appear in the paper.

## Dictionary for the fields findings

- FL-01 and FL-03 are formulas in free Z-modules and split coordinate projections. Their scalar-extension statement lives in locally free sheaves and the group schemes G-SGA3. Integral divided powers must be distinguished from the ordinary symmetric quotient.
- FL-02 is a tautological closed incidence in Gr(q,W) times a projective secant variety in each algebraically closed fiber. EGA properness, and not an analytic limit, makes its image closed. Relative Hilbert/Quot constructions G-FGA-Q1/Q2/H can retain limiting schemes together with their spans; they are not needed to identify the span of a bad limiting Hilbert point.
- FL-04 is a unit-minor calculation over Z. For the pencil results, exterior-power/Koszul morphisms also exist integrally. G-SGA6-L/R/G1/G2 describe the bundle classes, while actual minors certify the map's rank. This respects predecessor F-20: K_0 and gamma classes alone do not determine the rank.
- FL-05 is the factorial obstruction in the ordinary symmetric quotient. It locates the boundary of the all-field statement, rather than imposing characteristic-zero polarization where it does not exist.
- No new l-adic, weight, purity or motivic theorem is obtained. Predecessor F-21 explains why the constant sheaf or absolute point motive forgets the embedding. SGA5 is not invoked by any proof here; no spurious SGA5 theorem locator is supplied.
