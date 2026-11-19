# SA04: crystals and the cote 93 strands; combinatorial geometry of cotes 69-89; descent and local cohomology of cotes 94-102: what is where

Claude Opus 5.5 at effort max, a6d42bf6fe2b0d8a8, horizontal sweep 2 part 2, 2026-11-18.

The topic is "Géométrie et topologie combinatoire", part 2. It has three layers:
- **Cote 93, scans 47-91 and 219-236, with cote 161:** Barsotti-Tate crystals and p-adic representations, the Schwarzian and projective connections, periods, the Euler characteristic axioms and typed analysis exercises.
- **Cotes 69-89 (Work and Codex notes only):** graphs, polygons and polyhedra over rings, quadratic forms and orthogonal groups, triangle groups.
- **Cotes 94-102:** descent, including the draft "Pour EGA VI" of cote 102; local cohomology (dated 1958); Hilbert schemes; Chern classes.

Heavy notes: the Pro packages MPL_93_047-091, MPL_93_221-236+161-5, MPL_98 (GPT-6 Astra, ChatGPT Pro mode). Light notes: 102 Work folders and 98 Codex folders on cotes 69-102.

Pieces of sweep 2 part 2: `sweep2/REPORTS/cote93_scan052_exercise_22a.md` and `sweep2/REPORTS/cote102_pour_EGA_VI.md`.

How to read an entry:
- **Where:** cote and scans, the notes it is in (package or folder), and the notes files. Scans are the PDF pages of the cote in `grothendieck_archive_montpellier`.
- **Depends:** what the item uses and what uses it, with the basis: his page, our note, or a proof (ours).
- **Claims:** his claims on the item, linked to what proves, refutes or refines them (CLAIM_LINKS.tsv).
- **Units:** the companion units that discuss it (UNIT_LINKS.tsv).
- **Flags, corrections:** from FLAGS.tsv and CORRECTIONS.tsv.

## Crystals, p-adic representations and good reduction (cotes 93, 100, 161)

### SA04-1: Barsotti-Tate groups and their crystals: the crystalline comparison for abelian schemes, deformations (Serre-Tate, Messing), canonical filtration, the isogeny category

- **Status on his pages:** stated; several steps deferred or self-flagged. **Kind:** programme/theorem (stated).
- **Where:** cote 93.
- **Notes (35 entries):** MPL_93_047-091 (35).
- **Notes files:** `inputs/SA04/pro/MPL_93_047-091_notes.md`.
- **Depends:** related: SA03-16 (our note); used by: SA04-13 (his page), SA04-15 (his page), SA04-3 (our note), SA04-38 (his page).
- **Corrections:** K93-07 (SA03), K93-13 and MPL_93_092-134 (SA01): filed under SA03 and SA01 -> cote 93 strands of SA04 (H02H, H00B, H00C, H03D, H03E, H03F, H0JE, H02J).
- **Flags:** a link across folders (2).
- **Other topics:** SA03-16 (the crystal programme, cote 93 scans 37-46); SA04-38 (cote 100).

### SA04-3: p-adic representations and crystals: Tate's theorem, Hodge-Tate condition, full faithfulness on an admissible category, a quasi-inverse, F-crystals

- **Status on his pages:** programme; later proved results cited by the notes. **Kind:** programme/conjecture.
- **Where:** cote 93, scans 55,83.
- **Notes (15 entries):** MPL_93_047-091 (15).
- **Notes files:** `inputs/SA04/pro/MPL_93_047-091_notes.md`.
- **Depends:** used by: SA04-14 (our note); uses: SA04-1 (our note).
- **Flags:** a link across folders (1).
- **Other topics:** SA03-16; p-adic Hodge theory (literature).

### SA04-14: p-adic Galois representations: Hodge-Tate grading, the algebraic envelope, openness of inertia, Sen's theorem (cote 161 offprints and notes)

- **Status on his pages:** printed results and notes. **Kind:** theorem (stated)/comparison.
- **Where:** cote 93, scans 4-5,7-10,13,15-17,19-21,23,41,44,61,168.
- **Notes (23 entries):** MPL_93_221-236+161-5 (23).
- **Notes files:** `inputs/SA04/pro/MPL_93_221-236+161-5_notes.md`.
- **Depends:** uses: SA04-3 (our note).
- **Other topics:** related: SA23-34 (H0DO, Serre 1967, cote 161-5).

### SA04-15: filtered modules for Barsotti-Tate groups: fibre functors, Tate twists, descent with Frobenius (cote 161 sheets) (= H00D)

- **Status on his pages:** worked; reading questions. **Kind:** construction.
- **Where:** cote 93, scans 23-27,38-39,41,43,234.
- **Notes (22 entries):** MPL_93_221-236+161-5 (22).
- **Notes files:** `inputs/SA04/pro/MPL_93_221-236+161-5_notes.md`.
- **Depends:** uses: SA04-1 (his page).
- **Other topics:** = H00D (SA23-36).

### SA04-13: formal de Rham data and derived Hom toward the crystal construction (formally exact, formal Poincaré, torsor extension) (= H00C)

- **Status on his pages:** stated; the notes supply a roof proof (own idea). **Kind:** construction.
- **Where:** cote 93, scans 46,154,160,168,231-236.
- **Notes (16 entries):** MPL_93_221-236+161-5 (16).
- **Notes files:** `inputs/SA04/pro/MPL_93_221-236+161-5_notes.md`.
- **Depends:** uses: SA04-1 (his page).
- **Units (3):** K93-02.u05, K93-02.u06, K93-03.u04.
- **Other topics:** = H00C (SA23-44); related: SA23-38 (H0DR, Quillen tapis, cote 162-5).

### SA04-16: cocycle parametrization of extensions and the cohomology of Gamma and pi (Hua's rank-one counterexample)

- **Status on his pages:** stated; notes verify Hua's example. **Kind:** proposition.
- **Where:** cote 93, scans 25,27-29.
- **Notes (12 entries):** MPL_93_221-236+161-5 (12).
- **Notes files:** `inputs/SA04/pro/MPL_93_221-236+161-5_notes.md`.
- **Claims:**
  - SA04-C4 (93 (cote 161 sheets)): "his cocycle parametrization of extensions, with the cohomology of Gamma and pi, as stated". **refutes as stated (Hua credited)**: Hua's rank-one counterexample, verified by the Pro notes.

### SA04-38: good reduction of abelian varieties via Barsotti-Tate groups over any base (cote 100)

- **Status on his pages:** Work notes only. **Kind:** theorem (stated).
- **Where:** cote 100.
- **Notes (32 entries):** work:K100-01 (6); work:K100-02 (6); work:K100-03 (6); work:K100-04 (6); codex:K100-01 (2); codex:K100-02 (2); codex:K100-03 (2); codex:K100-04 (2).
- **Notes files:** `codex_web_20261113/returns/K100-01/out/K100-01_mathnotes.md`; `codex_web_20261113/returns/K100-01/out/K100-01_notes.md`; `codex_web_20261113/returns/K100-02/out/K100-02_mathnotes.md`; `codex_web_20261113/returns/K100-02/out/K100-02_notes.md`; `codex_web_20261113/returns/K100-03/out/K100-03_mathnotes.md`; `codex_web_20261113/returns/K100-03/out/K100-03_notes.md` ....
- **Depends:** uses: SA04-1 (his page).
- **Other topics:** SA04-1; SA03-16.

## Projective connections, the Schwarzian, uniformization and periods (cote 93)

### SA04-7: the Schwarzian derivative as a projective invariant over any base: cocycle, invariance, rigidity, normalization G = 12G_0, characteristics 2 and 3

- **Status on his pages:** stated; a test value on 73 wrong as printed (Hua VI). **Kind:** theorem (stated)/calculation.
- **Where:** cote 93, scans 23,36,72-75,82,84,86,121.
- **Notes (59 entries):** MPL_93_047-091 (59).
- **Notes files:** `inputs/SA04/pro/MPL_93_047-091_notes.md`.
- **Depends:** related: SA01-32 (our note); used by: SA04-8 (his page), SA04-9 (his page).
- **Claims:**
  - SA04-C1 (93/073): "the test value G_0(t, t^2) = dt^2/(2t)". **refutes his value**: Hasse derivatives give dt^2/(4t^2) (sweep 1; Hua VI).
- **Corrections:** 93/073: G_0(t, t^2) = dt^2/(2t) -> dt^2/(4t^2), up to sign.
- **Flags:** suspected misreading (1); a link across folders (1); suspected misreading (test value on 73).
- **Other topics:** SA03-14 (the Schwarzian on cote 93 scans 2-46).

### SA04-8: logarithmic and n-differentials, frames of line bundles, uniformization diagrams and rank-two splittings

- **Status on his pages:** worked; several questioned maps. **Kind:** construction.
- **Where:** cote 93, scans 36,75-78,80-82,121,126.
- **Notes (59 entries):** MPL_93_047-091 (59).
- **Notes files:** `inputs/SA04/pro/MPL_93_047-091_notes.md`.
- **Depends:** uses: SA04-7 (his page).
- **Other topics:** related: SA32-2 (H0JE, uniformization by projective connections).

### SA04-9: projective connections and opers: rank-two bundles, PGL_2 and Borel reductions, Killing forms, the bad characteristic two

- **Status on his pages:** worked; some boxed factors checked by the notes. **Kind:** construction.
- **Where:** cote 93, scans 36,43,86-91.
- **Notes (49 entries):** MPL_93_047-091 (49).
- **Notes files:** `inputs/SA04/pro/MPL_93_047-091_notes.md`.
- **Depends:** related: SA01-31 (our note); used by: SA04-11 (our note); uses: SA04-7 (his page).
- **Other topics:** SA04-30 (SO(3) = GP(1), cote 82); related: SA32-2 (H0JE).

### SA04-11: Gauss-Manin, Picard-Fuchs, the Cartier operation and p-curvature: the notes' comparisons across the cote

- **Status on his pages:** not on these pages as a proof. **Kind:** comparison.
- **Where:** cote 93, scans 47,72,80,86,90-91.
- **Notes (36 entries):** MPL_93_047-091 (14); codex:K93-01 (2); codex:K93-02 (2); codex:K93-03 (2); codex:K93-04 (2); codex:K93-05 (2); codex:K93-06 (2); codex:K93-08 (2) ....
- **Notes files:** `codex_web_20261113/returns/K93-01/out/K93-01_notes.md`; `codex_web_20261113/returns/K93-02/out/K93-02_notes.md`; `codex_web_20261113/returns/K93-03/out/K93-03_notes.md`; `codex_web_20261113/returns/K93-04/out/K93-04_notes.md`; `codex_web_20261113/returns/K93-05/out/K93-05_notes.md`; `codex_web_20261113/returns/K93-06/out/K93-06_notes.md` ....
- **Depends:** used by: SA04-12 (our note); uses: SA04-9 (our note).
- **Flags:** a link across folders (1).
- **Other topics:** SA03-12, SA03-18 (Cartier, Gauss-Manin); related: SA23-24 (H0DD, connections, cote 23).

### SA04-12: periods and the Picard-Fuchs construction from logarithmic differentials (cote 93, scans 221-236) (= H00B)

- **Status on his pages:** constructed; identification open. **Kind:** construction.
- **Where:** cote 93, scans 23,36,142,154,162,219,222-224,227-230.
- **Notes (14 entries):** MPL_93_221-236+161-5 (14).
- **Notes files:** `inputs/SA04/pro/MPL_93_221-236+161-5_notes.md`.
- **Depends:** uses: SA04-11 (our note).
- **Units (5):** K93-01.u04, K93-02.u02, K93-02.u03, K93-02.u07, K93-06.u11.
- **Other topics:** = H00B (SA23-43).

## Topology and analysis on cote 93

### SA04-4: axioms for the Euler characteristic of locally compact spaces (ordinary and compact support): additivity, Mayer-Vietoris, conical class, end-link defect, triangulability in low dimensions

- **Status on his pages:** stated; uniqueness left open by him. **Kind:** axiomatics.
- **Where:** cote 93, scans 27-28,55-56,58,60,62,64,66,68,72-73,79.
- **Notes (48 entries):** MPL_93_047-091 (48).
- **Notes files:** `inputs/SA04/pro/MPL_93_047-091_notes.md`.
- **Claims:**
  - SA04-C5 (93/27-68): "uniqueness of the Euler characteristic under his axioms". **open (left open by him)**: none.
- **Other topics:** SA21 (Vers une geometrie des formes; tame topology).

### SA04-6: loop spaces and deloopings: when the first class vanishes

- **Status on his pages:** question; the notes give a model with a nonzero class after one delooping. **Kind:** question.
- **Where:** cote 93, scans 83.
- **Notes (8 entries):** MPL_93_047-091 (8).
- **Notes files:** `inputs/SA04/pro/MPL_93_047-091_notes.md`.
- **Claims:**
  - SA04-C7 (93/83): "the loop-space question: when the first class vanishes". **answers (the notes; not checked here)**: the notes give a model with a nonzero class.

### SA04-2: pseudo-resolvents and resolvent estimates (typed analysis exercises: Liouville, little-o growth, perturbation)

- **Status on his pages:** stated with literal errors (notes). **Kind:** exercise/proposition (others' text?).
- **Where:** cote 93.
- **Notes (19 entries):** MPL_93_047-091 (19).
- **Notes files:** `inputs/SA04/pro/MPL_93_047-091_notes.md`.
- **Depends:** uses: Cohen's factorization theorem (1959) (a proof (ours)).
- **Claims:**
  - SA04-C3 (93/052): "exercise 22 a) as typed (the lemma of Cohen's factorization theorem)". **proves (as typed)**: my proof; both transcriptions misread ||yw - w|| as ||yw - u||.
- **Corrections:** 93/052: ||yw - u|| < epsilon -> ||yw - w|| < epsilon; MPL_93_047-091 BT29-BT54: filed as Barsotti-Tate -> typed exercises on pseudo-resolvents and Banach algebras (22 b) is Cohen's facto.
- **Flags:** note overstates or misreads the page (1); note overstates or misreads the page? (typed exercise source unidentified).

## Combinatorial geometry: graphs, polygons and polyhedra (cotes 69-89)

### SA04-20: cubic graphs: the 27-vertex criterion, roots from pairs of vertices, configurations and stabilizers (cote 69) (= H02O)

- **Status on his pages:** Work notes only. **Kind:** combinatorics.
- **Where:** cote 69.
- **Notes (49 entries):** work:K69-01 (6); work:K69-02 (6); work:K69-03 (6); work:K69-04 (6); work:K69-05 (6); work:K69-06 (6); work:K69-07 (6); codex:K69-01 (1) ....
- **Notes files:** `codex_web_20261113/returns/K69-01/out/K69-01_mathnotes.md`; `codex_web_20261113/returns/K69-01/out/K69-01_notes.md`; `codex_web_20261113/returns/K69-02/out/K69-02_mathnotes.md`; `codex_web_20261113/returns/K69-02/out/K69-02_notes.md`; `codex_web_20261113/returns/K69-03/out/K69-03_mathnotes.md`; `codex_web_20261113/returns/K69-03/out/K69-03_notes.md` ....
- **Depends:** related: SA04-34 (my inference).
- **Units (79):** K69-01.u01, K69-01.u02, K69-01.u03, K69-01.u04, K69-01.u05, K69-01.u06, K69-01.u07, K69-01.u08 ....
- **Other topics:** = H02O.

### SA04-21: geometric realizations of regular polyhedra: the group G_n generated by involutions, affine realizations of the pinned icosahedron (cote 70) (= H02P)

- **Status on his pages:** Work notes only. **Kind:** construction.
- **Where:** cote 70, scans 17,19,21-22,30,35-37,70,75,81,112,116,118.
- **Notes (56 entries):** work:K70-01 (6); work:K70-03 (6); work:K70-05 (6); work:K70-07 (6); work:K70-08 (6); work:K70-02 (6); work:K70-04 (6); work:K70-06 (6) ....
- **Notes files:** `codex_web_20261113/returns/K70-01/out/K70-01_mathnotes.md`; `codex_web_20261113/returns/K70-01/out/K70-01_notes.md`; `codex_web_20261113/returns/K70-02/out/K70-02_mathnotes.md`; `codex_web_20261113/returns/K70-02/out/K70-02_notes.md`; `codex_web_20261113/returns/K70-03/out/K70-03_mathnotes.md`; `codex_web_20261113/returns/K70-03/out/K70-03_notes.md` ....
- **Depends:** related: SA01-1 (our note), SA04-24 (my inference), SA04-26 (my inference), SA04-32 (my inference).
- **Units (72):** K70-01.u01, K70-01.u02, K70-01.u03, K70-01.u04, K70-01.u05, K70-01.u06, K70-02.u01, K70-02.u02 ....
- **Other topics:** SA01-1 (pinned realizations, cote 72); = H02P.

### SA04-22: polygons in an affine plane over a base (cote 73) (= H02Q)

- **Status on his pages:** Work notes only. **Kind:** construction.
- **Where:** cote 73, scans 4,6,9.
- **Notes (14 entries):** work:K73-01 (6); work:K73-02 (6); codex:K73-01 (1); codex:K73-02 (1).
- **Notes files:** `codex_web_20261113/returns/K73-01/out/K73-01_mathnotes.md`; `codex_web_20261113/returns/K73-01/out/K73-01_notes.md`; `codex_web_20261113/returns/K73-02/out/K73-02_mathnotes.md`; `codex_web_20261113/returns/K73-02/out/K73-02_notes.md`.
- **Units (16):** K73-01.u01, K73-01.u02, K73-01.u03, K73-01.u04, K73-01.u05, K73-01.u06, K73-01.u07, K73-01.u08 ....
- **Other topics:** = H02Q.

### SA04-23: cubic complexes: graphs from group data, triads, hexagons and their coverings (cote 74) (= H02R)

- **Status on his pages:** Work notes only. **Kind:** combinatorics.
- **Where:** cote 74, scans 45,53,55,63-64,74-75,78-79,93,99,132.
- **Notes (56 entries):** work:K74-01 (6); work:K74-02 (6); work:K74-03 (6); work:K74-04 (6); work:K74-05 (6); work:K74-06 (6); work:K74-07 (6); work:K74-08 (6) ....
- **Notes files:** `codex_web_20261113/returns/K74-01/out/K74-01_mathnotes.md`; `codex_web_20261113/returns/K74-01/out/K74-01_notes.md`; `codex_web_20261113/returns/K74-02/out/K74-02_mathnotes.md`; `codex_web_20261113/returns/K74-02/out/K74-02_notes.md`; `codex_web_20261113/returns/K74-03/out/K74-03_mathnotes.md`; `codex_web_20261113/returns/K74-03/out/K74-03_notes.md` ....
- **Units (87):** K74-01.u01, K74-01.u02, K74-01.u03, K74-01.u04, K74-01.u05, K74-01.u06, K74-01.u07, K74-01.u08 ....
- **Other topics:** = H02R.

### SA04-24: n-cellular maps: faces, incidence, flags, quasi-simplicial sets, cube symmetries (cote 76) (= H02S)

- **Status on his pages:** Work notes only. **Kind:** combinatorics.
- **Where:** cote 76.
- **Notes (28 entries):** work:K76-01 (6); work:K76-02 (6); work:K76-03 (6); work:K76-04 (6); codex:K76-01 (1); codex:K76-02 (1); codex:K76-03 (1); codex:K76-04 (1).
- **Notes files:** `codex_web_20261113/returns/K76-01/out/K76-01_mathnotes.md`; `codex_web_20261113/returns/K76-01/out/K76-01_notes.md`; `codex_web_20261113/returns/K76-02/out/K76-02_mathnotes.md`; `codex_web_20261113/returns/K76-02/out/K76-02_notes.md`; `codex_web_20261113/returns/K76-03/out/K76-03_mathnotes.md`; `codex_web_20261113/returns/K76-03/out/K76-03_notes.md` ....
- **Depends:** related: SA04-21 (my inference).
- **Units (44):** K76-01.u01, K76-01.u02, K76-01.u03, K76-01.u04, K76-01.u05, K76-01.u06, K76-01.u07, K76-01.u08 ....
- **Other topics:** = H02S.

### SA04-26: regular polygons and cyclotomic polynomials: pinned regular n-gons over rings, unimodularity, orientations (cote 78) (= H02U)

- **Status on his pages:** Work notes only. **Kind:** construction.
- **Where:** cote 78, scans 82-83,86,98,102.
- **Notes (63 entries):** work:K78-01 (6); work:K78-02 (6); work:K78-03 (6); work:K78-04 (6); work:K78-05 (6); work:K78-06 (6); work:K78-07 (6); work:K78-08 (6) ....
- **Notes files:** `codex_web_20261113/returns/K78-01/out/K78-01_mathnotes.md`; `codex_web_20261113/returns/K78-01/out/K78-01_notes.md`; `codex_web_20261113/returns/K78-02/out/K78-02_mathnotes.md`; `codex_web_20261113/returns/K78-02/out/K78-02_notes.md`; `codex_web_20261113/returns/K78-03/out/K78-03_mathnotes.md`; `codex_web_20261113/returns/K78-03/out/K78-03_notes.md` ....
- **Depends:** related: SA04-21 (my inference).
- **Units (88):** K78-01.u01, K78-01.u02, K78-01.u03, K78-01.u04, K78-01.u05, K78-01.u06, K78-01.u07, K78-01.u08 ....
- **Other topics:** SA01-1; = H02U.

### SA04-27: regular triangulated 2-polyhedra from free rank-two modules over Z/nZ and Z: repères, edge types, automorphisms, torsors (cote 79) (= H02V)

- **Status on his pages:** Work notes only. **Kind:** construction.
- **Where:** cote 79, scans 68,151,222,229,266,268.
- **Notes (133 entries):** work:K79-01 (6); work:K79-02 (6); work:K79-03 (6); work:K79-04 (6); work:K79-05 (6); work:K79-06 (6); work:K79-07 (6); work:K79-08 (6) ....
- **Notes files:** `codex_web_20261113/returns/K79-01/out/K79-01_mathnotes.md`; `codex_web_20261113/returns/K79-01/out/K79-01_notes.md`; `codex_web_20261113/returns/K79-02/out/K79-02_mathnotes.md`; `codex_web_20261113/returns/K79-02/out/K79-02_notes.md`; `codex_web_20261113/returns/K79-03/out/K79-03_mathnotes.md`; `codex_web_20261113/returns/K79-03/out/K79-03_notes.md` ....
- **Claims:**
  - SA04-C6 (79/115-116): ""J'ignore s'il existe une structure de 2-polyèdre régulier ..."". **open (his question)**: none.
- **Units (192):** K79-01.u01, K79-01.u02, K79-01.u03, K79-01.u04, K79-01.u05, K79-01.u06, K79-01.u07, K79-01.u08 ....
- **Other topics:** SA01-2 (level-n regular maps); SA01-1; = H02V.

### SA04-28: pseudoline systems: configurations, a distinguished line, orientation and the canonical functor (cote 80) (= H02W)

- **Status on his pages:** Work notes only. **Kind:** combinatorics.
- **Where:** cote 80, scans 22,26-27.
- **Notes (22 entries):** work:K80-01 (6); work:K80-03 (6); work:K80-04 (6); codex:K80-01 (1); codex:K80-02 (1); codex:K80-03 (1); codex:K80-04 (1).
- **Notes files:** `codex_web_20261113/returns/K80-01/out/K80-01_mathnotes.md`; `codex_web_20261113/returns/K80-01/out/K80-01_notes.md`; `codex_web_20261113/returns/K80-02/out/K80-02_notes.md`; `codex_web_20261113/returns/K80-03/out/K80-03_mathnotes.md`; `codex_web_20261113/returns/K80-03/out/K80-03_notes.md`; `codex_web_20261113/returns/K80-04/out/K80-04_mathnotes.md` ....
- **Depends:** related: SA11-8 (our note).
- **Units (29):** K80-01.u01, K80-01.u02, K80-01.u03, K80-01.u04, K80-01.u05, K80-01.u06, K80-01.u07, K80-01.u08 ....
- **Other topics:** SA01-9 and SA11 (cote 154 pseudolines); = H02W.

### SA04-31: 2-polyhedra and 1-polygons: dihedral and triangle-group representations, traces and orders (cote 85) (= H030)

- **Status on his pages:** Work notes only. **Kind:** group theory.
- **Where:** cote 85, scans 44-45,48,73-74.
- **Notes (49 entries):** work:K85-01 (6); work:K85-02 (6); work:K85-03 (6); work:K85-04 (6); work:K85-05 (6); work:K85-06 (6); work:K85-07 (6); codex:K85-01 (1) ....
- **Notes files:** `codex_web_20261113/returns/K85-01/out/K85-01_mathnotes.md`; `codex_web_20261113/returns/K85-01/out/K85-01_notes.md`; `codex_web_20261113/returns/K85-02/out/K85-02_mathnotes.md`; `codex_web_20261113/returns/K85-02/out/K85-02_notes.md`; `codex_web_20261113/returns/K85-03/out/K85-03_mathnotes.md`; `codex_web_20261113/returns/K85-03/out/K85-03_notes.md` ....
- **Depends:** uses: SA04-30 (his page).
- **Units (58):** K85-01.u01, K85-01.u02, K85-01.u03, K85-01.u04, K85-01.u05, K85-01.u06, K85-01.u07, K85-01.u08 ....
- **Other topics:** SA01-27 (icosahedral matrices); SA01-2; = H030.

### SA04-32: regular polyhedra: incidence data, antipodism, the fifteen directions and trihedra (cote 86) (= H031)

- **Status on his pages:** Work notes only. **Kind:** combinatorics.
- **Where:** cote 86, scans 16-17.
- **Notes (14 entries):** work:K86-01 (6); work:K86-02 (6); codex:K86-01 (1); codex:K86-02 (1).
- **Notes files:** `codex_web_20261113/returns/K86-01/out/K86-01_mathnotes.md`; `codex_web_20261113/returns/K86-01/out/K86-01_notes.md`; `codex_web_20261113/returns/K86-02/out/K86-02_mathnotes.md`; `codex_web_20261113/returns/K86-02/out/K86-02_notes.md`.
- **Depends:** related: SA04-21 (my inference).
- **Units (27):** K86-01.u01, K86-01.u02, K86-01.u03, K86-01.u04, K86-01.u05, K86-01.u06, K86-01.u07, K86-01.u08 ....
- **Other topics:** = H031.

### SA04-33: convex polyhedra: convex hulls, faces and relative interiors (cote 87) (= H032)

- **Status on his pages:** Work notes only. **Kind:** geometry.
- **Where:** cote 87, scans 3,5,8.
- **Notes (21 entries):** work:K87-01 (6); work:K87-02 (6); work:K87-03 (6); codex:K87-01 (1); codex:K87-02 (1); codex:K87-03 (1).
- **Notes files:** `codex_web_20261113/returns/K87-01/out/K87-01_mathnotes.md`; `codex_web_20261113/returns/K87-01/out/K87-01_notes.md`; `codex_web_20261113/returns/K87-02/out/K87-02_mathnotes.md`; `codex_web_20261113/returns/K87-02/out/K87-02_notes.md`; `codex_web_20261113/returns/K87-03/out/K87-03_mathnotes.md`; `codex_web_20261113/returns/K87-03/out/K87-03_notes.md`.
- **Units (39):** K87-01.u01, K87-01.u02, K87-01.u03, K87-01.u04, K87-01.u05, K87-01.u06, K87-01.u07, K87-01.u08 ....
- **Other topics:** = H032.

### SA04-34: the root-system functor (cote 88, "Cartes standards") (= H033)

- **Status on his pages:** Work notes only. **Kind:** algebra.
- **Where:** cote 88, scans 4-5.
- **Notes (7 entries):** work:K88-01 (6); codex:K88-01 (1).
- **Notes files:** `codex_web_20261113/returns/K88-01/out/K88-01_mathnotes.md`; `codex_web_20261113/returns/K88-01/out/K88-01_notes.md`.
- **Depends:** related: SA04-20 (my inference).
- **Units (8):** K88-01.u01, K88-01.u02, K88-01.u03, K88-01.u04, K88-01.u05, K88-01.u06, K88-01.u07, K88-01.u08.
- **Other topics:** = H033.

### SA04-35: the combinatorial hexagon and 3-3 sets: orientations, torsors and partitions (cote 89) (= H034)

- **Status on his pages:** Work notes only. **Kind:** combinatorics.
- **Where:** cote 89, scans 6-7,17-19.
- **Notes (14 entries):** work:K89-01 (6); work:K89-02 (6); codex:K89-01 (1); codex:K89-02 (1).
- **Notes files:** `codex_web_20261113/returns/K89-01/out/K89-01_mathnotes.md`; `codex_web_20261113/returns/K89-01/out/K89-01_notes.md`; `codex_web_20261113/returns/K89-02/out/K89-02_mathnotes.md`; `codex_web_20261113/returns/K89-02/out/K89-02_notes.md`.
- **Units (15):** K89-01.u01, K89-01.u02, K89-01.u03, K89-01.u04, K89-01.u05, K89-01.u06, K89-01.u07, K89-02.u01 ....
- **Other topics:** = H034.

## Quadratic forms and orthogonal groups over rings (cotes 77, 82)

### SA04-25: affine quadrics and quadratic extensions: rank-two forms, alpha^2 - 4, mu_2 actions, the Arf scheme (cote 77) (= H02T)

- **Status on his pages:** Work notes only. **Kind:** algebra.
- **Where:** cote 77, scans 53,62,69,74,78,130,134,146,148,152,157.
- **Notes (70 entries):** work:K77-01 (6); work:K77-02 (6); work:K77-03 (6); work:K77-04 (6); work:K77-06 (6); work:K77-07 (6); work:K77-08 (6); work:K77-09 (6) ....
- **Notes files:** `codex_web_20261113/returns/K77-01/out/K77-01_mathnotes.md`; `codex_web_20261113/returns/K77-01/out/K77-01_notes.md`; `codex_web_20261113/returns/K77-02/out/K77-02_mathnotes.md`; `codex_web_20261113/returns/K77-02/out/K77-02_notes.md`; `codex_web_20261113/returns/K77-03/out/K77-03_mathnotes.md`; `codex_web_20261113/returns/K77-03/out/K77-03_notes.md` ....
- **Depends:** related: SA02-1 (our note).
- **Claims:**
  - SA04-C2 (77/069): ""On présume que epsilon = (-1)^m": B^2 - epsilon Delta = 0 mod 4, for the generic determinant Delta with doubled diagonal and B the sum over". **proves**: expansion of the determinant over permutations mod 4 (sweep 2 part 1).
- **Units (112):** K77-01.u01, K77-01.u02, K77-01.u03, K77-01.u04, K77-01.u05, K77-01.u06, K77-01.u07, K77-01.u08 ....
- **Flags:** his presumption epsilon = (-1)^m checked true (77/069).
- **Other topics:** SA02-1 (quadratic algebras, cote 84); SA01-28; = H02T.

### SA04-30: SO(3) = GP(1) over a base: rank-three quadratic modules, the sl_2 action, the stabilizer of a section of P^1 (cote 82) (= H02Z)

- **Status on his pages:** Work notes only. **Kind:** algebra.
- **Where:** cote 82, scans 14-17,19.
- **Notes (35 entries):** work:K82-01 (6); work:K82-02 (6); work:K82-03 (6); work:K82-04 (6); work:K82-05 (6); codex:K82-01 (1); codex:K82-02 (1); codex:K82-03 (1) ....
- **Notes files:** `codex_web_20261113/returns/K82-01/out/K82-01_mathnotes.md`; `codex_web_20261113/returns/K82-01/out/K82-01_notes.md`; `codex_web_20261113/returns/K82-02/out/K82-02_mathnotes.md`; `codex_web_20261113/returns/K82-02/out/K82-02_notes.md`; `codex_web_20261113/returns/K82-03/out/K82-03_mathnotes.md`; `codex_web_20261113/returns/K82-03/out/K82-03_notes.md` ....
- **Depends:** used by: SA04-31 (his page).
- **Units (50):** K82-01.u01, K82-01.u02, K82-01.u03, K82-01.u04, K82-01.u05, K82-01.u06, K82-01.u07, K82-01.u08 ....
- **Other topics:** = H02Z.

## Algebraic geometry: descent, local cohomology, Hilbert schemes, Chern classes (cotes 94-102)

### SA04-36: coherent modules from a functor and prorepresentability (cote 94) (= H035)

- **Status on his pages:** Work notes only. **Kind:** algebra.
- **Where:** cote 94, scans 7,13.
- **Notes (8 entries):** work:K94-01 (6); codex:K94-01 (1); codex:K94-02 (1).
- **Notes files:** `codex_web_20261113/returns/K94-01/out/K94-01_mathnotes.md`; `codex_web_20261113/returns/K94-01/out/K94-01_notes.md`; `codex_web_20261113/returns/K94-02/out/K94-02_notes.md`.
- **Depends:** related: SA04-40 (a proof (ours)).
- **Units (14):** K94-01.u01, K94-01.u02, K94-01.u03, K94-01.u04, K94-01.u05, K94-01.u06, K94-01.u07, K94-01.u08 ....
- **Other topics:** = H035.

### SA04-40: functors (Sch)^op -> (Ens): recollements along a class of covers (cote 102) (= H03A)

- **Status on his pages:** Work notes only. **Kind:** construction.
- **Where:** cote 102.
- **Notes (7 entries):** work:K102-01 (6); codex:K102-01 (1).
- **Notes files:** `codex_web_20261113/returns/K102-01/out/K102-01_mathnotes.md`; `codex_web_20261113/returns/K102-01/out/K102-01_notes.md`.
- **Depends:** related: SA04-36 (a proof (ours)); uses: SGA 4 (sites, topos); EGA IV (étale, flat, henselian); SGA 1 VIII (fpqc descent) (his page).
- **Corrections:** cote 102: combinatorial geometry (archive section 11) -> descent and the EGA themes (Part III), with SA04-36.
- **Units (11):** K102-01.u01, K102-01.u02, K102-01.u03, K102-01.u04, K102-01.u05, K102-01.u06, K102-01.u07, K102-01.u08 ....
- **Flags:** a link across folders (a draft for EGA VI).
- **Other topics:** = H03A; EGA VI (recollements, K102-01).

### SA04-39: local cohomology: cones, twists, topologies on H^0, change of rings and duality (cote 101) (= H038)

- **Status on his pages:** Work notes only. **Kind:** algebra.
- **Where:** cote 101.
- **Notes (21 entries):** work:K101-01 (6); work:K101-02 (6); work:K101-03 (6); codex:K101-01 (1); codex:K101-02 (1); codex:K101-03 (1).
- **Notes files:** `codex_web_20261113/returns/K101-01/out/K101-01_mathnotes.md`; `codex_web_20261113/returns/K101-01/out/K101-01_notes.md`; `codex_web_20261113/returns/K101-02/out/K101-02_mathnotes.md`; `codex_web_20261113/returns/K101-02/out/K101-02_notes.md`; `codex_web_20261113/returns/K101-03/out/K101-03_mathnotes.md`; `codex_web_20261113/returns/K101-03/out/K101-03_notes.md`.
- **Depends:** uses: local cohomology, later SGA 2 (our note).
- **Units (35):** K101-01.u01, K101-01.u02, K101-01.u03, K101-01.u04, K101-01.u05, K101-01.u06, K101-01.u07, K101-01.u08 ....
- **Flags:** a link across folders (1).
- **Other topics:** = H038.

### SA04-17: Hilbert schemes and norms (cote 98): norms, symmetric powers, descent, bounded families, Tor and Ext

- **Status on his pages:** not checked. **Kind:** proposition.
- **Where:** cote 98, scans 2-7,9-25,27-36,38-40,42-44,172,383.
- **Notes (8 entries):** MPL_98 (8).
- **Notes files:** `inputs/SA04/pro/MPL_98_notes.md`.

### SA04-37: Chern classes of representations: the regular representation of a cyclic group (cote 97) (= H036)

- **Status on his pages:** Work notes only. **Kind:** algebra.
- **Where:** cote 97.
- **Notes (7 entries):** work:K97-01 (6); codex:K97-01 (1).
- **Notes files:** `codex_web_20261113/returns/K97-01/out/K97-01_mathnotes.md`; `codex_web_20261113/returns/K97-01/out/K97-01_notes.md`.
- **Units (9):** K97-01.u01, K97-01.u02, K97-01.u03, K97-01.u04, K97-01.u05, K97-01.u06, K97-01.u07, K97-01.u08 ....
- **Other topics:** = H036.

## Documentary and apparatus

### SA04-5: documentary: reused administrative sheets (research policy, a 1976 budget) in cote 93

- **Status on his pages:** documentary. **Kind:** documentary.
- **Where:** cote 93, scans 27,32,57.
- **Notes (4 entries):** MPL_93_047-091 (4).
- **Notes files:** `inputs/SA04/pro/MPL_93_047-091_notes.md`.

### SA04-18: documentary: offprints, covers and year labels of cotes 93 and 161 (= H00E)

- **Status on his pages:** documentary. **Kind:** documentary.
- **Where:** cote 93, scans 3,10,18,28,37,161,222,234.
- **Notes (5 entries):** MPL_93_221-236+161-5 (5).
- **Notes files:** `inputs/SA04/pro/MPL_93_221-236+161-5_notes.md`.
- **Other topics:** = H00E (SA23-45).

### SA04-29: documentary: autobiographical and administrative typescripts among cotes 69-102 (cote 80 scans 22-30; cote 94 report on local fields) (= H02X)

- **Status on his pages:** documentary. **Kind:** documentary.
- **Where:** cote 80; cote 94.
- **Notes (12 entries):** work:K80-02 (6); work:K94-02 (6).
- **Notes files:** `codex_web_20261113/returns/K80-02/out/K80-02_mathnotes.md`; `codex_web_20261113/returns/K94-02/out/K94-02_mathnotes.md`.
- **Units (22):** K80-02.u01, K80-02.u02, K80-02.u03, K80-02.u04, K80-02.u05, K80-02.u06, K80-02.u07, K80-02.u08 ....
- **Other topics:** = H02X.

### SA04-41: documentary: title sheets, section headings, dates and reused sheets of cotes 69-102 (Codex notes on the sheets): course and draft titles, page counts, reused notices, letters and administrative sheets of 1975-1981 (= H02X)

- **Status on his pages:** documentary. **Kind:** documentary.
- **Where:** cote 69, scans 83-84,90,96-97,99,104,106,108,114; cote 70, scans 39,91,96; cote 73; cote 74, scans 39,43,47,50,68,73,88-89,93,106-107,120; cote 76, scans 6,19,51,63; cote 77, scans 34-35,59,66,98,103,108,113,144-145,158; cote 78, scans 17,19,23,27,31-32,34,40,53,61,74,94,117,130; cote 79, scans 27,33-34,36,38,62,71-72,90,93,103,116,124,130,145,159-160,175,179,191,195-197,199,213,236,239,266; cote 80, scans 8,39,54-55,61,71; cote 82, scans 17,65; cote 85, scans 7,34,44,46,49,53,76,83,85-86,95-96,98; cote 86, scans 3,6,11; cote 87, scans 3,29-30,38,40; cote 88, scans 2,11; cote 89, scans 12,20-21; cote 94, scans 2-3,12,14,22; cote 97; cote 101, scans 16-18,29-31,40; cote 102.
- **Notes (98 entries):** codex:K101-01 (1); codex:K101-02 (1); codex:K101-03 (1); codex:K102-01 (1); codex:K69-01 (1); codex:K69-02 (1); codex:K69-03 (1); codex:K69-04 (1) ....
- **Notes files:** `codex_web_20261113/returns/K101-01/out/K101-01_notes.md`; `codex_web_20261113/returns/K101-02/out/K101-02_notes.md`; `codex_web_20261113/returns/K101-03/out/K101-03_notes.md`; `codex_web_20261113/returns/K102-01/out/K102-01_notes.md`; `codex_web_20261113/returns/K69-01/out/K69-01_notes.md`; `codex_web_20261113/returns/K69-02/out/K69-02_notes.md` ....
- **Corrections:** reused sheets of cotes 69-80: undated notes -> terminus post quem about 1975-1981 from the reused sheets.
- **Flags:** a link across folders (2).
- **Other topics:** SA04-29 (= H02X); SA01-43 (thesis notices, cote 71).

### SA04-10: the notes' apparatus and synthesis for cote 93 (strands, sources, the strand comparisons S20, X01-X07)

- **Status on his pages:** apparatus. **Kind:** apparatus.
- **Where:** cote 93, scans 4,7,23,36,46-47,50,70,72,84,168.
- **Notes (22 entries):** MPL_93_047-091 (15); MPL_93_221-236+161-5 (7).
- **Notes files:** `inputs/SA04/pro/MPL_93_047-091_notes.md`; `inputs/SA04/pro/MPL_93_221-236+161-5_notes.md`.

## Counts

- Items: 40; placed entries: 1270.
- DEPENDS rows: 45; CLAIM_LINKS: 7; UNIT_LINKS: 1015; CORRECTIONS: 6; part-2 check events: 3.
