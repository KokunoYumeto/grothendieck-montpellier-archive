# Primer, Part B of prompt 76: Grothendieck's two homotopy conjectures (cotes 136 and 134-8), as of checkpoint 04 (23 Nov 2026)

This primer is by agent a9e9559d (Claude Opus 5.5 at effort high), for the main session to read after a compaction.

**The run** (GPT-6 Astra, ChatGPT Pro mode) **has not started Part B.** At checkpoint 04 both Part B questions are "NOT YET ACTIVE" (QUESTIONS.tsv; LEDGER.md, "Part B — not yet active"). The mathematics below is therefore the inherited state: the seed `ours/seed/SEED_ARCH_ALG.md`, Papers 1-2, in the ZIP of prompt 76, restated faithfully.

**Check labels:** `[ARCH_ALG intake]` marks checks by our ARCH_ALG intake (Claude Opus 5.5 at effort high, 21-22 Nov), as the seed's tables record them. Nothing here was checked in this task.

## 1. Cote 136: divided-power de Rham theories

**The setting.** k is a commutative ring and S = Γ_k(T).
- An **admissible theory** is a simplicial object C of nonnegatively bigraded (weight w, form degree q), strictly commutative differential algebras with divided powers over S, such that:
  - for each d there is a W, independent of the simplex, with H^0(C_n^{w,*}) = S^w and H^p(C_n^{w,*}) = 0 for 1 ≤ p ≤ d, for all w ≥ W;
  - for each q the simplicial module C_*^{w,q} has acyclic normalization, degree zero included, for all large w.
- 𝒜_k is the category of admissible theories. These two conditions are **our reading** of the conditions on the scans (physical pp. 111, 117, 119, 121).
- **The model:** B_n = Γ_k(x_0, …, x_n) ⊗ Λ_k(e_0, …, e_n)/(Σ e_j), with dx_j = e_j.
- **Homotopy ≃:** finite chains of maps into the cotensors n ↦ C(Δ[n] × Δ[1]).

**Theorem**, the seed's Paper 1, with proofs in AB (ALPOGE_BRIDGES.tex) and AR (`research/cote136/`).
1. **STRICT** `[ARCH_ALG intake: targeted proof check]`. For every nonzero k, ℤ included, there are two maps j_0, j_1 : B ⇉ B ⋉ M (the second is the universal relative divided-power derivation) that no admissible C'' → B equalizes. The strict conjecture is false.
2. **PATHS, FRACTIONS** `[ARCH_ALG intake: targeted proof check]`. For every k, inverting all maps of 𝒜_k is computed by right fractions modulo ≃.
   - Two parallel maps f, g become equal iff fh ≃ gh for some admissible h.
   - "Equalized up to ≃ after precomposition" holds iff each component of the groupoid is simply connected.
   - With common sources, this means the groupoid is a point.
3. **SEMILOCAL, COSPAN, CONNECTED-SOURCES, SEMILOCAL-SOURCES** `[ARCH_ALG intake: targeted proof check]`. If all but finitely many primes are invertible in k:
   - every finite family has a common admissible source, by strict maps;
   - every parallel pair is equalized up to ≃ after a precomposition;
   - the all-arrow groupoid is a point.
4. **ARITH-BOUND** `[ARCH_ALG intake: targeted proof check]`. Over a Z_(P)-algebra with P = {p_1, …, p_s}, let N bound the zero-form acyclicity and take N_i = p_i^{a_i} ≥ N. Then the comparison object is horizontally acyclic in form degree q for w ≥ (q+1)·max N_i, and has coefficient cohomology through degree d for w ≥ N(d+2). There is no sum over the primes in the bound.

**The mechanism.**
- COMPARISON: H^j(C^{w,*}(X)) ≅ H^j(X;k) ⊗ S^w for large w, uniformly in X.
- One prime (PLOCAL) and the rational case are glued by the fracture sequence; finitely many primes glue because max N_i is finite.
- Over ℤ the cutoffs N_i ≥ p for p > N grow without bound, so the local models do not glue.

**Toward ℤ** (the seed's last section; statement level only):
- DEGREE-TWO-FREE: a partial free source with every condition except vertical exactness in degree two.
- DEGREE-TWO-RESIDUE: the obstruction is a difference of coefficient residues.
- Noncompletion theorems: no repair keeps an arbitrary prescribed partial source with its two maps. This refutes a route, not the conjecture.
- ASSOCIATIVE-TERMINAL: the associative analogue is terminal over ℤ.

**Open row B136-integers.** Over ℤ: do any two admissible theories have a common admissible source, and is the all-arrow groupoid a point?
- **Gate:** one weight cutoff valid for all primes at once (the degree-two simultaneous lifting of an H^2[N] class with its residues).
- **Routes not tried:**
  - a weight-tail invariant (π_0 of maps out of B; Steenrod-type operations with the weight multiplication);
  - a model not built from local sources (the PD envelope of binomial forms; a weight-filtered crystalline complex);
  - a transfinite small-object argument that changes old maps;
  - descent along ℤ → ∏ Z_(p) with a bound on q·p^{a_p}/w.

## 2. Cote 134-8: a derived left adjoint that does not preserve coproducts

**Grothendieck's hypotheses**, in our reading. ℳ is a k-linear abelian category with enough projectives, equipped with:
- an exact scalar embedding κ with adjoints φ ⊣ κ ⊣ ψ and Lφ∘κ = id;
- a symmetric monoidal bilinear tensor;
- an interval 1 → J, monic after tensoring, with Lφ(J ⊗ C) = 0.

His Thm(?), on physical pp. 48-49: inverting the maps W inverted by Lφ gives D_{≥0}(k).

**Theorem**, ARCH-134-01/02/03 `[ARCH_ALG intake: targeted proof check, given F-SM-34]`. For every field k there is a complete and cocomplete such ℳ, with a colimit-preserving tensor and a flat interval and quotient, in which:
1. ⊕ L_2φ(X_s) → L_2φ(⊕ X_s) is not surjective: its source is 0 and its target is E(k^(ℕ)), where E(V) = V**/V;
2. W is not closed under countable coproducts;
3. nevertheless ℳ[W^{-1}] ≅ D_{≥0}(k).

So this is no counterexample to the Thm(?): it shows only that the natural proof, which resolves by sums and applies Lφ termwise, fails.

**Mechanism.** It is built on F-SM-34, a category 𝒩 with L_{2r}φ_𝒩(κV) = E^r(V); this was read as a statement only. The square-zero unitization ARCH-134-01 then gives the example.

**Positive results** (statement level):
- the Thm(?) holds when coproducts are compatible, in particular under AB4 with enough projectives (F-SM-32) and in countable form (F-SM-33);
- the comparison is monic in all degrees and bijective in degrees 0-1 (F-SM-44);
- the raw counit over Noetherian rings of finite Krull dimension (ARCH-134-04);
- two further models (ARCH-134-05, -06).

**Open row B134-localization.** Is ℳ[W^{-1}] ≅ D_{≥0}(k) from the axioms alone, or is there a counterexample where the localization differs?
- **Gate:** every known proof uses coproduct compatibility or the all-scalar counit.
- **Routes not tried:**
  - simplicial resolutions by J^{⊗n} with finite sums only;
  - fractions in the homotopy category of cofibrants without small-object arguments;
  - a non-reflective W from an adjunction whose derived unit needs uncountable sums.
- **Prompt 76 also asks to reprove F-SM-34.**

## 3. Where the records are

- Seed: `ours/seed/SEED_ARCH_ALG.md`, ll. 21-242 (Papers 1-2).
- Proofs: AB `ALPOGE_BRIDGES.tex`, line ranges in the seed's tables; AR `research/cote136/`, `research/cote15/136/` and `research/cote1348/`.
- Earlier intake: `field_experts/intake_20261121/intakes/ARCH_ALG/INTAKE_ARCH_ALG_20261122_final.md`.
