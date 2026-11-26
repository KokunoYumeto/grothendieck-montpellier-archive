# Filing the two checked papers

This is an undeposited Format 1 candidate for the existing algebraic-cycles-and-motives workbench. UNFILED-A and UNFILED-B are temporary work folders, and UNFILED statement tags are provisional identities. No public commit, permanent number, publication or deposit is claimed.

## Preparation already authorized

After the final proof records, page records and source-only builds are complete, refresh the statement/source metadata and check events. Then run the finishing formatter against this workbench while no other process is writing its files. It preserves the papers, canonicalizes table statuses without losing their qualifications, archives whole-paper events, normalizes file extensions, excludes regenerable build/cache files, removes host-specific path prefixes, places each paper's referenced checks inside its own version and regenerates the two manifests.

The formatter's provenance and transformation records are in each version's `checks/format/`. The transformation log records operations, original/resulting hashes and replacement counts; it does not republish private host paths. Source citations and source hashes remain available, but no downloaded primary paper, extracted source body, external certificate archive or official checker is bundled.

The official Format 1 checker must then be run separately, without its `--write` option. Do not call a provisional-identifier failure a PASS. Record the exact exit code, fault categories and final output line for this package, rather than citing the older one-paper check.

## Assignments at filing

1. Obtain the actual permanent work number or numbers from `registry/works.tsv` in the mathematics-workbenches catalogue. Confirm the intended treatment of the two-paper split. Use the existing algebraic-cycles-and-motives repository; no empty new repository is needed.
2. Create the individual permanent `works/WB-nnnn.md` page or pages and rename the temporary work folders. Apply the explicit statement-tag map while preserving every statement's suffix identity, all supersedes relationships and the complete historical check-event record. Retain the old-to-new map.
3. Replace each paper's catalogue-root `recordurl` by its assigned individual permanent page. Keep the author line blank unless the depositor directs otherwise.
4. Set only actual commit, version tag and deposit metadata. FORMAT asks the paper to print the version manifest hash and commit, while its manifest hashes the paper's TeX/PDF. The catalogue's seal convention must resolve this self-reference; do not insert a fabricated or stale value. This candidate does not silently invent an exception.
5. Rebuild from fresh sources if the paper metadata changes, and reconcile every changed rendered page. Regenerate manifests, rerun the official checker, and separately validate the status values and record links; provisional tag faults previously short-circuited some official row checks.
6. Read the exact addition list for ownership, prohibited source copies, private records and paths. Only then publish/deposit as authorized. Create `DEPOSITED.md` after the actual deposit. A deposited folder is immutable; a later correction is a new version with a dated entry on the permanent page.

## Manifest scope

Each `MANIFEST.sha256` hashes every file of its version except files named `MANIFEST.sha256` and `DEPOSITED.md`, matching the official generator. The version-local checks are the reproducibility material covered by that manifest. Shared root checks may remain as navigation/source copies, but they do not substitute for the sealed version-local records.

Run any writing reproduction program in a separate copy. Program commands, expected outputs and historical source hashes describe their exact verification runs; later formatting and path normalization are recorded separately and do not masquerade as unchanged original bytes.

## Current mathematical and review scope

Conditional theorems retain their hypotheses. Failure of a proposed inference is not relabelled as falsity of algebraicity. Statement-only same-model attempts, proof-aware targeted audits, exact computations and rendered-page readings are recorded as different activities. No human or external-model validation is claimed unless a record explicitly identifies it. Permanent identifiers and filing actions remain distinct from completion of the mathematical and page review.

## Final candidate check records

The returned ZIP root contains `FINAL_FORMAT_CHECK.json` and `FINAL_INTEGRITY_CHECK.json`, produced after export-specific changes and manifest sealing. The official checker retains the actual provisional-identifier failure; the separate integrity check covers canonical statuses, record paths, current manuscript hashes and all version manifests. The pre-seal format result in `checks/format/` records the earlier two stale manifests before regeneration and is explicitly not the final result. Permanent numbering and the actual publication seal remain the depositor's work.
