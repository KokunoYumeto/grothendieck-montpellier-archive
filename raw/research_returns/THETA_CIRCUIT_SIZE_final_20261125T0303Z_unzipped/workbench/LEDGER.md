# Research ledger

Clock start: 2026-11-25 02:02:11 UTC (03:02:11 Europe/Berlin).
The archive was unpacked once, to a separate source directory. The bounded
research window ends no later than 04:02:11 UTC.

## Initial interval

- Read the task and audited the pinned circuit definition.
- Split work across independent mathematical workers: the general branch
  proof in the nonadjacent theta certificate; adjacent-theta and monotone
  arguments; and the hazard derivative argument.
- Confirmed that the Lean executable and Lake are absent from PATH. LaTeX,
  Poppler and Python are available. Any Lean files returned without a successful
  compiler run must be marked uncompiled.
- Installed python-sat 1.9.dev25, z3-solver 5.4.1.0 and networkx 3.7 for exact
  experiments; the independent baseline verifier uses only the standard library.
- Began a direct audit of branching wires. A candidate matching lower bound
  could replace the finite twin-deletion enumeration; it remains under review.

The production model is GPT-6 Astra Pro, at the session's inherited effort
setting (the numeric effort is not exposed). Parallel checks are by separate
workers of that same model, not by independent model families or humans.

## Before the first half-hour return

- Independent truth-table and mutation controls passed; source graph counts
  and unique cover rechecked.
- The general first-branch proof was extended by a direct vertex-cover
  construction, proving n−1+τ binary gates for every min-degree2 no-C4 graph.
- A fresh worker independently re-proved the complete shared-DAG theorem
  before reading the run proof, then targeted-audited the concrete paper.
- The positive18 bound was re-proved from singleton carriers and consumption
  slots, credited to fengqiaoqu. Therefore the primary optimum is18.
- Restriction was proved not to increase branch count under local
  simplification. This closed the requested C8 roots0,3 case at14, and yielded
  an exact formula for even cycles with two leaves.
- A separate two-leaf worker independently proved the numerical reduction
  and same-parity case, then audited the other case after reading. A further
  fresh worker is completing a statement-only proof with published source
  lemmas, without reading this run's proof.
- An independent17-gate one-NOT SAT experiment returned UNKNOWN after122.16s;
  the pinned18 positive control was SAT and valid on the full cube.
- Official Lean4.36.0 was installed locally. The compact core graph helper
  compiled and all axiom dependencies were inspected. The full pinned
  Mathlib cache bootstrap failed on native initializer/symbol requirements;
  no full project formalization is claimed.
- A complete shorter re-proof of the general positive theta theorem was
  written after the concrete theorem closed. It is included as a research
  proof now and will be incorporated into the next paper draft.
- The paper built from a fresh directory:11 pages, no overfull boxes or
  undefined references. All11 rendered pages were visually inspected.

## Half-hour review1 — 2026-11-25 02:32:11 UTC

Movement: primary optimum18 and requested follow-on14 proved, independent
re-proofs completed, compact graph lemma kernel checked. A distinct next task
is actionable: incorporate the shorter general positive-theta proof into the
standalone paper and complete its independent verification. Continue research.

## Second interval

- Incorporated and fully rechecked the positive theta equality obstruction;
  the paper now proves the exact all-gate size of every theta graph without
  a 4-cycle, including direct-edge and triangular cases permitted by that
  hypothesis. The earlier positive theorem is credited to fengqiaoqu.
- A fresh statement-based worker completed the two-leaf proof, and separate
  workers re-proved the general theta and odd-cycle follow-on arguments.
  Their precise prior exposure and the distinction between re-proof and
  targeted audit are recorded in the check events.
- Proved the odd-cycle theorem with three pairwise nonadjacent leaf roots
  at odd cyclic distances. In particular, the C9 roots0,3,6 example has
  exact size17. Its explicit witness passed all4096 assignments and a
  deliberately changed gate failed74 assignments.
- Found and preserved a genuine normalization omission in a standalone
  carrier helper. The triangle constant-true counterexample refutes the
  unnormalized wording; the corrected normalized statement is sufficient
  for every theorem. No main numerical result changed.
- Added finite graph, restriction and witness controls, including365759
  theta parameter triples for the independent cover formula check. These
  computations are controls, not exhaustive circuit lower bounds.
- Audited the elementary scheme-over-Z dictionary and corrected the
  presentation/metadata and invariant qualifications. No unsupported
  lambda-ring, K-theoretic, motivic or weight consequence is claimed.
- Completed the14-page standalone paper from a fresh source copy, using
  three pdfLaTeX passes. There are no LaTeX warnings, overfull boxes or
  unresolved references. Read the complete final text as an expert and as
  a newcomer and visually inspected all14 rendered pages.
- Updated all30 statement records and48 check events, source attributions,
  deposit sheet, replay instructions, outstanding questions and method
  disclosures. The return audit found no unchanged source copies or
  credential patterns.

## Half-hour review2 — checkpoint scheduled 2026-11-25 03:02:11 UTC

The review was prepared immediately before the sixty-minute checkpoint.
Movement since review1: the full positive-theta proof is now incorporated
and independently re-proved; the odd-cycle three-root family is settled;
all main proofs, finite controls and final paper checks are complete.
The primary17-versus18 question is answered18 and the requested C8 follow-on
is answered14. The reusable graph theorem has a small compiled Lean core.

Stop mathematical research after this review and complete the cumulative
checkpoint and final packaging. The next substantial tasks are a full formal
circuit-to-partition proof and the next four-marked cycle family. Neither
is needed for the proved results, and no additional short decisive argument
is currently in progress. Do not extend the run by speculative work.

The final archive will be reopened, its complete manifest and safe paths
validated, and the primary, independent-primary, branch-certificate, two-leaf
and three-leaf programs replayed from extraction. The packaging result is
reported with the final delivery; it is not used to certify a mathematical
lower bound.

## Finalization — 2026-11-25 03:03:50 UTC

The second checkpoint was created at the sixty-minute milestone, reopened
and hash/path checked, and all five included replay programs succeeded from
its extraction. It was saved and its working download link exposed. Both
checkpoint files remain unchanged. Their exact hashes, validation reports
and durable links are recorded in research/checkpoint_status.json.

The last cross-file review then caught an omitted k>=3 hypothesis in the
README and question-table even-cycle summaries; the paper and THETA-015
already had it. The summaries are corrected in the final return. A64-row
six-gate C4 counterexample is preserved as THETA-031. This is separate from
the earlier normalization correction. The paper is unchanged from its
fully reviewed fourteen-page build. The final records have31statements and
50check events. Mathematical research is complete.

The final package adds this correction and a sixth extracted replay check.
It will be delivered as THETA_CIRCUIT_SIZE_final.zip alongside both immutable
checkpoint links. No public repository or external recipient was changed.
