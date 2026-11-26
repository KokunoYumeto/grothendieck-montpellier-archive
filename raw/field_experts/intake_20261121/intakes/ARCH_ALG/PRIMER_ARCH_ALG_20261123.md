# Primer: the mathematics of ARCH_ALG as of its final return (22 Nov 2026, 06:22 UTC)

By agent a0805369bae2ebddc (Claude Opus 5.5 at effort high), for the main session to read after a compaction. It
restates; it does not develop. Run: prompt 50, GPT-6 Astra (ChatGPT Pro mode), effort not exposed. It stopped
INCOMPLETE after two reviews without movement.

**Files.** Final return: `research_returns\ARCH_ALG_final_20261122T0622Z_unzipped` (`AR`). It continues ALPOGE_BRIDGES
checkpoint 09 (`AB`; "AB l." means lines of `ALPOGE_BRIDGES.tex`). Intake: `INTAKE_ARCH_ALG_20261122_final.md` in this
folder. Seed: `reports_20261122\paper_seeds\SEED_ARCH_ALG.md`, five papers.

**Check labels:**
- `[TPC]`: targeted proof check by our intakes;
- `[COMP]`: our computation;
- `[run]`: run only;
- `[stmt]`: statement level.

## Cote 136: divided-power de Rham theories (scans 111-121)

**Setting.**
- S = Γ_k(T). An admissible theory is a simplicial object C of bigraded (weight w, form q) strictly commutative
  differential divided-power S-algebras, with two conditions:
  - vertical cohomology equal to S^w in degree 0 and zero through degree d for w ≥ W_d, uniformly in the simplex;
  - each row C_*^{w,q} with acyclic normalization for large w.
- 𝒜_k is the category of these. Its model is B_n = Γ(x₀..x_n) ⊗ Λ(e₀..e_n)/(∑e_j), dx_j = e_j (AQ-136-DP-MODEL
  `[TPC]`).
- Grothendieck asks (p. 121) whether any two theories have a common source C″ (conjecture (a)), whether two parallel
  maps are "equalized" (« égalise ») by some C″ → C (conjecture (b)), and whether the groupoid obtained by inverting
  all maps is a point.

**Main theorem, in four parts.**
1. **AQ-136-STRICT `[TPC]`** (AB l. 3223-3338). The strict conjecture (b) is false over every nonzero ring. The two
   maps are j₀, j₁ : B ⇉ B ⋉ M, j₁ by the universal relative divided-power derivation.
2. **ARCH-136-HOM-DEFINITION, PATHS, FRACTIONS, HOM-SEMILOCAL `[TPC]`** (`AR\research\cote136\homotopy.tex`).
   - Homotopy: a strict map into the cotensor n ↦ C(Δ[n]×J), J a finite edge path, with constant coefficients.
   - PATHS: path cotensors and their pullbacks are admissible. Leaves of J collapse; the comparison bound is
     independent of the simplicial set; endpoint maps are surjective on acyclic rows.
   - FRACTIONS: right fractions modulo homotopy compute the all-arrow groupoid, with f = g there iff fh ≃ gh for some
     admissible h. The cancellation axiom is proved by the pullback (Y×Y)×_{Z×Z}P_J Z (Stacks 04VB, 4.27.14).
   - HOM-SEMILOCAL: homotopy-(b) holds iff every component is simply connected; with (a), iff the groupoid is a point.
3. **The semilocal theorem `[TPC]`.** If all but finitely many primes are units in k, there are strict common sources,
   homotopy-(b) holds, and the groupoid is a point. Lemmas:
   - **COMPARISON** (AB l. 3035-3112): H^j(C^{w,*}(X)) ≅ H^j(X;k) ⊗ S^w for large w, uniformly in the simplicial set
     X. Proof by derived sections on simplicial sets and two hypercohomology spectral sequences.
   - **PLOCAL** (AB l. 3549-3676): over a ℤ_(p)-algebra take N = p^e. The map Γ(U) → Γ(T), U ↦ T^{[N]}, makes S free,
     since c_m = (mN)!/(m!(N!)^m) is a p-adic unit. Then B_N = S ⊗_{Γ(U)} B maps to every target once its weight-N
     zero-form row is acyclic: lift T^{[N]} to a normalized primitive.
   - **SEMILOCAL** (AB l. 4417-4832), five steps:
     1. the fracture sequence 0 → M → ⊕M_i ⊕ M₀ → M₀^s → 0 (Chinese remainder theorem, flat ℚ^s);
     2. a rational tensor lemma, with the Koszul basis change η_i = ξ_i − t^{N_i−N₁}ξ₁;
     3. arithmetic path replacements ℰ(C) with de Rham paths K[z,dz];
     4. one local source per prime with coordinate homotopies for every edge of a finite diagram;
     5. gluing, after which every finite word telescopes to β_end β_start⁻¹.
   - **COSPAN, CONNECTED-SOURCES, SEMILOCAL-SOURCES** (AB l. 5601-5800): the path pullback (A×B)×_{C×C}P_s C is
     admissible; common sources ⇔ connected; hence strict sources in the semilocal range.
4. **ARCH-136-ARITH-BOUND `[TPC]`** (`AR\research\cote136\arithmetic_improvement.tex`). With one rational
   B_N(K) in place of the tensor of local models, the source is horizontally acyclic in form q for
   w ≥ (q+1)·max N_i, with vertical bound N(d+2). The sum ∑N_i of (136.S2) disappears. max N_i ≥ p for p > N cannot,
   for these prescribed local models.

Good for: Grothendieck's question has a precise form and a positive answer away from ℤ. Over ℤ the whole difficulty
is one cutoff for all primes.

**Toward ℤ, route records `[stmt]` (`AR\research\cote136\`, `AR\research\cote15\136\`).**
- DEGREE-TWO-FREE: a free source with every condition except vertical H² in degree two.
- DEGREE-TWO-RESIDUE: the obstruction is differences of coefficient residues of H²[N].
- DEGREE-FOUR-CONCENTRATION: an alternative source with only degree four left.
- LOW-TATE-RETAINED-COMPLETION, FREE-PARTIAL-NONCOMPLETION: no admissible completion retains a prescribed diagram.
  The targets are equal, so this refutes a route, not (a).
- ASSOCIATIVE-TERMINAL: the associative analogue is terminal over ℤ.
- TW-TOR: the strict PD totalization keeps Tor (ℤ/p in weights p^a).
- About 120 further repair and obstruction lemmas.

**Open:** connectedness of 𝒜_ℤ (conjecture (a)), terminality, homotopy-(b) over ℤ.

## Cote 134-8: the linear Thm(?) of the Dérivateurs (scans 046-056)

**Setting.** A k-linear abelian ℳ with enough projectives; an exact scalar embedding κ with φ ⊣ κ ⊣ ψ and
Lφκ = id; a symmetric monoidal bilinear tensor; an interval with Lφ(J⊗C) = 0. The Thm(?) says that localizing at the
maps inverted by Lφ gives D_{≥0}(k). Proved earlier, `[stmt]`: under coproduct compatibility, so in particular under
AB4 with enough projectives (F-SM-32); and comparison maps monic in all degrees, bijective in degrees 0 and 1 (F-SM-44).

**ARCH-134-01 to 03 `[TPC]`, given F-SM-34** (`AR\research\cote1348\arch134_checked.tex`).
- Construction: 𝒜 = triples (V, X, h : κV → X) over F-SM-34's category 𝒩 (in which L_{2r}φ(κV) = E^r(V),
  E(V) = V**/V), with a pushout tensor; ℳ = Ch_{≥0}(𝒜), with J = the disk D₁(1).
- Statement: every axiom holds, but ⊕L₂φ(X_s) = 0 → L₂φ(⊕X_s) = E(k^(ℕ)) ≠ 0, so the class W is not closed under
  countable sums. Still ℳ[W⁻¹] ≅ D_{≥0}(k): the derived adjunction has invertible counit.
- Good for: higher coproduct surjectivity is neither implied nor needed. The Thm(?) itself stays open.

ARCH-134-04 (the raw counit over noetherian rings of finite Krull dimension), 05 and 06 (further models) `[stmt]`.

## Cote 15: motives over F_p (scans 092-107)

- **ARCH-15-HONDA-CHECK `[TPC, lines read]` `[COMP]`** (`AR\research\cote15\cote15_honda_check.tex`).
  - Statement: K = ℚ(√−23) (h = 3), γ = 12 − 4√−23, with γγ̄ = 512 and γ + γ̄ = 24, and Frobenius polynomial
    (t²−24t+512)³ over F₅₁₂. The abelian variety is a geometrically simple threefold; its endomorphism algebra is the
    division algebra of degree 3 over K with invariants 1/3 and 2/3 at the two primes over 2. Its isogeny class does
    not descend to F₈ = F_{2^{h_K}}.
  - Mechanism: Tate's invariant formula (Bourbaki 352, p. 96). A descended label α must satisfy α³ = ±γ, and the local
    cube roots give invariant 1/3 ≠ 0.
  - Good for: it contradicts Thakur arXiv:2001.00210v1 Prop. 2.9 as the run reads it (draft note E6). The preprint
    was not opened by us.
- **SPLIT-CUBIC, KUMMER `[stmt]`.**
  - f(x)+g(y) = 0 has a degree-3 map from Bl(S_f × S_g) (Shioda-Katsura).
  - Kummer surfaces: h(K) is a summand of h(Ã) by a degree-2 map.
  - Both give forward Chow cycles.
- **CUBIC-GATE, K3-GATE `[stmt]`:** for a general cubic fourfold or finite-height K3, forward cycles exist iff a
  finite family of mixed Tate classes is algebraic.

## Cote 123: the letter to Kostant of 22 Oct 1969 (scans 022-023)

- **Apposition quadruples `[TPC for CC-APG01, CC-APG04 existence]`** (AB l. 18648-19550).
  - There are |W|²/(hzφ(h)) classes.
  - Some choice of Borels is always opposite; every choice is opposite exactly in A_r with r+1 prime, B₂ and G₂.
  - An Out-invariant class exists iff the type is not A_{2m}.
- **ARCH-123-COUNT `[COMP, n ≤ 9]`** (`AR\research\cote123\companion.tex` l. 284-363).
  - Statement: in type A_{n−1}, n = 2m = 2^s u, exactly [2^m m!]²/(n²φ(n))·(n/2 or n)·2^{ω(u)} classes have
    automorphism group C₂ (8 of 18 for n = 4); none for odd n.
- **The subregular guesses are false:** in every type the rank there is r − 1. This is known (Richardson 1987,
  Lemma 5.1, after Slodowy).

## Where the results went

- **Seed:** `SEED_ARCH_ALG.md`, five papers: 136 (lead), 134-8, 15, 123, and 133 (from GCT_PLETH).
- **Errata:** note E6 (Thakur) in `reports_20261120\errata\`.
- **Superseded:** ALPOGE_BRIDGES's bound (136.S2), and prompt 50's surjectivity route to the Thm(?).
- **Hexagon:** none ready; the gates are in the intake's §8.
