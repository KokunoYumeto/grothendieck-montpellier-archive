# Post-checkpoint-05 investigation: whole prime-to-p Brauer finiteness

Date: 19 November 2026. Part D independent argument, outside frozen checkpoint files. This note is initially a proof of the abstract descent upgrade conditional on the prime-uniform smooth unit-cup source theorem being checked by Part B. It is not yet an integrated main statement.

## 1. Exact algebraic upgrade

Put R=Z[1/p] and D=⊕_{ell≠p} Q_ell/Z_ell, equivalently Q/Z[1/p]. For any finite-type F_p-scheme S put A_S=H²_et(S,G_m) tensor R and let C_S be the image of units(S) tensor D under the arithmetic cyclic-cup map. The cup map is the sum of its prime components. Its image is a divisible torsion subgroup, hence an R-submodule of A_S.

Every input in the existing arbitrary-base descent argument, except the smooth unit-cup cokernel, is already prime-uniform:

1. The full-H² kernel K for the chosen finite-type perfected v-cover is finitely generated over Z[1/p] itself, by Bhatt–Scholze plus Jaffe. No ell-dependent localization is necessary.
2. The unit-cup kernel on any finite-type scheme is finite for D, not merely finite on each ell-primary subgroup. The normal-projective valuation matrix is a single integral full-column-rank matrix. Its Smith invariant factors are fixed nonzero integers. The kernel on D is the direct sum of their finite prime-to-p torsion groups, and so is finite, supported at finitely many primes.
3. The middle homology of the unit-lattice complex tensored with D is finite. The underlying finite free integer-lattice complex is rationally exact in the middle. Smith normal form gives a bound by a finite torsion group, again with only finitely many primes. This is a uniform assertion, not a sum of unrelated ell-adic finiteness assertions.
4. For smooth quasi-projective T, A_T=Br(T)[p′], and A_T[h] is finite for each fixed integer h prime to p by the Kummer sequence and finiteness of H²_et(T,mu_h). A global finite-cotype claim for the direct sum over all primes is unnecessary.

Assume Part B's prime-uniform smooth theorem: C_T has finite cokernel in A_T for every smooth quasi-projective T under the universal surface-divisor Tate hypothesis. Choose N annihilating that finite cokernel, M annihilating the finite unit-cup kernel on T_1, and L annihilating the finite unit-lattice middle homology. The earlier exact calculation then gives

    LMN a - c_S(v) ∈ K

for each a∈A_S and some v∈units(S) tensor D. All integers are fixed independently of a and of ell.

Consider A_S/C_S→A_T/q*C_S. Its kernel is (K+C_S)/C_S, a finitely generated R-module. Its image is killed by h=LMN. Since q*C_S is divisible, the map A_T[h]→(A_T/q*C_S)[h] is surjective: for a class represented by b with hb∈q*C_S, choose c∈q*C_S with hc=hb and replace b by b-c. Thus the target's h-torsion is finite by item 4. (The p-power factor of h can be removed because p is invertible on these groups.) The image is consequently finite, proving A_S/C_S finitely generated over R.

The torsion of A_S is exactly Br(S)[p′], because localization cannot turn an originally nontorsion element into torsion. Since C_S is torsion, torsion of A_S/C_S is exactly Br(S)[p′]/C_S. A finitely generated torsion Z[1/p]-module is a finite abelian group. Thus unit cups generate the whole prime-to-p Brauer group up to a finite cokernel. In particular (H²_et(S,G_m)/torsion) tensor Z[1/p] is finitely generated.

If f:X→S identifies global units, f*C_S=C_X, so the whole prime-to-p relative Brauer cokernel is finite. This applies to every smooth proper morphism with geometrically connected fibres, in every relative dimension, over arbitrary finite-type bases. The surface-pencil converse is unchanged, so this strengthening has the same universal surface-Tate gate.

## 2. Proper-source primary literature found

Independently opened Cadoret–Hui–Tamagawa, *Q_l- versus F_l-coefficients in the Grothendieck–Serre/Tate conjectures*, author PDF https://webusers.imj-prg.fr/~anna.cadoret/GST.pdf. Exact author-version Corollary 1.4, p.4, states the equivalence between divisor Tate for every ell≠p and finiteness of the invariant prime-to-p geometric Brauer group. The following paragraph explicitly says that over finite fields this is Tate's Proposition 4.3 and that divisor Tate is ell-independent there. Web reference turn644289366view0. Older citations call the corollary 1.5; do not transfer that number to this author version. Full §7 proof is being checked separately.

Also independently read the complete proof of Colliot-Thélène–Skorobogatov author-draft Proposition 15.1.1, pp.312–314, and Lemma 15.1.2. The Néron–Severi intersection discriminant gives integral equivariant splitting of the divisor lattice at all but finitely many primes, and Gabber's torsion theorem supplies the corresponding mod-ell splitting. This is sufficient for a direct finite-field Frobenius determinant proof of the uniform proper input. The draft already exists in the frozen source archive; no frozen file has been modified.

Part B independently found Qin, arXiv:2012.01681v2, Theorem 1.2 and Theorem 5.2, including smooth nonproper geometric Brauer finiteness. Part B is checking those complete proofs and the arithmetic unit-cup consequence. That source has not yet been independently opened by Part D at the time this paragraph was written.

## 3. Completed independent source and written-proof checks

At 06:32 UTC I completed the independent full read of Part B's `pending_post05_b3_prime_uniform_b.md`. Its smooth prime-uniform theorem passes in its exact written scope. I checked the arithmetic-unit term through H²(Gamma,E)≅H²(Gamma,N)≅N_Gamma tensor Q/Z, the surjection from invariant arithmetic units using Hilbert 90, finiteness of H¹(Gamma,Pic(Ubar)) using the finite boundary subgroup of Pic⁰, the two-step Hochschild–Serre filtration, and the final bounded quotient by a divisible subgroup. The trace-to-Brauer argument uses generic-zero Kummer lifts, so no unstated integral divisor-pushforward theorem is needed. Constant-field extension rescales the character by a nonzero integer, which leaves its divisible unit-cup image unchanged.

I also independently opened Riou's primary article *Classes de Chern, morphismes de Gysin, pureté absolue*, Astérisque 363–364 (2014), Exposé XVI, pp.301–349, at https://www.numdam.org/item/AST_2014__363-364__301_0.pdf. Exact passages read: Proposition 2.5.13 and Remark 2.5.14, Corollary 3.1.2, and the complete proofs of Lemmas 3.5.8–3.5.10, printed pp.323 and 333–335. Web references turn673303881view0, turn452058661view0–3. The finite-coefficient setup is explicit at the beginning of the article. Ample-line-bundle hypotheses are respected by quasi-projective source and target. Lemma 3.5.9 is situated in an invertible-degree application, but its scalar calculation, reduced to the dense finite locus, does not invert the degree; Proposition 2.5.13 supplies the finite-flat trace normalization including inseparable multiplicity. Thus the needed identity is valid for every n prime to p, even when n shares factors with the alteration degree.

Independently read Colliot-Thélène–Skorobogatov author-draft Lemmas 3.5.2–3.5.3 and Theorem 3.5.4 with their complete proofs, pp.88–89. These supply regular full-H² torsion and injection of the regular Brauer group into the function-field Brauer group. The latter makes the trace on H²(mu_n) descend to Brauer n-torsion because Kummer classes of line bundles become zero at the generic point.

Qin's primary v2 has now also been independently archived and read through its complete internal chain: Lemmas 3.2–3.4, Propositions 4.2–4.3, Theorem 4.4, Lemma 5.1, and Theorem 5.2, author pp.8–15. Its fixed annihilating Frobenius polynomial and splitting at eigenvalue 1 control almost-all-prime coinvariant torsion; the geometric H³ invariant theorem removes the other term, and the arithmetic Brauer quotient becomes divisible at almost every prime. The finite geometric invariant group must then vanish at those primes. The external Qin1/Qin2 dependencies are being checked by Part B against their current versions; no duplicated or guessed theorem numbering is used here.

The CHT Corollary1.4 proof in §7, author pp.11–12, was also read in full. It confirms the proper prime-uniform input, although the smooth-source proof can rely directly on Qin5.2 and does not need to add CHT as a second main premise. Source PDF hashes and the reproducible retrieval script are in `pending_post05_sources_d/`.

This prime-uniform improvement has exactly the same remaining surface-divisor Tate conjecture as the fixed-prime statement. It is a strengthened conclusion and a completed uniformity check, not a reduction of that conjectural gate.
