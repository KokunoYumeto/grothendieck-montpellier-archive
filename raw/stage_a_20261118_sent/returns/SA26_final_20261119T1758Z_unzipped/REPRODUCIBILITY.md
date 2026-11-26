# SA26 — Reproducibility, data conventions and evidence inventory

## Canonical deliverables

The nine `SA26_*` files named in the task, `CHECK_EVENTS.tsv` and `progress.log` are the canonical deliverables. `SA26_dossier.md` provides the connected exposition and validated counts. `SA26_entries.tsv` has exactly one manually determined verdict for every supplied index row. The item, claim and problem identifiers are stable within this part; gaps reflect the reader partitions, not omissions.

The `agents/` directories preserve each reader's detailed contribution, actual query logs, structured decisions, proof notes, source-read records, serializers, finite certificates and outputs. Their duplication of canonical records is intentional audit documentation. The canonical files are the integrated results. A reader's completion message or progress log is not a substitute for its actual evidence files.

## Source identity and locations

The source package was unpacked once into `sources/` during the run. Its six files are listed with SHA-256 hashes in `evidence/source_manifest.json`. No supplied file was changed. `evidence/source_navigation.json` records every indexed entry's actual notes-line interval and every source scan block's global TeX line interval. Navigation extraction was mechanical and used only to facilitate full reading, never to assign a verdict.

Source attachments are deliberately absent from this ZIP. To rerun source-dependent indexing, metadata checks or the readers' serializers, use the original attachment and the directory layout in the programs, adjusting the task root if needed. Some audit scripts retain the absolute path of the original workspace for documentary accuracy. The numerical and formal certificates listed below have no dependency on the manuscript files.

Line numbers in the canonical item and claim records are **one-based physical lines of the supplied combined TeX file**, except strings explicitly prefixed `notes`. Scans are cote-local `scanpage` numbers and begin at2. A manuscript sheet/page number, an upper unit number and a printed computer-page label are not interchangeable.

The JSON field names match the requested schemas. Single-cote mathematical records use a scalar `cote`; cross-cote documentary items use a list. Scan fields in single-cote records are numeric lists, while cross-cote documentary items retain qualified range strings. `lines` and problem `occurrences` preserve detailed authored locators, including mixed source-note and TeX references where needed. These are locators, not executable instructions. The one transcription-only item, `SA26-125`, intentionally has an empty `sources` list. `his_words: null` means that a contextual report is not a statement by Grothendieck; no quotation was fabricated for it.

Modern mathematical statements normalize typography where needed. Fields attributed to Grothendieck retain exact diplomatic TeX excerpts, with global source-line labels where several excerpts are joined. The transcription remains the witness for cancellation, uncertain lettering and exact layout. An `unsure` alternative is never resolved by the modern formula in another field. The dossier explains the projection convention and distinguishes pullback `p_B^*` from right adjoint `p_B*` in plain-text records.

The final quotation audits are recorded in `agents/a/exact_excerpt_ledger.tsv`, `agents/b/source_excerpt_audit.tsv` and `agents/c/exact_excerpt_ledger.tsv`. The cote106 audit covers all 48 quotation fields: 47 exact nonempty excerpts and one null bibliography item. The cote107 audit covers all 60 quotation fields through 118 exact excerpt fragments. The documentary audit checks the five remaining nonempty quotation fields; its six null context quotations remain null. These audits verify exact source substrings and containment within the stated source locators; canceled passages retain or explicitly identify their outer cancellation scope. Selection was editorial, while substring and locator validation was mechanical. Saved hash baselines for the cote106 and documentary repairs verify that repairing quotation fidelity changed no mathematical statement, verdict, classification or other nonquotation field.

## Independent executable certificates

| Program | Recorded output | What it checks |
|---|---|---|
| `code/independent_computations.py` | `outputs/independent_computations.json` | Exact finite-set counterexamples, separate/joint continuity tests, finite telescoping coefficients, p-adic residues and matching-object illustrations |
| `code/typed_compositions.py` | `outputs/typed_compositions.json` | Source-target typing and localized formal rewrites in three manuscript calculations; two reading alternatives |
| `agents/a/computations.py` | `agents/a/computations_output.jsonl` | Twelve explicitly named finite/formal certificate families for cote106 |
| `agents/b/cotensor_counterexample.py` | `agents/b/cotensor_counterexample_output.json`; root rerun in `outputs/cotensor_counterexample_root_rerun.json` | The ten commutative squares in the two-element idempotent monoid |
| `agents/c/code/audit_metadata.py` | `agents/c/outputs/audit_metadata.json` | Source scan blocks, printed dates, page-label distinctions, doubt-table count and original hash |

Run a certificate with Python3, for example `python3 code/independent_computations.py`, from the unpacked dossier directory. It prints its result to standard output and asserts the stated finite equalities. The programs use ordinary standard-library arithmetic and enumeration. These are not formalizations of all category-theory or model-category axioms. In particular, the finite residues do not by themselves prove the infinite Ext quotient, and counting monoid squares does not by itself prove their relevance to a cotensor. Those arguments are written out in the proof notes.

The source hash and metadata checks require the original attachment. Source serializers are included to show how the manually authored records were written; they do not decide truth from keywords. Failed initial directory/redirection and integration-header attempts are documented in `outputs/integration_attempts.log` and the reader command logs; they were corrected before canonical output was produced.

## Written mathematical checks

`evidence/independent_audit.md` contains the integrating reader's independent proofs of the original-roof universal property, inversion of acyclic cofibrations, comparison through joint-cofibrant roofs, the projection exponential formula, the telescope algebra, the no-alternative-colimit argument, the relative-square criterion and the retraction construction. It also independently checks the new cotensor counterexample.

`agents/a/findings.md` supplies the exact H hypotheses, weak-lifting construction, complete composition/unit comparison and source-status distinctions. `agents/b/mathematical_audit.md` supplies the detailed cote107 arguments. Any additional cross-review in `agents/a/` records a fresh critique of the strongest cote107 conclusions, not a new historical claim. The check-event table identifies the type of check actually performed and its scope.

## Literature and provenance

Every claim is indexed in `evidence/claim_search_coverage.tsv`, which points to the reader's actual search records and states the exact match and remaining boundary. `agents/a/search_log.tsv`, `agents/b/search_log.tsv`, request-only query logs, `agents/c/search_log.tsv` and `evidence/root_search_log.tsv` preserve the searches and source opens. A broad or unsuccessful search is not evidence that a theorem is undeveloped. Metadata-only access is not represented as inspection of the theorem body.

Every bibliography entry has exactly the requested verification note. `verified` means that the cited URL or DOI/source endpoint was opened; `annote` or `addendum` records what was inspected. `unverified` covers the inaccessible Hovey reference and the missing private source groups. Submission, first accessible preprint version, copyright, publication and modern reedition dates are kept distinct. An external publication is not assigned the manuscript's intended hypotheses merely because it concerns similar mathematics.

The separate context tables preserve255 concordance rows,12 numbered NEW_RESULTS entries plusK1–K3, exact reported prover/checker cells, selected status reports and run paths. Their status strings remain attributed. The public-project endpoint table records the actual three recovered Hua findings and the inspected scope of their displayed Lean sources. No Lean kernel execution, Mathlib rebuild or replay of historical review events was performed in this run. Public report access and theorem verification are different events.

Downloaded reference texts, repository source caches, screenshots and raw search-response bodies are excluded from the archive. Their source URLs, relevant locators, request records and hashes remain where available. The code that retrieved public material is included with its metadata output, without redistributing the full source cache.

## Integration validation and packaging

`code/integrate_dossier.py` assembles the three manually adjudicated contributions. It verifies exact entry coverage, schema fields, unique IDs, source-entry membership, item/claim/reference cross-references, existence of actual searched-fate rows for all55 claims, check-event coverage, all15 topic cotes, source immutability, and the provenance identifiers of all eight directions. It generates the counts in the dossier and writes `outputs/integration_validation.json` and `outputs/integration_counts.json`.

`code/verify_archive.py` checks an archive without changing it: CRC integrity, exact manifest membership, every recorded byte count and SHA-256, required canonical files, safe relative paths, and exclusion of attachments, downloaded caches and earlier archives. Its checkpoint result is included in `outputs/checkpoint_01_archive_validation.json`; the same verifier is run on the final ZIP after packaging.

`code/manage_run.py` records UTC stages and packages immutable ZIPs. A checkpoint is allowed only after 45 minutes since the start or previous checkpoint. Earlier checkpoint archives and all source attachments are excluded. The final archive contains `ARCHIVE_MANIFEST.json`, recording the path, byte count and SHA-256 of every included authored file. If a checkpoint exists, its history file records the earlier names; the existence of a manifest entry is not itself evidence of successful persistent saving, which is separately recorded in the run log. The first checkpoint was due at 17:46:01 UTC and was created at 17:53:14 UTC, at the first execution after context compaction; this delay is recorded rather than backdated.

The work began at `2026-11-19T17:01:01Z`. All check dates and progress times are UTC. No elapsed time, reasoning-effort setting, proof-assistant execution or inaccessible review event has been invented.
