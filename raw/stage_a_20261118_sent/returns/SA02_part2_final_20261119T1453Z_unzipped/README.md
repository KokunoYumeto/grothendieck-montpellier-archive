# SA02 — Part 2 dossier

**Assessment date: 19 November 2026.** Start with **SA02_dossier.md** for the source-ordered overview, principal findings, limitations, and final counts. **SA02_directions.md** contains sixteen ranked follow-up tasks; they are proposals, not additional research developed here.

## Main registers

| File | Purpose |
|---|---|
| SA02_entries.tsv | Exactly one verdict for each of the 389 supplied indexed entries |
| SA02_items.json | 336 consolidated items and their passage-level checks |
| SA02_claims.json | 274 assertion records with source status, computations, searched fate, references, and attribution |
| SA02_problems.json | 101 question records, including resolved local steps and ten nonmathematical essay questions |
| SA02_readings.tsv | 197 mathematical or documentary alarms for a future scan review; no ink decision made here |
| SA02_links.tsv | 158 archive/publication links checked at both endpoints |
| SA02_project_leads.tsv | Fifteen separately labelled external-project leads whose context packets were unavailable |
| SA02_references.bib | 88 references, each with a scoped access/verification note |
| CHECK_EVENTS.tsv | 1,084 events distinguishing textual checks, proof work, computations, and background use |

## Audit and supporting work

SA02_aliases.tsv preserves retired identifiers after true mergers. Source occurrences and their different proof statuses remain in the canonical records. SA02_claim_fate_audit.tsv maps every canonical claim to the actual search logs. SA02_source_inventory.tsv records file hashes and supplied witnesses; SA02_scope.tsv accounts for all thirty catalogue cotes, with the other parts clearly outside this run’s substantive scope.

The **evidence/** directory contains the root proofs, reading and search notes, and explicit consolidation decisions. The **parts/** directories retain the three readers’ complete source assessments, proofs, literature audits, and validation reports. The **programs/** directories and their **outputs/** retain the mathematical certificates and the serializers used to assemble the manually assessed records. Final structural validation is recorded in **outputs/final_validation.json** and **outputs/final_validation.txt**: all 49 checks passed, with no warnings.

The source attachment is deliberately not duplicated. Source paths refer to the supplied archive extracted into a sibling **source/** directory, with the dossier work in **SA02_work/**. Some packet programs retain the original execution path, `/workspace/scratch/95cd10054c54`; adjust that path if reproducing the work elsewhere. Mathematical Python programs use their documented imports, including SymPy where applicable. The existing outputs are the evidence from this run, not promises that every historical network download remains available.

Full external publications and raw web retrieval excerpts are not redistributed. Their locations, concise search results, exact inspected sections, failed access attempts, and verification limits remain documented. The packaging exclusions and the SHA-256 digest of every included file are in **ARCHIVE_MANIFEST.json**. Earlier checkpoint ZIPs and the source attachment are not nested in this archive.

The current transcriptions have not been changed. An uncertain sign or hypothesis remains an ink question even when the literal formula has a counterexample. An inaccessible external-project endpoint remains a lead, and an undated mathematical sheet does not establish priority.
