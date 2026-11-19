# Follow-ups reader (Claude Opus 5.5 at effort max), working state, 17 Nov 2026

Brief: the main session's launch prompt (verdict for every notes entry of kind "own idea" / "unpursued implication").

## Scope found
- notes_crosslinks_20261117.tsv: 1669 rows whose kind STARTS WITH "own idea" or "unpursued implication"
  (the brief's "about 480" = the 482 rows whose kind is exactly "own idea." or "unpursued implication.";
  the other 1187 are the same kinds with extra text in the kind cell, e.g. "own idea. **confidence:** high").
- All 1669 extracted (0 missing): numbered_index.tsv (n -> package, entry exactly as in the TSV).
- Reading files: cbatches/c01..c46.txt (compressed: search logs, file paths, bare kind labels removed; quotes cut
  to 160 chars). Uncompressed: batches/b01..b31.txt. Scripts: extract.py, make_batches.py, compress.py.

## Verdict format (verdicts/v_cNN.txt, one line per entry)
n|v|cluster|rank|statement
- v: a = research item, b = edition matter (second pass), c = nothing further
- cluster (a only): ANAB, GT, DER, GS, CRYS, MOT, or a NEW-xxx code listed in clusters.md
- rank (a only): 1 strongest, 2, 3
- statement: for a, the item to prove or refute with cote and scan; for b/c one short line.
Assembly: assemble.py writes FOLLOWUPS_FROM_NOTES_20261117.md and .tsv in field_experts.

## Progress
(see verdicts/ folder: one file per cbatch done)
- DONE 17 Nov 2026: verdicts for all 1669 entries (v_c01..v_c31 for @1-@1125, v_d01..v_d06 for @1126-@1669);
  assemble.py run: missing 0, extra 0, no duplicates. Counts: (a) 41, (b) 495, (c) 1133.
  Outputs: field_experts\FOLLOWUPS_FROM_NOTES_20261117.md and .tsv.

## Method change at @1126 (context 715k at end of c31, bound was ~500k)
- Entries @1-@1125 (verdict files v_c01..v_c31) were read in full (compressed batches).
- From @1126 on: digest reading (header, location, first ~260 chars of body) in dbatches/d*.txt,
  with full text read for every entry the digest marks as a possible research item.
- Assembly: assemble.py (to write) -> FOLLOWUPS_FROM_NOTES_20261117.md/.tsv in field_experts.
