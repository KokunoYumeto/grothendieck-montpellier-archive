# SA25 dossier — part 1

**Start with `SA25_dossier.md`.** It explains the manuscript's two working sequences, the checked claims and failures, the literature, the unresolved ink questions, and the final counts.

This ZIP contains the completed consolidation of the 374 indexed entries of package MPL_105, cote 105. The scope is part 1 only. The fifteen-folder topic inventory is accounted for in `SA25_folder_coverage.tsv`; fourteen folders' mathematical texts belong to other parts and are not supplied here.

## Main registers

| File | Purpose |
|---|---|
| `SA25_entries.tsv` | One read verdict for each stable source entry |
| `SA25_items.json` | Consolidated objects, statements, questions and readings, with source evidence |
| `SA25_claims.json` |82 claim records: source status, reconstruction, computation, searched fate and present qualification |
| `SA25_problems.json` |30 merged authorial problems and their qualified state of the art |
| `SA25_readings.tsv` |64 mathematically motivated alarms; every ink reading remains undecided |
| `SA25_links.tsv` | All406 link and lead rows, with endpoint evidence |
| `SA25_project_links.tsv` | The382 project/provenance leads kept separate from verified mathematical comparisons |
| `SA25_project_link_evidence.json` | Full supplied contextual wording retained where recorded separately |
| `SA25_directions.md` | Eight bounded future tasks, ranked by interest and one-run feasibility |
| `SA25_references.bib` |39 bibliographic keys; opened sources and unopened historical leads explicitly distinguished |
| `SA25_refinements.json` | Ten precise repairs or restricted statements associated with the failed unrestricted proposals |
| `SA25_search_coverage.tsv` | Each claim/problem connected to its actual searches, opened sources and exact locators |
| `CHECK_EVENTS.tsv` |553 source, proof, computation, background-use and refutation events |

Reference names such as `Cisinski2006` are bibliography keys, not unlinked appeals to memory. Exact theorem/paragraph locators are in the claim/problem/search records. `verified` in the bibliography means an actual URL or DOI was opened; it does not mean every theorem in that work was independently reproved. The event registry specifies the actual scope.

## Evidence and programs

`work/a`, `work/b`, and `work/c` preserve the section readers' final source judgments, reading logs, proofs, searched-result records and computation programs. The coordinating reader's independent arguments and complete reading log are in `work/root_proof_checks.md` and `work/root_reading_log.md`. `work/b/integrated_audit.md` records the additional independent audit of the combined narrative.

The final data use canonical item and problem IDs. Explicit aliases and reasons for consolidation are in `work/item_aliases.json`, `work/merge_decisions.json`, `work/problem_aliases.json`, and `work/problem_merge_decisions.json`. Original component IDs inside provenance records remain traceable through those aliases. `work/claim_reconciliation.json` explains repeated arguments without conflating changes of hypotheses or source status.

The scripts in `code/` rebuild the final tables from those final read-authored records. `code/build_all.py` runs the final assembly and structural validation. It does not extract the archive again, redo verdicts by keywords, or replay web searches. The historical section-serialization scripts document their actual uses; final section JSON/TSV files also incorporate the explicitly recorded later reader revisions.

The finite certificates and their outputs live beside the relevant section proofs. They check only their stated finite arithmetic, graph, permutation, cardinality or set-lifting examples. Their limitations are explicit. The unbounded mathematical arguments are in the proof files.

`outputs/validate_bundle.json` records the final structural checks. `BUNDLE_MANIFEST.json` lists the files actually inside this ZIP with hashes. The supplied source attachments are intentionally omitted; their hashes are in `source_manifest.json`. Search responses are retained as requests, URLs, reference identifiers, exact locators and concise findings, without bulk external prose. Earlier checkpoint archives are not nested inside this final archive.

## Limits that affect interpretation

The images were unavailable by design, so no diplomatic reading was changed. The private project registers and companions named by the earlier notes were not supplied or retrieved; their external claims remain unchecked leads. The 17 public-work passage links and 4 internal cote 105 passage links have both mathematical endpoints checked. Three cross-part folder leads have only their source passage and target catalogue metadata available. These distinctions are carried in every relevant record and are not concealed by the completion counts.

All physical line locators refer to the supplied 1,895-line LaTeX file. The source's scan labels, original page numbering, catalogue page count and printer dates are distinct. An undated manuscript has not been given a composition date from reused 1982 paper.
