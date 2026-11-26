# Primer: HODGE_DIVISION (prompt 46, with follow-up 46b): bounding the detector degree of Weil classes

By Claude Opus 5.5 at effort high (agent aaf694615cb43adc1, a copy of abcaba9b6ae84b747, author of the division attack
on which the run is built), 23 Nov 2026. The sources are the intakes in this folder (parts 1–3 of 21 Nov; checkpoint 34
of 22 Nov), with their check events, and `reports_20261122\paper_seeds\SEED_HODGE_DIVISION.md`.

**Two runs of prompt 46, GPT-6 Astra (ChatGPT Pro mode). They use different statements under the same ids:**
- **Run A:** began 21 Nov 10:38:55 UTC; newest read is `research_returns\HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped\`.
- **Run B:** began 21 Nov 10:36:29 UTC; received follow-up 46b; newest read is
  `research_returns\HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped\` (sections\*.tex).
- Their filings were mixed in run A's `_from_earlier_checkpoints`.

## Setting

- (A, θ) of dimension 2n with an imaginary quadratic K acting with signature (n,n) and Rosati compatibility.
- W = ∧_K^{2n}H¹ is the Weil plane, with projector e_W.
- δ_W is the least degree of an integral n-subvariety with e_W[Y] ≠ 0.
- For t ∈ W, with δt integral and T = (−1)^n∫t²: c_t = least max(N, deg Z⁺, deg Z⁻) with Nt = [Z⁺] − [Z⁻].

## 1. Quadratic extraction: one detector gives the plane

- **HD-WQ (run A, research/gaussian_fourfold.tex 268–334; my rederivation).** On W, A = [a]^* satisfies A + A^† = s and
  A^†A = q², with s = a^{2n} + ā^{2n} and q = Nm(a)^n. So the Gram matrix of (y₁, y₂ = Ay₁) is d·[[1, s/2], [s/2, q²]],
  and only H·d needs clearing (H = 4q² − s²). Then N ≤ δH(RD/n!)², and the degrees are ≤ 4δq√(HT)κRD²/n!.
- **HD-U (run A, research/uniform_division.tex 1–128; checked; projector recomputed for ten fields, n ≤ 6).**
  - Statement: c_t ≤ ⌈8·16^n/n!⌉·δ·⌈√T⌉·Nm(a)^{2n(n+1)}·δ_W². The constants are 1024, 5462, 21846 for n = 2, 3, 4.
  - The projector: ∏_{j=1}^n(S − α_j) = ±R·e_W, with S = [a]^* + [ā]^*, α_j = a^jā^{2n−j} + a^{2n−j}ā^j and
    α₀ − α_j = ā^{2n}(1 − r^j)(1 − r^{2n−j}) ≠ 0 for r = a/ā.
  - The mass κ = ∏(2q + |α_j|) ≤ (4q)^n.
  - The choice a = f(2 + √−m) works in every order.
- **HD-D01/D02 (run B, sections/extraction.tex 12–107; checked).** The same quadratic form; and for Q(i), n = 2,
  (1+[i]^*)(4−[1+i]^*) = 16e_W and A = [2+i]^* with eigenvalues −7 ± 24i, giving c_t ≤ 61,440·δ⌈√T⌉D².
- **Superseded later by HODGE_FINISH Paper A:** ⌈2·16^n/n!⌉ and Nm(a)^{n(2n+1)}, through clearing the lattice index.
- The general constant is not the best; the explicit Gaussian one (61,440) is the sharp case.

## 2. Small detectors on fourfolds

- **Q(i), even principal U², δ_W ≤ 48 (run B HD-Q03, sections/gaussian.tex 73–104; checked given van Geemen 1996).**
  - van Geemen (Math. Z. 221: Lemma 3.3, Prop. 3.6, Th. 3.7): six odd sections of |2Θ| map X to a smooth quadric in P⁵,
    and the strict inverse image of a general ruling plane Λ detects.
  - A P³ ⊃ Λ meets Q in Λ ∪ Λ′. Two divisors D₁, D₂ ∈ |2Θ| with no common component give C = D₁·D₂ of class 4θ²
    (e_W C = 0) and degree 96.
  - So C = Y + R with e_W R = −e_W Y, and one of the two has degree ≤ 48. Closedness carries this to the component.
- **Odd principal I_{2,2}, δ_W ≤ 192 (HD-Q04):** P = [[1,1],[1,−1]] with P^tUP = 2I_{1,1}, a degree-16 isogeny, and
  pullback factor 4. c_t ≤ 2,264,924,160·δ⌈√T⌉.
- **Q(ω) principal, δ_W ≤ 36; c_t ≤ max(3δ, 36⌊δ√(2T)/3⌋) ≤ 17δ⌈√T⌉; 3·W_Z algebraic** (run B HD-F1-S07,
  followup_fixed_surface.tex 475–600; HD-F1-T05, followup_exact_division.tex 1–202; checked given S05–S06).
  - Schoen 2007 smoothing surfaces S on J×J, through the degree-9 quotient q₀ = R ⊕ R with R = [[1,ζ],[1,ζ²]],
    R^†R = [[2,−1],[−1,2]] and N(det R) = 3.
  - [Z] = (3/2)θ² + w′ with ∫w′² = 18.
  - The integral Weil lattice has least norm 6 (my computation), so O·w′ = (1−ω)W_Z and u = (1−ω)w′ spans 3W_Z.
  - Γ = aZ₀ + (b−a)Z₁ − bZ₂ uses the three unit translates.
- **Earlier, superseded:** the Prym–Bézout route gave D_Pr = 914,248,581,120 (Q(i); HD-G01–G06 and attack §5), and
  Schoen's Prym gave 132,269,760 (Q(ω); GHOSTS R12).
  - Θ|_B = 2ξ, of type (2,2,2,2) with kernel B[2] (Mumford, Prym I §3);
  - the norm fibre is 6-dimensional, of type (1,1,1,1,4,4) (HD-G03);
  - dominance is van Geemen 1996 Th. 5.3(3), pp. 629–630, checked by the main session; the attack's S-b is a second
    route.

## 3. Stabilization (run A HD-COMP, research/general_compensation.tex 3–123; checked)

- **Statement.** If split Weil (2n+2)-folds over a class-number-one K have detectors of degree ≤ D_{n+1}(Δ), every Weil
  2n-fold over K, of any determinant, has δ_W ≤ (1 + Nm τ)·D_{n+1}(Δ²), with O_K = Z[τ].
- **Mechanism:**
  - take the product with B = E_K² (balanced action, λ = ϑ₁ + Δϑ₂, Hermitian determinant −Δ); the product is split, by
    the classification in Schoen 1998 §7;
  - contract with one of the four divisors (the axes, the graphs of 1 and τ), each ≤ c_K·λ in the nef order.
- **HD-COMP4:** applies this to fourfolds.
- **Superseded:** the factor max(1, Nm τ/Δ)/(n+1) (HODGE_BOUNDED_CYCLES, opposite graphs).

## 4. Higher dimensions (statement level for me unless noted)

- **Split Q(ω) eightfolds, D-G34-01..07 (run A, agents/g34_eightfolds/g34_section.tex 31–677):**
  - G₃₄ is identified: degrees 6, 12, 18, 24, 30, 42; order 39,191,040; 126 hyperplanes × 6 = 756 roots (checked by the
    main session);
  - rank-16 period differential; K-minor 1728 (reconstruction script rerun by me: PASS);
  - supplier repair, Brauer transfer;
  - D₈(Δ) = (4G⁸Δ)⁸B₀.
  - Severn's numbers are used only as a recomputed witness.
- **Sixfolds:**
  - Q(i) even, Q(i) odd, Q(ω) principal: 746,496, 5,971,968 and 30,375 (Schoen 1998 Lemma 13; Koike 2004 Th. 2.1);
  - Q(√−7) by G₂₄, Q(√−2) by the F₄ extension;
  - every Eisenstein determinant (HD-E6).
- **All nine class-number-one fields through Perry's preprint:**
  - run B HD-N07–N10: 10^258 d^69 f^33 Δ⁶ for split sixfolds; b_d 10^258 d^69 f^46 Δ^12 for every fourfold determinant;
  - run A's "2^324 d^57" has d = 4mL² with L = lcm(1..2^2048), so it is not comparable.
- **Gaussian class −3 sixfolds** (run B HD-R02/R03; later HODGE_FINISH Q24).
- **Imprimitive sources, n ≥ 5 (D-IM):** natural sources have period rank ≤ 15 < 25 at n = 5, so they do not dominate.
- **Graphs:** in matched products with core index J = p^{4k}, explicit graphs give δ_W ≤ 8 (run B HD-F1-S02).

## 5. Open rows at the end

| Row | Gate |
|---|---|
| Q2i (run A), T2-OTHER (run B): nonsplit sixfold determinants outside the covered classes | many exclusions of monodromy suppliers (D-TD, HD-ALT, HD-AST, D-SPW: a single Sp₄(3) residual); no new supplier. By stabilization it follows from split eightfolds |
| Q5i (run A), T5-EIGHTFOLD / RM-seed rows (run B): a semiregular seed on an auxiliary RM fourfold | finite-defect Ext exclusions; the bridge to a Weil eightfold (Q5au) is unproved |
| The main question | bounded detectors on split Weil families over K ≠ Q(ω) in dimension 8, and uniformly in n |

## 6. Where it went

- Seed `reports_20261122\paper_seeds\SEED_HODGE_DIVISION.md` → prompt 70 HODGE_BOUNDED_CYCLES → 70c HODGE_FINISH
  (Papers A and B).
- Hexagon register: H12, H19, H25.
- The attack file carries a "superseded in part" note since 23 Nov.
