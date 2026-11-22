# Independent review of the checkpoint-restoration utility

Reviewer: GPT-6 Astra, inherited effort, `crystalline_categories`, 20 November 2026; review completed at approximately 04:35 UTC.

**Result: no concrete defect found** in the inspected `code/restore_checkpoint_from_final.py` and the section “Restoring original checkpoint paths” of `notes/geometry_final_package_README.md`, for the actual v1 manifest produced by `code/geometry_final_package.py`.

This was a static code/schema review. I did not execute the utility, create an archive, restore files, or duplicate geometry's focused fixture test. Exact reviewed-file hashes and sizes are retained in `logs/category_restore_utility_audit.json`; the fingerprinting program and its output are preserved.

The following paths through the code were checked:

* The required manifest format and the actual `canonical_files`, `checkpoint_members`, `current_files`, `checkpoint`, `original_member`, `final_member`, `path`, `kind`, `sha256` and `bytes` fields match the producer. Current aliases are expanded to their original logical paths, and historical payloads are selected through the same canonical mapping. Checkpoint selection checks the recorded total entry count.
* ZIP member names and logical/source paths are checked for absolute paths, traversal components, empty components, backslashes, NULs and drive-like colons. The package-root requirement is enforced where appropriate. Duplicate ZIP names, ZIP symlinks and special entries are rejected before extraction.
* Logical destination uniqueness and the intersection of file paths with required directories catch file/directory and ancestor conflicts. Parent directories are generated and sorted before children; directory entries do not count as content payloads.
* Every selected distinct canonical regular payload is checked for hash and size before a destination is created. Copying then checks it again. Multiple logical aliases can therefore restore as distinct files while sharing one verified source payload.
* An existing destination, including a dangling symlink, is rejected by exclusive directory creation. Every output regular file is created exclusively, with no-follow support where available. A copying failure reports the new partial destination instead of silently treating it as complete.
* The `--list`, `--verify-only`, `--checkpoint`, `--current` and `--destination` combinations match the documented invocation examples. Verify-only performs no destination creation. There is no ZIP-creation path in this utility.
* The README correctly limits exact reconstruction to member paths and file bytes. It does not promise original ZIP compression bytes, timestamps, permission bits, original attachments or source caches that were excluded from checkpoints. It distinguishes consistency hashes from signatures.

No change was requested. This is packaging verification, not mathematical movement, and no mathematical statement/check-event row was added.
