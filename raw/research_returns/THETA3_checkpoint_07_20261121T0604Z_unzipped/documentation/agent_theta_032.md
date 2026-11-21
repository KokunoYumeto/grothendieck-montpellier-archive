# THETA3: 032 and its character-theoretic companion

Author/checker: `/root/theta_032`, GPT-6 Astra Pro, inherited effort (the exact effort label is not exposed to this agent). Run THETA3, 2026-11-21. This note is research documentation for the parent, not a claim that the full requested bridge is proved.

## 1. Sources actually read

- 032, *The rational Hodge conjecture for CM abelian varieties*: introduction §§1.2–1.3; §§4–6 in full; Corollary 3.2; the cited bibliography. Printed pages 3–4, 12–45, 51–53. Text extracted from the attached PDF. In particular, the distinction between a bar over the last two forms and no bar matters: the mixed period is of type (2,2), not a product of four (1,0)-forms on a surface.
- van Hoften–Sempliner (vHS), *The Hodge Conjecture for CM abelian varieties*, attached Hexagon 2610.00259v2: §§3.1–4.2 in full, printed pages 9–22, with the introduction's explanation of the method.
- Bridge sketch, Route 1, especially proposed statement 1.7, read in the parent context.
- Author-hosted BMM manuscript inspected through web: https://www.math.umd.edu/~millson/papers/BMM_Unitaire_Revision.pdf, retrieved 2026-11-21. It is a 97-page manuscript whose §5 proposition numbering differs from the vHS-cited version. It is NOT silently substituted for arXiv:1306.1515v2. Main note below relies on vHS's attached restatements; the author manuscript is used only to locate the standard Schrödinger and doubling architecture. Web retrieval refs: `turn261496126view0`, `turn800650799view0`, `turn800650799view1`, `turn800650799view2`. Parent must open/search a ref itself before citing it in chat.

## 2. Exact dictionary: the 032 construction

| Datum | Exact source and meaning |
|---|---|
| Fields | 032 §4.1, p.13: E is Galois CM, F=E^+, [F:Q]≥2; c is conjugation; Σ representatives of Gal(E/Q)/<c>; distinguished embedding μ=1. |
| CM signs | d_i(τ)=v_i(τ^{-1}); each v_i is odd and v_i(1)=1; d_1+d_2=d_3+d_4. |
| Target group | V/E Hermitian of dimension 3, signature (2,1) at μ and (3,0) elsewhere; G=SU(V) over F. D is the negative-line complex two-ball. V is anisotropic over F because a rational isotropic vector would survive at a definite real place. |
| Auxiliary space | P is an E/F-Hermitian multiplicity space of dimension 1 or 2; the actual dual pair uses skew-Hermitian δP, c(δ)=−δ. Symplectic form is Tr_{E/F}(δ h_V h_P), 032 (4.4). |
| Line signatures | If τ(δ)=it_τ, the Hermitian coefficient of W_i has sign −d_i(τ)sgn(t_τ), also at μ where d_i(μ)=1. Thus the auxiliary rank-two W can be indefinite at a compact *V*-place. |
| Active filtration | For a multiplicity line W_i, (F_i)_μ=L⊗(W_i)_μ and (F_i)_{cμ}=Q^*⊗(W_i)_μ^*, with Q=V_μ/L. Q^* is the holomorphic annihilator of L. |
| Compact filtration | At τ≠μ, select the whole cτ summand for d_i(τ)=1 and the whole τ summand for d_i(τ)=−1. |
| Half determinant | Lemma 4.1, (4.6): det F_P=L^{2n}⊗C_P and its square root L^n⊗C_P^{1/2}; C_P is constant and trivial for SU(V), not necessarily U(V). |
| Theta vector | 032 (4.9) is the rational theta sum with finite Schwartz input φ; (4.10) is its completed Taylor expansion. The first Taylor coefficient T_1 is the ordinary holomorphic gradient. |
| Splitting characters | §4.4 pp.19–21 chooses χ_H,χ_K restricting to ε_{E/F}^{dim H}, ε_{E/F}^{dim K}. They define the circle-extension unitary splittings. Lemma 4.4 makes their determinant twists disappear on SU(V). They are NOT the explicitly identified source characters of a global theta lift in this paper. |
| Differential kernel | Θ_i(φ) is the cμ projection of T_1, landing in Ω_D^1. For W=W_1⊥W_2, Ξ_W(φ) is the double-alternating projection of T_2, landing in K_D, 032 (4.7)–(4.8). |
| Nonvanishing | Proposition 4.5: Gaussian isolation of a lattice vector makes values span each cotangent fiber. Proposition 4.6: a product input gives nonzero wedge. Corollary 4.7: compact-place continuity preserves a nonzero pairing after changing rational line decomposition. |
| What varies | 032 Proposition 4.6(iii), pp.22–24: rational W, symplectic space, rational G embedding, finite action, total finite φ, principal quotient X, active total filtration all remain fixed. Signed subspaces W_τ^+,W_τ^- at τ≠μ vary. The signature of V does NOT change. |
| What changes later | Only after rational endpoints are chosen does one change rational Schrödinger coordinates, factor into finite sums of simple tensors, and pass to a common cover. Thus there is no assertion that the *individual line inputs* or their stabilizers stay fixed. |
| Arithmetic geometry | Theorem 5.1 and Corollary 6.7: every finite family of Θ_i classes lies in spans of rational Hodge maps U(v_i)→H^1(S,Q) on a common projective principal cover. These maps are induced up to rational multiple by maps to CM abelian varieties. |
| Integral Frobenius relation | Proposition 5.5, (5.9), p.32: Φ^3−D_1Φ^2+qD_2Φ−q^3D_3=0 in End(Ã_S). This is a q-power Frobenius endomorphism, not a reciprocal Frobenius convention. |
| Spectral parameter | Lemma 6.2, pp.37–38: D_q^M=ω on theta classes, ω²=ζ∏τ(r)^{−3d(τ)}, rr̄=1, val_w(r)=M, val_w̄(r)=−M. Proposition 6.3, pp.39–40: projective half-modulus Satake parameter {q^{1/2},q^{−1/2},e}, e=e_0^{−1}, e_0^M=ω, and ν_ι(σe)=−(3/2)v(σ|_E). |
| Hodge extraction | Proposition 6.6, pp.43–44: t_η=1/2−(1/3)ν_ι(e′) is 0 or 1; weak admissibility plus *filtration-preserving* Hecke projectors gives pure Hodge type. §6.3 uses all scalar conjugates to descend to rational CM Hodge maps. |

The distinction between global Hecke characters and characters of a finite-dimensional spherical Hecke algebra is essential: 032's §6 "Hecke characters" are the latter. The literal identification of a particular global character and its local test vectors is supplied by the companion, not stated in 032 §§4–6.

## 3. Exact dictionary: the vHS companion

Here G=U(V), H=Res_{F/Q}G, V still has (2,1) at one real place and (3,0) elsewhere. The Shimura surface can have several components; it is smooth projective at sufficiently small level (vHS §3.1.1–3.1.2, p.9).

1. A conjugate-symplectic automorphic Hecke character μ has μ|_{A_F^×}=ε_{E/F}. It has weight one when μ_τ(z)=|z|/z for τ in its CM type Φ_μ; vHS §3.1.3, p.9 (Liu21 Definitions 4.1 and 4.3). Lemma 3.1.5 constructs such a μ for any CM type.
2. An admissible oscillator triple (μ,ε,χ) chooses skew-Hermitian line local invariants ε and an auxiliary character χ. Admissibility is represented by e∈E^× with e^c=−e and Im τ(e)<0 for τ∈Φ_μ; vHS §3.1.4 (Liu21 Definitions 4.11 and 4.12).
3. Proposition 3.1.7 (Liu21 Proposition 4.13) decomposes all H^1 of the tower into the representations ω(μ,ε,χ). Theorem 3.1.11 (Liu21 Theorem 4.18) identifies their multiplicity spaces with Hom(A_∞,A_μ), where A_μ is CM. This is stronger than merely saying that selected theta classes are CM.
4. The dual pair is U(V)×U(W_i), W_i a skew-Hermitian line. At the active place it has signature (0,1) for the (1,0) cohomological lift. The splitting pair is ν_i=(μ_i,ν_5). The second character ν_5 can be held fixed; changing it twists the source torus character π_i. See §4.1.1–4.1.7, pp.13–15.
5. The raw cohomological theta form Θ^{1,0}_{ψ,ν_i}(φ_i,t_i) uses the BMM cocycle at the active place and Gaussian vectors at the definite places. An integrated lift pairs it with f_i∈π_i on [U(W_i)]. All adelic quotients in vHS §4.1 are given probability measure.
6. For four CM types, §4.2 chooses μ_1,μ_2,μ_3 and μ_4=μ_1μ_2μ_3^{−1}. Thus μ_1μ_2=μ_3μ_4 globally, not only at infinity. The restriction condition and CM type of μ_4 follow from the balanced four-factor relation.
7. Lemma 4.2.1 produces a rational isometry Ψ:W_1⊥W_2≅W_3⊥W_4. Put W=W_1⊥W_2 and W^□=W⊥(−W), a split skew-Hermitian space of dimension 4. The doubled Weil representation is on S(V(A_E)^2), dual pair U(V)×U(W^□), splitting pair (1,ν_5); §4.2.3–4.2.4, pp.16–17.
8. Remark 4.2.5 is the exact cancellation: μ_1μ_2=μ_3μ_4 makes the diagonal U(V)-action simply Φ(x)↦Φ(g^{−1}x). Without this equality, the zero-orbit integral below acquires a character and can vanish.
9. The doubling intertwiner δ is a partial Fourier transform; §4.2.4 gives δ(φ_1⊗overline{φ_2})(0)=〈φ_1,φ_2〉. Proposition 4.2.6 gives its rational summation identity by Poisson summation. Equation in §4.2.8, p.20, identifies the cup period with C times

   I_{Φ_∞}(Φ_f)=∫_[U(V)] Σ_{x∈V(E)^2} Φ(g^{−1}x) dg,

   with C the explicitly specified quotient-volume conversion constant. This is a doubled theta integral. It is not yet an asserted Alpöge Bessel period or an Euler-product Rallis inner-product formula.
10. Lemma 4.2.9 uses real split-preserving isometries to make Φ_∞(0) a nonzero multiple of the Kudla–Millson top form. Compact-place factors are products of Gaussian L² norms. Rational isometries close to this one preserve nonvanishing by strong continuity. Lemma 4.2.7 then varies finite test data to obtain a nonzero I. This is a different permitted variation from 032's fixed finite total input.
11. Lemma 4.2.10 gives a *finite* Fourier expansion in automorphic characters of U(W_i). The fixed infinity type and fixed compact open finite stabilizer make the character support finite. Evaluation at identity is a finite sum of integrated lifts. The proof of Theorem 4.0.2 then selects a nonzero fourfold term; Proposition 4.1.8 assigns its CM source.

## 4. Finding THETA3-A1: a signature-independent zero-orbit pairing

This is a full elementary proof of a form of the doubling constant term that is useful here. It does not assert an identity of the unaveraged mixed period with Alpöge's Bessel period.

### Statement

Let E/F be CM, V an anisotropic nondegenerate Hermitian E-space, and r≥1. Let W^□ be the split skew-Hermitian space of E-dimension 2r, with complementary maximal isotropic subspaces W^Δ,W^∇. In the Schrödinger model attached to V⊗W^∇, choose coordinates identifying its Schwartz space with S(V(A_E)^r). Choose compatible unitary splittings such that the U(V)-action is the untwisted pullback

    (ω(g)Φ)(x)=Φ(g^{−1}x).

Let N_s be the Siegel unipotent radical of U(W^□). Identify N_s with the additive F-space Herm_r(E) so that its action is

    (ω(n(b))Φ)(x)=ψ(〈b,Q_V(x)〉)Φ(x),

where Q_V(x) is the Hermitian Gram matrix (h_V(x_i,x_j)) and 〈−,−〉 is the nondegenerate F-bilinear trace pairing. A conventional factor 1/2 can be absorbed into this identification; it does not change the zero character. Fix a nontrivial global additive character ψ of A_F/F and probability Haar measures on [U(V)] and [N_s]. Define

    T_Φ(h)=∫_[U(V)] Σ_{x∈V(E)^r}(ω(g,h)Φ)(x) dg.

Then

    ∫_[N_s] T_Φ(n) dn = Φ(0).                                      (A1.1)

In particular this averaged pairing is independent of the real signature of V, after the common normalization of Φ(0), for any anisotropic V of the given dimension. It applies to 032/vHS's V and to a totally definite V. The underlying theta functions, nonzero-orbit coefficients, and unaveraged periods need not agree.

### Proof

Anisotropy of the Hermitian space makes U(V) anisotropic over F, including its norm-one central torus, hence [U(V)] is compact. The quotient [N_s] is the additive compact quotient of the finite-dimensional F-vector space Herm_r(E). The theta series for a Schwartz function converges absolutely and locally uniformly on the product of the two quotients: at finite places its support restricts the rational points to a finite union of lattice cosets, and at infinity Schwartz decay dominates any polynomial growth in the lattice count. On compact sets of g the same decay bound is uniform. The N_s action only introduces unit-modulus factors. These observations justify interchanging summation and both integrals.

For rational x, the Gram matrix Q_V(x) belongs to Herm_r(E). Preservation of h_V gives Q_V(g^{−1}x)=Q_V(x) for adelic g∈U(V)(A_F). Thus

    ∫_[N_s]T_Φ(n)dn
      =∫_[U(V)] Σ_x Φ(g^{−1}x) [∫_[N_s]ψ(〈b,Q_V(x)〉)db] dg.

The bracketed integral equals 1 if Q_V(x)=0, and 0 otherwise. Indeed the character is trivial precisely for zero Gram matrix, by nondegeneracy of the trace pairing and nontriviality of ψ; a nontrivial character has zero integral by translating the probability Haar measure by an element on which that character is not 1. If Q_V(x)=0, each diagonal entry h_V(x_i,x_i) is zero. Since V is anisotropic over E/F, every x_i=0. Only x=0 survives. Pullback fixes zero, so the remaining integral is Φ(0) times vol[U(V)]=Φ(0). This proves (A1.1).

The last assertion follows by repeating the same proof for each anisotropic V. It compares the same scalar functional evaluation Φ↦Φ(0), not a canonical identification of distinct global Hermitian spaces or of their motives. ∎

### Check and caveats

Whole proof re-read by this agent on 2026-11-21. Checked: anisotropy, compactness, absolute convergence, moment-map invariance, additive character orthogonality, normalization, zero Gram⇒zero vector, and the limit of the conclusion. Pass. No Lean certificate was constructed. The Schrödinger unipotent formula is standard oscillator background; in the doubled setting it is also the concrete ingredient underlying vHS Lemma 4.2.7. If a nontrivial diagonal character survives, the conclusion becomes Φ(0)∫_[U(V)]χ(g)dg and can vanish. If V is isotropic, nonzero isotropic tuples survive and the stated formula must be replaced by a sum of zero-Gram orbits.

### Geometric interpretation

The period side on the ball surface is the intersection pairing of theta cohomology classes and, after the surface criterion, of algebraic correspondences to CM abelian varieties. Equation (A1.1) identifies a zero-orbit coefficient of their doubled theta expression. On a definite Shimura set the same proof gives a weighted finite-set pairing with the same averaged zero orbit. This is a precise common theta operation that survives signature change. It is not an algebraic correspondence between the ball surface and the definite Shimura set. To identify Alpöge's particular Bessel period with this coefficient one must specify its unipotent subgroup/character, the hermitian space, the rational embeddings, and the normalized local vectors; a general invocation of "seesaw" does not establish those data.

## 5. Finding THETA3-A2: quantitative finite-translate consequence

### Statement

In A1, write Φ=Φ_∞⊗Φ_f, assume a=Φ_∞(0)≠0 and Φ_f(0)=1, and keep Φ_∞ fixed. For every 0<ε<1 there exists h_f∈N_s(A_{F,f}) such that

    |I_{Φ_∞}(ω_f(h_f)Φ_f)| ≥ (1−ε)|a|,                            (A2.1)

where I_{Φ_∞}(Ψ_f)=T_{Φ_∞⊗Ψ_f}(1). Moreover the finite Schwartz L² norm is unchanged by the translation, because ω_f is unitary. No bound for the conductor, stabilizer level, or denominators of h_f is asserted.

### Proof

By A1, a=∫_[N_s]T_Φ(n)dn. Compactness and continuity imply there is n=(n_∞,n_f) with |T_Φ(n)|≥|a|. Weak approximation for the additive F-vector space N_s gives γ_j∈N_s(F) with (γ_j)_∞→n_∞. By continuity,

    T_Φ((γ_j)_∞,n_f) → T_Φ(n_∞,n_f).

Automorphy on the left by γ_j gives

    T_Φ((γ_j)_∞,n_f)=T_Φ(1,(γ_j)_f^{−1}n_f).

Choose j so that the absolute difference from T_Φ(n) is at most ε|a|, and put h_f=(γ_j)_f^{−1}n_f. The triangle inequality proves (A2.1). Commutativity of the U(V) and U(W^□) actions identifies the right side with the finite-translated input, and unitarity proves equality of L² norms. ∎

### Independent check of the parent's earlier full-flag version

Before proving A1, this agent independently checked the parent's proof using the full-flag N and vHS Lemma 4.2.7. It passes for the same reason: compact [N], probability averaging, real weak approximation, left automorphy, and finite Weil unitarity. The Siegel version above makes N additive and gives a direct proof of the needed constant term. Both versions change finite theta data and should not be presented as preserving 032's fixed finite input. The total doubled input does retain its old U(V) compact stabilizer, by commutation of the dual-pair actions (as clarified in the later Q7 check); decomposition into individual factors can require a smaller common level.

## 6. Finding THETA3-A3: the precise loss in extracting actual character lifts

### Statement

Suppose a finite tensor decomposition after inverse doubling gives

    δ_f^{−1}(Ψ_f)=Σ_{a=1}^R c_a φ_{1,a}⊗φ_{2,a}⊗overline{φ_{3,a}}⊗overline{φ_{4,a}},

and let the raw theta form associated to φ_{i,a} have a finite torus-character expansion with N_{i,a} nonzero terms (vHS Lemma 4.2.10). Let P be the corresponding fourfold mixed period, with the same geometric normalization throughout. Then at least one quadruple of actual integrated character lifts in these expansions has mixed period P_{a,χ_1,χ_2,χ_3,χ_4} satisfying

    |P_{a,χ_1,χ_2,χ_3,χ_4}|
       ≥ |P| / [Σ_{a=1}^R |c_a| Π_{i=1}^4 N_{i,a}].               (A3.1)

Terms with c_a=0 may be omitted. The denominator is finite and positive when P≠0. If the geometric identity is P=C I_{Φ_∞}(Ψ_f), combine A2 and A3 to obtain lower bound (1−ε)|C a| divided by the displayed finite decomposition cost.

### Proof

Expand each of the four raw forms into its finite sum, wedge them with conjugation on the last two, and integrate. Multilinearity gives P as a sum of the selected integrated periods, with coefficient c_a for each character quadruple associated to a. Let M be the maximum of their absolute values. The triangle inequality gives |P|≤M Σ_a|c_a|Π_iN_{i,a}. Rearranging proves the assertion. All sums are finite, so no convergence exchange is involved. ∎

The denominator is a cost of actual chosen finite data. Positivity and A2 do not themselves bound it in terms of conductor, discriminant, or dimension. The decomposition into CM Hodge maps introduces another finite coefficient cost if one insists on selecting a single rational correspondence; that cost must also be retained instead of implicitly setting it to one.

## 7. Honest same-signature seesaw identity (background form)

For W=W_1⊥W_2, the oscillator space for V⊗W is the tensor product of the oscillator spaces for V⊗W_i. Compatible splittings give the see-saw of the commuting groups U(V)×U(V) against U(W_1)×U(W_2), and diagonal U(V) against U(W). Its elementary content is

    θ_W(g,h_1,h_2;φ_1⊗φ_2)
      =θ_{W_1}(g,h_1;φ_1) θ_{W_2}(g,h_2;φ_2).

For differential kernels, the double-alternating projection is the wedge (032 Proposition 4.6, (4.17)). Integrating the product against characters of the two norm-one tori and a test function/form on [U(V)] gives the usual seesaw equality by Fubini. Compactness ensures convergence. A second decomposition W_3⊥W_4 gives a second pair of tori in the SAME U(W), not a global definite U(V) automatically. Doubling W with −W yields the common kernel used in A1. This explains exactly what can be proved without a hidden matching theorem.

## 8. Status of sketch 1.7

- Proven structural refinement: common oscillator representation, direct-sum product operation, character-cancelled doubled theta integral, and signature-independent averaged zero orbit A1; quantitative input selection A2.
- Source-supported positive local comparison: vHS §4.2.4 and Lemma 4.2.9 express the archimedean zero evaluation as an oscillator inner product and use positive Gaussian norms at compact places.
- Undecided literal statement: equality of the 032/vHS mixed period with Alpöge step 12's particular Bessel period after a change of global signature. It is not refuted merely because the attached 032 paper does not state it. It requires an actual local and global matching map, including coherence of the hermitian spaces, source representations, splittings, test vectors, and measures.
- False stronger reading to avoid: "moving compact-place data in 032 changes V from signature (2,1) to totally definite while keeping every finite datum fixed." Proposition 4.6 holds V fixed; the moved subspaces lie in W. This is a source-level correction, not a counterexample to every possible inner-form comparison.

No Grothendieck manuscript scan was supplied to this agent. No transcription correction is inferred from a source not read. Exact cote/scan claims require the parent's archival work; the motivic statements above live at the level of homological correspondences and Hodge realizations, and do not by themselves construct a new motivated or algebraic transfer between the two signatures.

Later source updates and the positive finite-frame comparison are recorded in `work/paper_A.tex`; the earlier statement above is not a claim of permanent source unavailability. The parent and other agents have subsequently retrieved primary archival scans and a pinned secondary Lean mirror.

## 9. Independent checks of the parent's quantitative formulations

Read `work/root_quantitative.md` in full and independently reconstructed the proofs of Q1–Q3,Q5–Q6. All pass, with the following exact observations.

- Q1: reverse triangle/Cauchy–Schwarz yields (1−η)A; pullback to degree-d finite cover multiplies period and norm square by d; coefficient sum is (Σ|a_r|)(Σ|b_s|).
- Q2: max_{r≥0} r exp(−πλr²/2)=1/√(πeλ), so the prefactor 2√(π/(eλ)) is correct. The inequality r≥k||m||/2 gives b=πλk²ρ²/8. The ball-packing count (2j+3)^d is an overestimate and hence valid without covolume data. Successive ratios decrease with j; the displayed geometric tail bound is valid. The projected wedge-error estimate is correct.
- Q3: coordinate rounding in an integral Q-basis gives the stated denominator bound. For P(w)=ww*H/(w*Hw), numerator/denominator differences are bounded by h(2U+1)ε when ε≤1; division gives exactly 2h(2U+1)/η·(1+hU²/η)ε. Orthogonal complements have projector I−P and the same error.
- Q5: the weighted triangle inequality is correct. For a computable bound, N_{i,a} should denote the cardinal of the permissible character set (or an upper bound from the finite class quotient), not require deciding which Fourier coefficients are exactly nonzero. Including zero terms causes no problem and only weakens the lower bound.
- Q6: expanding the determinant polynomial and using E[z_i overline{z_j}]=δ_ij proves the asserted Gram determinant norm. The parent supplied the published BMM PDF at `work/external/BMM_published2016.pdf`; I read Proposition 5.17 on printed p.48 and Proposition 5.19 on p.49. Proposition 5.19(1) directly gives the determinant Δ_b^q, specializing to the claimed 2×2 determinant for p=b=2,q=1. This establishes the polynomial shape. The Bargmann/Schrödinger transfer is unitary only after explicitly chosen measures; Q6 correctly treats a_0=1 as a chosen normalization and retains the unnormalized a_0 of vHS when conventions are not fixed.

These are independent re-proofs/checks of the mathematical arguments, not formal verification. Corresponding events are appended to `agent_theta_032_CHECK_EVENTS.tsv`.

## 10. Primary Liu dictionary and the higher-ball obstruction

The parent supplied Liu, *Fourier–Jacobi cycles and arithmetic relative trace formula (with an appendix by Chao Li)*, locally as `work/external/Liu_FJ2021.pdf` and `.txt`. I read Definition 4.11–Proposition 4.13 (printed pp.46–49), Theorem 4.18 and its proof opening (pp.52–53), Appendix B.2 (pp.96–97), and Appendix D.1 (pp.125–128). Exact additions:

- Liu's metaplectic cover in B.2 has center C¹: this is the circle extension, consistent with 032's careful distinction. With Hermitian V of rank n and skew-Hermitian W of rank m, his splitting convention is μ_V|A_F^×=ε_{E/F}^m and μ_W|A_F^×=ε_{E/F}^n. The labels index the *acting unitary group*, not the dimension exponent. This must be reconciled when using other authors' opposite labeling conventions.
- Definition 4.11's auxiliary χ is a character of E¹\(A_{E,f})¹. In D.1 it selects the *central character* of the U(V) oscillator quotient ω(μ,ε,χ). It is distinct from μ, and its relationship with the source U(1) character depends on the second splitting character.
- In Lemma D.1's split-place proof, p.126, write E_v=F_v×F_v, μ=ν⊠ν^{-1}, and identify U(V)=GL_n(F_v). Then ω(μ,ε,χ) is normalized parabolic induction from GL_{n−1}×GL_1 of

      (ν∘det) ⊠ χν^{1−n}.

  For n=3 its Satake tuple is

      {ν(π)q^{1/2}, ν(π)q^{-1/2}, χ(π)ν(π)^{-2}},

  hence projectively {q^{1/2},q^{-1/2},χ(π)ν(π)^{-3}}. This gives an explicit character-theoretic explanation of the shape in 032 Proposition 6.3. If passing between the direct oscillator Hecke action and 032's geometric pullback, apply the reciprocal operation proved in 032 Lemma 6.1; do not silently identify the two orientations.
- Lemma D.2, p.127: at infinity μ_m(z)=arg(z)^m with m odd, ε=±i and central χ_l(z)=z^l. For rank n≥3, the holomorphic H¹ representation of U(n−1,1) is ω^{−1,−,0}_{n−1,1}; the antiholomorphic one is ω^{1,+,0}_{n−1,1}. At a definite U(n,0), only ω^{1,+,0}_{n,0} and ω^{−1,−,0}_{n,0} are trivial. These are the exact local signs behind the CM type.
- Proposition 4.13 applies to *every rank n≥3*, not just n=3. The proof's last paragraph on p.49 invokes Rallis' inner-product formula to put Θ^V_{(μ,ν),W}(π_W) in L²_disc(G), and footnote 8 states this rank-one-to-rank-n lift is always in Weil's convergent range. This is the precise occurrence of the Rallis formula underlying vHS Proposition 3.1.7, though no normalized Euler-product formula is printed there.
- Together Proposition 4.13 and Theorem 4.18 show that all finite-level Albanese varieties in this standard ball tower are of CM type up to isogeny for every complex ball dimension n−1≥2. Therefore increasing the ball dimension while keeping trivial coefficients and degree-one sources does not introduce simple non-CM abelian sources. The rank-two unitary (curve) case is different: Appendix D.3, Definition D.3, separates stable and endoscopic cohomological finite representations. This identifies a concrete next setting for a non-CM source rather than leaving the same obstruction unaddressed.

The split Satake calculation above is an elementary consequence of Liu's stated normalized induction: a GL_{n−1} determinant character ν has Satake parameters ν(π)q^{(n−2)/2},…,ν(π)q^{−(n−2)/2}; induction adjoins χ(π)ν(π)^{1−n}. Dividing by ν(π) gives the displayed rank-three tuple. The calculation was re-read and checked, but no claim is made that all global finite test vectors in 032 have now been spectrally normalized.

## 11. Independent checks of the definite-side B1 and B2

Read the whole proofs in `work/agent_definite_bridge.md` and independently checked:

- B1: the local determinant norm sign at a real place is (−1)^{negative index}. Changing 1 to 3 preserves that sign, while changing 1 to 0 reverses it. The former leaves the global product condition intact and the latter needs one compensating finite nonsplit place. Under the cited Landherr classification, the existence/nonexistence assertions follow. This is about Hermitian spaces, not merely their abstract unitary groups; odd-dimensional scalar rescaling can identify the latter without identifying oscillator embeddings.
- B2: for a k-dimensional multiplicity space, active scalar r acts by r on a k-dimensional summand and r^{−1} on a 2k-dimensional summand. Hence detF has r^{−k}; writing r=t², its square root has t^{−k}. The projected degree-k term contributes t^{−2k}, giving t^{−3k}. Negative-definite V with the original P sign puts the full 3k-dimensional nonconjugate summand in F, giving t^{3k+2j} on degree j. Positive-definite V puts the full conjugate summand in F and its vacuum has t^{−3k}. These calculations pass in the **covariant Taylor target** convention of 032 (4.12).

One necessary language correction: 032 (4.13) says the actual infinite Schrödinger Gaussian/Taylor coefficient vectors transform as j^{−1}Sym(J^{−1}), while the global Taylor tensor target in (4.12) transforms as j Sym(J). Thus the displayed target model is dual to that local oscillator convention. Taking reciprocal characters on **both** sides preserves the absence and the positive-definite vacuum matching. A common honest scalar twist also preserves absence. Merely naming the same splitting characters is not itself a proof that the bare-to-circle correction is the same for two different embeddings; that correction must be included in an actual transfer. These qualifications leave the scoped B2 statement valid and prevent interpreting it as a universal packet nonexistence theorem.


## 12. Applicable convergent-range Rallis formula

A direct primary source is Jaeho Haan, *The Bessel period of U(3) and U(2) involving a non-tempered representation*, arXiv:1403.5061v7, §3.3, Theorem3.4, printed p.8. Exact source downloaded to `work/external/Haan_BesselU3U2_2014.pdf` and `.txt`; printed p.8 was visually verified in `Haan_Theorem3_4.png`. Its proof cites J.-S. Li1992 Theorem2.1, not an inapplicable second-term-range theorem.

The source takes Hermitian source rank1, skew-Hermitian target rank3, symplectic form (1/2)Tr of the tensor product, additive character psi, and unitary gamma with gamma|A_F^*=epsilon. Its splitting pair is (gamma,gamma^3). Both global measures are Tamagawa, local measures and pairings factor their global counterparts. Section3.2 defines the partial Fourier/doubling section rho_1,3 with rho(phi tensor barphi)(0)=||phi||². At s=1 Theorem3.4 gives the norm of theta(barf,phi) as L_E(3/2,BC(tau)gamma^3)/L_F(3,epsilon) times the product of normalized local doubling integrals. The normalizer is L_v(3,epsilon)/L_Ev(3/2,BC(tauv)gamma_v^3), and unramified normalized factors equal1. The full cross formula, precise section and local integral are transcribed in the first subsection of `work/paper_A.tex`.

Keep Haan's tau/bar-input, pairing, and base-change conventions when quoting. To pass to another splitting, first establish omega'=lambda(g)kappa(t)omega. The corresponding input change is then explicitly tau→tau kappa^{-1}; a unitary target twist does not affect the norm. Source versus target labels, additive-character scaling, probability versus Tamagawa measures, and U versus SU components are separate matching data. Haan's main U3/U2 Bessel theorem is specialized and is not being applied to an arbitrary wedge of two theta lifts.

## 13. A4 and A5: complete proofs saved in paper_A.tex

**A4** extends the analytic one-active-ball construction to Hermitian rank m≥3. The active determinant formula is det(F_P)=L^{2k}(det V)^{-k}(det P)^{2−m}. Thus the first projected tensor still gives Omega1 and the double-alternating second gives Omega2; the latter is canonical only for m=3. The Gaussian isolation, finite-input selection, direct-sum product, and fixed-data compact continuity arguments extend with the position dimension changed to m. Pair with an ample Kähler class to degree m−3. At rational endpoints the forms are holomorphic and closed, and a smooth complete-intersection surface multiplies the mixed pairing by the product of its defining degrees. The proof does not silently extend 032's rank-three arithmetic extraction; Liu's all-rank CM Albanese result is a separate cited input. Raising the rank does not turn one-active-ball signatures into every-place signatures or a totally definite iterated chain.

**A5** provides a separate, exact global comparison to definite U2 periods. For a finite-dimensional fixed-level scalar K-infinity-type theta space E on adelic U(V), choose a global negative line Ez and H=U(z-perp), which is totally definite. For finite a set R_a f(h)=f(ha). Its level is K_H(a)=H(A_f) intersect aK_fa^{-1}; fixed infinity type makes the restriction space finite, with the ordinary reciprocal-stabilizer mass norm. The Cayley parametrization proves the needed U(V)(F) real weak approximation. It shows that the family R_a separates E. A greedy kernel argument needs at most dim(E) translates. Therefore Q=sum R_a^*R_a is positive definite and

    <u,v>_G = sum_a <R_a Q^{-1}u, R_a v>_H.

Finite orthonormal expansion on H expresses this as an exact finite sum of products of global U3/U2 Bessel periods. The original uncorrected periods satisfy the lower and upper eigenvalue bounds of Q. In coordinates Q=G_ball^{-1} sum_a R_a^* Mass_a R_a. The correction is analytic; rationality or algebraicity of Q is not a consequence of finite dimensionality. Evaluation of canonical forms at CM points is not cohomological restriction to a zero-dimensional variety.

I read A4 and A5 from hypotheses to conclusions after drafting. The independent noncm_integral agent also read the whole A5 proof and the actual complete-intersection portion of A4 and reported a pass, including the Gram formula, conjugate-linear-first convention, and conditional minor bound. That agent records its own events. A standalone LaTeX compilation attempt was blocked before reading the source because the installed pdflatex has no format file; no compilation success is claimed.
