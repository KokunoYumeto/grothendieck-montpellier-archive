# SA08 dossier archive

This archive is the completed consolidation of the supplied part of the Montpellier topic **Complexe de De Rham**, cote 136. The assessment date is 19 November 2026. The original attachments and external published full-text caches are intentionally not copied into it.

## Main files

| File | Purpose |
|---|---|
|`SA08_dossier.md`|English overview, source strata, mathematical findings, present status and counts|
|`SA08_entries.tsv`|Exactly 437 indexed-note verdicts, one per original NOTES_INDEX row|
|`SA08_items.json`|Consolidated note items and explicitly marked direct-transcription leads|
|`SA08_claims.json`|Claim statements, page status, computations, searched fates and bibliography keys|
|`SA08_problems.json`|Historical open steps, including later-resolved questions and explicit scope limits|
|`SA08_readings.tsv`|Mathematical reasons to inspect the ink; no diplomatic reading was changed|
|`SA08_links.tsv`|Checked links between supplied passages or to opened published passages|
|`SA08_project_links.tsv`|Separate unverified external-project provenance leads, with local note attributions|
|`SA08_directions.md`|Twelve ranked task specifications; directions are not developed here|
|`SA08_references.bib`|Canonical bibliography with verified/unverified status and narrower access annotations|
|`CHECK_EVENTS.tsv`|Proof, computation, source-reading, background and refutation events with checker identity|
|`progress.log`|UTC start, stages, checkpoints and completion|

## Audit supplements

`SA08_entry_item_expansion.tsv` records semantic facets of large composite indexed entries. It does not create extra verdict rows. `SA08_id_aliases.tsv` resolves merged packet IDs; the one compound problem is explicitly distributed to its separately scoped canonical questions. Surviving IDs are not renumbered, so numerical gaps are intentional.

`SA08_claim_audit.json` retains attribution, proof scope and search-family metadata from the original authored records. `SA08_claim_searches.tsv` maps every claim occurrence to its recorded fate search. `SA08_project_provenance.json` preserves the differently structured project-context tables. `SA08_statistics.json` and `SA08_validation.json` contain final counts and structural validation results.

There are two sorts of item without indexed sources: direct Codex leads/metadata and one Pro proposition found by full-text reading but not independently headed in the notes. They use `sources: []`, explain their origin, and create no NOTES_INDEX verdict row. All other `sources` values are original stable entry IDs.

## Locators and statement conventions

Line numbers are **one-based lines in the supplied original transcription files**, not PDF page numbers or the prefixed line numbers of the temporary reading copies. `pro/` and `codex/` paths are relative to the restored texts attachment; `notes/pro/` explicitly denotes a note-file locator. The original authored packet records retain any older A/B/P/Q/D/E abbreviations. In a few composite or metadata records, a prose locator identifies the scope instead of pretending to supply a numeric line range.

`his_words` and `his_statement` contain brief source selections; exact quotation audits retain the selected line ranges. Uncertain, inserted or cancelled source wording is preserved where included. A statement labelled as a modern reconstruction is not attributed verbatim to Grothendieck. The three refined reconstruction claim records remain explicit targets for checks and counterexamples.

The A–F class is a literature-fate class. It is not the truth value of the transcribed formula. Page status and the actual check explain false, corrected, withdrawn and hypothesis-dependent assertions. Class A donor matches refer to the earlier draft-to-own-SGA-publication relation; the 1972 publication does not become a later development of the 1975–1976 live PD work. Class D records a bounded nonmatch, not a novelty theorem. Reference `note={verified}` means an actual URL or DOI was opened; an annotation can restrict that to metadata access.

## Rechecking the mathematics

The four principal proof memoranda are:

- `work/early/proofs.md`
- `work/middle/mathematical_checks.md`
- `work/late/proofs.md`
- `work/root/codex_proof_checks.md`

Other source, quotation and peer-review audits are retained beside them. All substantive calculation programs and their outputs are under `programs/` and `logs/`; mathematical finite output is accompanied by its general argument or explicitly limited test scope. Preliminary failed runs are retained where they document an error subsequently repaired. They are not the final mathematical conclusions.

The consolidation pipeline is `root_complete.py`, `root_codex_items.py`, `integrate_dossier.py`, `finish_prose.py`, and `validate_dossier.py`, with the separate packet and bibliography builders. To restore, extract this archive into a directory named `SA08_work`, put the original `SA08_notes.zip` and `SA08_texts.zip` in its adjacent `upload/` directory, and run `programs/setup.py`. Re-running the builders requires those restored sources and preserving any later audited overrides. The individual final records under `work/` are the authoritative saved judgments; the compiler's explicit merge lists are bookkeeping, not automated reading verdicts.

`research/retrieval_audit.json` preserves searches, opened-source URLs, retrieval identifiers and hashes without redistributing external copyrighted texts. Download/OCR programs can restore source caches when a particular primary passage needs reinspection. No original attachment or earlier checkpoint ZIP is embedded in the final archive.

## Integrity

`FINAL_MANIFEST.json` lists archive members and SHA-256 hashes. The final validation checks all 437 verdict IDs, required fields, canonical links, reference keys, check-event coverage, claim-search coverage, numeric source-locator bounds and direction anchors. It is a structural/editorial validation; the independently authored mathematical checks are documented in the ledger and proof memoranda.
