# Full intake of RESEARCH_SA14_SA19 (cp08): the 99 statements no intake had checked

Claude Opus 5.5 at effort max, agent a262249a0710a599b (the sweep-3 reader of cotes 43, 44 and 58-60, and the author of
the cp05 intake `INTAKE_RESEARCH_SA14_SA19_20261120.md`), 22 Nov 2026. The coordinator asked for this full intake at the
user's word ([the user's words, omitted]).
- Return: `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA14_SA19_checkpoint_08_20261120T2005Z_unzipped`.
  It is by GPT-6 Astra (ChatGPT Pro mode) and its report opens "INCOMPLETE".
- List: `field_experts/INTAKE_LEDGER.md` §9, row RESEARCH_SA14_SA19 (99 ids).
- Check events: `INTAKE_RESEARCH_SA14_SA19_20261121_full_CHECK_EVENTS.tsv`.
- Work notes: `agent_notes/a262249a0710a599b_NOTES.md`.

Terms (as in the cp05 intake):
- **confirmed**: targeted proof check; the proof was read in full and found correct.
- **background**: a cited theorem carried without opening the source; the run's locator is repeated.
- **statement level**: only the statement was read.
- **open**: the run labels the item undecided and I agree with the label.

No literature source was opened in this intake.

## H. Higher Ext of the pro-generalized Jacobian; SA19 H1-H2 (43:16, 21, 70-74, 80, 116-120)

File: `sections/H.tex`, read in full.

| Row | Statement | Run status | Check | Verdict |
|---|---|---|---|---|
| H1, H-all | in Serre's category P of commutative pro-quasi-algebraic groups over k = k̄ of char p: J_∞ = lim J_n has projective dimension <= 1, so Ext^i(J_∞, G) = 0 for i >= 2 and every G in P | Proved | targeted. Checked: 0 -> L -> J_∞ -> J -> 0 (inverse limits exact in P); L ≅ Π_{x≠x_0} G_m × Π_x U_x (the residue at x_0 splits the diagonal G_m); U_x ≅ Π_{p∤r} W (Artin-Hasse); pd G_m = pd W = 1 and pd J <= 1 (Serre 1960 §§7.5, 8.6, 9.2); Ext^2 of an infinite product into a quasi-algebraic target is the direct limit over finite subproducts (§3.4 Prop. 7), then Prop. 9; the long exact sequence. Serre's results were not opened | **confirmed** (given Serre 1960). **This settles our research package RP2 of c43_c44** (43:80, Ext^{>=2}(J_{K/k}, G) = 0) positively, for the connected object |
| H2, H-Ga | Ext^i(P, B) = 0 for i >= 2, every P in P and every connected quasi-algebraic B (in particular G_a) | Proved | deduction read: elementary sources (Serre §8.6 Cor. 5 for G_a; pd <= 1 for finite groups, G_m and abelian varieties), composition series, §3.4 Prop. 7, §10.1 Th. 1 | **confirmed** as a deduction (sources not opened) |
| H3 | Ext^*(J_∞, G) = H^*(K, G) fails in degree 0 without the augmentation by Z | Refuted comparison | targeted: Hom(J_∞, Z/ℓ) = 0 (J_∞ is connected) while H^0(K, Z/ℓ) = Z/ℓ; 43:80's J'_{X/k} is an extension of Z by a connected group | **confirmed** |
| H3b | no source P on the perfect étale site gives Hom(P, G^perf) ≅ H^0(k(t), G) naturally in G | Refuted claim | targeted: Frobenius on G_a is bijective on Hom(P, G_a^perf) but not surjective on k(t) (p·v_0(h) = 1 is impossible) | **confirmed** |
| H4 | for A = k[[s,t]]: H^2_{m,ét}(A, Z/p) = 0 and H^3_{m,ét}(A, Z/p) ≅ ⊕_{(i,j), p∤gcd} (k, +) | Proved | targeted: E = H^2_m(A) = ⊕ k e_{i,j}; F(a e_{ij}) = a^p e_{pi,pj} is injective - 1 on each orbit p^r v (finite support); coker(F - 1) on an orbit ≅ k by Σ a_r e_{p^r v} -> Σ a_r^{p^{-r}} (k perfect); Artin-Schreier | **confirmed** |
| SA19-H4 | the Lead: the concentration of local cohomology of groups (43:70-74) and a projective local Jacobian carry over to étale cohomology | Refuted | through H4: the Zariski statement of 43:70-74 stands; the étale one with Z/p coefficients fails in degree 3 | **confirmed (refuted)**. Our c43_c44 §3 statement ("concentrated in degree d") holds for Zariski cohomology and unipotent coefficients only; carry that scope into the reading |
| H4b | Toën's local Jacobian J_x of k[s,t]_{(s,t)} is not projective: Ext^1_naive(J_x, Z/p) ≅ E/(F-1)E != 0 | Refuted claim (of projectivity) | targeted: the Artin-Schreier pullback extension splits iff (F-1)h = s^{-1}t^{-1} has a solution in E_0 = E, and it has none; Ext^1(J_x, G_a) = 0 by Toën 2026 Lemma 3.9 (not opened) | **confirmed** (given Toën) |
| H5 | on (Perf/k)_ét, Ext^n(J_∞, G) ≅ Ext^n_P(J_∞, G) = 0 for n >= 2 and quasi-algebraic G | Proved | statement level for the comparison: Suzuki 2022 Prop. 3.8.1 and Rem. 3.8.4 (not opened); J_∞ is in their class (an extension of an abelian variety by an affine pro-group) | **background**; the deduction from H1 is immediate |
| SA19-H1, R10 | 43:117's duality of π_0(A), π_0(B) in Q/Z is SGA 7 IX (1.2.1) with perfectness Conj. 1.3, proved by Suzuki (2020, Th. C) for perfect residue fields; the claimed 1962-64 date of the leaf is not established | Known; chronology undetermined | statement level; the dating argument was read: the dates near 43:117 are bibliographic or administrative, and the catalogue gives cote 43 the span 1961 to about 1968 | **background**; the run is right that our R10 (c43_c44 §1.5) and Lead SA19-H1 cannot date 43:117 to 1964-65. **Erratum for the c43_c44 reading**: "about 1963" is unsupported; say "undated (cote 43: 1961 to about 1968)" |
| SA19-H2 | the three-variable Ext of 43:16, 21 is the biextension formalism (SGA 7 VII Cor. 3.6.5; Mumford 1969); pre-SGA 7 priority is not established | Known; chronology undetermined | statement level | **background**; the same erratum for our Lead H2 |

## I. The endomorphism algebra of the residual complex (43:45-69)

File: `sections/I.tex`, read in full except the input file `work/bce/I_strict_dense_columns.tex` (I7b), whose statement only was read.

| Row | Statement | Run status | Check | Verdict |
|---|---|---|---|---|
| I1 | regular local A: End^0(K) = Π_p Â_p (product of adic topologies), End^{<0}(K) = 0 | Proved | targeted: Hom(E_p, E_q) = 0 unless p ⊆ q (a ∈ p∖q kills E_p locally nilpotently, acts invertibly on E_q); Matlis End(E_p) = Â_p | **confirmed** |
| I2, I-2d | A = k[[s,t]]: End^*(K) with θ is universal for complete graded topological algebras with degree zero F × Π R_p × A, θ^2 = 0 and incidence; End^1 = 𝔸 ⊕ P, End^2 = 𝔸/F, product c∘a = [(c_p a_p)] | Proved | targeted: residual resolution 0 -> A -> F -> ⊕E_p -> E -> 0; Hom(E_p, E) = R_p free of rank 1 with basis δ_p (Schenzel 2013 Th. 1.1, not opened); 𝔸 = S^{-1}P (factoriality); dualizing gives 0 -> A -> P -> D(F) -> E -> 0 and End^2 = D(F) = 𝔸/F; the degree-2 relation is the diagonal F (not one zero relation per intermediate prime); the two topologies on P (product adic, and τ_p with basis m^N A + f_p^n R_p); the universal morphism and its continuity read | **confirmed**. **Settles our research package RP1 of c43_c44 in dimension two, degree two** (43:65-66: "𝒜 libre pour ces propriétés"), with the caution that the two occurrences of P carry different topologies |
| I3 | the same for every regular local surface, with the completions C_p of R_p in τ_p | Proved | read: injectivity and density of R_p -> Hom(E_p, E), End^1 = S^{-1}P ⊕ C, End^2 = S^{-1}C/S^{-1}B, extension of the universal map by uniform continuity | **confirmed** (structure) |
| I4 | adjacent arrows p ⊂ q in any dimension: T = Â_p -> Hom(E_p, E_q) injective and dense, basis m^N R + (pR_p)^n T | Proved | read: pd_R(R/I_n) <= h, the surjection E_p[I_n] -> E_q[I_n], Gorenstein generation by e_n/u, commensurability of W_n with R/I_n | **confirmed** (structure) |
| I5 | the subalgebra generated by degree zero and θ is dense in every degree | Proved | targeted: induction on the height gap through the surjection ⊕ E_r[I] -> E_q[I] (pd <= d-1) and injectivity of the hulls | **confirmed** |
| I6 | closed-image exactness of the columns Hom(E_p, K_R^j), j > h | Proved | read: v ∉ p kills Ext^j(R/I, R) for j > h; the class restricted to Re is v times a class, hence zero | **confirmed** (structure) |
| I7 | complete regular local A: the column Hom(E_p, K^•) is exact, with open surjections onto cycles for j > h+1 | Proved | targeted: Ext^j(E_p, A) = Hom(Tor_j(E_p, E), E) and E_p ⊗^L E = E_p ⊗^L_{A_u} E_u = 0 for u ∈ m∖p | **confirmed** |
| I7b | the same density without completeness | Proved | statement level only (the input file was not read) | **statement level** |
| I8 | the full presentation in every dimension, in the category of separated complete graded topological A-algebras with a basis of open left ideals | Proved | targeted, structure: Cousin complexes; the universal property (I8.1) of C_J = K[J] for a regular sequence J (Koszul self-duality, Stacks 0BQZ); the surjection (I8.2) ⊕C_J -> M; every residual endomorphism acts on every discrete Cousin complex (kernel preserved by density, I5); targets Q decompose as lim Q/L of shifted Cousin complexes, giving φ = lim φ_L, multiplicative by density | **confirmed** (structure). **This settles RP1 in every dimension in that category**; the run is right that the transcription of 43:64-66 does not fix the category |
| I-all, I-full, SA19-H3 | the presentation for an unspecified completion (43:64-66), and the Lead SA19-H3 | Undecided | statement level; the gate read: I8 settles it for open-left-ideal topologies; I2-I3 hold in the enlarged category for surfaces | **open**, correctly labelled; the remaining question is a reading of 43:64-66, not mathematics |

## J. The programme of 1964 (44:2-9) and SA19 H5-H6

File: `sections/J.tex`, read in full.

| Row | Statement | Run status | Check | Verdict |
|---|---|---|---|---|
| J0 | textual scope: the complementary index is n+1-i (the letter at 44:8: "J^i et J^{n+1-i} sont canoniquement duales"); the manuscript's equivalence relation is unidentified ("que je ne sais pas bien identifier") | Proved textual scope correction | targeted against my reading c43_c44 §2.1 (Th. 3's overwritten superscript; the mathematics requires n+1-i) | **confirmed** |
| J1i | Saito's incidence quotient P^i_inc (any codimension, any characteristic), with 2 dim <= b^{2i-1}; the family kernel N_inc(ξ) = ker f_ξ as group schemes (J1i.1) | Known, with the derived kernel statement proved | targeted on (J1i.1): universality gives one inclusion, and θ_X^i being itself a Picard homomorphism (Saito (3.5)) gives the other; Saito 1979 not opened. Kleiman 1971 p. 446 credits the boundedness to an unpublished 1964 observation of Grothendieck (background) | **confirmed** for the derived statement; the rest **background** |
| J1-Th1 | Th. 1 (44:2): N(ζ) is the kernel ("ensemblistement" in Codex, "en substance" in Pro) | Proved for common incidence or regular-test kernels | through J1i. The identification with his undefined N(ζ) is a textual gate. The single-self-incidence shortcut of 44:9 is refuted on E×P^1×P^1 (the self-pairing is 0 while N_inc = 0) | **confirmed** for the incidence reading. Our c43_c44 §2.1 decided the reading conflict on the scan ("(ensemblistement)", an insertion); the run did not have that decision |
| J1-Th2 | Th. 2: the dimensions are bounded by ½b^{2i-1} | Known for incidence; all-regular open | statement level: Saito Prop. 3.4; ACMV Prop. 8.2 for i = 1, 2, n | **background** |
| J1-Th3, J2-isomorphism, J2a | Th. 3 with n = 3, i = 2: the intersection of cycles gives a canonical isomorphism Ab^2(X) -> Ab^2(X)^∨ | Refuted | targeted, on X = Jac(C), C: y^2 = x^7 + a_6x^6 + ... + a_0, generic over F_5. (i) H^1(B) is a Galois quotient of Λ^3V(1) = V ⊕ P (Sp_6 monodromy, Achter-Pries, not opened). (ii) P is excluded: an ordinary specialization (y^2 = x^7 - x has Cartier-Manin determinant 2 mod 5) puts a slope -1 eigenvalue in P, which is impossible on H^1 of an abelian variety, so dim B <= 3. (iii) The translation family z_t = [C+t] - [C], with [C] = θ^2/2, gives u^∨ρu = ±2λ_A, hence deg u = 8. (iv) A[2](k) is the irreducible S_7-module F_2^7/⟨1⟩, so no Galois-stable kernel of order 8 exists | **confirmed (refuted)**. A rational pairing or an isogeny is not refuted; Saito's isogeny duality stands |
| J1-Th4, J2-positivity, J2b | Th. 4 and the letter of 12.8.1964: the raw middle autoduality is a polarization up to one sign | Refuted | targeted: X = E×P^1×P^1, Ab^2 = E^∨×E^∨. D = r_*(p^*z·q^*z) gives ρ = [[0,λ],[λ,0]] (h_1^2 = h_2^2 = 0, ∫h_1h_2 = 1). Pullback along the diagonal and the antidiagonal gives 2λ and -2λ, so neither ρ nor -ρ is a polarization | **confirmed (refuted)**. His own correction at 44:8 ("il faut tenir compte de la décomposition primitive") is consistent: the Gram matrix on sum and difference is diag(2,-2) |
| J1-Th5 | Th. 5 (44:4) in higher codimension: ⟨ζ,ζ'⟩ = (-1)^m Z·Z' for a pencil with geometrically integral fibres | Refuted | targeted, every computation. X = V(x_0x_3 + x_1x_4 + x_2x_5) over F̄_3, with the pencil x_2 = tx_5 (fibres of rank >= 4, integral). The planes α = V(x_3,x_4,x_5), β = V(x_2,x_3,x_4), α' = V(x_0,x_1,x_5), β' = V(x_0,x_1,x_2) lie on X. α∩Y = β∩Y = L and α'∩Y = β'∩Y = L', so ζ = ζ' = 0. α∩α' = {e_2} and β∩β' = {e_5}, both transverse, and the crossed intersections are empty, so Z·Z' = 2 | **confirmed (refuted)**. It agrees with our c43_c44 §2.2, where Th. 5 was re-proved for surfaces with integral fibres; the failure begins in higher codimension |
| J1-Th6, J6C | Th. 6 middle clause (2i = n): the fixed factor of P^i(Y) is the image of P^i(X) | Refuted (the literal middle clause) | targeted. The cubic fourfold x_0^3 + x_1^3 + x_2^3 + x_3^2x_4 + x_4^3 + x_5^3 = 0 over F̄_5 is smooth (gradient checked). The pencil x_5 = tx_4 has members with a = 1 + t^3 and is geometrically integral. Its axis is the cone over the Fermat cubic E. H^3(X) = 0 gives Ab^2(X) = 0. The multiplicity of B at p is 3 (v(1 + av^2) = -(u_0^3 + u_1^3 + u_2^3)), which gives N_S·ℓ = -2 and vu = [-2] on J = Pic^0(E): a constant elliptic factor in Ab^2(Y) | **confirmed (refuted)** for the literal clause (singular axis); the smooth-axis version is J6P. The stable and high ranges stay open, so J1-Th6 overall is **open** |
| J6L | conditional: under B(X) (resp. B(Y)), j^*: P^i_inc(X) -> P^i_inc(Y) is an isogeny for 2i <= n-1 (resp. surjective for 2i >= n+1) | Proved under explicit algebraicity hypotheses | targeted: the detection lemma (a correspondence acting as zero on H^{2a-1}(a) induces zero on incidence varieties, through a miniversal cycle and a Picard realization); β = Λ_X∘j_* inverts j^* on H^r; hard and weak Lefschetz (Deligne 1980, not opened) | **confirmed** (conditional) |
| J6P | smooth pencil axis, n >= 4: im(j^*) = im(trace) in Ab^2(Y); for n >= 5, j^* is surjective | Proved under explicit smooth-axis and generic hypotheses | read: the blow-up formula Ab^2(X̃) = Ab^2(X) × Pic^var(B); the exceptional summand lands in im(j^*) through the isogeny Pic^var(X) -> Pic^var(B); Lang-Néron and the constant Galois action on T_ℓA for n >= 5 | **confirmed** (structure; ACMV and Conrad not opened) |
| J6Z | j^*: P^{n-1}_inc(X) -> Alb(Y) is surjective in every characteristic | Proved | targeted: Pic^var(Y) -> Alb(Y) by H_Y^{n-2} is an isogeny (hard Lefschetz on H^1(1) -> H^{2n-3}(n-1)) and factors through j^* | **confirmed** |
| JWalker | complex Walker Abel-Jacobi: ω is universal among all regular homomorphisms iff dim im(ψ, φ) = dim J_a for every regular φ | Unresolved; exact equivalent dimension test | targeted on the equivalence (initiality among isogeny lifts, ACMV-Walker Th. 2.3, not opened) | **confirmed** (the equivalence); the question is **open** |
| J1-Th7 | Th. 7 (44:6): numerical equivalence = τ-equivalence | Refuted | targeted on the data: the Fermat quartic is smooth of genus 3; the Ceresa cycle Z = a_*[C] - [-1]_*a_*[C] has class 0 ([-1] = +1 on H^4), hence is numerically trivial; its infinite order modulo algebraic equivalence is Bloch 1984 Th. (4.1) (not opened); the product with P^m gives every intermediate codimension | **confirmed (refuted)**, given Bloch. It agrees with our c43_c44 §2.3 refutation (Griffiths) |
| SA19-H5 | the Lead's open-status classification of the seven theorems | Refuted as stated; corrected programme | statement level: the run's table. Th. 1-3 are settled for incidence; Th. 3, 4, 5, the Th. 6 middle clause and Th. 7 are refuted; the Th. 6 stable range is conditional or open | **background** |
| SA19-H6 | no rational-point-to-section injectivity in cote 43; H6a: the sweep's variance is reversed | Complete scoped audit; inferred π_1 injectivity refuted | targeted on H6a: injectivity of the pullback of characters ⟺ surjectivity of π_1(U)^ab -> π_1(J)^ab (Z/4 -> Z/2 shows that the kernel is not detected); H6b (the audit of 195 files) at statement level | **confirmed** (H6a); H6b **background**. **Erratum** for our SA19 Lead H6 (the variance) |

## F. The local fundamental group (58:19), the rows added after cp05: F7-F13h

File: `sections/F.tex` lines 634-2278. Read: every statement, and the proofs of F7, F7b, F8b, F9b, F10b, F10c, F11, F12,
F12b, F13f, F13g and F13h. The long proofs of F8 (root stacks), F9 (gluing), F10 (refined Swan conductor), F13, F13a-F13e
were read at the level of the statement and the structure only.

| Row | Statement | Run status | Check | Verdict |
|---|---|---|---|---|
| F7 | for a fixed SNC resolution X of a complete normal local surface in char p, h^1(U, M\|_U) <= C_X·rank M for every F_p-local system M on X (any monodromy) | Proved | targeted: V\|_C is semistable of degree 0 (trivialized by a finite étale cover; subbundles have degree <= 0), so h^0(V\|_C ⊗ T) = 0 for deg T < 0 and h^1(V\|_C) <= r g(C); with these bounds F5's nearby-cycle argument goes through with the same cutoff m_0 | **confirmed** (given F5's structure, checked in the cp05 intake) |
| F7a | relative generation criterion for a normal pro-p kernel over a finitely generated quotient | Proved | statement level | **statement level** |
| F7b | a quotient G with normal pro-p P whose G/P factors through π_1(X) is finitely generated, with a bound depending only on X | Proved | targeted: simple F_p-modules kill P (invariant vectors), so they extend over X and F7 applies; π_1(X) ≅ π_1(D) (proper base change, Stacks 0A48) is finitely generated (SGA 1 X 2.9) | **confirmed** |
| F8 | h^1(U,M) <= C_X·rank M for every F_p-local system tame along D (any monodromy) | Proved | statement and status read (root-stack proof, independent root audit and BCE check by the run); proof not read | **statement level** |
| F8b | every pro-p-by-pro-prime-to-p quotient of π_1(U) is uniformly finitely generated | Proved | targeted on the deduction: simple modules have prime-to-p monodromy, hence are tame; F8; Γ is a quotient of π_1^{(p')}, finitely generated (Grothendieck-Murre); F7a | **confirmed** as a deduction from F8 and F7a |
| F9 | uniform generator bound for the full tame local quotient | Known method; proved here | gluing part read (SGA 1 XIII Cor. 2.12, not opened) | **background** |
| F9b | normal pro-p kernel over a tame quotient: d(G) <= max(d_X, ⌈C_X⌉+1) | Proved | deduction from F8, F9, F7a read | **confirmed** as a deduction |
| F10 | the kernel of π_1(U)^ab -> π_1(X)^ab is finite, killed by p^e\|det B\|; Swan conductors s_i(χ) <= t_i with t = (-B)^{-1}k | Proved | statement read; the proof rests on Krishna-Majumder, arXiv:2601.12177v2 (8 Nov 2026), Cor. 9.7 (not opened) | **statement level** |
| F10b | one fixed abelian cover U' -> U and resolution X' remove the inertia of every abelian-monodromy system | Proved | targeted: Q' ∩ I = 0, valuative extension to X, purity | **confirmed** (given F10) |
| F10c | h^1(U,M) <= C_A·rank M for every prime ℓ and abelian monodromy | Proved | targeted: ℓ = p by F7 after F10b; ℓ != p: the cocycles factor through the tame quotient (wild inertia is pro-p), F9; inflation-restriction with d(F) | **confirmed** (given F7, F9, F10) |
| F11 | **every metabelian quotient of π_1(U) is topologically finitely generated**, with a bound depending only on A | Proved | targeted: a minimal normal M ⊂ F' of a finite metabelian quotient is a simple F_ℓ[F]-module on which F acts through F/F' (abelian), so F10c gives (F11.1), and the complement counting of F4 applies | **confirmed**, given F10c (hence F7, F9, F10). The strongest new step toward his conjecture of 58:19 |
| F12 | h^1(U,M) <= C·rank M for simple F_p-systems with metabelian monodromy | Proved | targeted on the deduction: Γ' is prime to p (Lemma F12a, not read); after the F10b cover the system is tame; F8; inflation-restriction | **confirmed** as a deduction (given F8, F12a) |
| F12b | quotients whose closed second derived subgroup is pro-p are uniformly finitely generated | Proved | deduction from F11, F12, F7a read | **confirmed** as a deduction |
| F13, F13a, F13b, F13c, F13d, F13e | the derived-length-three programme: uniform logarithmic conductor after one cover; induction from characters for abelian-by-abelian groups; invariance of the Swan cutoff; bounded p-power twists; a degree-linear tame-generator criterion; refined-Swan zeros | Proved (F13d: a criterion) | statement level (proofs not read) | **statement level** |
| F13g | a Swan divisor S != 0 on a resolution has a component with s_i > 0, S·C_i < 0 and p \| s_i | Proved | targeted: for p ∤ n the refined Swan residue n·ū != 0 gives a nonzero section of O_X(S)\|_{C_i}, so S·C_i >= 0; S^2 < 0 by negative definiteness (Krishna-Majumder Cor. 9.6-9.7 and Lemma 9.11, Yatagawa 2017, not opened) | **confirmed** (given the cited global refined Swan section) |
| F13f, F13h | under the cutoff t_i < p, all derived-length-3 quotients are uniformly finitely generated; the exponent e with p^{e+1} > max t_i | Proved | targeted on the deductions from F13g (Swan divisors with all coefficients < p vanish) | **confirmed** as deductions |
| F, F-full | his conjecture of 58:19 in full | Undecided | the gate: derived length >= 3 without the cutoff, and nonsolvable wild quotients | **open**, correctly labelled |

## A, D, E: the rows added after cp05, and the rows left open in the cp05 intake

Files read in full:
- `work/root/A1_known_targets.tex`;
- `work/dgj/A2_cartier_leading.tex`, `A2_closed_forms.tex`, `A2_target_frobenius.tex`, `A2_target_surfaces.tex`,
  `A2_fierce_cover.tex`;
- `work/root/A2_multisection_exclusion.tex`;
- `work/dgj/attempt_A2_Gs_smooth_surface.tex`;
- `work/dgj/section_D_partsch.tex`;
- `sections/E.tex` Theorem E4.Curve.

| Row | Statement | Run status | Check | Verdict |
|---|---|---|---|---|
| A1Q | Pic(X) -> Pic(Y) is injective (n >= 3) and an isomorphism (n >= 4) when the smooth ample Y is quasi-F-split; an isomorphism for n = 4 when Y is Fano | Known; derivation proved | deduction read: Petrov 2025 Cor. 4.10(2) and Kawakami-Tanaka 2025/2026 (not opened) give H^i(Y, A^{-m}) = 0 for i = 1, 2; then A4c | **background**; deduction confirmed |
| A2V | a nonzero closed one-form vanishing along a smooth ample Y has order m = pa; if it is Cartier-fixed, then ker(F: H^1(Y,L^{-a}) -> H^1(Y,L^{-pa})) != 0, and h^0(Ω^1_X) >= h^0(O(pY)) | Proved necessary condition | targeted: dη = 0 gives m dt∧α ≡ 0 mod t, so p ∤ m would make the leading term conormal, in H^0(L^{-m-1}) = 0; Cartier: Cα = t^{(p-1)a}α, so the tangential leading term lies in B^1 ⊗ L^{-a}; the sequence 0 -> L^{-a} -> F_*L^{-pa} -> B^1 ⊗ L^{-a} -> 0; the local model d log(1 + t^p x) | **confirmed** |
| A2W | if every global one-form is closed and L is very ample, then H^0(Ω^1 ⊗ L^{-1}) = 0, so Picard restriction is injective for n >= 3 | Proved under explicit closedness hypothesis | targeted: d(s/s_0) ∧ η = 0 for coordinate ratios spanning Ω^1_K contradicts η != 0 (n >= 2); the bound (A2W.2) | **confirmed** |
| A2Y | injectivity holds if Frobenius is injective on H^1(Y, O_Y), or if Y lifts to W_2(k) | Proved under either explicit target hypothesis | targeted on (i): j_s: H^1(Y, L^{-a}) ↪ H^1(Y, O_Y) commutes with F; (ii) Langer 2011 Cor. 11.2 (not opened) | **confirmed** ((ii) given Langer) |
| A2S-cross | a threefold point-kernel target Y is of general type, with a^2 L^2 <= B_p(Y) | Known deduction | deduction from A2V and A3s read | **background** (A3s's sources not opened) |
| A2Z | a degree-p separable cover with smooth integral Y = π^*C cannot kill p-torsion of Pic(C) | Proved construction exclusion | targeted: Y is the normalization of the μ_p-torsor T and ρ is purely inseparable; ω_Y = ρ^*ω_C(-D) (conductor) against ω_Y = ρ^*ω_C ⊗ O(R)\|_Y with R >= Y; intersecting with Y^{n-2} gives 0 = R·Y^{n-1} + D·(Y\|_Y)^{n-2} > 0 | **confirmed** |
| A2P | a relative Frobenius multisection of a P^1-bundle cannot kill p-torsion of its base | Proved construction exclusion | targeted: Q^{p-1} ≅ O_Y(-D) with Q ample (its p-th power is the normal bundle) is impossible | **confirmed** |
| A2Gs-cross | no smooth projective surface Z with a smooth ample curve D and a line subbundle O(-D) ⊂ T_Z tangent to D; so no G_s-torsor has a smooth total space with a smooth inverse image of Y | Undecided candidate exclusion; independent audit pending | **independent check** of every step: O_D(-D) ≅ T_D gives D^2 = 2g - 2 > 0, K·D = 0, c_2 = -D^2 < 0; κ = 0 is excluded (c_2 ∈ {0, 12, 24}, Liedtke, not opened); ruled case: I re-derived 2b = a(e + 2g - 2) + Σm_i, D^2 = 2a^2(g-1) + Σm_i(a - m_i), and (2a^2 - 4)(g-1) + Σ(m_i(a - m_i) + 1) = 0, impossible for a >= 2 and for a = 1 | **confirmed**. This check can serve as the audit the run asked for; the exclusion is proved, and A2 stays open |
| D4b | a deformation of a Jacobian ordinary Igusa surface need not lift its Albanese elliptic fibration (against Partsch 2013, Prop. 6.6, Th. 6.7, Prop. 6.9) | Refuted | targeted: a lifting f would give f^*: Pic^0_{C/R} -> Pic^τ_{X/R} lifting Pic^var(X_0), which D4a excludes (confirmed in the cp05 intake given Katz); the étale-source rigidity counterexample h: Z/2 -> μ_2 over k[ε], h(1) = 1 + ε, checked | **confirmed (refuted)**, given Katz 1981. A correction to a published paper; Partsch was not opened |
| E4-315schemeCurve | Pic_{C/S} is a smooth separated scheme for every proper smooth curve family with geometrically connected fibres, over any base | Proved | read: g != 1 is locally projective (BLR 9.3); for g = 1, Pic^n = C/E[n] is a scheme since finite sets lie in an affine (BLR 6.6 Th. 2(c), not opened); approximation | **confirmed** (structure). Probably known; not claimed new |
| A1, A2, SA14-H4 | the main question and the boxed "noyau nul" | Undecided | gates read: A1r, A4, A4b, A2D (cp05 intake) and the new exclusions A2V-A2Gs | **open**, correctly labelled |
| SA14-H7, E4, E4-315schemeNormal, E4-315schemeIntegral | schematicity of Pic over an arbitrary base for normal or integral fibres | Undecided | gate read; the curve case is now E4.Curve | **open**, correctly labelled |
| E4-308, E4-312 | a title leaf and a tensor-product insertion | no claim | statement read | **no claim** |
| E4-309bprime, E4-3105diagram, E4-3106criterion | reading questions on 57:309-310 | readings | statement read; not checked on the scan here | **reading questions**; to a scan check |
| E4-309h | hyperplane Pic^τ bijectivity, delegated to Part A | delegated | see A1, A2 | **open** with A1-A2 |
| R3u | = SA14-H1 (generic kernel infinitesimal unipotent) | Proved | confirmed in the cp05 intake under the id SA14-H1 | **confirmed** (cp05 intake) |
| R4 | = A4b (bounded finite p-groups) | Proved | confirmed in the cp05 intake under the id A4b | **confirmed** (cp05 intake) |
| R2, R5 | our R2 (57:144 relation up to sign) and R5 (Igusa's b_2 factor 2) | Carried as background; not used | statement level | **background** |
| R7 | my result of c58_c60 §2.5(d): μ_x = 0, so δ^♮(E)^2 = q^{χ^♮(E)} at 60:53 | Carried as background; not used | statement level here (the proof is mine, c58_c60 §2.5(d)) | **background** (no independent check yet) |
| K | the register itself | register | read as the source of statements | **no claim** |

## Summary

**Checked in this intake: all 99 ids.** Counts by type are in §Counts below. The cp05 intake (Parts A-G) is not repeated
here.

**Refutations confirmed.** Each is a counterexample that I checked:
- **J2a.** No integral intersection autoduality Ab^2 ≅ (Ab^2)^∨ on the generic genus-3 hyperelliptic Jacobian in char 5.
- **J2b.** E×P^1×P^1: the raw middle autoduality is not a polarization for either sign.
- **J5.** A split quadric fourfold over F̄_3: Th. 5 fails in codimension 2 (0 = 2).
- **J6C.** A cubic fourfold over F̄_5 with a singular-axis pencil: the Th. 6 middle clause fails.
- **J1-Th7.** The Fermat-quartic Ceresa cycle, given Bloch.
- **H3, H3b, H4b, SA19-H4.** H4: H^3_{m,ét}(k[[s,t]], Z/p) is infinite.
- **D4b.** Against Partsch 2013, given Katz.

**Positive results confirmed.**
- **H1.** pd J_∞ <= 1 in Serre's category. This settles our RP2 of 43:80 for the connected object.
- **I2/I3/I8.** The presentation of End^*(K^•) of the residual complex. This settles our RP1 (43:45-69) in dimension 2,
  and in every dimension for open-left-ideal topologies.
- **J6L, J6P, J6Z.** Lefschetz for incidence and algebraic representatives, in the stated scopes.
- **F7-F12b, F13f-F13h.** In particular F11: every metabelian quotient of the local π_1 of a complete normal surface in
  char p is finitely generated, given F8 and F10, which were read at statement level.
- **A2V-A2Gs.** Necessary conditions and construction exclusions for A2. My check of A2Gs is the independent audit the run
  asked for.

**Errata for our readings** (to carry into c43_c44):
- the date "about 1963" for 43:117 is unsupported; cote 43 runs from 1961 to about 1968 (H, SA19-H1);
- the variance in our Lead SA19-H6 is reversed;
- the concentration claim of 43:70-74 holds for Zariski cohomology only (H4).

**New against the literature** (none opened here, so novelty is not established):
- J5, J2a, J2b and J6C are explicit counterexamples to Grothendieck's unpublished 1964 statements;
- F11 and F12b are partial results toward his local π_1 conjecture of 58:19;
- I8 is a presentation theorem;
- D4b corrects a published paper.

## Hexagon readiness (field_experts/HEXAGON_CANDIDATES.md, the five tests)

None passes all five tests today.
- **Counterexamples to Grothendieck's 1964 programme** (J5; J2b; J2a; J6C).
  - Tests 1 (complete) and 2 (self-contained) pass: elementary inputs, published sources cited.
  - Test 4: my targeted check exists, and J5's intersections were recomputed by hand; a scripted independent computation
    is still to be recorded.
  - Test 3 is the gate: the JAC1964 run (Hexagon entry H11, "Grothendieck's 1964 Th. 4 for abelian varieties") treats the
    same theorems. Consistency check: J2b's threefold is not an abelian variety, so the two do not conflict, but the post
    must be coordinated with H11.
  - Test 5: moderate.
  - **One gate away** (test 3).
- **A3** (a very ample H^1 counterexample to Kodaira vanishing on a surface in char 2; cp05 intake).
  - Tests 1 and 2 pass.
  - Test 4 needs an independent computation: running `code/certify_A3.py` from a work folder.
  - Test 3 needs a literature search: the root-cover trick may be folklore.
  - Test 5: strong.
  - **Two gates.**
- **G1** (Pic^δ has a universal section iff at most one elementary divisor is odd; cp05 intake).
  - Tests 1, 2 and 4 pass: the existence half was derived independently in my c58_c60 §4.4 before the run, and the run's
    necessity half was confirmed by a targeted check.
  - Test 3: a literature search of the theta-characteristic literature is needed.
  - **One gate.**
- **D4o, D4b, D4-gap** (corrections to published claims: Chai-Oort §3.9(iv), Chai Th. 2.4(iii), Partsch 2013). These are
  better handled as notes to the authors (informing-authors memory) after the sources are opened; this is not a Hexagon
  post now.
- **F11.** Not ready: test 2 (the input Krishna-Majumder 2026 is a preprint) and test 4 (F8 and F10 not independently
  checked).

## Counts (check events of this intake, by type)

- carried as background without fault found: 43
- independent re-proof: 1
- refuted, with the refined statement's id: 5
- targeted proof check: 50
- Total: 99 events for 99 ids.

## Second pass (deepening the carried rows), 22 Nov 2026

At the coordinator's request, the rows I had carried at statement level whose proofs are in the return were read in full.
New check events are appended to the TSV; the old ones are kept.

| Row | What was read | New check | Verdict |
|---|---|---|---|
| F8 | the whole proof (F.tex 777-1140): root stack X_N (Abhyankar, purity); semistability of V on each gerbe component; coarse estimates (F8.3)-(F8.5); the Frobenius-cokernel slope bound b_i = 2(p-1)K_i/p independent of N (Sun's T^a(Ω^1) filtration); the uniform cutoff m_0; the character cancellation (F8.13), which gives h^1(J^{-m}V/V) <= r m Σ c_i(g_i+ν_i+mL_i+1) independent of N; the proper term (F8.15) | targeted proof check | **confirmed**, given Sun 2008 Th. 3.7, Suzuki 2023 Props. 2.1 and 3.1, and the root-stack conventions of Cadman and Borne (not opened) |
| F10 | the whole proof (F.tex 1327-1474) | targeted proof check | **confirmed**, given Krishna-Majumder (arXiv:2601.12177v2, a preprint) Cor. 9.6-9.7, Th. 9.4, Lemma 3.2. The steps checked: S·C_i >= -k_i from the residue sequence; C = -B is inverse-nonnegative (the run's proof checked), so s <= t; Witt restriction; I is killed by b p^e in a finitely generated Q, hence finite |
| F11 | its chain F7, F8, F9, F10, F10b, F10c, F4 | used and rechecked | **confirmed** at the level of targeted proof checks. The only unopened input that is not a published theorem is the Krishna-Majumder preprint (through F10) |
| F7a, F9 | the full proofs (relative complement counting; surjection π_1(𝔇_N) -> π_1(𝔛_N), central gerbe inertia, SGA 1 XIII 2.12, gluing over the dual graph) | targeted proof check | **confirmed** |
| F12 | Lemma F12a now read (normal p-subgroups act trivially on simple F_p-modules) | targeted proof check | **confirmed** |
| F13, F13a, F13b, F13c, F13d, F13e | the full proofs (F.tex 1680-2135) | targeted proof check | **confirmed**: F13a monomiality through a maximal isotropic subgroup of the commutator pairing; F13b Riemann-Hurwitz and the projection formula; F13 given Kato-Saito Th. 1.3 and Abbes-Saito Prop. 3.15(3); F13c divisibility of H^1(X_1, Q_p/Z_p) from H^2(D_1, F_p) = 0; F13d as a conditional criterion; F13e the degree-linear bound on refined-Swan zeros. The gates (F13.5) and (F13.6) remain open, as the run says |
| I7b | the whole proof (work/bce/I_strict_dense_columns.tex) | targeted proof check | **confirmed**: openness by the v-trick using the given preimage (no completeness needed); density by I6; product topology |
| A3 | `code/certify_A3.py` rerun from a work folder (python -I -B through a runpy wrapper; outside the return) | computation | **reproduced**: GF(2) ranks 147, 105 and 70; nullities 210, 186 and 160, equal to Riemann-Roch; h^0(Q) = 6, h^1(Q^{-1}) = 1, Q^2 = 16, K·Q = 20, χ = -2, h^1(O_S) = 9; totals 562, 1 and 565. The basis equals the run's JSON as data; the byte hash differs only by line endings. This reruns the run's own code. With my cp05 hand derivations of every dimension, it meets the computation half of A3's test 4 |
| SA19-H5 | the run's corrected classification of the seven theorems | targeted proof check | **consistent** with every J-row verdict confirmed in this intake |

**Still carried after this pass.** These rows rest on unopened cited sources, or carry no claim:
- **On cited sources:** H2, H-Ga, H5 (Serre 1960, Suzuki 2022); J1-Th2 (Saito, ACMV); SA19-H1, SA19-H2, R10 (SGA 7, Suzuki 2020, Mumford 1969); A1Q (Petrov, Kawakami-Tanaka); A2S-cross (A3s sources); F1-type citations.
- **Not in this return:** R2, R5, R7. R7 is my own result, in c58_c60 §2.5(d).
- **Open:** A1, A2, SA14-H4, SA14-H7, E4, E4-315schemeNormal, E4-315schemeIntegral, I-all, I-full, SA19-H3, F, F-full.
- **No claim or reading questions:** E4-308, E4-312, E4-309bprime, E4-3105diagram, E4-3106criterion, E4-309h, K.

**Hexagon update.**
- **A3.** The computation half of test 4 is met (the rerun). Its remaining gate is test 3, a literature search on very
  ample counterexamples to Kodaira vanishing for H^1 on surfaces in characteristic p. **One gate away.**
- **F11.** Test 4 is now met at the level of targeted proof checks. Test 2 still fails: F10 rests on the Krishna-Majumder
  preprint (arXiv, 8 Nov 2026). Gates: that input, and a literature check (test 3). **Two gates.**

## Counts after the second pass

- second pass, computation or formal certificate: 1
- second pass, targeted proof check: 13
- second pass, used and rechecked in this run: 1
- Total events in the file: 114 (99 first-pass, 15 second-pass).
