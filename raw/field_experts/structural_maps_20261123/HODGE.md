# The Hodge line towards global Langlands: structural note

By Claude Opus 5.5 at effort high (agent aaf694615cb43adc1), 23 Nov 2026, at the user's word, for the main session
329fb1e6 (Claude Opus 5.5 at effort max).

**Sources:**
- the primers HODGE_SIGN, SIGN_NEXT, HECKE_DIV, THETA3, HODGE_DIVISION, HODGE_BOUNDED_CYCLES and HODGE_FINISH, and the
  intakes behind them;
- the primers of DEG_L, ZETA_HEAT and ALP_CONNES (other agents' intakes);
- the runs themselves, all by GPT-6 Astra (ChatGPT Pro mode).

**Status labels:** "checked" means a check event in our intakes. Everything else is a construction written out here or a
citation marked "from memory". Nothing is graded.

**A** = Alpöge's theorem (RH for every Dirichlet L-function, ζ included; GL₁ over Q).

---

## 1. The maps, written out

### M1. Weil classes and the unitary Shimura variety

- **Objects.** On the geometric side, a polarized 2n-fold A with an imaginary quadratic field K acting with signature
  (n,n), and its Weil plane W_K = ∧_K^{2n}H¹(A,Q). On the group side, the hermitian space (V,h) = (H₁(A,Q), K) and its
  unitary group U(V) ≅ U(n,n) over Q.
- **The map.** A ↦ a point of the U(V)-Shimura variety; W_K is the line of the determinant character det: U(V) → U(1)
  on ∧_K^{2n}.
  - So Weil classes are the invariants of SU(V) on top of the invariants of the full symplectic group.
  - Being of type (n,n) is equivalent to SU(V)(R) ⊂ the Mumford–Tate group.
- **Transported:** the integral structure, giving the degree of a detector and the multiplier.
- **Proved (checked):**
  - extraction: one detector gives the plane at cost quadratic in its degree (Paper A, Theorem extraction; HD-WQ, HD-U);
  - one principal family U^n per field and dimension (Paper A, principal quotient, Q10);
  - small detectors 48, 192 and 36 (Paper A §small);
  - stabilization from split 2n+2 to every determinant in 2n (Paper A; HD-COMP).

### M2. CM points and Hecke characters (GL₁ of the CM field)

- **Objects.** A CM point x of a special family is an abelian variety A_x with CM by a CM algebra E. Its Galois
  representation is ⊕ of algebraic Hecke characters ψ of E, by Shimura–Taniyama (from memory).
- **The map.** x ↦ (E, Φ, ψ); the reduction of A_x at a good prime v is determined by ψ(Frob_v).
- **Transported:**
  - the Tate classes of A_{x,v}, which are the eigen-tensors of Frobenius;
  - the action of [a]^* on the Weil plane, whose eigenvalues a^{2n} and ā^{2n} are the values of the K-character a ↦ a
    on the two extreme lines.
- **Proved:**
  - Paper A's equivalence (Q01, checked): Hodge for abelian varieties ⟺ one degree bound D for cycles on the reductions
    A_{x,v}, uniform in x, at infinitely many v;
  - the dichotomy (Q05, checked);
  - THETA3 C13 and HECKE_DIV P1: the resultant projector in [a]^*. The integer R is the product of the differences of
    the K-character values a^jā^{2n−j}.

### M3. Degrees of special cycles and L-values (Rallis)

- **Objects.** The surfaces of OpenAI's CM Hodge proof (032), built by theta lifts U(1) → U(3), and Hecke L-functions of
  the CM field.
- **The map.** The Rallis inner product formula (Haan, Th. 3.4, carried in the DEG_L intake).
- **Transported:** deg = (2/a_K)Σ_{j,σ} L_E(3/2, BC(τ_σ)⊗γ_σ³)/L_F(3, ε_{E/F})·Z_σ^# (DEG_L T6.11, proof read with Haan
  carried).
- **Proved (DEG_L intake):**
  - **B1 (checked):** ζ_K(2σ)/ζ_K(σ) ≤ |L_K(σ,χ)| ≤ ζ_K(σ) for σ > 1, so the values at 3/2 are bounded both ways
    **with no GRH and no A**;
  - **T6.2:** the output class of 032 Prop. 3.1 has degree zero;
  - **B19, B21:** in a CM isogeny class the least witness degree is pinched between multiples of √J,
    J = [Λ : Λ^−] (B19 checked).

### M4. Mumford's fourfold, Kuga–Satake and the triple tensor

- **Objects.**
  - A is Mumford's fourfold: Hodge group a Q-form of SL₂³, from a quaternion algebra D over a totally real cubic F.
  - V = H¹(A) is the 8-dimensional tensor induction of the standard representation of D^× from F to Q. Over Q̄ it is
    (2,2,2).
  - On the other side, a K3 surface S of rank 12 and its Kuga–Satake variety KS(U).
- **The map.** The Clifford morphism κ: U₀ → End H¹(KS(U)), κ(x)(a) = xae (Paper B, eq. canonical).
- **Transported:** the quadratic Lie block 𝔤 = Res_{F/Q} sl₁(D) acting on V.
- **Proved (Paper B):**
  - algebraicity of that block implies the Hodge conjecture for every power of A (statement level for us);
  - **the half-twist embedding ν cannot produce the block by commutators, Hodge endomorphisms or isogenous powers**
    (checked). On the derived group H₁ contains only (2,1,1), (1,2,1), (1,1,2), while the block is (2,2,2), and
    Hom_G(U₀, End V) = 0.

### M5. The sign-only purity proof (H01)

- **Objects:** X over F_q and a constructible F; and the Frobenius module H_c^*(X, F) in K₀.
- **The map.** One global sign (−1)^{D−1} makes the remainder R = Q·N − M^k an honest trace on
  H_c^d(U,F)^{⊗k} ⊕ K_k, with K_k = ker(Gysin) the evanescent part E^{n−1} of cote 16, scans 034–036 (HODGE_SIGN SG-08,
  checked).
- **Transported:** effectivity, giving the power-sum bound, giving |λ| ≤ q^{(w+i)/2} (HS-01, HS-02, SG-09–SG-11,
  checked).
- **Status:** published as hexagon:2611.00789.

---

## 2. Where each map sits on the Langlands ladder

| Rung | What sits there | Map | Where A enters |
|---|---|---|---|
| GL₁ over Q (Dirichlet) | A itself; cyclotomic Frobenius | M2 at primes split in K = Q(i), Q(ω): split primes in a residue class mod q | **A gives effective Chebotarev for abelian extensions of Q** (from memory: least prime in a progression ≪ (q log q)² under GRH). So in Paper A's arithmetic direction, for K = Q(i) or Q(ω), a good ordinary split prime v outside E_D can be chosen of explicit size in the level and the conductor |
| GL₁ over a CM field E (Hecke) | CM points and their reductions (M2); the L-values of M3 | M2, M3 | **Not reached by A** (Hecke RH for the Kummer character over Q(ω) is ALP_MACHINE Q3, open). M3 needs only s = 3/2, inside absolute convergence: B1 bounds it with no RH at all |
| U(1) → U(3), U(n,n) theta lifts | 032's surfaces; Weil classes (M1); THETA3's seesaw | M1, M3 | THETA3: the analytic seesaw is proved, but the definite matching with Alpöge's MainX is open (A7: the multiplicity space is totally definite exactly when the CM types agree) |
| Central values at s = 1/2 | Alpöge's chain: the bottom period | ALP_MACHINE LIFT074/077 (statement level): \|b\|² = (explicit constant) × L-ratio(1/2) × local factors | **This is where A's mechanism lives:** the definite unitary chain. Paper A has no central value; DEG_L's values are at 3/2 |
| Tensor induction F → Q, triple product | Mumford's fourfold (M4) | M4 | none yet |
| Function fields | H01 (M5) | — | the sign-only proof **is** Alpöge's footnote 3 made complete; there A's step 5 is a theorem |

**The next rung, as concrete statements:**
1. **GL₁ over E: one-prime lifting with an explicit prime.** For K = Q(i) and one CM point x (say E_i⁴ with the odd
   principal lattice), bound the least split ordinary prime v ∉ E_D in terms of D. With A this is a Dirichlet question:
   v ≡ 1 mod 4, plus a residue condition from the level. The missing input is an explicit E_D, the exceptional set of
   Proposition lift, which the run left non-effective (Q27 is its open row).
2. **Central values for the Weil engine.** Express the detector degree of the U(n,n) theta cycle at a CM point as a
   Rallis sum whose terms are **central** values (s = 1/2) rather than values at 3/2. Then a uniform detector bound along
   CM points is an upper bound for central values, where Hecke-GRH-type information (beyond A) would act, and a lower
   bound would need nonvanishing. M3 shows the 032 cycles land at 3/2, so this needs a different cycle, for example a
   Kudla–Millson special cycle of codimension n on the U(n,n) Shimura variety.
3. **Mumford by functoriality.** The block (2,2,2) is the triple tensor product. The Tate-side statement is that the
   order of the pole at s = 1 of L(s, ∧²(⊗-ind ρ)) counts Tate classes on A² (Tate's pole conjecture, from memory). A
   cycle-free route would need that order for the tensor-induced L-function: Asai/triple-product type.

---

## 3. Structural notes: the same mechanism in two fields

### 3.1 A remainder that is an honest trace, and Weil positivity

| | H01 (finite fields) | ALP_CONNES (Q), Connes's programme |
|---|---|---|
| Main term | M^k (point count of the path form) | 2 log Λ·h(1,1) + the polar terms |
| Remainder | R = Tr(F^n \| H_c^d(U)^{⊗k} ⊕ K_k), after one sign | the cutoff defect of Q_Λ against Weil's distribution W(h) (AC-T50, AC-T51) |
| The honest space | the Gysin kernel K_k = E^{D−1}(Y) (cote 16, scans 034–036) | the prolate images E_χ(PW_Λ), summed over χ |
| Positivity used | effectivity in K₀ plus the power-sum lemma (HS-01) | W(f∗f*) ≥ 0, the Connes–Consani–Marcolli criterion |
| Our result | Deligne's bound, weight-free (SG-08–SG-11, checked) | A ⟺ the trace-formula limit (AC-T51; the deduction checked in the ALP_CONNES intakes) |

**The dictionary:**
- the Gysin kernel ↔ the cutoff defect;
- the tensor power k ↔ the bandwidth Λ;
- Parseval on the path form ↔ Plancherel on the prolate window.

**The obstruction (SIGN_NEXT SN-14, checked).** Effectivity is weaker than positivity. A Jordan block N with
F = c·exp(N) has all traces Tr(aF^s) = 3a₀c^s, while τ(N^†N) = 0. So the sign-only mechanism cannot give the Hodge-index
positivity (scan 049, semisimplicity), and Weil positivity on Q is the stronger statement. On Q the positivity comes for
free from A, which is the converse direction of AC-T51.

### 3.2 Heat-flow positivity (ZETA_HEAT) and the detector minimum

- **ZETA_HEAT:**
  - H_{−a} = e^{a∂²}H₀;
  - the first negative Toeplitz minor appears at order ≈ x𝔯_m/(2√(2a)) near a zero of multiplicity m;
  - 𝔯_m is the spread at which the unitary orbital integral φ_m first turns negative (𝔯₂ = π, 𝔯₃ = 2π/√3);
  - simplicity ⟺ every detection index → ∞ (ZETA_HEAT primer §1).
- **Paper A (Q05):** the minimum cycle degree b_v at good reductions is eventually b₀, or tends to ∞.
- **The parallel:** a sequence of finite tests, each of finite cost; the global statement holds exactly when the
  minimal failing size escapes to infinity in a controlled way.
- **The dictionary:**
  - order of the minor ↔ cycle degree;
  - the heat time a ↔ the prime v;
  - multiplicity m ↔ the Weil-type defect.
- **What it suggests:** a "ghost" class (algebraic at every v, b_v → ∞) is the analogue of a multiple zero detected only
  at growing order. Then ZETA_HEAT's exact rate x𝔯_m/(2√(2a)) suggests asking for the **rate** of b_v → ∞ for a
  hypothetical ghost. Paper A's B04 (one-prime) and Q27 give no rate. A rate would turn the dichotomy into a finite test.

### 3.3 One symmetry eigenspace, three times

- **The Weil plane:** the extreme eigenlines of [a]^*, with eigenvalues a^{2n} and ā^{2n}. Extraction uses the integral
  polynomial ∏(S − α_j) (HD-U).
- **H01:** HS-01 separates eigenvalues by poles of the generating function. In both, a nonzero multiplicity cannot
  cancel.
- **ALP_MACHINE AM-S1–S3** (checked in my 22 Nov intake): a phase s of finite order d can replace the sign only if it
  commutes with Frobenius on an actual module, with powers divisible by d. A reflected phase sees only the part fixed by
  the rotation (counterexample: the standard representation of S₃ ⊗ Q_ℓ(−N)).

**The dictionary:** the K-character eigenlines of [a]^* ↔ the μ_d-eigenspaces of a finite phase. In both, an operator
that **inverts** the rotation (ā for a; the reflection s for the C₃ rotation) kills the rotating part:
- e_W is the projector that survives because a/ā is not a root of unity;
- AM-S2 is the failure when the analogue of a/ā is a root of unity.

**A test of this dictionary:** for K = Q(ω) with a = ω, a/ā = ω² is a root of unity, and HD-U's hypothesis fails. In AM-S2
the same C₃ makes reflected traces blind. So the cubic phase problem of the 21 Nov programme (an order-3 sign mechanism)
and the failure of the projector for a = ω are one phenomenon. Every working projector over Q(ω) uses a non-unit a
(3 + ω, or [√−3]), and pays a power of 3 in its denominator (HD-U's R; GHOSTS R10's denominator 54 = 2·3³).

### 3.4 Lifts that cannot carry a block

Two obstructions with the same shape:
- **Paper B, half-twist (checked):** ν lands in isotypic parts (2,1,1), …, disjoint from (2,2,2), so no Hodge-equivariant
  operation reaches the Mumford block.
- **ALP_MACHINE LIFT075** (checked in my checkpoint-32 intake): a type-II theta lift GL_a → GL_r adds d = r − a equal
  GL₁ characters, so its constituents carry a linear Green factor of multiplicity ≥ d. Alpöge's squarefree e0 kills it.

**The dictionary:** the representation-theoretic type of the lift (an isotypic support; a Green parameter) ↔ the
projector of the target (the Mumford block; e0). The obstruction is in both cases a disjointness of supports, proved
before any analysis. The common lesson is that a lift chosen for convenience must first be tested by its type against
the target projector.

---

## 4. What it suggests, most promising first

1. **An explicit one-prime criterion over Q(i) and Q(ω) using A.**
   - Make Paper A's exceptional set E_D effective for the families of the 48 and 36 bounds; the run's own Q27 row is the
     gate.
   - Then A (through least primes in progressions) gives an explicit ordinary split prime at which one bounded cycle
     certifies the class in characteristic 0.
   - This would be the first place where Alpöge's theorem enters the Hodge criterion as an input.
2. **A rate for ghosts (§3.2).** For a fixed variety and class, bound from below how fast b_v must grow if b₀ = ∞, in
   terms of the size of the Hilbert-scheme parameter space (degrees, the Chow form) and N(v). Even a weak rate gives a
   finite test with an explicit stopping point.
3. **Central-value detectors (§2, item 2).** Compute the degree of a Kudla–Millson special cycle of codimension n on the
   split U(n,n) Shimura variety, at a CM point, as a Rallis sum, and locate its L-values relative to s = 1/2.
   - If they are central, a uniform detector bound becomes a statement about central values of GL₁(E) twists.
   - That would connect the Weil engine to the rung where Alpöge's chain lives (ALP_MACHINE LIFT077).
4. **The cubic phase over Q(ω) (§3.3).** Prove the exact form: for a = ω every integral polynomial in [ω]^*, [ω̄]^* that is
   ≡ e_W modulo the middle summands has 3-adic denominator ≥ 3^{c(n)}, and compute c(n). This quantifies the obstruction
   that AM-S2 states qualitatively.
5. **The Mumford block by tensor induction (§2, item 3).** Write the Tate-side count of Tate classes on A_v² for an
   ordinary reduction of Mumford's fourfold. Test whether a uniform bound in v of the minimal cycle degree (Paper A's
   criterion, applied to the Mumford special family) can be obtained from the K3 side, where the Kuga–Satake
   correspondence is algebraic on reductions (from memory, Madapusi Pera).
