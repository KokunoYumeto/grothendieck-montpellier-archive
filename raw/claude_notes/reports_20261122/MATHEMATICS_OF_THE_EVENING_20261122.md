# The mathematics of the evening of 22 November 2026

Main session ed7922ad, Claude Opus 5.5 at effort max; written 22 Nov 2026 22:33 UTC at the user's request. It collects
the mathematics worked through this evening, before the exchange with Michel Hua about rights: what was proved or
computed here, what came in from the intakes, and what was withdrawn. Each item gives its check level. No human has
checked any of it.

Page numbers are printed pages; the scan number is one more (printed page p is scan p + 1).

---

## 1. Cote 54 and Alpöge's proof of RH

**On the sheet.** Printed 4 (scan 5), last two lines: « Je dis que F^A et F^B sont orthogonaux l'un de l'autre ». Printed
6 (scan 7) obtains it by transposing F and V, and displays

    0 → Gr(t_A) → pA → D(Gr(t_B)) → 0.

The case on the sheet is A[p^∞] for an abelian variety A.

**In the Lean proof** (leanprover-community/riemann-hypothesis, commit 40e56bab), the statement, for p-divisible groups,
is a dependency of `riemannHypothesis`:
1. `finrank_range_relFrob_dual_add_finrank_ker_verschiebung` (FinrankFrobeniusDualAddFinrankKerVerschiebung.lean,
   lines 10–32): ker V is the annihilator of the image of the dual's Frobenius, by the same transposition.
2. `height_le_finrank_cot_add_finrank_cot_dual` (HeightLeCotangentDimAddDualCotangentDim.lean:14) uses it toward
   height = dimension + dual dimension.
3. That equality is `hdk` in `window_matrices` (HasPeriodIntegral.lean:98). `omega` closes `d + k = G.height` with it
   (line 157), which makes the period matrices square; `sumIdx hdk` consumes it further on (EqSumEpsPairingSmul.lean).
4. These give `prismaticDieudonneHodge` and `farguesExact` (PrismaticDieudonneHodge.lean:19–28;
   FarguesExactOfPrismatic.lean:56). The latter is an argument of the covolume bound in
   `every_character_of_literature_of_vWin` (EveryCharacterOfLiteratureOfVWin.lean:812), from which `riemannHypothesis`
   follows.

**Check level.** Traced in the source by the main session. The Lean was not built, and it is not shown that the proof
could not avoid this step. The statement itself is classical (Hua's register: `54-frobenius-kernels-orthogonal`,
matched).

**Correction.** The boxed « puissance p-ième nulle » on the sheet concerns t_A^∨ of the universal vector extension and
holds for every abelian variety. It is not step 2's D^p ≡ 0 (DP10).

## 2. Step 2 of Alpöge's proof: height two

If D^p ≡ 0, as in step 2, then ker F = α_p on the CM curve, and the sequence of cote 54 makes E[p] an extension of α_p by
α_p, so the formal group has height two. For a formal group of height two,

    v_p(D^n f(0)) ≥ pn/(p² − 1) − 1,   and   p/(p² − 1) = 1/p + 1/p³ + …

is the exponent of step 2 (DP6, proved in the run DP_MULT, GPT-6 Astra in ChatGPT Pro mode, and checked at its intake).

**Computed (main session, exact rational arithmetic):** on y² = x³ + 1 for p = 5 and p = 11 (supersingular,
p ≡ 2 mod 3), with w = t³ + w³ and D = (1 − 3w²) d/dt: D^p ≡ 0 mod p, and the bound holds for n ≤ 60 and f = t, t², t³.
Three functions only. Script: reports_20261122/hua_reply_checks/defence_checks.py, part 3.

## 3. Cote 16: the sign behind a proof of RH over finite fields

**On the sheets.** Printed 33, last display: E^{n−1} ≅ Ker(φ_{n−1}: H^{n−1}(Y) → H^{n+1}(X)); printed 35, the corollary
Ker φ_* = E^{n−1}. Printed 49, lines 2–3: a deduction of the Weil conjectures from conjectures C and A. Printed 43 and
48: the Hodge index relation, and C + I(X × X) ⇒ semisimplicity.

**The sign identity.** Let X be smooth projective of dimension n over F_q, Y a smooth hyperplane section, F the
Frobenius. By weak Lefschetz and Poincaré duality, φ_*: H^j(Y)(−1) → H^{j+2}(X) is bijective for j ≥ n and onto for
j = n − 1, with kernel E^{n−1} there. The trace formula gives

    (−1)^{n−1} (q·#Y(F_q) − #X(F_q)) = Tr(F | E^{n−1}(−1)) + Tr(F | H^n(X)) + (terms from the degrees of X below n).

The two middle terms carry the same sign, so they cannot cancel as virtual modules: this is the mechanism of Alpöge's
footnote 3. On a power U^k of a smooth affine variety the lower degrees vanish, and the same kernel with compact supports
leaves

    (−1)^{D−1} R = Tr(F | H_c^d(U)^{⊗k}) + Tr(F | K),   D = kd.

For a generic hypersurface of the footnote's path form, Parseval bounds R, and letting k grow gives Deligne's bound.

**Checked (main session, exactly):** the identity on the quadric surface xy = zw with the section z = w (a conic;
E = 0, the trace on H²(X) is 2q) and on P³ with a split quadric as section (the trace on E(−1) is q², H³ = 0), for
p = 5, 7, 11, 13 (defence_checks.py, part 2).

**What it is not.** The sign is a parity of degree with no pairing, not the index form (HODGE_SIGN; SIGN_NEXT SN-14:
trace data alone cannot give the positivity of printed 48).

**Published.** The short proof of Deligne's bound by this route: hexagon:2611.00789, "A short proof of Deligne's bound
for Frobenius eigenvalues, after Alpöge" (first written by the main session; version 5 by Claude Fable 5.2 at effort
max, which also checked HODGE_SIGN independently). The research run on these sheets started at 00:14 UTC on 21 Nov and
returned a proof at 00:57; public 01:56; Hexagon 03:21.

## 4. The index relation on C × C is Weil's criterion

Let C be a curve of genus g over F_q, Γ_n the graph of F^n on C × C, D = Σ a_n Γ_n, h(x) = Σ a_n x^n and D₀ the
primitive part of D. From Γ_n·Γ_m = q^m #C(F_{q^{n−m}}) for n > m and Γ_n·Γ_n = q^n (2 − 2g),

    −D₀·D₀ = Σ_α h(α) h(q/α),   α over the eigenvalues of Frobenius on H¹(C).

With α = q^ρ the right side is Σ f(ρ) f(1 − ρ). It is ≥ 0 for every real h exactly when RH holds for C, and the Hodge
index theorem on C × C gives ≥ 0.

**Checked exactly (main session):** on y² = x³ + 3x + 1 over F_7, y² = x³ + x + 1 over F_5 (genus 1), y² = x⁵ + 2x + 1
over F_3 and y² = x⁵ + x + 1 over F_5 (genus 2), with 4,000 random integer h each, the form computed from point counts
equals Σ h(α) h(q/α): 0 mismatches, 0 negative values. An off-line pair of eigenvalues (3, 7/3) makes it negative
(defence_checks.py, part 1).

**What does not follow.** For ζ, Weil's criterion is the same inequality over the zeros of ξ, for real test functions.
The passage from the curve to ξ is Weil's analogy, not a proved map: the dictionary does not supply the surface that
C × C is here. (Correction of "it is exact" in our reply of 20:39 UTC; posted 21:31 UTC.)

## 5. Cote 1: the determinant theorem

**On the sheets.** Printed 70 (scan 71), Théorème 1: if u ∈ L¹(E), then (λ_i(u)) ∈ ℓ¹ and det(1 + zu) is of genus 0,

    det(1 + zu) = ∏ (1 + zλ_i(u)),   equivalently   α_n(u) = Σ_{i₁<…<i_n} λ_{i₁}⋯λ_{i_n}   and   Tr u = Σ λ_i(u).

On printed 78 (scan 79) the same statement as Théorème 2, with its boxed (20) det(1 + u) = ∏(1 + λ_i), is struck
through (seen on the facsimile); the margin keeps (22) and (23), Tr u = Σ λ_i(u).

**Printed 111.** The ink has θ between π/3 and π; the next line needs θ < π/2, as the margin's drawing shows. The π is a
slip on the sheet, and Hua's argument is right.

**Withdrawn.** MAS-10's operator R₊ with det(1 − wR₊) = Ξ(√w)/Ξ(0) on Masullo's weighted quotient was conditional on his
Theorem 10.2.2.1. Applied to ζ, the theorem gives only a reformulation (Hua's entry `1-lidskii-genus-zero`). Alpöge's
determinants are finite Gram, Capelli and period determinants, with a different sign (TRACE_DET).

## 6. Cotes 67–68

Printed 97–98 classify the real structures on elliptic curves; the hexagonal case is C/Z[ω] (Hua's reading rightly
corrects a = √3 to a = 3). The vertex and face reflections, with the lattice translations, generate the extended
(2,3,6) triangle group; its orientation-preserving half is the orbifold group of E/μ₆. That is the curve of Alpöge's
step 3. No use of the real structures in his proof was found.

## 7. Cote 149

The point-separation statement needs no GRH (AN_GRH, A05; an earlier run had proved it). The analytic inputs named on
20 Nov (Hooley's proof of Artin's conjecture, effective Chebotarev) need GRH beyond Dirichlet L-functions, which
Alpöge's theorem does not reach. "Masullo's claim reaches them" is withdrawn.

## 8. Masullo's draft

Not a proof. In MAS_ARTIN (GPT-6 Astra in ChatGPT Pro mode; MA-HM-001 and MA-HM-003 confirmed by Claude Opus 5.5 at
effort high, given GRH_NIGHT MT-M18 and M26), in the corrected model the step of §§12.3–12.4 on which the location of the
zeros rests, the every-width narrow return, is equivalent to RH for the function concerned. Vakil's update, about eight
hours after his post: problems reported, not accepted. In Tao's thread of 20 Nov: closer to Deninger's strategy than to
Connes's; a commenter places the gap at §12.3 (p. 514 is a heading "Include section"). By the user's rule, work in that
field is an independent construction from Alpöge's theorem, never a fix (memory masullo-not-a-fix).

## 9. Asvin G., "Tower of curves": Case B

Notation of the paper: Λ = Z_ℓ[[T]] with T = T_ℓ A; C of genus g, r = 2g − 2, d = dim A; Π the geometric pro-ℓ
fundamental group of C, K = ker(Π → T), X = K^ab.

**Criterion.** M_∞ is free over Λ if and only if d = 1 and ℓ ∤ deg f.
*Proof.* The invariant parts die in the limit under the traces, so M_∞ = X(−1), with or without saturation. The Fox
complex P: 0 → Λ → Λ^{2g} → Λ → 0 has homology Z_ℓ, X, 0, so X has generic rank r. The five-term sequence is
0 → ∧²T / Z_ℓ·f_*[C] → X_T → ker(T_ℓ Jac(C) → T) → 0, so X_T has rank d(2d − 1) − 1 + 2g − 2d = r + (2d − 1)(d − 1).
If X is free this must be r, so d = 1, and X_T has no torsion, so ℓ ∤ deg f. Conversely X_T = Z_ℓ^r, and Nakayama with
the generic rank gives X = Λ^r. (So the Abel–Jacobi map of a curve of genus ≥ 2 never gives a free module. The step that
fails is the end of the proof of Theorem 14: equal characters give an isomorphism with (R_n/N_n)^r only after ⊗ Q_ℓ.)

**The congruence of Theorem 19(3), for every d, granted Theorem 26.** The differentials of P lie in the maximal ideal, so
a semilinear lift of Frobenius (twisted by Z_ℓ(−1)) is invertible in each degree, with matrices F_0, F_1, F_2. At a
primitive character v of G_n, P has homology only in degree one, M_n(v). With k = k_n(v) and A^{(i)} the product of F_i
along the orbit,

    det(1 − yσ^k | M_n(v)) = det(1 − yA^{(1)}) / ( det(1 − yA^{(0)}) · det(1 − yA^{(2)}) ),

so h̃_n = r^{(1)}_n / (r^{(0)}_n r^{(2)}_n). Theorem 26 applies to the three free modules, the polynomials have constant
term 1, and one divides in Z_ℓ[[y]].

**The limit clause** after it does not follow from a congruence mod ℓ^n alone when b ≥ 2, since the normalization
divides by ℓ^{(n−n₀)(b−1)}: the sequence a_{n+1} = a_n^ℓ (1 + ℓ^n y) satisfies the congruences while its normalized
differences stay 1. For scalar Q the stronger congruence mod ℓ^{nb} makes the normalized logarithms converge. The
general case is undecided.

**Case A** is free: the group of C − f⁻¹{0, ∞} is free on r + 1 generators, and Crowell's sequence
0 → X → Λ^{r+1} → I → 0 has I ≅ Λ, so M_∞ is free of rank r. **Affine curves:** for a quotient T = Z_ℓ^b (b ≥ 1) of a
free pro-ℓ group on m generators, pd X = max(b − 2, 0), so X is free (of rank m − 1) iff b ≤ 2; this includes the tower
of Fermat curves.

**Check level.** Proofs by the main session; minimal generators computed mod ℓ for ℓ = 3, 5 and g = 2, 3
(asvin_freeness_second.py). A blind check by ad85573792c61a914 (Claude Opus 5.5 at effort high) agreed on Case A, the
Case B criterion and the congruence, with point-count tests. The affine statement is the main session's alone. Sent to
Asvin G. at 20:55 UTC (grant_evidence/outbox_20261122/04d_Asvin_G_reply_mathematics.txt).

## 10. The cubic sum (Codex's check request): confirmed

**Statement.** Fix m ≥ 1. For p ∤ 3·269·m let t(p) = #{x mod p : x³ ≡ 269} − 1. With z = (log y)², sum over squarefree
n in (y, 2y] with n ≡ 1 mod m whose prime factors all exceed z and are prime to 3·269·m, with weight
(log n) ∏_{p|n} t(p). Then the sum is O_{m,ε}(y^{1/2+ε}), unconditionally.

**Proof.**
1. For L = Q(∛269, ζ₃) with group S₃ and ρ its two-dimensional representation, the permutation representation on the
   roots of x³ − 269 is 1 ⊕ ρ, so t(p) = tr ρ(Frob_p) ∈ {2, −1, 0}.
2. Expand 1[n ≡ 1 mod m] in the characters χ mod m.
3. ρ = Ind_{Q(√−3)}^Q ψ for a cubic character ψ, so ρ ⊗ χ = Ind(ψ·(χ∘N)), and L(s, ρ⊗χ) = L(s, ψ') is the L-function
   of a nontrivial Hecke character of finite order: entire, with a functional equation of degree 2.
4. The rough squarefree series is F_χ = L(s, ψ')·H_χ. At the kept primes the Euler factor of H_χ is
   1 + (αβ − (α + β)²)X² + (α + β)αβX³, with no linear term; at the removed primes it is L_p⁻¹. Hence
   Σ |h(d)| d^{−1/2−ε} ≤ ∏_{p≤z} (1 + 2p^{−1/2} + p^{−1}) · O_{m,ε}(1) = exp(O(√z / log z)) = y^{o(1)}, because √z = log y.
5. For an entire degree-2 L-function with coefficients bounded by d(n), the partial sums are ≪ u^{1/2+ε} (Perron,
   the functional equation, Phragmén–Lindelöf; Landau's method gives u^{1/3+ε}).
6. Convolve, then partial summation for the weight log n.
No zero of any L-function enters: the bound comes from the functional equation, which is why it is unconditional and
why the primes alone, which are governed by the zeros, are not bounded by it.

**Numbers (m = 3):** |S|/√y ≤ 4.2 for y = 10⁵, 4·10⁵, 10⁶, 4·10⁶, 10⁷
(scratchpad cubic_check/cubic_sum.py). **Check level:** the main session alone; not checked by anyone else. Reply:
field_experts/intake_20261121/CLAUDE_TO_CODEX_CUBIC_CHECK_20261122.md. Codex's other claim (an upper bound for the
composites alone is equivalent to cubic RH under Dirichlet GRH) was not checked.

## 11. From the intakes of the evening

**ALP_CONNES, checkpoint 24** (intake by af2a18f62da23b48e, Claude Opus 5.5 at effort high; the run is GPT-6 Astra in
ChatGPT Pro mode):
- **S50, proof checked, under Alpöge's theorem.** Matrices built only from prime-side Weil pairings (finitely many
  primes at each stage) give real-rooted polynomials that converge to Ξ/Ξ(0) and recover every zero's multiplicity, with
  no zero data put in. It builds on Suzuki, arXiv:2610.32704; a novelty claim needs that comparison.
- **T51:** Connes's trace formula over Q is equivalent to Alpöge's theorem.
- **G114, proof checked:** strict Selmer vanishing at 269, unconditional. The unit certificate was recomputed; PARI's
  class number 7 was not rerun.
- **T15 and T17, re-proved independently:** they correct Morishita's Deninger–Connes–Consani preprint,
  arXiv:2508.15971, Theorem 2.2.8(2) and the surjection (2.2.7).
- **The four main gates have not moved:** H04.4, cubic RH, the T51 limit without zero location, and the lower bound
  on a₂.
- **Next questions:** a Lefschetz formula on the corrected Deninger space with spectral side AC-T46, abelian fields
  first; which of Connes–Consani's conditional F₁ statements follow from Alpöge's theorem; Alpöge's theorem through the
  BC/BCM systems; the a₂ bound.

**ALP_MACHINE, checkpoint 29** (intake by abcaba9b6ae84b747, Claude Opus 5.5 at effort high):
- **LIFT54 and LIFT55 stand.** Under Alpöge's formal size hypotheses, two lifts are impossible, the chain length m
  exceeds 2^7778, and m grows like x^{1/2+O(ε)}.
- **The support floor** of the all-top J⁵⁶ kernel rose from 12 to 18 (R057, R060, R062). R062's exponent,
  −726048945/4096, was recomputed, and its error sum is below 2^{−230}.
- **The open question** the run is being redirected to (follow-up 49b, ready): can step 8 be done with a chain of
  bounded length, by a replacement for `SizesAt`, or does the method force m → ∞?
- *Status at checkpoint 55 (23 Nov 15:05 UTC, intake by abcaba9b6ae84b747, Claude Opus 5.5 at effort high):* 49b was
  sent but not taken up by this run; the bounded-chain question is worked in NIGHT_AFTER_ALPOGE Part B. New: LIFT110,
  a literal instance of Alpöge's formal interface needs a coefficient field outside K^ab (proof checked). The finite
  signed gate now sits at support >= 28 (DO129).

**Codex's workshop**, reported by Codex and not checked by us beyond §10: under Dirichlet GRH, a one-sided bound on the
rough squarefree composites is equivalent to RH for ζ_{Q(∛269)}/ζ.

## 12. Withdrawn or corrected this evening

| What | Where | Why |
|---|---|---|
| MAS-10, R₊ with det(1 − wR₊) = Ξ(√w)/Ξ(0) | reply of 20:39, §3 | conditional on Masullo's draft, which is not a proof |
| "Masullo's claim reaches" the cote 149 inputs | comment of 20 Nov | same |
| "the map to ξ is exact" | reply of 20:39, §2 | exact on curves; the step to ξ is Weil's analogy |
| cote 1 at printed 78 | reply of 20:39, §3 | struck on the sheet; the live statement is printed 70, Théorème 1 |
| the cote 149 GRH pointer | 20 Nov | the statement needs no GRH |
| "the boxed zero p-th power is step 2's D^p ≡ 0" | defence, in chat | it concerns the universal vector extension, for every A |
| the doubt-mark counts at aef7db2 | reply of 20:39, §6 | rerun at 1edcf59; conclusions unchanged |

All corrections to what was posted went out in the follow-up of 21:31 UTC (comment 7086120487).

## Files

- reports_20261122/hua_reply_checks/: defence_checks.py, both_directions_nodraw.py and its JSON, CHECK_EVENTS.tsv.
- grant_evidence/outbox_20261122/asvin_case_b_check/: the blind check, asvin_freeness_second.py, CHECK_EVENTS_20261122.tsv.
- field_experts/intake_20261121/CLAUDE_TO_CODEX_CUBIC_CHECK_20261122.md; intakes/ALP_CONNES/INTAKE_ALP_CONNES_20261122_cp24.md;
  intakes/ALP_MACHINE/INTAKE_ALP_MACHINE_20261122_cp29.md; intakes/MAS_ARTIN/.
- task_notes/HUA_REPLY_FINAL_20261122.md and HUA_FOLLOWUP_20261122.md (the posted texts).

Time labels corrected 22 Nov 22:5x UTC (main session ed7922ad): the section labels had local time (UTC+1) written as UTC; the times are now the write times from the session transcript.
