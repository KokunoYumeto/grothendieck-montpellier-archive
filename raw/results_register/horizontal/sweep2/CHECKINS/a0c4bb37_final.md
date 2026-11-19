# Horizontal sweep 2, part 1: final check-in of the broad agent

By a0c4bb37 (Claude Opus 5.5 at effort max), 18 Nov 2026, 21:27 UTC.

Part 1 covers the work list's items 1, 2 and 8-12 (`results_register/horizontal/SWEEP2_WORKLIST.md`). The tables are in `sweep2/SA<nn>/` and the map is in `sweep2/GLOBAL/`. To rebuild the map, run `python -I -B _tools/make_build_global2.py` and then `python -I -B _tools/build_global2.py`. `sweep1/` is unchanged except for the inboxes.

## Coverage before and after
The measure is against the refreshed inputs (`inputs/UNITS.tsv`): every notes file under one id rule (`GLOBAL/ID_RULE.md`), with the doubts files left out.

| | before part 1 (20:16 UTC) | after (21:26 UTC) |
|---|---:|---:|
| entries | 17,394 (3.09M words) | 17,394 |
| placed | 13,590 | 17,259 |
| linked by script (second chats, variant folders) | 121 | 135 |
| unplaced | 3,683 (about 660k words) | 0 |

**The doubts files** hold 4,558 entries (about 8M words): Pro 850, Codex 3,630, and the doubts of the second chats and variants. They are notation and reading registers, so they are not placed. `GLOBAL/DOUBTS_JOIN.tsv` joins 2,174 of them to the items that place the same cote and scan. The other 2,384 name no scan that a placement cites.

**Out of scope:** the Codex `_audit.md` files, which are audits of the transcription and not notes. The checkpoint-only Pro packages (MPL_15_139-194, MPL_136_328-376 and others) have no notes file. Their records and research leads are placed, and their doubts are in the join.

## Totals

| | sweep 1 | sweep 2, part 1 |
|---|---:|---:|
| placement rows | 14,395 | 18,143 |
| basis: index row, heading, folder map, scan overlap | 13,241 | 14,497 |
| basis: entry read, opening read | 1,063 | 3,505 |
| basis: passage read | 91 (88 agree, 2 understate, 1 overstates) | 141 (137 agree, 2 understate, 2 overstate) |
| items | 799 | 872 |
| global objects (H tags) | 756 | 792 |
| objects in more than one topic | 37 | 64 |
| themes | 55 | 57 |
| flags | 281 | 360 |
| check events | 1,077 (in sweep1/) | 100 more (in sweep2/) |

The 100 new check events break down as:
- 35 second-pass verdicts on MPL_16+47+54+44, imported once in SA18;
- 65 others: a6d42bf6fe2b0d8a8 12, a34c04448e8299803 24, ae4ae3dc17acaa440 12, a28ea31fa17dd65e1 1, and my sub-agents 16 (SA12 6, SA13 6, SA23 4).

**The check register** now holds 25,637 checks on 8,893 ids from 53 files. It changed as follows:
- **At 20:17:** 26,624 rows from 62 files. Every sweep-1 event was counted twice, because the sweep-2 tables started as copies.
- **At 20:34:** I removed the 1,065 copied rows from the sweep-2 files of the finished topics.
- **At 21:15:** 25,649 rows from 57 files. The 90 rows over the 20:17 figure, less the 1,065 removed, are the sweep-2 events written after 20:17.
- **At 21:24:** I removed 12 more copied rows: 11 in a28ea31fa17dd65e1's topics, and 1 in SA13 that the sub-agent had re-quoted. That gives 25,637 rows from 53 files.

The rows removed total 1,077, exactly the sweep-1 events. The sweep-1 files are untouched, and each sweep-2 file holds only sweep-2 events. The 100 left match every agent's reported count, so nothing was lost. The file count fell from 62 to 53 because 9 sweep-2 files held only copied rows (SA03, SA05, SA14, SA16, SA19, SA26, SA27, SA29, SA31), and the register counts only files that have rows.

## What part 1 settled
- **Ids** (ID_RULE.md, ID_ALIASES.tsv): 184 aliases.
  - Label and sub-entry ids such as #R001 and #3:N046.
  - Variant folders, which keep the base name inside (returns/K43-02_2/out/K43-02_mathnotes.md).
  - 21 exact duplicate sections.
- **Stale placements** (STALE_PLACEMENTS.tsv): 6, each checked against its file.
  - MPL_137_002-044#SQ1-2 are now #112-113.
  - work:H66-01#1-2 are codex:H66-01#1-2.
  - work:K32-02#7 and work:K123-02#7 are #6: sweep 1 counted a "### Reading questions" subsection as an entry.
  - The superseded rows in SA09 and SA22 are removed.
- **Double placements** (DOUBLE_PLACEMENTS.tsv, DOUBLE_OBJECTS.tsv). 744 entries were placed in two topics. Each is kept in one owner topic, and the other rows become links.
  - Owner overrides at a6d42bf6fe2b0d8a8's word (OWNER_OVERRIDES.tsv, ITEM_HOMES.tsv): K84-10 and K90-02 go to SA02, K93-13 and K93-07 to SA04.
  - One real disagreement between agents, to read on the page: **H03F**. SA04-9 has "boxed factors checked", while SA32-4 has "computed on the page with a sign conflict".
- **Second chats and variants** (LINKED_PLACEMENTS.tsv): 120 of the 210 chatB entries were linked by label, heading or scans. The rest were placed by a28ea31fa17dd65e1 (SA07, 64) and a65dbdc241d1a129a (SA12, 18). Each variant follows its base or sibling folder.
- **Joins** (MERGES.tsv):
  - The five-point problem is one object (H0HW): SA22-7, SA29-Q1, SA30-6, SA31-Q1 and SA31-5. ae4ae3dc17acaa440 asked for it. The SA29, SA30 and SA31 items are my choice, for part 2 to check.
  - Good reduction via Barsotti-Tate groups on cote 100 is one object: SA04-38 (sweep 1) = SA15-19 (sweep 2). It is the same manuscript, placed from two packages.
  - **Strands**, a layer of their own that does not chain themes:
    - TH-C93, the cote-93 strand. a6d42bf6fe2b0d8a8 asked for one object; its items keep distinct tags that other topics cite.
    - TH-C109, cote 109 across SA25 and SA27.
    - TH-CRYS, crystals, Barsotti-Tate groups and Dieudonné theory across cotes 5-9, 93, 100 and 161. This is my inference from sweep 1, now explicit in SA15-16.
  - Cotes 137-138 are joined across SA08 and SA09 through a34c04448e8299803's own "= SA09-k" statements.
- **Agents' equalities.** A bare "= tag" or "= item" from an agent joins items, even within one topic. "SAnn-k (= H0xx)" after an item id is read as a link to that item, not an equality.

## What part 2 should take (items 3-6), as each agent listed it
- **Mine:**
  - the crystals, Dieudonné and motives dependency picture (TH-CRYS, TH-C93, the motives theme);
  - cote 156 against the tame-topology axioms (156-4 to 156-9: the moutures of Analysis Situs and the GF series to 15 July 1986);
  - the five-point counts against M_{0,5} (H0HW);
  - the scan readings below.
- **a34c04448e8299803:**
  - 716 entries were placed from their heading or folder only and should be read;
  - K157-3-23, his "Contre-exemples pour la totale asphéricité", against the research runs and HTA1/HTA2;
  - chapter XII against the vertical finding that XII Théorème 2 fails;
  - a scan-to-manuscript concordance for cote 157;
  - the question "f^! existe-t-il pour X -> e ?" (157-1 scan 3);
  - Mme Hoàng Xuân Sính's text in cotes 103 and 135 is credited to her.
- **a28ea31fa17dd65e1:**
  - 1,012 SA15 entries were placed from their opening words only;
  - the letter to Mumford (cote 13, 1 Nov 1965, "a bit rash with the conjectures"): which conjectures;
  - whose hand wrote the margins of the Tate-Deligne Formulaire (H63-04) and the "Gribouillis de Tate";
  - cote 47 scan 009, the χ factor;
  - 57:144, whether "à vérifier" is the Fourier check;
  - the sweep-1 pointers into its topics (SA20-10, SA20-12, SA31-13, SA23-24).
- **a6d42bf6fe2b0d8a8:**
  - 93/100, 93/113 and 93/117: suspected slips;
  - 84/120: a lemma hypothesis;
  - the signs in the χ-split extensions (SA02-4);
  - exercise 22 a) at 93/052;
  - cote 102 headed "Pour EGA VI".
- **ae4ae3dc17acaa440:**
  - characteristic 5 at 67/086;
  - √3 against 3 at 67/098;
  - the date of cote 67 (1977-78, not 1983-84);
  - cote 123's letter to Kostant;
  - CTRL-145 and CTRL-145_2 read the group on 145/023-033 differently.
- **My sub-agents:**
  - SA12 F23: three witnesses that Prop. 4 breaks where reducedness is lost;
  - SA12 F26: 29/183, compactness;
  - SA12 F31: 37/094, whether formal smoothness is local;
  - SA12 F24 and F25: the E8 plate 33/075 and 33/090;
  - SA13: the sign of the parallelogram identity at 36/56; cote 32 scans 31-32, which are Deligne's letter;
  - SA23 F15: 2/045, normalization against O_C;
  - SA23 F14: the Fuglede-Kadison determinant of cote 1 (my sub-agent's identification).
