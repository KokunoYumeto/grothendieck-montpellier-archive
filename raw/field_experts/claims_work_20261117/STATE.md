# Claims reader (Claude Opus 5.5 at effort max), working state, 17 Nov 2026

Brief (the authority): `field_experts/BRIEF_CLAIMS_READER_20261117.md`. Reread it after any compaction, then this file.
Same agent as the follow-ups pass (a9ebc3d6); that pass is DONE (`FOLLOWUPS_FROM_NOTES_20261117.md/.tsv`, @1-@1669).

## Scope
- `field_experts/GROTHENDIECK_CLAIMS_MAP_20261117.tsv`: 1387 rows, numbered #1-#1387 in table order.
- In scope: the 1137 rows whose `runs` cell is empty (50 packages). All 1137 extracted, 0 missing.
- `numbered_index.tsv`: n, package, entry (exact), kind, subjects, for the 1137 in-scope rows only.
- Reading files: `cbatches/k01..k31.txt` (compressed like the follow-ups pass; 1.16M chars; manifest in
  `batches_manifest.txt`). Script: `extract_claims.py`.

## Verdict format (`verdicts/v_kNN.txt`, one line per entry)
n|v|cluster|rank|statement
- v: a = research item, b = edition matter, c = nothing further
- cluster (a only): ANAB, GT, DER, S6, TAME, CYCLES (the six consolidated prompts of
  UNPROMPTED_IDEAS_AUDIT_20261117.md), or NEW-<plain name>
- rank (a only): 1 decides a question G. marks as central or a block of a companion; 2; 3
- statement: (a) the item to prove or refute, cote and scans, his words where they fix it;
  (b) one line; (c) why: known result (name it), settled in the notes/next pages, duplicate of @n / #n, too local.
- Before calling an (a) new: grep PROGRAMME_MAP.md and HEADLINE_RESULTS.md (notes_headlines/).

## Assembly
- `assemble_claims.py` (to write) -> `field_experts/CLAIMS_FROM_NOTES_20261117.md` and `.tsv`
  (TSV columns: #n, package, entry, verdict, cluster, rank, statement).
- Final message: the counts, and the ten strongest research items, one line each (#n, cote, scans, statement,
  cluster, rank).

## Progress (last #n done; update every 100 entries)
- k01-k04 done (#13-#226; 143 entries): verdict files v_k01..v_k04. Research items so far: #133 TAME 1 (mobility
  stratification + Conjecture 1, cote 121), #189 GS 3 (cote 131, example for 8°). Cluster GS = new: group schemes,
  representability and descent (cotes 56, 90, 91, 131; LM1 line).
- Conventions used: "part of @n" / "folded into #n" / "duplicate of @n" for (c); @n = follow-ups items
  (FOLLOWUPS_FROM_NOTES_20261117.md). Cote 136 (PD de Rham) -> @305/@304; cote 155 -> @237; cote 153 -> @215;
  cote 131 criterion -> @247; cote 121/065 -> @210; cote 11 bivariant -> @120.
- Context at start of this pass: ~815k (carried over from the follow-ups pass); compaction expected.
- k05-k06 done (#227-#297; total 213 entries). New research item: #243 CYCLES 2 (automorphisms of the PD de Rham
  functor, 136/162-188, Hua 136-automorphism-group-scheme). Provenance leads: #62 (cote 11 typescript ~ Mumford GIT),
  #279 (cote 136 typescript ~ SGA 7 IX), #88 (cote 56 = SGA 3 XII draft).
- k07-k10 done (#298-#428; total 344 entries). New research items: #309 GT 2 (profinite envelope of the category of
  surfaces with finite covers, 142/009-017), #328 GT 2 (unit multiplier => automorphism?, 142/025). Cote 142/018-021
  -> @355; 142/090-100 -> @435.
- k11-k14 done (#429-#608; total 496 entries). New research item: #468 ANAB 3 (faithfulness over fields finite over
  the field of moduli, 142/096). Cote 146 -> @553/@570/@603/@605; 144/168+148 -> @516; 147 basics known (DM, Knudsen).
- k15-k18 done (#609-#788; total 660 entries). No new research items: 147/079-190 -> @672/@684/@731 and #133
  (147/181-190 stratification); cote 14 motives -> @792; 148/029-072 -> @516.
- k19-k20 done (#789-#946; total 733 entries). No new research items: cote 150 -> @835/#133; 151 -> @210;
  120 -> @160; 154 -> @944; 156 -> @1003/@1008/@1039; cote 14 Albanese -> @792.
- k21-k22 done (#947-#1031; total 813 entries). New research item: #964 CYCLES 3 (places by motivic torsors,
  15/207-227; 18/043-062 lattice comparisons folded in). Period conjecture witnesses -> (b) #973, #976, #978.
- k23-k24 done (#1032-#1095; total 875 entries). New research item: #1039 GS 3 (converse in SGA 3 X 5.11 bis,
  31/014). Provenance leads: #1082 (cote 33 Coxeter/root typescript ~ Bourbaki ch. VI), #1094 (EGA IV 19.7.1).
- k25-k26 done (#1096-#1181; total 957 entries). No new research items (cote 33/34 = SGA 4/5/7 drafts, known;
  cote 36 = SGA 7 VII-IX drafts). Provenance leads #1144 (analysis typescript), #1173 (cote 36 quotients ~ GIT).
  NB: v_k25 had a stray line for #1114 (out of scope) - removed.
- Totals above corrected 17 Nov by script (cumulative line counts of the verdict files); the earlier running
  totals were miscounted.
- k27-k31 done (#1182-#1387; total 1137 entries = the whole scope; last #n done: #1387). New research item: #1264
  QUAD 3 (cote 84/121, non-étale biquadratic fibre of the contracted triple product). New cluster QUAD: quadratic
  algebras and covers over a general base (cote 84). Cotes 36 (orthogonality), 39, 43, 57, 60, 62, 84, 90, 91, 93:
  folded into @1370-@1402 (36), @1387 (39), @1146/@1415/@1420/@1430 (43), @1447-@1469 (57), @1586/@1600 (84),
  @1610/@1613 (90+91), @1641/@1646/@1649/@1659/@1662 (93), or known (SGA 6 XIII, Artin, Greenberg, Messing,
  Mazur-Messing, Voight 2016, Murre 1965, Olivier 1968, ...).
- Verified by script: 1137 verdicts, 0 missing, 0 extra, 0 duplicates, 0 format errors.
  Counts: (a) 9, (b) 115, (c) 1013.
- DONE 17 Nov 2026: assemble_claims.py run (index 1137, verdicts 1137, missing 0, extra 0, duplicates 0; 50 packages).
  Outputs: field_experts/CLAIMS_FROM_NOTES_20261117.md (301 lines) and .tsv (1137 rows + header).
  Counts: (a) 9, (b) 115, (c) 1013. Research items: #133 TAME 1; #309, #328 GT 2; #243 CYCLES 2; #964 CYCLES 3;
  #468 ANAB 3; #1039, #189 GS 3; #1264 QUAD 3. None in DER or S6. Final message sent to the coordinator.
