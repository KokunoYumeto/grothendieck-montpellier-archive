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

The fourth formal movement review was completed at2026-11-22 02:05:02 UTC and found movement in4 main gates. The consecutive no-movement count is0. The next review is due2026-11-22 03:04:37 UTC. Checkpoint08 was saved at2026-11-22 02:05:18 UTC. This is the checkpoint09 assembled state, due at02:49:37 UTC; its creation/upload receipts are retained in work/receipts after saving. Checkpoint10 is due2026-11-22 03:34:37 UTC. See work/reviews/review_04.json and the frozen baseline work/gate_history/formal_review_04.json; interim updates never reset that baseline.

The latest assembled snapshot contains 147 findings, all with completed deduction-proof readings. The exact symmetric fixed-D closed-table dimension-ring optimum is2744 cancelling pairs, with a unique parameter realization. For the entire original132-position support, the current proved interval is[900,2744]; for all810 allowed nonunit-input positions it is [104,2744]. Integral formal counting covers the stated subpolynomial scopes and actual-degree budgets, arbitrary-density growing-width CNFs in the explicit range k=o(loglog n/logloglog n), and supplied sparse-plus-low-rank permanent decompositions with residual support n^{1+o(1)} and rank o(n). Both branch-center classes have positive lower proportions for every fixed primitive Dirichlet character under A, and for each specified Dedekind zeta under its RH, supplied conditionally by M. NN-A046 proves square-root-scale signed cancellation and at least c_chi,epsilon T^(1-epsilon)logT centers of each strict ordinary simple sign in (T,16T] for every fixed primitive Dirichlet character under the stated A scope; the zeta case needs RH alone. Positive ordinary proportions and half balance remain open. NN-C044 gives unconditional nonuniform bounded-integer-output simulation with polynomial-bit algebraic constant descriptions and individual degrees d for which lcm(1,...,d) is polynomial, including d=O(log n). The orbital positivity radii satisfy r_m=Theta(sqrt(m)). General PIT, polynomial NP isolation, canonical GCT multiplicities and arithmetic extreme gaps remain separate gates. No P versus NP or VP versus VNP resolution is claimed.

## Check semantics

E and A are the designated input theorems specified by the task. All uses of M remain conditional. A complete proof reading checks the deduction, not all imported input theorems. No Lean build has been performed. Effort is not exposed by the runtime. Finite calculations and exact interval/symbolic certificates are logged separately from proof checks. The corrected archive excerpts are transcriptions unless an image inspection is separately recorded.

The complete TeX source and proof fragments are included. The paper compiles to 508 pages. Every page passed the text-edge check. Explicitly viewed sample pages and their result are recorded in work/pdf_qa/cp09_bounds_check.json. This is sampled layout QA, not a claim of visual inspection of every page. Source-locator verification and mathematical proof readings remain separate from compilation and layout checks. Earlier build failures are retained in the work log.

Use `clock__curr_time`, not the host shell clock, for all dated events. The host clock was observed approximately one hour ahead. Never reconstruct elapsed work or invent review times from file modification dates.

Research reference copies acquired during this run are represented by their exact locators and checksums in EXTERNAL_REFERENCE_COPIES.json. The supplied archive sources and all original proofs, registers, code and certificates are included. The Goldreich–Izsak paper explicitly permits CC-BY reuse and is retained with its license.
