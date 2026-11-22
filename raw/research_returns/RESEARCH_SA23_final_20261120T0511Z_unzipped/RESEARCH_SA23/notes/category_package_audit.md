# Independent review of final-package preparation

2026-11-20 UTC. Reviewer: crystalline_categories. Packaging only; this is
not a mathematical proof check or mathematical movement for the stopping
rule. Reviewed `code/geometry_final_package.py` against `code/checkpoint.py`.
No archive was created, and no `--create-final` invocation was made.

The reviewed logic passes the requested checks:

- Current regular files are processed first. The shared `(SHA256, size)` map
  then deduplicates historical contents globally, including identical bytes
  at different names. The manifest keeps every current logical path and every
  previous checkpoint member, so aliases do not erase restore information.
- Every old ZIP entry is read and hashed. Previously recorded archive hashes,
  unsafe paths, duplicate member names, and checkpoint-manifest inventories
  are checked. Distinct old bytes at changed or deleted paths remain as
  historical canonical members; every mapped file is checked against its
  target's hash and size. Original checkpoint manifests are retained.
- Runtime/source/PDF/web-cache/full-extraction/scan/ZIP/TeX auxiliary
  exclusions agree with checkpoint.py. Original input directories and symlink
  handling are explicit. Historical-policy conflicts are reported and block
  final creation instead of silently dropping a previous included member.
- Default and `--estimate` paths only write JSON plan/estimate reports.
  Current report files can change as a consequence of an estimate; the
  explicit creation path deliberately rebuilds the plan and does not rewrite
  reports that it has hashed.
- Explicit later creation checks copied-source hashes and sizes, verifies
  the final member inventory and contents, checks the actual 500MB limit,
  and only then atomically creates a non-overwriting hard link at the final
  destination. Temporary output is removed on success or failure.

The estimate appropriately remains an estimate: it reuses old compressed
sizes where available and reserves space for report/metadata changes. The
actual-size check is the delivery gate. No concrete correctness defect was
found in this source review. Geometry owns the separate live estimate run.

This review does not claim preservation of filesystem metadata beyond the
stated content/path manifest, nor does it override the existing source-cache
policy. Program versions are fingerprinted in the corresponding audit log.
