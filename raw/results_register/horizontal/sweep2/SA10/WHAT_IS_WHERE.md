# SA10: stratified spaces (cotes 150, 151, 152, 120): what is where

Claude Opus 5.5 at effort max, a6d42bf6fe2b0d8a8, horizontal sweep 2 part 2, 2026-11-18.

The topic is "Espaces stratifiés", part 1. It holds:
- **Cote 150:** stratifications, conical neighbourhoods and collars, the reconstruction of a stratified space, pro-neighbourhoods of strata with their bands and flags.
- **Cote 151 (1981):** the stratified topos.
- **Cote 152:** word types and plane trees.
- **Cote 120:** his tame-geometry axioms M1-M11.

Four requested questions recur in every package: tubulure and ombre, the Remords, o-minimality, Shiota. They are the notes' research.

Heavy notes: five Pro packages (GPT-6 Astra, ChatGPT Pro mode). The second pass of 17 Nov (Claude Opus 5.5 at effort max) checked them against the scans; its 282 verdicts are now check events, and its corrections are in CORRECTIONS.tsv. There are no Work or Codex notes.

One research run reads these pages: EXIT_TOWER, on cote 150, folios 9 and 15-16.

How to read an entry:
- **Where:** cote and scans, the notes it is in (package or folder), and the notes files. Scans are the PDF pages of the cote in `grothendieck_archive_montpellier`.
- **Depends:** what the item uses and what uses it, with the basis: his page, our note, or a proof (ours).
- **Claims:** his claims on the item, linked to what proves, refutes or refines them (CLAIM_LINKS.tsv).
- **Units:** the companion units that discuss it (UNIT_LINKS.tsv).
- **Flags, corrections:** from FLAGS.tsv and CORRECTIONS.tsv.

## Stratifications and their neighbourhoods (cote 150)

### SA10-6: stratifications: partitions, preorders, faithful and smallest stratifications, local stratifications and descent

- **Status on his pages:** defined; several claims conditional. **Kind:** definition.
- **Where:** cote 150, scans 4,38,181-182.
- **Notes (8 entries):** MPL_150_001-043 (8).
- **Notes files:** `inputs/SA10/pro/MPL_150_001-043_notes.md`.
- **Depends:** used by: SA10-14 (his page), SA10-7 (his page).

### SA10-7: conical neighbourhoods, collars, strict and cylindrical structures, equisingularity, and the reconstruction of a stratified space from its strata and gluing data

- **Status on his pages:** stated; self-flagged revisions (F01-F14). **Kind:** definition/theorem (stated).
- **Where:** cote 150, scans 12,14-16,18,23,30-31,37,39,59,128,133,140,161,177,179-182,187-190.
- **Notes (59 entries):** MPL_150_001-043 (58); MPL_150_044-084 (1).
- **Notes files:** `inputs/SA10/pro/MPL_150_001-043_notes.md`; `inputs/SA10/pro/MPL_150_044-084_notes.md`.
- **Depends:** used by: SA10-12 (his page); uses: SA10-2 (our note), SA10-6 (his page).
- **Claims:**
  - SA10-C1 (150/28-30): "the stratification of the moduli of stable curves on folio 9: its intervals and intersections of strata". **proves (research run)**: EXIT_TOWER:A.1, A.2, A.3 (Proved): every interval of the poset of stable graphs G_{g,n} is Boolean; pairs with a common lower bound have an infimum exactly for g = 0, n >= 3; g = 1, 1 <= n <= 3; (g,n) = (2,0); X_G meets X_G' in the union of the X_H below both.
  - SA10-C2 (150/39-42): "the face and flag assertions of folios 15-16 (the run's Part A(e), formulated from these folios)". **refutes in part; proves in part (research run)**: EXIT_TOWER:A.11 (Refuted): raw oriented faces fail (ii) and (iv); EXIT_TOWER:A.13 (Refuted): an unpinned flag need not give the cartesian square, at type (3,0); EXIT_TOWER:A.12 (Proved): local triviality of the deployed family and its lattice monodromy.
  - SA10-C3 (150/33-42): "the reconstruction of a stratified space from its strata and links: the reconstruction (19), the theorem on 035, the flag presentation 039-0". **his claim (stated)**: the second pass (17 Nov) keeps the notes against the scans; no proof is checked.
- **Corrections:** MPL_150_001-043#53 (scans 190): conical neighbourhoods, collars, strict and cylindrical structures, equisingular -> correct: (precision): 033 l. 50 now reads (20)ⓐ "Les X_β disjoints" (#12), a con; MPL_150_001-043#63 (scans 181): conical neighbourhoods, collars, strict and cylindrical structures, equisingular -> correct: The right margin (039 l. 29) reads "Cela est trop faible, \unsure{si on; MPL_150_001-043#65 (scans 39,188): conical neighbourhoods, collars, strict and cylindrical structures, equisingular -> correct: (quotation): 041 l. 37-39 reads "b̲ est loc.^t un morphisme bord (i.e. ; MPL_150_001-043#66 (scans 188): conical neighbourhoods, collars, strict and cylindrical structures, equisingular -> correct: Drop the last sentence: "discrète" is not on the page (042 l. 11 reads ; MPL_150_001-043#80 (scans 181): conical neighbourhoods, collars, strict and cylindrical structures, equisingular -> drop: 019 l.10 has no inserted "f ?". The ink above "implique" is the "(X_i)" of; MPL_150_001-043#83 (scans 181): conical neighbourhoods, collars, strict and cylindrical structures, equisingular -> correct: 031 l. 22-25 now reads: "Une stratification précylindrique resp. cylind; MPL_150_001-043#88 (scans 181): conical neighbourhoods, collars, strict and cylindrical structures, equisingular -> correct: (quotation): As R41: "Cela est trop faible, \unsure{si on veut\ | = pou.
- **Flags:** note overstates or misreads the page (2).

### SA10-12: pro-neighbourhoods of strata and their restrictions: bands, flags, gluing formulas, strict flags, the band lemma, the spectral sequence (cote 150, scans 44-84)

- **Status on his pages:** constructed; several claims conditional or self-flagged. **Kind:** construction.
- **Where:** cote 150, scans 65,80-81.
- **Notes (64 entries):** MPL_150_044-084 (64).
- **Notes files:** `inputs/SA10/pro/MPL_150_044-084_notes.md`.
- **Depends:** used by: SA10-15 (his page); uses: SA10-7 (his page).
- **Claims:**
  - SA10-C5 (150/44-84): "the band lemma and the gluing formulas of pro-neighbourhoods". **his claim**: none; several steps conditional or self-flagged.
- **Corrections:** MPL_150_044-084#16 (scans ): pro-neighbourhoods of strata and their restrictions: bands, flags, gluing formul -> correct: the margin's hook arrow has a written target: `V_{ij}^{\unsure{b}}=V_i\; MPL_150_044-084#19 (scans ): pro-neighbourhoods of strata and their restrictions: bands, flags, gluing formul -> correct: the label: "(69)" is only in the margin, "on voit que dans ce cas on a ; MPL_150_044-084#38 (scans ): pro-neighbourhoods of strata and their restrictions: bands, flags, gluing formul -> correct: The struck datum in (37) is φ₂ (058 l.27, #6; Hua p. 57 agrees): "et on; MPL_150_044-084#42 (scans ): pro-neighbourhoods of strata and their restrictions: bands, flags, gluing formul -> correct: The margin (067 l.13-15, #21) reads "que le bord soit la réunion des Σ_; MPL_150_044-084#45 (scans ): pro-neighbourhoods of strata and their restrictions: bands, flags, gluing formul -> correct: the margin reads "à condition d'avoir ajusté de façon **évidente** les ; MPL_150_044-084#47 (scans ): pro-neighbourhoods of strata and their restrictions: bands, flags, gluing formul -> correct: as V05: the target is read (doubtfully) as V_ij, so the queried map is ; MPL_150_044-084#52 (scans ): pro-neighbourhoods of strata and their restrictions: bands, flags, gluing formul -> correct: the anchor: The criterion "On a lissité (à tous les coups) ssi la suite; MPL_150_044-084#53 (scans ): pro-neighbourhoods of strata and their restrictions: bands, flags, gluing formul -> correct: 048 l. 11: he struck "semi" and wrote "pré" above it: "un espace \inser; MPL_150_044-084#59 (scans ): pro-neighbourhoods of strata and their restrictions: bands, flags, gluing formul -> correct: The step reads "mais comme Σ*_ii → Σ*_i est une imm. rare, on doit avoi; MPL_150_044-084#72 (scans ): pro-neighbourhoods of strata and their restrictions: bands, flags, gluing formul -> correct: its anchor "protopos de raccord" is a doubtful margin word (U51), and t.

### SA10-14: the last section of cote 150 (scans 85-99): conditions Strat 1-5, "non dense", metrizability

- **Status on his pages:** stated; one sentence dropped by the second pass. **Kind:** definition/theorem (stated).
- **Where:** cotes 150+151, scans 85-89,91-93,95-99,132,134,140,145,150,153,157,161,177,181,185,187,190.
- **Notes (18 entries):** MPL_150_085-099+151_001-031 (18).
- **Notes files:** `inputs/SA10/pro/MPL_150_085-099+151_001-031_notes.md`.
- **Depends:** uses: SA10-6 (his page).
- **Corrections:** MPL_150_085-099+151_001-031#2 (scans 85,134,177): the last section of cote 150 (scans 85-99): conditions Strat 1-5, "non dense", m -> correct: The objects listed are Σ_i, Σ_{i_0…i_n}, Σ_J, **Σ_J^L** (l.7, row 1: ex; MPL_150_085-099+151_001-031#3 (scans 86,98,161): the last section of cote 150 (scans 85-99): conditions Strat 1-5, "non dense", m -> correct: The two "≟" stand (l.20, l.21). Correct the frame: the first formula of; MPL_150_085-099+151_001-031#4 (scans 87,157): the last section of cote 150 (scans 85-99): conditions Strat 1-5, "non dense", m -> correct: (75) reads **T_{Σ_J,Σ_{I'}} = Σ_{I'} ∩ ⋃_{j∈J} T_j (= Σ_{I'} ∩ ⋃_{j∈J̄}; MPL_150_085-099+151_001-031#5 (scans 88,145,190): the last section of cote 150 (scans 85-99): conditions Strat 1-5, "non dense", m -> correct: The intrinsic meaning "(dans une catégorie isotopique convenable)" is c; MPL_150_085-099+151_001-031#10 (scans 92,132,181): the last section of cote 150 (scans 85-99): conditions Strat 1-5, "non dense", m -> drop: (resolved): The page reads "i.e. j<i ⇒ X_j \uline{rare} dans X_i" (l.14, r; MPL_150_085-099+151_001-031#11 (scans 93,153,181): the last section of cote 150 (scans 85-99): conditions Strat 1-5, "non dense", m -> correct: Formulas unchanged; NB box completed "X^*_{J∪K} = X^*_J ∪ X^*_K" (094 l; MPL_150_085-099+151_001-031#12 (scans 95,140,145): the last section of cote 150 (scans 85-99): conditions Strat 1-5, "non dense", m -> correct: The qualifier is certain: "(X métrisable)" (l.9, row 35; Hua batch-05's; MPL_150_085-099+151_001-031#14 (scans 97,157): the last section of cote 150 (scans 85-99): conditions Strat 1-5, "non dense", m -> correct: Flag confirmed (l.10). The hypothesis on Z: "si Z est ~~fermé~~ une par; MPL_150_085-099+151_001-031#16 (scans 86,98,161): the last section of cote 150 (scans 85-99): conditions Strat 1-5, "non dense", m -> correct: The second line of (106) reads V_J^{L ~~[glyph]~~} = V_J ∩ X^*_L **\uns; MPL_150_085-099+151_001-031#17 (scans 99,150): the last section of cote 150 (scans 85-99): conditions Strat 1-5, "non dense", m -> correct: Add: the line before (110) began with "clairement", which he struck and.
- **Flags:** note overstates or misreads the page (3).

### SA10-2: his terms "tubulure" and "ombre": where the tubular pro-neighbourhood and the shadow are introduced (cotes 150, 151, 147, 149, 136, 67)

- **Status on his pages:** used, not defined, on these pages. **Kind:** reading question (requested).
- **Where:** cote 150, scans 77,80,133,140; cotes 150+151, scans 3,12-13,23,27,57,60,69,133-134,138,140-142,145,190; cote 151, scans 12,27,29,32,57,59,77,133,140; cote 152, scans 2-3,12-13,22-23,25-29,63-64,133,140,142,146,163.
- **Notes (19 entries):** MPL_152+120 (7); MPL_150_085-099+151_001-031 (6); MPL_150_001-043 (4); MPL_150_044-084 (1); MPL_151_032-075 (1).
- **Notes files:** `inputs/SA10/pro/MPL_150_001-043_notes.md`; `inputs/SA10/pro/MPL_150_044-084_notes.md`; `inputs/SA10/pro/MPL_150_085-099+151_001-031_notes.md`; `inputs/SA10/pro/MPL_151_032-075_notes.md`; `inputs/SA10/pro/MPL_152+120_notes.md`.
- **Depends:** related: SA11-1 (our note), SA21-10 (our note); used by: SA10-7 (our note).
- **Flags:** a link across folders (1).
- **Other topics:** cotes 147, 149, 136, 67 (other topics: SA11? SA12?).

### SA10-3: the "Remords": his reconsideration of the realization and its date (December 1981) (= H00L)

- **Status on his pages:** stated; the date is a source question. **Kind:** his claim / history.
- **Where:** cote 150, scans 76,177,180; cote 151, scans 2,39-41,179; cote 152, scans 2,25,41-44,133,177-180,188,190.
- **Notes (12 entries):** MPL_152+120 (8); MPL_150_001-043 (2); MPL_150_044-084 (1); MPL_151_032-075 (1).
- **Notes files:** `inputs/SA10/pro/MPL_150_001-043_notes.md`; `inputs/SA10/pro/MPL_150_044-084_notes.md`; `inputs/SA10/pro/MPL_151_032-075_notes.md`; `inputs/SA10/pro/MPL_152+120_notes.md`.
- **Depends:** related: SA11-2 (our note).
- **Other topics:** = H00L (SA20-9).

## The stratified topos (cote 151, 1981)

### SA10-15: the stratified topos (cote 151, 1981), scans 1-31: hypotheses, phi_!, finite diagrams, left exactness

- **Status on his pages:** constructed; questioned implications. **Kind:** construction.
- **Where:** cotes 150+151, scans 3,5,7,9,11-15,17-25,27-32,95,133-134,140,145,150,156-157,161-162,168,179-181,188,190.
- **Notes (30 entries):** MPL_150_085-099+151_001-031 (30).
- **Notes files:** `inputs/SA10/pro/MPL_150_085-099+151_001-031_notes.md`.
- **Depends:** used by: SA10-16 (his page), SA10-8 (our note); uses: SA10-12 (his page).
- **Corrections:** MPL_150_085-099+151_001-031#26 (scans 22,23,168): the stratified topos (cote 151, 1981), scans 1-31: hypotheses, phi_!, finite dia -> correct: The corrected l.4 reads "toutes les autres orbites sont de cardinal 3 (; MPL_150_085-099+151_001-031#27 (scans 23,161): the stratified topos (cote 151, 1981), scans 1-31: hypotheses, phi_!, finite dia -> correct: drop the surjectivity sentence: The arrow X_3^* → X_2, p^* = p\ | X_3^*.
- **Flags:** note overstates or misreads the page (1).
- **Other topics:** SGA 4 recollement (literature).

### SA10-16: the stratified topos, scans 32-58: tubes, flags, local triviality, (1)-(25)

- **Status on his pages:** worked; conjectures and withdrawals. **Kind:** construction.
- **Where:** cote 151, scans 32-58.
- **Notes (53 entries):** MPL_151_032-075 (53).
- **Notes files:** `inputs/SA10/pro/MPL_151_032-075_notes.md`.
- **Depends:** used by: SA10-17 (his page); uses: SA10-15 (his page).

### SA10-17: the theorem on 151/069 and its continuation (scans 59-75): cylinder and cone descriptions, tube base change, subsection C

- **Status on his pages:** stated; proof paragraph cancelled. **Kind:** theorem (stated).
- **Where:** cote 151, scans 1-2,32-33,57,59-75,133.
- **Notes (48 entries):** MPL_151_032-075 (48).
- **Notes files:** `inputs/SA10/pro/MPL_151_032-075_notes.md`.
- **Depends:** uses: SA10-16 (his page).
- **Claims:**
  - SA10-C4 (151/69-75): "the theorem on 151/069: cylinder and cone descriptions, base change of tubes". **his claim (proof cancelled)**: none: its proof paragraph is cancelled on the page.

## Stratified homotopy types

### SA10-8: stratified homotopy types: exit paths, gerbes and homotopy amalgams; the stratified homotopy hypothesis (comparisons with Treumann and modern repairs)

- **Status on his pages:** his sketches; the notes' comparisons. **Kind:** comparison/conjecture.
- **Where:** cote 150, scans 179,188; cotes 150+151, scans 2,30,41-43,130,133-135,179-180; cote 151, scans 41.
- **Notes (21 entries):** MPL_150_085-099+151_001-031 (9); MPL_150_044-084 (8); MPL_150_001-043 (3); MPL_151_032-075 (1).
- **Notes files:** `inputs/SA10/pro/MPL_150_001-043_notes.md`; `inputs/SA10/pro/MPL_150_044-084_notes.md`; `inputs/SA10/pro/MPL_150_085-099+151_001-031_notes.md`; `inputs/SA10/pro/MPL_151_032-075_notes.md`.
- **Depends:** related: SA21-8 (our note); uses: SA10-15 (our note).
- **Other topics:** Pursuing Stacks / exit paths (Part II of the handbook outline); cote 147.

## Word types and plane trees (cote 152)

### SA10-18: the category of word types and plane trees (cote 152): operations, admissibility, orientation torsor, contours, nonpenetration, stable-tree indexing (= H00J)

- **Status on his pages:** constructed; revisions. **Kind:** construction.
- **Where:** cote 152, scans 2-5,7-8,10-11,13,133,156,185,187.
- **Notes (18 entries):** MPL_152+120 (18).
- **Notes files:** `inputs/SA10/pro/MPL_152+120_notes.md`.
- **Depends:** related: SA01-9 (my inference).
- **Other topics:** SA01 (planar maps, cote 88 "Cartes standards"); dessins (SA03?); = H00J (SA20-7).

## Tame geometry: his axioms (cote 120) and the notes' comparisons

### SA10-19: cote 120 tame-geometry axioms M1-M11 and the graph calculus (amalgams, scalar extension, compact graphs, countability) (= H00K)

- **Status on his pages:** stated; the notes realize them. **Kind:** axiomatics.
- **Where:** cote 152, scans 3-7,9-25,105,122,140,150,156,164-165,171,181-184.
- **Notes (33 entries):** MPL_152+120 (33).
- **Notes files:** `inputs/SA10/pro/MPL_152+120_notes.md`.
- **Depends:** related: SA11-3 (our note), SA21-12 (our note); used by: SA10-4 (our note), SA10-5 (our note).
- **Other topics:** SA21; SA04-4; = H00K (SA20-12).

### SA10-4: comparison of his tame-topology axioms (cotes 120-121, M1-M11) with o-minimal structures

- **Status on his pages:** not his claim; the notes' comparison. **Kind:** comparison (requested).
- **Where:** cote 150, scans 181-182,190; cotes 150+151, scans 3-7,10,13,20-21,28,54,56,65,88,92,133,181-182,190; cote 151, scans 3-5,10,19,45,54,56; cote 152, scans 3-4,7,17,30,181-182,184.
- **Notes (40 entries):** MPL_152+120 (19); MPL_150_085-099+151_001-031 (10); MPL_150_001-043 (5); MPL_150_044-084 (5); MPL_151_032-075 (1).
- **Notes files:** `inputs/SA10/pro/MPL_150_001-043_notes.md`; `inputs/SA10/pro/MPL_150_044-084_notes.md`; `inputs/SA10/pro/MPL_150_085-099+151_001-031_notes.md`; `inputs/SA10/pro/MPL_151_032-075_notes.md`; `inputs/SA10/pro/MPL_152+120_notes.md`.
- **Depends:** related: SA11-4 (our note); uses: SA10-19 (our note).
- **Flags:** requested comparison; the notes' work, not his.
- **Other topics:** SA21 (Vers une geometrie des formes); SA04-4 (Euler characteristic axioms).

### SA10-5: comparison with Shiota's Hauptvermutung for definable sets and its isotopy refinements

- **Status on his pages:** not his claim; the notes' comparison. **Kind:** comparison (requested).
- **Where:** cote 150, scans 188,190; cotes 150+151, scans 88,145,181,190; cote 151, scans 44; cote 152, scans 177-178,181-182.
- **Notes (34 entries):** MPL_152+120 (15); MPL_150_085-099+151_001-031 (8); MPL_150_001-043 (5); MPL_150_044-084 (5); MPL_151_032-075 (1).
- **Notes files:** `inputs/SA10/pro/MPL_150_001-043_notes.md`; `inputs/SA10/pro/MPL_150_044-084_notes.md`; `inputs/SA10/pro/MPL_150_085-099+151_001-031_notes.md`; `inputs/SA10/pro/MPL_151_032-075_notes.md`; `inputs/SA10/pro/MPL_152+120_notes.md`.
- **Depends:** uses: SA10-19 (our note).
- **Corrections:** MPL_150_044-084#95 (scans ): comparison with Shiota's Hauptvermutung for definable sets and its isotopy refin -> correct: its anchor "de façon cohérente" is not on the page (C13). The isotopy r.
- **Flags:** note overstates or misreads the page (1); a link across folders (1); requested comparison; the notes' work, not his.

## Reading questions, lexical findings, documentary and apparatus

### SA10-10: reading questions and index slips in the three-stratum induction (cote 150, scans 1-43)

- **Status on his pages:** reading questions. **Kind:** reading question.
- **Where:** cote 150, scans 181,187-188.
- **Notes (5 entries):** MPL_150_001-043 (5).
- **Notes files:** `inputs/SA10/pro/MPL_150_001-043_notes.md`.
- **Corrections:** MPL_150_001-043#100 (scans 181): reading questions and index slips in the three-stratum induction (cote 150, scan -> correct: For the 031 part: 031 l. 37 now reads "minorant \unsure{k\ | h} (tel qu; MPL_150_001-043#101 (scans 188): reading questions and index slips in the three-stratum induction (cote 150, scan -> drop: The word "discrète" is not on the page (042 l. 11, #38). The question it r; MPL_150_001-043#103 (scans 187): reading questions and index slips in the three-stratum induction (cote 150, scan -> correct: The identity symbol is settled as i̲ (041 l. 43, #36). The other arrowh.
- **Flags:** note overstates or misreads the page (1).

### SA10-13: reading questions of cote 150, scans 44-99 and cote 151, scans 1-31

- **Status on his pages:** reading questions. **Kind:** reading question.
- **Where:** cote 150; cotes 150+151, scans 14-15,22,25,27,31,87,97-99,133,140,157,160,188.
- **Notes (17 entries):** MPL_150_044-084 (12); MPL_150_085-099+151_001-031 (5).
- **Notes files:** `inputs/SA10/pro/MPL_150_044-084_notes.md`; `inputs/SA10/pro/MPL_150_085-099+151_001-031_notes.md`.
- **Corrections:** MPL_150_044-084#103 (scans ): reading questions of cote 150, scans 44-99 and cote 151, scans 1-31: The inverse -> correct: Two readers (this pass, and Hua p. 64) read b_ij^{-1} in the ink, so it; MPL_150_044-084#105 (scans ): reading questions of cote 150, scans 44-99 and cote 151, scans 1-31: Variables i -> correct: The lower elements are x_i and x_j (#29), not x_i and y. The mismatch i; MPL_150_044-084#109 (scans ): reading questions of cote 150, scans 44-99 and cote 151, scans 1-31: Stars, the  -> correct: "missing target in the 077 margin": the target is now read, doubtfully,; MPL_150_085-099+151_001-031#53 (scans 27,31,133,140): reading questions of cote 150, scans 44-99 and cote 151, scans 1-31: 151.pdf, sc -> correct: settled: The neighbourhood letter is the looped V, read \mathcal V: sam.

### SA10-11: lexical findings: paths, fundamental groupoids, homotopy vocabulary, protopos

- **Status on his pages:** lexical. **Kind:** lexical.
- **Where:** cote 150.
- **Notes (4 entries):** MPL_150_044-084 (4).
- **Notes files:** `inputs/SA10/pro/MPL_150_044-084_notes.md`.
- **Corrections:** MPL_150_044-084#5 (scans ): lexical findings: paths, fundamental groupoids, homotopy vocabulary, protopos: P -> correct: The "no secure standalone topos" finding stands, but the main-text word; MPL_150_044-084#12 (scans ): lexical findings: paths, fundamental groupoids, homotopy vocabulary, protopos: L -> correct: the "topos" row: see Q5 (one doubtful protopos in the margin, one conte; MPL_150_044-084#13 (scans ): lexical findings: paths, fundamental groupoids, homotopy vocabulary, protopos: F -> correct: the quoted sentence now reads "On s'intéresse aux \unsure{protopos\ | p.

### SA10-9: documentary: covers, title sheets, dates, numbering and page counts of cotes 150-152 and 120

- **Status on his pages:** documentary. **Kind:** documentary.
- **Where:** cote 150, scans 44-45,67,72,80,128,136,140,179,190; cotes 150+151, scans 1-4,10-11,17,25,27,29,85-86,91,150,156,162,181; cote 152, scans 1-3,5-7,9,13.
- **Notes (32 entries):** MPL_150_001-043 (9); MPL_150_044-084 (9); MPL_150_085-099+151_001-031 (7); MPL_152+120 (7).
- **Notes files:** `inputs/SA10/pro/MPL_150_001-043_notes.md`; `inputs/SA10/pro/MPL_150_044-084_notes.md`; `inputs/SA10/pro/MPL_150_085-099+151_001-031_notes.md`; `inputs/SA10/pro/MPL_152+120_notes.md`.
- **Corrections:** MPL_150_001-043#98 (scans 136): documentary: covers, title sheets, dates, numbering and page counts of cotes 150 -> correct: The word after "Reprenons la description" (043 l. 41) is \unsure{Ab ovo; MPL_150_085-099+151_001-031#54 (scans 85,86,91,150): documentary: covers, title sheets, dates, numbering and page counts of cotes 150 -> correct: Sheet numbers 39, 40, 41, 42, 43, 44, 45, 46 on 086, 087, 089, 091, 093.

### SA10-1: the notes' apparatus for the stratified-spaces packages (evidence, statuses, sources, research tasks)

- **Status on his pages:** apparatus. **Kind:** apparatus.
- **Where:** cote 150, scans 23,44,91,128,133,138,140,177; cote 151, scans 1-4,32; cote 152, scans 2,22-23,41,43.
- **Notes (22 entries):** MPL_150_001-043 (10); MPL_152+120 (6); MPL_150_044-084 (3); MPL_151_032-075 (3).
- **Notes files:** `inputs/SA10/pro/MPL_150_001-043_notes.md`; `inputs/SA10/pro/MPL_150_044-084_notes.md`; `inputs/SA10/pro/MPL_151_032-075_notes.md`; `inputs/SA10/pro/MPL_152+120_notes.md`.

## Counts

- Items: 19; placed entries: 537.
- DEPENDS rows: 36; CLAIM_LINKS: 5; UNIT_LINKS: 0; CORRECTIONS: 42; part-2 check events: 282.
