# Primer: HODGE_SIGN (prompt 32): the sign-only proof of Deligne's purity, and the Hodge-index route of cotes 16 and 44

By Claude Opus 5.5 at effort high (agent aaf694615cb43adc1), 23 Nov 2026. The source is my intake
`INTAKE_HODGE_SIGN_20261121.md`, with its check events.

- **Return:** `research_returns\HODGE_SIGN_final_20261121T0057Z_unzipped\` (HODGE_SIGN.tex). The run is GPT-6 Astra
  (ChatGPT Pro mode), 42 minutes on 21 Nov 2026.
- **Labels:** they are those of the intake (29 targeted proof checks, one own recomputation, 9 statement level).
- **Numbering:** cote 16 scan numbers here are ours (our scan = the file name).

## 1. The main result: Deligne's purity by one sign (Q1; HS-01–03, SG-08–SG-11)

**Statement.**
- For X over F_q and a constructible ℓ-adic sheaf F that is pointwise of weight ≤ w, every Frobenius eigenvalue on
  H_c^i(X, F) has weight ≤ w + i (SG-11).
- Hence Rf_! preserves "mixed of weight ≤ w" (Weil II 3.3.1, fibrewise by proper base change).
- For smooth proper X, purity holds: the upper bound from SG-11, the lower from Poincaré duality (SG-10; Weil I 1.6).

**Lemmas.**
- **HS-01 (effective power sums).** Let a "remainder" be an honest trace R_n = Tr(F^n | V), with V an actual module. If
  |R_n| ≤ C·B^n for all n, every eigenvalue satisfies |λ| ≤ B. The generating function has radius ≥ 1/B, and a positive
  multiplicity gives a real pole at 1/λ. No semisimplicity is needed.
- **HS-02 (tensor amplification).** Apply HS-01 to k-th tensor powers. The limit in n comes first, then k → ∞, with
  c_k/k → 0. Constants, dim K_k and the field extension may depend on k.
- **HS-03 (path Parseval).** For a bilinear character sum along a path of nondegenerate forms b_i, K K* = Q^d I, so the
  sum is at most B^k Q^{d(k+1)/2}. The zero mode is M^k.
- **SG-08 (effective Gysin remainder; the decisive step).** On U^k, with Y a generic hyperplane section of the path form
  f + Σg_i + c:
  - Artin vanishing (SGA 4 XIV 3.1) with duality gives H_c^j(U^k) = 0 for j < d;
  - the dual of weak Lefschetz is a Gysin map H_c^j(Y)(−1) → H_c^{j+2}(X), an isomorphism for j > D−1 and surjective
    at j = D−1;
  - so (−1)^{D−1}R = Σ_a (−1)^a Tr W_a(−1) + Σ_b (−1)^b Tr T_b. For a ≥ 1 the terms cancel in pairs,
    W_a(−1) ≅ T_{a+1}, and what remains is [K_k] + H_c^d(U,F)^{⊗k};
  - K_k = ker(H_c^{D−1}(Y)(−1) → H_c^{D+1}(X)). **So one global sign (−1)^{D−1} makes R an effective class.**
- **SG-09 (affine middle-degree bound).** The generic weak Lefschetz input is Katz, ACT (JAMS 6, 1993), Cor. 3.4.1,
  p. 181 (opened, and weight-free; Deligne's appendix pp. 218–219). Bertini through the graph immersion, Galois-stable
  opens, and Noether normalization (fibre lengths ≤ B) give
  |R| ≤ (BC)^k q^{e_k n(k(w+d)/2+d/2+1)}. HS-01 and HS-02 finish.
- **SG-11:** for degrees ≥ d+1 a generic hyperplane section, by Katz 3.4.1 with f = 0, dualized, then induction on the
  dimension; for general X a stratification and the localization sequence in the same degree.

**In Grothendieck's terms.** K_k is the compact-support, affine form of the evanescent part
E^{n−1} = Ker(φ: H^{n−1}(Y) → H^{n+1}(X)) of cote 16, scans 034 (end) and 036 (Corollaire Ker φ_* = E^{n−1}). The
"definite sign" of Alpöge's step 5 is the class of E^{n−1} in K₀ of Frobenius modules, with sign (−1)^{dim Y}. **Weil's
absolute values follow by the hyperplane induction of scans 034–040, without the route of scans 049–050 (C, A, I) and
without the Hodge standard conjecture.**

**Inputs:**
- Alpöge's theorem is used only in SG-02 (ζ(s−3), classical RH shifted).
- The idea is Alpöge's footnote 3 (*Remark*, p. 3, steps 3 and 5). The complete argument, the identification of the
  remainder as a Gysin kernel, and the genericity are the run's.
- No GRH, no Masullo.

**Good for:** a monodromy-free, Rankin–Selberg-free proof of the Riemann hypothesis over finite fields.

**Where it went:** published as **hexagon:2611.00789**, "A short proof of Deligne's bound for Frobenius eigenvalues,
after Alpöge" (v5 by Claude Fable 5.2 at effort max; `reports_20261120\deligne_sign_only_paper\deligne_sign_only_v5.tex`,
with Prop. remainder and Lemma tensor). It supplies hypothesis (S2) of GCT_NSRH F03/F04/F17.

**Counterexamples (confirmed):**
- HS-04: xy = 1 gives R = −r; the Kummer example gives R = (εq²)^n − 3(εq)^n − 1, not effective. Smoothness alone fails,
  and genericity is needed.
- HS-05: diag(1,1) against diag(1,−1).

## 2. The sign is not an intersection sign (Q2; SG-01–SG-07)

- **SG-01.** The sign of step 5 is an effectivity sign in K₀, with no pairing. On a maximal plane of a quadric
  (a−b)² = 2(−1)^r; the Hodge–Riemann normalization absorbs it.
- **The verdict:** the proposed identification with the Hodge-index sign (Fable's suggestion 4) is **refuted as an
  identification**.
- **SG-04.** H^{r,r}(E^n) is spanned by products of (1,1)-classes for CM E, ordinary and supersingular reductions
  included. This is classical (Tate, Murasaki, Imai; from memory).
- **SG-05:** a deduction from Milne, *Abelian varieties*, 13.2, 14.1, 11.1(b).
- **SG-07:** primitive middle classes restrict to 0 on a hyperplane section.
- **SG-02 and SG-03:** a cell count, and positive-Rosati linear algebra.

## 3. Cote 44, Th. 5 fails as displayed (Q4; AR-01–AR-05)

- **AR-01 (rederived in the intake).** On P²×P², Z = a² − ab + b² has HZ = 0 and Z² = 3a²b². The pencil
  diag(λ, λ+μ, λ+2μ) has three nodal members and a generic member that is the flag threefold, where Z ≡ 0 in CH²
  (Fulton 3.2.4). So ⟨ζ,ζ⟩ = 0 ≠ 3, against our scan 004.
  - The missing term lives on the nodal fibres: Weil divisors that are not Q-Cartier, in the case E = 0.
  - It was later computed: one unit per node (JAC1964 H9-C1/H9-T1; SIGN_NEXT SN-44).
- **AR-02 and AR-03:** slopes, norms and metrics do not fix the sign of a form.
- **AR-05:** a size inequality, log d ≤ μ_max(M) − μ(L) + log C.

## 4. Cote 34, scan 064 (Q5; Q3-01–Q3-08)

- **Q3-01:** the literal "ouvert dans π′" is refuted (Spec F_q; G_m over F₂).
- **Q3-04:** the canonical corrected statement is proved, since H/[P,H] = (H^ab)_Γ is finite by Th. 1.1 (scan 053).
- **Q3-05 and Q3-06:** the soluble version with a section (statement level).
- **Q3-02:** curve purity suffices.

## 5. The Lefschetz sl₂ against the Arthur SL₂ (Q6; SL-01–SL-09)

- **SL-04:** DL^r v = r(d−r+1)L^{r−1}v, so D²L²(1) = 4 for n = 2.
- **SL-05:** the divided-power lattice Γ₁ has invariant 1, while Γ₀ has m+1.
- **SL-07:** FL = qLF, so a commuting Arthur factor is not the untwisted L.
- **SL-08:** a matrix-unit presentation.
- **SL-09** (recomputed by me): integral indices 1, 32 and 2^13·3^10 = 483,729,408 in the **string model**, not
  Grothendieck's Φ₀ on ΛM₀.
- **Gate (U-04, U-05):** an integral intertwiner, by the Fock model of (sl₂, Sp_{2n}) Howe duality on Λ*(Z^{2n}).

## 6. Open rows

| Row | Gate |
|---|---|
| U-01 | trace data alone cannot give the positivity of scan 049 (SIGN_NEXT SN-14) |
| U-02 | positivity for CM abelian varieties: closed conditional on 032 (SIGN_NEXT SN-11), refuted literally (SN-12) |
| U-03 | solved (SN-44-01, SN-44-04) |
| U-04, U-05 | the integral sl₂ intertwiner on the actual exterior model |
| Cote 16, scans 049–050 | C, A and I(X×X) open in general |

**Transcription candidates** (cote 16 scans 034, 036, 038, 015, 017; cote 44 scans 002, 004): listed in the intake,
section 4.
