# Rebuild and provenance

The sources and read logs were read manually. The programs contain manually authored judgments, not automatic verdict inference from headings.

Run from the workspace root:

```sh
python SA23_work/parts/analysis_curves/functional_claims.py
"$CODEX_PRIMARY_RUNTIME_PYTHON" SA23_work/parts/analysis_curves/computations.py > SA23_work/parts/analysis_curves/computation_run.txt
python SA23_work/parts/analysis_curves/finalize.py > SA23_work/parts/analysis_curves/finalize_run.txt
python SA23_work/parts/analysis_curves/build_evidence.py > SA23_work/parts/analysis_curves/evidence_run.txt
python SA23_work/parts/analysis_curves/assign_status_categories.py
python SA23_work/parts/ega/final_reference_origin_audit.py
python SA23_work/parts/ega/add_lefschetz_request.py
python SA23_work/parts/ega/apply_problem_origin_audit.py
python SA23_work/parts/analysis_curves/validate.py > SA23_work/parts/analysis_curves/validation.txt
python SA23_work/integration/validate_ega_origin_application.py
```

Do not run the initial source builder alone: it deliberately restores the initial source adjudications before literature mapping. The finalized JSON and TSV files are the deliverables. The prose `section.md`, `proof_notes.md`, and final `coverage.md` are authored separately; the source builder’s old incremental coverage paragraph must not replace the final coverage document. `search_queries.json` stores exact final targeted queries; `search_log.jsonl` adds every claim’s match/limits and the relevant earlier access/bibliography trail. Full external works and raw caches belong under `sources/external/analysis_curves`, excluded from the final ZIP.

`render_primary.py` renders two image-only original1955 passages for inspection; those images are external-source caches, not user-authored figures. The initial probe used pages1,4,8,12,16,20,220,240,260 to establish the page map: chapterII printed p corresponds to one-based physical p+201. No OCR text is treated as an adjudicated manuscript reading.

For final source-origin labels, run ../ega/final_reference_origin_audit.py after both parts have been rebuilt, then the recovered-request and approved-problem-origin overlays shown above. The final analysis/curves part has14 authorial problems,15 editorial tasks,8 Stage6 directions and1 separate editorial direction. Whole redirects use original_id; partial contexts use source_problem_id. The original22 records and9 directions remain in provenance/pre_origin_audit. The overlay is idempotent and prevents repeated boilerplate in why_open fields.
