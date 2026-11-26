# Primer: the mathematics of AN_GRH as of its final return (23 Nov 2026)

This primer is by agent a28ea31f (Claude Opus 5.5 at effort max), for the main session to read after a compaction. It
restates the mathematics; it does not develop it.

**The run:** prompt 30, by GPT-6 Astra (ChatGPT Pro mode). Its final return was saved on 21 Nov 2026 at 08:21 UTC.

**The paper:** `grothendieck_archive_transcription_20261110/research_returns/AN_GRH_final_20261121T0821Z_unzipped/AN_GRH.tex`.
Ids below are the paper's Finding ids; line numbers refer to AN_GRH.tex.

**Intakes:**
- `INTAKE_AN_GRH_20261121_full.md`, by a28ea31f, 22 Nov, with 108 check events. This is the source of every check label
  below.
- af2a18f6's earlier intakes, `INTAKE_AN_GRH_20261121{,_part2,_part3}.md`, which recorded no check events.

**Check labels:**
- `[IRP]`: independent re-proof;
- `[TPC]`: targeted proof check, every step re-derived unless the entry says otherwise;
- `[COMP]`: computation by my own scripts in `_work_a28ea31f/`, never the run's;
- `[BG]`: carried as background.

No finding is refuted.

**The analytic inputs (lines 152-180, 512-532):**
- **A is Alpöge's theorem:** RH for every Dirichlet L-function, ζ included (20 Nov 2026, formalized in Lean). It is a
  theorem; cite it as one.
- **M is Masullo's draft claim:** GRH for the Hecke L-functions of every number field. It is unproved, so every use of
  it stays conditional.
- **Hooley's primitive-root theorem needs M, not A.** It needs Dedekind GRH for K_n(a) = Q(ζ_n, a^{1/n}), and K_3(2)
  already has the nonabelian group S_3. Alpöge's Dirichlet theorem therefore does not supply it.
- **Results stated "under Dirichlet GRH" are now unconditional.** These are T01, T07, and G05's first bound.

## 1. A05: A1 without A or M (lines 630-915) `[IRP]` Steps 1-2, `[TPC]` Steps 3-6

**Statement.** Let C be a smooth hyperbolic curve, proper or open, over a field K finitely generated over F_p; finite
fields are included. Let Π_C be its arithmetic fundamental group with the geometric kernel replaced by its maximal
prime-to-p quotient. Then distinct points of C(K) have sections of Π_C → G_K that are not conjugate.
- In characteristic 0 this is classical: the Abel map to the generalized Jacobian separates points.
- Section surjectivity is not claimed.
- The run calls A05 a checked reconstruction of the recovered later ANABELIAN_A1 run (A.2-A.5, A.14-A.19,
  A.30-A.33) and claims no originality.

**Proof.** Fix r ≠ p and pass to the cuspidally pro-r quotients.
1. **The relative configuration fibre is retained** (A05.1): 1 → F_c → E_c → Δ → 1 is exact. Here Λ = π_1(C−P) and
   Γ = π_1(C² − diag) give the topological fibration 1 → Λ → Γ → π_1(C) → 1.
   - Free-group lemma: if 1 → L → H → B → 1 with L free of rank ≥ 2, and H acts on L/[L,L]L^r through an r-group,
     then L^(r) → H^(r) is injective.
   - The reason: the Frattini kernel of Aut of a finite r-group is an r-group, and a nonabelian free pro-r group has
     trivial centre (Magnus embedding).
2. **Equal sections transport the cusp** (A05.2-A05.3).
   - The diagonal boundary has decomposition group 𝒟, with 1 → Z_r(1) → 𝒟 → Π_C → 1. Tame inertia comes from
     SGA 1 XIII 5.2. The full Z_r(1) comes from the Heisenberg test: a handle pair goes to 1+e12 and 1+e23 in
     UT_3(Z_r), so the boundary goes to 1+e13.
   - Conjugate sections s_P ~ s_Q then give β: G_P ≅ G_Q over id_{Π_C}, preserving cusp classes. Here G_P and G_Q are
     the maximal cuspidally pro-r quotients of π_1(C−P) and π_1(C−Q).
3. **Corresponding open covers have equal point counts.** The key lemma is I^(r) ≅ (I/N)^(r).
4. **β sends point decomposition groups to point decomposition groups**, by compactness over the finite sets of
   L-points X_H(L).
5. **The Kummer step.**
   - Set-up: [P−Q] ∈ J(k)[p^∞], and f has div f = p^e(P−Q). The cuspidally central quotients E_P and E_Q have kernel
     Z_r(1).
   - The comparison gives (A05.4): κ_r(f) = p^e·χ + κ_r(a).
   - At a good closed point R, Step 4 and ST2009 Lemma 1.7 (a proper section's decomposition group is its own
     normalizer) make χ a coboundary, so κ_{r,k(R)}(f(R)/a) = 0.
   - Since f is nonconstant, a good R with f(R)/a not an r-th power exists, which is a contradiction.
   - Saïdi-Tamagawa's finite exceptional set enters only as finitely many excluded auxiliary points.
6. **Finitely generated fields and open curves**: spread out and specialize (SGA 1 X 3.8-3.9).

**Inputs:**
- SGA 1 III 7.4, X 3.8-3.9, XIII 2.9-2.12 and 5.2;
- Weil I;
- Saïdi-Tamagawa, Publ. RIMS 45 (2009): Prop. 1.8(vi), Lemma 1.7 and Rem. 1.2.

It uses no GRH and no M.

**Good for:** Hexagon candidate H07. Over finitely generated fields of characteristic p, A05 removes Saïdi-Tamagawa's
exceptional set (ST2009 Prop. 1.8; ST2018, the introduction, pp. 4-5) for rational points. In the sources read on
22 Nov it is new. Stix, LNM 2054, Ch. 7 is unread because it is paywalled (intake §8).

## 2. Route 2: separation by one cyclic cover (A45-A52, A34)

**Common set-up and mechanism.**
- C/k has genus g ≥ 2 over a finite field of characteristic p, and P ∈ C(k).
- D → C is geometrically connected, étale and geometrically cyclic of odd degree n prime to p, with P' ∈ D(k) over P.
- A collision of the sections of P and Q gives Q' ∈ D(k) with δ = [Q'−P'] ∈ J_D(k)[p^∞] (A01, the covering
  formulation).
- An integral annihilator B of δ gives a function f with div f = B(Q'−P').
- Poonen's controlled field (Gonality, Prop. 2.1, Lemma 2.2, Cor. 2.3; `[BG]`) is generated by the deck translates of
  f, has index e > 1, and its curve Z has genus at most (d/e − 1)².
- The deck group acts freely on Z, so g(Z) = 1.
- The integral signs of B exclude identical image orbits: r_Q·B = −r_P·Bσ^{−j}, iterated through the odd order of
  σ^j, gives (r_Q^t + r_P^t)B = 0.
- So both orbits are totally and wildly ramified. That gives e | (coefficient gcd), e = p^a, and by Riemann-Hurwitz
  2ne ≤ 2n(g−1).
- Hence C_k̄ → E = Z/G has degree p^a ≤ g−1, totally ramified at P and Q, and D is the pullback of an étale cyclic
  Z → E.

**The results:**
- **A46, the rational primitive criterion** (lines 10396-10682) `[TPC]`.
  - Statement: if P_n(L)[p^∞] = 0, then the section of P differs from that of every other point of C(L), in every
    genus and every characteristic. Here P_n is the primitive conductor-n subvariety, P_n = im(p_n) with
    p_n = n·e_n = Σ c_n(a)σ^a ∈ Z[G] (Ramanujan sums), and the deck group need not be constant.
  - Corollary: a cover whose primitive factor has geometric p-rank 0 separates points.
  - Proof: B = A = ∏_{ℓ|n}(1 − σ^{n/ℓ}), with Ap_n = nA and 2^{ω(n)} coefficients ±1. Since M_n = 1, e | 1, which is
    a contradiction.
  - Hexagon gates: an independent re-proof, and the literature, which is not settled (§8).
- **A47, bounded primitive torsion** (10683-11019) `[TPC]`.
  - Statement: n > (2^{ω(n)}M_n − 1)², with M_n = exp P_n(k)[p^∞], forces the elliptic obstruction with e | M_n. So it
    separates whenever 2 ≤ g ≤ p, or whenever no such map is totally ramified at P.
  - Equivalently M_n < (√n + 1)/2^{ω(n)} (BP.15).
  - The coarse Weil bound M_n ≤ (√q+1)^{2r} can never supply it (BPW.1-4).
- **A45, the whole Prym with a nonconstant deck group** (9768-10395) `[TPC]`.
  - Statement: n > (2M − 1)², with M = exp B(k)[p^∞] for the connected norm kernel B, gives the same obstruction. It
    extends A34, which is the case of genus 2, characteristic 2 and a constant deck group.
  - Semilinear descent (SD.3): O_n ⊗_{R_n} M^F ≅ M and exp M = exp M^F. So a primitive conductor has the same exponent
    over k as over its deck field.
  - Degree-39 example on the twist Y² + X²Y = uX⁵ + uX⁴ + X³ + uX over F_4: exp_2 = 2 over F_4 and 16 over F_256. A45
    applies over F_4 (39 > 9); A34 fails over F_256 (39 ≤ 961). `[COMP]`, except (ND.19) and (ND.21)-(ND.22).
- **A34** `[TPC]` (genus 2, characteristic 2, constant deck group): n > (2M−1)² ⇒ separation. Per the abstract, an
  exact degree-19 example has M = 2.
- **A52, small integral annihilators** (12916-13494) `[TPC]`.
  - Statement: any A ∈ Z[G] with Aδ = 0, A(ζ_n) ≠ 0 and n > (‖A‖₁ − 1)² gives the obstruction.
  - In a Z_ℓ-tower there is a lattice bound (IA.14): n > (2·min{M_r, C_E·⌊W_r^{1/h}⌋} − 1)², with W_r the annihilator
    index.
  - Norm lower bound (TN.3): ‖A‖₁ ≥ W^{1/h}.
  - Trace relations factor through earlier levels (TN.6-TN.9).
  - An order jump gives a trace-zero differential (PD.2).
- **A48** `[TPC]`.
  - At least n − f_n ≥ n − (g−1)φ(n) of the n constant twists have no rational primitive p-torsion; in genus 2 that
    is n − φ(n) > 0.
  - But the P-split twist is unique, and pointing a good twist returns the pointed model's torsion (TW.5-TW.8).
- **A49, the variable-quotient supply** (11480-11818) `[TPC]`; its certificate was not rerun.
  - Set-up: genus 2, H a quotient of J_C(k) of odd exponent n with b(κ_P) = 0 and ⟨p,−1⟩ = (Z/n)^×.
  - Statement: F_H ≠ U_H in F_p[H] (OQ.3) iff some cyclic quotient's P-split Lang cover has a primitive factor with no
    rational p-torsion.
- **A50** `[COMP]` covers the limits of partial-packet projectors.
- **A51**, compatible classes in towers `[TPC]`:
  - (NC.15) bounds the number of rational generators, not their orders;
  - FX: completed group rings allow any exponent;
  - TD: in the fully transitive genus-2, characteristic-2 case, B(k)[2] = 0 iff the 2-rank is 0, and otherwise it has
    dimension 1;
  - WV: Weil restrictions show that weights and principal polarization allow exponent q^f.

**Good for:** a second, purely geometric route to A1 over finite fields once a suitable cover is supplied. Universal
supply is the open gate (§6).

## 3. Canonical-class detectors and the RM reduction

- **A29, the canonical-prime criterion** (4731-5044) `[TPC]`.
  - Statement: let C have genus 2 over F_q, and κ_P = [K_C − 2P]. If an odd prime r ≠ p has ord_r(p) even and
    (κ_P)_r ≠ 0, then there is a constant P-split cyclic cover of degree r^a over k whose primitive factor 𝒫 has
    p ∤ #𝒫(k). This separates P.
  - Mechanism: L_P(χ,T) = 1 + c₁T + q·χ(b(κ_P))T²; R ↦ ιR with [ιR−P] = κ_P − [R−P]; p^{ord/2} ≡ −1.
- **A33, reduction to real multiplication** `[TPC]`, plus `[COMP]` for its RM example. The genus-2, characteristic-2
  point-section assertion reduces to (DR.1): ordinary genus-2 E with Rosati-fixed O_5 = Z[(1+√5)/2] ⊂ End(J_E).
  - Mechanism: a quintic cover D → C, and a lift τ of the hyperelliptic involution with τστ^{−1} = σ^{−1}.
  - The reflection quotients E = D/τ have genus 2 and 𝓑 ~ J_E², with f_𝓑 ∈ {0, 4}.
- **A40, the inverse construction** `[TPC]`. Every ordinary E with T² + T − 1 = 0 and T† = T arises this way.
  - Construction: D_t = F_t*Θ − V_t, with F_t(P,Q) = T(z_P − z_t) − z_Q. D_t is integral and smooth for all but at
    most 34 values of t (A41), and has genus 6.
  - The D_5 action makes C = D/σ of genus 2, and D → C étale. Any R ∈ E is the image of a split lift.
- **A41 and A43** `[TPC]`, with `[COMP]` for A43's ring identities.
  - The A13 curve y² + y = x + 1/x + 1/(x+1) over F_2 is ordinary, with P_A = T⁴ − T² + 4.
  - Over F_128, every non-Weierstrass rational point R has ord[K_E − 2R] = 4159, and ord_4159(2) = 2079 is odd.
  - For at least 95 parameters, all five reflection images fail A29. This holds also for rank-one sources and both of
    their Weierstrass points (A43, via u = T − π of order 3).
- **A39** `[TPC]` `[COMP]`: on the A36 cover over F_256, three-primary detectors separate both Weierstrass points,
  through étale covers of degree 15 or 45. The Riemann-Roch rank certificate (155 of 155) was recomputed.
- **A37:** on the ordinary RM locus the generic curve's Raynaud theta support has no nonzero odd-order point.

## 4. The theta route of the Hooley proposal: accounting

- **A01:** the covering formulation; equal sections give equal Kummer classes.
- **A03:** the condition T(C): some prime ℓ with ord_ℓ(2) = ℓ − 1 has a nonzero ℓ-torsion point on the Raynaud Θ_B.
  Together with A01, it suffices.
- **A04, the density inference is false.** On the primes ℓ ≡ 1 (mod 8), of density 1/4, ⟨2,−1⟩ ≠ F_ℓ^×.
- **A06:** T(C) fails geometrically on an explicit genus-2 curve over F_{2^38}, by a six-prime obstruction.
  `[COMP]` for its finite content.
- **A11, the prime-power bridge:** if ⟨2,−1⟩ = (Z/ℓ^r)^× and Θ has a point of order ℓ^r, there is a cover whose
  primitive factor has 2-rank 0.
- **A15 and A18:** the composite and all-genus versions.
- **A07 and A21:** generic curves on the positive-rank strata avoid all nonzero odd orders.
- **A08, A19, A22, A35, A44:** finite prime avoidance and explicit fields. In A44, a 2-power tower has only finitely
  many eligible primes, S_A = {3,5} for A13; the odd-tower supplement is OT.
- **Explicit witnesses:** A09 (order 13, rank one), A13 (order 4159, ordinary), A16 (order 15), A31 (degree 7).
- **Failures of the numerical tests:** A23, A25, A27, A30, A36 and A38.
- **A42:** a Lang-cover equidistribution count.
- **A02, A17 and A24:** densities conditional on M.

## 5. The analytic findings

**Under M (conditional):**
- **G01:** under GRH for ζ_{L̃} and ζ_Q, a bounded prime p outside S with Frob_p ⊂ C.
- **G02 and G03:** trace comparison and an explicit uniform trace bound, with N = 2(q^{2d²} − 1).
- **G06:** y² = x³ − 3x ± 6 have surjective mod-ℓ image for ℓ > 964 log 6 + 5760. `[TPC]` for the Mayle-Wang constant
  only.

**Unconditional:**
- **G04:** Frobenius traces cannot separate extension classes; the cyclotomic-log counterexample.
- **G05, first part:** now unconditional by A. There is a prime q ∤ m with q ≡ 2 or 5 (mod 9) and
  q ≤ [72 log 3 + 24 log(4m) + 35]². Its second part is under M.
- **T01:** now unconditional by A. Primes p ∤ N with p < 3(log N)² generate (Z/N)^×, for N ≥ 3 (Bach).
- **T07:** now unconditional by A. Lamzouri-Li-Soundararajan v3, Thm 1.1, for N ≥ 3000.
- **T03 and T05:** coefficient-2 certificates without GRH: N = 2^a·3^b, and 53 moduli with 4,825 words. `[COMP]`
- **T02:** finite cyclotomic tests for GT̂_0.
- **T04:** the LM7_PUSH cusp moduli 24, 48, 96, 192, 36, 108, 324, 972 and 72.
- **T06:** the evidence boundary.

**Audit findings:**
- **S01:** the GRH draft's 13.3.1.2 has no statement.
- **S02:** the dependency rule.
- **R01:** 800 of 1,190 source rows recovered, with 591 proof blocks.
- **R02:** the RH/GRH flags are false positives.
- **R03:** fixed-prime criteria are not Artin-existence theorems.

## 6. Open rows and their gates

- **Universal supply for route 2.** Every prescribed (C, P) needs a pointed cover satisfying A46, A47 (BP.15) or A52.
  The gate is an arithmetic bound on the primitive exponent or annihilator index. This includes the ordinary RM case
  (DR.1) and literal primitive-rank-zero existence (the recovered A1 rows B.24, B.5 and B.32).
- **The Hooley route:** conditional on M; the universal T(C) is false by A06.
- **H07:**
  - read Stix LNM 2054, Ch. 7 (library);
  - read every page of the post text before submission.
- **A46:** an independent re-proof, and the literature (Pop-Saïdi, Sarashina).
- **Intake residue:**
  - A49's certificate;
  - A45's (ND.19) and (ND.21)-(ND.22);
  - the R01 and R02 counts;
  - A35's RM refinement;
  - the run's remark that Asvin 2023, Lemma 11 fails integrally. Its counterexample [ℓ]* = ℓ on H¹(E, Z_ℓ) is
    correct, but the paper itself was not checked.
- **The run's own audit is incomplete:** 390 register statements and 209 LM7 proof blocks are missing.

## 7. Where the results went

- **`field_experts/HEXAGON_CANDIDATES.md`:**
  - row H07 (A05), flagged to the user on 22 Nov;
  - A46, named as a new criterion.
- **Prompt 47 (KTOWER, sent)** carries:
  - A05 (cote 149, scans 35-36);
  - route 2 (A33-A52, with A46);
  - the final return folder and `INTAKE_AN_GRH_part3.md`.
- **The LM8_PUSH cp17 audit:** AN_GRH's verdicts on 304 LM8 rows are in §6 of the full intake.
