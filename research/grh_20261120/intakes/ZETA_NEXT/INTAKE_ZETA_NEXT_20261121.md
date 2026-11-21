# Intake of ZETA_NEXT (prompt 43, "effective class numbers, Λ-schemes and the non-CM gate"), final, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent ad85573792c61a914), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode), root and branch agents (normal/, cm/, lambda/, noncm/) of the same
model; it writes "GPT-6 Astra Pro, effort not exposed". Prompt 43 was built from §6 of my ZETA_TWO intake.

Notation: **A** = Alpöge's RH and Dirichlet GRH (a theorem); **M** = Masullo's Hecke GRH (conditional); **U** = unconditional.

## 0. What was read, and the scope

- **Return folder:** `research_returns\ZETA_NEXT_final_20261121T0340Z_unzipped` (the final, 03:40 UTC). The only ZETA_NEXT
  folder present.
- **Prompt as sent:** `SENT\43_ZETA_NEXT_effective_class_numbers_Lambda_schemes_and_the_non-CM_gate\PROMPT.md` (the task).
- **Read:** `README.md`, `QUESTIONS.tsv` (all 31 rows), `normal\findings.tex` in full (NX01-NX04), `cm\findings.tex` lines 19-58
  (NC01 statement and the start of its proof) and 223-345 (NC03 with proof, NC04 statement and the start of its proof),
  `lambda\findings.tex` lines 1-175 (NX-L01 with proof; NX-L02 statement and the first part of its proof), 299-520 (NX-L03,
  NX-L04 with proof, NX-L05, NX-L06 with proof, NX-L07 with proof), and the NG01 statement in `noncm\findings.tex`. I did not
  read the assembled `ZETA_NEXT.tex` (it collects these modules), NC02's proof, the rest of NC04, NX-L02's perfectoid steps
  in full, NX-L03's proof, or NG02-NG07.
- **Read in full, every step checked (8):** NX01, NX02, NX03, NX04, NX-L01, NX-L04, NX-L06, NX-L07.
- **Proof read, cited theorems carried (2):** NC01 (Louboutin's relative class number formula and upper bound), NC03
  (Gaudron-Rémond's isogeny estimate, Tsimerman's Lemma 4.1).
- **Statement level:** NC02, NC04, NX-L02 (structure only), NX-L03, NX-L05, NG01-NG07.
- **Computation:** 4C_4 = 8·exp(21/8 + (γ + 2 log 2)/(4 log 3)) = 8·e^{3.0718} ≈ 172.6 < 173 recomputed; the elliptic curve
  y² = x³ − x over F_5 recounted (8 points, a = −2, inverse roots −1 ± 2i).

## 1. Verdicts

| Id | Statement (short) | Input | Verdict |
|---|---|---|---|
| **NX01** | for every normal K ≠ Q: κ_K = Res_{s=1}ζ_K > 1/(173 log D_K), so h_K R_K > w_K√D_K/(173·2^{r_1}(2π)^{r_2} log D_K) | A (Stark 1974 Lemmas 3, 4 (11), 8; Garcia-Lee §3) | **confirmed.** Stark's Lemma 8 moves a real zero in [1 − 1/(4 log D), 1) to a quadratic subfield, where A excludes it; then Stark's Lemma 4 with β_1 = 1 − 1/(4 log D) gives κ > 1/(4C_4 log D); C_4 checked numerically. |
| **NX02** | every K of degree n: κ_K > 1/(173·n!·log D_K); CM fields of degree 2g: h_E R_E > w_E√D_E/(173(2g)!(2π)^g log D_E) | A (Stark Lemma 7, Aramata-Brauer) | **confirmed** (log D_L ≤ m log D_K ≤ n! log D_K for the Galois closure L; a zero of ζ_K is a zero of ζ_L; the two cases for β_1). |
| NX03 | effective Brauer-Siegel for normal fields: the two-sided bound with Louboutin's upper bound (e log D/(2(n−1)))^{n−1} | A + Louboutin 2001 Thm 1(1) | **confirmed** (w_K ≤ 2n² from φ(t)² ≥ t/2). |
| NX04 | h_K ≤ √D_K(1 + ½ log D_K)^{n−1} | U (Minkowski) | **confirmed** (M ≤ √D_K for n ≥ 2; d_n summation). Classical in form. |
| **NC01** | CM field E of degree 2g: h_E ≥ h_E/h_F > c_g D_E^{1/4}/(log D_E)^g, c_g explicit; for h_E ≤ H an explicit discriminant cutoff; imaginary quadratic: h > √D/(173π log D) | A | **proof read** (the quadratic case and the shape of c_g, from NX02 and Louboutin's upper bound for κ_F with log D_F ≤ ½ log D_E, checked; the full constant chain carried). |
| NC02 | h_F(A) ≤ 2^{g−1}(75/2 + 16g!) log D_E + 4g(2^g − 1) for CM abelian varieties (averaged Colmez) | A + averaged Colmez | statement level. |
| **NC03** | geometrically simple A with End = O_E: every field of definition of A and its endomorphisms has degree ≥ ℓ_g D_E^{η_g}; field of moduli degree ≥ (ℓ_g/s_g)D_E^{1/(16384g³)}: **an effective version of Tsimerman's Theorems 1.2 and 4.2** | A (+ Gaudron-Rémond, Polarisations et isogénies, Thm 1.4; Tsimerman 2018 Lemma 4.1) | **proof read, cited theorems carried.** The chain (h_E isogeny classes ↦ ideals of norm ≤ N by Gaudron-Rémond; #ideals ≤ 2^{2g}N²; NC01; solve for k) is right. |
| NC04 | every CM point x of A_g: \|Gal·x\| ≥ s_g^{−1}T_g^{−1/P_g}\|disc Z(End A_x)\|^{1/P_g}, P_g = 28672g⁴ (Rémond's maximal-order replacement) | A | statement level (start of proof read). |
| NC-AO scope | the orbit constants are effective; the counting step of André-Oort (Pila-Wilkie) is not made effective | — | correct scope statement. |
| **NX-L01** | for any closed Z ⊂ A^d_{F_p}, two copies of A^d_Z glued along A^d − \|Z\| form a flat, finite-type, **nonseparated** Λ-scheme X with ζ_X = ζ(s−d)·Z(Z, p^{−s}); for Z: y² = x³ − x over F_5 the bad factor (1 + 2t + 5t²)/(1 − 5t) has inverse roots of modulus √5 | U | **confirmed.** I checked: φ_p^{−1}(U) = U (Frobenius is a homeomorphism of the special fibre), ψ_q = i_1φ_q r for q ≠ p, the commutation identities, ψ_q is Frobenius mod q; the point count; the curve (1,1,2,2,1 affine points, 8 in all). It refutes the conjecture as I worded it (j ∈ Z, no separatedness). |
| NX-L02 | proper flat X/Z_p with a Frobenius lift: H^i(X_{F̄_p}, Z/ℓ^a) ≅ colim_{φ^*} H^i(X_{Q̄_p}, Z/ℓ^a), G_{Q_p}-equivariantly; rationally a stable direct summand | U (Huber; Scholze, Perfectoid spaces, Thms 5.2, 7.12, 9.7) | statement level, first part of the proof read (A_∞ = W(B), B the perfection of the special fibre). |
| NX-L03 | proper flat Λ-scheme: at every prime H^i(X_{F̄_p}, Q_ℓ) = ⊕ V_{p,i,j}(−j), finite image, semisimple; every factor of R_{X,S} is (1 − ξp^{j−s})^{±1} | U (NX-L02 + Borger Cor. 6.2) | statement level (the deduction from NX-L02 and Borger is immediate as stated). |
| NX-L04 | μ_p = Spec Z[t]/(t^p − 1): special H⁰ of dimension 1, generic p, inertia invariants 2; correction 1 − t | U | **confirmed**. |
| NX-L05 | Bl_E(P²_{Z_p}) for a cubic E ⊂ P²_{F_p} has no Frobenius lift | U | statement level. |
| **NX-L06** | proper flat Λ-scheme: every non-real zero or pole of ζ_X has real part in ½Z; global factors on j + ½, local and correction factors on integers | A | **confirmed** given NX-L03 (Borger Thm 6.1, Cor. 6.2; ZT01, ZT04; A for the Dirichlet factors). |
| NX-L07 | Z[ζ_5] has cyclotomic local factors but no Frobenius lift at 5 (endomorphisms of O_K are automorphisms; Frobenius kills ε = T − 1 in F_5[T]/(T−1)⁴): **it is not a Λ-ring** | U | **confirmed.** It corrects my ZETA_TWO intake (§5.2), which listed "rings of integers of abelian fields" among the Λ-schemes for which the conjecture holds. Their local factors are cyclotomic, but they are not Λ-schemes. |
| Q2-DP11-SCOPE | DP_MULT DP11 concerns identity lifts (binomial rings); general flat Λ-structures are commuting Frobenius lifts (Borger §1.1) | — | correct. |
| NG01 | for a pure motive M of abelian type over Q (absolute Hodge): canonical M = C(M) ⊕ N(M), C(M) = H_B(M)^{D_M}, D_M = (G_M°)^{der}; its ℓ-adic realization is a direct sum; so the CM part of h^j(A) is available for CM01 and the incomplete L-function factors exactly | U (Deligne-Milne) | statement level (standard Tannakian argument). It **closes the gap I found in ZETA_TWO ZT06** for every abelian-type piece. |
| NG02-NG06 | curves: H¹ of non-CM Q-simple Jacobian factors with exact multiplicities; abelian varieties: N_r primitive CM complements; full Sp_{2g}: primitive exterior powers; E^m: Sym^{a−b}E(−b); det_K H¹ is CM of types (p,q),(q,p) | U | statement level. |
| NG07 | A = Jac(y³ = x⁵ − x − 1), dim 4, End_{Q̄} = Z[ζ_3]: absolutely simple, non-CM, yet primitive h⁴ contains a rank-two CM summand of types (3,1),(1,3) defined over Q | U (computation) | statement level. Refutes the "only h¹ matters" shortcut (Q3-H1-SHORTCUT). |

**Counts.** 22 findings and 3 scope rows. Every step checked: 8 (NX01-NX04, NX-L01, NX-L04, NX-L06, NX-L07). Proof read with
cited theorems carried: 2 (NC01, NC03). Statement level: 12. Refuted by me: 0. The run's refutations (NX-L01, NX-L04, NX-L05,
NX-L07, NG05-NG07 for the h¹ shortcut) stand as far as I read.

## 2. What is new

- **Against the literature.** NX01-NX03 are Stark's 1974 theorem with its Siegel-zero clause discharged by A; Garcia-Lee record
  the same constant extraction. They are transfers, now with the absolute constant 173. NC01 is a transfer of the
  Louboutin/Stark-Odlyzko relative class number bounds. **NC03-NC04 are the substantive new statements**: Tsimerman's Galois
  orbit lower bounds for CM points in A_g (Annals 2018) were ineffective only through Brauer-Siegel; with A and Stark's descent
  they become effective, with explicit exponent 1/(16384g³), resp. 1/(28672g⁴). Earlier effective versions assumed GRH for
  the CM fields (Tsimerman 2012); here only Dirichlet GRH enters. A literature search is still owed.
- **Λ-schemes.** NX-L03/NX-L06 give the correct statement: for **proper** flat Λ-schemes, all bad fibres are integral
  Artin-Tate, and the Riemann hypothesis for ζ_X holds in the form "global divisors on j + ½ (by A), local ones on integers".
  NX-L01 shows that properness, or at least separatedness, cannot be dropped; the separated nonproper case is open.
- **The non-CM gate.** NG01 is the canonical CM/non-CM splitting that ZT06 lacked; NG07 shows that a non-CM abelian variety can
  carry a CM summand in higher cohomology, so the "non-CM gate" of Q02 is a statement about N(M), not about h¹.

## 3. What it settles of my ZETA_TWO prompt updates (§6)

1. **(a) Effective Brauer-Siegel for normal fields:** settled (NX01-NX03, NC01). **The Galois-orbit bounds:** made effective
   (NC03, NC04). **Effective André-Oort:** not settled; the Pila-Wilkie counting step stays ineffective as stated (the run says
   so). Next attack: combine NC04 with an effective counting theorem (Binyamini's effective Pila-Wilkie for Noetherian or
   Pfaffian functions, and the work of Binyamini, Schmidt and Yafaev on effective André-Oort; locators to be checked).
2. **(b) The bad fibres of Λ-schemes:** decided. The conjecture as I worded it is **refuted** (NX-L01, nonseparated); for proper
   flat Λ-schemes it is **proved** (NX-L03); separated nonproper is **open**.
   - **The Λ-scheme gloss it uses.** The run starts from ZT05 (Spec Z[1/p] is a Λ-scheme, zeros 2πik/log p) and uses DP_MULT
     DP11 only as the identity-lift special case (Q2-DP11-SCOPE). It confirms the correction to the ALPOGE_BRIDGES intake gloss
     ("RH for ζ_X of every Λ-scheme" is false): the true statement is NX-L06 for proper ones.
   - **One correction to my intake:** NX-L07 shows that Z[ζ_5] is not a Λ-ring. My ZETA_TWO intake §5.2 listed rings of
     integers of abelian fields among the cases; that was wrong. Their local factors are cyclotomic (true), but they are not
     Λ-schemes.
   - **A remark the run does not make:** by Weil II (3.3.1), every local factor of every scheme of finite type over Z has its
     divisors on lines Re s = w/2, w ∈ Z. So NX-L01's example (inverse roots of modulus √5, line Re s = ½) violates the
     "integer line" form but not the weaker "½Z" form, which holds for the bad factors of every scheme of finite type. The
     content of NX-L06 is that, for proper Λ-schemes, the local lines are integers and the global ones are j + ½.
3. **(c) The non-CM gate:** ZT06's gap is closed for abelian-type motives (NG01); exact residual lists for curves, abelian
   varieties and E^m (NG02-NG05).
4. **Attachments** (Anderson, Stark, Borger, DP11): used with exact locators.
5. The run kept the main question first, as asked.

## 4. The scope of the two proofs

- **A:** NX01-NX03, NC01-NC04 (zero exclusion near 1 for normal Dedekind zeta functions via Stark; no full GRH for them), NX-L06.
- **M:** only where CM01 is invoked for the CM summands C(M) (NG01-NG07); NG07's CM summand of types (3,1),(1,3) is a Hecke
  character of infinite order over Q(ζ_3): RH for it is M.
- **Beyond both:** RH for every N(M) (non-CM factors), stated as such. No statement claims more than its input.

## 5. In Grothendieck's frameworks

NX01-NX03 concern ζ of Spec O_K and the class number formula (the Picard group and the unit lattice of Spec O_K); NX-L02-NX-L06
are statements about ℓ-adic cohomology of the special fibres of proper Λ-schemes (SGA 4 XII-XIII proper base change does not
suffice; the Frobenius lift and perfectoid tilting do), with the inertia-invariant comparison of SGA 7 I; NG01 is in Deligne's
absolute Hodge motives (Tannakian, the motivic Galois group G_M). The run anchors to cote 60 scans 3-9 (determinant algebra) and
SA06 B.4a-e as inherited readings; no new scan reading.

## 6. Integration

- **ZETA_TWO intake §5.2 (my own):** replace "It holds for Spec Z[1/n], Spec of abelian rings of integers and their localizations,
  and split tori" by "It holds for Spec Z[1/n], μ_n = Spec Z[t]/(t^n − 1) and split tori; abelian rings of integers are not
  Λ-rings (ZETA_NEXT NX-L07). Decided by ZETA_NEXT: refuted for nonseparated (NX-L01), proved for proper (NX-L03, NX-L06)."
- **ALPOGE_BRIDGES CC-F01b and its intake:** add "the RH form for proper flat Λ-schemes is ZETA_NEXT NX-L06".
- **Bridges Q01:** add NX-L06 as the class of schemes over Z with full RH (proper flat Λ-schemes, A only); and NG01-NG05 as the
  exact residual lists for curves and abelian varieties.
- **SA06 B.4a-e:** NX04 bounds the sufficient power of B.4e effectively (h_K ≤ √D(1 + ½ log D)^{n−1}); B.4c stays refuted.
- **SA07 (CM heights):** NC02 as the effective height bound (with IA05).
- **Prompt 30 (anabelian) and the André-Oort line:** NC03-NC04.
- **HODGE line (prompts 37-41):** NG07 is a concrete absolutely simple non-CM fourfold whose h⁴ has a CM summand; it is a test
  case for the Weil/CM-class constructions of DEG_L and HECKE_DIV.

## 7. Prompt updates (successor)

1. **Effective André-Oort for A_g:** NC04 plus an effective point-counting theorem; or locate the exact ineffective step that
   remains.
2. **Separated nonproper Λ-schemes:** the open case; test toric and cellular schemes, and the Λ-equivariant compactification
   question.
3. **NG07:** compute the CM Hecke character of its h⁴ summand and check End_{Q̄} = Z[ζ_3] independently.
4. Model and effort: GPT-6 Astra (ChatGPT Pro mode).

## 8. Hexagon readiness

- **New candidate H11: "Effective Galois orbits of CM points in A_g from Alpöge's theorem" (NC01, NC03, NC04, with NX02).**
  1 Complete: NC03's proof read; NC04 and NC02 not yet. 2 Self-contained: yes (Stark, Louboutin, Gaudron-Rémond, Rémond,
  Tsimerman, averaged Colmez, all published; Alpöge's Lean theorem as input). 3 Stable: the run is final; a literature search
  is owed (Tsimerman 2012 under GRH; any 2026 effective version). 4 Checked: my partial check; NC04 and the constant chain need
  an independent check. 5 Interest now: **high** (it is a direct, nontrivial consequence of Alpöge's theorem that people will
  look for). **Gates:** read NC02 and NC04 in full, literature search, independent check of the constants. **Timely, one to two
  gates away: flag to the user.**
- **NX-L06 / NX-L03 ("RH for proper Λ-schemes")**: complete in the run; NX-L02's perfectoid proof needs a full read; interest
  moderate (F_1 / Borger community). Candidate after that read.
- NX01-NX03 alone are transfers (Stark, Garcia-Lee); they belong in the post of H11, not in one of their own.
