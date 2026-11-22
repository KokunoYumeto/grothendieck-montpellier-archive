# Final-package guide and preparation record

This guide records packaging preparation and gives creation and restoration
instructions. Packaging does not constitute mathematical movement or decide
whether the formal stopping rule has triggered. The dated preparation
snapshots below are historical records; actual final creation, if performed,
is established by its verified creation result and generated manifest.

## Prepared files

- `code/geometry_final_package.py`: default estimate mode and an explicit
  later-use archive-creation branch.
- `notes/geometry_final_package_plan.json`: preview of the full content and
  path mapping for the inspected snapshot.
- `notes/geometry_final_package_estimate.json`: compressed-size estimate.
- `logs/geometry_final_package_estimate.txt`: complete successful dry-run
  output. The first run is preserved with `_attempt01` filenames.

The initial 03:04 UTC snapshot contained 816 current logical files and all
835 member entries in checkpoints 01–03. Global content deduplication
requires 911 regular-file contents, including 132 historical contents
distinct from the current tree. The estimate is **187,104,145 bytes**;
adding the 2,000,000-byte reserve gives **189,104,145 bytes**, below the
500,000,000-byte delivery limit. These are estimates, not the size of a
created final archive. Later edits and checkpoints are discovered afresh.

## Refreshed checkpoint-04 audit

The 03:36:48 UTC snapshot, preserved in
`notes/geometry_final_package_plan_cp04.json` and
`notes/geometry_final_package_estimate_cp04.json`, contains 1,945 current
logical files and all 2,075 entries from checkpoints 01–04. Global
deduplication needs 2,012 regular-file contents, including 150 historical
contents distinct from the current tree. The estimate is **304,062,037
bytes**, or **306,062,037 bytes with reserve**, leaving 193,937,963 bytes
below the 500 MB limit. The measured estimate run took 9.06 seconds.

`logs/geometry_final_package_cp04_audit.json` verifies that all 1,240
checkpoint-04 entries are mapped, including its 265 logs and 144 code
files. All seven required current deliverables, including the progress
ledger, are direct canonical members. There are no current `.tex`, `.py`,
or `.sh` aliases. All 1,258 excluded regular source/cache files in this
snapshot have individual path, SHA256 and byte-count records.

The approximately 28 MB increase from the initial 03:32 estimate is
chiefly a newly retrieved Bourbaki source payload and raw page images under
`notes/`. They were not in checkpoint 04. Their owning agent is relocating
them unchanged into `sources/`, with path/hash records, before checkpoint
05. The estimate above retains the files present at its stated timestamp;
it does not assume that later relocation has completed. The initial CP04
outputs survive in `_cp04_initial` files, and the missing `/usr/bin/time`
attempt is recorded before the successful standard-library timing wrapper.

The two bookkeeping additions preserve individual excluded-file hashes
and, just before final publication, recheck the current included path set
and contents and the complete checkpoint set and hashes. Their focused
independent review passed; see `notes/category_package_additions_audit.md`.
The 03:36:48 UTC preparation audit executed no archive-creation branch.
Writers must be quiescent for an actual final run, and the destination and live stdout capture must remain
outside the included research tree. Final creation rebuilds its plan.
The progress ledger is included, but the packager does not determine
whether the stopping rule has triggered; root owns that decision.

## Preservation and deduplication

The script follows `code/checkpoint.py` for runtime, retrievable source,
source PDF, web-cache, full-text-cache, verification-scan, nested ZIP and
TeX-auxiliary exclusions. Original attachments and extracted input trees
remain external. Symbolic links are not dereferenced.

Each distinct SHA256-plus-size content is stored once. Current content
gets priority for its ordinary path; an older distinct version is placed
under `RESEARCH_SA23/history/checkpoint_NN/`, using its earliest occurrence.
If identical content occurs at several current paths or checkpoints, every
logical path maps to its one canonical member in the generated manifest.
Thus an exact historical view can be reconstructed without nesting ZIPs
or repeating identical file content. At the initial preparation snapshot, duplicate current paths were logs
and an empty note; no executable code or TeX input was a direct-path alias.
The actual final manifest records the aliases at creation time.

Every checkpoint manifest is itself preserved as historical content.
Checkpoint 01's manifest did not list its own filename; the actual member
exists and is mapped. The inventory check accepts only this self-listing
difference, and records which manifests list themselves. Other inventory
mismatches remain blocking conflicts.

The generated `final_package_manifest.json` records each original
checkpoint member, its final member, SHA256, size, and relation to the
current path. It also records current aliases, exclusions, checkpoint
hashes, and the exact compression estimate method.

## Restoring original checkpoint paths

The final ZIP contains `code/restore_checkpoint_from_final.py`. Extract
that script to a convenient location, or use the copy in this research
tree. It reads the archive's actual `RESEARCH_SA23_deduplicated_final_v1`
manifest and restores every logical checkpoint member from its canonical
payload, including unchanged files, older versions and the checkpoint's
own manifest. It also supports the final current view, restoring duplicate
logical paths as separate files with identical bytes.

```sh
python restore_checkpoint_from_final.py RESEARCH_SA23_final.zip --list
python restore_checkpoint_from_final.py RESEARCH_SA23_final.zip \
  --checkpoint 5 --verify-only
python restore_checkpoint_from_final.py RESEARCH_SA23_final.zip \
  --checkpoint 5 --destination restored_checkpoint_05
python restore_checkpoint_from_final.py RESEARCH_SA23_final.zip \
  --current --destination restored_current
```

Each destination must **not exist**; its parent must already exist. The
restored files appear below `destination/RESEARCH_SA23/` with their original
logical paths. The script checks every selected canonical payload's SHA256
and byte count before creating the destination, then checks again while
copying. It rejects traversal paths, duplicate member names, symlinks,
special ZIP entries, inconsistent mappings and file/directory collisions.
It creates files exclusively and never overwrites an existing destination.
If an I/O failure occurs during copying, it reports the newly created
partial directory and leaves it for inspection; rerun into another new
directory after resolving the failure.

Restoration reproduces member paths and file bytes, not the old ZIP's
compression bytes, timestamps or permissions. Source caches and original
inputs excluded from a checkpoint were never checkpoint members and remain
outside this reconstruction; their recorded provenance and fingerprints
are retained. Hashes check consistency with the manifest, rather than
provide a digital signature. This utility creates no ZIP and does not
invoke the final-package creation branch.

## Permitted preparation command

From the workspace parent directory:

```sh
python RESEARCH_SA23/code/geometry_final_package.py --estimate
```

This reads the current tree and existing checkpoint ZIPs and writes JSON
reports. It creates no archive. Estimates use existing ZIP entry compressed
sizes for identical content, dry-run raw DEFLATE level 6 for new content,
the generated manifest's compressed size, and ZIP header overhead.
The preview is informational; it is never used as a stale creation plan.

## Creation command, after the stopping rule is documented

After the formal stopping decision, create the final package with:

```sh
python RESEARCH_SA23/code/geometry_final_package.py \
  --create-final /workspace/scratch/a7ef7e55112c/RESEARCH_SA23_final.zip
```

Creation starts with a fresh plan. It refuses an existing destination,
policy conflicts, files changing during planning, and an excessive size
estimate. It verifies each copied source and then all archive members
against their SHA256 and size, rejects duplicate regular-file contents,
checks the actual 500 MB limit, and publishes by an atomic hard link that
cannot overwrite another file. Only its own temporary file is removed if
creation fails. The preparation-only audits described above independently reviewed this
branch without executing it. A later successful creation must be evidenced
by its verified result and generated manifest; this guide does not assert
that creation has occurred.

## Review record

The category agent independently reviewed deduplication, complete member
mapping, exclusions, source/hash checks, no-archive default behavior,
atomic publication and size enforcement, and reported no concrete defect.
No mathematical result/check-event row was added for this packaging work.
