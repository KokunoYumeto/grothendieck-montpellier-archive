# Brief: the note entries both passes missed (17 Nov 2026, 04:2x UTC)

From the main session (Claude Opus 5.5 at effort max) to the follow-ups reader a9ebc3d6 (Claude Opus 5.5 at effort
max). This is the third part of the same job, after the follow-ups pass (`FOLLOWUPS_FROM_NOTES_20261117.md`) and the
claims pass (`CLAIMS_FROM_NOTES_20261117.md`).

- Model: Claude Opus 5.5. Effort: max.
- Sub-agents allowed: 0.
- Compute bound: about 600k tokens.
- This account is near its weekly limit and may stop you before the end. So write `STATE.md` every 100 entries, and
  write the output files as you go, not only at the end.
- If your context is compacted, the summary is not reliable. Reread this brief and `STATE.md`, then continue.

## Why these entries were missed

Both passes selected entries by the `**Kind:**` line. About a third of the notes write the kind otherwise:
- at the end of the title ("A003.1 — Scan 003, lines 14-19 — unproved claim"; "...; reading question");
- inside a bold line ("**Kind: reading question — ...**", "· Kind: unpursued implication");
- or not at all (thematic prose sections, such as MPL_72's "Bridge B5: what is proved ...").

## The entries

`field_experts/NOTES_GAP_ENTRIES_20261117.tsv` (built by `tools_20261113/notes_gap_entries.py`) lists 1,772 entries in
62 packages, numbered g1 to g1772. Each row gives its kind as written, its class and its notes file.
- **g1-g828:** own ideas, unpursued implications, unproved claims and conjectures. Do these first.
- **g829-g1772:** entries with no kind. For each, first say what it is (an own idea, an implication, a claim of his, a
  reading question, a summary, a source comparison), then give the verdict.

The core Longue Marche packages of cote 149 (MPL_149_001-090, MPL_149_091-136) are among them. Their notes fed
FLAGGED_149 and ANABELIAN_149_PUSH, so check an item against those prompts' subjects in `PROGRAMME_MAP.md` before
calling it new.

## The verdicts (as in your two passes)

- **(a) Research item:** a statement to prove or refute, with the cote and scans, his words where they fix it, a
  cluster and a rank from 1 to 3.
  - The clusters are the six consolidated prompts (ANAB, GT, DER, S6, TAME, CYCLES; see the audit's last two
    sections) or a plainly named new cluster.
  - The ids are g-numbers.
- **(b) Edition matter for the second pass.**
- **(c) Nothing further:** a known result (named, from memory, marked as such), settled in the notes, a duplicate of
  @n, #n or another g-number, or too local.

Check against `notes_headlines/PROGRAMME_MAP.md` and `HEADLINE_RESULTS.md` by grep before calling an entry new. Where
an entry credits Michel Hua's project, the credit stays with his project.

## Write

- **`field_experts/GAP_FROM_NOTES_20261117.md` and `.tsv`** in your format: scope and method, the summary table, the
  research items by cluster with their g-numbers, and the edition matters by package. The TSV has one row per entry:
  g, package, entry, what it is (for the untyped ones), verdict, cluster, rank, statement.
- **`STATE.md`** in `field_experts/gap_work_20261117/`, updated every 100 entries with the last g-number done.
- **The final message, short:** the counts, and the strongest research items (up to ten), one line each.
