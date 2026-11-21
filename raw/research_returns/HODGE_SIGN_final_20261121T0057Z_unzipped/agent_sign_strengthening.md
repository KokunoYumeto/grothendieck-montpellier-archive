# SG-08–SG-10: the effective Gysin remainder and the affine-to-projective proof

2026-11-21. Independent reconstruction/check by /root/sign_geometry, GPT-6 Astra Pro, effort not exposed. This note developed after agent_sign_geometry.md. It supersedes any earlier statement that the geometric sparse-family gate was merely untried. Root proposed the sparse embedding and Noether-normalization route; this agent supplied and checked the cancellation strengthening removing compact middle-concentration, and checked the complete affine-to-projective argument below.

The key input is *generic weak Lefschetz*, not smoothness alone. Katz, **Affine Cohomological Transforms, Perversity, and Monodromy**, JAMS6(1) (1993),149–222, Theorem3.4 and Corollary3.4.1, pp180–181, prove that, for a quasi-finite map π:V→A^N and any fixed f:V→A¹, generic hypersurfaces f+Aπ+b=0 have the required restriction maps. The Appendix, A.5, pp220–221, gives Deligne's direct proof using Artin vanishing and generic base change. That proof does not use Weil I/II or a weight theorem. The source PDF and extracted text were read locally at reference_cache/Katz_ACT.pdf and .txt, especially §§3.3–3.4 and Appendix A.1–A.5. Relevant foundational locators are BBD4.1.1–4.1.3,4.2.8; SGA4 XIV3.1 and XVII5.4.3; SGA4½, Théorèmes de finitude1.9. BBD affine exactness was additionally verified in the original primary PDF search results: https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf (Cor4.1.3, p103; generic exposed screenshot did not have extractable text).

## SG-08 — Effective remainder without base middle concentration

### Smooth affine form

Let U/F_q be smooth affine and purely of dimension d≥1, and let ℱ be a lisse Q_l-bar sheaf on U. Let k≥2, put D=kd and Z=U^k, and let ℱ_k=ℱ^{⊠k}. Let i:Y→Z be a smooth affine hypersurface, defined over some finite extension of F_q if necessary, such that restriction

    H^a(Zbar,ℱ_k^∨) → H^a(Ybar,ℱ_k^∨)

is an isomorphism for a<D−1 and injective for a=D−1. (The same condition for the dual, obtained by Katz generic weak Lefschetz, is all that the following argument needs.) Define

    M_n = Σ_{u∈U(F_{q^n})} Tr(F_{u,n},ℱ_u),
    N_{k,n} = Σ_{y∈Y(F_{q^n})} Tr(F_{y,n},(ℱ_k)_y),
    R_{k,n}=q^n N_{k,n}−M_n^k.

Here F_{u,n} and F_{y,n} denote local geometric Frobenius over F_{q^n}. Let V=H_c^d(Ubar,ℱ). Then there exists an actual finite-dimensional Frobenius module K_k such that, for all n,

    (−1)^{D−1}R_{k,n} = Tr(F^n,V^{⊗k})+Tr(F^n,K_k).

Thus, after one sign, the virtual Frobenius remainder is effective and contains V^{⊗k}; no assumption that the entire H_c(U,ℱ) is concentrated in degree d is necessary.

**Proof.** Artin vanishing and Poincaré duality give H_c^a(U,ℱ)=0 for a<d and H_c^a(Y,ℱ_k|Y)=0 for a<D−1. The stated restriction maps, dualized by Poincaré duality on the smooth schemes Z,Y, give natural Frobenius-equivariant Gysin maps

    H_c^j(Y,ℱ_k|Y)(−1) → H_c^{j+2}(Z,ℱ_k)

that are isomorphisms for j>D−1 and surjective for j=D−1. Write T_b=H_c^{D+b}(Z,ℱ_k), W_a=H_c^{D−1+a}(Y,ℱ_k|Y), with a,b≥0. A Tate twist (−1) multiplies Frobenius eigenvalues by q. Therefore

    (−1)^{D−1}R_{k,n}
      = Σ_{a≥0}(−1)^a Tr(F^n,W_a(−1))
        +Σ_{b≥0}(−1)^b Tr(F^n,T_b).

For a≥1 the Gysin isomorphism identifies W_a(−1) with T_{a+1}; the corresponding terms have opposite signs and cancel. The surviving virtual class is

    [W_0(−1)]+[T_0]−[T_1].

Define K_k=ker(W_0(−1)→T_1); the map is surjective, so this class is [K_k]+[T_0]. By Künneth, each factor in total degree D is in its smallest possible degree d, so T_0=V^{⊗k}. This proves the identity. All exactness statements hold as Frobenius modules, not just as vector-space dimension equalities. ∎

### Perverse form

The identical calculation works for a perverse sheaf P on an affine X, after choosing a generic non-characteristic hyperplane section of X^k in an affine embedding. Let t_n(x)=Tr(Frob,P_x), M_n=Σt_n and N_n=Σ_{Y}∏t_n. Put P_Y=i^*(P^{⊠k})[−1]. Artin gives H_c^j(X,P)=0 and H_c^j(Y,P_Y)=0 for j<0. Generic weak Lefschetz and the non-characteristic identification give Gysin maps

    H_c^r(Y,P_Y)(−1)→H_c^{r+1}(X^k,P^{⊠k})

isomorphic for r>0 and surjective for r=0. Because i^*P^{⊠k}=P_Y[1], the trace of its stalks on Y is minus that of P_Y. Consequently **−R**, rather than a dimension-dependent sign, is the trace of

    H_c^0(X,P)^{⊗k} ⊕ ker(H_c^0(Y,P_Y)(−1)→H_c^1(X^k,P^{⊠k})).

When P=ℱ[d], converting the trace function back to that of ℱ restores the sign (−1)^{kd−1} above. No positivity of an intersection form enters either version.

## SG-09 — Fourier-compatible generic sections and the middle affine bound

**Statement.** Let U/F_q be smooth affine, purely of dimension d≥1, and ℱ a lisse sheaf such that for some fixed embedding into C and constants C,w,

    |Tr(Frob_{x,n},ℱ_x)|≤ C q^{nw/2}

at every x∈U(F_{q^n}), for every n≥1. Then every eigenvalue of Frobenius on H_c^d(Ubar,ℱ) has absolute value at most q^{(w+d)/2}. The same conclusion holds for all embeddings if the trace bounds do. The statement is proved with geometric hypotheses precise enough for the note's sign-only mechanism, and does not presuppose purity of any cohomology group.

**Proof.** Choose a finite Noether normalization π:U→A^d. Since O(U) is a finite module over F_q[x_1,…,x_d], choose B module generators. Every geometric fibre has length at most B, and hence at most B rational points over every finite extension. This avoids a needless assertion that π is étale or that its fibre cardinality is its degree. Choose affine coordinate generators z_1,…,z_s of U, giving a closed immersion U→A^s.

For each k≥2 fix the path function

    f(u_1,…,u_k)=Σ_{i=1}^{k−1} b(π(u_i),π(u_{i+1})),

where b is any fixed nondegenerate bilinear form on A^d. For each vertex i let g_i be a variable linear combination of its z_j, and let c vary. The hypersurface is

    Y: f+Σ_i g_i+c=0.

The map Z=U^k→A^{sk} given by all vertex coordinates is a closed immersion, hence quasi-finite. Katz Cor3.4.1, applied to the fixed f and this map, gives a dense open set of coefficients for which ordinary weak Lefschetz holds for ℱ_k^∨. Smoothness also holds on a dense open: use the graph closed immersion Z→A^{sk+1}, z↦(z,f(z)); its generic hyperplanes, restricted to the open parameter chart where the coefficient of f is nonzero, can be uniquely rescaled to the displayed family. Bertini for this genuine immersion gives smoothness. The two dense opens meet. Choose coefficients in their intersection over a finite extension F_{q^{e_k}}; a nonempty open over an algebraic closure has a point over some finite extension. The coefficient choice remains fixed while one subsequently runs through *all* further finite extensions. The degree e_k may depend on k.

For h≠0 and x∈A^d(F_{q^n}), define the vertex weight

    a_{i,h,n}(x)=Σ_{u:π(u)=x}Tr(Frob_{u,n},ℱ_u) ψ_n(h g_i(u)).

It satisfies |a_{i,h,n}(x)|≤BC q^{nw/2}. Orthogonality of additive characters gives q^nN=M_n^k+R; the h=0 mode is M_n^k, independent of all g_i. For every nonzero h the remaining sum is a path product of the Fourier matrices K_h(x,y)=ψ_n(hb(x,y)), with internal multiplications by a_{i,h,n}. Each Fourier matrix has operator norm q^{nd/2} on counting-measure l², each internal multiplier has norm at most BC q^{nw/2}, and each endpoint vector has norm at most BC q^{n(w+d)/2}. There are k−1 Fourier matrices, k−2 internal multipliers and two endpoints. Therefore

    |R_{k,n}|≤(BC)^k q^{n[k(w+d)/2+d/2+1]}.

This argument allows different vertex weights and their dependence on h; neither affects the norm estimate. For the chosen extension F_{q^{e_k}}, the same formula has q replaced by q^{e_k} and n ranging over all positive integers.

Apply SG-08. The signed R is an effective finite power sum containing α^{e_k k} for every eigenvalue α of Frobenius on V=H_c^d(U,ℱ). Distinct roots cannot cancel in such a power sum. Its generating rational function has a nonzero pole at the reciprocal of each distinct root, so the all-n bound forces

    |α|^{e_k k}≤q^{e_k[k(w+d)/2+d/2+1]}.

Taking the e_k k-th root gives |α|≤q^{(w+d)/2+(d/2+1)/k}. Let k tend to infinity. No uniformity in e_k or in Betti numbers of Y is needed, because n is sent to infinity first for each fixed k. ∎

**Exact input scope.** Lissity gives smooth-scheme Poincaré duality with the dual coefficient sheaf, and ℱ[d] perverse. Pointwise *trace* control suffices for this fixed embedding; assuming pointwise purity of weight w is one way to obtain the control with C=rankℱ. No conjecture about algebraic cycles or a real polarization is used.

## SG-10 — From the affine bound to Weil I, and the lisse coefficient version

**Statement.** SG-09, together with generic weak Lefschetz and Poincaré duality, gives the finite-field absolute-value assertion of Weil I for every smooth projective X. More generally it gives |α|=q^{(w+i)/2} on H^i(Xbar,ℱ) when ℱ is a pointwise pure lisse sheaf of weight w, with its dual pointwise pure of weight −w. No Hodge standard conjecture is used. This is a reconstructed proof of a known theorem, not a newly claimed discovery of Weil's result.

**Proof for the absolute values.** Induct on d=dimX. After a finite extension, handle geometric connected components separately; roots of unity from descent do not change absolute values. In dimension0 the assertion follows directly from pointwise purity (constant coefficients give a permutation representation). In positive dimension choose a smooth hyperplane section H, passing to a finite extension if necessary, and put U=X\H, which is smooth affine of dimension d.

For i<d, weak Lefschetz identifies H^i(X,ℱ) with H^i(H,ℱ|H) for i<d−1 and injects it for i=d−1. The induction hypothesis therefore gives the required modulus in all lower degrees. In middle degree use localization

    H_c^d(U,ℱ)→H^d(X,ℱ)→H^d(H,ℱ|H).

SG-09 bounds the left term by q^{(w+d)/2}; the induction hypothesis bounds the right term by the same value (and it is zero when d=1). Every eigenvalue of the middle term occurs in the left or right term as a subquotient, so it has this upper bound.

Apply the same upper-bound argument to ℱ^∨, whose pointwise weight is −w. Poincaré duality gives a perfect pairing

    H^d(X,ℱ)⊗H^d(X,ℱ^∨)→Q_l(−d).

Thus q^d/α occurs for the dual coefficient sheaf, and its bound q^{(−w+d)/2} gives |α|≥q^{(w+d)/2}. The middle degree is pure. For i>d, pair H^i(X,ℱ) with H^{2d−i}(X,ℱ^∨), whose purity is already known in a lower degree, obtaining |α|=q^{(w+i)/2}. Purity after a finite extension descends because |α^{e}|=(q^{e})^{(w+i)/2} forces the original modulus. ∎

For constant coefficients this is exactly the missing absolute-value assertion. Integrality of characteristic polynomials, independence of l, and rationality should be attached using the established Grothendieck rationality/trace formalism and Deligne Weil I's argument (1.7)⇒(1.6); they are not being silently supplied by the complex pole lemma. If the root package presents only the absolute-value theorem, it should say so. The proof works for every embedding since point counts/constant-sheaf traces are embedding independent. For general pure lisse coefficients one explicitly assumes pointwise bounds under the embeddings being claimed.

**Check record.** All Gysin degree shifts and twists, the cancellation at b≥2, the surjective border map, the unique lowest Künneth degree, the module-generator fibre bound, generic coefficients over finite extensions, Fourier endpoint exponents, and the projective localization/duality step have been reconstructed independently and read in full. The remaining proofreading task is to align these labels with the parent's final theorem numbering, not to establish a missing mathematical implication.


## SG-11 — All compact-support upper bounds and smooth proper purity

**Independent check of the final root strengthening.** Let X/F_q be separated of finite type and ℱ a constructible sheaf, with every local Frobenius eigenvalue of ι-absolute value at most |κ(x)|^{w/2}. Then each eigenvalue on H_c^i(X,ℱ) has absolute value at most q^{(w+i)/2}.

**Proof.** First take X smooth affine, pure of dimension d, and ℱ lisse. A geometric zero-dimensional component has cohomology only in degree zero. If it is defined over F_{q^a}, Frobenius induction replaces a local eigenvalue λ by the roots of T^a−λ, so the given local weight bound gives |α|≤q^{w/2}. This proves the dimension-zero base case without a purity theorem.

For positive d, Artin vanishing and duality kill H_c^i for i<d. The pointwise eigenvalue assumption gives |Tr(Frob_{x,n},ℱ_x)|≤rank(ℱ) q^{nw/2} for all rational points over every extension, so SG-09 proves the bound for i=d. Choose a smooth affine generic hyperplane section Y satisfying ordinary weak Lefschetz for ℱ^∨; the same exact Katz hypothesis used in SG-08 provides it after a finite extension. The Gysin map H_c^{i−2}(Y,ℱ|Y)(−1)→H_c^i(X,ℱ) is surjective for i=d+1 and isomorphic for i>d+1. Dimension induction bounds its source by q times q^{(w+i−2)/2}, which is exactly q^{(w+i)/2}. A subquotient inherits this spectral bound. This proves all degrees for the smooth affine lisse case.

Over the perfect field F_q, remove nilpotents and stratify X into finitely many smooth affine locally closed pieces, of pure dimension, on which ℱ is lisse. Refine the stratification to admit a filtration by closed subsets; the open successive pieces may be finite disjoint unions. For a closed complement Z of an open union U, localization has the exact segment H_c^i(U,ℱ|U)→H_c^i(X,ℱ)→H_c^i(Z,ℱ|Z). Every eigenvalue on the middle term is an eigenvalue of a subquotient of one of these two adjacent groups. Both are in degree i, so the induction on strata incurs no degree loss. This proves the asserted bound. Any finite extension used above is harmless: |α^e|≤(q^e)^{(w+i)/2} implies the original bound.

For smooth proper X of pure dimension d and pointwise pure lisse ℱ of weight w, properness identifies H^i with H_c^i, giving the upper bound. The dual ℱ^∨ is pointwise pure of weight −w. Poincaré duality is Frobenius-equivariant and pairs H^i(X,ℱ) with H^{2d−i}(X,ℱ^∨) into Q_l(−d). Thus q^d/α occurs in the latter whenever α occurs in the former. Applying the upper bound to that dual group yields |q^d/α|≤q^{(−w+2d−i)/2}, or |α|≥q^{(w+i)/2}. This matches the upper bound and proves smooth proper purity, including nonprojective smooth proper X. No cohomological semisimplicity, algebraicity for arbitrary sheaves, or general six-functor theorem is proved by this numerical argument. ∎

**Final-text audit, 2026-11-21 UTC.** The complete file section_main.tex was read and re-proved, including HS-01–HS-03, SG-08–SG-11, and HS-04/04B/05. All pass relative to the explicitly listed foundational inputs. Katz Corollary3.4.1 and AppendixA.1–A.5 were re-read for the exact fixed-function family, quasi-finite map, degree range and weight-free proof. The conclusion above is stronger than the earlier projective-only induction, and supersedes that limitation without changing the scope concerning cycle-class kernels or index positivity.
