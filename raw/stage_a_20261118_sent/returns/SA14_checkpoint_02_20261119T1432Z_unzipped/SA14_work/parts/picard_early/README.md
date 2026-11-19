# Early Picard part

The authoritative current deliverables are the JSON/TSV/Markdown files in this directory. `outputs/validation.json` records structural coverage and join checks; it is not a theorem-proof certificate. All155 assigned source-note IDs have exactly one verdict and one consolidated item.

Mathematical rechecks are in `computations.md`, with code in `scripts/recheck_calculations.py` and exact results in`outputs/calculations.json`. The26 calculation groups deliberately distinguish illustrative algebraic models from geometric counterexamples. The full explanatory dossier is`synthesis.md`; ranked unexecuted future tasks are`directions.md`.

`links.tsv` holds checked current archive/publication links. `project_leads.tsv` separately records unavailable older contextual endpoints. Current271–315 endpoints were checked by the neighboring part owner; the named older project files remain quarantined.

The scripts serialize authored decisions; they do not classify notes by text matching. Rebuilding the original authored records requires this order: `build_items.py`, `build_claims.py`, `finalize_records.py`, `build_problems.py`, `build_readings.py`, `build_references.py`, `build_links.py`, `finish_aux.py`, then `build_audit.py`, `supplement_audit.py` and `validate_part.py`. `finalize_records.py` is intended to run once after its two builders. The current files already include those corrections. Do not run an earlier builder alone and mistake its intermediate output for the final reviewed records.

The initial read-log timestamps are actual packet-display timestamps. Later additional-read records explicitly say when the precise read time was not separately stored. Source scans and source physical lines are different locator systems; the supplied diplomatic transcriptions were not edited. No ink decision was made without scans.

`supplement_root_audit.md` records the separately requested Corr/conormal investigation and independent audit of root claims C601–686, followed by the finite Stein factor refinement proposed for root C687. Those claims belong to the root register and are not silently duplicated into this part’s142 claims. `supplement_search_log.tsv` records the separate root-source investigation. Its initial query wording summarizes search themes; `outputs/web_72.json` additionally preserves exact search input and output for the final bounded follow-up.
