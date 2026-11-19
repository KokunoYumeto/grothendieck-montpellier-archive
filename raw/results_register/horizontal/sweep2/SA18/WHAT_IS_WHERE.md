# SA18: what is where

Claude Opus 5.5 at effort max, a28ea31fa17dd65e1, sweep 2 part 2, 18 Nov 2026. Built from this folder's PLACEMENT, OBJECTS, FLAGS,
DEPENDS, CLAIM_LINKS and UNIT_LINKS (sweep 1 and sweep 2). Items are in mathematical order.

How to read the links: 'Uses' and 'Used by' come from DEPENDS.tsv, with the basis in brackets (his page: the page
refers to or builds on it; our note: a note links them; proof: the mathematics requires it). Claim links are
item-level unless a row says 'decided on the scan': 'known' means the item's subject is established in the cited
literature, not that each of his claims was checked one by one. Companion units come from
UNITS_DRAFT_20261118.tsv, which does not yet cover every folder.

SA18 is cotes 45-56 (Variétés abéliennes), with the shared package MPL_16+47+54+44. Group schemes (cotes 45, 46, 48, 53),
quadratic forms and quadrics (45, 56), the Picard functor of abelian schemes (49-52), the Fourier transform (47), duality
and intermediate Jacobians (44 via 54), integral models (cote 16 package), Stein spaces (55). Reading decided on the scan
in sweep 2: REPORTS/cote47_scan009_chi_factor.md. The second-pass verdicts on MPL_16+47+54+44 are in this folder's
CHECK_EVENTS.

| # | Item | Entries | Status |
|---|---|---:|---|
| 1 | SA18-21: schemes and group schemes over a field (cote 53, J series): connected and irredu | 5 | his notes; known |
| 2 | SA18-1: infinitesimal theory of group schemes: hyperalgebras (distributions), deformatio | 23 | his text; known |
| 3 | SA18-7: relative Frobenius and Verschiebung; infinitesimal group schemes and Frobenius k | 17 | his text; known |
| 4 | SA18-2: forms of tori and reductive group schemes: nonabelian H1 and its fibres, outer a | 46 | his text; known |
| 5 | SA18-6: torsors under twisted groups, Lang's theorem and unit Frobenius modules | 21 | his text; known |
| 6 | SA18-9: étale sheaves and cohomological triviality; the axioms a) and b) | 7 | his notes |
| 7 | SA18-10: Brauer-Severi schemes, linear systems and descent; the Picard obstruction | 21 | his text; known |
| 8 | SA18-3: quadratic and bilinear forms over rings and fields: the Witt ring, discriminant, | 34 | another author's offprint and his notes; known |
| 9 | SA18-16: the cohomology of quadrics (even, odd, affine, cones): Gysin maps, specializatio | 49 | his text; known |
| 10 | SA18-17: the Picard functor of an abelian scheme and its automorphisms: cohomological fla | 35 | his text; known |
| 11 | SA18-8: Picard p-torsion, Cartier duality, restricted Lie algebras of height one, and Od | 15 | his text; known |
| 12 | SA18-14: duality of abelian varieties, the universal vector extension, intermediate Jacob | 23 | his claims; known in substance |
| 13 | SA18-13: the Fourier transform of abelian varieties (cote 47): kernels and inversion, det | 28 | his construction; known since |
| 14 | SA18-11: integral models and local duality: exterior models, discriminant pairings, resol | 23 | his claims; partly known |
| 15 | SA18-15: correspondences and the construction of motives: correspondence rings, tautologi | 34 | his construction; known as definitions |
| 16 | SA18-12: abstract Lefschetz algebras and the standard conjectures (Lefschetz type, Hodge  | 21 | conjectures, open |
| 17 | SA18-20: orbit calculations in tensor squares (cote 16, scans 25-29) | 5 | his calculations |
| 18 | SA18-18: coherent analytic sheaves on compact Stein spaces; dimension in fibres (cote 55) | 7 | his notes; known |
| 19 | SA18-5: the programme's carry questions: a second Fourier witness (cote 47) and earlier  | 19 | planning |
| 20 | SA18-4: reused typescripts and sheets: ordered fields, local subrings, soft sheaves, iso | 13 | reused typescripts |
| 21 | SA18-19: the dossier as a document: titles, headings, pagination, references, citation co | 32 | documents |

## SA18-21: schemes and group schemes over a field (cote 53, J series): connected and irreducible components, a geometric-irreducibility criterion and its 'rectificatif', finite etale schemes, representability of Hom(G, G_m), immersions of monoids, induced operations

- **Status:** his notes; known. Schemes and group schemes over a field (cote 53): components, geometric irreducibility, finite étale schemes, Hom(G, G_m); questions open on the sheets.
- **Where (his pages):** cote 53, scans 3, 5-6, 8-9, 11, 13, 15-17, 20, 25, 29.
- **Where (our notes):** codex:J53-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J53-01/out/J53-01_notes.md`; codex:J53-02 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J53-02/out/J53-02_notes.md`; codex:J53-03 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J53-03/out/J53-03_notes.md`; codex:J53-04 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J53-04/out/J53-04_notes.md`; codex:J53-05 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J53-05/out/J53-05_notes.md`.
- **Across topics:** linked SA19-2 (duality of group schemes: Hom(G, G_m)); H0CB.
- **Uses:** nothing recorded. **Used by:** SA18-1 (proof), SA18-2 (proof).
- **His claims:** 5 entries: known SGA 3 VI_A; EGA IV §4.
- **Flags (1):** a link across folders: Cote 53 asks 'Hom(G, G_m) representable ?' for group schemes over a field and leaves the base (S or k) open; this is Cartier duality for groups of 

## SA18-1: infinitesimal theory of group schemes: hyperalgebras (distributions), deformations, Lie algebra cohomology H0, H1, H2 and rigidity

- **Status:** his text; known. Hyperalgebras and the infinitesimal theory of group schemes (SGA 3 II, VII_A).
- **Where (his pages):** cote 45, scans 4, 6, 18-27, 29-32, 34-36, 38, 40, 42, 246.
- **Where (our notes):** MPL_45_033-080 (9) in `grothendieck_archive_transcription_20261110/returns/MPL_45_033-080_unzipped/MPL_45_033-080_notes.md`; work:K45-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K45-01/out/K45-01_mathnotes.md`; work:K45-02 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K45-02/out/K45-02_mathnotes.md`; codex:K45-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K45-01/out/K45-01_notes.md`; codex:K45-02 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K45-02/out/K45-02_notes.md`.
- **Uses:** SA18-21 (proof). **Used by:** SA18-7 (proof).
- **His claims:** 4 entries: known SGA 3 II and VII_A; Demazure-Gabriel.
- **Companion units (27):** Lemma and its reductions —; Finite-kernel corollary —; Frobenius lemma and corollary — ...

## SA18-7: relative Frobenius and Verschiebung; infinitesimal group schemes and Frobenius kernels; affineness

- **Status:** his text; known. Relative Frobenius and Verschiebung, Frobenius kernels (SGA 3 VII_A).
- **Where (his pages):** cote 45, scans 40, 68; cote 46, scans 13, 17, 19, 24, 26; cote 56.
- **Where (our notes):** MPL_46_002-048 (13) in `grothendieck_archive_transcription_20261110/returns/MPL_46_002-048_unzipped/MPL_46_002-048_notes.md`; MPL_45_033-080 (2) in `grothendieck_archive_transcription_20261110/returns/MPL_45_033-080_unzipped/MPL_45_033-080_notes.md`; MPL_11_043-058+56 (1) in `grothendieck_archive_transcription_20261110/returns/MPL_11_043-058+56_unzipped/MPL_11_043-058+56_notes.md`; codex:C46-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/C46-01/out/C46-01_notes.md`.
- **Uses:** SA18-1 (proof). **Used by:** SA18-6 (proof), SA18-8 (proof).
- **His claims:** 6 entries: known SGA 3 VII_A.

## SA18-2: forms of tori and reductive group schemes: nonabelian H1 and its fibres, outer automorphisms, pinnings, maximal tori, the reductive centre and the Weyl group

- **Status:** his text; known. Forms of tori and reductive group schemes, isotriviality over a field (SGA 3 VIII-X, XXIV).
- **Where (his pages):** cote 45, scans 45, 47, 49, 51, 53, 55, 57, 59; cote 48; cote 56, scans 16, 33, 38, 176, 255, 715.
- **Where (our notes):** MPL_11_043-058+56 (20) in `grothendieck_archive_transcription_20261110/returns/MPL_11_043-058+56_unzipped/MPL_11_043-058+56_notes.md`; MPL_45_033-080 (18) in `grothendieck_archive_transcription_20261110/returns/MPL_45_033-080_unzipped/MPL_45_033-080_notes.md`; work:K56-03 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K56-03/out/K56-03_mathnotes.md`; codex:H48-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/H48-01/out/H48-01_notes.md`; codex:K56-03 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K56-03/out/K56-03_notes.md`.
- **Uses:** SA18-21 (proof). **Used by:** SA18-6 (his page).
- **His claims:** 17 entries: known SGA 3 VIII-X (isotriviality: X), XXIV.
- **Flags (2):** the LM/Dérivateurs lens: the note reads the page through a research-run or LM planning question: G18 — A comparison with the reviewed Kummer run has strict limits | a link across folders: Cote 48 (new to the register) has a section plan 'sur un corps' and the 'theoreme de l'isotrivialite sur un corps'; placed under SA18-2 (tori and r

## SA18-6: torsors under twisted groups, Lang's theorem and unit Frobenius modules

- **Status:** his text; known. Torsors under twisted groups and Lang's theorem (Lang 1956).
- **Where (his pages):** cote 46, scans 6-7, 9, 87, 91.
- **Where (our notes):** MPL_46_002-048 (7) in `grothendieck_archive_transcription_20261110/returns/MPL_46_002-048_unzipped/MPL_46_002-048_notes.md`; work:K46-01_2 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K46-01_2/out/K46-01_mathnotes.md`; work:K46-03 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K46-03/out/K46-03_mathnotes.md`; MPL_46_002-048:records:research_leads (1) in `grothendieck_archive_transcription_20261110/returns/MPL_46_002-048_unzipped/records/research_leads.md`; codex:K46-03 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K46-03/out/K46-03_notes.md`.
- **Uses:** SA18-2 (his page), SA18-7 (proof). **Used by:** SA18-10 (proof).
- **His claims:** 3 entries: known Lang (1956).
- **Companion units (9):** Twisting an action; Invariants and equivalent twists; Averaging and a finite-dimensional algebra argument (, top ...

## SA18-9: étale sheaves and cohomological triviality; the axioms a) and b)

- **Status:** his notes. Étale sheaves and cohomological triviality; axioms a) and b).
- **Where (his pages):** cote 46, scans 29, 31, 38-39.
- **Where (our notes):** MPL_46_002-048 (7) in `grothendieck_archive_transcription_20261110/returns/MPL_46_002-048_unzipped/MPL_46_002-048_notes.md`.
- **Uses:** nothing recorded. **Used by:** nothing recorded.
- **His claims:** 2 entries: no proof or refutation found in the register or the topic.

## SA18-10: Brauer-Severi schemes, linear systems and descent; the Picard obstruction

- **Status:** his text; known. Brauer-Severi schemes and descent; the Picard obstruction (Le groupe de Brauer I).
- **Where (his pages):** cote 46, scans 58.
- **Where (our notes):** MPL_46_002-048 (14) in `grothendieck_archive_transcription_20261110/returns/MPL_46_002-048_unzipped/MPL_46_002-048_notes.md`; work:K46-02 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K46-02/out/K46-02_mathnotes.md`; codex:K46-02 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K46-02/out/K46-02_notes.md`.
- **Uses:** SA18-6 (proof). **Used by:** nothing recorded.
- **His claims:** 11 entries: known Grothendieck, Le groupe de Brauer I.
- **Flags (1):** the same thing noted with different readings or statements: our transcription reads an inserted 'mono' ('un monomorphisme P^ -> P(Q), je dis que c'est un isom sur un P(E)
- **Companion units (8):** Brauer classes and obstruction questions; Restriction of scalars; Purely inseparable examples ...

## SA18-3: quadratic and bilinear forms over rings and fields: the Witt ring, discriminant, Clifford and Stiefel-Whitney invariants, characteristic two; Delzant's offprint

- **Status:** another author's offprint and his notes; known. Quadratic forms, the Witt ring, Delzant's Stiefel-Whitney classes (1962); the lambda-structure (C45-01).
- **Where (his pages):** cote 45, scans 62, 64, 66, 68, 70, 76-79; cote 56.
- **Where (our notes):** MPL_45_033-080 (21) in `grothendieck_archive_transcription_20261110/returns/MPL_45_033-080_unzipped/MPL_45_033-080_notes.md`; MPL_11_043-058+56 (12) in `grothendieck_archive_transcription_20261110/returns/MPL_11_043-058+56_unzipped/MPL_11_043-058+56_notes.md`; codex:C45-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/C45-01/out/C45-01_notes.md`.
- **Uses:** nothing recorded. **Used by:** SA18-16 (proof).
- **His claims:** 7 entries: known Delzant (1962); Witt rings.

## SA18-16: the cohomology of quadrics (even, odd, affine, cones): Gysin maps, specialization, local and compact supports, torsion

- **Status:** his text; known. The cohomology of quadrics (SGA 7 XII).
- **Where (his pages):** cote 56, scans 2, 5, 15-18, 20-27, 30.
- **Where (our notes):** MPL_11_043-058+56 (35) in `grothendieck_archive_transcription_20261110/returns/MPL_11_043-058+56_unzipped/MPL_11_043-058+56_notes.md`; work:K56-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K56-01/out/K56-01_mathnotes.md`; work:K56-02 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K56-02/out/K56-02_mathnotes.md`; codex:K56-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K56-01/out/K56-01_notes.md`; codex:K56-02 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K56-02/out/K56-02_notes.md`.
- **Uses:** SA18-3 (proof). **Used by:** nothing recorded.
- **His claims:** 16 entries: known SGA 7 XII.
- **Flags (1):** the LM/Dérivateurs lens: the note reads the page through a research-run or LM planning question: N061 — The local pairing is an input to investigate for WG H9

## SA18-17: the Picard functor of an abelian scheme and its automorphisms: cohomological flatness, translations, equivalence of divisors, Pic and Alb, Hom and rational sections

- **Status:** his text; known. The Picard functor of an abelian scheme and its automorphisms.
- **Where (his pages):** cote 49, scans 3-10; cote 50, scans 2-11; cote 51, scans 2-12; cote 52, scans 2-14.
- **Where (our notes):** work:K49-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K49-01/out/K49-01_mathnotes.md`; work:K50-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K50-01/out/K50-01_mathnotes.md`; work:K51-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K51-01/out/K51-01_mathnotes.md`; work:K51-02 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K51-02/out/K51-02_mathnotes.md`; work:K52-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K52-01/out/K52-01_mathnotes.md`; codex:K49-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K49-01/out/K49-01_notes.md`; codex:K50-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K50-01/out/K50-01_notes.md`; codex:K51-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K51-01/out/K51-01_notes.md`; and 2 more sources.
- **Uses:** nothing recorded. **Used by:** SA18-8 (proof), SA18-14 (proof), SA18-13 (his page).
- **His claims:** 10 entries: no proof or refutation found in the register or the topic.
- **Companion units (51):** U1 · The Picard theorem; U2 · The translation map; U3 · A local flatness lemma ...

## SA18-8: Picard p-torsion, Cartier duality, restricted Lie algebras of height one, and Oda's comparison

- **Status:** his text; known. Picard p-torsion, Cartier duality, Oda's comparison (Oda 1969).
- **Where (his pages):** cote 46, scans 21; cote 56.
- **Where (our notes):** MPL_46_002-048 (14) in `grothendieck_archive_transcription_20261110/returns/MPL_46_002-048_unzipped/MPL_46_002-048_notes.md`; MPL_11_043-058+56 (1) in `grothendieck_archive_transcription_20261110/returns/MPL_11_043-058+56_unzipped/MPL_11_043-058+56_notes.md`.
- **Across topics:** SA14 (Picard), SA15 (crystals).
- **Uses:** SA18-7 (proof), SA18-17 (proof). **Used by:** nothing recorded.
- **His claims:** 5 entries: known Oda (1969).

## SA18-14: duality of abelian varieties, the universal vector extension, intermediate Jacobians and the seven theorems of cote 44

- **Status:** his claims; known in substance. Duality of abelian varieties, the universal vector extension (Mazur-Messing 1974), intermediate Jacobians; the seven theorems of cote 44.
- **Where (his pages):** cote 47, scans 2-9; cote 54, scans 2-9.
- **Where (our notes):** MPL_16+47+54+44 (16) in `grothendieck_archive_transcription_20261110/returns/MPL_16+47+54+44_unzipped/MPL_16+47+54+44_notes.md`; work:K54-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K54-01/out/K54-01_mathnotes.md`; codex:K54-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K54-01/out/K54-01_notes.md`.
- **Across topics:** SA19 (Jacobians), SA14 (Picard).
- **Uses:** SA18-17 (proof). **Used by:** SA18-13 (his page), SA18-11 (proof), SA18-5 (our note).
- **His claims:** 8 entries: known duality of abelian schemes; universal vector extension (Mazur-Messing 1974).
- **Flags (1):** a link across folders: the 'second Fourier witness' (cote 47) and the 'seven Jacobian theorems' (cote 44) are asked in three packages; one item SA18-5 with the cote 47 an

## SA18-13: the Fourier transform of abelian varieties (cote 47): kernels and inversion, determinant lines, Chern classes, Riemann-Roch and integrality

- **Status:** his construction; known since. The Fourier transform of abelian schemes (cote 47): Lemma 2 admitted, a compatibility left open, a slip in the Chern-class expansion (47:9, decided in part 2); the inversion theorem is Mukai's (1981).
- **Where (his pages):** cote 47, scans 1, 3-11, 27; cote 54, scans 3-11.
- **Where (our notes):** MPL_16+47+54+44 (21) in `grothendieck_archive_transcription_20261110/returns/MPL_16+47+54+44_unzipped/MPL_16+47+54+44_notes.md`; work:K47-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K47-01/out/K47-01_mathnotes.md`; codex:K47-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K47-01/out/K47-01_notes.md`.
- **Across topics:** SA19 (Jacobians), SA07 (motives), SA14 (Picard).
- **Uses:** SA18-14 (his page), SA18-17 (his page). **Used by:** SA18-5 (our note).
- **His claims:** 7 entries: known since Mukai (1981), the Fourier-Mukai transform and its inversion.
- **Flags (2):** a link across folders: the 'second Fourier witness' (cote 47) and the 'seven Jacobian theorems' (cote 44) are asked in three packages; one item SA18-5 with the cote 47 an | suspected misreading: The Work model remark M1 (high confidence): at chi = 3 the displayed power should have quadratic and cubic coefficients 1/3 and -1/27, while the wri

## SA18-11: integral models and local duality: exterior models, discriminant pairings, resolution, Brauer quotients, injective modules, the different, trace duality, EGA/SGA corrections

- **Status:** his claims; partly known. Integral models and local duality: exterior models, discriminant pairings, Brauer questions (SGA 7 IX).
- **Where (his pages):** cote 47, scans 9-10, 14, 16, 19, 21, 23, 26, 37, 39, 41, 43, 52, 54; cote 54, scans 9-10, 14, 16, 19, 21, 23, 26, 37, 39, 41, 43, 52, 54.
- **Where (our notes):** MPL_16+47+54+44 (23) in `grothendieck_archive_transcription_20261110/returns/MPL_16+47+54+44_unzipped/MPL_16+47+54+44_notes.md`.
- **Uses:** SA18-14 (proof). **Used by:** nothing recorded.
- **His claims:** 3 entries: known in part SGA 7 IX (Grothendieck's pairing).

## SA18-15: correspondences and the construction of motives: correspondence rings, tautological classes, excess intersection, Euler characteristics, the sorted-weight cone

- **Status:** his construction; known as definitions. Correspondences and the construction of motives.
- **Where (his pages):** cote 56, scans 36, 45, 55.
- **Where (our notes):** MPL_11_043-058+56 (34) in `grothendieck_archive_transcription_20261110/returns/MPL_11_043-058+56_unzipped/MPL_11_043-058+56_notes.md`.
- **Uses:** nothing recorded. **Used by:** SA18-12 (proof).
- **His claims:** 17 entries: no proof or refutation found in the register or the topic.
- **Flags (2):** the LM/Dérivateurs lens: the note reads the page through a research-run or LM planning question: N061 — The local pairing is an input to investigate for WG H9 | the LM/Dérivateurs lens: the note reads the page through a research-run or LM planning question: N099 — The open section-class item and the reviewed descent item keep the

## SA18-12: abstract Lefschetz algebras and the standard conjectures (Lefschetz type, Hodge type, numerical versus homological equivalence, Künneth projectors)

- **Status:** conjectures, open. Abstract Lefschetz algebras and the standard conjectures; open in general, known for abelian varieties in characteristic 0 (Lieberman 1968).
- **Where (his pages):** cote 47, scans 3, 5, 14-17, 33-34, 40, 42, 44-51; cote 54, scans 3, 5, 14-17, 33-34, 40, 42, 44-51; cote 56.
- **Where (our notes):** MPL_16+47+54+44 (20) in `grothendieck_archive_transcription_20261110/returns/MPL_16+47+54+44_unzipped/MPL_16+47+54+44_notes.md`; MPL_11_043-058+56 (1) in `grothendieck_archive_transcription_20261110/returns/MPL_11_043-058+56_unzipped/MPL_11_043-058+56_notes.md`.
- **Across topics:** SA07, SA05, SA06 (motives).
- **Uses:** SA18-15 (proof). **Used by:** SA18-20 (his page).
- **His claims:** 2 entries: open the standard conjectures; known for abelian varieties in characteristic 0 (Lieberman 1968).
- **Flags (1):** the LM/Dérivateurs lens: the note reads the page through a research-run or LM planning question: N099 — The open section-class item and the reviewed descent item keep the

## SA18-20: orbit calculations in tensor squares (cote 16, scans 25-29)

- **Status:** his calculations. Orbit calculations in tensor squares (cote 16, scans 25-29); checked by the second pass (D16-D20).
- **Where (his pages):** cote 47, scans 25, 27, 29; cote 54, scans 25, 27, 29.
- **Where (our notes):** MPL_16+47+54+44 (5) in `grothendieck_archive_transcription_20261110/returns/MPL_16+47+54+44_unzipped/MPL_16+47+54+44_notes.md`.
- **Uses:** SA18-12 (his page). **Used by:** nothing recorded.
- **His claims:** 0 entries: no proof or refutation found in the register or the topic.

## SA18-18: coherent analytic sheaves on compact Stein spaces; dimension in fibres (cote 55)

- **Status:** his notes; known. Coherent analytic sheaves on compact Stein spaces.
- **Where (his pages):** cote 55, scans 102-104, 109-111.
- **Where (our notes):** work:K55-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K55-01/out/K55-01_mathnotes.md`; codex:K55-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K55-01/out/K55-01_notes.md`.
- **Uses:** nothing recorded. **Used by:** nothing recorded.
- **His claims:** 2 entries: no proof or refutation found in the register or the topic.
- **Companion units (11):** and — Modules on a compact Stein space; and — Codimension in a fibre; and — Dimension over a field ...

## SA18-5: the programme's carry questions: a second Fourier witness (cote 47) and earlier forms of the seven Jacobian theorems (cote 44); chronology and priority

- **Status:** planning. The programme's carry questions (cote 47 Fourier witness, cote 44).
- **Where (his pages):** cote 45, scans 3, 6-8, 33-34, 38, 49, 53, 67, 79; cote 46.
- **Where (our notes):** MPL_46_002-048 (11) in `grothendieck_archive_transcription_20261110/returns/MPL_46_002-048_unzipped/MPL_46_002-048_notes.md`; MPL_45_033-080 (8) in `grothendieck_archive_transcription_20261110/returns/MPL_45_033-080_unzipped/MPL_45_033-080_notes.md`.
- **Uses:** SA18-13 (our note), SA18-14 (our note). **Used by:** nothing recorded.
- **His claims:** 2 entries: no proof or refutation found in the register or the topic.
- **Flags (3):** the same thing noted with different readings or statements: our transcription reads an inserted 'mono' ('un monomorphisme P^ -> P(Q), je dis que c'est un isom sur un P(E) | a link across folders: the 'second Fourier witness' (cote 47) and the 'seven Jacobian theorems' (cote 44) are asked in three packages; one item SA18-5 with the cote 47 an | the LM/Dérivateurs lens: the note reads the page through a research-run or LM planning question: G18 — A comparison with the reviewed Kummer run has strict limits
- **Companion units (4):** Finite-kernel corollary —; Frobenius lemma and corollary —; Reduction of the H¹ problem — ...

## SA18-4: reused typescripts and sheets: ordered fields, local subrings, soft sheaves, isotropic subspaces, hermitian forms, exterior contractions, uniform structures, Coxeter pages, injective modules

- **Status:** reused typescripts. Used as paper.
- **Where (his pages):** cote 45, scans 33, 39, 46, 50, 58, 67, 69; cote 46, scans 29, 38.
- **Where (our notes):** MPL_45_033-080 (7) in `grothendieck_archive_transcription_20261110/returns/MPL_45_033-080_unzipped/MPL_45_033-080_notes.md`; MPL_46_002-048 (6) in `grothendieck_archive_transcription_20261110/returns/MPL_46_002-048_unzipped/MPL_46_002-048_notes.md`.
- **Uses:** nothing recorded. **Used by:** nothing recorded.
- **His claims:** 1 entries: no proof or refutation found in the register or the topic.

## SA18-19: the dossier as a document: titles, headings, pagination, references, citation conventions

- **Status:** documents. Titles, headings, pagination.
- **Where (his pages):** cote 45, scans 33, 37, 45; cote 46, scans 2, 85, 94-95; cote 47, scans 2-3, 11; cote 48; cote 49, scans 2, 10; cote 50; cote 51, scans 13, 22-23; cote 52, scans 2-3; cote 53, scans 2, 5-6, 10, 12-13, 15-21, 29, 33; cote 54; cote 55, scans 2, 17; cote 56, scans 5.
- **Where (our notes):** MPL_46_002-048 (4) in `grothendieck_archive_transcription_20261110/returns/MPL_46_002-048_unzipped/MPL_46_002-048_notes.md`; MPL_11_043-058+56 (3) in `grothendieck_archive_transcription_20261110/returns/MPL_11_043-058+56_unzipped/MPL_11_043-058+56_notes.md`; MPL_45_033-080 (2) in `grothendieck_archive_transcription_20261110/returns/MPL_45_033-080_unzipped/MPL_45_033-080_notes.md`; codex:C45-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/C45-01/out/C45-01_notes.md`; codex:C46-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/C46-01/out/C46-01_notes.md`; codex:H48-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/H48-01/out/H48-01_notes.md`; codex:J53-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J53-01/out/J53-01_notes.md`; codex:J53-02 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J53-02/out/J53-02_notes.md`; and 18 more sources.
- **Uses:** nothing recorded. **Used by:** nothing recorded.
- **His claims:** 0 entries: no proof or refutation found in the register or the topic.
- **Companion units (16):** Averaging and a finite-dimensional algebra argument (, top; Localization and completion; A new heading ...
