# SA12 research packages (sweep 3)

The SA12 lead, a65dbdc241d1a129a (Claude Opus 5.5 at effort max), 19 Nov 2026. The four packages go into the one prompt `pro_prompt_builds/RESEARCH_SA12/PROMPT.md`, in this order. RP-SA12-1 is the main question.

## RP-SA12-1 (main). His conjectures on the cohomological dimension of affine schemes (31/070-087, 31/023)
**Questions.** Each is to be proved or refuted. "Bon" is read as quasi-excellent, and the noetherian case without quasi-excellence is decided separately.
- **(a) 1° (31/085).** X is an affine integral scheme with generic point x, and ℓ is invertible on X. Is cd_ℓ(X) ≤ cd_ℓ(k(x))? His margin: does equality hold for every sufficiently small nonempty affine open U?
- **(b) 3° (31/085).** If some prime ℓ' is invertible on X, is cd_ℓ(X) ≤ cd_ℓ(k(x)) for every prime ℓ?
- **(c) 2° (31/085).** If ℓ is neither invertible nor nilpotent on X, is cd_ℓ(X) ≤ sup(cd_ℓ k(x), δ(V(ℓ)) + 3)? Here ℓ^{δ(k)} = [k : k^ℓ], and δ(Z) is the sup over the maximal points of Z.
- **(d) 4° (31/085).** A is a henselian local integral quasi-excellent ring with char K = 0. Is cd_ℓ(U) ≤ dim A + δ(k) + cd_ℓ(k) for every affine open U of Spec A and every prime ℓ?
- **(e) 31/082.** X is noetherian affine with ℓ invertible, and n = sup_x[cd_ℓ k(x) + dim O_{X,x}]. Is cd_ℓ(X) ≤ n? Is n the sup of cd_ℓ(U) over the affine opens U?
- **(f) The "Th" of 31/080.** Y = Spec A is strictly local, X is affine of finite type over Y, X₀ is the closed fibre, X' = X ×_Y (Y − {m}), and ℓ is prime to the residue characteristic. Is cd_ℓ(X) ≤ sup(dim X₀, dim X' + 1)? For X not affine, is the bound sup(2 dim X₀, 2 dim X' + 1)?
- **(g) 31/070.** Is cd_ℓ K ≤ dim A for every noetherian strictly henselian local domain A, ℓ invertible? (His words: "probablement tjrs. le cas, du moins si X est 'bon'".)
- **(h) The margin of 31/070.** A is a noetherian henselian local domain, ℓ ≠ char K and cd_ℓ k < ∞. Is cd_ℓ K ≥ dim A + cd_ℓ k?
- **(i) 31/023.** For a noetherian local domain A and r = 2, is the restriction to regular A in exception b) needed ("cette restriction est-elle inutile ???")?

**Why it matters.** These are his own conjectures, written as a programme ("Conjectures sur la cohomologie des schémas affines") around Artin's theorems of SGA 4 X and XIV. A complete answer places his programme against what Gabber later proved, and settles the cases not covered.

**Rests on.**
- 31/019-023 (Artin's theorems; SA12-44);
- 31/063-083 (the φ-criterion, his sequence of theorems 1_n, 2_n; SA12-38, SA12-39);
- 31/002-009 (cd_p of fields of characteristic p, the p-degree; SA12-41).

**Strongest reduction known to us** (locators unverified):
- Gabber's affine Lefschetz theorem and his bound for fields: Illusie-Laszlo-Orgogozo, Travaux de Gabber (Astérisque 363-364, 2014), Exp. XV and XVIII-A;
- Gabber-Orgogozo, "Sur la p-dimension des corps", Invent. Math. 174 (2008), for the ℓ = p field bounds;
- Artin-Verdier and Milne, Arithmetic Duality Theorems II, for Spec O_K and its opens;
- the checks of sweep 3 (STUDY.md §§24-26).

**Material.** The transcriptions of cote 31 (Pro MPL_31_002-051; Codex/Work K31-01..03, with notes and math notes), readings/c31_lead.md and HUNCHES H1-H6.

## RP-SA12-2. Birational invariance of Pic^τ in characteristic p (29/071-077)
**Questions.**
- **(a)** k is algebraically closed of characteristic p > 0, and f: X → Y is a dominant birational morphism of integral proper k-schemes, X normal and Y regular. Is Pic^τ_{Y/k} → Pic^τ_{X/k} an isomorphism of group schemes? Decide also under "X normal 'sur k'" and "Y projectif" (his margins).
- **(b)** The Question of 29/075. For K/k finitely generated, is dim H¹(X, O_X) bounded as X runs over the proper models of K normal over k? Equivalently, is the inductive system of the Pic^τ essentially constant?
- **(c)** Prove the bound n(K/k) on dim Pic over normal models (29/076-077) without the fundamental group, as he asks.

**Why it matters.** The theorem is proved on his pages in characteristic 0, and in characteristic p on points and on H¹, without resolution. Only the infinitesimal step is missing.

**Rests on.** 29/071-077 and readings/c29a.md (the step-by-step check, the α_p ⊂ α_{p²} gap, the l ≠ p correction).

**Strongest reduction.** The theorem holds if H²(Y,O_Y) → H²(X,O_X) is injective, which by Leray means H⁰(Y, R¹f_*O_X) → H²(Y,O_Y) is zero. For smooth X it holds by Chatzistamatiou-Rülling (locator unverified).

## RP-SA12-3. Pointed torsors and the fundamental group scheme over a base (29/124-143, 29/164-172)
**Questions.**
- **(a)** S is reduced, connected and noetherian, with a point a, and C is a category of finite flat S-groups as on 29/141. Find the exact class of pairs (C, morphisms) for which Proposition 4 holds, and prove it. In particular:
  - C = {G₀ ×_k S}, with morphisms over k and with morphisms over S;
  - S normal versus S non-normal.

  The cusp (29/139) refutes the statement with S-morphisms over a non-normal base. Is it true for every normal S, with all S-morphisms?
- **(b)** The question of 29/131. f: X → S is proper flat with a section, f_*O_X = O_S universally, and G is finite étale (then finite flat). Is the functor of pointed G-torsors on X_T representable by an étale, quasi-finite, separated S-scheme?

**Why it matters.** This is his construction of 1959, before Nori: the "vrai" fundamental group. Its relative form over a base is the subject of later work on fundamental group schemes over Dedekind and general bases.

**Rests on.** 29/124-143 (readings/c29a.md §§124-140; readings/c29b_c31.md items 1-2) and 29/164-172 (item 10).

**Strongest reduction.**
- The étale case is proved, and the case where the equalizer is admissible (sweep 3).
- Reader B shows that the whole weight lies on the uniqueness of pointed maps from a minimal P.

## RP-SA12-4. His open questions on finiteness and descent for π₁ (cote 29), and two local questions (cote 31)
Each is to be proved or refuted.
- **(a) 29/061.** X is normal and complete over an algebraically closed field, and Y ⊂ X is closed. Is π₁(X − Y), modulo the closed normal subgroup generated by the wild inertia groups at the codimension-1 components of Y, topologically of finite type?
- **(b) 29/066.** For X connected and normal of finite type over an algebraically closed field and Y ⊂ X closed of codimension ≥ 2, is Ker(π₁(X − Y) → π₁(X)) topologically of finite type? And is π₁(Z − Y) topologically of finite type for Z proper, not projective, of characteristic p, with Y of codimension ≥ 2?
- **(c) 29/098.** What is Π₂^t(Spec ℤ − S), and more generally Π₂^t of X₀ − D'₀ for X₀ = Spec O_K − S? Is Spec ℤ − S of type K(π,1) for tame coefficients?
- **(d) 29/116.** char k = 2, dim X odd, and a Lefschetz pencil that is not generic. Are the vanishing cycles conjugate under π₁(D − D^v)?
- **(e) 29/180.** S, S' are noetherian and S' → S is proper surjective, not flat. Is every descent datum on a constant G_{S'} effective?
- **(f) 31/044.** For a wildly ramified finite Galois extension of a henselian DVR, is H¹(G,O*) → H¹(G_i,(O/m)*) bijective? And the same for GL(n)?
- **(g) 31/101.** G is locally constant on the complement V of a smooth divisor in X smooth over S. Under what necessary and sufficient condition are the R^i h_* G locally constant on S?

**Rests on.** readings/c29a.md and c29b_c31.md (the items named), and readings/c31_lead.md items 6 and 16.
