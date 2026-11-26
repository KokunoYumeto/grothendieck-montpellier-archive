# Proposition 10 of the ZH3 note: independent check

Checker: Claude Opus 5.5 at effort high, agent a25c2acbb3a6f11f7 (the agent that re-proved Theorems 1 and 2,
`REPROOF_THM1_THM2.md`). Date: 24 Nov 2026. Text checked: `zh3_note.tex`, §8, lines 461–586 (Proposition
`prop:heat` at line 480 and its proof). Everything below was redone by hand in this task; nothing is taken from memory.

## Verdict

The proposition holds as stated, under RH, and the proof is correct. Every step was rederived, every explicit constant
was recomputed, and both sources say what the note cites them for. I found no error. There are two wording points
(W1, W2 below); neither changes the mathematics.

## 1. Step-by-step check

| Step (note) | What I did | Result |
|---|---|---|
| Positivity: terms of Φ positive, H_{-a}(iy) > 0, b_k(a) > 0 | Φ term = πn²e^{5u}(2πn²e^{4u} − 3); cosh expansion gives b_k = ∫e^{-au²}Φu^{2k}/(2k)! / H_{-a}(0) | correct |
| Growth O(R log(R+3)); G of order ≤ ½ in w; genus-0 product of F_a; zeros w_i = −z_i² off [0,∞) | log M(√ρ) ≪ √ρ log ρ gives order ½ in w, so genus 0 with F_a(0) = 1; F_a > 0 on [0,∞) | correct |
| N_H(R) ≪ R log(R+3) | Jensen's formula and the growth bound | correct |
| Cone estimate: \|Q_z(v)\| ≤ e^{S\|v\|²/2} | \|(1+w)e^{-w}\|² ≤ e^{\|w\|²} from \|1+w\|² ≤ e^{2Re w+\|w\|²}; the product over ±x converges since Σm_x/x² < ∞ | correct |
| \|Q_z(v) − 1\| ≤ 8S\|v\|²e^{2S\|v\|²} | Schwarz on a circle of radius R: \|Q−1\| ≤ (\|v\|/R)²(1+e^{SR²/2}). Take R² = 1/S if 4\|v\|² ≤ 1/S (bound 2e^{1/2}S\|v\|² < 3.3 S\|v\|²); otherwise R = 2\|v\| (bound ½(1+e^{2S\|v\|²}) ≤ e^{2S\|v\|²} < 8S\|v\|²e^{2S\|v\|²}, as 8S\|v\|² > 2) | correct |
| H_{-a} = E H_0(z+U), U ~ N(0, 2a); shift by p = 2aL | ∂_t H_t = −∂_z²H_t, so H_{-a} = e^{a∂²}H_0 is the Gaussian average with variance 2a. Tilting by e^{LU} moves the mean by 2aL with factor e^{aL²} | correct |
| The displayed bound 16e^{16B}(4B/√(1−16A) + 2A/(1−16A)^{3/2}) | Recomputed: S\|p\|² = 4B; E e^{4SU²} = (1−16A)^{-1/2}; E U²e^{4SU²} = 2a(1−16A)^{-3/2}. This gives the two terms exactly | correct |
| At most 7/16 when A, B ≤ 2^{-10} | Value ≈ 0.0965 | correct, with a wide margin |
| S ≪ q^{-2}log(r+3)/(r+1); \|L\| ≪ q^{-1}log(r+3) | Split the zeros at r/2 and 2r: the middle range uses \|z∓x\| ≥ qr; the outer ranges use \|z²−x²\| ≥ 3r²/4 and ≥ 3x²/4 | correct |
| A ≪ η^{-2}log/r, B ≪ η^{-4}log³/r; cone \|arg z\| ≤ κ√a for \|z\| ≥ R_0 | q = η√a < 1 for a ≤ 1; choose η in terms of κ | correct |
| F(D)z^d = z^d J_d(1/z) | Since J_d(0) = f_0 ≠ 0, the nonzero roots correspond under z ↦ 1/z, real to real | correct |
| Symbols: (z+w)^{d−1}(z+w+dβ); the quadratic factor; discriminant 4dβ²(1 − d sin²θ) | Recomputed; for real roots in s = z+w, Im s > 0 excludes zeros | correct |
| Compositions; limits by Hurwitz | T_a(0) = 1, so the limit of degree-d images is nonzero | correct |
| 𝒥 entire, \|c_k\| ≤ C^k k^{-4k/3} | Cauchy at ρ ≈ k²/log²k gives \|c_k\| ≤ C^k(log k)^{2k}k^{-2k}, which is ≤ C'^k k^{-4k/3} | correct |
| 𝒥(a, 1/d, w) = H_{-a}(0)J_{d,a}(w/d) | Π_{j<k}(1 − j/d) = (d)_k/d^k | correct |
| e_s(k) has degree 2s and leading coefficient 1/(2^s s!); principal part (−1)^s w^{2s}D^{2s}/(2^s s!) | From e_s(k+1) − e_s(k) = k e_{s−1}(k) | correct |
| ℒ = −4wD² − 2D | z = i√w: ∂_z = −2z∂_w, ∂_z² = −2∂_w + 4z²∂_w², with z² = −w; ∂_aG = ∂_z²H | correct |
| Local form: no power below q^m; at q^m, e^{cD²}u^m with c = 4γx² − x⁴/2 | Term a^r ε^s: order drop ≤ 2s on a coefficient of vanishing order ≥ m−2r, times q^{2r+2s}. Principal parts give Σ(−4γw_0)^r/r!·(−w_0²/2)^s/s!·D_u^{2(r+s)}u^m | correct |
| Hermite forms for c > 0 and c < 0 | Scale u = λv with λ² = −2c | correct |
| x_*²/8 = γ_*²/2; H_0(z) = Ξ(z/2)/8 | x = 2γ | correct |
| Upper bound | d = ⌈γ/a⌉, ad ∈ [γ, γ+a]; Rouché about a nonreal Hermite root; H_{-a}(0) ≠ 0 | correct |
| Lower bound: P_a, T_a, P_a = UG locally, A_0 = AU_0(w_0) | The U_j with j ≥ 1 raise the order by 2j | correct |
| Head, d ≥ d_1 | γ ∈ [0, γ_0] with γ_0 < x²/8 at every multiple endpoint, so c < 0 there. Each Rouché disk is symmetric, so its single root is real; the count δ is exhausted | correct |
| Head, d < d_1 | Interlacing for 1+βD: p'/p is decreasing on each gap and positive on (0,∞). The root at 0 loses one multiplicity; the count is d | correct |
| Tail | \|θ\| = 2\|arg z\| ≤ 2κ√a; d sin²θ ≤ 4κ²γ_0 = ¼ ≤ 1. Purely imaginary z are excluded by F_a > 0 on [0,∞). T_a(D) commutes with P_a(D) | correct |
| The x_* = ∞ case | Lower bound with any γ_0 | correct |
| Value > 4766.003712 | 97.632²/2 = 4766.003712 exactly, and γ_* > 97.632 is strict (Prop. `prop:const`). Not rechecked: the certificate behind Prop. `prop:const` | arithmetic correct |

## 2. The sources at their locators

- **Borcea–Brändén, Theorem 2.** In `sources/borcea_branden/bb2.txt`, at line 233, after four form feeds, so p. 5 as
  cited. The theorem says that T: ℝ_n[z] → ℝ[z] preserves hyperbolicity if and only if (a), or (b) T[(z+w)^n] ∈ H_2(ℝ),
  or (c) T[(z−w)^n] ∈ H_2(ℝ). The note uses the "if" direction of (b), with H_2(ℝ) the real stable polynomials in two
  variables: real coefficients and no zero with Im z, Im w > 0. That is what the note states. Status: carried as
  background without fault found. I read the statement, not BB's proof.
- **Rodgers–Tao.** `sources/rodgers_tao/rt.txt` defines H_t and Φ exactly as the note does (abstract, and (1)–(4)
  of §1). Their (1) is H_0(z) = (1/8)ξ(1/2 + iz/2), with ξ in (2). So H_0(z) = Ξ(z/2)/8, and RH is equivalent to all
  zeros of H_0 being real. Status: carried as background without fault found.

## 3. §8 read against Theorem 1

Under RH, my independent proof of Theorem 1 (`REPROOF_THM1_THM2.md`) gives sup_{N,k}H_{N,k} = γ_*, with the value ∞
when every zero is simple. Proposition 10 gives lim a·j_*(−a) = γ_*²/2. Together they give the restatement
½(sup H_{N,k})², ∞ included. Two things agree:
- Both sides single out the *first multiple* ordinate. In Proposition 10 it enters through c > 0 exactly at multiple
  endpoints, m ≥ 2, with the threshold γ = x_*²/8. In Theorem 1 it enters through the moment deficit.
- Both use the same normalization: ordinate γ ↔ x = 2γ.

## 4. Points for the text (no mathematical change)

- **W1** (line ≈ 541, "Local form"). "Let K(a,w) be holomorphic near (0,w_0)" is weaker than what is used. 𝒥_K is
  formed from Taylor coefficients at w = 0. Its expansion in ε as Σ(−ε)^s E_sK needs K holomorphic in w on a disk
  about 0 containing w_0, with 𝒥_K entire in ε. Both uses satisfy this: G is entire with the stated growth, and P_a
  is a polynomial. Suggested wording: "Let K(a,w) be holomorphic for small a and entire in w, with 𝒥_K entire (as for
  G and for polynomials), and suppose that near w_0 ...".
- **W2** (Borcea–Brändén). One could add "(H_2(ℝ): real stable polynomials in two variables)", so that the reader
  sees that the note's "no zero with Im z, Im w > 0" is BB's condition (b).

## 5. Not covered by this check

- The certificate behind γ_* > 97.632 (Prop. `prop:const`). Only the arithmetic 97.632²/2 was checked.
- The implied constants in the "≪" bounds of the cone estimate are not made explicit, in the note or here. The
  argument needs only that they are finite and uniform in 0 < a ≤ 1, and I checked that they are.
