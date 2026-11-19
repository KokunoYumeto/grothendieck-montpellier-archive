# SA01 Géométrie et topologie combinatoire: topic notes (horizontal sweep 1)

Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, 18 Nov 2026.

## What the notes cover

**Heavy nodes:** three Pro packages (GPT-6 Astra, ChatGPT Pro mode).

| Package | Entries | Pages | Subject |
|---|---|---|---|
| MPL_72_035-081 | 119 | cote 72 | Regular polyhedra over a ring: rank-one operators, the invariant quadratic form, characteristic two, determinant and continuant calculations |
| MPL_81_038-055+154_046-076 | 116 | in fact only cote 154, scans 46-76 | The surface of relative positions of an added pseudoline: local gluing, dihedral monodromy and the parity character, four natural-map schemes |
| MPL_83_178-222 | 97 | cote 83 | Lambda-split extensions; rank-four Azumaya algebras and trace identities for 2x2 matrices; the trace cube of four matrix variables; reused autobiographical typescript |

**Light nodes:**
- 21 Work math-notes files on cotes 72 (K72-01 to K72-07) and 83 (K83-01 to K83-14), 126 units in all;
- 54 non-empty Codex stage-A note units, including J81 (cote 81, immersions of the disc).

## Main objects and clusters

| Item | Object |
|---|---|
| SA01-1 | Pinned regular realizations |
| SA01-3 | The invariant form and the conic |
| SA01-4 | Determinant recurrences |
| SA01-9 to SA01-12 | The pseudoline surface |
| SA01-16 | Bi-icosahedra |
| SA01-17 | Lambda-split extensions |
| SA01-18 to SA01-20 | Azumaya algebras, traces, invariants |
| SA01-21 and SA01-22 | The cube and its determinants |
| SA01-27 and SA01-28 | Icosahedral matrices; quadratic algebras (Work only) |

The documentary and apparatus items are SA01-7, 8, 15, 24 and 26.

Much of the Pro notes answers questions that the prompts asked through La Longue Marche (SA01-2, SA01-23). MPL 83's own Q01 says the leaves contain no level-n polyhedron, no map X(n) -> X(1) and no five-point relation.

## Counts

| Measure | Value |
|---|---|
| Rows | 512 (332 index entries, 126 Work units, 54 Codex units) |
| Items | 26 |
| Basis | 502 index-row, 8 entry-read, 2 passage-read |
| Fidelity of the passage reads | both agree |
| Flags | 8 |
| Check events | 5 |

## Checks made

- **83/219.** The block determinant is 512 for the transcribed matrix, not his 27^2 - 1 = 728. Pro (C19) and Work (K83-14) found this independently, and Hua XIII had it first.
  - With +1 in the overwritten corner the determinant would be 384 = 2^7 x 3. That contradicts his "premier à 3", so the conclusion favours the reading -1.
- **The trace identity.** With the reconstructed variable meanings, tr(xyz)tr(xzy) equals his Pi minus 4cc'c''. It holds on 300 random integer triples, which confirms A11 (credited to Hua XII-XIII).
- **72/036.** The trigonometric line is inconsistent as transcribed. Pro A15 and Work S36 both found this.

## What sweep 2 should look at first

1. The six Work folders that re-read Pro pages: K72-03 to K72-05 and K83-12 to K83-14. They give two readings of the same pages; compare them page by page.
2. The suspected misreading at 72/036 ("+1" or "-1" in 2cos^2 theta_i ± 1).
3. The pseudoline package. It is cote 154 and belongs with SA11. Its items SA01-9 to SA01-12 are the same objects as SA11's.
4. Separate what is on the pages from the LM questions put to them (SA01-2, SA01-23).

## Sweep 2, part 1: the gap entries (18 Nov 2026)

Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8. There were 139 gap entries; all are placed, as 14 new items (SA01-30 to SA01-43) and two more entries in SA01-29.

**What came in:**
- **MPL_93_092-134, 90 Pro notes on cote 93, scans 92-134.** NOTES_INDEX had missed this package. It fills the gap between MPL_93_047-091 (SA04) and MPL_93_221-236 (SA04). Its strands:
  - projective connections on a relative curve (SA01-31, = H03F);
  - the Schwarzian G, its cocycle and the integral invariant G_0 with G = 12 G_0 in characteristics 2 and 3 (SA01-32, = H03D);
  - uniformization by the canonical projective bundle and the algebraicity questions (SA01-33, = H0JE);
  - the notes' own Gauss-Manin, Cartier and p-curvature bridges (SA01-34, = H02J).
- **Codex notes on the sheets for new cotes:**
  - cote 71: C. Contou-Carrère's manuscript on the Jordan theorem and three good vertices of a plane polygon (15 July 1976), on the backs of April 1977 thesis notices (SA01-40, SA01-43);
  - cote 75: the DEA course "Géométries combinatoires" (C4, 24 pp.; SA01-41);
  - cote 97: EGA IV typescript leaves and 1966 letterheads (SA01-42);
  - cote 81: J81-03, which is empty.
- **Work and Codex notes on folders whose objects are SA02's and SA04's:**
  - K84-10: chi-trivialised extensions (= H01R), with the Récoltes et Semailles typescript (= H01T);
  - K90-02: KG(X) over a Dedekind ring (= H01J), with the EGA IV henselization typescript and its pencil criticisms (= H01K);
  - K93-13: periods and the canonical de Rham connection (= H00B, H00C).

**Basis:**
- 135 entry-read. For the 90 Pro notes this means the opening of each entry (source, kind and claim); the Codex and Work entries were read in full when short.
- 4 passage-read, all agreeing with the frozen transcription: 93/095, 93/100, 93/113, 93/117.

**Checks (9):**
- Five of the notes' claims, checked by computation, all agree: G = 12 G_0 (D01); the Frobenius constants A[t^p], A[t^4], A[t^9] (D04); the developing-map system (B12); the linearization u'' = (mu/4)u (B13); the thrice-punctured-line coefficient (B18).
- Four notes checked against the transcription.

**Flags (9):**
- Three suspected misreadings or slips, passage-read:
  - 93/100: + b where + b f is needed;
  - 93/113: the sign of the exponent;
  - 93/117: "diagonales" for scalars.
- One further list of reading questions.
- Four links across folders.
- One LM-lens test, on 93/101.

**What part 2 should take from here:** the merge of SA01-31 to SA01-35 with SA04-7, -8, -9, -11, -12, -13 and SA03-14, which joins the cote 93 uniformization strand into one place; the three suspected misreadings; and the notes' own results in D07-D14 (rigidity with nilpotents, descent, the Picard hypothesis removed in odd characteristic), which are unchecked here.
