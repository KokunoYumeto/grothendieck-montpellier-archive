# SA07 Théorie des motifs (part 3: cotes 15, 18, 10, 16, 19): horizontal sweep 1

By Claude Opus 5.5 at effort max (agent a28ea31fa17dd65e1), 18 Nov 2026. The notes are by GPT-6 Astra (ChatGPT Pro mode)
for the Pro packages and by GPT-6 Astra in Work/Codex-web for the math notes. Scripts: `../SA16/tools/hsweep.py`,
`../SA16/tools/clusters_SA07.py`.

## What the notes cover

- **Cote 15, scans 195-228, and cote 18** (MPL_15_195-228+18_002-017, MPL_18_018-062):
  - reconstruction of varieties and places from motivic fibre functors (the place-to-torsor map, motivic rigidity);
  - periods: the period torsor, and on cote 18, scan 059, his "conjecture de transcendance N° 1" (the genericity of the
    period point; read and confirmed), with a strong and an elliptic period conjecture;
  - cycle classes and comparison maps;
  - real structures and Hodge theory;
  - correspondence rings and motivic groups;
  - reused Lie-theory typescripts;
  - a register of 36 steps he marks as unverified.
- **The shared package MPL_16+47+54+44** (85 entries): SA07-11..14 and SA07-20 are SA18-11..14 and SA18-20.
- **Work:**
  - cote 10: polarizations and Weil forms; operations on representation rings;
  - cote 16: Lefschetz elements and local Picard groups;
  - cote 19: a homological formalism of derived functors, extraordinary inverse images and gluing data.

## Items, light and heavy

There are 19 items.

- **Heavy:**
  - SA07-2, periods (59 entries);
  - SA07-5, reused Lie theory (46);
  - SA07-1, reconstruction from fibre functors (44);
  - SA07-18, the homological formalism of cote 19 (36, Work);
  - SA07-10, his unverified steps (36).
- **Light:**
  - SA07-4, linear against nonlinear (5);
  - SA07-17, cote 16 (6).

## Counts

- **Entries:** 423 = 339 Pro entries + 84 Work units.
- **Basis:** 338 index-row, 84 entry-read, 1 passage-read.
- **Fidelity of the passage read:** 1 agrees.
- **Flags:** 8 (4 links, 4 LM lens).
- **Check events:** 1.

## What sweep 2 should look at first

1. **The period conjecture in his own notes.**
   - On cote 18, scan 059, he writes "la conjecture de transcendance N° 1" as the genericity of the period point on the
     torsor P_{v,k}. I read it on the page. Strong and elliptic forms appear elsewhere (P15, P22, P25).
   - This is the documentary core for the history of Grothendieck's period conjecture. Collect all the witnesses into
     SA07-2 with exact lines.
2. **SA07-1, reconstruction from fibre functors at places,** is the motivic counterpart of the anabelian question of
   points as sections. Record it as a link to that line, not as a lens.
3. **The 36 author-marked steps on cote 18** (SA07-10) are indexed by location only. Attach each to its object.
4. **The shared package** needs one global tag per object with SA18 and SA19.

## Sweep 2, part 1 (gap entries; Claude Opus 5.5 at effort max, a28ea31fa17dd65e1, horizontal sweep 2, 18 Nov 2026)

Entries placed: 92 (pro_chatB 64, codex_sheet_notes 28).
Basis: opening-read 55, heading 23, folder-map 14.
New items: none.
Flags added: 0. Check events added: 1.

Basis words in PLACEMENT (sweep 2):
- heading: placed from the heading alone (title sheets, dates and page counts go to the documents item);
- opening-read: I read the entry's opening (about the first 14-30 words), and the deciding words are in it;
- body-keyword: placed by a keyword rule that matched further into the entry, which I did not read there;
- folder-map: the entry's folder covers the same pages as a sweep-1 Work folder, placed under that folder's item;
- scan-overlap: the same cote and scan as sweep-1 placements of the topic;
- entry-read: I read the whole entry; passage-read: I read the passage on the scan.
Fidelity is assessed only for entry-read and passage-read rows.

What the gap list added to SA07:
- The 28 Codex sheet notes on K10, K16-02 and K19 follow the sweep-1 folder map (SA07-15, -16, -3, -17, -18; title sheets to SA07-9).
- The 64 entries of the second chat MPL_15_195-228+18_002-017_chatB that the broad agent could not link by script are placed as parallel witnesses of MPL_15_195-228+18_002-017, under the main chat's item for the same series where there is one: PG (periods) to SA07-2, B and O (Hom comparisons, Oda) to SA07-4, the cote 18 R notes on fundamental classes, the Gysin claim and the integral model to SA07-6, the cote 15 R notes on the reused root-space and coalgebra typescripts to SA07-5, the L notes on cote 16 (ring and category, operator normalizations, lettering audit) to SA07-12, the semisimplicity notes to SA07-3, the worked elliptic example P-A (y^2 = x^3 - x + 1, discriminant -368, which I recomputed) to SA07-2, and the apparatus (read-through, context searches, references) to SA07-9.
- The second-pass check events on MPL_16+47+54+44 are in SA18's CHECK_EVENTS, written once.


## Status after the third-sweep papers (POLISH_TOPOLOGY_PERIODS, prompt 91, checkpoints 12-13; intake of 23 Nov 2026)

Added by the intake agent a9e9559d (Claude Opus 5.5 at effort high), 23 Nov 2026. The run is GPT-6 Astra (ChatGPT Pro mode); checkpoint 13 (10:48 UTC) is probably its last; continuation prompt 91b sent. Intakes: `field_experts/intake_20261121/intakes/POLISH_TOPOLOGY_PERIODS/` (cp12 and cp13). Locators below are to the run's papers in `research_returns/POLISH_TOPOLOGY_PERIODS_checkpoint_13_20261123T1048Z_unzipped/papers/`.

- **Strong transcendence (cote 18, sheet 11), Paper 3 Thm 1.1:** the joint comparison torsor of N = M + c*M with v = dim N2 - dim(N2 n B^-), 0 <= v <= u, gives image dimensions g, u, b+v, u, u+v, g+v for alpha, beta, gamma, phi, psi, (alpha,beta): unconditional upper bounds, equalities under the period conjecture for N. The prediction holds (conditionally) iff v = u; if v < u five predicted degrees are false unconditionally. Targeted proof check by the cp12 intake (Lemma 3.1, Prop 3.2, Cor 3.3).
- **Counterexample, Paper 3 Cor 1.2:** h^1 of y^2 = x^3 - x + 1 over Q (the P-A example above), (g,b,u,v) = (4,3,1,0); real Frobenius makes the conjugate Hodge filtration rational, so trdeg k(gamma) <= 3 < 4 and trdeg Q(psi) <= 1 < 2. Independently recomputed by the cp12 intake.
- **B.4.1 refined:** the equalizer of two comparison sections is normal only under both global centralizations and compatibility; the unconstrained clause is refuted (run, CROSSWALK row 74).
- **Correction for authors (not in the paper):** Bhowmik-Pathak, arXiv:2408.00271v1, Thm 1.11 p. 3: counterexample tau = i, f = E4, g = j, F0 = 1 + E2 E6 / E4^2; repair: some f_r(tau) != 0 with r >= 1 and weight k != 0. Confirmed by the cp12 intake; e-mail draft unsent.
