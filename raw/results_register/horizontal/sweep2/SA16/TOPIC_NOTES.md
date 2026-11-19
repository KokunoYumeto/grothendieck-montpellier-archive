# SA16 Courbes elliptiques: horizontal sweep 1

By Claude Opus 5.5 at effort max (agent a28ea31fa17dd65e1), 18 Nov 2026. The notes are by GPT-6 Astra (ChatGPT Pro mode)
for the Pro packages and by GPT-6 Astra in Work/Codex-web for the math notes. Scripts: `tools/hsweep.py`,
`tools/clusters_SA16.py`.

## What the notes cover

- **Cote 62** (MPL_62_002-050, 103 entries):
  - the Weierstrass model of a relative elliptic curve: pole filtration, Riemann-Roch, cohomological flatness and the cubic
    embedding;
  - the discriminant and the modular invariant;
  - the λ-line with its S₃ action and the Z/3 and Z/2 quotient stages;
  - trisections, S₃-torsors and Brauer-Severi curves;
  - a reused algebra typescript on completion (Artin-Rees, strict maps) and on valuations;
  - a comparison with Oda's de Rham/Dieudonné paper.

  Work notes K62-01..03: the classical analytic theory (℘, ζ, σ, θ, sn/cn/dn, the Hermite formula) and the
  completion typescript.
- **Cote 63** (Work K63-01, K63-02; no Pro package): the formulary of invariants, smoothness, small characteristics,
  weights, forms and periods, and divisors on the modular site.
- **Cote 64** (four Pro packages, 263 entries): moduli in characteristic ≠ 2.
  - Level 2 and level 4 as an octahedral configuration on P¹ with S₄ symmetry: orientation torsors, faces, Sylow counts,
    the characteristic-5 exception.
  - Four-pointed lines, the Klein cover and the doubling map.
  - The Legendre pinning (épinglage de Legendre), left unfinished by him on scans 118-126.
  - The transcendental approach: E = C/lattice and the universal cover of M₁,₁.
  - The modular cusp and congruence levels.
  - Connections (Gauss-Manin, Cartier).
  - Normality of quadratic extensions.

## Items, light and heavy

There are 19 items in OBJECTS.tsv.

- **Heavy:**
  - SA16-9, level structures (77 entries);
  - SA16-12, the transcendental theory (72);
  - SA16-2, Weierstrass equations, discriminant, invariant (29);
  - SA16-10, the Legendre pinning (23).
- **Light:**
  - SA16-8, Oda (2);
  - SA16-18, planning questions (2);
  - SA16-19, exceptional j-values (4).

## Counts

- **Entries:** 396 = 366 Pro entries + 30 Work units.
- **Basis:** 362 index-row, 33 entry-read, 1 passage-read.
- **Fidelity of the passage read:** 1 understates.
- **Flags:** 26. 21 are the LM lens (planning questions B5, S20 and the "LM context", put to cote 64 by the prompts); 2 note
  overstates or misreads the page; 1 same thing with different statements; 2 links across folders.
- **Check events:** 4.

## What sweep 2 should look at first

1. **The modular invariant on cote 62.**
   - B03 leaves open what scan 019 settles. The first display, −27c²/(b³ − 27c²) = j, gives the boxed
     b³/c² = 27(j − 1)/j. The line "b³/c² = j" is the slip, and c = 27(j − 1)/j is the case b = c.
   - B04 judges a discriminant against x³ + bx + c, while the sheet works with y² = 4x³ − bx − c.
   - Fix one normalization in the handbook. Cote 62 uses two: 1 − J/1728 on scans 019, 023 and 040, and the classical J
     on scan 025.
2. **The 21 LM-lens notes** on cote 64 (B5, S20, "LM context") are answers to the prompts' planning questions, not
   readings of the pages. Read cote 64 on its own terms: level structures and pinnings.
3. **Scans in NOTES_INDEX.** In 147 of the 366 Pro entries the index's `scans_cited` differs from the note's own Source
   field; it picks up context scans of other cotes (for example B03: index "54", Source "scan 019"). PLACEMENT.tsv uses
   the Source scans. The list is in `_index_scan_mismatch.txt`.
4. **The unfinished Legendre pinning** (L01-L92, U01-U02: "Dieu sait comment — il faudra … y revenir") and the
   characteristic-5 exception (RN014: in characteristic 5 the octahedral divisor is all of P¹(F₅), with stabilizer
   PGL₂(F₅) ≅ S₅) are the mathematical cores of cote 64.

## Sweep 2, part 1 (gap entries; Claude Opus 5.5 at effort max, a28ea31fa17dd65e1, horizontal sweep 2, 18 Nov 2026)

Entries placed: 70 (pro_records 42, codex_sheet_notes 28).
Basis: scan-overlap 30, heading 14, opening-read 12, folder-map 10, entry-read 4.
New items: SA16-20 (congruences for the coefficients of modular forms and congru), SA16-21 (Mordell-Weil, minimal models and reduction of elliptic curve), SA16-22 (elliptic curves with complex multiplication over Q: the clas).
Flags added: 2. Check events added: 1.

Basis words in PLACEMENT (sweep 2):
- heading: placed from the heading alone (title sheets, dates and page counts go to the documents item);
- opening-read: I read the entry's opening (about the first 14-30 words), and the deciding words are in it;
- body-keyword: placed by a keyword rule that matched further into the entry, which I did not read there;
- folder-map: the entry's folder covers the same pages as a sweep-1 Work folder, placed under that folder's item;
- scan-overlap: the same cote and scan as sweep-1 placements of the topic;
- entry-read: I read the whole entry; passage-read: I read the passage on the scan.
Fidelity is assessed only for entry-read and passage-read rows.

What the gap list added to SA16:
- The 42 research leads of MPL_62_002-050 restate the Pro notes scan by scan; they are placed with the sweep-1 item of the same scan (scan-overlap), the title sheet under SA16-17, and the reused typescripts under SA16-6 (completion, filtered modules) or SA16-7 (valuations, n. 272).
- The Codex sheet notes on K62/K63 follow the sweep-1 Work folders (SA16-12, SA16-2).
- The H63 series is new: other authors' typescripts kept in cote 63. Three new items: Atkin's congruence typescripts, an English typescript on Mordell-Weil and minimal models, a French typescript with the CM table. The Tate-Deligne Formulaire (two versions) joins SA16-2.
- Dating evidence (mine, from the notes, not checked on the scans): the CM typescript (H63-08, scans 78-81) says the integrality of the Frobenius eigenvalues on H^i(X, Z_l) and |alpha| = q^(i/2) are not proved, and lists the class-number-one discriminants with "plus peut-etre une autre valeur" after 163, so it was written before Stark and Baker (1966-67).
- The K62-02 Codex note finds no self-marked step; nothing beyond SA16-12.
- Which typescript is by whom rests on the title sheets the Codex notes transcribe; the Mordell-Weil typescript has no title in the notes.
