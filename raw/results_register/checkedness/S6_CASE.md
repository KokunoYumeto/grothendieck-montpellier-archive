# The S6 case: how often the unrecorded and the credit-pending S6_10 rows have been iterated over

Built 2026-11-18 14:00 UTC by `build_checkedness.py` (script; no model). Written by Claude Opus 5.5 at effort max. The S6_10 intake (`s6_pro_prompts_20261112_work/intake/S6_10_INTAKE_20261118.md`, Claude Opus 5.5 at effort max) found 246 printed rows with no line in CHECK_EVENTS.tsv and 286 rows whose credit comparison is pending. The question here is the user's: are they not checked, and how many times have they been iterated over?

Every count below is per row and comes from `CHECKEDNESS_EVENTS.tsv` (one row per event, with its file). Columns:
- **Checkpoints** = results tables of the source run in which the row stands (each checkpoint we hold; a row of S6_06_BLIND that stood through 17 checkpoints counts 17). These are one Astra instance carrying the row, not separate checks.
- **Runs** = distinct runs that hold the row, re-wrote it or re-derived it: the source run, S6_09_PAPERS, S6_10_PAPERS, and S6_06_BLIND where it re-derived the row blind. All are GPT-6 Astra (ChatGPT Pro mode).
- **S6_10 checks / events** = this writing run's own check events on the row (targeted proof checks, re-proofs, computations, uses), then all its events (editorial reconciliations and alias records included). They come from the inventory's check_record JSON and records/*.tsv, which hold the events CHECK_EVENTS.tsv omits, and are deduplicated against CHECK_EVENTS.tsv.
- **S6_09** = the S6_09 writing check carried in the inventory (GPT-6 Astra (ChatGPT Pro mode), 17 Nov: whole statement and proof read, proof re-derived).
- **Blind** = S6_06_BLIND rows that re-derived the row's stated value without its proof (one per run).
- **Claude docs (checks)** = distinct Claude documents (intakes, reviews, referee reports, expert notes) that name the row, then those whose line about it records a check or re-derivation.

## The printed rows with no line in CHECK_EVENTS.tsv (246)

- By paper: II 104, IV 120, VI 22; main rows: 13.
- **They are checked in S6_10 itself:** 244 of the 246 rows have at least one S6_10 check event of their own outside CHECK_EVENTS.tsv; 2 have none. Their S6_10 events by type: targeted proof check 213, computation 99, independent re-proof 65, editorial or alias record 19, other 3, used and rechecked 2, source check 1.
- Earlier iterations: an S6_09 writing check on 133 rows; a blind re-derivation on 20; a Claude document names 142 (and records a check or re-derivation of 6).
- Checkpoints of the source run in which the row stands: median 10; runs that hold or re-derived it: 1 runs: 2 rows, 2 runs: 147 rows, 3 runs: 72 rows, 4 runs: 18 rows, 5 runs: 7 rows.
- Real checks per row (all sources): median 2, maximum 15; rows with none: 1.

| Label | Paper | Main | Source run | Status | Checkpoints | Runs | S6_10 checks / events | S6_09 | Blind | Claude docs (checks) | Real checks | Strongest |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `night:P3K.36` | II | main | S6_06_BLIND | Refuted | 16 | 2 | 0 / 1 | 0 | 0 | 2 (0) | 0 | read in an intake (register level, not a proof check) |
| `inv:wb:uniform-nontorsion-provenance` | II |  |  | Proved | 0 | 2 | 0 / 1 | 1 | 0 | 0 (0) | 1 | targeted proof check (in its own run) |
| `night:P4.10` | II |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.12` | II |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.14` | II |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.15` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.16` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.17` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.18` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.2` | II |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.21` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.22` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.23` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.27` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.28` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.3` | II |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.30` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.31` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.5` | II |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.9` | II |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.1` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.2` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.3` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.4` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.5` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.6` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `cdp:st:C4g` | II |  | S6_03_CDP | Proved | 9 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C5a` | II |  | S6_03_CDP | Proved | 9 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C5c` | II |  | S6_03_CDP | Proved | 9 | 3 | 1 / 1 | 1 | 0 | 2 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:D.1.10` | II |  | S6_03_CDP | Proved | 9 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:D.1.13` | II |  | S6_03_CDP | Proved | 9 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:D.1.15` | II |  | S6_03_CDP | Proved | 9 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:D.1.6` | II |  | S6_03_CDP | Proved | 9 | 3 | 1 / 1 | 1 | 0 | 2 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:E10` | II |  | S6_03_CDP | Proved | 9 | 3 | 1 / 1 | 1 | 0 | 2 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:E11` | II |  | S6_03_CDP | Proved | 9 | 3 | 1 / 1 | 1 | 0 | 3 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:E5` | II |  | S6_03_CDP | Proved | 9 | 3 | 1 / 1 | 1 | 0 | 5 (0) | 2 | targeted proof check (by a later run) |
| `inv:E2.2` | II |  | S6_01_INVARIANTS | Proved | 1 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `inv:E2.4` | II | main | S6_01_INVARIANTS | Proved | 1 | 3 | 1 / 1 | 1 | 0 | 3 (0) | 2 | targeted proof check (by a later run) |
| `night:P4.38` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.39` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.4` | II |  | S6_06_BLIND | Proved | 17 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P4.40` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.41` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.42` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.43` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.44` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.45` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.46` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.47` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.48` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.49` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.50` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4R.10` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4R.11` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4R.12` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4R.14` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4R.15` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4R.16` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4R.17` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `push:src:E.5.2` | II |  | S6_02_PUSH | Proved | 10 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `push:src:E.5.3` | II |  | S6_02_PUSH | Proved | 10 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `wb:thm:uniform-nontorsion-audit` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:cor:candidate-conductor-actual` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:cor:candidate-pic0-route` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:cor:normal-crossing-kernel` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:cor:surface-top-base-change` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:lem:analytic-support-specialization` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:lem:cdp-generic-endpoints` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:lem:curve-flatness` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:lem:extending-gluing` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:lem:generic-endpoints` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:lem:gluing-bundle` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:lem:picard-crossed-defect` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:lem:picard-cusp-defect` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:lem:picard-finite-norm` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:lem:torsion-identification` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:prop:all-pic-restriction` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:prop:analytic-ah-boundary` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:prop:analytic-base-change` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:prop:cartier-duality-absolute` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:prop:direct-boundary-picard` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:prop:leray-edge-restriction` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:prop:local-cusp-picard-obstruction` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:prop:pic0-pullback` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:prop:relative-local` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:test:cdp-comparison` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:thm:analytic-all-picard` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:thm:candidate-conductor` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:thm:cartier-duality` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `wbII:thm:corrected-cdp-fibrewise` | II |  |  | Proved | 0 | 2 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `push:src:E.5.1` | II |  | S6_02_PUSH | Proved | 10 | 3 | 1 / 1 | 1 | 0 | 4 (1) | 3 | targeted proof check (by Claude) |
| `wbII:cor:corrected-cdp-relative` | II |  |  | Proved | 0 | 2 | 1 / 2 | 2 | 0 | 0 (0) | 3 | targeted proof check (by a later run) |
| `wbII:cor:relative` | II |  |  | Proved | 0 | 2 | 1 / 2 | 2 | 0 | 0 (0) | 3 | targeted proof check (by a later run) |
| `wbII:prop:conductor` | II |  |  | Proved | 0 | 2 | 1 / 2 | 2 | 0 | 0 (0) | 3 | targeted proof check (by a later run) |
| `wbII:prop:conductor-differential` | II |  |  | Proved | 0 | 2 | 1 / 2 | 2 | 0 | 0 (0) | 3 | targeted proof check (by a later run) |
| `wbII:thm:corrected-cdp-global` | II |  |  | Proved | 0 | 2 | 1 / 2 | 2 | 0 | 0 (0) | 3 | targeted proof check (by a later run) |
| `wbII:thm:corrected-global` | II |  |  | Proved | 0 | 2 | 1 / 2 | 2 | 0 | 0 (0) | 3 | targeted proof check (by a later run) |
| `night:P4.1` | II |  | S6_03_CDP, S6_06_BLIND | Proved | 26 | 4 | 2 / 2 | 1 | 1 | 8 (0) | 4 | targeted proof check (by a later run) |
| `night:P4.6` | II |  | S6_03_CDP, S6_06_BLIND | Proved | 26 | 4 | 2 / 2 | 1 | 1 | 2 (0) | 4 | targeted proof check (by a later run) |
| `night:P4.7` | II |  | S6_03_CDP, S6_06_BLIND | Proved | 26 | 4 | 2 / 2 | 1 | 1 | 2 (0) | 4 | targeted proof check (by a later run) |
| `night:P4.8` | II |  | S6_03_CDP, S6_06_BLIND | Proved | 26 | 4 | 2 / 2 | 1 | 1 | 2 (0) | 4 | targeted proof check (by a later run) |
| `wbII:lem:conductor` | II |  | S6_03_CDP | Proved | 9 | 3 | 1 / 3 | 3 | 0 | 1 (0) | 4 | targeted proof check (by a later run) |
| `wbII:lem:conductor-square` | II |  | S6_03_CDP | Proved | 9 | 3 | 1 / 3 | 3 | 0 | 1 (0) | 4 | targeted proof check (by a later run) |
| `cdp:st:E8` | II |  | S6_01_INVARIANTS, S6_02_FAMILY, S6_03_CDP | Proved | 12 | 5 | 3 / 3 | 3 | 0 | 4 (2) | 8 | targeted proof check (by Claude) |
| `night:P3F.18` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.30` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.35` | IV | main | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.44` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | independent re-proof |
| `night:P3F.52` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 2 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.108` | IV | main | S6_06_BLIND | Proved | 3 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.12` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.13` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 3 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.14` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 2 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.15` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 2 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.16` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 2 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.18` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.19` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.20` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | independent re-proof |
| `maps:src:B.6.13` | IV |  | S6_04_MAPS_MANIFOLDS | Proved | 7 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `maps:src:B.6.14` | IV |  | S6_04_MAPS_MANIFOLDS | Proved | 7 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `maps:src:B.6.15` | IV |  | S6_04_MAPS_MANIFOLDS | Proved | 7 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `maps:src:B.6.16` | IV |  | S6_04_MAPS_MANIFOLDS | Proved | 6 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `maps:src:B.6.18` | IV |  | S6_04_MAPS_MANIFOLDS | Proved | 6 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `maps:src:B.6.19` | IV |  | S6_04_MAPS_MANIFOLDS | Proved | 6 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `maps:src:B.6.22` | IV |  | S6_04_MAPS_MANIFOLDS | Proved | 5 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `maps:src:B.6.23` | IV |  | S6_04_MAPS_MANIFOLDS | Proved | 5 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `maps:src:B.6.5` | IV |  | S6_04_MAPS_MANIFOLDS | Proved | 8 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.19` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.20` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.23` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.36` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.37` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.38` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.39` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.40` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.41` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.42` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P3F.43` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P3F.45` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P3F.46` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.47` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.48` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.49` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.50` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.51` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.54` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.55` | IV |  | S6_06_BLIND | Proved | 15 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.56` | IV |  | S6_06_BLIND | Proved | 15 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.104` | IV | main | S6_06_BLIND | Proved | 3 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.105` | IV | main | S6_06_BLIND | Proved | 3 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.21` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.26` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P3K.28` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P3K.38` | IV |  | S6_06_BLIND | Proved | 15 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P3K.42` | IV |  | S6_06_BLIND | Proved | 14 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.47` | IV |  | S6_06_BLIND | Proved | 13 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.48` | IV |  | S6_06_BLIND | Proved | 13 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.49` | IV |  | S6_06_BLIND | Proved | 13 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.51` | IV |  | S6_06_BLIND | Proved | 13 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.53` | IV |  | S6_06_BLIND | Proved | 13 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.67` | IV |  | S6_06_BLIND | Proved | 12 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.70` | IV |  | S6_06_BLIND | Proved | 12 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.75` | IV |  | S6_06_BLIND | Open | 12 | 2 | 2 / 3 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.76` | IV |  | S6_06_BLIND | Proved | 11 | 2 | 2 / 3 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.78` | IV |  | S6_06_BLIND | Proved | 10 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.81` | IV |  | S6_06_BLIND | Proved | 9 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.82` | IV |  | S6_06_BLIND | Proved | 9 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.83` | IV |  | S6_06_BLIND | Proved | 9 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.84` | IV |  | S6_06_BLIND | Proved | 9 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.85` | IV |  | S6_06_BLIND | Proved | 8 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.87` | IV |  | S6_06_BLIND | Proved | 8 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.91` | IV |  | S6_06_BLIND | Proved | 8 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `push:src:C.2.2` | IV |  | S6_02_PUSH | Proved | 9 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `push:src:C.2.3` | IV |  | S6_02_PUSH | Proved | 9 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `push:src:C.3.14` | IV |  | S6_02_PUSH | Proved | 8 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `push:src:C.3.16` | IV |  | S6_02_PUSH | Proved | 7 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `push:src:C.3.17` | IV |  | S6_02_PUSH | Proved | 7 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `push:src:C.3.18` | IV |  | S6_02_PUSH | Proved | 7 | 3 | 1 / 1 | 1 | 0 | 2 (0) | 2 | targeted proof check (by a later run) |
| `push:src:C.3.19` | IV |  | S6_02_PUSH | Proved | 7 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `push:src:C.3.2` | IV |  | S6_02_PUSH | Proved | 10 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `push:src:C.3.20` | IV |  | S6_02_PUSH | Proved | 7 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `push:src:C.3.23` | IV |  | S6_02_PUSH | Proved | 6 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `push:src:C.3.25` | IV |  | S6_02_PUSH | Proved | 6 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `push:src:C.3.6` | IV |  | S6_02_PUSH | Proved | 9 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `push:src:C.3.7` | IV |  | S6_02_PUSH | Proved | 9 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `push:src:C.3.8` | IV |  | S6_02_PUSH | Proved | 8 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `push:src:C.3.9` | IV |  | S6_02_PUSH | Proved | 8 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `push:src:C.4.2` | IV |  | S6_02_PUSH | Proved | 10 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `push:src:C.5.1` | IV |  | S6_02_PUSH | Proved | 10 | 3 | 1 / 1 | 1 | 0 | 3 (0) | 2 | targeted proof check (by a later run) |
| `fam:src:E.2.3` | IV |  | S6_02_FAMILY | Proved | 2 | 3 | 2 / 2 | 1 | 0 | 2 (0) | 3 | targeted proof check (by a later run) |
| `iv:i3_all_reduced_caps` | IV | main |  | Proved | 0 | 1 | 3 / 3 | 0 | 0 | 1 (0) | 3 | targeted proof check (in its own run) |
| `iv:rank_two_specialization` | IV |  |  | Proved | 0 | 1 | 3 / 3 | 0 | 0 | 0 (0) | 3 | targeted proof check (in its own run) |
| `maps:src:B.6.10` | IV |  | S6_04_MAPS_MANIFOLDS | Proved | 7 | 4 | 2 / 2 | 1 | 1 | 1 (0) | 3 | targeted proof check (by a later run) |
| `maps:src:B.6.11` | IV |  | S6_04_MAPS_MANIFOLDS | Proved | 7 | 3 | 2 / 2 | 1 | 0 | 1 (0) | 3 | targeted proof check (by a later run) |
| `maps:src:B.6.12` | IV |  | S6_04_MAPS_MANIFOLDS | Proved | 7 | 3 | 2 / 2 | 1 | 0 | 1 (0) | 3 | targeted proof check (by a later run) |
| `maps:src:B.6.17` | IV |  | S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 18 | 4 | 2 / 2 | 1 | 1 | 2 (0) | 3 | targeted proof check (by a later run) |
| `maps:src:B.6.20` | IV |  | S6_04_MAPS_MANIFOLDS | Proved | 6 | 4 | 1 / 1 | 1 | 1 | 2 (1) | 3 | targeted proof check (by a later run) |
| `maps:src:B.6.24` | IV | main | S6_04_MAPS_MANIFOLDS | Proved | 5 | 4 | 1 / 1 | 1 | 1 | 4 (0) | 3 | targeted proof check (by a later run) |
| `maps:src:B.6.6` | IV |  | S6_04_MAPS_MANIFOLDS | Proved | 8 | 3 | 2 / 2 | 1 | 0 | 1 (0) | 3 | targeted proof check (by a later run) |
| `maps:src:B.6.7` | IV |  | S6_04_MAPS_MANIFOLDS | Proved | 8 | 3 | 2 / 2 | 1 | 0 | 1 (0) | 3 | targeted proof check (by a later run) |
| `maps:src:B.6.8` | IV |  | S6_04_MAPS_MANIFOLDS | Proved | 8 | 3 | 2 / 2 | 1 | 0 | 1 (0) | 3 | targeted proof check (by a later run) |
| `night:P3F.21` | IV | main | S6_06_BLIND | Proved | 16 | 2 | 3 / 3 | 0 | 0 | 1 (0) | 3 | targeted proof check (by a later run) |
| `night:P3K.106` | IV | main | S6_06_BLIND | Proved | 3 | 2 | 3 / 3 | 0 | 0 | 1 (0) | 3 | targeted proof check (by a later run) |
| `night:P3K.79` | IV |  | S6_06_BLIND | Proved | 9 | 2 | 3 / 3 | 0 | 0 | 0 (0) | 3 | targeted proof check (by a later run) |
| `night:P3R.1` | IV |  | S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 24 | 4 | 1 / 2 | 1 | 1 | 1 (0) | 3 | targeted proof check (by a later run) |
| `push:src:C.3.15` | IV |  | S6_02_PUSH, S6_06_BLIND | Proved | 24 | 4 | 2 / 2 | 1 | 0 | 3 (0) | 3 | targeted proof check (by a later run) |
| `push:src:C.3.22` | IV |  | S6_02_PUSH | Proved | 6 | 3 | 1 / 1 | 1 | 0 | 2 (1) | 3 | targeted proof check (by a later run) |
| `maps:src:B.6.2` | IV |  | S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 26 | 4 | 2 / 2 | 1 | 1 | 0 (0) | 4 | targeted proof check (by a later run) |
| `night:P3K.107` | IV | main | S6_06_BLIND | Proved | 3 | 2 | 4 / 4 | 0 | 0 | 1 (0) | 4 | independent re-proof |
| `night:P3K.77` | IV |  | S6_06_BLIND | Proved | 10 | 2 | 4 / 4 | 0 | 0 | 0 (0) | 4 | targeted proof check (by a later run) |
| `push:src:C.3.11` | IV |  | S6_02_PUSH, S6_06_BLIND | Proved | 24 | 4 | 2 / 2 | 1 | 1 | 1 (0) | 4 | targeted proof check (by a later run) |
| `push:src:C.3.12` | IV |  | S6_02_PUSH, S6_04_MAPS_MANIFOLDS | Proved | 18 | 4 | 2 / 2 | 2 | 0 | 1 (0) | 4 | targeted proof check (by a later run) |
| `push:src:C.3.13` | IV |  | S6_02_PUSH, S6_04_MAPS_MANIFOLDS | Proved | 18 | 4 | 2 / 2 | 2 | 0 | 0 (0) | 4 | targeted proof check (by a later run) |
| `push:src:C.3.21` | IV |  | S6_02_PUSH, S6_06_BLIND | Proved | 22 | 4 | 2 / 2 | 1 | 1 | 4 (0) | 4 | targeted proof check (by a later run) |
| `push:src:C.3.26` | IV |  | S6_02_PUSH, S6_06_BLIND | Proved | 22 | 4 | 2 / 2 | 1 | 1 | 2 (0) | 4 | targeted proof check (by a later run) |
| `push:src:C.3.27` | IV | main | S6_02_PUSH, S6_06_BLIND | Proved | 22 | 4 | 3 / 3 | 1 | 0 | 3 (0) | 4 | targeted proof check (by a later run) |
| `push:src:C.3.10` | IV |  | S6_02_PUSH, S6_06_BLIND | Proved | 24 | 4 | 3 / 3 | 1 | 1 | 2 (0) | 5 | targeted proof check (by a later run) |
| `maps:src:B.6.25` | IV |  | S6_02_PUSH, S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 27 | 5 | 3 / 3 | 2 | 1 | 4 (0) | 6 | targeted proof check (by a later run) |
| `push:src:C.3.24` | IV | main | S6_02_PUSH, S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 27 | 5 | 3 / 3 | 2 | 1 | 4 (0) | 6 | targeted proof check (by a later run) |
| `maps:src:B.6.21` | IV |  | S6_02_PUSH, S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Refuted | 32 | 5 | 4 / 5 | 2 | 1 | 4 (0) | 7 | targeted proof check (by a later run) |
| `push:src:C.4.1` | IV |  | S6_02_PUSH, S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Refuted | 32 | 5 | 4 / 5 | 2 | 1 | 4 (0) | 7 | targeted proof check (by a later run) |
| `night:P3R.2` | IV |  | S6_02_PUSH, S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 36 | 5 | 3 / 3 | 2 | 1 | 3 (1) | 8 | targeted proof check (by a later run) |
| `push:src:C.3.4` | IV |  | S6_02_PUSH, S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 36 | 5 | 3 / 3 | 2 | 1 | 3 (1) | 8 | targeted proof check (by a later run) |
| `night:P3K.80` | IV |  | S6_06_BLIND | Proved | 9 | 2 | 15 / 15 | 0 | 0 | 0 (0) | 15 | independent re-proof |
| `cdp:st:C.2.UN.67` | VI |  | S6_03_CDP | Proved | 3 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.68` | VI |  | S6_03_CDP | Proved | 3 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.69` | VI |  | S6_03_CDP | Proved | 3 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.70` | VI |  | S6_03_CDP | Proved | 3 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.71` | VI |  | S6_03_CDP | Proved | 3 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.72` | VI |  | S6_03_CDP | Proved | 2 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.73` | VI |  | S6_03_CDP | Proved | 2 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.74` | VI |  | S6_03_CDP | Proved | 2 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.75` | VI |  | S6_03_CDP | Proved | 2 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.76` | VI |  | S6_03_CDP | Proved | 2 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.77` | VI |  | S6_03_CDP | Proved | 2 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.78` | VI |  | S6_03_CDP | Proved | 2 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.79` | VI |  | S6_03_CDP | Proved | 1 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.80` | VI |  | S6_03_CDP | Proved | 1 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.81` | VI |  | S6_03_CDP | Proved | 1 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.82` | VI |  | S6_03_CDP | Proved | 1 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.83` | VI |  | S6_03_CDP | Proved | 1 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.84` | VI |  | S6_03_CDP | Proved | 1 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.85` | VI |  | S6_03_CDP | Proved | 1 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.UN.86` | VI |  | S6_03_CDP | Proved | 1 | 3 | 1 / 1 | 1 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.VII.3` | VI |  | S6_03_CDP | Proved | 9 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `cdp:st:C.2.VII.4` | VI |  | S6_03_CDP | Proved | 9 | 3 | 1 / 1 | 1 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |

## The rows awaiting the credit comparison (286)

- By paper: I 18, II 79, III 10, IV 151, V 28; main rows: 31.
- **They are checked in S6_10 itself:** 283 of the 286 rows have at least one S6_10 check event of their own outside CHECK_EVENTS.tsv; 3 have none. Their S6_10 events by type: targeted proof check 285, computation 165, independent re-proof 49, editorial or alias record 48, used and rechecked 6, other 4, source check 3.
- Earlier iterations: an S6_09 writing check on 38 rows; a blind re-derivation on 31; a Claude document names 203 (and records a check or re-derivation of 16).
- Checkpoints of the source run in which the row stands: median 16; runs that hold or re-derived it: 1 runs: 3 rows, 2 runs: 244 rows, 3 runs: 1 rows, 4 runs: 34 rows, 5 runs: 3 rows, 6 runs: 1 rows.
- Real checks per row (all sources): median 2, maximum 15; rows with none: 3.

| Label | Paper | Main | Source run | Status | Checkpoints | Runs | S6_10 checks / events | S6_09 | Blind | Claude docs (checks) | Real checks | Strongest |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `night:P5.7` | I |  | S6_06_BLIND | Known | 16 | 2 | 0 / 0 | 0 | 0 | 1 (0) | 0 | read in an intake (register level, not a proof check) |
| `night:P2.5` | I |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P2.8` | I |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P2.9` | I | main | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P5.1` | I |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P5.2` | I |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P5.4` | I |  | S6_01_INVARIANTS, S6_06_BLIND | Proved | 18 | 3 | 1 / 1 | 0 | 0 | 2 (0) | 1 | targeted proof check (by a later run) |
| `night:P2.2` | I | main | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 2 (1) | 2 | targeted proof check (by Claude) |
| `night:P2.10` | I |  | S6_02_PUSH, S6_06_BLIND | Proved | 27 | 4 | 2 / 2 | 1 | 0 | 3 (0) | 3 | targeted proof check (by a later run) |
| `night:P2.1` | I |  | S6_02_PUSH, S6_06_BLIND | Proved | 21 | 4 | 2 / 2 | 1 | 1 | 2 (0) | 4 | targeted proof check (by a later run) |
| `night:P2.3` | I |  | S6_02_PUSH, S6_06_BLIND | Proved | 27 | 4 | 2 / 2 | 1 | 1 | 4 (0) | 4 | targeted proof check (by a later run) |
| `night:P2.4` | I |  | S6_02_PUSH, S6_06_BLIND | Proved | 18 | 4 | 2 / 3 | 1 | 1 | 3 (0) | 4 | targeted proof check (by a later run) |
| `night:P2.6` | I |  | S6_02_PUSH, S6_06_BLIND | Proved | 18 | 4 | 2 / 2 | 1 | 1 | 2 (0) | 4 | targeted proof check (by a later run) |
| `night:P2.7` | I | main | S6_02_PUSH, S6_06_BLIND | Proved | 18 | 4 | 2 / 3 | 1 | 1 | 5 (0) | 4 | targeted proof check (by a later run) |
| `night:P2.11` | I |  | S6_02_PUSH, S6_06_BLIND | Refuted | 27 | 4 | 3 / 3 | 1 | 1 | 5 (0) | 5 | targeted proof check (by a later run) |
| `night:P5.5` | I |  | S6_02_FAMILY, S6_06_BLIND | Proved | 19 | 4 | 4 / 4 | 1 | 0 | 5 (2) | 7 | targeted proof check (by Claude) |
| `night:P5.3` | I |  | S6_01_INVARIANTS, S6_02_FAMILY, S6_03_CDP, S6_06_BLIND | Proved | 29 | 6 | 6 / 6 | 2 | 0 | 9 (2) | 8 | targeted proof check (by Claude) |
| `night:P5.6` | I |  | S6_02_FAMILY, S6_06_BLIND | Proved | 19 | 4 | 4 / 4 | 2 | 0 | 5 (3) | 9 | targeted proof check (by Claude) |
| `night:P3K.36` | II | main | S6_06_BLIND | Refuted | 16 | 2 | 0 / 1 | 0 | 0 | 2 (0) | 0 | read in an intake (register level, not a proof check) |
| `night:P4.10` | II |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.11` | II |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.12` | II |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.13` | II |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.14` | II |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.15` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.16` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.17` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.18` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.19` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.2` | II |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.20` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.21` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.22` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.23` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.24` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.25` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.26` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.27` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.28` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.29` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.3` | II |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.30` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.31` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.32` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.33` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.34` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.35` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.36` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.37` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.5` | II |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.51` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.52` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.53` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.54` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.55` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.56` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.57` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.58` | II | main | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 2 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.9` | II |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.1` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.13` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.18` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.19` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.2` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.20` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.3` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.4` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.5` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.6` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.7` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.8` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4R.9` | II |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P4.38` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.39` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.4` | II |  | S6_06_BLIND | Proved | 17 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P4.40` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.41` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.42` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.43` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.44` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.45` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.46` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.47` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.48` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.49` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.50` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4R.10` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4R.11` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4R.12` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4R.14` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4R.15` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4R.16` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4R.17` | II |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P4.1` | II |  | S6_03_CDP, S6_06_BLIND | Proved | 26 | 4 | 2 / 2 | 1 | 1 | 8 (0) | 4 | targeted proof check (by a later run) |
| `night:P4.6` | II |  | S6_03_CDP, S6_06_BLIND | Proved | 26 | 4 | 2 / 2 | 1 | 1 | 2 (0) | 4 | targeted proof check (by a later run) |
| `night:P4.7` | II |  | S6_03_CDP, S6_06_BLIND | Proved | 26 | 4 | 2 / 2 | 1 | 1 | 2 (0) | 4 | targeted proof check (by a later run) |
| `night:P4.8` | II |  | S6_03_CDP, S6_06_BLIND | Proved | 26 | 4 | 2 / 2 | 1 | 1 | 2 (0) | 4 | targeted proof check (by a later run) |
| `mapsIII:carrier-three-complex-wedge` | III |  |  | Proved | 0 | 1 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (in its own run) |
| `mapsaudit:finite-degree-three` | III |  |  | Proved | 0 | 1 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (in its own run) |
| `night:P3F.26` | III |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.27` | III |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.28` | III |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.29` | III |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.31` | III |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.32` | III |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.33` | III |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 2 (1) | 2 | targeted proof check (by Claude) |
| `night:P3F.34` | III | main | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 3 (1) | 2 | targeted proof check (by a later run) |
| `night:P3F.14` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.16` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.18` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.22` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.3` | IV |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.30` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.35` | IV | main | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.4` | IV |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.44` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | independent re-proof |
| `night:P3F.5` | IV |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.52` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 2 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.6` | IV |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.7` | IV |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.8` | IV |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.1` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.12` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.13` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 3 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.14` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 2 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.15` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 2 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.16` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 2 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.18` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.19` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.2` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.20` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | independent re-proof |
| `night:P3K.23` | IV | main | S6_06_BLIND | Refuted | 16 | 2 | 1 / 2 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.3` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.31` | IV | main | S6_06_BLIND | Refuted | 16 | 2 | 1 / 2 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.33` | IV | main | S6_06_BLIND | Refuted | 16 | 2 | 1 / 2 | 0 | 0 | 2 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.34` | IV |  | S6_06_BLIND | Refuted | 16 | 2 | 1 / 2 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.5` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.6` | IV |  | S6_06_BLIND | Refuted | 16 | 2 | 1 / 2 | 0 | 0 | 2 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.61` | IV |  | S6_06_BLIND | Proved | 13 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.62` | IV |  | S6_06_BLIND | Proved | 13 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.63` | IV |  | S6_06_BLIND | Proved | 13 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.64` | IV |  | S6_06_BLIND | Proved | 12 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.65` | IV |  | S6_06_BLIND | Proved | 12 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.72` | IV |  | S6_06_BLIND | Proved | 12 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3K.92` | IV |  | S6_06_BLIND | Proved | 7 | 2 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (by a later run) |
| `night:P3F.12` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.15` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.2` | IV |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 2 (1) | 2 | targeted proof check (by a later run) |
| `night:P3F.23` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.36` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.37` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.38` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.39` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.40` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.41` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.42` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P3F.43` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P3F.45` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P3F.46` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.47` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.48` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.49` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.50` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.51` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.53` | IV | main | S6_06_BLIND | Refuted | 16 | 2 | 2 / 4 | 0 | 0 | 2 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.54` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.55` | IV |  | S6_06_BLIND | Proved | 15 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.56` | IV |  | S6_06_BLIND | Proved | 15 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.10` | IV | main | S6_06_BLIND | Refuted | 16 | 2 | 2 / 3 | 0 | 0 | 2 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.100` | IV | main | S6_06_BLIND | Proved | 4 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.101` | IV | main | S6_06_BLIND | Proved | 3 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.102` | IV | main | S6_06_BLIND | Proved | 3 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.103` | IV | main | S6_06_BLIND | Proved | 3 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.104` | IV | main | S6_06_BLIND | Proved | 3 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.105` | IV | main | S6_06_BLIND | Proved | 3 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.17` | IV |  | S6_06_BLIND | Refuted | 16 | 2 | 2 / 4 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.21` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.22` | IV | main | S6_06_BLIND | Refuted | 16 | 2 | 2 / 5 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.24` | IV |  | S6_06_BLIND | Refuted | 16 | 2 | 2 / 3 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P3K.25` | IV |  | S6_06_BLIND | Refuted | 16 | 2 | 2 / 3 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P3K.26` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P3K.27` | IV |  | S6_06_BLIND | Refuted | 16 | 2 | 2 / 3 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P3K.28` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P3K.29` | IV |  | S6_06_BLIND | Refuted | 16 | 2 | 2 / 3 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P3K.32` | IV |  | S6_06_BLIND | Refuted | 16 | 2 | 2 / 3 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.38` | IV |  | S6_06_BLIND | Proved | 15 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | independent re-proof |
| `night:P3K.4` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.40` | IV |  | S6_06_BLIND | Refuted | 14 | 2 | 2 / 4 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.42` | IV |  | S6_06_BLIND | Proved | 14 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.43` | IV |  | S6_06_BLIND | Refuted | 14 | 2 | 2 / 4 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.44` | IV |  | S6_06_BLIND | Refuted | 14 | 2 | 2 / 4 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.45` | IV |  | S6_06_BLIND | Refuted | 14 | 2 | 2 / 3 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.46` | IV |  | S6_06_BLIND | Refuted | 13 | 2 | 2 / 4 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.47` | IV |  | S6_06_BLIND | Proved | 13 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.48` | IV |  | S6_06_BLIND | Proved | 13 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.49` | IV |  | S6_06_BLIND | Proved | 13 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.51` | IV |  | S6_06_BLIND | Proved | 13 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.53` | IV |  | S6_06_BLIND | Proved | 13 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.55` | IV |  | S6_06_BLIND | Proved | 13 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.66` | IV |  | S6_06_BLIND | Proved | 12 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.67` | IV |  | S6_06_BLIND | Proved | 12 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.70` | IV |  | S6_06_BLIND | Proved | 12 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.71` | IV |  | S6_06_BLIND | Proved | 12 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.73` | IV |  | S6_06_BLIND | Proved | 12 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.74` | IV |  | S6_06_BLIND | Proved | 12 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.75` | IV |  | S6_06_BLIND | Open | 12 | 2 | 2 / 3 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.76` | IV |  | S6_06_BLIND | Proved | 11 | 2 | 2 / 3 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.78` | IV |  | S6_06_BLIND | Proved | 10 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.81` | IV |  | S6_06_BLIND | Proved | 9 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.82` | IV |  | S6_06_BLIND | Proved | 9 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.83` | IV |  | S6_06_BLIND | Proved | 9 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.84` | IV |  | S6_06_BLIND | Proved | 9 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.85` | IV |  | S6_06_BLIND | Proved | 8 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.86` | IV |  | S6_06_BLIND | Proved | 8 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.87` | IV |  | S6_06_BLIND | Proved | 8 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.88` | IV |  | S6_06_BLIND | Proved | 8 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.89` | IV |  | S6_06_BLIND | Proved | 8 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.9` | IV |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.90` | IV |  | S6_06_BLIND | Proved | 8 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.91` | IV |  | S6_06_BLIND | Proved | 8 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | independent re-proof |
| `night:P3K.93` | IV |  | S6_06_BLIND | Proved | 7 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.94` | IV |  | S6_06_BLIND | Proved | 7 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.95` | IV |  | S6_06_BLIND | Proved | 6 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.96` | IV |  | S6_06_BLIND | Proved | 6 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.97` | IV |  | S6_06_BLIND | Proved | 6 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.98` | IV |  | S6_06_BLIND | Proved | 5 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3K.99` | IV | main | S6_06_BLIND | Proved | 4 | 2 | 2 / 2 | 0 | 0 | 0 (0) | 2 | targeted proof check (by a later run) |
| `night:P3F.21` | IV | main | S6_06_BLIND | Proved | 16 | 2 | 3 / 3 | 0 | 0 | 1 (0) | 3 | targeted proof check (by a later run) |
| `night:P3K.30` | IV | main | S6_06_BLIND | Refuted | 16 | 2 | 3 / 4 | 0 | 0 | 1 (0) | 3 | independent re-proof |
| `night:P3K.35` | IV |  | S6_06_BLIND | Refuted | 16 | 2 | 3 / 4 | 0 | 0 | 1 (0) | 3 | targeted proof check (by a later run) |
| `night:P3K.37` | IV |  | S6_06_BLIND | Refuted | 15 | 2 | 3 / 4 | 0 | 0 | 2 (0) | 3 | targeted proof check (by a later run) |
| `night:P3K.41` | IV |  | S6_06_BLIND | Refuted | 14 | 2 | 3 / 5 | 0 | 0 | 0 (0) | 3 | targeted proof check (by a later run) |
| `night:P3K.58` | IV |  | S6_06_BLIND | Refuted | 13 | 2 | 3 / 4 | 0 | 0 | 0 (0) | 3 | targeted proof check (by a later run) |
| `night:P3K.60` | IV |  | S6_06_BLIND | Refuted | 13 | 2 | 3 / 5 | 0 | 0 | 0 (0) | 3 | targeted proof check (by a later run) |
| `night:P3K.68` | IV |  | S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 18 | 4 | 2 / 2 | 1 | 1 | 2 (0) | 3 | targeted proof check (by a later run) |
| `night:P3K.69` | IV |  | S6_06_BLIND | Proved | 12 | 2 | 1 / 1 | 0 | 0 | 2 (2) | 3 | targeted proof check (by Claude) |
| `night:P3K.7` | IV |  | S6_02_PUSH, S6_06_BLIND | Proved | 24 | 4 | 2 / 2 | 1 | 0 | 3 (0) | 3 | targeted proof check (by a later run) |
| `night:P3K.79` | IV |  | S6_06_BLIND | Proved | 9 | 2 | 3 / 3 | 0 | 0 | 0 (0) | 3 | targeted proof check (by a later run) |
| `night:P3R.1` | IV |  | S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 24 | 4 | 1 / 2 | 1 | 1 | 1 (0) | 3 | targeted proof check (by a later run) |
| `night:P3F.10` | IV |  | S6_02_PUSH, S6_06_BLIND | Proved | 22 | 4 | 2 / 2 | 1 | 1 | 4 (0) | 4 | targeted proof check (by a later run) |
| `night:P3F.11` | IV |  | S6_02_PUSH, S6_06_BLIND | Proved | 22 | 4 | 2 / 2 | 1 | 1 | 2 (0) | 4 | targeted proof check (by a later run) |
| `night:P3F.17` | IV |  | S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 26 | 4 | 2 / 2 | 1 | 1 | 0 (0) | 4 | targeted proof check (by a later run) |
| `night:P3F.9` | IV |  | S6_02_PUSH, S6_06_BLIND | Proved | 24 | 4 | 2 / 2 | 1 | 1 | 1 (0) | 4 | targeted proof check (by a later run) |
| `night:P3K.50` | IV |  | S6_06_BLIND | Refuted | 13 | 2 | 4 / 5 | 0 | 0 | 0 (0) | 4 | targeted proof check (by a later run) |
| `night:P3K.52` | IV |  | S6_06_BLIND | Refuted | 13 | 2 | 4 / 5 | 0 | 0 | 0 (0) | 4 | targeted proof check (by a later run) |
| `night:P3K.54` | IV |  | S6_06_BLIND | Refuted | 13 | 2 | 4 / 5 | 0 | 0 | 0 (0) | 4 | targeted proof check (by a later run) |
| `night:P3K.56` | IV |  | S6_06_BLIND | Refuted | 13 | 2 | 4 / 5 | 0 | 0 | 0 (0) | 4 | targeted proof check (by a later run) |
| `night:P3K.59` | IV |  | S6_06_BLIND | Refuted | 13 | 2 | 4 / 5 | 0 | 0 | 0 (0) | 4 | targeted proof check (by a later run) |
| `night:P3K.77` | IV |  | S6_06_BLIND | Proved | 10 | 2 | 4 / 4 | 0 | 0 | 0 (0) | 4 | targeted proof check (by a later run) |
| `night:P3K.8` | IV |  | S6_02_PUSH, S6_06_BLIND | Proved | 22 | 4 | 3 / 3 | 1 | 0 | 3 (0) | 4 | targeted proof check (by a later run) |
| `night:P3F.1` | IV |  | S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 27 | 4 | 3 / 3 | 1 | 1 | 0 (0) | 5 | targeted proof check (by a later run) |
| `night:P3F.13` | IV |  | S6_02_PUSH, S6_06_BLIND | Proved | 24 | 4 | 3 / 3 | 1 | 1 | 2 (0) | 5 | targeted proof check (by a later run) |
| `night:P3F.24` | IV |  | S6_02_PUSH, S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 27 | 5 | 3 / 3 | 2 | 1 | 4 (0) | 6 | targeted proof check (by a later run) |
| `night:P3K.11` | IV |  | S6_02_FAMILY, S6_06_BLIND | Proved | 18 | 4 | 3 / 3 | 1 | 0 | 6 (2) | 6 | targeted proof check (by Claude) |
| `night:P3F.25` | IV |  | S6_02_PUSH, S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Refuted | 32 | 5 | 4 / 5 | 2 | 1 | 4 (0) | 7 | targeted proof check (by a later run) |
| `night:P3R.2` | IV |  | S6_02_PUSH, S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 36 | 5 | 3 / 3 | 2 | 1 | 3 (1) | 8 | targeted proof check (by a later run) |
| `night:P3K.57` | IV |  | S6_06_BLIND | Refuted | 13 | 2 | 10 / 12 | 0 | 0 | 0 (0) | 10 | targeted proof check (by a later run) |
| `night:P3K.80` | IV |  | S6_06_BLIND | Proved | 9 | 2 | 15 / 15 | 0 | 0 | 0 (0) | 15 | independent re-proof |
| `night:P1.6` | V |  | S6_06_BLIND | Known | 17 | 2 | 0 / 0 | 0 | 0 | 1 (0) | 0 | read in an intake (register level, not a proof check) |
| `mapsaudit:order-four-torsion-transgression` | V |  |  | Proved | 0 | 1 | 1 / 1 | 0 | 0 | 0 (0) | 1 | targeted proof check (in its own run) |
| `night:P1.17` | V | main | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P1.5` | V |  | S6_06_BLIND | Refuted | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P1.7` | V |  | S6_06_BLIND | Proved | 17 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P1A.5` | V | main | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P1A.6` | V | main | S6_06_BLIND | Proved | 16 | 2 | 1 / 1 | 0 | 0 | 1 (0) | 1 | targeted proof check (by a later run) |
| `night:P1.1` | V |  | S6_06_BLIND | Proved | 17 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P1.15` | V |  | S6_06_BLIND | Proved | 17 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P1.16` | V |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P1.18` | V | main | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P1.3` | V |  | S6_06_BLIND | Proved | 17 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P1.4` | V |  | S6_06_BLIND | Proved | 17 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P1A.1` | V | main | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P1A.4` | V | main | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 1 (0) | 2 | targeted proof check (by a later run) |
| `night:P1.10` | V |  | S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 27 | 4 | 1 / 1 | 1 | 1 | 1 (0) | 3 | targeted proof check (by a later run) |
| `night:P1.13` | V | main | S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 27 | 4 | 1 / 1 | 1 | 1 | 1 (0) | 3 | targeted proof check (by a later run) |
| `night:P1.19` | V |  | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 2 (1) | 3 | targeted proof check (by a later run) |
| `night:P1A.3` | V | main | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 2 (1) | 3 | targeted proof check (by a later run) |
| `night:P1.12` | V |  | S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 26 | 4 | 2 / 2 | 1 | 1 | 3 (0) | 4 | targeted proof check (by a later run) |
| `night:P1.14` | V |  | S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Known | 27 | 4 | 1 / 1 | 1 | 1 | 5 (1) | 4 | targeted proof check (by Claude) |
| `night:P1.2` | V |  | S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 26 | 4 | 2 / 2 | 1 | 1 | 3 (0) | 4 | targeted proof check (by a later run) |
| `night:P1.9` | V |  | S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 27 | 4 | 2 / 2 | 1 | 1 | 2 (0) | 4 | targeted proof check (by a later run) |
| `night:P1A.2` | V | main | S6_06_BLIND | Proved | 16 | 2 | 2 / 2 | 0 | 0 | 3 (2) | 4 | targeted proof check (by a later run) |
| `night:P1B.1` | V |  | S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 26 | 4 | 2 / 2 | 1 | 1 | 1 (0) | 4 | targeted proof check (by a later run) |
| `night:P1B.2` | V |  | S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 26 | 4 | 2 / 2 | 1 | 1 | 1 (0) | 4 | targeted proof check (by a later run) |
| `night:P1.11` | V |  | S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 27 | 4 | 2 / 2 | 1 | 1 | 3 (1) | 6 | targeted proof check (by a later run) |
| `night:P1.8` | V |  | S6_04_MAPS_MANIFOLDS, S6_06_BLIND | Proved | 26 | 4 | 3 / 3 | 1 | 1 | 3 (1) | 6 | targeted proof check (by a later run) |

