# Reproducibility of the workstream

The Python builders serialize individually researched and written records. They do not infer reading verdicts from source headings or generate mathematical conclusions. All claims, proofs, queries and reference decisions were written from the source/literature audit.

The final records are already saved and validated. To rebuild their serialized presentation, use this order from the workspace root:

1. `python SA19_work/workstreams/cotes44_47_54/code/build_items.py`
2. `python SA19_work/workstreams/cotes44_47_54/code/build_claims.py`
3. `python SA19_work/workstreams/cotes44_47_54/code/build_problems.py`
4. `python SA19_work/workstreams/cotes44_47_54/code/build_references.py`
5. `python SA19_work/workstreams/cotes44_47_54/code/polish_records.py`
6. `python SA19_work/workstreams/cotes44_47_54/code/finalize.py`
7. `python SA19_work/workstreams/cotes44_47_54/code/build_tables.py`
8. `python SA19_work/workstreams/cotes44_47_54/code/build_audit.py`

`code/computations.py` reproduces the exact mathematical certificates; its output is already saved under `outputs/`. `computations.md` states the geometric hypotheses, complete arguments and the limits of each finite symbolic calculation. The numerical certificates alone do not establish the general geometric theorems.

`fetch_primary_extract.py` was used to extract the exact EGA and ICM passages from complete primary PDFs. It is retained as a provenance tool, not a dependency for reading the supplied final records. Primary extract JSON files retain the source URL and hash. Numbered search files preserve the actual web responses.

Root integration may merge these records with records from other workstreams. Do not rebuild merged root files from a worker builder: root integration has its own cross-package identifiers and origin annotations.
