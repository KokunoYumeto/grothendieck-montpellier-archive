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
- https://www.numdam.org/article/PMIHES_1964__20__5_0.pdf — original EGA zero-IV scan, downloaded in full, SHA256 and bytes in `logs/algebra_fetch_ega.txt`; printed pp.85–86 (19.3.12), p.94 (19.5.5–19.5.6), 20.4.6, 20.4.13(iv).
- https://geotoppos.org/divers/ega41.pdf — mirror of the same primary scan, opened by web tool before the full download completed.
- https://www.numdam.org/article/PMIHES_1967__32__5_0.pdf — original EGA IV-4 scan, downloaded in full, printed pp.6–7 (16.1.5–16.1.6), pp.206–209 (19.5.5–19.5.6), pp.227 onward (meromorphic sections).
- https://stacks.math.columbia.edu/tag/07PK — Proposition 15.50.2, opened for the independent audit of root's A.3 argument; complete-local formal smoothness is equivalent to regularity.
- https://stacks.math.columbia.edu/tag/08SM — Lemma 92.16.1, opened for the A.3 audit; square-zero ring-map obstruction lies in Ext² of the cotangent complex.

## Secondary textual witnesses, explicitly not substituted for originals

- https://grothendiecksga.com/read/sga6/fr/VII-1.html — modern French transcription of SGA 6 VII 1.1–1.8. Proposition 1.7(iii) retains the Noetherian hypothesis. The original SGA 6 scan is not yet opened.
- https://jcreinhold.github.io/ega/iv/29-ch4-16-differential-invariants.html — modern English translation used initially to locate EGA IV 16.1.5–16.1.6; their immersion hypotheses were subsequently verified against the original Numdam scan.

## Searches and outcomes

Earlier searches (web response archives `algebra_web_01.json` through `algebra_web_16.json`) covered minimal Cohen factorization/AFH, regular sequences and fpqc descent, the exact SGA 6 VII transitivity statements, Artin–Rees/pro-Tor, the EGA locators, and the Ext/grade criterion. These files preserve the returned sources; the early request payloads were not separately persisted. Exact opened URLs are listed above.

The later exact searches include:

- `"19.3.12" "smooth" Grothendieck`; `"19.3.12" "lisse" erreur`; `"formally smooth" "linearly compact" Artinian lifting` (`algebra_web_17.json`). They located the printed proposition and mirrors but no source for the particular square-zero/closed-power repair. We therefore prove it in full and claim no novelty.
- `EGA IV "19.5.5" "19.5.6"`; `EGA III "4.3.6" K completion`; `EGA "19.3.12" "errata"` (`algebra_web_18.json`, stronger search engine). Coverage was poor; primary scans were obtained directly instead.
- `algebraic field extension polynomial presentation monic regular sequence artinian flat arbitrary lifts`; `"Cohen factorization" "minimal" Avramov Foxby Herzog`; `Koszul regular quasi regular nonnoetherian idealization regular sequence permutation`; `"graded" "A tensor" "flat" "section" algebra good conditions` (`algebra_web_20.json`, including full request). No exact source for the arbitrary-cardinality algebraic-field presentation was located. A complete elementary proof is given in B.2. Stacks provides nearby general regular-sequence facts and an independent example; the exact idealization counterexample is proved directly.

## Reproducible programs and outputs so far

- `code/algebra_fetch_ega.py`, output `logs/algebra_fetch_ega.txt`: original Numdam downloads, bytes, hashes, elapsed time. Large downloads continue independently of proof work.
- `code/algebra_fetch_mirrors.py`, output `logs/algebra_fetch_mirrors.txt`: geotoppos direct-download attempt; all three returned HTTP 403. Browser/search retrieval of the first mirror did work. No unavailable mirror is treated as opened by download.
- `code/algebra_fetch_more.py`, output `logs/algebra_fetch_more.txt`: parallel Montpellier cote 23 and William Stein mirror retrieval, in progress at this checkpoint.
- `code/algebra_extract_sources.py`, output `logs/algebra_extract_sources.txt`: Poppler extraction and exact-locator indexing; original PDF has harmless OCR syntax warnings, preserved in the rendering log where applicable. The extraction uses the original bytes without alteration.
- `code/algebra_render_sources.py`, output `logs/algebra_render_sources.txt`: original-source page images for direct reading. Rendering a page alone is not counted as visual inspection; inspected pages are named in the check record.
- `code/algebra_finite_checks.py`, output `logs/algebra_finite_checks.txt`: exhaustive four-element ring laws (64 triples, 16 pairs, 4 elements), all 16 source and 32 target tensor-balancing relations, and two further finite graded counterexamples. Runtime 0.000259 seconds on the recorded run. This proves the finite counterexample by exhaustive linear algebra; it makes no assertion about the infinite examples.
- `code/algebra_update_registry.py`, output `logs/algebra_update_registry.txt`: mergeable statement and check-event tables, generated from the numbered LaTeX fragments and explicit audit records.

## Current exact gates

B.1, B.2, C.1–C.3 and the three G implications have complete proofs/refutations on disk. Original scan-dependent readings of C/G await cote 23 download; the mathematical alternative readings are explicitly separated. D.1 is complete and independently audited by root. Remaining D items are actively being compared with the now available original IV-4 scan; III-1 download is still pending. No partial D completion is claimed.
