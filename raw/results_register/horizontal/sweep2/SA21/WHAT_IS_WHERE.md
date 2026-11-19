# SA21: Vers une géométrie des formes (cote 156): what is where

Claude Opus 5.5 at effort max, a6d42bf6fe2b0d8a8, horizontal sweep 2 part 2, 2026-11-18.

The topic is cote 156, in nine parts:
- **156-1 and 156-2 (Pro package MPL_156-1+156-2):** forms, one-dimensional models and their axioms F1-F6, networks, ficelles, cuttings, rives and mailles.
- **156-3 to 156-9:** the dated 1986 series marked GF (or CF) III to IX bis, from 8 June to 15 July 1986:
  - 156-3: networks via cuttings;
  - 156-4: "Analysis situs (première mouture)", with the contrées;
  - 156-5: "Sorite ensembliste";
  - 156-6: "Analysis situs (deuxième mouture)", with the ateliers;
  - 156-7: "Analysis Situs (troisième mouture)" (Chap VII);
  - 156-8: magasins and oriented multistrata;
  - 156-9: morphisms of ateliers.

The 1986 series is read so far only by the Codex notes on the sheets: the steps marked unverified, and the title sheets. Reused Récoltes et Semailles typescript leaves (1985 and May 1986) lie in 156-8 and 156-9.

How to read an entry:
- **Where:** cote and scans, the notes it is in (package or folder), and the notes files. Scans are the PDF pages of the cote in `grothendieck_archive_montpellier`.
- **Depends:** what the item uses and what uses it, with the basis: his page, our note, or a proof (ours).
- **Claims:** his claims on the item, linked to what proves, refutes or refines them (CLAIM_LINKS.tsv).
- **Units:** the companion units that discuss it (UNIT_LINKS.tsv).
- **Flags, corrections:** from FLAGS.tsv and CORRECTIONS.tsv.

## Forms and one-dimensional models (156-1)

### SA21-1: the notion of form ("forme"): a complete definition only in dimension zero (156-1, 156-2)

- **Status on his pages:** complete only in dimension zero (D01). **Kind:** definition.
- **Where:** cotes 156-1+156-2.
- **Notes (1 entry):** MPL_156-1+156-2 (1).
- **Notes files:** `inputs/SA21/pro/MPL_156-1+156-2_notes.md`.
- **Depends:** related: SA21-8 (our note); used by: SA21-2 (his page).
- **Other topics:** SA11-3, SA10-4 (tame topology, cotes 120-121).

### SA21-2: one-dimensional models: segments, endpoints and branches; the axioms F1-F5 and their revisions; restriction

- **Status on his pages:** revised on the pages; several claims withdrawn or unproved; the notes give a counterexample to arbitrary restriction (A12) and a repair (A13). **Kind:** axiomatics.
- **Where:** cotes 156-1+156-2, scans 4,7,9-10,24.
- **Notes (20 entries):** MPL_156-1+156-2 (20).
- **Notes files:** `inputs/SA21/pro/MPL_156-1+156-2_notes.md`.
- **Depends:** used by: SA21-3 (his page), SA21-4 (his page); uses: SA21-1 (his page).
- **Claims:**
  - SA21-C1 (156-1/010): "arbitrary restriction of a segment structure (asserted, not proved; his own warning on 008: "on n'affirme pas égalité!")". **refutes (the notes; not checked here); refines**: MPL_156-1+156-2#28 (A12): a counterexample of the notes; #29 (A13): a repair by closure under required gluings.

### SA21-3: filtering: the axiom F6 and its two formulations; local against global filtering; singular endpoints

- **Status on his pages:** the passage from local to global filtering is retracted on the page (A21); F6 has two formulations. **Kind:** axiomatics.
- **Where:** cotes 156-1+156-2, scans 13,19,21-22.
- **Notes (10 entries):** MPL_156-1+156-2 (10).
- **Notes files:** `inputs/SA21/pro/MPL_156-1+156-2_notes.md`.
- **Depends:** used by: SA21-4 (his page); uses: SA21-2 (his page).
- **Claims:**
  - SA21-C2 (156-1/021-022): "the passage from local to global filtering". **withdrawn (his); confirmed by the notes**: withdrawn by him; #38 (A22): a branching-order counterexample confirming the withdrawal.
  - SA21-C5 (156-1/019): "the local strict inequality on 019 ("si x <= y,z" ... "x < u < y,z")". **suspected misreading or his slip (open)**: none; inconsistent as written for x = y; the strict version at 013.
- **Corrections:** 156-1/019: si x <= y,z ... x < u < y,z -> the strict antecedent of 013.
- **Flags:** suspected misreading (1).

### SA21-4: networks (reseaux) and segment models: divisible and reduced cases; reconstruction of the order, the components and the orientation

- **Status on his pages:** order reconstruction conditional; the orientation theorem self-flagged as unverified; topology not reconstructed. **Kind:** construction.
- **Where:** cotes 156-1+156-2, scans 13,18.
- **Notes (8 entries):** MPL_156-1+156-2 (8).
- **Notes files:** `inputs/SA21/pro/MPL_156-1+156-2_notes.md`.
- **Depends:** related: SA03-13 (our note); used by: SA21-5 (his page); uses: SA21-2 (his page), SA21-3 (his page).
- **Claims:**
  - SA21-C3 (156-1/018): "the orientation theorem for networks". **open (his own flag)**: none: explicitly unverified by him.

## Ficelles, cuttings, rives and mailles (156-2)

### SA21-5: ficelles and regular immersions: contraction quotients, cone bases, sides, connectivity, existence and uniqueness, the interval classification

- **Status on his pages:** asserted separately; endpoint enlargement and universal equivalence withdrawn. **Kind:** construction.
- **Where:** cotes 156-1+156-2, scans 2-7,11.
- **Notes (22 entries):** MPL_156-1+156-2 (22).
- **Notes files:** `inputs/SA21/pro/MPL_156-1+156-2_notes.md`.
- **Depends:** related: SA10-7 (our note); used by: SA21-6 (his page); uses: SA21-4 (his page).
- **Claims:**
  - SA21-C4 (156-2/011): "endpoint enlargement of ficelles; the universal equivalence of oriented structures". **withdrawn (his)**: withdrawn by him; #72 (B27): a tripod explains the obstruction.
  - SA21-C6 (156-2/003): "W'_t = X - V_t, with V_t in X/A". **suspected misreading or his slip (open)**: none; W_t would be type-correct.
  - SA21-C7 (156-2/006): "the end of the proof of the first three ficelle conditions: "X - {c} ne serait pas connexe"". **suspected misreading or his slip (open)**: none; the target is X - {a}.
- **Corrections:** 156-2/003: W'_t = X - V_t -> W'_t = X - W_t; 156-2/006: X - {c} ne serait pas connexe -> X - {a}.
- **Flags:** suspected misreading (2); a link across folders (1).
- **Other topics:** SA10 (conical neighbourhoods and collars, MPL_150_001-043 Q1b); SA11-1 (tubulure).

### SA21-6: cuttings (decoupages): separating lieux, cone gluing, tubular boundaries, gluing homeomorphisms, the exchange lemma, ordered cuts and finite chains, partial cuts

- **Status on his pages:** lemmas stated; the cone-gluing lemma lacks a covering hypothesis; regular immersion of the cut boundary unproved. **Kind:** construction.
- **Where:** cotes 156-1+156-2, scans 3,7-14,17-19.
- **Notes (21 entries):** MPL_156-1+156-2 (21).
- **Notes files:** `inputs/SA21/pro/MPL_156-1+156-2_notes.md`.
- **Depends:** used by: SA21-12 (his page), SA21-15 (our note), SA21-7 (his page); uses: SA21-5 (his page).
- **Flags:** a link across folders (1).
- **Other topics:** SA10 (MPL_150_001-043 Q1b, 150/012-015, 022-023; 147/140-142).

### SA21-7: rives, birives and mailles: germs of clopen sets, the Boolean algebra Comp, the sheaf spectrum and Stone spaces, links

- **Status on his pages:** definitions; the link identification plausible, unproved. **Kind:** definition/proposition.
- **Where:** cotes 156-1+156-2, scans 2,15-18.
- **Notes (15 entries):** MPL_156-1+156-2 (15).
- **Notes files:** `inputs/SA21/pro/MPL_156-1+156-2_notes.md`.
- **Depends:** uses: SA21-6 (his page).
- **Other topics:** SA10 (pro-neighbourhoods of strata, MPL_150_044-084).

## The 1986 series: from networks to ateliers and magasins (156-3 to 156-9)

### SA21-12: 156-3, "Reseaux ... via decoupages" (8 June 1986, sheet III): troncons and sous-troncons, closed tame parts

- **Status on his pages:** read only by Codex stage-A notes: self-flagged steps and dates. **Kind:** construction.
- **Where:** cote 156-3, scans 2-41.
- **Notes (5 entries):** codex:J156-3-01 (1); codex:J156-3-02 (1); codex:J156-3-03 (1); codex:J156-3-04 (1); codex:J156-3-05 (1).
- **Notes files:** `codex_web_20261113/returns/J156-3-01/out/J156-3-01_notes.md`; `codex_web_20261113/returns/J156-3-02/out/J156-3-02_notes.md`; `codex_web_20261113/returns/J156-3-03/out/J156-3-03_notes.md`; `codex_web_20261113/returns/J156-3-04/out/J156-3-04_notes.md`; `codex_web_20261113/returns/J156-3-05/out/J156-3-05_notes.md`.
- **Depends:** related: SA11-3 (our note); used by: SA21-13 (our note); uses: SA21-6 (his page).
- **Other topics:** SA11-3 (tame axiomatics, cote 121); SA10-19 (cote 120).

### SA21-13: 156-4, "Analysis situs (premiere mouture)" (10-13 June 1986, sheet IV): contrees and their axioms Cont 1-5, figures, a presumed Boolean algebra

- **Status on his pages:** read only by Codex stage-A notes: self-flagged steps and dates. **Kind:** axiomatics.
- **Where:** cote 156-4, scans 2-4,10-89.
- **Notes (11 entries):** codex:J156-4-01 (1); codex:J156-4-02 (1); codex:J156-4-03 (1); codex:J156-4-04 (1); codex:J156-4-05 (1); codex:J156-4-06 (1); codex:J156-4-07 (1); codex:J156-4-08 (1) ....
- **Notes files:** `codex_web_20261113/returns/J156-4-01/out/J156-4-01_notes.md`; `codex_web_20261113/returns/J156-4-02/out/J156-4-02_notes.md`; `codex_web_20261113/returns/J156-4-03/out/J156-4-03_notes.md`; `codex_web_20261113/returns/J156-4-04/out/J156-4-04_notes.md`; `codex_web_20261113/returns/J156-4-05/out/J156-4-05_notes.md`; `codex_web_20261113/returns/J156-4-06/out/J156-4-06_notes.md` ....
- **Depends:** used by: SA21-10 (our note); uses: SA21-12 (our note).
- **Other topics:** SA11-3; SA10-19.

### SA21-14: 156-5, "Sorite ensembliste" (15-18 June 1986): set-theoretic sorites, the order relations and their comparison

- **Status on his pages:** read only by Codex stage-A notes: self-flagged steps and dates. **Kind:** proposition.
- **Where:** cote 156-5, scans 2-25,34-49.
- **Notes (6 entries):** codex:J156-5-01 (1); codex:J156-5-02 (1); codex:J156-5-03 (1); codex:J156-5-04 (1); codex:J156-5-05 (1); codex:J156-5-06 (1).
- **Notes files:** `codex_web_20261113/returns/J156-5-01/out/J156-5-01_notes.md`; `codex_web_20261113/returns/J156-5-02/out/J156-5-02_notes.md`; `codex_web_20261113/returns/J156-5-03/out/J156-5-03_notes.md`; `codex_web_20261113/returns/J156-5-04/out/J156-5-04_notes.md`; `codex_web_20261113/returns/J156-5-05/out/J156-5-05_notes.md`; `codex_web_20261113/returns/J156-5-06/out/J156-5-06_notes.md`.

### SA21-10: ateliers (workshops): not defined in 156-1, 156-2 (D16); defined and used in 156-6 ("Analysis situs (deuxième mouture)"), 156-7 ("Analysis Situs (troisième mouture)", Chap VII, 23 June 1986) and 156-9 (GF IX, 5-15 July 1986): sub-ateliers, the axioms At, saturation, spatial ateliers, multiombre and ombres, quasi-correspondences, disjunctors and "Spotos", magmas with strata, morphisms of ateliers (= H0K9)

- **Status on his pages:** read only by Codex stage-A notes: self-flagged steps and dates. **Kind:** definition/construction.
- **Where:** cotes 156-1+156-2; cote 156-6, scans 2-9,18-33,35,42-87; cote 156-7, scans 10-41,46,50-72,80-86,108,111; cote 156-9, scans 10,12,17,19,29,42-57,74-82,84,86,90-104,126-133.
- **Notes (46 entries):** MPL_156-1+156-2 (1); codex:J156-6-01 (1); codex:J156-6-02 (1); codex:J156-6-03 (1); codex:J156-6-04 (1); codex:J156-6-05 (1); codex:J156-6-06 (1); codex:J156-6-07 (1) ....
- **Notes files:** `codex_web_20261113/returns/H156-01/out/H156-01_notes.md`; `codex_web_20261113/returns/J156-6-01/out/J156-6-01_notes.md`; `codex_web_20261113/returns/J156-6-02/out/J156-6-02_notes.md`; `codex_web_20261113/returns/J156-6-03/out/J156-6-03_notes.md`; `codex_web_20261113/returns/J156-6-04/out/J156-6-04_notes.md`; `codex_web_20261113/returns/J156-6-05/out/J156-6-05_notes.md` ....
- **Depends:** related: SA10-2 (our note); used by: SA21-15 (our note); uses: SA21-13 (our note).
- **Corrections:** MPL_156-1+156-2 D16: no definition of an atelier on 156-1 and 156-2 -> ateliers are defined and used in 156-6, 156-7 and 156-9 (Codex notes).
- **Flags:** a link across folders (2); a link across folders.
- **Other topics:** SA10-2, SA11-1 (ombre: multiombre in 156-6, ombres in 156-7); = H0K9.

### SA21-15: 156-8 (CF VIII, 27 June - 4 July 1986): magasins généraux and oriented multistrata ("magasins orienteurs"), polyhedral ateliers, homomorphisms of magasins and ateliers, axioms for lieux and the gluing of refinements, supports and constructible supports, the magma associated with an ordered set; elementary figures (= H0KJ)

- **Status on his pages:** read only by Codex stage-A notes: self-flagged steps and dates. **Kind:** construction.
- **Where:** cote 156-8, scans 10,14,16,18-25,27-28,30,34-41,53-54,56,58-73,77-78,90-105,110,118,121,126-127.
- **Notes (16 entries):** codex:J156-8-03 (1); codex:J156-8-05 (1); codex:J156-8-08 (1); codex:J156-8-09 (1); codex:J156-8-12 (1); codex:J156-8-13 (1); codex:J156-8-01 (1); codex:J156-8-02 (1) ....
- **Notes files:** `codex_web_20261113/returns/J156-8-01/out/J156-8-01_notes.md`; `codex_web_20261113/returns/J156-8-02/out/J156-8-02_notes.md`; `codex_web_20261113/returns/J156-8-03/out/J156-8-03_notes.md`; `codex_web_20261113/returns/J156-8-04/out/J156-8-04_notes.md`; `codex_web_20261113/returns/J156-8-05/out/J156-8-05_notes.md`; `codex_web_20261113/returns/J156-8-06/out/J156-8-06_notes.md` ....
- **Depends:** uses: SA21-10 (our note), SA21-6 (our note).
- **Flags:** a link across folders (1).
- **Other topics:** SA21-6 (= H0KJ; lieux and cuttings, 156-1/2).

## The programme questions put to the pages (the notes')

### SA21-8: the requested programme questions P01-P16: pro-objects of finite posets or categories, finite T0 spaces, simple homotopy, exit paths, the Esquisse comparison

- **Status on his pages:** P01: the README conjecture (a form as a tame space recovered from a pro-object of finite posets or categories) is not confirmed on these pages. **Kind:** comparison (requested).
- **Where:** cotes 156-1+156-2.
- **Notes (16 entries):** MPL_156-1+156-2 (16).
- **Notes files:** `inputs/SA21/pro/MPL_156-1+156-2_notes.md`.
- **Depends:** related: SA21-1 (our note).
- **Corrections:** MPL_156-1+156-2 P01: the README reads a form as a tame space recovered from a pro-object of finite po -> not on these pages (our framing): finite chains of cuts, no category of refineme.
- **Flags:** requested questions; the notes' work.
- **Other topics:** SA10-8 (exit paths, stratified homotopy); SA11-4; the homotopy line (finite posets as models).

## Documentary and apparatus

### SA21-11: documentary: covers, title sheets, dates and pagination of cote 156; the 1986 series marked GF (or CF) III to IX bis, 8 June to 15 July 1986; reused Récoltes et Semailles typescript leaves (typed p. 936 with note 171(i), 1985; typed pp. 951-953 and 1074-1088, 6 and 8 May 1986) (= H01T)

- **Status on his pages:** documentary. **Kind:** documentary.
- **Where:** cotes 156-1+156-2, scans 1,3,6-7,9,13,27,148; cote 156-3, scans 2-41; cote 156-4, scans 2-4,10-89; cote 156-5, scans 2-25,34-49; cote 156-6, scans 2-9,18-33,35,42-87; cote 156-7, scans 10-41,46,50-72,80-86,100; cote 156-8, scans 10,18-25,27,34-41,55,58-73,79,90-105,116-119; cote 156-9, scans 7,23,25,34,38,42-57,59-61,70-71,74-81,90-104,119,126-133,500,600.
- **Notes (84 entries):** MPL_156-1+156-2 (1); codex:J156-3-01 (1); codex:J156-3-02 (1); codex:J156-3-03 (1); codex:J156-3-04 (1); codex:J156-3-05 (1); codex:J156-4-01 (1); codex:J156-4-02 (1) ....
- **Notes files:** `codex_web_20261113/returns/H156-01/out/H156-01_notes.md`; `codex_web_20261113/returns/J156-3-01/out/J156-3-01_notes.md`; `codex_web_20261113/returns/J156-3-02/out/J156-3-02_notes.md`; `codex_web_20261113/returns/J156-3-03/out/J156-3-03_notes.md`; `codex_web_20261113/returns/J156-3-04/out/J156-3-04_notes.md`; `codex_web_20261113/returns/J156-3-05/out/J156-3-05_notes.md` ....
- **Depends:** related: SA02-6 (our note).
- **Corrections:** cote 156 series: the GF series dated 8 June to 12 July 1986 (sweep 1) -> to 15 July 1986 (GF IX, J156-9-01); third mouture 23 June (H156-01).
- **Flags:** a link across folders (3); a link across folders (Récoltes et Semailles typescript in cotes 84 and 156).
- **Other topics:** MPL_148_029-072 T01 (covers); the Récoltes et Semailles typescript also in cote 84 (= H01T; SA02-6, SA01-37).

### SA21-9: the notes' apparatus for SA21 (scope, standing questions, register relations, sources, limits)

- **Status on his pages:** apparatus. **Kind:** apparatus.
- **Where:** cotes 156-1+156-2, scans 279.
- **Notes (7 entries):** MPL_156-1+156-2 (7).
- **Notes files:** `inputs/SA21/pro/MPL_156-1+156-2_notes.md`.

## Counts

- Items: 15; placed entries: 288.
- DEPENDS rows: 36; CLAIM_LINKS: 7; UNIT_LINKS: 0; CORRECTIONS: 6; part-2 check events: 0.
