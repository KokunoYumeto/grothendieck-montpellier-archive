# Reproduction and audit

Run commands from the workspace root. The mathematical verdicts and source identifications in the builders are explicitly authored records; the programs serialize them and validate joins. They do not infer verdicts from headings or keywords.

The current tables can be regenerated with:

```bash
python SA14_work/parts/lfunctions/scripts/build_items.py
python SA14_work/parts/lfunctions/scripts/build_claims.py
python SA14_work/parts/lfunctions/scripts/build_auxiliary.py
python SA14_work/parts/lfunctions/scripts/build_bibliography.py
python SA14_work/parts/lfunctions/scripts/build_links.py
python SA14_work/parts/lfunctions/scripts/build_search_log.py
python SA14_work/parts/lfunctions/scripts/build_check_events.py
python SA14_work/parts/lfunctions/scripts/calculations.py > SA14_work/parts/lfunctions/outputs/calculations.txt
python SA14_work/parts/lfunctions/scripts/validate.py > SA14_work/parts/lfunctions/outputs/validation.txt
```

`calculations.py` uses Python and SymPy. It contains25 labelled calculations and explicit assertions. Its final success marker is in `outputs/calculations.txt`; the validation report records hashes of both files. Finite calculations certify their examples. General arguments and exact published inputs are separately stated in `proof_notes.md`.

`read_source.py` prints a requested physical source range, saves that exact displayed range and appends its timestamp to `read_log.tsv`. It is a documentary tool, not a proof checker. `outputs/read_*.txt` records the requested reading chunks. The first ranges were logged retrospectively without pretending to have exact timestamps; a final reread closes the initially truncated note range.

The `refine*.py`, `extend_proofs.py`, `polish_claims.py` and `audit_source_alignment.py` files are records of one-time authored edits made during the investigation. Their changes are already present in the current builders and prose. They are not a pipeline to rerun on the final state: some deliberately assert that the old paragraph still exists before replacing it.

Saved `web_*.json` responses and the query table document retrieval. The bibliography and primary-read log distinguish exact theorem/proof reads from metadata verification. Whole external PDFs were kept outside the deliverable directory and are referenced by URL rather than redistributed.

`validate.py` checks source-ID coverage, item membership, schemas, statuses, source-line bounds, scan starts, references, search mappings, event coverage, complete logged source ranges and computation markers. It does not replace the substantive reading or mathematical arguments.
