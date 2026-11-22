# Checkpoint-06 final-package estimate and restoration audit

Snapshot: 2026-11-20T04:41:28.542588+00:00. This is packaging verification, not mathematical
movement. No ZIP or restored tree was created.

The fresh plan includes all six checkpoint archives and **6,773
historical logical entries**. It also includes **2,575 current
logical files**, represented by **2,645 canonical
regular-file payloads** after content deduplication.

The compressed estimate is **287,607,776 bytes**.
With the 2,000,000-byte reserve it is **289,607,776 bytes**, leaving
**210,392,224 bytes** below 500,000,000. These are dated estimates, not an
assertion that a final ZIP has been created. Actual final creation replans
and checks the real archive size.

| Checkpoint | Original logical entries | Actual file payloads hash-checked | Uncompressed bytes checked |
|---|---:|---:|---:|
| 01 | 106 | 106 | 3,328,208 |
| 02 | 256 | 256 | 10,702,366 |
| 03 | 473 | 473 | 104,430,559 |
| 04 | 1,240 | 1,240 | 214,464,241 |
| 05 | 2,125 | 2,125 | 298,389,938 |
| 06 | 2,573 | 2,573 | 308,064,032 |

For each actual checkpoint ZIP, the audit checked its whole-file SHA256
and size, exact member-name set, member kind, CRC and byte count, then read
every regular member and checked its SHA256 against the new manifest. It
also ran the restoration utility's real mapping logic for all six
checkpoints, checking canonical payload fingerprints and every original
logical path. All six inventories are complete. The current-view mapping
was checked against this plan; a second current-payload read was not
claimed. The package estimator itself hashes current contents while
building the plan.

No policy conflict or changing current file was reported by the estimate.
Source scans and other excluded caches remain subject to the established
checkpoint exclusions, with their per-file provenance fingerprints in the
plan. Their contents are not silently counted as retained checkpoint files.

Records: `notes/geometry_final_package_plan_cp06.json`,
`notes/geometry_final_package_estimate_cp06.json`,
`logs/geometry_final_package_cp06_estimate.json` and
`logs/geometry_restore_checkpoint_mapping_cp06.json`. The mapping audit
took 3.706 seconds. Earlier estimate and audit
files were not overwritten. Final creation must still use a fresh plan
after writers are quiescent and the formal stopping decision is recorded.
