# Review of the separate e=38,40 completion audit

Reviewer `/root/lean_chain`; GPT-6 Astra Pro; effort not exposed.
21 November 2026. No Lean kernel execution and no large unitary replay
are claimed by this review.

## Reviewed code and actual execution

The entire new files `../higher4/native_full_further_completion_snapshot.py`
and `../higher4/further_certificate_audit.py` were read. The current
reviewed hashes and the hashes of the actual fresh audit reports are in
`further_audit_review_manifest.json`.

The fresh execution at review time completed successfully and reported
`complete_degrees=[]`, `pending_degrees=[38,40]`. At that time e=38 had
complete exact discovery support and all three full classical replays;
its full initial unitary replay and both alternate native calculations
were still running. Initial discovery support for e=40 was not yet
complete. These statuses are a dated observation, not a prediction of
later results.

## What is checked

The native collector requires a final full PASS report, every identifying
row, every one of the thirteen frames, the full independently reconstructed
harmonic kernel, complete model text verification, and dimensions agreeing
with the actual model arrays. It reconciles both model hashes, the
unmodified structural verifier and its exact prefix, the native source
and executable, the wrapper, and the neighbor-frame source. With exact
Python integers it verifies the comparison factor, all model denominator
units, the quadratic norm units, and `det(A) det(D)=det(S)` in the
specified quadratic coefficient algebra. Missing final reports produce
pending rows. Progress logs are not a completion input.

The main audit recomputes both initial-field comparison polynomial
evaluations, their common gcd, the displayed small-prime factorization,
bounded-factor divisions, and the repeated gcd exhaustion by the two
remaining composite moduli. Large primality is explicitly unused. It
checks the discovery-to-frozen-data equality and hashes.

A full initial unitary replay is accepted only through its final report,
full kernel dimensions, all neighbor evaluations, both characteristic
polynomials, extra-point checks, and corresponding frozen source/input
hashes. The sum-first path also checks matching start/end provenance.
The cyclic paths require both full-dimensional modular Krylov witnesses
and exact integer Horner-zero certificates. These are reconciliations
of completed runs, not fresh executions by the audit.

For each degree the classical gate requires one initial and two alternate
full fresh model replays, an exact three-row shape, current source and
data hashes, and the expected moduli. The candidate alternate calculations
are checked for dimension, weight, comparison point, all recorded pivot
units and the final cubic determinant unit. The fresh replay compares
every numerical object, excluding elapsed time only.

The final completion flag is the conjunction of a completed full initial
unitary replay, both completed alternate unitary units, and a completed
three-model classical replay. Exhaustive support alone is insufficient.

## Identified and repaired modulus-binding issue

The initial version constructed directory names from the required support
moduli but checked only that the model modulus agreed with its own report.
A consistently misplaced model and report could therefore have passed
under another modulus's directory name. I reported this exact issue to
the parent. The reviewed final version iterates over the required modulus
and path together and explicitly asserts

`model.q == report.modulus == required_modulus`.

The main audit additionally checks every completed native row's modulus
and degree against its required case. I inspected both repairs and ran
the hardened audit successfully. No earlier frozen scripts were edited.
The parent's separate reconciliation of older completed cases is a
separate check event, not a new execution by this reviewer.

## Separate classical drivers

The new `gl2_further_moduli.py` and `verify_further_classical.py` were
written and read in full. Their underlying finite-model algorithms are
the previously audited ones. They execute the frozen model source,
record start/end hashes and write atomic final reports. The per-degree
fresh replay reports are distinct, so completion of e=38 does not imply
completion of e=40.

Actual e=38 execution passed both alternate models in dimension 149,
followed by a fresh replay of the initial model and both alternate
models. The exact residues and report hashes are saved in
`../higher4/further_e38_start_manifest.json` and the linked final reports.
This is a fresh same-code classical replay, not an independently derived
new classical model, and does not by itself imply K76 vanishing.
