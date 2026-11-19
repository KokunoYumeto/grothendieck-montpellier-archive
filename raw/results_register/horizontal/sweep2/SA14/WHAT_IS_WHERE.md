# SA14: what is where

Claude Opus 5.5 at effort max, a28ea31fa17dd65e1, sweep 2 part 2, 18 Nov 2026. Built from this folder's PLACEMENT, OBJECTS, FLAGS,
DEPENDS, CLAIM_LINKS and UNIT_LINKS (sweep 1 and sweep 2). Items are in mathematical order.

How to read the links: 'Uses' and 'Used by' come from DEPENDS.tsv, with the basis in brackets (his page: the page
refers to or builds on it; our note: a note links them; proof: the mathematics requires it). Claim links are
item-level unless a row says 'decided on the scan': 'known' means the item's subject is established in the cited
literature, not that each of his claims was checked one by one. Companion units come from
UNITS_DRAFT_20261118.tsv, which does not yet cover every folder.

SA14 is cotes 57-60 (Picard): the existence and properness of the Picard functor, Lefschetz theorems and local Picard
groups (SGA 2), algebraization, Néron-Severi, the theorem of the cube, the Picard of curves with several components and
the Kummer class of the degree-one torsor (cote 57, scans 133-179, new in sweep 2), the universal vector extension, the
determinant and Riemann-Roch (cote 59), and l-adic L-functions on curves (cote 60). Reading decided on the scan in sweep 2:
REPORTS/cote57_scan144_a_verifier.md. A theme only, no dependency: SA23-24 (connections on fibre products, cote 23) and
SA14-2 (connections on the Picard scheme); the sweep-1 pointer that sent SA23-24 to SA19 was a parsing artifact
(REPORTS/sweep1_pointers_into_my_topics.md).

| # | Item | Entries | Status |
|---|---|---:|---|
| 1 | SA14-11: reused commutative-algebra typescripts: Fitting ideals, reflexive modules, Hense | 46 | reused typescripts; known |
| 2 | SA14-18: pseudomorphisms (cote 57, scans 166-171): separatedness, the quasi-coherence pro | 6 | his text; known |
| 3 | SA14-9: the theorem of the cube and the Picard functor of a product: multiplication pull | 15 | his text; known |
| 4 | SA14-4: existence and properness of the Picard functor: the Seshadri argument, the valua | 95 | his text; known |
| 5 | SA14-7: relative Picard objects and Néron-Severi: quotient definitions, polarizations, t | 24 | his text; known |
| 6 | SA14-5: the analytic criterion and the algebraization of Picard: Picard groups of germs, | 34 | his text; known |
| 7 | SA14-3: Lefschetz theorems for the Picard group and the fundamental group (SGA 2): restr | 67 | his text; known |
| 8 | SA14-6: local Picard groups of punctured spectra: isolated singularities, cones, factori | 33 | his text; known in substance |
| 9 | SA14-8: gluing, pinching and noncomplete varieties; the Picard group of a curve with sev | 29 | his text; known |
| 10 | SA14-17: the Kummer class and transgression for the Picard of a curve: finite Kummer clas | 8 | his claim, marked 'à vérifier'; the mechanism is known |
| 11 | SA14-2: the universal vector extension and connections on the Picard scheme (Picard-omeg | 25 | his text; known |
| 12 | SA14-14: sections of torsors and their classes; determinants of perfect complexes, Rieman | 14 | his text; known |
| 13 | SA14-10: L-functions of l-adic sheaves on curves over finite fields: determinants, functi | 115 | his text; known |
| 14 | SA14-1: the programme's carry questions on these cotes: the Fourier compatibility check  | 55 | the notes' carry questions |
| 15 | SA14-16: the notes' links to the research register and the planning questions (motivic ca | 16 | the notes' links |
| 16 | SA14-12: Michel Hua's project: credited links and comparisons for these cotes | 11 | credited comparison |
| 17 | SA14-13: the dossier as a document: titles, pagination, letters, reused typescripts, refe | 59 | documents |

## SA14-11: reused commutative-algebra typescripts: Fitting ideals, reflexive modules, Hensel factorization, monogenic algebras, differents, divisors and ramification, graded rings

- **Status:** reused typescripts; known. Commutative algebra (Fitting ideals, reflexive modules, Hensel factorization, Koszul, Cohen-Macaulay), used as paper and sometimes annotated.
- **Where (his pages):** cote 57, scans 134, 136, 154, 161, 164-167, 169-171, 173-179, 297; cote 58, scans 7, 9, 14, 19, 354, 358; cote 60, scans 4, 12, 16, 22, 26, 30, 32, 37.
- **Where (our notes):** MPL_60_002-035 (11) in `grothendieck_archive_transcription_20261110/returns/MPL_60_002-035_unzipped/MPL_60_002-035_notes.md`; MPL_57_089-132 (8) in `grothendieck_archive_transcription_20261110/returns/MPL_57_089-132_unzipped/MPL_57_089-132_notes.md`; work:K57-10 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K57-10/out/K57-10_mathnotes.md`; work:K58-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K58-01/out/K58-01_mathnotes.md`; work:K58-02 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K58-02/out/K58-02_mathnotes.md`; MPL_57_133-179 (6) in `grothendieck_archive_transcription_20261110/returns/MPL_57_133-179_unzipped/MPL_57_133-179/MPL_57_133-179_notes.md`; codex:K57-10 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K57-10/out/K57-10_notes.md`; codex:K58-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K58-01/out/K58-01_notes.md`; and 1 more sources.
- **Across topics:** Bourbaki-style exercises.
- **Uses:** nothing recorded. **Used by:** nothing recorded.
- **His claims:** 17 entries: no proof or refutation found in the register or the topic.
- **Companion units (32):** Divisors, Picard classes and tangents; Completion of a topological module; Passing to separated objects ...

## SA14-18: pseudomorphisms (cote 57, scans 166-171): separatedness, the quasi-coherence proposition (withdrawn), codimension-one regularity, normality relaxations, minimal primes, a birational fundamental-group statement

- **Status:** his text; known. Pseudomorphisms (cote 57, scans 166-171); the notion is EGA IV §20.2's. The quasi-coherence proposition is withdrawn on the page.
- **Where (his pages):** cote 57, scans 166-167, 169-170.
- **Where (our notes):** MPL_57_133-179 (6) in `grothendieck_archive_transcription_20261110/returns/MPL_57_133-179_unzipped/MPL_57_133-179/MPL_57_133-179_notes.md`.
- **Uses:** nothing recorded. **Used by:** SA14-4 (his page).
- **His claims:** 1 entries: known EGA IV §20.2 (pseudo-morphismes).
- **Companion units (4):** Schematically dense opens; Pseudomorphisms and pseudo-sections; Divisor of a function ...

## SA14-9: the theorem of the cube and the Picard functor of a product: multiplication pullback, marked invertible sheaves, rigid groups, composition laws

- **Status:** his text; known. The theorem of the cube and the Picard functor of a product; an English letter (A57-02) on Corr and Raynaud's construction.
- **Where (his pages):** cote 57, scans 34-49.
- **Where (our notes):** work:K57-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K57-01/out/K57-01_mathnotes.md`; work:K57-02 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K57-02/out/K57-02_mathnotes.md`; codex:A57-02 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/A57-02/out/A57-02_notes.md`; codex:K57-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K57-01/out/K57-01_notes.md`; codex:K57-02 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K57-02/out/K57-02_notes.md`.
- **Uses:** SA14-4 (proof). **Used by:** nothing recorded.
- **His claims:** 5 entries: known the theorem of the cube (Mumford, Abelian Varieties).
- **Flags (1):** a link across folders: An English letter in cote 57 says Raynaud is extending his construction, that an earlier proof needed the Pic functor of one factor representable, 
- **Companion units (22):** U1 · Multiplication pullback; U2 · Picard functors of a product; U2a · Marked invertible sheaves ...

## SA14-4: existence and properness of the Picard functor: the Seshadri argument, the valuative criterion, units and vertical divisors, separation, existence by rigidification and descent, finiteness (Igusa's inequality)

- **Status:** his text; known. Existence and properness of the Picard functor (FGA; Kleiman 2005): the Seshadri argument, divisors and frames (57:157-164), the Picard functor and its three variants (57:173-179).
- **Where (his pages):** cote 57, scans 104-105, 111-112, 114, 116, 118, 122-124, 126, 128-129, 133-136, 138-145, 147-149, 158-160, 164, 173-179, 210-212, 214-225, 276, 283-284, 380.
- **Where (our notes):** MPL_57_133-179 (36) in `grothendieck_archive_transcription_20261110/returns/MPL_57_133-179_unzipped/MPL_57_133-179/MPL_57_133-179_notes.md`; MPL_57_089-132 (31) in `grothendieck_archive_transcription_20261110/returns/MPL_57_089-132_unzipped/MPL_57_089-132_notes.md`; work:K57-03 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K57-03/out/K57-03_mathnotes.md`; work:K57-04 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K57-04/out/K57-04_mathnotes.md`; work:K57-07 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K57-07/out/K57-07_mathnotes.md`; work:K57-08 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K57-08/out/K57-08_mathnotes.md`; codex:K57-03 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K57-03/out/K57-03_notes.md`; codex:K57-04 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K57-04/out/K57-04_notes.md`; and 2 more sources.
- **Across topics:** SA18-17 (Picard functor of abelian schemes).
- **Uses:** SA14-18 (his page). **Used by:** SA14-7 (proof), SA14-5 (proof), SA14-8 (proof), SA14-17 (his page), SA14-2 (proof), SA14-14 (proof), SA14-9 (proof).
- **His claims:** 38 entries: known FGA (Technique de descente V-VI); Kleiman, 'The Picard scheme' (2005).
- **Flags (1):** a link across folders: An English letter in cote 57 says Raynaud is extending his construction, that an earlier proof needed the Pic functor of one factor representable, 
- **Companion units (43):** Corollary; A stronger rigidity condition; The failed openness assertion ...

## SA14-7: relative Picard objects and Néron-Severi: quotient definitions, polarizations, the rational cone, specialization of Néron-Severi and its torsion, Igusa's example

- **Status:** his text; known. Relative Picard objects and Néron-Severi (SGA 6 XIII).
- **Where (his pages):** cote 57, scans 273.
- **Where (our notes):** MPL_57_271-315 (24) in `grothendieck_archive_transcription_20261110/returns/MPL_57_271-315_unzipped/MPL_57_271-315_notes.md`.
- **Uses:** SA14-4 (proof). **Used by:** nothing recorded.
- **His claims:** 15 entries: known SGA 6 XIII.

## SA14-5: the analytic criterion and the algebraization of Picard: Picard groups of germs, Mittag-Leffler, formal characteristic-zero Picard groups, projectivity and GAGA

- **Status:** his text; known. The analytic criterion and the algebraization of Picard (SGA 2 XII).
- **Where (his pages):** cote 57, scans 159, 272.
- **Where (our notes):** MPL_57_226-270 (33) in `grothendieck_archive_transcription_20261110/returns/MPL_57_226-270_unzipped/MPL_57_226-270_notes.md`; MPL_57_133-179 (1) in `grothendieck_archive_transcription_20261110/returns/MPL_57_133-179_unzipped/MPL_57_133-179/MPL_57_133-179_notes.md`.
- **Uses:** SA14-4 (proof). **Used by:** SA14-3 (proof).
- **His claims:** 15 entries: known SGA 2 XII.

## SA14-3: Lefschetz theorems for the Picard group and the fundamental group (SGA 2): restriction to hyperplane sections, connectedness, depth, formal comparison, effectivity (the conditions Lef/Leff)

- **Status:** his text; known. Lefschetz theorems for Pic and pi_1 (SGA 2 X-XII).
- **Where (his pages):** cote 57, scans 97, 99-103; cote 58.
- **Where (our notes):** MPL_58_020-067 (53) in `grothendieck_archive_transcription_20261110/returns/MPL_58_020-067_unzipped/MPL_58_020-067_notes.md`; MPL_57_089-132 (14) in `grothendieck_archive_transcription_20261110/returns/MPL_57_089-132_unzipped/MPL_57_089-132_notes.md`.
- **Across topics:** SA18, SA19; SGA 2.
- **Uses:** SA14-5 (proof). **Used by:** SA14-6 (proof).
- **His claims:** 36 entries: known SGA 2 X-XII.
- **Flags (3):** the LM/Dérivateurs lens: 'A geometric tool for LM6 is not an arithmetic reduction proof': the note weighs a cote 58 Lefschetz-type statement as a tool for the research ru | the LM/Dérivateurs lens: the note reads the page through a research-run or LM planning question: N61. What the genus sketches can and cannot add to the tower register | the LM/Dérivateurs lens: the note reads the page through a research-run or LM planning question: N77. A geometric tool for LM6 is not an arithmetic reduction proof

## SA14-6: local Picard groups of punctured spectra: isolated singularities, cones, factoriality, henselian rings (an extension he calls conjectural)

- **Status:** his text; known in substance. Local Picard groups of punctured spectra (SGA 2 XI; Boutot 1978); one extension he calls conjectural; 'Local Picard schemes' in English (A57-01).
- **Where (his pages):** cote 57, scans 193-199, 201-206, 208-209; cote 58.
- **Where (our notes):** MPL_57_226-270 (14) in `grothendieck_archive_transcription_20261110/returns/MPL_57_226-270_unzipped/MPL_57_226-270_notes.md`; MPL_58_020-067 (11) in `grothendieck_archive_transcription_20261110/returns/MPL_58_020-067_unzipped/MPL_58_020-067_notes.md`; work:K57-06 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K57-06/out/K57-06_mathnotes.md`; codex:A57-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/A57-01/out/A57-01_notes.md`; codex:K57-06 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K57-06/out/K57-06_notes.md`.
- **Uses:** SA14-3 (proof). **Used by:** nothing recorded.
- **His claims:** 18 entries: known SGA 2 XI; Boutot, Schéma de Picard local (1978).
- **Flags (1):** the LM/Dérivateurs lens: the note reads the page through a research-run or LM planning question: N61. What the genus sketches can and cannot add to the tower register
- **Companion units (16):** Local Picard groups in dimension one and in characteristic \; Passage through the henselization; Title leaf ...

## SA14-8: gluing, pinching and noncomplete varieties; the Picard group of a curve with several components

- **Status:** his text; known. Gluing, pinching and the Picard group of curves with several components (cote 57, scans 147-156).
- **Where (his pages):** cote 57, scans 85, 147, 149-163, 165, 225, 304, 322.
- **Where (our notes):** MPL_57_133-179 (12) in `grothendieck_archive_transcription_20261110/returns/MPL_57_133-179_unzipped/MPL_57_133-179/MPL_57_133-179_notes.md`; MPL_57_271-315 (10) in `grothendieck_archive_transcription_20261110/returns/MPL_57_271-315_unzipped/MPL_57_271-315_notes.md`; work:K57-09 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K57-09/out/K57-09_mathnotes.md`; codex:K57-09 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K57-09/out/K57-09_notes.md`.
- **Uses:** SA14-4 (proof). **Used by:** SA14-17 (his page).
- **His claims:** 9 entries: known Bosch-Lütkebohmert-Raynaud, Néron Models, ch. 9.
- **Companion units (5):** Direct construction; Associated débitages and transitivity, typescript; and · Proposition , typescript ...

## SA14-17: the Kummer class and transgression for the Picard of a curve: finite Kummer classes, one and two punctures, vanishing statements, the semiabelian bridge, three obstruction constructions (cote 57, scans 141-147, 'Curve Picard')

- **Status:** his claim, marked 'à vérifier'; the mechanism is known. The Kummer class for the Picard of a curve: xi_n = delta_n(eta) (57:144), decided on the scan in part 2.
- **Where (his pages):** cote 57, scans 142, 144-145, 304.
- **Where (our notes):** MPL_57_133-179 (8) in `grothendieck_archive_transcription_20261110/returns/MPL_57_133-179_unzipped/MPL_57_133-179/MPL_57_133-179_notes.md`.
- **Across topics:** SA14-14 (sections of torsors and their classes).
- **Uses:** SA14-8 (his page), SA14-4 (his page). **Used by:** SA14-1 (our note).
- **His claims:** 3 entries: known in the literature (same mechanism) the splitting obstruction of the abelianized fundamental group extension is the divisibility of the degree-one Albanese/Picard torsor class (Harari-Szamuely 2009, Thm 1.2; register SECTION_GHOSTS:P.10, Known); same object in a run ANABELIAN_A1_SUCCESSOR:B.68 (generalized Jacobian, Kummer sequence, Abel map); ANABELIAN_149_PUSH:A.1 (prime-to-p Kummer kernel of a semiabelian variety).

## SA14-2: the universal vector extension and connections on the Picard scheme (Picard-omega, rigidified extensions), compared with Oda's Dieudonné/de Rham theory

- **Status:** his text; known. The universal vector extension and connections on Pic (Mazur-Messing 1974); Oda.
- **Where (his pages):** cote 57, scans 80, 91, 94, 180-192.
- **Where (our notes):** MPL_57_089-132 (9) in `grothendieck_archive_transcription_20261110/returns/MPL_57_089-132_unzipped/MPL_57_089-132_notes.md`; MPL_57_271-315 (9) in `grothendieck_archive_transcription_20261110/returns/MPL_57_271-315_unzipped/MPL_57_271-315_notes.md`; work:K57-05 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K57-05/out/K57-05_mathnotes.md`; codex:K57-05 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K57-05/out/K57-05_notes.md`.
- **Uses:** SA14-4 (proof). **Used by:** nothing recorded.
- **His claims:** 8 entries: known Mazur-Messing (1974).
- **Companion units (10):** A connection from a rational form; A working question; Divisors with prescribed invertible sheaf ...

## SA14-14: sections of torsors and their classes; determinants of perfect complexes, Riemann-Roch and the Weil sheaf (cote 59)

- **Status:** his text; known. Sections of torsors and their classes; determinants of perfect complexes and Riemann-Roch (Knudsen-Mumford 1976; Deligne 1987); the Weil sheaf (cote 59).
- **Where (his pages):** cote 59, scans 2-14, 16.
- **Where (our notes):** work:K59-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K59-01/out/K59-01_mathnotes.md`; work:K59-02 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K59-02/out/K59-02_mathnotes.md`; codex:K59-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K59-01/out/K59-01_notes.md`; codex:K59-02 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K59-02/out/K59-02_notes.md`.
- **Uses:** SA14-4 (proof). **Used by:** SA14-10 (proof).
- **His claims:** 4 entries: known Knudsen-Mumford (1976); Deligne, 'Le déterminant de la cohomologie' (1987).
- **Companion units (16):** 1 · . Changing the section; 2 · . A section of a torsor; 3 · . Computing the class ...

## SA14-10: L-functions of l-adic sheaves on curves over finite fields: determinants, functional equations, epsilon factors, weights and purity, boundary terms, local epsilon constants and conductors

- **Status:** his text; known. L-functions of l-adic sheaves on curves over finite fields, functional equations, epsilon factors (SGA 4 1/2, SGA 5; product formula: Laumon 1987).
- **Where (his pages):** cote 60, scans 7, 9, 15, 17, 19, 27, 36, 38-40, 42, 44, 46, 51-52, 54, 56, 58, 60-62, 64, 66, 68, 70.
- **Where (our notes):** MPL_60_036-070 (60) in `grothendieck_archive_transcription_20261110/returns/MPL_60_036-070_unzipped/MPL_60_036-070_notes.md`; MPL_60_002-035 (55) in `grothendieck_archive_transcription_20261110/returns/MPL_60_002-035_unzipped/MPL_60_002-035_notes.md`.
- **Across topics:** SA05, SA06, SA07 (motives), the Weil conjectures.
- **Uses:** SA14-14 (proof). **Used by:** nothing recorded.
- **His claims:** 7 entries: known SGA 4 1/2, SGA 5; Laumon (1987) product formula.
- **Flags (3):** note overstates or misreads the page: not an overstatement: the note is right and the page is wrong. The typescript reads 'd_k(M/N) ⊂ d_k(M)'; with d_k = Fitt_k (its own  | the LM/Dérivateurs lens: the note reads the page through a research-run or LM planning question: C01 — The packet uses the motivic category sought in the planning questio | the LM/Dérivateurs lens: the note reads the page through a research-run or LM planning question: C10 — The result register's arithmetic entries retain their stated status

## SA14-1: the programme's carry questions on these cotes: the Fourier compatibility check (cote 47), the seven theorems of cote 44, dating (= SA18-5)

- **Status:** the notes' carry questions. FW and JAC notes read cote 57 against the cote 47 Fourier check and the cote 44 theorems; FW01-FW02 conclude no second witness.
- **Where (his pages):** cote 57, scans 133, 135, 142, 144-145, 147-149, 151, 156, 158, 160, 162, 164, 169, 173-174, 178-179, 275, 309; cote 58, scans 9.
- **Where (our notes):** MPL_57_133-179 (14) in `grothendieck_archive_transcription_20261110/returns/MPL_57_133-179_unzipped/MPL_57_133-179/MPL_57_133-179_notes.md`; MPL_58_020-067 (11) in `grothendieck_archive_transcription_20261110/returns/MPL_58_020-067_unzipped/MPL_58_020-067_notes.md`; MPL_57_089-132 (10) in `grothendieck_archive_transcription_20261110/returns/MPL_57_089-132_unzipped/MPL_57_089-132_notes.md`; MPL_57_226-270 (10) in `grothendieck_archive_transcription_20261110/returns/MPL_57_226-270_unzipped/MPL_57_226-270_notes.md`; MPL_57_271-315 (10) in `grothendieck_archive_transcription_20261110/returns/MPL_57_271-315_unzipped/MPL_57_271-315_notes.md`.
- **Uses:** SA14-17 (our note), SA18-13 (our note). **Used by:** nothing recorded.
- **His claims:** 10 entries: no proof or refutation found in the register or the topic.
- **Flags (3):** the same thing noted with different readings or statements: the note says Michel Hua's reading reverses the direction of the global-projectivity example; to decide on the | a link across folders: the Fourier check of cote 47 and the seven theorems of cote 44 are asked in four more packages here; one global object with SA18-5 | a link across folders: Fifteen notes of the new Pro package read cote 57 against the programme's carry questions: FW against the missing Fourier verification of cote 47 (
- **Companion units (10):** Divisors, Picard classes and tangents; Divisor of a function; Two preliminary Picard functors ...

## SA14-16: the notes' links to the research register and the planning questions (motivic category, LM6 tool, RESULTS_STATE coverage)

- **Status:** the notes' links. Links to the research register and planning questions.
- **Where (his pages):** cote 58; cote 60, scans 61, 65.
- **Where (our notes):** MPL_60_002-035 (10) in `grothendieck_archive_transcription_20261110/returns/MPL_60_002-035_unzipped/MPL_60_002-035_notes.md`; MPL_58_020-067 (4) in `grothendieck_archive_transcription_20261110/returns/MPL_58_020-067_unzipped/MPL_58_020-067_notes.md`; MPL_60_036-070 (2) in `grothendieck_archive_transcription_20261110/returns/MPL_60_036-070_unzipped/MPL_60_036-070_notes.md`.
- **Uses:** nothing recorded. **Used by:** nothing recorded.
- **His claims:** 1 entries: no proof or refutation found in the register or the topic.
- **Flags (4):** the LM/Dérivateurs lens: 'A geometric tool for LM6 is not an arithmetic reduction proof': the note weighs a cote 58 Lefschetz-type statement as a tool for the research ru | the LM/Dérivateurs lens: the note reads the page through a research-run or LM planning question: N77. A geometric tool for LM6 is not an arithmetic reduction proof | the LM/Dérivateurs lens: the note reads the page through a research-run or LM planning question: C01 — The packet uses the motivic category sought in the planning questio | ...

## SA14-12: Michel Hua's project: credited links and comparisons for these cotes

- **Status:** credited comparison. Michel Hua's readings for these cotes.
- **Where (his pages):** cote 57, scans 3, 14, 24, 42, 59, 65, 67, 80, 102, 104, 115, 125, 141, 157, 166, 173, 185, 195, 201, 214, 274, 294, 304-305, 308; cote 58.
- **Where (our notes):** MPL_57_226-270 (8) in `grothendieck_archive_transcription_20261110/returns/MPL_57_226-270_unzipped/MPL_57_226-270_notes.md`; MPL_57_271-315 (2) in `grothendieck_archive_transcription_20261110/returns/MPL_57_271-315_unzipped/MPL_57_271-315_notes.md`; MPL_58_020-067 (1) in `grothendieck_archive_transcription_20261110/returns/MPL_58_020-067_unzipped/MPL_58_020-067_notes.md`.
- **Uses:** nothing recorded. **Used by:** nothing recorded.
- **His claims:** 0 entries: no proof or refutation found in the register or the topic.
- **Flags (1):** the same thing noted with different readings or statements: the note says Michel Hua's reading reverses the direction of the global-projectivity example; to decide on the
- **Companion units (14):** U1 · Multiplication pullback; U4 · A product decomposition; Torsors with a morphism from $X$ ...

## SA14-13: the dossier as a document: titles, pagination, letters, reused typescripts, references

- **Status:** documents. Titles, covers, the Benjamin letter (Massy, 21 Nov 1966), reused typescripts.
- **Where (his pages):** cote 57, scans 42, 133-134, 141, 143, 150, 152, 157, 163, 165-166, 179, 249, 272, 278, 309-310; cote 58, scans 11, 13, 19-20, 53; cote 59, scans 2, 9, 15-17, 20, 26; cote 60.
- **Where (our notes):** MPL_57_226-270 (18) in `grothendieck_archive_transcription_20261110/returns/MPL_57_226-270_unzipped/MPL_57_226-270_notes.md`; MPL_57_133-179 (12) in `grothendieck_archive_transcription_20261110/returns/MPL_57_133-179_unzipped/MPL_57_133-179/MPL_57_133-179_notes.md`; MPL_57_271-315 (6) in `grothendieck_archive_transcription_20261110/returns/MPL_57_271-315_unzipped/MPL_57_271-315_notes.md`; MPL_58_020-067 (5) in `grothendieck_archive_transcription_20261110/returns/MPL_58_020-067_unzipped/MPL_58_020-067_notes.md`; MPL_60_002-035 (1) in `grothendieck_archive_transcription_20261110/returns/MPL_60_002-035_unzipped/MPL_60_002-035_notes.md`; MPL_60_036-070:records:research_leads (1) in `grothendieck_archive_transcription_20261110/returns/MPL_60_036-070_unzipped/records/research_leads.md`; codex:A57-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/A57-01/out/A57-01_notes.md`; codex:A57-02 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/A57-02/out/A57-02_notes.md`; and 14 more sources.
- **Uses:** nothing recorded. **Used by:** nothing recorded.
- **His claims:** 1 entries: no proof or refutation found in the register or the topic.
- **Companion units (17):** Completion of a topological module; Passing to separated objects; Schematically dense opens ...
