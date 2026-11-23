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

The latest hourly formal review is review09, completed2026-11-22 07:05:26 UTC; qualifying movement in MAIN01, MAIN04 and MAIN09 left the no-movement streak at0. The next formal review is due08:04:37UTC. Checkpoint14 was created06:34:37UTC and saved06:35:23UTC. This is the checkpoint15 assembled state, due07:19:37UTC; creation/upload receipts are retained after saving. Checkpoint16 is due08:04:37UTC. The immutable formal review and baseline remain work/reviews/review_09.json and work/gate_history/formal_review_09.json. Post-review results will be assessed at the next scheduled review; packaging is not movement.

The latest assembled snapshot contains 164 findings, all with completed full deduction-proof readings, 183 question rows and 1267 check events.

Under A the fully reviewed A049 theorem now has absolute kappa,c,T0: simultaneously for every T>=T0 and every primitive character of conductor q<=T^kappa, including zeta, each strict ordinary normal-velocity sign has at least1e-30 of all original zero occurrences represented by distinct simple centers. The same branches retain that side throughout0<tau<=c/T. They remain simple, disjoint and within the ordinate window on the larger anisotropic region(1+T|tau|)exp(12T|Imtau|)<=c1 exp(sqrt(loglogT/2)), and on the original sqrt(loglogT)/(100T) complex disk. Fixed larger real exp(B sqrt(loglogT))/T intervals and fixed multiples of sqrt(loglogT)/T complex disks have positive surviving fractions after reselection; their side assertion remains on the smaller c/T interval. Every fixed finite interval has a conductor-uniform Gaussian counting lower component of1e-30 times its Gaussian mass for normalized log derivative and both log speeds. These are lower components, not full CLTs or equal-label laws. Fixed-character proofs retain the sharper stated1e-24 critical count and1e-16 Gaussian component; the RH-only zeta sublogarithmic predecessor remains separately valid. Wider conductors, larger strict-side intervals, exact frequencies and ordinary general Dedekind signs remain open.

New C055, using E and the explicitly credited classical partial-matching contraction, constructs uniform constant-free integral permanent circuits for supplied nested cut-coordinate trees. Large leaf blocks may have arbitrarily distributed support m^(1+o(1)); each leaf may additionally carry a supplied low-rank correction. Sublinear outer width plus maximum leaf rank, and sublinear maximum E leaf cost, give2^o(n) circuits with polynomial formal degree in the original n, over every commutative ring. The complete matching boundary algebra and every contraction coordinate are charged. The one-leaf specialization contains the C041 sparse-plus-global-rank class, and a proved generic coarse-width-two family lies outside every old quasilinear-sparse-plus-rank-o(n) presentation and every full singleton-tree sublinear-cut-width presentation. No decomposition-finding or arbitrary dense permanent algorithm is claimed. C053 retains unconditional randomized exact simulation for the stated real odd-root and mixed flat-initialization classes. C054 proves all domain/zero/coordinate-sign tests for arbitrary nested principal complex binary roots are in P^PosSLP, with explicit branch labels, bounded-step exact control and FP^PosSLP tagged bounded-integer output. Boolean many-one equivalence uses a separately credited, locally audited classical adaptive-query compilation theorem. Oracle removal, unspecified complex constants, the remaining mixed-root sampling case and general Boolean/algebraic transfers remain open.

A050 gives every fixed fraction below2/3 as simple real branches surviving a common c_eta/log²T negative-time interval. A051 gives unconditional double-exponential actual nonreal-height ceilings, also for each fixed Dirichlet and Dedekind family. Under RH the first nonreal height tends to the least multiple endpoint, or infinity when all endpoints are simple; a finite endpoint has the proved linear drift and O(a²) remainder. Endpoint multiplicities, sharper all-simple escape and arithmetic collision origins remain open.

G039 now proves the exact extended limit a*j_*(-a)=x_*²/8 under A, where x_* is the least positive multiple endpoint and the value is infinity if all endpoints are simple. The proof gives uniform hyperbolicity through every scaled degree gamma/a with gamma<x_*²/8, and a simple complex pair above the threshold. Its unconditional eventual upper degree remains triple exponential. The finite Jensen algebra has a negative trace-square witness when the pair appears. The reviewed counterfamily has Jensen failure already at degree2 while all original Toeplitz/character tests through any prescribed finite r remain strictly positive, even after coefficient normalization. The Jensen metric is therefore recorded separately from original detecting order, index window and unitary rank; no automatic older-gate movement credit is assigned.

The original132-position graded interval remains[932,2744], and the unrestricted all810-position interval remains[112,2744]. The symmetric fixed-D closed-table optimum is exactly2744 with unique parameters. A fully reviewed source-reconstructed Hasse associator calculation constrains all810 pair-mass parities to a92-dimensional binary linear space:3249 rows have rank718 and force421 coordinates, including340 new nonunit-output positions, to have added dimensions divisible by4. Further joint congruences remain available. These are necessary constraints; only a separately checked positive-gap integer certificate changes a numerical bound. Necessary-relaxation attainers are not effective graded lifts.

The integral counting, isolation, canonical GCT realization and general complexity-transfer gates remain precisely scoped. No P versus NP or VP versus VNP resolution is claimed.

Earlier-stage open-gate remarks inside the chronological proofs are historical; the current summaries and later explicitly stated refinements supersede them. Each earlier theorem retains its own hypotheses and constants.

## Check semantics

E and A are the designated input theorems specified by the task. All uses of M remain conditional. A complete proof reading checks the deduction, not all imported input theorems. No Lean build has been performed. Effort is not exposed by the runtime. Finite calculations and exact interval/symbolic certificates are logged separately from proof checks. The corrected archive excerpts are transcriptions unless an image inspection is separately recorded.

The complete TeX source and proof fragments are included. The paper has 768 pages. Every page passed the word-boundary audit; actual sampled image views are recorded in work/pdf_qa/cp15_bounds_check.json. This is sampled layout QA, not visual inspection of every page. Whole-proof readings, explicitly read amendments, source-interface checks, exact finite computations and compilation are separately recorded. Earlier failures and corrections remain documented.

Use `clock__curr_time`, not the host shell clock, for all dated events. The host clock was observed approximately one hour ahead. Never reconstruct elapsed work or invent review times from file modification dates.

Research reference copies acquired during this run are represented by their exact locators and checksums in EXTERNAL_REFERENCE_COPIES.json. The supplied archive sources and all original proofs, registers, code and certificates are included. The Goldreich–Izsak paper explicitly permits CC-BY reuse and is retained with its license.
