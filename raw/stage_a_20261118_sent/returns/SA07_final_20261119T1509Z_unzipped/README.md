# SA07 dossier — part 3

**Assessment date: 19 November 2026.** Start with `SA07_dossier.md`. The complete scholarly judgments are in the individual registers; the overview gives their relationships and the consequential corrections.

## Contents

| File | Purpose |
|---|---|
| `SA07_dossier.md` | English synthesis, source boundaries and exact final counts. |
| `SA07_entries.tsv` | One verdict for each of the 339 supplied indexed entries. |
| `SA07_items.json` | Canonical items, all source-entry IDs, quotations, locations and textual assessments. |
| `SA07_claims.json` | Claim statements, page status, computation checks, searched fate, historical class and dated present status. |
| `SA07_problems.json` | Author questions/deferred steps and separately labelled verification questions, with exact state-of-art limits. |
| `SA07_readings.tsv` | Mathematical reading alarms and supplied second-pass settlements; no new scan adjudication. |
| `SA07_links.tsv` | Complete link audit, including the explicit availability/status of both endpoints. |
| `SA07_project_links.tsv` | Separate table of earlier-project leads. Their reported statuses are not adopted as results. |
| `SA07_archive_published_links.tsv` | Archive and publication subset of the link audit. |
| `SA07_directions.md` | Eighteen ranked tasks, each tied to item, claim and problem IDs. |
| `SA07_references.bib` | Opened references and explicitly unverified backward/discovery leads. |
| `SA07_reference_audit.json` | Full original reference records, exact passage or metadata-only scopes, and chronology. |
| `SA07_claim_search_coverage.tsv` | Every original claim mapped to actual query/open batches, with canonical aliases. |
| `SA07_literature_search.tsv` | All reader search-ledger rows, retained as structured JSON within TSV cells. |
| `CHECK_EVENTS.tsv` | What was actually checked, by whom, using which kind of check. |
| `progress.log`, `checkpoints.tsv` | UTC work log and scheduled checkpoint record. |
| `code/`, `root_records/`, `provenance/agents/`, `evidence/` | Authored programs, original reader judgments, proof audits, outputs, retrieval metadata and validation. |

The three alias tables cover retired item IDs, claim/problem IDs, and duplicate reference keys. An alias is not a missing record. Merged items and claims retain their original assessments in `source_assessments` or `source_records`; original keys in those records resolve through the reference alias table. Canonical identifiers are kept stable and need not be consecutive.

## Reading the evidence accurately

`status_on_pages` describes the manuscript. `class` describes the searched historical fate of the precise formulation, including a corrected or restricted version when expressly stated. `present_status` is dated. A class B record can therefore contain a false literal formula together with an established corrected theorem; neither the page status nor the correction is hidden.

Class A is qualified when the exact paragraph appears in a collective publication or an exposition by another named contributor. No individual authorship or priority is inferred just from a reused sheet. Class D means that the logged searches did not identify an exact development; it is not a universal negative. Class F means that the surviving statement or antecedent is insufficiently identifiable.

The problem register retains its complete `problem_origin` description. Its shorter reporting group is a count label, not a claim that every entry was an explicit open question on the page or remains open today. Four supplemental claim records are marked as this run's refinements; CL-SA07-222 is explicitly a question from a later published discussion. Codex-only claims can legitimately have an empty `items` array because the user assigned no indexed-note verdict rows to Codex leads.

A BibTeX `note={verified}` certifies that the named reference was opened. It does **not** mean that the entire work was read or its proof independently checked. The `annote` and reference-audit records give the actual theorem, passage, abstract or metadata scope. Several original texts remain unverified; adjacent or later exact results are identified separately. An unavailable link endpoint remains labelled unavailable even when a neighboring theorem is known.

All quotations from the supplied transcriptions are diplomatic witnesses. The supplied second pass is authoritative for its changed readings. This run did not have the archive scans, did not alter any transcription and did not replace uncertain ink with a mathematically convenient expression.

## Proofs and exact calculations

The main proof audits are:

- `evidence/root_computations.md`: supplementary Codex categories, quaternion orders, finite fields, analysis, ODEs, lattice constructions and homotopy conventions.
- `provenance/agents/p15/computations.md`: realization/period algebra, the countable-tower obstruction, Lie and local-group material, Haar normalization and formal duality.
- `provenance/agents/p16/computations.md`: Lefschetz strings and counterexamples, differents and étale hypotheses, Fourier/Chern/Todd formulas, finite group schemes and cycle representatives.
- `provenance/agents/p18/computations.md`: cycle and trace normalization, real forms, adelic obstructions, cocycle words, root systems, Haar and Dedekind proofs.

The finite programs use exact integer, rational and symbolic arithmetic. Their assertions prove the finite identities they test. The prose gives the general arguments and states when a finite example is only an illustration or a counterexample. External theorem reading is not counted as an independent re-proof.

## Replaying the computations and integration

For a replay, put the contents of this final archive in a directory called `deliverable/` inside a fresh workspace. Restore the three reader folders from `deliverable/provenance/agents/` to `agents/` beside it. Put the original supplied input ZIP at `upload/SA07_Thorie_des_motifs_part3.zip` and extract its 29 members once to `work/`. The inputs are intentionally not embedded in this archive.

Python 3 and SymPy are required. The exact versions used are in `evidence/computation_replay/report.json`. From that workspace, run:

```bash
python3 deliverable/code/inventory_inputs.py
python3 deliverable/code/recheck_computations.py
python3 deliverable/code/integrate_stage1.py
python3 deliverable/code/integrate_core.py
python3 deliverable/code/assemble_audit.py
python3 deliverable/code/build_dossier.py
python3 deliverable/code/validate_final.py
```

The first command verifies that the extracted source bytes still match the original ZIP. The second replays the five independent computation programs and saves their outputs. The integration programs serialize and check manually authored decisions; they do not infer note verdicts or mathematical truth from headings or keywords.

Reader drafting programs are preserved as run documentation. Some contain the original scratch path and expect source-entry indexes regenerated from the original inputs. They need a path adjustment before replay in a new location. They are not needed to rerun the independent calculations or integrate the preserved final reader records. Live literature searches cannot be reproduced offline; exact requests, source URLs/ref metadata, source hashes and the dated judgments are retained for reinspection.

## What is intentionally outside the archive

The supplied attachments, previous checkpoint ZIPs, downloaded third-party books/articles and full retrieved source bodies are not copied into the final archive. The source inventory and retrieval metadata identify them. The corpus does not include the other two parts of SA07 or the original external LM/WG/Hua project records. Their absence is disclosed in the dossier and links table; no claim is made to have read those missing endpoints.

`SNAPSHOT_MANIFEST.json`, written when the ZIP is created, lists every archived member with its size and SHA-256 hash. `evidence/final_validation.json` reports the consistency and coverage checks on the assembled deliverable.
