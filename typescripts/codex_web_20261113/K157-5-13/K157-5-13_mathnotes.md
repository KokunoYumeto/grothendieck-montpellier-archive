# K157-5-13 — mathematical notes

These light notes refer to scans 197–212, manuscript pages 113–128. The sixteen page files and the assembled transcription were frozen at **2026-11-20 00:54:23 UTC**. The supplied `RESULTS_STATE.md` was read in full after that freeze, followed by the supplied K157-4-04 notes. Readings remain those of the frozen text. A report that the author states or argues something is not an independent verification of it.

## What the pages do

**U01 — Revising a small-subcategory estimate (197–199).** Lemma 4.5.5 seeks a subcategory containing a prescribed small family of arrows while remaining “grande devant” a cardinal. The initial use is explicitly conditional: “Ce lemme étant admis.” An example using subsets of a set and its automorphisms tests the cardinal estimate; the calculation reaches a bound involving pi to the power pi-zero. “Finalement je me suis convaincu” then revises the preceding formulation and the scope of earlier corollaries. Cancelled bounds and marginal qualifications are part of this argument's history.

**U02 — Accessible objects and cardinally bounded presentations (200–202).** A proposition whose heading reads 4.5.5|4.5.6 compares accessibility, membership in Filt, and presentations by indexing categories of controlled cardinality. The proof gives the implication chain and a small-subcategory construction. For sets, the text identifies the classes under discussion using cardinal bounds. Corollary 4.5.7 relates M with lower pi to Filt with a raised iterated cardinal. The foot of 202 acknowledges an omitted part of the proof and starts to supply it.

**U03 — Pointwise accessibility in a functor category (203–204).** Lemma 4.5.8 gives the set case and a pointwise test in the underlined Hom category. The first argument writes a set as a coproduct of singleton sets and examines a filtered presentation. The second uses evaluation at x and its right adjoint, then the displayed Hom adjunction. Existence of the indicated products is explicitly assumed. The converse is announced with an extra cardinal bound on Fl(C), but its details are left unexpanded. Two formula questions are isolated as S01–S02 below.

**U04 — A cardinal filtration for an Ind construction (205–208).** Proposition 4.5.9 takes M = Ind-prime with lower pi-zero of C and uses the full subcategories of pi-accessible objects. The inserted threshold pi-one involves Sup(pi-zero, card Fl C). The proof separates the filtration conditions and studies the slice M-pi/x. Lemma 4.5.10 counts reduced categories and presheaf-like objects; 4.5.11 bounds Hom sets; 4.5.12 applies the estimates to the slice. The precise raised decoration and several high exponents remain reading questions. The final comparison calls the earlier estimates too coarse and prepares a stronger formulation.

**U05 — Six conditions and the primed filtration (209–211).** Proposition 4.5.13 compares presentations, cofinality and strictly epimorphic families, labelled a, a', a'', b, b', b'', c and d in the surrounding discussion. It defines P(pi) and Filt-prime, displays inclusions between these classes, and gives additional conditions for equality with M-pi. The lower assertions on 210 are in the source order 3), 1), 1'), 2), with a relocation arrow. The next page lists cases A–C, involving a cardinal identity, universality of strict epimorphic families, and compatibility of filtered colimits with base change. The remark compares the construction with SGA 4 I 9.13 and records the author's change of preference.

**U06 — Comparison and start of proof (212).** “Donc apparemment” says that the cardinal filtrations he can construct on his prototypes coincide with the M-pi filtration. He then begins the proof of 4.5.13: the six-object diagram records seven immediate implications, and the remaining reduction is a implies b-double-prime. The right marginal note invokes strong generation by C and the colimit over C/x. This proof continues beyond scan 212.

## Statements left without proof

| ID | Scan(s) | Author's words and local status |
|---|---|---|
| A01 | 197–198 | “Ce lemme étant admis” uses the small-subcategory lemma before the subsequent examination and revision. The marginal restriction remains partly doubtful. |
| A02 | 201 | “AQT” closes part of the implication argument. It is retained as the manuscript's shorthand; no missing derivation is supplied here. |
| A03 | 204 | “en vertu de loc. cit. 9.8” invokes the accessibility of the right adjoint; the external result is not reproduced or checked here. |
| A04 | 204 | “je ne vais pas l'expliciter ici” expressly leaves the converse of the pointwise criterion unexpanded. |
| A05 | 205 | “cf SGA 4 I 9.9” supports stability of M-pi under the indicated colimits. The introductory words remain “une connue|bien connue|connue”; no grammar correction is made. |
| A06 | 208 | “C'est essentiellement la même démonstration, mais plus simple” introduces the next bound with a brief comparison rather than a fully separate development. |
| A07 | 209–212 | Proposition 4.5.13 is stated and its proof begins, but the final reduction on 212 is not discharged within this sixteen-scan batch. This is a batch boundary, not an assertion that the manuscript never proves it. |

## Questions and conjectures

| ID | Scan(s) | Words and question |
|---|---|---|
| Q01 | 197 | The marginal “N'est prouvé … que si” and question marks qualify the original lemma. Any precise reconstruction of the qualification has **low confidence**, because several connecting words and signs remain doubtful. |
| Q02 | 208–209 | “Apparemment” accompanies the comparison of bounds; “hasarder” introduces the proposed stronger statement. The notes do not certify strictness or replace the uncertain high exponents by a convenient estimate. |
| Q03 | 211, diagonal note | “Je soupçonne que cette condition revient|équivaut …” compares a condition on M with one on C for suitably bounded filtered colimits. The connecting equality/similarity wording is doubtful; the exact conjecture has **low confidence**. |
| Q04 | 211–212 | “Je soupçonne … maintenant qu'en général … en dehors des conditions A) B) C)” questions whether the primed filtration is cardinal. “Donc apparemment” then restricts the positive observation to prototypes he knows how to construct. These are his expressed expectations, not conclusions proved in this return. |

## Slips

**S01 — Inner argument of the right adjoint (204, adjunction display). Model diagnosis, medium confidence.** The frozen right side ends in `Hom(F, epsilon_{x*}(F))`; the inner letter is visibly F. The left side is a functor of E, and the displayed domain of epsilon with lower star is the coefficient category. The locally consistent argument would be **E**, giving `epsilon_{x*}(E)`. This is a targeted type check of the displayed formula, not a re-proof of the accessibility theorem. The transcription keeps F.

**S02 — Order of the Hom arguments (204, product formula). Conditional model diagnosis, low confidence.** The frozen formula has `epsilon_{x*}(E)(y|x) = E^{Hom(x,y)}`. If its left argument is y and the underlined Hom(C,E) means covariant functors as displayed, the evaluation right adjoint uses the index **Hom(y,x)**. The left argument is itself uncertain, so this remains a conditional variance question and cannot be promoted to a firm authorial error. No reading is changed.

No spelling or agreement slip is asserted. In particular, the compressed prose on 205, the ordonnée wording on 209, and the endings in the family condition are kept as reading questions. Other unresolved local questions include the heading on 200, the final subscript on 202, the C|G on 207, and the amended numerical label at the bottom of 207.

## Pointers

| ID | Scan(s) | Manuscript reference or supplied-note connection |
|---|---|---|
| P01 | 197–202 | Internal references include 4.5.2, 4.5.3, 4.5.4 and 4.5.6. The later clear 4.5.6 does not silently correct the doubtful heading on 200. |
| P02 | 200–201 | The diagonal note on 200 points to 4.7.1 and page **161|151**. The lower note on 201 says “Comparer le lemme 4.5.14”, page|pg 133. |
| P03 | 202–204 | References to manuscript pages 108–109; on 203 “Cf généralisation 4.14.18 p. 391”, and SGA 4 I 9.9; on 204 “loc. cit. 9.8”. |
| P04 | 205–208 | SGA 4 I 9.9 and 4.5.7; the lower note on 206 repeats 4.5.11 in both clauses; on 208 the compressed “reven. à|revenant à|revenons à : 4.5.9.1”. |
| P05 | 209–212 | 4.5.10–11; on 210, 4.5.3 p.109 and 4.5.6 p.116; on 211, “compléments 4.5.18” and SGA 4 I 9.13; on 212, SGA 4 I 9. |
| P06 | 203–205; supplied K157-4-04 | **K157-4-04 U02** reports ordinary restriction adjoints under limit and accessibility assumptions; **K157-4-04 P01** records his reference to notes on accessible categories and filtrations. The present pages supply a related evaluation-adjoint argument and cardinal-filtration discussion. This is a documentary connection, not an identification of an otherwise unattested reference or a new proof of the earlier claims. |

## Remarks of the model

**R01 — Scope relative to GALOIS B.13. High confidence as a scope comparison.** The supplied results state leaves **GALOIS B.13** open: accessibility of the relevant localizer for an arbitrary derivator satisfying only Der 1–4. Here the concrete hypothesis on 205 is “M = Ind'” of C, with specified cardinal and colimit assumptions; 212 says “dans tous les cas où je sais construire” and “sur un prototype du moins”. These pages do not provide the missing passage from arbitrary bare derivator axioms to that concrete presentation. The open status is carried as supplied; it is not settled or re-proved here. The FINMON and EXIT_TOWER headline results are not premises of these notes, and no direct mathematical use of them is made by these sheets.

**R02 — The bound comparison remains a reading-sensitive lead. Low confidence.** The transition from the estimates of 208 to the stronger-looking pi-prime-to-pi expression in 209 is worth retaining as part of the manuscript's development. Several exponents and the amended reference are doubtful. These notes neither prove a strict comparison nor claim that a printed correction is forced.

**R03 — The revisions are mathematical evidence. Medium confidence.** The explicit admission on 197, the reconsideration on 199, the omitted-proof acknowledgement on 202, and the change of preference on 211 should remain visible together. They document the development of the argument; they do not themselves verify its final form. The comparison here is confined to the statements and qualifications on these pages.

The event ledger records only the limited type/variance checks and the background/scope comparisons actually made. Ordinary visual transcription and documentary summaries U01–U06 are not entered as proof checks. No independent re-proof, computation, formal certificate, literature search, or general error audit was performed.
