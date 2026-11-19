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

## Sweep 2, part 1 (gap entries; Claude Opus 5.5 at effort max, a28ea31fa17dd65e1, horizontal sweep 2, 18 Nov 2026)

Entries placed: 302 (pro_notes 104, codex_sheet_notes 88, work_mathnotes 78, pro_records 32).
Basis: heading 148, folder-map 119, opening-read 26, opening-read (title sheet or reused typescript) 6, scan-overlap 2, entry-read 1.
New items: SA05-18 (motives over finite fields: the Weil-number protorus, the Ar), SA05-19 (Deuring's gerbes and norm categories: rank-one objects over ), SA05-20 (tensor categories and the tannakian formalism (cote 10, B se), SA05-21 (the Hodge group, the letter to Mumford (Algiers, 1 November ).
Flags added: 3. Check events added: 1.

Basis words in PLACEMENT (sweep 2):
- heading: placed from the heading alone (title sheets, dates and page counts go to the documents item);
- opening-read: I read the entry's opening (about the first 14-30 words), and the deciding words are in it;
- body-keyword: placed by a keyword rule that matched further into the entry, which I did not read there;
- folder-map: the entry's folder covers the same pages as a sweep-1 Work folder, placed under that folder's item;
- scan-overlap: the same cote and scan as sweep-1 placements of the topic;
- entry-read: I read the whole entry; passage-read: I read the passage on the scan.
Fidelity is assessed only for entry-read and passage-read rows.

What the gap list added to SA05:
- MPL_12_150-168+15_002-033 (104 Pro notes, new to the register): the headings say what each note is about and their prefixes give the clusters. M (cote 12, scans 150-167: the construction of the category of motives, effectivity, projectors, Kunneth, Tate inversion, the niveau decomposition, positivity, Nori-Ayoub and Andre) goes to SA05-12, with the niveau notes to SA05-9, the positivity notes to SA05-11, the lettering note to SA05-2 and the Nori-Ayoub-Andre notes to SA05-8. FF (cote 15, scans 2-14) and D (scans 16-32) are two new items, motives over finite fields and Deuring's gerbes. R notes follow their witness scans.
- The Work and Codex notes of the K folders follow the sweep-1 folder map, extended to the new folders by their 'What the pages do': K14-01 (structure of effectivity) and K12-09 to SA05-12; K14-07 (the graph of a homomorphism) to SA05-1; K15-09 and K18-03 (archimedean fibres, two conjugations) to SA05-10; K16-01 and K16-03 (grading by projectors, Hodge algebras, L and Lambda) to SA05-16; K16-04 (a letter to Coates on the index conjecture) to SA05-11; K18-02 (distributions and tangent maps) to SA05-4; the reused typescripts and papers K15-03 (reflexive modules, VI.5), K15-04 (maps of ringed spaces), K15-10 (invariant forms), K18-01 (papers and bibliography, Saavedra), K18-04 (valuations) to SA05-17.
- New Codex folders: B10-01 to B10-03 (sections 10-11 of a group-scheme text: projective limits, affine group preschemes) join SA05-4; B10-04 to B10-10 are a new tannakian item; H13-01 and J13 (the letter to Mumford, the Hodge group, double lattices) a new item. B12-01 and B12-02 (cote 12, 'Exemples 7.5.3', 'le plus important probleme reste ...') are placed by the scans they cite, else SA05-17; their subject is not identified from the openings.
- MPL_15_139-194 research leads (31, cote 15, scans 139-178; that package's notes are in no sweep-1 table): scans 139-168 (tori over Weilian fields, the connected group S_K^0 = T_K/R, CM structures and CM bimodules, the characters psi_Sigma, fibre functors to Hodge objects) join SA05-8; scans 172-178 ('Calculs de cohomologie absolue des Motifs de Tate Z(n)', with self-flagged '=0?' and '[est-on nul ??]') join SA05-10; the covers (157: 'Corps de classes commutatif = Motifs a groupe fondamental motivique connexe commutatif'; 172) and the reused typescript leaves n. 413 go to SA05-17.
- For part 2: codex:B10-02#1 records a circled handwritten 'fausse Formule' beside the canonical-map formula of Lemma 11.1 (cote 10, scan 43), on the group-scheme text.
