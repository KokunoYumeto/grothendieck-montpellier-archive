# Source checks behind the outreach notes of 22 Nov 2026

By Claude Opus 5.5 at effort max (agent a447db23), 22 Nov 2026, for the outreach register
(`OUTREACH_REGISTER_20261122.md`). Each section records one check of a finding by a research run against the other
party's text. The run that found each point is named in its section. For each one I opened the paper (arXiv source or
the free published text), read the statement and the proof at the locator, and rechecked the counterexample. A check is
not a proof; it records what was read and what was found.

Proposed public path: `raw/results_register/outreach_checks/OUTREACH_CHECKS_a447db23_20261122.md` in
grothendieck-montpellier-archive.

## 1. Nagpal-Snowden, proof of Theorem 7.1(a) (RESEARCH_SA08_C3_D031, A-L14)

- **Source:** R. Nagpal, A. Snowden, *The module theory of divided power algebras*, arXiv:1606.03431v2 (LaTeX source
  `dp_revised.tex`). Published in Illinois J. Math. 61 (2017), 287-353; that text was not opened.
- **Theorem 7.1(a)** (`thm:selfinj`): over a field, if infinitely many π_n vanish, D is injective as a graded
  D-module.
- **The proof, first paragraph:** for a nonzero finitely generated homogeneous ideal I and a map φ: I[d] → D, φ extends
  to ψ: D[d] → D, and "Since the space uHom(D, D)_d is at most one-dimensional, it follows that ψ is unique."
- **The proof, second paragraph:** it uses this uniqueness for φ restricted to I_1, assuming only that I_1 ≠ 0.
- **Check.** Uniqueness fails when φ = 0 and the spanning map of uHom(D, D)_d kills I.
  - Example: D = Γ_{F_p}(T) and I = (T). The zero map I⟨p−1⟩ → D has two extensions, 1 ↦ 0 and 1 ↦ T^{[p−1]}, because
    T·T^{[p−1]} = pT^{[p]} = 0.
  - For φ ≠ 0, uniqueness holds: the space is one-dimensional and the restriction is nonzero.
  - So the second paragraph needs I_1 chosen with φ restricted to I_1 nonzero, which is possible whenever φ ≠ 0; for
    φ = 0, take ψ = 0.
  - The theorem is unaffected.

## 2. Asvin G., Lemma 11 (AN_GRH, the A51 supplement)

- **Sources:** Asvin G., *On the variation of the Frobenius in a non abelian Iwasawa tower*:
  - Algebra & Number Theory 17 (2023), 2151-2179 (published PDF at msp.org, p. 9);
  - arXiv:2203.16774v5, the accepted version (label `lem: direct factor`).
- **Lemma 11:** "For a finite extension of curves f: X → Y, H^1_ét(Ȳ, Z_ℓ) is a direct factor of H^1_ét(X̄, Z_ℓ)."
- **The proof:** f_* f^* = deg f on Jac(Y), so f_* is surjective, "which in turn implies that the map on Tate modules
  T_ℓ(f): T_ℓ(X) → T_ℓ(Y) is surjective."
- **Check.** That inference fails for isogenies of degree divisible by ℓ. For f = [ℓ]: E → E, both maps are
  multiplication by ℓ, with cokernel (Z/ℓ)^2.
- **Case B of Definition 8** (C_n the pullback of [ℓ^n]: A → A along f: C → A) is an étale (Z/ℓ^n)^{2d}-cover.
  - There the image of H^1(C̄) in H^1(C̄_n) is not saturated. M_n = H^1(C̄_n)/H^1(C̄), said to be free on p. 10
    (source lines 408 and 431; p. 2158 before Theorem 14 and Lemma 15 in the published numbering), has torsion.
  - Lemma 12 fails integrally in the unramified case too. In the five-term sequence of Hochschild-Serre,
    0 → H^1(G, Z_ℓ) = 0 → H^1(Ȳ) → H^1(X̄)^G → H^2(G, Z_ℓ) → H^2(Ȳ) ≅ Z_ℓ(−1), the last map is zero because its
    source is finite and its target torsion-free. So H^1(X̄)^G/H^1(Ȳ) ≅ H^2(G, Z_ℓ) ≅ Hom(G, Q_ℓ/Z_ℓ) ≠ 0.
  - The proof's degeneration step ("G is torsion and Z_ℓ is torsion free") kills H^1(G, Z_ℓ) but not H^2(G, Z_ℓ).
    For [ℓ]: E → E the invariants are all of H^1(E), and the image is ℓH^1(E).
- **Where the lemmas hold.** Both hold after ⊗Q_ℓ. Integrally they hold in Case A, which is totally ramified over
  f^{-1}{0, ∞}: there f^* is injective on Jacobians and T_ℓ(f_*) is onto.

## 3. Milne, report on the OpenAI preprints, §3.6 (GHOSTS C15)

- **Source:** J. S. Milne, *On the Hodge, Tate, and standard conjectures for abelian varieties*, Hexagon 2611.00244v1
  (the only version on 22 Nov 2026), p. 8, §3.6.
- **Printed:** "The Hodge standard conjecture says that the pairing P^r(A) × P^r(A) → Q, a, b ↦ a·b·ξ^{g−2r} is
  positive definite."
- **Check.** The sign (−1)^r is missing.
  - On A = E × E with ξ = θ_1 + θ_2, the class a = θ_1 − θ_2 satisfies a·ξ = θ_1^2 − θ_2^2 = 0, so it is primitive
    (g = 2, r = 1).
  - But a^2 = −2.
  - The positive form is (−1)^r a·b·ξ^{g−2r}.

## 4. Partsch 2013, Proposition 6.6, Theorem 6.7, Proposition 6.9 (RESEARCH_SA14_SA19, D4a and D4b)

- **Source:** H. Partsch, *Deformations of elliptic fiber bundles in positive characteristic*, Nagoya Math. J. 211
  (2013), 79-108 (free PDF on Cambridge Core).
  - Prop. 6.6, p. 102: "Let f: X → C be a Jacobian bielliptic surface over k. Then f extends to any deformation X of X
    over Λ ∈ Alg_W."
  - Theorem 6.7, p. 104: "Every deformation X of a bielliptic surface X induces a lifting of the elliptic fibration
    X → C = Alb(X)."
  - Prop. 6.9, p. 106: "every deformation X of X extends both elliptic fibrations."
  - The paper treats p = d = 2 (Prop. 6.1, and the table of Prop. 6.2).
- **The example.**
  - k = F̄_2. E_0 = F_0 is y^2 + xy = x^3 + 1, which has Δ = 1 and is ordinary. P = (0, 1) has order 2.
  - X_0 = (E_0 × F_0)/⟨(−1, t_P)⟩, Jacobian through the image of {0} × F_0.
  - A/k[ε] is the deformation of E_0 × F_0 with Serre-Tate matrix q = [[1, 1+ε], [1, 1]].
  - diag(−1, 1) lifts, because (1+ε)^{−1} = 1+ε. t_P lifts uniquely, since P is étale. The lift σ is a free
    involution.
  - Twice the product polarization lifts, because (1+ε)^2 = 1. So X = A/⟨σ⟩ is a smooth projective deformation of X_0.
- **Check (Katz, Serre-Tate local moduli, Thm 2.1(3), (4)).**
  - A lift of f_0 = (0, φ^∨): Y_0^∨ → A_0^∨ would need q_{A^∨}(e_F^∨, e_E) = q_B(x, 0) = 1.
  - But q_{A^∨}(e_F^∨, e_E) = q_A(e_E, e_F^∨) = 1+ε.
  - So no abelian subscheme of Pic^τ_{X/R} lifts Pic^var(X_0) = Y_0^∨. A lift X → C of the Albanese fibration would
    give one through f^* on Pic^0_{C/R}.
  - This contradicts the three statements for this X_0.
- **The trace step on p. 103.** A map that is zero on a connected subgroup and induces zero on the étale quotient need
  not vanish. Example: h: Z/2 → μ_2 over k[ε], h(1) = 1+ε, which is nonzero with zero special fibre.

## 5. Buss-Grigoriev-Impagliazzo-Pitassi, proof of Corollary 21 (NEG_NIGHT, NN-C021)

- **Source:** *Linear gaps between degrees for the polynomial calculus modulo distinct primes*, JCSS 62 (2001),
  267-289. The journal-final manuscript is at https://mathweb.ucsd.edu/~sbuss/ResearchWeb/lineargaps/journalfinal.pdf
  (pp. 7 and 19).
- **The definitions (p. 7).**
  - "P is (d1, d2)-reducible to Q" defines the y's by degree-d1 polynomials in the x's and derives Q(r(x)) from P(x)
    in degree d2.
  - Lemma 1: a degree-d3 refutation of Q gives a degree-max(d2, d3·d1) refutation of P.
  - Lemma 2: BTS_{n,p} is (1, pr)-reducible to TS_{n,p}.
- **Corollary 21 (p. 19).** Its proof reads: "By Lemma 2, BTS_{n,p} is (1, rp) reducible to TS_{n,p}, and by Theorem
  15, polynomial calculus refutations of TS_{n,p} require degree Ω(n) over F′. Thus, the same is true for proofs of
  BTS_{n,p} over F′."
- **Check.**
  - By Lemma 1, a reduction of BTS to TS carries lower bounds from BTS to TS, not from TS to BTS. Corollary 20 uses
    Lemmas 1 and 4 in the right direction.
  - The step needs TS reducible to BTS. That reduction holds: x_{e,i} = (1/p) Σ_j ω^{−ij} y_e^j, of degree p − 1,
    with each constraint local.
  - So Corollary 21 holds with δ divided by about p − 1.

## 6. Ekedahl-van der Geer, Examples 3.4 and 12.2 (RESEARCH_SA15, lem:ppav-nonordinary-strata-candidate)

- **Source:** T. Ekedahl, G. van der Geer, *Cycle classes of the E-O stratification on the moduli of abelian
  varieties*, arXiv:math/0412272v2 (LaTeX source `strata.tex`). Published in Progr. Math. 269 (2009), 567-636; that
  text was not opened.
- **Example 3.4.** Printed: "(equivalently, on G_g the operator V has rank g−1 and semi-simple rank g−f)".
  - The paper itself says, before Lemma 4.9: "The p-rank or semi-simple rank f".
  - The proof of that lemma concludes that "the semi-simple rank of V on E_g is f".
  - The Weyl element given in the example has f semi-simple indices.
  - So "g−f" should be "f".
- **Example 12.2.** Printed: "The four final strata ... lie étale of degree 1 over the p-rank 2 locus, the p-rank 1
  locus, the locus ... p-rank 0 and a-number 1, and the locus of superspecial surfaces."
  - The table in the same example gives π_*[U_{[3,4]}] = 1 + p. The text before it gives
    γ_2(w_∅) = p + 1, from the formula γ_g(w_∅) = Π_{i=1}^{g−1}(p^i + … + 1).
  - The table also gives π_*[U_{[1,2]}] = (p^4 − 1)λ_1λ_2, which is (p + 1) times the class (p − 1)(p^2 + 1)λ_1λ_2 of
    the superspecial locus.
  - So the ordinary and the superspecial final strata have degree p + 1. The two middle strata have degree 1,
    consistent with γ_2(u_1) = γ_2(u_0) = 1.

## 7. Caradot-Lin, Proposition 3.10 (RESEARCH_SA08 D-031; RESEARCH_SA08_C3_D031 B-001)

- **Source:** A. Caradot, Z. Lin, arXiv:2511.22614v4 (the current version, 20 Jun 2026; LaTeX source
  `HOMOTOPY_LIE_ALGEBRA.tex`).
- **Printed.**
  - §2.1: "We say that (M^*, d^*) is A-free if M^i is a free A-module for all i".
  - Prop. 3.10 and its proof: "As X^* is assumed to be free, there exists a lift ρ′: X^* → I′ such that ρ = π∘ρ′."
- **Check (with the intake's counterexample).**
  - R′ = k ⊕ E with E^{−2} = ku, E^{−1} = kv, du = v; R = k ⊕ kε with ε in degree −2. Both ideals are square-zero,
    with γ_n = 0 for n ≥ 2.
  - π(u) = ε, π(v) = 0 is surjective on the ideals.
  - Take X = kε and ρ = id. A chain lift would need ρ′(ε) = u and d(u) = v = 0.
  - Termwise freeness gives a graded lift, not a chain lift.
- **Reach.** The intake (a34c0444) found no other result of v4 that rests on Proposition 3.10.

## 8. Keller 2016, Lemma 2.17 (RESEARCH_SA05, rem:B-Keller-closure-error)

- **Source:** T. Keller, *On the Tate-Shafarevich group of Abelian schemes over higher dimensional bases over finite
  fields*, arXiv:1410.5293v2 (LaTeX source; Manuscripta Math. 150 (2016), 211-245).
- **Lemma 2.17 (label lemma:finiteMorphismOfRelativeCurves).** Printed: "Let π: C → X be a proper relative curve with X
  integral and let D be an irreducible Weil divisor in the generic fibre C of π. Let D̄ be the closure of D in C. Then
  π_{D̄}: D̄ → X is a finite morphism."
- **The proof's last step:** a non-finite fibre would be a whole fibre C_x, "But then D̄ would have more than one
  irreducible component".
- **Check (the run's counterexample).**
  - Take X = A^2 over a field, C = P^1 × X, and D the point [u:v] = [x:y] of the generic fibre.
  - Its closure uy − vx = 0 is the blow-up of A^2 at the origin. It is integral and contains the whole fibre P^1 over
    (0, 0), so it is not quasi-finite over X.
  - The lemma holds when dim X ≤ 1. There D̄ is irreducible of dimension dim X, so it cannot contain a fibre and still
    dominate X.
- **Uses.** The lemma is used in the proof of Corollary 2.18 (second claim) and in the proof of Theorem 4.27, for the
  degree of D̄. Over a regular base the fibre degree of O(D̄) is still constant, which is what the run's own proof uses.
  The norm argument of Corollary 2.18 was not rechecked.

## 9. Kerr-Yang, §4 (RESEARCH_SA05, lem:B-KY-degenerate): already corrected by the author

- Kerr-Li, *Two applications of the integral regulator*, Pacific J. Math. 306 (2020), 539-556 (arXiv:1809.04114,
  LaTeX source). It records, for r = 4: "there is an error in the computation of the boundary of the last component
  W_2: in fact, it is degenerate, and the cycle Z̃ is therefore not closed". It gives a corrected construction.
- The run's lemma extends the degeneracy to every weight m ≥ 4 by the same homogeneity (substitution) argument.
- **Verdict:** no note. The author has published the correction, and the extension is the same argument.

## 10. Bauer-Catanese-Grunewald, Theorem 0.1 (RESEARCH_SA07, Source-RootBCG2013): no note

- arXiv:1303.2248v1, Theorem 0.1 (label fundamentalgroup), repeated as Theorem 4.13. Printed: "If σ ∈ Gal(Q̄/Q) is not
  in the conjugacy class of c, then there exists a surface isogenous to a product X such that X and the Galois
  conjugate variety X^σ have non isomorphic fundamental groups."
- Read literally it includes σ = 1, for which it fails. The intended σ ≠ 1 is evident.
- **Verdict:** a slip with no mathematical consequence; no note.

## 11. Knudsen 1983, Corollary 3.9(b) (MPL_147_003-047 note N048; FOR_FABLE F19)

- **Source:** F. F. Knudsen, *The projectivity of the moduli space of stable curves, II: The stacks M_{g,n}*, Math.
  Scand. 52 (1983), 161-199. The free publisher scan at journals.msp.org (no text layer) was read by OCR, p. 190.
- **Printed:** "Corollary 3.9. a) The clutching morphism β is finite and unramified. b) When g_1 ≠ g_2 or n ≠ 0,
  β_{g_1,g_2,H,K} is a closed immersion." The proof ends "and this proves a); b) is clear."
- **Check.** Take g = 3, n = 0, g_1 = 1, g_2 = 2 and a stable chain E_1 ∪ E_2 ∪ E_3 of elliptic curves with E_1 ≇ E_3.
  - It has two preimages under β: M̄_{1,1} × M̄_{2,1} → M̄_3. Cutting at E_1 ∩ E_2 gives (E_1, (E_2 ∪ E_3, p));
    cutting at E_2 ∩ E_3 gives (E_3, (E_1 ∪ E_2, q)).
  - So β is not injective on points and not a closed immersion. Part (a) is unaffected.
- **Context.** Grothendieck's own margin on cote 147, scan 030, reads "une imm. locale, mais pas une immersion". The
  statement (b) is repeated as printed in the literature, for example in the survey arXiv:1806.04654 ("a closed
  immersion if i ≠ g − i ... [Knu83, Corollary 3.9]").
- The paper prints only a postal address (Matematisk Institutt, Universitetet i Trondheim, N.T.H.).

## 12. Hoshi-Tsujimura, RIMS-1950 (2021), Proposition 1.4(ii) and Theorem A(iii) (SECTION_GHOSTS P.3)

- **Source:** Y. Hoshi, S. Tsujimura, *Construction of abundant explicit nongeometric pro-p Galois sections of
  punctured projective lines*, RIMS preprint 1950 (June 2021), PDF from kurims.kyoto-u.ac.jp, pp. 2-3 and 5-6.
- **Setting.** X is the complement of {a_1, ..., a_n} in A^1. The map X(K) → K \ {a_1, ..., a_n} is t_X, and the
  embedding X ↪ J = G_m^n sends a ↦ (a_i − a)_i. "Geometric" is Hoshi's Definition 1.1(iii): contained in a
  decomposition group of a rational point of the smooth compactification, the point ∞ included.
- **Prop. 1.4(ii).** It proves (1) ⇔ (2) ⇒ (3) ⇔ "(2) or (4)". Here:
  - (2) asks for a with (a_i − a)/x_i p-divisible for all i;
  - (4) asks for i_0 with (a_i − a_{i_0})/x_i p-divisible for all i ≠ i_0.
- **Check.** The implication (3) ⇒ "(2) or (4)" omits the sections at ∞.
  - Near ∞, every coordinate a_i − t equals −t times a unit congruent to 1, so the tangential sections at ∞ map to
    (c, …, c) for every c in (K^×)^(p).
  - Take p = 3, F = Q(μ_3), n = 2, (a_1, a_2) = (0, 1) and (x_1, x_2) = (3, 3). The 3-divisible elements of F^× are ±1.
  - (2) needs a ∈ {±3} ∩ {1 ∓ 3} = ∅, and (4) needs 1/3 = ±1 or −1/3 = ±1. So (2) and (4) fail, while the tangential
    section at ∞ gives (3).
  - The same pair satisfies the hypotheses of Theorem A, the conditions of (ii) and (iii) included: 1 = ±3 ± 3 has no
    solution, and 3 is not a root of unity. Yet the class of (3, 3) in GalSect(J) is the image of a geometric section
    at ∞. So Theorem A(iii) needs the extra hypothesis that x_1/x_2 is not p-divisible. For odd p the sign at ∞ does
    not matter, since −1 is p-divisible. This is the run's corrected tripod statement.
- The run (GPT-6 Astra) records a script with the same example: tangent v = 1/3, pair (3, −3), equal to (3, 3) modulo
  ±1.

## 13. Mochizuki-Tsujimura, RIMS-1974 (June 2023), Theorem F(ii) (LM6_POINTS_AS_SECTIONS B.34)

- **Source:** S. Mochizuki, S. Tsujimura, *Resolution of nonsingularities, point-theoreticity, and metric-admissibility
  for p-adic hyperbolic curves*, RIMS preprint 1974 (June 2023), PDF from kurims.kyoto-u.ac.jp, pp. 7-8.
- **Theorem F(ii), as printed.**
  - Hypotheses: the restriction to H of the l-adic cyclotomic character has open image. Y and Z are "[not necessarily
    proper!] hyperbolic curves over K", and f: Y → Z is a dominant morphism. s_Y and s_Z are sections over H with s_Y
    mapped to s_Z by f.
  - Conclusion: "s_Y arises from an Ω^H-rational point ∈ Y(Ω^H) if and only if s_Z arises from an Ω^H-rational point
    ∈ Z(Ω^H)."
- **Check (the run's example).**
  - K = Q_5 and H = G_K, so H ∩ I_K = I_K surjects onto Z_l and the cyclotomic character has open image.
  - Y = P^1 \ {0, 1, ∞, 2}, Z = P^1 \ {0, 1, ∞}, and f is the inclusion.
  - Let s_Y be a tangential section at the cusp 2 of Y. It lands in the decomposition group of that cusp, which maps
    into the decomposition group D_2 ≅ G_K of the interior point 2 of Z. So f_*s_Y is the point section of 2 ∈ Z(K).
  - But s_Y, a cuspidal section, does not arise from a point of Y(Ω^H). So the "if" direction fails when a point of Z
    is a cusp of Y.
  - It holds for f finite (or with cusps counted as points). The run claims nothing against RNS Theorem A or the Isom
    theorems.
