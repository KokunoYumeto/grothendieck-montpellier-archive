# Final package contents and checkpoint account

The two language ZIPs contain twelve unique final PDF editions and their standalone
TeX sources. The guide PDF and guide TeX are repeated in both language packages.
README.md is repeated in all three packages. The records ZIP uses edition-relative
paths at its root; extract it into a directory named edition to use the supplied
build commands. FINAL_FILE_MANIFEST.tsv maps each final package member back to
that edition-relative source path and gives its byte count and SHA-256.

All 260 checked page sources, cumulative decisions, full-page review records,
full-page PDF review images (including historical versions), guide paragraphs,
translations, intermediate sources, authored scripts, sanitized logs and other
documentary outputs are retained. The development directory preserves documentary
source and diagnostic history; the current standalone books are named in README.

Earlier development PDFs are superseded by the current reviewed PDFs of the same
work. Toolchain and margin-diagnostic PDFs are omitted as diagnostic artifacts;
their source, sanitized logs and resulting repair records remain. Regenerable TeX
auxiliaries, engine-format files, Python bytecode and runtime locks are omitted.
Source-scan crops remain reproducible from the supplied scans and are omitted;
the original input archives and scans are not copied into the release.

CHECKPOINT_MEMBER_ACCOUNT.tsv contains one row for every file member of every
saved numbered checkpoint, with the exact old bytes and SHA-256. Each row states
retained, superseded, or omitted; retained and superseded rows name the final ZIP
member and its SHA-256. Omission rows give a concrete reason. The companion summary
identifies every immutable checkpoint and totals its dispositions. No checkpoint
ZIP is nested in a final package.

The account and final manifest are created after the last numbered checkpoint.
The manifest lists every final member except its own row: its complete bytes are
contained in the records ZIP, whose digest is recorded in the release receipt.
The packaging script reopens each ZIP, verifies its member list and every member's
SHA-256, checks for CRC errors, and checks that the source files remained unchanged
while packaging. It names the three final ZIPs only after these checks pass.

The final PDF paths in build records correspond to the edition_source column of
FINAL_FILE_MANIFEST.tsv. Their actual delivered locations are the final_package
and member columns; copying a delivered PDF to its recorded build path restores
that exact layout for review tooling without recompilation.
