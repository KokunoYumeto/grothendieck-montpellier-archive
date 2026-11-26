# GCT cluster: geometric complexity theory, border rank, Kronecker and plethysm coefficients, tensor norms

**Intake pile of 24-25 Nov 2026.** Cluster reader: Claude Opus 5.5 at effort high, launched by main session 329fb1e6
(Claude Opus 5.5 at effort max). Work file:
`<local>/Documents\agent_notes\20261124T2111Z_Intake_pile_GCT_cluster_NOTES.md`.

**The runs.** GCT_OBS, GCT_POS, CUE_GCT, GCT_PLETH, GCT_NSRH, GCT_KRON, BR_PENCIL, GCT_GINEQ and DP_MULT. Every run is
GPT-6 Astra (ChatGPT Pro mode). Each run's own records give its effort as "not exposed".

**Companion files** in this folder:
- `GCT_ITEMS.tsv`, one row per item;
- `INTAKE_<RUN>_20261124_CHECK_EVENTS.tsv`, nine files;
- `checks_GCT/`, my eight scripts with their outputs.

## How to read this file

**Nothing new has come back from any of the nine runs since their intakes.**
- Every newest return was taken in on 21-22 Nov. The intakes are in `field_experts\intake_20261121\intakes\<RUN>\`, and
  each run has a primer of 23 Nov there, `PRIMER_<RUN>_20261123.md`.
- **GCT_OBS:** the newest return is checkpoint 15. It is not in `research_returns` (that folder holds only checkpoint
  05). Its text is in `reports_20261122\overnight_intake\GCT_OBS_cp15\text\`, and the split zip is in `Downloads`.
- **GCT_POS:** the zips `GCT_POS_checkpoint_07.zip` and `_08.zip` in `Downloads` are the last scheduled checkpoints
  *before* the final. Checkpoint 08's state is "02:01Z STOPPED - FINALIZING"; the final was written at 02:19Z.
- **The ledger is out of date.** `field_experts\INTAKE_LEDGER.md` still says "not taken in" for all nine runs
  (lines 105-145 and 267-280).

**What is new since the intakes** comes from elsewhere:
- the two VP ≠ VNP claims of 23-24 Nov;
- the joint GCT lemma space with the pequalnp.com fleet (23-24 Nov);
- Codex's runs BORDER_RANK, GCT_SEPARATIONS and GCT_FLIP. I did not open them, as the brief says. I cite them only
  through `JOINT_GCT_LEMMA_SPACE.md`;
- the H09 note, drafted to v4 on 23 Nov and not posted.

**This file adds:**
- a ranking across the cluster;
- for each run, what the VP ≠ VNP claims change;
- nine spot checks of my own. They are listed per run below and in the check-event files.

**Labels.**

| Label | Meaning |
|---|---|
| [TPC] | targeted proof check |
| [COMP] | computation by an intake |
| [MS] | the main session's check |
| [stmt] | statement level only |
| [run] | the run's own whole-proof reviews only |

## The VP ≠ VNP claims, in one paragraph (for every run below)

Two unrefereed preprints claim VP ≠ VNP: Anthropic's, by Claude (23 Nov), and OpenAI's (24 Nov). Each comes with Lean,
and no human has checked either. Our reading of them is `<local>/pequalnp_work\fleet_map\VPVNP_INTEGRATION_20261124.md`.

**What they give for GCT:**
- **The target, by a route around GCT.** L-gct-011 (Mulmuley-Sohoni for every c) is implied: OpenAI's Corollary 1.2;
  Anthropic's Theorem 1.4 with Remark N.6.
- **No occurrence or multiplicity obstruction.**
- **Ineffective constants.** So the claims say nothing at any fixed size. Our (8, 9), (17, 23), n = m families and 4×4
  border ranks are untouched.
- **The GCT-facing step is unformalized in both releases:** orbit closure, then border determinantal expression, then
  circuit.

**What this means for our results:**
- **Our explicit fixed-size witnesses keep their value.**
- **Our barrier results** (KRON M-008/O-018, OBS S-004, CUE R-14, GCT_FLIP no-occurrence) "change meaning". If the claims
  hold, they mark where the separation exists but has no low-height witness.
- **Our border-rank, substitution, apolarity and moment-polytope tools** are named as tools for the open hinge of both
  proofs: flat against contracting prices; strict shortening.
- **Nothing of ours contradicts either claim.**

---

## The cluster's most interesting items, ranked by usefulness

1. **Numerical PH3 fails for Kronecker coefficients, for every n ≥ 2** (GCT_POS K-023, R-NEW-004, K-024, PNEW-013;
   Hexagon H02b).
   - **Statement.** Put k_n(s) = g((s^n), (s^n), (s^n)). Σ k_n(s)t^s has a pole at a primitive root of order
     2^{n-1}·3^r for some r ≥ 0. So every positive form has denominator weight ≥ 2^{n-1}, against GCT VI's rank
     n² + 5n.
   - **Why it matters.** It refutes the existence clause of GCT VI Hypothesis 3.3.4 for the coefficients GCT is built
     on. The run's own text cites 1.6.7; that citation is an erratum.
   - **Checks:**
     - the main session's [MS] (Claude Opus 5.5 at effort max): proof check plus computations, `reports_20261122\gct_pos_ph3_check\CHECK.md`;
     - the intake's [TPC];
     - mine: a re-derivation of the PNEW-013 transfer, with no gap.
   - **Open:** r = 0 for n ≥ 6; PH2 and SH(a).
   - **Where:** `research_returns\GCT_POS_final_20261122T0219Z_unzipped\branches\plethysm\modular_pole_transfer.tex`
     and the K branch.
   - **Prompt:** the write-up is prompt 57, with H24 and H02.
2. **All zeros of plethysm coefficients in outer degree five, and positive polytope formulas in outer degrees four and
   five** (GCT_PLETH G-031, G-036, T-037).
   - **Statement.** Every p^λ_{μ,(n)}, μ ⊢ 5, is decided by an explicit rule: a strict-chamber rule, plus a normal form
     with period 10, plus a catalogue of 344 vectors.
   - **Why it matters.** It is a complete answer in a case of the plethysm positivity problem, Stanley's Problem 9. That
     problem is central to algebraic combinatorics independently of GCT.
   - **Checks:**
     - the intake: [COMP] on all 2,408,042 coefficients with n ≤ 22;
     - mine: my own coefficient code and my own implementation of the rule from the TeX, 47,866 coefficients with n ≤ 9,
       no mismatch; and 258 catalogue vectors whose seven multiplicities agree.
     - Nobody has read the proof of exhaustion.
   - **Where:** `GCT_PLETH_checkpoint_09_20261121T0546Z_unzipped\GCT_PLETH.tex` from line 20109, and
     `work\root\FIVE_ROW_SUPPORT_INDEX.json`.
   - **Prompt:** the write-up is prompt 60 (H20, H21).
3. **Four-row multiplicity obstructions under genuine padding** (CUE_GCT R-14, R-13, G-20 with R-27; Hexagon H14).
   - **Statement:**
     - For n > m, a dimension criterion c_m + 3 > 2n² + 2 gives, in every large degree, an exactly-four-row λ with
       m_λ(z^{n-m}per_m) > m_λ(det_n).
     - This yields explicit padded pairs (8, 9) through (16, 22).
     - With R-27, the range for m ≥ 17 is exactly n² ≤ 2m² − m + 1.
   - **Why it matters.** These are multiplicity obstructions in a genuinely padded range. None were found in the
     literature by our intakes; the novelty search is not done.
   - **Checks:**
     - R-14: the intake's [TPC], and my own [TPC] of the full proof;
     - G-06 (dimension 2n² + 2 of the quaternary determinantal image): my computation for n ≤ 8;
     - R-13 for m = 4-10: the intake's [COMP];
     - R-23, R-26, R-27: unread by any intake.
   - **VP ≠ VNP:** this becomes a "witness desert" result. Four-row witnesses stop at about √2·m, while the claims would
     separate at every n = m^c.
   - **Prompt:** the write-up is prompt 58.
4. **Explicit occurrence obstructions per_n against det_n with no padding, along every stretch** (GCT_KRON A-030,
   A-034, O-030; Hexagon H13).
   - **Statement:**
     - λ = (n + q + 1, 3, 2^{n²−2}) in degree n² + 1 has a_λ = 1, K_n(λ) = 0 and q_λ = 1, with a zero Kronecker
       coefficient.
     - Every stretch gives a strict multiplicity gap, and O-030 gives a three-parameter family.
   - **Checks:**
     - the intake's [TPC] with computations;
     - mine: F-024 recomputed with independent code at 15 pairs (n, d), including the A-030 point (13, 3, 2^7); Muir's
       constant c_3 = −2; Θ(per_3) ≠ 0 at an explicit zero; and a short re-proof of the Kronecker zero.
   - **VP ≠ VNP:** unchanged. These are fixed-size, explicit witnesses.
   - **Gate:** the literature (Kumar; Bürgisser-Ikenmeyer-Hüttenhain; Ikenmeyer-Kandasamy; Dörfler-Ikenmeyer-Panova).
   - **Prompt:** prompt 58.
5. **A sign-only purity criterion and the exact weight gate** (GCT_NSRH F03, F24, F50).
   - **What it is.** A Deligne-type purity theorem in which a path-sign hypothesis replaces the weight.
   - **Status:** posted as **H01, hexagon:2611.00789 (deposited 21 Nov)**.
   - **F50 locates the whole difficulty:** the sign is always free, and the content is an independent stalk weight
     bound.
   - **Check:** mine, the squarefreeness of the path determinants d_k over F_p, 200 cases.
   - **Rank four:** F57, F58 and F67 show that strict positivity of Mulmuley's nonstandard objects fails from rank four
     on. This is the substance of erratum H23.
6. **Sharp divisibility of invariant derivatives on formal groups of every height** (DP_MULT DP1, DP3, DP34).
   - **Why it matters.** It answers Katz's 1977 question beyond the Lubin-Tate case of Bannai-Kobayashi, and gives the
     local exponent of Alpöge's step 2.
   - **Status:** the note `reports_20261123\h09_note\h09_note_v4.tex` is written and checked by three readers, and is not
     posted.
   - **Check:** mine, on the Honda group of height 2 at p = 3. It confirms DP1 and DP3 for n ≤ 170, and the failure of
     Katz's height-two bound by one at n = p² − 1 = 8 (the note's Theorem B).
   - **Not GCT.**
7. **Border rank of the 4×4 determinant and permanent tensors** (BR_PENCIL R-05, R-08, R-10; Hexagon H03).
   - **Statement:** ≥ 43 over C; ≥ 42 over every algebraically closed field.
   - **Superseded since:**
     - by GCT_OBS BR-006, ≥ 44 for det_4 in characteristic 0;
     - by Codex's BORDER_RANK thm:52, ≥ 52 for both in characteristics 0, 2, 3, according to the joint lemma space. I
       did not open it.
   - **For H03:** post the newest bound, with BR_PENCIL's substitution lemma R-01 and torus reduction P-01 as its
     method.
8. **Padded quaternary quartics are 7×7 determinants** (GCT_OBS QC-014).
   - **Statement:** no ≤ 4-row multiplicity obstruction exists for z^{n−4}per_4 against det_n, n ≥ 7. This is a clean
     positive containment beyond n/m = √2.
   - **The named (8, 9) direction (QC-019):** the weight s(216, 9, 9, 9) at s = 67·28^38.
     - My exact check: the binomial comparison holds, and s is within a factor of about 3 of the smallest s that the
       two bounds allow (about 1.66·10^56).
9. **Tensor norms do not bound rank** (GCT_GINEQ F-05, F-13, F-23, F-08).
   - **F-05:** nuclear²/Frobenius² = 8 > 7 = R(M_2). It follows at once from Derksen's ‖M_n‖_* = n³, so it is marginal.
   - **F-13 and F-23:** border substitution in any order, and the exact residual reduction. They seeded BR_PENCIL.
   - **F-08:** a defect in Friedland-Lim v3, to report to its authors.

---

## GCT_POS (prompt 52): positivity hypotheses after the plethysm refutations

**Useful.** It refutes a named hypothesis of GCT VI (numerical PH3, Hypothesis 3.3.4) for triple-rectangular Kronecker
coefficients, the coefficients GCT is built on. Its nonstandard branch answers the rank-four questions left by
GCT_NSRH.

**What it proved.** Notation: k_n(s) = g((s^n), (s^n), (s^n)) and M = 2^{n−1}.

- **The main theorem (K-023 + R-NEW-004 + K-024 + PNEW-013):** for every n ≥ 2, Σ k_n(s) t^s has a pole of order
  M·3^r (a pole at a primitive root of unity of that order) for some r ≥ 0.
  - Checks: [MS] Claude Opus 5.5 at effort max, 22 Nov; intake [TPC] (a0805369, Claude Opus 5.5 at effort high).
  - Mine: [TPC] of PNEW-013, the proof read in full and re-derived (`INTAKE_GCT_POS_20261124_CHECK_EVENTS.tsv`).
  - The step K-024 uses ALPOGE_GCT P-F23, P-F27 and P-F30, which are ours and unpublished.
- **Exact order M (r = 0) for small n:** n = 2, 3 (classical); n = 4 (K-008, 13 fixed curves, residue
  (14 − 10√2)/256, [COMP]); n = 5 (K-014, 424 curves, [COMP]).
- **K-009 [TPC]:** no pole at order above B_n = (3 − 2/n)^{(3n−2)/2}/n.
- **K-018 [COMP] at n = 9:** the premise "maximal order 2^{n−1}" is false. Polystable free supports reach determinant
  order 2^{n−1+⌊(n−2)/7⌋}.
- **PNEW-016:** a dichotomy for n ≥ 79004 between large indices and huge coefficient mass. It decides neither PH2 nor
  SH(a).
- **Plethysm side:**
  - PNEW-005: p(f_n) > 2^{n/8} for n ≥ 79,000, given PNEW-002 to 004;
  - R-NEW-001: an outer-degree-six table of 5,214 coefficients, recomputed by our intake with 0 mismatches.
- **Nonstandard branch:**
  - N-012: GCT VIII Conj. 3.2 has no minimum as printed (H23);
  - N-002: the first P-word of Ȟ₄ outside the C⊗C cone has length 5;
  - N-003: a positive K-basis of B₄ exists;
  - N-009: Ȟ₄ has no Z[v^±]-basis.

**New since the last intake.** No new return; the final was intaken on 22 Nov. What the VP ≠ VNP claims change:
- **Nothing mathematically.** The claims reach the flip's target (permanent against determinant) without the flip.
- **The refutation keeps its point.** The positivity hypotheses belong to Mulmuley's programme for P ≠ NP and #P ≠ NC,
  which the claims do not touch.
- **The K-series could become a tool.** It computes the invariant theory and moment polytopes of 3-tensors (polystable
  points, grading stabilizers). Our integration note names these as the source of the explicit spectral points
  (quantum functionals) on which the flat/contracting hinge turns (VPVNP_INTEGRATION finding 3). Those functionals are
  provably of the contracting kind, so the K-series cannot decide the hinge by itself.

**Open.**

| Row | Gate |
|---|---|
| r = 0 for n ≥ 6 | K-031's collision-supported moving Koszul class must cancel a 3-adic unit; attack it on the n = 18 component (K-038) |
| PH2 and SH(a) for Kronecker | the coefficient estimate U_Δ^+ < 2^{(17/240)n⁴ − 6n³ − 4} (PNEW-016c) |
| Uniform positive formulas (Q4), outer degree six (Q5) | — |
| Positive designated bases of Ȟ_r | — |

**Relations.**
- **Our runs:** ALPOGE_GCT (P-F14, P-F19, P-F31, P-F57: the plethysm refutations, H02); GCT_PLETH (G-040 limited by
  PNEW-010); GCT_NSRH (rank-four answers).
- **Literature:** GCT VI v4 (arXiv, 22 Jan 2009), Hypotheses 1.6.7 and 3.3.4, §3.4; Bremner-Hu arXiv:1112.2949 Th. 2.4
  (n = 3); Pak-Panova-Swanson (outer six, two rows); for K-018, Kravtsov and Franks-Reichenbach.
- **Grothendieck:** K-023 is the Adams operation ψ³ on Schur functors, the λ-ring structure of the representation ring
  (cote 133's λ-operations). K-024 is Lefschetz-Riemann-Roch on a fixed curve.

**Candidates.**
- **Hexagon H02b:** gates are the literature with Hexagon, a self-contained write-up (it must carry P-F23, P-F27 and
  P-F30) and a reading of every page. The write-up is prompt 57, with H24.
- **Next prompt:** r = 0 at n = 18, and an off-residue witness at n = 4 from R-NEW-003.

**Problems.**
- **The PH3 citation.** `branches\plethysm\modular_pole_transfer.tex` lines 207-208, `IMPLICATIONS.md` line 5,
  `QUESTIONS.tsv` row Q1ph3 and `GCT_POS.tex` lines 92-93 cite GCT VI **1.6.7** (plethysm constants). The Kronecker
  statement is **3.3.4**. The cause is partly our prompt 52, which defined PH3 as 1.6.7.
- **Unread proofs.** K-026 to K-038 are at statement level.

## GCT_PLETH (prompt 25): plethysm coefficients through λ-rings

**Useful.** It gives a complete decision of the zeros in outer degree five, and positive #P-type polytope formulas in
outer degrees four and five and for stable families. These are wanted results on plethysm positivity in algebraic
combinatorics, whatever happens to GCT.

**What it proved.**
- **G-031** [COMP intake; COMP mine]. For μ ⊢ 5 and λ ⊢ 5n, the rule NW.1-NW.3 decides whether p^λ_{μ,(n)} > 0:
  - In the strict chamber (all four gaps positive), G-028: the five middle labels always occur. The two one-dimensional
    labels vanish exactly at g = (L,1,1,1) and (1,1,1,L) with L ≡ 1 mod 5. The trivial label also vanishes at (1,2,2,1)
    and (2,1,1,2).
  - Otherwise, normalize with period 10 and look the vector up in a catalogue of 344 vectors.
  - Checked by the intake on 2,408,042 coefficients (n ≤ 22). Checked by me with independent code on 47,866
    coefficients (n ≤ 9), and on all seven multiplicities at 258 catalogue vectors (`checks_GCT/c7_pleth_output_n9.txt`).
  - The proof of exhaustion has not been read by anyone outside the run.
- **G-036** [COMP]. Outer degree 5: every coefficient is a sum over ≤ 152 bounded polytopes in ≤ 11 variables. 539 of
  539 values checked; proofs not read.
- **T-037** [COMP]. Outer degree 4: ≤ 108 polytopes in ≤ 5 variables, through an S₄-equivariant freeness. 60 of 60;
  proofs not read.
- **G-015, T-032 to T-036** [run; COMP on 10,164 coefficients]. The stable chart: p^λ_{μ,(n)} = [S_γW : ν] when λ₂ ≤ n.
- **G-037 to G-040.** Stable families:
  - hooks, G-037 [COMP 790 values; support test 15,943 cases];
  - tails (a,2) and (a,3);
  - every fixed b, G-040 [run]. It is polynomial for each fixed b only (GCT_POS PNEW-010).
- **Cote 133:**
  - A-001 [TPC]: the boxed 2λ²E + E = E² of scan 019 fails;
  - A-003 [TPC]: the split Green ring is not special;
  - A-007 [TPC];
  - A-013 [TPC];
  - A-023 [TPC]: no free generation by the ρ_i over Z_(2)[ε]/(2ε, ε²).

**New since the last intake.** No new return. The seed `reports_20261122\paper_seeds\SEED_GCT_PLETH.md` records the
corrections below. The VP ≠ VNP claims change nothing: plethysm positivity is a combinatorial question that the claims
do not touch.

**Open.**
- **Q-EFFICIENT:** positive formulas uniform in b. Gate: the cokernel C_ν, whose literal cover is barred by PNEW-010.
- Outer degree six beyond two-row output.
- **Q-MAP:** the critical annihilator for r = 3, 4.
- Width 7.

**Relations.**
- **Our runs:** GCT_POS (R-NEW-001, PNEW-010); ALPOGE_GCT (H02); GCT_KRON (cote 133 A-ids, independently agreeing with
  CUE_GCT G-01).
- **Literature:** Sarkar arXiv:2610.07929v2 Th. E (T-012/T-013); Kahle-Michałek and Fischer-Ikenmeyer (#P membership for
  fixed |μ|, known); Pak-Panova-Swanson arXiv:2511.02312 and Narayanan arXiv:2403.03443 (varying outer degree, known);
  Macdonald I §3 Ex. 2-3; Kirillov-Pak and Molchanov (hook series).
- **Grothendieck:** λ-rings and the special λ-structure on representation rings (cote 133).

**Candidates.**
- **H20 and H21:** prompt 60. The proposed headline is "the complete list of zeros in outer degree five" (G-031).
- **Gate:** an intake proof reading of G-031's exhaustion and of G-036's three providers.

**Problems** (all recorded in the seed and the register):
- "First with varying outer degree" is false (Pak-Panova-Swanson; Narayanan). It has been withdrawn from H21.
- G-040's construction is polynomial for each fixed b only.

## CUE_GCT (prompt 36): the random-matrix side, isolation, and padded obstructions

**Useful (the GCT part).**
- R-14 and its range are multiplicity obstructions under genuine padding.
- The prompt's random-matrix and isolation questions gave statement-level material only.

**What it proved.**
- **R-14** [TPC intake; TPC mine].
  - Statement: if c_m + 3 > 2n² + 2, where c_m = dim P_{m,4} (the four-variable image of per_m), then for every large d
    some λ ⊢ nd of length exactly four has m_λ(z^{n−m}per_m) > m_λ(det_n).
  - I read the proof in full (CUE_GCT.tex lines 1238-1360) and found no gap. The transfer of ≤ 4-row multiplicities
    from GL₄ to GL_{n²} works through highest-weight vectors in Sym(Sym^n W) and the ideal of the restriction image.
- **G-06** [TPC intake; COMP mine]: dim D_{n,4} ≤ 2n² + 2. My Jacobian ranks give exactly 2n² + 2 for n = 4 to 8. The
  identity C(n+3,3) − (2n² + 2) = C(n−1,3) also holds.
- **R-13** [COMP intake for m = 4-10]: c_m = C(m+3,3) for 4 ≤ m ≤ 16, and dominance fails at m = 17 (1124 < 1140). This
  gives the finite padded pairs (8,9), (9,10), …, (16, 17-22).
- **R-27 and G-20** [stmt]: c_m = min(C(m+3,3), 4m² − 2m + 2) for every m. So for m ≥ 17 four-row gaps exist exactly when
  n² ≤ 2m² − m + 1. I checked the equivalence arithmetic for m = 17 to 199.
- **G-05** [TPC]: no obstruction with ≤ 3 rows. This is classical (Dickson; Beauville Prop. 3.1(a)).
- **Cote 133, G-01** [TPC]: independent agreement with GCT_KRON A-001.
- **P-11, I-18** [TPC]: isolation.
- **I-21 to I-44 and P-01 to P-20** [stmt].

**New since the last intake.** No new return.
- **The VP ≠ VNP claims sharpen R-14's meaning.** If either claim holds, z^{m^c−m}per_m is outside the det orbit closure
  for every c. Four-row multiplicity witnesses exist only up to n ≈ √2·m, and no route through four variables passes
  √2 (RQ-26).
- **The run's sentence calling m²/2 "the established" border bound (ctx-G13) is out of date twice over:**
  - by the fleet's Lean-checked (2m² − 10m + 11)/3 (L-gct-070) and border dc/m² → ∞ (L-gct-074);
  - by the claims, if they hold.
- **The isolation material (I-Q01):** nothing in the claims gives ROABP hitting sets.

**Open.**
- Explicit four-row λ, degree and equation at (8, 9) and (17, 23). GCT_OBS took this over.
- Padding beyond √2·m: needs comparisons other than dimension counts.
- I-Q01 and I-Q13.
- P-08.
- Rerunnable certificates for R-13 (m = 11-16), R-24, R-25 and R-27.

**Relations.**
- **Our runs:** GCT_OBS (QC-019 names the weight at (8, 9); QC-014 shows nothing exists at m = 4, n ≥ 7); GCT_KRON
  (M-007 = G-08, universality); the fleet's L-gct-010/011 (separation known; barrier).
- **Literature to search:** Kadish-Landsberg; Landsberg's GCT book ch. 8-9; Dörfler-Ikenmeyer-Panova;
  Ikenmeyer-Kandasamy; Gesmundo-Ikenmeyer-Panova; Bürgisser's survey.
- **Grothendieck:** R-23 places the remaining defect in one graded Tor₁ piece, in SGA 6's Tor-independence dictionary.

**Candidates.**
- **H14:** prompt 58. A narrower post (R-14 with m = 8-16) needs only the literature search and a check of R-13 for
  m = 11-16. The full statement also needs R-23, R-26 and R-27 read, and the m = 17 certificate recomputed (a minor of
  order 88 mod 101).

**Problems.**
- The ctx-G13 sentence above.
- The run's text says plainly that the asymptotic formula for c_m beyond the certified range is "a separate
  generic-fiber problem" (lines 1351-1356 of the cp08 TeX). The register's "exactly for n² ≤ 2m² − m + 1" rests on
  R-27, which none of us has read.

## GCT_KRON (prompt 26): Kronecker coefficients through λ-operations on G-sets

**Useful.** It gives explicit occurrence obstructions with no padding along whole rays, and a sharp ledger of where
padded obstructions cannot be. The prompt's λ-ring question gave corrections to our cote-133 study rather than
positivity results.

**What it proved.**
- **A-030** [TPC intake + COMP; mine: COMP and a re-proof of the Kronecker zero].
  - Statement: let R = n², q = R(n − 2), d = R + 1 and λ = (n + q + 1, 3, 2^{R−2}). Then a_λ(d[n]) = 1, K_n(λ) = 0,
    q_λ^n(d) = 1 and g(λ, (d^n), (d^n)) = 0.
  - Proof: the covariant Θ(F) = q·H(F)·dF − n·F·dH(F). Muir's identity H(det_n) = c_n·det_n^{n(n−2)} gives Θ(det) = 0.
    The Mignon-Ressayre point gives Θ(per) ≠ 0. F-024 gives a_λ = 1.
  - My checks: H(det₃) = −2·det₃³, which equals c_3 of the run's formula (A-030.3). Θ(per₃) ≠ 0 at an explicit zero of
    per₃ with Hessian rank 9. F-024 holds with my own code at n = 3, d = 3-11 (including (13, 3, 2^7)), at n = 4, d = 3-7,
    and at n = 5, d = 3-5.
  - Kronecker zero, re-proved: removing the twist by 2 columns leaves (N − 1, 1), and g((N−1,1), μ, μ) = #distinct
    parts(μ) − 1 = 0 for a rectangle.
- **A-034** [TPC]: for every stretch s, q(sλ_n) ≥ p_n(s) > h_n(s) = K_n(sλ_n).
- **O-030** [TPC; the two-row identity COMP for n ≤ 8].
  - Statement: Λ(u, a, k) = (na + u(q+2) − k, 2u + k, (2u)^{R−2}) has K_n = g = h_n(k), and q_Λ ≥ Σ_{j ≤ min(u,k)}
    h_n(k − j).
  - Mine: the Kronecker value re-derived (generating function 1/∏_{i=2}^n(1 − q^i)).
- **F-025:** q = 6 > K = 5 at per₃/det₃, λ = (19, 7, 2⁵). This is a multiplicity obstruction that is not an occurrence
  one. GCT_OBS S-002/S-003 rebuilt both sides.
- **The padded ledger:**
  - M-006 [TPC] and M-013 [TPC];
  - M-007, M-008, F-021, O-018, A-025, M-019, A-035 to A-038 and O-011 [stmt].
  - Summary: no multiplicity obstruction with ≤ 2c + 1 rows at n ≥ m^c. In the BIP range, ≥ 52 rows and m ≥ 190 are
    needed, among other row conditions.
- **Cote 133:** A-001 [TPC] (scan 019's boxed identity fails); A-002 (known: Bouc-Rökaeus); A-013; A-029 (Grothendieck's
  q_H^n, read from the scan).

**New since the last intake.** No new return.
- **The VP ≠ VNP claims leave A-030, A-034 and O-030 unchanged:** these are explicit witnesses at n = m, and the claims
  are asymptotic and ineffective.
- **M-008 and O-018 change meaning.** If the claims hold, the separation exists at n = m^c, but no multiplicity
  obstruction with ≤ 2c + 1 rows witnesses it. This holds under the fleet's independent padding as well, through
  GCT_OBS S-004.

**Open.**
- QMMAIN in the large-padding range (the evaluation-tensor ranks, F010).
- An explicit padded obstruction: covariants outside the Hessian algebra.
- QA033 (the same statement as the fleet's L-gct-084).

**Relations.**
- **The fleet:** A-030 uses L-gct-013 (the Mignon-Ressayre point) and parallels L-gct-012 (Muir). The separation itself
  is L-gct-010. F-009 is L-gct-006 applied to Grenet (L-gct-007).
- **Literature:** Mignon-Ressayre 2004 Prop. 3.1; Landsberg-Manivel-Ressayre, Comment. Math. Helv. 88 (2013) p. 476;
  BIP (no occurrence obstructions); Kumar (Compositio 2015); Bürgisser-Ikenmeyer-Hüttenhain (PAMS 2017);
  Ikenmeyer-Kandasamy (STOC 2020).
- **Grothendieck:** cote 133, the λ-operations q_H^n on G-sets (A-029); Burnside rings.

**Candidates.**
- **H13:** prompt 58. Restate it as O-030 with S-002/S-003. The gate is the literature. My checks add F-024 at 15
  points.
- **A correction to our own study** of cote 133 (SA17), A-001: already recorded.

**Problems.** None found by me. F-025's determinant side rests on LMR's printed value; GCT_OBS S-002/S-003 removed that
dependence.

## GCT_OBS (prompt 53): explicit padded obstructions and border rank of 4×4 det/per

**Useful, mainly for its by-products.** The main question was an explicit obstruction at (8, 9) with a separating
equation. It is still open. What came of the run:
- S-002/S-003, the explicit LMR example on both sides;
- QC-014, padded quaternary quartics in the determinant closure;
- QC-019, a named direction at (8, 9);
- BR-006, BR(det₄) ≥ 44.

**What it proved** (from checkpoint 15, read by the intake a17221e5, Claude Opus 5.5 at effort high):
- **S-002, S-003** [TPC, COMP].
  - At n = m = 3, d = 12, λ = (19, 7, 2⁵): a = 6, the ideal multiplicity is 1, K₃ = 5 and q = 6.
  - The separating equation is Ψ = 2P₀ + 21P₁ + 7P₂ + 35P₃ + 7P₄.
  - Mine: the key Hessian step, rank 6 for det₃ at a rank-two matrix (= the fleet's L-gct-012 at n = 3).
- **S-004** [TPC]: the padding conventions. The independent pad gives cap m² + 1. M-019's threshold becomes 238,356,708.
- **QC-014** [TPC, COMP]: ℓ^{n−4}q ∈ D_{n,4} for every quaternary quartic q and n ≥ 7. So q_λ ≤ K_n(λ) for every λ with
  ≤ 4 rows at (4, n).
- **QC-019** [TPC on the comparison; the 156-function certificate is carried].
  - Statement: q_{8,9}(sλ₀) ≥ C(s+155, 155) and K₉(sλ₀) ≤ C(27s+151, 151) for λ₀ = (216, 9, 9, 9), degree 27s. So there
    is a strict gap at s = 67·28^38.
  - The run's scaling refinement reports that its 156-square minor is 13 mod 101 on a fresh replay
    (`work\quaternary\rectangular_slice_scaling_refinement.tex`). No intake has recomputed it.
  - Mine [COMP]: the exact big-integer comparison holds. The smallest s for which these two bounds give a gap is
    1.66·10^56, so the run's s is about 3 times that.
- **QC-021** [stmt]: I(D_{n,r})_d = 0 for n ≥ 6 and d ≤ 10.
- **The box exclusions** [stmt]: OBS-011 to 016, QC-015 to 018, QC-020 and QC-026 to 029. At (8, 9) a four-row
  obstruction needs second row ≥ 15; at (17, 23), ≥ 20.
- **BR-002** [stmt]: ≥ 43 in every characteristic. **BR-006** [stmt]: μ₁₀ ≥ 18 for det, so BR(det₄) ≥ 44 in
  characteristic 0.

**New since the last intake.** No new return (checkpoint 15 of 22 Nov is the newest anywhere on disk).
- **Codex's GCT_SEPARATIONS** (not opened; from the joint lemma space) states II.thm:finite-nonic, a named finite
  obstruction at (8, 9) in degree 54·10^51. That is a smaller degree than QC-019's 27·67·28^38 ≈ 4.5·10^57. Both are
  far beyond computation.
- **The VP ≠ VNP claims change nothing at (8, 9) or (17, 23).** Those separations were already known (L-gct-010: border
  dc(per₈) ≥ 32 > 9), and the claims' constants are ineffective.
- **S-004 is exactly the convention under which our integration note checked OpenAI's padding step.** It works with
  either pad.

**Open.**
- Q1a and Q1b: an explicit four-row separator, degree and equation at (8, 9) (second row ≥ 15) and at (17, 23) (≥ 20).
  4,214 labels remain.
- QC-019's certificate, to be recomputed by us.
- 44 for per₄: 10 ten-plane orbits remain.

**Relations.**
- **Our runs:** CUE_GCT R-14 (the range in which QC-019 lives); GCT_KRON F-016 = S-001, and F-025; BR_PENCIL
  (BR-ids).
- **The fleet:** L-gct-010, 012, 024. QC-014 is consistent with L-gct-024 (padded quaternary quartics have border
  dc ≤ 7).
- **Literature:** Landsberg-Manivel-Ressayre p. 476.

**Candidates.**
- **H13** (with S-002/S-003): prompt 58.
- **H14** (with QC-019): after the certificate.
- **A small note on QC-014:** after a literature check on the determinantal complexity of quaternary quartics.

**Problems** (from the intake, §1.5):
- S-001 calls itself an independent complete proof. It is F-016's argument.
- S-025's heading "an actual graded multiplicity gap" overclaims: the gap needs QC-019's upper bound.
- Q-BR10-EXACT was labelled proved at checkpoint 05 and corrected at checkpoint 15.

## BR_PENCIL (prompt 44): border rank of det₄ and per₄ by multi-dimensional substitution

**Useful.** It was the best bound with a full proof at its time, and the method (R-01 substitution of j-planes, P-01
torus reduction to coordinate minima, P-06 anchored collections) is reusable. The value itself is superseded twice:
by GCT_OBS BR-006 (44 for det, characteristic 0) and by Codex's BORDER_RANK thm:52 (≥ 52, characteristics 0, 2, 3,
according to the joint lemma space; not opened).

**What it proved.**
- **R-01** [TPC]: BR(T) ≥ q − j + μ_j, with incidence closedness by EGA II 5.4-5.5.
- **P-01** [TPC]: torus reduction.
- **The chain of minima:** μ₂..μ₉ = 6, 8, 9, 11, 12, 14, 15, 16.
  - j ≤ 5: [TPC, COMP].
  - j = 7: 1,506 of 1,517 permanent orbits and 11 of 25 ideals were recomputed by the intake. **25 prolongation cases**
    rest on the run's certificates only.
- **The bound:** BR(det₄), BR(per₄) ≥ 43 over C, and ≥ 42 over every algebraically closed field.
- **Mine [COMP]:** q = 36 as the 2|2-flattening rank of det₄ and of per₄; the chain values 40, 41, 41, 42, 42, 43, 43, 43;
  and μ_j − j nondecreasing.
- **R-06, R-11** [stmt]: BR ≥ C(n,2)² + 7 for every n ≥ 4 in characteristic 0.

**New since the last intake.** No new return.
- **Superseded numerically**, as above.
- **The VP ≠ VNP claims leave the result unchanged.** Our integration note names border apolarity, Koszul flattenings,
  substitution and P-01's torus degeneration as lower-bound tools for the asymptotic-restriction question at the claims'
  hinge (strict shortening; flat prices). Those are graph tensors with hubs.

**Open.**
- 44 and beyond: now in Codex's BORDER_RANK.
- 43 in every characteristic with unit minors.
- An independent recomputation of the 25 prolongation cases.

**Relations.**
- **Our runs:** GCT_GINEQ F-13/F-23 (the j = 1 case); GCT_OBS BR-ids.
- **The fleet:** P-01 is a candidate parallel to L-gct-139, riffle rank (PNP-MBR:A4).
- **Literature:** Landsberg-Michałek Prop. 2.3; Conner-Huang-Landsberg Prop. 2.1; Farnsworth (38, symmetric, det₄);
  Boij-Teitler and Landsberg-Teitler (Waring, a different quantity).

**Candidates.**
- **H03:** post the newest proved bound (prompt 59 = BORDER_RANK) with R-01 and P-01 as the method.

**Problems.**
- The numbering differs between `work\pencil\PENCIL_PROOFS.md` and the sections (P-08). Noted in the joint lemma space.

## GCT_GINEQ (prompt 27): Grothendieck's inequality and tensor norms

**Marginal, with one durable output.** The main question (norm-based rank bounds) is answered negatively and cleanly:
- F-05: nuclear²/Frobenius² ≤ rank fails for tensors;
- F-02, F-12: nuclear/operator certificates on one linear map inherit that map's rank barriers;
- F-19: no norm is GL-invariant.

The durable output is F-13/F-23 (border substitution in any order; an exact residual reduction), which seeded
BR_PENCIL.

**What it proved.** All 23 findings carry the intake's [TPC] (a17221e5), five of them also [COMP].
- **F-05.** Mine: re-proved. Spectral norm 1 by |tr ABC| ≤ ‖A‖_F‖B‖_F‖C‖_F, so the nuclear norm is 8 and the ratio
  is 8 > 7. It is a direct corollary of Derksen's ‖M_n‖_* = n³ (Found. Comput. Math. 2016).
- **F-01:** BR(T) ≥ ⌈b(T)^{1/(d−1)}⌉.
- **F-13:** BR(T) ≥ q + min_{u∈U} BR(u) − 1.
- **F-23:** min BR(u) = BR(T_b), so BR ≥ 39 for det₄ and per₄. Also det₅ ≥ 116, per₅ ≥ 115, det₆ ≥ 416, per₆ ≥ 415.
- **F-08:** two displays of Friedland-Lim v3 are false as printed (A = e ⊗ I_m gives m against 1; I_m gives m against
  √m). The conclusion eq:bdnn stands.
- **F-15 to F-22:** frameworks (an integral secant image, Koszul maps as sheaf morphisms, incidence closedness).

**New since the last intake.** No new return. The VP ≠ VNP claims change nothing, and they confirm GINEQ's barrier
picture. Neither proof uses norms. Both use ranks across varying cuts (Anthropic: spectral points, which are monotone
multiplicative functionals, not norms) and diagonalization. So F-19's obstacle does not bear on them.

**Open.**
- Q-30: certify α(U) outside the four families (the DPS hierarchy).
- The orbit maximum of α (a Kempf-Ness quantity).

**Relations.** BR_PENCIL (successor); the fleet's L-gct-139 (F-13 specializes to riffle rank 2n − 1); Landsberg-Ottaviani
(F-12); EGOW and Lovitz (barriers); Friedland-Lim v3.

**Candidates.**
- **A correction to report:** F-08, to Friedland and Lim (draft nothing here).
- No Hexagon note of its own; H03 has moved to the newer bounds.

**Problems.** None found.

## GCT_NSRH (prompt 24): Mulmuley's nonstandard Riemann hypothesis against sign-only purity

**Useful.**
- F03, F24 and F50 are a clean sign-only purity criterion, and it is posted (H01, hexagon:2611.00789, 21 Nov).
- F50 shows exactly where any such route must spend its effort.
- The rank-four negatives (F57, F58, F67) settle what form IV/VIII's positivity can take.

**What it proved.**
- **F03** [TPC]: path signs at unboundedly many lengths, a pointwise bound and a dual system give purity.
- **F24** [TPC]: real coefficients, even k. Two counterexamples were checked.
- **F50** [TPC, intake part 2]: the Gaussian encoding J_ψ(C) satisfies F03's sign hypothesis exactly at k = 2pr. The
  bounds hold iff C is pure.
  - Mine [COMP]: d_k = det tridiag(h/2, 1, h/2) = (h/2)^k U_k(1/h), and it is squarefree over F_p whenever p ∤ k + 1,
    for p ≤ 13 and k ≤ 40. The run's remark that the condition is not necessary (k = 2) is confirmed.
- **F26 and F42** [TPC]: no single finite Weil object carries the nonstandard traces.
- **F09; INT-NSRH-1 and INT-NSRH-2** (our intake's own results): positivity at rank three.
- **F57** [TPC, COMP]: a word of length 11 has trace with coefficient −1 at v^{±18} on N^#.
- **F58** [TPC]: a strictly positive basis cannot respect source cells.
- **F67** [TPC, COMP]: iterated tensor products fail.
- **F34** [TPC]: GCT VI Hypothesis 1.6.4(2) fails under compact binary input.
- F59: read in part. F60 to F69: statement level.

**New since the last intake.** No new return.
- H01 has been deposited.
- `reports_20261123\NONSTANDARD_RH_SLICES_20261123.md` sets this run in the nonstandard-RH programme.
- **The VP ≠ VNP claims are irrelevant here:** the nonstandard RH belongs to the flip, and the claims do not use the
  flip.

**Open.**
- The stalk gate. By F50 it is the whole task.
- Designated bases at rank ≥ 4, in signed or factored form only.
- F69 (filtered composition).

**Relations.**
- **Our runs:** GCT_POS N-ids (rank four answered); E4 consult (H23); ALPOGE_GCT (Alpöge's footnote 3 mechanism).
- **Literature:** GCT IV §11 (Remark 11.19, Prop. 11.6), GCT VIII Conj. 3.2, IV Conj. 19.1; Deligne Weil I Th. 1.6 and
  Weil II 3.3.1; SGA 4½ Sommes trig. 1.18; Blasiak.
- **Grothendieck:** weights and purity, the ℓ-adic formalism, the Lefschetz trace formula.

**Candidates.**
- H01 is done.
- **H23** (GCT VIII erratum): prompt 61.
- **The sign-only proof of |Gauss sum| = q^{1/2}:** possibly a short remark inside H01 v2.

**Problems.** N-006 (in GCT_POS) and F50 show that stalk purity of π*M(1) equals purity of M. A route that assumes one
to get the other is circular; the run says so itself.

## DP_MULT (prompt 34): divided powers in Alpöge's step 2

**Useful, but number theory, not GCT.** It answers Katz's 1977 divisibility question for every height under hypothesis
(H_h), and identifies the exponent of Alpöge's step 2 as the height-two slope.

**What it proved** (the intake ad855737, Claude Opus 5.5 at effort high, checked the following):
- **DP1** [TPC]: D^n f ∈ p^{max(0, ⌈c_h n − (h−1)⌉)}R[[t]], with c_h = 1/(p−1) − 1/(p^h−1). The constant h − 1 is
  optimal.
- **DP3** [TPC]: E_h(n) = Σ_{h∤j}⌊n/p^j⌋, sharp at p-powers.
- **DP34** [TPC]: Honda duals, with slopes p^i/(p^h − 1) and constant 1.
- **DP42** [TPC, with DP41 carried]: the mixed-line ceiling 1/(p² − 1).
- **DP6:** the height-two exponent.
- **DP51, DP64:** [stmt] and leading term respectively.

**Mine [COMP]**, on the Honda group of height 2 over Z₃, for n ≤ 170:
- DP1 and DP3 hold for f = t and f = t^8;
- t^8 attains the error h − 1 at n = 8, 16, …;
- v(D^9 t(0)) = 3 and v(D^81 t(0)) = 30, which equal c_h(q^r − 1) and E_2;
- at n = 8, Katz's ⌊np/(p² − 1)⌋ = 3 fails by one for t^8. This is the note's Theorem B.

**New since the last intake.**
- **The H09 note exists:** `reports_20261123\h09_note\h09_note_v4.tex`/`.pdf`, deposit sheet "not posted".
  - Checked by Claude Opus 5.5 at effort max (session ed7922ad, line by line, with an independent DP42 computation), by
    Claude Fable 5.2 at effort max (editor a3ccbc11) and by the main session 329fb1e6.
  - It reframes the result as Katz's question.
  - It says Bannai-Kobayashi already give c_h n − (h−1) for Lubin-Tate groups over unramified bases. So the new part is
    the generality (any formal group with (H_h), any p-torsion-free Z_(p)-algebra), the second bound, sharpness, the
    Honda-dual model and Theorem B.
- **The VP ≠ VNP claims:** no relation.

**Open.**
- Q3e: a global mixed-type family on a CM Jacobian with a net saving. The local ingredients DP54-DP65 went to
  ALP_MACHINE.
- Q5f: its statement was never supplied.

**Relations.**
- **Our runs:** ALP_MACHINE (prompt 49); ZETA_TWO ALP02 (refined by DP6).
- **Literature:** Katz 1977 and 1981 (Main Thm 3.11(I), Lemma 3.12); Bannai-Kobayashi; Hazewinkel; Lubin-Tate 1966; Tate;
  Zink; SGA 3 VII_A.
- **Grothendieck:** crystals and divided powers (cote 54, DP10: the boxed "p-th power zero" concerns the universal vector
  extension); Cartier duality; binomial rings as λ-rings with ψ^n = id (DP11).

**Candidates.**
- **H09:** post after the user's look at the PDF; the deposit sheet is ready.
- **Next prompt:** Q3e only if the ALP_MACHINE line needs it.

**Problems.**
- In the H09 note v1 (our text, not the run), Lemma 3.2's clause "since v_p(n!) ≥ (n−1)/(p−1)" was false. Claude
  Fable 5.2 at effort max found it and repaired it in v2; no statement changed.
- None in the run found by me.

---

## Things I could not do, or did not do

- **I did not open Codex's runs** (BORDER_RANK, GCT_SEPARATIONS, GCT_FLIP), as the brief says. Their numbers above come
  from `JOINT_GCT_LEMMA_SPACE.md`.
- **No literature or Hexagon novelty search** was done in this pass. It remains the first gate for H02b, H13, H14,
  H20/H21 and H09.
- **The PLETH check finished** for n ≤ 9: 47,866 coefficients, no mismatch (`checks_GCT/c7_pleth_output_n9.txt`).
