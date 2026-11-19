# SA23: research packages (sweep 3, wave 1)

Each package is a question to settle: proved or refuted, with complete proofs. The places are his pages; the readings give the details.

## RP1. Formal smoothness for the discrete topology, and Cohen lifts (cote 22; the main question)
- **(a) His question 2.** For a field k of characteristic 0 and A = K[[t_1..t_n]] (n > 0) with Ω_{K/k} finite-dimensional, is A formally smooth over k for the discrete topology? Equivalently, is Ω_{A/k} projective (free, A being local)? Start with Q[[t]] over Q.
  - He presumes "jamais" (22/023). His Proposition settles the case of infinite-dimensional Ω_{K/k} (22/024-025).
  - **The case p > 0.** He says yes with a finite p-base and is "pessimiste" otherwise (22/022). Settle the case without a finite p-base.
- **(b) His open problem on 22/014.** Over a square-zero thickening A → A_0, does every Cohen algebra B_0 (adic, condition P, formally smooth) over A_0 lift to a Cohen algebra over A? He proves it only for separable residue extensions (4.10).
- **(c) His questions 3 and 4 (22/020-021).**
  - Openness of the locus of formally smooth fibres for flat A → B of noetherian rings: for which classes, and with a counterexample where it fails.
  - Openness of the flat locus for arbitrary noetherian A → B, not of finite type: prove or refute.

## RP2. Deligne's lemma (1966): the Cohen factorization and its open point (cote 23, 060-063)
- **Prove the lemma in full.** For a local homomorphism A → B of noetherian local rings with B complete, B is a quotient of a local, flat A-algebra C with C ⊗ k regular and gr(C ⊗ k) → gr(B ⊗ k) bijective in degrees 0 and 1. Also prove the pro-isomorphism "lim" Tor_p^A(N, M)/m^k ≅ "lim" Tor_p^A(N/m^kN, M).
- **Settle Deligne's open point.** Every algebraic extension K/k is k[T_α]/(P_i) such that, for every artinian A with residue field k, the lifted relations give a flat A-algebra A[T_α]/(P̃_i). Prove or refute.
- **Compare** with the minimal Cohen factorizations of Avramov, Foxby and Herzog (1994).

## RP3. Regular immersions (cote 23, 053-054)
- **His Koszul-regular notion.** Prove everything he claims for it: quasi-regularity; independence of the generating system; fpqc descent; composition; the transitivities of EGA IV 19.1.5 (iii) without noetherian hypotheses.
- **A counterexample.** Give a local ring with (x, y) regular and (y, x) not.
- **His characterization.** Prove the characterization of regular ideals by Sym(I/I²) ≅ gr and ∧(I/I²) ≅ Tor (Deligne's 0_IV 15 proposition).

## RP4. The errata to EGA in the letters (cote 23, 044-065)
Settle each item as true or false in the printed text, with a proof or a counterexample:
- **0_IV:** 19.3.12; 19.5.5 b) ⇒ c) without separation; 19.5.6 (ii); 20.4.6 (the sign of dx); 20.4.13 (iv).
- **IV:** 16.1.5 (Deligne: "J'ignore si la proposition est vraie"); 16.1.6 (is the kernel of A → B finitely generated when B is of finite presentation?).
- **III:** 4.3.6 (K' = K ⊗_A Â).
- **Lê Dũng Tráng's errata:** 20.1.3-21.6.2.

## RP5. The discriminant over a base (23/006)
- **The corrected statement.** δ is a section of M̌^{(r+1)(k−1)^r} ⊗ (det E)^{k(k−1)^r}, and P^r_φ is smooth over S iff δ is invertible.
- **The integral normalization.** Settle it, including the primes dividing the naive discriminant.
- **The elliptic check.** Rederive ω^{⊗12} for the plane cubic of 23/005.

## RP6. "Foncteur différentiel d'ordre ≤ n" (23/039-041)
Characterize the functors on smooth S-schemes of relative dimension d (with étale maps) that come from objects with an action of the jet group G^{d,n}. This is an algebraic natural-bundle theorem. Prove that, under locality and finiteness hypotheses to be stated, every such functor is of finite order and associated to a G^{d,n}-object.

## RP7. Graded flatness (23/096-098)
Under his "bonnes conditions" (a, b''), prove or refute:
- C flat over K ⇒ B flat over A;
- A and C flat over K ⇒ B flat over K;
- his other implication.

## RP8. Cote 1: Lidskii and the determinant Δ
- **(a) Lidskii.** Write the complete proof of Lidskii's trace formula from his steps (71, 79, 89, 111-112) and identify the gap on 71.
- **(b) The determinant.** Prove Δ(AB) = Δ(A)Δ(B) for all operators in his setting, not only invertible ones, including the case A = λ + B with T(1) infinite. Settle his question Δ(B*HB) ?= Δ(A*A)Δ(B*B).

## RP9. Cote 161-2: accessible categories and the classifying topos
- **(a) Accessible categories.** Prove his equivalences for "(modifié 9.4 ?)" accessible = Ind_π(C) and for the axiom c) of cardinal filtrations, with the exact cardinal hypothesis (π'^π = π').
- **(b) The classifying topos.** Prove the existence and universal property of his topos modulaire relative to a base topos X (161-2, 112), using the 2-fibred products of 22.

## RP10. Cote 161-5: the crystalline realisation
- **(a) Extension and uniqueness.** Can T_cr, with its F-isocrystal, filtration and Hodge comparison, be extended from Barsotti-Tate groups up to isogeny to the Tannakian category they generate in the Hodge-Tate category, as a ⊗-functor? Is it unique up to unique isomorphism?
- **(b) The cohomology.** Is H^1(Γ, G'(S)) → H^1(π, G'(S)) injective, or with trivial kernel?
- **Answer** both in today's terms (crystalline representations, D_cris).

## RP11. Cote 26: the "Problèmes-types à résoudre" a)-j)
For each problem, give its state with exact references. Where it is open as he posed it, settle it: in particular j), the theorem of the square for non-projective abelian schemes, and i), the simplicity of the formal moduli of an abelian variety.

## RP12. Cote 162-5: his version of Quillen's theorem (notes of 6.9.68)
Part L of the prompt: the Θ-Lie algebras (Lie algebroids) and the equivalence, in char 0, of adic formal categories with flat Ω and De Rham complexes. Prove the correct statement with the missing condition, since δ_1δ_0 = 0 alone does not give δ² = 0.
