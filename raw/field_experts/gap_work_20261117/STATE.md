# Gap reader (Claude Opus 5.5 at effort max), working state, 17 Nov 2026

Brief (the authority): `field_experts/BRIEF_GAP_READER_20261117.md`. Reread it after any compaction, then this file.
Same agent as the follow-ups pass (@n, FOLLOWUPS_FROM_NOTES_20261117) and the claims pass (#n, CLAIMS_FROM_NOTES_20261117);
both DONE. This is the third part.

## Scope
- `field_experts/NOTES_GAP_ENTRIES_20261117.tsv`: 1772 entries g1-g1772 in 62 packages (columns g, package, entry,
  kind_as_written, cls, how, notes_file).
- g1-g828: own ideas, implications, unproved claims, conjectures (do first). g829-g1772: no kind (say what each is).
- Cote 149 core packages (MPL_149_001-090: 214 entries, MPL_149_091-136: 141) fed FLAGGED_149 and ANABELIAN_149_PUSH:
  check their subjects in PROGRAMME_MAP.md before calling an item new.

## Files
- `extract_gap.py` -> `index.tsv` (g, package, entry, kind, cls, how) and `batches/gNN.txt` (compressed full text).
- Verdicts: `verdicts/v_gNN.txt`, one line per entry: `g|v|cluster|rank|what|statement`
  (g = number without the letter; v = a/b/c; cluster+rank for (a) only; what = what the entry is, for g829+;
  statement as in the two passes: (a) item with cote, scans, his words, (b) one line, (c) why).
- `assemble_gap.py` -> `field_experts/GAP_FROM_NOTES_20261117.md` and `.tsv` (columns g, package, entry, what it is,
  verdict, cluster, rank, statement); run it after every few batches so the outputs stay current (unread rows are
  listed as "not yet read").
- Clusters: ANAB, GT, DER, S6, TAME, CYCLES (six consolidated prompts), GS and QUAD (new in the claims pass), or a new
  plain name.

## Progress (last g done; update every 100 entries)
- 17 Nov: extract_gap.py run: 1772 records, 0 missing; 2.69M chars (g1-g828: 0.70M; g829-g1772: 1.99M).
  Full batches batches/g01..g70 (manifest batches_manifest.txt; g01 = g1-g54 ... g19 = g804-g840).
  Digest batches dbatches/d01..d12 for g829-g1772 (title + first 360 chars; manifest dbatches_manifest.txt).
- READING PLAN (compute bound ~600k): g1-g840 in full (batches g01-g19); g841-g1772 as digests (d01 from g841 on,
  skipping g829-g840 already read in full), opening the full text in batches/gNN.txt only where a digest points to a
  possible research item. assemble_gap.py (written) refreshes GAP_FROM_NOTES_20261117.md/.tsv: run it after every
  batch or two.
- Context at the start of this pass: ~860k (carried over from passes 1-2); a compaction is expected soon.
- g01-g03 done (g1-g143; full reading). Research item: g6 DER 2 (G.'s "Thm(?)" for linear coefficients,
  134-8/048-049). Cote 134-8 mapping rows (STRATA/PATHS/BISITE/RESIDUE) -> (c). Provenance (b): g24 Modelizing Story
  copying, g26 SGA 6 XIV corrections sheet, g36 SGA 7 VIII production note, g40 Kimchi typescript. Outputs assembled.
- g04-g05 done (g144-g214). No new research items (cotes 143/141, 144/122-167, 146/100-134 fold into our LM\n  runs or are known: CM main theorem g172, cusp neighbourhoods g200, Massarenti g152). (b): g132, g181, g186, g190.
- g06-g07 done (g215-g302). No new research items; cote 147/138-190 folded into @731 (and @684). (b): g227, g235,
  g252, g255 (dated notices 25 Nov 1981).
- g08-g09 done (g303-g401). No new research items; cote 149 (A, B sections) covered by FLAGGED_149 (B9, ZCF6) and
  known results (Mochizuki 1999/2004, Ozeki 2025, Serre). (b) errors of the page: g336, g342, g369, g374, g387, g392,
  g398, g401.
- g10-g11 done (g402-g502). No new research items; cote 149 C/D (Conjectures A, B, B', fondamentale) covered by
  FLAGGED_149, CYCLOTOMIC_KERNEL, LM6, SECTIONS_OVER_Q. (b): g403, g413, g422, g439, g484, g492 (Carlos = Contou-Carrere?).
- g12 done (g503-g551). No new research items. (b): g526, g529.
- g13 done (g552-g594; cote 149 core complete). No new research items. (b): g554, g556, g589, g592.
- g14 done (g595-g636; cote 14/087-132 Lefschetz/Nakai). No new research items (local Lefschetz for Chow groups = open
  Bloch-Beilinson-type, g601). (b): g595, g596, g610, g611, g615, g630.
- g15 done (g637-g675). No new research items. (b): g656, g673.
- g16 done (g676-g712). No new research items. (b): g708 (15/089 = SGA 4 VIII).
- g17 done (g713-g760). No new research items. (b): g729, g734, g747, g752, g754.
- g18 done (g761-g803). No new research items. (b): g768, g773, g789 (Tohoku = Chevalley 1955).
- g19 done (g804-g840): FULL READING OF g1-g840 COMPLETE. Research items so far: g6 DER 2 only. (b) this batch: g817,
  g825, g828. NEXT: digest batches dbatches/d01 (start at g841) .. d12; 'what' field required for g829+.
- d01-d02 done (g841-g996, digests). No research items. (b): g854, g869, g950, g960, g961, g967, g969, g970, g976,
  g987, g992.
- d03-d04 done (g997-g1161, digests; full text opened for cote 136/095-141 and 235-281, wholly missed by both
  earlier passes, and for the dating entries). Research items: g1048 CYCLES 2 (weight localization and
  'compatible avec multiplication', 136/244-281), g1004 CYCLES 3 (uniqueness conjecture, 136/119-121).
  (b): g998, g1003, g1007, g1010, g1025, g1029, g1063, g1102, g1103, g1113, g1129, g1138-g1142, g1144, g1149.
- d05-d06 done (g1162-g1314). Research item: g1276 ANAB 3 (G.'s converse for elementary U, 149/120).
  (b): g1172, g1291. Cote 147/164-178 items fold into @731; cote 149/091-136 RN-series covered or settled.
- d07 done (g1315-g1398). No research items. (b): g1342, g1349, g1357, g1395. Cote 22+23 (EGA draft) wholly
  in the gap; its questions are answered in the published EGA 0_IV.
- d08 done (g1399-g1484). No research items. (b): g1413 (EGA 0_IV 22.5.10(i) printed example fails as
  displayed), g1415 (our EGA 0_IV transcription swaps u/v in 20.5.7.1, reverses 20.7.2, differs in 20.7.3).
- d09 done to g1556 (g1485-g1556; g1557-g1566 of MPL_72_035-081 go with d10: that package, 100 entries, was
  missed by both earlier passes). No research items. (b): g1490, g1502, g1516 (cote 60 errors of the page).
- d10 done (g1557-g1654; cote 72/035-081, wholly missed before). Research items: g1557 POLY 2 (G.'s pinned
  regular hyperpolyhedra and the equivalence of 72/077), g1558 POLY 3 (the level-N family vs the Farey map of X(N);
  read cote 79). New cluster POLY. (b): g1573, g1577, g1591, g1641.
- d11 done (g1655-g1745; cotes 7-8 package MPL_7_061-072+8_001-078 wholly missed before: its conjectures are
  known or famous open problems). No research items. (b): g1684 (provenance of the reused cote 8 typescripts),
  g1694 (cote 8 slips of the page).
- d12 done (g1746-g1772). ALL 1772 ENTRIES HAVE A VERDICT. (b): g1757 (Récoltes et Semailles draft on the
  reused cote 84 sheets, about autumn 1984).

## DONE (17 Nov 2026)
- 1772 verdicts (assembly: 0 missing, 0 duplicates, 0 extra): (a) 6, (b) 100, (c) 1666.
- Research items: g6 DER 2; g1048 CYCLES 2; g1557 POLY 2; g1004 CYCLES 3; g1276 ANAB 3; g1558 POLY 3.
- Outputs: field_experts/GAP_FROM_NOTES_20261117.md and .tsv (assemble_gap.py). New cluster POLY (Esquisse §4).
- Compute: well past the 600k bound (context carried over from passes 1-2 plus this reading).
