# SA19 Jacobiennes: horizontal sweep 1

By Claude Opus 5.5 at effort max (agent a28ea31fa17dd65e1), 18 Nov 2026. The notes are by GPT-6 Astra (ChatGPT Pro mode)
for the Pro packages and by GPT-6 Astra in Work/Codex-web for the math notes. Scripts: `../SA16/tools/hsweep.py`,
`../SA16/tools/clusters_SA19.py`.

## What the notes cover

- **Cote 43** (MPL_43_094-142, 89 entries; Work K43-01..10, 60 units):
  - generalized Jacobians and geometric class field theory (modulus, norms, reciprocity, idèles);
  - a long duality programme for commutative group schemes over local fields and curves (sites, Ext groups,
    Cartier-Serre-Pontryagin, supports, completions; most steps flagged by him as open);
  - local cohomology and local relative Jacobians;
  - formal groups and Witt rings;
  - reused typescripts on homotopy (Thom complexes), Stiefel manifolds, flatness and multiplicities, and sheaves.
- **The shared package MPL_16+47+54+44** (85 entries) is placed with the same items as in SA18 (SA19-11..14 and SA19-20
  are SA18-11..14 and SA18-20).
- **The planning question of the "1983 bridge"** (section 1 of the cote 43 package) and the "second Fourier witness" are
  research-run questions put by the prompts. The notes answer them; they are not the pages' own subject.

## Items, light and heavy

There are 13 items.

- **Heavy:** SA19-2, duality for group schemes (44 entries); SA19-1, generalized Jacobians and class field theory (29).
- **Light:** SA19-7, classification and gluing (6); SA19-20, orbits (5).

## Counts

- **Entries:** 234 = 174 Pro entries + 60 Work units.
- **Basis:** 172 index-row, 60 entry-read, 2 passage-read.
- **Fidelity of the passage reads:** 2 agree.
- **Flags:** 3 (1 suspected misreading, 2 links across folders).
- **Check events:** 1.
- **Scans:** 12 Pro entries have index scans that differ from the note's Source field.

## What sweep 2 should look at first

1. **Cote 43, scan 110 (transcription line 753): "Si l'inégalité est vérifiée, alors F est plat."**
   - This is false as written. R06's counterexample is R ⊕ k over k[[t]]: fibre lengths 2 and 1, and the module is not
     flat. I checked it.
   - Equality of the lengths is the right condition, and the page continues "on ne peut avoir égalité" (line 768).
   - Either the ink reads "l'égalité" or the slip is his. The displayed sign is itself uncertain (≥ or >). Decide on the
     scan.
2. **The duality programme D01-D29.** Nearly every step is self-flagged. It needs one statement of the intended
   theorem, the duality of commutative group schemes over a local field or a curve with supports, in today's terms, and
   then a check against Milne's *Arithmetic Duality Theorems* III.
3. **The cote 47/44 questions** (SA19-3) duplicate SA18-5, SA18-13 and SA18-14. Give them one global object.
