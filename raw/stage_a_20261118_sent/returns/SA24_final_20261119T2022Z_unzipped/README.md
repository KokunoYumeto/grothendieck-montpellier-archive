# SA24: reading the consolidated dossier

This package consolidates the supplied SA24 notes and transcriptions as of **19 November 2026**. Start with **[SA24_dossier.md](SA24_dossier.md)** for the mathematical and historical account. The JSON and TSV registers provide the individual records and their evidence; **[SA24_directions.md](SA24_directions.md)** lists future tasks without developing them here.

## Files and their roles

| File | What it contains |
|---|---|
| `SA24_entries.tsv` | One editorial verdict for each of the 509 original note-index entries, including its final item ID and reason. |
| `SA24_items.json` | Merged note items, brief source quotations, reconstructed formulations, and textual checks. |
| `SA24_claims.json` | Manuscript claims, page-level status, computations, literature fate, present status, confidence and references. |
| `SA24_problems.json` | Questions and unfinished steps, their occurrences, supported formulations and current literature position. |
| `SA24_readings.tsv` | Mathematical alarms for a later scan inspection. These are proposed readings, not ink decisions. |
| `SA24_links.tsv` | Checked connections within the supplied archive and to public/published work. |
| `SA24_project_leads.tsv` | Earlier-run leads to La Longue Marche, Les Dérivateurs and other external projects, kept separate from verified results. |
| `SA24_references.bib` | Bibliography with explicit verified/unverified labels and verification scope. |
| `SA24_search_log.tsv` / `SA24_claim_search_map.tsv` | Recorded searches and openings, their outcomes, and the claim-to-search crosswalk. |
| `CHECK_EVENTS.tsv` | What was actually checked, used, computed, re-proved or refuted; the event type limits the claim of verification. |
| `SA24_refinements.json` | Ten explicitly named scope corrections used by the proof reports/events, linked to final claim IDs. |
| `SA24_id_map.tsv` / `evidence/working_to_final_ids.json` | Translation of working item/claim/problem/reference IDs into final identifiers. |
| `REPRODUCTION.md` / `evidence/code_inventory.json` | Input layout, dependencies, replay instructions, and the complete authored-program inventory. |
| `agents/` | The reader records, proof reports, source audits and merge decisions underlying the final consolidation. These retain working IDs. |
| `code/` / `outputs/` / `evidence/` | Programs, saved calculation/validation outputs, numbered source selections, hashes, access manifests and reading provenance. |
| `progress.log` | UTC progress and checkpoint history. |

The top-level registers are the authoritative consolidated records. Working records in `agents/` preserve the audit trail and can contain earlier IDs, counts or formulations that were subsequently corrected. Follow the ID map and the final register when a working report and the consolidation differ.

## Identifier and locator conventions

- An original note entry is `MPL_134-8_043-087#n`, where n is its position among the note file's third-level headings and agrees with `NOTES_INDEX.tsv`.
- An item ID is `SA24-n`, retained from the smallest source-entry number of its merged item. Gaps in the item-number sequence are expected. Every source entry still has its own verdict row.
- Final claims are `CL-SA24-001` through `CL-SA24-137`; final problems are `MP-SA24-01` through `MP-SA24-41`. Working prefixes such as `CCORE-`, `CMID-`, `CLA-`, `CROOT-`, `PCORE-`, `PMID-`, `PLA-` and `PROOT-` are resolved by the ID map.
- Refinement IDs beginning `REF-` name this run's explicit repairs or restricted formulations. They are not newly attributed manuscript statements. `REF-LATE-STABLE-1` and `REF-ROOT-054` name the same stabilization correction in two working reports and are cross-referenced accordingly.
- A **cote** is the archive folder identifier. A **scan** is the value of the source `\scanpage{N}` marker. It is not the manuscript's printed or handwritten page number and is not the archive sheet number in a source comment.
- A **line** is a **1-based physical line in the exact named source `.tex` or `.md` file**, including comments and diagram code. It is not a rendered PDF line or a fresh per-page count. `evidence/source_manifest.json` records the 24 source-file hashes needed to reproduce those coordinates.

Bibliographic locators specify the publication's printed page, section, theorem or equation where available. A PDF page index, when used in working evidence, is a separate coordinate and must not be substituted for a printed page number.

## Coverage and its limits

All **509 note-index entries** received an entry-by-entry verdict after the note and its source passage were read. The scope includes the one supplied Pro transcription and all nine supplied Codex transcription files: K134-2-01/02/03, K134-4-01, K134-8-01, and K135-01/02/03/04. This covers the **supplied packet**, not every catalogued page of SA24. `TOPIC.md` explicitly assigns other portions of cotes 134-1, 134-3, 134-5, 134-6 and 134-7 to other parts; it also gives larger catalogue page totals than the files supplied here. These absent portions are not silently treated as read.

The Pro file contains 44 scan blocks numbered 43–87, with scan 60 absent from the supplied transcription. No scan images and no `second_pass/` files were supplied. The source files remain unchanged. Reused song sheets, a seminar programme, covers and calendar artwork were recognized as such rather than turned into mathematical claims. The large vector calendar is documented by its source inspection, not as a proof-bearing calculation.

In `SA24_readings.tsv`, **confidence measures the strength of the mathematical alarm**, not confidence that the proposed alternative matches unseen ink. A high-confidence inconsistency can still have several possible paleographic resolutions. Only inspection of the scans can decide among them.

The original ZIP attachments and their extracted source folders are **not included in this package**. The numbered selections under `outputs/` are reading evidence, not a replacement for the source attachments. Full third-party PDFs, OCR and raw external-text caches are also excluded; their provenance, URLs, hashes where recorded and assessed outcomes remain in the manifests, bibliography and search logs.

“Not on the page” is a bounded textual finding about the supplied passage or packet. It does not say that a result is absent from an external project or from the author's complete archive. The 392 external-project leads retain their earlier-run attribution; inaccessible private target proofs are not promoted to verified results.

## Final counts

The following counts come from `outputs/consolidation_counts.json`.

| Register or classification | Count |
|---|---:|
| Original entries | 509 |
| Merged items | 373 |
| Entry verdicts: kept / corrected / merged | 372 / 7 / 130 |
| Claims | 137 |
| Claim classes A / B / C / D / E / F | 0 / 28 / 31 / 1 / 60 / 17 |
| Problems | 41 |
| Reading alarms | 82 |
| Checked archive/public-work links | 53 |
| External-project leads | 392 |
| Check events | 800 |
| References: verified / unverified | 83 / 3 |
| Search-log rows | 194 |
| Claims without a search crosswalk | 0 |

The claim classes follow the requested scheme: **A**, found in his own later published work; **B**, developed by others into established results; **C**, partly developed, with the residual qualification stated; **D**, not identified as developed within the documented search; **E**, already known before these notes; **F**, not identifiable precisely from the pages. A class or a publication on the same broad subject does not erase the record's explicit hypotheses and qualifications.

The separate page-status counts are: proved there 6; proof sketched 32; stated without proof 50; corrected by himself later 4; false as stated 6; open on the pages 39. They describe the manuscript status and should not be read as the modern literature classification.

## What the evidence establishes

The 800 events are not 800 independent proofs. Reading a theorem statement, checking a bibliographic record, applying a known result, checking a special case, proving a universal identity and constructing a counterexample are distinguished in the event types and outcomes. The four computation programs have saved exact outputs and companion proof reports; finite tests are not presented as general proofs. Structural validation checks coverage, hashes, schemas and links, not mathematical truth.

The 86-reference bibliography contains 83 verified access records and 3 explicit unverified entries: `Conduche1984`, `EilenbergMacLane1947` and `MacLane1963`. Their access failures and alternative checked sources are recorded. “Verified” means the identified reference was opened to the scope stated in its note/annotation; it does not imply that the entire proof was independently checked. Current preprint claims, including the 2026 homotopy-hypothesis claim, retain their stated verification limits. The universal sheaf Picard realization problem is not declared settled merely because an Ext³ obstruction group appears.

Search logs record failures and limitations as well as useful results. Some early middle-reader retrieval batches do not preserve the exact original query string; this is explicitly recorded, and later explicit-query batches supply the claimed searched-fate coverage. No missing query is silently invented.

For proof details begin with `agents/core_report.md`, `agents/middle_proof_checks.md`, `agents/late_proof_checks.md`, `agents/root_proof_checks.md` and `agents/late_stable_picard_followup.md`; use the ID map to connect their working IDs with the final registers.
