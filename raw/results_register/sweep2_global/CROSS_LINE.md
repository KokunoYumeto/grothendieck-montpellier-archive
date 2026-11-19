# The links between lines, and what each makes possible

Claude Opus 5.5 at effort max (sweep 2), 18 Nov 2026. The lines:
- **the Longue Marche and the archive**, in two sweep-1 scopes: the tower and the sections;
- **Les Dérivateurs**, the homotopy line. PRETOT and TOTEX belong here, although the register files them under the
  Longue Marche;
- **S6**, which has its own tag space.

The counts come from `GRAPH_EDGES.tsv`:
- 3,159 edges between runs;
- 722 of them cross the sweep-1 scopes;
- 34 cross the lines, with PRETOT and TOTEX counted as Dérivateurs;
- none touches S6.

Cluster ids (SC..) refer to `CLUSTERS.tsv`.

## A. Les Dérivateurs and the Longue Marche

**1. Exit paths of the moduli tower (SC07).** RESIDUE H.3 and H.5, BISITE F.16 and STRATA F.11 come from the
Dérivateurs line; EXIT_TOWER C.2 and EXIT_ONE_TYPE P1e3 come from the Longue Marche.
- The two lines prove the same theorem about the forgetful functor of the entrance and exit categories of M̄_{g,n}. It
  is W_∞-proper for every stable (g, n), and W_∞-smooth only for (0, 3). Its lifting categories are contractible or
  BZ, and the BZ case is a contracted rational bridge whose node is smoothed.
- EXIT_TOWER's manuscript column cites RESIDUE H.3, and STRATA F's count of 26 objects for M̄_{0,5} is EXIT_ONE_TYPE
  P1e3.
- **What it makes possible:** the Lego of the tower (Part I.2) can be stated in the language of Part II. Properness
  makes the fibres of the forgetful maps compute homotopy fibres, and this is what the completed exit system of
  EXIT_TOWER E.42 needs, with GT̂ acting on it. In the handbook, one item serves both chapters (I.2 and IV.1).

**2. Stratified coefficients and glued topoi (SC09).** STRATA B.6, B.10, B.12 and C.3–C.8 come from the Dérivateurs
line; LM5 E.15 and F.30 from the Longue Marche.
- LM5 checks and extends STRATA's results on enhanced presheaf categories.
- LM5's geometric shape of a glued topos, the homotopy pushout along the genuine link, rests on STRATA's gluing along a
  sieve and its cosieve. STRATA C.7 (Refuted) serves as LM5's example of a lost mapping path.
- **What it makes possible:** the multi-Galois topoi of cotes 149 and 147 (Part I.4) rest on the stratified coefficient
  theory of Part II.

**3. Finite tests do not see the shift (SC08).** PATHS E.13, E.1 and CATHOT F.2 come from the Dérivateurs line; LM5
A.20 from the Longue Marche.
- One counterexample appears in both lines: the shift and the identity of the finitary symmetric group's classifying
  space. FINMON's report notes the same.
- **What it makes possible:** one item marks where finite tests stop, in Part II.4 (S² and finite tests: S2COUNT,
  CATHOT D.6) and in Part I.4 (finitely generated source tests on Galois topoi).

**4. The other cross-line edges.** There are 34; `tools/crossscope_edges.tsv` lists them, the scope pair being
derivateurs with tower or sections. Most are LM5's checks of STRATA and EXIT_TOWER's uses of RESIDUE. None carries a
status conflict.

## B. Between the two Longue Marche scopes (tower and sections)

These links decide the main questions. No sweep-1 agent saw both ends.

**5. Δ on GT̂ (SC01).**
- LM7_PUSH E.65 and E.3 are in the sections scope.
- The proofs of record are in the tower scope (EXIT_TOWER E.44, E.49; GT_TOWER_CHECK A.1, A.3, A.7) and back in the
  sections scope (SECTION_GHOSTS E.176–E.198).
- The two routes are independent in their finite-subgroup input: one uses Boggi–Zalesskii, the other the run's own
  fusion statement E.176 together with Hatcher–Lochak–Schneps's Λ. Both use the genus-one compatibility of the GT̂
  action.
- **What it makes possible:**
  - LM7_PUSH E.3 closes;
  - FERMAT_SUCCESSOR C.15 and LM4_SUCCESSOR A.13 (on GT̂) close;
  - the strict inclusions GT̂ ⊊ ker Δ ⊊ GT̂₀ hold, with two witnesses;
  - the open part narrows to two questions: C_L ⊆ ker Δ (LM8_PUSH C.8), and C_P ⊆ ker Δ (GT_TOWER_CHECK B.1).
- **What it costs:** one outside referee, for E.44 and for E.179–E.181, with a field check against Lochak–Nakamura–Schneps
  2026.

**6. The Fermat curves (SC02, SC05, SC06).**
- The same error, the cusp constant v₂(q) = −8, was found independently in both scopes. It is on record by 16 Nov 02:52
  (LM8_PUSH D.22, checkpoint 17) and by 16 Nov 06:49 (FERMAT_SUCCESSOR A.4, checkpoint 6). These are checkpoint times,
  not the times of discovery.
- It was repaired twice: LM8_PUSH D.23 and FERMAT_SUCCESSOR A.11.
- SECTION_GHOSTS E.100 (sections scope) strengthens LM7 E.25 (no section for even n), and it shows that the prompt's
  reading of the noncuspidal-section results of LM6, LM7 and LM8 (both scopes) overreached.
- **What it makes possible:** one theorem with two independent proofs (Part I.5), and a clean split between what is
  unconditional and what rests on the local theorem (gate G1).

**7. The p-adic local section theorem (SC03).**
- It is stated as a tool in the sections runs (LM6's Tool (1); FERMAT_SUCCESSOR A.20, A.31).
- It is re-derived in a tower run (LM8_PUSH D.54, D.56).
- **What it makes possible:** one item for Part I.4 that 73 rows can cite, so that their conditional status is visible
  in one place.

**8. The 149 chain and the cyclotomic kernel (SC16, SC17).**
- CYCLOTOMIC_KERNEL (tower) feeds ANABELIAN_149_PUSH (sections) through prompt row R15.
- LM6 F.13 confirms CYCLOTOMIC_KERNEL B8, his false formulas (32)–(33) at cote 149, scan 127. It also reduces
  ANABELIAN_149_PUSH D.U2 (the birational section conjecture for P¹/Q) to the nontriviality of a centralizer.

**9. LM7_PUSH's lifting theorems (SC20).**
- D.50 and E.58 are used by DELTA_ON_GT, GT_TOWER_CHECK, LM4_SUCCESSOR and FERMAT_SUCCESSOR, all as "refereed: proved
  as claimed" (by Claude Opus 5.5 at effort max, per the prompts' rows).
- They are reconstructed independently in SECTION_GHOSTS E.57.
- LM4_SUCCESSOR A.18 and B.54 show that they admit no unrestricted strengthening.

**10. Ghosts (SC21).**
- "Ghost" names two objects: section ghosts (SECTIONS_OVER_Q, GT_TOWER_CHECK Part C, SECTION_GHOSTS) and the GT̂₀
  element of EXIT_TOWER E.46.
- The handbook needs two names.

## C. Inside Les Dérivateurs: FINMON, which the register misses

**11. Finite models (SC11–SC15).**
- FINMON (695 rows, decoded checkpoint 20) closes or narrows four questions of other runs:
  - CATHOT G.17: the RP² poset minimum is 49, and K(Z,2) has no finite model;
  - CATHOT D.6: answered no, with S2COUNT;
  - RESIDUE A.5: extended through order 6.
- It carries the programme map's headline: the CP² monoid minimum is 23, and the category minimum lies in [17, 22].
- **What it makes possible:** a complete Part II.4.1 size table.
- Placement and merges: `FINMON_PLACEMENT.tsv` and `FINMON_MERGES.tsv`.

## D. S6

No edge joins S6 to the other lines. The statement-similarity pairs between S6 and the Longue Marche or the
Dérivateurs are coincidences of wording: "the theta identity" and "duplication steps". This agrees with the sketch:
S6 keeps its own tag space.
