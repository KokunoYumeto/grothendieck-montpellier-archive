# SA03: deformations and representability (cote 91); characteristic p, connections and crystals (cote 93): what is where

Claude Opus 5.5 at effort max, a6d42bf6fe2b0d8a8, horizontal sweep 2 part 2, 2026-11-18.

The topic holds two cotes:
- **Cote 91, scans 19-143:** lifting of morphisms and their obstructions, representability of Hom, Isom and Aut, descent and the projective immersion, finite étale comparisons, functors of local nature, the constructible topology, the Greenberg functor and Néron spaces, and finite-order evaluation. Numbered typescripts are reused on the backs: exercise sheets on restricted Lie algebras and formal groups, and exterior algebras.
- **Cote 93, scans 2-60 and 135-220:** pointed genus-one curves in characteristic p, Hasse-Witt and the Cartier operation, connections and Gauss-Manin, the Schwarzian and p-curvature, and the Dieudonné-crystal programme (the Montreal notes, Ch. V). Also Wanderley's offprint on orientation, a typescript on operator semigroups, and reused administrative typescripts.

Cote 91 is split with SA02 (scans 2-18), and cote 93 with SA01 (scans 92-134) and SA04 (scans 47-91, 219-236).

Heavy notes: the Pro packages MPL_91_019-058, MPL_91_059-098, MPL_91_099-143, MPL_93_002-046 (GPT-6 Astra, ChatGPT Pro mode). Light notes: Work and Codex K91-02..10, K93-01..08.

Piece of sweep 2 part 2: `sweep2/REPORTS/cote93_scan052_exercise_22a.md`.

How to read an entry:
- **Where:** cote and scans, the notes it is in (package or folder), and the notes files. Scans are the PDF pages of the cote in `grothendieck_archive_montpellier`.
- **Depends:** what the item uses and what uses it, with the basis: his page, our note, or a proof (ours).
- **Claims:** his claims on the item, linked to what proves, refutes or refines them (CLAIM_LINKS.tsv).
- **Units:** the companion units that discuss it (UNIT_LINKS.tsv).
- **Flags, corrections:** from FLAGS.tsv and CORRECTIONS.tsv.

## Deformations, representability and descent (cote 91, scans 19-98)

### SA03-1: lifting of morphisms and its Ext obstruction classes; rigidity and rigidification (Murre's criterion)

- **Status on his pages:** stated; naturality and compatibility left as obligations. **Kind:** proposition.
- **Where:** cote 91, scans 16-25,31.
- **Notes (15 entries):** MPL_91_019-058 (15).
- **Notes files:** `inputs/SA03/pro/MPL_91_019-058_notes.md`.
- **Depends:** used by: SA03-2 (his page).

### SA03-2: representability of Hom, Isom and Aut functors by schemes (quasi-projectivity, separatedness, finite type of components, étale covers, descent of Aut and Isom)

- **Status on his pages:** stated; scope and proof status qualified by the notes. **Kind:** theorem (stated).
- **Where:** cote 91, scans 19,23,25-29,31-32,34-35,138.
- **Notes (21 entries):** MPL_91_019-058 (21).
- **Notes files:** `inputs/SA03/pro/MPL_91_019-058_notes.md`.
- **Depends:** related: SA02-12 (our note); used by: SA03-3 (his page); uses: SA03-1 (his page).
- **Flags:** a link across folders (1); a link across folders (SA02 Work K91 folders re-read these pages).
- **Other topics:** SA02-12 (cote 91 scans 2-18, MPL_90+91_002-018); EGA/SGA Hom schemes.

### SA03-3: descent, norms and the projective immersion: very ampleness, determinants, Nagata's example, the orbit lemma, finite type

- **Status on his pages:** stated with revisions; "fermé" deleted. **Kind:** proposition.
- **Where:** cote 91, scans 34-50,55,61,70,75-76,78,138.
- **Notes (33 entries):** MPL_91_019-058 (33).
- **Notes files:** `inputs/SA03/pro/MPL_91_019-058_notes.md`.
- **Depends:** uses: SA03-2 (his page).

### SA03-4: infinitesimal and finite étale comparisons: smoothness, étale repair, sections, the n^nu bound, dimension under Weil restriction, homogeneity

- **Status on his pages:** stated; one equation reversed (Hua VI). **Kind:** proposition.
- **Where:** cote 91, scans 14,34-35,50-59,118,124,126,608.
- **Notes (26 entries):** MPL_91_019-058 (26).
- **Notes files:** `inputs/SA03/pro/MPL_91_019-058_notes.md`.
- **Depends:** used by: SA03-6 (his page).
- **Claims:**
  - SA03-C1 (91/52): "D(s) = n D'(s) (the set equation before the corollary on dimension nd)". **corrects (reversed as written)**: Hua VI p. 51 corrects it; Pro note C05 agrees with the page (sweep 1 passage read).
- **Corrections:** 91/52: D(s) = n D'(s) -> reversed (dimension nd, as his corollary has it).

### SA03-6: functors on rings of local nature: the étale envelope, the equivalence criterion, partial right adjoints, gluing with triple intersections

- **Status on his pages:** stated; one corollary withdrawn. **Kind:** proposition.
- **Where:** cote 91, scans 11,16,19,59,61-80,138.
- **Notes (30 entries):** MPL_91_059-098 (30).
- **Notes files:** `inputs/SA03/pro/MPL_91_059-098_notes.md`.
- **Depends:** related: SA04-40 (our note); uses: SA03-4 (his page).

## Constructible topology, Greenberg-Néron and jets (cote 91, scans 99-143)

### SA03-7: constructible sets and the constructible topology: atomic points, piecewise isomorphism, noetherian topology vs scheme, finite type vs presentation, limits

- **Status on his pages:** stated; several reading questions. **Kind:** proposition.
- **Where:** cote 91, scans 81-82,84,87,89,91,93,95,97,99,101-102,104-111,113-116,118,120,126,132,134,136.
- **Notes (57 entries):** MPL_91_059-098 (22); MPL_91_099-143 (20); MPL_91_099-143:records:research_leads (15).
- **Notes files:** `inputs/SA03/pro/MPL_91_059-098_notes.md`; `inputs/SA03/pro/MPL_91_099-143_notes.md`; `returns/MPL_91_099-143_unzipped/.../research_leads.md`.
- **Depends:** used by: SA03-9 (his page).

### SA03-9: the Greenberg functor and Néron spaces: the six-part programme, ind objects, valuation-ring points, the Greenberg promorphism, Laurent-unit stages

- **Status on his pages:** programme; stated theorems. **Kind:** programme/theorem (stated).
- **Where:** cote 91, scans 16,31,59,61,67,75,80,84,89-90,92,99-101,109,111,115-116,118,120-124,126-128,130-132,134-136,141.
- **Notes (36 entries):** MPL_91_099-143 (20); MPL_91_099-143:records:research_leads (11); MPL_91_059-098 (5).
- **Notes files:** `inputs/SA03/pro/MPL_91_059-098_notes.md`; `inputs/SA03/pro/MPL_91_099-143_notes.md`; `returns/MPL_91_099-143_unzipped/.../research_leads.md`.
- **Depends:** related: SA04-40 (our note); uses: Greenberg (1961, 1963); Bosch-Lütkebohmert-Raynaud, Néron Models (our note), SA03-10 (his page), SA03-7 (his page).
- **Claims:**
  - SA03-C4 (91/118): ""Pb à poser. Espaces de Néron!" in the six-item programme". **open (programme)**: none: a programme item.
- **Other topics:** SA02-12; Greenberg, Néron models (literature).

### SA03-10: finite-order evaluation, jets and the affine-space rows; exterior-algebra components

- **Status on his pages:** unfinished calculations. **Kind:** calculation.
- **Where:** cote 91, scans 100,119,121,123,128,138,140,142.
- **Notes (16 entries):** MPL_91_099-143 (9); MPL_91_099-143:records:research_leads (7).
- **Notes files:** `inputs/SA03/pro/MPL_91_099-143_notes.md`; `returns/MPL_91_099-143_unzipped/.../research_leads.md`.
- **Depends:** used by: SA03-9 (his page).
- **Flags:** a link across folders (1).

## Characteristic p: curves, the Cartier operation and connections (cote 93)

### SA03-11: pointed genus-one curves in characteristic p: the formulary (Hasse invariant, Legendre polynomial, Tate cusp, j = 1728, wild automorphisms in characteristics 2 and 3)

- **Status on his pages:** stated; two reference requests. **Kind:** calculation.
- **Where:** cote 93, scans 3-8,12-15,17-19,21-22.
- **Notes (42 entries):** MPL_93_002-046 (26); work:K93-10 (6); work:K93-11 (6); codex:K93-10 (2); codex:K93-11 (2).
- **Notes files:** `codex_web_20261113/returns/K93-10/out/K93-10_mathnotes.md`; `codex_web_20261113/returns/K93-10/out/K93-10_notes.md`; `codex_web_20261113/returns/K93-11/out/K93-11_mathnotes.md`; `codex_web_20261113/returns/K93-11/out/K93-11_notes.md`; `inputs/SA03/pro/MPL_93_002-046_notes.md`.
- **Depends:** used by: SA03-12 (his page).
- **Other topics:** any topic with the Legendre family or Hasse invariants (SA10?).

### SA03-12: Hasse-Witt, the Cartier operation on differentials and Cartier descent

- **Status on his pages:** stated. **Kind:** proposition.
- **Where:** cote 93, scans 7,23-24,179.
- **Notes (9 entries):** work:K93-04 (6); codex:K93-04 (2); MPL_93_002-046 (1).
- **Notes files:** `codex_web_20261113/returns/K93-04/out/K93-04_mathnotes.md`; `codex_web_20261113/returns/K93-04/out/K93-04_notes.md`; `inputs/SA03/pro/MPL_93_002-046_notes.md`.
- **Depends:** used by: SA03-16 (our note); uses: SA03-11 (his page).
- **Units (11):** K93-04.u01, K93-04.u02, K93-04.u03, K93-04.u04, K93-04.u05, K93-04.u06, K93-04.u07, K93-04.u08 ....

### SA03-18: connections: principal parts, Gauss-Manin, logarithmic connections, stratifications on torsors, Picard functors with connection (cote 93 typescript)

- **Status on his pages:** typescript (Work notes). **Kind:** construction.
- **Where:** cote 91; cote 93, scans 76-77,135-136,151,165,193,207.
- **Notes (68 entries):** work:K93-01 (6); work:K93-02 (6); work:K93-03 (6); work:K93-05 (6); work:K93-06 (6); work:K93-09 (6); codex:K91-01 (2); codex:K91-02 (2) ....
- **Notes files:** `codex_web_20261113/returns/K91-01/out/K91-01_notes.md`; `codex_web_20261113/returns/K91-02/out/K91-02_notes.md`; `codex_web_20261113/returns/K91-03/out/K91-03_notes.md`; `codex_web_20261113/returns/K91-04/out/K91-04_notes.md`; `codex_web_20261113/returns/K91-05/out/K91-05_notes.md`; `codex_web_20261113/returns/K91-06/out/K91-06_notes.md` ....
- **Depends:** related: SA04-11 (our note); used by: SA03-14 (our note).
- **Units (47):** K93-01.u01, K93-01.u02, K93-01.u03, K93-01.u04, K93-01.u05, K93-01.u06, K93-01.u07, K93-01.u08 ....

### SA03-14: the Schwarzian, second-order equations and p-curvature

- **Status on his pages:** calculated; coefficient corrected on the page. **Kind:** calculation.
- **Where:** cote 93, scans 7,23,36.
- **Notes (6 entries):** MPL_93_002-046 (6).
- **Notes files:** `inputs/SA03/pro/MPL_93_002-046_notes.md`.
- **Depends:** related: SA01-32 (our note), SA04-7 (our note); uses: SA03-18 (our note).

## Crystals (cote 93, scans 37-60)

### SA03-16: the Dieudonné-crystal programme (Montreal notes, Ch. V): Problems 1-3, F-V exactness, Barsotti-Tate groups and their deformations, abelian crystals and de Rham (= H024, H02H)

- **Status on his pages:** programme; theorems announced, not proved here. **Kind:** programme/conjecture.
- **Where:** cote 93, scans 7,18,32,37-61.
- **Notes (42 entries):** MPL_93_002-046 (35); work:K93-07 (5); codex:K93-07 (2).
- **Notes files:** `codex_web_20261113/returns/K93-07/out/K93-07_mathnotes.md`; `codex_web_20261113/returns/K93-07/out/K93-07_notes.md`; `inputs/SA03/pro/MPL_93_002-046_notes.md`.
- **Depends:** related: SA04-1 (a proof (ours)); used by: SA03-15 (our note); uses: SA03-12 (our note).
- **Claims:**
  - SA03-C3 (93/49-51): "Problem 4: the essential image of the restriction functor, a valuative criterion, a Zariski-open description in the Grassmannian". **open**: none: an open question of his.
- **Corrections:** K93-07 (cote 93 scans 47-60): filed under SA03 -> a second reading of SA04's MPL_93_047-091 (H02H, H02N, SA04-4).
- **Flags:** a link across folders (2); a link across folders (K93-07 re-reads SA04 pages).
- **Other topics:** crystalline Dieudonné theory (Montreal notes); cotes 100 (Barsotti-Tate, SA01 list) and 159; = H024; K93-07 re-reads SA04's MPL_93_047-091 (= H02H, SA04-1), Problem 4 continues Problems 1-3.

### SA03-21: Work K93-07's remarks on cote 93 scans 52-60: the typed Banach-algebra exercise 22 a) (the lemma of Cohen's factorization theorem), the Euler characteristic of spheres by the hemisphere recurrence, the local-system cell lemma (= H02N)

- **Status on his pages:** decided on the scan (part 2): the type reads ||yw - w||, both transcriptions misread it as ||yw - u||; M52 refutes only the misreading and the exercise as typed is true; the recurrence agrees on dimensions 0-8. **Kind:** remarks (the Work notes').
- **Where:** cote 93, scans 47-60.
- **Notes (1 entry):** work:K93-07 (1).
- **Notes files:** `codex_web_20261113/returns/K93-07/out/K93-07_mathnotes.md`.
- **Depends:** related: SA04-2 (a proof (ours)), SA04-4 (our note).
- **Claims:**
  - SA03-C2 (93/052 (typed, struck)): "exercise 22 a): ||u|| < C, ||uw - w|| < eta, 0 <= gamma <= 1/4C imply ||yw - w|| < epsilon, y = [(1 - gamma)e + gamma u]^-1". **proves (as typed)**: my proof (||v^-1|| < 2, yw - w = -gamma v^-1 (uw - w)); the Work M52 refutes only the misreading ||yw - u||.
- **Corrections:** 93/052: ||yw - u|| < epsilon (Pro MPL_93_047-091 and Work K93-07) -> ||yw - w|| < epsilon; work:K93-07#6 (M52): M52: the printed wording is refuted at u = 1, w = 0 -> M52 refutes the misreading only; S52's intended reading is the typed text.
- **Flags:** suspected misreading (1); suspected misreading or an error of the typed exercise (scan 52).
- **Other topics:** = H02N (SA04-2, the pseudo-resolvent exercises); SA04-4 (Euler characteristic axioms).

### SA03-15: the notes' proposed bridges to cotes 159 and 64 (arithmetic routes)

- **Status on his pages:** not on the pages. **Kind:** notes' proposal.
- **Where:** cote 93, scans 4,7,44.
- **Notes (3 entries):** MPL_93_002-046 (3).
- **Notes files:** `inputs/SA03/pro/MPL_93_002-046_notes.md`.
- **Depends:** uses: SA03-16 (our note).
- **Flags:** a link across folders (1); a link across folders (bridges to cotes 159, 64).

## Other mathematics on reused leaves

### SA03-8: the printed exercise sheets with editorial requests (polarization, restricted Lie identities, tensor reciprocity, restricted enveloping algebras, formal groups)

- **Status on his pages:** printed; exercises. **Kind:** documentary/exercise.
- **Where:** cote 91, scans 83,85,88,90,92,94,96-98,100-101,119,127,129,134,138-139,141,143.
- **Notes (21 entries):** MPL_91_059-098 (9); MPL_91_099-143 (7); MPL_91_099-143:records:research_leads (5).
- **Notes files:** `inputs/SA03/pro/MPL_91_059-098_notes.md`; `inputs/SA03/pro/MPL_91_099-143_notes.md`; `returns/MPL_91_099-143_unzipped/.../research_leads.md`.
- **Flags:** a link across folders (1).
- **Other topics:** SA02-16 (restricted enveloping algebras, K91-10); the numbered typescripts n° 285, 316, 371 (possibly Bourbaki rédactions: my inference from the numbering, not checked).

### SA03-13: Wanderley's offprint "Théorie axiomatique de l'orientation des variétés topologiques à bord" and his handwritten orientation sheets

- **Status on his pages:** offprint and definitions. **Kind:** documentary/definition.
- **Where:** cote 93, scans 27-31,33,61.
- **Notes (7 entries):** MPL_93_002-046 (7).
- **Notes files:** `inputs/SA03/pro/MPL_93_002-046_notes.md`.
- **Depends:** related: SA21-4 (our note).
- **Flags:** a link across folders (1).
- **Other topics:** SA21 (Vers une géométrie des formes) and the tame topology / pseudoline material (SA11).

### SA03-19: a typescript on operator semigroups and the Yosida-Hewitt decomposition (cote 93, typed pp. 5-6)

- **Status on his pages:** documentary. **Kind:** documentary (others' mathematics).
- **Where:** cote 93, scans 32,34.
- **Notes (12 entries):** work:K93-12 (6); MPL_93_002-046 (4); codex:K93-12 (2).
- **Notes files:** `codex_web_20261113/returns/K93-12/out/K93-12_mathnotes.md`; `codex_web_20261113/returns/K93-12/out/K93-12_notes.md`; `inputs/SA03/pro/MPL_93_002-046_notes.md`.

## Documentary and apparatus

### SA03-20: a reused typescript report on university research (cote 93, scans 61-67)

- **Status on his pages:** documentary. **Kind:** documentary.
- **Where:** cote 93, scans 61-67.
- **Notes (8 entries):** work:K93-08 (6); codex:K93-08 (2).
- **Notes files:** `codex_web_20261113/returns/K93-08/out/K93-08_mathnotes.md`; `codex_web_20261113/returns/K93-08/out/K93-08_notes.md`.

### SA03-5: the notes' apparatus for cote 91 (keys, scan summaries, comparisons, plans)

- **Status on his pages:** apparatus. **Kind:** apparatus.
- **Where:** cote 91, scans 2,19-21,25,31,34-35,37,50,59,61,97-102,106,115,126-127,131,172,312,383-384,608.
- **Notes (21 entries):** MPL_91_019-058 (13); MPL_91_059-098 (4); MPL_91_099-143 (4).
- **Notes files:** `inputs/SA03/pro/MPL_91_019-058_notes.md`; `inputs/SA03/pro/MPL_91_059-098_notes.md`; `inputs/SA03/pro/MPL_91_099-143_notes.md`.

### SA03-17: the notes' apparatus for cote 93

- **Status on his pages:** apparatus. **Kind:** apparatus.
- **Where:** cote 93, scans 7,32,34,38,61.
- **Notes (1 entry):** MPL_93_002-046 (1).
- **Notes files:** `inputs/SA03/pro/MPL_93_002-046_notes.md`.

## Counts

- Items: 21; placed entries: 475.
- DEPENDS rows: 39; CLAIM_LINKS: 4; UNIT_LINKS: 58; CORRECTIONS: 4; part-2 check events: 2.
