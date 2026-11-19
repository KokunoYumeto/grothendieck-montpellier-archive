# SA14 Picard: horizontal sweep 1

By Claude Opus 5.5 at effort max (agent a28ea31fa17dd65e1), 18 Nov 2026. The notes are by GPT-6 Astra (ChatGPT Pro mode)
for the Pro packages and by GPT-6 Astra in Work/Codex-web for the math notes. Scripts: `../SA16/tools/hsweep.py`,
`../SA16/tools/clusters_SA14.py`.

## What the notes cover

- **Cote 57** (three Pro packages, 233 entries; Work K57-01..10):
  - the Picard functor: existence and properness (Seshadri's argument, rigidification, descent, finiteness, Igusa's
    inequality);
  - the universal vector extension with connection;
  - Lefschetz restriction to hyperplane sections;
  - the analytic criterion, formal Picard groups and GAGA;
  - local Picard groups of punctured spectra;
  - Néron-Severi and its specialization;
  - gluing and pinching;
  - the theorem of the cube (Work).
- **Cote 58** (85 entries; Work K58-01, -02): the Lefschetz comparison of SGA 2 type (connectedness, depth, effectivity,
  formal comparison), cones and local Picard groups.
- **Cote 60** (139 entries): L-functions of ℓ-adic sheaves on curves over finite fields (determinants, functional
  equations, ε-factors, weights, boundary terms, local constants), and reused commutative-algebra typescripts (Fitting
  ideals, reflexive modules).
- **Cote 59** (Work K59-01, -02, no Pro package): sections of torsors, determinants of perfect complexes, the Weil sheaf.

## Items, light and heavy

There are 15 items.

- **Heavy:**
  - SA14-10, L-functions (115 entries);
  - SA14-3, Lefschetz for Pic (67);
  - SA14-4, existence and properness of Pic (55);
  - SA14-1, carry questions (41: planning questions, not page readings).
- **Light:**
  - SA14-8, gluing and pinching (16);
  - SA14-16, links to the research register (16);
  - SA14-14, cote 59 (12).

## Counts

- **Entries:** 524 = 440 Pro entries + 84 Work units.
- **Basis:** 437 index-row, 86 entry-read, 1 passage-read.
- **Fidelity of the passage read:** 1 agrees.
- **Flags:** 9 (5 LM lens or research register, 2 links, 1 reading against Hua, 1 page error).
- **Check events:** 1.

## What sweep 2 should look at first

1. **Cote 60, scan 064, typescript exercise 10 f.**
   - The page prints d_k(M/N) ⊂ d_k(M). For the Fitting ideals d_k = Fitt_k (its own definition) the inclusion is the
     other way round (Stacks 07ZA(5)). The note A02 is right; I checked it with M = A, N = aA.
   - On the scan: is the typed symbol ⊃?
2. **SA14-10, L-functions on cote 60.** This is a large, self-contained piece on the functional equation with ε-factors.
   It belongs with the Weil-conjecture material of the motives topics (SA05-SA07), not with Picard. The sign and
   normalization questions (F19, LF10, LF14) should be checked as one set.
3. **SA14-1** (41 entries) is the carry-question layer: the Fourier check of cote 47 and the seven theorems of cote 44.
   It is the same object as SA18-5 and SA19-3.
4. **P04, MPL_57_226-270#41.** Hua's reading reverses the direction of a global-projectivity example. Decide on the
   scan.
