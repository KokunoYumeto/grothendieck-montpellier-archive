# TRACE_DET evidence index

This index covers the release through **DET-19 and MAS-12**. Paths below are relative to the final ZIP root: the paper and registers are at the root, and supporting documentation remains under `work/`. The final paper states the results; research notes preserve their development and may contain explicitly superseded intermediate gates.

## 1. Start with the final deliverables

| File | What it establishes or records |
|---|---|
| `TRACE_DET.tex` and `TRACE_DET.pdf` | The standalone paper and its 81-page reading copy: finding IDs, complete proofs, exact source locators, hypotheses, and separate unresolved identifications in Part II. |
| `QUESTIONS.tsv` | Each treated question and its proved/refuted result or precise remaining gate. |
| `CHECK_EVENTS.tsv` | Dated source readings, proof checks, independent re-proofs and computations, with reviewer/model/run information and the originating event filename. |
| `LEDGER.md` | Dated progress, attempted routes, gate changes, checkpoint receipts and review timing. Later entries supersede earlier provisional states. |
| `IMPLICATIONS.md` | Consequences for cote 1, the SA23/Fable runs, the cited literature and the RH programmes. |
| `TRANSCRIPTION_NOTES.tsv` | Exact cote/scan/line repairs, their mathematical reasons, and the remaining manuscript-image attribution limits. |
| `README.md` | Short reading and compilation guide. |

For the main question, read B-01, DET-06/10, DET-15–19 and Part II. For Masullo, read the statement comparison and MAS-10–12. A determinant identity, positivity in a specified Hilbert metric, and an identification of group actions are distinct conclusions.

## 2. Main determinant research and proof documentation

**Concrete Xi operator and the toy proposal — B-01–03, TOY-01–02, DET-01–05/08.**
`work/root_proofs.md` and `work/determinants_audit.md` contain the initial constructions, refinements and counterexamples. The numerical corroboration is reproducible from `work/check_toy.py`, with output in `work/check_toy_results.json`; it supplements the proofs. `work/det05_mas_check.md` records a separate check of the positive-limit criterion and its scope. The integrated base text is `work/paper_core.tex`.

**Actual finite source determinants, signed geometry and period frames — DET-06–07/10/12/14.**
Start with `work/determinants_actual_sources.md`, then `work/period_positive_bridge.md` and `work/gram_kernel_independent.md`. The independent step-4 search also contains the finite inertia proof: `work/step4_adaptive.md`. Final sections are `work/paper_actual_determinants.tex`, `work/paper_signed_kernel.tex` and `work/paper_period_frame.tex`. These records distinguish the signed source determinant, its valid determinant-line interpretation, and constructed positive frames.

**Positive Berezin transform — DET-13.**
`work/positive_kernel_independent.md` gives the source comparison and frame construction. `work/positive_kernel_source_manifest.json` records the primary Neretin source and exact locators. Final proof: `work/paper_positive_kernel.tex`.

**Fixed Bessel model and arithmetic weight tests — DET-15/17.**
Use `work/bessel_projector_bridge.md`, `work/bessel_projector_independent.md` and `work/bessel_instantiation_weights.md`. The last follows the actual source instantiation and distinguishes finite tensor weights, constant weights and von Mangoldt weights; its searches are preserved in `work/bessel_instantiation_search_manifest.json`. Final proofs: `work/paper_bessel_projector.tex` and `work/paper_bessel_weights.tex`.

**Scalar endpoint, Weil form and multiplicity reconstruction — DET-09/11/16, STEP6-01–03.**
`work/independent_det11.md` checks the exact resolvent and Mellin normalization. `work/step6_weil_bridge.md` contains the two-indicator Weil calculation, corrected explicit formula and global one-sided Landau argument; `work/step6_source_manifest.json` identifies the Ramaré corrigendum. `work/arithmetic_kernel_sources.md` and `work/arithmetic_kernel_independent.md` document arithmetic reconstruction and the distinction between atom masses and ordinary spectral multiplicities. Final sections are `work/paper_endpoint.tex`, `work/paper_resolvent_bridge.tex`, `work/paper_weil_bridge.tex` and `work/paper_arithmetic_kernel.tex`.

**Rational weighted-character endpoint — DET-18.**
`work/weighted_endpoint_determinant.md`, `work/weighted_endpoint_independent.md` and `work/weighted_endpoint_source_manifest.json` record the actual family, integer multiplication, central multiplicity, exact Mellin corrections and integrality criterion. Final proof: `work/paper_weighted_endpoint.tex`.

**Natural boost obstruction and the remaining direct-sign question — DET-19.**
`work/bessel_boost_obstruction.md` and `work/bessel_boost_independent.md` document the specific covariance obstruction; the final proof is `work/paper_bessel_boost.tex`. `work/main_gate_challenge.md` explains why that obstruction leaves the stated scalar certificate route open. It does not establish universal absence of other correspondences.

## 3. Historical matching, Masullo, programmes and archive

**Historical step 1/4/full 7 matching.** `work/step1_adaptive.md`, `work/step1_deeper.md`, `work/step4_adaptive.md` and `work/external_history_search.md` preserve the actual candidate searches and their limits. Chronology evidence is in `work/step1_archive_metadata.json` and `work/step1_mirror_commit_metadata.json`. `work/step7_deeper.md` proves the interlacing selector and period-functional consequences; its finite pattern check is `work/check_step7_threshold.py` with `work/check_step7_threshold_results.json`. These results do not identify every historical phrase with a unique Lean declaration. The final scope is `work/paper_end.tex` and the root question register.

**Masullo statement comparison and actual quotient.** `work/masullo_trace.md` identifies the different draft trace statements and test restrictions. `work/masullo_bridge.md` and `work/masullo_bridge_independent.md` address compact tests, heat operators and the quotient metric. Their earlier heat trace-norm gate is superseded by `work/masullo_traceideal_gate.md`: MAS-10 constructs the ordinary determinant using the Green operator. Final sections are `work/paper_masullo.tex`, `work/paper_masullo_green.tex` and `work/paper_masullo_bridge.tex`.

**Character extension and metric obstruction — MAS-11/12.** `work/masullo_character_bridge.md`, `work/masullo_characters_independent.md` and `work/masullo_character_metric.md` treat completed characters, central Riesz blocks, partner/parity distinctions and selfadjoint-similarity obstruction. Final proofs: `work/paper_masullo_characters.tex` and `work/paper_masullo_character_metric.tex`. Dependence remains on the specified draft spectral claim; these are not certifications of the entire draft.

**RH programmes, finite fields and archive repairs.** Use `work/rh_programmes.md`, `work/archive_audit.md`, `work/paper_programmes.tex` and `work/paper_archive.tex`. The root transcription table is the authoritative repair list. Source excerpts and earlier renderings support exact locators but do not replace the missing original manuscript images.

## 4. Source provenance and its limits

- `work/input_manifest.tsv` lists the supplied input paths, byte sizes and SHA256 hashes. Its `source/` paths refer to the original extracted attachments, not a promise that every supplied input is duplicated inside the final ZIP.
- The external Lean material came from the public GitHub release mirror `CocoSgt/riemann-hypothesis-lean`, release `v2026-11-20`. `work/checkpoint_scope.md` records the archive URL, size and SHA256. The mirror's Main/Statements files were compared byte for byte with the supplied entry files. `work/determinant_retrieval_manifest.tsv` records separately retrieved source hashes and their agreement with the mirror.
- This establishes the recorded byte comparisons, **not independent authentication of the author's original multipart archive**. No Lean build, complete dependency audit or formal mathematical certification was performed. The prompt's stipulated Alpöge RH/Dirichlet-GRH convention is retained.
- Topic-specific manifests above preserve additional source reads and retrieval details. Large reproducible external caches and the Lean archive are distinct from the research documentation. The paper's bibliography and exact statement/file locators identify what was used.
- The Grothendieck material supplied for this run consists of transcriptions. Mathematical repair and paleographic attribution remain separate; Masullo-dependent conclusions retain their particular conditional hypotheses.

## 5. How the check evidence is organized

`CHECK_EVENTS.tsv` is the authoritative merged register. Its `event_source` column leads to the preserved `work/*events.tsv` stream. Filter by finding ID, then read the event's actual type and outcome: a source reading, numerical computation, whole-proof reading and independent re-proof are not interchangeable.

`work/root_events.tsv`, `work/root_extension_events.tsv` and `work/root_late_events.tsv` hold root source/proof checks; `work/root_release_events.tsv` separately records final layout/structure/assembly checks; the late stream includes complete DET-18/19 readings. Topic streams accompany the notes above. The `work/integrated_*events.tsv` streams record checks of assembled proof sections. `work/delivery_consistency_audit.md` and `work/delivery_consistency_audit_events.tsv` record register/scope synchronization, including resolved intermediate issues; they are not a replacement for mathematical proof checks.

**Overwritten intermediate file:** `work/root_independent_events.tsv` was affected by an early filename collision and is deliberately excluded from the final merge. The authoritative restored streams are `work/root_independent_det_events.tsv` and `work/root_independent_mas_events.tsv`; the latter records the restoration as `MAS-EVENT-RESTORE`. Restoration records an earlier check, not a second check. `work/merge_check_events.py` implements that exclusion and validates event structure; it does not verify mathematical truth.

## 6. Final build 23 versus historical snapshots

The final visual-review set is **build 23**, the **81-page** paper: `work/latex_build_23.log`, `work/pdf_qa_build23/page_01.png` through `page_81.png`, and seven `contact_*.png` sheets covering every page. `work/render_final_qa.py` produces those renders. The release reviewer completed visual inspection of all 81 pages; `work/pdf_qa_build23.md` records the actual scope, file hashes and benign underfull paragraph. This index does not claim a second visual review. Layout review is distinct from proof verification.

`work/pdf_qa_build16.md` describes an earlier **43-page** build. Earlier logs and the directories `work/pdf_qa/`, `work/pdf_qa_current/` and `work/pdf_qa_final/` are development history; the word “final” in an older directory name does not identify the release review. Use the explicit **build23** set.

`work/assemble_paper.py` records the fragment order used to generate the standalone TeX. The root TeX compiles directly as described in `README.md`. The assembly and event-merge scripts use `deliverables/` when that directory exists and otherwise use the archive root, so they support both the original workspace and the extracted release layout.

Checkpoint 01, 02 and 03 are earlier dated recovery snapshots, not alternative final releases. Their actual persistence records are in `LEDGER.md`, with the third receipt also in `work/checkpoint03_receipt.json`; `work/make_checkpoint.py` and `work/checkpoint_scope.md` document packaging/recovery. Earlier checkpoint ZIPs are not nested in the final package. Consult the latest root ledger/status for the session's final stopping description, rather than treating an older “ongoing” note or this index as a movement review.
