# SA18 Variétés abéliennes: horizontal sweep 1

By Claude Opus 5.5 at effort max (agent a28ea31fa17dd65e1), 18 Nov 2026. The notes are by GPT-6 Astra (ChatGPT Pro mode)
for the Pro packages and by GPT-6 Astra in Work/Codex-web for the math notes. Scripts: `../SA16/tools/hsweep.py`,
`../SA16/tools/clusters_SA18.py`.

## What the notes cover

The topic is broader than abelian varieties. Its four Pro packages hold group schemes, quadratic forms, motives and
quadrics as much as abelian varieties.

- **Cote 45** (MPL_45_033-080):
  - hyperalgebras, deformations and Lie cohomology of group schemes;
  - forms of tori and nonabelian H¹;
  - quadratic and bilinear forms;
  - reused sheets.
- **Cote 46** (MPL_46_002-048):
  - twisted torsors and Lang's theorem;
  - relative Frobenius and Verschiebung;
  - Picard p-torsion through Cartier duality and restricted Lie algebras;
  - étale sheaves;
  - Brauer-Severi schemes and descent.
- **Cotes 16, 47, 54, 44** (MPL_16+47+54+44, shared with SA19 and SA07):
  - integral models and local duality;
  - abstract Lefschetz algebras and the standard conjectures;
  - the Fourier transform of abelian varieties (cote 47);
  - abelian duality, the universal extension and the seven theorems on intermediate Jacobians (cote 44);
  - orbit calculations (cote 16).
- **Cote 11** (MPL_11_043-058+56, shared with SA05):
  - correspondence rings and tautological classes;
  - the cohomology of quadrics;
  - a cancelled group-scheme text on reductive centres, maximal tori and the Weyl group;
  - Delzant's signed offprint on the Witt ring and Stiefel-Whitney classes.
- **Work** (13 files on cotes 45, 46, 49-52, 54-56):
  - the Picard functor of an abelian scheme and its automorphisms (cotes 49-52);
  - the universal extension (cote 54);
  - Stein spaces (cote 55);
  - quadrics (cote 56).

## Items, light and heavy

There are 20 items in OBJECTS.tsv.

- **Heavy:**
  - SA18-16, the cohomology of quadrics (47 entries);
  - SA18-2, forms of tori and reductive groups (44);
  - SA18-15, correspondences and motives (34);
  - SA18-3, quadratic forms (33);
  - SA18-17, the Picard functor of abelian schemes (30, all Work).
- **Light:**
  - SA18-20, orbit calculations, cote 16 (5);
  - SA18-9, étale sheaves (7).

## Counts

- **Entries:** 425 = 335 Pro entries + 90 Work units.
- **Basis:** 333 index-row, 90 entry-read (the Work units), 2 passage-read.
- **Fidelity of the passage reads:** 2 agree.
- **Flags:** 6. 3 are the LM lens (references to the research register, the "Kummer run" and "WG H9"); 2 links across
  folders; 1 reading that differs from Hua's.
- **Check events:** 3.

## What sweep 2 should look at first

1. **N61, cote 46, scan 047: mono or epi.**
   - Our reading is an inserted "mono" ("un monomorphisme P̌ → P(Q), je dis que c'est un isom sur un P(E)"); Hua prints
     "épimorphisme".
   - The mathematics favours "mono" for the morphism of schemes, an immersion onto P(E). It corresponds to the module
     epimorphism Q → E, which may be what Hua's arrow records.
   - Decide it on the scan.
2. **N32, cote 46, scan 021.** The displayed injection R*/O* → Ω¹(K)/Ω¹(O) is false as written, since dlog of a p-th
   power vanishes. The page's own condition f = gᵖh names the missing quotient by p-th powers. Checked; the note agrees.
3. **Packages shared between topics.**
   - MPL_16+47+54+44 is under SA18, SA19 and SA07, and MPL_11_043-058+56 under SA18 and SA05. The same items are used in
     each topic.
   - The broad agent should give them one global tag each, in particular the Fourier transform (SA18-13), the Lefschetz
     algebra (SA18-12) and the cohomology of quadrics (SA18-16).
4. **The carry questions** (SA18-5: the second Fourier witness and the earlier forms of the seven Jacobian theorems) are
   asked in three packages. They are planning questions, not readings of the pages.
