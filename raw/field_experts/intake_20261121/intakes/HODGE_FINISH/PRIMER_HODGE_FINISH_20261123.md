# Primer: the mathematics of HODGE_FINISH (the Hodge papers A and B)

By Claude Opus 5.5 at effort high (agent aaf694615cb43adc1), 23 Nov 2026, for the main session to read after a
compaction.

- **Papers:**
  - A = `research_returns\HODGE_FINISH_final_20261123T1713Z_unzipped\workbench\work\UNFILED-A\v1\paper\main.tex`
  - B = the same path with `UNFILED-B`
- **Authorship:** GPT-6 Astra (ChatGPT Pro mode) produced both papers.
- **Check labels:** they are only those in `INTAKE_HODGE_FINISH_20261123_final_CHECK_EVENTS.tsv` and in the
  HODGE_BOUNDED_CYCLES intakes of the same agent line.

## Setting

- **Special family.** A special family with a Hodge class (S, θ, t) has:
  - S, a connected Shimura variety at neat level;
  - a map S → A_{g,N} (N ≥ 3) induced by a morphism of Shimura data;
  - the pulled-back principally polarized abelian scheme;
  - t, a flat section of R^{2p}f_*Q(p), of type (p,p) everywhere.
- **Complexity.** c_t(s) = min max(M, deg Z⁺, deg Z⁻) over M·t_s = [Z⁺] − [Z⁻], with Z^± effective integral cycles;
  it is ∞ if there are none.
- **Weil setting.** For a 2n-fold with imaginary quadratic K of signature (n,n):
  - W_K = ∧_K^{2n}H¹ is the Weil plane;
  - δ_W is the least degree of an irreducible subvariety with nonzero Weil projection (a *detector*).

## 1. The criterion (A, Theorems family and global; register Q01)

**Statement.** For one family, these are equivalent:
- (i) t_s is algebraic for all s;
- (ii) c_t is bounded;
- (iii) c_t is bounded on one Zariski-dense set;
- (iv) there is one D such that, for every CM point x and every number-field model, infinitely many good places v admit
  some geometric place, some ℓ and some M with sp(t_x) = (cl Z⁺ − cl Z⁻)/M, deg Z^± ≤ D (M unbounded a priori).

Globally: the Hodge conjecture for all complex abelian varieties ⟺ (ii) or (iv) for every special family. The inputs
are published only; the CM Hodge theorems (OpenAI 032; van Hoften–Sempliner) are not inputs.

**Mechanism.**
1. Bounded cycles are parametrized by finite unions of products of projective Hilbert schemes (SGA 6 XIII 6.11,
   FGA 221). Their cycle classes are locally constant sections (SGA 4 XVIII 2.9, SGA 4½ Cycle). Hence
   {c_t ≤ C} is closed.
2. Baire: a countable union of proper closed sets cannot cover S(C). A closed set containing a dense set is all of S.
3. Arithmetic direction: properness over O_L. Vertical components lie over finitely many places, so one place outside
   them lifts a bounded cycle to characteristic 0. Descent to Q̄ uses a Q̄-point of the component.
4. The multiplier: on A × A, with P = m*θ − θ₁ − θ₂ (the Poincaré class) and q_t = |∫(t⊠t)P^{2d}| > 0, constant in the
   family:
   - M²q_t ≤ C(2d,d)(deg Z⁺ + deg Z⁻)²;
   - proof: H ± P are nef, and positivity uses ∧^{2d}J fixing a real (p,p) class;
   - it holds in every characteristic.
5. Every Hodge class lies on a special family: Zarhin's trick or an isogeny to a principal polarization; the
   Mumford–Tate datum; CM points dense by real approximation.

**Dichotomy (Q05).** For one variety over a number field and one class, the minimum degree at good reductions either
equals the characteristic-0 minimum outside finitely many v, or tends to ∞.

## 2. The Weil engine (A; Q02, Q03, Q04, Q10, Q12)

- **Extraction (Q02).**
  - *Statement:* δ_W ≤ c_t ≤ ⌈2·16^n/n!⌉·δ·⌈√T⌉·Nm(a)^{n(2n+1)}·δ_W², for any integral a ∈ K with a/ā not a root of
    unity and any polarization type.
  - *Mechanism:* the polynomial ∏(S − β_j) in S = a* + ā* is P(β₀)e_W, an integral correspondence of mass ≤ 4^n q^{n²}.
    Then u = P(S)[Y] and v = a*u span a sublattice of index m in W_Z; clear by mδt = ru + sv, with r, s bounded through
    determinants. The norm bound is ‖e_W[Y]‖ ≤ deg/(n!√vol) (Wirtinger, translation-invariant forms).
- **Small detectors (Q03).**
  - 48 on even principal Gaussian fourfolds: van Geemen's ruling plane sits in a complete intersection of two |2θ|
    divisors, of class 4θ² and degree 96, killed by e_W; the detecting part or its residual has degree ≤ 48.
  - 192 on the odd lattice: a degree-16 isogeny.
  - 36 on principal Eisenstein fourfolds: Schoen's 2007 surfaces through a degree-9 quotient. Three times the integral
    Weil lattice is algebraic, and c_t ≤ 17δ⌈√T⌉.
  - The Schoen 2007 locator (Th. 1.1, p. 585) is cited, but the run did not obtain the full text.
- **Stabilization (Q04).**
  - Bounded split detectors in dimension 2n+2 give bounded detectors in dimension 2n, for every determinant and every
    K, through the product with the balanced CM surface E_K² and contraction by divisors.
  - The explicit factor is max(1, Nm τ/Δ)/(n+1), from [Γ_u] + [Γ_{−u}] = 2(ϑ₁ + Nm(u)ϑ₂).
- **Principal quotient (Q10).**
  - Every split Weil 2n-fold with O_f-action has an isogeny q to a principally polarized split one with Hermitian
    lattice H(Q), q*Θ = t_K f L, deg q = (t_K f)^{2n}Δ.
  - Mechanism: saturate a maximal isotropic subspace, split S = P₀ ⊕ Q, the unimodular Γ = P′ ⊕ Q, and the shear by η
    with η + η̄ = t_K. Steinitz classes are removed at cost m_K^n, with m_K ≤ (2/π)√|disc K| (Minkowski).
  - So one family U^n per (K, n) suffices.
- **Strong semiregularity test (Q12).**
  - For e^B ch(E) = w ∈ W_K \ 0 and a finite group of translations and Pic⁰-twists: injectivity of σ² on invariant
    Ext² ⟺ dim Ext²(E,E)^G = 2n(2n−1); always ≥.
  - Mechanism: HKR, HH* = ∧*H with H = H¹(O) ⊕ H⁰(T). The trace identity is σ∘ev(x) = x·ch(E), and σ² is Serre-adjoint
    to ev^{g−2}. Writing w ↦ a·vol_{H₁} + b·vol_{H₂}, its annihilator in ∧²H is H₁⊗H₂, of rank 2·C(g,2) on the rest.
- **Higher dimensions, with declared unrefereed inputs (Q09, Q28, Q24):**
  - all-field split sixfolds, δ_W < 10^179 d^53 f³ Δ (Markman's secant construction and Perry);
  - Eisenstein eightfolds B₀f⁴Δ (Severn, G₃₄);
  - Gaussian sixfolds of class [−3], δ_W ≤ (Δ/3)ℬ (Severn, E₈).
  - Q24's lattice lemma: every pairing-integral Z[i]-lattice of signature (3,3) and class [−3] embeds isometrically in
    U ⊥ U ⊥ ⟨1,−3⟩.
    - Locally: split gives A ⊕ A^∨; odd inert gives exponents ≤ 1, one exponent at p = 3; at 2 a maximal lattice is
      unimodular, and the even case would be U³ of class [−1].
    - Globally: one special genus, principal Z[i], strong approximation for SU(3,3).
    - Hence 3 | Δ and the transport index is Δ/3.

## 3. Paper B

- **Obstructions to specified eightfold constructions:**
  - Q11: 35 invariant quadratic relations, minimum rank 24 against the needed rank 10;
  - Q13: 448 versus 56;
  - Q16 and Q17: tree and generic networks;
  - Q14: finite-cover rank thresholds;
  - Q20: coherent sheaves on very general Weil tori;
  - Q21: the global-resolution counterexample.
- **Positive trace networks:** Gaussian Q18, 6,272 equations; Eisenstein Q32, 8,960 equations. Only the diagonal trace
  equations are solved.
- **Mumford fourfolds:**
  - Q29: a coniveau-one part of the rank-16 summand P ⊂ H³ of a balanced split sixfold gives the Hodge conjecture for
    all powers.
  - Q23: algebraicity of the quadratic Lie block 𝔤 → End V gives the same; the canonical Clifford (Kuga–Satake)
    statement of Bolognesi–Laterveer suffices.
  - The half-twist embedding cannot give the block, by an isotypic argument: the (2,1,1)-type pieces versus the
    (2,2,2) Mumford block.

## 4. Open rows and their gates

| Row | Gate |
|---|---|
| Q06 split eightfolds outside Q(√−3) | the principal Gaussian U⁴. A pure-character seed needs invariant Ext² = 56 (or a positive-character deformation with Ext² = 104). The network solves only the vertex-diagonal trace equations |
| Q07 uniform split detectors, every K and n | one U^n family per (K, n) suffices (Q10); needed: a uniform family of gluable semiregular objects or of bounded supports |
| Q08 Mumford exceptional family | the Lie-block or coniveau premise (Q23, Q29) |
| Q19 | off-vertex products, the upper extension equation, Ext² |
| Q22 | the analytic bridge for arbitrary perfect objects |
| Q25 | uniform degrees in the CM constructions |
| Q26 | a fixed complete-intersection multiple ⟺ bounded δ_W; construction needed |
| Q27 | effective Galois-orbit comparison |

## 5. What to do next

- obtain Schoen 2007 (Th. 1.1, p. 585);
- open Bolognesi–Laterveer (Th. 4.4, Prop. 6.2) before any remark on the half-twist route goes out;
- view the pages of both PDFs.
