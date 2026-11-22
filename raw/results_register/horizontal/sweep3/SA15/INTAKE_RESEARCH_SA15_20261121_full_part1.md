# Full intake of RESEARCH_SA15 cp37, part 1 of 3 (ids 1-318 of INTAKE_LEDGER section 9)

Claude Opus 5.5 at effort max, agent afcdf31bb407576f5 (the SA15 c7_c8 sweep-3 reader, author of the part-2 intake of
20 Nov), from 22 Nov 2026. The run: RESEARCH_SA15, GPT-6 Astra (ChatGPT Pro mode), with its internal sub-agents.
Return read: checkpoint 37 (20 Nov 06:35 UTC). Verdict codes as in the check rubric; "statement only" is said plainly.
All 318 ids are done (finished 22 Nov 2026). The summary, refutations (none), what is new, the errata, the bridges and
the Hexagon readiness are at the end of this file, after the 24 batch tables.

## Verdicts, in file order

### Batch 1 (A_coherent_counterexample, A_foundations 1-181, A_full_radical_image_structure, A_integral_counterexample)

| # | Row | Check | Result |
|---|---|---|---|
| 145 | lem:A-cyclic-coherent-kernel | targeted proof check | Right. Cyclic cover y^q = b of R; π_*O_X = ⊕ L^(-j), π_*A^(-1) = ⊕ L^(-j-1); multiplication by y maps the summand j = 0 (H^(n-1)(R,L^(-1))) identically onto the target summand j = 1, so H^(n-1)(X,O) → H^(n-1)(Y,O) has a nonzero kernel whenever H^(n-1)(R,L^(-1)) ≠ 0; for ay + s the s-part keeps the summand index and cannot cancel. Smoothness by the Jacobian, very ampleness by the explicit cone embedding. |
| 1 | A-ALG-FITTING (= lem:A-fitting) | targeted proof check; known | Right: stabilization of images and kernels of iterates, exactness by lifting through a common iterate, p-adic limit with Artin-Rees. Known: Ogus 1975, Lemma 4.8 and Remark 4.10 (as cited). |
| 2 | A-NAKAYAMA (= lem:A-derived-Nakayama) | independent re-proof | Right: the universal coefficient sequence 0 → H^j(K)/p → H^j(K ⊗^L R/p) → H^(j+1)(K)[p] → 0 and Nakayama for j < s, then H^s(K)[p] = 0. Standard. |
| 3 | A-R1 (= lem:A-R1) | targeted proof check | Right: F^a on H^j(X,O(-d)) factors through H^j(X,O(-p^a d)), whose dual H^(n-j)(X,ω(p^a d)) vanishes for large a (Serre vanishing), for j < n; then exactness of the stable part. No Kodaira vanishing used. (This is the same factorization as sweep 3's proof of 8.5.7, `STUDY.md` §1.) |
| 4 | A-R2 (= lem:A-R2) | independent re-proof | Right: F_dR = βα and F_O = αβ with α the augmentation and β: f ↦ f^p; so α is an isomorphism on bijective parts. Agrees with sweep 3's check SA15-S3-1 (cote 4, Lemma 8.4.3). |
| 5 | A1-HIGH (= thm:A-high-degree) | targeted proof check | Right. RΓ(Ω^a_X(-t)) ∈ D^(≥n) for t ≥ d_int by regularity and Serre duality; the conormal sequence resolves Ω^a_Y by Ω^(a-b)_X\|_Y(-bd), giving Cone(RΓΩ^a_X → RΓΩ^a_Y) ∈ D^(≥n-a-1), hence the de Rham restriction cone in D^(≥n-1); crystalline reduces mod p to de Rham, so derived Nakayama gives isomorphisms below n-1, injectivity in n-1 with torsion-free cokernel, and T^(n-1)(X) ≅ T^(n-1)(Y). An explicit-regularity form of BMS 2016, Lemma 2.12 (as cited; not opened by me). |
| 136 | cor:root-full-radical-submodules-orbits | targeted proof check of the deduction | The deduction from the structure (FR5) is right (transitivity off K by GL(X) and shears; every proper submodule lies in K; invariant covectors vanish when dim V/K ≥ 2). (FR5) itself (the proposition at the start of A_full_radical_image_structure.tex) is not in my list and I did not read it. |
| 139 | cor:root-odd-image-parabolic-alternative | read; deduction right | Combines cor:fixed-ppav-odd-full-hyperplane-inertia, thm:nonordinary-ppav-all-covectors and (FR5); the deduction is right; those inputs I did not check here. |
| 107 | cor:OC-all-prime-integral-counterexample | computation (numbers) + read | Recomputed at p = 2: g = 7, B_2 = 35, a_i = 6, 5, 4, r = 210 + 186 + 160 = 556, as stated; the formula for r is Riemann-Roch summed over the filtration (degrees above 2g-2). The inequality h^0(X,Ω^1) ≤ q^r(B_p + r) and the final strict inequality rest on lem:OC-explicit-differential-bound and prop:OC-product-integral-counterexample, not in my list, not read. |
| 8 | A2-EXACT (= thm:A-exact85) | targeted proof check | Right. Stable universal-coefficient sequence 0 → (C^j/p)_ss → H^j(O)_ss → C^(j+1)[p]_ss → 0 (derived crystalline base change + R2); C^j[p]_ss = 0 for j > dim Z; snake lemma on the rows for X and Y in degree n-1 (middle map injective by R1) gives 0 → T^n(X)[p]_ss → (E/pE)_ss → E(Y,O_Y)_ss → 0 in every degree d ≥ 1, ker v = 0, and both directions of 8.5.10. **This is Grothendieck's (8.5.1) on cote 4, scans 6-8, as a theorem in every degree.** |
| 10 | A2-UNIT (= thm:A-unit-count) | targeted proof check (inputs cited, not opened) | Right. Mod-p weak Lefschetz from Artin-Schreier and R1; derived Nakayama over Z_p for the étale cone; Ogus 1975, Thm 4.9 (C^j(Z)^u ≅ H^j_ét(Z̄,Z_p) ⊗ W(k̄), including torsion) makes E^u torsion-free of rank the slope-0 difference; Katz-Messing 1974, Thm 1 (crystalline and ℓ-adic characteristic polynomials agree) and ℓ-adic weak Lefschetz identify this with the number of unit reciprocal roots of P_van. **Grothendieck's unit-root count of 8.5.4 (cote 4), proved.** Bridge: Katz-Messing's theorem is a consequence of Deligne's Weil I (see the bridges section). |
| 7 | A1-TRANSPOSE (= prop:A-transpose-u2) | targeted proof check | Right: torsion linking pairings T^j × T^(2 dim+1-j) → W[1/p]/W pair T^n(X)[p] with T^(n+1)(X)/p and T^n(Y)[p] with T^(n-1)(Y)/p; pullback and Gysin are adjoint; with T^(n-1)(X) ≅ T^(n-1)(Y) the composite is cup product with d·c_1(O(1)) (self-intersection), zero for p \| d. This is Grothendieck's u''_2 on cote 4 (8.2.1/8.3). |
| 9 | A2-STAR-DUAL (= prop:A-star-dual) | targeted proof check | Right: H^n(O)_ss ≅ (C^n/p)_ss; dualizing by Serre duality, free Poincaré duality and the linking pairing sends F to its σ⁻¹-semilinear adjoint V, so the sheet 8.4.4's sequences (*) and (**) are dual with V, not F, on the dual side. |
| 6 | A1-SMALL (= open:A-small-degree) | read (summary remark) | A summary: A.1(a)-(c) false, with exact degree ranges from thm:OC-product-exact-degrees, thm:OC-exact-integral-injectivity-degrees, cor:OC-surface-exact-degrees, cor:OC-all-prime-integral-counterexample; those theorems are not in my list except #107 (numbers checked above). |

Errata/transcription note from A_foundations.tex lines 18-23: the run reports that both transcription witnesses of cote 4 keep a **cancelled section 8.2 with (8.2.1) on scans 3-4**, so the prompt's "no section 8.2" needs that qualification. Sweep 3 (`STUDY.md` §1) did not mention the cancelled 8.2; a check on the scan is needed before an edition.

The rows 1-5, 7-10 above were also checked in part 1 (Claude Opus 5.5 at effort max, agent SA15-c9_c100-part2, called a8d91f19c2d8f19c1 in the coordinator's message; corrected 22 Nov from an earlier wrong "effort high", `INTAKE_RESEARCH_SA15_20261120_part1.md`, lines 135-154); my checks agree with its verdicts.

### Batch 2 (A_lifting.tex: A.6, stable torsion and a characteristic-zero lift)

| # | Row | Check | Result |
|---|---|---|---|
| 13 | A6-IDENTITY (= thm:A-special-torsion) | targeted proof check (prismatic part cited) | The identity T^j(Z_k̄)[p]_ss ≅ H^j_ét(Z_k̄,Z_p)[p] ⊗ k̄ follows from Ogus 1975, Cor. 4.11 (unit part ≅ étale ⊗ W, with torsion) by taking p-torsion, W(k̄) being flat over Z_p: right. The description of ker s^j and its bounds (injective for e(j-1) < p-1) are Li-Liu 2022, Thm 4.10, Lemma 4.11, Thm 4.14, Cor. 4.15, as cited; not opened by me. |
| 12 | A6-COUNTEREXAMPLE (= thm:A-BMS-counterexample) | independent re-proof of the hand-checkable steps | Right. I re-derived: ι(x,y) = (x,-x-y) preserves x_i^2 + x_jx_k - y_i^2 - x_iy_i (the y-part is invariant); ι is free in characteristic 2 (a fixed point forces x = 0, then y = 0); for E: y^2 + xy = x^3 + 1, b_2 = 1, b_4 = 0, b_6 = 4, b_8 = 1, so Δ = -1 - 27·16 = -433; P = (u/4, -u/8) lies on E iff u^3 + u^2 + 64 = 0, P = -P, and [2u:-u:8] reduces to O; D = (Q x E)/⟨(ι,+P)⟩ has special fibre S_0 x E_0 and generic π_1 = Ẑ^2 (torsion-free H^2); H^1(D_0,F_2) = F_2^2, H^1(D_0,Z_2) = Z_2, so H^2(D_0,Z_2)[2] = F_2, carried to the surface by weak Lefschetz on H^1. So T^2(X_0)[2]_ss ≠ 0 while H^2_ét of the generic fibre is torsion-free (p = n = 2, the boundary e(n-1) = p-1). The BMS 2016 phenomenon (Thm 2.1, Remark 2.3) made explicit; no priority claimed by the run. The smoothness of Q mod 2 (run's Groebner check) I did not rerun; its hand argument reads right. |
| 11 | A6-COMPUTATION (= rem:A-K3-computation) | read; not rerun | Describes `code/k3_lift_check.py`. The facts it certifies that can be checked by hand (Δ_E = -433, the equation for u, the invariance under ι) I checked above. |
| 14 | A6-SMALL-RANGE (= cor:A-lifting-small-range) | targeted proof check | Right: for e(n-1) < p-1 specialization is injective (Li-Liu), so torsion-free generic H^n forces T^n[p]_ss = 0. |

Archive: A.6 concerns 8.5.10 of cote 4 (φ bijective iff (pTors^n(X))_ss = 0): its vanishing condition is on the special fibre and cannot be replaced by torsion-freeness of the generic fibre of a lift (counterexample above), except in the range e(n-1) < p-1.

### Batch 3 (A_monodromy.tex: eventual Hodge parenthesis; products; the supersingular product E_0 x E_0; ppav remarks)

| # | Row | Check | Result |
|---|---|---|---|
| 114 | cor:eventual-hodge-parenthesis | targeted proof check of the deduction | Right: dim E(Y,O_Y) = h^0(ω L^d) - h^0(ω) is Y-independent; on U_d, thm:A-exact85 + thm:A-unit-count give unit-root count = f_(X,d) + dim H^n_cris(X)[p]_ss > 0. The positivity input thm:all-X-explicit-positive-rank is outside my list and was not checked by me. The scope note (a supersingular plane cubic has H^1(O) ≠ 0 and no unit root) is right. Archive: answers the "pour Y générique" of 8.5.8 (cote 4, scans 8-9). |
| 131 | cor:ordinary-products-irreducible-kernel | targeted proof check of the deduction | Right given thm:ordinary-products-Hasse-irreducible (not checked by me): with thm:product-char2-all-parities-fixed-quotient and lem:irreducible-hasse-quotients-trivial (both checked in my part-2 intake) every proper invariant subspace contains K. The extension to distinct ordinary factors is valid: the pushforward computations are factorwise. |
| 23 | auto:A_monodromy:3a04f9cdd890 | computation (count) + read | Program remark. The count is right: there are 7 x 7 = 49 rank-one 3x3 matrices over F_2 and C(49,3) = 18424 triples. Program not rerun. |
| 302 | lem:DE-A3-ss-norm | independent re-proof | Right. (x,y) ↦ (x+a, y+a^2x+c) preserves y^2+y = x^3 iff a^4 = a and c^2+c = a^3 (re-derived); i, j as given satisfy i^2 = j^2 = [-1] = (x,y+1) and ji = [-1]ij (recomputed: ij = (x+ω^2, y+ωx+ω), ji = (x+ω^2, y+ωx+ω^2)); Rosati = conjugation, so the norm form is a^2+b^2+c^2+d^2; the four-square descent argument is right. |
| 303 | lem:DE-A3-ss-prym | targeted proof check | Right: g = m^2+1 by adjunction; j: Pic^0(X) → J_Y a closed immersion (Künneth vanishing); q∘j = [m]; ker q = P connected (isogeny duality); f_Y = f_P ≤ m^2-1; for m even X[2] ⊂ P[2] gives the connected order-4 ker V_X inside ker V_P, so dim P - f_P ≥ 2 and f_Y ≤ m^2-3. |
| 95 | cor:DE-A3-ss-product-defect | targeted proof check of the auxiliary facts | Pic^0 = E_0^2 smooth, crystalline cohomology of a product of elliptic curves torsion-free (Illusie 1979 II 7.1.1, as cited), C(dx) = 0: right. The defect values g - f = 2 (odd d), 4 (even d) are thm:DE-A3-ss-product-rank, outside my list, not checked. So eventual relative ordinarity fails on a surface with smooth Pic^0 and torsion-free crystalline cohomology (given that theorem). |
| 22 | auto:A_monodromy:3502a4b6e144 | read; not rerun | Program remark for the supersingular degree-one certificates. |
| 25 | auto:A_monodromy:9cc9a63fa2c6 | read; not rerun | Program remark; says itself it is not used in the proof. |
| 112 | cor:all-theta-fixed-point-jets-candidate | targeted proof check | Right: an infinite R_P would give [2]Θ = Θ + 3P as reduced curves; the class of [2]Θ is 2Θ or 4Θ, never Θ. |
| 29 | auto:A_monodromy:bcd64c5e340f | read; count checked | Remark; the 243 = 3^(2g+1) Heisenberg matrices for g = 2 is the right order. Program not rerun. |
| 20 | auto:A_monodromy:20bf13b82135 | read | Scope remark; accurate. |
| 15 | auto:A_monodromy:03a3e68c4a1c | read; not rerun | Program remark (the six elements of GL_2(F_2) acting on F_2^4/F_2·1). |
| 18 | auto:A_monodromy:12aa8c66349f | read; **erratum (stale)** | Says the supersingular-product images are certified only in degrees 1-3 and the uniform question remains; this is superseded by thm:ss-all-odd-full-groups (17294) and thm:ss-product-all-full-groups (17893) later in the same file. The paper should drop or date this remark. |

### Batch 4 (A_monodromy.tex 9778-11113: theta Pfaffian, principally polarized surfaces, polarizations, mixed products)

| # | Row | Check | Result |
|---|---|---|---|
| 305 | lem:DE-A3-theta-pfaffian | independent re-proof of the key computations | Right. I recomputed det B = (α_0^3+α_1^3+α_2^3)x_0x_1x_2 - α_0α_1α_2(x_0^3+x_1^3+x_2^3), which is the stated formula in characteristic 2; rank 8 at s = e_0 (four 2x2 blocks, Pfaffian ∏α_i); Heisenberg invariance leaves the basis P_*, P_i; q = 0 iff ∏α_i = 0 and α_i Σ_(j≠i) α_j^3 = 0, so all nonzero cubes equal u with (r-1)u = 0: r odd, r ∈ {1,3}; 4 + 4·9 = 40 projective points. The Fourier normalization of the three-direction form reads right. |
| 296 | lem:DE-A3-ppav-odd-norm | targeted proof check | Right given prop:DE-A3-ppav-degree-one (genus-10 curves of 2-rank 8+f_A; outside my list): φ: A' → A of degree d^2 with φ*Θ ≡ dΘ', so Nm(3Θ') ≡ 3dΘ; nodes 18(d^2-1)/2 = 9(d^2-1), arithmetic genus 10 + 9(d^2-1) = 9d^2+1 as it must be; the node graph is Frobenius-bijective, so the defect 2 - f_A is preserved. |
| 295 | lem:DE-A3-ppav-even-bound (bridge flag) | targeted proof check | Right: j: Pic^0 → J_Y an immersion; qj = [3d] (Debarre 1994, (3.2)-(3.3), cited); for d even A[2] ⊂ P_Y[2], so the connected order-2^(2-f_A) part of ker V_A embeds in ker V_(P_Y), giving a Prym defect ≥ 2 - f_A; total ≥ 2(2 - f_A). The ℓ-adic Tate modules enter only as an alternative proof of qj = [3d] over k̄; no Frobenius weights (see the bridges section). |
| 298 | lem:DE-A3-principal-norm-source | targeted proof check | Right: λ_M λ_N λ_M = λ_(M^D) = Dλ_M, so λ_N = Dλ_M⁻¹; χ(N) = χ(M^D)/deg λ_M = D^3/D^2 = D; a maximal isotropic subgroup of ker λ_N gives the principal quotient; φ = ψ^∨ of odd degree is étale and preserves the 2-rank. |
| 265 | lem:DE-A3-general-polarization-Prym | targeted proof check | Right given Debarre's (3.2)-(3.3) (cited, not opened): j*λ_(J_Y) = mDλ_M⁻¹ = mλ_N; for even m the Verschiebung argument as in 295. |
| 274 | lem:DE-A3-ordinary-polarization-kernel | targeted proof check | Right: for ordinary A, A[2^n] ≅ μ_(2^n)^2 x (Z/2^n)^2; the commutator pairing is trivial on the multiplicative factor (no maps from a local group to an étale one) and on the étale factor (μ_(2^n)(k̄) = 1), so it pairs the two perfectly, each of order D_2; odd parts by the exponent argument; DK = 0. |
| 273 | lem:DE-A3-ordinary-etale-norm | targeted proof check | Right: taking the multiplicative factor K_2^0 in the maximal isotropic H makes ker(ψ^∨) = H^D étale even for D even. A good device. |
| 275 | lem:DE-A3-ordinary-principal-multiples | targeted proof check | Right given lem:ppav-surface-dichotomy and lem:ppav-ordinary-members (outside my list): very ampleness of nΘ by translates of rΘ; ordinary nodal theta sums (indecomposable) or grids of 2n ordinary elliptic curves with n^2 nodes (decomposable); h^1 = n^2+1. |
| 263 | lem:DE-A3-all-multiple-nodal-norm | targeted proof check | Right: jet transfer by sections of translates of rΘ (theorem of the square), finitely many bad translations, three-value independence; each nonzero kernel translate meets C in (nΘ)^2 = 2n^2 points, so n^2(deg φ - 1) nodes. |
| 270 | lem:DE-A3-mixed-odd-factor | targeted proof check | Right given thm:DE-A3-ppav-ranks (genus-10 curves of stable rank 9 on a mixed principal product; outside my list): étale isogenies of degree e (iterated Verschiebung of an ordinary curve, plus odd part) and c; the image of the product cubic has class (3c, 3e) (I recomputed φ_*C'·(E_o x pt) = 3·deg φ_s = 3c); 9(ce-1) nodes; lower bound 9ce, upper bound g - 1 = 9ce from the nilpotent line of E_s. |
| 268 | lem:DE-A3-mixed-even-bound | targeted proof check | Right: for m even the first factor is a Frobenius pullback, ∂_o acts on H^0(N), C(s) = 0 and C(∂_o s) = C(f df ∧ ω_s) = 0; 1+x and x are independent sections (normal form y^2+xy = x^3+a_2x^2+a_6); relative stable rank = stable rank of H^2(N⁻¹) ≤ mn - 2 since H^2(O_A) has Frobenius zero. |

### Batch 5 (A_monodromy.tex 11202-12315: mixed surfaces of 2-rank one)

| # | Row | Check | Result |
|---|---|---|---|
| 271 | lem:DE-A3-mixed-polarization-blocks (bridge flag) | targeted proof check | Right: A[2^∞] = G_ét x G_mult x G_ll (heights 1, 1, 2); the Riemann form on the Dieudonné lattice is alternating (skew over W, no 2-torsion), the ordinary block has indices (a,a), the local-local block [[0,c],[-c,0]] has (b,b); deg λ_M = D^2 gives v_2(D) = a + b; for N = descent of M^D, λ_N = Dλ_M⁻¹ and the indices swap: a(N) = v_2(D) - a(M) = b(M). The "Tate module" is the rank-one 2-adic Tate module of G_ét: no Frobenius weights. Oda 1969 cited for the Dieudonné dictionary (not opened). |
| 269 | lem:DE-A3-mixed-index-zero-source | targeted proof check | Right in both directions: a(M) = 0 puts the 2-primary kernel of λ_N in the ordinary block, whose multiplicative factor is maximal isotropic, so φ = ψ^∨ is étale; conversely an étale φ preserves the local-local factor and DΘ_B has local-local index v_2(D), forcing a(M) = 0. |
| 266 | lem:DE-A3-mixed-all-even-Prym | targeted proof check | Right: qj = mλ_N (Debarre, cited) kills A^∨[2] for m even; the connected ker V of order 2 embeds in the Prym; g - f ≥ 1 + 1. |
| 264 | lem:DE-A3-axis-nodal-norm | targeted proof check | Right: g(C) = 19 (N^2 = 36), image p_a = 18n+1, nodes 18(n-1); norm classes (6,3n) for φ_1 x 1 and (6n,3) for 1 x φ_2 (I recomputed via π*(a,b) = (na,b) and the class (6n,3n) of the sum of translates). The incidence-dimension arguments read right. |
| 90 | cor:DE-A3-mixed-thin-vone | targeted proof check | Right given lem:root-mixed-six-three-cartier (outside my list): 17 + 18(n-1) = 18n-1 from the nodal image, and the upper bound 18n-2 from lem:DE-A3-mixed-even-bound (checked in batch 4); a ≡ 2 mod 4 ⇔ 3a = 6n with n odd, so r_1 = 9a-2. |
| 276 | lem:DE-A3-ordinary-two-pencils | targeted proof check | Right: F_*O_E = O ⊕ B with B = ker τ, B^2 ≅ O, H^0(B) = H^1(B) = 0; 0 → B → H ⊕ HB → H^2 → 0 and HB(-A) = B, H(-D) = B give the three isomorphisms. |
| 272 | lem:DE-A3-mixed-residue-determinant | targeted proof check of the logic (residue formulas read, not recomputed) | Right: kernel k_a, k_b of T_s; Q(ker T_s) → coker T_s is the 2x2 obstruction matrix [[t,u],[v,t]]; under b_1 ↦ b_1 + λb_2, t and v are constant, u has nonzero linear coefficient c_1 (a nonzero combination of squares of independent evaluation coordinates), v ≠ 0 (cubes); det = t^2 + u(λ)v is a nonconstant polynomial, so nonzero for some λ; then kernel ∩ image = 0 and stable rank = rank = 6q-2. |
| 89 | cor:DE-A3-mixed-product-no-exception | read; deduction right | r_d = 9abd^2 - 1 - ε(ad) assembles thm:DE-A3-mixed-all-product-ranks and thm:DE-A3-mixed-thin-all (outside my list, not checked); consistent with #90 (a even, d = 1 gives 9a-2). |
| 280 | lem:DE-A3-positive-index-Prym | targeted proof check | Right: b(N) = a, so mλ_N kills G_ll[2] when a + v_2(m) > 0; Prym defect ≥ 1; g(Y) = Dm^2+1; for L = M^3, r_d ≤ 9Dd^2 - 2. |
| 281 | lem:DE-A3-positive-index-descent | targeted proof check | Right: the ordinary étale factor of ker λ_M is cyclic of order n = 2^a; descent by a rescaled linearization; a(M) = a(H) + a; Deuring-Shafarevich f_Y - 1 = n(f_C - 1) (Crew 1984, (1.8.2), cited; the run's direct Euler-characteristic proof is right) and Hurwitz give g_Y - f_Y = n(g_C - f_C). |
| 283 | lem:DE-A3-positive-index-image-candidate | targeted proof check | Right as a reduction: μ_2 ⊂ ker λ_N isotropic, N = π*H for the inseparable π: A → A/μ_2; W = W_0 ⊕ W_1 of equal dimension b/2; C(f^2 ω) = C(f e(f) ω) = 0, so the coherent Frobenius lands in I = ker(s, es); sharp rank b-2 ⇔ the degree-b determinant form is nonzero, which the lemma itself leaves open (its name "candidate" fits that; its status "Proved" fits the reduction). |

### Batch 6 (A_monodromy.tex 12340-13208: the reduction at positive ordinary index)

These lemmas reduce the sharp rank b-2 at positive ordinary index to the invertibility of a cup product β ∪ - : H^0(D,A) → H^1(D,A) on a determinant curve D, and further to a trace/determinant condition on a 2x2 matrix A(u). None claims the final nonvanishing; the run says so in each. The "-candidate" names mark that, while the statuses "Proved" refer to the reduction steps, which hold.

| # | Row | Check | Result |
|---|---|---|---|
| 282 | lem:DE-A3-positive-index-double-corank-candidate | targeted proof check | Right: trace sequence 0 → V_B → I_A → I_B → 0; F\|I_B bijective gives ker(F\|I_A) = π*K_B, image ∩ kernel = 0, first = stable rank b-4; the variation vanishes on pulled-back directions (β symmetric, e self-adjoint) and factors through Tr. |
| 294 | lem:DE-A3-positive-two-bundles | targeted proof check | Right: ker F_B = μ_2 x α_2; F_*H = ν_*J ⊕ ν_*(JQ) = E_0 ⊕ E_0P; alternating perfect pairings (C(ω) = 0); h^0(E_i) = b/2 and, from χ = (c_1^2 - 2c_2)/2 with c_1^2/2 = b, c_2 = b/2 (recomputed). |
| 279 | lem:DE-A3-positive-determinant-curve | targeted proof check | Right: p_a(D) = 1 + (LP)^2/2 = b+1; χ(K) = b/2 + b/2 - b = 0, χ(Q_s) = 0, χ(R_s) = 0, so deg R_s = p_a - 1 = b (recomputed); sharpness gives h^0 = h^1 = 2. |
| 292 | lem:DE-A3-positive-torsor-boundary | targeted proof check | Right: Čech representatives r_b - r_a = c_ab s_i give the boundary α. |
| 293 | lem:DE-A3-positive-trace-radical | targeted proof check | Right: corrected trace lifts; C(q_iq_jω) = 0 for i ≠ j (weight one) and C(q_i^2 ω_A) = q_i C(ω_A) = 0 (mixed), so the variation kills R = ⟨s_0, s_1⟩. |
| 284 | lem:DE-A3-positive-matrix-ruling | independent re-proof | Right (classical): with A = diag(1,0) in the image, det(A+tB) ≡ 0 gives b_22 = 0 and b_12b_21 = 0; a vector space over an infinite field is not a union of two proper subspaces. |
| 288 | lem:DE-A3-positive-pencil-candidate | targeted proof check | Right: R_0 ≅ O_D(Z_0), R_0P ≅ O_D(Z_1), A = R_0^2 of degree b, R_s ≅ ω_D ⊗ A⁻¹ (Tor computation and adjunction), valid for nonreduced D. |
| 287 | lem:DE-A3-positive-norm-pencil-candidate | targeted proof check | Right: the α_2-norm n(a+bz) = a^2 + hb^2 gives σ with S_i\|_D = σa_i, σ a nonzerodivisor; d log u glues to η_P with C(η_P) = η_P, nonzero since P is nontrivial. |
| 289 | lem:DE-A3-positive-pencil-contraction-candidate | targeted proof check | Right: Ext^q(E_0,E_1) = 0 (filtration by the acyclic Q); (DE-TP6) realizes C_s on D; at a sharp source h^0(A) = h^1(A) = 2; ∂(σa) = β\|_D ∪ a from r ∧ z_i r = n(r) = σr^2. |
| 92 | cor:DE-A3-positive-first-rank-candidate | targeted proof check | Right: the torsor trace sequence on D gives kernel dimension 2 + dim ker(α\|_D ∪ -). |
| 278 | lem:DE-A3-positive-cup-derivative-candidate | targeted proof check (structure; not every term recomputed) | The splitting independence of A(u) = P H r and the derivative identity (DE-CD1) follow as written; trace-zero ⇔ tr A is a square, since ker d on a rational function field over a perfect field of characteristic 2 is the subfield of squares. |

### Batch 7 (A_monodromy.tex 13243-14380: the reduction at positive index, continued; the primitive case)

| # | Row | Check | Result |
|---|---|---|---|
| 277 | lem:DE-A3-positive-acyclic-alternating-candidate | independent re-proof of the identity | Right: 𝔤 acyclic from (DE-TP5); tr(XY) on End^0/scalars is bd'+db' (alternating, perfect); I recomputed aJ_2a^t = [[2uh^2, w],[w,0]] = wJ_2 = f(u⁻¹J_2)f^t in characteristic 2. |
| 93 | cor:DE-A3-positive-tracezero-matrix-line-candidate | independent re-proof | Right: N^2 = 0 by Cayley-Hamilton; det(N + tB) = tc + t^2(a^2+bc) (recomputed), so c = a = 0. |
| 285 | lem:DE-A3-positive-monad-note | targeted proof check | Right: (DE-MN1) exact with Lagrangian image; (DE-MN2) at a sharp source. |
| 286 | lem:DE-A3-positive-monad-variation-note | independent re-proof of the local computation | Right: commutators of trace-zero 2x2 matrices are scalar in characteristic 2; aJ_2ȧ^t + f(u⁻¹J_2)ḟ^t = [[0,ẇ],[ẇ,0]] = ẇJ_2 (recomputed). |
| 267 | lem:DE-A3-mixed-common-power-root | targeted proof check | Right given that symmetric homomorphisms over k̄ are λ_L in every characteristic (EvdGM Prop. 11.2, Cor. 11.3, cited): λ_M = nφ, φ symmetric (Hom(A,A^∨) torsion-free), H = H_0 ⊗ Q; indices drop by r; maximality. |
| 88 | cor:DE-A3-mixed-primitive-rank-gate | targeted proof check | Right as stated: an exact reduction to a(H) > 0, b(H) = 0; the run says the primitive nonvanishing stays open. |
| 291 | lem:DE-A3-positive-restricted-Petri-note | targeted proof check | Right: (DE-PT1) from the twisted K-sequence; the cup-wedge map is symmetric (two signs); (DE-PT5) duality. |
| 91 | cor:DE-A3-positive-Petri-radical-note | targeted proof check | Right, via #93. |
| 290 | lem:DE-A3-positive-pushforward-jets | targeted proof check | Right: ν⁻¹(m_t^2) = (x^2, xz^2, z^4) ⊃ (x,z)^4, quotient basis 1,z,z^2,z^3,x,xz; cubes of very ample bundles separate third jets. |
| 300 | lem:DE-A3-residual-pencil-boundary | targeted proof check | Right: the images wf_1^2, wf_1f_2, f_1f_2, f_2^2 have relation module generated by e_1⊗f_2 - we_2⊗f_1; cokernel (O/w)f_1^2; the two-step Čech boundary is the cup-wedge map, also for r = s, without division by 2. |
| 94 | cor:DE-A3-residual-pencil-restriction | targeted proof check | Right: on an integral D a quadratic relation among r_0^2, r_0r_1, r_1^2 would make r_1/r_0 constant. |
| 297 | lem:DE-A3-primitive-unipotent | independent re-proof of the transition | Right: M^[2]/N sends (h_j,1) to (h_i,1) (I recomputed: first coordinate h_iN, second N) and in the frames ((h_i,1),(1,0)) has matrix [[1, b^2/N],[0,1]], so γ_ij = b^2/(a^2+b^2h_i); nonvanishing through κ = dλ_J(δ) and (ν^c)* an isomorphism on H^1(O). |
| 307 | lem:DE-A3-unipotent-Frobenius | independent re-proof | Right: dγ = γ^2 dh (recomputed: d(b^2) = 0), Hodge-de Rham degeneration kills d on H^1(O), cup with θ injective, so Fγ = 0; Sym^2U ≅ U ⊕ O and (h^0,h^1,h^2)(Sym^2G) = (2,4,2). |
| 299 | lem:DE-A3-residual-boundary-kernel | targeted proof check | Right: (DE-SK2) by composing the two boundaries; (DE-SK3) by tensoring the squared-pencil sequence with the acyclic G; the norm section gives h^0(D, A⊗G\|_D) ≥ 1. |

### Batch 8 (A_monodromy.tex 14399-21261: twisted pencils; the supersingular norm family; collision machinery; mixed products)

| # | Row | Check | Result |
|---|---|---|---|
| 306 | lem:DE-A3-twisted-pencil-lift | targeted proof check | Right: σ_G ≠ 0 (else a surjection P\|_D → R between line bundles of degrees 0 and b > 0); γ\|_D ∪ σ_G = 0 as the Yoneda obstruction of an extendable map; Serre duality on D and χ(AP) = 0 give h^0(A⊗G\|_D) = m + dim ker(γ∪) ≥ m+1. |
| 308 | lem:DE-A4-contact-discriminant-span | targeted proof check | Right: the h-coefficient γZ^2 + δ(z^2Z+w+d) + ε = 0 forces γ = δ = ε = 0 by pole orders 4, 6, 0 at O; then αℓ/A_1 + β = 0 with A_1 = Y + Xx^2 = y^2 + b + ax^2 (pole order 6; I rechecked the reduction using y^2 + y = x^3) forces α = β = 0. The chart support calculation reads right. |
| 96 | cor:DE-A4-third-value-smooth | targeted proof check | Right: injective projections give X(k), Z(k) ≠ 0, so H_k is none of the forced hyperplanes; det S = FTU; the nondegenerate Frobenius cubic contains no plane. |
| 310 | lem:DE-A4-uniform-triple-local-type | targeted proof check | Right: the five linear conditions give S = [[0,αb_02,αb_01],[βb_12,0,βb_10],[r,s,0]]; contact of order exactly two iff ακ_0l_1 + βκ_1l_0 ≠ 0 and transversality iff rb_20 + sb_21 ≠ 0, finitely many proper lines in the (r,s)-plane; the global open meets the local-type open in the irreducible P^3-bundle. |
| 141 | cor:ss-degree3-hasse-irreducible | read; deduction right | Follows from lem:ss-global-contact03, lem:ss-global-tangent-triples (computational witnesses) and prop:ss-level3-three-witness-reduction, which are outside my list; I did not rerun the witness programs. |
| 28 | auto:A_monodromy:b303eb6cd268 | targeted check of its one claim | Right: Aut(E_0, O) has order 24 and acts transitively on the 8 points of E_0[3] \ O, so product automorphisms are transitive on pairs of nonzero 3-torsion points. |
| 30 | auto:A_monodromy:c25cfd1730a5 | read; consistency checked | Program remark; for φ = [[1,b],[-b^†,1]] one has φ^†φ = 1 + b^†b = d when b^†b = d-1, as stated. Program not rerun. |
| 125 | cor:mixed-every-modulus-full-root-inertia-candidate | read; deduction right | Follows from lem:moving-kernel-full-root-inertia-candidate (outside my list, not checked). |
| 124 | cor:mixed-every-fixed-modulus-all-degrees-candidate | read; deduction right | Combines the all-odd and all-even mixed theorems (outside my list, not checked). |
| 24, 21, 16, 27, 19, 31, 26, 17, 32 | auto:A_monodromy:9292c61fd3ca, 2b2a821f869e, 0638c557453d, ac724428800d, 1e009f1c7aa8, ee94dcb570ad, 9f1f96604bfd, 0c2f1cb265b6, feea204b71c7 | read; not rerun | Scope remarks and records of the certificate programs (seeds, timings, failed candidates kept). They are records, not statements to prove; I found nothing inconsistent with the surrounding theorems. |

### Batch 9 (A_monodromy.tex 21438-29242: nonordinary principal surfaces, degree assembly, Moore/Fermat, dual Cartier ranks)

| # | Row | Check | Result |
|---|---|---|---|
| 128 | cor:nonordinary-genus-two-no-three-torsion-triple-candidate | targeted proof check of the deduction | Right given lem:char2-genus-two-three-total-ramifications-candidate (outside my list): h^0(3Q) = 2, the pencil is basepoint-free, so 3P ~ 3Q ~ 3R would give a degree-3 map totally ramified at three points. |
| 130 | cor:nonordinary-theta-three-torsion-nodal-norm-candidate | targeted proof check | Right given the 2-rank-one normal form lemma: a tangency forces 3(P-W) ∈ {0, W'-W}, hence P ∈ {W, W'} by |3W| = W + |K| and |K+W'| = W' + |K|; each type {g,-g} gives C·(C+g) = 2 nodes, total \|K\|-1. |
| 111 | cor:abstract-Pfaffian-common-incidence | independent re-proof of the example | Right: at s = e_0+e_2, M_s(t) = (t_1, t_1, t_2+t_0, t_3, ..., t_2m) (recomputed from (PH2.7)), rank N-1, left kernel e_0* + e_1*. |
| 309 | lem:DE-A4-product-Frobenius-interpolation | independent re-proof | Right: F_*L = E_1 ⊠ E_2; dual evaluation images U_1(q_1) ⊗ U_2(q_2) with (A⊗B) ∩ (A'⊗B') = (A∩A') ⊗ (B∩B'); 4 + 4 - 1 = 7 for distinct coordinates, 6 if one agrees. So two general points do not impose independent conditions although 8 < 9. |
| 102 | cor:DE-SS-odd-rectangle-dual-rank | targeted proof check of the deduction | Right given thm:DE-SS-odd-pullback-dual-rank (outside my list): odd-degree endomorphisms from lem:DE-A3-ss-norm are étale, and the pullback of O(O) is O(aO) because an odd-order kernel sums to zero. |
| 142 | cor:ss-product-two-axis-reduced-deformation-open | targeted proof check | Right: the bad locus is closed with closed image by properness and misses the product point. |
| 134 | cor:principal-theta-odd-cover-dual-rank | targeted proof check | Right given the preceding proposition (coefficients θ(a_χ)^2): (n-1)/2 nonsingular inverse-pair blocks, the trivial summand pairs to zero (C(ω) = 0 in 2-rank zero), rank n-1. |
| 313 | lem:DE-Fermat-affine-lines | targeted proof check | Right: on a line subgroup the determinant is the product of three expressions (DE-MF4); modulo the smooth (irreducible) Fermat cubic it is ∏(cube sums)·(∏x_h)^3, so one cube sum vanishes; 81 = 9 + 72 configurations. |
| 315 | lem:DE-Fermat-full-and-eight | targeted proof check (concurrent case re-derived; the non-concurrent algebra read, its ideal certificate not rerun) | Concurrent case right: the four lines through h cover every other point once, so their cube sums add to Σc^3 + 3c_h^3 = Σc^3 + c_h^3, forcing c_h = 0. |
| 314 | lem:DE-Fermat-coefficient-reductions | read; certificate not rerun | A computational reduction (55,296 monomials, 511 supports); the coefficient (Σc_g^3)^3 of ∏x_g and the line cubes are as described. |
| 133 | cor:ppav-odd-cover-maximal-dual-Cartier | targeted proof check | Right given the cross-determinant theorem and the rank-8 trivial block: rank 8 + 18(n-1)/2 = 9n-1, the maximum for an alternating form on a space of odd dimension 9n. |
| 121 | cor:fixed-ppav-all-odd-maximal-dual-Cartier | targeted proof check | Right: a maximal isotropic K ⊂ A[d] of order d^2 gives a principal symmetric M_0 on B with π*M_0 = O(dΘ); apply #133 with n = d^2. |
| 129, 110, 127, 119, 120, 115, 126, 118, 116, 117 | cor:nonordinary-ppav-uniform-root-inertia-candidate, cor:RD-A4-powers-three, cor:nonordinary-even-three-power-sums-candidate, cor:f0-three-five-degree-groups-candidate, cor:f0-three-five-seven-degree-groups-candidate, cor:f0-all-even-nine-theta-transfer-candidate, cor:nonordinary-all-odd-multiples-three-candidate, cor:f0-odd-multiples-three-five-seven-candidate, cor:f0-odd-multiples-eleven-candidate, cor:f0-odd-multiples-thirteen-candidate | read; deductions right | Assemblies of transfer theorems outside my list (thm:RD-A4-three-step, the good-theta and nine-theta norm transfers, the even-addition theorem, the neighbour theorems). The arithmetic is right: d ≡ 0, 4, 2 (mod 6) as 3 + (d-3), 1 + (d-1), 5 + (d-5); with every degree divisible by 3, 5, 7, 11 or 13 known, the first open odd degree on a fixed 2-rank-zero surface is 17. |

### Batch 10 (A_monodromy.tex 29446-34055, A_nonordinary_ppav_Coble_ranks.tex 166-214, A_nonordinary_trigonal_direct.tex 124-144: odd principal systems, polar irreducibility, the main Lang orbit, wedge bounds, the uniform sparse section)

| # | Row | Check | Result |
|---|---|---|---|
| 105 | cor:DE-odd-principal-cube-kernel-birational | targeted proof check of the deduction | Right given prop:root-dual-kernel-differential and the common-incidence proposition (not checked): rank dκ = h-1 = dim U at one point gives separable dominance; the radical line of B_λ is the rational inverse. |
| 122 | cor:fixed-ppav-odd-full-hyperplane-inertia | targeted proof check of the deduction | Right given the odd-cover full-inertia theorem (not checked); a hyperplane radical on a space of rank r = 9d^2-1 has order 2^{r-1} = 2^{9d^2-2}, as stated. |
| 318 | lem:DE-Lang-polar-factor-covector | targeted proof check, every step re-derived | Right: δ_i q = ((Aσ)_i)^2 = 0 (A alternating, hence symmetric); the δ_i commute and square to zero in characteristic two; f divides δ_i f, so δ_i f = f L_i; δ_s^2 = 0 gives δ_s L_s = L_s^2 (DE-LP9); on the Lang scheme δ_s y = y, so L_s^2 = L_s, an F_2-valued additive covector, invariant under (s,y) ↦ (as, a^{-1}y); if it vanishes, D^t s ∈ ks generically, D = aI, and (DE-LP9) gives a^2 (s^t y)^2 = 0, so a = 0 and B(y^{[2]})∇f = 0. Not seen: the parity argument for q ≠ 0, which needs (DE-LP4). |
| 104 | cor:DE-odd-polar-main-component | targeted proof check | Right given the polar-irreducibility theorem, thm:nonordinary-ppav-all-covectors and prop:DE-common-Cartier-incidence (not checked). Re-derived: y = λ^{[1/2]} gives (y^t s_0)^2 = λ(s_0^{[2]}) = 0, so q(y) = 0 at a point of maximal dual rank; on that open the s-solutions are an affine line in direction σ(y)^{[2]}; the Jacobian in y is the identity, so the N-dimensional incidence dominates. |
| 317 | lem:DE-Lang-main-orbit | targeted proof check | Right given the exact group-structure theorem and the complete common-wall theorem (not checked). Re-derived: for y outside the regular hyperplane, z = ay satisfies M_s^t z^{[2]} = a z, so the reduction has z̄^{[2]} ∈ kλ_0 and B(z^{[2]}) keeps rank N-1; K lies in H because the full radical fixes K; hence the main component is the orbit V∖K, of degree 2^r - 2^{dim K}. |
| 316 | lem:DE-Lang-block-slice-bound | targeted proof check | Right: K ⊂ gH for g ∈ G_0, the GL(V_0)-orbit of a nonzero functional spans V_0^*, and the common kernel of the extended functionals is V_1. |
| 103 | cor:DE-general-source-principal-divisor-bound | targeted proof check of the deduction | Right given the preceding proposition (not checked): 9(d^2-e^2) + (9e^2-1) = 9d^2-1; the degree bound follows from the main-orbit formula; e = 1 gives the bound 8. |
| 113 | cor:compatible-cyclic-principal-prime-criterion | targeted proof check of the deduction | Right given the CCI theorem (not checked): T_H^2 = 2ℓ, and d_1 d_2 = ℓ prime with d_1 dividing d_2 forces type (1, ℓ); a rank-two kernel of order ℓ^2 has ℓ+1 lines. |
| 101 | cor:DE-Lang-wedge-cyclic-principal-bounds | targeted proof check of the arithmetic | Right given the wedge theorem (not checked): type (3, 3ℓ), N = 9ℓ, (9ℓ-1) - 3ℓ = 6ℓ-1; for the system 3dΘ, N = 9d^2, and d = 1 gives K = 0. The clause on "the degree e" (one of 3ℓ, 6ℓ, 9ℓ) uses a symbol the statement does not define (presentation erratum). |
| 106 | cor:DE-prime-compatible-wedge-bound | targeted proof check, all numbers recomputed | Right given (DE-CR4), (DE-CR6) and the theorem (not checked): 8 + (ℓ+1)(3ℓ-8) = 3ℓ^2-5ℓ; the complement (ℓ+1)(6ℓ-1) = 6ℓ^2+5ℓ-1 agrees with the sum of the source wedge bounds; F_2[C_ℓ] is semisimple with nontrivial simples of dimension f = ord_ℓ(2); at ℓ = 17, f = 8, 8·⌊101/8⌋ = 96, 18·96 = 1728, 9·289-1 = 2600, 2600-1728 = 872. |
| 140 | cor:root-primitive-permutation-Lang-components | independent re-proof | Right: for n odd each nonzero class of F_2^B/constants has a unique representative of size j ≤ (n-1)/2; the sizes C(n,j) sum to 2^{n-1}-1; n = 5 gives 5 and 10. |
| 123 | cor:generic-nonordinary-ppav-finite-degrees-candidate | targeted proof check of the spreading-out argument | Right given the preceding theorem and the frame-component lemma (not checked): finitely many dense opens, descent to a finite field, a closed point. The Stacks tag 0559 was not opened. "-candidate" label on a proved row. |
| 301 | lem:DE-A3-ss-Frobenius-endomorphisms | targeted proof check, every step re-derived | Right: Frobenius zero on H^1 gives h^0(B^1) = 1, so B^1 = O and U is nonsplit; C(dx) = C(x^2 dx) = 0, C(x dx) = dx; dim End U = 2; H^1(O) → H^1(End U) is dual to the trace on global endomorphisms, which is zero; x + t^{-2} = y/x^2 for t = x/y (recomputed from y^2 + y = x^3), so mult_x is a global class modulo scalars; the matrices [[0,X],[1,0]] and [[0,1],[0,0]] are right. |
| 304 | lem:DE-A3-ss-uniform-sparse | targeted proof check, every displayed value recomputed | Right. Recomputed: the pole orders 2q-1, 2q, 2q-3; the p-basis rows a, b (from y = y^2 + x·x^2); the rank-drop locus (β ≠ 0: Q_ζ and Q_{ζ^2}, which needs 3 dividing q/2; β = 0: the minor equals 1+u because 1+u = x^3u^2, and it cannot vanish); the local form Ψ = (a+td, tf, e), its kernel and the trace-zero submodule; deg K = 2; the condition αλ + β = 0 at Q_λ and its independence for λ = ζ, ζ^2; b(Q_λ) = (0, λ, λ^2), (A,B,C)(Q_λ) = (0, 1, λ^2), (∂A,∂B,∂C)(Q_λ) = (0, λ^2, λ); the kernel-to-cokernel matrix [[ζ,1],[ζ^2,1]] with determinant 1. The identification of H^0(Ψ) with C_{s_q} was checked only on the second-factor Cartier values C(z dz) = dz, C(w dz) = z dz, C(zw dz) = w dz; lem:ss-rectangular-even-bound was not checked. No computer run. |
| 137 | cor:root-nonordinary-Lang-rank-four-excluded-candidate | targeted proof check | Right given the preceding rank lemma and the nonproportionality of q with the Fermat cubic (not checked): the rank-at-most-four part has dimension at most 3 + 5 = 8 < 9; x^{[2]} spans the kernel at rank eight, so compatibility is Σx_a^3 = 0; the Fermat cubic is smooth in characteristic two, hence integral; the affine-line torsor has dimension 9 and dominates by étaleness. |
| 138 | cor:root-nonordinary-theta-no-three-triples-candidate | targeted proof check of the deduction | Same argument as #128: 3P ~ 3Q ~ 3R and h^0(3Q) = 2 give a degree-three map totally ramified at three points; right given the same lemma (not checked). |

### Batch 11 (A_ppav_two_jets, A_product_degrees, A_route_limitations(_29), A_surface_counterexample; B.tex 210-1937: torsion levels, tame and wild bounds)

| # | Row | Check | Result |
|---|---|---|---|
| 132 | cor:ppav-discriminant-one-node | targeted proof check | Right given the rank-stratum dimension bounds of the two-jet lemma (not checked): the one-point incidence is a P^5-bundle over A (dimension 7); for integrality, t = Θ·B ∈ [1,5], Hodge index gives B^2 ≤ t^2/2, so B·D ≥ 3t - t^2/2 ≥ 5/2, hence at least 3, while two components of a curve with one ordinary node meet with multiplicity at most 1. |
| 33 | auto:A_ppav_two_jets:0557c5a87cfe | carried as background without fault found | Scope remark (Bauer-Szemberg, Alvarado-Pareschi not imported in characteristic two); no mathematics to check. |
| 108 | cor:OC-all-prime-product-degrees | targeted proof check of the deduction | Right given the two surface bounds and the product criterion (not checked); 2d ≥ p+1 for d ≥ p^2-p holds for every prime (2p^2-3p-1 ≥ 0); at p = 2 the bound d ≥ 2 is exact because degree one fails. |
| 144 | ex:root-rational-residual-parabolic | independent re-proof | Right: P is a proper subgroup fixing U; the block-diagonal GL_r × GL_s (r, s ≥ 2) has no fixed vectors or covectors; the preimage of P in GL_d(Z_p) is open, hence Zariski dense. The retained program was not run (returned code is not executed). |
| 135 | cor:root-dual-kernel-birational | targeted proof check of the deduction | Right given prop:root-dual-kernel-differential (not checked): the radical line of B_ℓ recovers [s]. |
| 143 | ex:root-kernel-compression-countermodel | independent re-proof | Right in characteristic two (which the setting assumes; b(s,s) = 2ℓ_0(s)s): for ℓ_0(s) ≠ 0 the right kernel is ks and the image is ker ℓ_0, so κ is constant [ℓ_0]; B_ℓ = ℓ_0 ∧ ℓ. |
| 109 | cor:OC-surface-exact-degrees | targeted proof check, all numbers recomputed | Right given the eigensheaf formulas of the construction (not checked): g(y^2+y = x^15) = 7; pole semigroup ⟨2,15⟩ gives h^0(N) = 2, h^0(N^3) = 4, h^0(L) = 6; for r = 1, (m_0,m_1,m_2) = (1,2,2) and the contributions 0, N^{-2}, O give h^1(L^{-1}) = 1; for r ≥ 2 the exponent 1-r < 0; h^0(L^9) = 210 + 186 + 160 = 556 (degrees 18+6a, 22+6a, 26+6a, all above 12); 6 + 556 sections give P^561. This agrees with the r = 556 recomputed in batch 1. |
| 70 | cor:B-RD6 | targeted proof check | Right, and agrees with part 1 (targeted proof check, confirmed): the Serre-Tate canonical lift has p-divisible group μ_{p^∞} ⊕ Q_p/Z_p, so E'[p] ≅ (Z/p)^2 over K ⊇ μ_p; inertia trace 2 against -2 at the inertia involution. |
| 238 | lem:B-RD9 | targeted proof check (the cubic itself taken from thm:B-RD8, not recomputed) | Right: with v(3) = e, v(w) = r, 2r < e, the coefficients have valuations e+4r, e+3r, e+2r with unique lowest terms; the Newton polygon has one slope -(e+4r)/3 and 3 ∤ e+r gives a totally ramified cubic; v(x_0) = e+2r; f'(x_0) = 9 g'(X_0) with v(g'(X_0)) = e+3r, so v(3x_0^2+a) = 3(e+r); the substitution x = x_0 + u^2 X, y = u^3 Y gives Y^2 = X^3 + (3x_0/u^2)X^2 + X, middle valuation (e+r)/2 > 0, discriminant 16(c^2-4) a unit; v(Δ) = 9(e+r) forces the factor 4/gcd(4,e+r), the 2-division field (unramified 2-torsion under good reduction) the factor 3. |
| 61 | cor:B-RD11 | targeted proof check | Right given thm:B-RD7 and thm:B-RD2 (not checked here): (p^2-1)/6 > p-1 iff (p-1)(p-5) > 0; at p = 5 the defect is 6, the scaling by ϖ^{δ/12} over K(ϖ^{1/6}) keeps the residue field F_5, torsion parameters have valuation 1 = 24/24, and E[5](K) → F_5 (leading coefficient) is additive and injective, impossible on a 2-dimensional source. |
| 62 | cor:B-RD13 | targeted proof check of the arithmetic | Right given thm:B-RD12 (not checked): n-1 ≤ s, 2n-2 ≤ L, 4n-4-s ≤ L solve to n ≤ 1 + min(s, ⌊L/2⌋, ⌊(L+s)/4⌋). |
| 46 | auto:B:b9f011fa8019 | independent re-proof | Right: a split Tate curve with q = a^{p^n} and μ_{p^n} ⊂ K has full rational p^n-torsion (ζ^i a^j). |
| 147 | lem:B-RD14 | independent re-proof | Right: normalize the Weil-pairing form to have a unit value; trivial action on T_p/p^n gives (χ_p(σ)-1)b ≡ 0 mod p^n. |
| 148 | lem:B-RD17-common | targeted proof check, every step re-derived | Right: Zassenhaus refinement Q_ij; finite flat models by schematic closure; special Dieudonné modules generated by at most h_i (resp. h'_j) elements; φψ = ψφ = p^{2c}; on each ζ-eigensummand (integral idempotents, m prime to p) kernel and cokernel have length at most 2c h_i, 2c h'_j; summing, \|n(a_ζ - b_ζ)\| ≤ 2c Σ h_i h'_j = 2ch^2 < n. |
| 149 | lem:B-RD17-degree | targeted proof check | Right given Kisin 2006 Cor. 2.2.6 and Fontaine 1994 (cited, not opened): dim_{Q_p} End_F(D) ≤ (2h)^2 = d by the fixed-vector independence argument; the image H of inertia embeds in GL_{≤d}(Z_p) and injects into GL_d(F_p) (p odd) or GL_d(Z/4) (p = 2); \|GL_d(Z/4)\| = 2^{d^2}\|GL_d(F_2)\|; J = ker(I_0 → H) is normal; e(L/K) = \|H\|; the lattice step (quotient by the closure of T/p^a T_0) gives Tate lattice p^{-a}T. |
| 38 | auto:B:5338697ffdba | carried as background without fault found | Scope remark; consistent with thm:B-RD17 and prop:B-RD4. |
| 63 | cor:B-RD18 | targeted proof check of the deduction | Right given (B-RD18.1) (not checked): with m = p+1, m e/(p^2-1) = e/(p-1), so L agrees with cor:B-RD13. The statement uses s without defining it (s = v_p(e/(p-1)), as in B-RD13): presentation erratum. |
| 48 | auto:B:c9c8e4df645d | carried as background without fault found | Finite certificate (verify_honda_bounds.py) not run; it checks integer arithmetic only, as it says. |
| 150 | lem:B-RD19 | targeted proof check | Right: if v(j) < 0, E is the quadratic twist of a Tate curve by ε, E[p]^ss = ε̄χ̄_p ⊕ ε̄, trivial forces ε̄ = 1, hence ε = 1 for p odd, so E is split multiplicative. |
| 151 | lem:B-RD20-wild | targeted proof check | Right given prop:B-RD3 and the Hesse-pencil results of Anema-Top-Tuijp (cited, not opened): δ ≡ 0 (mod 3) since Δ is a cube; v_L(u) = mδ/12 is divisible by 3 for m = 3, 6, 12; the invariant differential b_0 ω_K with b_0 ∈ F; the translation x ↦ x + r on y^2 = x^3 - x gives t ↦ t + r t^3 + ... in t = -x/y; v(σx - x) = 3v(x) against v(σx - x) ≥ v(x) + b with equality when 3 ∤ v(x); the case A = B with 3 ∤ A: the leading coefficients satisfy c̄X^3 = dX, whose roots form one F_3-line, while the leading-coefficient map from F_3^2 is injective. |
| 64 | cor:B-RD21 | targeted proof check, arithmetic re-derived | Right given prop:B-RD20 and (B-RD20.3) (not checked): N_w ≤ N_t + 1; the gap occurs iff k ≤ s ≤ 2k-1 and L = 4k-s-1 (the case max = 2k is excluded by s ≤ L); for k = 1, e/2 ∈ {12, 15, 21, 24}, so e ∈ {24, 30, 42, 48}. The defect assertions were not checked. |
| 45 | auto:B:b02333f8ed15 | carried as background without fault found | Pointer remark. Checked: the k = 2 gap band has smallest e = 216 (s = 3, L = 4, e/2 = 108), as stated. |

### Batch 12 (B.tex 2222-3665: the wild trace arc, the exact characteristic-three range, the height-two formal group at 3)

| # | Row | Check | Result |
|---|---|---|---|
| 47 | auto:B:c83d5f781371 | carried as background without fault found | Certificate remark (verify_level27_basechange_obstruction.py); not run. |
| 152 | lem:B-RD26-trace-arc | targeted proof check (identities recomputed; the regularity of the Drinfeld-level ring, Carter-Strauch 2021, and the weighted factorization from thm:B-RD12 taken as given) | Right as far as checked. Recomputed: (B-RD26.1) is exactly the total weight of the primitive 3^n-torsion coordinates (2·3^{2n-1} of weight 1, 4·3^{2n-j-2} of weight min(A, 3^{2j}) for 1 ≤ j ≤ n-1, 2·3^{n-1} of weight A), as it must be since 3 is a unit times their product; disc(Y^2 = X^3+uX^2-X) = 16(u^2+4); log T = T - uT^3/6 + ... gives [3]_{T^3} = 4u; the 3-division polynomial 3X^4+4uX^3-6X^2-1; the F_3[X] identity (with f = X^3-X, X^9-X = f^3+f); h(T) = T(1+T^2)^{-1/2} from X ↦ X+1; u ∈ m^{6M} from the sixth elementary symmetric function; the expansions (B-RD26.8) (D_y = 3y^{-4}+6y^{-2}+5, ∏(w+j) = w^3+3w^2+2w) and (B-RD26.9) (6a = 2A); the simple root at Z = c; τI = -I, τU_y = -U_y, τZ = i^{1-A}Z, and 4 \| d when A is odd. |
| 34 | auto:B:10f3741cc5dc | carried as background without fault found | Certificate remark (verify_wild_trace_arcs.py); not run. |
| 65 | cor:B-RD27-exact-three | targeted proof check of the arithmetic | Right given thm:B-RD26-wild (not in my list) and agrees with part 1 (consistency check): N(e) is N_w of cor:B-RD21; (B-RD27.2) is equivalent to n ≤ N_w (u ≥ 3^{2n-3} and u ≥ 3^{4n-5-s}); at e = 216, u = 108, s = 3, L = 4, N = 1 + min(3, 2, 2) = 3. The exact defect twelve at e = 216 was not checked. |
| 40 | auto:B:688dec0e6255 | carried as background without fault found | Scope remark. |
| 153 | lem:B-RD29-isogeny-Tate | independent re-proof | Right: φ̂ maps B[r] onto ⟨P⟩ with kernel μ_r (any preimage of P is r-torsion because φφ̂ = [r]); the extension class lies in H^1(K, μ_r) = K^×/K^{×r} and is realized by T_q[r] with v(q) > 0 after multiplying by an r-th power; the Tate curve's graded pieces μ_{p^∞}, Q_p/Z_p give character 2. |
| 42 | auto:B:7f506124b28c | carried as background without fault found | Certificate remark (verify_p3_character_level2.py); not run. Pointer to thm:B-RD42. |
| 49 | auto:B:cb3f24f10664 | carried as background without fault found | Cites Bondarko 2006 Theorem E(1) (not opened); used only for actual formal BT groups, as it says. |
| 154 | lem:B-RD31-finite | targeted proof check | Right: AF = FA for F = [[0,3],[1,0]]σ gives exactly A(a,c) = [[a, 3σ(c)],[c, σ(a)]] with a, c ∈ Q_9 (recomputed); det = N(a) - 3N(c) ≠ 0, so a quaternion division algebra; P = C_3 (no element of order 9, degree 6 > 2); C_H(P) ⊂ μ_6; \|H\| ≤ 12; joint images: 9·4 = 36, 3·8 = 24, 8 (a cyclic subgroup of C_{t_1} × C_{t_2} has order at most lcm). |
| 155 | lem:B-RD31-point | targeted proof check, every step re-derived | Right: j b_j ≡ 0 (mod 3) from the invariant differential, b_3..b_8 ∈ m by height, so v([3]x) ≥ min(a+v, 1+3v, 9v); an order-3 point has v ≤ (a-1)/2 (unique lowest term 3y otherwise, including the a = 1 case); v_{i+1} ≥ 3v_i + 1 from v_0 ≥ 1 gives v_{n-1} ≥ (3^n-1)/2, hence a ≥ 3^n. |
| 44 | auto:B:a26975327b26 | carried as background without fault found | Certificate remark (verify_height_two_small_bounds.py); not run; pointer to thm:B-RD42. |
| 156 | lem:B-RD32-norm | targeted proof check | Right: -1 is the only involution; norm 1 on μ_6; no nonabelian group of order 6 (its involutions would be noncentral); in order 12 the Sylow 2-subgroup is cyclic of order 4 with j^2 = -1, norm 1; an element of order 8 lies in Q_9 with norm ζ_8^{1+3} = -1; reduced traces 2, -2, 0 for orders 1, 2, 4. |
| 41 | auto:B:72e408a14989 | carried as background without fault found | Certificate remark (verify_height_two_character_gate.py); not run. |
| 35 | auto:B:18f97bffbcfd | carried as background without fault found | Scope remark citing Bondarko 2006 Theorem 5 (not opened). |
| 158 | lem:B-RD34-log | targeted proof check, every step re-derived | Right: U([3]X) J = 3U(X) makes J divisible by 3, so coefficients of monomials with an exponent prime to 3 are divisible by 3; the valuation recursion; v(c_α) ≥ -a min v_3(α_j) ≥ -a⌊log_3 m⌋ and 3^r - 1 ≥ 2r give v(c_α z^α) ≥ q + (m-1)(q - a/2) ≥ q; log([3]^u z) = 3^u log z. |

### Batch 13 (B.tex 3666-5958: the refined kernel estimate, integral conjugacy at 3 and 2, the level-27 test at e = 2, the dyadic point bound)

My own verifier for this batch: `agent_notes/afcdf31bb407576f5_work/check_b13.py` (copied from the scratchpad; sympy): it confirms Δ(E) = a_3^3(a_1^3-27a_3), the isogenous curve (B-RD41.1) through the map (B-RD41.4) modulo the source equation, the normalized differential, c_4(E_1) and Δ(E_1) of (B-RD41.2), j(E_1) of (B-RD41.3), c_4 and Δ of (B-RD37.3), and both j-identities of (B-RD42.13). All True.

| # | Row | Check | Result |
|---|---|---|---|
| 157 | lem:B-RD34-kernel | targeted proof check of the new steps (Bondarko 2006 Props. 6, 8-12, 16, Lemma 3, Theorem 2(8) cited, not opened) | Right as far as checked: (B-RD34.7) from lem:B-RD34-log; (B-RD34.8) from f z = 3(z - z(0))Δ^{-1} by induction (integral constant terms) and 3R ⊂ J; the numbers: q_2 = 2a+1 (a ≤ 2), a+4 (3 ≤ a ≤ 9), 13 (9 ≤ a ≤ 24), each > a/2; at a = 72, q = 1, 4, 13, 40 and 40 > 36. |
| 36 | auto:B:2b832ed8e5d4 | carried as background without fault found | Certificate remark (verify_supersingular_log_bound.py); not run. |
| 159 | lem:B-RD35-conjugacy | targeted proof check, every identity re-derived | Right: Aut(y^2 = x^3-x) has order 12; jζj^{-1} = ζ^{-1}; (ζ-1)(ζ^{-1}-1) = 3, so v_D(ζ-1) = 1; (ζ-1)j(ζ-1)^{-1} = -ζj ∈ H_0; d = z+ζ+1 conjugates z to ζ (both satisfy X^2+X+1); d = t+j conjugates t to j; q = ζ-ζ^{-1} has q^2 = -3 and qjq^{-1} = -j; in order 12, t = bj with b b̄ = 1, c = 1+b (or ζ-ζ^{-1} if b = -1) has c/c̄ = b and c^{-1}tc = j. |
| 39 | auto:B:665ea52b93eb | carried as background without fault found | Reduction remark (integral Weierstrass coefficients); asserts no existence, as it says. |
| 37 | auto:B:4074b39ba0d6 | carried as background without fault found | Certificate remark (verify_elliptic_inertia_conjugacy.py); not run. |
| 160 | lem:B-RD37-patterns | targeted proof check, with my own computation of (B-RD37.3) | Right given prop:B-RD36 for the last column (not checked): v(t) = -a gives v(j) = 6-3a, so a = 1; (ζ-1)^2 = -3ζ; for (r,1,1), v(t^3-1) = r+2 and t^3+8 = (t^3-1)+9 with v(9) = 4 give v(j) = 6, ≥ 6, 12-3r, so r ≤ 3; δ = 6+3S = -3, 6, 15, 18, 21; the residue classes modulo 3 are disjoint also after negation and permutation. |
| 161 | lem:B-RD37-units | independent re-proof | Right: x̄ = 1 in characteristic three, and 3w + 3w^2 + w^3 has valuation at least 3 when v(3) = 2. |
| 162 | lem:B-RD39-units | independent re-proof | Right: (1+πw)^3 = 1 + π^3(w + πw^2 + w^3), solvable by Hensel; the depth is 1 or 2 and independent of t (cubes of t, t + πm differ by π^3); over L with v_L(3) = 6 the three terms have valuations 6+r, 6+2r, 3r. |
| 163 | lem:B-RD41-isogeny | computation or formal certificate (my own sympy check) | Confirmed: (B-RD41.1) is satisfied by the map (B-RD41.4) modulo the source equation, the differential is normalized, and (B-RD41.2), (B-RD41.3) hold. The degree and kernel argument (pole divisor 2(O + (0,0) + (0,-a_3))) is right. |
| 164 | lem:B-RD42-normal | targeted proof check | Right given prop:B-RD36 and prop:B-RD38 (not checked): v(c_4) = (δ+6)/3; with v(48) = 2, v(864) = 6, v(1728) = 6 the coefficient valuations are (2, ≥0), (4, ≥3), (6, ≥6), and the last scales down; ψ_3/3 = x^4 + 6ax^2 + 4Bx - 3a^2; its Newton polygons for v(B) = 0, 1 (recomputed) have a root of unique valuation; v(B) ≥ 3 would give good reduction over K(√π); r^3 - 3r + 3b has v(r) = 2/3 and discriminant 27(4-9b^2), a square; the substitution x = π^2X + πr, y = π^3Y gives (B-RD42.4) exactly; with D_b D̄_b = 1, u^3 = iD_b gives u^3 + u^{-3} = -3b, so u + u^{-1} is a root; D_b ≡ 1 + (3i/2)b has deviation of valuation 2, so it is not a cube, and D_b D_{b'}^{±1} ≡ 1 + (3i/2)(b ± b') gives (B-RD42.2). |
| 165 | lem:B-RD42-reverse | targeted proof check of the algebra (Fisher 2015 equation (11) and prop:B-RD40's multiplier identity taken as given) | Right as far as checked: RSR^{-1} = S^{-1} = -S; h(t) = (t+2)/(t-1) is an involution; (B-RD42.11) expands correctly; v_F(T'-T) ≥ 2+3+1; (B-RD42.13) (my sympy check); H - 4 = (T^2-12)/(T+3); H^3 ≡ 64 + 16π^4 d and 64/(1-9b^2/4) ≡ 64 + 16π^4 b^2 give d ≡ b^2, the first identity gives d ≡ 2a, hence (B-RD42.14) and b̄'^2 = b̄^2. Step (B-RD42.9) (residue -1 of the cocycle ratio) was followed but rests on prop:B-RD40. |
| 166 | lem:B-RD44-conjugacy | targeted proof check, every identity re-derived | Right: no element of order 8 in a quaternion algebra over Q_2; two order-4 elements in different cyclic groups generate Q_8; the common anticommutant of i, j is Q_2·ij; C_4 ⋊ C_3 would contain an element of order 12; the 24 maps (B-RD44.2) are automorphisms exactly when t^2 + t = s^3 (substituted); the eight with u = 1 square to [-1]; ζ = (-1+i+j+ij)/2; conjugation by i - j sends i ↦ -j, j ↦ -i, hence ζ ↦ ζ^{-1}; b = 1+c (or i) has b/b̄ = c; 1+i sends j to ij. |
| 167 | lem:B-RD44-point | targeted proof check | Right given Tate's algorithm table (cited, not opened): a_1 ∈ 2O (Hasse invariant, or c_4 ≡ a_1^4 mod 2); [2](T) = 2T - a_1T^2 + ... has unique lowest term 2T on the maximal ideal; E_0/E_1 = G_a has exponent 2 and the component group's 2-part exponent at most 4, so [8]P = 0. |

### Batch 14 (B.tex 6041-7592: dyadic graph estimates, the cubic part of dyadic inertia, the level-8 models, the p^2 tests at p ≥ 5)

My own verifier for this batch: `agent_notes/afcdf31bb407576f5_work/check_b14.py` (sympy): Norm_{K(θ)/K} q_θ(t), computed as a resultant, equals (B-RD48.5), and 6Aθ^2 - 9Bθ + 4A^2 = 𝒟/γ modulo θ^3 + Aθ + B. Both True.

| # | Row | Check | Result |
|---|---|---|---|
| 50 | auto:B:e906eee05992 | carried as background without fault found | Scope and certificate remark; certificate not run. |
| 168 | lem:B-RD45 | targeted proof check (Bondarko 2006 at p = 2 and prop:B-RD44-realization taken as given) | Right as far as checked: e_0 = (1+τ+τ^2)/3 is 1 on the factor where τ = 1 and 0 where τ^2+τ+1 = 0; the rank-2^b subgroup of a one-dimensional connected formal group is ker F^b; exponents r + r by isotropy; the recursion min(a+q, 1+2q, 4q); v(c_α z^α) ≥ q + (m-1)(q-a) since ⌊log_2 m⌋ ≤ m-1; the map P → Q × M has special kernel 0 × ker F^n, and F^u with u < n leaves rank 2^{n-u} > 1. |
| 43 | auto:B:a2534788021e | carried as background without fault found | Certificate remark; not run. It records a first-draft crossing formula that omitted a = 3, corrected without changing (B-RD45.6). |
| 169 | lem:B-RD46-discriminant | targeted proof check | Right given lem:B-RD44-conjugacy (checked in batch 13): m ∈ {1,2,3,4,6,8,24}; Δω^{12} is invariant, so 12 v_L(c) = -mδ; for 3 ∤ m, 3 \| δ; for 3 \| m the order-3 element acts on the special cotangent line by ζ^{-v_L(c)}, nontrivially (an order-3 automorphism tangent to the identity linearizes by averaging), so 3 ∤ v_L(c) and v_3(m) = 1 give 3 ∤ δ; traces 2 and -1. |
| 170 | lem:B-RD47 | targeted proof check, the whole table recomputed | Right: the 2-isogeny (B-RD47.1) is the standard one; the target 2-division discriminant is 16b; 1 + 4O ⊂ squares by Artin-Schreier and Hensel; Δ = 16b^2 D, c_4 = 16(a^2-3b), v(j) = 8 + 3v(a^2-3b) - 2β - v(D); the four cases give (v(D), v(Δ), v(j)) = (2,6,6), (3,7,5), (2,8,7), (3,9,6), the excluded cases make D or b a square, and 3 \| \|H\| iff 3 ∤ δ iff v(D), v(b) have different parities. |
| 171 | lem:B-RD48-models | targeted proof check (Chen 2014 models and Fisher 2010 taken as given) plus my own computation | Right as far as checked: det [[u, -T_v],[v, T_u]] = uT_u + vT_v = 6T for T of degree 6; (B-RD48.5) and the multiplier-three coefficient 𝒟/γ confirmed by check_b14.py. The identity a_E^3 - b_E^2 = (c^3-d^2)Φ_E^4 needs Chen's Appendix polynomials, which are not in the return text I read; not checked. |
| 173 | lem:B-RD49-point | targeted proof check, every step re-derived | Right given Hopkins-Gross 1994 for the shape (B-RD49.2) (cited; I rederived c_p = (1-p^{p-1})u from log T = T + (u/p)T^p + ...): order-p points have v ≤ a/(p-1); b ≥ a is impossible; Z = b + pA is forced; at [p]x cancellation forces a + Z = b + pZ, so a = p(b + (p-1)A), contradicting p ∤ a. |
| 172 | lem:B-RD49-inertia | targeted proof check | Right, and agrees with part 1 (confirmed given lem:B-RD17-degree, which I checked in batch 11): no element of order p in D for p ≥ 5; finite subgroups embed in F_{p^2}^×; tame cyclic; lcm divides p^2-1. |
| 174 | lem:B-RD50-boundary | targeted proof check (Bondarko 2006 inputs taken as given) | Right as far as checked: q = min(a+1, p+1, p^2) ≥ a/(p-1) exactly when a ≤ p^2-1 (the binding term p+1); ⌊log_p n⌋ ≤ (n-1)/(p-1); equality q = a/(p-1) is harmless; m^{-[a/(1-p)]} = π^{⌈a/(p-1)⌉} = J; pR ⊂ J. |
| 66 | cor:B-RD50-remaining | targeted proof check | Right given thm:B-RD49 (nonsquare determinant; not checked): the twist to a primitive η; norm λ^{p+1} primitive iff gcd(c, p-1) = 1, so c is odd and gcd(c, p^2-1) = gcd(c, p+1) is odd; m = (p^2-1)/gcd(d_1,d_2); p = 5 gives m = 24, 8; p = 7 gives 48. |
| 175 | lem:B-RD51-orbits | independent re-proof | Right: gcd(m, p+1) = q, image of λ ↦ λ^{p+1} is μ_{p-1}; λ ↦ λ^p is an involution on the fibre without fixed points (a fixed point has norm λ^2, not primitive); q/2 orbits; for q ≥ 4 a primitive m-th root with norm η exists via (Z/m)^× ↠ (Z/(p-1))^×. |
| 67 | cor:B-RD51-p5 | independent re-proof | Right: d = 3 gives q = 2, excluded; for m = 24 the fibre is e ≡ 1 (mod 4); multiplication by 5 pairs {1,5}, {9,21}, {13,17} with orders 24, 8, 24; adding 12 swaps A and C and fixes B; two patterns {A,B}, {A,C}. |

### Batch 15 (B.tex 7624-9200: potentially CM groups, the first wild layer, the p^2 test at irreducible residual inertia, the ramification-break analysis)

| # | Row | Check | Result |
|---|---|---|---|
| 176 | lem:B-RD52-CM | targeted proof check | Right given Tate 1967 full faithfulness (cited): reduction of homomorphisms is injective (dividing by π^r and reducing f∘[p] = [p]∘f modulo π^{r+1}); the endomorphism algebra is a division algebra acting on V_p, hence a quadratic field E; ramified E: \|Γ\| divides 2(p-1), and for p ≡ 3 (mod 4) every λ with λ^{2(p-1)} = 1 has λ^{(p^2-1)/2} = 1 (since 4 \| p+1), so ψ is a square; for p ≡ 1 (mod 4) the determinants ±N(a) of units have square residue; unramified E: E^×Π has odd valuation, so Γ centralizes E; a nonsquare ψ(g) gives Z_p[ρ(g)] = O_E. Part 1 named this row only in its bridge section; this is the first check. |
| 177 | lem:B-RD52-LT | targeted proof check | Right given Hopkins-Gross 1994 and Lubin-Tate 1965 (cited): x = Σ v^i λ^{-i} satisfies vx = xλ and x ≡ N (mod Π), a unit; the tangent eigenvalue λ^{p-1} ≠ 1; Φ_2(T) = (pT+T^q)^{q-1} + p is the primitive p^2-torsion polynomial (g(g(T))/g(T) for g = pT + T^q) and is Eisenstein of degree q(q-1) = \|(O_E/p^2)^×\|; its wild Sylow subgroup survives the tame base change. |
| 178 | lem:B-RD53-leading | targeted proof check | Right given lem:B-RD49-inertia and Tate full faithfulness: a normal p-group fixes a nonzero vector, so irreducibility kills wild inertia; the product of the p^2-1 nonzero torsion coordinates gives (p^2-1)A = (p-1)t, A = t/(p+1); σ acts on ϖ^A by ζ^{(N/t)A} = ζ^{p-1}, giving α = ζ^{c+p-1}. |
| 68 | cor:B-RD53-quadratic | targeted proof check of the arithmetic (the cycle structure (B-RD53.3) of the preceding proposition taken as given) | Right as far as checked: at p = 7 the norm fibre is e ≡ 1 (mod 6), the four Frobenius pairs are {1,7}, {13,43}, {25,31}, {19,37} (7e mod 48 recomputed), and the quadratic twist (+24) exchanges opposite pairs of the displayed cycle; at p = 5, n = 3 gives a triangle. |
| 179 | lem:B-RD54-continuity | targeted proof check | Right given Hopkins-Gross 1994 Props. 14.7, 14.9 for the descent isomorphisms: W'_0(α) has valuation na (from w([p^n]T)[p^n]'(T) = p^n w(T) and W(α) = 0); Hensel with v(W_x(α)) ≥ b > 2na; canonical Lubin-Tate torsion differences have valuation a/((p^2-1)p^{2(r-1)}) ≤ a/(p^2-1) < na, so the balls are disjoint; additivity and equivariance by uniqueness. |
| 180 | lem:B-RD55-valuations | targeted proof check, every step re-derived | Right: after subtracting a first-level coordinate the Newton polygon is the single segment (0,α)-(q,0) because (q-j)α > (1-j/q)α; so primitive coordinates have valuation α/q; [F:L] = \|W\|; v_F = \|W\|t/((p+1)p^2) is an integer and p ∤ t(p+1), so p^2 divides \|W\| ≤ p^4. |
| 181 | lem:B-RD56-anti-layer | targeted proof check | Right given prop:B-RD53-cycle and lem:B-RD55-valuations: End_{F_p}(F_q) = {az + bz^p}; conjugation multiplies b by λ^{1-p}, of order h > 2 dividing p+1, hence not in F_p, so U is irreducible; W = U ⊕ (Cartan line); one break on U; the complement s·(-N^{-1}w); η^{p^3} = ζ and p^4 ≡ 1 (mod N) give η = ζ^p; A = p^3(p^2-1)/((p+1)p^2) = p(p-1), e_F = NqA. |
| 69 | cor:B-RD56-p5 | independent re-proof of the arithmetic | Right: with residual eigenvalues {c+4, 5(c+4)} mod 24, c = 1 and c = 21 both give {1,5} (order 24, projective ratio ζ^4 of order 6); c = 5 and 17 both give {9,21} (order 8, ratio ζ^12 of order 2); the special types are A = {1,5}, B = {9,21}, A, C = {13,17}. |
| 184 | lem:B-RD57-first-term | targeted proof check of the degree bookkeeping ((B-RD56.5) taken as given) | Right as far as checked: modulo ϖ^{qA+1} the ring has characteristic p (e_F > qA); ϖ^j first changes in degree j + p^{v_p(j)} b; with v_p(A) = 1 and b_0 = (q-1)A/p, b < b_0 forces j = A + (p-1)b and p ∤ b, b > b_0 forces j = qA - b; [p] raises leading coefficients to the q-th power, fixing z ∈ F_q. |
| 183 | lem:B-RD57-anti | targeted proof check | Right given prop:B-RD56-cubic-wild: σ acts on U by -1, so η^b = -1 and b ≡ N/2 (mod N), never b_0 = N(p-1); for breaks b_1 < b_2 both cases contradict the displacement valuation qA (Cartan-linear leading map, or all changes beyond qA). |
| 182 | lem:B-RD57-Cartan | targeted proof check, the p = 5 list recomputed | Right: Cartan breaks satisfy N \| c; b > b_0 is impossible in all three ranges of c; for b < b_0, c = qA - j = p b_0 - (p-1)b > b_0; at p = 5, N = 24, b_0 = 96, b ∈ {12, 36, 84} (60 removed by 5 ∤ b), c = 480 - 4b = 432, 336, 144, each divisible by 24. |
| 186 | lem:B-RD58-final-Cartan | targeted proof check | Right given the upper-numbering quotient compatibility (Serre 1962, Colmez; cited): v_E(T(P)) = p-1 prime to p gives the single break (q-1)(p-1) = b_0; ∩ H_v = 0 kills W^{>b_0}; det(1+pB) = 1 + p tr B, and L(μ_{p^2})/L has degree p with x = ζ_{p^2}-1 of valuation N and displacements of valuation pN, break b_0; a tame-fixed vector in S forces η^c = 1, so S lies in the centralizer Z = F_q of the irreducible tame generator, and surjectivity onto W/H_v forces S = Z; φ(c) = b_0 with S ⊊ W gives c > b_0. |

### Batch 16 (B.tex 9201-10727: anti-Cartan signatures, the reducible residual case, the arc construction, the mixed-case threshold, the weighted kernel estimate)

| # | Row | Check | Result |
|---|---|---|---|
| 185 | lem:B-RD58-anti-signature | targeted proof check | Right given lem:B-RD58-final-Cartan: D_U is a 2-dimensional F_p-space stable under η^b, which generates F_q, so D_U = d_U F_q and η^b ≠ 1; with A = q(p-1) (v_p(A) = 2) the leading change is (p-1)dz d_g^q in degree A + qb; for b > b_0 a polynomial a X^p + b'X cannot vanish on q points, and the Cartan element then has no change at qA; for b < b_0 the cancelling polynomial must be (p-1)dz(X^q - d_U^{q-1}X), the subspace polynomial of d_U F_q, giving K = A + Nb, J > A + (q-p)b and (B-RD58.6). |
| 188 | lem:B-RD59-final-bound | targeted proof check | Right: A + qc > qA as c > b_0; a coincident J/K change has coefficient a d_g^p + b d_g, which cannot vanish on the q leading coefficients of the final group Z; so both first changes are ≥ qA and one equals qA. |
| 187 | lem:B-RD59-anti-patterns | targeted proof check | Right: the subspace polynomial of span(a,b) is Y^p - Y(b)^{p-1}Y with Y = X^p - a^{p-1}X, whose linear coefficient Y(b)^{p-1}a^{p-1} ≠ 0 (expanded); one break: K = A + Nb, J ≥ A + (q-p)b, and J + pc - (K+c) ≥ (p-1)(c-b) > 0, A + qc - (K+c) = N(c-b) > 0; two breaks: the slope argument excludes A + qb_2 from the minimum, so J + pb_2 = K + b_2 and A + qb_1 = J + pb_1, giving (B-RD59.4) and b_1 < b_0. |
| 190 | lem:B-RD60-break | targeted proof check | Right, and agrees with part 1 (independent re-proof, confirmed). |
| 189 | lem:B-RD60-Newton | targeted proof check | Right given the Hopkins-Gross coefficient shape: the vertex (p,b) lies on the segment (1,e)-(q,0) exactly at b = ep/(p+1); the one-slope case gives a scalar or irreducible tame action, excluded by reducibility and the nonsquare determinant; two slopes give p-1 points of valuation (e-b)/(p-1) and q-p of valuation b/(p(p-1)); the line H is rational over L because L is the tame extension of degree N, which kills every tame character of order dividing p-1; e = (p-1)N gives b = (p-1)B, 0 < B < p(p-1), α > β; B ≡ c (mod p+1) from σ(a_p) = ζ^{(p-1)c}a_p (with the return's sign convention); the inverse step from β gives one segment and valuation B/p^3. |
| 191 | lem:B-RD61-point-field | independent re-proof | Right: the image on M[p^2] lies in 1 + pM_2(F_p); conjugates of P lie in a fibre of [p] of size p^2; g ↦ gP - P is an injective homomorphism because M[p] is rational. |
| 192 | lem:B-RD62-arc | targeted proof check, the construction re-derived | Right given Hopkins-Gross Prop. 5.7 for (B-RD62.5): b - (q-p)q^{n-2} = N(e - p^{2n-3}) > 0, q^{n-1} < d < Nq^{n-1}, b ≡ -(p-1) (mod N); Y_j ≡ X^{q^j} (mod p) because b > (q-p)q^{j-1}; P ≡ X^d (mod p) with P(0) = p, so R = W[[X]]/(P) is a DVR with v(p) = d and x has exact order p^n; the recursion gives l_j(a^{p-1}u) = a^{p^j-1}l_j(u) (using N \| p^j - p^{j-2}), hence Y_j(ζX) = a^{-1}Y_j(X), P(ζX) = P(X), a descent datum fixing the point; v_K(p) = e; μ_p ⊂ K from (-p)^{1/(p-1)} ∈ K. |
| 193 | lem:B-RD62-extension | independent re-proof | Right: Kummer transition maps are surjective, averaging over Δ (order prime to p) keeps surjectivity on invariants, cocycles are made compatible by lifting coboundaries, and the limit lattice defines the BT group. |
| 71 | cor:B-RD62 | targeted proof check of the arithmetic | Right given the theorem: e_n = p^{2n-3} + p - 2 is the least multiple of p-1 above p^{2n-3} (as p^{2n-3} ≡ 1 mod p-1), is ≡ -2 (mod p), lies below p^{2n-2}, and equals 2(p-1) at n = 2. |
| 194 | lem:B-RD63-point | targeted proof check, every case re-derived | Right given the Hopkins-Gross coefficient shape: the inverse-step polygon (B-RD63.3); the one-slope case forces q^{n-1} \| a; Z = β gives a > (p+1)b/p ≥ Nq^{n-1}; Z = α with uniform steps gives a ≥ Nα/p ≥ Np^{2n-3}, equality excluded by p ∤ a; otherwise a high rational step would give a = p(b + (p-1)A), so the step is β and a > (p+1)b ≥ Np^{2n-3}. |
| 72 | cor:B-RD63 | targeted proof check of the deduction | Right given the mixed-case proposition and the arc theorem: p^{2n-3} < e iff 2n-3 ≤ ⌊log_p(e-1)⌋, giving (B-RD63.8); existence for every e > p^{2n-3} follows from the arc at the level n' with p^{2n'-3} < e < p^{2n'-2} (e is prime to p, so not a power of p). |
| 195 | lem:B-RD64-weighted-kernel | targeted proof check (Bondarko 2006 inputs taken as given) | Right as far as checked: averaged eigen-coordinates; a coefficient's valuation is congruent mod N to its character exponent, which for degree-p monomials is ≡ 0 (mod p-1) under (B-RD64.1), so it is ≥ p-1; monomials of degree below 2p other than degree p have an exponent prime to p; hence min{a+q, p-1+pq, 1+2pq, p^2 q} = min{a+q, p-1+pq} for q ≥ 1, p ≥ 5. |

### Batch 17 (B.tex 10923-12165: the comparison rules and quotient transformations at the five-adic index twelve, at middle ramification and at every prime-to-p index; the small and full wild images)

These rows repeat the arguments of batches 15-16 with new parameters. For each I recomputed the parameter-specific numbers and re-ran the argument's steps.

| # | Row | Check | Result |
|---|---|---|---|
| 196 | lem:B-RD65-Newton | targeted proof check, numbers recomputed | Right: at p = 5, e_L = 288: ep/(p+1) = 240, e/N = 12; b = 4B gives α = 72 - B, β = B/5, 0 < B < 60; b ≡ 4c (mod 24) gives B ≡ c (mod 6), B odd since c ≡ 1 (mod 4); break r = 5α - B = 360 - 6B for 5 ∤ B; one B_i divisible by 5 forces B_1 > B_2 and then 25B_2 ≥ B_2 + 24B_1, a contradiction; in the tame case 24b_1 = 24b_2, and different high lines would force α_1 = b. |
| 197 | lem:B-RD65-quotient | targeted proof check, the inverse polygons recomputed | Right: the quotient coordinate is the sum of the five differences; for B > 12 the vertex (5, 4B) lies above the segment iff 6B > 72, giving 20 points of valuation (72-B)/5 and B' = 72 - B; for B < 12 the segments give (72-5B)/5 (5 roots) and B/5 (20 roots), hence 4 points of valuation 72-5B and 20 of valuation B, B' = 5B; B = 12 is excluded since B is odd. |
| 198 | lem:B-RD65-square | targeted proof check | Right given prop:B-RD64-formal and prop:B-RD50-square: a = 12m ≤ 72; q_1 = min(a+1, 6, 25) = 6, q_2 ≥ min(a+6, 31) ≥ a/4; F^2 ker F_N^3 = ker F_N has rank 5, contradiction. |
| 200 | lem:B-RD66-rules | targeted proof check | Right: with e_L = (p-1)s, α = s - B, β = B/p, and α > β iff B < ps/(p+1) = pe_0; N \| s gives the character ζ^{c-B}; r = ps - (p+1)B; the comparison rules as in #196 with p^2 B_2 ≥ B_2 + NB_1. |
| 199 | lem:B-RD66-quotients | targeted proof check, the inverse polygons recomputed | Right: single segment iff B > s/(p+1) = e_0, giving B_high = s - B; otherwise (s-pB)/p and B/p, giving B_high = pB; e_0 = N/2 is even and B odd; for a low line, high classes get α + (p-1)β = s - B/p and the p^2-p other points get β/p = B/p^2, so B_low = B/p. |
| 203 | lem:B-RD67-normalization | targeted proof check | Right given Tate 1967: first-level valuation e_L/N = e; primitive second-level v_F = e p^{r-2}, so r ≥ 2 as p ∤ e; the split complement; η^A = ζ^{e p^{-2}} = ζ^e; the residual eigenvalues ζ^{c+e} generate F_q, so an intertwiner is F_q-linear (equal characters) or z ↦ az^p. |
| 204 | lem:B-RD67-small-wild | targeted proof check | Right: r = 2: A = e prime to p, every g ≠ 1 has b_g = qA - A and B_i(g) = κ_i d_g on a q-element space; the semilinear intertwiner would need κ_2 d_g = κ_1^p d_g^p for all d_g, i.e. d_g^{p-1} constant on q-1 values, impossible; r = 3: the cases U ⊂ W with one or two breaks and W = Z ⊕ U_1 are excluded by the same arguments as lem:B-RD57-anti/-Cartan, each ending in β_2 = β_1^p on a full plane. |
| 201 | lem:B-RD67-final-plane | targeted proof check | Right given upper-numbering quotient compatibility (cited): b_0 = qe - e = Ne; in L(μ_{p^2}) the valuations Ne/(p-1) = (p+1)e (prime to p) and pNe/(p-1) give break b_0; then S = Z and c > b_0 as in lem:B-RD58-final-Cartan. |
| 202 | lem:B-RD67-full-wild | targeted proof check | Right: A = qe with v_p(A) = 2; (B-RD67.10)-(B-RD67.16) as in lem:B-RD59-final-bound and -anti-patterns; on Z, β_i(g) = κ_i d_g, and β_2 = β_1^p is impossible; so r = 4 is excluded. |
| 206 | lem:B-RD68-rules | targeted proof check | Right: s = Ne/(p-1) = (p+1)e = tN when e = t(p-1); B < pe; a scalar leading action would have square determinant, excluded by the nonsquare normalization (the cyclotomic part is trivial mod p as μ_p ⊂ K); the F_p-valued high-line character ζ^{c+s-B} forces B ≡ c (mod p+1); c ≡ 1 (mod p-1) makes B odd; the comparison rules as in #200. |

### Batch 18 (B.tex 12166-14629: the initial tame sector, exchanged high lines, marked low lines, the iteration through actual quotients, the third index)

The sector of B-RD68 is e = t(p-1), 2 ≤ t ≤ p-1, s = e(p+1) = tN (B.tex 12036-12050, read to check the bound below).

| # | Row | Check | Result |
|---|---|---|---|
| 205 | lem:B-RD68-quotients | targeted proof check | Right: as lem:B-RD66-quotients with s = (p+1)e: the inverse polygon has one segment iff B > e, giving B_H = s - B, otherwise B_H = pB; B is odd and e even; B_J = B/p. |
| 207 | lem:B-RD68-square | targeted proof check | Right given prop:B-RD64-formal: m \| p+1, a = em; q_1 ≥ p+1 (a ≥ p), q_2 ≥ min(a+p+1, p^2+p+1); (B-RD68.11) a/(p-1) ≤ t(p+1) ≤ N holds because the sector has t ≤ p-1 (checked against B.tex 12038-12044); then F^2 kills a kernel containing ker F_N^3, a contradiction. |
| 209 | lem:B-RD69-rules | targeted proof check | Right: as lem:B-RD68-rules without the parity input; the residual image over L lies in the upper unipotent group of order p; r = ps - (p+1)B; the comparison rules as before. |
| 208 | lem:B-RD69-quotients | targeted proof check, the new cases recomputed | Right: at B = e the vertex (p, (p-1)e) lies exactly on the chord from (0, pe) to (q, 0), so all quotient points have valuation e; from one slope (all valuations e, product eN) the quotient by a line has p-1 points of valuation pe and q-p of valuation p·e/q = e/p, so B' = e and α' = s - e = pe. |
| 211 | lem:B-RD70-high | targeted proof check | Right given (B-RD69.10): B_1 ≡ B_2 (mod p-1) gives b_1 ≡ b_2; with b_i ≤ p the only unequal pair is {1, p}, and then c_2 - c_1 ≡ p(p-1) ≡ (p-1)c_1 (mod N) (as c_1 ≡ p mod p+1), so c_2 ≡ pc_1: the same orbit with unequal parameters; for B_i > e the quotient parameters s - B_i are prime to p (p ∤ s); mixed sides give opposite divisibility. |
| 210 | lem:B-RD70-exchange | independent re-proof | Right: eigenvalues ζ^{c-B} and ζ^{pc+B} (determinant ζ^{(p+1)c}); exchanged lines give two congruences whose combination (×p, add, p^2 ≡ 1) is N \| (p+1)(B_1+B_2), i.e. p-1 \| B_1+B_2; for B_i = p^2 this needs p-1 \| 2, impossible for p ≥ 5. |
| 212 | lem:B-RD71-first-level | targeted proof check | Right: nontrivial upper-unipotent action of order p; r = p(s-B_i) - B_i from lem:B-RD60-break; equal r gives equal B, the high character gives equal c. |
| 213 | lem:B-RD71-marked-low | targeted proof check | Right: D = pB; J has valuation B < s - pB (as B < e); two stable lines make M'[p] L-rational; eigenvalues ζ^{pc-pB} and ζ^{c+pB}, ratio exponent (1-p)c + 2pB ≡ (p+1)B (mod N) because N \| (p-1)(c-B); scalar iff p-1 \| B. |
| 214 | lem:B-RD72-first-mixed | independent re-proof | Right: r = ps - (p+1)C_pr and r < ps - (p+1)C_div give C_pr > C_div. |
| 216 | lem:B-RD73-high-branch | targeted proof check | Right: tame semisimplicity or two stable lines give F_p^×-valued characters, killed over L; L-rationality forces p \| D; the inverse polygon (0, s-D), (p, (p-1)D), (q, 0) has its middle vertex below the chord iff (p+1)D < s; C = s - pD is prime to p; the high branch is one coset of H; [E:L] = p and b(g) = p(s-D) - C = (p-1)s = eN. |
| 215 | lem:B-RD73-common-high | targeted proof check | Right given prop:B-RD73-high-recovery (not in my list): the cases B_i > e, opposite sides, D_i > e, D_1 < e < D_2 (tame against wild first level) are excluded or settled; for D_i = qb_i < e < p^3, b_i ≤ p-1 and b_1 ≡ b_2 (mod p-1) give b_1 = b_2. |
| 217 | lem:B-RD74-actual-levels | targeted proof check | Right: (M/H)[p^{r-1}] = {X ∈ M[p^r] : p^{r-1}X ∈ H}/H; the tame/wild alternatives as in #213 and #212. |
| 73 | cor:B-RD74-third-index | targeted proof check of the deduction | Right given the upper-bound theorem (n = 4) and the arc theorem (lower bound 3 from e > p^3); at p = 5 the multiples of 4 in (125, 625) prime to 5 run from 128 to 624. |
| 218 | lem:B-RD75-terminal | targeted proof check | Right: the same computation as #211 (b_i ∈ {1, ..., p}, the pair {1, p} gives c_2 ≡ pc_1). |

### Batch 19 (B.tex 14738-16501: the wild absolute index e = p(p-1): the point bound with p \| a, determinant detection, the CM model, the third-level wild image)

| # | Row | Check | Result |
|---|---|---|---|
| 220 | lem:B-RD76-point | targeted proof check, every case re-derived | Right: Z_j = (a/p^j - b)/(p-1), so a = p^j(b + (p-1)Z_j) and j ≤ v = v_p(a); uniform after j high steps: a ≥ Np^{j-1}Z_j ≥ Np^{2n-3-j}, strict also at j = v (equality would give v_p(a) = 2n-3-v > v as v ≤ n-2); a low step gives a > Np^{2n-3-j}; all steps high gives a ≥ p^n > Np^{n-2} ≥ Np^{2n-3-v}. |
| 219 | lem:B-RD76-determinant | independent re-proof | Right: v(ζ_{p^n}-1) = ep^r/(p^{n-1}(p-1)) is an integer, so r ≥ n-1-v ≥ 1; then χ_p^{d_1-d_2} of prime-to-p order forces p \| d_1-d_2, so d_1 = d_2, and μ_{p-1} injects mod p. |
| 74 | cor:B-RD76 | targeted proof check of the deduction | Right given (B-RD76.8) (not seen): at p = 5, e = 20, v = 1, n = 3 = v+2 and 20 ≤ 5^{2·3-3-1} = 25. |
| 221 | lem:B-RD77-kernel | targeted proof check (Bondarko inputs taken as given) | Right as far as checked: min{a+q, 1+pq, p^2 q} = min{a+q, 1+pq} for q ≥ 1; the coefficient classes as in lem:B-RD50-boundary. |
| 75 | cor:B-RD77 | targeted proof check, the recurrence recomputed | Right given prop:B-RD64-formal and the B63 construction: e = p(p-1) > p gives the lower bound 2; the mixed case at p^4 would need e > p^4; with a = e(p^2-1), q_1 = 2p-1, q_2 = 2p^2-1, q_3 = 2p^3-1 > p^3 - p = a/(p-1) while q_2 < p^3 - p for p ≥ 5, so index three; at p = 5 the degree-8 fibre is one orbit, leaving 24 and the types A, B, C. |
| 223 | lem:B-RD78-model | targeted proof check | Right: the argument of lem:B-RD52-CM and lem:B-RD52-LT (checked in batch 15) uses p ∤ e nowhere, as the row says. |
| 222 | lem:B-RD78-layer | targeted proof check | Right given Lubin-Tate 1965 (cited): v_p([L:K_0]) = v; Φ_n = ([p]^{∘(n-1)}T)^{q-1} + p is Eisenstein of degree (q-1)q^{n-1} = \|(O_E/p^n)^×\|; [U : U ∩ J] ≤ p^v, so U^{p^v} ⊂ J; for odd p, U^{p^v} = (1+p^{v+1}O_E)/(1+p^n O_E), which contains the last layer when n ≥ v+2. |
| 224 | lem:B-RD79-layers | targeted proof check | Right: one valuation e on M[p] (product eN); inverse polygons give e/q^{j-1} because (q-i)e > (1-i/q)Z for Z ≤ e; the kernel of GL_2(Z/p^3) → GL_2(F_p) has order p^8; e/q^2 = (p-1)/p^3 forces r ≥ 3; (1+pA+p^2B)^p ≡ 1 + p^2 A (mod p^3) gives W_1 ⊂ W_2; W_1 = 0 would leave at most p^2 conjugates; r = 3 forces (1,2). |
| 76 | cor:B-RD79 | targeted proof check of the deduction | Right given the proposition excluding r = 3: 4 ≤ r ≤ 8, and 5^4 = 625. |
| 225 | lem:B-RD80-first | targeted proof check | Right: b_0 = (D-A)/p; ϖ^A = (ϖ^p)^{p-1} changes by (A/p)d_g^p in degree A + pb; cancellation gives j = A + (p-1)b and f_j(z) = -(A/p)d z d_g^{p-1}/j; for b > b_0, j = D - b. |
| 227 | lem:B-RD80-plane | targeted proof check | Right: a nonabelian 2-dimensional Lie algebra has [H,E] = E, so tr E = tr E^2 = 0 and det E = (tr(E)^2 - tr(E^2))/2 = 0, a nilpotent line, excluded; the dual-number case likewise; in the split case g = 1 + pE_22 + p^2B with B_11 ≡ 0 fixes v = e_1 + pw (w_2 = -B_21) modulo p^3 (recomputed) while g^p ≠ 1, an orbit of size at most p^2 < p^3; the nonsplit case gives (Z/p^2)^2. |
| 226 | lem:B-RD80-orientation | targeted proof check | Right: the normalizer of a nonsplit Cartan E' is E'^× ⋊ Gal; in the other coset the ±1 eigen-generators g_± and their breaks are excluded by the first-term lemma, and g_-^p has a larger break with a z-linear first change where a z^p-leading displacement of valuation q^2A is required. |
| 228 | lem:B-RD81-levels | targeted proof check | Right: the leading ramification coefficient is additive, so b(g^p) > b(g) when g^p ≠ 1; U = pW consists of p-th powers. |
| 77 | cor:B-RD81 | targeted proof check of the deduction | Right: 5 ≤ r ≤ 8, and 5^5 = 3125. |
| 229 | lem:B-RD82-Newton | targeted proof check | Right: e_L = eN = (p-1)s gives u_0 = (p-1)B, α = s - B, β = B/p; the high character ζ^{c-B} as N \| s; two single-segment inverse steps give B/p^3 and B/p^5; the residual image over L is upper unipotent of order at most p. |

### Batch 20 (B.tex 16502-18194: the terminal plane, exchanged-line quotients, the tame reducible sector at e = p(p-1), the cyclotomic breaks at p = 5, e = 20)

| # | Row | Check | Result |
|---|---|---|---|
| 230 | lem:B-RD82-terminal | targeted proof check | Right: primitive points off H have v_F = p^4·B/p^5 = b; a terminal element displaces all of them by b + b(g), so every Cv (v ∉ H) is nonzero with one common status; a nonzero lower-left entry would give one high and one low image among (x,1), so C is upper triangular, and with zero lower diagonal C = b_0 E_12; 4 = ε + r_1 + t with r_1 ≤ t ≤ 2 forces t = 2. |
| 232 | lem:B-RD83-tame | independent re-proof | Right: v_L(T(P_i)) = b_i/q; the common point field is Galois of degree q (denominator q); a translation off both high lines has break (q-1)b_1 = (q-1)b_2. |
| 231 | lem:B-RD83-quotients | targeted proof check | Right: B_i = p^2 k_i > e = p(p-1); s = pN, so the quotient parameters are p(N - pk_i) and pk_j; N - pk_i ≥ 2p-1 > p-2 ≥ k_j, both prime to p, so lem:B-RD83-tame excludes a tame residual action. |
| 78 | cor:B-RD83 | targeted proof check of the deduction | Right given B77, B81, B82 and the five-dimension proposition: the case split is exhaustive; with agreeing high lines, k_1 ≡ k_2 (mod p-1) on {1, ..., p-2} gives equality. |
| 79 | cor:B-RD84-first-wild | targeted proof check, the p = 5 list recomputed | Right: k_i odd in {1,2,3} (c ≡ 1 mod 4, B ≡ c mod 6), so B_i ∈ {25, 75}; solving the exchange congruences mod 24 gives exactly (25,1;75,9) and (25,13;75,21), with high/other exponents (0,6;6,0) and (12,18;18,12) (eigenvalues ζ^{c-B}, ζ^{5c+B}); the types are A/B and C/B. |
| 233 | lem:B-RD85-diagonal | targeted proof check, all valuations recomputed | Right: α_1 = p(N - pk_1); the vertex (p, (p-1)p^2 k_1) is above the chord iff pk_1 > p-1; v_E(T_1(P_1)) = N - pk_1, v_E(T_2(P_2)) = k_2; the two breaks p(p+1)k_1 - N and qN - (p^3+1)k_2 would require p(p+1)k_1 + (p^3+1)k_2 = p^4 - 1, while at k_1 = k_2 = p-2 the right side exceeds the left by (p+1)(p^2+1). |
| 80 | cor:B-RD85-tame | targeted proof check of the deduction | Right given prop:B-RD83-Lie: dim W_1 ≥ 3, W_1 ⊂ W_2, \|W\| ≥ p^6 = 15625 at p = 5. |
| 234 | lem:B-RD86-cyclotomic | independent re-proof | Right: [K(μ_{p^2}):K] divides p and N, so is 1; K = K_0(ζ_{p^2}) at e = p(p-1); σπ - π = ζ_3(ζ_p^a - 1) has valuation p^2, so the break of K_3/K is N; with t^N = π, (σt/t)^N = σπ/π gives v_C(σt/t - 1) = N(p^2-1) = N^2. |
| 81 | cor:B-RD86-tame | targeted proof check of the deduction | Right given the trace proposition: total dimension 6 would force W_1 = W_2 = sl_2 (E_12, E_21 and their commutator), excluded; so ≥ 7. |
| 235 | lem:B-RD87-coefficient | targeted proof check | Right: m(b) = min(A + pb, J + b); m(t) < D_0 < D_1 forces the cancellation J = A + (p-1)t; at u the J-term is uniquely first, D_0 = A + (p-1)t + u; the quotient break (u + (p-1)t)/p from the coset average (one element of T, p-1 outside), and t for the quotient killing T. |
| 236 | lem:B-RD87-fields | targeted proof check | Right given B83, B85 (W_1 = ⟨E_12, E_21, Z⟩): tame weights 6 on E_21, 18 on E_12, 0 on the diagonal; η = ζ^5 since 5·5 ≡ 1 (mod 24); 5b ≡ weight gives d ≡ 0, o_1 ≡ 6, o_2 ≡ 18 (mod 24); a single break would equalize the quotient breaks. |
| 82 | cor:B-RD87-full | targeted proof check of the deduction | Right given the proposition excluding dim W_1 = 3: W_1 = M_2(F_5), W = 1 + 5M_2(Z/125) of order 5^8; det(1+5A) = 1 + 5 tr A is nontrivial, so μ_25 ⊄ L. |
| 83 | cor:B-RD88-cyclotomic | targeted proof check, the Herbrand integration recomputed | Right given the proposition's four coordinate breaks: lower breaks 6, 6 + 5·18 = 96, 96 + 25·42 = 1146, 1146 + 125·6 = 1896; ranks 4, 3, 2, 1; 156 = (5^4-1)/4 lines, counted 1 + 5 + 25 + 125 by last nonzero coordinate; L(μ_25) is the quotient for A_11 + A_22 with break 72; the tame scaling b(D/L) = 24 b(C/K) gives 3. |

### Batch 21 (B.tex 18247-20014: the explicit base field at p = 5, e = 20, the point towers, the crossings, the cyclotomic upper break, the residual-wild group)

| # | Row | Check | Result |
|---|---|---|---|
| 237 | lem:B-RD89-base | independent re-proof of the construction | Right: (1+T)^5 - ζ_5 + π_1^4 T^2 expands to (B-RD89.2) and is Eisenstein at π_1, so e_K = 20; with x = ζ_25 - 1 - t the shifted polynomial (B-RD89.3) has coefficient valuations 22, 20, 20, 20, 20, 0, one Newton segment, v_K(x) = 22/5; so [C:K] = 5, v_C(x) = 22, v_C(gx - x) = v_C(ζ_5^j - 1) = 25, break 3; K ∩ K_1(μ_125) = K_1, so K(μ_125)/K has degree 25; the tame scaling gives 72. |
| 239 | lem:B-RD90-point-towers | targeted proof check, every number recomputed | Right: with s = 120, (B_1, B_2) = (25, 75) give first-level (β, α) = (5, 95) and (15, 45); the table (B-RD90.4) (A = 95, 15, 5, 45; D = 625·(5, 95, 15, 45)); η = ζ^5 since 5^3 ≡ 5 (mod 24); E_1^+/E_1: an off-diagonal last line gives 606 = (3125-95)/5 and then the forced change 3045 ≠ 28125; with the diagonal last line, (9375-15)/5 = 1872, u = 9360 - 4t, and t < 606 (change 9455) and t > 606 (J - 95 - 4u = 15t - 34410 < 0, change 12485 - 5t) are excluded, so (t,u) = (606, 6936), J = 27839 and 2439; E_2^+/E_2: (3125-5)/5 = 624 and the change 3165 exclude a diagonal last line; (9375-45)/5 = 1866, u = 9330 - 4t, t < 624 (9335) and t > 624 (15t - 34200 < 0, 12455 - 5t) excluded, so (624, 6834), J = 27341 and 2541; quotient breaks (u+4t)/5 = 1872 and 1866. |
| 240 | lem:B-RD91-first-break | independent re-proof | Right: r = ps - (p+1)B_1 for p ∤ B_1; the inequality in the other coordinate gives (p+1)(B_1 - B_2) ≥ 0, strict if p \| B_2. |
| 243 | lem:B-RD92-tame25 | targeted proof check, every number recomputed | Right: coordinate valuations (19/5, 3/5) and (1/5, 9/5); in a degree-5 field the three line types give breaks (456,72), (6,222), (6,72) and (474,66), (24,216), (24,66), never equal, so both evaluations are surjective; dimension three is excluded (E_1 forces the diagonal break 72, E_2 gives 24 or an off-diagonal last line with diagonal break below 66); in E_1, t ∈ {6, 30, 54} with u = 360 - 4t: t = 30 would need J = 95 and t = 54 J = 71 in model 1, both impossible, so (6, 336); in E_2, the diagonal last line gives (18, 48) and the change 165 ≠ 1125, the off-diagonal one t ∈ {24, 48}, where t = 48 forces the change 215 ≠ 2375; t = 24 is consistent (J = 941; my own check); breaks A_21, A_22, A_12, A_11 = 6, 24, 66, 72. |
| 242 | lem:B-RD92-parahoric | targeted proof check | Right given lem:B-RD92-tame25 and B91: in the basis (e_1/5, e_2) the matrix is [[ρ_11, 5ρ_12],[ρ_21/5, ρ_22]], so 25 \| ρ_21; the group (B-RD92.6) has order 5^{2+3+1+2} = 5^8; for g = I + X with residual upper entry u, 10X^2 ≡ 0 and X^3 ≡ 0 (mod 25), so g^5 ≡ 1 + 5uE_12 (recomputed); the breaks (66, 24) and (6, 72) follow from (B-RD92.1) with the index identification. |
| 241 | lem:B-RD92-common-high | targeted proof check, all arithmetic recomputed | Right: a last line other than the common high line would give 24b_1 = 24b_2; the two rows u + 4t = 15000 - 630b_i and u - t = 15000 - 750b_i; the mixed case gives t = 150b_1 - 126b_2 < 24b_1; at t = 24b_2 the excess is 750(80 - 5b_1 + b_2) > 0 (max of 5b_1 - b_2 is 71) and J_2 = 750b_1 - 649b_2 < 101b_2; hence t = 24b_1 and u = 15000 - 630b_2 - 96b_1. |
| 244 | lem:B-RD93-cyclotomic | targeted proof check, the Herbrand computations recomputed | Right given upper-numbering base-change compatibility (cited): d ≤ 24 since the term 5t^4 (valuation 24) cannot cancel; Gal(T/K_1) = C_5 ⋊ C_m; the different gives 5m - 1 + 4b_T = m - 1 + md, u_T = (d-4)/4 ≤ 5; C_2/K_1 has lower breaks 4, 24 and upper breaks 4, 8; ψ_{T/K_1}(8) = m u_T + 5m(8 - u_T) = m(44 - d); so the last upper break is 44 - d ≥ 20, and ≥ 480 after the tame extension. |
| 245 | lem:B-RD93-terminal-bound | targeted proof check of the arithmetic ((B-RD93.6)-(B-RD93.8) of the preceding proposition taken as given) | Right as far as checked: 625·3/25 = 75, displacement 625·75 = 46875, b(h) ≤ 46800; 6 + (46800-6)/5 = 46824/5; 223146 + 125(46824/5 - 8946) = 275496; 3125/625 = 5, b(g) ≤ 3120; 1896 + 25(3120 - 384) = 70296. |
| 247 | lem:B-RD94-group | independent re-proof | Right: det ≡ 1 + 5(a_0 + d_0 - v_0 w_0) (mod 25), so the constraint; \|W\| = 5^{2+2+2+3-1} = 5^8; modulo 25 the original matrix is fixed by (v_0, w_0, a_0, v_1), the quotient matrix [[1+5a, 5v],[w, 1+5d]] by (v_0, w_0, a_0, w_1), so [F_2:L] = [F_Q:L] = 5^4, [E:L] = 5^5 and Gal(F/E) as displayed; μ_25 ⊂ L forces μ_25 ⊂ K = K_0(μ_25); break 24 over K, 576 over L. |
| 248 | lem:B-RD94-ordering | targeted proof check | Right: the conjugation formula (B-RD94.7) (recomputed); ±1 conjugates give ρ ≤ x ≤ C, strict by the distinct tame weights 1, λ, λ^{-1}; x > r by [G_i, G_j] ⊂ G_{i+j+1}; ρ - σ = 5(r' - r); the diagonal restrictions 5x - 4ρ = 5y - 4σ give y = x + 4(r - r'); the eigenvalue ratio -4c - 10b ≡ -6b (mod 24) and 5^{-1} ≡ 5 give r ≡ -6b, r' ≡ 6b; r < 600 - 30b from the strict B60 inequality at valuation 5b. |

### Batch 22 (B.tex 20015-21634: the common-high point fields, the terminal conductor bounds, the critical pairs, the gap lemma, the irreducible-residual degrees and conductors)

| # | Row | Check | Result |
|---|---|---|---|
| 246 | lem:B-RD94-common-high | targeted proof check, the inequalities recomputed | Right: the prime case repeats #241; for the four pairs, 60000 + 630m_1 - 3630m_2 = 30480, 15960, 1440, 480 > 0 and 630m_2 - 750m_1 = 1920, 4440, 6960, 720 > 0; hence 5z + A_1 > D_{1,1} (using t < 24m_2), J_1 = D_{1,1} - z, J_1 + t - D_{0,1} = 630m_2 - 750m_1 + 5t > 0; t ≥ 24m_1 is excluded because 25 \| A_1; the second upper break (z+4t)/5 = 3000 - 126m_2. |
| 249 | lem:B-RD94-terminal | targeted proof check of the degrees and Herbrand arithmetic ((B-RD94.17), (B-RD94.15) taken as given) | Right as far as checked: the stabilizer degrees 25, 125, 125, 625, 3125, 3125 from (B-RD94.2); v_{T_h} = 25j, displacement 15625j, b(h) ≤ 15600j; with ψ(v) = 25v - 4ℓ_5 - 20ℓ_4 the bounds 1170000 - 4ℓ_5 and 390000 - 4ℓ_4; with ψ(v) = 25v - 4ℓ_4 - 120 and 25v - 4ℓ_5 - 20ℓ_2 the bounds 389880 - 4ℓ_4 and 1170000 - 4ℓ_5 - 20ℓ_2 (all recomputed). The final table needs (B-RD94.17), not in my list. |
| 250 | lem:B-RD95-critical | targeted proof check, all bounds recomputed | Right: both strict rows give z > 15000 - 726a = 9918 or 7014 > 5550, while B60 on the coordinate of value 75 gives z < 5550, so t = 24a; for z > 1110 the divisible terms change after 5625, so J = 5625 - z, and J + t ≥ 80 + 5t gives C ≤ 1109; C ≡ 6 (mod 24) (weight ζ^6, multiplier ζ since 25 ≡ 1), so C ≤ 1086. |
| 253 | lem:B-RD96-selected | targeted proof check | Right: \|W\| = 5^9 for (B-RD96.3); stabilizers and degrees 25, 125, 3125; the reordered quotient matrix [[1+5d, w],[5v, 1+5a]]; high first-level value 5(24-b) = 120 - 5b, inverses (24-b)/5, (24-b)/125; A = 25(24-b), D_0 = 3125b, D_1 = 15625(24-b), v_T(5) = 3125·480. |
| 252 | lem:B-RD96-opposite | targeted proof check, the table recomputed | Right: one break is excluded by the distinct tame weights; for prime pairs a non-high last line would give 24m_1 = 24m_2; for (15,19), u + 4t = 120·19 and the three tie cases give displacements N + 2280 > 1875, A + 20t + 2280 > 1875, and A + 600m_2, J + u > 1875; then t' = 24m_1 and C' = 3000 - 126m_2 give 264/606, 168/606, 216/858, 216/1362, and 24 ≤ t' ≤ 336 for (15,19). |
| 251 | lem:B-RD96-gap | independent re-proof | Right: one break forces D_1 = D_0; a last line T_1 ≠ H gives u ≤ Δ_i and t ≤ Δ_i/5, so z = (u+4t)/5 ≤ 9Δ_i/25, contrary to (B-RD96.15); with H last, J_i + t = D_{0,i} and D_{1,i} = J_i + u, so D_{1,i} - D_{0,i} = u - t for every i. |
| 255 | lem:B-RD97-degrees | targeted proof check | Right: v_L(P) = e/q = (p-1)/p and v_L(P^+) = (p-1)/p^3 at e = p(p-1); if [E:L] = p, [T:L] = p^3, A = p-1 is prime to p, one break D - A with leading map A a_i d_g in both models, contradicting the Frobenius orientation; W_1 ⊂ W_2 gives all translations in T/E. |
| 254 | lem:B-RD97-conductors | targeted proof check | Right: one break b < b_0 would make d_g^{p-1} constant on q-1 values, b > b_0 would make the two leading maps proportional; two breaks give J + u = D and largest quotient break (D-A)/p = b_0; c_1 = N(p-1), c_2 = (q^2-1)(p-1); F_2 has last break c_1 by the character-sum bound; ψ_{F_2/E_i} has slopes at most p^{r_1-2}. |
| 84 | cor:B-RD97-layers | targeted proof check | Right given the preceding proposition (sl_2 excluded): a 2-dimensional abelian subalgebra of sl_2 cannot exist (a centralizer meets sl_2 in a line), a nonabelian one has a nilpotent derived line, excluded by irreducibility; so r_1 = r_2 = 3 forces sl_2; the remaining shapes (3,4) with nonzero trace and (4,4) give 5^7 and 5^8. |

### Batch 23 (B.tex 21693-22687 and C.tex 28-686: the different bound, ν_min(5,20,2) = 2, the scaled versions, the third-level arc; the first C rows)

| # | Row | Check | Result |
|---|---|---|---|
| 256 | lem:B-RD98-different | independent re-proof | Right: [K:K_1] = p and K ∩ C_0 = K_1, so [C:K] = p^2; d(K/K_1) ≤ p^2-1 (the term pπ^{p-1} has valuation p(p-1) + p-1 and the others are ≢ -1 mod p); d(C/C_0) ≥ p-1; C_0/K_1 has lower breaks p-1 and p^2-1, so d(C_0/K_1) = (p^2-p)p + (p-1)p^2 = 2p^2(p-1); transitivity gives d(C/K) ≥ p^2(p-1)^2 + p-1; a cyclic p^2-extension has d = (p-1)(δ_1 + pδ_2 + p + 1) (recomputed from the lower breaks δ_1, pδ_2 - (p-1)δ_1); hence δ_1 + pδ_2 ≥ p(p^2-p-1), and δ_2 ≥ p^2-p-2+1/p when δ_1 ≤ p-1. |
| 85 | cor:B-RD98-exact-five | targeted proof check of the assembly | Right given the theorem for irreducible residual inertia, B96 and B82-B90 (most checked in batches 19-23): B76 applies at n = 3 (3 ≥ v+2, 20 ≤ 25); μ_5 ⊂ K because 5^{1/4} ∈ K and K_0(5^{1/4}) is the unique tame quartic extension K_0(μ_5); the arc at level 25 (e = 20 > 5) gives the lower bound. So ν_min(5,20,2) = 2. |
| 258 | lem:B-RD99-points | targeted proof check | Right: with e = tp(p-1), p ∤ t: v_L(P) = t(p-1)/p, v_L(P^+) = t(p-1)/p^3; [E:L] = p is excluded by the Frobenius orientation as in B97; for r_1 = 2: a_0 = tN(p-1), j_0 = D_1 - a_0 ≡ -t (mod p) (recomputed), the cases a ≠ a_0 and a = a_0 (with b_* - (D_2-A)/p = (p-1)(D_2-D_1)/p > 0, recomputed) all make the two terminal maps proportional; c_1 = tN(p-1), c_2 = t(q^2-1)(p-1). |
| 257 | lem:B-RD99-cyclotomic | independent re-proof | Right: d(K/K_1) ≤ tp^2 - 1 (v_K(i) = tp(p-1)v_p(i) is a multiple of tp); the transitivity bound tp^4 - 2tp^3 + tp + p^2 - 1 = (p-1){tp(p^2-p-1) + p + 1} (expanded); hence (B-RD99.12) and δ_2 ≥ t(p^2-p-2+1/p); if μ_{p^2} ⊂ L, the break N of C_0/K_2 scales by t and N to tN^2. |
| 146 | lem:B-RD100-arc | targeted proof check, the construction re-derived | Right given Hopkins-Gross Prop. 5.7: A exists (x_0 < A ≤ x_0 + 2 < px_0); b - (q-p)A = (N/p)(e - p^2A) > 0, (q-p)qA - b = (N/p)(p^3A - e) > 0, d = b + (p-1)J, d - J = (p-1)b + pq(p-2)A, b ≡ -(p-1)A (mod N) (all expanded); Y_1 ≡ X^{qA}, Y_2 ≡ X^J, P ≡ X^d (mod p) with NJ > d because b < (q-p)J; the descent with a = ζ^{-A} fixes x^A. |
| 60 | cor:B-RD100-threshold | targeted proof check of the deduction | Right: necessity from prop:B-RD76-mixed at n = 3, v = 1 (e > p^{2·3-3-1} = p^2), existence from the arc. |
| 87 | cor:C-RD4 | targeted proof check | Right, and agrees with part 1 (confirmed): S_0 → S finite surjective, de Jong's good-reduction and homomorphism-extension theorems on the trait, Néron for morphisms; ε ≠ 0 gives nonreducedness. |
| 56 | auto:C:4b7cbcb1fe87 | targeted proof check | Right, and agrees with part 1: EGA IV 8.8.2 spreads one finitely presented isomorphism, not an infinite compatible system. |
| 259 | lem:C-RD11-ring | targeted proof check | Right, and agrees with part 1 (every step re-derived there): m = (p, z), z^2/p ∈ m (valuation 2v(z)-1 > 0, derivative 2z/p integral), m^{2r} ⊂ aR, the conductor argument with u_N = (J - c_N)/p^N. |
| 55 | auto:C:3d23f9b8075d | carried as background without fault found | Certificate remark (verify_nonfinite_reduction.py), not run; part 1 recomputed its identities by hand. |
| 52 | auto:C:2b1cfc4567d4 | targeted proof check | Right, and agrees with part 1: the normalization is integral radicial but not finite, so prop:C-RD1 does not apply. |
| 261 | lem:C-RD8-sections | targeted proof check | Right, and agrees with part 1: spreads agree at generic points, separatedness on the reduction, formal unramifiedness across the nilradical. |
| 57 | auto:C:63e1d81ef0f5 | targeted proof check | Right, and agrees with part 1: the [-1] gluing at a node is the twist by a finite étale double cover. |
| 262 | lem:C-RD9-coherent | targeted proof check | Right, and agrees with part 1: differences vanish at all associated points, hence vanish. |

### Batch 24 (C.tex 762-1313, D.tex 64-1356: the remaining C remarks and lemmas, F-divided modules, the nodal family, the completed Čech complex, constant BT groups)

| # | Row | Check | Result |
|---|---|---|---|
| 51 | auto:C:24b235bcb6c7 | targeted proof check | Right, and agrees with part 1: a realization over R[ε] would reduce to one over R. |
| 54 | auto:C:3a7ebde95252 | carried as background without fault found | Scope remark; Hochster 1973 not obtained (as part 1 recorded, statement level). The deduction "Spec R has no open cover by schemes with finite surjective geometrically unibranch covers" is the contrapositive of thm:C-RD8 applied to the counterexample, and is right. |
| 260 | lem:C-RD12-complete | targeted proof check | Right, and agrees with part 1: the torsor of square-zero liftings, Serre-Tate over R/p^r, the compatible differences d_r and Artin-Rees, completeness of the finite-level coordinate algebras. |
| 53 | auto:C:35345d1cc7ea | targeted proof check | Right, and agrees with part 1. |
| 86 | cor:C-RD14 | targeted proof check | Right, and agrees with part 1: O(3e) is relatively ample, EGA III 5.4.5 algebraizes, flatness and smoothness by the local criteria, Moret-Bailly's QPROJ descent. |
| 58 | auto:C:cfff6b2c31f1 | targeted proof check | Right, and agrees with part 1. |
| 59 | auto:D:fa384818cda6 | carried as background without fault found | Remark citing Detinko-Flannery-Hulpke 2018 Theorem 2.5 (not opened); its claims refer to proofs earlier in D.tex; part 1 confirmed it. |
| 312 | lem:DE-Fdiv-universal-homeomorphism | targeted proof check | Right given Stacks 0CNF (cited): A ⊂ B by reducedness and surjectivity; B^q ⊂ A for one q = p^N (q-th powers of polynomials in finitely many generators); b ↦ b^q gives g with f∘g and g∘f the N-th absolute Frobenius; Frobenius pullback is an equivalence on F-divided systems (the shift), so f^* is one. |
| 100 | cor:DE-E2-relative-node | targeted proof check | Right given prop:DE-E2-relative-Frobenius: R[x,y]/(xy) is free on 1, x^i, y^j; the retraction keeping p-divisible exponents is linear over R[x_n,y_n]/(x_n y_n) (x^{pa} y^j = 0 matches x_n^a y_n^{j/p} = 0), so relative Frobenius splits. |
| 98 | cor:DE-E2-Noetherian-counterexample | targeted proof check | Right given the identities of thm:DE-E2-counterexample (not in my list), and agrees with part 1: I = R[t^{-1}]/R is not finitely generated, and B ⊗ I is free of rank 2p over I with nonzero x^p coefficient b_1. |
| 99 | cor:DE-E2-coherent-any-field | targeted proof check of the local-freeness step | Right as far as checked: the stratification identifies the completed stalk with Ô ⊗ M_x/m_x M_x, so stalks are free; the rest rests on Tonini-Zhang 2019 Thm. 6.8(4) and the preceding proposition (cited; part 1 records that this chain rests on Jiang 2023 and Tonini-Zhang). |
| 311 | lem:DE-E2-completed-Cech | targeted proof check | Right, and agrees with part 1: the completions are B-flat, the nerve modulo I has extra codegeneracies, and the finite I-adic filtration gives exactness. |
| 97 | cor:DE-BT-constant | targeted proof check of the lattice step | Right given de Jong 1995 Cor. 5.1.2 and the preceding theorem (Esnault-Shiho; cited, as part 1 recorded): the intersection of the Galois conjugates of the fibre lattice is a full F- and V-stable lattice with descent datum, so Dieudonné theory over k gives G_0, and the quasi-isogeny becomes an isogeny after multiplying by a power of p. |


## Summary of the checks (all 318 ids)

Counted by script from the check-events file (one event per id, 318 events):

- targeted proof check: 225;
- independent re-proof: 37;
- computation or formal certificate: 3. These are cor:OC-all-prime-integral-counterexample (the p = 2 numbers recomputed, B_2 = 35, r = 556), auto:A_monodromy:3a04f9cdd890 (C(49,3) = 18424) and lem:B-RD41-isogeny (my own sympy script);
- carried as background without fault found: 53;
- refuted: 0.

The 53 background rows fall into two groups:

- 36 auto:* remarks: certificate remarks whose returned code I did not run, plus scope and pointer remarks;
- 17 corollaries that only apply theorems outside my list. Examples are the ten degree-transfer assemblies of batch 9, A6-COMPUTATION, and the three batch-8 corollaries.

I read every row in full (statement and proof); no row was taken at statement level only. Where a proof rests on a result outside my list or on a cited source I did not open, the row says so ("given X (not checked)").

My own verifiers are in `agent_notes/afcdf31bb407576f5_work/`. Each was run with `python -I -B` from my work folder, and none of the return's code was run:

- `check_b13.py` checks the 3-isogeny (B-RD41.1)-(B-RD41.3), the invariants (B-RD37.3) and the j-identities (B-RD42.13).
- `check_b14.py` checks the norm (B-RD48.5) and the multiplier-three coefficient.

The rows overlapping part 1 (Claude Opus 5.5 at effort max, agent SA15-c9_c100-part2) agree with its verdicts. They are cor:B-RD6, cor:B-RD27-exact-three, lem:B-RD49-inertia, lem:B-RD60-break, the C rows (C-RD4, C-RD8, C-RD9, C-RD11, C-RD12, C-RD14 and their remarks), cor:DE-E2-Noetherian-counterexample and lem:DE-E2-completed-Cech. Some rows have no check event of part 1's own: lem:B-RD17-degree, lem:B-RD52-CM and lem:B-RD26-trace-arc, which part 1 only names, and lem:DE-Fdiv-universal-homeomorphism and cor:DE-E2-relative-node, which its md lists as "argument followed". I checked them here.

## Refuted or corrected

Nothing was refuted. Every proof I followed is right as far as it goes; the dependencies outside my list are named in each row.

The return itself refutes two claims of the manuscript, and I confirmed both refutations:

- cor:B-RD6: the cas test is negative for every odd p.
- cor:C-RD4: the proposed reducedness criterion is false, with S = Spec k[[t]][ε]/(ε^2) as counterexample.

## What is new (as the return claims it; I did not search the literature)

**A, crystalline foundations:**

- Grothendieck's sequence (8.5.1) is exact with zero kernel in every degree for smooth ample sections (A2-EXACT).
- The unit-root count holds in every degree (A2-UNIT).
- Integral crystalline weak Lefschetz fails at every prime (the OC chain). At p = 2 the explicit surface has C: y^2 + y = x^15 (genus 7), its Raynaud polarization, and a root cover embedding X in P^561. For a smooth degree-d section Y_d, ker(H^1(X,O) → H^1(Y_d,O)) has dimension 1 for d = 1 and 0 for every d ≥ 2.
- The product examples are injective with torsion-free cokernel for d ≥ p^2 - p.

**A, monodromy of Lang covers for abelian surfaces in characteristic two:**

- On a nonordinary principally polarized surface, the system |3dΘ| (d odd) has a full hyperplane radical of order 2^{9d^2-2}.
- Its main Lang component is the orbit V∖K, of degree 2^{9d^2-1} - 2^{dim K}.
- The exceptional submodule satisfies dim K ≤ 9d^2 - 1 - max{8, 3d}. At ℓ = 17, it is at most 1728 of 2600.
- The sparse sections s_q on E × E (6 | q) have stable Cartier rank 6q - 2.
- On a fixed 2-rank-zero surface, every degree divisible by 3, 5, 7, 11 or 13 is known, so the first open odd degree is 17.

**B, torsion levels and the inertia character (the run's B.3/B.4):**

- No additive potentially good curve over Q_p(ζ_p) has full p-torsion for p ≥ 5 (B-RD11).
- The least good-forcing level is N + 1 (B-RD13).
- A finite universal index exists (B-RD17-common, -degree).
- At p = 3 the exact additive range is N(e) = 1 + min(s, ⌊(L+1)/2⌋, ⌊(L+s+1)/4⌋), and 27-torsion first occurs at e = 216 (B-RD20, B-RD21, B-RD26, B-RD27).
- Level 9 fails at (3, 2) (B-RD29).
- At e = 1 in residue characteristic two there is no point of order 16 (B-RD44-point).
- For p ≥ 5, a mixed comparison at level p^n exists iff e > p^{2n-3} when p ∤ e (B-RD63), and needs e > p^{2n-3-v} in general (B-RD76).
- ν_min(p,e,2) = 3 for p^3 < e < p^4, under the hypotheses of its theorem (B-RD74).
- ν_min(5,20,2) = 2, with an explicit base field (B-RD89, B-RD98-exact-five).
- When v_p(e) = 1, third-level ambiguity occurs iff e > p^2 (B-RD100).

**C, extending abelian schemes:**

- A reduced counterexample with nonfinite normalization (C-RD11): the ring R ⊂ V_0, whose completion is V[ε].
- Serre-Tate across finite nilpotent thickenings of complete bases (C-RD12).
- The elliptic case needs no extra ample-class or atlas condition (C-RD14).

**D, crystals and F-divided modules:**

- F-divided modules are invariant under finite universal homeomorphisms.
- The nodal family R[x,y]/(xy) satisfies the crystal-stratification equivalence.
- Restriction fails to be faithful over F_p[t] with noncoherent coefficients.
- Over any field, coherent infinitesimal crystals are the same as coherent stratified modules (given Tonini-Zhang 2019).
- Over the stated simply connected bases, BT groups are constant up to isogeny (given Esnault-Shiho and de Jong 1995).

## Errata

1. auto:A_monodromy:12aa8c66349f is stale (batch 3).
2. The run reports a cancelled section 8.2 (8.2.1) on cote 4, scans 3-4 (batch 1). This needs checking on the scan.
3. Many rows marked "Proved" carry a "-candidate" label, for example the cor:nonordinary-*-candidate and cor:f0-*-candidate rows, cor:generic-nonordinary-ppav-finite-degrees-candidate and cor:root-nonordinary-*-candidate. This is a naming erratum for the register.
4. cor:DE-Lang-wedge-cyclic-principal-bounds uses a symbol e ("the degree e is one of 3ℓ, 6ℓ, 9ℓ") that its statement does not define.
5. cor:B-RD18 uses s without defining it in the statement (s = v_p(e/(p-1)), as in B-RD13).
6. ex:root-kernel-compression-countermodel is alternating only in characteristic two. The setting assumes this, but the example does not say so.
7. lem:B-RD92-tame25 says "at t = 30 the compulsory prime exponent is 135". The exclusion of t = 30 actually comes from the other model's row: there J + 30 = 125 would force J = 95, which is divisible by five. The conclusion (6, 336) stands; only the stated reason is misattributed.
8. lem:B-RD60-Newton derives B ≡ c (mod p+1) from σ(a_p) = ζ^{(p-1)c} a_p. With the opposite point-action convention the sign flips. The return notes the convention elsewhere; the statement depends on it.
9. On our side, my Batch-2 note had given part 1's effort as "high". It is corrected in place to "effort max", which is what part 1's header and its check events record.

## Bridges (to RH, GRH, weights and Tate motives)

- **thm:A-unit-count (A2-UNIT)** rests on Katz-Messing 1974, a consequence of Deligne's Weil I, which is RH over finite fields. The unit-root count in every degree is the slope-zero part of the Frobenius eigenvalues on crystalline cohomology. Through Katz-Messing these are the eigenvalues of geometric Frobenius on ℓ-adic H^i, of weight i. So the result counts the p-adic units among Weil numbers of weight i.
- **The B rows on χ_p, Z_p(1), the Lubin-Tate character θ and CM by Q_{p^2}** (B-RD14, B-RD29, B-RD52, B-RD76, B-RD78) are statements about the tame part of the inertia type at p of a weight-one motive (H^1 of an elliptic curve or of a height-two BT group). The type is what enters the local factor and the conductor at p of L(E, s). So B-RD98-exact-five says that E[125] determines that tame part when e = 20.
- These links carry no RH or GRH content, because both are statements about global L-functions and the B results are purely local. Part 1's bridge section says the same for the B rows it flagged.

## Hexagon readiness (field_experts/HEXAGON_CANDIDATES.md, the five tests)

No finding in my 318 rows passes all five tests. Test 3 (stability and a literature search) is open for all of them; I searched no literature. The nearest candidates, with their gates:

1. **The p ≥ 5 index results: ν_min(5,20,2) = 2 (B-RD98-exact-five), ν_min(p,e,2) = 3 for p^3 < e < p^4 (B-RD74), and the thresholds of B-RD63, B-RD76 and B-RD100.**
   - Test 1: about a hundred rows of the chain (batches 14-23) are checked here, sixteen of them by independent re-proof (B-RD51-orbits, B-RD51-p5, B-RD56-p5, B-RD61-point-field, B-RD62-extension, B-RD70-exchange, B-RD72-first-mixed, B-RD76-determinant, B-RD83-tame, B-RD86-cyclotomic, B-RD89-base, B-RD91-first-break, B-RD94-group, B-RD96-gap, B-RD98-different, B-RD99-cyclotomic).
   - Test 4: met for those lemmas.
   - Gates:
     - the propositions and theorems of the chain outside my list need their checks from parts 2 and 3 (a8d07e78, a1cf7c6b). These are thm:B-RD49, prop:B-RD64-formal, prop:B-RD83-Lie, the irreducible-residual theorem at e = 20, the B82-B90 propositions and B96's theorem;
     - a literature search (ramification bounds for BT groups: Bondarko, Hattori and others);
     - for test 2, Herbrand and different citations should go to Serre's Local Fields rather than Colmez's course notes.
   - Test 5: moderate. It is a sharp answer to the run's version of a manuscript question.
2. **The exact p = 3 range (cor:B-RD27-exact-three; 27-torsion at e = 216).**
   - The construction lem:B-RD26-trace-arc and the bound lem:B-RD20-wild are checked here (identities recomputed).
   - Gates:
     - thm:B-RD26-wild is not in my list;
     - the input on the regularity of the Drinfeld-level ring (Carter-Strauch 2021) needs a source check;
     - a literature search (full p^n-torsion over p-adic fields).
3. **The OC chain**, which is part 2's candidate "Grothendieck's admitted integral weak Lefschetz fails".
   - My rows add a computation (B_2 = 35 and r = 556 recomputed) and recomputed every number of the exact-degree surface example (cor:OC-surface-exact-degrees: g = 7, h^0 = 2, 4, 6 and 556).
   - The gates stay as listed: a literature search, and an independent re-proof of the main theorem, which is not in my list.
4. **(8.5.1) in every degree and the unit-root count (A2-EXACT, A2-UNIT).**
   - Checked at targeted level. Test 2 inputs are published (Ogus 1975, Katz-Messing 1974).
   - Gates: a literature search (the result may be known) and an independent re-proof.
5. **The C counterexamples (C-RD4, C-RD11).**
   - Complete, and checked by part 1 and here (targeted).
   - Gates: an independent re-proof and a literature search.

None of these is one gate away with a strong test 5, so nothing is flagged for immediate posting.

## Scope

- **Done:** all 318 ids of my list, in file order, in 24 batches. There were no sub-agents and no git, and no code from the return was run.
- **Read beyond the return's statement texts:** only B.tex 12036-12050, to check the sector bound in lem:B-RD68-square.
- **Not done:**
  - the dependencies outside my list, named row by row above;
  - any literature search or source opening;
  - re-running the return's certificates.
