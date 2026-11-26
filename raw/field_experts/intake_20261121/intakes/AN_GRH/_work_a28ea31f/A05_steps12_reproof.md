# A05, Steps 1-2: an independent re-proof

By Claude Opus 5.5 at effort max (agent a28ea31fa17dd65e1), 22 Nov 2026, for the full intake of AN_GRH. The finding is
by GPT-6 Astra (ChatGPT Pro mode), AN_GRH final, `AN_GRH.tex` lines 628-916.

I wrote the argument out myself, step by step. The order of ideas follows the run's, but every sub-claim the run states
in one line is proved here or reduced to a named standard result. This is H07's gate. Steps 3-6 are not part of this
re-proof.

Notation, as in A05:
- C is a proper smooth curve of genus g ≥ 2 and r ≠ p is a prime;
- Λ = π_1(C − P), Γ = π_1(C^2 − diag), B_0 = π_1(C) and Δ = B_0^{(p')};
- F = Λ^{(p')} and E = Γ^{(p')}, with K_F = ker(F → Δ) and K_E = ker(E → Δ × Δ);
- N(K) is the smallest closed normal subgroup of K with pro-r quotient (characteristic in K);
- F_c = F/N(K_F) and E_c = E/N(K_E).

## Step 1: 1 → F_c → E_c → Δ → 1 is exact (A05.1)

**(a) The topological sequence.** The second projection C^2 − diag → C is a locally trivial fibration with fibre
C − {pt} (Fadell-Neuwirth). Since π_2(C) = 0 for g ≥ 1 and the fibre is connected, the homotopy sequence gives
1 → Λ → Γ → B_0 → 1.

**(b) Lemma.** Let 1 → L → H → B → 1 be exact, with L free of finite rank d ≥ 2, and suppose H acts on
H_1(L, F_r) = L/[L,L]L^r through a finite r-group. Then L^{(r)} → H^{(r)} is injective.

Proof.
1. Conjugation gives a continuous action of H on L^{(r)}. A finitely generated pro-r group has a basis of open
   characteristic subgroups U_n, and Aut(L^{(r)}) = lim Aut(L^{(r)}/U_n).
2. For a finite r-group Q, the kernel of Aut(Q) → Aut(Q/Φ(Q)) is an r-group. By Burnside's basis theorem it acts
   freely on the |Φ(Q)|^d tuples lifting a fixed basis of Q/Φ(Q): an automorphism that fixes a generating tuple is the
   identity.
3. Q_n = L^{(r)}/U_n has Q_n/Φ(Q_n) a quotient of H_1(L, F_r), on which H acts through an r-group by hypothesis. So
   the image of H in Aut(Q_n) is an r-group, an extension of an r-group by an r-group.
4. Hence the closure A of the image of H in Aut(L^{(r)}) is pro-r, and H → A factors through H^{(r)}.
5. On L the action is by inner automorphisms. So L^{(r)} → H^{(r)} → A is the map x ↦ Inn(x), whose kernel is the
   centre of L^{(r)}.
6. A free pro-r group of rank ≥ 2 has trivial centre; its centralizers of nontrivial elements are procyclic (Ribes-
   Zalesskii, Profinite Groups, free pro-p groups; the run's own Magnus-embedding argument also proves it).
7. So the composite is injective, hence L^{(r)} → H^{(r)} is injective. As a closed embedding, every finite r-quotient
   of L is dominated by a finite r-quotient of H. ∎

**(c) Every finite quotient of F_c is seen in E_c.**
1. Let Q be a finite quotient of F_c, R the image of K_F (an r-group, because F_c kills N(K_F)) and A = Q/R. A is a
   quotient of F/K_F = Δ, so it defines a proper Galois cover a: C' → C, étale with group A.
2. Put Y = (C' × C') − ∪_{σ∈A} Γ_σ, where Γ_σ = {(σx, x)}. These graphs are pairwise disjoint, because A acts freely.
   Y → C^2 − diag is Galois with group A × A, so H = π_1(Y) is normal in Γ with Γ/H = A × A.
3. The second projection Y → C' is a locally trivial fibration with fibre V' = C' − a^{-1}(a(c')). Its group is
   L = π_1(V'), free of rank 2g(C') + |A| − 1 ≥ 4.
4. In Γ, Λ ∩ H = ker(Λ → A) = L: Λ maps to B_0 × {1} in B_0 × B_0.
5. The hypothesis of the lemma holds.
   - The monodromy of π_1(C') on H_1(V', F_r) is trivial on the quotient H_1(C', F_r), because the compactified
     family is the product C' × C' → C'.
   - It is trivial on the boundary classes. Each puncture σ(c') returns to itself along a closed loop of c', so the
     punctures are not permuted.
   - So it is unipotent, I + N with N: H_1 → ⟨boundary⟩ and N(boundary) = 0: an elementary abelian r-group.
   - L acts on its own homology trivially.
6. The image of L in Q is ker(Q → A) = R, an r-group. By the lemma there is a normal T ⊂ H of finite r-power index
   with T ∩ L ⊂ ker(L → R).
7. Let T' = ∩_{γ∈Γ/H} γTγ^{-1}. It is normal in Γ, H/T' is an r-group, and Γ/T' is an extension of A × A by H/T', of
   order prime to p. So Γ → Γ/T' factors through E.
8. K_E maps into ker(Γ/T' → A × A) = H/T', an r-group, so the map factors through E_c.
9. On the fibre: Λ ∩ T' ⊂ Λ ∩ H ∩ T = L ∩ T ⊂ ker(L → R) = L ∩ ker(Λ → Q). So the kernel of Λ → Γ/T' lies in
   ker(Λ → Q).
10. Hence every finite quotient of F_c factors through E_c, and F_c → E_c is injective (both are profinite, and F_c is
    the limit of these quotients).

**(d) The rest of the sequence.**
- Pro-(p') completion is right exact, so F → E → Δ → 1 is exact.
- K_F maps into K_E, so N(K_F) maps into N(K_E). Hence F → E_c factors through F_c.
- N(K_E) ⊂ K_E ⊂ ker(E → Δ, second factor), so E_c → Δ is defined and onto, and ker(E_c → Δ) is the image of
  ker(E → Δ) = im F, which is im F_c.
- With (c), (A05.1) holds for complex curves.

**(e) Characteristic p.**
- Lift C, with P, to W(k) (SGA 1, III, Cor. 7.4; the point lifts by smoothness).
- The prime-to-p geometric groups of C − P, of C^2 − diag (a smooth proper surface with a smooth divisor; every
  prime-to-p cover is tame along it) and of C specialize isomorphically and functorially (SGA 1, XIII, Cor. 2.9, §2.10,
  Lemma 2.11).
- The subgroups K_F, K_E and N(·) are defined group-theoretically and functorially, so (A05.1) holds for the étale
  groups.
- N(K_F) and N(K_E) are characteristic in normal subgroups of the arithmetic groups, so the arithmetic quotients exist
  and form extensions of the unchanged G_k.
- **Holds.**

## Step 2: equal sections transport the cusp (A05.2, A05.3)

**(a) The diagonal decomposition group 𝒟 is an extension of Π_C by the full Z_r(1).**
1. Along the smooth divisor diag ≅ C in C^2, the prime-to-p covers of the complement are tame. By Abhyankar's lemma on
   Kummer charts (SGA 1, XIII, Prop. 5.2), the decomposition group of diag in the limit is an extension of π_1(diag),
   whose image is Π_C mapped diagonally to Π_C ×_{G_k} Π_C, by the image of tame inertia Ẑ'(1). In E_c this inertia
   image is a quotient of Z_r(1), because the rest is killed by N(K_E).
2. It is the whole of Z_r(1).
   - In Λ = ⟨a_i, b_i⟩ the puncture loop is c = ∏[a_i, b_i].
   - The map a_1 ↦ 1 + e_12, b_1 ↦ 1 + e_23 (all other generators ↦ 1) into the Heisenberg group UT_3(Z_r) sends c to
     1 + e_13, of infinite order.
   - UT_3(Z_r) is pro-r, so prime to p, and the map factors through F. Its restriction to K_F has pro-r image, so it
     factors through F_c.
   - So c has infinite order in F_c, and, by Step 1, in E_c. The diagonal meets each fibre transversally in one point,
     so the fibre's cusp inertia is the diagonal inertia.
   - I checked the commutator by hand: [1 + e_12, 1 + e_23] = 1 + e_13.
3. Transversality with multiplicity one makes the cusp group of the fibre over P the full inverse image of s_P(G_k) in
   𝒟.

**(b) β.**
1. Suppose s_Q = γ s_P γ^{-1} with γ ∈ Δ_C. Lift γ to γ̃ ∈ 𝒟; since 𝒟 maps diagonally, pr_1(γ̃) = pr_2(γ̃) = γ.
2. Conjugation by γ̃ maps G_P = pr_2^{-1}(s_P(G_k)) onto pr_2^{-1}(s_Q(G_k)) = G_Q. These are the fibre groups over P
   and Q; their identification with the cuspidally pro-r groups of C − P and C − Q uses Step 1.
3. It maps the cusp group pr_2^{-1}(s_P(G_k)) ∩ 𝒟 onto pr_2^{-1}(s_Q(G_k)) ∩ 𝒟, and acts on the first coordinate by
   Inn(γ).
4. Choose δ in the geometric fibre group over Q with pr_1(δ) = γ^{-1}. This is possible because F_c → Δ is onto.
   Conjugation by δγ̃ is then an isomorphism G_P → G_Q over id_{Π_C}, preserving cusp conjugacy classes. This is
   (A05.3).
- **Holds.**

## Outcome

Steps 1-2 hold, by an independent re-proof. The standard inputs are:
- Fadell-Neuwirth;
- Burnside's basis theorem;
- the trivial centre of free pro-r groups of rank ≥ 2;
- SGA 1, III 7.4, XIII 2.9-2.11 and XIII 5.2;
- Abhyankar's lemma.

No gap was found. Two places in the run's text are terse but correct:
- the claim that the image of H in Aut(L^{(r)}) has pro-r closure, which needs the Frattini-kernel fact at every
  characteristic level;
- the inclusion Λ ∩ T' ⊂ ker(Λ → Q), which needs Λ ∩ H = L.

I would write both out in a publication.
