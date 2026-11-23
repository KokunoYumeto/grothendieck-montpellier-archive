# Restoring a checkpoint

Current deliverables, the complete paper, registers, modules, input material,
and all unmarked evidence are ordinary files in the checkpoint ZIP. Beginning with the
checkpoint that first records `working_history_storage` in
`CHECKPOINT_MANIFEST.json`, the complete `work_in_progress` tree is stored as
`ALP_CONNES/work_in_progress.tar.xz` inside that ZIP. This is a lossless storage
change. Every original path, byte count and SHA256 remains listed individually
in the logical manifest. No earlier checkpoint is changed or included.

After extracting the ZIP, run this command from the extracted `ALP_CONNES`
directory before resuming research:

```bash
python scripts/restore_work_in_progress.py
```

The script first verifies the bundle and every logical file, then restores all
original paths as separate regular files. It refuses to overwrite an existing
file with different contents and rejects destination symlinks. Repeating it on
identical independently restored files is safe. Existing hard-linked files are
rejected: use a clean extracted destination and this script to obtain independent
copies. New files are installed exclusively without overwriting a concurrently
created target. To verify without restoring:

```bash
python scripts/restore_work_in_progress.py --verify-only
```

If restoration is interrupted immediately after exclusive installation, a
same-directory `.restore-*` temporary hard link may remain. A retry then refuses
the aliased destination. Recovery is to verify that the reported destination
and that temporary file have the same device/inode and expected manifest hash,
remove only the matching temporary link, and rerun the script. Keep the restored
research file. This narrowly timed interruption preserves both copies of the
data but requires that explicit cleanup; automatic crash recovery or protection
against hostile concurrent parent-directory replacement is not claimed.

The compressed tree is also a standard tar.xz archive. Identical original file
contents may be represented by backward tar hard links; the supplied restoration
script materializes independent copies so later edits cannot affect another
path. The ZIP contains no nested ZIP or earlier checkpoint. Publications already
represented by the established external-publication manifest retain that prior
policy; this storage change introduces no additional content exclusions.

Checkpoint completion verifies ordinary ZIP members by CRC and SHA256, and all
logical tar members by size and SHA256. Snapshot time and compression completion
time are recorded separately. A completed checkpoint remains immutable.
The frozen logical manifest and recovery state are saved before solid compression
starts. A resumed unfinished checkpoint uses those exact frozen bytes. Before a
later checkpoint is made from a restored workspace, the previous compressed
container is checked against its original manifest and every logical path must
be present; only then is that generated representation omitted from the new
snapshot in favor of the complete current logical tree.


## Optional generated-QA storage

For a new checkpoint, `--solid-wip --solid-generated-qa` additionally stores
files under the historical generated trees `evidence/visual_*` and
`evidence/recovery_pdf_qa` in the same `work_in_progress.tar.xz` member.
Only directory descendants are eligible. Every bundled logical manifest row
has `solid_member: "ALP_CONNES/work_in_progress.tar.xz"`; its original `path`,
`bytes` and `sha256` are unchanged. Current paper/PDF/modules/input material
and all other evidence remain direct ZIP members. No logical exclusion or
image modification is introduced. The previous external-publication policy
is unchanged.

Use the same restore command above. The supplied updated reader accepts both
old unmarked WIP-only manifests (including CP38) and new marked manifests.
It rejects marked paths outside the exact WIP/generated-QA allowlist,
noncanonical paths, unexpected tar types, unsafe hard links, and destination
symlinks. A prior container is skipped in a later snapshot only after every
logical WIP and marked-QA path has been restored. Intentionally edited restored
files are then frozen and hashed as current data, not required to equal the old
checkpoint. All selected sources are reverified from the frozen spool before
compression; all restored duplicates become independent regular-file inodes.

Storage selection is frozen with the logical manifest before compression.
Resume cannot add generated QA or WIP to an already frozen selection, and a
completed checkpoint is immutable. No earlier ZIP is rewritten. The existing
manual cleanup rule for a narrowly interrupted exclusive installation and the
absence of protection against hostile concurrent directory replacement remain
unchanged. As an additional preflight, new snapshots reject source symlinks.
