# Intake of GT_AFTER_H17, checkpoint 07 (prompt 95)

Claude Opus 5.5 at effort max (agent ae4ae3dc17acaa440), 25 Nov 2026, for the main session 329fb1e6, under the brief
`agent_notes/INTAKE_NEW_RETURNS_BRIEF_20261125.md`.
- **The checkpoint:**
  `grothendieck_archive_transcription_20261110/research_returns/GT_AFTER_H17_checkpoint_07_20261125T0716Z_unzipped/workbench/`.
  The run is GPT-6 Astra Pro (ChatGPT Pro mode).
- **Check events:** `INTAKE_GT_AFTER_H17_20261125_CHECK_EVENTS.tsv`.

**Before this intake.**
- No one outside the run had checked anything (`who_checked.py --source GT_AFTER_H17`: 589 ids, every check by the
  run's own same-model workers).
- The pile's INDEX has only the prompt (line 634).

**The checkpoint.**
- Two papers:
  - `papers/arithmetic_quotient/` (120 pp.);
  - `papers/gentle_characters/` (33 pp.).
- 185 statements, 645 in-run check events.
- Of these, 70 are "independent re-proof" by a separate worker of the same model, and 342 are "targeted proof check".

**What I read.**
- The README, QUESTIONS.tsv, the end of the LEDGER, and LITERATURE.md (searches).
- Both abstracts and the statement sections of both papers.
- Line by line, the two chains below. I could not read all 153 pages in one pass. The rest is carried as background, as
  §1 says, and is the place for the next reader.

## 1. Verdicts

| Statement (run's tag, printed number) | Claim | Verdict |
|---|---|---|
| AQ.013, Thm 1.2 (with AQ.006 Thm 5.1, AQ.007 Lem 6.1, AQ.008 Lem 6.2, AQ.009 Thm 6.3, AQ.010 Thm 6.4) | Ihara's integral cocycle ρ_d^I is even on multiplier one in GT̂₀ for every d. ψ_q = ρ_q^I/2 mod 2 is an invariant quadratic character of the normalized subgroup N = Λ₀, restricting to K₂(q^{1/4})/K₂, with K₂ = Q(μ_∞, 2^{1/∞}). dim H¹(Λ₀, F₂)^{GT̂} and its restriction image are both ℵ₀ | **Holds**, targeted proof check, every step followed (details below) |
| GC.014, Thm 11.5 (with GC.010-GC.013, Lems 11.1, 11.2, 11.4, Thm 11.3; GC.005 Thm 8.1, GC.006 Lem 8.2) | For every prime p ≡ 5 (mod 12) a continuous character ϑ_p : GT̂₀ → F₂ vanishing on GT̂. Jointly onto ∏ F₂ already on multiplier one. So the quadratic characters of the Harbater-Schneps group vanishing on GT̂, or on G_Q, form a space of dimension ℵ₀ | **Holds**, targeted proof check of the whole chain, including the peripheral-lifting machinery. Published input not opened by me: Ihara's beta factorization on all of GT̂ (Ihara 1999, Prop. 1.6.1, as recalled in Furusho 2003, §2.3, p. 101) |
| GC.025, Thm 1.2 and GC.018, Cor 11.6, quadratic factor | (GT̂₀/⟨⟨GT̂⟩⟩)^ab ↠ (Z/2)^ℕ | **Holds**, as GC.014 |
| GC.025, Thm 1.2 and GC.018, Cor 11.6, odd factors | ↠ ∏_{p≥5} ∏_{k,j} Z/p^k | **Carried as background**: rests on Brown's construction, "the all-weight upper bound of OpenAI" and Willwacher's proof of it, none opened |
| AQ.012, Thm 1.1 | GT̂/N ≅ Gal(K₂/Q) (affine group); GT̂^ab ≅ Ẑ^× × B; Hom(B, F_p) = ker(X_p → Y_p). This is Lochak-Schneps Q1.2 in exact form | **Carried as background**: statement and its use of the decomposition read, proof not checked |
| Normalizations through weight 10, uniform dyadic, mixed weight 11 (Thms 1.3-1.10 of the first paper; questions Q1.radical, Q1.weight5-11, Q1.uniform-dyadic) | Successive exact 2-adic images, already attained by G_Q; the kernel E′ carries the same relative obstruction | **Carried as background.** In-run: same-model statement-only re-proofs for weights 9, 10 and uniform dyadic; the cubic attack partial |
| CM frames, harmonic and cubic comparisons, χ₃ = 0 (Thms on adelic CM frames; Furusho-type identities) | Exact joint image; ε_h = ε_c = χ₃ = 0 | **Carried as background**: published inputs Furusho 2003, Lemmas 4.1-4.2 |
| Refuted extensions (η₅, η₇, η₈ do not extend invariantly) | Refutations by explicit arithmetic witnesses | **Carried as background** |
| GC.007 (weight 16, dim 75/37/38), Thm 1.3 pentagon mod 17, weight-12 certificate | Computations, reimplemented in-run | **Carried as background** |
| GC.024, Thm 1.3 (elliptic-frame character Δ on GT̂₀, witness in F̂₂‴) | Extends H17's normalized frame character δ/Δ to GT̂₀ | **Carried as background** |
| The run's citations of our notes | GT̂ = Λ₀·G_Q is "Theorem 2 of [H17]"; Lemma 7 gives the cocycle law and evenness of ρ₂; (IV), (III′) and IΓ = GT̂ are Theorems 1, 20 and Corollary 21; invertibility and the unit multiplier come from hexagon:2611.01024, Thms A, E | **Correct.** Verified against `h17_note_v2.tex` (Thm 2 at l.127, Lemma 7(b)(c) at l.368-369, Thm 20, Cor 21). The Monoid note's Thms A and E(b) are the ones I checked on 25 Nov |

**The dimension theorem (AQ.013), the steps I followed.**
1. **Lemma 6.1.** On H_d^ab, Φ_g sends [y_j] to λ[y_{λj mod d}], so ℓ_d∘Φ_g = λℓ_d. With f_{gg′} = f_g Φ_g(f_{g′}), this
   gives the cocycle law and ρ(gng⁻¹) = λ(g)ρ(n).
2. **Lemma 6.2.** In the class-two quotient of H_n, the boundary word (yx)^n is preserved up to conjugation. The
   coefficients of X∧Y_i force t_i = t_X, and those of Y_i∧Y_j then give c_j = c_{−j}.
3. **Theorem 6.3.** With n = 2d, c₀ + c_d = −2Σc_j. The input "φ(xy) conjugate to xy at multiplier one" is Lemma 3.1 of
   the Monoid note, rechecked on 25 Nov.
4. **Theorem 5.1.**
   - At p = 2, it uses Eisenstein quartics X⁴ − a and X⁴ − 2a, and the unique index-2 subgroup of
     Gal(K₂/Q^ab) = 2Ẑ.
   - At odd p, it uses Šafarevič for UT₃(F_p)^m, cited from Schmidt-Wingberg.
5. **Theorem 6.4.** Invariance holds because multipliers are odd. On K the character is the fourth-root Kummer character.
   R(K) = R(N) = 2Z₂^m by the mod-4 lifting argument. The countable bound comes from second countability.

**The quadratic family (GC.014), the steps I followed.**
1. **The value E_p and its sign.**
   - E_p(g) = B(ω,ω)B(ω²,−1)/(B(ω,−1)B(ω,−ω)) mod p obeys the crossed law. The twist σ_λ is Frobenius when
     λ ≡ −1 mod 3.
   - Ihara's associativity at (ω, ω, −1) gives E_p = 1 on GT̂.
   - Lemma 11.4 (genus 10, 18 boundaries, 36-fold cover) gives B(a,b)B(a⁻¹,b⁻¹) = 1 at multiplier one. Its
     form-preservation step needs φ to permute the boundary classes, so that the sum of their degree-two coordinates is
     unchanged. That is true, and implicit in the text.
   - So E_p has norm one, and ϑ_p = sign of E_p^{(p+1)/2} is a homomorphism (Frobenius inverts the norm-one group).
2. **Lemma 11.1.** α_p (−1 on the cubic pair V_p) is an automorphism of Q = ∏M_p ⋊ Γ₆, since V_p and W_p are
   Γ₆-stable. It acts trivially on H₂(Q, Z), because V_p ⊗ W_p has no coinvariants.
3. **Lemma 11.2.** The lift through finite central extensions is unique and involutive. The peripheral conjugators come
   from the invertibility of 1 − t on V_p, and z² = 1 forces z = 1.
4. **Lemma 8.2.**
   - The triple count is (1/|M|) Σ_ρ d_ρ⁻¹ ∏ tr S_{i,ρ}, over J-invariant ρ, through the projective central extensions
     Q_ρ. I re-derived it from the regular character and Schur's lemma.
   - Conjugating by (j_i, r_i) transports it term by term.
   - Möbius inversion over subgroups gives a new epimorphism.
5. **Theorem 8.1 and Theorem 11.3.** Compactness plus the Hopfian property.
   - The two inner corrections act trivially on all M_q.
   - (sf)² = (f⁻¹r)³ = 1 are the normalized (I) and (II), and the restriction to F is x ↦ x, y ↦ f⁻¹yf with f ∈ F̂₂′.
   - The witnesses give E_p = −1 at the chosen prime and 1 elsewhere, and (p+1)/2 is odd for p ≡ 5 (mod 12).

## 2. What is new

- **Against the pile.**
  - The pile's A4 ("GT̂ inside GT̂₀", INDEX: "No printed source has strictness of the inclusion. Its profinite steps are
    run-only") rested on LM8_PUSH C.39 and GT_TOWER_CHECK A.7: characters of GT̂₀ to F₅, F₇, F₁₃ vanishing on GT̂, with
    unchecked profinite steps.
  - This run gives a different family at the prime 2, ℵ₀ of them, with a complete profinite lifting argument, now read
    by me.
  - So **GT̂ ⊊ GT̂₀ is proved**, and more: the normal closure of GT̂ has a quotient (Z/2)^ℕ. The pile's earlier F₅, F₇,
    F₁₃ claims are subsumed by the run's odd-primary statement (for every p ≥ 5), which still rests on unchecked external
    inputs.
- **Lochak-Schneps Q1.2 (2006).** Is the abelianization of GT̂ given by λ?
  - Theorem 1.1 makes it exact: the relative abelianization B is dual to ker(X_p → Y_p).
  - Theorem 1.2 shows that invariant quadratic characters of Λ₀ abound (ℵ₀), with ℵ₀ restrictions to K = G_{K₂}.
  - It is the kernel of restriction that decides Q1.2 mod 2, and that kernel is open (the run's main question).
  - Every normalization in the first paper is "already attained by G_Q", so none produces a character of GT̂ trivial on
    G_Q. The run is candid about this.
- **Literature.** The run searched (LITERATURE.md) and found the classical sources. It found Marin 2008 §6.3 (weights 3
  and 5 through Burau rigidity) and Markarian, arXiv:2611.01745v2 (18 Nov 2026, restricted pro-2 tangent
  interpretation). Neither has the gentle quotient or the dimension theorem. I know of no printed proof of GT̂ ⊊ GT̂₀;
  Dolgushev-Guynee say only that GT̂₀ "obviously contains" GT̂.
- **For Grothendieck's questions.** It settles the strictness of the pentagon over the two cycle relations in the
  profinite setting: the two equations (I), (II) of La Longue Marche §46 do not determine GT̂. It does not settle Q1.2 or
  GT̂ = G_Q.

## 3. Consequences for the waiting prompts

- **Q09_31_SA28, PROMPT.md l.153.** Now: "Leads: our runs LM8_PUSH C.39 and GT_TOWER_CHECK A.7 claim GT̂ ⊊ GT̂₀, with
  characters of GT̂₀ to F₅, F₇, F₁₃ that vanish on GT̂ … the profinite steps are unchecked." It becomes statable as:
  - GT_AFTER_H17 (checkpoint 07) proves GT̂ ⊊ GT̂₀, and that GT̂₀/⟨⟨GT̂⟩⟩ has the quotient (Z/2)^ℕ, by characters ϑ_p,
    p ≡ 5 (mod 12) (its gentle paper, Thm 11.5, with Thm 8.1 and Lem 8.2). This was checked line by line by Claude Opus
    5.5 at effort max on 25 Nov, apart from Ihara's beta factorization (Ihara 1999, Prop. 1.6.1).
  - It also claims odd-primary quotients for every p ≥ 5 (Thm 1.2). These rest on Brown, an OpenAI all-weight bound and
    Willwacher, and are unchecked.
  - The question of that prompt ("whether those equations already determine the Grothendieck-Teichmüller group") then
    has the answer no.
- **Q03_INTAKE_A_ANABELIAN_SECTIONS, l.130-134.**
  - The first question there, (III′) on GT̂, is closed by H17 v2, Thm 20.
  - The second ("does the action of Λ₀ together with the Galois action form one action of GT̂ on the tower with marked
    points") has a partial run answer: GT_AFTER_H17 Q2.b says that the Nakamura-Schneps and Lochak-Nakamura-Schneps
    actions agree as outer actions for zero or one marked point, with an explicit inner correction. I did not check
    that.
- **Q05_28_SA30 (l.179-186) and Q06_30_SA31 (l.213).** They state the H17 v2 and Monoid results that this run uses.
  Nothing changes there except that both now have a downstream user. Q06's mention of the gentle group (l.193-194) can
  cite the strictness above.

## 4. Candidates for Hexagon

1. **"The profinite Grothendieck-Teichmüller group is not normally dense in the Harbater-Schneps group".** Countably many
   quadratic characters of GT̂₀ vanish on GT̂ (GC.014 with its chain). This is the strongest candidate: short (§§8 and 11
   of the gentle paper), answers a natural question, and closes the pile's A4. Still needed:
   - open Ihara 1999, Prop. 1.6.1 and Furusho 2003, §2.3 at the statement used (the beta factorization for all of GT̂,
     not only G_Q);
   - a literature search on the strictness of GT̂ ⊂ GT̂₀ (Harbater-Schneps 2000, Dolgushev-Guynee, Lochak-Schneps,
     Hexagon);
   - a reader of another model family before posting.
2. **The quadratic dimension theorem for Λ₀ (AQ.013).** Checked by me. It is a structural partial result on Q1.2 and
   would fit as a section of the same note, or as a remark in a note on Q1.2, rather than on its own.
3. **The odd-primary quotients (GC.025).** Not yet: open Brown's construction and the OpenAI bound with Willwacher's
   proof first.

## 5. Not checked here

- The 120-page first paper beyond §§5-6 and its statements: the weight 5-11 normalizations, the CM frames, the harmonic
  and cubic comparisons, the Brauer invariant and the Hecke conductors.
- The weight-16 and mod-17 computations.
- The frame character Δ on GT̂₀.
- Q2.b and Q2.c.

These carry only the run's same-model checks.
