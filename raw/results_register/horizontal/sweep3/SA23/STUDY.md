# SA23 in depth (sweep 3, wave 1, 19 Nov 2026)

**Who did the work.** The lead is a3d30d2d3a27966ed (Claude Opus 5.5 at effort max). The readers are aac7b158968982dd2 (A, then A2) and acadc29d15e8e7c65 (B), both Claude Opus 5.5 at effort max.

**Scope.** SA23 is about 610 Pro and Codex pages over 17 cotes:
- functional analysis (1);
- Riemann-Roch notes (2);
- the EGA drafts and letters (21, 22, 23, 26);
- his dossiers on categories, universal algebra, topoi, an introduction to algebraic geometry, Barsotti-Tate, the icosahedron and Quillen's tapis (161-1 to 161-6, 162-1, 162-5, 162-6).

**The readings.** Each holds, per item, what he does, what is proved, what was checked, what is wrong and what is open:
- `readings/A_161-1_161-3.md`;
- `readings/A2_161-4_161-6_162.md`;
- `readings/B_1_2_21.md`;
- `readings/C_22_23_26_161-5.md`.

The item index is at the end of this file.

## What the pages contain and establish
### Cote 1, functional analysis (reader B)
- **Lidskii's theorem, in his hand.** On the crossed-out pages 1/079-080 he states and proves the trace formula Tr u = Σ λ_i for trace-class u on Hilbert space (Lidskii, 1959). He starts from the summable eigenvalues and |α_n(u)| ≤ α_n(|u|), and uses a genus-0 lemma "supposé connu" that he proves on 111-112. Reader B withdrew its earlier "cannot work" for 71. Not yet checked: whether his 1955-56 papers print this argument.
- **The determinant Δ.** On rings of operators with a trace, Δ(A) = exp ∫_0^{T(1)} log φ_|A|: the Fuglede-Kadison determinant in today's terms (our identification). His question on 30, Δ(B*HB) ?= Δ(A*A)Δ(B*B), is the missing step of his Prop. 8, Δ(AB) = Δ(A)Δ(B). Reader B proves it for invertible operators.
- **Readings.** Two were decided on the scan: 1/4 and 1/39. The heading on 1/082 reads "classes remarquables" (sweep 2).

### Cotes 2 and 21 (reader B; all 210 pages of B read: 72 check events, 31 corrections, 9 hunches)
- **Cote 2:** the lambda-ring and Chern-ring comparison (the sign of Proposition 2, F06: the ink reads (-1)^i, his slip), K with supports, Riemann-Roch for curves and surfaces. The formula on 2/045 is his slip, exact for f_*O_C~ (sweep 2).
- **Cote 21:** an EGA 0_III draft, "Notes pour Dieud.".

### Cote 22, the EGA 0_IV draft for Dieudonné (lead)
- **§4 "algèbres de Cohen" (22/010-018).** "Formellement simple" is the later "formellement lisse". Lemmas 4.2 and 4.3 and Corollaries 4.4-4.5 are correct, and Theorem 4.6 holds once its typescript slip is read as C for B (decided on the scan). Corollary 4.13 is the shape of printed 0_IV 19.7.1, with a residue-field hypothesis the print drops.
- **His proposed restructuring:** "en deux pages ou trois".
- **His open problems.**
  - The existence of Cohen lifts over square-zero thickenings in general (22/014).
  - **Four "Questions ouvertes" (22/020-021):** formally smooth vs universally regular; formal smoothness for the discrete topology; openness of the smooth-fibre locus; openness of the flat locus.
- **The discrete topology (22/024-025).** His Proposition, proved and checked: K[[t_1..t_n]] with the discrete topology is not formally smooth when Ω_{K/k} is infinite-dimensional. The finite-dimensional case in char 0, for example Q[[t]] over Q, is left open.
- **The Remarque and counterexamples (22/027-029).** Both are correct, with a finite example. The printed 0_IV 22.5.10(i) needs the root of the coefficient in K (F01).
- **His pencil on Jouanolou's CRAS note (1963).** The printed lemma needs A ⊂ B.

### Cote 23, EGA IV complements (lead)
- **Canonical sheaves and the discriminant (23/004-006).**
  - The canonical sheaves of complete intersections in P(E) are correct.
  - The discriminant degree (k−1)(r+1) is his slip; the true degree is (r+1)(k−1)^r, with weight k(k−1)^r in det E (decided on the scan).
- **Nilpotent exponential and hyperalgebras (23/008-016).** Cartier's theorem, infinitesimal automorphisms equal to derivations in char 0. Correct.
- **23/017-050.**
  - Weil restriction and "points proches"; smooth liftings as torsors; jet bundles and connections of order n.
  - Examples of regular, non-geometrically-regular rings.
  - His question on "foncteurs différentiels d'ordre ≤ n": the algebraic natural-bundle theorem.
  - A Bourbaki draft no. 215.
  - Lê Dũng Tráng's errata to EGA IV 20-21 (1968).
- **23/051-065.**
  - **His PS.** EGA IV 16.9.2's regular immersion "n'est pas la bonne notion": use Koszul-regular sequences, and add a remark 19.1.8.
  - **Three letters of Deligne (Oct-Dec 1966).** They contain errata to 0_IV, III and IV: 19.3.12, 16.1.5, 16.1.6, 19.5.6, III 4.3.6, and more. They also hold a proof of the minimal Cohen factorization of a local homomorphism, whose only open point is a "complete intersection" property of algebraic field extensions, and a characterization of regular ideals by Tor.
  - **His erratum decision on the sign of dx in 0_IV 20.4.6.**
- **23/066-099.**
  - The plan of the Zariski Main Theorem proofs (EGA IV 18.12).
  - Morphisms essentially of finite presentation.
  - Schemes with all points closed.
  - The (S_k) lemma along finite maps.
  - Finiteness of the normalization.
  - A non-Cohen-Macaulay-locus example (EGA IV 12).
  - A graded flatness criterion by Hilbert series, with his open question.
  - Lemma 1 of 23/083 has a quantifier slip: corrected.

### Cote 26 (lead)
A plan headed "V" (the catalogue says "EGA VI"): descent and quotients, non-projective and projective constructions (Hilbert, Picard, Mumford's invariants). It ends with "Problèmes-types à résoudre" a)-j), with his notes "OK. par Raynaud" and "oui".

### Cotes 161-1 to 161-3 (reader A)
- **Accessible categories (161-2, scans 55-62).** These sheets cite SGA 4 I by number (8.7, 8.9, 8.12.8.1, 8.13.2, 9.1-9.22), and every number checked matches the printed 1972 Exposé I.
  - He proposes "(modifié 9.4 ?)": accessible means Ind_π(C), the definition Makkai and Paré published in 1989.
  - He strengthens condition c) of SGA 4 I 9.12.
  - "Axiome c) des filtrations cardinales" is on scan 61, and its proof needs π'^π = π'.
- **"Topos modulaire" (scan 112).** It defines a classifying topos relative to a base topos X. It calls the 2-fibred product of topoi "pas encore prouvé", while scan 22 constructs it.
- 160 pages read, 74 check events, 18 corrections, 11 hunches.

### Cotes 161-4, 161-6, 162-1, 162-5, 162-6 (reader A2)
79 pages read (161-4: 27, 161-6: 26, 162-1: 9, 162-5: 12, 162-6: 5), 25 check events, 17 corrections, 6 hunches.
- **162-5, notes dated 6.9.68.** He defines a "Θ-Algèbre de Lie" (a Lie algebroid) and states "Quillen's theorem": in char 0, adic formal categories with flat Ω are equivalent to De Rham complexes. One step is false: δ_1δ_0 = 0 alone does not give δ² = 0 (a three-dimensional counterexample). His margin calls it a generalisation of "mon th. fondamental de démarrage des cristaux", which confirms F09 on the page.
- **161-6/018, F02 decided.** The ink reads "4π/5 < 2π/3": his slip.
- **162-1.** The loan list runs to about 1970; its 1964-67 dates are all in struck-through entries.
- **161-4 scan 18** belongs to the products-of-topoi series of 161-3.

### Cote 161-5 (lead)
- **Serre's offprints (1967, 1968-69).** Reused, with two margins citing Sen.
- **His notes, 23-29.** A Tannakian formulation of a crystalline realisation T_cr for the category generated by Barsotti-Tate groups: his "mysterious functor" programme, later Fontaine's. It leaves two questions:
  - can T_cr be extended to M^BT as a ⊗-functor, and is it unique?
  - is H^1(Γ, G'(S)) → H^1(π, G'(S)) injective?

## Unread stretches
- **Outside the 604 pages.** The API transcriptions of cote 24 (EGA V in English, 76 pages), cote 25 (Nouveau EGA V, 184 pages) and the 162-5 typescript of the tapis (51 pages) are not read.

## Item index of the readings
### Reading A2_161-4_161-6_162 (`readings/A2_161-4_161-6_162.md`)
- Cote 161-4, "Introduction à géométrie algébrique" (K161-4-01: scans 3-13, 15-17; K161-4-02: scans 18, 20-32; 27 pages)
- 1. Faithfully flat descent: a numbered course outline (scans 3-9, his pages 1-5 and two unnumbered sheets)
- 2. Ampleness, properties of morphisms, plan of a course (scans 10-13)
- 3. Schemes as functors (scans 15, 17)
- 4. A sheet of the products-of-topoi series (scan 18)
- 5. "Géom. Algébrique": affine algebraic spaces over k as functors (scans 20-32)
- Cote 161-6, "Graphes, icosaèdre" (K161-6-01: scans 2, 4-11, 13-17; K161-6-02: scans 18-20, 22-23, 25-31, 33-34; 26 pages; SA23-37)
- 6. The folder sheet (scan 2)
- 7. The icosahedron from a point and a tangent direction (scans 4-11)
- 8. Arithmetic of the pentagon: ζ_5, the golden ratio over Z[1/5] (scans 13, 15)
- 9. Stray sheets: frames and a flower (scans 16, 17)
- 10. The icosahedron again, A_5, and the icosahedron over a base scheme (scans 18-20, 22)
- 11. Graphs embedded in oriented surfaces (scans 25-31) and graph symmetries (scans 33-34)
- Cote 162-1, "Papiers prêtés" (H162-01, scans 2-10; 9 pages; SA23-55)
- Cote 162-5, "Le Tapis de Quillen, notes d'Alexandre (1968)" (K162-5-02: scan 2; K162-5-01: scans 20, 22-31; 12 pages; SA23-38, SA23-52)
- 12. Title and bibliography (scans 2, 20)
- 13. Formal categories, De Rham complexes, Lie algebroids, Quillen's theorem (scans 22-31, "Notes du 6.9.68")
- Cote 162-6, sheet "Gal(E/Q) - C(E)" (H162-02, scans 2-6; 5 pages; SA23-56)

### Reading A_161-1_161-3 (`readings/A_161-1_161-3.md`)
- Cote 161-1, "Catégories" (folder K161-1-01; scans 4-8, 10-14, 16-20; 15 pages)
- 1. Adjunctions and the largest subcategories where they are equivalences (scans 4-8; SA23-29)
- 2. Free symmetric monoidal category, products of families, contraction, signs (scans 10-13)
- 3. Theories with finite limits and their constructions (scan 14, his page "2")
- 4. Exactness of extended functors; topoi as left exact reflections (scan 16)
- 5. Stray sheet: Hodge-Tate cocharacter of filtered F-crystals (scan 17, upside down)
- 6. Extending functors from a strictly generating subcategory (scans 18-20; scan 19 is a small diagram)
- Dating clues in 161-1
- Cote 161-2, "Algèbre universelle [ou catégories]"
- K161-2-01 (scans 4-19; scans 10 and 16 nearly blank, 15 a list; 15 pages; SA23-30)
- K161-2-02 (scans 20-25, 27-32, 34-35; 14 pages; SA23-30, SA23-32)
- K161-2-03 (scans 37-50; scan 41 a margin only; 14 pages; SA23-31, SA23-32)
- K161-2-04 (scans 51-53, 55-65; scan 58 nearly blank; 14 pages; SA23-31, SA23-53)
- K161-2-05 (scans 66-79; scan 67 one line; 14 pages; SA23-30)
- K161-2-06 = K161-2-06_2 (scans 81-88, 90-95; 14 pages; the two folders have the same transcription, checked by comparison; SA23-30)
- K161-2-07 (scans 96, 98-107, 109-110, 112; 14 pages; SA23-30, SA23-54)
- Cote 161-3, "Topos"
- K161-3-01 (scans 4-13, 15-16, 18-21; 16 pages; SA23-32)
- K161-3-02 (scans 22, 24-27, 29, 31-33, 35-40; 15 pages; SA23-32)
- K161-3-03 (scans 41, 43-55; scan 42 blank; 15 pages; SA23-32)
- Hunches (with grounds)
- Dependencies (items used, with the page that shows them)
- Reused material
- Deliverable state

### Reading B_1_2_21 (`readings/B_1_2_21.md`)
- Cote 1, scans 3-36 (Pro MPL_1_002-050): rearrangements, Weyl functions, traces, the determinant Δ
- Cote 1, scans 38-50 (Pro MPL_1_002-050): singular numbers, Ky Fan, trace class, Hilbert tensor products
- Cote 1, scans 51-64 (Codex web K1-01): Hilbert-Schmidt and trace class, Hilbert exterior powers
- Cote 1, scans 65-78 (Codex web K1-02): exterior powers of operators, Weyl-Horn, determinants of sums
- Cote 1, scans 79-92 (Codex web K1-03): Weyl's lemma and the two convexity theorems
- Cote 1, scans 93-107 (Codex web K1-04): Schatten classes
- Cote 1, scans 108-121 (Codex web K1-05): genus and order; a proof of Lidskii's theorem
- Cote 1, scans 122-136 (Codex web K1-06): determinants of sums, Schatten classes for 0 < p
- Cote 1, scans 137-150 (Codex web K1-07): Hölder for all exponents, continuity
- Cote 2, scans 21-23 (Pro MPL_2): the Chern ring and the γ-filtration (F06)
- Not read in this run (budget)
- Hunches
- Dependencies (items of sweep2/SA23/OBJECTS.tsv)
- Deliverable state
- Second run (19 Nov, at the lead's request): the pages left over
- Cote 1, scans 140-145 and 149-150 (Codex web K1-07)
- Cote 2, scans 2-8 (Pro MPL_2): K of a curve and of a scheme of dimension ≤ 1
- Cote 2, scans 9-20 (Pro MPL_2): trivial Chern classes, equivariant modules
- Cote 2, scans 23-30 (Pro MPL_2): geometric elements, the universal Chern ring
- Cote 2, scans 32-39 (Pro MPL_2): K and Chow with supports, covariant Chern characters
- Cote 2, scans 40-45 (Pro MPL_2): Riemann-Roch for embeddings, fibrations, curves and surfaces
- Cote 21, scans 2-16 (Codex web K21-01): vanishing tests, Watts's theorem, I-torsion functors
- Cote 21, scans 17-29 (Codex web K21-02): P_1, P_2, P_3 for sheaves and fibred categories

### Reading C_22_23_26_161-5 (`readings/C_22_23_26_161-5.md`)
- Cote 22: "[EGA IV]. [Chapitre] 0 IV. Cohen, différentielles, algèbres formellement simples (Compléments)"
- 22/002-009: Jouanolou's printed note, with his pencil (SA23-15, H0D3)
- 22/002-009 in detail: his pencil on Jouanolou's note (SA23-15)
- 22/010-018: §4 of the EGA 0_IV draft for Dieudonné, "algèbres de Cohen" (SA23-17, H0D5)
- 22/019-021: "Questions ouvertes" (SA23-18, H0D6)
- 22/022-025: formal simplicity for the discrete topology (SA23-19, H0D7)
- 22/026: struck heading "Différentielles"; otherwise blank.
- 22/027 and 22/029: the Remarque and the counterexample (SA23-20, H0D9; flag F01)
- 22/028 and 22/030: reused typescript
- Cote 23: "EGA IV. Compléments". Scans 2-16 (Pro package MPL_22+23_002-016; Codex K23-06 is a second witness)
- 23/004-005: the canonical sheaf of a complete intersection in P(E) (SA23-21, H0DA)
- 23/006: the discriminant (SA23-21)
- 23/007: reused English typescript (SA23-12, H0D0)
- 23/008-016: "Exponentielle": nilpotent exponential, hyperalgebras, Cartier (SA23-22, H0DB)
- Cote 23, scans 17-50 (Codex web K23-01, K23-02; GPT-6.2 Astra Max)
- 23/017-032: bundles of germs, Weil restriction, infinitesimal transformations (SA23-23, H0DC)
- 23/034-037: "Exemples, Cas particuliers"; criteria (SA23-24, H0DD)
- 23/038: reused Bourbaki draft
- 23/039-041: "Foncteur différentiel d'ordre ≤ n" (SA23-23)
- 23/044-047: a letter of Lê Dũng Tráng (11 Jan 1968) with errata to EGA IV
- 23/049: "EGA IV 18" (SA23-25)
- 23/050: cover "Suites régulières / Th. II(?).2.9. de Raynaud".
- Cote 23, scans 51-65 (Codex web K23-03): regular immersions, and Deligne's letters of 1966 on EGA IV (SA23-25, H0DE)
- 23/051-052: two IHÉS sheets
- 23/053-054: his PS on regular immersions (for Dieudonné; date 1966-67, from the SGA 6 reference)
- 23/055-065: three letters of Pierre Deligne to Grothendieck, 1966 (correspondence; the margins are his)
- Cote 23, scans 66-82 (Codex web K23-04): "Divers" (SA23-26, H0DF; SA23-25)
- 23/067-068: "Structure Main Theorem", a plan of proofs (IHÉS sheet)
- 23/070-071: "Morphismes ess. de prés. finie", "Morphismes essentiellement affines"
- 23/073: schemes all of whose points are closed
- 23/074 and 23/079: reused typescript pages
- 23/075-078, 080: condition (h_0) on open-closed parts, and étale covers
- 23/081-082
- Cote 23, scans 83-99 (Codex web K23-05): dimension, (S_k), Cohen-Macaulay loci, graded flatness (SA23-27, H0DG)
- 23/083-084: Lemma 1, "Rappels sur la dimension"
- 23/085: "∂-Catégorie"
- 23/087: depth along a finite morphism
- 23/088-089: finiteness of the integral closure
- 23/090: margins on factoriality (partly in English)
- 23/091-094: "IV 12 Fibres des morphismes plats de présentation finie" and an example
- 23/096-099: graded flatness by Hilbert series
- Cote 26: "EGA VI. Plans, notations, problèmes ouverts" (Codex web H26-01, scans 2-11; SA23-28, H0DH)
- Cote 161-5: "Barsotti-Tate" (Pro package MPL_93_221-236+161-5; Codex K161-5-01/02 a second witness)
- 161-5/003-022: Serre's printed texts (reused material; SA23-34 H0DO, SA23-35 H0DP)
- 161-5/023-029: his notes, "a crystalline realisation for the Tannakian category generated by Barsotti-Tate groups" (SA23-36, H00D with SA04-15)
- Deliverable state of stretch C

