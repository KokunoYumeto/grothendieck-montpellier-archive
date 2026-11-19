# SA01: regular polyhedra over rings, 2x2 matrices and traces, plane topology, and the cote 93 uniformization notes: what is where

Claude Opus 5.5 at effort max, a6d42bf6fe2b0d8a8, horizontal sweep 2 part 2, 2026-11-18.

The topic is "Géométrie et topologie combinatoire", part 1. Its subjects, by cote:
- **Cote 72:** pinned regular realizations of the regular polyhedra over rings.
- **Cote 83:** 2x2 matrices, traces and quadratic algebras: the trace identity for triples, the trace cube and its determinants, Azumaya algebras.
- **Cote 81 and cote 154, scans 46-76:** immersions of the disc and pseudoline arrangements. The shared package belongs to SA11.
- **Cotes 71 and 75:** plane polygons, C. Contou-Carrère's Jordan-theorem manuscript and the DEA course "Géométries combinatoires".
- **Cote 93, scans 92-134 (from sweep 2):** projective connections, the Schwarzian and uniformization; with K93-13, periods and the canonical de Rham connection.

Several folders filed here belong with SA02 or SA04 by object: K84-10, K90-02, K93-13 and MPL_93_092-134. Their items carry the global tags of those objects.

Heavy notes: the Pro packages MPL_72, MPL_81_038-055+154_046-076, MPL_83_*, MPL_93_092-134 (GPT-6 Astra, ChatGPT Pro mode). Light notes: Work and Codex K72, K83, K84-10, K90-02, K93-13, J71, J75, J81, H97.

Piece of sweep 2 part 2: `sweep2/REPORTS/cote93_scans100_113_117_slips.md`.

How to read an entry:
- **Where:** cote and scans, the notes it is in (package or folder), and the notes files. Scans are the PDF pages of the cote in `grothendieck_archive_montpellier`.
- **Depends:** what the item uses and what uses it, with the basis: his page, our note, or a proof (ours).
- **Claims:** his claims on the item, linked to what proves, refutes or refines them (CLAIM_LINKS.tsv).
- **Units:** the companion units that discuss it (UNIT_LINKS.tsv).
- **Flags, corrections:** from FLAGS.tsv and CORRECTIONS.tsv.

## Regular polyhedra and their realizations over rings (cotes 72, 75, 83)

### SA01-1: pinned regular realizations of the regular n-polyhedron over a ring (rank-one operators, flags, base change)

- **Status on his pages:** stated and worked in coordinates; general equivalence on 77 left with reading and descent questions (notes). **Kind:** definition/construction.
- **Where:** cote 72, scans 2-3,35,59,73-77,80-83,98-100.
- **Notes (33 entries):** MPL_72_035-081 (9); work:K72-01 (6); work:K72-06 (6); work:K72-07 (6); codex:K72-01 (2); codex:K72-06 (2); codex:K72-07 (2).
- **Notes files:** `codex_web_20261113/returns/K72-01/out/K72-01_mathnotes.md`; `codex_web_20261113/returns/K72-01/out/K72-01_notes.md`; `codex_web_20261113/returns/K72-06/out/K72-06_mathnotes.md`; `codex_web_20261113/returns/K72-06/out/K72-06_notes.md`; `codex_web_20261113/returns/K72-07/out/K72-07_mathnotes.md`; `codex_web_20261113/returns/K72-07/out/K72-07_notes.md` ....
- **Depends:** used by: SA01-2 (our note), SA01-3 (his page), SA01-41 (our note).
- **Units (28):** K72-01.u01, K72-01.u02, K72-01.u03, K72-01.u04, K72-01.u05, K72-01.u06, K72-01.u07, K72-01.u08 ....
- **Flags:** LM/Derivateurs lens (1); a link across folders (1).

### SA01-3: the invariant quadratic form of the reflection realization, its orthogonal automorphism group, the conic and characteristic two

- **Status on his pages:** worked on 35-43; parts proved in the notes. **Kind:** proposition/calculation.
- **Where:** cote 72, scans 18,35-36,38-39,43,52,54-55,59.
- **Notes (35 entries):** MPL_72_035-081 (20); work:K72-02 (6); work:K72-03 (5); codex:K72-02 (2); codex:K72-03 (2).
- **Notes files:** `codex_web_20261113/returns/K72-02/out/K72-02_mathnotes.md`; `codex_web_20261113/returns/K72-02/out/K72-02_notes.md`; `codex_web_20261113/returns/K72-03/out/K72-03_mathnotes.md`; `codex_web_20261113/returns/K72-03/out/K72-03_notes.md`; `inputs/SA01/pro/MPL_72_035-081_notes.md`.
- **Depends:** used by: SA01-4 (our note), SA01-6 (his page); uses: SA01-1 (his page).
- **Units (12):** K72-02.u01, K72-02.u02, K72-02.u03, K72-02.u04, K72-02.u05, K72-02.u06, K72-02.u07, K72-02.u08 ....

### SA01-4: determinant recurrences, permutation and matching counts, continuants and dual bases of the realization (scans 45-71)

- **Status on his pages:** calculated on the pages; several cancelled attempts. **Kind:** calculation.
- **Where:** cote 72, scans 45-53,57,61,63,65,67,69,71,75,78.
- **Notes (45 entries):** MPL_72_035-081 (29); work:K72-04 (6); work:K72-05 (6); codex:K72-04 (2); codex:K72-05 (2).
- **Notes files:** `codex_web_20261113/returns/K72-04/out/K72-04_mathnotes.md`; `codex_web_20261113/returns/K72-04/out/K72-04_notes.md`; `codex_web_20261113/returns/K72-05/out/K72-05_mathnotes.md`; `codex_web_20261113/returns/K72-05/out/K72-05_notes.md`; `inputs/SA01/pro/MPL_72_035-081_notes.md`.
- **Depends:** uses: SA01-3 (our note).

### SA01-6: the trigonometric line at 72/036: beta_i, alpha_i = 4cos^2 theta_i and cos 2theta_i

- **Status on his pages:** stated with an inconsistency (his slip or a misreading). **Kind:** reading question / slip.
- **Where:** cote 72, scans 35-36.
- **Notes (2 entries):** MPL_72_035-081 (1); work:K72-03 (1).
- **Notes files:** `codex_web_20261113/returns/K72-03/out/K72-03_mathnotes.md`; `inputs/SA01/pro/MPL_72_035-081_notes.md`.
- **Depends:** uses: SA01-3 (his page).
- **Claims:**
  - SA01-C3 (72/036): "2(2cos^2 theta_i + 1) = 4cos 2theta_i as transcribed". **suspected misreading, open (scan not viewed)**: false as transcribed; "+1" against "-1" (Pro A15, Work S36).
- **Corrections:** 72/036: 2(2cos^2 theta_i + 1) = 4cos 2theta_i -> with -1 the identity holds.
- **Flags:** suspected misreading (2); suspected misreading.

### SA01-27: the icosahedral group in 2x2 matrices over a ring: elements of orders 2, 3, 5, elementary subgroups, frames and codiagonals

- **Status on his pages:** calculated (Work notes). **Kind:** calculation.
- **Where:** cote 83, scans 3,32,46.
- **Notes (24 entries):** work:K83-01 (6); work:K83-09 (6); work:K83-11 (6); codex:K83-01 (2); codex:K83-09 (2); codex:K83-11 (2).
- **Notes files:** `codex_web_20261113/returns/K83-01/out/K83-01_mathnotes.md`; `codex_web_20261113/returns/K83-01/out/K83-01_notes.md`; `codex_web_20261113/returns/K83-09/out/K83-09_mathnotes.md`; `codex_web_20261113/returns/K83-09/out/K83-09_notes.md`; `codex_web_20261113/returns/K83-11/out/K83-11_mathnotes.md`; `codex_web_20261113/returns/K83-11/out/K83-11_notes.md`.
- **Depends:** used by: SA01-16 (our note).
- **Units (30):** K83-01.u01, K83-01.u02, K83-01.u03, K83-01.u04, K83-01.u05, K83-01.u06, K83-01.u07, K83-01.u08 ....

### SA01-16: bi-icosahedra and the icosahedral structure at p = 5 (oriented vs non-oriented)

- **Status on his pages:** discussed; not settled. **Kind:** definition/question.
- **Where:** cote 83, scans 63-64,571.
- **Notes (11 entries):** work:K83-02 (6); MPL_83_178-222 (3); codex:K83-02 (2).
- **Notes files:** `codex_web_20261113/returns/K83-02/out/K83-02_mathnotes.md`; `codex_web_20261113/returns/K83-02/out/K83-02_notes.md`; `inputs/SA01/pro/MPL_83_178-222_notes.md`.
- **Depends:** uses: SA01-27 (our note).
- **Units (11):** K83-02.u01, K83-02.u02, K83-02.u03, K83-02.u04, K83-02.u05, K83-02.u06, K83-02.u07, K83-02.u08 ....

### SA01-41: the DEA course "Géométries combinatoires" (C4, 24 pp., cote 75): groups and homogeneous spaces, graphs and their topological and rectilinear realizations, the affine group of a group, small finite sets, classical groups, regular realizations, the vector envelope of a combinatorial polygon, orientation of a finite set

- **Status on his pages:** course notes; one step marked "il faut prouver que c'est bien une réalisation rectiligne si n >= 3". **Kind:** course notes.
- **Where:** cote 75, scans 2-7,9-16,18,26-28.
- **Notes (8 entries):** codex:J75-01 (2); codex:J75-02 (2); codex:J75-03 (2); codex:J75-04 (2).
- **Notes files:** `codex_web_20261113/returns/J75-01/out/J75-01_notes.md`; `codex_web_20261113/returns/J75-02/out/J75-02_notes.md`; `codex_web_20261113/returns/J75-03/out/J75-03_notes.md`; `codex_web_20261113/returns/J75-04/out/J75-04_notes.md`.
- **Depends:** related: SA01-40 (our note); uses: SA01-1 (our note).
- **Other topics:** related: H00W (SA01-1, pinned regular realizations); H02P (SA04-21, cote 70); SA04-22 (polygons, cote 73).

## Quadratic algebras, traces and 2x2 matrices (cotes 83, 84, 90)

### SA01-28: quadratic algebras over a ring and their discriminants; the invariant rho = lambda + 1/lambda

- **Status on his pages:** calculated (Work notes). **Kind:** calculation.
- **Where:** cote 83, scans 96,113-114,145-147,162-163.
- **Notes (32 entries):** work:K83-04 (6); work:K83-05 (6); work:K83-07 (6); work:K83-08 (6); codex:K83-04 (2); codex:K83-05 (2); codex:K83-07 (2); codex:K83-08 (2).
- **Notes files:** `codex_web_20261113/returns/K83-04/out/K83-04_mathnotes.md`; `codex_web_20261113/returns/K83-04/out/K83-04_notes.md`; `codex_web_20261113/returns/K83-05/out/K83-05_mathnotes.md`; `codex_web_20261113/returns/K83-05/out/K83-05_notes.md`; `codex_web_20261113/returns/K83-07/out/K83-07_mathnotes.md`; `codex_web_20261113/returns/K83-07/out/K83-07_notes.md` ....
- **Depends:** used by: SA01-17 (his page), SA01-18 (his page).
- **Units (37):** K83-04.u01, K83-04.u02, K83-04.u03, K83-04.u04, K83-04.u05, K83-04.u06, K83-04.u07, K83-04.u08 ....

### SA01-17: lambda-split extensions and their product * (with f-circle data)

- **Status on his pages:** construction begun; universal property open. **Kind:** construction.
- **Where:** cote 83, scans 178-180.
- **Notes (15 entries):** MPL_83_178-222 (7); work:K83-12 (6); codex:K83-12 (2).
- **Notes files:** `codex_web_20261113/returns/K83-12/out/K83-12_mathnotes.md`; `codex_web_20261113/returns/K83-12/out/K83-12_notes.md`; `inputs/SA01/pro/MPL_83_178-222_notes.md`.
- **Depends:** related: SA01-36 (our note); uses: SA01-28 (his page).

### SA01-36: extensions of invertible modules with a chi-trivialisation and their tensor product: changes b_i' = b_i + chi u_i, the map Hom(M,L) (x) Hom(M',L') -> Hom(M (x) M', L (x) L') (cote 84, scans 146-160) (= H01R)

- **Status on his pages:** calculations; question marks on the table entries (154.06). **Kind:** calculation.
- **Where:** cote 84, scans 146,148.
- **Notes (5 entries):** work:K84-10 (4); codex:K84-10 (1).
- **Notes files:** `codex_web_20261113/returns/K84-10/out/K84-10_mathnotes.md`; `codex_web_20261113/returns/K84-10/out/K84-10_notes.md`.
- **Depends:** related: SA01-17 (our note).
- **Flags:** a link across folders.
- **Other topics:** = H01R (SA02-4); related: H01W (SA02-9), H00Z (SA01-17).

### SA01-18: reconstruction of a rank-four Azumaya algebra from traces; the trace form in characteristic two

- **Status on his pages:** worked; notes correct and qualify. **Kind:** proposition.
- **Where:** cote 83, scans 245.
- **Notes (8 entries):** MPL_83_178-222 (8).
- **Notes files:** `inputs/SA01/pro/MPL_83_178-222_notes.md`.
- **Depends:** used by: SA01-23 (his page); uses: SA01-28 (his page).

### SA01-23: Azumaya algebras vs projective-line bundles; the trace quotient and the LM lifting gerbe

- **Status on his pages:** not on the pages. **Kind:** comparison.
- **Where:** cote 83, scans 245,257-258.
- **Notes (4 entries):** MPL_83_178-222 (4).
- **Notes files:** `inputs/SA01/pro/MPL_83_178-222_notes.md`.
- **Depends:** uses: SA01-18 (his page).
- **Flags:** the same thing noted with different readings or statements (1); LM/Derivateurs lens.
- **Other topics:** LM lifting gerbe (research register).

### SA01-19: the trace identity for triples of 2x2 matrices: tr(xyz)tr(xzy) and the missing term -4cc'c''

- **Status on his pages:** stated with a missing term (found by Hua XII-XIII). **Kind:** identity.
- **Where:** cote 83, scans 183-186.
- **Notes (10 entries):** MPL_83_178-222 (10).
- **Notes files:** `inputs/SA01/pro/MPL_83_178-222_notes.md`.
- **Depends:** used by: SA01-20 (his page).
- **Claims:**
  - SA01-C2 (83/183-186): "tr(xyz) tr(xzy) as he writes it, without the term -4cc'c''". **refines (adds the missing term)**: the identity with -4cc'c'' checked on 300 random integer triples (sweep 1).
- **Corrections:** 83/183-186: tr(xyz) tr(xzy) without -4cc'c'' -> Pi - 4cc'c''.
- **Flags:** a link across folders (1).
- **Other topics:** classical Fricke-type trace identities (literature, later sweep).

### SA01-20: invariants of triples of 2x2 matrices: the invariant ring, the quotient vs conjugacy orbits, specialization

- **Status on his pages:** stated without proof. **Kind:** proposition/question.
- **Where:** cote 83, scans 147,183,190,255.
- **Notes (7 entries):** MPL_83_178-222 (7).
- **Notes files:** `inputs/SA01/pro/MPL_83_178-222_notes.md`.
- **Depends:** used by: SA01-21 (his page); uses: SA01-19 (his page).

### SA01-21: the trace cube of four matrix variables: face and edge relations, 28 variables and 32 equations, the face-to-edge map

- **Status on his pages:** calculated; presentation not proved. **Kind:** calculation.
- **Where:** cote 83, scans 119,194,209-219.
- **Notes (38 entries):** MPL_83_178-222 (24); work:K83-13 (6); work:K83-14 (4); codex:K83-13 (2); codex:K83-14 (2).
- **Notes files:** `codex_web_20261113/returns/K83-13/out/K83-13_mathnotes.md`; `codex_web_20261113/returns/K83-13/out/K83-13_notes.md`; `codex_web_20261113/returns/K83-14/out/K83-14_mathnotes.md`; `codex_web_20261113/returns/K83-14/out/K83-14_notes.md`; `inputs/SA01/pro/MPL_83_178-222_notes.md`.
- **Depends:** used by: SA01-22 (his page); uses: SA01-20 (his page).

### SA01-22: the determinants on 211 (2^10) and 219 (512; his 27^2 - 1 = 728)

- **Status on his pages:** calculated on the page with an error at 219. **Kind:** calculation.
- **Where:** cote 83, scans 209-219.
- **Notes (5 entries):** MPL_83_178-222 (3); work:K83-14 (2).
- **Notes files:** `codex_web_20261113/returns/K83-14/out/K83-14_mathnotes.md`; `inputs/SA01/pro/MPL_83_178-222_notes.md`.
- **Depends:** uses: SA01-21 (his page).
- **Claims:**
  - SA01-C1 (83/219): "the determinant of the trace-cube system on 219 is 27^2 - 1 = 728". **refutes his value**: Pro C19, Work K83-14 and Hua XIII: 512 (with -1 in the corner; +1 gives 384 = 2^7 x 3, against his "premier à 3").
- **Corrections:** 83/219: 27^2 - 1 = 728 -> 512 (first reading -1 in the corner).
- **Flags:** a link across folders (2); a link across folders (Pro and Work agree).

### SA01-38: KG(X) over a Dedekind ring: an affine group, the regular representation, stable quasi-coherent submodules of finite type, flat base change and direct limits (cote 90, scans 14-25) (= H01J)

- **Status on his pages:** a cancelled proposition; the stable-submodule construction developed. **Kind:** proposition.
- **Where:** cote 90, scans 14,18,21-24.
- **Notes (4 entries):** work:K90-02 (4).
- **Notes files:** `codex_web_20261113/returns/K90-02/out/K90-02_mathnotes.md`.
- **Flags:** a link across folders.
- **Other topics:** = H01J (SA02-10).

## Plane topology, pseudolines and immersions (cotes 71, 81, 154)

### SA01-40: plane polygons and the Jordan theorem: C. Contou-Carrère's manuscript on three good vertices of a polygon (cote 71, dated 15 July 1976), lemmas I-XXI, with marginal marks; simplicial realizations (|K|, |L|)

- **Status on his pages:** proved in the manuscript; marked "faux", "faux pour n = 3!", "so what" in the margins (hand not identified in the notes). **Kind:** theorem/proof (another author's manuscript).
- **Where:** cote 71, scans 21-24,28-29,31,33-34,36-39,43.
- **Notes (10 entries):** codex:J71-03 (2); codex:J71-04 (2); codex:J71-05 (2); codex:J71-06 (2); codex:J71-01 (1); codex:J71-02 (1).
- **Notes files:** `codex_web_20261113/returns/J71-01/out/J71-01_notes.md`; `codex_web_20261113/returns/J71-02/out/J71-02_notes.md`; `codex_web_20261113/returns/J71-03/out/J71-03_notes.md`; `codex_web_20261113/returns/J71-04/out/J71-04_notes.md`; `codex_web_20261113/returns/J71-05/out/J71-05_notes.md`; `codex_web_20261113/returns/J71-06/out/J71-06_notes.md`.
- **Depends:** related: SA01-41 (our note).
- **Other topics:** related: SA01-41 (cote 75, polygons and realizations).

### SA01-9: the combinatorial surface of relative positions of an added projective pseudoline (Esquisse §8): scope and genealogy

- **Status on his pages:** constructed in part; open on the pages. **Kind:** construction (programme).
- **Where:** cote 81, scans 46,86,151.
- **Notes (14 entries):** MPL_81_038-055+154_046-076 (14).
- **Notes files:** `inputs/SA01/pro/MPL_81_038-055+154_046-076_notes.md`.
- **Depends:** used by: SA01-10 (his page), SA01-12 (his page).
- **Corrections:** MPL_81_038-055+154_046-076: indexed under SA01 and SA11 -> cote 154, scans 46-76: SA11.
- **Flags:** a link across folders (cote 154 under SA01 and SA11).
- **Other topics:** SA11 (cote 154 pseudolines: MPL_154_001-045, 077-126, 127-176, K154); SA01 cote 80 (Systemes de pseudo-droites); Esquisse §8 (cote 119).

### SA01-10: local gluing of the relative-position surface: facewise maps, critical points and arcs, exceptional edges, reconstruction from the graph

- **Status on his pages:** sketched; several claims unproved or withdrawn. **Kind:** construction.
- **Where:** cote 81, scans 56,160.
- **Notes (27 entries):** MPL_81_038-055+154_046-076 (27).
- **Notes files:** `inputs/SA01/pro/MPL_81_038-055+154_046-076_notes.md`.
- **Depends:** used by: SA01-11 (his page); uses: SA01-9 (his page).
- **Other topics:** SA11 (same package).

### SA01-11: the dihedral monodromy of polygon transport and its parity (sign) character

- **Status on his pages:** calculated in part; conjectured; cancelled continuations. **Kind:** proposition/conjecture.
- **Where:** cote 81, scans 65.
- **Notes (34 entries):** MPL_81_038-055+154_046-076 (34).
- **Notes files:** `inputs/SA01/pro/MPL_81_038-055+154_046-076_notes.md`.
- **Depends:** uses: SA01-10 (his page).
- **Other topics:** SA11 (same package).

### SA01-12: the four natural-map schemes (A1, A2, B1, B2): immersions, generization markers and circuit tests

- **Status on his pages:** tested on the pages; self-flagged failures. **Kind:** construction/test.
- **Where:** cote 81, scans 69.
- **Notes (34 entries):** MPL_81_038-055+154_046-076 (34).
- **Notes files:** `inputs/SA01/pro/MPL_81_038-055+154_046-076_notes.md`.
- **Depends:** related: SA01-29 (our note); uses: SA01-9 (his page).
- **Flags:** a link across folders (1).
- **Other topics:** SA11 (same package); SA01-29 (immersions, cote 81).

### SA01-29: immersions of the disc and of the circle (cote 81)

- **Status on his pages:** not checked. **Kind:** construction.
- **Where:** cote 81.
- **Notes (14 entries):** codex:J81-01 (2); codex:J81-02 (2); codex:J81-04 (2); codex:J81-05 (2); codex:J81-06 (2); codex:J81-07 (2); codex:J81-03 (2).
- **Notes files:** `codex_web_20261113/returns/J81-01/out/J81-01_notes.md`; `codex_web_20261113/returns/J81-02/out/J81-02_notes.md`; `codex_web_20261113/returns/J81-03/out/J81-03_notes.md`; `codex_web_20261113/returns/J81-04/out/J81-04_notes.md`; `codex_web_20261113/returns/J81-05/out/J81-05_notes.md`; `codex_web_20261113/returns/J81-06/out/J81-06_notes.md` ....
- **Depends:** related: SA01-12 (our note).
- **Flags:** a link across folders (1).
- **Other topics:** SA01-12 (the stable immersion model of cote 154).

## Projective connections, the Schwarzian and uniformization (cote 93)

### SA01-31: projective connections on a relative curve (cote 93, scans 92-134): principal parts and transversality, the triple (P, sigma, c) and adjoint opers, the Riccati coordinate lambda and its poles, horizontal sections and frames, the torsor under omega^2, third jets (= H03F)

- **Status on his pages:** sketched; formulas corrected later on the pages (factor 2, the Riccati equation); several steps self-flagged. **Kind:** construction.
- **Where:** cote 93, scans 92-93,95-101,103,105,107,109-110,112,118,120,133-134.
- **Notes (29 entries):** MPL_93_092-134 (29).
- **Notes files:** `inputs/SA01/pro/MPL_93_092-134_notes.md`.
- **Depends:** related: SA01-35 (our note); used by: SA01-32 (his page), SA01-33 (his page); uses: EGA IV 16 (principal parts) (our note).
- **Claims:**
  - SA01-C4 (93/100): "D(f dt) = a df/dt + b". **corrects his slip**: ink read on the scan: no f; a linear operator needs + b f.
- **Corrections:** 93/100: D(f dt) = a df/dt + b -> D(f dt) = a df/dt + b f; 93/107: the change of reference connection without a factor 2 -> with the factor 2: F changes by 2 eta eta-bar; MPL_93_092-134, K84-10, K90-02, K93-13: filed under SA01 -> objects of SA04 (H03D, H03E, H03F, H0JE, H02J, H00B, H00C) and SA02 (H01R, H01T,.
- **Flags:** suspected misreading (1); a link across folders.
- **Other topics:** = H03F (SA04-9); related: H03E (SA04-8), H04T (SA08-18), SA32-4.

### SA01-32: the Schwarzian G_t(s) = -2s'''/s' + 3(s''/s')^2 as a cocycle of quadratic differentials: homography invariance, the developing equation G_t(s) = mu and its linearization, the integral invariant G_0 (G = 12 G_0) over any base, Frobenius constants and rigidity in characteristics 2 and 3 (= H03D)

- **Status on his pages:** stated ("on vérifie facilement"); the characteristic-zero kernel left "à vérifier !"; the characteristic-3 branch replaced on the page. **Kind:** definition/proposition.
- **Where:** cote 93, scans 102,113-114,116-117,119-124,133.
- **Notes (26 entries):** MPL_93_092-134 (26).
- **Notes files:** `inputs/SA01/pro/MPL_93_092-134_notes.md`.
- **Depends:** used by: SA01-33 (his page), SA01-34 (our note); uses: SA01-31 (his page).
- **Claims:**
  - SA01-C5 (93/113): "s' = c exp Lambda(t), between log s' = -Lambda + c and s = c int exp(-Lambda)". **corrects his slip**: ink read on the scan: no minus.
  - SA01-C6 (93/117): "H = GP(1,C) as invertible matrices "mod. matrices diagonales"". **corrects his slip**: ink read on the scan; the Möbius group is modulo scalars.
  - SA01-C7 (93/121-122): "G(t,s) = 12 G_0(t,s), the integral invariant defined without dividing by 12". **proves**: MPL_93_092-134#46 (D01), checked by hand with Hasse derivatives (sweep 2 part 1).
  - SA01-C8 (93/122): "the constants of D(1), D(2), D(3) in small characteristic". **proves**: MPL_93_092-134#49 (D04): A[t^p], A[t^4], A[t^9], checked by Lucas's theorem.
  - SA01-C9 (93/122): "Pic(A) = 0 gives a matrix with ad - bc = 1". **refutes; refines**: MPL_93_092-134#54 (D09): Hua's counterexample s = 2t in A[t]/t^5 over F_5; MPL_93_092-134#59 (D14): in odd characteristic the Picard hypothesis can be removed in this model.
  - SA01-C12 (93/119): "H \ P_{P^1} is "le faisceau final"". **refutes**: MPL_93_092-134#40 (C04): t and t^2 on G_m are both local coordinates; the local sheaf is not final.
  - SA01-C14 (93/121): "G(t,s) = 0 implies s = g o t ("lisse/S ??", "à vérifier !")". **proves in part (the notes)**: MPL_93_092-134#43 (C07): holds over a characteristic-zero field; the relative hypotheses stay open.
  - SA01-C16 (93/114): "the developing equations lambda = -s''/s', G_t(s) = mu and the linearization". **proves**: MPL_93_092-134#29 (B12) and MPL_93_092-134#30 (B13), checked by hand.
- **Corrections:** 93/113: s' = c exp Lambda(t) -> s' = c exp(-Lambda(t)); 93/117: mod. matrices diagonales -> mod. matrices scalaires (H = PGL_2(C)); 93/102: D_{u_M(t)} = D_t -> c_{D_s} = c_{D_t} (the affine connections differ under inversion); 93/114: the pure-weight coordinate-change formula for G -> with the inhomogeneous term G_t(t~); 93/122: Pic(A) = 0 gives ad - bc = 1 -> false (s = 2t over F_5); in odd characteristic the Picard hypothesis can be drop.
- **Flags:** suspected misreading (2); a link across folders; suspected misreadings at 93/113, 93/117.
- **Other topics:** = H03D (SA04-7); SA03-14 (the Schwarzian on cote 93 scans 2-46).

### SA01-33: uniformization by the canonical projective connection: the three types, Möbius stabilizers and real forms, the canonical projective bundle from the universal cover, algebraicity of the uniformizing connection ("Sont-elles algébriques ?"), the thrice-punctured line, the affine and multiplicative cases (= H0JE)

- **Status on his pages:** sketched; open questions on the pages ("prouver (ou l'infirmer !)", "mais pas l'algéb. de c !"). **Kind:** programme/theorem (sketched).
- **Where:** cote 93, scans 36,101,110,114-115,121,126-127,129-132.
- **Notes (25 entries):** MPL_93_092-134 (25).
- **Notes files:** `inputs/SA01/pro/MPL_93_092-134_notes.md`.
- **Depends:** used by: SA01-34 (our note); uses: GAGA; Deligne, Équations différentielles à points singuliers réguliers, II.5.9 (our note), SA01-31 (his page), SA01-32 (his page).
- **Claims:**
  - SA01-C10 (93/126): "Theorem 1: a homogeneous simply connected Riemann surface is of the three uniformization types, as written ("homogène")". **refutes the wording; refines**: MPL_93_092-134#60 (E01): C* is homogeneous but neither simply connected nor of the three types.
  - SA01-C11 (93/126-127): "PGL_2(R) = SL_2(R)/{+-1} for the disc stabilizer". **refutes; refines**: MPL_93_092-134#61 (E02): false on real points; the stabilizer is the identity component.
  - SA01-C13 (93/115): ""Sont-elles algébriques ?": algebraicity of the uniformizing connection". **answers (the notes; not checked here)**: MPL_93_092-134#34 (B17): yes for a fixed finite-type complex curve (cusp uniformization, GAGA); MPL_93_092-134#33 (B16), MPL_93_092-134#85 (F06): not holomorphic in families.
  - SA01-C15 (93/130-132): ""prouver (ou l'infirmer !)": the formal data determine an algebraic realization". **refutes the naive form (the notes)**: MPL_93_092-134#70 (E11): x exp(w) has algebraic coefficients and a transcendental realization.
  - SA01-C17 (93/115): "the uniformizing coefficient of P^1 minus three points". **proves**: MPL_93_092-134#35 (B18): mu = -(z^2 - z + 1)/(z^2 (z-1)^2), checked against the classical formula.
- **Corrections:** 93/126-127: the homogeneity theorem and PGL_2(R) = SL_2(R)/{+-1} -> simply connected; the identity component.
- **Flags:** the LM/Dérivateurs lens (1); a link across folders.
- **Other topics:** = H0JE (SA32-2); related: H03E (SA04-8).

### SA01-34: the notes' arithmetic bridges for the cote 93 uniformization strand: Frobenius rigidity against p-curvature, Cartier descent, Gauss-Manin nilpotence (Katz), Kodaira-Spencer, the second fundamental form, the Legendre family, register item S20 (= H02J)

- **Status on his pages:** not his claim. **Kind:** comparison (the notes').
- **Where:** cote 93, scans 23,92,114-115,121.
- **Notes (7 entries):** MPL_93_092-134 (7).
- **Notes files:** `inputs/SA01/pro/MPL_93_092-134_notes.md`.
- **Depends:** uses: SA01-32 (our note), SA01-33 (our note).
- **Other topics:** = H02J (SA04-11).

### SA01-35: periods and the canonical connection in relative de Rham cohomology (cote 93, scans 221-236): operators on closed cochains, integrals between two sections, the Cartan formula, mu(a,b) computed algebraically (= H00B)

- **Status on his pages:** stated; (15) admitted ("l'admettrons"); scope questions ("spécial à car. 0 ?", "steinien"). **Kind:** construction.
- **Where:** cote 93, scans 221-223,230,236.
- **Notes (8 entries):** work:K93-13 (6); codex:K93-13 (2).
- **Notes files:** `codex_web_20261113/returns/K93-13/out/K93-13_mathnotes.md`; `codex_web_20261113/returns/K93-13/out/K93-13_notes.md`.
- **Depends:** related: SA01-31 (our note).
- **Flags:** a link across folders.
- **Other topics:** = H00B (SA04-12); H00C (SA04-13).

## The requested LM bridge (a question the notes put to the pages)

### SA01-2: the requested LM bridge B5: level-n regular maps, the Farey map on X(n) -> X(1), M_{0,5} and the five-point relation

- **Status on his pages:** not on the pages. **Kind:** research question put to the pages.
- **Where:** cote 72; cote 83, scans 3,22,27,58,66-67,74,119,402,570-571,573.
- **Notes (18 entries):** MPL_83_178-222 (16); MPL_72_035-081 (2).
- **Notes files:** `inputs/SA01/pro/MPL_72_035-081_notes.md`; `inputs/SA01/pro/MPL_83_178-222_notes.md`.
- **Depends:** uses: SA01-1 (our note).
- **Flags:** LM/Derivateurs lens (1); LM/Derivateurs lens.
- **Other topics:** LM (La Longue Marche, cote 140) and the research register (B5, LM4 F.7); SA02/SA03 if they hold the Farey/dessins material.

## Typescripts and documentary

### SA01-39: the EGA IV typescript reused in cote 90 (typed numbers IV-962; sections 17-18: henselization, strict localization) with pencil criticisms ("pas très clair", "Rédiger mieux") (= H01K)

- **Status on his pages:** typed; criticized in the margin. **Kind:** documentary/proposition (typescript).
- **Where:** cote 90.
- **Notes (4 entries):** work:K90-02 (2); codex:K90-02 (2).
- **Notes files:** `codex_web_20261113/returns/K90-02/out/K90-02_mathnotes.md`; `codex_web_20261113/returns/K90-02/out/K90-02_notes.md`.
- **Depends:** uses: EGA IV sections 17-18 (his page).
- **Flags:** a link across folders (1); a link across folders.
- **Other topics:** = H01K (SA02-11); EGA IV sections 17-18.

### SA01-42: documentary: EGA IV typescript leaves in cote 97 (pp. 17-23 with (4.43) left "au lecteur"; "IV-1102" with a note to move a passage to 21.2) and 1966 Collège de France and IHES letterheads (H97-01)

- **Status on his pages:** documentary. **Kind:** documentary.
- **Where:** cote 97, scans 2,8,19.
- **Notes (2 entries):** codex:H97-01 (2).
- **Notes files:** `codex_web_20261113/returns/H97-01/out/H97-01_notes.md`.
- **Other topics:** SA04-37 (cote 97); EGA IV section 21.

### SA01-37: documentary: the Récoltes et Semailles typescript leaves (pp. 475-478) under the mathematical leaves of cote 84 (K84-10) (= H01T)

- **Status on his pages:** documentary. **Kind:** documentary (non-mathematical text).
- **Where:** cote 84, scans 147.
- **Notes (3 entries):** work:K84-10 (2); codex:K84-10 (1).
- **Notes files:** `codex_web_20261113/returns/K84-10/out/K84-10_mathnotes.md`; `codex_web_20261113/returns/K84-10/out/K84-10_notes.md`.
- **Other topics:** = H01T (SA02-6).

### SA01-24: the reused and cancelled typescripts on the backs of cote 83 (SGA, the Grundlehren resignation, order and chaos, dreams)

- **Status on his pages:** documentary. **Kind:** documentary (non-mathematical text).
- **Where:** cote 83, scans 5,17,79,119,129,183,214,216.
- **Notes (33 entries):** MPL_83_178-222 (9); work:K83-03 (6); work:K83-06 (6); work:K83-10 (6); codex:K83-03 (2); codex:K83-06 (2); codex:K83-10 (2).
- **Notes files:** `codex_web_20261113/returns/K83-03/out/K83-03_mathnotes.md`; `codex_web_20261113/returns/K83-03/out/K83-03_notes.md`; `codex_web_20261113/returns/K83-06/out/K83-06_mathnotes.md`; `codex_web_20261113/returns/K83-06/out/K83-06_notes.md`; `codex_web_20261113/returns/K83-10/out/K83-10_mathnotes.md`; `codex_web_20261113/returns/K83-10/out/K83-10_notes.md` ....
- **Units (20):** K83-03.u01, K83-03.u02, K83-03.u03, K83-03.u04, K83-03.u05, K83-03.u06, K83-03.u07, K83-03.u08 ....

### SA01-7: documentary: page numbering, covers and reused typed sheets of cote 72 (thesis and council notices)

- **Status on his pages:** documentary. **Kind:** documentary.
- **Where:** cote 72, scans 35,42,48,60,64,66,70.
- **Notes (8 entries):** MPL_72_035-081 (8).
- **Notes files:** `inputs/SA01/pro/MPL_72_035-081_notes.md`.

### SA01-15: documentary: dates, marginal pagination and reused printer paper of cote 154, scans 46-76

- **Status on his pages:** documentary. **Kind:** documentary.
- **Where:** cote 81, scans 46,53,62.
- **Notes (7 entries):** MPL_81_038-055+154_046-076 (7).
- **Notes files:** `inputs/SA01/pro/MPL_81_038-055+154_046-076_notes.md`.
- **Other topics:** SA11 (same package).

### SA01-26: documentary: covers, folio sequences, headings and dates of cote 83

- **Status on his pages:** documentary. **Kind:** documentary.
- **Where:** cote 83, scans 22,119,147,182,245,255,402,570.
- **Notes (6 entries):** MPL_83_178-222 (6).
- **Notes files:** `inputs/SA01/pro/MPL_83_178-222_notes.md`.

### SA01-43: documentary: reused Montpellier thesis-defence notices of April 1977 (geology, chemistry) under cote 71

- **Status on his pages:** documentary. **Kind:** documentary.
- **Where:** cote 71.
- **Notes (2 entries):** codex:J71-01 (1); codex:J71-02 (1).
- **Notes files:** `codex_web_20261113/returns/J71-01/out/J71-01_notes.md`; `codex_web_20261113/returns/J71-02/out/J71-02_notes.md`.

## Reading questions and apparatus

### SA01-5: scan-local reading doubts of MPL 72 (signs, arities, exponents, subscripts)

- **Status on his pages:** reading questions. **Kind:** reading question.
- **Where:** cote 72, scans 52-53,61.
- **Notes (29 entries):** MPL_72_035-081 (29).
- **Notes files:** `inputs/SA01/pro/MPL_72_035-081_notes.md`.

### SA01-8: the notes' own apparatus for MPL 72 (scope, sources, context checks against Hua, reproduction)

- **Status on his pages:** apparatus. **Kind:** apparatus.
- **Where:** cote 72, scans 21-22,25,35,38,43,46,49-51,54,58-59,61,63,73-74,76-78,80-81,150,170,198,231.
- **Notes (21 entries):** MPL_72_035-081 (21).
- **Notes files:** `inputs/SA01/pro/MPL_72_035-081_notes.md`.

### SA01-30: the notes' apparatus for the packages first placed in sweep 2 (MPL_93_092-134: context, conventions, reading list; MPL_83_178-222 records)

- **Status on his pages:** apparatus. **Kind:** apparatus.
- **Where:** cote 83; cote 93.
- **Notes (4 entries):** MPL_93_092-134 (3); MPL_83_178-222:records:research_leads (1).
- **Notes files:** `inputs/SA01/pro/MPL_93_092-134_notes.md`; `returns/MPL_83_178-222_unzipped/.../research_leads.md`.

## Counts

- Items: 40; placed entries: 651.
- DEPENDS rows: 51; CLAIM_LINKS: 17; UNIT_LINKS: 138; CORRECTIONS: 13; part-2 check events: 3.
