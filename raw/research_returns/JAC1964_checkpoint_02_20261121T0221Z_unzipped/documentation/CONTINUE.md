# Continuing this investigation

Run JAC1964-20261121 began 2026-11-21T00:51:37Z. The attached prompt remains the task specification. The archive was unpacked exactly once into `sources/`; to restore, use the original attachments and the hashes in `documentation/source_manifest.json`.

This checkpoint contains current deliverables, authored proof fragments, reviews, scripts and source maps. External full research papers and extracted source text are not redistributed; source maps give exact URLs and locators for retrieval. No earlier checkpoint is nested.

The three investigations are programme_audit, h9_height and arithmetic_sign. All used GPT-6 Astra Pro; effort setting is not exposed. No Lean build or complete source audit of the supplied breakthrough inputs is claimed.

The main geometric theorem JAC-T4.1–3, programme P00–06, H9 counterexample and repairs, and H9-T4/T5/T6 have whole-proof checks. Monodromy T6 is conditional on the explicitly stated all-primes irreducibility and nonzero vanishing-cycle hypotheses; it is not a claim for arbitrary special fibres. Arithmetic AR-1–7 have root whole-proof checks in the notes; AR-1a/AR-8 and the newest local refinement are being read and expanded. See the actual check events, not this overview, for scope.

Current arithmetic gate: after splitting the Picard summand, prove signed height positivity on the complementary Chow motive N. The CM Fermat quartic supplies a nonzero class in a rank-two N. Symmetry places its canonical Ceresa/Fourier class entirely in N; its height is a Gross–Schoen height. A stable-reduction tree gives a positive finite-place contribution; the remaining archimedean bound is being attacked. New primary source Gu arXiv2609.33223v2 gives a canonical adelic intersection formula and may supply the precise height line needed for the slope route.

Checkpoint timing: first due01:36:37UTC, next02:21:37UTC, then every45minutes. Never create an extra checkpoint between these times. First substantive movement review due03:51:37UTC, then hourly. Stop after two consecutive reviews with no open-row status change or strict main-gate reduction. No review has yet been due.

Rebuild the working paper by running `python work/build/assemble.py` from the restored workspace after adjusting its root path. The assembler currently puts the still-evolving arithmetic draft in a separate part. Before final delivery, complete whole-proof review of every final proof, move checked arithmetic deductions into the checked part, isolate unresolved gates, compile the paper and visually inspect its PDF. Update all tables and audit events. Deliver exactly one final ZIP named JAC1964_final.zip.

Persist checkpoint/final ZIPs using the Library skill. A local sandbox link alone does not persist a file. Do not overwrite older checkpoints.


## Checkpoint 02 update (2026-11-21 02:21:37 UTC)
New checked results since checkpoint 01: JAC-T4.4 actual primitive algebraic representative of an abelian threefold; JAC-T4.5 arbitrary-field descent; H9-T6a automatic variable monodromy; JAC-P07 automatic condition A for abelian pencils; H9-T7 full geometric-height decomposition; H9-T8 full semipositivity for abelian fourfold pencils; JAC-P09 geometric-generic degree-at-least-three axes; H9-T9 algebraically trivial incidence height and trace radical; H9-T10 actual algebraic representative of the generic threefold; JAC-P10 exact Fermat Faltings-height difference log(2)/4; AR-11 unconditional positive Fermat L-derivative; AR-12 exact theta reduction; AR-13 independently reviewed IEEE/Arb certificate proving the specified Fermat Ceresa height greater than 1/100. Full positivity on all CH(N) remains unproved. AR-13 is a reproducible numerical certificate under stated arithmetic assumptions, not formal verification. The latest individual proof fragments and per-agent check logs are authoritative for additions not yet integrated into the manuscript. The manuscript assembly will be refreshed immediately after this scheduled checkpoint. No stale compiled PDF is included.

Next: assemble all new fragments, root whole-read AR13 and T10 updated versions, rerun certifier, visually inspect compiled PDF; continue attacking full CH(N) positivity. First three-hour movement review due 03:51:37 UTC; next checkpoint due 03:06:37 UTC.
