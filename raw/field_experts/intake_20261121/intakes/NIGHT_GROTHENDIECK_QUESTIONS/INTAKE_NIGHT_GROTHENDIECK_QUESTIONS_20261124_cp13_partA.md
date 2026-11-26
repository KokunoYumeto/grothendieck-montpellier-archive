# Intake: NIGHT_GROTHENDIECK_QUESTIONS, Part A, checkpoint 04 to checkpoint 13

By agent a0805369bae2ebddc (Claude Opus 5.5 at effort high), 24 Nov 2026 ~11:xx UTC, at the request of the main
session 329fb1e6 (Claude Opus 5.5 at effort max). Brief: `INTAKE_WAVE_20261123_EVENING.md`, on top of
`INTAKE_BRIEF_20261121.md`.

The run is prompt 76, GPT-6 Astra (ChatGPT Pro mode); the effort is not exposed in the return. The return is
`research_returns\NIGHT_GROTHENDIECK_QUESTIONS_checkpoint_13_20261124T0037Z_unzipped`. It froze at 23:37 UTC on 23 Nov;
the archive is 00:37 UTC on 24 Nov.

**Parts B and C have not started by cp13.** The LEDGER, lines 333-334, and `CHECKPOINT_STATUS.md` say: "Parts B/C
remain inactive under sequential rule".

## 0. Scope

**The diff.** I hashed both checkpoints, cp04 (286 files) and cp13 (825 files): 541 files are new, 25 changed and 2 gone.
- **Changes to the papers:**
  - Only `papers/A133_lattices` changed: 18 new section files, 7 changed, and `even_truncations.tex` gone (it is
    subsumed by `all_truncations.tex`).
  - `papers/A15_finite_fields` and `papers/A123_tori` are byte-identical to cp04. The LEDGER confirms that the A15
    and A123 gates are unchanged.
- **The rest:** records for checkpoints 05-13, 226 workbench checks and 244 workbench work files. I opened none of
  them; the paper and the LEDGER were enough for the diff.
- **`_from_earlier_checkpoints/` (cp06, cp08, cp09):** these hold the A133 binomial-order drafts:
  - `even_binomial_orders.tex`;
  - `cubic_binomial_depth_two.tex`;
  - `deep_binomial_generators.tex`.

  Their statements (NGQ-A133-032, -037, -040, -042, -043) are marked "superseded by" Theorem 28.2 and Theorem 26.1 in
  cp13 `STATEMENTS.tsv`. I did not read the drafts.

**What I read in this task:**
- `STATEMENTS.tsv` in cp04 and cp13. There are 34 new statements, NGQ-A133-026 to -059.
- The LEDGER Part A rows from line 127 to the end.
- `CHECKPOINT_STATUS.md`.
- The `LITERATURE.md` diff, read for corrections.
- **Thm 26.1, `singular_distinguished_monic.tex`, read with proof:**
  - lines 1-600 in full: the supported-length lemma, the parameter choices, the polynomial lattices and the mesh,
    the generic zero, the detector and the evaluation;
  - Cor. 26.3 and Cor. 26.4 with their proofs (lines 672-730).
- **Thm 27.1 and Cor. 27.3:** statements only.
- **Thm 18.1, `prime_to_p_truncations_all_dvr.tex`:** the statement, the mesh lemma with its proof, and the surface
  lemma up to the minimal-generator step (lines 1-200).
- **The first theorem statements of** `all_truncations`, `odd_quadratic_orders`, `completion_generic_kernel`,
  `congruent_coefficients`, `ramified_truncations_vertical_ideals` and `monogenic_residue_degree_orders`.

**Computations in this task** (scratchpad `ngq\`):
- **`dm_check.py`, for Thm 26.1:**
  - Run on four cases: (p, F) = (3, t³+3t), (3, t⁴+9t³+3t²), (2, t³+2t) and (5, t⁴+25t).
  - The recursion (eq. singular-monic-finite-jet) stays integral.
  - g(α_c) + cF = t^N U_c holds exactly.
  - The residue of U_c(0) matches the three cases of (eq. singular-monic-unit-residue). In the first case, c = 1 is
    the excluded bad parameter (the residue is 0), as the paper's choice of c of large degree requires.
  - For every 0 ≤ i ≤ N, the X-operator on M_i has characteristic polynomial g(Z) + cF.
- **`trunc_check.py`, for Thm 13.1:** the generator matrix of `all_truncations.tex` satisfies T^p = I over Z[e]/(eⁿ)
  for (p, n, D) = (3,3,[2]), (3,4,[2]), (5,3, a cubic companion), (2,5,[1]) and (7,2, a quintic companion).
- **The Q(i) example of the Thakur draft:** re-derived by hand.

## 1. Verdicts

The counts are 7 statements checked with proof `[TPC]`, 2 by computation `[COMP]`, 25 at statement level `[stmt]`, and
0 refuted.

| id | statement | verdict |
|---|---|---|
| NGQ-A133-051, -054 | Thm 26.1: distinguished monic O[t]/(F), v_O(p)=1, split ⊕ℤ/N, N = min(n,pr) | `[TPC]` lines 1-600, `[COMP]` |
| (Cor. 26.3) | for F ≡ tⁿ mod p: Φ_A surjective ⇔ iso ⇔ A regular ⇔ a₀ ∈ pO∖p²O | `[TPC]` |
| (Cor. 26.4) | if the completed generic algebra is a field, N = n | `[TPC]` (valuation bound r ≥ n/2 checked) |
| NGQ-A133-055, -059 | Thm 27.1 / Cor. 27.3: edim(A/pA) ≤ 1 ⇒ positive iff regular | `[stmt]`; the Cohen reduction to 26.1 is sound as stated |
| NGQ-A133-047 | Thm 18.1: p ∤ n, any char-0 DVR: exact order-n class in both kernels | `[TPC]` on the mesh lemma and the surface lemma's div(X) = n𝔭; detector `[stmt]` |
| NGQ-A133-046 | Cor. 18.8: odd residue p, any DVR: dual numbers have an exact order-2 class | follows from 18.1 with n = 2; `[stmt]` for the detector |
| NGQ-A133-033 | Thm 13.1: Z_p, Z_(p), every n ≥ 2, split countable ℤ/n | `[COMP]` on the generator, `[stmt]` |
| NGQ-A133-053, -056, -058 | Thm 19.1, 19.7, 20.5: p ∣ n truncations over any DVR; vertical classes | `[stmt]` |
| NGQ-A133-028, -031 | Thm 23.1: a Z_p-order in a quadratic field is polynomial iff maximal | `[stmt]` |
| NGQ-A133-038 | Thm 24.1: congruence mod p^r, r > 2v_p|G|, preserves lattice K₀ | `[stmt]` |
| NGQ-A133-041, -057 | Thm 25.1: completion injective on K₀; generic kernels identified | `[stmt]` |
| NGQ-A133-035 | Thm 30.1: residue degree f > 1, a ⊕ℤ/f quotient | `[stmt]` |
| NGQ-A133-036 | Thm 17.1: the cp04 parity detectors vanish in the complementary range | `[stmt]`; a limit of that invariant only |
| NGQ-A133-039, -044, -045, -048 to -050, -052 | monic families mod p², p³, shallow top coefficient, standard meshes | `[stmt]`; mostly subsumed by 26.1 |
| -026, -027, -029, -030, -032, -037, -040, -042, -043 | earlier special cases | superseded within the run |

**How the proof of Thm 26.1 works:**
1. **The lattices.** Choose c with g(α_c(t)) + cF = t^N U_c, where g(X) = (1+X)^p − 1 and U_c is a unit. Then the
   2×2 factorization [[X−α_c, t^i], [−U_c t^{N−i}, h_c]] of g + cF gives C_p-lattices M_i, free of rank p, for
   0 ≤ i ≤ N.
2. **The mesh.** The endpoints M_0 and M_N are free. The coefficient-split mesh sequences give
   x_i = [M_i] − [A[C_p]] = i·x_1 and N·x_1 = 0.
3. **The generic fibre.** After inverting p, every M_i is free, because Z^p − 1 is separable.
4. **The detector.** Burke-Walker's generic-hypersurface equivalence takes the lattice to the chart z = c. The root
   section X = α(z,t) takes it on to S = D̂[[w,t]]/(t^N). There M_i becomes the ideal (p, tⁱ), and the
   supported-length map K₀ → ℤ/N gives i.
5. **The spectrum step.** The map K₀ → ℤ/N comes from Res ≃ N·G, by additivity over the filtration t^a S.
6. **The section.** Points c_j of pairwise distinct F_p^×-orbits give the split sum.

**The external inputs:** Blumberg-Gepner-Tabuada Thm 9.8 and 9.34; Antieau-Gepner-Heller Thm 1.1 (K₋₁ = 0); Orlov 2011
Lemmas 2.1, 2.5, 2.6; Burke-Walker Thm 2.10, Rem. 3.19, Cor. 3.18 and 3.20. I took each at the run's locator and
opened none of them.

## 2. What is new since cp04, and how the main questions moved

**Usefulness first.** This turns Grothendieck's question on cote 133, scan 29, from "no, here is a counterexample" into
a classification on a natural class. For finite free local algebras with curvilinear special fibre (edim(A/pA) ≤ 1),
including every monogenic order over an unramified DVR, generation holds exactly when the ring is regular. Wherever it
fails, the failure is a split infinite ⊕ℤ/N, with N read off from the first coefficient of valuation one.
- **Who would want it:** readers on integral representations (Grothendieck groups of lattices over orders: Swan,
  Reiner, Roggenkamp) and on λ-rings and Adams operations over singular bases. It also matters to anyone editing
  cote 133.

**Rows closed since cp04:**
- **Odd truncations:** closed negatively by Thm 13.1 and Thm 18.1.
- **Odd ramified dual numbers outside v₂(e) ≤ v₂(p−1):** closed negatively by Cor. 18.8.
  - The parity detector of cp04 vanishes there (Thm 17.1).
  - The divisor class of (X, t) on the normal surface O[[X,t]]/(g(X) + t²) detects the class instead.
  - The LEDGER row reads "REFUTED for generation".
- **Higher orders:** every monogenic singular order over Z_p or Z_(p), and over any DVR with v(p) = 1, by Thm 26.1 and
  Cor. 27.3.

**Rows still open:**
- **A133-classification:** singular rings with edim(A/pA) ≥ 2, that is non-monogenic orders.
- **A133-normal-singular:** an intrinsic criterion for normal singular rings.
- **Exact kernels over ramified DVRs.**
- **A15-minimum:** non-central models and the sharp bound. Unchanged since cp04.
- **A123-natural:** a preferred class. Unchanged since cp04.

**Withdrawn or refuted:** nothing. `even_truncations.tex` was replaced by `all_truncations.tex`, and the cp06-09 binomial
drafts were superseded by Thm 28.2 and Thm 26.1.

## 3. The Thakur draft, board rows A133a and A15c, and new corrections

- **The Thakur draft:** it holds against cp13. The A15 paper is byte-identical to cp04, and nothing in cp13 touches
  Thakur's Prop. 2.9 or the non-central case. I re-derived the Q(i) example of the draft (p = 5, d = 3,
  π = (5(2+i))^{1/3}):
  - π is a Weil 5-number, and x³ − ρ is irreducible over ℚ(i), since v = (2, 1) are not cubes.
  - End⁰ = ℚ(π), because the local invariants are 3·(2/3) and 3·(1/3), both ≡ 0.
  - Over F₁₂₅ the invariants are 2/3 and 1/3 over ℚ(i): type IV(1,3), simple over every extension.
  - The draft needs no change. Its state stays "pending the run's final" and the user's yes.
- **A15c:** it holds as written; nothing in cp13 changes it.
- **A133a: out of date.** Its gate "the order-two and infinite-summand parts" is discharged in the run by Cor. 18.8 and
  Thm 13.1 / 26.1. The row states only the cp04 answer. Proposed replacement text in section 5.
- **New corrections to published work: none.**
  - I searched the new A133 sections and `LITERATURE.md` for errata, corrections and disagreements with published
    work.
  - The only hit is an attribution note ("Classical Swan comparison: source-attribution clarification", LITERATURE
    2026-11-23 20:29). It says the addendum in the Bass Seattle volume is by Gersten (1973), not Swan. That is a
    citation fix inside the run, not an error in a published paper.
  - No draft is made.

## 4. Integration

- **Applied:** `results_register\horizontal\sweep3\SA17\STUDY.md`, cote 133 scans 28-29. The cp04 "Open" line now notes
  the two rows closed at cp13, and a new block "Further answers at cp13" follows it. Backup:
  `integration_backups\20261123\NIGHT_GROTHENDIECK_QUESTIONS\STUDY_SA17_before_cp13_partA_20261124.md`.
- **For the main session** (logged in the Part A integration tsv):
  - **HEXAGON_BOARD:** replace A133a, and add A133b (section 5).
  - **`reports_20261122/paper_seeds/SEED_ARCH_ALG.md`:** still unapplied from cp04 (point Papers 3-5 to this run's
    papers).
  - **`reports_20261120/errata/NOTE_E6_Thakur_draft.md`:** superseded by `EMAIL_DRAFT_Thakur_20261123.md`; mark it so.
- **The primer** is updated in place, with the cp04 version backed up.

## 5. Board candidates

- **A133a, replacement text.** Grothendieck's question, cote 133 scan 29, is answered no, and is classified in the
  curvilinear case:
  - Characteristic 0 is necessary.
  - Locality and K₀ = ℤ are not sufficient: flat dual numbers fail at every prime, over every characteristic-0 DVR of
    odd residue characteristic (an exact order-2 class), and every truncation O[t]/(tⁿ) fails.
  - For a finite free local algebra over a mixed-characteristic DVR with edim(A/pA) ≤ 1, generation holds iff A is
    regular. A singular one has split ⊕_ℕ ℤ/N in the degree-p generic kernel.
  - **Checks:** a0805369 (Claude Opus 5.5 at effort high). At cp04: the dual-number and positive-characteristic
    sections with proofs. At cp13: Thm 26.1 lines 1-600 and Cor. 26.3/26.4 with proofs, with the factorization
    identities recomputed, and Thm 18.1's mesh and surface lemmas.
  - **Gates left:**
    - Cor. 27.3 and Thm 13.1/19.1 read in full;
    - the external inputs (Burke-Walker, Blumberg-Gepner-Tabuada) at their locators;
    - non-curvilinear singular rings;
    - the run's final.
- **A133b, new: "regularity criterion for lattice generation".** The statement of Cor. 26.3 / Cor. 27.3: Φ_A is an
  isomorphism iff A is regular, for A finite free local over any mixed-characteristic DVR with edim(A/pA) ≤ 1, and
  N = min(n, pr) as above.
  - **What it adds:** the first classification theorem for Grothendieck's question; the cp04 results were
    counterexamples.
  - **Checks:** as for A133a.
  - **Gates left:** the same.

A15c and A123: no new candidates.

## 6. For the P vs NP fleet

None of the new results bears on complexity. They concern lattice Grothendieck groups over singular coefficient rings,
and the fleet's proof graph has no node for them. The only node near the subject is L-gct-149 (the Kronecker exponent),
and it is unrelated. No map is made.

## 7. Prompt updates and Hexagon readiness

- **Prompt updates:** none; the run is live.
- **Hexagon:** not ready. The run has not finished, and its own LEDGER records that the "final expert/newcomer
  whole-paper readings remain due". Post after the final, with A133b as the lead result.
