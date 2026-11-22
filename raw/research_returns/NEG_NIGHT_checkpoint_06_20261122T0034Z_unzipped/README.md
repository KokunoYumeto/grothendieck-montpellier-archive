# NEG_NIGHT research checkpoint

This is a continuing checkpoint of the task in `TASK_PROMPT.md`. The run started at 2026-11-21 20:04:37 UTC. No final exhaustion decision has been made.

## Read first

- `NEG_NIGHT.tex` is the paper entry point. Compile from the archive root; its complete proof fragments are in `paper_parts/`.
- `CONSEQUENCES.tsv` and `CONSEQUENCES.json` identify the findings, exact inputs, implications, geometric translations and proof-review status.
- `QUESTIONS.tsv` identifies treated questions and the current open gates.
- `LEDGER.md`, `CHECK_EVENTS.tsv` and `IMPLICATIONS.md` explain actual progress, checks and consequences.
- `BUILD_STATE.json` records the snapshot time and reviewed/unreviewed totals.

All supplied source files are preserved in `sources/`, together with their original relative names and the source manifest in `work/source_manifest.json`. The original archive was unpacked once. Do not unpack it again. Earlier checkpoint ZIPs are not embedded.

## Continue the work

The four tracks are `/root`, `/root/complexity`, `/root/gct` and `/root/analytic`; their working files and scripts are under `work/`. The assembler is `work/assemble.py`; it requires an actual UTC tool-clock value. It does not create an archive. `work/checkpoint.py` refuses early or overwrite creation and requires the numbered 45-minute boundary.

The second formal movement review was completed at 2026-11-22 00:04:54 UTC. Ordinary ideal certificates and dimension-ring optimization had strictly smaller proved gates. The consecutive no-movement count is zero. The next review is due at2026-11-22 01:04:37 UTC; the next checkpoint after06 is due at2026-11-22 01:19:37 UTC. See work/reviews/review_02.json and its frozen formal baseline in work/gate_history/formal_review_02.json. Interim progress does not reset that baseline.

This snapshot contains128 findings, all with completed deduction-proof readings. The exact symmetric closed-table dimension-ring optimum is2744 cancelling pairs, with a unique parameter realization; the larger class allowing additional zero-trace table positions remains open. New integral formal counting circuits handle arbitrary fixed-width CNFs in the original variable parameter; the characteristic-two exponent is stronger. Sparse permanent circuits need only a total quasilinear support bound. Under A, at least one sixth of all positive-height zero occurrences of each fixed primitive Dirichlet L-function are simple and transverse; the left/right proportions remain open. General PIT, polynomial NP isolation, canonical GCT multiplicities and extreme gaps remain separately scoped gates. No P versus NP or VP versus VNP resolution is claimed.

## Check semantics

E and A are the designated input theorems specified by the task. All uses of M remain conditional. A complete proof reading checks the deduction, not all imported input theorems. No Lean build has been performed. Effort is not exposed by the runtime. Finite calculations and exact interval/symbolic certificates are logged separately from proof checks. The corrected archive excerpts are transcriptions unless an image inspection is separately recorded.

The complete TeX source and proof fragments are included. The paper compiles to374 pages. Every page passed the text-edge check, and pages91,94,178 and254 were explicitly visually inspected without clipping or overlap. The complete check is recorded in work/pdf_qa/cp06_bounds_check.json. This is sampled layout QA, not a claim of visual inspection of every page. Source-locator verification and mathematical proof readings remain separate from compilation and layout checks. Earlier build failures are retained in the work log.

Use `clock__curr_time`, not the host shell clock, for all dated events. The host clock was observed approximately one hour ahead. Never reconstruct elapsed work or invent review times from file modification dates.

Research reference copies acquired during this run are represented by their exact locators and checksums in EXTERNAL_REFERENCE_COPIES.json. The supplied archive sources and all original proofs, registers, code and certificates are included. The Goldreich–Izsak paper explicitly permits CC-BY reuse and is retained with its license.
