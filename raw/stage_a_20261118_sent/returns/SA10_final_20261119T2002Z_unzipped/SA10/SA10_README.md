# SA10 — Espaces stratifiés, part 1

Begin with `SA10_dossier.md`. The authoritative consolidated records are the nine `SA10_*` files requested in the task, together with `CHECK_EVENTS.tsv` and `progress.log`.

| File | Purpose |
|---|---|
| `SA10_entries.tsv` | One manually researched verdict for each of the 537 indexed entries. |
| `SA10_items.json` | Consolidated objects, questions, readings and documentary items. |
| `SA10_claims.json` | Exact claim formulations, manuscript status, computations and searched fate in the literature. |
| `SA10_claim_status_index.tsv` | Manual reporting categories for the full, qualified page-status statements. |
| `SA10_problems.json` | Authorial open steps, with supported modern formulations and source limits. |
| `SA10_readings.tsv` | Mathematical reading alarms, including explicitly labelled closures from the supplied second pass. |
| `SA10_reading_status.tsv` | Every reading row classified as active, closed or an optional lexical check. |
| `SA10_links.tsv` | Archive, published-work and attributed project links. |
| `SA10_project_leads.tsv` | The project-lead subset, kept separate for convenient use without promoting its reported statuses. |
| `SA10_directions.md` | Ranked future tasks, each tied to items, claims and problems. |
| `SA10_references.bib` | Checked bibliographical records; annotations specify the exact level of access. |
| `SA10_aliases.json` | Explicit editorial reconciliation of reviewer identifiers. |
| `CHECK_EVENTS.tsv` | Events distinguished by the kind of checking actually performed. |

## Evidence and reproducibility

`parts/p1` through `parts/p5` contain the individual researchers' manually authored tables, proofs, source audits, read logs, programs and outputs. These are work records; the consolidated root-level tables govern the final verdict and identifier. A former identifier in a proof or local table is resolved through `SA10_aliases.json`. No source entry was classified by headings or keyword matching.

The package assignments are p1 = 150/001–043; p2 = 150/044–084; p3 = 150/085–099 plus 151/001–031; p4 = 151/032–075; p5 = 152 plus 120. The cross-reviews include the p3 audit of p5's mathematical models and pushouts and the p1 audit of p4's counterexamples.

`code/` holds corpus navigation, bibliography inventory, consolidation, packaging and structural validation. `outputs/` contains their recorded output. Exact finite certificates supplement the written proofs; they are not represented as universal proofs. Bibliography annotations and search logs record the inspected theorem locators, unsuccessful access attempts and the limits of matching a later theorem to an incompletely specified manuscript statement.

The attachments and earlier checkpoint archives are not embedded in this archive. The source inventory identifies the attached files and their hashes. Full externally retrieved papers and public transcription caches are also not redistributed: the source-cache and web-locator ledgers preserve their identifiers, URLs and hashes, while the authored audits preserve the conclusions and exact passages inspected. This excludes source reproductions, not the mathematical proofs or computational output of this run.

## Locator conventions

Unless explicitly marked as a page-local line in a supplied second-pass log, a line number is the physical line in the combined supplied transcription file, counted from one. Scans use the cote and the `scanpage` number; covers count as scans. External public French transcription witnesses use an archive footer one less than the official PDF scan. Every external quotation or comparison identifies that witness rather than claiming a new reading of ink.

The present status is assessed as of **19 November 2026**. A verified reference means the link or source was opened at the scope stated in its annotation. It does not mean every result in a book was re-proved. A current source-access failure, an unidentified exact claim and evidence that a statement is mathematically false are three different outcomes. The `MPL150Early` bibliography entry identifies an actually read supplied local witness through a relative source path; it is not a claim to have newly inspected the original scans.

The final totals are 537 entries, 400 items, 276 claim records, 73 problems and 12 directions. The reading ledger contains 108 active records, 35 closed provenance records and one optional lexical check. The 49 project leads retain the explicit source-access exception in dossier §10; their external register statuses were not promoted to verified results.

## Resuming in another workspace

Unpack this archive once, and unpack the user's original outer attachment once beside the resulting `SA10` directory as `source/`, retaining its already expanded `SA10_notes` and `SA10_texts` folders. The local source inventory is sufficient to check identity. The mathematical certificates and manually authored records are already present. Run `python SA10/code/relocate_workspace.py` from the new workspace to adjust historical absolute paths in the copied programs before replaying them. It does not alter the user's source files or any mathematical judgment.

`progress.log` and the local part logs record work as it occurred. Checkpoint 01 was saved after a context-handoff delay relative to its first scheduled time; the actual time is recorded without backdating. Checkpoints are independent full snapshots of the then-current work, and are not inputs required to use this final dossier.
