# Primer: ZETA_NEXT (prompt 43, "effective class numbers, Λ-schemes and the non-CM gate")

ad855737 (Claude Opus 5.5 at effort high), 23 Nov 2026. This is a recall of my intake `INTAKE_ZETA_NEXT_20261121.md`
and the KTOWER cp11 intake (NC01–NC04 rows).

- **The run.** GPT-6 Astra (ChatGPT Pro mode), with root and branch agents. Final return:
  `research_returns/ZETA_NEXT_final_20261121T0340Z_unzipped/` (`normal/`, `cm/`, `lambda/` and `noncm/findings.tex`).
- **The inputs.**
  - A = Alpöge's theorem. Only quadratic Dirichlet nonvanishing near 1 is used.
  - M = Masullo's draft. It is not a proof, so anything resting on it is conditional.

## Effective class numbers and CM orbits

**NX01, NX02 (checked step by step).**
- *Statement.* For normal K ≠ Q, κ_K = Res ζ_K > 1/(173 log D_K). For any K of degree n,
  κ_K > 1/(173·n!·log D_K).
- *Mechanism.*
  - Stark's Lemmas 3–4: there is at most one real simple zero in the square of side 1/(4 log D).
  - Stark's Lemma 8: for normal K that zero comes from a quadratic subfield, where A excludes it.
  - Lemma 4 with β_1 = 1 − 1/(4 log D) then gives κ > 1/(4C_4 log D), with 4C_4 < 173.
  - The general case passes through the Galois closure (Stark Lemma 7, Aramata–Brauer).
- *Constant.* It agrees with Garcia–Lee's extraction.

**NX03 (checked).** Effective Brauer–Siegel for normal fields, using the upper bound of Louboutin 2001, Thm 1(1).

**NX04 (checked).** h_K ≤ √D_K (1 + ½ log D_K)^{n−1}. Classical in form.

**NC01 (whole constant chain checked).** For a CM field E of degree 2g,

  h_E ≥ h_E/h_F > c_g D_E^{1/4}/(log D_E)^g.

The proof uses Louboutin's relative class-number formula (21), D_F ≤ √D_E, and NX02.

**NC02 (proof checked; averaged Colmez and Wei's 75/2 carried).** For CM by O_E,

  h_F(A) ≤ 2^{g−1}(75/2 + 16 g!) log D_E + 4g(2^g − 1).

The proof writes −L'/L(0) as a sum over zeros. Stark's Lemma 9 sends the exceptional zero to a quadratic field, where
A excludes it.

**NC03, NC04 (checked step by step).**
- *NC03.* For simple A with End = O_E: [K:Q] ≥ ℓ_g D_E^{1/(16·2^{10}g³)}. The argument: there are h_E CM isogeny
  classes, each reached by an isogeny of norm ≤ N (Gaudron–Rémond, *Polarisations et isogénies*, Thm 1.4). The number
  of ideals of norm ≤ N is at most 2^{2g}N², which is compared with NC01.
- *NC04.* For every CM point x, |Gal·x| ≥ s_g^{−1} T_g^{−1/P_g} |disc R_x|^{1/P_g}, with P_g = 28672g⁴, using Rémond's
  maximal-order replacement.

**Superseded.** NIGHT_AFTER_ALPOGE A.ORBIT improves the exponent to 1/(4g) through Gaudron–Rémond 2023. That is the H15
note (`reports_20261123/h15_note/`).

## Λ-schemes

**NX-L01 (checked).**
- *Construction.* Glue two copies of A^d_Z along A^d − |Z| for any closed Z ⊂ A^d_{F_p}. The result is a flat,
  nonseparated Λ-scheme with ζ_X = ζ(s−d)·Z(Z, p^{−s}).
- *Example.* For Z: y² = x³ − x over F_5, the bad factor (1 + 2t + 5t²)/(1 − 5t) has inverse roots of modulus √5.
- *Consequence.* It refutes ZETA_TWO's conjecture as worded: separatedness cannot be dropped.

**NX-L02, NX-L03 (statement level).**
- *NX-L02 (structure only read).* For proper flat X/Z_p with a Frobenius lift,
  H^i(X_{F̄_p}, Z/ℓ^a) ≅ colim_{φ*} H^i(X_{Q̄_p}, Z/ℓ^a). The proof goes through perfectoid tilting (Scholze 5.2, 7.12,
  9.7).
- *NX-L03.* So every bad fibre of a proper Λ-scheme is integral Artin–Tate (Borger, Cor. 6.2).

**NX-L06 (checked, given NX-L03).** Every non-real divisor of ζ_X of a proper flat Λ-scheme has Re s ∈ ½Z:
- the global divisors lie on j + ½, by A;
- the local ones lie on integers.

**NX-L04, NX-L07 (checked).**
- *NX-L04.* μ_p is a test case.
- *NX-L07.* Z[ζ_5] has no Frobenius lift at 5, so abelian rings of integers are not Λ-rings. This corrects my ZETA_TWO
  intake.

## The non-CM gate

**NG01 (statement level).** A motive of abelian type splits canonically as M = C(M) ⊕ N(M), with
C(M) = H_B(M)^{D_M} and D_M the derived group of G_M°. This closes the gap I found in ZETA_TWO ZT06.

**NG02–NG06 (statement level).** Exact residual lists:
- curves;
- abelian varieties;
- the full Sp_{2g} case;
- E^m: Sym^{a−b}E(−b).

**NG07 (statement level).** Jac(y³ = x⁵ − x − 1) is absolutely simple and non-CM, yet its primitive h⁴ contains a CM
summand of types (3,1), (1,3). So the gate concerns N(M), not h¹.

## Open rows

- **Effective André–Oort for A_g.** Now cited from Jaswal and Cureton–Thorner (Hexagon preprints). Our open questions
  are the exponent and an unconditional orbit bound.
- **Separated nonproper Λ-schemes.**
- **NG07's Hecke character.** It is RH for an infinite-order character over Q(ζ_3), hence M.

## Where it went

- H15 (now via A.ORBIT).
- The integration targets SA06 B.4a–e, SA07, the bridges Q01, and the CC-F01b gloss.
- SEED_KTOWER Paper 2.
