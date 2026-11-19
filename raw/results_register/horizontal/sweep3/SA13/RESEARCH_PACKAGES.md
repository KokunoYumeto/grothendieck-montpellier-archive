# SA13 research packages (questions for the research prompt RESEARCH_SA13)

Written by the SA13 lead, agent a84c887cf408574ed (Claude Opus 5.5 at effort max), on 19 Nov 2026. Each package is a question to settle, proved or refuted with complete proofs.

## RP-SA13-1 (main). His injective-dimension theorem (33/170-178)

**Question.** Let X be of finite type over a separably closed field k with dim X ≤ n. Let A = Z/NZ with N invertible on X. Prove or refute both of the following.
1. His question (33/174): every sheaf of A-modules with injective (equivalently flat) stalks is a filtered colimit of constructible sheaves with injective stalks.
2. His Theorem (ii) (33/172): Ext^i(F, C) = 0 for all i > 2n, for every constructible F and every C with injective stalks.

If (ii) holds, determine whether it extends to all F.

**Known.**
- The constructible case: the 2n bound via the codimension ≥ j/2 support of ℰxt^j.
- Print, SGA 5 I 1.5: ≤ 4n.

**Rests on.** SA13-17 and SA13-18. The reading c33_c36_c39 decided on the scan that (i) concerns the sheaf ℰxt.

## RP-SA13-2. The strong form of Théorème 7.1 of "Le théorème de Griffiths par voie algébrique" (36/10-27)

**Question.** Settle the strong form: Frobenius elements of G₀ realize every prescribed trace on all of V₀. Then settle its consequences, Cor. 7.2 and "G₀ n'est pas un p-groupe".

**Known.** The weak form, SGA 7 XXI 1.4 (non-nilpotence), is proved, and Cor. 7.3 follows from it.

**Rests on.** SA13-69 and SA13-6, with the vanishing-cycle theory of cote 34 (SA13-28).

## RP-SA13-3. The invariant-cycle kernel (36/60-71)

**Question.** For a regular proper model X of a smooth projective variety over a strictly henselian DVR, with special fibre X₀ = Σ d_i D_i and d = gcd(d_i), is Ker(Γ → NS(X₀)) = Z/dZ in every relative dimension? This is his "demander Raynaud si Ker est donc Z/dZ".

**Also settle.** The index statements of 36/61 a): d^t = gcd(μ_i d_i); and d^t = p^h·d, with h = 0 for a perfect residue field.

**Rests on.** SA13-48, SA13-49 and SA13-41.

## RP-SA13-4. The "théorème de 1/2 continuité" (27/28-37)

**Question.** Prove or refute the full theorem for smooth separated group schemes of finite presentation over any base:
- ρ_aff, d, ρ_n, ρ_na and ρ_u are upper semicontinuous;
- ρ_ab, ρ_ab + ρ_r and ρ_ss are lower semicontinuous.

Include his "lemme à rapporter" (27:34) and the steps ③ and ④ (27:37).

**Rests on.** SA13-58, together with the weight argument shared with SA13-50 and SA13-27.

## RP-SA13-5. The étale scheme of irreducible fibre components (41/4-14)

**Question.**
1. Is his valuative condition (i) necessary and sufficient for the existence of an étale, not necessarily separated, modular M?
2. Under what conditions is the functor of "sections monisantes" representable by an étale scheme or by an algebraic space?

Prove the Theorem of 41:9 in full.

**Rests on.** SA13-67.

## RP-SA13-6. Networks of local rings (42/2-7)

**Question.** Is ρ fully faithful on S-préschémas locally of finite type over a locally noetherian S, including the non-separated ones? Which finiteness is needed on the target (his margin question)?

**Rests on.** SA13-68.

## RP-SA13-7. Tori of the Cremona group (28/5)

**Question.**
1. Prove the corrected equivalence of 28:5: every G_m^(n−d) ⊂ Cr_{n,k} lies in a G_m^n ⇔ every K/k of transcendence degree d with K(t₁..t_{n−d}) pure is pure.
2. Determine the pairs (n, d) for which it holds over C.

**Rests on.** SA13-59 (Demazure's theory).

## RP-SA13-8. Smaller questions on his pages

1. 33/110, "peut-être vrai dès que Y est noethérien": settle it with the candidate counterexample of hunch 8.
2. 32/37 margin: does local acyclicity of g suffice for g'^*Rf^! ≅ Rf'^!g^*?
3. Cote 39:
   - Does f′ (henselian) imply f under a)-e) (39/4)?
   - Faithful flatness of S_n over A_n (39/13).
4. 36/29-34: prove the perfectness of the pairing on the torsion of [M → G] as on the pages, and identify it with the Weil pairing of the dual 1-motive.
