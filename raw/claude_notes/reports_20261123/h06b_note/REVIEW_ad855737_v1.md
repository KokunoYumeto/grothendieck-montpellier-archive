# Second reading of the H06b note, Sections 4-6, and the result of the literature gate

By ad855737 (Claude Opus 5.5 at effort high), 23 Nov 2026, for the main session 329fb1e6 (Claude Opus 5.5 at effort
max).

- **Text read:** `h06b_note.tex` (Fable editor a49aabbf, Claude Fable 5.2 at effort max), lines 46-130 (§§1-2) and
  176-1050 (§§3-7), every line of §§4-6.
- **Comparison:** a diff against the run's paper (`…checkpoint_13…/ihara/main.tex`) shows that §§3-6 are the run's
  text, except for the removal of the p = 2 sentences and one deleted word ("actual").
- **Sources opened for this reading:** Wake-Wang-Erickson 2017 (arXiv:1510.01661v4, §2.1, Prop. 2.2.6 with proof,
  Cor. 5.1.1-5.1.2), Wake-Wang-Erickson 2018 (arXiv:1505.05128v3, Cor. 2.1.3, Conj. 2.1.5, Cor. 8.1.3), Fukaya-Kato
  (author preprint 2012, §6.1.5, §§7.1.1-7.1.10), Sharifi 2002 (arXiv v2). Hashes are in
  `GATE_H06b_ad855737_20261123.md`.

## Usefulness first

**Yes. The result is new at irregular Vandiver primes, and it answers the question as Anderson and Ihara asked it.**
- The question (Anderson-Ihara 1988, p. 272, (a), as quoted by Ishii) is whether Ω_p* equals the maximal pro-p
  extension of Q(μ_p) unramified outside p. The note's Theorem 1 proves exactly that equality at every odd p with
  X_p^+ finite, so at every Vandiver prime and at every odd p < 2^31.
- The gate found it nowhere earlier:
  - Sharifi 2002, Thm 1, covers regular p only;
  - Sharifi, RIMS Kôkyûroku 2120 (2019), p. 222, writes that for irregular p it "is a very interesting open question
    of Anderson and Ihara";
  - Ishii (Jan. and Sept. 2026) records only the regular case;
  - Hexagon and the arXiv searches found nothing.
- The arithmetic input is in the literature: Vandiver ⇒ Sharifi's conjecture (WWE 2017), and Fukaya-Kato §7.1.10
  turns this into cup-product generation at every level. The bridge from that to the kernel field is new: Lemmas 4.1
  and 5.1 of the note.

## Verdict on Sections 4-6

**No mathematical error found.** Every step below was checked; the cited theorems were read at the source where marked.

**§4, the rational outer image.**
- Functoriality of rational completion, the density of the cyclotomic-kernel image (Hain-Matsumoto, Thm 8.4) and its
  identification with H were checked.
- So was the Levi normalization: γ s_m = u^m s_m, and Δ acting without a unipotent part because u^m − 1 is
  invertible in every positive weight.
- Correct.

**§4, Lemma 4.1 (finite-level cup comparison).** Checked line by line:
- N = ∧̂²U, with the quotient by brackets involving T; c = +1 on N; the plus part is the extension 0 → N → E → T → 0.
- C_e = q_e(γ)y ∈ N[1/p] is the odd-odd companion error.
- γ acts on the two-variable coordinates of N by (1+T_1)(1+T_2), so vanishing on D_α = 0 is divisibility by γ − α,
  by Weierstrass division after the integral change of variable S = D_α.
- w̃ = r_e(γ)y − A satisfies (γ − α)w̃ = C_e − C_e = 0, so E[1/p] splits over W.
- The cochain k(h) = −(p^b/2)f(h)g(h) − ψ(p^b z(h)) has dk = p^b f(h_1)g(h_2). This was recomputed from
  z(h_1h_2) = z_1 + z_2 + [x_1,x_2]/2: the two summands give (p^b/2)(f_1g_2 + f_2g_1) and (p^b/2)(f_1g_2 − f_2g_1).
- The residual cocycle on P_n is −ψ(p^b β_δ(t)), which vanishes on W.
- H²(P_n, O/p^n(2))^+ ≅ H¹(Γ_n, Hom(T, O/p^n)(2)), because H and Γ_n have cohomological dimension one and the U-part
  is odd.
- The c-even classes vanish on T and on the Γ_n-section.
- The finite coinvariant quotients restricted to W*(2), with γ = u²/α, form a separated system. A fixed p^b
  annihilating all of them contradicts the nonzero torsion-free quotient.
- Correct.

**§5, Lemma 5.1 (separation of Magnus coefficients).** Checked line by line:
- The compact free basis:
  - a torsion-free compact Z_p-module is a product of copies of Z_p;
  - the free pro-p group on a pointed convergent sequence has abelianization ∏ Z_p;
  - Frattini surjectivity and the section argument hold.
- The finite-rank Magnus injectivity, by killing tails.
- The odd coordinates have bounded denominators in each degree; the singleton kernels are evaluation at u^m − 1,
  rescaled by density.
- Even companion coordinates:
  - y_{e,j} has no odd-linear term and leading target length two;
  - B_{e,j} = z^j B_{e,0};
  - q_e(z)B_{e,0;m,n} = C_{e;a,b}(u^m − 1, u^n − 1). The length-two parts of products of even factors add, and E_e
    has zero abelian class, so its degree-two Magnus part is the pure odd alternating tensor C_e.
- The partial fractions in z = (1+T_1)(1+T_2).
- The pole extraction:
  - every denominator from a different root or position is a unit in K_0[[S]]; checked for overlapping neighbours,
    where the constant term α_j(1+T_{j+2})/(1+T_j) − α' is nonzero in independent base variables;
  - maximality kills patterns with an extra pair;
  - componentwise maximality kills dominated pole vectors;
  - wrong even characters have zero numerator for the chosen odd types;
  - the surviving coefficient is a product of nonzero factors in a field.
- The identity theorem on the Cartesian grid: there are finitely many excluded weights, and the residue-class
  sequences have interior accumulation points.
- Correct.

**§6, the arithmetic hypotheses under Greenberg (and so under Vandiver).**
- Lemma 6.1 (étale comparison): H¹(N, A)^P = 0 for the kernel N of the maximal pro-p quotient, and the five-term
  sequence; the passage to étale cohomology is carried from Milne LEC §14, not opened.
- The Δ-lift γ by the coprime complement theorem.
- H free: Ferrero-Washington with Iwasawa 1981, Thm 2 (run's locator); M finitely generated over Λ.
- R = Λ[1/p] is a PID: a one-dimensional noetherian UFD. ✓
- **Odd module, through WWE 2017 Prop. 2.2.6 (opened).**
  - The proof there gives Ext¹_Λ(𝔛^#_{χ^{-1}}(1), Λ) = X_θ and Ext² = 0 before any vanishing is assumed.
  - With θ = ω a^{-1} one has χ^{-1} = ωθ^{-1} = a. So M_a = 𝔛_a, and the hypotheses of their §2.1 at N = 1 (θ
    primitive, θ ≠ ω²) are exactly a ≠ ω, ω^{-1}.
  - Greenberg makes X_θ[1/p] = 0. Over the PID R, Ext¹(torsion, R) ≠ 0, so M_a[1/p] is free.
  - The rank is one by their exact sequence 0 → U → 𝔛 → X → 0 and Iwasawa's theorem (in their proof).
  - The excluded a = ω^{±1} are computed via Coleman's sequence: carried from Sharifi's notes, not opened.
  - ✓ as used.
- **Even module, through WWE 2018 (opened).** Conj. 2.1.5 states that X^+ finite implies X^- pseudocyclic, through
  Cor. 2.1.3; with Kummer duality (Sharifi's notes, carried) this gives T_e[1/p] cyclic. ✓
- **Symbol surjectivity, through WWE 2018 Cor. 8.1.3(2) (opened).**
  - The hypotheses are exactly the two localized conditions quoted in the note's (8). Both follow from Greenberg:
    X_θ is finite, and X_χ(1)[1/p] is cyclic by pseudocyclicity.
  - The conclusion is that ϖ: (H^-/IH^-)/(tor) → X_χ(1) is an isomorphism.
  - X^- is p-torsion-free (Ferrero-Washington, as FK §7.1.1 notes), so the original ϖ factors through the
    torsion-free quotient and is surjective. ✓
- **Fukaya-Kato (opened).**
  - §6.1.5: at N = 1 the excluded characters are exactly θ = 1, ω².
  - §7.1.9 identifies H²(Z[1/p, ζ_{p^r}], Z_p(2))/p^r with Cl(Q(ζ_{p^r}))/p^r ⊗ μ_{p^r}.
  - §7.1.10 uses only the surjectivity of ϖ (with the surjection S → H²) to give generation by the symbols
    {1 − ζ^u, 1 − ζ^v} at every r. ✓
  - The note's exclusion of θ = 1, ω² (X_{ω^{-1}} = X_ω = 0; surjective norm projections) and of components with
    unit characteristic series (finite and torsion-free, so zero) is correct.
- The finite levels P_n = Gal(Ω_p/F_{n+1}) are maximal pro-p quotients of π_1(Spec O_{F_{n+1}}[1/p]). ✓
- Reduction from p^{n+1} to p^n coefficients is surjective on H², since the cohomological dimension is 2. ✓
- No Brauer term. ✓
- Parity: for a p-unit v, v/c(v) is a unit (c fixes the unique prime above p) of absolute value one, hence a root
  of unity. So the minus p-units mod p^n are cyclic, their self-cups vanish (2 is a unit), and mixed cups are odd.
  So the plus part of H² is generated by cups of plus classes. ✓ The c-even Kummer classes are those of plus units. ✓
- Lemma 6.1 then gives (10). ✓
- The dual root u²/α and character ω^{2−e} match. ✓
- The kernel of ρ_p is cyclotomically trivial, so it lies in H, and ρ is injective on H. ✓
- **§7 (Vandiver, Lemma 7.1, persistence of p ∤ h up a totally ramified Z/p tower):** checked again, every step. ✓

## Faults and recommended corrections (none mathematical)

| Place | Fault | Correction |
|---|---|---|
| Abstract and the method note | "Claude Opus 5.5 at effort high checked the deduction from Vandiver's conjecture and, in earlier versions, the separation argument" | Now: "checked the present text of Sections 4-7 step by step, with Wake-Wang-Erickson and Fukaya-Kato read at the cited places" (23 Nov). |
| §1 Context | The evidence that the question was open is understated | Add Sharifi, *Soulé characters in the work of Ihara*, RIMS Kôkyûroku 2120 (2019), p. 222: for irregular p "a very interesting open question of Anderson and Ihara". |
| §1 Credit | It does not say that Vandiver ⇒ Sharifi's conjecture is Wake-Wang-Erickson's (2017, abstract and Cor. 5.1.2) | Add a sentence. The note uses WWE 2018 Cor. 8.1.3(2) under Greenberg, which is right for part (a); in part (b) WWE 2017 Cor. 5.1.2 suffices. |
| §6, eigenlift citation | "\cite[Lemma 2.1, pp. 3–4]{Sharifi2002}" | In arXiv v2 the averaging statement is **Lemma 4**, p. 3 (g(m) = lim g^{θ_m^i}, with (2)). Check the numbering in the cited 13-page author version; otherwise cite "Lemma 4 (arXiv:math/0104116v2)". |
| Bibliography, Sharifi 2002 | the venue | Proc. Sympos. Pure Math. 70 (2002), 275-284 is correct (journal reference on arXiv), and not J. reine angew. Math. 549. |
| §6 | Milne LEC §14 and Sharifi's Iwasawa notes (Prop. 3.4.7, Coleman sequence) | Locators not opened by me; carried. |

**Scope.** The note leaves out p = 2, so part (c) is right as "every odd prime below 2^31". The run's separate p = 2
theorem was checked by me in its K17 form on 21 Nov and is not part of this note.

## Check events

| statement | date | who | type | outcome |
|---|---|---|---|---|
| H06b gate: Anderson-Ihara at irregular Vandiver primes is not in the literature | 2026-11-23 | Claude Opus 5.5 at effort high, ad855737 | targeted proof check (literature) | not found: Sharifi 2002 (regular only), Sharifi 2011 (no mention), FK 2012, WWE 2017/2018 (arithmetic input only), Ishii 2026 ×2 (regular only), Sharifi 2019 RIMS ("open question"), Hexagon 2609-2611, arXiv searches |
| Note §4: rational outer image, Levi normalization | 2026-11-23 | same | targeted proof check | confirmed; Hain-Matsumoto and Brown carried |
| Note Lemma 4.1 (finite-level cup comparison) | 2026-11-23 | same | targeted proof check | confirmed every step; dk identity recomputed |
| Note Lemma 5.1 (separation of Magnus coefficients) | 2026-11-23 | same | targeted proof check | confirmed every step on the present text |
| Note Lemma 6.1 (étale comparison) | 2026-11-23 | same | targeted proof check | confirmed; Milne LEC §14 carried |
| Note §6: odd module free of rank one under Greenberg | 2026-11-23 | same | targeted proof check | confirmed against WWE 2017 Prop. 2.2.6 and proof (opened) |
| Note §6: even components cyclic after inverting p | 2026-11-23 | same | targeted proof check | confirmed against WWE 2018 Cor. 2.1.3, Conj. 2.1.5 (opened); Kummer duality carried |
| Note §6: finite-level symbol generation, eq. (10) | 2026-11-23 | same | targeted proof check | confirmed against WWE 2018 Cor. 8.1.3(2) and FK §§6.1.5, 7.1.9-7.1.10 (opened) |
| Note Lemma 7.1 and the Vandiver deduction | 2026-11-23 | same | used and rechecked in this run | confirmed (already checked 21 Nov and 23 Nov) |
| Note Theorem 1 (a)-(c) | 2026-11-23 | same | targeted proof check | confirmed given the cited theorems; no error found |
