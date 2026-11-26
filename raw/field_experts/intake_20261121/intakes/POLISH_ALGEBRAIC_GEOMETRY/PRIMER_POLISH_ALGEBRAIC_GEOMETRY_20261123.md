# Primer: the mathematics of POLISH_ALGEBRAIC_GEOMETRY (prompt 90) as of checkpoint 35 (A2 section updated 24 Nov ~11:50 UTC)

For the main session, to read after a compaction, before any discussion of this run. By Claude Opus 5.5 at effort high
(agent a018e2d2, field expert), 23 Nov 2026. The run is GPT-6 Astra (ChatGPT Pro mode), still running (checkpoint 20,
16:00 UTC).

All locators refer to
`grothendieck_archive_transcription_20261110/research_returns/POLISH_ALGEBRAIC_GEOMETRY_checkpoint_35_20261124T0416Z_unzipped/workbench/papers/paper_0N/`.

The labels "confirmed" and "statement only" record **my** check events only, from the cp12 and cp20 intakes. Everything
else is the run's claim with the run's own checks. This primer restates; it develops nothing new.

## Paper 1. Counterexamples to Grothendieck's cohomological-dimension conjectures (14 pp., unchanged since cp12)

**Source.** Cote 31, archive sheet 84 (PDF p. 85; the prompt's "31/85" is the PDF page): for an integral affine X with
ℓ invertible, cd_ℓ(X) ≤ cd_ℓ(k(X)), possibly after shrinking, with a residual-characteristic affine-open bound.

**Thm 1.1 (arithmetic; `arithmetic.tex`). Confirmed.**
- **Statement.** There is an excellent Dedekind domain R, of characteristic 0 with 2 ∈ R^×, whose fraction field K is
  algebraic over Q, such that:
  - cd₂K = 1, while cd₂U = 2 for every nonempty open U;
  - Pic(U)/2 is infinite-dimensional;
  - no residue field is orderable.
- **Lemma (wreath).** G = (V⊕V)⋊⟨τ⟩ with Σ(x,y;ε) = x+y. Then:
  - ker Σ = A₀ ≅ 𝔽₂⊕V, with v·(b,u) = (b, u+bv);
  - 𝔽₂[V] ↠ A₀ by e_g ↦ (1,g);
  - Ver_{G,H}(x,y;ε) = (x+y, x+y);
  - (b,u;v)² = (0, bv; 0).
- **Lemma (one step).** Let F be totally imaginary, C_F = Pic(O_F[1/2])/2 ≅ Gal(M/F), where M is unramified and
  dyadically split, and let S be a finite set of primes containing the dyadic ones. There is a quadratic L/F that is
  inert at S, with C_F ↪ C_L and dim C_L ≥ 2 dim C_F. The mechanism:
  1. Chebotarev in a ray class field of M gives 𝔓 = (η).
  2. Adjoin the square roots of all V-conjugates of η: the Galois group is 𝔽₂[V]⋊V.
  3. Pass to the quotient G; then L = N^H.
  4. Inertia (1,σ) lies outside H, so N/L is unramified.
  5. Transfer is v ↦ (v,v), which gives injectivity and a surjection C_L ↠ V⊕V.
- **The tower.** Start at Q(√−35), with h = 2 and 2 inert. Take R as the union of the rings O_{F_n}[1/2], prescribing
  inertness at more and more primes.
- **Why the conclusions hold.**
  - Eventual inertness makes R Dedekind (finite splitting) and makes local degrees even, so Br(T)[2] = 0 for every
    finite T/K and cd₂K = 1.
  - Kummer theory and injective transitions give Pic/2 ↪ H²(U, μ₂) infinite.
  - SGA 4 X 4.4 gives cd₂U ≤ 2.
- **Credit.** Popescu 2022 §5 (eventual inertness tower).

**Thm 1.2 (wild; `wild.tex`). Confirmed at reading level.**
- **Statement.** A = W(𝔽̄₂)[[t]], U = Spec A[1/t]: then H³(U, 𝔽₂) ≠ 0 and cd₂U = 3.
- **Mechanism.**
  1. Excision gives H³_z(U) = H²(L), with L = Frac((A_(2))^h).
  2. Kato's filtration (Suzuki 2024, Props 6.1.2, 8.1.4, 8.2.1, 8.2.3) gives gr⁰ = E^×/E^{×2} and gr¹ = Ω¹_E,
     E = k((t)).
  3. Classes from V = Spec A[1/2t] have gr¹ in B·dt + k·dlog t.
  4. c = {1+2/t, t} has gr¹ class t⁻²dt, which lies outside that subspace.

**Thm 1.3. Known.** R¹f_*O = 0 for proper birational f, normal source, regular target: Ishii–Yoshida Cor. 1.4. Pic^τ
birational invariance: Li–Wang Cor. 4.6, with purity from Marrama Thm 6 (Moret-Bailly).

**Thm 1.4 (boundary; `boundary.tex`). Confirmed at reading level.**
- **Statement.** If the closed set Y has a quasi-projective neighbourhood in the normal proper X, then Q(X,Y) (π₁ of the
  complement modulo wild inertia) is topologically finitely generated.
- **Mechanism.** A Bertini curve section, with Abhyankar charts and Martinelli–Naranjo–Pirola connectedness, gives
  π₁^t(C°) ↠ Q. Raynaud's Chow lemma, with centre outside the neighbourhood, reduces to the projective case.

## Paper 2. Picard schemes, very ample surfaces and metabelian local groups (152 pp. at cp35; only this paper changed in substance since cp12)

**Thm 1.1 (G1). Confirmed.**
- **Statement.** Over Z[1/2], Pic^δ on the stack of abelian schemes polarized of type (d₁|…|d_g) has a universal
  section iff at most one dᵢ is odd.
- **Mechanism.**
  - Symmetric classes correspond to quadratic refinements of b = e₂(·, λ·) (Poonen–Rains Prop. 3.6).
  - Rank ≤ 2: q = 0 on the radical and 1 off it (Poonen–Rains 3.12(f); known).
  - Necessity: the transvections T_v(x) = x + E(x,v)v preserve E. Invariance forces q(v) = 1 for every v ≠ 0 in W, and
    two orthogonal v, w then give q(v+w) = 0, a contradiction.

**E4, schematicity of abelian torsors. Statement only.**
- **Thm 1.2.** For any S and h: A → B smooth proper with connected fibres, h_*T is a scheme if T is (Raynaud's
  criterion).
- **Cor. 1.3.** Pic_{T/S} is a separated scheme locally of finite presentation for schematic abelian torsors T.
- **Thm surface-torsor-modification.** A projective modification X → Q of an abelian-surface torsor algebraic space,
  with X proper, flat and finitely presented with geometrically integral fibres, forces Q to be a scheme.
- **Thm torsor-projective-bundle** (cp20: **every base**). P_Q(E) is a scheme iff Q is.

**Thm 1.6 (A3, Kodaira vanishing). Confirmed; posted as P90a, hexagon:2611.00936.**
- **Statement.** In characteristic 2 there is a smooth surface Y with L very ample, h⁰(L) = 562, h¹(L⁻¹) = 1 and
  h¹(O) = 565.
- **Mechanism.**
  1. Raynaud's surface S: a triple cover of P(E) over y² + y = x¹⁵, with g = 7.
  2. Q = O(2T) ⊗ f*N is globally generated, with h¹(Q⁻¹) = 1 and H¹(Q⁻ⁿ) = 0 for n ≥ 2.
  3. Q⁹ is very ample, with h⁰ = 210 + 186 + 160 = 556.
  4. Adjoin ninth roots of a general basis of H⁰(Q⁹).
- **P90a v2.** On Y, Pic_Y → Pic_H is not a closed immersion, which answers Kweon's Q7.7(ii) negatively (arXiv
  2008.01908v2, p. 19).

**Cor. smooth-torsor.** For Y a smooth ample curve, there is no G_s-torsor with smooth total space and smooth integral
inverse image of Y. Here G_s is the deformed group scheme with Δu = u⊗1 + 1⊗u + s·u⊗u. Statement only.

### The A2 line: Picard kernels on geometric points

**The setup.**
- X is a smooth projective surface in characteristic p, and Y is a smooth ample (or very ample) curve.
- M ≠ O has order p with M|_Y ≅ O_Y.
- N is the normalization of the μ_p-torsor of M.
- The question is Grothendieck's: is Pic(X) → Pic(Y) injective on points? It is also Kweon's Q7.7(i), for a hyperplane
  section.

1. **Conductor identity (Prop. normalized-mup-conductor, `picard_kernel_constraints.tex`).** dlog M has order pa along Y
   (a ≥ 1) with nonzero tangential leading coefficient, hence 2g(Y) − 2 ≥ apY². The conductor coefficient is a(p−1).
   In equality, N is a G_{s_a}-torsor; when a = 1, N has a singular point off D. Statement only.
2. **Euler formula (Cor. normalized-equality-euler, `equality_torsor_euler.tex`).** In equality,
   χ(O_N) = pχ(O_X) − p(p−1)a((p+1)a−3)Y²/12. Its source is a degree filtration of π_*O_N with graded pieces
   L^i ⊗ P^i. **Recomputed by me.**
3. **Smallest equality (a = 1).**
   - Ekedahl I.2.4(ii) makes N almost ruled, or else (p = 2) gives a K3 alternative.
   - For very ample Y the K3 alternative is excluded (Kadets 2.8 and a normal-bundle argument).
   - Every degree-p ruled cover equals N over k(X) (Prop. distinguished-ruled-cover).
   - Positive-genus ruling: the fibration X → C^(p) has rational-double-point singularities on N, separable
     multisections, the Albanese map an isomorphism, M ≠ 0 in NS[p], nontrivial on the generic fibre.
   - Rational ruling: canonical defect ε ≤ 1, which excludes p ≥ 5.

   Statement only.
4. **Prop. residual-adjoint (`canonical_subsystem_strictness.tex`). Confirmed.**
   - **Statement.**
     - Hypotheses: Y very ample, and ω ≠ 0 a closed 1-form vanishing on Y to exact order m.
     - Conclusion:
       - p | m;
       - A = K − (m−2)Y − Z is nef and big with A² > 0, where Z is the divisorial zero part of ω/s^m;
       - W = {d((u/s)ω) : u ∈ H⁰(O(Y))} has exact fixed divisor (m−2)Y + Z, kernel ks and surface image;
       - p_g ≥ h⁰(O(Y)) − 1.
   - **Mechanism.**
     - d((u/s)ω) = s^{m−2}·(t du − u dt)∧(ω/t^m).
     - On Y this restricts to the hyperplane embedding.
     - A curve image would make the generic fibre a P¹_F on which the adjoint has negative degree.
5. **Lemma negative-cotangent-adjoint. Confirmed.** A nonzero section of Ω¹(−aH−Z), with H very ample, makes
   K + (2−a)H − Z big. The Plücker coordinates of the tangent lines show that a curve image would force sections on
   lines.
6. **Thm strict-picard-all. Confirmed, given items 1–3.**
   - **Statement.** With Y very ample, 2g(Y) − 2 > pY², and K − (p−2)Y is big with surface canonical image.
   - **Mechanism.** In equality, item 4 with m = p and Z = 0 gives L² > 0 for L = K − (p−2)Y. Chern-number bounds on X
     then make L² ≤ 0 in each ruled case:
     - positive genus: L² ≤ 4(p−3)(g−1)/p − (p−2)d, combined with Riemann–Hurwitz for p ≥ 5;
     - rational, p = 3: L² ≤ 1 − d, or d = 2 against very ampleness;
     - rational, p = 2: the very-ample numerical obstruction.

7. **Thm conductor-equality-structure (cp24, `conductor_equality_structure.tex`). Confirmed** (the a = 4 step rests on
   Gu–Sun–Zhou, which I have not opened).
   - **Statement.**
     - Hypotheses: Y very ample and 2g(Y) − 2 = paY² exactly.
     - Conclusion:
       - a ≥ 5 and a ≠ 6;
       - K_X ∼ (pa−1)Y and K_N ∼ (a−1)π*Y, ample;
       - N is smooth, or (p = 2) has one A₁ point (ε = 1);
       - p | (Y² − ε);
       - the minimal resolution T is of general type, with K_T² = p(a−1)²d, c₂ = −pad + 2ε and
         12χ = pd(a²−3a+1) + 2ε;
       - the embedding is strange, hence not a complete intersection (Furukawa).
   - **Mechanism.**
     1. β = ω/s^{pa} has zeros only at finitely many points off Y. Its annihilator is F = H^m ⊗ ω⁻¹ ⊂ T_X.
     2. Pull back the Euler sequence along F → T_P. This gives 0 → O → E → B → 0, with B = K − (m−2)Y nef and big.
     3. A general determinant curve C = div(e₀∧e_s) is reduced and connected (Hodge index), so the coefficient
        λ ∈ H⁰(O_C) = k is constant. Hence E ≅ O ⊕ B, so A = K − (m−1)Y ≅ O.
     4. The splitting gives a constant vector v ∈ V* through which every tangent plane passes (strange).
     5. The radial μ_p action x₀∂/∂x₀ has quotient N^{(p)}, which is smooth by Seshadri. Closedness at v forces p = 2.
     6. Chern numbers, then: a = 1 (K ≡ 0 surfaces have c₂ ≥ 0), a = 2 (χ ≤ 0), a = 3 and a = 4 (Gu–Sun–Zhou
        K² ≤ 32χ and its genus-two Albanese clause against K = 3A).
     7. Projection from v gives p | (d − ε).
8. **Prop. conductor-six-excluded (`all_characteristic_a6.tex`). Confirmed** (the sources were not opened).
   - Shepherd-Barron's c₂ < 0 theorem gives an Albanese fibration with 5 | 2g − 2, so g ≥ 6.
   - Gu–Sun–Zhou give K²/χ ≤ 800/51, while ε = 0 gives 300/19.
   - ε = 1 gives d ≤ 8 against 12χ(O_X) = 109d + 1.
9. **Thm positive-square-picard (`positive_square_picard_strictness.tex`). Confirmed in full.**
   - **Statement.**
     - Hypotheses: X normal projective; Y smooth in the smooth locus with Y² > 0; M of order p, trivial on Y; m the
       exact order of dlog M.
     - Conclusion: p | m and 2g − 2 ≥ mY². At equality [M] ∉ p^{v_p(m)} NS(X). In particular algebraically trivial
       classes give strict inequality.
   - **Mechanism.**
     1. At equality the tangential coefficient is nowhere zero.
     2. If B = A^p: locally u = f^p + h^{pq}v. The normalization of z^p = u has coordinate t = (z−f)/h^q, with
        t^p = v, and is smooth near C′.
     3. The log form of π*A has order exactly q, because C′² = pC² > 0 rules out a conormal leading term.
     4. Iterating v_p(m) times reaches an order prime to p, which contradicts closedness. Pic⁰ is divisible.
10. **Statement only:**
    - Prop. odd-higher-conductor-equality: three Albanese fibre genera; a ≥ A_num(p) = 5, 7, 5, 9, 11 for
      p = 3, 5, 7, 11, 13, and (p−1)/2 for p ≥ 17.
    - `conductor_picard_descent`: M|_{aY} trivial and M|_{(a+1)Y} not; descent to the radial quotient needs p | a.

11. **Thm positive-excess-picard (cp35, `positive_square_picard_strictness.tex`; it supersedes item 9, which is now its
    corollary). Confirmed** for the induction and the NS lift; its three lemmas are at statement level.
    - **Statement.**
      - Hypotheses: X normal projective; Y smooth in the smooth locus with d = Y² > 0; M of order p, trivial on Y, of
        exact log order m; r = v_p(m); [M] ∈ p^r NS(X), which includes every algebraically trivial M.
      - Conclusion: δ = 2g(Y) − 2 − md ≥ 0 satisfies (Q_r − 1)δ ≥ md, where Q_r = ∏_{j=1}^{r}(1 + 2(p−1)m/p^j).
      - For r = 1: δ ≥ pd/(2(p−1)), and the inequality is strict for odd p (Thm odd-positive-excess-strict, statement
        level).
    - **Lemmas** (statement level):
      - resolution loss: a suitable resolution of a normal surface makes the curve smooth with
        D² − C_T² ≤ 4(p_a − g);
      - root genus: (p−1)δ = ℓ + 2Δ_D for D = π*C on the normalized torsor, with D² = pd;
      - resolved transfer: d_T ≥ pd − 2(p−1)δ, so δ_T ≤ (1 + 2(p−1)a)δ, with log order a = m/p.
    - **Mechanism.** Suppose M = P^{p^r}. Iterate the resolved transfer r times. If Q_r δ < G, every square stays
      positive. The final log order m/p^r is then prime to p, which closedness forbids. The NS step lifts the
      hypothesis using the divisibility of Pic⁰.
12. **Characteristic-2 boundary corollary.** Statement level.
    - Hypotheses: p = 2, m = 2a with a odd, [M] ∈ 2NS and δ = d.
    - Conclusion: T = ω_Y ⊗ N^{−(2a+1)} has exact order 2 (a = 1, and then dim Pic(Y)[2] ≥ 2) or is trivial
      (a ≥ 3). Hence Pic(Y)[2] = 0 implies δ > d.
13. **The smallest endpoint** (characteristic 2, m = 2, δ = d, algebraically trivial M, Albanese a surface of degree
    two). Statement level.
    - d = 4χ, 2d < K² < 3d, 1 ≤ c₂ ≤ d − 1.
    - The Stein factor is a normal Gorenstein double cover with 2t = d + ε, L² = 3d/2 + ε and 4c₂t ≥ d².
    - Very ample Y needs d ≥ 12. Further elliptic and inseparable-Albanese branch restrictions apply.
    - **Internal Cartier descent:** at a characteristic-2 internal centre, [M] ∉ 2NS.

**Open rows of the A2 line (cp35):**
- **Existence or exclusion of a nontrivial geometric Picard kernel:**
  - with positive excess below the bound of item 11 for classes outside p^r NS;
  - at or above the bound for classes inside it;
  - including the characteristic-2 smallest endpoint, where the run's research is concentrated.
- **Merely ample residual branches,** as before.
- **Kweon Q7.7(i)** remains open.

**Run checking state at cp35:**
- the 152-page PDF readings are at 0;
- the positive-excess theorem has a statement-only reconstruction (PASS);
- the endpoint results have reconstructions or exposed audits at their stated scopes.

**Own-work note:** hexagon:2611.00936 v1, Theorem 2, needs dim X > 0 for connectedness. It is fixed in p90a_note_v2.

### Local fundamental groups (Suzuki line; `local_groups.tex`). Statement only.

A is complete noetherian normal local of dimension 2 in characteristic p, with algebraically closed residue field and a
fixed SNC resolution X.
- **Thm 1.7.** dim H¹(U, M) ≤ C_X·rank M for every tame locally constant 𝔽_p-sheaf M.
- **Thm 1.8.** Swan conductors are at most t = (−B)⁻¹k. The kernel I of π₁(U)^ab → π₁(X)^ab is finite and killed by
  p^e·|det B|. The input is Kato's integrality theorem (Bright–Newton Thm 4.1).
- **Thm 1.9.** The maximal metabelian quotient of π₁(U) is topologically finitely generated (a part of SGA 2 XIII
  Conj. 3.1).
- **Open (F13):** uniform bounds for wild coefficients.

## Paper 3. The locally quasi-finite representability criterion and Murre's announced analogue (19 pp., unchanged)

The source is cote 131, sheets 13, 34 and 36, and Murre 1965, p. 247.

- **Thm 1.2 (counterexample). Confirmed except Prop. integral-descent.** The functor P(R) = {x ∈ R^h_(t) : x^p = 0} on
  𝔽_p[t]-algebras satisfies axioms 1–8 and (7_rel), but is not represented by a separated scheme.
  - Over D(t) it is terminal, since R^h = 0 there.
  - In F_p[t,ε]/(ε^p) the sections 0 and ε agree on the schematically dense D(t).
  - Its fpqc descent goes through strictly henselian bases.
- **Thm 1.3 (H). Statement only.** H(R) = {x : x^p = 0, x ∈ (tx)} satisfies the fixed-base axioms, but its modularity
  locus is {(t)}. This refutes our earlier SA17 Thm A:L1-general.
- **Thm 1.4 (relative openness), Thm 1.5 (criterion with (7_pro) over every locally noetherian base), Thm 1.6 (cote 128
  finite semilocal descent in every rank). Statement only.**

## Paper 4. Cohen lifting for adic algebras and Deligne's algebraic extensions (10 pp., unchanged)

- **Thm 1.1 (EGA 0_IV 19.3.12, withdrawn in Err_IV 8, restored). Confirmed.** Linear compactness is applied only to
  square-zero kernels; then a tower of closed powers.
- **Thm 1.2 (A16, nonlocal noetherian adic Cohen lifting). Confirmed for the algebra part.**
  - The cotangent complex reduces mod J^n to projective P_n (via Popescu and Neeman 2.12).
  - Ext^{>0}(L, N) = 0 by R lim.
  - The obstruction vanishes, giving a unique lift with automorphisms Der(B₀, I⊗B₀).
- **Thm 1.3 (transfinite triangular presentations). Statement only.**
- The three "EGA corrections" are known: the EGA III/2 errata, and Kleiman 1979.

## Paper 5. Grothendieck's Albanese equivalence and his conjectures on cycles (14 pp., unchanged)

**Thm 1.1 (E.3e, cote 14 sheets 37–38). Confirmed.**
- **Statement.**
  - Hypotheses: characteristic p > 0, Z an integral correspondence, u_Z = 0.
  - Conclusion: ^tZ_* : H^{2(n−i)+1}(X) → H¹(A) is zero with Q_ℓ and with Z_ℓ coefficients.
  - The integral premise is sharp: y² = x³ − x over 𝔽̄₅.
- **Mechanism.**
  1. Spread out the whole finite Albanese-kernel relation and specialize to 𝔽̄_p, where CH₀⁰ is torsion.
  2. Bloch's Theorem 4.2 kills the ℓ-part.
  3. The torsion cycle map vanishes.
  4. Take Tate modules.

**Thm 1.2 (universal range modulo algebraic equivalence over C), Thm 1.3 (s_J(A) | gcd(2, δ) for surfaces and
| gcd(6, δ) for threefolds). Statement only.**

## Paper 6 (gerbe of 𝔽_p): withdrawn

All its statements are Milne's (*Gerbes and Abelian Motives*).

## The correction dossier (CORRECTIONS_FOR_AUTHORS.md)

- **Checked by me at cp12:**
  - Stacks 07BV and 0BTP;
  - Popescu 2022 §4;
  - Milne, *Abelian Varieties* Rem. 8.5, and *Gerbes*, p. 23;
  - Achter–Casalaina-Martin §1.7.2;
  - Cotner–Zavyalov Ex. 3.4.6(ii);
  - Cossec–Dolgachev–Liedtke, p. 366;
  - Liedtke's table;
  - the ordinary Igusa surface (flatness of Pic^τ against Chai, Chai–Oort and Partsch; no gap found, independent
    re-proof missing).
- Email drafts: `EMAIL_DRAFTS_POLISH_ALGEBRAIC_GEOMETRY.md`.
- **New at cp20, not checked by me:** Catanese–Oguiso, Kleiman Rem. 5.8, Gu–Sun–Zhou, Shepherd-Barron, Stacks 0AGS,
  FGA 221 Lemma 3.5 (known), and two EGA-edition slips.
