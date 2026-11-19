# What is where: Autour de Pursuing Stacks (cotes 103, 104, 105, 109)

Built by Claude Opus 5.5 at effort max (agent a34c04448e8299803) in horizontal sweep 2, part 2, 18 Nov 2026, from this folder's tables (PLACEMENT, OBJECTS, FLAGS, DEPENDS, CLAIM_LINKS, UNIT_LINKS, CORRECTIONS).

Items are in mathematical order. For each item the report gives:
- where it is: cotes, scans, and the packages or folders holding its notes (paths in the key at the end);
- its status as his pages show it;
- what it uses and what uses it;
- the research statements linked to it, its flags and its entries.

'My reading' marks a dependency I inferred from the item statements, not one written on his pages or in the notes.

**Counts:** 21 items; 388 entries (entry-read 9, index-row 370, passage-read 9); 9 flags in FLAGS.tsv; 8 dependency rows; 37 claim links; 1 companion-unit links; 3 corrections.

## Cote 105: the excision axioms and localizers

### SA25-2 · the strengthened excision axioms W7, W7 bis ('forme renforcee de W7'), W8 bis and the reverse implications
- **Where:** 105. Notes in: MPL_105.
- **Status:** proposed as axioms; the derivation from the derivator axioms is marked 'a verifier' by him.
- **Statement:** W7 bis (scan 52): for a diagram X_a <- X_0 -> X_b in Cat with total category X over Phi, i_a in W <=> i'_a in W and i_b in W <=> i'_b in W; W8 bis for cartesian maps of such diagrams. On scan 46 the square criterion is marked 'a verifier (ou a mettre en axiome sur les derivateurs)'.
- **Uses:** none recorded · **Used by:** SA25-7, SA25-9, SA25-10, SA25-11
- **Research:** POLES:B.8; POLES:G.2; TOTAL_ASPHERICITY:A.13 (refutes for W_infty (the reverse clauses)); TOTAL_ASPHERICITY:A.14 (proves for W_R); 9 register statements cite these pages (DER_LOCALIZERS:A2.5, DER_LOCALIZERS:A2.8, DER_LOCALIZERS:A.1, DER_LOCALIZERS:A.3, DER_LOCALIZERS:A.5, DER_LOCALIZERS:A.6, DER_LOCALIZERS:A.7, DER_LOCALIZERS:A.9, …)
- **Other topics:** Les Derivateurs XII ms. 75-76 (W(7 bis)); research runs TOTASPH A.9, A.13, POLES B.8, G.2
- **Flags:** different readings (Pro vs Hua) (1); FLAGS.tsv rows naming it: 2
- **Entries:** 17 (index-row 14, passage-read 3)

### SA25-9 · the five-lemma proposal and the same-sheet retraction
- **Where:** 105. Notes in: MPL_105.
- **Status:** the extra five-lemma implication unproved; a presumption cancelled without a full proof.
- **Uses:** SA25-2 · **Used by:** none recorded
- **Entries:** 4 (index-row 4)

### SA25-10 · the classification conclusion from reverse excision ('homology only')
- **Where:** 105. Notes in: MPL_105.
- **Status:** not on the pages (a caution about our records).
- **Statement:** Failure of the strengthened axiom for W_inf does not classify every localizer satisfying it (note R21).
- **Uses:** SA25-2 · **Used by:** none recorded
- **Research:** DER_LOCALIZERS:A.7; DER_LOCALIZERS:A.9 (the runs side with NEW_RESULTS 7 against 8)
- **Other topics:** research runs POLES D.1, F.14, DER_LOCALIZERS A.7
- **Flags:** notes contradict each other (1)
- **Entries:** 1 (index-row 1)

### SA25-7 · derivator axioms for localizers: W = W_D?, shifted derivators, constant against locally constant coefficients, the dualizing object
- **Where:** 105. Notes in: MPL_105.
- **Status:** questions; no general equality proved.
- **Statement:** The heading 'Dem. de W7, W(7bis) et W=W_D ?' (scan 43); a proposed derivator axiom turns into a stability question; the existing derivator axioms 'seem insufficient'.
- **Uses:** SA25-2 · **Used by:** none recorded
- **Research:** Hua finding 105-derivator-crible-excision (credited) (Hua's 'from the derivator axioms alone' overstates the page); 10 register statements cite these pages (DER_LOCALIZERS:A2.1, DER_LOCALIZERS:A2.2, DER_LOCALIZERS:A2.3, DER_LOCALIZERS:A2.4, DER_LOCALIZERS:A2.9, DER_LOCALIZERS:A2.10, DER_LOCALIZERS:A2.11, DER_LOCALIZERS:A2.12, …)
- **Other topics:** research runs GALOIS (W_D, W_D^lc), REVLOC G.2 (every accessible W is W_D)
- **Entries:** 8 (index-row 7, passage-read 1)

## Cote 105: model structures from intervals

### SA25-5 · interval generators and the factorization: building C cap W from intervals, smallness, transfinite composites
- **Where:** 105. Notes in: MPL_105.
- **Status:** programme with factorizations admitted (self-flagged).
- **Statement:** Interval pushout-products and a universal-W condition on a Lawvere object generate the trivial cofibrations; factorization is admitted for the time being; taking all intervals may spoil smallness; the ordinal bound to be fixed.
- **Uses:** none recorded · **Used by:** SA25-6
- **Research:** DER_LOCALIZERS:B.1 (proves (hypotheses 1-5 give both weak factorization systems)); 11 register statements cite these pages (DER_LOCALIZERS:B.1, DER_LOCALIZERS:B.2, DER_LOCALIZERS:B.3, DER_LOCALIZERS:B.4, DER_LOCALIZERS:B.5, DER_LOCALIZERS:B.7, DER_LOCALIZERS:B.9, DER_LOCALIZERS:B.10, …)
- **Other topics:** research run DER_LOCALIZERS B (interval recognition): link; Hua findings register 105-interval-anodyne-generators
- **Flags:** different readings (Pro vs Hua) (1); FLAGS.tsv rows naming it: 1
- **Entries:** 18 (index-row 18)

### SA25-6 · a Quillen model structure on Cat from a localizer W: M1-M5, orthogonality, pushout-products, retracts, saturation
- **Where:** 105. Notes in: MPL_105.
- **Status:** programme; several steps self-flagged.
- **Statement:** The axioms M1 and M5 'not yet known'; which orthogonal class; pushout-product closure to check; saturation versus retract stability questioned; 'strict Quillen triple'.
- **Uses:** SA25-5 · **Used by:** SA25-8, SA25-11
- **Research:** 2 register statements cite these pages (DER_LOCALIZERS:B.6, DER_LOCALIZERS:B.8)
- **Other topics:** Thomason model structure; Cisinski Asterisque 308
- **Entries:** 24 (index-row 24)

### SA25-8 · fibrations: path projections as W_inf-fibrations, model against intrinsic fibrations, properness, Kan against Serre
- **Where:** 105. Notes in: MPL_105.
- **Status:** questions; a path-space fibration question cancelled.
- **Uses:** SA25-6 · **Used by:** none recorded
- **Other topics:** research runs POLES C, BISITE A-B, RESIDUE C-D
- **Entries:** 6 (index-row 6)

### SA25-11 · the last page: a programme of strengthened corollaries
- **Where:** 105. Notes in: MPL_105.
- **Status:** stated as a programme.
- **Uses:** SA25-2, SA25-6 · **Used by:** none recorded
- **Entries:** 3 (index-row 3)

### SA25-12 · the Lawvere-object criterion and its proof obligation
- **Where:** 105. Notes in: MPL_105.
- **Status:** proof obligation open (note R31).
- **Entries:** 2 (index-row 2)

## Cotes 103, 104 and 109

### SA25-19 · cote 103 (H103-01, H103-02; catalogue: correspondence on Sinh's thesis, 1974): an annotated copy of Mme Hoang Xuan Sinh's note 'Esquisse d'une theorie des Gr-categories' ('9/74 Envoyé par Grothendieck'); his letters to Deligne ('…
- **Where:** 103 scans 2-74. Notes in: codex:H103-01, codex:H103-02.
- **Status:** letters and an annotated note; open steps marked (Codex notes table).
- **Statement:** Codex's notes list open steps of both texts. Those of scans 2-7 are sentences of Sinh's typed note, one with a handwritten insertion ('on [doit] retrouver bien sûr le premier invariant de Postnikov'); those of scans 9-17 are his letters ('Je sais prouver (sauf erreur) ...', 'Peut-on court-circuiter sa théorie ...').
- **Other topics:** SA24-38 (Sinh's note again in cote 135); SA24-40 (letters to Breen 1974-75)
- **Flags:** attribution: Sinh's typed note (1); FLAGS.tsv rows naming it: 1
- **Entries:** 4 (entry-read 1, passage-read 3)

### SA25-20 · cote 104 ('Champs (stacks) 1', copies of handwritten notes; H104-01, H104-02): composition of homs and a missing condition, a Gr-stacks passage beside an English typescript (scans 2-9); facets, a reduced M, 'b) est-il conséquence…
- **Where:** 104 scans 2-12. Notes in: codex:H104-01, codex:H104-02.
- **Status:** open questions marked by him (Codex notes table).
- **Statement:** 'il manque encore une condition pour composer les hom' (scan 9); the questions of scan 12 are his.
- **Entries:** 4 (entry-read 4)

### SA25-21 · cote 109 (H109-01 to H109-03; 1983-84): the edition of Pursuing Stacks: a terminology list, 'Reflexions Mathématique[s]' with Pursuing Stacks as its first volumes, 'Comments on Pursuing Stacks', his correction lists keyed to type…
- **Where:** 109 scans 2-84. Notes in: codex:H109-01, codex:H109-02, codex:H109-03.
- **Status:** his correction lists (Codex notes table).
- **Statement:** Corrections and queries keyed to page and line of the Pursuing Stacks typescript.
- **Other topics:** = SA27-25 (cote 109, K109-01: tables and corrections for the edition); SA24-SA27 (Pursuing Stacks)
- **Flags:** ; FLAGS.tsv rows naming it: 1
- **Entries:** 6 (entry-read 4, passage-read 2); companion units: 1

## Context and the lens

### SA25-1 · cote 105 ('Champs (stacks) 2'): titles, internal paginations, reused typescript, dates
- **Where:** 105. Notes in: MPL_105.
- **Status:** on the pages (codicological).
- **Statement:** Two substantive internal headings, English and French paginations, a reused typescript page 90, no total length declared.
- **Flags:** ; FLAGS.tsv rows naming it: 1
- **Entries:** 16 (index-row 16)

### SA25-3 · 'totalement aspherique => filtrant' does not occur in cote 105
- **Where:** 105. Notes in: MPL_105.
- **Status:** not on these pages.
- **Other topics:** Les Derivateurs II ms. 36ter
- **Entries:** 1 (index-row 1)

### SA25-4 · relative Theorem A is not stated in cote 105
- **Where:** 105. Notes in: MPL_105.
- **Status:** not on these pages.
- **Other topics:** Les Derivateurs XVI; research run REVLOC F.1
- **Entries:** 1 (index-row 1)

### SA25-13 · what the package adds; the variance of the final Phi drawing
- **Where:** 105. Notes in: MPL_105.
- **Status:** not checked.
- **Entries:** 3 (index-row 3)

### SA25-14 · the Derivateurs companion's NEW_RESULTS and three addenda mapped onto cote 105
- **Where:** 105. Notes in: MPL_105.
- **Status:** not on these pages.
- **Flags:** Derivateurs lens (15)
- **Entries:** 15 (index-row 15)

### SA25-15 · research-run family STRATA mapped onto cote 105
- **Where:** 105. Notes in: MPL_105.
- **Status:** not on these pages.
- **Flags:** Derivateurs lens (10)
- **Entries:** 10 (index-row 10)

### SA25-16 · research-run family PATHS mapped onto cote 105
- **Where:** 105. Notes in: MPL_105.
- **Status:** not on these pages.
- **Flags:** Derivateurs lens (76)
- **Entries:** 76 (index-row 76)

### SA25-17 · research-run family BISITE mapped onto cote 105
- **Where:** 105. Notes in: MPL_105.
- **Status:** partial antecedents for some.
- **Flags:** Derivateurs lens (113)
- **Entries:** 113 (index-row 113)

### SA25-18 · research-run family RESIDUE mapped onto cote 105
- **Where:** 105. Notes in: MPL_105.
- **Status:** partial antecedents for some.
- **Flags:** Derivateurs lens (56)
- **Entries:** 56 (index-row 56)

## Corrections and refinements (CORRECTIONS.tsv)

- codex:H103-01#1, attribution: its rows for scans 2-7 are sentences of Sính's typed note; only 'doit' (scan 4) is handwritten [images 103/2, 103/4; decided]
- SA25-7, reading: Hua's finding 105-derivator-crible-excision (credited): 'from the derivator axioms alone' overstates scan 46 ('à vérifier (ou à mettre en axiome sur les dérivateurs)') [sweep 1, transcription; decided on the transcription]
- SA25-10, refinement: NEW_RESULTS 7 and 8 contradict in wording ('homology localizers only'); the runs side with 7 [DER_LOCALIZERS:A.7, A.9; decided]

## Key: where the notes are

- MPL_105: `results_register/horizontal/inputs/SA25/pro/MPL_105_notes.md`
- codex:H103-01: `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/H103-01/out/H103-01_notes.md`
- codex:H103-02: `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/H103-02/out/H103-02_notes.md`
- codex:H104-01: `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/H104-01/out/H104-01_notes.md`
- codex:H104-02: `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/H104-02/out/H104-02_notes.md`
- codex:H109-01: `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/H109-01/out/H109-01_notes.md`
- codex:H109-02: `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/H109-02/out/H109-02_notes.md`
- codex:H109-03: `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/H109-03/out/H109-03_notes.md`
