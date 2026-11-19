# Reproducing the SA04 audit files

## Inputs and layout

The ZIP contains the authored work products, calculation programs and saved outputs. It deliberately omits the original attachments and external primary-source PDFs/OCR. Extract the three original user ZIPs beside a directory named `SA04_work`, so that the source files are under `source/SA04_texts`, `source/SA04_notes` and `source/SA04_PROMPT`. Extract this deliverable into `SA04_work`; the canonical root registers can remain at the extracted root. For rebuilding, create `SA04_work/final` and copy those canonical root registers there first. The analysis-body template is in `parts/root/dossier_body.md`.

The standalone dated prompt is authoritative for the45-minute checkpoint cadence. Its input hash is in SOURCE_MANIFEST. No program reads a note heading to decide a verdict: the builder files serialize already authored judgments. Rerunning a serializer does not itself repeat the manual source review.

## Runtime and relocation

The recorded session used Python3.12 and SymPy for exact algebra. The finite-field computations use explicit arithmetic in their source. Source fetch and OCR helpers additionally name their dependencies, such as PyMuPDF, requests, pdftoppm, tesseract or DVI tools. External retrieval requires network access; a retrieval log records whether a given fetch succeeded.

Several earlier programs retain the original workspace root `/workspace/scratch/594d1dc856a9`. Before rerunning those programs elsewhere, replace that literal workspace prefix with the new absolute workspace root, or recreate the layout at the recorded path. The final validator reports the affected files. This replacement changes paths, not mathematical inputs or assertions. `/tmp/SA04_*_external` paths identify transient downloaded reference copies: fetch them again from the recorded URLs if needed, rather than treating a missing temporary PDF as a missing deliverable.

## Calculation entry points

The principal mathematical programs are `a_computations.py`, `b_computations.py`, `b_supplement_computations.py`, `c_computations.py`, `c_manin_check.py`, `c_review_genus2.py`, `root_computations.py`, `root_git_computation.py` and `root_weierstrass_supplement.py`. Their outputs are saved in `outputs`. The written proof appendices state which outputs are finite checks and which identities have a universal argument. `b_tits_check.py` also preserves the exact building-action diagnostic.

## Assembly and validation

The final assembler reads the saved component registers and manually agreed alias/locator patches. To assemble from those saved components, run `programs/assemble.py`; to compile the overview with its current counts, then run `programs/compile_dossier.py`. The root stream can be regenerated with `root_finish.py`, followed by `root_references.py` and `root_search_ledger.py`; running `root_build.py` alone omits the final manually authored refinements.

`source_inventory.py` rebuilds the input hashes and catalogue scope from the original sources. `c_final_register_audit.py` independently audits source boundaries and event coverage. `final_quality_checks.py` checks the final canonical registers, exact event labels, authored overview, citation keys, saved outputs and packaging exclusions. It does not prove the mathematical claims.

The final root registers, not the pre-consolidation component files, determine the delivered IDs and counts. `ID_ALIASES.tsv` records C-SA04-217→C-SA04-122, MP-SA04-201→MP-SA04-164 and MP-SA04-204→MP-SA04-168, plus the single reassigned source-entry link. Bibliography provenance preserves historical stream keys; the two Milne works remain distinct.

The checkpoint program is tied to the original session’s scheduled cadence and must not be rerun to create unscheduled checkpoint copies. The final packaging program creates `SA04.zip`; it is a final deliverable, not a checkpoint.
