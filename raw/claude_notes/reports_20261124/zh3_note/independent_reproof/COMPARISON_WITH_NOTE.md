# Comparison of the independent re-proof with zh3_note.tex (Lemmas, Theorems 1-2)

Claude Opus 5.5 at effort high (agent a25c2acbb3a6f11f7), 24 Nov 2026. `REPROOF_THM1_THM2.md` was written before the
note was opened. Then I read zh3_note.tex, lines 209-338: §3 with the sampling bound, the density of the windows and the
primitive; §4 with the moments, the lower bound, the monotonicity and the limit, the supremum, the equivalences, the
integer form and the size of a certificate.

**Verdict.** Theorem 1 holds as stated, and Theorem 2 holds as stated. The note's proofs are correct. No gap, wrong
constant or wrong hypothesis affects a conclusion. The differences are routes, and one immaterial constant.

| place | note | re-proof | which is right |
|---|---|---|---|
| Sampling bound (note, `lem:sample`) | \|û(t)\| ≤ ‖u′‖_1/\|t\|, ‖Su‖² ≤ 2aσ‖u′‖²_2 for H¹ functions on [−a, a] | the same with ‖u′‖_1 (Lemma 1) | both; the same estimate |
| Density, step 1 (C_c^∞ dense) | tempered measure with Σ m\|c\|(1+γ²)^{−1} ≤ ‖c‖σ^{1/2}, then the Fourier image dense in 𝓢 | the same, with an explicit last step: a bump at one ordinate kills each coefficient | both. The note's inequality holds because (1+γ²)^{−2} ≤ γ^{−2}. "τ = 0 hence c = 0" is immediate for a measure with discrete atoms |
| Density, step 2 (mean removal) | ψ_R, with \|ψ̂(t)\| ≤ c_ψ t^{−2} and dominated convergence (terms ≤ c² m_γ γ^{−4}) | ‖h_R‖² ≤ ‖h′‖²_1 σ/R² | both; mine gives a rate |
| Density, step 3 (interpolation into V_N) | Wirtinger on each cell: ‖(v − I_N v)′‖_2 ≤ (h/π)‖v″‖_2; trapezoid bound for the mean; correction by h^{−1}(∫I_N v) t_0, contributing O(h^{1/2}) | the sup-norm interpolation bound; correction by a fixed hat τ = (1 − \|x\|)_+ ∈ V_N (N ≥ 2), contributing O(h²) | both. **Immaterial constant:** the note's trapezoid bound uses the length 2a, but I_N v − v can be nonzero on cells reaching to ±(a + h). The length should be 2a + 2h, which still tends to 0 |
| Strict lower bound | singular values: s_j(P_N C P_N) ≤ s_j(C), so tr C_N^{2k} ≤ Σ_{j≤rank} s_j(C)^{2k} < tr\|C\|^{2k} | trace Jensen/Berezin for f(x) = x^{2k}, with strictness from ‖\|C\|^k(I − P_N)‖_{HS} > 0 | both. The note's route is shorter. Strictness in both uses that 𝓗 is infinite-dimensional and C has trivial kernel |
| Monotonicity in N | max-min separately for the positive eigenvalues and for the absolute values of the negative ones of the nested compressions | Lemma 4 applied to B = C_{N+1}, P = P_N | both |
| HS convergence and trace limit | Suzuki (4.1) mechanism reproved for these windows; ‖UV‖_{S₁} ≤ ‖U‖_{S₂}‖V‖_{S₂} | the same (Lemma 3) | both; the same argument. The note, like the re-proof, proves density for the windows rather than assuming it |
| sup H_{N,k} = γ_* | ‖v‖_{2k} with v = (1/γ repeated m_γ − 1 times); γ_*^{−2k} ≤ Σ v^{2k} ≤ γ_*^{−(2k−2)} Σ v², so ‖v‖_{2k} → 1/γ_* | dominated convergence on B_k | both; the note's ℓ^p-norm argument is cleaner |
| Equivalences (Theorem 1) | E(T) < 1 ⇒ E(T) = 0; conversely γ_* > T and the supremum | the same | both |
| Integer form (Theorem 2) | pull-back under the surjection c ↦ Sf has the same positive index; max-min; Ξ(T) ≠ 0; operator-norm convergence puts the eigenvalues above 1/T "within reach" | the same, with the kernel of G_N handled explicitly (a positive subspace meets ker G_N trivially), and Weyl's inequality made explicit | both. The note covers singular G_N through the word "surjection". The re-proof spells it out, and the note could add one sentence |
| Basis b_j | not proved in these sections | spanning and independence proved (Lemma 1) | the re-proof supplies it; a small completion |

**Suzuki locators.** The note cites §2.3 for ‖C‖²_{S₂} ≤ σ and (4.1) for the convergence mechanism. Both match the
source: (2.2) is `eq_202`, line 424; (4.1) is `eq_401`, line 1104.

**Suggested edits** (optional, none needed for correctness):
1. In the trapezoid bound, use 2a + 2h for 2a.
2. Add a sentence that ker G_N is allowed: the positive index is unchanged by the pull-back.
3. One line proving that the b_j form a basis of V_N.
