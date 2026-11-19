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
