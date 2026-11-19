## Sweep 2, part 1: your gap list (from the broad agent a0c4bb37, Claude Opus 5.5 at effort max, 18 Nov 2026, 20:12 UTC)

The user, 19:2x UTC: [the user's words, omitted] Every entry below is read, placed and merged, not only listed.

**Your entries:** 63, about 9,477 words, in SA20, SA22, SA30.

By class:
- Pro records (research leads, pointers): 47 entries (5,519 words)
- Codex notes on the sheets: 16 entries (3,958 words)

- **The full list** has one row per entry, with its file and line: `results_register/horizontal/sweep2/inputs/<SAnn>/GAP_INDEX.tsv`. Its columns are entry_id, cls, topic, source_file (relative to `C:/Users/user/Documents`), line, heading, label, words, scans and linked_to.
- **The ids** follow one rule, set out in `results_register/horizontal/sweep2/GLOBAL/ID_RULE.md`.
- **New since sweep 1:**
  - Pro packages that NOTES_INDEX missed, or that came back after the inputs were built (09-11 UTC);
  - the Codex notes on the sheets;
  - every Work and Codex-web folder filed since then (rounds 7-9 and round D).

**What to do**
1. Your sweep-2 tables are in `results_register/horizontal/sweep2/SA<nn>/`: copies of your sweep-1 PLACEMENT, OBJECTS, FLAGS, CHECK_EVENTS and TOPIC_NOTES. Extend them there and leave `sweep1/` as it is.
2. Place every entry of your GAP_INDEX files as in sweep 1 (`results_register/horizontal/HORIZONTAL_SWEEP1_BRIEF.md`, steps 1-5), under the entry_id given.
   - Merge an entry into an existing item where it is the same object; new items continue your numbering.
   - In cross_topic, name the global tag ("= H0xx", from `sweep1/GLOBAL/GLOBAL_OBJECTS.tsv`) where an item is a global object.
3. Read the passage wherever his mathematics or a reading is at stake, and record the basis and fidelity honestly.
4. Keep CHECK_EVENTS as in sweep 1. Placing or reading an entry is not a check.
5. After each topic, check in to `results_register/horizontal/sweep2/CHECKINS/<your agent id>.md` with:
   - the time (date -u) and the counts;
   - the five most important flags;
   - the objects that cross into other topics.

**What I do (not yours)**
- The second chats (chatB) and the variant folders: I link them by script.
- The stale and double placements: I settle them in `sweep2/GLOBAL` (STALE_PLACEMENTS.tsv, DOUBLE_PLACEMENTS.tsv) and apply them in the global build. Leave those rows as they are.
- The doubts files (`sweep2/inputs/DOUBTS_INDEX.tsv`) are reading registers. They are joined to items by scan, not read.

**Addition, 20:25 UTC: the control runs of cotes 145 and 148.** CTRL-145, CTRL-145_2, CTRL-148 and CTRL-148_2 (in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns_control/`) have 32 entries of math notes and notes on the sheets: work:CTRL-145#1-6, work:CTRL-145_2#1-6, work:CTRL-148#1-6, work:CTRL-148_2#1-6, and codex:CTRL-*#1-2. They are second readings of pages that SA28's folders also cover. Please place them in sweep2/SA28/PLACEMENT.tsv as variant readings. Put "control run of <folder>" in the note column, and use the item of the entry that reads the same pages. Their headings and file lines are in `sweep2/inputs/UNITS.tsv`.

**By source**

| topic | source | class | entries | words | file |
|---|---|---|---:|---:|---|
| SA20 | codex:C123-01 | Codex notes on the sheets | 2 | 574 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/C123-01/out/C123-01_notes.md |
| SA20 | codex:C123-02 | Codex notes on the sheets | 2 | 512 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/C123-02/out/C123-02_notes.md |
| SA20 | codex:K123-01 | Codex notes on the sheets | 2 | 599 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K123-01/out/K123-01_notes.md |
| SA20 | codex:K123-02 | Codex notes on the sheets | 2 | 504 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K123-02/out/K123-02_notes.md |
| SA20 | codex:K123-03 | Codex notes on the sheets | 2 | 834 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K123-03/out/K123-03_notes.md |
| SA20 | codex:K125-01 | Codex notes on the sheets | 2 | 225 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K125-01/out/K125-01_notes.md |
| SA22 | codex:H66-01 | Codex notes on the sheets | 2 | 649 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/H66-01/out/H66-01_notes.md |
| SA22 | MPL_67_002-052:records:research_leads | Pro records (research leads, pointers) | 46 | 2,669 | grothendieck_archive_transcription_20261110/returns/MPL_67_002-052_unzipped/records/research_leads.md |
| SA22 | MPL_67_053-101:records:research_leads | Pro records (research leads, pointers) | 1 | 2,850 | grothendieck_archive_transcription_20261110/returns/MPL_67_053-101_unzipped/records/research_leads.md |
| SA30 | codex:K147-01 | Codex notes on the sheets | 2 | 61 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K147-01/out/K147-01_notes.md |

## From the broad agent a0c4bb37 (Claude Opus 5.5 at effort max), 18 Nov 2026, about 15:25 UTC

For the record; your topics are done. The lists are in GLOBAL\COVERAGE.tsv and GLOBAL\GLOBAL_OBJECTS.tsv.

- Codex/API folder notes that are in neither list and unplaced: SA20 C123-01, C123-02; SA22 H66-01; SA31 K147-01.
- Your equalities with SA23 on MPL_68_033-056+162-1+162-6 are merged: H0DU, H0DV, H0DS, H0DW (H0KO and H0KY are now aliases of H0DS and H0DW: GLOBALTAG_ALIASES.tsv).
- Your second-pass import for MPL_152+120 (SA20) covers entries that SA10 placed too. The central register should carry each verdict once.
- Correction at 15:30 UTC: every inputs\SA<nn>\codex\<folder>_notes.md file is Codex's "notes on the sheets". None of them is the same file as the Work math notes of that folder (all 221 pairs compared). Those without a codex:<folder>#<n> row: SA20 6, SA22 1, SA30 1, SA31 1 (9 files, about 4k words). The full list is in GLOBAL\COVERAGE.tsv, column codex_only_unplaced.

<!-- AUTO from _broad_tools/build_global.py, 2026-11-18 15:33 UTC -->
## Cross-topic entries for ae4ae3dc17acaa440 (topics SA28 SA29 SA30 SA31 SA20 SA22), built 2026-11-18 15:33 UTC

Tags: GLOBAL\GLOBAL_OBJECTS.tsv gives every item a tag H??? (same object across topics) and a theme TH-nn (related objects). Name the tag in cross_topic ("= H00x") when an item of yours is that object.

### Same object in your topics and another agent's (11)
- H00K: the axioms of a tame topology on cote 120: the graph calculus, finite unions, categorical reconstruction, finite graph d | items SA10-19 SA20-12 | merged by: stated equal (= or 'same') in SA10-19
- H00M: later drafts on tame topology (121/049-073): canonical adapted partitions, incidence orders, conservativity, effective e | items SA11-3 SA20-15 | merged by: stated equal (= or 'same') in SA11-3
- H05G: the 'tubulure' and the 'ombre': where they occur (149/133, a dated 1975 étale-tubular passage), germs and neighbourhood  | items SA10-2 SA20-8 | merged by: stated equal (= or 'same') in SA20-8
- H0DU: the exponential of a locally nilpotent endomorphism or derivation (package MPL_68_033-056+162-1+162-6): nilpotence hypot | items SA22-10 SA23-40 | merged by: stated equal (= or 'same') in SA22-10
- H00L: the 'remords' and whether he resolved it: his own reconsideration, the calculation that convinced him, the December 1981 | items SA10-3 SA20-9 | merged by: stated equal (= or 'same') in SA10-3
- H00O: a Tannakian-type duality over a field extension k'/k (cotes 153, 155): pro-objects, the idealizer quotient, descent data | items SA11-6 SA20-17 | merged by: stated equal (= or 'same') in SA11-6
- H0DV: orientations as a real sign quotient of determinant lines: two-element lemmas, unique morphisms against existence, from  | items SA22-11 SA23-41 | merged by: stated equal (= or 'same') in SA22-11
- H00J: plane trees and their rotations (cote 152): the admissibility rule, orientation torsors, rotation sheets, a permutation  | items SA10-18 SA20-7 | merged by: stated equal (= or 'same') in SA10-18
- H00N: binomial and lambda 'analysers' (cotes 153, 155): products, coaddition, comultiplication, divided powers, optional axiom | items SA11-5 SA20-16 | merged by: stated equal (= or 'same') in SA11-5
- H0DS: positional games ('Jeux de position', cote 68): plays and positions of bounded length, strategies and winning positions, | items SA22-1 SA23-39 | merged by: stated equal (= or 'same') in SA22-1
- H0DW: package apparatus: the reference key to Hua's readings, covers, letter pages, typed and printed supports, his question m | items SA22-A SA23-42 | merged by: stated equal (= or 'same') in SA22-A

### Other agents' items that point to your topics (20)
- SA01-9 (SA01, H00A) -> SA20 [cote 119]: the combinatorial surface of relative positions of an added projective pseudoline (Esquisse §8): scope and gen | its cross_topic: SA11 (cote 154 pseudolines: MPL_154_001-045, 077-126, 127-176, K154); SA01 cote 80 (Systemes de pseudo-droites); Esquisse §8 (cote 119)
- SA10-18 (SA10, H00J) -> SA20 SA20-7 [item id]: the category of word types and plane trees (cote 152): operations, admissibility, orientation torsor, contours | its cross_topic: SA01 (planar maps, cote 88 "Cartes standards"); dessins (SA03?); = H00J (SA20-7)
- SA10-19 (SA10, H00K) -> SA20 SA20-12 [item id]: cote 120 tame-geometry axioms M1-M11 and the graph calculus (amalgams, scalar extension, compact graphs, count | its cross_topic: SA21; SA04-4; = H00K (SA20-12)
- SA10-2 (SA10, H05G) -> SA28 [cote 147]: his terms "tubulure" and "ombre": where the tubular pro-neighbourhood and the shadow are introduced (cotes 150 | its cross_topic: cotes 147, 149, 136, 67 (other topics: SA11? SA12?)
- SA10-3 (SA10, H00L) -> SA20 SA20-9 [item id]: the "Remords": his reconsideration of the realization and its date (December 1981) | its cross_topic: = H00L (SA20-9)
- SA10-8 (SA10, H05L) -> SA28 [cote 147]: stratified homotopy types: exit paths, gerbes and homotopy amalgams; the stratified homotopy hypothesis (compa | its cross_topic: Pursuing Stacks / exit paths (Part II of the handbook outline); cote 147
- SA11-2 (SA11, H05W) -> SA20 SA20-9 [item id]: the "Remords" and his own repair; its date | its cross_topic: SA10-3; H00L (SA10-3, SA20-9)
- SA11-3 (SA11, H00M) -> SA20 [cote 120]: the axiomatics of moderate (tame) spaces in cote 121: adapted partitions, graphs, conservativity, effective ep | its cross_topic: SA10-19 (cote 120); SA21; = H00M (SA20-15)
- SA11-3 (SA11, H00M) -> SA20 SA20-15 [item id]: the axiomatics of moderate (tame) spaces in cote 121: adapted partitions, graphs, conservativity, effective ep | its cross_topic: SA10-19 (cote 120); SA21; = H00M (SA20-15)
- SA11-5 (SA11, H00N) -> SA20 SA20-16 [item id]: analysers (cote 153): binomial and lambda operations, plethories, divided powers, coaddition and comultiplicat | its cross_topic: lambda-rings, plethories (literature); = H00N (SA20-16)
- SA11-6 (SA11, H00O) -> SA20 SA20-17 [item id]: rigidity of tensor categories and reconstruction (cote 155): exactness and faithfulness after diagonal tensori | its cross_topic: Tannakian categories (literature); Deligne; = H00O (SA20-17)
- SA11-8 (SA11, H00A) -> SA20 [cote 119]: the combinatorial surface of relative positions of an added projective pseudoline (Esquisse §8): scope, tame t | its cross_topic: SA01-9 (same package under SA01); SA04-28 (cote 80 Work); Esquisse §8 (cote 119)
- SA21-12 (SA21, H0KB) -> SA20 [cote 120]: 156-3, "Reseaux ... via decoupages" (8 June 1986, sheet III): troncons and sous-troncons, closed tame parts | its cross_topic: SA11-3 (tame axiomatics, cote 121); SA10-19 (cote 120)
- SA21-12 (SA21, H0KB) -> SA20 [cote 121]: 156-3, "Reseaux ... via decoupages" (8 June 1986, sheet III): troncons and sous-troncons, closed tame parts | its cross_topic: SA11-3 (tame axiomatics, cote 121); SA10-19 (cote 120)
- SA21-6 (SA21, H0KJ) -> SA28 [cote 147]: cuttings (decoupages): separating lieux, cone gluing, tubular boundaries, gluing homeomorphisms, the exchange  | its cross_topic: SA10 (MPL_150_001-043 Q1b, 150/012-015, 022-023; 147/140-142)
- SA23-22 (SA23, H0DB) -> SA22 [cote 68]: Cartier theory: logarithm, primitives and group-like elements, Cartier duality, formal groups, exponential (co | its cross_topic: cote 68 (SA23-40: nilpotent exponential and unipotent automorphisms); cote 161-5 (SA23-36: Dieudonne/Cartier duality); P93 X02 (Cartan formu
- SA23-39 (SA23, H0DS) -> SA22 [cote 68]: combinatorial games: winning and losing positions, kernels of graphs, ordinal induction (cote 68) | its cross_topic: cote 68 (outside SA23)
- SA23-40 (SA23, H0DU) -> SA22 [cote 68]: nilpotent exponential and logarithm; unipotent automorphisms and nilpotent derivations; functors in modules (c | its cross_topic: cote 68 (outside SA23); cote 23 (SA23-22)
- SA23-41 (SA23, H0DV) -> SA22 [cote 68]: orientations and Stokes maps; graded determinants and the SK_1 obstruction (cote 68; 162-6 link) | its cross_topic: cote 68 (outside SA23); 162-6 (norm and idele classes)
- SA23-42 (SA23, H0DW) -> SA22 [cote 68]: cote 68 documentary: contents, witnesses, the numeral 82, headings | its cross_topic: cote 68

### Notes of your topics without a PLACEMENT row (4 topics; see GLOBAL\COVERAGE.tsv)
- SA20: NOTES_INDEX rows unplaced 0; Pro packages missing from NOTES_INDEX and unplaced: none; Work folders unplaced: none; Codex/API folder notes on the sheets (inputs\SA20\codex\<folder>_notes.md, not the Work math notes) unplaced: C123-01 C123-02 K123-01 K123-02 K123-03 K125-01
- SA22: NOTES_INDEX rows unplaced 0; Pro packages missing from NOTES_INDEX and unplaced: none; Work folders unplaced: none; Codex/API folder notes on the sheets (inputs\SA22\codex\<folder>_notes.md, not the Work math notes) unplaced: H66-01
- SA30: NOTES_INDEX rows unplaced 0; Pro packages missing from NOTES_INDEX and unplaced: none; Work folders unplaced: none; Codex/API folder notes on the sheets (inputs\SA30\codex\<folder>_notes.md, not the Work math notes) unplaced: K147-01
- SA31: NOTES_INDEX rows unplaced 0; Pro packages missing from NOTES_INDEX and unplaced: none; Work folders unplaced: none; Codex/API folder notes on the sheets (inputs\SA31\codex\<folder>_notes.md, not the Work math notes) unplaced: K147-01

<!-- /AUTO -->
