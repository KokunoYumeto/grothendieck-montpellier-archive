# B.3–B.4 research outcome

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026. No priority claim. Complete proofs are in bmodels.tex; its editable components are bmodels_b3.tex, bmodels_b4.tex and bmodels_b4_extra.tex.

## Outcomes and exact scope

| Task | Outcome | Statement |
|---|---|---|
| B.3 / L1 / R12 | Refuted literally: six-element C1–C8₀ lattice, with C4 bis, not any prime-event configuration poset. | SA21-BM-r12 |
| Corrected B.3 | Exact iff: locally distributive finite-figure systems, equivalently multistrates prime for bounded joins, correspond to binary-conflict prime events with finite causes. | SA21-BM-event-iff |
| Binary/general prime events | Ternary consistency gives the distinction and violates C3. | SA21-BM-binary |
| Domains and supports | Ideal completion is the full configuration domain. Whole-figure supports are event-disjunction closed polars. Refinement is additional structure. | SA21-BM-domain; SA21-BM-refinement |
| B.4 / L5 | Proved for the specified closed-support generalized-cell frontier model on every definable X in an o-minimal real closed field, parameters allowed. | SA21-BM-cell-definition through SA21-BM-cell-moderation |
| All B.1 axiom clauses | Chronological truth table, full proofs and explicit failures. | SA21-BM-cell-axioms; SA21-BM-cell-limits |
| Faithfulness and supports | Full powerset P(X), including nondefinable subsets. | SA21-BM-cell-support |
| Extension | Explicit unique coarsest extension; no triangulation needed. | SA21-BM-cell-extension |
| Literal At14bis | All-target order reflection fails for a subdivided interval; corrected exterior-target clause holds. | SA21-BM-14bis-reading |
| Moderation | Compatible triangulation gives common subdivision of every finite collection. | SA21-BM-cell-moderation |
| B.2 coordination | Refinement components are definable connected components of X. Within one finite figure, incidence components equal support components. | SA21-BM-cell-connected |

The six-element obstruction satisfies exactly the C1–C8₀ package, not later open-shadow lieu divisibility. Its subdivision is equality and refinement incidence. Its multistrates d,a,b,c are incidence connected, so C4 cannot repair its missing distributivity.

In the o-minimal model, a multistrate remembers its entire boundary decomposition. Supports are closed in fixed X; closures need not be regular cells. The model is not generally polyhedral or simplicial. Global incidence C4 fails while the corrected refinement connectedness holds.

CL(pol) and At CD2′ are TRUE: they add hypotheses to sufficient compatibility criteria. The biconditional At9″ is FALSE. Sibling axioms caught this distinction during the audit; it is corrected in all current fragments.

## Computation

Code: code/bmodels_checks.py. Output: code/bmodels_checks_output.json. Python standard library only.

- Exhaustive binary-event checks on all labelled orders and hereditary conflicts with 0–4 events: 963 structures, 6,728 configuration occurrences. Structures by n: 1,1,4,41,916. C1–C3 and reconstruction pass.
- Ternary consistency: axioms pass; all eight binary graphs fail to represent it.
- Six-element literal contrée: all64 families used to determine suprema/irreducibility; C1–C4bis and equality-subdivision clauses checked; missing downset and nondistributivity verified.
- Two refinement systems on one two-event skeleton: Mag1–4, divisibility and MagL2 verified, lieux differ.
- Two-arc circle and monogon: finite incidence checks for Atpol1/Atsimp1 failure. Geometric realizations proved in paper.
- Subdivided interval: complete five-stratum carrier; literal At14bis fails; exterior clause holds.
- Latest complete run: all assertions passed, 0.283964 seconds measured in program.

Enumeration establishes only its stated finite scope. General equivalences and the o-minimal model have independent proofs in the paper.

## Corrections to supplied material

CORRECTIONS.tsv records 30 source-resolved corrections or explicit scope annotations, with exact supplied filenames and verified line ranges. It includes the duplicated earlier check verdicts, H1/H6-2/H9-3 leads, the configuration-domain distinction, literal At14bis and the At9-double-prime/CL(pol) chronology.

1. study/STUDY.md lines250–261, especially259/261; study/CHECK_EVENTS.tsv line6 (SA21-C3-05); prompt line77 (R12), line90 (L1): irreducibility does not imply deployment preserves joins as unions. Exact repair: SA21-BM-event-iff.
2. J156-4-07_transcription.tex line100, scan54, defines irreducibility by equality with a supremum. Scan55's union claim lacks local distributivity. This is a mathematical defect, not a change of that equality into another reading.
3. FINAL SOURCE CORRECTION: study/readings/156-6.md line58 and SA21-R6-12 are VALID under explicit156-6(1.20), J156-6-02 lines77-84, which defines bounded-join primality. The earlier bmodels refutation is withdrawn and its audit rows are explicitly superseded. Equality-based counterexamples apply to156-4 and the explicit independent atlas definition at156-8/20, not the actual prime156-6 definition.
4. study/readings/156-6_INTEGRATION.md line82: a Shiota-type theorem is unnecessary for At14 in this general-cell model. Extension is explicit. Compatible triangulation is needed for moderation. Fixed simplices form a different model.
5. J156-6-12_transcription.tex scan88: the mixed-order clause ranges its second variable over all F′. This fails for interval subdivision with G=F. The exterior-variable correction is separate. Sibling axioms visually checked the ink.
6. L5 needs its definitions fixed: arbitrary nonclosed supports with self-relative closures fail disjoint-support compatibility (interval plus endpoint).
7. Winskel1987 Definition1.3.4 allows higher consistency; the exact binary subclass is §3.4.6.

## Source audit

Complete bibliographic entries and opened states are in references.bib.

- Grothendieck156-4: complete official89-page PDF fetched; PDF54/55/72/73 visually inspected. Equality-based irreducibility, the false join-union corollary and unqualified C6(a) uniqueness confirmed.
- NPW1981: full author PDF; printed99 and102 visually inspected; Def14 and Thms8–9 used.
- Winskel1987: full author PDF; Def1.3.4 pp335–336, §3.4.6 p378; official Springer metadata checked.
- Birkhoff1948: full scan; ChapterIX §4 Lemma1 and Thm5, p139, visually inspected.
- Coste1999: full author notes in web reader; §1.3 pp9–10 (arbitrary real closed field); Thm3.4 pp26–27; Thm3.9 p28; Thm3.22 pp34–35; Thm4.4 p42, proof42–44. Primary statements re-opened and checked.
- Van den Dries1998: official chapter metadata/contents opened; linked full PDF timed out or returned503. Standard locator Chapter8 §2 Thm2.9 cross-checked in seminar bibliography. We rely on the opened Coste equivalent, not this inaccessible page.
- Shiota1997: official publisher metadata and contents opened, full text not opened; no Hauptvermutung is invoked.
- Pillay–Steinhorn1986: official AMS PDF returned403; bibliographic data confirmed in author publication list. Full text NOT OPENED, and no theorem from it is used.

Fetched full PDFs, extracted texts and rendered source pages are in /workspace/scratch/ab1b9070a65e/SA21_sources/bmodels/ outside the deliverable fragments. Short provided-transcription excerpts remain in this part's sources folder.

## Literature search scope

Queries included Grothendieck with the exact terms contrées/event structures, atelier/o-minimal/156 and formes/prime event. No relevant published comparison emerged in those searches. This does not prove absence of prior work. Root subsequently identified a 2002 Montpellier forms seminar and 2025 Carmona slides and is auditing them. All established event-domain and finite distributive representation results are credited. No novelty or priority claim is made.

## Handoff

All B.3/B.4/L1/L5 mathematical claims are written as complete proofs or counterexamples with exact replacements. Root independently audits integration, notation and typesetting. Updates should be made in the three components and then merged. Final source-image checks of156-4/54–55 and72–73 are complete and recorded in CHECK_EVENTS.tsv and AXIOMS_AUDIT.md. Independent proof audits of root support and support-transfer results and the sibling axiom countermodels are in the three audit notes in this directory.
