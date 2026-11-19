# SA15 — Complete dossier

**Start with `SA15_dossier.md`.** It presents the folders in their working
sequence, explains the major corrections and exact later fates, and ends
with the final census. `SA15_directions.md` contains twelve ranked, bounded
next tasks. The remaining files are the underlying research registers and
the audit trail.

## Main files

| File | Purpose |
|---|---|
| `SA15_entries.tsv` | Exactly the 80 supplied index IDs, one read verdict per row |
| `SA15_supplementary_entries.tsv` | The 847 additional in-scope notes omitted from the supplied index |
| `SA15_items.json` | Consolidated items, brief source wording, precise statements, reconstructions and text checks |
| `SA15_claims.json` | Documentary status, computation/proof records, searched later fate, dates, references and confidence |
| `SA15_problems.json` | Every retained open step, hope and doubt, including resolved or withdrawn questions |
| `SA15_readings.tsv` | Undecided mathematical alarms for a future scan-based review |
| `SA15_links.tsv` | Links checked at both source endpoints |
| `SA15_unverified_links.tsv` | Absent cote 54 endpoints and the unverified exact Demazure–Gabriel passage |
| `SA15_project_leads.tsv` | Intentionally header-only: no named external project/run endpoint occurs in the supplied in-scope notes |
| `SA15_references.bib` | Every cited bibliographic key, with verified/unverified access note |
| `SA15_reference_guide.md` | Readable key-to-work/URL table |
| `SA15_reference_evidence.json` | Exact inspected locators, source versions and access/proof limitations |
| `SA15_claim_search.tsv` | One row for every final claim, with exact source search work and scope assessment |
| `SA15_status_census.tsv` | Documentary status separated from modern validity and refinement provenance |
| `SA15_counts.json` | Final machine-readable counts |
| `SA15_id_map.json` | Temporary reviewer IDs mapped to final item/claim/problem IDs |
| `CHECK_EVENTS.tsv` | Actual text, theorem, proof, computation and refutation checks |
| `progress.log` | UTC start, stage milestones, scheduled checkpoint and completion |

The code, saved outputs, written proofs, source-read records and per-reviewer
evidence are in `work/`. The original attachments are deliberately not
duplicated. The supplementary cote 100 inventory is an exclusion record,
not an uncompleted part of SA15.

## Evidence conventions

Locations refer to one-based lines of the supplied transcription files,
including blank lines, paired with their cote and scan. They do not claim
to number ink lines on scans not supplied here. Brief `his_words` quotations
come from those transcriptions; an empty quotation on an earlier-run idea
means that no manuscript statement is being attributed to it. Some
`his_statement` fields are concise reports of the displayed assertion,
explicitly identified as such, rather than new diplomatic transcriptions.
The precise original wording and cancellations remain at the cited lines.

Class A is restricted to an exact endpoint in Grothendieck's own authored
later work. Artin and Deligne exposés do not become class A merely because
they appear in SGA. The other fate classes, documentary statuses, modern
truth judgments and provenance labels are independent fields. In
particular, a false assertion can have a well-identified published fate.
No failure to find a paper has been converted into class D.

Some refutation events point to a separate refinement claim; six compound
records instead retain the manuscript report and an explicitly identified
`refined_statement` under the same record ID. The event points to that
corrected field, not to a circular proof of the rejected assertion.

`verified` means the listed URL or DOI was opened. The evidence file says
whether this yielded a theorem, a proof passage, a later report, an
image-only scan or bibliographic metadata. It is not a blanket proof
certificate. A few elementary counterexamples have no external theorem
reference because their complete proofs and exact output are supplied.
Unidentified foreign leaves likewise have no invented exact-match citation;
their search evidence and identification limits remain explicit.

All mathematical searches and present-status assessments are as of
19 November 2026. Dates of first circulation are given only where verified.
Source-year metadata are not claims of priority. No proof assistant was
executed. A source reporting a Lean proof is labelled as that source's
report, separately from the written proofs and exact calculations here.

## Proof and computation map

| Subject | Written argument | Program / saved result |
|---|---|---|
| Universal PD algebra, W(ν,r), valuations, Artinian de Rham and elliptic diagnostics | `work/cotes5_6/reviews/independent_proofs.md` | `work/cotes5_6/code/recheck_algebra.py`; `work/cotes5_6/outputs/algebra_checks.json` |
| Formal-group, de Rham, weak-completion and Gauss–Manin checks | `work/cotes6_7/computation_notes.md` | `work/cotes6_7/code/computations.py`; its results under `work/cotes6_7/outputs/` |
| Completed diagonal, ordinary gauges, A-linear modules, periods, jets, Tannakian and co-Lie checks | `work/root_review/proof_audit_root.md` | `work/root_review/code/check_root_math.py`; `work/root_review/outputs/root_math.json` |
| Constant 5-torsion with different finite inertia | `work/cotes8_9_4/proofs.md`, §1 | `check_elliptic_inertia_counterexample.py`; `outputs/elliptic_inertia_counterexample.json` in that directory |
| Cote 4 torsion defect and determinant/representation tests | `work/cotes8_9_4/proofs.md`, §§2–4 | `check_calculations.py`; `outputs/calculations.json` |
| Nontrivial Witt-coefficient identities | `work/cotes8_9_4/proofs.md` and claim register | `check_dieudonne_twists.py`; `outputs/dieudonne_twists.json` |
| Dimension-one monodromy boundary | Claim record and `work/cotes8_9_4/proofs.md` | `check_monodromy_boundary.py`; `outputs/monodromy_boundary.json` |
| Exact SGA7 filtration-length special case | `work/cotes6_7/sga7_pcase_audit.md` | A general written deduction; no numerical or formal certificate is claimed |

Where the short program names in the last four rows are used, they are
under `work/cotes8_9_4/code/`, with the results under the corresponding
`outputs/` directory. Finite computations are explicitly bounded. Their
successful output is corroboration for examples, not a proof for every
parameter. The general arguments state their hypotheses separately.

## Rebuilding the assembled registers

The final curated owner registers are retained. From the archive root,
these commands rebuild the combined files and their counts:

```bash
python3 work/root_review/code/finalize_root.py
python3 work/root_review/code/build_search_ledger.py
python3 work/code/add_comparison_links.py
python3 work/code/merge_core.py
python3 work/code/merge_aux.py
python3 work/code/finalize_records.py
python3 work/code/build_documents.py
python3 work/code/validate_final.py
```

The last validation also checks the supplied source hashes when the
attachments have been placed back under `sources/`. It reports explicitly
when they are absent. The assembly scripts do not search the literature
again or infer new note verdicts. Earlier authoring serializers are included
for inspection; some are sequential amendments intended to run once after
fresh curation. `work/execution_notes.md` describes that distinction.

The recorded runtime is Python 3.12.14 and SymPy 1.14.0. The assembly uses
only the standard library; the exact algebra scripts use SymPy and Python
integer/fraction arithmetic. `work/outputs/runtime_versions.txt` records
the actual versions. Successful structural validation certifies coverage,
schemas and joins, not the mathematical truth of every theorem.

`archive_manifest.json` lists included files and hashes, and records omitted
temporary literature copies. Complete third-party PDFs, page images and
verbatim web-response bodies are not redistributed. Exact queries, opened
URLs, original scope assessments and failures of access remain in the
search/evidence records. `packaging_result.json` records the packaging
operation without a self-referential archive checksum.
