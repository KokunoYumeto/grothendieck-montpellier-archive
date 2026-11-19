# SA05: what is where

Claude Opus 5.5 at effort max, a28ea31fa17dd65e1, sweep 2 part 2, 18 Nov 2026. Built from this folder's PLACEMENT, OBJECTS, FLAGS,
DEPENDS, CLAIM_LINKS and UNIT_LINKS (sweep 1 and sweep 2). Items are in mathematical order.

How to read the links: 'Uses' and 'Used by' come from DEPENDS.tsv, with the basis in brackets (his page: the page
refers to or builds on it; our note: a note links them; proof: the mathematics requires it). Claim links are
item-level unless a row says 'decided on the scan': 'known' means the item's subject is established in the cited
literature, not that each of his claims was checked one by one. Companion units come from
UNITS_DRAFT_20261118.tsv, which does not yet cover every folder.

SA05 is cotes 10-13 and parts of 14-18 (Théorie des motifs I): correspondences and the standard conjectures (cote 11-12),
abstract motives and the motivic Galois group (cote 12, MPL_12_150-168), the tannakian text and a group-scheme text
(cote 10, B series), the Hodge group and the letter to Mumford (cote 13), motives over finite fields and Deuring's gerbes
(cote 15, 2-32), the Serre group and CM structures, absolute cohomology of Z(n) (cote 15, 139-178), the cote 16
programme. Reading decided on the scans in sweep 2: REPORTS/mumford_letter_cote13.md.

| # | Item | Entries | Status |
|---|---|---:|---|
| 1 | SA05-1: the category of correspondences V^A of a cohomology theory A (Hom(X,Y)=A(X x Y)) | 122 | his construction; known as definitions |
| 2 | SA05-2: Grothendieck's standard conjectures as he lettered them (draft and printed A-D): | 14 | conjectures, open |
| 3 | SA05-16: the cote 16 programme: the Lefschetz correspondence ring and the singular-hypers | 18 | his programme, open |
| 4 | SA05-11: positive forms and polarizations: the positive cone, orthogonal splitting, semis | 29 | his claims; known in characteristic 0 |
| 5 | SA05-12: abstract motives: the universal pseudo-abelian additive target, projectors and t | 66 | his construction; known as definitions |
| 6 | SA05-20: tensor categories and the tannakian formalism (cote 10, B series): the plan 'Gen | 7 | his text; known |
| 7 | SA05-8: the motivic Galois group: fibre functors, arithmetic quotients, Hodge groups, th | 60 | his claims; known in part |
| 8 | SA05-9: weights and levels of motives and l-adic sheaves: weight bounds, coniveau, dimen | 72 | his claims; known in part |
| 9 | SA05-21: the Hodge group, the letter to Mumford (Algiers, 1 November 1965) and transcende | 6 | his conjectures, withdrawn by him; settled since |
| 10 | SA05-10: absolute cohomology of motives and arithmetic: Ext and effaceability, Ind-motive | 66 | his claims; open in general |
| 11 | SA05-13: smooth integral motives over a base: the one-prime independence conjecture, inte | 18 | his conjectures, open |
| 12 | SA05-18: motives over finite fields: the Weil-number protorus, the Artin-Tate quotient an | 27 | his notes; known conditionally |
| 13 | SA05-19: Deuring's gerbes and norm categories: rank-one objects over maximal orders, Azum | 31 | his notes; known in substance |
| 14 | SA05-14: linear versus nonlinear statements: Hom of Jacobians against Hom of curves, the  | 9 | his question; known in parts |
| 15 | SA05-15: Oda's comparison of de Rham/Dieudonné realizations in characteristic p | 5 | known |
| 16 | SA05-3: the cohomology of quadrics (= SA18-16) | 35 | = SA18-16 |
| 17 | SA05-4: a cancelled group-scheme text: reductive centre, maximal tori, the Weyl group (= | 31 | = SA18-2 |
| 18 | SA05-5: Delzant's offprint: the Witt ring, Stiefel-Whitney and Clifford invariants, Brau | 13 | = SA18-3 |
| 19 | SA05-7: a reused typescript on spherical buildings: Tits's centre conjecture, geodesics, | 15 | reused typescript; proved since |
| 20 | SA05-17: the dossiers as documents and registers: evidence keys, title sheets, page count | 116 | documents and registers |

## SA05-1: the category of correspondences V^A of a cohomology theory A (Hom(X,Y)=A(X x Y)): composition, units, graphs and transposes, signs, degree rules, stable systems A' in A, Poincaré algebras, tautological classes (cote 11)

- **Status:** his construction; known as definitions. The category of correspondences V^A of a cohomology theory (Manin 1968; Kleiman 1968).
- **Where (his pages):** cote 11, scans 3, 5, 7, 9, 11-13, 15-29, 31, 34, 36, 38, 40, 42-47, 55; cote 14, scans 87-90, 92, 94-96, 98, 100.
- **Where (our notes):** MPL_11_002-042 (51) in `grothendieck_archive_transcription_20261110/returns/MPL_11_002-042_unzipped/MPL_11_002-042_notes.md`; MPL_11_043-058+56 (35) in `grothendieck_archive_transcription_20261110/returns/MPL_11_043-058+56_unzipped/MPL_11_043-058+56_notes.md`; work:K11-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K11-01/out/K11-01_mathnotes.md`; work:K11-02 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K11-02/out/K11-02_mathnotes.md`; work:K11-03 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K11-03/out/K11-03_mathnotes.md`; work:K11-04 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K11-04/out/K11-04_mathnotes.md`; work:K14-07 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K14-07/out/K14-07_mathnotes.md`; MPL_11_043-058+56:records:research_leads (1) in `grothendieck_archive_transcription_20261110/returns/MPL_11_043-058+56_unzipped/records/research_leads.md`; and 5 more sources.
- **Across topics:** SA18-15; SA06, SA07 (motives).
- **Uses:** nothing recorded. **Used by:** SA05-2 (proof), SA05-12 (proof).
- **His claims:** 48 entries: known Manin (1968); Kleiman (1968, 1972).
- **Flags (1):** a link across folders: SA05-1, SA05-3, SA05-4, SA05-5 are the same objects as SA18-15, SA18-16, SA18-2, SA18-3

## SA05-2: Grothendieck's standard conjectures as he lettered them (draft and printed A-D): Lefschetz operators, the inverse and lowering maps, the content of each letter

- **Status:** conjectures, open. The standard conjectures as he lettered them (A-D); Lefschetz type open in general, known for abelian varieties in characteristic 0 (Lieberman 1968); Hodge type known in characteristic 0.
- **Where (his pages):** cote 11, scans 3, 16, 21, 23, 27, 34; cote 12, scans 12, 16, 40, 99, 151-152.
- **Where (our notes):** MPL_11_002-042 (8) in `grothendieck_archive_transcription_20261110/returns/MPL_11_002-042_unzipped/MPL_11_002-042_notes.md`; MPL_12_150-168+15_002-033 (2) in `grothendieck_archive_transcription_20261110/returns/MPL_12_150-168+15_002-033_unzipped/MPL_12_150-168+15_002-033/MPL_12_150-168+15_002-033_notes.md`; MPL_11_043-058+56 (1) in `grothendieck_archive_transcription_20261110/returns/MPL_11_043-058+56_unzipped/MPL_11_043-058+56_notes.md`; MPL_12_002-050 (1) in `grothendieck_archive_transcription_20261110/returns/MPL_12_002-050_unzipped/MPL_12_002-050_notes.md`; MPL_12_051-098 (1) in `grothendieck_archive_transcription_20261110/returns/MPL_12_051-098_unzipped/MPL_12_051-098_notes.md`; MPL_12_099-149 (1) in `grothendieck_archive_transcription_20261110/returns/MPL_12_099-149_unzipped/MPL_12_099-149_notes.md`.
- **Uses:** SA05-1 (proof). **Used by:** SA05-16 (his page), SA05-11 (proof), SA05-12 (our note).
- **His claims:** 1 entries: open the standard conjectures; Lieberman (1968) for abelian varieties in characteristic 0.
- **Flags (2):** the same thing noted with different readings or statements: a later vanishing on the pages contradicts the earlier degree-two example (N037: the constant Jacobian gives a | a link across folders: the draft and printed lettering of the standard conjectures is asked in cote 11, cote 12 and the shared package; one object with SA18-12

## SA05-16: the cote 16 programme: the Lefschetz correspondence ring and the singular-hypersurface questions

- **Status:** his programme, open. The cote 16 programme: the Lefschetz correspondence ring and the singular-hypersurface question.
- **Where (his pages):** cote 12, scans 56, 59, 105, 107, 143; cote 16, scans 8-11, 13-14, 16, 31, 33-37, 39-43.
- **Where (our notes):** work:K16-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K16-01/out/K16-01_mathnotes.md`; work:K16-03 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K16-03/out/K16-03_mathnotes.md`; MPL_12_051-098 (2) in `grothendieck_archive_transcription_20261110/returns/MPL_12_051-098_unzipped/MPL_12_051-098_notes.md`; MPL_12_099-149 (2) in `grothendieck_archive_transcription_20261110/returns/MPL_12_099-149_unzipped/MPL_12_099-149_notes.md`; codex:K16-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K16-01/out/K16-01_notes.md`; codex:K16-03 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K16-03/out/K16-03_notes.md`.
- **Uses:** SA05-2 (his page). **Used by:** nothing recorded.
- **His claims:** 5 entries: no proof or refutation found in the register or the topic.

## SA05-11: positive forms and polarizations: the positive cone, orthogonal splitting, semisimplicity and isotypic components (cote 12)

- **Status:** his claims; known in characteristic 0. Positive forms and polarizations; the Hodge standard conjecture holds in characteristic 0 (Hodge-Riemann) and is open in characteristic p beyond surfaces.
- **Where (his pages):** cote 12, scans 2, 8, 11-12, 15-16, 44, 49, 82, 84, 86-87, 89-95, 153, 159, 161, 163, 203; cote 16, scans 44, 46-50, 52, 54.
- **Where (our notes):** MPL_12_051-098 (10) in `grothendieck_archive_transcription_20261110/returns/MPL_12_051-098_unzipped/MPL_12_051-098_notes.md`; work:K12-06 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K12-06/out/K12-06_mathnotes.md`; work:K16-04 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K16-04/out/K16-04_mathnotes.md`; MPL_12_150-168+15_002-033 (5) in `grothendieck_archive_transcription_20261110/returns/MPL_12_150-168+15_002-033_unzipped/MPL_12_150-168+15_002-033/MPL_12_150-168+15_002-033_notes.md`; codex:K12-06 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K12-06/out/K12-06_notes.md`; codex:K16-04 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K16-04/out/K16-04_notes.md`.
- **Uses:** SA05-2 (proof). **Used by:** SA05-12 (our note).
- **His claims:** 5 entries: known in characteristic 0 Hodge-Riemann bilinear relations; open in characteristic p beyond surfaces.

## SA05-12: abstract motives: the universal pseudo-abelian additive target, projectors and their splitting, semisimplicity, Schur projectors in characteristic zero, Lefschetz structures, Galois descent (cote 12, scans 137-149)

- **Status:** his construction; known as definitions. Abstract motives, projectors, Künneth, Tate inversion, effectivity, niveau (MPL_12_150-168, M notes); numerical motives are semisimple (Jannsen 1992).
- **Where (his pages):** cote 12, scans 3-4, 9, 11-18, 26, 44, 47-49, 99, 112-113, 135, 137, 139-159, 165, 167; cote 14, scans 3, 5, 7, 9, 11, 13, 15.
- **Where (our notes):** MPL_12_099-149 (25) in `grothendieck_archive_transcription_20261110/returns/MPL_12_099-149_unzipped/MPL_12_099-149_notes.md`; MPL_12_150-168+15_002-033 (25) in `grothendieck_archive_transcription_20261110/returns/MPL_12_150-168+15_002-033_unzipped/MPL_12_150-168+15_002-033/MPL_12_150-168+15_002-033_notes.md`; work:K12-09 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K12-09/out/K12-09_mathnotes.md`; work:K14-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K14-01/out/K14-01_mathnotes.md`; MPL_12_002-050 (2) in `grothendieck_archive_transcription_20261110/returns/MPL_12_002-050_unzipped/MPL_12_002-050_notes.md`; codex:K12-09 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K12-09/out/K12-09_notes.md`; codex:K14-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K14-01/out/K14-01_notes.md`.
- **Uses:** SA05-1 (proof), SA05-2 (our note), SA05-11 (our note). **Used by:** SA05-8 (proof), SA05-9 (proof), SA05-10 (proof), SA05-13 (proof), SA05-14 (proof).
- **His claims:** 15 entries: known Kleiman (1972); Jannsen (1992), numerical motives are semisimple.
- **Flags (1):** the same thing noted with different readings or statements: our reading 'Tout morphisme u:P->Q est "direct"' against Michel Hua's account (a condition first for monomorph

## SA05-20: tensor categories and the tannakian formalism (cote 10, B series): the plan 'Generalites sur les operations (x) sur une categorie' with an appendix on coalgebras, comodules and bialgebras, examples of tensor categories, a tannakian category over k with diagonalizable band

- **Status:** his text; known. The tannakian text of cote 10 (B series): the plan of a treatise on tensor categories; Saavedra (1972), Deligne-Milne (1982).
- **Where (his pages):** cote 10, scans 60-66, 69-76, 78-81, 87, 104-106, 108, 115-126, 128-130, 137.
- **Where (our notes):** codex:B10-04 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/B10-04/out/B10-04_notes.md`; codex:B10-05 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/B10-05/out/B10-05_notes.md`; codex:B10-06 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/B10-06/out/B10-06_notes.md`; codex:B10-07 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/B10-07/out/B10-07_notes.md`; codex:B10-08 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/B10-08/out/B10-08_notes.md`; codex:B10-09 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/B10-09/out/B10-09_notes.md`; codex:B10-10 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/B10-10/out/B10-10_notes.md`.
- **Across topics:** linked SA07-1 (H047), SA15-6 (H0AH).
- **Uses:** nothing recorded. **Used by:** SA05-8 (proof).
- **His claims:** 7 entries: known Saavedra (1972); Deligne-Milne (1982).

## SA05-8: the motivic Galois group: fibre functors, arithmetic quotients, Hodge groups, the exact sequence over Q, the Tannakian formalism, the period torsor and the period conjecture (cote 12)

- **Status:** his claims; known in part. The motivic Galois group (conditional on the standard conjectures; unconditional variants: André 1996, Nori, Ayoub); with the Serre group S_K and CM structures (cote 15, 139-168).
- **Where (his pages):** cote 12, scans 2, 4-6, 8-9, 12, 15-16, 18-19, 21, 23-32, 34-35, 44, 49, 51-57, 59, 94, 150-152, 159, 213; cote 15, scans 139, 141-145, 147-152, 154-155, 159, 161, 163, 165, 168.
- **Where (our notes):** MPL_12_051-098 (20) in `grothendieck_archive_transcription_20261110/returns/MPL_12_051-098_unzipped/MPL_12_051-098_notes.md`; MPL_15_139-194:records:research_leads_before_context (19) in `grothendieck_archive_transcription_20261110/returns/MPL_15_139-194_checkpoint_01_unzipped/research_leads_before_context.md`; work:K12-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K12-01/out/K12-01_mathnotes.md`; work:K12-02 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K12-02/out/K12-02_mathnotes.md`; MPL_12_150-168+15_002-033 (4) in `grothendieck_archive_transcription_20261110/returns/MPL_12_150-168+15_002-033_unzipped/MPL_12_150-168+15_002-033/MPL_12_150-168+15_002-033_notes.md`; MPL_12_002-050 (3) in `grothendieck_archive_transcription_20261110/returns/MPL_12_002-050_unzipped/MPL_12_002-050_notes.md`; codex:K12-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K12-01/out/K12-01_notes.md`; codex:K12-02 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K12-02/out/K12-02_notes.md`.
- **Across topics:** SA06, SA07, SA15-6.
- **Uses:** SA05-12 (proof), SA05-20 (proof). **Used by:** SA05-21 (his page), SA05-18 (proof).
- **His claims:** 12 entries: known in part Deligne-Milne (1982); André (1996); Nori; Ayoub.

## SA05-9: weights and levels of motives and l-adic sheaves: weight bounds, coniveau, dimension type, Hodge level, admissibility, direct images, spectral-sequence degeneration (cote 12)

- **Status:** his claims; known in part. Weights and levels; weights by Deligne (Weil I, II).
- **Where (his pages):** cote 12, scans 9, 12, 15-16, 33, 41-54, 58, 73, 88, 92-93, 101, 104-109, 111-116, 118-120, 122, 125, 127, 129, 131, 133, 135, 142, 155, 205.
- **Where (our notes):** MPL_12_099-149 (37) in `grothendieck_archive_transcription_20261110/returns/MPL_12_099-149_unzipped/MPL_12_099-149_notes.md`; MPL_12_051-098 (9) in `grothendieck_archive_transcription_20261110/returns/MPL_12_051-098_unzipped/MPL_12_051-098_notes.md`; work:K12-03 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K12-03/out/K12-03_mathnotes.md`; work:K12-07 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K12-07/out/K12-07_mathnotes.md`; work:K12-08 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K12-08/out/K12-08_mathnotes.md`; MPL_12_150-168+15_002-033 (3) in `grothendieck_archive_transcription_20261110/returns/MPL_12_150-168+15_002-033_unzipped/MPL_12_150-168+15_002-033/MPL_12_150-168+15_002-033_notes.md`; MPL_12_002-050 (2) in `grothendieck_archive_transcription_20261110/returns/MPL_12_002-050_unzipped/MPL_12_002-050_notes.md`; codex:K12-03 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K12-03/out/K12-03_notes.md`; and 2 more sources.
- **Across topics:** SA14-10, SA06, SA07.
- **Uses:** SA05-12 (proof). **Used by:** SA05-18 (proof).
- **His claims:** 25 entries: known in part Deligne, Weil I-II.
- **Flags (4):** suspected misreading: the transcription reads the level bound '2(n−i+j)'; for an elliptic curve (n=i=1, j=0) it gives level 0 at weight 1, but H^1 has Hodge level 1; the  | the same thing noted with different readings or statements: our reading 'Tout morphisme u:P->Q est "direct"' against Michel Hua's account (a condition first for monomorph | the LM/Dérivateurs lens: 'The prime-to-p point problem is not answered here': the note reads cote 12 through the research run's point-section question (ANABELIAN A1) | ...

## SA05-21: the Hodge group, the letter to Mumford (Algiers, 1 November 1965) and transcendental descriptions of motives in characteristic 0 by double lattices (cote 13)

- **Status:** his conjectures, withdrawn by him; settled since. The Hodge group and the letter to Mumford (Algiers, 1 Nov 1965): decided on the scans in part 2.
- **Where (his pages):** cote 13, scans 10, 23-24, 29-32, 39-40, 42, 44, 46-47.
- **Where (our notes):** codex:H13-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/H13-01/out/H13-01_notes.md`; codex:J13-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J13-01/out/J13-01_notes.md`; codex:J13-02 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J13-02/out/J13-02_notes.md`; codex:J13-03 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J13-03/out/J13-03_notes.md`; codex:J13-04 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J13-04/out/J13-04_notes.md`; codex:J13-05 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J13-05/out/J13-05_notes.md`.
- **Across topics:** linked SA06-4 (H041), SA06-2, SA07-2.
- **Uses:** SA05-8 (his page). **Used by:** nothing recorded.
- **His claims:** 6 entries: known since Griffiths transversality (1968); Griffiths-Robles-Toledo (2014): quotients of non-classical flag domains are not algebraic; Borel density for his margin question.

## SA05-10: absolute cohomology of motives and arithmetic: Ext and effaceability, Ind-motives, the finiteness conjectures (Tate, BSD, Sha, Brauer), the G_m calculation, rational points, zeta and L-invariants (cote 12, scans 051-098)

- **Status:** his claims; open in general. Absolute cohomology of motives and arithmetic; with 'Calculs de cohomologie absolue des Motifs de Tate Z(n)' (cote 15, 172-178).
- **Where (his pages):** cote 12, scans 51-57, 59-65, 67-69, 71-80, 82, 84-85, 93-98; cote 15, scans 173-178, 207, 209, 211, 213-215, 217; cote 18, scans 33-36, 40, 43, 47.
- **Where (our notes):** MPL_12_051-098 (31) in `grothendieck_archive_transcription_20261110/returns/MPL_12_051-098_unzipped/MPL_12_051-098_notes.md`; work:K12-04 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K12-04/out/K12-04_mathnotes.md`; work:K12-05 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K12-05/out/K12-05_mathnotes.md`; MPL_15_139-194:records:research_leads_before_context (6) in `grothendieck_archive_transcription_20261110/returns/MPL_15_139-194_checkpoint_01_unzipped/research_leads_before_context.md`; work:K15-09 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K15-09/out/K15-09_mathnotes.md`; work:K18-03 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K18-03/out/K18-03_mathnotes.md`; codex:B12-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/B12-01/out/B12-01_notes.md`; codex:K12-04 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K12-04/out/K12-04_notes.md`; and 3 more sources.
- **Uses:** SA05-12 (proof). **Used by:** nothing recorded.
- **His claims:** 25 entries: no proof or refutation found in the register or the topic.
- **Flags (1):** the same thing noted with different readings or statements: a later vanishing on the pages contradicts the earlier degree-two example (N037: the constant Jacobian gives a

## SA05-13: smooth integral motives over a base: the one-prime independence conjecture, integral structures, extension over the base, the essential image (cote 12)

- **Status:** his conjectures, open. Smooth integral motives over a base; the one-prime independence conjecture.
- **Where (his pages):** cote 12, scans 142.
- **Where (our notes):** MPL_12_099-149 (18) in `grothendieck_archive_transcription_20261110/returns/MPL_12_099-149_unzipped/MPL_12_099-149_notes.md`.
- **Uses:** SA05-12 (proof). **Used by:** nothing recorded.
- **His claims:** 0 entries: no proof or refutation found in the register or the topic.

## SA05-18: motives over finite fields: the Weil-number protorus, the Artin-Tate quotient and the mu_2 factor, the rational Frobenius, real and p-adic fibre functors, gerbes (cote 15, scans 2-14)

- **Status:** his notes; known conditionally. Motives over finite fields (cote 15, 2-14), = H046; Milne (1994), conditional on the Tate conjecture.
- **Where (his pages):** cote 12, scans 2-3, 5-7, 9, 11, 13-16, 18, 21, 49, 52, 54, 88, 117, 213.
- **Where (our notes):** MPL_12_150-168+15_002-033 (27) in `grothendieck_archive_transcription_20261110/returns/MPL_12_150-168+15_002-033_unzipped/MPL_12_150-168+15_002-033/MPL_12_150-168+15_002-033_notes.md`.
- **Across topics:** = H046 (CM motives over finite fields; SA06-9); linked H03R (SA06-10).
- **Uses:** SA05-8 (proof), SA05-9 (proof). **Used by:** SA05-19 (proof).
- **His claims:** 1 entries: known conditionally Milne, 'Motives over finite fields' (1994).

## SA05-19: Deuring's gerbes and norm categories: rank-one objects over maximal orders, Azumaya algebras and the reduced norm, the definite quaternion and supersingular cases, Kummer and square classes (cote 15, scans 16-32)

- **Status:** his notes; known in substance. Deuring's gerbes and norm categories (cote 15, 16-32), = H045; Deuring (1941).
- **Where (his pages):** cote 12, scans 1, 6, 15-24, 26, 28, 30, 32, 119, 123, 135, 203.
- **Where (our notes):** MPL_12_150-168+15_002-033 (31) in `grothendieck_archive_transcription_20261110/returns/MPL_12_150-168+15_002-033_unzipped/MPL_12_150-168+15_002-033/MPL_12_150-168+15_002-033_notes.md`.
- **Across topics:** = H045 (Deuring gerbes; SA06-8).
- **Uses:** SA05-18 (proof). **Used by:** nothing recorded.
- **His claims:** 3 entries: known in substance Deuring (1941).

## SA05-14: linear versus nonlinear statements: Hom of Jacobians against Hom of curves, the anabelian analogies (cote 12)

- **Status:** his question; known in parts. Linear against nonlinear: Hom of Jacobians against Hom of curves (Faltings 1983; Mochizuki 1999).
- **Where (his pages):** cote 12, scans 57, 59.
- **Where (our notes):** MPL_12_099-149 (7) in `grothendieck_archive_transcription_20261110/returns/MPL_12_099-149_unzipped/MPL_12_099-149_notes.md`; MPL_12_002-050 (1) in `grothendieck_archive_transcription_20261110/returns/MPL_12_002-050_unzipped/MPL_12_002-050_notes.md`; MPL_12_051-098 (1) in `grothendieck_archive_transcription_20261110/returns/MPL_12_051-098_unzipped/MPL_12_051-098_notes.md`.
- **Uses:** SA05-12 (proof). **Used by:** nothing recorded.
- **His claims:** 0 entries: known in parts Faltings (1983); Mochizuki (1999).
- **Flags (2):** the LM/Dérivateurs lens: 'The prime-to-p point problem is not answered here': the note reads cote 12 through the research run's point-section question (ANABELIAN A1) | the LM/Dérivateurs lens: the note reads the page through a research-run or LM planning question: LN07 — The prime-to-p point problem is not answered here

## SA05-15: Oda's comparison of de Rham/Dieudonné realizations in characteristic p

- **Status:** known. Oda (1969).
- **Where (his pages):** cote 11, scans 17, 27, 34, 42; cote 12, scans 7, 74.
- **Where (our notes):** MPL_12_099-149 (2) in `grothendieck_archive_transcription_20261110/returns/MPL_12_099-149_unzipped/MPL_12_099-149_notes.md`; MPL_11_002-042 (1) in `grothendieck_archive_transcription_20261110/returns/MPL_11_002-042_unzipped/MPL_11_002-042_notes.md`; MPL_11_043-058+56 (1) in `grothendieck_archive_transcription_20261110/returns/MPL_11_043-058+56_unzipped/MPL_11_043-058+56_notes.md`; MPL_12_051-098 (1) in `grothendieck_archive_transcription_20261110/returns/MPL_12_051-098_unzipped/MPL_12_051-098_notes.md`.
- **Uses:** nothing recorded. **Used by:** nothing recorded.
- **His claims:** 0 entries: no proof or refutation found in the register or the topic.

## SA05-3: the cohomology of quadrics (= SA18-16)

- **Status:** = SA18-16. See SA18.
- **Where (his pages):** cote 11, scans 2, 30.
- **Where (our notes):** MPL_11_043-058+56 (35) in `grothendieck_archive_transcription_20261110/returns/MPL_11_043-058+56_unzipped/MPL_11_043-058+56_notes.md`.
- **Uses:** nothing recorded. **Used by:** nothing recorded.
- **His claims:** 12 entries: no proof or refutation found in the register or the topic.
- **Flags (1):** a link across folders: SA05-1, SA05-3, SA05-4, SA05-5 are the same objects as SA18-15, SA18-16, SA18-2, SA18-3

## SA05-4: a cancelled group-scheme text: reductive centre, maximal tori, the Weyl group (= SA18-2, its cote 11 part)

- **Status:** = SA18-2. A cancelled group-scheme text, with the B10-01..03 sections 10-11 (affine group preschemes).
- **Where (his pages):** cote 10, scans 43, 45, 50-51, 56-57; cote 11, scans 16; cote 18, scans 21, 24, 26, 28.
- **Where (our notes):** MPL_11_043-058+56 (21) in `grothendieck_archive_transcription_20261110/returns/MPL_11_043-058+56_unzipped/MPL_11_043-058+56_notes.md`; work:K18-02 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K18-02/out/K18-02_mathnotes.md`; codex:B10-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/B10-01/out/B10-01_notes.md`; codex:B10-02 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/B10-02/out/B10-02_notes.md`; codex:B10-03 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/B10-03/out/B10-03_notes.md`; codex:K18-02 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K18-02/out/K18-02_notes.md`.
- **Uses:** nothing recorded. **Used by:** nothing recorded.
- **His claims:** 20 entries: no proof or refutation found in the register or the topic.
- **Flags (1):** a link across folders: SA05-1, SA05-3, SA05-4, SA05-5 are the same objects as SA18-15, SA18-16, SA18-2, SA18-3

## SA05-5: Delzant's offprint: the Witt ring, Stiefel-Whitney and Clifford invariants, Brauer generation (= SA18-3, its cote 11 part)

- **Status:** = SA18-3. Delzant's offprint.
- **Where (his pages):** cote 11.
- **Where (our notes):** MPL_11_043-058+56 (13) in `grothendieck_archive_transcription_20261110/returns/MPL_11_043-058+56_unzipped/MPL_11_043-058+56_notes.md`.
- **Uses:** nothing recorded. **Used by:** nothing recorded.
- **His claims:** 6 entries: no proof or refutation found in the register or the topic.
- **Flags (1):** a link across folders: SA05-1, SA05-3, SA05-4, SA05-5 are the same objects as SA18-15, SA18-16, SA18-2, SA18-3

## SA05-7: a reused typescript on spherical buildings: Tits's centre conjecture, geodesics, parabolic characters, proper actions, descent and quotients (cote 11)

- **Status:** reused typescript; proved since. Tits's centre conjecture for spherical buildings, a theorem since 2006-2013 (Mühlherr-Tits; Leeb-Ramos-Cuevas; Ramos-Cuevas).
- **Where (his pages):** cote 11, scans 4, 6, 12, 14, 16, 18, 20, 22, 24, 26, 28, 32, 35, 37, 39, 41.
- **Where (our notes):** MPL_11_002-042 (15) in `grothendieck_archive_transcription_20261110/returns/MPL_11_002-042_unzipped/MPL_11_002-042_notes.md`.
- **Uses:** nothing recorded. **Used by:** nothing recorded.
- **His claims:** 11 entries: proved since Tits's centre conjecture (Mühlherr-Tits; Leeb-Ramos-Cuevas; Ramos-Cuevas, 2006-2013).

## SA05-17: the dossiers as documents and registers: evidence keys, title sheets, page counts, results-register uptake, references

- **Status:** documents and registers. Titles, page counts, reused typescripts (EGA 0, reflexive modules, invariant forms, valuations), the papers list of K18-01.
- **Where (his pages):** cote 10, scans 33, 43, 48, 51-58, 60-69, 77-84, 86-87, 102, 115-122, 131-137; cote 11, scans 3-4, 6, 15, 23, 27-32, 34-42, 44, 48, 51; cote 12, scans 2-5, 9, 12, 15-16, 18, 24, 26-27, 30, 36, 42-43, 47, 51, 53-54, 56, 60, 66, 70, 72, 74, 77, 81, 83-86, 90, 96-97, 99-100, 102, 105, 111, 115-117, 119-121, 123, 125-126, 128, 130, 132, 134, 136, 138-139, 141, 143-144, 149-151, 155-156, 158-160, 162, 164, 166, 168; cote 13, scans 2, 4, 14-16, 21, 23, 27, 29, 31-32, 34, 38, 46, 48, 51; cote 14, scans 2-15, 87-88, 90-91, 93, 97, 99; cote 15, scans 87-89, 91-97, 99-101, 104-106, 108, 112, 114, 118, 157, 160, 162, 164, 166, 172, 208, 210-216, 218, 220, 222, 224, 226, 228; cote 16, scans 3, 31-35, 37, 43-44, 48, 51-52, 54, 56; cote 18, scans 2-7, 9-18, 20, 22, 24, 26, 28, 30-32, 35, 37, 42-44, 46, 48-52, 54-62.
- **Where (our notes):** MPL_12_099-149 (11) in `grothendieck_archive_transcription_20261110/returns/MPL_12_099-149_unzipped/MPL_12_099-149_notes.md`; MPL_11_002-042 (7) in `grothendieck_archive_transcription_20261110/returns/MPL_11_002-042_unzipped/MPL_11_002-042_notes.md`; MPL_12_150-168+15_002-033 (7) in `grothendieck_archive_transcription_20261110/returns/MPL_12_150-168+15_002-033_unzipped/MPL_12_150-168+15_002-033/MPL_12_150-168+15_002-033_notes.md`; MPL_15_139-194:records:research_leads_before_context (6) in `grothendieck_archive_transcription_20261110/returns/MPL_15_139-194_checkpoint_01_unzipped/research_leads_before_context.md`; work:K15-03 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K15-03/out/K15-03_mathnotes.md`; work:K15-04 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K15-04/out/K15-04_mathnotes.md`; work:K15-10 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K15-10/out/K15-10_mathnotes.md`; work:K18-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K18-01/out/K18-01_mathnotes.md`; and 47 more sources.
- **Uses:** nothing recorded. **Used by:** nothing recorded.
- **His claims:** 11 entries: no proof or refutation found in the register or the topic.
- **Flags (1):** the LM/Dérivateurs lens: the note reads the page through a research-run or LM planning question: Results-register status and what this package adds
