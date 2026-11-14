# Checkpoint reconciliation

Every member of every immutable checkpoint is accounted for in CHECKPOINT_RECONCILIATION.tsv. Its earlier hash, final destination and hash, status, and reason are explicit. For replaced UTF-8 files, the linked unified diff lists removed passages and their replacements, with the privacy redactions described below. Earlier partial reader PDFs are identified by hash and superseded by the final compiled PDF; their build measurements remain in BUILD_HISTORY.jsonl.

| Status | Checkpoint members |
|---|---:|
| omitted supplied duplicate | 21 |
| preserved with explicit archival name | 12 |
| superseded | 1265 |
| unchanged | 9468 |

The supplied input-table duplicates removed after checkpoint03 remain in the original TEXT archive and are individually listed in OMITTED_CHECKPOINT_FILES.tsv. No original archive or earlier checkpoint ZIP is embedded in these final packages.

CHECKPOINT_MANIFEST_PROVENANCE.tsv records each immutable ZIP hash and the origin and hash of its inventory. Checkpoints01--04 predate embedded inventories; their numbered inventories are derived from the exact preserved ZIP bytes. Later numbered inventories preserve CHECKPOINT_CONTENTS.tsv verbatim. The derived inventories add no member to, and change no byte of, an earlier checkpoint.

Historical text diffs contain 20 explicit path/address-span redactions, individually listed in CHECKPOINT_PRIVACY_REDACTIONS.tsv by checkpoint, relative file, original line/column, character range, removed-span SHA-256 and reason. Each redacted span is replaced by a labelled hash marker; the other diff text is exact. This accounts for the omitted path strings without copying them into the final records. The immutable earlier checkpoints are unchanged.
