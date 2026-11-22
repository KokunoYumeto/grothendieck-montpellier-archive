# Algebra research source and search log

Date: 20 November 2026. Work: GPT-6 Astra (OpenAI), inherited effort,
`algebra_letters` run. No priority is claimed for constructions proved here.

## Exact opened primary URLs and locators

- https://arxiv.org/pdf/1205.2119 — Nasseh–Sather-Wagstaff, version 3 (30 May 2013), Definitions 2.3 and 2.5 and Fact 2.6(a), PDF pp.3–4. This is the opened statement used for the minimal Cohen factorization. The original AFH 1994 article itself has **not** been opened.
- https://researchprofiles.ku.dk/da/publications/structure-of-local-homomorphisms/ — original AFH bibliographic metadata, DOI 10.1006/jabr.1994.1057.
- https://stacks.math.columbia.edu/tag/062D — Section 15.31, regular/Koszul/quasi-regular implications and Noetherian local equivalence, Lemma 15.31.7.
- https://stacks.math.columbia.edu/tag/00LH — Example 10.68.3, nonpermutable regular sequences.
- https://stacks.math.columbia.edu/tag/067M — regular ideal sheaves.
- https://stacks.math.columbia.edu/tag/0638 — regular immersions, conormal and transitivity lemmas.
- https://stacks.math.columbia.edu/tag/06LD — completion and flatness, Lemmas 15.28.2–15.28.3.
- https://stacks.math.columbia.edu/tag/09B7 — inverse systems, Lemma 10.98.2.
- https://stacks.math.columbia.edu/tag/00LE — depth, Section 10.72. It was inspected but **not used** to justify a general ideal-grade theorem; the Ext argument is instead proved directly in C-8.
- https://www.numdam.org/article/PMIHES_1964__20__5_0.pdf — original EGA zero-IV scan, downloaded in full; printed p.19 (15.1.19), pp.85–86 (19.3.12), p.94 (the actual zero-IV19.5.5–19.5.6, which are NOT the letter's filtered propositions), pp.123–127 (20.4.1–20.4.13). Exact bytes and hash are recorded below.
- https://geotoppos.org/divers/ega41.pdf — mirror of the same primary scan, opened by web tool before the full download completed.
- https://www.numdam.org/article/PMIHES_1967__32__5_0.pdf — original EGA IV-4 scan, downloaded in full, printed pp.6–7 (16.1.5–16.1.6), pp.206–209 (19.5.5–19.5.6), pp.227 onward (meromorphic sections).
- https://www.numdam.org/article/PMIHES_1961__11__5_0.pdf — original EGA III-1 scan, downloaded in full; III4.3.6, printed pp.132–133. Printed p.133 is physical PDF page130; this differs from the IV-volume offset.
- https://library.slmath.org/nonmsri/sga/sga/pdf/sga6.pdf — original full SGA6 scan, downloaded and visually inspected. ExposéVII by Pierre Berthelot, 1.1–1.7, printed pp.416–423, physical423–430; June1971 Preface on physical2. Mathematical definitions and the Noetherian restriction in1.7(iii) were checked directly.
- https://link.springer.com/book/10.1007/BFb0066283 — official publisher metadata for SGA6; https://link.springer.com/chapter/10.1007/BFb0066291 — official VII metadata, author and pp.416–465.
- https://grothendieck.umontpellier.fr/23.pdf — complete original archival scan. Physical53–54 (footer52–53) are the PS; physical96–98 (footer95–97) are the graded notes. These pages were visually inspected. The PS is undated. Its visible degree line has a blank before0; a positive-degree sign is editorially reconstructed from the surrounding mathematics and final published definitions, not read from recovered ink.
- https://stacks.math.columbia.edu/tag/09PN — Lemma23.6.9, Tate resolution construction, including the full inductive proof. For a quotient R to R/I one starts in degree0 with R; adjoining the degree1 generators gives exactly the chosen Koszul complex. Used in C7.
- https://stacks.math.columbia.edu/tag/00IN — Lemma10.51.2, Artin–Rees; used in B1.
- https://stacks.math.columbia.edu/tag/00ON — Lemma10.112.7, dimension formula; used in the minimal-factorization comparison.
- https://stacks.math.columbia.edu/tag/0BNH — Lemmas10.97.1–10.97.3 and10.97.8, finite-module completion and semilocal decomposition; used in D11.
- https://stacks.math.columbia.edu/tag/00IQ — Lemma10.51.5(2), Krull intersection in the Jacobson radical; used in D6.
- https://stacks.math.columbia.edu/tag/07PK — Proposition 15.50.2, opened for the independent audit of root's A.3 argument; complete-local formal smoothness is equivalent to regularity.
- https://stacks.math.columbia.edu/tag/08SM — Lemma 92.16.1, opened for the A.3 audit; square-zero ring-map obstruction lies in Ext² of the cotangent complex.

## Secondary textual witnesses, explicitly not substituted for originals

- https://grothendiecksga.com/read/sga6/fr/VII-1.html — modern French transcription used initially. Its VII1.1–1.7 statements were subsequently checked against the original SGA6 scan listed above; the original, not this transcription, supports the final theorem identification.
- https://geotoppos.org/divers/SGA6.pdf — a short modern table-of-contents reconstruction, NOT the original full SGA6. It was opened while locating the full volume and is not substituted for it.
- https://jcreinhold.github.io/ega/iv/29-ch4-16-differential-invariants.html — modern English translation used initially to locate EGA IV 16.1.5–16.1.6; their immersion hypotheses were subsequently verified against the original Numdam scan.

## Searches and outcomes

Earlier searches (web response archives `algebra_web_01.json` through `algebra_web_16.json`) covered minimal Cohen factorization/AFH, regular sequences and fpqc descent, the exact SGA 6 VII transitivity statements, Artin–Rees/pro-Tor, the EGA locators, and the Ext/grade criterion. These files preserve the returned sources; the early request payloads were not separately persisted. Exact opened URLs are listed above.

The later exact searches include:

- `"19.3.12" "smooth" Grothendieck`; `"19.3.12" "lisse" erreur`; `"formally smooth" "linearly compact" Artinian lifting` (`algebra_web_17.json`). They located the printed proposition and mirrors but no source for the particular square-zero/closed-power repair. We therefore prove it in full and claim no novelty.
- `EGA IV "19.5.5" "19.5.6"`; `EGA III "4.3.6" K completion`; `EGA "19.3.12" "errata"` (`algebra_web_18.json`, stronger search engine). Coverage was poor; primary scans were obtained directly instead.
- `algebraic field extension polynomial presentation monic regular sequence artinian flat arbitrary lifts`; `"Cohen factorization" "minimal" Avramov Foxby Herzog`; `Koszul regular quasi regular nonnoetherian idealization regular sequence permutation`; `"graded" "A tensor" "flat" "section" algebra good conditions` (`algebra_web_20.json`, including full request). No exact source for the arbitrary-cardinality algebraic-field presentation was located. A complete elementary proof is given in B.2. Stacks provides nearby general regular-sequence facts and an independent example; the exact idealization counterexample is proved directly.

## Reproducible programs and outputs so far

- code/algebra_fetch_ega.py, output logs/algebra_fetch_ega.txt: all three original Numdam downloads completed; elapsed1757.473329 seconds, with exact bytes and hashes below.
- `code/algebra_fetch_mirrors.py`, output `logs/algebra_fetch_mirrors.txt`: geotoppos direct-download attempt; all three returned HTTP 403. Browser/search retrieval of the first mirror did work. No unavailable mirror is treated as opened by download.
- code/algebra_fetch_more.py, output logs/algebra_fetch_more.txt: the preliminary parallel Montpellier/William Stein retrieval was interrupted without a completed file or returned output. It is not treated as a successful opening. The separate completed programs below supersede it.
- `code/algebra_extract_sources.py`, output `logs/algebra_extract_sources.txt`: Poppler extraction and exact-locator indexing; original PDF has harmless OCR syntax warnings, preserved in the rendering log where applicable. The extraction uses the original bytes without alteration.
- `code/algebra_render_sources.py`, output `logs/algebra_render_sources.txt`: original-source page images for direct reading. Rendering a page alone is not counted as visual inspection; inspected pages are named in the check record.
- code/algebra_finite_checks.py, output logs/algebra_finite_checks.txt: exhaustive four-element ring laws (64 triples,16 pairs,4 elements), all16 source and32 target tensor-balancing relations, plus all THREE G4 graded counterexamples. Latest recorded runtime0.000233 seconds. This certifies only these finite examples; the infinite constructions have separate mathematical proofs.
- `code/algebra_update_registry.py`, output `logs/algebra_update_registry.txt`: mergeable statement and check-event tables, generated from the numbered LaTeX fragments and explicit audit records.

## Further programs and exact source comparison

- code/algebra_fetch_manuscript23.py, logs/algebra_fetch_manuscript23.txt: complete Montpellier23 original, elapsed886.577587 seconds.
- code/algebra_fetch_sga6.py, logs/algebra_fetch_sga6.txt: complete SLMath SGA6 original, elapsed7.712320 seconds. Web parsing rejected the size, but this direct original-file download succeeded.
- code/algebra_extract_sga6.py, logs/algebra_extract_sga6.txt: extraction found only sparse digital page-number text. The chapter was therefore read from rendered originals, not from nonexistent extracted prose.
- code/algebra_render_more.py, logs/algebra_render_more.txt: original SGA6 and extra EGA pages; repeat runs skip already rendered files and preserve new run outputs.
- code/algebra_render_manuscript23.py, logs/algebra_render_manuscript23.txt: original physical44–47,52–54,60,65,96–98 rendered; elapsed59.249155 seconds. Rendering alone is not counted as visual inspection.
- code/algebra_reorder_sections.py, logs/algebra_reorder_sections.txt: moved D12–D16 after D11; final count16 D statements.
- code/algebra_write_corrections.py, logs/algebra_write_corrections.txt: verifies unique anchors in the attached files and writes exact file-plus-line corrections. The initial failed duplicate-anchor attempt and the successful reruns are retained.

Exact original-file provenance:

| File | Bytes | SHA256 |
|---|---:|---|
| EGA0IV.pdf |31990654|df11afc6b6318fc491032b1239cd4af9cbc2a7c73219dcc49bf65e5ee6c13140|
| EGAIV4.pdf |49852990|b4277fb99c6edf8feec5b01f54368e4b8521bcd52871316c0edf6ff4ae69389e|
| EGAIII1.pdf |19942549|3ed59fe81da07f1ab685ddc54a93128a364419d4ddafbc7affcd8abc8b401605|
| algebra_SGA6.pdf |54325694|5194436e290b8fca54bacd5ff672588335408f1aad3ae07d62bba68df35e3d76|
| algebra_manuscript23.pdf |38145060|4e34450a12349194215f837a7d683c4fc45255ebd60a69ffa09dd5ff12420a6c|

Visually inspected source pages relevant to final conclusions include:

- EGA0IV physical18 (printed19,15.1.19), physical93 (printed94,actual19.5.5 and19.5.6 heading), physical124 (printed125,20.4.6).
- EGAIV4 physical188 (printed189,19.1.8),206–208 (printed207–209,19.5.5–19.5.6),226 (printed227,20.1.3),260 (printed261,21.2.9),270 (printed271,21.6.2),346–347 (printed347–348,ErrIV8,12–14).
- EGAIII1 physical130 (printed133,4.3.6). Physical132 was first read during locator checking but is printed135, not the cited page.
- SGA6 physical423–430 (printed416–423) and physical2–3 (Preface and introduction). Extra rendered pages not specifically listed here are not automatically counted as inspected.
- Montpellier23 physical45–47,52–54 and96–98. The archive footer is one less than the physical PDF page number; all section citations distinguish them. Physical45–47 were inspected on the final Lê item-by-item coverage pass; the crossed-out21.2.12 and21.3.6 entries are explicitly recorded as withdrawn.

The original IV4 ErrIV12 has an additional printed defect: its first instruction says to replace p2−p1 by p1−p2, even though the original0IV20.4.6.1 already has p1−p2. Its tensor clause and ErrIV13 both give the opposite, coherent correction d=p2−p1. D7 records the discrepancy explicitly instead of silently normalizing the erratum.

## Later searches and outcomes

Requests and outputs24–29 are both preserved in the corresponding algebra_web JSON files.

- Search24: site.stacks.math.columbia.edu Tate resolutions divided power differential graded algebra resolve quotient Koszul; SGA6 pdf ExposéVII immersions régulières Koszul. This led to the exact Tate construction.
- Search25: SGA6 pdf1971; SGA6 VII Deligne1.7, using the stronger search engine. Search26 opened the modern short table of contents and Stacks062D. Search27 located the official publisher chapter metadata and the SLMath original. Search28 attempted web parsing of the original and opened the chapter metadata; direct download followed.
- Search29: Grothendieck Berthelot1966 immersions régulières; SGA6 VII1967 janvier; SGA6 Koszul letter, using the stronger engine. No exact dated lecture header or documentary causal attribution of VII to this PS was found. A secondary repost of an Illusie recollection was not used as primary evidence. The original PS and SGA volume are the actual documentary evidence used.

## Completion and exact historical limit

B1–B2, C1–C9, all seventeen D results, and G1–G4 now have complete proofs or counterexamples. C9 explicitly refutes the blanket forecast for zero-IV section15 using15.1.19, with a finite-module nonvacuous variant and a complete-filtration repair. C10 records the exact SGA6 identification. D17 separately proves the true literal zero-IV19.5.5 finite-conormal testing remark; zero-IV19.5.6 is a proof heading, not a standalone19.5.6(ii). Root has targeted-check events for B1–B2, C1–C9, D3, and D7–D16; our audits of root A3 and A4 are in algebra_root_A_audit.md. Check events distinguish an audit from independent discovery.

The original AFH1994 paper is not opened; the opened Nasseh–Sather-Wagstaff theorem statement suffices for the known Cohen-factorization input. No unstated original-source claim is made for AFH. The PS cannot be the first instant at which all the reported work was invented, because it reports a prior Berthelot verification. Its exact causal influence on later published wording, or an absolute priority claim for the definition, remains undocumented by the opened sources. This historical limit does not leave the mathematical identification open.

## Final targeted audits and source checks

- Search30 tried the missing condition-P identification using Grothendieck/Cohen/formal-projective queries and the archive. It found no missing definition. The retained draft begins after the relevant section. Internal use of a countable strict limit of projectives supports the strict-formal-projectivity reading but is not substituted for an absent definition. The query and results are preserved in algebra_web_30.json.
- Retrievals31–33 independently opened the ICM1970 original, Fontaine1982 and Colmez–Fontaine author texts for categoryJ9. Exact URLs, theorem locators, and the visual/source distinction are recorded in algebra_category_audit.md; I12 and L5 were also checked there. Kisin's actual downloaded DVI text and the Beilinson–Drinfeld author chapter were read locally. No secondary exposition is used for their theorem statements.
- Root subsequently targeted-checked C9's finite-module counterexample and complete-filtration repair, and independently viewed the original printed ErrIV12 to confirm its reversed first substitution. These are additional check events, not retroactive independent-discovery claims.
- Broad supplied sweep IDs SA23-25 and SA23-27 are retained in narrowly scoped new events. The former event concerns our C/D and Deligne-factorization work; the latter only the graded-flatness sheets. Neither event claims a new check of every unrelated item bundled under those broad IDs.
