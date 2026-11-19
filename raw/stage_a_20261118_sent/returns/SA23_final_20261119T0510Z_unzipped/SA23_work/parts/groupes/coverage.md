# Coverage and completion — Groupes part

**Scope:** all supplied transcriptions and Codex companion notes for cotes 161-1 and 161-2. The archive catalogue lists 19 leaves for 161-1 [173] and 111 leaves for 161-2; neither is dated in the supplied topic inventory. The actual assignment contains eight transcription files, not seven. There are no indexed Pro entries in this part, so `entries.tsv` deliberately has its header and no verdict rows. The 27 additional archival subject items have empty `sources` arrays.

## Full source reading

| File stem | Transcription physical lines | Companion-note physical lines | Completion |
|---|---:|---:|---|
| K161-1-01 | 727 | 24 | Entire text and note read |
| K161-2-01 | 534 | 29 | Entire text and note read |
| K161-2-02 | 808 | 21 | Entire text and note read |
| K161-2-03 | 860 | 22 | Entire text and note read |
| K161-2-04 | 538 | 26 | Entire text and note read |
| K161-2-05 | 340 | 25 | Entire text and note read |
| K161-2-06 | 473 | 25 | Entire text and note read |
| K161-2-07 | 726 | 47 | Entire text and note read |

Total: **5,006 transcription lines and 219 companion-note lines**. `read_logs/reads.jsonl` records source hashes and complete intervals, and `read_coverage.json` verifies their union. The eight `analysis_*.md` ledgers preserve the manual mathematical assessments made during reading. The end of file 06 was read again in short blocks after a combined tool output was truncated. Quotations were then checked against the actual source lines, with the choices recorded in `quotation_audit.json`. No scan, no `second_pass` file, and no unprovided leaf was used.

## Completed stages

1. **Source items:** 27 additional subject items, SA23-901–927; no new Stage 1 indexed verdicts. Each has a literal excerpt and source coordinates. These source items supplement the already completed indexed core. Root integration may merge genuinely repeated subject occurrences with other owners while preserving this owner witness.

2. **Claims:** 115 claims, C-SA23-groupes-001–115, each with a manually assigned page status, precise modern statement, literal source excerpt, reconstruction boundary, searched fate, exact references, confidence, and a recorded check event. The 42 search records map to every claim. `claim_search_map.json` makes that mapping explicit. Every computation is either an executed symbolic/finite check or a written general proof or scope audit; the index is `computations/proof_certificates.md`.

3. **Questions:** 61 authorial problem records, including actual live questions, canceled doubts, explicit deferred steps, and unfinished programmes. The final origin audit moved eleven bare assertions or correction histories out of Stage3 and narrowed seven mixed records to their real author cues. Thirteen editorial tasks retain those checks and two separated portions without labeling them author questions. Every retained occurrence preserves its drafting status. Individual development judgments distinguish settled commentary, bounded residual mathematics, and scan-first identification. `flag_coverage.md` lists every problem and all recorded source occurrences; `problem_origin_audit.json` and `problem_editorial_redirects.json` make the distinction inspectable.

4. **Reading alarms:** 59 records. Mathematical evidence raises an alarm; no uncertainty or cancellation was settled by looking at ink. Literal quotation fields retain `deleted`, `inserted`, and `unsure` markup where present.

5. **Links:** 10 verified links: seven archival-folder links and three exact published-work links. Both archival endpoints were read. The links to the self-braiding, graded-orientation, and Barsotti–Tate passages keep distinct questions distinct. The companion Codex notes provide no prior-project context packet, so no link to La Longue Marche, Les Dérivateurs, S6, or a named earlier research run is invented. `project_links.tsv` is empty apart from its schema.

6. **Directions:** the ranked, bounded tasks in `directions.md` and `directions.json` cite actual item, claim, and problem IDs, and give numerical interest and one-run progress scores, known results, residual issues, and the first concrete step. No direction was developed as a new research project here.

## Counts and interpretation

| Claim class | Count |
|---|---:|
| A | 14 |
| B | 51 |
| C | 48 |
| F | 2 |

Class C includes a developed restricted theorem whose hypotheses do not establish the unrestricted source wording, a refuted wording with its precise repair, and a remaining formulation gap. It does not mean that every such record is a currently open problem. The two F records are the unidentified comparison endpoint (017) and detached formulas (111). Searches were completed for both; absence of a theorem matching undefined notation is recorded as an identification limit, not as evidence of novelty. No undated sheet is assigned priority from its catalogue position.

| Page-status category | Count |
|---|---:|
| proved there | 8 |
| open on the pages | 31 |
| false as stated | 15 |
| proof sketched | 35 |
| stated without proof | 16 |
| corrected by himself later | 10 |

There are 203 check-event rows, 33 verified bibliography records, 42 search records, and 19 executed program sections covering 23 claims. Reference verification means the identified URL or DOI and stated passage were opened to the degree recorded; a metadata-only item is not used as a proof. The Bird thesis download failures, blocked zbMATH records, and broad but unmatched searches remain visible in the search log. Opened external PDFs and full texts are stored under `external/` as working evidence and are excluded from the final ZIP by root integration.

## Genuine limits retained

The categories and functor in the last filtered-F-crystal comparison are not specified well enough to identify an equivalence. The detached cohomology/ring-topology formulas do not determine a theorem. The mixed-doctrine construction leaves its successor operation and several size/preservation hypotheses open. The internal connected-component assignment, formal smoothness/étaleness quantifiers, and final stack of topoi require a chosen precise formulation. These are the mathematical and textual outcomes of completed reading and searches; they are not unperformed source work.

Root owns final integration, cross-owner duplicate decisions, the combined dossier, checkpoints, and the single final ZIP. This part makes no Library mutation.

## Publication authorship audit

All fourteen class-A records have an exact authorship audit in `authorship_audit.json`. Their SGA 4 counterpart is in Exposé IV, Topos, whose original printed p.299 explicitly names A. Grothendieck and J. L. Verdier as joint authors. This is not an inference from the volume editors. The separate credits to Giraud and Artin on p.300 and to J.-E. Roos in Exercise7.6(d), p.415, remain explicit; class A does not assert sole discovery or manuscript priority. No mathematical statement or class count changed in this bounded audit.
