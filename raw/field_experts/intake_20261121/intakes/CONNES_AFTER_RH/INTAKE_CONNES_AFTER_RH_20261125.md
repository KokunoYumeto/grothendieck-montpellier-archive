# Intake: CONNES_AFTER_RH (prompt 68, reworked), checkpoint 07

- **Intake:** 25 Nov 2026, by Claude Opus 5.5 at effort high (agent a25c2acbb3a6f11f7), on the brief of main 329fb1e6
  (Claude Opus 5.5 at effort max), `agent_notes/INTAKE_NEW_RETURNS_BRIEF_20261125.md`.
- **The run:** GPT-6 Astra (ChatGPT Pro mode), on prompt 68 as reworked on 24 Nov (Connes's Lemma 3 in characteristic
  zero; then Q(√−3)). It was sent ~22:35 UTC on 24 Nov.
- **Checkpoint:** 07, 25 Nov 04:05 UTC,
  `grothendieck_archive_transcription_20261110/research_returns/CONNES_AFTER_RH_checkpoint_07_20261125T0405Z_unzipped/`.
- **What it contains:**
  - a 101-page paper (`workbench/paper/`, 24 source files), "The prolate trace formula over Q and Q(√−3), after Connes's
    Lemma 3";
  - CROSSWALK (79 statements, CA-001 to CA-079);
  - CHECK_EVENTS (174 rows);
  - LEDGER, QUESTIONS, LITERATURE and DEPOSIT_SHEET.
- **Earlier checks:** `who_checked.py --source CONNES_AFTER_RH` lists 127 ids. All their checks are the run's own: GPT-6
  Astra (ChatGPT Pro mode) sub-agents, at inherited effort, doing targeted proof checks and statement-only re-proofs.
  The run credits earlier checks of its imported AC-T lemmas (ALP_CONNES) to Claude Fable 5.2 at effort max (Gram,
  leakage, comparison) and to Claude Opus 5.5 at effort high (the conditional assembly and converse). This run was not in
  the pile.
- **Status rule:** every status below comes from what I read in this task. The type names are those of the check rubric.

## 1. Verdicts

### 1a. The main theorems

| Id | Statement | Verdict |
|---|---|---|
| CA-031 (`thm:main-dirichlet`, Thm 1.1) | For every primitive Dirichlet χ and h ∈ C_c^∞(ℝ): lim (2 log Λ·h(0) − Tr(Q_{χ,Λ}V(h))) = 𝔅_χ(h) = Σ_ρ m_ρ ∫H(iτ) dμ_{α_ρ,γ_ρ}(τ). μ_{α,γ} is the Poisson (harmonic) measure of the zero, a point mass if α = 0. With the principal polar correction for χ = 1. The defect measures converge against Schwartz tests with polynomial local mass. No hypothesis on zero location | **Holds as far as checked.** I checked the upper/local chain and the uniform-mass chain line by line (1b). The lower bound and Gram estimate (CA-003, CA-004) carry the run's checks and the earlier ALP_CONNES checks. The run's own statement-only re-proofs stop exactly at the upper/no-extra-defect estimate and the uniform mass; that is the part I checked. |
| CA-032 (`cor:main-adelic`, Cor 1.2) | Summed over a finite set of characters on the Bruhat test algebra: lim T_Λ(h) = Σ 𝔅_χ(h_χ). This equals Weil's distribution for every test iff RH holds for ζ and all primitive Dirichlet L-functions, so A (Alpöge) gives the trace formula | **Holds, given CA-031.** I checked the deduction: if every α = 0 then 𝔅 = 𝔚. Conversely, 𝔅 ≥ 0 on convolution squares, so 𝔚 ≥ 0, and Weil's criterion gives RH. The statement is Connes's; the run proves it for this cutoff. |
| CA-002 / CA-033 (band theorem, Thm 1.3) | \|𝔅(h) − 𝔚(h)\| ≤ 2𝒩_δ(h)·Σ m\|α\|/(1+γ²) ≤ 2δ𝒩_δ(h)Z₂ | **Independent re-proof by me**, from the statement, before reading theirs. For one zero, (1+γ²)·\|D\| ≤ 2\|α\|·𝒩_δ(h); the kink at t = 0 contributes 2\|α\|\|h(0)\|. Their proof agrees. |
| CA-025 (`prop:sign`) | For a reflected pair, (𝔅−𝔚) = −2∫h(t) sinh(a\|t\|)e^{iγt}dt, and this takes both signs on convolution squares | **Correct** (targeted proof check). It is the refined statement for the refuted Q04 (see 1d). |
| CA-001 (`thm:finite-packet`) | For a finite packet of zero jets at ±L, Tr(P_{F,L}C_φ) → Σ m_z ∫φ dμ_{a,γ}, with no location or simplicity assumption | **Correct** (targeted proof check). The Takenaka–Malmquist basis gives the Poisson densities, and the joint Gram matrix becomes block diagonal. Their remark is checked at Connes's text, see §3. |
| CA-059 (`thm:main-hecke`) | The same harmonic-measure limit for every finite-order Hecke χ of Q(√−3), for every fixed concentration threshold 0 < ν < 1 (½ included), via the Hankel transform; under a half-plane Re s > θ, \|lim − 𝔚\| ≤ 2δ𝒩_δ(h)Z_{2,χ} with δ = θ − ½ | **Carried as background without fault found.** I read the statement and the proof overview, not the proofs (CA-018 to CA-030, CA-040 to CA-058). The run's whole-chain targeted checks passed. Its statement-only re-proof is INCOMPLETE at the deep upper estimate and the uniform mass. The half-plane part is CA-002 applied with Z₂ ≪ log conductor (I checked that deduction). δ ≈ 0.37333 with Liu, 3/8 with Hu, 15/32 with Cureton–Thorner. |
| CA-067 (`hnew:theorem`) and CA-079 (`hnew:odd-artin`) | The fixed-threshold harmonic limit for every primitive holomorphic newform of weight k ≥ 1, every level and nebentypus; hence for every odd irreducible 2-dimensional Artin representation over Q | **CA-067: carried as background**, and it is the weakest of the main claims. The run's own independent re-proof is INCOMPLETE at the bulk (G3) and tightness (G4) steps. **CA-079: targeted proof check of the deduction only**: Khare–Wintenberger modularity, plus Deligne–Serre's equality of all Euler factors, gives L(s,ρ) = L(s,f). |
| CA-064 (`cor:artin-induced-cutoff`) | The cutoff for Artin representations induced from Hecke characters of Q(√−3) | **Correct as a deduction** from CA-059, since L(s, Ind χ) = L_K(s,χ). |

### 1b. What I checked line by line: the upper/local and mass chains over Q

**CA-005 (`thm:endpoint-local-criterion`).** Correct. The checked steps are:
- strong convergence τ_{−L}(1−Q_L)τ_L → P_{K₊} on ℋ₋ = M₊ ⊕ K₊;
- the upgrade to Hilbert–Schmidt convergence on fixed HS operators;
- the identification P_{K₊}B₊ = P_{K₊}C_a, by translating and projecting onto a finite packet (bulk term
  ≤ O(L^{−N})·(1+L)^d → 0, opposite boundary → 0);
- the asymptotic HS-orthogonality of the two endpoint terms;
- the additivity over P_L ⊕ (1 − P_L).

**CA-049 (critical-window packet).** Correct: the O(L^{−1}) estimate, the Gram block (1/(j+k+1)), and
Tr(G^{−1/2}D*GDG^{−1/2}) → Σ m\|a(γ)\|².

**CA-013 (`lem:local-prolate-interior`).** Correct:
- ‖(1−Π)f‖² ≤ C(‖(1−P)f‖² + ‖(1−B)f‖²), because the first omitted concentration eigenvalue is bounded below 1 at the
  Shannon index;
- the Fourier-separation tail;
- the H_D^{5/16} graph bound, for which the trivial convexity exponent 1/4 < 5/16 suffices.

**CA-014 (`lem:local-halfline-closure`).** Correct:
- the Beurling identification of the closed image as an inner multiple of H²;
- the principal family ψ = (u∂_u + 1)φ, whose Mellin transform (1−s)ζ(s)𝓜φ(s) cancels the pole at s = 1;
- no singular inner factor;
- no common delay (profiles near u = 1, where only n = 1 contributes);
- Burnol's Theorem 3.2 as the source.

**CA-006 (`thm:rational-local-limit`).** Correct. The checked steps are:
- the distribution b = a/L(½+iτ,χ) with the −i0 prescription at real poles;
- the kernel κ: a Schwartz tail at +∞, and at −∞ an exponential polynomial that the critical jets cancel;
- E_χT_L = C_aW_L;
- the Poisson identities E_χ = (τ(χ)/√q)J_qE_χ̄𝓕;
- the three-term residual decomposition;
- the input boundary S_LC_a(1−S_L);
- the principal-sector constraint repair (b_{Λ,±}, the constraint matrix → identity);
- verification of conditions 1–4 of CA-005.

Condition 3 rests on CA-004 at every polynomial rate, which I did not recheck.

**CA-038 (`lem:rectangle-parametrix`).** Correct:
- Jensen in a fixed disk gives N ≪ log H zeros;
- Harnack gives the reciprocal bound;
- averaging log min(1,\|x−γ_k\|) gives zero-free vertical strips of width ≥ H^{−C};
- the numerator of R_{T,j} is bounded through the divided-difference contour formula, with no inverse root gaps;
- the residue difference is a contour integral bounded on −A ≤ t ≤ 0.

**CA-039 (`lem:allpole-boundary-bound`).** Correct:
- the Newton-form coefficients are complete homogeneous symmetric functions of bounded nodes, ≤ C^N;
- each first-order inverse has kernel modulus ≤ 1 in the decaying orientation, keeps the support in [−L, L] by the
  zero moment, and has HS norm ≤ 2L;
- subtracting R_{T,j,+} leaves only the bounded triangle.

The model example F(z) = z² + a² is right: the kernel 1_{t<s} sinh(a(t−s))/a stays bounded as a → 0.

**CA-007 (`thm:unconditional-frequency-tightness`).** Correct:
- for L ≥ H^D, the bulk error H^C(1+L)^{C log H}e^{−c₀L} ≤ 1, because (log L)² ≪ L;
- below that, dμ/dτ ≤ L/π gives the polynomial bound;
- the discarded packet costs ≤ rank ≤ C log H;
- the masses are summed against Schwartz tests.

This is the moving-window gate that the run's own re-proofs did not reach. I found no fault.

### 1c. Carried as background without fault found

These were read at statement level, with the run's targeted checks:
- **The Gram and lower-bound inputs:** CA-003, CA-004, CA-008 (`prop:trace-compression`), CA-015, CA-016, CA-024,
  CA-036, CA-037 (the polar trace) and CA-063 (the polar rate).
- **The Hankel and Hecke chain:** CA-009, CA-017 to CA-023, CA-026 to CA-030, CA-040 to CA-048 (CA-048 is superseded
  by CA-059) and CA-050 to CA-058.
- **The holomorphic chain:** CA-068 to CA-078.
- **The comparison items:** CA-010 to CA-012, CA-034 and CA-035.
- **GLₙ:** CA-060 to CA-062, CA-065 and CA-066. These give a finite positive cutoff on the cuspidal norm-twist
  quotient, with an exact normalization-loss identity. The zero limit is open (Q23).

### 1d. Refuted, with refined statements

- **CONNES_AFTER_RH:Q04.** The proposed definite sign of 𝔅 − 𝔚 is refuted; the refined statement is CA-025, which I
  checked. Positivity holds for 𝔅 itself.
- **CONNES_AFTER_RH:Q20.** "Multiplicity obstructs a unitary realization" is refuted; the refined statement is EX-04
  (only a faithful self-adjoint realization of nilpotent jets is obstructed). Carried as background.

## 2. What is new

**Against the pile.**
- The pile held the old 68 (Connes's equivalence; board item H27, which the user decided not to post).
- It proposed a "68 v2": the exact limit of the cutoff defect as a sum over all zeros, with no hypothesis, for every
  primitive Dirichlet character, then over Q(ω) with the off-line band (INDEX §8, row 2; ORDER.md "REWORKED").
- **The run delivers both parts** and adds:
  - the natural threshold ½ for Hecke;
  - holomorphic newforms and odd 2-dimensional Artin representations;
  - a finite GLₙ cutoff.
- This is new against ALP_CONNES too. AC-T51 needed A through the inverse Gram bound. Here the limit is computed with no
  hypothesis, as a harmonic measure, and A enters only to identify it with Weil's distribution (Cor 1.2).

**Against the literature.**
- **Connes 1999.** §VIII Lemma 3 proves this in positive characteristic, and after (33) Connes asserts the analogue for
  ζ. I opened arXiv math/9811068 at l. 2059–2125 (pp. 44–45).
- **Fixed-scale or different objects:**
  - Meyer's nuclear formula (ordinary evaluation at zeros);
  - Connes–Consani's fixed-scale Sonin identity;
  - Burnol's closure theorem (the boundary space only);
  - Connes–Consani–Moscovici (prolate operators, spectral counting).
- **Searches:** the run's LITERATURE.md, one web search of mine, and a grep of the Hexagon dump (1,530 works) for
  prolate, Connes, harmonic measure and Sonin found nothing that computes this growing-projection limit in
  characteristic zero. Li's 2012 prolate/Sonine paper was not accessible to the run; it is the one item to open before
  posting.
- **As far as checked, the theorem is new:** Connes's Lemma 3 in characteristic zero, with every zero entering through
  its harmonic measure.

**A correction to Connes 1999.** In the proof of Lemma 3, Connes says the normalized vectors ξ_z "are asymptotically
orthogonal". For two zeros on the same side this is false: the limit inner product is
√((1−\|z\|²)(1−\|w\|²))/(1−z w̄) ≠ 0. The run's remark after CA-001 says so (its example: 2√(ab)/(a+b) for one
ordinate). The trace conclusion survives through the Blaschke basis, which the run supplies. This is a subtle point
with a correct conclusion; under our errata policy it is handled by the paper's own remark, with no separate note.

**Grothendieck's questions.** None is settled directly; this is our RH-through-Connes line, one of the user's unique
lines (P9821–P9823).

**Our open items.**
- ALP_CONNES Q1 ("identify the positive defect limit with W without zero location") is now answered in the right form.
  The limit is 𝔅, not 𝔚. It equals 𝔚 exactly under RH, which A supplies for Dirichlet characters.
- The cubic Kummer characters of Q(ω, ∛269) (ALP_CONNES §3) now have an unconditional cutoff limit (CA-059). Their RH
  is equivalent to 𝔅 = 𝔚 on these tests, and the band theorem bounds the difference by δ = 0.3733 (Liu). The gate H04.4
  is unchanged.

## 3. Consequences for the waiting prompts

`TO_SEND/PRO/1_Archive_research_by_topic/` is parked (ORDER.md, 25 Nov ~06:3x UTC). None of Q03 to Q11 concerns Connes's
programme, ζ or L-functions. I grepped each; the one hit, Q03 l. 141, is an unrelated GRH mention in a provenance line.
**No sentence of Q03–Q11 becomes more precisely statable through this run.** Nothing was edited.

For a successor of 68 (not in that folder), the questions the run leaves open are exact:
- **Q21:** even 2-dimensional and 3-dimensional Artin representations. They need their own archimedean, Gram, endpoint
  and mass estimates.
- **Q23:** the GLₙ zero limit. It needs the inverse-window-weighted boundary norm, quantitative zero jets, and the graph
  and mass estimates.
- **Q08:** uniformity in the set of places S.
- **Q18:** an estimate on the actual Weil operator (the ground ratio, the gap).

## 4. Candidates for Hexagon

1. **The rational theorem** (Thm 1.1, Cor 1.2, Thm 1.3, CA-001 and CA-025): Connes's Lemma 3 over Q for every primitive
   Dirichlet character, with no hypothesis, and the band estimate. A self-contained note of about 40 pages, cut from §§1–10
   of the paper. **Still needed:**
   - an independent re-proof or line-by-line check of CA-003 and CA-004 (the Gram and lower bounds at every polynomial
     rate; they rest on the Matomäki–Shao–Tao–Teräväinen Möbius estimate);
   - opening Li 2012;
   - the user's word, because H27 (the equivalence alone) was not to be posted. This is a different and stronger
     statement, but the user should decide.
2. **The Q(√−3) theorem** (CA-059), as part of the same note or a second one. **Still needed:**
   - a check of the Hankel chain (CA-018 to CA-030, CA-040 to CA-058), at least the deep upper estimate and the uniform
     mass, where the run's re-proof stopped.
3. **Holomorphic newforms and odd 2-dimensional Artin representations** (CA-067, CA-079). **Not yet:** the run's own
   independent pass leaves the bulk (G3) and tightness (G4) open. Hold until they are checked.
4. **The 101-page paper as staged** (DEPOSIT_SHEET). Not as it stands: it mixes checked and unchecked chains. Split it,
   or post it only after items 1–3.

Nothing was posted, no prompt or paper was edited, and no session was contacted.
