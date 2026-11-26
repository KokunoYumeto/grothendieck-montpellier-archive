# The inputs of H1: the standard conjectures and Tate on all powers of the fourfold axes in E⁶

By Claude Opus 5.5 at effort high (agent acc1e1c0), for the main session 329fb1e6 (Claude Opus 5.5 at effort max),
25 Nov 2026. It follows the brief `agent_notes\acc1e1c0_H1_INPUTS_BRIEF_20261125.md`. Check events:
`CHECK_H1_INPUTS_20261125_CHECK_EVENTS.tsv`, beside this file.

## Verdict

**H1 is unconditional. It rests on published theorems only.** The two unrefereed inputs from OpenAI's 032 manuscript
(Milne's report, hexagon:2611.00244), C44_POS:032-Cor8.3 (Tate for abelian varieties over finite fields) and
C44_POS:032-Cor8.4 (signed Hodge standard conjecture with numerical = homological for abelian varieties), are **not used
anywhere in the H1 chain**.
- **Where they are used:** only in C44-W02, W03 and W06 (Theorem W in characteristic p, `C44_POS.tex` 31717 ff.); in
  C44-A08's general-ambient positivity (l. 2339); and as a remark on general abelian ambients after A42b (l. 15242,
  which says "Neither is used in this corollary").
- **What the chain needs instead:** the ambient E⁶ is supersingular at the selected primes. For powers of a supersingular
  elliptic curve, both inputs are covered by published theorems: Tate 1966, and Milne 2002, Remarks 3.7–3.8.

No fault found in any step I read.

**What I did not check:**
- A13's geometry and monodromy (targeted check by a8d753525905811ab, Claude Opus 5.5 at effort high, 22 Nov);
- the Chebotarev step through Entin;
- Steps 3–5 of A30 beyond the core positivity mechanism, which I independently re-derived on 24 Nov.

These stand as they were checked before.

## 1. What the H1 chain uses, and for which varieties

The chain: C44_POS final, A13 (l. 2627–2946), A28 (27076–27466), A30 (27722–28166) and A30a (28169–28246). B is a
smooth fourfold axis in A = E⁶, E: y² = x³ − x, at primes p ≡ 3 (mod 4). There E has CM by Z[i] with p inert, so E is
supersingular; over F_{p²} its Frobenius is the scalar −p. Then H*(B) = U ⊥ K ⊥ W:
- U, the ambient part, is a restriction from H*(E⁶);
- K = Q_ℓ w;
- W is the variable part with generic Frobenius.

| Need | Variety | Form | Where used |
|---|---|---|---|
| (a) Every even-degree class is spanned by divisor products; Tate for these | E^N, every N (E⁶ for B; E^{12} for B×B; E^{6N} for B^N) | over Q_ℓ, then over Q by a rational Gram matrix | A28, "unconditional supersingular abelian input" (27286–27316); A30 step 6 (Tate surjectivity, ambient part) |
| (b) Hodge standard conjecture with numerical = homological, for an arbitrary product polarization | E^{12} = A × A (and E^{6N}) | signed primitive forms positive on algebraic classes, every ℓ ≠ p | A28 ambient tensor block (27318–27382); A30 ambient blocks |
| (c) Maximal Frobenius torus at dense closed points | the lisse sheaf 𝒲 of W on the parameter curve | Chin, JAMS 17 (2004), Th. 5.7 | A28 selector (27138–27165); A30 step 1 (27770–27852) |
| (d) Lefschetz standard; numerical = homological from Hodge standard plus Lefschetz | B, B^N | Kleiman 1994, Prop. 5-1 | A28 (A28.7)–(A28.9); A30 step 6 |
| (e) Hodge index theorem for divisors, in any characteristic | B | signature (1, ρ₁ − 1) of ∫DD′L² | A30a only |

**Nothing in the chain needs a statement about a general abelian variety, or about an abelian variety that is not
isogenous to a power of E.** The Tate and Hodge statements are needed only for supersingular E^N.

## 2. Published theorems for each need, opened at the source

**(a) Tate on E^N: Tate 1966 suffices.**
- *Input:* Tate, *Endomorphisms of abelian varieties over finite fields*, Invent. Math. 2 (1966), Main Theorem. The run
  read it at p. 134 (its event C44-A28-primary-inputs, GPT-6 Astra, ChatGPT Pro mode, effort not exposed). I did not
  reopen it; it is the classical theorem.
- *Re-derived by me:*
  - After a finite extension, Frobenius on H¹(E) is a scalar, so Tate's theorem gives End(E) ⊗ Q_ℓ = M₂(Q_ℓ) =
    End(H¹(E)).
  - So H²(E^N)(1) is spanned by the coordinate classes and the graphs of endomorphisms: its Künneth pieces are the
    coordinate H²'s and the 4-dimensional pieces H¹ ⊗ H¹.
  - H^{2r}(E^N) = Λ^{2r}(H¹(E)^{⊕N}) is generated as an algebra by Λ², since a wedge of 2r vectors is a product of r
    wedges of two.
  - Hence all even cohomology is spanned by divisor products. The rational upgrade pairs an algebraic class against a
    rational dual basis of divisor products.
- **So every algebraic class on E^N is Lefschetz, and all even cohomology is algebraic after a finite extension.**
- Spiess (Math. Ann., DOI 10.1007/s002080050295) proves Tate for all products of elliptic curves over finite fields. It
  covers E^N, but it is not needed for this supersingular case. I confirmed only its bibliographic record, not its text.

**(b) Hodge standard conjecture with numerical = homological on E^N: Milne 2002, Remarks 3.7–3.8, suffice.**
- *Source:* Milne, *Polarizations and Grothendieck's standard conjectures*, Ann. of Math. 155 (2002) 599–610. I opened
  the arXiv source, math/0103175v3; its labels are `t5` and `t7`. The run cites Remarks 3.7–3.8 from an 11-page author
  copy, p. 9; I did not recheck the Annals numbering against the printed journal.
- **Remark t5 states:**
  - on Lefschetz classes, homological equivalence is independent of the Weil cohomology and equals numerical
    equivalence (from Milne 1999a, 5.2);
  - the forms (−1)^r⟨L^{n−2r}x·y⟩ on DP^r(A) (Lefschetz classes modulo numerical equivalence) are positive definite for
    every abelian variety over F̄_p, unconditionally;
  - a specialization argument extends this to every algebraically closed field.
- **Remark t7 states:** "the Hodge standard conjecture holds unconditionally for abelian varieties with no exotic
  algebraic classes."
- *Why it covers our case:* by (a), E^N has no exotic algebraic classes. The proof lifts the polarized abelian variety to
  CM type (Zink) with its polarization, so any polarization is allowed, including the product polarizations ρh₁ + σh₂.
- *Inside the 2002 paper this is a remark with a sketched proof*, resting on Milne 1999a (Duke) and Milne 1999b
  (Lefschetz motives). It is the refereed, published input the run names. **This replaces 032-Cor8.4 for every use the
  chain makes.**
- **Not needed:**
  - Clozel 1999 (numerical = homological on abelian varieties over finite fields, for a positive-density set of ℓ). It
    is weaker than what (b) gives here, since H1 needs every ℓ ≠ p, and the Lefschetz-class statement gives that.
  - Kahn 2003.
  - Ancona 2021's theorem on abelian fourfolds: A30a uses only Ancona's signature argument (Prop. 3.15), which is a
    linear-algebra count, applied to B with A30's numerical = homological.

**(c) Chin's Theorem 5.7, second reading.** I opened the arXiv source of the journal version, math/0206147.
- *Locator checked:* Theorem 5.7 is `thm:Serre max torus` (§5 Frobenius tori; numbered items 5.1–5.8, so 5.5 is Serre's
  finiteness theorem, 5.7 the maximal-torus theorem and 5.8 the corollary). Prop. 4.5 is `prop:algsheaf`. The run's
  locators are right.
- *Hypotheses of Th. 5.7:* X irreducible, normal, of finite type over a finite field; 𝓛 a semisimple lisse Λ-sheaf, Λ
  ℓ-adic, ℓ ≠ p; a number field E with an integer w, a real C ≥ 0 and an integer D > 0 such that 𝓛 is (1) E-rational,
  (2a) pure of weight w, (2b) plain of characteristic p, (2c) C-bounded in valuation, (2d) D-bounded in denominator.
  These are conditions on every Frobenius eigenvalue at every closed point.
- *Conclusion:* an open dense subset U of G_arith⁰, stable under G_arith-conjugation, such that Frob_x ∈ U forces the
  Zariski closure of ⟨Frob_x⟩ to be a maximal torus of G_arith⁰.
- **Each hypothesis as the run applies it (C44_POS.tex 27772–27830), checked by me:**
  - *X:* the smooth parameter curve: irreducible and normal.
  - *Semisimple:* G_geom ⊇ SO_d acting irreducibly in the standard representation (d = 3600t⁶ − 166 ≥ 3), so the
    arithmetic representation is irreducible. The run gets G_geom from A13 (SGA 7 XIX 3.4, Weil II 4.4.1).
  - *(1) E = Q:* the Frobenius polynomial on W is the middle polynomial divided by the ambient and K factors, all
    rational (Deligne).
  - *(2a) w = 0:* after the twist q^{−2} (Tate twists are allowed: Chin's Prop. 4.3).
  - *(2b) plain:* α and q⁴/α = ᾱ are algebraic integers, so α is a unit away from p, and so is λ = α/q².
  - *(2c) C = 2:* v(λ)/v(q) = v(α)/v(q) − 2 ∈ [−2, 2], since 0 ≤ v(α)/v(q) ≤ 4.
  - *(2d) D = b!, b = b₄(B), constant in the smooth family:* by Katz–Messing the ℓ-adic and crystalline polynomials
    agree; the slopes of a rank-b isocrystal have denominators ≤ b (Dieudonné–Manin); and v(α)/v(q) is a slope. This is
    Chin's own Lemma 3.3(2) argument.
- *Using the conclusion:*
  - G_arith⁰ = SO_d;
  - the compact ℓ-adic image is Zariski dense, so it meets U in a nonempty ℓ-adic open set;
  - Chebotarev, constant field handled through A12 (Entin), gives a dense set of closed points;
  - a maximal torus of SO_d has independent weights ±e_i, which gives (A30.3) and the A28 selector.

  No fault.

**(d) Ambient block, second reading** (A28, 27318–27382, the positive-spectrum comparison).
- *The setting:*
  - q = q_{T,r} is the primitive form on V_r ⊂ U ⊗ U on T = B × B;
  - q₁ = α*Q_A is the pull-back of the signed primitive forms of E^{12} along the injection α = (κ×κ)_*;
  - c = q⁻¹q₁.
- *The argument, checked:*
  - In the characteristic-0 lift both forms polarize the same Hodge structure, so c is self-adjoint and positive for the
    Hermitian form q(C·, ·̄), with positive real spectrum.
  - Both forms are given by algebraic correspondences (the Lefschetz inverses of (A28.7)), so c and c⁻¹ are rational
    polynomials in c, preserve the algebraic classes, and keep their characteristic polynomial under specialization.
  - q₁ is positive on algebraic classes of the special fibre, by (b) on E^{12}.
  - On the finite cyclic rational space spanned by z and its images under c, the operator c is q₁-self-adjoint with
    positive eigenvalues, so q(z, z) = q₁(c⁻¹z, z) > 0.
  - **The argument is complete.** The input it needs is exactly (b) for E^{12}.
- *The vanishing blocks:* W ⊗ U, U ⊗ W, W ⊗ K and K ⊗ W have no algebraic classes. In even degree the ambient
  eigenvalues are roots of unity, and the W eigenvalues are not. Correct.

**(e) A30a.**
- The signature count is right: N² = P_h² ⊥ hN¹ has signature (ρ₂ − ρ₁ + 1, ρ₁ − 1), independent of the polarization;
  subtracting LN¹ gives positivity on P_L².
- It uses A30's numerical = homological, and the Hodge index theorem for divisors in characteristic p (Segre and
  Grothendieck on surfaces, extended by a surface section). The latter is carried as classical background; I did not
  open a source.

## 3. Milne's report (hexagon:2611.00244, Thms 3.1 and 3.5)

Not needed, so not checked: no case H1 uses requires it. H1 should **not** cite it as an input. It may be cited as
context: under the 032 inputs it would give Tate and Hodge for all abelian ambients. That is the route to the general
form INT-C44-2 with nonsupersingular centres; it is not the H1 statement. Sun's Tate claim (arXiv 2611.28178) does not
enter.

## 4. For the write-up of H1 (H26)

- **Inputs:**
  - Tate 1966;
  - Milne 2002, Rem. 3.7–3.8 (arXiv labels t5, t7): supersingular E^N has no exotic classes;
  - Chin 2004, Th. 5.7, with the hypotheses as in §2(c);
  - Deligne, Weil I and II; SGA 7 XIX; Katz–Messing; Dieudonné–Manin;
  - Kleiman 1994, Prop. 5-1;
  - Entin 2021, Th. 3;
  - Ancona's signature argument (Prop. 3.15), for A30a.
- **State it as unconditional.**
- **Remove** any mention of 032 Cor. 8.3/8.4 or of Milne's report as an input of H1. Keep them only for the general form
  and for W02–W11.
- **The INDEX gate is met:** the second reading of Chin's hypotheses and of the ambient block. What remains are the
  literature search and the write-up. INDEX "Topicality" stays: Milne's report covers abelian varieties, not the axes.
