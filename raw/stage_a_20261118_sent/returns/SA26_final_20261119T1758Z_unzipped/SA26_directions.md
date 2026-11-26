# SA26 — Ranked directions for subsequent runs

**Assessment date: 19 November 2026.** These are task proposals arising from the completed consolidation. They are not additional claims or conjectures attributed to Grothendieck. No direction is developed here beyond its scope, known starting point and first concrete step. A problem identifier below points to the historical question that motivates a direction; it does not assert that the question remains open today.

Scores run from 1 to 5. **Interest** measures likely mathematical or editorial value. **Reach** measures what a focused run of a few hours could establish, given the stated inputs; it is not a promise of a new theorem. The overall rank balances those two considerations. The separate interest and reach ranks make the tradeoff explicit.

| Overall rank / direction | Interest | Interest rank | Reach | Reach rank | Likely bounded output |
|---|---:|---:|---:|---:|---|
| 1 / D-SA26-01 — Identify the literal cofibration axioms | 5 | 1 | 4 with scans; 1 without | 3 | A documented axiom correspondence and a companion statement whose hypotheses are exact |
| 2 / D-SA26-02 — State the A-valued cotensor criterion precisely | 5 | 2 | 4 | 2 | A short theorem-and-counterexample treatment with the intended range of weights identified |
| 3 / D-SA26-03 — Positive scope for the sequential comparison | 4 | 3 | 3 | 5 | One target-specific vanishing criterion and a clear boundary with the phantom example |
| 4 / D-SA26-04 — Higher comparison for revised roofs | 4 | 4 | 2 | 7 | An exact literature comparison, or a narrowly stated missing comparison with its hypotheses |
| 5 / D-SA26-05 — A companion proof of relative compatibility | 3 | 5 | 5 | 1 | A complete, readable account of the successful and unsuccessful extension problems |
| 6 / D-SA26-06 — Restricted mixed exponential identities | 3 | 6 | 4 | 4 | A classification in a small, explicitly chosen setting, plus tests of the manuscript’s specialization |
| 7 / D-SA26-07 — Chronology and later Grothendieck parallels | 3 | 7 | 2 | 8 | A dated concordance with primary evidence and all unproved priority inferences removed |
| 8 / D-SA26-08 — Reconcile private project leads against actual records | 2 | 8 | 3 with packets; 1 without | 6 | A statement-level provenance comparison, without transferring statuses across different hypotheses |

## D-SA26-01 — Identify the literal cofibration axioms

**Origin.** Items `SA26-1`, `SA26-5`, `SA26-21`, `SA26-24` and `SA26-25`; claims `CL-SA26-106-01`, `CL-SA26-106-03`, `CL-SA26-106-07`, `CL-SA26-106-18` and `CL-SA26-106-21`; problems `MP-SA26-01`, `MP-SA26-04` and `MP-SA26-06`. The opening reference, the subsequent use of C3 and the final section criterion jointly determine the issue.

**What the task would establish.** Determine what the source actually names and which axioms it supplies or presupposes. Separate a theorem under that literal system from the affirmative theorem under the modern sufficient system H already checked in this dossier. The deliverable should include a small correspondence table, with a source for each axiom and a list of consequences used at each step.

**What is known.** Brown’s A–E, Porter’s dual C1–C5 and Baues’s factorization and weak-lifting statements have been opened and compared. The manuscript’s use of C3 is not enough to identify a book or rename the author. Rădulescu-Banu’s CF1–CF4 gives an exact sufficient modern setting, including a cofibrant initial object. Thomas’s strict joint-cofibration fractions give an exact later comparison, with no functorial-factorization hypothesis in that setting. [Brown1973, pp. 420–421; Porter1976, §2; Baues1989, I §1 and II (1.10); RadulescuBanu2009, 1.1.1 and 6.1.6; Thomas2012, 3.124–3.128.]

**First concrete step.** Inspect the actual images of 106/002, 014 and 016 beside the frozen TeX and the eight cote-106 reading rows. Record the ink decision independently of the theorem one hopes to prove. Then test the exact recovered axiom list against the uses of initial objects, pushouts, factorization and excision.

**Few-hour boundary.** With scans, the reading and hypothesis table is realistic. A theorem under a genuinely weaker system may require a separate run. Without scans, do not spend the run trying to infer lettering from mathematical plausibility; the current modern theorem already answers the well-specified question.

## D-SA26-02 — State the A-valued cotensor criterion precisely

**Origin.** Items `SA26-109`, `SA26-110`, `SA26-111` and `SA26-122`; claims `CL-SA26-107-04`, `CL-SA26-107-06`, `CL-SA26-107-08` and `CL-SA26-107-10`; problems `MP-SA26-31`, `MP-SA26-32` and `MP-SA26-33`.

**What the task would establish.** Give the intended companion theorem for closure of `Fun(B^op,A)` under the ambient cotensor, stating exactly which limits are needed for every component. Distinguish relative evaluation at one weight from representability of the entire B-diagram. If the manuscript intends a finite-weight setting, identify that setting before deciding whether finite limits suffice.

**What is known.** The secure criterion uses the categories of elements of every `h_b×M`. Complete A suffices. The checked two-element idempotent-monoid example refutes the weaker reading based on a presentation of M alone, even with representable M and finite products in A. The counterexample is a checked audit consequence, not a novelty claim. The standard density/weighted-limit framework is explicit in SGA4 and Kelly; Van der Linden’s displayed simplicial formula also contains the product with `Δ[n]`. [SGA4I, 3.4–3.5; Kelly1982, §§3.1, 3.7; VanDerLinden2006, §7.2, p. 123.]

**First concrete step.** Make a table of the weights actually used on 107/008–015: representables, boundaries and the uncertain marginal class. For each, write its indexing diagram and compare it with the limit hypotheses printed in the source. Check the doubtful margin on the scan when available.

**Few-hour boundary.** A precise statement, a proof reference and a compact companion example are attainable. An optimal necessary-and-sufficient criterion for arbitrary A and B is broader than this task and should not be assumed to be new or open merely because the manuscript abbreviates its hypotheses.

## D-SA26-03 — Positive scope for the sequential homotopy-class comparison

**Origin.** Items `SA26-114`, `SA26-115`, `SA26-116`, `SA26-119` and `SA26-123`; claims `CL-SA26-107-25`–`CL-SA26-107-29`, `CL-SA26-107-33` and `CL-SA26-107-34`; problems `MP-SA26-37`, `MP-SA26-38`, `MP-SA26-39`, `MP-SA26-41` and `MP-SA26-42`.

**What the task would establish.** For a specified class of sequential cofibration diagrams and a specified class of targets, determine when the known surjection on homotopy classes is injective. Keep this target-specific comparison distinct from existence of an ordinary colimit object, which would require the universal property for every target.

**What is known.** The unrestricted assertion is false. The degree-p circle example and the retraction tower in this dossier give exact failures under all the source’s simplicial cofibration/fibrancy hypotheses. The mapping-tower obstruction is a nonabelian pointed-set `lim¹` in general and an abelian quotient in the cohomological example. Condition(ii), preservation of simplicial weak equivalences under filtered colimit, is separately true. [Milnor1962, Lemma 2; Hatcher2002, §3F; Hirschhorn2015, Definition 1.1 and Theorem 2.1; Kerodon00XE.]

**First concrete step.** Fix one target family, for example an explicitly specified Eilenberg–MacLane family, and write the actual inverse tower controlling the relevant fibre. Check a proposed Mittag–Leffler or surjectivity condition against that tower, with basepoints and the degree stated. Search the exact resulting criterion before claiming a new positive result.

**Few-hour boundary.** A clean known criterion and one worked positive family are realistic. This run should not promise a general classification of ordinary colimits in `Hot`, nor transfer the result to an unspecified localizer or an invariant-ind-object problem with different hypotheses.

## D-SA26-04 — Higher comparison for the revised roof category

**Origin.** Items `SA26-11`, `SA26-13`, `SA26-17`, `SA26-19` and `SA26-26`; claims `CL-SA26-106-14`, `CL-SA26-106-16` and `CL-SA26-106-21`; problems `MP-SA26-02` and `MP-SA26-04`. The higher question is a modern extension of those component questions; it is **not** an additional question recovered from the manuscript.

**What the task would establish.** Determine whether the precise revised roof category, with the stated endpoint-fixed apex maps, has the desired mapping-space homotopy type under a specified set of axioms. If already covered by a theorem, supply the exact comparison. If not, state the missing comparison as narrowly as possible.

**What is known.** The present audit proves only `π₀` bijections through the joint-cofibration category J. Object replacement and replacement of each connecting arrow suffice for that conclusion, not for a nerve equivalence. The checked Cisinski result models the original roof nerve. Horel’s own partial-Brown construction has functorial hypotheses distinct from the general background theorem he cites. Low’s theorem and appendix have version-specific hypotheses. Thomas’s strict Z-roof comparison is an exact component-level anchor. [CisinskiK2010, Proposition 3.23; Horel2016, Introduction and Theorem 7.5; Low2015, Theorem 4.11 and Appendix A.5; Thomas2012, Theorem 3.128.]

**First concrete step.** Put all four categories `F₀,F₁,J,R` and their allowed morphisms in one definition table. For each candidate comparison functor, identify the exact theorem and the required comma-category or replacement property. Do not infer homotopy cofinality merely from the component argument already proved.

**Few-hour boundary.** An exact theorem match, or an explicit obstruction to applying it, is plausible. A full proof without functorial choices may take longer. No claim of novelty is warranted until the matching literature has been exhausted at this precise convention.

## D-SA26-05 — A companion proof of relative compatibility

**Origin.** Items `SA26-105`, `SA26-107`, `SA26-114` and `SA26-117`; claims `CL-SA26-107-29`–`CL-SA26-107-33`; problems `MP-SA26-39`, `MP-SA26-40` and `MP-SA26-41`.

**What the task would establish.** Produce the companion exposition that follows the manuscript’s successive attempts, states the strictification criterion with its endpoint-relative condition, and explains exactly why one-endpoint extension proves surjectivity while two-endpoint extension does not prove injectivity.

**What is known.** Both directions of the criterion and the covering-space counterexample have been checked. The surviving source margin already contains “iff”. Quillen II §2 Proposition4 matches the mathematical content; the modern retypesetting’s numbering is known, but the handwritten original page numeral is not settled. The source’s general-model-category scope requires compatible cylinders or framings, rather than an unannounced simplicial tensor. [Quillen1967; QuillenRetypeset2022; Hirschhorn2015, Theorem 2.1.]

**First concrete step.** Prepare a three-column diagram sheet: source diagram and literal labels, typed modern diagram, and exact lifting hypothesis. Use the source images to decide the bar on the strict diagonal, the homotopy parameter and the next-stage index; leave each undecided until the ink is inspected.

**Few-hour boundary.** The mathematical exposition is readily finishable from the existing proofs. The remaining source decisions require scans. This is an editorial and explanatory task, not a search for a new relative lifting theorem.

## D-SA26-06 — Restricted mixed exponential identities

**Origin.** Items `SA26-101`, `SA26-103`, `SA26-108`, `SA26-112`, `SA26-120` and `SA26-121`; claims `CL-SA26-107-12`–`CL-SA26-107-19`; problems `MP-SA26-34` and `MP-SA26-35`.

**What the task would establish.** For one explicitly chosen class of bases and weights, characterize when the mixed constant-map arrow is an isomorphism, and explain how that restricted statement differs from the universally false formula in the manuscript. Preserve the independent validity of projection pullback preservation of exponentials.

**What is known.** Four exact finite counterexamples dispose of the unrestricted separate/joint, external-Hom and mixed-exponential identities. Genuine Yoneda and the separate extension theorem survive. The source’s specialization involving terminal factors has uncertain prime/scope information; mathematical truth alone cannot decide it. [SGA4I, 1.4 and 3.4–3.5; SGA4IV, 10.2.1; Kelly1982, Theorem 4.51; saved finite certificates.]

**First concrete step.** Choose a small setting such as simplicial sets, write the precise component formula for the mixed exponential, and test the proposed restriction on small weights. Compare its quantified statement with the actual specialization at 107/016 before drafting a general theorem.

**Few-hour boundary.** A restricted classification or an exact standard theorem match is realistic. Do not replace the false assertion by an unproved blanket “connectedness” condition, and do not treat the nearby matching-object scratchwork as a theorem about arbitrary weights.

## D-SA26-07 — Chronology and later Grothendieck parallels

**Origin.** Items `SA26-20`, `SA26-21`, `SA26-200`, `SA26-201`, `SA26-202`, `SA26-203` and `SA26-206`; claims `CL-SA26-106-01`, `CL-SA26-106-21`, `CL-SA26-107-14` and `CL-SA26-107-26`; problems `MP-SA26-01`, `MP-SA26-04`, `MP-SA26-32` and `MP-SA26-37`. The claims and problems identify the mathematical passages to date, not evidence of a historical influence.

**What the task would establish.** A primary-source concordance between these leaves and the later replacement, representability and colimit passages, distinguishing composition, first circulation, publication and electronic-edition dates. It should identify what is demonstrably a repeated question, what is merely a parallel, and what remains undated.

**What is known.** Reused 1982 printouts do not date the mathematical writing. The 2015 complete electronic *Pursuing Stacks* edition and SMF 2022 Volume I have different coverage. §125’s Baues discussion begins at old p. 531. The *Dérivateurs* original-text editions provide specific later passages, but their modern edition dates do not date the 1990–1991 composition. [MontpellierCatalogue; GrothendieckPS2015, §125; GrothendieckPS2022, Notice; MaltsiniotisDER; GrothendieckDER_VI, Théorème-Scholie2(I); GrothendieckDER_XVIII, §4.2.]

**First concrete step.** Inspect covers, versos, dated headings and any explicit cross-reference on the actual106/107 scans. Add only verifiable dates to the already checked passage table; identify the witness for every date. Use the later works as comparison texts, not as substitutes for a missing autograph date.

**Few-hour boundary.** A defensible concordance is attainable if the archival images are available. A priority claim or an explanation of why a problem was left unfinished requires correspondence or other independent historical evidence and may remain out of reach.

## D-SA26-08 — Reconcile private project leads against actual records

**Origin.** Items `SA26-19`, `SA26-203`–`SA26-210`, `SA26-114` and `SA26-123`; claims `CL-SA26-106-14`, `CL-SA26-106-21`, `CL-SA26-107-25`, `CL-SA26-107-26`, `CL-SA26-107-31` and `CL-SA26-107-34`; problems `MP-SA26-02`, `MP-SA26-04`, `MP-SA26-37`, `MP-SA26-38`, `MP-SA26-40` and `MP-SA26-42`.

**What the task would establish.** Reconcile a small, selected set of reported project statements with their actual proof and review records. The deliverable should distinguish statement equality, implication with additional hypotheses, thematic overlap and no relation. It must preserve the difference between a theorem’s truth and a report about who proved or checked it.

**What is known.** This dossier preserves all255 concordance rows, all12 NEW_RESULTS entries and K1–K3 notices, the exact prover/checker cells and run-path directory. Public original passages have been compared where accessible. Missing private originals and historical check records remain attributed reports. A mathematical resolution for W∞ here does not settle a differently stated CATHOT, PATHS, BISITE or RESIDUE question. [PrivateResultsState; PrivateDossierStatements; PrivateNewResults; the separate provenance tables and the current `SA26_links.tsv` evidence fields.]

**First concrete step.** Obtain the exact named result file, proof and independent review for one selected row. Compare its quantified statement against the relevant claim in this dossier before inspecting its status label. For a publicly retrievable finding, use the actual retrieved text and version as recorded in the provenance audit; do not treat repository identity alone as access to a finding.

**Few-hour boundary.** A handful of complete statement-level reconciliations is realistic with the packets. Revalidating270 project leads or resolving conflicting status registers is not a single-run task. Without the missing records, no new theorem-status change should be made.

## Scheduling boundary

These directions are ranked proposals only. No future automation, external message, repository change or project-status update has been created. Each task should receive its own exact input set and scope when undertaken. The archive’s claims map and problem index remain confined to cotes106 and107.
