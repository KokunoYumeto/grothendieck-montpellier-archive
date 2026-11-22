# Source provenance and limits

All Lean sources in `source/` were retrieved from the immutable commit
`7cbf7a0c32fca1badf05931879a37c3f8a2b03b4` of
https://github.com/CocoSgt/riemann-hypothesis-lean .

`SOURCE_MANIFEST.tsv` and `source_manifest.json` record the exact relative path, Git blob SHA-1, SHA-256, byte length, line count, and immutable raw URL of every downloaded file. The raw byte strings were checked against the pinned Git object IDs: 700 through the saved tree metadata and six through commit-specific contents API metadata. `SOURCE_VERIFICATION.json` records that all 706 source blobs matched. `AV_tree.json` is the complete untruncated AutomorphicVarieties subtree; `github_tree.json` is a larger truncated root listing and is not treated as a complete repository index. `extra_pinned_blobs.json` retains metadata for the six files not present in those listings.

Retrieval and hash verification are provenance checks, not proof checks. Only the specific definitions and proofs named in `ONECHAR_CHAIN.md`, `C7_EXPLICIT.md`, `QUARTIC_REVIEW.md`, and `CHECK_EVENTS.tsv` were substantively reviewed. Imported results are cited under the task's archive-theorem convention. No claim is made that every downloaded proof was read or that every transitive dependency was validated.

No Lean executable was available in this environment and no archive build was attempted. The included `OneCharUClosed_UNCOMPILED.lean` contains an extracted proof term and proposed `#check` / `#print axioms` commands, but those commands have not been executed. Consequently there is no new kernel certificate and no new axiom report.

For the explicit class-number-one specialization in `C7_EXPLICIT.md`, the cited external theorem is J. S. Milne, *Algebraic Number Theory*, version 3.08, Theorem 4.3, printed p.70 (PDF page index71), available at https://www.jmilne.org/math/CourseNotes/ANT.pdf . Its complete statement was checked in the official PDF on 2026-11-21. It is used as accepted background, and was not re-proved. The new six-field specialization and its inertness/arithmetic checks are written out in the proof and in `check_c7_arithmetic.py`.
