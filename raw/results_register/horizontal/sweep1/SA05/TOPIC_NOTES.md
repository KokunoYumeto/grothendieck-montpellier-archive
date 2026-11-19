# SA05 Théorie des motifs (part 1: cotes 11, 12): horizontal sweep 1

By Claude Opus 5.5 at effort max (agent a28ea31fa17dd65e1), 18 Nov 2026. The notes are by GPT-6 Astra (ChatGPT Pro mode)
for the Pro packages and by GPT-6 Astra in Work/Codex-web for the math notes. Scripts: `../SA16/tools/hsweep.py`,
`../SA16/tools/clusters_SA05.py`.

## The provisional Pro dossier (first reading)

SA04_v1_final (GPT-6 Astra, ChatGPT Pro mode, 13:35 UTC) has the same five packages and 380 entries as SA05. It is a
scaffold:

- every verdict is "pending";
- there is one item per entry and no merge;
- the claims, problems, readings and links files are empty.

What it adds are the Codex leads B12-01 and B12-02:

- scan 123: Deligne's theorem "modulo a Lefschetz theorem", the word uncertain;
- scan 134: "référence introuvable !!" after cos(π/3) = 1/2.

Nothing in it was used as a basis.

## What the notes cover

- **Cote 11** (MPL_11_002-042; with the shared MPL_11_043-058+56; Work K11-01..04):
  - Grothendieck's formalism of correspondences, the category V^A with Hom(X, Y) = A(X × Y), with his sign and
    centrality warnings;
  - the draft and printed lettering of the standard conjectures;
  - the cohomology of quadrics;
  - a cancelled group-scheme text;
  - Delzant's offprint;
  - a reused typescript on spherical buildings (Tits's centre conjecture).
- **Cote 12** (three Pro packages; Work K12-01..09):
  - the motivic Galois group (fibre functors, the exact sequence over Q, periods);
  - weights and levels;
  - absolute cohomology and the arithmetic finiteness conjectures (Tate, BSD, Sha);
  - positive forms and semisimplicity;
  - abstract motives (pseudo-abelian envelope, projectors);
  - smooth integral motives over a base;
  - linear against nonlinear statements.

## Items, light and heavy

There are 16 items.

- **Heavy:**
  - SA05-1, correspondences (110 entries);
  - SA05-9, weights and levels (66);
  - SA05-10, absolute cohomology and arithmetic (43);
  - SA05-8, the motivic Galois group (35);
  - SA05-3, quadrics (35, shared with SA18).
- **Light:**
  - SA05-14, linear against nonlinear (8);
  - SA05-15, Oda (5);
  - SA05-16, cote 16 programme (4).

## Counts

- **Entries:** 458 = 380 Pro entries + 78 Work units.
- **Basis:** 329 index-row, 129 entry-read (the 49 coded cote 11 notes H01-H20, MB01-MB13, CL, RQ and O, plus the Work
  units).
- **Flags:** 9.
- **Check events:** 1.
- **Scans:** 35 Pro entries have index scans that differ from the note's Source field.

## What sweep 2 should look at first

1. **W21, cote 12, scan 115.**
   - The level bound reads "2(n − i + j)". It fails on an elliptic curve (level 0 against level 1; I checked it), while
     "2n − i + j" of scan 108 (Hua's reading) passes.
   - Decide on the scan whether the parentheses are ink.
2. **M08, cote 12, scan 148.** Our "Tout morphisme u: P → Q est 'direct'" against Hua's account (first monomorphisms,
   then corrected).
3. **N037 against N041 (cote 12).** The pages give a nonzero degree-two term for the constant Jacobian, and later a
   vanishing that contradicts it.
4. **SA05-1.** The correspondence formalism of cote 11 is the foundation for SA06 and SA07, and it is SA18-15. Give it
   one global object and one statement in today's terms: the category of correspondences of a Weil-type cohomology with
   Künneth and Poincaré duality.
