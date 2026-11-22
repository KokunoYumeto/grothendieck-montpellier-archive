# Referee report: Δ on GT̂, the two gates

Referee: Claude Fable 5.2 at effort max, read in on this chunk only (agent a49aabbf5ed57bb8e). Date: 18 Nov 2026, 15:1x UTC. The work refereed is by GPT-6 Astra (ChatGPT Pro mode).
Method: every step read and re-derived by hand; no computer algebra. Papers opened are in `papers\` (list at the end).

## 1. Verdicts

| Gate | Verdict |
|---|---|
| Route 2 gate: SECTION_GHOSTS E.176–E.181 (relation (IV) for every element of GT̂; normalized elements lie in Λ) | **Proved.** I checked every step. Two citations need a supplied argument (§2.4 (a), §2.6 (b)); neither is a mathematical gap. |
| Route 1 gate: EXIT_TOWER E.44 (𝒥(A) = A through Boggi–Zalesskii Theorem A(i), (iii) for C₂², p = 2) | **Proved**, in the form "the standard action on R commutes with the cusp swap up to inner, hence the fixed-point equation of 𝒥 holds". The questioned closure-intersection step is not used. E.28 is not needed for that equation; E.28's own statement (𝒥 is an involutive automorphism of GT̂) I read only in part (§3.4). |

Not covered by these verdicts (budget spent on the gates): SECTION_GHOSTS E.182 (read once, no error found, not
re-derived), E.183–E.191 (statements of E.190 and E.191 read, proofs not checked); EXIT_TOWER E.37, E.49;
GT_TOWER_CHECK A.1, A.3, A.7. So this report certifies the two gates, not yet Δ|GT̂ = 0 itself.

The two routes are less independent than the register says. Both use the same ten-point Klein configuration in
Γ_{0,[10]}, the same two four-point forgettings and the same cusp swap. They differ in one input: route 1 cites
Boggi–Zalesskii Theorem A; route 2 proves the two needed statements itself (E.176). After the gate they differ again.

## 2. Route 2, step by step

Files: `...\SECTION_GHOSTS_final_20261118T1305Z_unzipped\SECTION_GHOSTS\sections\part_E_gt_geometric_repair.tex`
(E.176–E.179), `part_E_gt_coefficient_bridge.tex` (E.180), `part_E_gt_tower_repair.tex` (E.181, E.182).

### 2.1 E.176 (finite fixed-component recognition and fusion): correct
A Smith-theory argument at finite level, for H = C₂² acting on covers Y_i = X̃/U_i of an aspherical manifold X.
- E.176.5 (a finite-index subgroup killing H^{>0}(U; F₂)): the centre of W = F/(N′N²), N = F′F², maps trivially to
  F/N because the deck group C₂^r acts faithfully on H₁(N; F₂) (needs r ≥ 2: for v = e₁ take j = 2). The
  Lyndon–Hochschild–Serre step is right: row 1 dies because F₁ ⊂ F′F², row 0 dies through B₀, two filtration pieces,
  so two rounds. |W| = 2^{r+1+2^r(r−1)} is right.
- E.176.6–7: κ_m(P) is characteristic, of finite index, and inside U′; the vanishing passes to the smaller group.
- Tate step: for A = C₂, C*(Y, Y^A) is a bounded complex of coinduced modules (products of free orbits are still
  coinduced; Tate cohomology of a finite group commutes with products). The spectral sequence has d+2 rows, so d+2
  cohomologically-zero maps give zero on Tate hypercohomology, which is ⊕_q H̃^q(Y^A). Second stage for H/A on Y^A.
  After (d+2)² maps the map H̃^q(Y₀^H) → H̃^q(Y_V^H) is zero for every q ≥ −1.
- Degree −1 gives nonemptiness of Y₀^{ι(H)} (E.176.4); degree 0 of the pointed version gives that every fixed point
  of Y_V maps into the component of y₀ (E.176.2). The path arguments that follow are right: two lifts of the same
  label fixing the same point are equal, because deck transformations act freely.
- Literature used: Illman 1978 (equivariant triangulation of a smooth action of a finite group; X is not compact,
  which Illman's theorem allows). Not re-proved here.

### 2.2 E.177 (the ten-point Klein configuration): correct
- X = M_{0,10}(C) is aspherical of real dimension 14 with π₁ an iterated extension of free groups of ranks 2,…,8.
- X^H is two copies of P¹ ∖ {0, ∞, ±1, ±i}, exchanged by the C-flip; C_{S₁₀}(H) has order 32 (E.177.5).
- The second fixed-path subgroup is θHθ⁻¹ with θ a half twist on C₊, C₋; so the corrector lies in P ∪ Pθ and dies
  under both forgettings.
- E.177.3, C_Ĝ(H) = closure(N), follows from E.176.2 at every finite level. The compactness argument for one
  corrector in P̂ ∪ P̂θ is right (nested nonempty closed sets). The corrected automorphism preserves Ĝ and so C_Ĝ(H).

### 2.3 E.178 (two forgettings, one source): correct
- C⁺ = {e_A+e_B+e_C = 0} × H[D] preserves the base component Z; C⁺/H acts freely by z ↦ −z, 1/z; u = z² + z⁻²,
  Z/(C⁺/H) = P¹_u ∖ {∞, 2, −2}.
- First quartet {0, ∞, z, 1/z}: coordinate u. Second quartet {1, −1, z, −z}: r = (z−1)/(z+1), and
  r² + r⁻² = 2(u+6)/(u−2) = T(u). I recomputed this. T swaps the cusps ∞ and 2, fixes the cone point −2 and the base
  point u₀ = 6 (z₀ = 1+√2).
- The cusp types are right: at u = 2 the first quartet sees a half twist (D₁, D_b collide), the second a full twist
  (D₁ → B₊, D_a → B₋).
- S: v ↔ d represents T_*. I checked that Out(C₂ * Z) = {1, ι, t, S} and S is the only class that swaps the two cusp
  classes with orientation, so any other geometric marking changes S by an inner automorphism only.
- E.178.5–8 (closure(N^fix) = closure(N), descent to closure(N)/H): right.

### 2.4 E.179 (relation (IV) with the Schreier coefficient, for all of GT̂): correct
- φ(v) = v^λ, φ(d) = h⁻¹d^λh with h = f(v, d²) (E.179.4): follows from the standard action on B̂₃ with d = u, v = w²
  and antisymmetry. The projection (σ₁, σ₂, σ₃) ↦ (u, w, u) carries the four-point action to it, since
  w u² w = u⁻² in B₃/Z.
- E.179.5–7: ψ = SφS = Inn(g)φ gives g = d^t h and k d^t h = v^s with k = f(d, v²). C_R(d) = closure⟨d⟩ also follows
  from Herfort–Ribes (R = C₂ ⨿ Ẑ).
- E.179.8–10: K_std = F(v, d²) (index two, d v d⁻¹ = v⁻¹d⁻²); the Schreier basis (x², y, xyx⁻¹) goes to
  (Y, X², (X⁻¹Y⁻¹)²); [k] = (4c, 2c), [h] = 0; so s = 4c, t = −4c. Recomputed.
- E.179.11–12: the central exponent e = −2c from the character d ↦ 1, V ↦ 0, z ↦ 2. Recomputed.
- Result: f(u, w⁴) = w^{8c} f(u², w²) u^{4c} (uw)^{−6c} in B̂₃. This is exactly relation (IV) of Nakamura–Schneps
  (author version p. 3) with c in place of ρ₂.
- **(a) Citation to repair.** E.179 cites NS (1.1) for "the action commutes with labelled forgetting up to inner".
  NS (1.1) only gives the formula. The statement is true and short: for the stabilizer B_{n−1,1} of the last strand,
  deletion commutes strictly with (1.1), because F(σ_i) for i ≤ n−2 is the same word in B̂_{n−1}, and
  F(σ_{n−1}²) is a conjugate of σ_{n−1}^{2λ} by a pure braid, so it dies. For any other set of retained strands,
  conjugate by a braid b; F(b)b⁻¹ is pure, so the square commutes up to an inner automorphism by a pure element of
  the target. The proof should say this.

### 2.5 E.180 (c₂ = ρ₂ on all of GT̂): correct
- The symmetrizer g_F = β⁻¹ with α(s) = βsβ⁻¹ agrees with NS Definition 5.1 (g_F(y,x)⁻¹g_F(x,y) = f, g_F ≡ (xy)^{ρ₂}).
- E.180.11 (jφj⁻¹ = Ad(x^m)α on R_H) and E.180.14 (SφS = Ad(g)φ, g = d^{−4c}h): checked on generators.
- The character L (v ↦ 1, d ↦ −1) applied to the two conjugators of a: 4c + m − 2ρ = λ − m + 2ρ − 1, so c = ρ.
- NS prove ρ₂ = −A_F(−1,1) only on the subgroup defined by (III′) (Proposition 5.3). E.180 gets it on all of GT̂ from
  E.179. No circularity: E.179 does not use E.180.

### 2.6 E.181 (normalization, and (IV) ⇒ (R) ⇒ Λ): correct
- Cocycle law E.181.2 is NS Corollary 5.2. E.181.3: in the class-two quotient f = [x,y]^e, the λ = 1 hexagon gives
  3e = 0, and f = ϑ(β)β⁻¹ gives e = −ρ² − 2b; so ρ is even. E.181.4: κ₂(G_{Q^ab}) = 2Ẑ (√2 ∈ Q^ab; 2^{1/n} ∉ Q^ab for
  n ≥ 3). Hence F = F_*σ with σ ∈ G_Q, λ(F_*) = 1, ρ₂(F_*) = 0. I agree with sweep 2 on this step.
- (IV) ⇒ (R): this is Schneps 2006, p. 670, and I re-derived it. Under B̂₄ → Γ̂_{0,[5]} (σ_i ↦ half twists):
  e₁ ↦ x₄₅², e₃ ↦ x₅₁², e₂ ↦ a half twist with square x₁₄. The four substitutions are instances of
  f(u, w⁴) = f(u², w²) or its mirror, for pairs of half twists whose arcs meet in one endpoint. The middle two terms
  combine by the hexagon (x₄₅x₁₄x₅₁ = x₂₃ is central there), and the rest is the pentagon. Only (I), (II), (III) and
  normalized (IV) are used; ρ₃ does not occur, as E.181 says.
- **(b) The lift to the surface with boundary.** E.181 argues through capping and HLS Lemma 7. A shorter argument:
  the six factors of (R) are images of elements of B̂₄ (a_i ↦ σ_i; e₁ = (σ₁σ₂)⁶, e₃ = (σ₂σ₃)⁶ and
  e₂ = σ₃σ₂σ₁σ₂⁻¹σ₃⁻¹ hold on the surface with boundary). Their product dies in Γ̂_{0,[5]}, so it lies in the closure
  of the centre ⟨(σ₁σ₂σ₃)⁴⟩ of B̂₄. It also lies in the closed commutator subgroup, and (σ₁σ₂σ₃)⁴ has degree 12 in
  B̂₄^ab = Ẑ. So the product is 1 in B̂₄, hence in Γ̂₁². Same conclusion as E.181.
- Λ is, by HLS p. 4, the set of f ∈ GT̂¹ (= GT̂ with λ = 1) satisfying (R) in Γ̂₁². So f_* ∈ Λ.
- One identification I took from the literature and did not redraw: that the curve ε₂ of HLS Figure 2 is
  σ₃σ₂(α₁). It is stated by Schneps 2006, p. 659, and NS p. 4 quote the same (R).

## 3. Route 1

### 3.1 The solvable-case argument (NOTE_BOGGI_ZALESSKII_STEP.md, item 3): correct
If N_Ĝ(H) = closure(N_G(H)), then C_Ĝ(H) = ker(N_Ĝ(H) → Aut H) is open in it; an open subgroup U of the closure of a
dense subgroup D is the closure of U ∩ D; and U ∩ N_G(H) = C_G(H) because G embeds in Ĝ. So C_Ĝ(H) = closure(C_G(H)).
The note's caveat also stands: this needs the normalizer equality, which Boggi's Proposition 2.4 does not assume.

### 3.2 Does route 1 need the questioned step? No
- E.44 (`sections\E_branch_fixed_points.tex`, lines 155–177 and 199–209) uses Boggi–Zalesskii Theorem A (i) and (iii)
  for the 2-group H = C₂² in G ⊂ Γ_{0,[10]}: F(H) is conjugate into G, and C_Ĝ(H) = closure(N).
- The step ⋂ closure(Z(x_i)) = closure(⋂ Z(x_i)) is in Theorem 5.1(iii) (general subgroups) and in Boggi's
  Proposition 2.4. Theorem A is the p-group theorem (Theorem 3.x `pcase` in arXiv:2406.08639v2), proved by induction
  on |H| with its own argument.
- In that proof, item (iii) reads "By Lemma 2.3 and Lemma 2.2, we immediately conclude" both equalities. The
  normalizer equality does follow at once from item (ii) and Lemma 2.3 (`normcriterion`). For a non-cyclic H the
  centralizer equality does not follow from Lemma 2.2 (`centcriterion`), which is about single elements. It follows
  from the normalizer equality by the argument of §3.1. So for C₂² the published statement holds, with one line to
  add, and without the questioned step.
- The hypotheses of Theorem A for G at p = 2 (goodness, finite virtual cohomological type) are argued in E.44 lines
  159–177; that argument is right.
- I did not referee Boggi–Zalesskii's proof of Theorem A(i), (ii) (the order-p base case through the Brown-type
  theorem). **Route 1 does not have to rest on it:** E.176–E.177 of route 2 prove exactly the two statements E.44
  takes from Theorem A, for this G, and I checked them (§2.1–2.2).

### 3.3 E.44 from there on
The geometry is that of E.177–E.178 in another coordinate (U = (z²+1)²/(4z²), S(U) = U/(U−1), cone at 0). Lines
304–323 prove that the action β_A on R commutes with S_R up to an inner automorphism. I agree.

### 3.4 E.28
- E.28 (`sections\E.tex`, lines 3225–3525) defines 𝒥(λ, f) = (λ, V^{2c}f(v,d²)⁻¹D^{4c}) and claims that 𝒥(F) ∈ GT̂
  and that 𝒥 is a continuous involutive automorphism. E.44 then reads the commutation as 𝒥(A) = A.
- I checked that formula (E.72) is the parameter of SφS: f′(v, d²) = d^{4c} f(d, v²)⁻¹ v^{4c}. So the fixed-point
  equation 𝒥(F) = F is the first identity of E.179.2, which is (IV) modulo the centre.
- **The gate equation does not need E.28.** From "φ and SφS are inner-equivalent" the equation follows by the
  centralizer and abelianization computation of E.179.6–10, which I checked. E.28's extra content (that the pair
  (E.72) satisfies the five-point relation for every F, and the injective comparison) is needed only to speak of 𝒥
  as a map GT̂ → GT̂.
- Of E.28's proof I read lines 3225–3420 (the cut-surface group, first-strand doubling, strict doubling
  compatibility); no error found. Lines 3420–3525 are unread. E.28 as stated is therefore **not certified here**.
  The register can drop E.28 from the dependencies of the Δ gate and cite E.179.6–10 instead.

## 4. What the literature proves and leaves open

- **Nakamura–Schneps 2000** (Invent. Math. 141; author version 3.14, 48 pp., `papers\NS2000\`).
  - (IV): f(σ₁, σ₂⁴) = σ₂^{8ρ₂} f(σ₁², σ₂²) σ₁^{4ρ₂} (σ₁σ₂)^{−6ρ₂} in B̂₃ (p. 3); (III′) in Γ̂₀^{[5]} (Theorem 1.1).
  - Definition 1.1: 𝕀Γ = elements of GT̂ satisfying (III′) and (IV). Theorem 1.2: 𝕀Γ is a subgroup containing G_Q.
    Theorems 1.3–1.4: 𝕀Γ acts on every Γ̂^n_{g,m}, compatibly with subsurfaces.
  - Left open (p. 1): "we still leave it open to settle (in-)equalities between consecutive terms of
    G_Q ⊂ 𝕀Γ ⊂ GT̂".
  - Definition 5.1, Corollary 5.2: ρ₂ on GT̂ and its cocycle law. Proposition 5.3: ρ₂ = −A_F(−1,1), proved only under
    (III′). Lemma 6.1: under (III′), (IV) is equivalent to a formula for H_F(σ₂).
  - p. 4: (R) is for λ = 1; "the elements of 𝕀Γ with λ = 1, ρ₂ = 0 satisfy the above relation (R)".
- **Hatcher–Lochak–Schneps 2000** (J. reine angew. Math. 521; scan, `papers\HLS2000\`, pp. 3–5 read).
  - Λ = {f ∈ GT̂¹ : (R) holds in Γ̂₁²} (p. 4). Theorem A: Λ is a subgroup. Theorem B: for every surface and pants
    decomposition, ψ_P: Λ → Aut(Γ̂(Σ)) with the A- and S-move formulas; the outer action is canonical.
  - p. 3: Λ is known to contain G_K, K = Q(all roots of unity, all roots of 2), through NS. Whether Λ = GT̂¹ is not
    decided there.
- **Schneps 2006** (Math. Nachr. 279, `papers\Schneps2006\`): p. 659 lists (R), (III′), (IV), (NT1), (NT2) for
  λ = 1, ρ₂ = ρ₃ = 0; p. 670: (IV) with (I), (II), (III) implies (R).
- **Lochak–Nakamura–Schneps 2026** (arXiv:2602.12462v1, TeX in `papers\arxiv_2602.12462\src\`).
  - Theorem 1.1: every F ∈ GT̂ acts on Γ̂_{g,0} and Γ̂_{g,1}, g ≥ 1, by Drinfeld-type formulas on Wajnryb's generators.
  - §1: "It is unclear, however, whether the additional condition actually defines a proper subgroup of GT̂".
  - §8: whether the action restricts to images of Γ̂_{g′,n′} is not known for GT̂ ("At the writing of this paper, we
    do not know if this holds for GT̂"); it is known for 𝕀Γ; the extension of the Lego action to all of GT̂ is
    "the subject of a future research project".
- **Does LNS 2026 settle, use or contradict E.179–E.181?** None of the three. It proves a different statement
  (actions for n ≤ 1 without the Lego rules), by presentations, and states the question as open nine months ago.
  Nothing in it conflicts with (IV) holding on GT̂.

## 5. What the gate means for the field, if it stands

1. **(IV) is a consequence of (I)–(III).** Every F ∈ GT̂ satisfies (IV) with ρ₂(F). So NS's 𝕀Γ is cut out of GT̂ by
   (III′) alone, and NS Proposition 5.3 holds on all of GT̂. This answers half of the question NS left open; (III′)
   is untouched.
2. **Λ ⊇ {F ∈ GT̂ : λ = 1, ρ₂ = 0}, and GT̂ = Λ · G_Q.** HLS knew only G_K ⊂ Λ. With HLS Theorem B, every element of
   GT̂ is a product of an element acting on the whole pure tower by the flat pants formulas and a Galois element.
   That is not yet a Lego action of the group GT̂ on the tower (LNS 2026 §8): the two actions have to be shown to
   fit together into one homomorphism. SECTION_GHOSTS E.182 and EXIT_TOWER E.42 claim parts of this; I did not
   referee them.
3. The method is the new part: a finite subgroup of Γ̂_{0,[n]} is brought back to the discrete group by Smith
   theory along a cohomology-killing tower, and one special locus seen through two forgetting maps gives the
   relation. The same method should be tried on (III′) (the order-two and order-five loci of M_{0,5}).

**What a mathematician would check first:**
1. E.176: the two-stage Tate argument with infinite cochain complexes, and that it yields both E.176.2 and
   E.176.4. Boggi–Zalesskii Theorem A(i), (iii) at p = 2 gives the same two statements and is a cross-check.
2. The forgetting squares on the mixed label stabilizers (§2.4 (a)); this is where GT̂ sees both quartets.
3. T(u) = 2(u+6)/(u−2), the base point u₀ = 6, and T_* = S.
4. The coefficients in E.179.9–12 and E.180.17–18.
5. That HLS's ε₂ is σ₃σ₂(α₁) (§2.6).

Related work I know of but did not open in this pass: B. Collas, J. Théor. Nombres Bordeaux 24 (2012), on GT̂ and
prime-order torsion of Γ̂_{0,[n]}. It should be compared with E.176–E.177 before any claim of novelty for the method.

## 6. Papers opened
- `papers\arxiv_2602.12462\src\LochakNakamuraSchneps2026.tex` (lines 93–340, 1840–1890, bibliography).
- `papers\arxiv_2406.08639\goodtorsion18b.tex` (Theorem A; Lemmas 2.2, 2.3; Theorem `pcase` and its proof, lines 425–840).
- `papers\arxiv_2408.12486\src\CongSym.tex` (downloaded; not needed beyond the note's quotation of Proposition 2.4).
- `papers\NS2000\newGT.pdf` and `.txt` (§1, §5, §6 to Lemma 6.1).
- `papers\HLS2000\crelle.pdf` (scan; pp. 3–5 read as images). Pages 18–23 (Theorems 4–5, Lemma 7) not read.
- `papers\Schneps2006\automorphisms.pdf` and `.txt` (pp. 659, 670).
