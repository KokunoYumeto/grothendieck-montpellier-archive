# Reproducing the cote-16 checks

The mathematical verification program is `scripts/exact_checks.py`. Run it with Python and SymPy available. It writes the exact certificates to `outputs/exact_checks.json` and prints the same results; the saved text output is `outputs/exact_checks.txt`. The program uses exact integer and rational arithmetic, not floating-point tolerance tests. The general arguments and the limits of finite tests are in `proof_checks.md`.

The data-register builders serialize judgments authored after direct reading. They do not discover claims or assign verdicts by searching for words. `build_stage1.py` writes the entry/item register; `build_claims.py`, `build_problems.py`, `build_readings.py` and `build_links.py` write their named registers. After these, `build_support.py` writes coverage and check events. Their recorded outputs are retained under `outputs/`.

Run `scripts/validate_worker.py` after the registers exist. It checks required fields, entry coverage, ID and reference closure, origin records, the separated EGA comparison lead, claim search coverage, all54 scan markers, required prose files and selected exact-output invariants. Its output is `outputs/validation.json`, with the saved terminal transcript in `outputs/validation.txt`. A successful validation does not substitute for human/model source reading or a mathematical proof.

`finalize_worker.py` and `finish_audit.py` record one-time editorial amendments made during the run. They are process records against the immediately preceding file versions, rather than an idempotent build pipeline. Their results are already incorporated into the final builders. They should not be rerun on the final snapshot. Download and OCR scripts likewise document actual reference-access attempts. Interrupted EGA fetch outcomes are preserved explicitly; no empty output is represented as successful access.

No source attachment has been edited. The final top-level consolidated dossier is the parent's deliverable; this directory preserves the worker's independent records and evidence.
