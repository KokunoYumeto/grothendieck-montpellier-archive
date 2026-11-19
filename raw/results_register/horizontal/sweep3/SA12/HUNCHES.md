# SA12 hunches (sweep 3)

Merged by the SA12 lead, a65dbdc241d1a129a (Claude Opus 5.5 at effort max), 19 Nov 2026, from the three readings. None of these is a statement of his pages. Each names its source: A is reader A (a203d72bad105bea5), B is reader B (a3c8d7ded052a745e), L is the lead. All three are Claude Opus 5.5 at effort max.

## Cohomological dimension (cote 31)

**H1. Conjecture 1° of 31/085 is a theorem for quasi-excellent X (L).**
- The conjecture: cd_ℓ(X) ≤ cd_ℓ(k(x)) for a good affine integral X, ℓ invertible.
- Grounds:
  - Gabber's affine Lefschetz theorem (Illusie-Laszlo-Orgogozo, Travaux de Gabber, Exp. XV) bounds cd_ℓ of an affine X of finite type over a strictly local quasi-excellent base by the value of the dimension function at the generic point.
  - That value is cd_ℓ of the function field, by Gabber's bound for fields (Exp. XVIII-A) and Serre's formula cd_ℓ(k') = cd_ℓ(k) + tr.deg for finitely generated k'/k with cd_ℓ(k) < ∞ (Cohomologie galoisienne II.4.2).
  - It holds in every case I tested: varieties over algebraically closed and finite fields, Spec O_K[1/ℓ], strictly local rings.
  - All locators are unverified.
- What may fail: the passage to non-strictly-local bases, through Hochschild-Serre on the strict localizations, and non-excellent rings.

**H2. The question of 31/082 is open on the page, and it follows from 1° (L).**
- cd_ℓ(X) ≤ sup_x[cd_ℓ k(x) + dim O_{X,x}] for noetherian affine X with ℓ invertible. The generic point alone gives n ≥ cd_ℓ k(x).
- His refutation by number rings does not satisfy his own hypothesis on ℓ, since Spec O_K[1/ℓ] has cd_ℓ = 2 = n.
- That n is also attained by some affine open is plausible: at a regular point of dimension d, local purity gives a class in degree cd_ℓ k(x) + d.

**H3. 2° and 3° of 31/085 are calibrated on Artin-Verdier (L, checked as a computation).**
- Spec O_K has cd 3 = δ + 3, while its proper opens have cd 2. 3° (some prime invertible ⇒ cd_ℓ(X) ≤ cd_ℓ k(x)) is the shape of "U ≠ X ⇒ H³(U, F) = 0".
- Hunch: 2° and 4° are the scheme forms of the field bounds of Gabber-Orgogozo, "Sur la p-dimension des corps" (Invent. Math. 2008, locator unverified), with δ the p-degree. The methods of Gabber's affine Lefschetz with p-torsion coefficients may prove them, through the henselian-pair comparison.

**H4. Equality on small opens (his margin on 31/085) holds (L).**
- For A = k{x,y} strictly henselian, U = Spec A_{xy} has H²(U, μ_ℓ^{⊗2}) ∋ (x) ∪ (y) ≠ 0, so cd_ℓ(U) = 2 = cd_ℓ K. For the larger open Spec A_x, the constant sheaf and one extension by zero give only degree 1.
- Hunch: the complement of a normal-crossings divisor with dim A branches at the closed point attains cd_ℓ K, through the top cup product of Kummer classes.

**H5. "Probablement tjrs. le cas" (31/070), cd_ℓ K_{Y,ȳ} ≤ dim O_{Y,ȳ}, is Gabber's theorem for quasi-excellent strictly henselian local domains (L).** Without quasi-excellence it may fail: the completion can have larger dimension behaviour along non-reduced formal fibres.

**H6. The henselian lower bound (31/070 margin; 31/023 "cette restriction est-elle inutile ???") (L).**
- The bound: cd_ℓ K ≥ dim A + cd_ℓ k, for ℓ ≠ char K and cd_ℓ k < ∞.
- It should hold for excellent henselian domains without regularity: pass to the normalization and to a regular alteration of degree prime to ℓ (Gabber), where it is the regular case.
- Test: singular normal surface singularities over finite fields.

**H7. 31/044 in the wild case (L).** H¹(G,O*) → H¹(G_i,(O/m)*) is bijective in the tame case (checked). In the wild case it probably fails: U¹ is not uniquely divisible by the wild part, and a wildly ramified ℤ/p extension of a complete DVR is the test.

**H8. 31/011-017 and cote 37 (L).** His fA-cofinite example bears on Hartshorne's cofiniteness problem. Hartshorne's letter of 4.8.1969, "Affine duality and cofiniteness", is at 37/054-055.

**H9. 31/101 (L).** The local constancy of R^i h_* G for G on the complement of a smooth divisor is governed by the Swan conductors along the divisor (Deligne-Laumon semicontinuity; locators unverified).

## Fundamental group (cote 29)

**H10. Pic^τ in characteristic p (A; 29/071-075).**
- The theorem is probably true. The gap is infinitesimal, and his Frobenius split for H¹ (29/072-073) suggests the same split for H⁰(Y, R¹f_*O_X) or for H², which would give the injectivity H²(Y,O) → H²(X,O) that closes it.
- If it fails, the counterexample needs Pic^τ_Y non-reduced and R¹f_*O_X ≠ 0, so X must have non-rational singularities.

**H11. The Question of 29/075, dim H¹(O) bounded on normal models (L).**
- The dimension is non-decreasing up the system, since f_*O = O.
- In characteristic p and dimension ≥ 4, where resolution is unknown, a bound may come from de Jong-Gabber alterations together with the F-nilpotent/F-bijective split of 29/072-073.

**H12. Proposition 4 and the base (A, B).**
- The repair is that minimality must be taken in a class of groups closed under equalizers of the allowed morphisms: constant groups over a field, as in the letter to Serre and in Nori.
- Over a non-normal reduced base with morphisms varying along S, the cusp shows another notion is needed. Candidates are minimality among all closed subgroup schemes, flat or not, or the relative fundamental group scheme of Gasbarri and of Antei-Emsalem-Gasbarri (locators unverified).
- Reader B's remark decides where the weight lies: the final "unicité" of pointed maps from a minimal P.

**H13. π₁(Z − Y), Z proper non-projective, characteristic p (A; 29/066).**
- It is probably still of finite type. Abelian p-covers are finite in number in each degree, since the Frobenius-stable part of H¹(O) is finite-dimensional.
- This is weak.

**H14. Π₂^t(Spec ℤ − S) (A; 29/098, "Mais qu'est Π₂^t ???").** This is the K(π,1) question for arithmetic curves. A. Schmidt's results (Spec O_K − S is often K(π,1) for pro-p coefficients) answer it in many cases (locator unverified).

**H15. What LNM 208 dropped (A).** Murre's 1969 draft had a chapter X "plumbing" and an unwritten chapter on the analogue of Mumford's theorem (29/079-081). Grothendieck asked to apply it to the finite generation of the local prime-to-p π₁ (29/082). Comparing LNM 208 with Murre's chapters I-X would show what never appeared.

**H16. The 1959 "module de Weil" (A; 29/129-130).** It is an early written statement of the Dieudonné-module programme, seven years before crystals. It links to the crystals topics (SA05-SA07, SA15).

**H17. "Finitudes" (A; 29/041-045).**
- 3) b) is Orgogozo 2003.
- 1) b), finite presentation of π'₁ without resolution, is settled for the tame group with a good compactification (Esnault-Schusterman-Srinivas) and, I think, open in general.

**H18. 29/180 for proper surjective S' → S (B, L; revised after B's second stretch).**
- Every descent datum on a constant G_{S'} is probably effective for S, S' noetherian and S' → S proper surjective.
- Grounds:
  - Rydh's theorem: universally subtrusive morphisms of finite presentation are of effective descent for étale morphisms (Bull. SMF 2010, locator unverified). To check: whether the non-quasi-compact G_{S'} is within its hypotheses.
  - The test case is effective. For the normalization of a nodal curve, a datum g ∈ G glues S' × G into a chain of copies of S', a scheme étale over S.
  - His own partial result covers G residually finite.
- The earlier guess here, "probably false in general", is withdrawn.

**H19. Proposition 4 in Nori's setting (B).**
- Setting: Hom taken over k (Exemple II read with Hom_k), and S proper, reduced and connected with H⁰(S, O_S) = k.
- Pointed torsors are then rigid, and the cusp does not apply, since its [x] is not a k-morphism. Prop. 4 should hold there.
- 29/141-143 would then be the pro-object of Nori's fundamental group scheme (Nori 1976, 1982; locators unverified).

**H20. Ramification data are the étale sites of root stacks (B; 29/191-207).**
- Ex. 2 is the gerbe of n-th roots of O(D_i). The Kummer data with n_i prime only to the residue characteristics of D_i are the tame theory of LNM 208 and the later logarithmic Kummer-étale theory.
- The missing essential surjectivity of α (29/207) should follow by effective descent of finite étale covers along the Kummer covers, with C locally filtering.
- Links: SA12-16, SA12-17, SA12-31.

**H21. π₀ as a pro-set (B; 29/181-183).** The repaired 29/183 (finite stages, K profinite) and the ℕ^ℕ counterexample say that the natural home of his π₀ of a simplicial space is the strict pro-set (π₀ᵢ), not a topological space. This is the issue later met by Noohi groups (Bhatt-Scholze §7) and condensed sets.

**H22. 29/188 and SA12-70 (B).** The cancelled d''-homotopy sheet and the cote 33 typescript carry the same formula; the typescript may be his own (not decided).

**H23. G5 and finiteness (L, from B's refutation).** The countable ℤ-sets fail G5 because the Hom sets are infinite. The open point is which finiteness condition added to G0-G4 gives G5. Finite Hom sets between connected objects is the candidate, since it bounds the number of summands of X ×_Y X.
