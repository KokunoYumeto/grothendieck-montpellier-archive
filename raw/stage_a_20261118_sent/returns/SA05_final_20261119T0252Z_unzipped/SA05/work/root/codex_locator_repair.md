# Codex physical-locator repair

Completed 19 November 2026 by cote12c at root's request.

## Pipeline use

Run `python SA05/work/root/repair_codex_locators.py items` after
`author_middle.py` and before generating claims/problems from the items.
Run `python SA05/work/root/repair_codex_locators.py tables` after
`author_tables.py`. The optional `all` mode runs both.

The program was executed in `all` mode twice. Its first run inspected all 100
root items, changed 98 item locator fields, inspected all 56 reading rows and
all 74 link endpoints, and changed 104 mapped table locator fields. Its second
full run changed zero fields. A subsequent generator run naturally regenerates
stale input and can report fresh changes again; idempotence is separately checked
on the current canonicalized fields in the validation snapshot. The two
unchanged items are note-only records without declared manuscript scans.

## Method and preserved content

The source of truth is each actual `\scanpage{...}` marker in the nine K12
transcription files. A section begins at that marker's physical 1-based file
line and ends immediately before the next marker, or at EOF. These full
physical sections replace stale filename/offset guesses; the existing precise
Pro locators remain available for the narrow assertion.

Only `items.json:lines`, `readings.tsv:line`, and `links.tsv:from,to` are
changed. All other fields, including the competing readings and their evidence,
are asserted unchanged. Pro and B12 alias/line spans are separately asserted
unchanged. No source text, author script, run_all.py, claim file or consolidated
top-level output was edited by this repair.

## Examples of repaired locations

| Physical scan | Correct Codex file | Physical section lines |
|---|---|---|
|051|K12-04|2–35|
|064|K12-05|2–31|
|071|K12-05|94–140|
|072|K12-05|141–165|
|073|K12-05|166–219|
|074|K12-05|220–246|
|078|K12-05|368–387|
|082|K12-06|2–37|
|084|K12-06|38–66|
|086|K12-06|67–83|
|090|K12-06|145–162|
|095|K12-06|235–239|

There is no K12-series section for scans066,069,097 or098. B12 locators
covering these differently selected/labelled witnesses remain untouched. Link
endpoint125–126 explicitly records that125 is present and126 is absent from
the K12 series. Broad link ranges also disclose any other unretained scans,
rather than assigning them invented sections.

## Saved guide and audits

`source_guide_aliases.json` maps every K12, B12 and Pro alias to its actual
relative source path. It includes all 122 K12 scan sections and source hashes;
B12 sections are listed for orientation but their locators are not rewritten.

The first-run before/after evidence is retained in
`outputs/codex_locator_initial_items.json` and
`outputs/codex_locator_initial_tables.json`, with parallel TSV files. The latest
run has separate `outputs/codex_locator_audit_items.*` and
`outputs/codex_locator_audit_tables.*` files, so repeat pipeline runs do not erase
the first evidence of the stale locators.

Initial and latest run summaries are saved as
`outputs/repair_codex_locators_initial_items_run.txt`,
`outputs/repair_codex_locators_initial_tables_run.txt`,
`outputs/repair_codex_locators_items_run.txt` and
`outputs/repair_codex_locators_tables_run.txt`.

`outputs/codex_locator_validation.json` records that all 122 physical sections
point to their real markers, the K12 hashes match, reapplying repair to all
current fields would change zero locators, and the Pro/B12 locator spans and all nonlocator fields are
preserved. This is a source-locator repair, not an alteration of any mathematical
verdict or a resolution of a reading disagreement.
