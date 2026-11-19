# B.5--B.6 completed contribution and integration notes

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026. No priority claimed. The complete proofs are in `agent_B56_proofs.md` and their LaTeX conversion `B56.tex` (also `agent_B56.tex`). Metadata: `results_B56.csv`, `references_B56.bib`, `CHECK_EVENTS_B56.tsv`. Do not include fetched full copyrighted literature in the deliverable ZIP; retain bibliographic locators, our proofs, code and outputs.

## Outcomes

B.5 is settled in the precise typed sense given by B5.1--B5.10. Full ordinary comparison epimorphisms are exactly flatness and suffice for homotopy descent even before hypercompletion. The forest collection fails, with checked C2 examples. Exact necessary-and-sufficient local descent is the explicit subdivision-filling scheme B5.10.1 on the simplicial replacement, after hypercompletion. The pro-space comparison has the exact mapping-space tests B5.6.2; the original Artin--Mazur comparison is precisely q of the hypercomplete shape, with exact pi0 tests B5.6.3--4. Verdier comparisons and the symmetric case are explicit; every matching degree is independently indispensable. The supposed strictly-between relationship is false. Slice shapes and component sets must be kept separate, as must original Artin--Mazur Pro(Ho Spaces) and infinity-categorical pro-spaces.

B.6 is settled. The global relation list remains incomplete after both global invariances; a countermodel already appears on arities 1,2,3. A complete replacement follows from opened Grandis Theorem 4.2 by explicit inverse substitutions. The corrected final low-degree list of 151/005 is complete, with hom-cardinality matrix [[1,1,1],[2,4,8],[3,9,27]]. The two sigma3 alternatives in 151/003 and 005 are false. Original scans003,005and017 have now been independently inspected; the boxed003 sigma3, middle005 sigma1, and017 lowerbounds2,3 are clear. The last005 subscript remains visually unresolved; both readings are retained. See ink_B56/INK_REVIEW.md.

## Pivotal corrections to prior study

| Source locator | Finding | Corrected statement |
|---|---|---|
| `study/readings/151_001-017_INTEGRATION.md`, lines 61--68 and 78--83; `151_001-017.md`, lines 303--309 | Hypercovers need not satisfy Hyp2prime, even with symmetric indexing; flat simplicial systems need not be hypercovers | B5.5, B5.7, B5.10 |
| User R8 / `151_001-017.md`, group-nerve paragraph around lines 303--309 | “Realizes to BG” depends on realization | Homotopy colimit and ordinary simplicial realization are BG; finite-group naive symmetric coend is contractible, B5.3 |
| 151/017, boxed four relation families, plus 151/005 global boxes | Still not a complete global presentation | B6.1 countermodel; B6.2 complete replacement |
| 151/005 line 30, unsure subscript 1 or 3 | Only subscript1 is true; original ink remains visually unresolved | B6.3 proves corrected list complete and disproves subscript3 |
| 151/003 line55 vs 151/005 line23 | sigma3 e=e false; sigma1 e=e true | B6.3 independently confirms SA10-K151a-01 mathematically |
| 151/015 line29, single dot as Hyp1 diagram | One-object comparison is an identity | Empty diagram required, B5.1; no new ink claim |

## Computations

- `code_B56/check_B56.py` / `.out`: 14 corrected low-degree relations; all 56 finite maps on arities1--3; 412 typed global countermodel relation instances; four C2 cospans/eight completing squares; H1(BC2;F2) dimension1; 16 symmetric products, 1,528 cospans, 6,871 compatible target pairs; 126 monotone maps; 30 exact-rational symmetric singular-hypercover amalgams. Final recorded run: 0.044837 seconds.
- `code_B56/check_matching_independence.py` / `.out`: 32 GF2 matching comparisons, n=1--4 and k=0--7; unique failed degree k=n+1. Runtime 0.016021 seconds.
- `code_B56/check_stable_graphs_independent.py` / `.out`: independent check of root A4.5, using direct bounded multigraph enumeration instead of inverse contractions. Positive cases graph counts 2,5,23,7 and pair counts1,10,253,21; no failures. Times 0.000044, 0.000146, 0.002840, 0.000157 seconds.

All infinite-family assertions have proofs independently of finite bounds. The normal-form proof, not target verification alone, proves low-degree completeness.

## Primary literature opened

Full URLs, exact theorem locators and access status are in `references_B56.bib`. Grandis 2001, DHI 2004 (arXiv v2 and LaTeX source), HTT, Barnea--Schlank v9, Barnea--Harpaz--Horel 2017 Theorem6.0.4 pp625--626, Curtis 1971, Stacks 019G, and Kerodon 00ZA/00ZH/00ZK are opened and used. The requested Haine1811.01119v6 is fully opened; Definition1.1.4 and Theorem1.1.7 p8 are cited in C1_collage_B.tex for the flag-Segal framework, not used as a premise in B5. Dugger--Isaksen topological hypercovers and Stacks 01GZ were opened for context. Shulman 2012 search metadata was found, but full-text links failed; it is not used as a premise. Searches covered finite-set presentations, flat and covering-flat functors, arbitrary-index hypercovers, local weak equivalences, Artin--Mazur derived realization, symmetric realization, and Ex-infinity. We assert no priority.

## Independent review of parent Part A

A1.2 synchronized pro-Cech proof checked: the truncated simplex category has finitely many objects and morphisms, so the filtered-bicolimit/finite-bilimit interchange is legitimate, while infinite I stays inside each synchronized coproduct. A1.3 plane examples and the connected R2-in-R4 repair checked; identity comparisons on the strata prevent exchanging 0 and1 to repair the mismatch. A4.5 uniform negative families and genus-zero argument checked, and positive finite cases independently enumerated as above. These reviews have own CHECK_EVENTS rows.

## Further completed review

C5_Hurewicz_review.tex/.md and references_C5_Hurewicz.bib close the proper PL/smooth Hurewicz fibre-manifold gate, with independently audited complete constructions and an auxiliary A7 finite quotient certificate. B6.2 now includes explicit cycle words for every Grandis coface/codegeneracy, the full translated relation scheme, and a surjective-generator/composite-isomorphism argument that excludes missing defining equations. check_B6_translation.py/.out checks168 generator words through n12 in0.000609891seconds.


## Final B.5 scope audit

`B5_scope_audit.md` records exact request coverage and all implication directions. The primary BHH theorem explicitly identifies the hypercompleted shape; no inference from local weak equivalence to full nonhypercomplete shape remains. Full flatness still gives the stronger pre-hypercompletion assertion. Symmetric full Hyp implies hypercover strictly; ordinary flatness and hypercover are incomparable. The Artin--Mazur criterion applies pi0 after the limit of mapping spaces and applies q after the pro-space colimit.

`B56.tex` is the directly maintained authoritative proof, with separate B.5 and B.6 section headings. `code_B56/sync_B56_mirrors.py/.out` records the final normalization and regenerated TeX/Markdown mirrors. No hidden generator is required to reconstruct the source. The complete C5 Hurewicz proof and its separate references remain preserved.
