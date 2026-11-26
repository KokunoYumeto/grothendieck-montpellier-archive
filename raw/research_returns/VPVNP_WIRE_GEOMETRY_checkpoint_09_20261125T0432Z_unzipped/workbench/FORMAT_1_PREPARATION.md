# Filing preparation for format 1

The registry owner assigns the official WB number and permanent paper page.
Neither has been assigned here. The filing copy therefore uses
`work/_pending/v1` and stable local `WG-` tags. It contains no `DEPOSITED.md`
marker and claims no public deposit. The final numbered filing requires the
number actually assigned in the registry; a placeholder is not an assignment.

## Two layouts and how to reproduce the working one

The working layout keeps the paper in `papers/wire_geometry` and the original
programs, certificates and frozen records in their named folders. The canonical
filing copy keeps the complete version under `work/_pending/v1`: `paper` holds
the standalone editable project and its PDF; `checks` holds the programs,
certificates, proof records, tools and project records. The three reserved
tables have exactly the headers prescribed by the registry checker. Original
working tables are retained under names ending in `INDEX.tsv`, so they are not
mistaken for reserved format-1 tables.

The registry permits a limited set of text file extensions. Original JavaScript
and C++ sources are therefore carried as exact UTF-8 text with a `.txt` suffix;
`PORTABLE_PATHS.json` records their original paths and hashes. The genuine Git
bundle is carried in base64 text with its decoded hash. Compiled executables
and TeX build byproducts are reproducible and are omitted.

From the root of a filing copy, restore the original working layout with:

    python restore_working_copy.py --destination /absolute/new/working-copy

The destination must not exist. The helper first checks the complete version
manifest, restores the original filenames, decodes and checks the Git bundle,
and preserves the original record bytes. Outer project records are restored
inside `project-records/`; the exporter detects that location. Root metadata
and the original working README are also restored. The source restoration was exercised on a
checkpoint; its programs and certificates were compared byte for byte.

## Source identity and complete version identity

The paper prints a genuine local Git source revision and the SHA-256 of its
editable-source manifest. The supplied Git bundle contains that commit and
tag. The source manifest excludes the generated identity and compiled PDF:
including a file's own hash inside that file would make the identity circular.

The separate `MANIFEST.sha256` at the version root covers every file in the
finished version except the manifest itself and any later deposit marker.
It includes the PDF, printed identity, source manifest, encoded Git bundle,
proofs and check records. `EXPORT.json` records this manifest's SHA-256.
The source identity and complete payload identity are distinct.

## Refreshing a filing copy after edits

Run these commands from the restored working-copy root, after completing the
paper edits and records. Use new absolute destinations and an unused Git tag.

    python tools/refresh_records.py
    python tools/prepare_release.py stamp --history-dir /absolute/source-history --tag source-v1
    python tools/build_paper.py --fresh-directory /absolute/new/fresh-build --record records/root/FINAL_BUILD.json

The history directory must be outside the returned workbench. Existing Git
tags are never moved. The Git identity is GPT-6 Astra; the email field is the
literal `unassigned`, which is not a contact address. The build helper checks
references, exact source hashes and the two-point overfull-box limit. It does
not replace mathematical reading or visual inspection of every page.

After checking the PDF, export a new canonical copy outside the working tree:

    python tools/export_format1.py --destination /absolute/new/filing-copy --build-record records/root/FINAL_BUILD.json --aux-file /absolute/new/fresh-build/main.aux

The exporter verifies that the PDF and every editable input match the build
record, obtains printed statement numbers from the exact auxiliary file,
preserves historical statement rows and records, writes the reserved tables,
and computes the full version manifest. This is the canonical export path.
The older `prepare_release.py stage` command only makes a working-layout
snapshot and is not the format-1 exporter.

## Official validation and later assignment

The registry checker is available at
https://raw.githubusercontent.com/KokunoYumeto/mathematics-workbenches/main/tools/check_workbench.py.
The inspected version has SHA-256
`13042772b472b1a65f35fd8d8c349dc55a5e9cdabb5e6e5e4434aa1d4b6f0291`.
It was read in full before execution. Its external source is cited rather
than included in this package.

The official validator rejects pending folder names and local WG tags by
design. Its report distinguishes those expected assignment failures from
every other fault. A zero-unexpected-fault report is not described as an
unqualified validator pass. Source/hash checks, registry validation and
mathematical proof checks are separate.

After the registry owner assigns a number, update the paper's permanent
record address, make a new source revision, rebuild, inspect, and run the
canonical exporter with `--registered-work-id` followed by that exact assigned
number. The exporter maps the stable local statement suffixes to the official
number. Run the registry checker again on the resulting numbered copy. Only
after actual deposit should a deposit marker and registry Git tag be added.
Preserve deposited version folders; corrections belong in a new version.

## Check-event vocabulary

The canonical `CHECK_EVENTS.tsv` uses the format-1 event types. The working
index also preserves each contributor's original type wording and outcome.
`AUTHOR_EVENTS.tsv` separates derivations and author proofs from independent
checks. Frozen contributor ledgers and the pre-normalization aggregate remain
in `checks/records`; the current statement index links actual check events.
