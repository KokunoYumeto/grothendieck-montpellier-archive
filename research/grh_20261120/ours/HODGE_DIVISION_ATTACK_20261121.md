# The Hodge conjecture as one arithmetic quantity: the division bound, and an attack on it

By Claude Opus 5.5 at effort high (the agent that took in the Hodge line: HODGE_SIGN, HECKE_DIV, THETA3, GHOSTS,
SIGN_NEXT), 21 Nov 2026, for the main session (Claude Opus 5.5 at effort max), at the user's word: "If you've reduced
the Hodge conjecture to a single arithmetic quantity, go work on it." Work file:
`agent_notes\20261121_intake_HODGE_SIGN_NOTES.md`. Check events: `HODGE_DIVISION_ATTACK_20261121_CHECK_EVENTS.tsv`.
Scripts: `division_attack_scripts\` (beside this file).

**Status words.**
- **Proved here:** the full proof is in this file, and I checked it.
- **Cited, checked:** a statement of tonight's runs that an intake (mine, unless named) checked in full. It is cited by run
  and statement id.
- **Cited, statement level:** used with that status shown.
- **Input:** a theorem of the literature, or a 2026 claim, with its status: published; 032 (OpenAI, 6 Oct 2026, with a
  human proof by van Hoften–Sempliner, Hexagon 2610.00259, unrefereed); Markman (arXiv 2502.03415, preprint); Severn
  (Hexagon 2610.00387, unrefereed).

---

## 0. The answer in brief

1. **The quantity.** Fix a polarized family of complex abelian varieties f: A → S over a connected base and a flat
   rational Hodge class t. Let c_t(s) be the least max(N, deg Z⁺, deg Z⁻) over integral effective cycles with
   N·t_s = [Z⁺] − [Z⁻] (the "division bound"; ∞ if t_s is not algebraic). Then **t is algebraic on every fibre iff c_t is
   bounded on one Zariski-dense set**: a Hecke orbit, the CM points, or the reductions at infinitely many primes (R1–R3).
   A non-algebraic Hodge class is a ghost: finite complexity at every prime, tending to ∞ cofinitely (R3).
2. **For Weil classes the quantity does not depend on the class (Theorem W, new; any imaginary quadratic K and any
   dimension 2n).** The detector degree δ_W(s) is the least degree of an effective n-cycle with nonzero projection to
   the Weil plane. It satisfies δ_W ≤ c_t ≤ C·δ_W⁴, with C explicit in K, n, the denominator of t and its norm.
3. **J is not the quantity (Theorem E, new).** On the principal component of Weil fourfolds over Q(ω), δ_W ≤ 132,269,760
   everywhere (from Schoen's published construction, GHOSTS R12). But the splitting index J_W, the J of DEG_L B19 for the
   CM algebra K × K, is unbounded on CM points of that component. Graph detectors on CM points have degree at most C·J_W
   (Proposition G), and fixed-source transport has degree of order √J (DEG_L B19, B21). **So bounded division is won by
   target-dependent detectors, never by transport.**
4. **The exact obstruction for Weil classes (Proposition O, new).** Boundedness of δ_W on S is equivalent to **one
   irreducible family of n-cycles whose image dominates S**. So a construction must supply a source family of
   dimension ≥ n² = dim S.
   - Every cyclic-cover Prym family (Schoen's, ramified or not), and every Prym–Tyurin family of a Galois cover of a curve
     of genus ≥ 1, has image of dimension ≤ 3n. So they reach n ≤ 3 only (Propositions O, O′).
   - **For n ≥ 4 the source must be a Hurwitz family of P¹-covers with an irreducible representation of dimension
     ≥ (n² − 2n + 3)/2, or a non-curve source such as Markman's semiregular sheaves.** That is the next question, made
     exact.

---

## 1. The reduction, as theorems

**Setting.**
- S is a connected smooth complex variety of finite type.
- f: A → S is an abelian scheme of relative dimension g, with a relatively ample L and θ_s = c₁(L_s).
- t is a global section of R^{2p}f_*Q, of Hodge type (p,p) on every fibre. After a finite étale cover of S (SGA 1 XII
  5.1), any flat Hodge class extends to a global section.
- For an effective integral cycle Z of codimension p on A_s, deg Z := ∫ θ_s^{g−p} · cl(Z).
- **The division bound:** c_t(s) := min{ max(N, D) : N ≥ 1, Z^± effective integral, N·t_s = cl(Z⁺) − cl(Z⁻),
  deg Z^± ≤ D } ∈ N ∪ {∞}.

### R1 (the family equivalence). Proved here; it is HECKE_DIV R21 + P0 with GHOSTS B06, all checked.

**Statement.** For t ≠ 0:
(a) the loci S_C = {s : c_t(s) ≤ C} are Zariski closed;
(b) each multiplier is bounded by degree: N ≤ (deg Z⁺ + deg Z⁻)/(d!·√V·h), with d = g − p,
    V = ∫θ^g/g! and h = ‖t_s‖ (both constant);
(c) the following are equivalent:
  - (i) t_s is algebraic for all s;
  - (ii) t_s is algebraic for s outside a countable union of proper closed subsets;
  - (iii) c_t is bounded on S;
  - (iv) c_t is bounded on a Zariski-dense subset of S;
  - (v) for some D, deg Z^± ≤ D on a Zariski-dense subset, with N unrestricted.

**Proof.**
- **(a).** Replace L by a relatively very ample power; this multiplies degrees by a fixed factor.
  - For each D, the relative Chow variety of pairs of effective codimension-p cycles of degree ≤ D is projective over S,
    with finitely many connected components (Kollár, *Rational curves*, I.3.21).
  - On each component, the difference of the universal classes, minus N·t, is a flat section of the pulled-back local
    system. Classes specialize along curves through the component.
  - So its vanishing is constant on each component. The components where it vanishes are open, closed and proper over S,
    and their image is closed.
  - S_C is the finite union of these images over N ≤ C and degrees ≤ C.
- **(b).** Let β = *t_s, the Hodge star of the harmonic representative. By the Lefschetz decomposition of the flat class,
  β is again flat, and ∫ t ∪ β = h².
  - β is translation invariant, so its pointwise norm is h/√V and its comass is at most h/√V.
  - Wirtinger: vol(Z) = deg Z/d!. So |∫_Z β| ≤ (h/√V)·deg Z/d!.
  - Pair N·t = [Z⁺] − [Z⁻] with β: N·h² ≤ h(deg Z⁺ + deg Z⁻)/(d!√V).
- **(c).**
  - (i) ⇒ (iii): S = ∪_C S_C is a countable union of closed sets. A closed ball in the smooth locus is a Baire space, so
    some S_C has interior. By irreducibility, S_C = S.
  - (ii) ⇒ (iii): the same argument, with the countably many exceptional subsets added to the cover.
  - (iv) ⇒ (iii): S_C is closed and contains a dense set.
  - (v) ⇒ (iv): on each Chow component of degree ≤ D, at most one N satisfies the class equation. Two would give
    (N − N′)·t = 0. So the possible N form a finite set M_D, by (b) or by finiteness of the components.
  - The rest is immediate. ∎

### R2 (Hecke orbits and CM points). Proved here, from cited density and André–Oort; HECKE_DIV R22, R23, checked.

**Statement.** Let S be a connected Shimura variety of Hodge type with its universal family (neat level), and t a flat
Hodge class preserved by a connected rational group H acting transitively on the domain.
1. Every H(Q)-orbit (a tensor-compatible Hecke orbit) is analytically, hence Zariski, dense.
2. Hence t is algebraic everywhere ⟺ c_t is bounded on one Hecke orbit ⟺ c_t is bounded on the CM points.
3. If c_t is unbounded, then c_t(x_j) → ∞ along every strictly special-generic sequence of CM points.

**Proof.**
- Density: H(Q) is dense in H(R) (real approximation; Milne, *Introduction to Shimura varieties*, Th. 5.4).
- Rational Hodge isometries are induced by quasi-isogenies (Riemann). The CM points are dense.
- R1(iv) gives the equivalences.
- The dichotomy: if S_C ≠ S, André–Oort (Tsimerman 2018, Th. 1.3, for A_g) makes the CM points of S_C lie in a finite
  union of proper special subvarieties. ∎

**With 032 (input):** c_t(s) < ∞ at every CM point, because the Hodge conjecture holds for CM abelian varieties. So the
quantity Q(S,t) := sup over CM points of c_t is a supremum of finite numbers:

> **Hodge conjecture for (S,t) ⟺ Q(S,t) < ∞.**

Every Hodge class on an abelian variety lies on such an (S,t): the Mumford–Tate special subvariety through the point. So
**the Hodge conjecture for abelian varieties ⟺ Q(S,t) < ∞ for every special S of A_g and every flat Hodge class t on it.**

### R3 (primes, and ghosts). Cited, checked (GHOSTS B01–B06; HECKE_DIV P6), with the proof recalled.

**Statement.** Let X/U ⊂ Spec O_K be smooth projective and t an absolute Hodge class, fixed by Galois after a finite
extension (Deligne, *Hodge cycles*, Prop. 2.9). Let c(v) be the local division bound in a fixed prime-to-v realization.
1. If t is algebraic: c(v) = c_η outside finitely many v, and c(v) ≤ c_η everywhere.
2. If t is not algebraic: {v : c(v) ≤ C} is finite for every C.
3. Bounded integral numerator degrees at infinitely many v, with N unrestricted, force algebraicity.

**Proof.** Hilbert-scheme parameter spaces H_{N,D} are projective over U (FGA 221, 2.4 and 3.2). The class condition is
open and closed (SGA 4½ *Cycle* 2.3.8; SGA 4 XVI 2.2). Images are closed in the curve U, hence finite or all of U. ∎

**Ghosts.** By 032 Remark 8.5 (input), every Hodge class on an abelian variety over Q̄ is algebraic modulo every good
prime: c(v) < ∞ for all v. So **a non-algebraic Hodge class would be a ghost:** it passes the test at every single prime,
and its complexity escapes every bound cofinitely. There is no third behaviour.

### R4 = Theorem W (the detector reduction for Weil classes). New; proved here.

**Setting.** A is a complex abelian variety of dimension 2n with integral polarization θ. K is an imaginary quadratic
field, and O ⊂ K ∩ End(A) an order, acting with signature (n,n) on H^{1,0}, with Rosati involution inducing complex
conjugation on K.
- W = W_K(A) = ∧_K^{2n} H¹(A,Q) is the rational Weil plane, of type (n,n).
- Fix a ∈ O with a/ā not a root of unity. One exists in every order: a = m + b₀ with b₀ purely imaginary and m large
  (THETA3 C13).
- Put Nm = aā, and define:
  - f(t) = (t − a^{2n})(t − ā^{2n});
  - g(t) = ∏_{j=1}^{2n−1}(t − a^j ā^{2n−j});
  - R = Res(f, g);
  - integral u, v with uf + vg = R;
  - Σ_j c_j t^j = v(t)g(t), and κ = Σ_j |c_j|·Nm^{jn}.
- The **detector degree** δ_W(A) is the least deg_θ Y over integral n-dimensional subvarieties Y with e_W[Y] ≠ 0
  (∞ if there are none).

**Theorem W.** For every nonzero t ∈ W, with δ ≥ 1 such that δt is integral and T := (−1)^n ∫t² (> 0):

  δ_W(A) ≤ c_t(A) ≤ C_{n,a}(δ, T)·δ_W(A)⁴,  C_{n,a}(δ,T) = δ·Nm^{2n}·max( R⁴/(n!)⁴, 4√T·κ·R³/(n!)³ ).

[Sharp form (added 21 Nov 2026 after the intake of HODGE_DIVISION; the sharpening is the run's, HD-WQ, GPT-6 Astra
(ChatGPT Pro mode), confirmed and rederived in the intake): δ_W ≤ c_t ≤ C′·δ_W². On W, A = [a]^* satisfies
A + A^† = s := a^{2n} + ā^{2n} and A^†A = q² := Nm(a)^{2n}, so the Gram matrix is exactly d·[[1, s/2], [s/2, q²]] and only
the factor Hd (H = 4q² − s²) needs clearing, not det G ~ d². Then N ≤ δH(RD/n!)² and the degrees are ≤ 4δq√(HT)·κRD²/n!.
The statement above stays true; it is not sharp.]

**Proof.**
1. **The projector.** T_a := [a]^* acts on H^{2n}(A,C) = ⊕_j ∧^jV_a ⊗ ∧^{2n−j}V_ā by λ_j = a^j ā^{2n−j}.
   - V_a and V_ā are the eigenspaces of a on H¹, each of dimension 2n.
   - The Weil lines are j = 0 and j = 2n.
   - The λ_j are distinct, because a/ā is not a root of unity.
   - [a] is semisimple, so e_W := R⁻¹v(T_a)g(T_a) is 1 on the Weil lines (there f = 0, so vg = R) and 0 elsewhere (g = 0).
   - e_W is induced by an algebraic correspondence with integral numerator (vg)(T_a) = Σ c_j [a^j]^*.
2. **Orthogonality.** The Hodge metric on H¹ is ψ(x, Cy), with C the Weil operator.
   - Rosati gives ψ(ax, y) = ψ(x, āy), and [a] commutes with C.
   - So the Hodge adjoint of [a]^* is [ā]^*, on H¹ and hence on all exterior powers: T_a is normal.
   - Therefore e_W is an orthogonal projector, and ‖e_W x‖ ≤ ‖x‖.
3. **Norm from degree.** For an effective n-cycle Z of degree D: ‖[Z]‖ ≤ D/(n!·√V) ≤ D/n!.
   - Pair the harmonic representative with a unit harmonic β.
   - |∫_Z *β| ≤ comass(*β)·vol Z ≤ V^{−1/2}·D/n!, by translation invariance and Wirtinger.
   - V = ∫θ^{2n}/(2n)! is the product of the elementary divisors, so V ≥ 1.
4. **Two integral generators.** Let Y be a detector of degree D, and put y₁ := (vg)(T_a)[Y] = R·e_W[Y] ∈ H^{2n}(A,Z) ∩ W
   and y₂ := T_a y₁.
   - **Degrees:** deg([b]^*Z) = Nm(b)^n deg Z, because [b]^*θ = Nm(b)θ and deg[b] = Nm(b)^{2n}. So y₁ is the class of
     Σc_j[a^j]^*Y, with effective positive and negative parts of degree ≤ κD; y₂ has parts of degree ≤ Nm^n κD.
   - **Norms:** ‖y₁‖ ≤ R·D/n! =: m. T_a acts on W by a^{2n} and ā^{2n}, both of modulus Nm^n, so ‖y₂‖ = Nm^n‖y₁‖.
   - **Independence:** y₁ ≠ 0, and a^{2n} ∉ R (as a^{2n} ≠ ā^{2n}), so T_a has no rational eigenvector in W.
5. **Positivity (cote 44, Th. 4 in this case).** θ·W = 0: θ pairs V_a with V_ā, and ∧^{2n+1}V_a = 0. So W is primitive
   of type (n,n).
   - Hodge–Riemann on primitive middle (n,n) classes: *x = (−1)^n x.
   - So G := ((−1)^n ∫ y_i y_j) is an integral, positive definite Gram matrix, with 1 ≤ Δ := det G ≤ ‖y₁‖²‖y₂‖² (Hadamard).
6. **Cramer.** Put b_i = (−1)^n ∫ δt·y_i ∈ Z, with |b_i| ≤ δ√T‖y_i‖. Then Δδ·t = n₁y₁ + n₂y₂, with (n₁,n₂) = adj(G)b
   integral.
   - |n₁| ≤ 2δ√T‖y₁‖‖y₂‖² and |n₂| ≤ 2δ√T‖y₁‖²‖y₂‖.
   - The multiplier is N = Δδ ≤ δ·Nm^{2n}m⁴.
   - The degrees are at most κD(|n₁| + Nm^n|n₂|) ≤ 4δ√T·Nm^{2n}·κ·m³·D.
   - With m = RD/n! this is the upper bound.
7. **The lower bound.** If N·t = [Z⁺] − [Z⁻], then e_W[Z⁺] ≠ e_W[Z⁻]. So some integral component of Z^± is a detector,
   of degree ≤ c_t. ∎

**Computed constants** (`division_attack_scripts\weil_detector_constants.py`, exact arithmetic; the script also checks
that e_W is 1 or 0 on every eigenvalue):

| K, a | n | \|R\| | κ |
|---|---|---|---|
| Q(ω), a = 3+ω (Nm 7) | 2 | 25,729,836,300 = 2²3⁷5²7⁶ | 193,904,039,700 |
| Q(i), a = 2+i (Nm 5) | 2 | 1,936,000,000 = 2¹⁰5⁶11² | 4,637,600,000 |

The values for n = 3, 4 are in the script output. They are sufficient, not optimized. GHOSTS R10 gets the denominator 54 for
Q(ω), n = 2, with two operators: R = [ω]^* and S = [√−3]^*.

**Corollary W′.** Let S be a connected family of Weil-type 2n-folds (fixed K, O and polarization type), with the Weil
plane trivialized by a finite cover (finite monodromy; GHOSTS R13a for n = 2). Then the Weil classes are algebraic on
every fibre ⟺ δ_W is bounded on a Zariski-dense subset. The quantity is **class-independent:**
Q_W(S) := sup over CM points of δ_W.
*Proof:* Theorem W with R1(iv). For a flat t, δ and T are constant. ∎

---

## 2. The attack

### 2.1 Where the quantity is known to be finite

| Family | Bound on δ_W (hence on c_t) | Input and status |
|---|---|---|
| Weil fourfolds, K = Q(ω), principal (unimodular, U⊕U) component | **δ_W ≤ D₀ = 132,269,760 everywhere** (Theorem D below) | Schoen, Compositio 65 (1988) §3 and 114 (1998) p. 330: **published.** GHOSTS R10–R12, checked. D₀ recomputed by script |
| Weil fourfolds, K = Q(ω), every fixed polarization and determinant | δ_W ≤ D₆ = 57,854,793,024,000 (through a sixfold) | GHOSTS R20–R24, statement level. D₆ recomputed by script: 110,224,800 · 14,171,760/27 |
| Weil fourfolds, every K | finite (qualitative); explicit through HECKE_DIV M7–M10 | Markman (preprint) |
| Weil eightfolds, K = Q(ω), split | finite; explicit factorial bound | Severn (unrefereed); HECKE_DIV SQ1–SQ9, statement level |
| Points isogenous to E^{2n}, any n, K with h_K = 1 | δ_W ≤ C(n,K)·J_W (Proposition G) | proved here |
| Everything else (Weil classes for n ≥ 3 outside the cases above; non-Weil exceptional classes) | open | — |

**Theorem D (closedness for δ_W).** For a flat Weil family, the loci {s : δ_W(s) ≤ D} are closed. So GHOSTS R12's
detector, found on a dense set, gives δ_W ≤ D₀ on the whole principal component.
*Proof:* as R1(a). On each Chow component of n-cycles of degree ≤ D, the class e_W[Z] is a flat section, so its
(non)vanishing is constant. The union of the components with e_W ≠ 0 is open, closed and proper, and its image is closed. ∎

### 2.2 Graph detectors at the CM points isogenous to E^{2n} (Proposition G, new)

**Setting.**
- K has class number 1, and E = C/O_K.
- x₀ = E^n × E^n carries the balanced Weil action ι(a) = (a, ā) and the product principal polarization.
- A point s in its polarized Hecke orbit (in a fixed Weil family) is A_s = V_R/Λ_s, where:
  - V = K^{2n} = V₁ ⊕ V₂, with V_i the eigenspaces of the CM scalar action relative to ι (on V₁, ι(a) = a; on V₂,
    ι(a) = ā);
  - Λ_s is ι(O_K)-stable and ψ-unimodular.
- Put M_i = Λ_s ∩ V_i, and J_W(s) := [Λ_s : M₁ ⊕ M₂]. This is the core index of DEG_L B19 for the CM algebra K × K.

**Proposition G.**
(a) ψ(V₁, V₂) = 0.
(b) Each M_i is an O_K-lattice, so B_i := V_{i,R}/M_i ≅ E^n.
(c) For every O_K-linear isogeny φ: B₁ → B₂, the graph Γ_φ ⊂ B₁ × B₂ has e_W[Γ_φ] ≠ 0, and so does its image in A_s.
(d) δ_W(s) ≤ C(n,K)·J_W(s), with C(n,K) depending only on n and K through Hermite–Humbert reduction constants.

**Proof.**
- **(a).** For x ∈ V₁ and y ∈ V₂, the Rosati condition for ι gives ψ(ax, y) = ψ(ι(a)x, y) = ψ(x, ι(ā)y) = ψ(x, ay). The
  CM scalar Rosati gives ψ(ax, y) = ψ(x, āy). So ψ(x, (a − ā)y) = 0.
- **(b).** On V₁, ι(a) is the scalar a, and on V₂ it is the scalar ā. So ι-stability of Λ_s makes each M_i stable under
  the scalars O_K. As h_K = 1, each M_i is free.
- **(c).** On H¹ the a-eigenspace of ι^* is spanned by dz₁, …, dz_n (from B₁) and dw̄₁, …, dw̄_n (from B₂). The Weil form
  w = dz₁∧…∧dz_n∧dw̄₁∧…∧dw̄_n has type (n,n).
  - Pull it back along x ↦ (x, φx), with φ holomorphic linear of matrix Φ: it is det(Φ̄)·dz∧dz̄.
  - So ∫_{Γ_φ} w = det(Φ̄)·∫_{B₁} dz∧dz̄ ≠ 0, because φ is an isogeny.
  - The isogeny h: B₁ × B₂ → A_s (degree J_W) is ι-equivariant, and h_* is injective on rational cohomology. So
    h_*Γ_φ has nonzero Weil projection, and some reduced component of it is a detector.
- **(d).** deg_{θ_s} h(Γ_φ) ≤ deg_{h^*θ_s}(Γ_φ) = n!·Pf((ψ₁ + φ^*ψ₂)|M₁), with ψ_i = ψ|M_i.
  - In O_K-bases of M₁ and M₂, with positive definite hermitian Gram matrices H₁ and H₂, this is n!·c_K^n·det(H₁ + Φ^*H₂Φ),
    where c_K = √|d_K|/2.
  - Take Φ a permutation matrix in reduced bases (Humbert reduction: ∏_k (H_i)_kk ≤ γ(n,K)·det H_i). Hadamard gives
    det ≤ ∏_k (a_k + b_{π(k)}), with a, b the diagonals.
  - Since a_k, b_k ≥ μ_K > 0 (ψ is integral on M_i), ∏(a_k + b_{π(k)}) ≤ 2^n μ_K^{−n} ∏a_k ∏b_k ≤ 2^n μ_K^{−n} γ² det H₁ det H₂.
  - Finally, c_K^{2n} det H₁ det H₂ = Pf(ψ₁)Pf(ψ₂) = Pf(ψ|M₁⊕M₂) = J_W·Pf(ψ|Λ_s) = J_W. ∎

**Remark (lower bound for graphs before pushforward).** By Minkowski's determinant inequality,
det(H₁ + Φ^*H₂Φ) ≥ 2^n √(det H₁·det H₂)·|det Φ|. So deg_{h^*θ}Γ_φ ≥ 2^n n! √J_W. This is DEG_L B21's √J. After pushing
forward to A_s the degree can drop by up to deg(Γ_φ → h(Γ_φ)), so this is not a lower bound for detectors on A_s. That is
the point of 2.3.

### 2.3 J does not control the quantity (Theorem E, new)

**Lemma H (split-prime modification).** Let p split in K = Q(ω), and let Λ ⊂ V be a ψ-unimodular ι(O_K)-stable lattice
of signature (2,2). For each k ≥ 1 there is a lattice Λ_k with:
- Λ_k ⊗ Z_ℓ = Λ ⊗ Z_ℓ for ℓ ≠ p;
- Λ_k ψ-unimodular and ι(O_K)-stable;
- J_W(Λ_k) ≥ p^{2k}.

**Proof.**
- O_K ⊗ Z_p = Z_p × Z_p splits V_p = V_𝔭 ⊕ V_𝔭̄, two isotropic Q_p-spaces of dimension 4 paired perfectly by ψ.
  O_K ⊗ Z_p-stable lattices are M ⊕ M′ with M ⊂ V_𝔭 and M′ ⊂ V_𝔭̄. Unimodularity is M′ = M^∨.
- The CM decomposition gives V_𝔭 = V_{1,𝔭} ⊕ V_{2,𝔭}, with bases e₁, e₂ and f₁, f₂ adapted to Λ_𝔭 = Z_p⁴.
- V_𝔭 and V_𝔭̄ are ψ-isotropic: ψ(ax, y) = ψ(x, āy) with a_𝔭 ≠ ā_𝔭. The CM decomposition V = V₁ ⊕ V₂ commutes with ι,
  so V_𝔭 = V_{1,𝔭} ⊕ V_{2,𝔭}, each ≅ Q_p². Take bases e₁, e₂ and f₁, f₂ adapted to Λ_𝔭 = Z_p⁴; at x₀ = E²×E² the lattice
  is split.
- Let M_k = {(x, y) : x ∈ Z_p², y ∈ p^{−k}x + Z_p²}, in the e and f coordinates. It is spanned by e_i + p^{−k}f_i and f_i.
  - M_k ∩ V_{1,𝔭} = p^k(Z_p e₁ ⊕ Z_p e₂): y = 0 forces x ∈ p^kZ_p².
  - M_k ∩ V_{2,𝔭} = Z_p f₁ ⊕ Z_p f₂.
  - So [M_k : (M_k ∩ V₁) ⊕ (M_k ∩ V₂)] = [Z_p² : p^kZ_p²] = p^{2k}.
- Glue M_k ⊕ M_k^∨ at p with Λ elsewhere (lattices are determined by their localizations). This lattice is unimodular
  and ι-stable, and J_W ≥ p^{2k}. ∎

**Theorem E.** On the principal component S₀ of Weil fourfolds over Q(ω), with x₀ = E²×E² (GHOSTS R12: its lattice is
U⊕U):
- the points s_k := (V_R with the complex structure of x₀)/Λ_k lie in S₀;
- they satisfy J_W(s_k) → ∞, while δ_W(s_k) ≤ D₀ and c_t(s_k) ≤ 531441·δ·D₀⁴(1 + 4⌈√T⌉).

So the division bound is **not** controlled by J. Every fixed-source transport has degree of order √J (DEG_L B19, B21,
statement level), and the graph detectors of 2.2 have degree ≤ C·J_W. Neither is the minimal detector: the minimal one
is target-dependent (Schoen's Prym surfaces).

**Proof.**
- Λ_k is a unimodular Eisenstein hermitian lattice of signature (2,2), hence ≅ U⊕U. This is GHOSTS R12's classification:
  an isotropic primitive vector (Meyer), plus unimodularity, gives a hyperbolic splitting twice.
- So A_{s_k} is a principally polarized O_K-Weil fourfold of signature (2,2), a point of S₀ (after the finite level
  cover).
- Lemma H gives J_W(s_k) → ∞. Theorem D gives δ_W ≤ D₀. GHOSTS R11, checked, gives the c_t bound. ∎

### 2.4 The exact obstruction: dimension of the source family (Proposition O, new)

**Lemma Dom.** δ_W is bounded on a Zariski-dense subset of an irreducible Weil family S ⟺ there is an irreducible
variety Y with a proper family of effective n-cycles on A ×_S Y, of bounded degree and nonzero Weil projection, whose
map Y → S is dominant (hence surjective). In particular dim Y ≥ dim S = n². (dim S = n², the U(n,n) domain.)

*Proof.* (⇐) The image of Y is closed and dominant, so it is all of S. (⇒) The loci of Theorem D are closed. Finitely many
Chow components carry e_W ≠ 0, and their images cover a dense set. Since S is irreducible, one image is S. ∎

**Proposition O.** Let the detectors come from cyclic-cover constructions in Schoen's style:
- a cyclic d-cover C → X of a genus-g curve, with r branch points (d = 3 or 6 for Q(ω), d = 4 for Q(i));
- the (χ ⊕ χ̄)-isotypic part B of J(C), for a primitive character χ, of dimension 2n;
- any cycles functorially attached to (X, cover), on B or on a bounded isogeny quotient.

Then:
1. The family has dimension 3g − 3 + r = g + 2n − 1 ≤ 3n.
2. **So it can bound δ_W on the whole Weil family only if 3n ≥ n², that is n ≤ 3.**
   - n = 2: 6 ≥ 4, and Schoen's dominance holds (unramified, g = 3).
   - n = 3: 9 = 9, the borderline case. Only unramified covers with g = 4 can reach it: Schoen's 1998 sixfold Prym
     family, which GHOSTS R20–R24 use for compensation.
   - **n ≥ 4: impossible for every cyclic cover, ramified or not.**

*Proof.*
- Chevalley–Weil: mult_χ H^{1,0}(C) = (g − 1) + Σ_b ⟨−a_b⟩ and mult_χ̄ = (g − 1) + Σ_b ⟨a_b⟩. Here χ(γ_b) = e^{2πi·a_b} at
  the b-th branch point, and a_b ∉ Z, because χ is primitive and γ_b ≠ 1.
- Adding: dim B = 2(g − 1) + r = 2n. So r = 2(n − g + 1), g ≤ n + 1, and the moduli of (X, branch points, cover) have
  dimension 3g − 3 + r = g + 2n − 1 ≤ 3n.
- The cycles are functorial in this datum, and bounded isogenies are finite in number. So the image of the detector
  family in S has dimension ≤ 3n.
- Lemma Dom finishes. ∎

**Proposition O′ (every Galois cover of a base of genus ≥ 1; new, proved here).** Let C → X be a Galois G-cover with
g(X) = g ≥ 1, and ρ an irreducible representation of dimension m. Let B be the corresponding Prym–Tyurin abelian
variety: one copy of the (ρ ⊕ ρ̄)-isotypic part, with H^{1,0}(B) = Hom_G(ρ, H^{1,0}) ⊕ Hom_G(ρ̄, H^{1,0}).
- If dim B = 2n, any detector family functorial in the cover has image of dimension ≤ 3n in S.
- **So curve-cover sources over a base of genus ≥ 1 reach only n ≤ 3.**

*Proof.*
- Chevalley–Weil: m_ρ + m_ρ̄ = 2m(g − 1) + Σ_b (number of nontrivial eigenvalues of ρ(γ_b)) ≥ 2m(g − 1) + r′. Here r′ is
  the number of branch points with ρ(γ_b) ≠ 1.
- B is pulled back from C/ker ρ, so only those r′ branch points enter its moduli.
- For g ≥ 2: 3g − 3 + r′ ≤ (3/2)(2m(g − 1) + r′) ≤ (3/2)·2n. For g = 1: r′ ≤ 2n. ∎

**The one escape among curve-cover sources** is a base of genus 0. There m_ρ + m_ρ̄ ≥ r′ − 2m, and the moduli have
dimension r′ − 3 ≤ 2n + 2m − 3. **So G-covers of P¹ with an irreducible ρ of dimension m ≥ (n² − 2n + 3)/2 are not
excluded by dimension.** The source must be a Hurwitz space of P¹-covers with a large irreducible representation whose
isotypic part is of Weil type for K with signature (n,n). Severn's suppliers (cyclic covers, then Brauer induction to
non-abelian groups) are of this non-abelian kind.

**Corollary O″ (the genus-0 escape forces reflection groups; new, proved here).** In the genus-0 case, write c_b for the
number of eigenvalues ≠ 1 of ρ(γ_b). Suppose ρ ≇ ρ̄, B is of Weil type with signature (n,n), and the source family
dominates S. Then:
- (a) m = dim ρ ≥ (n² − 2n + 3)/2;
- (b) all but at most 2n + 2m − n² − 3 of the local monodromies ρ(γ_b) are **complex reflections** (c_b = 1);
- (c) so ρ(G) is generated by complex reflections, up to that bounded number of other generators. At the minimal
  m = ⌈(n² − 2n + 3)/2⌉ it is generated by reflections, up to at most one other element.

*Proof.*
- With g = 0, Chevalley–Weil gives 2n = dim B = Σ_b c_b − 2m, since ⟨θ⟩ + ⟨−θ⟩ = 1 for each nontrivial eigenvalue.
- Dominance needs r − 3 ≥ n², where r is the number of b with c_b ≥ 1.
- So 2n + 2m = Σc_b ≥ r ≥ n² + 3, which is (a). Also Σ_b (c_b − 1) = 2n + 2m − r ≤ 2n + 2m − n² − 3, which is (b).
- The γ_b generate G, because the cover of P¹ is connected. That gives (c). ∎

**A consistency check against the one known n = 4 case.** For n = 4 and K = Q(ω), (a) gives m ≥ 6. HECKE_DIV S2
reconstructed Severn's monodromy as a finite complex reflection group on K⁶, of order 39,191,040, with 756 roots. That
order and dimension are those of the Shephard–Todd group G₃₄ (Mitchell's group), a 6-dimensional reflection group over
Q(ω). The identification is by order and dimension, from memory. So the only known dominant source for n = 4 lies exactly
where Corollary O″ puts it, at the minimal dimension m = 6.

**The next attack, made concrete:** for each n ≥ 4 and K ∈ {Q(ω), Q(i)}, list the irreducible complex reflection groups
of dimension m ≥ (n² − 2n + 3)/2 with character field K. Shephard–Todd: the imprimitive G(d,e,m) with d ∈ {3,4,6}, and the
exceptional G₂₅, G₂₆, G₃₂ (Q(ω), dimensions 3, 3, 4), G₃₃, G₃₄ (dimensions 5, 6), G₂₉, G₃₁ (Q(i), dimensions 4, 4).
For each, compute by Chevalley–Weil the branch data that give an isotypic part of dimension 2n and signature (n,n).
- Above m = 6 only the imprimitive families G(d,e,m) remain. So **for n ≥ 5 (m ≥ 9) the source must have imprimitive
  reflection monodromy G(d,e,m)**, the monodromy of cyclic covers of covers (a wreath-product structure), or be
  non-curve (sheaves).
- That is the exact next test: whether G(3,1,m) or G(6,…,m) Hurwitz families give dominant Weil-type Prym–Tyurin
  families, with cycles of bounded degree, for n = 5.

**This is the next question, stated exactly:**

> *For n ≥ 4, find an irreducible family of dimension ≥ n² of pairs (Weil-type 2n-fold, effective n-cycle of bounded
> degree with nonzero Weil projection) that dominates the Weil family.*

Severn's mechanism for n = 4, K = Q(ω) (unrefereed) is suppliers, then Brauer transfer, then dominance proved by
boundary monodromy. It is the only candidate known to me. Markman's (n = 2, all K; sixfolds with discriminant −1) uses
semiregular secant sheaves, not cycles from a small family: a sheaf-theoretic source whose deformation space is the
whole family (DEG_L S-14). **For n ≥ 4 the S-14 route (one semiregular perfect complex at one fibre) is not subject to
Proposition O.** It is the next attack.

### 2.5 The Q(i) family and THETA3 C27

- For K = Q(i), n = 2, Schoen's construction uses an unramified cyclic 4-cover of a genus-3 curve (g_C = 9), and B is
  the (±i)-part of the Prym.
- An explicit D₀(Q(i)) follows from the same Bézout scheme as GHOSTS R12, once the polarization type of Θ|_B is fixed:
  - deg_{3Θ} W₄(C) = 3⁴·9!/5!;
  - deg_{3Θ} T₀ = 3⁴·4!·(product of the elementary divisors of Θ|_B); [superseded (21 Nov 2026, after the intake of
    HODGE_DIVISION, HD-G03, confirmed): this is a 4-dimensional degree and is wrong for T₀. The norm fibre T₀ is a finite
    union of translates of the 6-dimensional N, of type (1,1,1,1,4,4) (Lange–Ortega, arXiv 0805.1020, §4), degree
    8,398,080, as §5 (Q1-03) already uses.]
  - (1 − σ²)^*Θ ≤ 4Θ on B, since (1 − σ²)^†(1 − σ²) = 2(1 − σ²) has eigenvalues 0 and 4.
- The one missing number is the type of Θ|_B. Its kernel has order 2⁸ by complementarity with the pulled-back
  J(C/σ²). Whether it is (2,2,2,2) is the computation to finish. **Not claimed here.**
- THETA3 C25/C27 (statement level) is a different route: a nonzero quartic cup test on Hom_K⁰(Alb X, A) for a ball cover
  X of degree ≤ 43264. It would give an explicit detector on one non-CM Q(i) fourfold, a test of the theta machine. For
  the quantity Q_W it gives one point, not a bound on a dense set.

---

## 3. In the project's terms

- **Cote 16, the C, A, I route (scans 034–050; our numbering).**
  - c_t and δ_W are the quantitative, integral, uniform forms of Grothendieck's condition A ("algebraic elements map
    onto algebraic elements", scan 050, corrected in SIGN_NEXT SN-C03/C04).
  - Theorem W's step 5 is the index condition I on the Weil plane. His positivity (scan 049) is exactly what makes the
    Gram matrix of the two integral generators definite and the Cramer division finite.
  - The resultant projector e_W is his "algebraic inverse by Cayley–Hamilton" (scans 048–049, the letter dated 6.1.1966):
    an algebraic correspondence inverting T_a on a summand, with an explicit denominator R.
- **Cote 44.**
  - Th. 4 (the polarization of the primitive part): the Hodge–Riemann step of Theorem W is its case on the Weil plane.
  - Th. 5 (heights along a pencil) is not used. The vertical corrections (SIGN_NEXT SN-44, JAC1964 H9-T1) concern Abel–Jacobi
    images of homologically trivial cycles, not detectors.
- **Ghosts.** R3: a counterexample to the Hodge conjecture for abelian varieties is a ghost. It is algebraic modulo every
  prime, and its local division bound c(v) leaves every bounded set cofinitely. Theorem W turns c(v) into a local detector
  degree δ_W(v). In characteristic p the positivity of step 5 is the Hodge standard conjecture, known for abelian
  varieties under 032 (SIGN_NEXT SN-11).
- **Our ids.**
  - R1 = HECKE_DIV R21 + P0 + GHOSTS B06.
  - R2 = HECKE_DIV R22, R23.
  - R3 = GHOSTS B01–B06 + HECKE_DIV P6.
  - Theorem W generalizes GHOSTS R10–R11 and HECKE_DIV P1/P3 to all K and n.
  - Proposition G and Theorem E complement DEG_L B19/B21.
  - Proposition O names the gate after GHOSTS R12 and HECKE_DIV P4.

## 4. Open, and the next attack

1. **n ≥ 4 (Propositions O, O′):** a dominant source family of dimension ≥ n². By O′ it must be one of two kinds:
   - a Hurwitz family of G-covers of P¹ with an irreducible ρ of dimension ≥ (n² − 2n + 3)/2, whose Prym–Tyurin part is of
     Weil type for K with signature (n,n). The first test is the smallest G with a K-valued character of such a dimension
     and a signature computable by Chevalley–Weil;
   - the S-14 sheaf route (one weakly G-semiregular perfect complex at one fibre; DEG_L S-14, statement level; Perry's
     deformation theorem).
2. **n = 3:** decide dominance of Schoen's sixfold Prym family for every K and determinant (9 = 9 dimensions). Then
   extract D₆-type constants. This is the first open case reachable by Bézout.
3. **Q(i), n = 2:** finish the polarization type of the (±i)-Prym, and compute D₀(Q(i)) by the R12 scheme.
4. **Optimize Theorem W's constants** with the two-operator projector (GHOSTS P06 style) for each K. Optimization is not
   needed for the equivalence.
5. **Beyond Weil classes:** for a special S whose generic Hodge ring is not generated by divisors and Weil classes (e.g.
   Mumford–Tate groups of type III or IV), state the analogue of the Weil projector (the isotypic projector of the
   Lefschetz group's commutant) and of Theorem W. The proof of Theorem W uses only:
   - a rational semisimple algebraic operator isolating a rational Hodge summand W;
   - positivity on W (primitive, or Hodge–Riemann);
   - an operator generating W from one vector.

   For dim W > 2 it needs dim W generators. They come from the action of the endomorphism algebra on W if W is an
   irreducible module, and the bound becomes δ_W^{2 dim W}.

---

## 5. Target 1 carried out: Q(i), n = 2 (added 21 Nov, same agent)

**Setting.**
- X is a smooth projective curve of genus 3, and π: C → X an unramified cyclic 4-cover with generator σ, so g(C) = 9.
- C′ = C/⟨σ²⟩ is the intermediate étale double cover, of genus 5, and π₂: C → C′.
- In J(C), with its principal Θ:
  - B := Im(1 − σ²) = ker(1 + σ²)⁰, the (±i)-Prym, of dimension 4, with i := σ|_B;
  - its complement is B^⊥ = Im(1 + σ²) = π₂^*J(C′), of dimension 5;
  - N := ker(Nm_π)⁰ has dimension 6, with complement π^*J(X).

### Q1-01: the polarization type is (2,2,2,2); the kernel of order 2⁸ is B[2]. Proved here.

- For complementary abelian subvarieties of a principally polarized abelian variety, K(Θ|_B) = B ∩ B^⊥ = K(Θ|_{B^⊥})
  (Birkenhake–Lange, *Complex abelian varieties*, Cor. 12.1.5; from memory).
- For the étale double cover π₂: ker π₂^* = ⟨η⟩ ≅ Z/2, and (π₂^*)^*Θ_C ≡ 2Θ_{C′} (Mumford, *Prym varieties I*;
  Birkenhake–Lange §12.3; from memory).
- So the polarization L′ = Θ|_{B^⊥} on J(C′)/⟨η⟩ satisfies K(L′) = η^⊥/⟨η⟩ inside K(2Θ_{C′}) = J(C′)[2] ≅ (Z/2)^{10},
  with ⊥ for the Weil pairing.
- Hence K(Θ|_B) ≅ (Z/2)⁸. It is an exponent-2 subgroup of B of order 2⁸ = |B[2]|, so it equals B[2].
- **So Θ|_B has type (2,2,2,2), and Θ|_B = 2M with M a principal polarization on B.**
- No quotient step is needed. (The Q(ω) case, GHOSTS R12, has type (1,1,3,3) and needs a 9-isogeny.)
- **The Weil structure:** Z[i] acts through σ. The Rosati involution of Θ, hence of M, sends σ to σ⁻¹ = −σ on B, i.e. it
  is complex conjugation. The signature is (2,2), since Chevalley–Weil gives multiplicity g(X) − 1 = 2 for each of ±i.
- **Machine check** (`division_attack_scripts\qi_bezout.py`): |K(L′)| = 2^{10}/4 = 2⁸ = |B[2]|.

### Q1-02: the Prym hermitian lattice is even; the Pryms lie in the even component. Proved here.

Let h(x,y) = M(ix, y) + i·M(x, y) on Λ_B = H₁(B,Z). It is a unimodular hermitian Z[i]-lattice of signature (2,2).

1. **Λ_B = (1 − σ²)H₁(C,Z).**
   - p_B = (1 − σ²)/2 maps H₁(C) into ½Λ_B.
   - H₁(C)/(Λ_B ⊕ Λ_{B^⊥}) ≅ p_B(H₁)/Λ_B, of order |B ∩ B^⊥| = 2⁸ = [½Λ_B : Λ_B].
   - So p_B(H₁) = ½Λ_B.
2. **Evenness.** For x = (1 − σ²)y, put c_k := Θ(σ^k y, y). Because σ is a Θ-isometry of order 4, c₀ = c₂ = 0 and
   c₃ = −c₁. Expanding gives Θ(σx, x) = 4c₁, so h(x,x) = Θ(σx, x)/2 = 2c₁ ∈ 2Z.
3. **The consequence.** Over Z[i], Tr(Z[i]) = 2Z, so the parity of h(x,x) is an isometry invariant. **The unimodular
   signature-(2,2) moduli for Q(i) splits** into at least an even component (the Pryms) and an odd one (that of E_i⁴ with
   the balanced action and the product polarization: h(e₁,e₁) = 1).
   - Schoen's Prym family can bound δ_W only on the even component.
   - The odd component, which contains E_i⁴, needs another source, or a compensation step (GHOSTS R20–R24 style).
   - [Closed (21 Nov 2026, after the intake of HODGE_DIVISION, HD-G06, confirmed): the even lattice is U⊕U, the odd one
     I_{2,2}; S^*I_{1,1}S = 2U and S^*US = 2I_{1,1} with S = [[1,1],[1,−1]], so a degree-2⁴ isogeny carries the even type to
     the odd type, pulling the target polarization back to 2ξ. A detecting surface pushes forward with degree ≤ 4·D_Pr, so
     δ_W ≤ D_all = 4·914,248,581,120 = 3,656,994,324,480 on both components.]

### Q1-03: D₀(Q(i)) = 914,248,581,120 on the even component, given Schoen's S-a and S-b. Proved here modulo those.

**The construction.**
- T₀ := Nm_π⁻¹(K_X) ⊂ Pic⁴(C) is a finite union of translates of N.
- The Abel image of the preimage of |K_X| ≅ P² under the finite map Sym⁴C → Sym⁴X is exactly W₄(C) ∩ T₀.
- So every 2-dimensional component Z′ of that image is an irreducible component of W₄(C) ∩ T₀.
- Put φ := (1 − σ²): T₀ → (a translate of) B, and Z := φ(Z′).

**The degree.**
1. Embed Pic⁴(C) by 3Θ, which is very ample.
   - deg W₄(C) = 3⁴·9!/5! = 244,944, by the Poincaré formula [W₄] = Θ⁵/5!.
   - The type of Θ|_N is (1,1,1,1,4,4): K(Θ|_N) ≅ K(Θ|_{π^*J(X)}) = G^⊥/G ≅ (Z/4)⁴, with G = ker π^* ≅ Z/4 and
     (π^*)^*Θ = 4Θ_X. So each translate of N has degree 3⁶·6!·16 = 8,398,080.
   - Bézout for the components of an improper intersection (Fulton, Ex. 8.4.6): deg_Θ Z′ ≤ 244,944·8,398,080/9.
2. φ^†φ = (1 − σ²)² = 2(1 − σ²), with eigenvalue 4 on B and 0 elsewhere, and Θ|_B = 2M. So 2Θ − φ^*M is nef, and on a
   surface deg_M Z ≤ ∫_{Z′}(φ^*M)² ≤ 4·deg_Θ Z′.
3. **D₀(Q(i)) := 4·244,944·8,398,080/9 = 914,248,581,120** (exact; `qi_bezout.py`).

**Inputs, settled against Schoen 1988 as printed** (Compositio 65, 3–32; the Numdam PDF, read 21 Nov:
`recent_results_20261110\papers\hodge_sources_20261121\Schoen_1988_Hodge_classes_on_self-products_Compositio_65.pdf`).

- **S-a: settled by the 1988 text.**
  - **Theorem 2.0 (§2, pp. 11–12)** is stated for every m > 1. Its hypotheses: h even, and a simple (Z/m)^*-orbit, which
    is "automatically satisfied if r = 0 or 1". Its conclusion: the character subspace U ⊂ H^h(C^h) is generated by
    fundamental classes of algebraic cycles.
  - For our unramified Z/4-cover (r = 0, q = g(X) = 3), h = 2q − 2 + 2r = 4.
  - **The cycles (p. 12, the r = 0 construction):** P₀ = |K_X| ≅ P^{q−1} = P² ⊂ Sh X, and β₀⁻¹(P₀) ⊂ W₀ = G\C^h
    "consists of m irreducible components. These components will in essence be the sought after algebraic cycles".
  - **Corollary 3.1 (§3, p. 25)** is stated for every m > 2. B is the image of P = ∏_{0≠H≤Z/m} Σ_{t∈H}(Id − t). For
    m = 4, P = (4 − Σσ^t)(1 − σ²), whose image is the (±i)-Prym B of §5. Then **Weil's U′ ⊂ H^h(B,Q) is generated by
    fundamental classes of codimension-h/2 algebraic cycles.**
  - **The step to one detector (mine).**
    - U is nondegenerate for the cup pairing: it is a Q-structure stable under (Z/m)^*, closed under inverse characters.
    - U = Ξ^*P^*U′ (p. 25).
    - So for the Weil form w′ of B, some component Y_j of the preimage of |K_X| in C⁴ has ∫_{Y_j} Ξ^*P^*w′ ≠ 0.
    - On T₀, P = [4]∘φ + const, because Σσ^t is constant on the norm fibre. Since [4]^*w′ = 4⁴w′, we get
      ∫_{φ(Ξ(Y_j))} w′ ≠ 0. So Z := φ(Ξ(Y_j)) is a 2-dimensional detector, and Ξ(Y_j) is a component of W₄(C) ∩ T₀, as
      used above.
- **S-b: not in the 1988 text; proved here instead, modulo one lattice fact.** [Published by van Geemen 1996, *Theta
  functions and cycles on some abelian fourfolds*, Math. Z. 221 (1996) 617–632, Theorem 5.3(3), pp. 629-630; the proof in
  §5 is a second route. (Added 21 Nov 2026 after the intake of HODGE_DIVISION, HD-G02, with the main session's check of the
  locator against the GDZ scan, `recent_results_20261110\papers\hodge_sources_20261121\vanGeemen_1996_MathZ221_617-632_GDZ\`.)]
  - **What 1988 says.** p. 26 counts moduli and lists (h, m) = (4,4), our case, among the four pairs where the method
    "has a chance". The dimension condition is 6 = (3/2)h ≥ (φ(m)/2)(h/2)² = 4. **Theorem 3.2 (p. 26) proves only
    (4, 3), K = Q(μ₃).** The (4, 4) dominance is not proved in 1988.
  - **Proof of dominance here.**
    - At (X, η) with η of order 4, the cotangent space of the Weil moduli at B is H^{1,0}_χ ⊗ H^{1,0}_χ̄, of dimension
      2·2 = 4, with H^{1,0}_χ = H⁰(K_X ⊗ η) and H^{1,0}_χ̄ = H⁰(K_X ⊗ η⁻¹).
    - The codifferential of (X,η) ↦ (B,M) is multiplication μ into H⁰(2K_X), the cotangent space of M₃. This is the
      standard Prym-type identification, as in Schoen's (3.10)–(3.11) for m = 3 (pp. 28–30).
    - **μ is injective when |K_X + η| is base-point free**, by the base-point-free pencil trick: ker μ ≅ H⁰(−2η) = 0,
      since η² ≠ 0.
    - A base point p means h⁰(η⁻¹(p)) ≠ 0, i.e. η = O(p − q), so 4p ~ 4q. That gives a degree-4 map X → P¹ totally
      ramified at p and q (6 = 12 − 6 further simple ramifications, 8 branch points). Such curves form a locus of
      dimension ≤ 8 − 3 = 5 < 6 = dim M₃.
    - So for general X and every η of order 4, μ is injective, and the 6-dimensional family maps submersively onto an
      open subset of its 4-dimensional component.
  - **Q1-05: the even component is unique (proved here).** Every even unimodular hermitian Z[i]-lattice L of signature
    (2,2) is ≅ U_ev ⊕ U_ev, where U_ev = (Z[i]², [[0,1],[1,0]]).
    1. The underlying Z-form has rank 8 and is indefinite, so it is isotropic (Meyer). Take a primitive isotropic e.
    2. Unimodularity over the PID Z[i] gives f with h(e,f) = 1. Since h(f + ae, f + ae) = h(f,f) + Tr(a), with
       Tr(Z[i]) = 2Z and h(f,f) even, f can be made isotropic.
    3. ⟨e,f⟩ ≅ U_ev is unimodular, so it splits off orthogonally. The complement is even unimodular of signature (1,1),
       with det −1.
    4. A binary hermitian form is K-isotropic iff −det is a norm, and 1 is a norm. So step 2 applies again.
    - So the even moduli is Γ\D for one lattice, connected after level. With the dominance above, the Pryms are dense in
      it.
  - **The Addendum (1998) is not needed** for S-a or S-b as now settled. GHOSTS used its p. 330 for the polarization
    correction in the Z/3 case. Here the polarization is computed directly in Q1-01.

**The original statement of what Schoen had to provide** (kept for the record; superseded by the list above):

| Input | What it must provide | Where it should be |
|---|---|---|
| **S-a** (nonvanishing) | Some Z′ has ∫_{Z′} φ^*w ≠ 0 for the Weil form w of (B,M): the Z/4 analogue of the r = 0 construction GHOSTS R12 used for Z/3 | Schoen, Compositio 65 (1988), Th. 2.0 and pp. 12–13, if stated for every cyclic order, or else its Q(i) section |
| **S-b** (dominance) | The 6-dimensional family of (X, Z/4-cover) maps dominantly to the 4-dimensional even unimodular Q(i)-Weil moduli of signature (2,2) | the Q(i) analogue of the §3 cotangent calculation (pp. 24–30, read by GHOSTS only for Z/3); Addendum, Compositio 114 (1998), p. 330 |

If Schoen's Q(i) case uses another construction, S-a and S-b must be supplied for it, and D₀(Q(i)) recomputed. With S-a
and S-b, Theorem D gives δ_W ≤ D₀(Q(i)) on the whole even component. The Weil local system is trivialized by a cover of
degree ≤ 4, because the units of Z[i] are μ₄.

### Q1-04: C₄(Q(i)), the explicit extraction. Proved here.

1. **The projector.** e_W = (1 + R)(4 − S)/16, with R = [i]^* and S = [1+i]^*. On ∧^aV_σ ⊗ ∧^{4−a}V_σ̄:
   - R = (−1)^a;
   - S = −4·(−i)^{4−a}.

   So e_W = 1 for a = 0, 4 and 0 otherwise (checked by the script).
2. **One integral generator.** u := 16·e_W[Z] = [4Z + 4[i]^*Z] − [[1+i]^*Z + [i(1+i)]^*Z]. Both parts have degree ≤ 8D,
   and d := ∫u² ≤ (16·D/2)² = 64D².
3. **The second generator.** R and S are rational on W, so y₂ := Tu with T = [2+i]^*. On W_C, T has eigenvalues
   λ = (2+i)⁴ = −7 + 24i and λ̄, with |λ| = 25.
   - The Gram matrix is d·[[1, −7], [−7, 625]], with Δ = 576d².
   - The parts of Tu have degree ≤ 25·8D.
4. **Cramer.** Δδt = a·u + b·Tu, with |a| ≤ 800·δ√T·d^{3/2} and |b| ≤ 32·δ√T·d^{3/2}. Hence:
   - **N ≤ 2,359,296·δ·D⁴**;
   - **degrees ≤ 6,553,600·δ·√T·D⁴**.

   **C₄(Q(i)) = δ·D₀(Q(i))⁴·max(2,359,296, 6,553,600·√T)**, with D₀(Q(i))⁴ ≈ 6.99·10⁴⁷.

**Status.** Q1-01, Q1-02 and Q1-04 are proved. Q1-03 is proved given S-a and S-b; **the gate is reading Schoen 1988 (the
Q(i) case) and the 1998 Addendum.** The odd component needs its own source. [21 Nov 2026, after the intake of
HODGE_DIVISION: the odd component is reached by the degree-16 isogeny of HD-G06 (Q1-02 above), and S-b is van Geemen 1996,
Th. 5.3(3).]

**In the project's terms.** The evenness of the hermitian lattice is an integral invariant that a rational Hodge-theoretic
argument cannot see. It is the integral refinement the "(sur Z !)" of cote 16, scan 014 points to.
