# AN_GRH continuation state

Start: 2026-11-21 00:15 UTC (01:15 Europe/Berlin). Checkpoints only every 45 minutes: 01:00, 01:45, 02:30, 03:15, etc. Checkpoint01 and checkpoint02 were saved successfully and must not be altered or nested. First progress review is due 03:15 UTC, then hourly; two consecutive reviews with no movement trigger stopping. No scheduled review is due yet. The original ZIP was extracted once into source/.

## Current proved results

A01 gives the exact A1 statement and covering formulation, retaining the full arithmetic quotient. A05 is a checked unconditional reconstruction of the recovered cuspidal/configuration proof. The requested proof through Hooley remains unestablished. A02 supplies only its arithmetic theorem under Masullo's claim. A06 refutes the universal primitive-root theta bridge on the rank-zero B23 curve.

A07 gives generic positive-rank counterexamples over finitely generated fields with transcendental moduli, not finite fields. A08 gives finite-list avoidance over finite fields. A09 gives an exact order-13 rank-one witness. A10 excludes order-three theta incidence on nonordinary genus-two curves. A11 proves a prime-power sufficient criterion with <2,-1>=units. A12 is an unconditional Lang quotient/Weil incidence test; A13 gives at least four exact-order-4159 theta points on an ordinary curve over F128. A14 limits only eventual success of that sufficient test at one fixed odd prime.

A15 proves the arbitrary odd primitive-factor criterion on rank-one or non-bielliptic genus-two bases, including its rational version. A16 gives a rank-one order-15 example whose cover has genus16 and rank7, primitive rank0 and positive proper-conductor ranks. A17 gives the conditional Hooley–Lenstra family n=3q, q=5 mod8 with 2 primitive, of prime density Artin constant/2. A18 removes the geometric elliptic-double-quotient exception in every genus>=2 in characteristic2: the exceptional pullback forces primitive rank r*phi(n)>0. A19 gives a terminating exact all-exponent search for each finite odd prime support. A20 proves the A09 curve has no nonzero geometric 3-primary theta point, using #J(F_(2^20))=1099812538656, v3=4. All A01–A20 have full proof readings; exact checks are retained. No formal or different-model verification is claimed.

G01–G06 exact effective bounds, actual LM8 elliptic factors, unconditional Lombardo bounds, Bach's corrected coefficient3 theorem, 53 coefficient2 modulus certificates with4825words, and the LLS exp300 threshold are integrated. Coverage:800 complete recovered statements,591 available proof blocks;390 statements and209 LM7 blocks remain unavailable. All supplied flags and recovered rows are represented, without treating availability as proof verification.

## Current package

final/ contains all six required deliverables, standalone TeX, PDF, retained checked section sources, recovered user sources, audits and exact certificates. A12–A20 were recently integrated. Root check events are in final/evidence/root_check_events.json (append; do not rerun the old initial generator). Row agent owns final/reproduce/build_ledgers.py and is regenerating questions/events with A18–A20.

Row agent is compiling the expanded A01–A20 source (62 pages on first build), correcting two long-path overflows and visually reviewing every page. The previous44-page PDF remains a valid older snapshot until the new PDF/manifest is installed; do not claim it matches the expanded source before refreshing. Source is frozen during the build; row may make layout-only canonical edits. Root must refresh the full validation after PDF manifest and tables.

## Active approaches

Effective agent is proving A21: full Sp4(Z_ell) monodromy plus a compact-type ordinary/supersingular elliptic degeneration should extend generic prime-level avoidance to prime powers. Verify irreducibility on a dense smooth tricanonical parameter scheme and all boundary specialization steps. GT will whole-read it. Potential A22: joint finite-level symplectic monodromy and a chosen Frobenius congruence may turn avoidance at N=product S into avoidance of all S-primary theta torsion via A19 with d=1. Not yet proved; do not pre-empt checks.

GT also checked the direct composite Lang-test corollary H=J[3q]. Limited searches did not yet produce a case where that bound succeeds and the pure-q bound fails; do not expand examples indefinitely. Row agent read B28–B29 and recorded the exact prescribed-point obstruction in evidence/B28_B29_POINTING_ROUTE_AUDIT.md.

## Operational details

work/root/create_scheduled_checkpoint.py INDEX enforces the exact45-minute boundaries (up to3minutes late), no early writes, no overwrite and no nestedZIP. It captures final/,work/,source/, this state and the prompt. Complete externally downloaded research papers/text caches are excluded from subsequent snapshots; their hashes and all bibliographic/proof audits remain. Existing checkpoints stay immutable.

Checkpoint01: AN_GRH_checkpoint_01.zip, libfile_760f327eac508191bc1cd08293ecae1c. Checkpoint02: AN_GRH_checkpoint_02.zip, libfile_d6d32e0dffbc8191a57f2c3b6283ecb9, captured01:45:00.636UTC, SHA c7bc236dd2e893c5bf770e3b5279465d0ea178973b5711cb733d2ae4031b9c80. For>=50MiB uploads use the preserved work/library_upload_helpers/library_upload.py helper, which owns transfer/finalize/xattrs. For smaller archives use library_create_library_file and apply returned xattrs with work/library_helpers/library_file_transfer.py in the same code-mode call. Native links require the exact returned library_file_id.

Deliver only one final AN_GRH_final.zip when the work reaches its stopping condition, with a truthful final INCOMPLETE assessment if route2 or source coverage remains unresolved. Do not claim universal theta incidence, erase failed checks, or manufacture scheduled reviews. Masullo-dependent findings remain conditional on his draft claim; intended heading13.3.1.2 is blank.

## Checkpoint03 saved

Captured 2026-11-21 02:32:47.367708 UTC (2m47s after the scheduled02:30 boundary), 863 files,120642680 bytes, SHA25672018d19d09a5fa043d8459871c9015da533ccd2a21d3cd34e79e0535b301b18. Saved successfully as libfile_2361551139e481919e6da1f09cc495d6; local metadata applied by the preserved upload helper. The 62-page visual QA completed just before capture; matched final PDF installation was held until after capture. Row agent is now installing it. Next checkpoint04 due03:15UTC, also first scheduled progress review.

## Update at 02:47 UTC

A21–A23 are proved, fully read, and integrated in final/proof_sources and standalone TeX. A21 uses full joint symplectic monodromy and the translation intersection bound to exclude all odd generic theta torsion in both positive-rank strata; all odd cyclic new factors are ordinary. A22 excludes every nonzero geometric S-primary theta point, with arbitrary exponents and mixed products, on finite-field curves in every nonempty moduli open for every fixed finite odd S. Its explicit level-N² twist realizes rational Sylows J[ell], so A19 applies with d=1. A23 proves the ordinary A13 curve overF4 violates old B.3's size condition at every extension, despite a persisting4159 witness.

Root check events now95. Merged questions1363/events969 after late fragments; reported-review accounts normalize to used/rechecked rather than extra actual proof checks. The currently installed62-page PDF still matches the prior A01–A20 source snapshot; the expanded canonical source awaits a new build. Effective agent will own the next source freeze/build/visual QA once A24 resolves.

GT is writing A24: for the ordinary A13 curve, an eligible prime <2,−1>=U_ell inert in Q(sqrt−15) cannot occur as a theta order. Cayley–Hamilton gives Phi_F4²−Phi_F4+4=0; inert reduction gives Phi^(ell+1)=[4], and symmetry yields a large scalar orbit in one F_ell line, contradicting the Sidon/difference bound. The surviving split-prime family still has positive conditional Hooley–Lenstra density; that is not theta incidence. This result is pending its full written proof and whole-read checks. Row is testing precise primitive-divisor/large-subgroup implications for the distinct A12 Lang criterion. No scheduled progress review has occurred; first is03:15UTC and checkpoint04 due then.

## Pre-review update03:14UTC

Current standalone74-page source/PDF throughA25 passes full structural/build validation. A26 and A27 proof sources are retained in final/proof_sources with root and two same-model reviews; A27 finite checker rerun passes. They await assembly/table integration after checkpoint04. A26 removes a pair-count hypothesis from the rational criterion using even augmentation. A27 supplies rank-one curve overF4 where the size test fails over every extension and primitive2prime. New proposed A28: exploit hyperelliptic involution at a prescribed point to avoid numerical conditions when its branchpoint difference survives a quotient; root further suggests even ord_r(2) may suffice via inverse-character pairing. This is under active proof writing and checking, not yet proved in the package.

## Actual first scheduled review

2026-11-21T03:15:00.023460+00:00: review01 recorded, substantive movement yes, consecutive no-movement count0. All-row and every-gate snapshots retained under final/reviews. Next review04:15UTC; checkpoint04 due now03:15. Standalone source and74-page PDF match throughA25; A26/A27 complete whole-read sources await paper/table integration. Root events101; merged events may grow as final audit fragments arrive. Active next route is rational Fourier existence beyond failed size inequalities.
