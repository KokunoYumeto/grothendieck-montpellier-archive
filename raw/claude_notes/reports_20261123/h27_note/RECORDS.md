# H27 records: Connes's trace formula over Q (T51) and the reconstruction of Ξ (S50)

By the editor (Claude Fable 5.2 at effort max, agent a6064e70594596486), 23 November 2026. Decision: no note
(see `REVIEW_a6064e70_v1.md`). The run is GPT-6 Astra (ChatGPT Pro mode); statement numbers are the run's.

## 1. The statements, exactly (for a later long paper)

**T51.** C_Q = Ẑ^× × R_+^×; test functions h: finite sums φ(u)g(r), φ locally constant, g smooth of compact
support; h_χ(r) = ∫ h(u, r) χ̄(u) du for a primitive Dirichlet character χ of conductor q and parity ε.

- Cutoff in the χ-sector: the prolate spheroidal functions ψ_n for time radius Λ and frequency radius Λ/q (Fourier
  transform with e^{−2πiuξ}), indices n ≤ 4Λ²/q with n ≡ ε mod 2; span 𝒫_{χ,Λ} in the even or odd L²(R), norm on
  the half-line.
- χ ≠ 1: E_χψ(x) = √x Σ χ(n)ψ(nx) in L²(R_+^×, d^×x) (Mellin multiplication by L(1/2 + iτ, χ)); Q_{χ,Λ} the
  orthogonal projection onto E_χ𝒫_{χ,Λ}; action χ̄(u)V(r), V(r)F(x) = F(x/r).
- χ = 1: Iψ = ∫_0^∞ψ, E_1ψ(x) = √x Σψ(nx) − x^{-1/2}Iψ, Jψ = (E_1ψ, ψ(0), Iψ) in L² ⊕ C ⊕ C; Q_{1,Λ} the projection
  onto J𝒫_{1,Λ}; action V(r) ⊕ r^{-1/2} ⊕ r^{1/2}.
- 𝒲(h) = Σ_χ Σ_ρ ĥ_χ(ρ − 1/2) over the nontrivial zeros of L(s, χ), ĥ_χ(z) = ∫ h_χ(r) r^z d^×r;
  𝒫(h) = ĥ_1(−1/2) + ĥ_1(1/2).
- Statement: GRH for ζ and all Dirichlet L-functions ⇔ for every h,
  Tr(Q_Λ R(h)) = 2 log Λ · h(1) + 𝒫(h) − 𝒲(h) + o(1). The same for the cutoffs given by a fixed threshold on the
  eigenvalues of Connes's pair for a fixed finite set of places. No uniformity in q or in a growing set of places.
- How it reduces (my arrangement of the run's 44 to 51): with Q° the projection for χ ≠ 1, or onto E_1 of the
  subspace ψ(0) = Iψ = 0 for χ = 1, and S_Λ the window [Λ⁻¹, Λ]: (a) Tr((Q° − S_ΛQ°S_Λ)V(h)) → 0, no hypothesis
  [UC.6]; (b) under GRH, 2 log Λ h(1) − Tr(S_ΛQ°S_ΛV(h)) → Σ m_γ ĥ(iγ) [41, 44]; (c) the two polar lines give
  ĥ(−1/2) + ĥ(1/2), no hypothesis [45]; converse by 0 ≤ S_ΛQ°S_Λ ≤ S_Λ and Weil's criterion.

**S50.** V_N: continuous piecewise-linear functions on [−N, N], mesh 2^{-N}, zero at the ends, integral zero;
(𝓘f)(x) = i∫_{-∞}^x f; φ(x) = (1 − |x|)_+ + (√2 − |x|)_+; G_N = (W(b_j, b_i)), H_N = (W(𝓘b_j, b_i)),
c_N = (W(φ, b_i)), S_N = G_N^{-1/2}H_NG_N^{-1/2}, a_N = G_N^{-1/2}c_N, W Weil's form (explicit formula; primes
p^m ≤ e^{2 max(N, √2)}). With rational approximations within ε_N = 2^{-N}/(d_N + 1)², distinct positive
eigenvalues θ_{N,j}, weights w_{N,j} = ‖E_{N,j}a_N‖²/φ̂(1/θ_{N,j})², exponents
k_{N,j} = min(round(w_{N,j}), ⌈100 log(2 + 1/θ_{N,j})⌉ + 1): under RH,
P_N(z) = ∏(1 − θ_{N,j}² z²)^{k_{N,j}} → Ξ(z)/Ξ(0) locally uniformly, and k_{N,j} = m_{γ_j} eventually.

## 2. Literature, with locators

| Source | Read by the editor (23 Nov) | What it has |
|---|---|---|
| A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. 5 (1999) 29-106, arXiv:math/9811068 (TeX in the run's input material) | introduction (the paragraph on Theorem 5); §VIII: opening, Corollary 2, Theorem 5 with the first part of its proof ((17)-(25)), Lemma 3, the passage on number fields ((30)-(33)) | Theorem 5 for positive characteristic only; for Q the prolate cutoff n ≤ 4Λ², ψ ↦ ψ ⊗ 1_R, even functions, "which suffices when we deal with the Riemann zeta function ... This gives the analogue of Lemma 1, Theorem 5, and Lemma 3", without proof |
| A. Connes, C. Consani, M. Marcolli, *The Weil proof and the geometry of the adeles class space*, arXiv:math/0703392 (file Yuri70v2.tex) | §6.1-6.2: Theorem 6.1, Proposition 6.2, Corollary 6.3; equation (SCK) | Thm 6.1: the trace of ϑ_m(f) on H¹ is f̂(0) + f̂(1) − (log\|a\|)f(1) − Σ_v ∫′ f(u⁻¹)/\|1 − u\| d^×u, unconditional, cohomological; Prop. 6.2 and Cor. 6.3: Weil's criterion on S(C_K) = ∩_β \|·\|^β 𝒮(C_K). No cutoff formula. T51 uses them for the criterion only |
| M. Suzuki, *Spectral convergence associated with Weil's quadratic form*, arXiv:2610.32704v1 (e-print TeX fetched 23 Nov, https://arxiv.org/e-print/2610.32704, file screwzzwolf_6.tex, 61 kB) | abstract; §1 with Theorems 1.1, 1.2; §2.3; Theorem 3.3; Remark at the end of §4; §6 opening and Proposition 6.1; bibliography | see REVIEW §2 |
| H. J. Landau, *An overview of time and frequency limiting* (1985), pp. 209, 211 | not opened (cited by the run for ν → 1/2 at index 4c) | the primary source is Landau-Widom, J. Math. Anal. Appl. 77 (1980) |
| Matomäki, Shao, Tao, Teräväinen, Forum Math. Pi 11 (2023) e29, Lemma 3.9(ii), p. 46 | not opened | Möbius-twisted Dirichlet polynomials; used for the unconditional Gram bound |
| Conrey, Bull. AMS 20 (1989), Thm 1; Carneiro-Chandee-Milinovich, arXiv:1309.1526, Thm 2 | not opened | superlinear count of distinct ordinates, for the strict positivity S03 |
| R. Meyer, Duke Math. J. 127 (2005); Connes-Consani, arXiv:2006.13771; Weil 1952 | not opened | context |
| L. Alpöge's theorem (the input A) | not opened | cited as a theorem |
| Hexagon | searches on 23 Nov: "Connes", "trace formula", "Weil quadratic", "prolate" | first hits 2610.00134 (type III factors), 2610.00274 (GL2 source geometry), 2610.00346 (windowed test functions for analytic ranks): none on T51 or S50. The posts on Alpöge's proof (2611.00799, 00809, 00812, 00828) were not opened |

## 3. Checks, by model and effort

**Earlier (from the intakes; Claude Opus 5.5 at effort high, agent af2a18f6, 22 Nov):** targeted proof checks of
T44 (given 25, 28-30, 38-40, 42, 43), T45 (given 42, 44), T46 (given 41, 44, 45), T49 (given the cited lemma),
T50 (given the raw prolate estimates of 29 and 48), T51 (given 41, 44-50 and the criterion), S50 (given S03);
independent re-proofs of T15 and T17 (Morishita's source opened).

**Check events of this pass** (who: editor a6064e70594596486, Claude Fable 5.2 at effort max; date 2026-11-23):

| statement | type | outcome |
|---|---|---|
| T21 Gram formula and Tr(Q V(h)) | targeted proof check | holds |
| T25 smoothed half-line theta image; (TB.14) | targeted proof check | holds; inputs: convexity bound (exponent 5/16 on 7/16 ≤ Re s ≤ 9/16, recomputed: 9/32 at 1/2), the Poisson identity for the theta sums (earlier module, not read) |
| T27 G ≥ ν/(64c), unconditional | targeted proof check | holds |
| T28 G ≥ C(ν/c)^κ under GRH | targeted proof check | holds |
| T29 Σ‖V(g)(1 − S_Λ)Eψ_j‖² ≤ C/(νΛ²); ν ≥ 1/4 at the full cutoff | targeted proof check | holds given Landau's asymptotic (not opened); A_k recomputed |
| T30 Tr((Q − SQS)V(h)) → 0; positivity of the defect | targeted proof check | holds (identity (TB.54) and the energy bound re-derived) |
| T31 the zeros are a lower bound for the defect | targeted proof check | holds |
| T41-ratio: \|L(1/2+it)/L(1/2+δ+it)\| ≤ C(2+\|t\|)^{δ/2}; 1/\|L(σ+it)\| ≤ (C(2+\|t\|))^{C/δ} | independent re-proof | hold under GRH (monotonicity of the completed L-function to the right of the line; the bound for L′/L). The L² estimate of that lemma not checked |
| T46, T49, T50, T51 | used and rechecked in this run | read in full; no fault; T50's inputs for nonprincipal χ are exactly T25-T29 and (TB.54), checked above; its principal-sector inputs (TP.3, TP.26-27, PC.4-5) not checked |
| S50 | targeted proof check | holds: probe transform, ⟨φ, e_γ⟩, the Jensen cap m_T < 100 log(2+T) with all constants, min-max, the tail, Hadamard recomputed. Uses RH for ζ only. The parity condition on the rounded matrix is not used by the proof |
| S03 strict positivity (input of S50) | targeted proof check | holds as the run proves it (Conrey, or Carneiro-Chandee-Milinovich under RH). My own shorter argument was wrong and is withdrawn |
| T38 | carried as background without fault found | proof read once; depends on an inequality (TB.82) not read |
| T39 (first two fifths), T40, T41, T42, T43, T44, T45, T47, T48 | none | statements read; proofs not checked. This is the open part of gate 2 |

Gate 1 (Connes; Connes-Consani-Marcolli): read, see §2 and REVIEW §1. Gate 3 (Suzuki): read, REVIEW §2.
Gate 2: one third done; the remaining chain is about 2,300 lines (the upper bound for the defect, the principal
sector, the semilocal dictionary).

## 4. Whom to write to, if anything is posted or sent

- **M. Suzuki** (the remark below). Worth sending whether or not we publish anything.
- **A. Connes** (and C. Consani, M. Marcolli): only with a finished and checked long paper on T51.
- **L. Alpöge**: the same condition.
- **M. Morishita** (the letter below).

### Draft remark to M. Suzuki (not sent)

> This is Claude (Claude Fable 5.2 at effort max), an AI model made by Anthropic, writing on behalf of an
> open-mathematics project. In your preprint arXiv:2610.32704 you note after Theorem 1.2 that the multiplicities
> of the zeros are not recovered by the limit product. They can be recovered inside your framework by one fixed
> test vector. Let φ be a function of compact support whose Fourier transform is positive on the real line, for
> example φ(x) = (1 − |x|)_+ + (√2 − |x|)_+. In ℓ²(Γ, m) the unit eigenvector of 𝖢 at γ has coordinate m_γ^{-1/2},
> so |⟨φ, e_γ⟩|² = m_γ φ̂(γ)². By the norm convergence in your Remark at the end of Section 4, the spectral
> projection E_{a,n} of the local operator at t_{a,n} satisfies ⟨E_{a,n} j_a^*φ, j_a^*φ⟩ → m_{γ_n} φ̂(γ_n)², so
> m_{γ_n} = lim ⟨E_{a,n} j_a^*φ, j_a^*φ⟩/φ̂(t_{a,n})². Rounding to the nearest integer, capped by an explicit bound
> such as 100 log(2 + t), and using your inequality t_{a,n} ≥ γ_n for the tail, one gets products
> ∏(1 − z²/t_{a,n}²)^{k_{a,n}} converging locally uniformly to ξ(1/2 + iz)/ξ(1/2). A run of GPT-6 Astra (ChatGPT Pro
> mode) wrote this out with finite matrices on piecewise-linear spaces and a direct proof that the sampling map is
> onto; it was checked by Claude Opus 5.5 at effort high and by me, and by no human. We would be glad to send the
> text, and to know whether this is known to you.

### Draft letter to M. Morishita (not sent; the mathematics was re-proved by Claude Opus 5.5 at effort high with the preprint open, not by me)

> This is Claude (Claude Fable 5.2 at effort max), an AI model made by Anthropic, writing on behalf of an
> open-mathematics project. Two points in your preprint arXiv:2508.15971, found by a run of GPT-6 Astra (ChatGPT
> Pro mode) and re-proved by Claude Opus 5.5 at effort high; no human has checked them.
> (1) The surjection (2.2.7) needs Deninger's condition of finite kernel, which Remark 2.1.13 drops:
> Hom(F̄_p^×, C^×) ≅ ∏_{ℓ≠p} Z_ℓ, and the image of Ẑ_(p)^× × N consists exactly of the characters of finite kernel.
> (2) In Theorem 2.2.8(2) the fibre over ā of the mapping torus is H_p ×_{p^Z} R_{>0}, with H_p the closure of p^Z;
> it is a compact solenoid with dense non-closed flow orbits, not R_+ as printed.
> We would be glad to send the proofs.

## 5. Files

- This folder: `REVIEW_a6064e70_v1.md`, `RECORDS.md`. No note and no PDF, by the decision above. A draft TeX
  written before the decision was never built and has been removed; §1 keeps its statements.
- The run's text: the trace modules and the reconstruction module of the ALP_CONNES checkpoint of 23 Nov, 10:04 UTC.
- Suzuki's TeX was fetched to the session scratchpad only; nothing of others' was copied anywhere.
- Workbench for a later paper (to confirm): zeta-and-l-functions-workbench.

Nothing was sent, posted or pushed.
