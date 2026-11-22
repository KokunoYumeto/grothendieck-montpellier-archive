# Cote 84 (SA02, "Géométrie et topologie combinatoire", part 2): the reading

- **Who:** Claude Opus 5.5 at effort max, reader R4 of the deep-sweep agent a6d42bf6fe2b0d8a8 (Claude Opus 5.5 at effort max), horizontal sweep 3, wave 1, topic SA02.
- **Date:** 19 Nov 2026.
- **What was read, and how:**
  - The Codex-web transcriptions `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K84-01` to `K84-12` (scans 2-193), through the lead's cleaner (`clean_tex.py`, `show.py`), my squeezer and a filter that drops drawing coordinates.
  - The Pro packages (GPT-6 Astra, ChatGPT Pro mode) `inputs/SA02/pro/MPL_84_097-145` and `MPL_84_146-193`, through the same tools. Where the two witnesses overlap (97-193) they were compared; see "The witnesses compared".
  - The stage-A dossier of GPT-6 Astra (ChatGPT Pro mode), `stage_a_20261118_sent/returns/SA02_part2_final_20261119T1453Z_unzipped/`, was used as a witness where cited.
  - Scans: `grothendieck_archive_montpellier/11_geometrie_et_topologie_combinatoire/84.pdf` (193 pages, scan N = PDF page N).
  - The doubts files and audits were used only by counts.
- **Items (sweep 2 map):**
  - SA02-1: product of quadratic algebras.
  - SA02-2: relative trace and norm.
  - SA02-3: three quadratic algebras.
  - SA02-4: χ-trivialized extensions.
  - SA02-14: graded monoid, scan 2.
  - SA02-5 and SA02-9: questions and proposals of the notes.
  - SA02-6 and SA02-7: the reused typescript.
  - SA02-8: the apparatus.
- **Ids:** check events SA02-R84-nn; corrections SA02-K84-nn.
- **Computations:** in my scratchpad folder `r4sa02`.

## 84/2-8. A graded monoid of discriminant data; three quadratic algebras; scrap

**What he does.**
- 84/2-3 (SA02-14): R_* = R_0 ⊔ R_1 over Z/2.
  - R_0 consists of triples (L, δ, T_0), multiplied as (LL', δδ', T_0T'_0). R_1 consists of pairs (L, δ) ("discr. divisé"), multiplied as (LL', δδ').
  - α: R_0 → R_1 forgets T_0; β: R_1 → R_0 sends (L, δ) to (L, 4δ, 0), and is "pas un hom de monoïdes !".
  - The product ∧ is x·y on R_0, β(xy) on R_1 × R_1, and xα(y) on mixed pairs.
  - He reduces associativity to ① β(α(x)u) = xβ(u) and ② αβ(x) = xη (η = αβ(1) = α(ζ), ζ = β(1) = (O, 4, 0)), derives βα(x) = xζ and β(x)β(y) = ζβ(xy) ("OK"), and checks the concrete case.
  - Then a homomorphism w: R_* → R_0 and an "Arf(E)" for E = ⊕(L_i, δ_i), "un inv. plus fin que c_1(E) (si 2 non inv. sur X)".
- 84/4: three quadratic algebras A_i (u_i² + c_i = 0), A = A_1 ⊗ A_2 ⊗ A_3 with the involutions σ_i.
  - The seven quadratic subalgebras A_i, B_i = ⟨1, u_ju_k⟩ ≃ A_j ∧ A_k and B_0 = ⟨1, u_1u_2u_3⟩ ≃ A_1 ∧ A_2 ∧ A_3 are the fixed rings of the seven index-2 subgroups of F_2^3.
  - The seven rank-4 subalgebras A'_i, B'_i are the fixed rings of the seven involutions.
  - A_i ⊗ A'_i ≃ A, and B_0 ⊗ B'_0 ≃ A when the c_i are invertible; "14 situations biquadratiques".
- 84/6: in a quadratic algebra, N(ū + α) = N(ū) + αTr(ū) + α² forces α = 0 when 2 is invertible; norm-one elements; the norm torus 1 → SW → W^* → G_m → 1.

**Checks.**
- **SA02-R84-01 (independent re-proof).**
  - ① and ② are exactly what associativity of ∧ needs (cases b') and a')); both consequences follow, and so does the concrete check (L, δ) ↦ (L, 4δ, 0).
  - So the graded monoid is right as he sets it up.
  - His table on 84/3 labels the pairs "Pair" and the triples "Impair". By the products he writes (pair · pair = triple), the triples are the even part.
  - The w, Arf and c_1 formulas at the foot of 84/2 were read, not checked.
- **SA02-R84-02 (targeted proof check).**
  - The fixed rings on 84/4 are right.
  - The inclusion list has one slip: "B_2 ⊂ A'_1, B'_1, B'_0" should be B_2 ⊂ A'_2, B'_2, B'_0 (SA02-K84-01).

**Reused material.**
- 84/3 carries a household note and the printed wrapper of a ream of offset paper.
- 84/5 and 84/7 are typescript pages of Récoltes et Semailles (the passage on the "Éloge funèbre" of 18 May; "le chasseur de papillons ... l'enfant nu devant la mer").

## 84/9-42. "Formes quadratiques binaires et revêtements quadratiques" (a draft)

**What he does.**
- §1: similitude structures. Sim(E) = Quad(E)/O^*, with the faithful and strictly faithful cases. A structure ↔ a locally monogenic Δ ⊂ Quad(E), and the canonical form Q_Σ: E → Δ^∨ (1.4-1.5).
- §2, rank 2, L = det E:
  - 0 → O → End(E) → Sym²(E) ⊗ L^∨ ≅ Quad(E) ⊗ L → 0 (2.2). So similitude structures ↔ subalgebras 𝒜 ⊃ O·1 of End(E) with 𝒜/O monogenic (Lemma 1, by Cayley-Hamilton).
  - Lemma 2: strictly faithful ⇔ 𝒜 is a rank-2 subbundle ⇔ u(s) is never a scalar ⇔ E is an invertible 𝒜-module.
  - 2.3: Q_u(x) = u(x) ∧ x ("il faut vérifier le signe !"); in coordinates Q_u(λ, μ) = cλ² + (d-a)λμ - bμ², and the u_a with Q_{u_a} = αλ² + βλμ + γμ². Then δ(u) = (Tr u)² - 4N(u) = -δ(Q_u) ("Attention au signe").
  - 2.4-2.6: the quadratic algebra 𝒜_Q as a pullback extension, with norm N_Q, and u'_Q: 𝒜_Q → End(E). In bases u² - βu + αγ = 0 and u_Q = [[0, -γ], [α, β]]. Its quadratic cover "mérite de s'appeler l'invariant d'Arf de la forme quadratique binaire Q".
- §3, "Théorème récapitulatif": equivalences of fibered categories between
  - ① strictly faithful binary similitude structures;
  - ①' (E, Δ', Q) with Q nowhere zero on a fibre;
  - ② (𝒜, E), with E an invertible 𝒜-module;
  - ②' (X', Λ'), with ②' → ①' given by E = p_*Λ', Δ' = N_{X'/X}Λ' and Q the norm.
  - Cor. 1: torsors under W(𝒜)^*.
  - Cor. 2: scalar forms ↔ (𝒜, Π), Π a torsor under the norm-one group U_𝒜, "la top. (Zar) n'est plus assez fine".
  - The quadratic cover is the subscheme Q(x) = 0 of P(E).
- §4: the dependence only on the Azumaya algebra M = End(E). A first guess, E ≅ End(E)/𝒜 up to scalars, is withdrawn by him: "la supposition du début est erronée". "En rectifiant le tir" he takes M/M^♮ with φ_u(θ) = uθ - θū, and B = {θ : ūθ = θu}.
- 84/35-39: the Θ normalizing A and inducing σ correspond to u' = ū + α with 2α = 0 and α(α - b) = 0.
  - Hence (Prop. and Cor., 84/36): when A is étale at the points of characteristic 2, the canonical involution is the only automorphism inducing -id on A/O.
  - In characteristic 2, ramified, u ↦ u + α with α² = 0.
- 4.2 (84/36-42): the symmetry σ_D of a non-isotropic line, σ_e(x) = φ_Q(e, x)e - x.
  - σ_D u σ_D^{-1} = ū.
  - M = {Θ : Θu = ūΘ} is an invertible 𝒜-module; the Θ of norm -1 form a torsor under SW(A).
  - The non-isotropic lines P^* = P(E) - X' map compatibly with u ↦ u².

**Checks.**
- **SA02-R84-03 (targeted proof check).** The following are right:
  - Quad(E) ≅ Sym²(E^∨) for locally free E of finite type;
  - the sequence of 2.2, and Sym²(E) ⊗ L^∨ ≅ Quad(E) ⊗ L;
  - Lemma 1;
  - Lemma 2 (a non-scalar 2 × 2 endomorphism is cyclic; then Nakayama);
  - the basis description of 2.6 (Tr u_Q = β, N = αγ);
  - the zero form (dual numbers, 2.5);
  - δ(u) = -δ(Q_u) with his determinant definition of δ(Q) (det [[2α, β], [β, 2γ]] = 4αγ - β²).
- **SA02-R84-04 (targeted proof check).** His coordinate formula and u_a agree with each other, and give Q_u(x) = x ∧ u(x) in the basis e_1, e_2. The "u(x) ∧ x" he writes has the opposite sign, so his "il faut vérifier le signe !" is justified (SA02-K84-02).
- **SA02-R84-05 (carried as background without fault found).**
  - The equivalences of §3 are the correspondence between primitive binary quadratic forms with values in a line bundle and pairs (quadratic algebra, invertible module) (Kneser 1982; Wood 2011, "Gauss composition over an arbitrary base"; locators to be checked). Nowhere-zero on fibres is primitivity, and the zero locus in P(E) is Spec of the even Clifford algebra.
  - The topology remark is right: W(𝒜)^*-torsors are Zariski-local (Hilbert 90 for a Weil restriction of G_m), U_𝒜-torsors in general are not.
- **SA02-R84-06 (targeted proof check).**
  - The uniqueness of the canonical involution (84/35-39) is right: 2α = 0, α(α - b) = 0, and at a point of characteristic 2 where b is a unit, α must be 0.
  - The automorphisms of O[u]/(u²) are right.
  - σ_D u σ_D^{-1} = ū reduces to u x̄ = ū x on E = A, which is right.
  - Slip: on 84/42, f(u·D) = uū^{-1}f(D) "(= f(D)ū²)". For N(u) = 1, uū^{-1} = u², which is what his next line uses (SA02-K84-03).

## 84/43. Title sheet

- "χ-scindages, produits contractés d'extensions χ-scindées, construction de revêtements quadratiques, invariants d'Arf-Stiefel-Whitney généralisés, etc."
- This is the programme of the rest of the cote (SA02-4, SA02-1).

## 84/44-65. Quadratic covers through (L, P_1, Q); the case 2 regular; characteristic 2; the contracted product

**What he does.**
- 84/44-48: a quadratic algebra 𝒜 is described through E = 𝒜^∨, P_1 = ψ^{-1}(1) (an L-torsor), the trace T ∈ Γ P_2, the norm N ∈ Γ Sym²(E) and δ with T² - 4N = δ ("attention au signe → δ est le discr. de N changé de signe").
  - The form Q(x) = x² - ψ(x)Tx + ψ(x)²N takes values in L^{⊗2}, and Q(φ_N(x)) = N(x)δ ("Vérification à partir du cas décomposé").
  - Étale ⇔ φ_N is an isomorphism ⇔ δ is invertible.
  - z = 2x - T turns sections of X'/X into solutions of z² = δ.
  - On X_0 = V(2), T_0² = δ_0. The class "T_0² ≡ δ (4)" is well defined, since (τ_1 + 2α)² ≡ τ_1² (4).
- 84/49-53: "Supposons 2 O_X-régulier. Alors la donnée des rev. quadratiques X'/X équivaut à celle des (L, δ, T_0) satisfaisant T_0² ≡ δ (4)". He makes this explicit:
  - E = {(λ, ζ): ζ lifts λT_0};
  - 𝒜 = {(b, r) ∈ O × L^∨: b_0 = r_0T_0}, with N(b, r) = (b² - r²δ)/4 and xx' = (½(bb' + rr'δ), ½(br' + rb'));
  - φ_N = ½(bb' - rr'δ) and Q(λ, ζ) = (ζ² - λ²δ)/4, integral because ζ ≡ λT (2);
  - the normalization checked at y = T (84/54).
- 84/54-56: torsors under μ_2 against (Z/2)_X.
  - The forgetful functor (L, Θ) ↦ (L, 4Θ, 0) does not commute with ∧: (L⊗L', 16ΘΘ') against (L⊗L', 4ΘΘ').
  - So he defines a mixed monoidal category with parities, with the modified product (L, δ, 0) ∧^! (L', δ', 0) = (L⊗L', ¼δδ', 0). Here ¼δδ' := 4ΔΔ' with δ = 4Δ locally, which is independent of the choice of Δ. This is the graded monoid of 84/2.
- 84/57-58, characteristic 2: f_T(u) = u² + Tu, and X'/X is a torsor under the finite flat group G_T = ker f_T. Theorem: quadratic covers ↔ (L, P_1, T, α) ("Plus de doute, c'est lui !"). The products G_T × G_{T'} → G_{TT'} give ∧ of torsors.
- 84/59-62: four equivalent fibered categories, including ③' (an extension 0 → L → E → O → 0 with a form Q, Q|L = u ↦ u²). With a splitting x_0, N = x_0² - bx_0 + c, T = 2x_0 - b and Θ = T² - 4N = b² - 4c.
- 84/63-65: the contracted product of quadratic covers.
  - It has L = L_1 ⊗ L_2, δ = δ_1δ_2 and b = b_1b_2 ("sauf erreur").
  - From 4c = b² - δ: c = b_2²c_1 + b_1²c_2 - 4c_1c_2.
  - He guesses (x_1 + u_1) ∧ (x_2 + u_2) = x_1 ∧ x_2 + u_1b_2 + u_2b_1 + 2u_1u_2 and verifies it: Q(u) = b_2²Q_1(u_1) + b_1²Q_2(u_2) + 4[Q_1Q_2 - c_1Q_2 - c_2Q_1].
- 84/66: "Retenons donc Q(x_1 ∗ x_2) = c_1δ_2 + c_2δ_1 + 4c_1c_2".

**Checks.**
- **SA02-R84-07 (targeted proof check).** All right:
  - Q(z + T) = z² - δ;
  - the well-definedness of T_0² ≡ δ (4);
  - the explicit 𝒜 = {(b, r)}: write x = (b + r√δ)/2; then N = (b² - r²δ)/4 is integral because b² ≡ r²T² ≡ r²δ (4), and the product and φ_N follow;
  - Q(λ, ζ) = (ζ² - λ²δ)/4 with its integrality, and the normalization Q(T) = -δ (his displayed "(0 + 4δ)/4" should be (0 - 4δ)/4; his conclusion -δ is right);
  - the invariance of ¼δδ' := 4ΔΔ';
  - the characteristic-2 description (f_T additive, G_T finite flat, étale iff T is invertible).
  - The classification "(L, δ, T_0) with T_0² ≡ δ (4) when 2 is regular" is the classification of quadratic covers by (L, D, b_0) on cote 77 (77/53-64, 74-86; SA04-25, hunch H77-1), here in his own notation.
- **SA02-R84-08 (computation, `c84a.py`, sympy).**
  - The identity of 84/65 holds exactly as he first writes it: Q(u) - [b_2²Q_1(u_1) + b_1²Q_2(u_2) + 4(Q_1Q_2 - c_1Q_2 - c_2Q_1)] = 0.
  - His restatement in the box, with b_1² and b_2² exchanged, is wrong unless b_1² = b_2² (SA02-K84-04).
  - c_1δ_2 + c_2δ_1 + 4c_1c_2 = b_2²c_1 + b_1²c_2 - 4c_1c_2.
  - So u = 2u_1u_2 + b_2u_1 + b_1u_2 is a root of u² + b_1b_2u + c (SA02-1; the same as the ∗-composition c = b_2²c_1 + b_1²c_2 - 4c_1c_2 of SA01's cote 83).
- **Slips:**
  - "c = c_1δ_2 + c_2δ_1 + 4c_1c_1" on 84/64 should read 4c_1c_2 (SA02-K84-05);
  - "(0 + 4δ)/4" on 84/54 (in SA02-K84-05).

## 84/66-87. χ-trivialized torsors and their product ("Digression affine")

**What he does.**
- 84/66-68: for a section χ of O, the category of triples (L, P, T), T a trivialization of _χP. Equivalently: extensions 0 → M → E → O → 0 with T ∈ E, ψ(T) = χ; or χ-retractions π: E → M with π∘i = χ·id. The two are related by π(x) = χx - Tψ(x).
- 84/68-72: the product.
  - E_1 ∗ E_2 is the pushout of E_1 ⊗ E_2 along μ, which is defined by α_1 = id ⊗ π_{T_2} and α_2 = π_{T_1} ⊗ id. These agree on L_1 ⊗ L_2 (both give χu_1 ⊗ u_2; "OK !").
  - The χ-trivialization of the product is σ = χ·id ("On gagne !"). If χ is regular on L_1 ⊗ L_2, then χT = T_1 ∗ T_2, "T = (1/χ)T_1 ∗ T_2 (!)".
- 84/72-73: a first sign convention gives (x_1 + u_1) ∗ (x_2 + u_2) = x_1 ∗ x_2 + (-u_1⊗b_2 - b_1⊗u_2 + χu_1⊗u_2), with "Attention signe !". "Pour éliminer le signe" he redefines b = π_T(x) = χx - T. Then b_{T, x_1∗x_2} = b_{T_1,x_1} ⊗ b_{T_2,x_2}.
- 84/73-75, "Formulaire récapitulatif":
  - ① bilinearity; ② ψ(x_1 ∗ x_2) = ψ_1(x_1)ψ_2(x_2);
  - ③ u_1 ∗ x_2 = u_1 ⊗ π_2(x_2), x_1 ∗ u_2 = π_1(x_1) ⊗ u_2, u_1 ∗ u_2 = χu_1 ⊗ u_2;
  - ④ π_i(x) = χx - T_i;
  - ⑤ π_E(x_1 ∗ x_2) = π_1(x_1) ⊗ π_2(x_2);
  - Cor.: T = χ(x_1 ∗ x_2) - b_1 ⊗ b_2, and the verification χT = T_1 ∗ T_2 ("OK").
- 84/76-80:
  - the universal property (biaffine maps compatible with the χ-trivializations), and morphisms of χ-trivialized torsors;
  - the split case: T = χx_0 - b and π(λx_0 + u) = λb + χu; for products b = b_1 ⊗ b_2, "Il n'y a pas plus simple !";
  - the commutativity, associativity and unit constraints;
  - (E, ψ, T) is invertible for ∗ iff L is invertible and T_0 is a basis of L_0 on X_0 = V(χ).
- 84/80-87, χ = 2:
  - the canonical involution σ_E(x) = Tψ(x) - x;
  - with 2 invertible the theory is "tot.! triviale";
  - Proposition (84/86): for L_1, L_2 locally free of finite type, E_1 ⊗ E_2 → E_1 ∗ E_2 induces (E_1 ⊗ E_2)_{σ_1⊗σ_2} ≅ E_1 ∗ E_2 iff, at each point of X_0 = V(2), T_{10} or T_{20} generates L_{10} resp. L_{20}. With splittings and invertible L_i: 2O + b_1L_1^∨ + b_2L_2^∨ = O.
  - Corollary (84/87): dually, 𝒜 ≅ (𝒜_1 ⊗ 𝒜_2)^{σ_1^∨⊗σ_2^∨}.

**Checks.**
- **SA02-R84-09 (independent re-proof).** All right, with his final convention b = π(x):
  - π(x) = χx - Tψ(x), and the equivalence of the three descriptions;
  - the agreement of α_1 and α_2 on L_1 ⊗ L_2;
  - χT = T_1 ∗ T_2: T_1 ∗ T_2 = χ²x_1∗x_2 - χb_1⊗b_2 - χb_1⊗b_2 + χb_1⊗b_2 = χ(χx_1∗x_2 - b_1⊗b_2);
  - formulas ①-⑤ and the split case π(λx_0 + u) = λb + χu.
- **SA02-R84-10 (computation, `c84a.py`).** The Proposition and Corollary of 84/86-87 hold over Z. For A_i = Z[u_i]/(u_i² + b_iu_i + c_i), the fixed lattice of σ_1 ⊗ σ_2 is {a + pu_1 + qu_2 + ru_1u_2 : 2p = rb_2, 2q = rb_1}. It equals Z[u] (u = b_2u_1 + b_1u_2 + 2u_1u_2) iff b_1 or b_2 is odd, and has index 2 otherwise (e.g. Z[i] ⊗ Z[i]: Z[2ij] in Z[ij]). This is his condition 2O + b_1O + b_2O = O.
- **Transcription.** On 84/82 the overlines (x̄) are lost in "x_1∗x_2 = x_1∗x_2 = x_1∗x_2" (SA02-K84-06).

## 84/87-98. Back to quadratic covers: the admissible form on E_1 ∗ E_2; E ≅ 𝒜 ⊗ L

**What he does.**
- 84/87-89:
  - over X_0 = V(γ), a γ-trivialization is a section T of L;
  - E_1 ⊗ E_2 → E_1 ∗ E_2 factors through E_1 ×_O E_2, the extension of the torsor P_1 × P_2;
  - P_1 ∗ P_2 is the torsor pushed out along (u_1, u_2) ↦ u_1⊗b_2 + b_1⊗u_2.
- 84/89-91, admissible forms. On a 2-trivialized E, an admissible Q (Q(u) = u² on L, trace T) is, in a splitting, Q(λx + u) = u² + λbu + λ²c, so the choices form an L^{⊗2}-torsor.
  - Th. (84/90): there is a unique admissible Q on E_1 ∗ E_2 with Q(x_1 ∗ x_2) = Q_1(x_1)δ_2 + Q_2(x_2)δ_1 + 4Q_1(x_1)Q_2(x_2) for x_i ∈ P_i. In a splitting, c = c_1δ_2 + c_2δ_1 + 4c_1c_2 = c_1b_2² + c_2b_1² - 4c_1c_2.
  - Cor.: δ = δ_1δ_2.
  - "Il faut prouver que Q(y_1 ∗ y_2) satisfait la formule écrite -- c'est un petit calcul délectable, que j'ai pratiquement déjà fait plus haut."
- 84/92-93, the programme:
  - X_1 ∧ X_2 and X_1 × X_2 → X_1 ∧ X_2, with their constraints;
  - X_1 ∧ X_2 is the twist of X_2 by the Z/2-torsor X_1 when X_1 is étale;
  - X_1 ∧ X_2 is étale iff both are;
  - X_1 × X_2 → X_1 ∧ X_2 is faithfully flat except exactly at the points where neither is étale.
- 84/94-98: with a splitting x_0, 𝒜 ≅ O ⊕ L^∨, ⟨u, b⟩ = -Tr(u), the minimal equation u² + b(u)u + c(u) = 0, and the points x_0 + v with Q(v) = 0.
  - The isomorphism E ≅ 𝒜 ⊗ L given by g_x(y) = ψ(x)y - ψ(y)x, with the normalizing constant λ = 1 proved.
  - g is a morphism of extensions with -id on L ("Attention au signe").
  - N and Q correspond: N(v + λ) = λ² - λ⟨v, b⟩ + ⟨v², c⟩.

**Checks.**
- **SA02-R84-11 (independent re-proof).**
  - The Theorem of 84/90 is right for all x_i ∈ P_i, not only for the base points. With y_i = x_i + u_i, y_1 ∗ y_2 = x_1 ∗ x_2 + w with w = u_1b_2 + b_1u_2 + 2u_1u_2 (χ = 2). Then Q(y_1 ∗ y_2) = w² + bw + c, which by the identity of SA02-R84-08 equals b_2²Q_1 + b_1²Q_2 + 4(Q_1Q_2 - c_1Q_2 - c_2Q_1) = Q_1(y_1)δ_2 + Q_2(y_2)δ_1 + 4Q_1(y_1)Q_2(y_2). This is the "petit calcul délectable".
  - δ = δ_1δ_2 is right.
  - "X_1 ∧ X_2 étale iff both are" follows.
  - The faithful-flatness statement agrees with the criterion of 84/86 (SA02-R84-10) and was not checked further.
- **SA02-R84-12 (targeted proof check).** The isomorphism g of 84/95-97 is right: g_x(u) = ψ(x)u, and on L, g(x)(y) = -ψ(y)x. So is the norm in the splitting.
  - His "Q_N(φ_N(x)) = -N(x)δ_N" (84/98) differs in sign from "Q(φ_N(x)) = N(x)δ" (84/47). This follows his two conventions for δ (84/44: "δ est le discr. de N changé de signe"); it is not a contradiction.

## 84/99-112. The trace and norm of A_1 ⊗ A_2 over A = A_1 ∧ A_2; quasi-quadratic algebras

**What he does.**
- 84/99-104: the map τ: A_1 ⊗ A_2 → A, x_1 ⊗ x_2 ↦ x_1 ∗ x_2 (a "trace"), and the map i: A → A_1 ⊗ A_2, U ↦ 2U_1U_2 + b_1U_2 + b_2U_1.
  - i(Tr ξ) = ξ + ξ̄ with ξ̄ = (σ_1 ⊗ σ_2)(ξ).
  - The images 1 ↦ 2, U_1 ↦ -b_1, U_2 ↦ -b_2, and "il y a lieu de prendre U_1 ∗ U_2 = U + b_1b_2".
  - When at every point of characteristic 2 one of the factors is étale, i is injective with image (A_1 ⊗ A_2)^{σ_1⊗σ_2}.
- 84/105-107, Proposition:
  - 1) Tr_{A_1⊗A_2/A}, with i ∘ Tr = ξ + ξ̄ and Tr(i(η)) = 2η;
  - 2) a unique quadratic N = N_{A_1⊗A_2/A} with N(x_1 ⊗ x_2) = N_1(x_1)N_2(x_2) and φ_N(ξ, η) = Tr(ξη̄). Then i(N(ξ)) = ξξ̄, N is invariant under σ_1 ⊗ id, N(i(η)) = η², and the transitivities N_{A/O}(N(ξ)) = N_{A_1⊗A_2/O}(ξ) and Tr_{A/O} ∘ Tr = Tr_{A_1⊗A_2/O}. He proves the first through the four conjugates ξ_0ξ_1ξ_2ξ_3.
- 84/107-110: the axioms of an "algèbre quasi-quadratique" (α: k → A not necessarily injective, with t and n satisfying ①-⑤, and ⑥ optional). x̄ = τ(x) - x is an algebra automorphism ⇔ 2xy = τ(xy) - τ(x)τ(y) + τ(y)x + τ(x)y. φ_n(x, y) = t(xȳ), n(1) = 1, α(n(x)) = xx̄.
- 84/111-112: the "quasi-biquadratique" data, A_1, A_2, A_3, A with compatible quasi-quadratic structures (SA02-2, SA02-3).

**Checks.**
- **SA02-R84-13 (targeted proof check).** All right:
  - U_1 ⊗ U_2 + Ū_1 ⊗ Ū_2 = 2U_1U_2 + b_1U_2 + b_2U_1 + b_1b_2, so U_1 ∗ U_2 = U + b_1b_2. His display writes Ū_1 = "-b_1 + U_1" for -b_1 - U_1 (SA02-K84-07); the result is right.
  - The injectivity condition is the Proposition of 84/86 (SA02-R84-10).
  - N_{A/O}(ξξ̄) = (ξ_0ξ_3)(ξ_1ξ_2) is the transitivity of norms in the tower O ⊂ A ⊂ A_1 ⊗ A_2 when i is injective. Where i is not injective, the transitivity rests on his universal definition and was not checked.
  - The axioms of 84/107-110: 2xy = τ(xy) - τ(x)τ(y) + xτ(y) + yτ(x) is equivalent to x̄ȳ = conj(xy); n(x̄) = n(x) from n(x + λ) = n(x) + λ² + λt(x); α(φ_n(y, z)) = τ(yz̄).

## 84/112-122. Quasi-biquadratic systems; three quadratic algebras; the étale case

Read in the Pro witness (MPL_84_097-145), compared with K84-08.

**What he does.**
- 84/112-115, the axioms:
  - 1° T_2(α_1(x)) = t_1(x), i.e. t_1 ⊗ id = T_1 on A_1 ⊗ A_2, so σ_2 induces the involution of A_1;
  - 2° the same for norms, and 2° implies 1°;
  - 3° σ_1σ_2σ_3 = 1, so the σ_i commute, and 2x = T_1(x) + T_2(x) + T_3(x) - T_{A/k}(x).
  - Then n_i(N_i(x)) = x_0x_1x_2x_3 and N_1(x)N_2(x)N_3(x) = x²N_{A/k}(x).
- 84/116-118: the even subgroup γ ⊂ F_2^3 acts on A. He wants Spec A → X_1 ∧ X_2 ∧ X_3 to be constant, which follows from A^γ = k·1_A. If 2 is invertible, A^γ = k: σ_i(a) = a for all i gives 6a = 2a + T_{A/k}(a), so a = ¼T_{A/k}(a).
- 84/119-121: Proposition (all A_i étale, k → A injective, ⊗A_i → A onto, A^γ = k): the situation is a twist of the one of three 2-element sets. The proof uses the Lemma of 84/120. "J'ai envie de vérifier" the non-étale case.
- 84/122: the universal situation over X_1 ∧ X_2 ∧ X_3, whose morphism "n'est pas même fini loc. libre, ni même plat".

**Checks.**
- **SA02-R84-14 (used and rechecked in this run).**
  - The identities of 84/114-115 and the computation 4a = T_{A/k}(a) are right.
  - The Lemma of 84/120 was decided in sweep 2 on the scan (`sweep2/REPORTS/cote84_scan120_lemma_hypothesis.md`): the ink reads X_J in b), the lemma is false as written, and true with k → Γ(𝒳, O_𝒳) injective and 𝒳 closed, by his own argument. I rechecked the counterexample (Spec k/𝔞)_J and the corrected argument. This is SA02-K84-10, recorded here for completeness.

## 84/124-192 (even scans). χ-trivialized extensions of invertible modules; signs; the product A_1 ∧ A_2 by duality

Read in the Pro witness (MPL_84_097-145 for 124-144, MPL_84_146-193 for 146-192), compared with K84-09 to K84-12. The odd scans are the reused typescript (below).

**What he does.**
- 84/124-144: extensions 0 → L_i → E_i → M_i → 0 with splittings p_i and χ-trivializations b_i. A change p'_i = p_i - U_i gives b'_i = b_i + χU_i, and the change for the product is U = b_1⊗U_2 + U_1⊗b_2 + χU_1⊗U_2.
  - On 132, "Je dis que U'' = U + U'", with both sign conventions in the ink.
  - On 134-136, (U_1 ∗ U_2)(x_1 ∗ x_2) = -χU_1(x_1) ⊗ U_2(x_2), "signe étrange !". He blames the "-id" in the diagram E → Hom^!(E, H), x ↦ [y ↦ -xψ(y) + yψ(x)].
  - On 140, the line "2 - χ = 1".
- 84/146-158:
  - σ_i = id - γπ_i;
  - 152: the check "-χ(1 - γχ) + 2(1 - γχ)χ + γχ² = χ, χ = χ o.K.!", his correction of 140;
  - 156: for χ = 2, δ = 1, the map 2x_1⊗x_2 - [x_1⊗π_2(x_2) + π_1(x_1)⊗x_2] + π_1(x_1)⊗π_2(x_2) = x_1⊗x_2 + x̄_1⊗x̄_2 ("o.K.");
  - 158: β = γ = 1 - δχ and α = -χ(1 - δχ);
  - 156: "-χ(1 - δχ) ≟ χ ⇔ δχ = 2".
- 84/160-170:
  - the dual (E_1 ∧ E_2)^∨ ≅ E_1^∨ ∧ E_2^∨;
  - two constructions E_1 ∨ E_2 and E_1 ∧ E_2 with a canonical map between them;
  - χ-trivializations as pairs (π_i, ϖ_i) with α_iπ_i + ϖ_iψ_i = χ id (170);
  - the 4 × 4 table of F_ij (154, 164, 166).
- 84/172-192:
  - u = 2u_1u_2 + b_2u_1 + b_1u_2 solves u² + bu + c = 0, with b = b_1b_2, c = b_1²c_2 + b_2²c_1 - 4c_1c_2 and δ = δ_1δ_2, "(injectif sauf si car. 2 et b_1 = b_2 = 0)" (172);
  - u_1 ∗ u_2 = b_1b_2 + u through the pairing (176);
  - the pairing between A = (A_1 ⊗ A_2) ⊕_{A_1⊕_O A_2} O and E = (E_1 ⊗ E_2) ⊕ L_1⊗L_2, with ⟨f, x⟩ = ⟨f + σf, x⟩ = ⟨f, x + σx⟩ (178-190);
  - Tr(u_1 ∗ u_2) = -λβ + 2μ and N(u_1 ∗ u_2) = λ²c + μ² - λμβ (190);
  - u_1 ∗ u_2 = u_1⊗u_2 + (u_1 + b_1)⊗(u_2 + b_2), which "croule si 2 = 0, b_1 = b_2 = 0" (192).

**Checks.**
- **SA02-R84-15 (independent re-proof).** The verdicts of the sweep 2 report (`sweep2/REPORTS/cote84_chi_split_extension_signs.md`) stand, and I re-derived them:
  - With the plus convention b'_i = b_i + χU_i, b'_1⊗b'_2 = b_1⊗b_2 + χU.
  - U'' = U + U' exactly: expand U' = (b_1 + χU_1)U'_2 + U'_1(b_2 + χU_2) + χU'_1U'_2. With the minus convention the residual is -2χ(U_1U'_2 + U'_1U_2).
  - The missing χ in the last line of 130 (SA02-K84-11).
  - The mixed conventions of 132 (SA02-K84-12).
  - "2 - χ = 1" on 140 (SA02-K84-13). With π_i(u_i) = χu_i the restriction gives (2χ - χ)λ_1λ_2u_1⊗u_2 = λ_1λ_2(u_1 ∗ u_2), with no condition. His own 152 is the identity -χ(1 - γχ) + 2χ(1 - γχ) + γχ² = χ, true for all γ, χ.
  - 156 and 158 are right: with π_i(x_i) = x_i - x̄_i the χ = 2 map is x_1⊗x_2 + x̄_1⊗x̄_2.
- **SA02-R84-16 (independent re-proof): the "signe étrange" of 134-136 is consistent; this settles the point left open in sweep 2 (B13).**
  - Let Φ: E → Hom^!(E, L), x ↦ [y ↦ ψ(x)y - ψ(y)x], be his map of 134 (it is g of 84/95). On L it is -id: Φ(u) = -u∘ψ.
  - With his rule (U_1 ∗ U_2) = -χU_1⊗U_2 (i.e. his formula for f_1 ∗ f_2 on 138 at λ_i = 0):
    Φ(u_1) ∗ Φ(u_2) = (u_1ψ_1) ∗ (u_2ψ_2) = -χ(u_1⊗u_2)∘ψ = Φ(χu_1⊗u_2) = Φ(u_1 ∗ u_2).
  - So the minus sign is exactly what makes Φ multiplicative on L_1 ⊗ L_2: the two input signs cancel and the output sign remains. His attribution of the sign to the -id is right.
  - Checked on L_1 ⊗ L_2 only, not for general f_i.
- **SA02-R84-17 (used and rechecked in this run).**
  - The formulas of 172, 176 and 192 are the identity of SA02-R84-08 and the computation of SA02-R84-13.
  - The norm on 190: with Tr u = -β and N u = c, N(λu + μ) = λ²c + μ² + λμ Tr u = λ²c + μ² - λμβ. So the doubtful "-|+" of 190 is "-", as sweep 1 decided (SA02-C1).
  - The pairing statements of 178-190 were read, not checked.

## The reused typescript (odd scans 125-193, and 84/5, 84/7)

- 84/5 and 84/7: typescript of Récoltes et Semailles, the passage on the "Éloge funèbre" with a note of 18 May.
- 84/125-193, all odd scans: typescript of Récoltes et Semailles, notes (106₁) of 3 October, (107) of 4 October, (108₁), (108₂) of 6 October and (110) of 11 October. They cover childhood, the parents, the yin-yang pairs (177: "dynamisme-équilibre / élan-assise / ardeur-persévérance ...") and "Le muscle et la tripe" (n° 106).
- They are documentary (SA02-6, SA02-7). I identified each page by its first and last lines; they were not read as mathematics.
- The stage-A dossier counts 35 leaves, folios 465-500 except 481 and 485, plus 475bis. It dates the essay to October 1984 and later annotations. My identification agrees.
- **Dating.** The mathematics of 84/124-192 is on the backs of typescript pages of October 1984, so it was written in late 1984 or later. The early sheets 84/4-6 share their leaves with the typescript of 84/5 and 84/7.

## The witnesses compared (97-193)

- **SA02-R84-18 (computation, token similarity per scan between K84 and the Pro packages).**
  - Typescript pages agree at 0.93-0.98.
  - Mathematical pages agree at 0.65-0.95. The lowest are 99 (0.61), 130 (0.65), 132 (0.71), 144 (0.74), 150 (0.75), 140 (0.76), 168 and 174 (0.76), 134 and 166 (0.77).
  - 130, 132, 136 and 140 were decided on the scans in sweep 2, and both witnesses carry the readings used above.
  - Scan 123 is in neither witness (no inventory row), nor are 1 and 8.
  - I read 2-111 in K84 and 112-193 in the Pro witness, with the K84 text of 97-111 compared by the measure only.

## The stage-A dossier (GPT-6 Astra, ChatGPT Pro mode): claims used and rechecked

- **SA02-R84-19 (used and rechecked in this run; refuted, refined SA02-K84-08).**
  - His margin on 84/27 says "Torseur sens fppf ou sens (ét), cela revient ici au =". It fails for non-étale A in characteristic 2.
  - Over k = F_2(t), take A = k[ε]/(ε²) and Q = t·N. Since N(a + bε) = a², the torsor {x : Q(x) = 1} is a² = t^{-1}, which has a point fppf-locally but after no separable extension. U_A ≅ μ_2 × G_a is not smooth.
  - The dossier's example, rechecked.
- **SA02-R84-20 (used and rechecked; refined SA02-K84-09).**
  - The Corollary of 84/36, as transcribed ("l'involution canonique est le seul automorphisme d'Alg de A qui induise -id sur A/O·1_A"), lacks the hypothesis his proof uses (84/35, 84/39): Θ is not the identity near the points of X_0.
  - Without it the Corollary fails: on A = F_2 × F_2 the identity and the swap both induce -id = id on A/O.
  - With it, the proof stands (SA02-R84-06). The dossier notes that the ink may carry the qualification; I did not view the scan.
- **Consistent with my reading, not rechecked further:**
  - the eight parity patterns of the associativity of 84/2 (SA02-R84-01);
  - Q_u = x ∧ u(x) (SA02-K84-02);
  - End(E)/A ≅ E ⊗_A E ⊗ (det E)^∨ and his withdrawal of "E ≅ End(E)/A" (84/29-32);
  - the non-representability of μ'_2 that he asserts on 84/49 (the dossier proves it);
  - ker(A → A_1 ⊗ A_2) = Ann(2, b_1, b_2)U (SA02-R84-10);
  - the dating of the typescript.
- **Not rechecked:**
  - the Z/4 example against multiplicativity in his five quasi-quadratic axioms (84/110);
  - the elliptic-curve counterexample to an endpoint-fixing comparison of E_1 ∨ E_2 and E_1 ∧ E_2;
  - the perfectness of the χ = 2 pairing.

## Links

- **Cote 77 (my SA04 reading, SA04-25).** The classification "2 régulier: (L, δ, T_0) with T_0² ≡ δ (4)" (84/49) is the (L, D, b_0) classification of quadratic covers of 77/53-64 and 77/74-86. Hunch H77-1 and package P-R4-1 therefore belong to SA02's prompt, with cote 84 as the fuller treatment (products, characteristic 2, the graded monoid).
- **SA01, cote 83** (`sweep3/SA01/readings/cotes83_93-92-134.md`):
  - the ∗-composition c = b_2²c_1 + b_1²c_2 - 4c_1c_2 is the product of 84/64, 84/90-91 and 84/172 (SA02-1);
  - the λ-split extensions of cote 83 are the χ-trivialized extensions of 84/66-87 and 84/124-170 (SA02-4);
  - the rank-4 Azumaya algebra End(E) appears on 84/28-34.
- **Within SA02:**
  - the graded monoid of 84/2 (SA02-14) is the discriminant data of the product (84/54-56);
  - χ = 2 specializes SA02-4 to SA02-1 (84/80-87).

## What was not reached (exactly)

- Every transcribed mathematical scan was read: 2-122 and the even scans 124-192.
  - 2-111 in K84; 112-193 in the Pro witness, with K84 compared by measure.
  - The typescript scans (5, 7 and the odd scans 125-193) were identified by their opening and closing lines, not read.
- Scans 1, 8 and 123 have no inventory row in either witness and were not viewed.
- No scan was viewed in this reading. The readings of 120, 130, 132, 136 and 140 rest on the sweep 2 scan checks.
- Read but not checked step by step:
  - the w, Arf and c_1 formulas of 84/2;
  - 84/111-112 (beyond the axioms);
  - the universal situation of 84/122;
  - the F_ij tables of 154-166;
  - the pairing of 178-190;
  - the faithful-flatness claim of 84/92-93.
- The doubts files and audits were used only by counts. The Pro notes were consulted only through the sweep 2 reports and the stage-A dossier.
