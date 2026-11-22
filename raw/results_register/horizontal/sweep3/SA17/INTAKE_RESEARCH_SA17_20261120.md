# Intake of RESEARCH_SA17 at checkpoint 12: the finishing run (cotes 126-133)

Taken in by Claude Opus 5.5 at effort max (agent ac8bd2a26d00b4f37) on 20 Nov 2026, from 19:27 UTC. This agent read
the Work folders K126-K132 in sweep 3, took in checkpoint 02 (`INTAKE_RESEARCH_SA17_20261119.md`), and built the
finishing prompt `pro_prompt_builds/RESEARCH_SA17_FINISH/PROMPT.md`. No sub-agents.

## 0. The return, and my scope

- **The run.** GPT-6 Astra (ChatGPT Pro mode) on the prompt RESEARCH_SA17_FINISH.
  - It started at 13:06:58 UTC on 19 Nov 2026 and continued from the first run's checkpoint 02.
  - This intake reads checkpoint 12, saved at 20:37 UTC: about 7 h 30 min into the finishing run.
- **The return folder:** `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA17_checkpoint_12_20261119T2037Z_unzipped/RESEARCH_SA17/`.
  - The report opens with INCOMPLETE.
  - The register has 271 rows. The sort is `field_experts/intake_20261120/SORTED/RESEARCH_SA17.md`.
  - My rows: all 271, in packets 29-33.
- **Scope: read in full, with the proofs.**
  - Part A of the finishing run:
    - `sections/A_finish_fpqc_solution.tex`, `A_finish_candidate.tex`, `A_finish_localglobal.tex`,
      `A_finish_L1_general.tex`, `A_finish_L2.tex` and `A_finish.tex`;
    - the opening of `A.tex`, with the statement of the conditions and A:8-literal;
    - the ink of 7° on scan 14 in the cote 131 transcription.
  - The 128 Théorème in every rank: `A45.tex` lines 395-787.
  - The nonvanishing detector: `B.tex` lines 1071-1200.
  - The run's gate section: `sections/unresolved.tex`.
- **Scope: carried from my cp02 intake.** These rows are unchanged since checkpoint 02 (diffed): `A.tex`,
  `A_gluing.tex`, and the cp02-checked parts of `A45.tex`, `C.tex` and `D.tex`.
- **Scope: statement level.** Everything else: 228 rows, among them the 187 C rows other than the three carried
  counterexamples, the B closure propositions, A5, D and the intermediate fpqc rows.
- **The record.** Section 1 gives the verdicts, and the appendix lists every row.
  - Check events: `INTAKE_RESEARCH_SA17_20261120_CHECK_EVENTS.tsv`, 43 rows.
  - The generating script: `intake_RESEARCH_SA17_20261120/make_rows.py`.

## 1. Verdicts, row by row

The check types are those of the check rubric. "Carried from cp02" means: the statement and its proof are unchanged
since checkpoint 02 (`sections/A.tex` and `A_gluing.tex` are byte-identical by diff), and my intake of 19 Nov checked
them as recorded there.

### 1.1 Part A: the representability programme (cote 131) and the descent notes (126-128)

**The main answer.** Grothendieck's Théorème of cote 131 scan 14, read as written, is false: the run gives a
counterexample. With the premise of 7° strengthened to pro-modularity, the theorem holds. I checked both proofs.
- **The ink of 7°** (transcription MPL_131, scan 14):
  - Grothendieck wrote "qui soit promodulaire", struck it, and inserted "tel que η soit modulaire", with the bracket
    "[on verra que cela implique: pro-modulaire...]".
  - So the literal 7° has an actual-modularity premise.
  - The corrected theorem restores his struck first wording. The run notes that scan 5 also uses the pro-modular
    premise.
- **The counterexample** is P(R) = α_p(R^h_(t)) over F_p[t].
  - Over F_p[[t]] there is no finite local pair that is actually modular. The test ring is
    A[u]_(m,u)[ε]/(ε²): the Artin-Schreier root f of f^p − f = tu has f ≡ 0 mod t in the henselisation, and εf is a
    section that no local map gives.
  - So the premise of 7° is never met, and 7° holds vacuously, while P is not representable.
  - The struck premise of 7° fails for P, as it must.

| Row | Run's status | My check | Outcome |
|---|---|---|---|
| A:main-counterexample | Refuted (the literal theorem) | targeted proof check | **confirmed.** Every condition checked: 1-3 (via A:hensel-fpqc and the gate proposition), 4 (Krull), 5 (t unit or nilpotent over an Artinian base), 6 (reduced henselisations), 7 vacuous (the εf test), 8 (t nilpotent at the generic point, or D(t) terminal); non-representability by henselian ZMT. One cited step not opened by me: de Jong-Olander, Theorem 2 (the étale equalizer over a henselian base). |
| A:hensel-remaining-gate | Proved | targeted proof check | confirmed, the same reading; the fppf refinement cites Stacks 37.48.2 (not opened) |
| A:hensel-fpqc | Proved | targeted proof check | confirmed. Strict-local case: e = (u⁻¹⊗1)(1+tc) is a separability tensor, A:fpqc-local-integral puts b in A, and D = (B⊗B_q)^h is faithfully flat over B. Then étale gluing and Zariski refinement. |
| A:fpqc-finite-module | Proved | targeted proof check | confirmed |
| A:fpqc-indecomposable-basechange | Proved | targeted proof check | confirmed (idempotent lifting by Hensel factorisation of χ_H; Brauer group of a separably closed field is 0; D_i ⊗_k K local for D_i/k purely inseparable) |
| A:fpqc-local-integral | Proved | targeted proof check | confirmed; sanity check by hand: a purely inseparable b ∉ k over a separably closed field k admits no such tensor, since Ann(b⊗1−1⊗b) lies in the kernel of μ |
| A:fpqc-hensel-kernel | Proved | targeted proof check | confirmed |
| A:pro7-representability | Proved under 7_pro | targeted proof check | **confirmed in its structure.** Induction on dim; the formal models B_i by 5 and 4; 7_pro makes (Z_i)_U → X_U étale; monomorphy by 6 and a trait. Two steps rest on rows I did not read: A:formal-gluing (gluing) and A:artinian-base's use of A:comparison. Necessity checked. |
| A:local-models-suffice | Proved under the local-representability hypothesis | targeted proof check | confirmed: constructibility of the étale locus by noetherian induction, with 8° over R/I^N and the uniform Artin-Rees lemma (N fixed by (R, I, C_R)); charts by the étale corollary; Stacks 02WW, 03KV, 0417 (cited, not opened) |
| A:uniform-AR | Proved | independent re-proof | confirmed (Artin-Rees K ∩ I^N R^d ⊂ IK, then Nakayama twice) |
| A:etale-finitefibres-qc | Known; deduction proved | targeted proof check | confirmed in its logic (the degree bound from the generic points is right); Stacks 086R and 07RY not opened |
| A:L1-general (L1) | Proved | targeted proof check | **confirmed.** M(T, η) ⊂ U (the open part of the Artinian formally étale locus) by contradiction at a generic point of a component of T − U; U → F étale chart, its image an open algebraic subspace and a scheme. No local models are assumed. The naive induction's error (modularity after a closed base change) is avoided as claimed. |
| A:actual-pro-generization | Proved | targeted proof check | confirmed (7° applied to the finite branch over Ô; fpqc descent of formal étaleness by the next row) |
| A:fpqc-open-formal-descent | Proved | targeted proof check | confirmed |
| A:generic-thickening-reflection | Proved | targeted proof check | confirmed (D_w → C_w iso mod I^N, then iso by uniform Artin-Rees; the étale variant through the finite étale extension D'_w) |
| A:L2-counterexample (L2) | Refuted | targeted proof check | **confirmed.** H(R) = {x : x^p = 0, x ∈ tRx} over F_p[[t]]. It satisfies 1-3, 5, 6 and 8, and the strengthened 4° for every complete noetherian adic ring (Krull on R/(tx)). It fails 7°: the zero section is actually modular at the closed point, but over F_p((t)) the test K[ε] has the extra section ε. |
| A:artinian-base | Proved under 1-5 | targeted proof check | confirmed, except the step through A:comparison (not read) |
| A:Murre-F8 | Proved | targeted proof check | confirmed (the generic component is Spec(A_p/J) with J ⊂ I_p; nonextension forces J = I_p; 8° gives W; local modularity forces I_w ⊂ J_w). It does not use N·I = 0. |
| A:unramified-corollary (Corollaire 2) | Known; reduction proved | targeted proof check | confirmed: the matching of 1-8, NR(a) and corrected NR(b) with Murre's (F1)-(F8), Theorem 1 (the source I opened on 19 Nov) |
| A:8-literal | Refuted literally; necessity with f.t. tests | targeted proof check (reread) | confirmed; carried from cp02 |
| A:NR-counterexample, A:NR-density | Refuted; Proved under hypotheses | carried from cp02 | confirmed there (example checked, proof read) |
| A:ind-thickening | Proved | carried from cp02 | confirmed there |
| A:artinian-tests, A:etale-corollary | Proved; Known with reduction | carried from cp02 | confirmed there (proof read; Murre Corollary 2 opened) |
| A:completion-descent (L3) | Known | carried from cp02 | confirmed against Murre 294 §4 Theorem (d), opened |
| A:nonfinite-descent | Refuted | carried from cp02 | confirmed there (Hironaka's 3-fold) |
| A:polarized-descent | Known | carried from cp02 | carried as background without fault found (SGA 1 VIII 7.7-7.8, not opened) |
| A:comparison, A:formal-gluing, A:localiso-qc, A:local-to-global | Proved (under stated hypotheses) | not read in full | statement level only, here and at cp02. A:formal-gluing and A:comparison carry the gluing step of A:pro7-representability and the comparison step of A:artinian-base. |
| A:hensel-adic-failure, A:hensel-L1-open | Proved | not read in full | statement level. The first says P fails the strengthened 4° for noetherian adic rings; it is consistent with the L2 example, which is a different functor. |
| A:fpqc-schematic-interior, A:fpqc-open-relation, A:fpqc-reduced-base, A:fpqc-nilpotent-base-reduction | Proved | not read in full | statement level; intermediate steps of the fpqc question, which the main proof of A:hensel-fpqc does not cite |

### 1.2 A.4 and A.5: the Théorème of cote 128, and projectivity

- **A.4: the Théorème of cote 128 survives in every rank. Confirmed by targeted check.** I read the full proofs of
  four rows:
  - A4:derivation-orbits:
    - the stabiliser of 0 is GL_r(S), S = ker δ;
    - after base change to k̄, the zero orbit is an orbit of the unipotent group 1 + M_r(rad D). It is closed by
      Kostant-Rosenlicht and has full dimension;
    - back over k, the fibres are Res_{S/k} GL_r-torsors, which are trivial over the Artinian semilocal S;
    - the converse follows by density for infinite k and by counting for finite k.
  - A4:finite-rank-equivalence: square-zero induction along the m-adic filtration.
  - A4:infinite-orbits:
    - column-finite matrices;
    - the operators R_i are jointly nilpotent, by the cycle construction and the trace argument on a simple module;
    - flat modules over an Artinian local ring are free in every rank.
  - A4:finite-descent-theorem:
    - (a) in every free rank, through B^(n);
    - (b) G_a by Krull, and GL_r by a Mittag-Leffler limit over the completion, then descent from the completion;
    - (c) flat base change over an Artinian A, with T-flatness proved through Tor.

  The theorem keeps apart one fixed rank, every finite rank and arbitrary free rank, as our prompt asked. It
  asserts no arbitrary-rank (b) over a non-Artinian base. The two lemmas (127 Lemma 1.3 true; 128 Lemma 1 false for
  every p) are carried from cp02.
- **A4:boundary-gate, A4:boundary-counterexample, A4:flatclosure-scope, A4:artinianflat:** statement level (the last
  changed only in its opening lines).
- **A.5** (A5:projectivity, A5:fixed-projective-space, A5:correspondences): statement level. The run's label is
  "Known under explicit projectivity convention"; Murre 294 §3 carries the same application.

### 1.3 Part B: Barsotti-Tate groups and Dieudonné crystals (cote 129)

- **B:finite-PD, the nonvanishing lemma behind the refutation of scan 114: independent re-proof by hand, confirmed.**
  - The detector: B_p = F_p[x,y,u,v]/(x³, x²y, xy², y³, xu, yu, xv, yv, u², v²), with basis
    1, x, y, x², xy, y², u, v, uv, and K = (x², xy, y², u, v).
  - xK = yK = 0, K² = F_p·uv and K³ = 0.
  - The divided powers are given by a product of six generating factors, for instance
    (1 + a x²T + a^p u T^p), each multiplicative in its coefficient. I checked:
    - additivity;
    - γ_n(rz) = r^n γ_n(z), using r^p = r_0^p for odd p, and r² − r_0² ∈ F_2x² + F_2y² for p = 2;
    - the product table (1,1), (1,p), (p,p), with the vanishing binomials by Lucas;
    - the composition γ_2γ_p = γ_{2p}, with coefficient (2p)!/(2(p!)²) ≡ 1, including 3 ≡ 1 mod 2.
  - τ maps to uv ≠ 0, on both presentations.
  - The run's program for p = 2, 3 (`code/B_finish_PD_detector.py`, log present) was not run by me.
  - The run's remark that Stacks Example 60.22.1 omits the term de·uv at p = 2 was not checked against Stacks (not
    opened).
- **B:crystal-counterexamples: the refutation of the unrestricted conjecture stands.** cp02's checks hold, and τ ≠ 0
  is now confirmed.
- **B:largest-literature-class, B:positive-closure, B:closure-reduction, B:PD-not-QSyn, B:positive-exclusion,
  B:reduced-PD-excellent, B:PD-two-generator-rejected: statement level.** The answer is a union, not a maximality
  theorem:
  - U = Q ∪ P_F ∪ P_E: quasisyntomic, reduced F-finite PD-torsion-free, and reduced excellent PD-torsion-free
    F_p-algebras.
  - Its closure properties are decided.
  - R_⋆ = k[a^{1/p^∞}, b^{1/p^∞}] ×_k k[c,d] is in P_F but not in Q, so the raw union is not stable under products
    or colimits.
- **The rest of B** (B:NiceV, B:NiceIV, B:DVR-classification, B:Delta, B:coLie-Dieudonne, B:L6-refutation,
  B:PD-bounds, B:square-zero-Hom, B:effectivity, B:positive-crystals, B:divided-target, B:base-kinds): statement
  level; B:Kummer is carried from cp02.

### 1.4 Part C: cote 133 (190 rows)

The run spent most of its 7 h 30 min here: 190 of the 271 rows are C rows. I read them at the level of the
statement, with the run's own gate section (`sections/unresolved.tex`) in full and the opening of
`sections/C4_finish.tex`. Three counterexamples are carried from cp02: C:local_charzero_counterexample,
C:isoclinism_counterexample and C:formal_Frobenius_counterexample. Their proofs lie in unchanged parts of `C.tex`.
- **C.1 (scan 29, "Est-ce vrai si k est un anneau local ?"): open, as the run says.**
  - Settled by the run:
    - the regular coherent criterion (C:regular-coherent-criterion): polynomial iff characteristic 0 and Z ≅ K_0(k).
      It covers every valuation domain of any rank;
    - square-zero thickenings A ⋉ J of characteristic-0 DVRs: polynomial iff multiplication by p is bijective on J.
      This is proved in residue characteristic 2 with any ramification, and at every p for unramified DVRs;
    - dyadic nodes xy = 2^n u: polynomial iff n = 1;
    - torsion of order 3 in the comparison kernel over a dyadic cubic thickening.
  - Open: an intrinsic criterion for singular rings of mixed characteristic (C:allrings_gate).
- **C.2 (C:distinguished_ring, C:lambda_failure, C:partition_formula):** statement level; unchanged from cp02 in
  substance.
- **C.3: the λ-criterion is settled (C:BO_affine_lambda), and split WG(BO_m) is determined over many families.** Open
  over arbitrary coefficient bases (C:BO_general_gate). The families determined:
  - finite commutative rings with 2 invertible;
  - all algebraic extensions of finite fields;
  - perfect fields with finite-dimensional coefficient algebras;
  - complete noetherian local rings with finite odd residue field;
  - global function fields, henselisations, and C1-type coefficients.
- **C.4: proved in the categories stated.**
  - C:formal-noncommutative-unipotent: over a perfect field, an extension of a connected p-divisible P by a solvable
    U of bounded exponent splits after [p^b].
  - C:baseline-free-realization: realisation of a prescribed centre and derived group without a baseline group.
  - I read the opening of the vector-kernel lemma (semisimplicity of multiplicative-type representations, additive
    linearisation of the action), not the rest.
  - For a commutative kernel the splitting is formal: p^N kills Ext¹(P, U). The content is the solvable,
    non-commutative case.

### 1.5 Part D: cote 130

D:rank and D:height are carried from cp02, where I checked them at statement level against my readings (ρ(X̃) − 2,
z = number of base points). `D.tex` changed only inside D:local. D:fixed, D:local, D:quotient-polarization,
D:elliptic and D:reducible-counterexample: statement level.

### 1.6 Counts

- Rows with a check event in this intake: 43 (`INTAKE_RESEARCH_SA17_20261120_CHECK_EVENTS.tsv`):
  - 24 targeted proof checks, confirmed. One of them, B:crystal-counterexamples, completes cp02's check of a
    refutation;
  - 2 independent re-proofs, confirmed (A:uniform-AR, B:finite-PD);
  - 17 carried without fault found: 16 checked in the cp02 intake and unchanged since, and A:polarized-descent
    (standard).
- Refuted by this intake: none. Gaps found: none in what I read. The unread dependencies are A:formal-gluing and
  A:comparison, and the étale equalizer of de Jong-Olander.
- Statement level: 228 rows, among them 187 C rows.
- The appendix lists every row.

## 2. What is new

Against the literature as far as I know it, without opening new sources (my context guard stood above 70 %). The run
claims no priority.
- **A:main-counterexample is new for us,** and I know of no published counterexample to the locally quasi-finite form
  of Grothendieck's criterion.
  - Murre 294 proves the unramified theorem, and its Note after Corollary 2 announces a locally quasi-finite analogue
    without stating its axioms.
  - P is not unramified (its closed fibre is α_p), so it contradicts no published theorem.
- **A:pro7-representability is a proof of that announced analogue,** with the pro-modular 7°, for every locally
  noetherian base. It uses no excellence hypothesis, unlike Artin's criteria, and it ends in a scheme through Stacks
  0417.
  - Whether a proof was published after 1965 (by Murre or in SGA 3) I have not searched.
- **A:L1-general (openness of the modularity locus under the literal axioms) and A:L2-counterexample:** new for us. L2
  was our own Lead (Claude's inference), and it is refuted.
- **A.4:** the cote 128 theorem in every rank, with the boundary comparison false for every p (cp02). Both are new for
  us. The all-rank argument (A4:infinite-orbits) is a self-contained nil-semigroup proof.
- **B:** the detector B_p, a clean finite certificate that τ ≠ 0 at every prime. The closure table of the literature
  union is new for us.
- **C.1, C.3 and C.4:** many new criteria for us (above), unread in their proofs.

## 3. Implications for the archive and the programme

- **Cote 131, scan 14, condition 7°: an edition note is needed.**
  - The literal theorem is false.
  - The ink has "qui soit promodulaire" struck and "tel que η soit modulaire" inserted. The theorem holds with his
    first wording, which scan 5 also uses.
  - His bracket "[on verra que cela implique: pro-modulaire...]" is right: modular implies pro-modular. What the
    proof needs is the converse, and P shows that the converse fails.
  - The reader's note at scan 14 should give P (A:main-counterexample) and the corrected theorem
    (A:pro7-representability).
- **Cote 131, scan 14, the margin "Est-ce que 7° est surabondant? Non, si on renforce aussi 4° au cas adique noeth.":**
  H shows that 7° does not follow even from the adic 4°.
  - Read as "No (7° is not superfluous), even with 4° strengthened", his "Non" holds in the strong form.
  - Read as our Lead L2 read it, it is refuted.
  - The reader's note should give H and say that the margin is ambiguous.
- **Cote 131, Corollaire 2 (scan 16):** proved through Murre's Theorem 1 with the corrected NR(b) (unique associated
  prime). "Intègre" against "irréductible" still needs a reader on the scan (cp02 intake, section 6).
- **Cote 128:** Lemma 1 (scans 20-21) is false for every p, but the Théorème (scans 26-30, (a)-(c)) holds in every
  rank by a proof through vanishing. The edition note on Lemma 1 should say both.
- **Cote 129 scan 114:** the conjecture is false in general (τ, now certified). It holds on the literature union U,
  whose exact closure properties are known.
- **Cote 133 scan 29:**
  - For number rings the answer reads "iff the class number is 1", since K_0(O_F) = Z ⊕ Cl(O_F).
  - In general the question is open for singular rings of mixed characteristic.
- **Cote 133 scan 36:**
  - (I) holds up to isogeny for solvable kernels of bounded exponent over perfect fields, and over F_p it fails for
    μ_{p^∞}-kernels.
  - The page states no base field, so the edition note should state both.
- **The programme.** Part A is closed: the main question is answered, with L1, L2 and both corollaries. What remains
  of SA17 is C.1 (singular mixed characteristic) and C.3 (arbitrary coefficient bases). Both are open-ended
  classifications, and they took most of this run's hours.

## 4. Bridges

The brief's corrected criterion: every row that treats weights, Tate twists, L- or zeta values, K-theory, motivic
cohomology or positivity, and every flagged row, gets one of three statements: what the bridge gives there, what the
row gives back, or why the link carries nothing. RH and GRH for Dirichlet L-functions are cited to L. Alpöge,
*Remark*, https://alpo.ge/remark.pdf (with the Lean archive). Purity is cited to Deligne, *La conjecture de Weil* I and
II.

1. **C:formal_Frobenius_counterexample (the flagged row: "rational Tate modules").** The link carries nothing beyond
   showing that the object is not motivic.
   - The row's p-divisible group is a twisted form of μ_{p^∞}² over F_p. On its character group, Frobenius acts by
     the unipotent [[1,1],[0,1]].
   - In that realisation this is the non-split self-extension of the unit object given by the nonzero class in
     H¹_cont(Gal(F̄_p/F_p), Q_p) = Hom(Ẑ, Q_p) ≅ Q_p ("Frobenius ↦ 1").
   - Among motives over F_p the corresponding Ext¹(Q(0), Q(0)) = H¹_M(F_p, Q(0)) is 0. Every rational motivic
     cohomology group of a finite field vanishes outside H⁰(Q(0)); for K-theory this is Quillen's finiteness of
     K_*(F_q).
   - So the counterexample has no motivic counterpart.
   - Purity (Deligne) bounds the absolute values of Frobenius eigenvalues. Here they are 1, of weight 0, consistent
     with purity. Purity says nothing about semisimplicity, and the failure here is non-semisimplicity.
   - For the p-divisible groups of abelian varieties over F_q, Frobenius is semisimple (Weil, Tate). There, (I) and
     (II) up to isogeny follow from Poincaré reducibility.
   - RH and GRH (Alpöge) give nothing here, and the row gives nothing back.
2. **Part B (Barsotti-Tate groups, Dieudonné crystals: slopes and weights).** The link carries nothing for these rows.
   - The slopes of a BT group are its p-adic weights. For A[p^∞] of an abelian variety over F_q they are the
     p-adic valuations of Weil q-numbers of weight 1 (Weil for abelian varieties; Manin). Deligne's purity extends
     the weights to crystalline cohomology of smooth projective varieties (Katz-Messing, through Deligne).
   - The B rows decide full faithfulness and the Hodge-filtration classification over bases that are not finite
     fields (F_p[x,y]/(x,y)², two planes, quasisyntomic and F-finite rings, p-adic rings).
   - Their invariants are integral and torsion: τ has pτ = 0, and the Kummer obstruction lives at p = 2. Frobenius
     eigenvalues do not occur.
   - Neither RH, nor GRH, nor purity gives anything there, and the rows give nothing back.
3. **Part D (cote 130: heights, local symbols, Shioda's formula). Here the bridge carries.**
   - D:rank is the Shioda-Tate formula: rank MW(J') = ρ(X) + H² − 2 minus the reducible-fibre excess. ρ(X) is the
     rank of the Tate classes in H²(X̄, Q_ℓ(1)).
   - **What purity gives there.** Over a finite field, Deligne's purity puts every Frobenius eigenvalue on
     H²(X̄, Q_ℓ) on |α| = q. The Tate classes are the eigenvalues q·(root of unity).
   - With Tate's unconditional inequality, ρ(X) is bounded by the order of the pole of ζ_X at s = 1. Through the
     rank formula:
     - rank MW(J') ≤ ord_{s=1} L(J'/k(t), s), the function-field inequality of Birch and Swinnerton-Dyer;
     - equality is equivalent to the Tate conjecture for X (Tate 1966, Milne 1975).
   - **What the row gives back.** D:height and D:local give the height pairing and its local corrections: the
     regulator in the leading term of that L-function, with the component-group pairing of SGA 7 IX.
   - Alpöge's RH and GRH for Dirichlet L-functions do not reach these L-functions, which belong to elliptic
     surfaces over finite fields.
4. **C.1 (K_0 of number rings).** The link carries little.
   - For k = O_F the run's criterion (regular, characteristic 0, Z ≅ K_0) reads h_F = 1.
   - The class number is the K_0-part of the leading term of ζ_F at s = 0, which is −hR/w.
   - **What GRH gives there.** Alpöge's GRH for Dirichlet L-functions gives Littlewood's effective
     L(1, χ_d) ≫ 1/log log |d|. So h(−d) is effectively bounded below, which was known unconditionally for class
     number 1 (Heegner, Baker, Stark: nine fields).
   - Bach's bound (Cl(O_F) generated by primes of norm ≤ 12 (log |d_F|)²) needs GRH for the Hecke L-functions of
     class-group characters. For abelian F these are Dirichlet L-functions only when the Hilbert class field is
     abelian over Q.
   - Neither statement decides the criterion in general, and the rows give nothing back to L-functions.
5. **C.2 and C.3 (λ- and Adams operations, Grothendieck-Witt and representation rings: the K-theory side).** The link
   carries nothing.
   - The rows concern K_0 of representation and hermitian categories over coefficient rings, where the Adams
     weights are the degrees of symmetric functions.
   - Special values of ζ and L-functions enter through the higher groups K_{2n−1}(O_F) (Borel, Lichtenbaum,
     Beilinson). No row computes those.
   - The global-function-field rows use class field theory and the Hasse principle for hermitian forms, not
     L-functions. I searched every section file for zeta functions, L-series, Chebotarev, purity, weights and
     Deligne: the only hits are the flagged row and a "Weil extension theorem" (for rational maps into group
     schemes) in A5.
6. **Part A (representability, descent).** No row treats any of the listed objects; the link carries nothing.

## 5. Prompt updates

For a successor of this run:
- **Drop Part A and Part B as items.** Their main questions are answered and checked here. Carry three things as
  statements to check, not as background:
  - A:formal-gluing and A:comparison, which carry the gluing and base steps of A:pro7-representability and
    A:artinian-base;
  - the étale equalizer of de Jong-Olander, Theorem 2, which A:hensel-remaining-gate cites;
  - B:PD-not-QSyn and the closure table of B.3, read by no second party.
- **C.1:** state the gate exactly as C:allrings_gate and `sections/unresolved.tex` give it.
  - The object to find: an intrinsic criterion for singular rings of mixed characteristic.
  - Give the families already solved (above) as background.
  - Name the approaches that stalled, which the run records:
    - the MCM comparison (C:odd-node-MCM-comparison-boundary);
    - the relative Swan-MF category, whose Grothendieck group is uncomputed (C:relative-Swan-MF-bridge);
    - the cyclotomic cancellation at lower ramification height.
- **C.3:** say what "arbitrary coefficient bases" means: every commutative ring with 2 invertible, or every
  noetherian one. Say what form the answer takes: generators and relations of split WG(BO_m), and its operations.
  Without that, the item has no finishing line, and this run produced 190 rows without closing it.
- **Edition notes** for the readers of cotes 128, 129, 131 and 133, from section 3, with the statements cited by
  label and page of the run's paper.
- **A successor intake of the 228 rows read here at statement level,** most of them C rows, by a reader of cote 133.
  My reading here is Part A in full and the main rows of A.4 and B.3.

## Appendix: every row, with what this intake did

Generated by `intake_RESEARCH_SA17_20261120/make_rows.py` from the sorted register. The verdicts and check types are
in the check-event TSV.

| Row | Run's status | This intake |
|---|---|---|
| A:NR-counterexample | Refuted | carried (checked earlier or standard) |
| A:NR-density | Proved under stated hypotheses | carried (checked earlier or standard) |
| A:ind-thickening | Proved | carried (checked earlier or standard) |
| A:completion-descent | Known | carried (checked earlier or standard) |
| A:8-literal | Refuted literally; corrected necessity proved | targeted check, confirmed |
| A:artinian-tests | Proved | carried (checked earlier or standard) |
| A:etale-corollary | Known; reduction proved | carried (checked earlier or standard) |
| A:nonfinite-descent | Refuted | carried (checked earlier or standard) |
| A:polarized-descent | Known | carried (checked earlier or standard) |
| A:comparison | Proved under stated hypotheses | not read in full: statement level |
| A:formal-gluing | Proved under stated hypotheses | not read in full: statement level |
| A:localiso-qc | Proved | not read in full: statement level |
| A:local-to-global | Proved under stated hypotheses | not read in full: statement level |
| A:artinian-base | Proved | targeted check, confirmed |
| A:Murre-F8 | Proved | targeted check, confirmed |
| A:unramified-corollary | Known; reduction proved | targeted check, confirmed |
| A:uniform-AR | Proved | independent re-proof, confirmed |
| A:etale-finitefibres-qc | Known; deduction proved | targeted check, confirmed |
| A:local-models-suffice | Proved under stated hypothesis | targeted check, confirmed |
| A:pro7-representability | Proved with explicitly strengthened condition7 | targeted check, confirmed |
| A:hensel-adic-failure | Proved | not read in full: statement level |
| A:hensel-remaining-gate | Proved | targeted check, confirmed |
| A:L2-counterexample | Refuted | targeted check, confirmed |
| A4:artinianflat | Known; additional assertion proved | not read in full: statement level |
| A4:flatclosure | Proved | carried (checked earlier or standard) |
| A4:flatclosure-scope | Proved | not read in full: statement level |
| A4:boundary | Proved | carried (checked earlier or standard) |
| A4:boundary-gate | Proved distinction; finite theorem proved | not read in full: statement level |
| A5:projectivity | Known; consequence proved | not read in full: statement level |
| A5:fixed-projective-space | Proved counterexample | not read in full: statement level |
| A5:correspondences | Proved | not read in full: statement level |
| D:fixed | Proved | not read in full: statement level |
| D:rank | Proved | carried (checked earlier or standard) |
| D:local | Proved; comparison Known and derived | not read in full: statement level |
| D:height | Proved with explicit normalization | carried (checked earlier or standard) |
| D:quotient-polarization | Proved | not read in full: statement level |
| D:elliptic | Proved | not read in full: statement level |
| D:reducible-counterexample | Proved counterexample | not read in full: statement level |
| A4:boundary-counterexample | Proved counterexample | not read in full: statement level |
| A4:derivation-orbits | Proved | targeted check, confirmed |
| A4:finite-rank-equivalence | Proved | targeted check, confirmed |
| A4:infinite-orbits | Proved | targeted check, confirmed |
| A4:finite-descent-theorem | Proved | targeted check, confirmed |
| A4:all-primes | Proved counterexample | carried (checked earlier or standard) |
| A:fpqc-schematic-interior | Proved | not read in full: statement level |
| A:fpqc-open-relation | Proved | not read in full: statement level |
| A:fpqc-reduced-base | Proved | not read in full: statement level |
| A:fpqc-nilpotent-base-reduction | Proved | not read in full: statement level |
| A:hensel-L1-open | Proved | not read in full: statement level |
| A:fpqc-open-formal-descent | Proved | targeted check, confirmed |
| A:actual-pro-generization | Proved | targeted check, confirmed |
| A:generic-thickening-reflection | Proved | targeted check, confirmed |
| A:L1-general | Proved | targeted check, confirmed |
| A:fpqc-finite-module | Proved | targeted check, confirmed |
| A:fpqc-indecomposable-basechange | Proved | targeted check, confirmed |
| A:fpqc-local-integral | Proved | targeted check, confirmed |
| A:fpqc-hensel-kernel | Proved | targeted check, confirmed |
| A:hensel-fpqc | Proved | targeted check, confirmed |
| A:main-counterexample | Refuted | targeted check, confirmed |
| B:PD-bounds | Proved | not read in full: statement level |
| B:square-zero-Hom | Known, with the needed uniform bound proved | not read in full: statement level |
| B:effectivity | Known, with the nonnoetherian comparison explained | not read in full: statement level |
| B:NiceV | Proved | not read in full: statement level |
| B:Kummer | Proved | carried (checked earlier or standard) |
| B:NiceIV | Known | not read in full: statement level |
| B:positive-crystals | Known | not read in full: statement level |
| B:divided-target | Known | not read in full: statement level |
| B:finite-PD | Proved | independent re-proof, confirmed |
| B:crystal-counterexamples | Refuted | targeted check, confirmed |
| B:base-kinds | Proved consequence | not read in full: statement level |
| B:Delta | Proved | not read in full: statement level |
| B:coLie-Dieudonne | Proved | not read in full: statement level |
| B:L6-refutation | Refuted | not read in full: statement level |
| B:DVR-classification | Known classification; explicit deduction proved | not read in full: statement level |
| B:largest-literature-class | Determined union; all requested closure properties proved or | not read in full: statement level |
| B:reduced-PD-excellent | Proved from cited theorems | not read in full: statement level |
| B:positive-closure | Proved | not read in full: statement level |
| B:closure-reduction | Proved equivalence; all four equivalent conditions refuted b | not read in full: statement level |
| B:positive-exclusion | Proved | not read in full: statement level |
| B:PD-two-generator-rejected | Proved | not read in full: statement level |
| B:PD-not-QSyn | Proved; root targeted audit passed | not read in full: statement level |
| C:Qalgebras | Proved | not read in full: statement level |
| C:positive_characteristic | Proved | not read in full: statement level |
| C:local_charzero_counterexample | Refuted | carried (checked earlier or standard) |
| C:DVR | Known for Z; reduction proved for DVR | not read in full: statement level |
| C:allrings_gate | Open | not read in full: statement level |
| C:distinguished_ring | Proved | not read in full: statement level |
| C:lambda_failure | Refuted | not read in full: statement level |
| C:partition_formula | Proved | not read in full: statement level |
| C:charzero_lambda | Proved | not read in full: statement level |
| C:orthogonal_representation_ring | Proved | not read in full: statement level |
| C:BO_general_gate | Open | not read in full: statement level |
| C:odd_characteristic_failure | Refuted | not read in full: statement level |
| C:hyperbolic_SW | Proved | not read in full: statement level |
| C:central_twists | Proved | not read in full: statement level |
| C:isoclinism_counterexample | Refuted | carried (checked earlier or standard) |
| C:formal_Frobenius_counterexample | Refuted | carried (checked earlier or standard) |
| C:formal_corrected | Proved | not read in full: statement level |
| C:normal_domain_counterexample | Refuted | not read in full: statement level |
| C:Specht_G0 | Proved | not read in full: statement level |
| C:regular_noetherian | Proved | not read in full: statement level |
| C:filtered_colimits | Proved | not read in full: statement level |
| C:BO_positive_failure | Refuted | not read in full: statement level |
| C:algebraically_closed_WG | Known; specialization checked | not read in full: statement level |
| C:torsion_generic_kernel | Refuted | not read in full: statement level |
| C:field_WG_structure | Known; specialization checked | not read in full: statement level |
| C:allrings_injectivity | Proved | not read in full: statement level |
| C:allrings_obstructions | Proved reduction | not read in full: statement level |
| C:char2_boundary | Proved | not read in full: statement level |
| C:tame_degree | Proved | not read in full: statement level |
| C:regular_modular_locus | Proved | not read in full: statement level |
| C:Jordan_Adams_p | Proved | not read in full: statement level |
| C:BO_field_lambda | Proved | not read in full: statement level |
| C:BO_lowrank_base | Proved | not read in full: statement level |
| C:BO_affine_lambda | Proved | not read in full: statement level |
| C:BO_Qalgebra | Proved | not read in full: statement level |
| C:BO3_wild_gate | Proved reduction | not read in full: statement level |
| C:Bockstein_parity | Proved | not read in full: statement level |
| C:flat_nilpotent_kernel | Proved | not read in full: statement level |
| C:flat_nilpotent_infinite_kernel | Proved | not read in full: statement level |
| C:epsilon_Bockstein | Proved | not read in full: statement level |
| C:dualnumber_C2_ring | Proved | not read in full: statement level |
| C:divisible_nil_invariance | Proved | not read in full: statement level |
| C:divisible_nil_positive | Proved | not read in full: statement level |
| C:fibre_invisible_kernel | Proved | not read in full: statement level |
| C:reduced_regular_fibres | Proved | not read in full: statement level |
| C:BO3_not_finitely_generated | Proved | not read in full: statement level |
| C:three_cycle_length | Proved | not read in full: statement level |
| C:cubic_Bockstein | Proved | not read in full: statement level |
| C:cubic_three_torsion | Proved | not read in full: statement level |
| C:linear_nil_Bockstein | Proved | not read in full: statement level |
| C:squarezero_intrinsic_criterion | Proved | not read in full: statement level |
| C:ramified_squarezero_criterion | Proved | not read in full: statement level |
| C:derived_fibre_twins | Proved | not read in full: statement level |
| C:cyclic_linear_Bockstein | Proved | not read in full: statement level |
| C:unramified_flat_squarezero_allprimes | Proved | not read in full: statement level |
| C:modp2_Tate_Bockstein | Proved | not read in full: statement level |
| C:odd_torsion_heightzero | Proved | not read in full: statement level |
| C:curvature_length | Proved | not read in full: statement level |
| C:odd_torsion_allheights | Proved | not read in full: statement level |
| C:allprime_squarezero_criterion | Proved | not read in full: statement level |
| C:ramified_torsion_infinite | Proved | not read in full: statement level |
| C:unramified_torsion_infinite | Proved | not read in full: statement level |
| C:cyclotomic_torsion_cancellation | Proved | not read in full: statement level |
| C:cyclotomic_matrix_cancellation | Proved | not read in full: statement level |
| C:ramified_linear_Bockstein | Proved | not read in full: statement level |
| C:cyclotomic_flat_criterion | Proved | not read in full: statement level |
| C:cyclotomic_C3_lattices | Proved | not read in full: statement level |
| C:S3_cyclic_detection | Proved | not read in full: statement level |
| C:shallow_commuting_trace | Proved | not read in full: statement level |
| C:shallow_tangent_quotient | Proved | not read in full: statement level |
| C:cyclotomic_S3_lattices | Proved | not read in full: statement level |
| C:S3_isotypic_shallow_cancellation | Proved | not read in full: statement level |
| C:baseline-free-realization | Proved | not read in full: statement level |
| C:baseline-free-obstruction-example | Proved | not read in full: statement level |
| C:formal-noncommutative-unipotent | Proved | not read in full: statement level |
| C:formal-vector-splitting | Proved | not read in full: statement level |
| C:formal-unipotent-filtration | Proved | not read in full: statement level |
| C:formal-finite-kernel | Proved | not read in full: statement level |
| C:C1-coherent-products-WG | Proved | not read in full: statement level |
| C:C1_field_forms | Known; re-proved here | not read in full: statement level |
| C:C1_Galois_WG | Proved; independently audited | not read in full: statement level |
| C:C1_algebra_certificates | Proved; independently audited | not read in full: statement level |
| C:Om_effective_C1 | Proved; independently audited | not read in full: statement level |
| C:C1_tower_example | Proved; independently audited | not read in full: statement level |
| C:C1-henselization-access | Proved | not read in full: statement level |
| C:C1-henselization-WG | Proved | not read in full: statement level |
| C:function-field-henselization-WG | Proved | not read in full: statement level |
| C:Greenberg-congruence-decisions | Proved | not read in full: statement level |
| C:Greenberg-valued-algebra-decisions | Proved | not read in full: statement level |
| C:MF-Swan-transfer | Proved | not read in full: statement level |
| C:ramified-A2-MF-cancellation | Proved | not read in full: statement level |
| C:algebraic_field_arithmetic | Proved | not read in full: statement level |
| C:all_algebraic_fields_WG | Proved | not read in full: statement level |
| C:algebraic_fields_scalar | Proved | not read in full: statement level |
| C:artinian_algclosed_templates | Proved; independently audited | not read in full: statement level |
| C:artinian_algclosed_WG | Proved; independently audited | not read in full: statement level |
| C:finite_algclosed_algebra_WG | Proved; independently audited | not read in full: statement level |
| C:artinian_algclosed_example | Proved; bounded certificate passed | not read in full: statement level |
| C:finite-algebra-projectivity-descent | Proved | not read in full: statement level |
| C:artinian_perfect_Galois_indices | Proved | not read in full: statement level |
| C:artinian_perfect_WG_reduction | Proved | not read in full: statement level |
| C:perfect-residue-Artin-reduction | Proved | not read in full: statement level |
| C:artinian_effective_C1 | Proved | not read in full: statement level |
| C:artinian_effective_imperfect_C1 | Proved | not read in full: statement level |
| C:nonnoetherian-henselian-lifting | Proved | not read in full: statement level |
| C:effective-coherent-henselization-WG | Proved | not read in full: statement level |
| C:lexicographic-valuation-henselization-WG | Proved | not read in full: statement level |
| C:complete_Hom_detection | Proved | not read in full: statement level |
| C:complete_algclosed_indices | Proved | not read in full: statement level |
| C:complete_algclosed_WG | Proved | not read in full: statement level |
| C:complete_unbounded_detection | Proved | not read in full: statement level |
| C:integral-orthogonal-coalgebras | Proved | not read in full: statement level |
| C:complete-finite-canonical | Proved | not read in full: statement level |
| C:complete-finite-WG | Proved | not read in full: statement level |
| C:complete-finite-bounded-image | Proved | not read in full: statement level |
| C:complete-finite-products | Proved | not read in full: statement level |
| C:extended-henselian-products-WG | Proved | not read in full: statement level |
| C:finite-base-polynomial-equality | Proved | not read in full: statement level |
| C:Om-finite-base-algorithm | Proved | not read in full: statement level |
| C:Om-finite-base-form-example | Proved | not read in full: statement level |
| C:Om-finite-field-algorithm | Proved | not read in full: statement level |
| C:Om-finite-field-form-example | Proved | not read in full: statement level |
| C:function-field-pth-roots | Proved | not read in full: statement level |
| C:function-field-constant-bound | Proved | not read in full: statement level |
| C:function-field-factorization | Proved | not read in full: statement level |
| C:function-field-WG | Proved | not read in full: statement level |
| C:global-function-coefficient-WG | Proved | not read in full: statement level |
| C:global-function-henselization-WG | Proved | not read in full: statement level |
| C:global-function-field-arithmetic | Proved | not read in full: statement level |
| C:global-function-central-simple-algorithms | Proved | not read in full: statement level |
| C:global-function-finite-algebra-algorithms | Proved | not read in full: statement level |
| C:global-function-local-form-algorithms | Proved | not read in full: statement level |
| C:global-function-skew-hermitian-isometry | Proved | not read in full: statement level |
| C:global-function-hermitian-isometry | Proved | not read in full: statement level |
| C:henselian-finite-algebra-lifting | Proved | not read in full: statement level |
| C:effective-henselian-DVR-WG | Proved | not read in full: statement level |
| C:function-DVR-henselization-effective | Proved | not read in full: statement level |
| C:finite-field-henselization-WG | Proved | not read in full: statement level |
| C:flat-local-residue-reflection | Proved | not read in full: statement level |
| C:effective-henselian-flat-unions | Proved | not read in full: statement level |
| C:infinite-variable-henselian-WG | Proved | not read in full: statement level |
| C:henselian-global-field-arithmetic | Proved | not read in full: statement level |
| C:henselian-global-finite-algebra-algorithms | Proved | not read in full: statement level |
| C:henselian-global-coefficient-WG | Proved | not read in full: statement level |
| C:henselian-global-new-families | Proved | not read in full: statement level |
| C:henselian-minimal-form-bounds | Proved | not read in full: statement level |
| C:henselian-products-WG | Proved | not read in full: statement level |
| C:henselian-projective-decisions | Proved under stated hypotheses | not read in full: statement level |
| C:henselian-central-simple-algorithms | Proved under stated hypotheses | not read in full: statement level |
| C:henselian-hermitian-isometry | Proved under stated hypotheses | not read in full: statement level |
| C:division_binary_chain | Proved | not read in full: statement level |
| C:hermitian_scalar_presentation | Proved | not read in full: statement level |
| C:WG_hermitian_scalar_operations | Proved under stated hypotheses | not read in full: statement level |
| C:infinite-residue-henselian-arithmetic | Proved | not read in full: statement level |
| C:infinite-residue-henselian-WG | Proved | not read in full: statement level |
| C:infinite-residue-new-families | Proved | not read in full: statement level |
| C:integer-algebra-linear-algorithms | Proved | not read in full: statement level |
| C:arithmetic-henselization-WG | Proved | not read in full: statement level |
| C:splitWG-filtered-colimits | Proved | not read in full: statement level |
| C:finite-ring-powers | Proved | not read in full: statement level |
| C:finite-ring-powers-scalar | Proved | not read in full: statement level |
| C:locally-finite-equality-obstruction | Proved | not read in full: statement level |
| C:noncoherent-positive-boundary | Proved | not read in full: statement level |
| C:dyadic_residue_Bockstein | Proved; independently audited | not read in full: statement level |
| C:normal_trivialK0_kernel | Proved; independently audited | not read in full: statement level |
| C:dyadic_normal_node_criterion | Proved; independently audited | not read in full: statement level |
| C:odd-node-MCM-comparison-boundary | Proved | not read in full: statement level |
| C:NoetherDeuring_rational | Proved | not read in full: statement level |
| C:perfect_Galois_indices | Proved | not read in full: statement level |
| C:perfect_Green_image | Proved | not read in full: statement level |
| C:profinite-projective-data | Proved | not read in full: statement level |
| C:profinite-WG | Proved | not read in full: statement level |
| C:ramified_exponent_two_node | Proved; independently audited | not read in full: statement level |
| C:Schur-perfect-generation | Proved | not read in full: statement level |
| C:regular-coherent-criterion | Proved | not read in full: statement level |
| C:valuation-domain-criterion | Proved | not read in full: statement level |
| C:coherent-regular-modular-locus | Proved | not read in full: statement level |
| C:relative-Swan-MF-bridge | Proved | not read in full: statement level |
| C:separably-closed-effective-arithmetic | Proved | not read in full: statement level |
| C:separably-closed-coefficient-WG | Proved | not read in full: statement level |
| C:separably-closed-nonC1-family | Proved | not read in full: statement level |
| C:shallow-commuting-translations | Proved | not read in full: statement level |
| C:shallow-full-support-three-torsion | Proved | not read in full: statement level |
| C:arithmetic-strict-henselization-access | Proved | not read in full: statement level |
| C:arithmetic-strict-henselization-WG | Proved | not read in full: statement level |
| C:canonical-polynomial-elimination | Proved | not read in full: statement level |
| C:canonical-tuples | Known; specialization checked | not read in full: statement level |
| C:Om-canonical-templates | Proved | not read in full: statement level |
| C:Om-canonical-WG | Proved | not read in full: statement level |
| C:Om-canonical-example | Proved | not read in full: statement level |
