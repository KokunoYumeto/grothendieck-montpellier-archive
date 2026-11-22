# Final-package preparation — no final archive created

This is packaging work. It does not constitute mathematical movement and
does not determine whether the formal stopping rule has triggered.

## Prepared files

- `code/geometry_final_package.py`: default estimate mode and an explicit
  later-use archive-creation branch.
- `notes/geometry_final_package_plan.json`: preview of the full content and
  path mapping for the inspected snapshot.
- `notes/geometry_final_package_estimate.json`: compressed-size estimate.
- `logs/geometry_final_package_estimate.txt`: complete successful dry-run
  output. The first run is preserved with `_attempt01` filenames.

The latest inspected snapshot contains 816 current logical files and all
835 member entries in checkpoints 01–03. Global content deduplication
requires 911 regular-file contents, including 132 historical contents
distinct from the current tree. The estimate is **187,104,145 bytes**;
adding the 2,000,000-byte reserve gives **189,104,145 bytes**, below the
500,000,000-byte delivery limit. These are estimates, not the size of a
created final archive. Later edits and checkpoints are discovered afresh.

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
or repeating identical file content. Current duplicate paths in this
snapshot are logs and an empty note; no executable code or TeX input is
lost as a direct-path alias.

Every checkpoint manifest is itself preserved as historical content.
Checkpoint 01's manifest did not list its own filename; the actual member
exists and is mapped. The inventory check accepts only this self-listing
difference, and records which manifests list themselves. Other inventory
mismatches remain blocking conflicts.

The generated `final_package_manifest.json` records each original
checkpoint member, its final member, SHA256, size, and relation to the
current path. It also records current aliases, exclusions, checkpoint
hashes, and the exact compression estimate method.

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

## Later creation command, only after the stopping rule triggers

The branch below is prepared but **has not been run**:

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
creation fails. The creation branch was independently code-reviewed but
was not executed, as required by the parent instruction.

## Review record

The category agent independently reviewed deduplication, complete member
mapping, exclusions, source/hash checks, no-archive default behavior,
atomic publication and size enforcement, and reported no concrete defect.
No mathematical result/check-event row was added for this packaging work.
