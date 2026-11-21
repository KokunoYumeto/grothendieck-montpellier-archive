# Independent whole-proof audit: D-SR-01–04

2026-11-21. Auditor: GPT-6 Astra Pro, HODGE_DIVISION /root/sixfolds; inherited effort not exposed. Source read in full: `agents/imprimitive/SEMIREGULAR_CM_PROOFS.md`, revision including the direct Hom/Serre-duality Ext bound and the explicit isogeny/negative-Ext proof, SHA256 `caebef323489009de7e49fe52955dffd17304cb9276bbe816e1c7fbf942e80fa`. The audit is an independent mathematical re-derivation and a separate exact exterior-algebra certificate, not a proof-assistant check.

**Outcome: D-SR-01–04 pass in their stated scope.** No Markman theorem is needed by these proofs. Their final deformation consequence uses the supplied DEG_L S-14/Perry input, whose status must remain explicit. The finite cyclic subgroup is specified by a terminating algebraic search; its astronomically large point coordinates have not been enumerated. The categorical theorem by itself does not yield a numerical detector-degree bound.

## D-SR-01

The difference map C×C→C−C has generic degree one: equality p−q=p′−q′ gives p+q′∼p′+q, and nonhyperellipticity makes this degree-two divisor unique, apart from the zero-fibre coincidence. Its pushforward class is2Θ by the Pontryagin/Poincaré formula. Two pullbacks of general3Θ hyperplanes through0 cut the surface properly because their base locus is the finite group J[r]; each torsion point contributes at least one. This independently gives108r⁴.

The map from exact-order-N vectors to exact-order-q vectors is uniform. One may justify it by transitivity of GL6(Z/N) on primitive vectors, or directly prime by prime. The total number of primitive q-vectors is greater than q⁶/2. For each divisorq, counting allφ(q) generators only overcounts. The Euler product bound is exact:

    Σ_(q|N) φ(q)/q² = Π_(p^a||N) (1+(1−p^(−a))/p).

The dyadic Chebyshev estimate is valid: in(r,2r] at most one power of each prime occurs, and its contribution to v_p binom(2r,r) is at leastone, while every other Legendre summand is nonnegative. Summing gives log L<Plog4. Since every prime ofN is>P, Σ1/p≤logN/((P+1)log(P+1))<1/500 forP=2^2048, includingN=4mL²+1,m≤163. Thus the union bound is≤216/499<1 and proves a disjoint cyclic orbit exists. This is a finite existential search with an explicitly specified bound, not an observed torsion enumeration.

The quotient restriction is an embedding, and the rational polarization and volume are correctly normalized: q*θ=Θ and ∫θ³/6=1/N. Pulling back the claimed ideal Chern character gives precisely that of N disjoint genus-three curves. In particular the top character integrates to2, as χ(I_Cbar)=2 requires.

## D-SR-02

The normal-sequence proof ofh0N=3 is complete: the dual of its obstruction map is multiplication H0(K)⊗H0(K)→H0(K²), surjective for a plane quartic because no quadric contains it. The normal degree4 givesh1N=3.

I independently checked the revised direct Ext bound. Hom(I,O)=C and its restriction toO_C iszero, so H0N injects intoExt¹(I,I). Serre duality givesExt¹(I,O)=H²(I)*. The Abel–Jacobi restriction H¹O_Z→H¹O_Cbar is an isomorphism; henceH²I≅H²O_Z hasdimension3. ThusExt¹(I,I) hasdimension≤6. Translation directions give3 independent embedded deformations, while degree-zero tensor directions give3 independent trace directions. Their determinant traces distinguish them, so the bound is attained. Simplicity and CY3 Serre duality give(1,6,6,1).

The degree-one trace hasrank6: its H¹O block isidentity from rankone, and translation contraction withch2=−Nθ²/2 isinjective on the three-dimensional holomorphic tangent space. The degree-two trace hasrank6 because its H²O block isidentity, and the H¹T contraction block maps ontoH³Ω¹. In a Darboux basis the latter is the surjection H¹T→∧²H¹O followed by the isomorphism β↦βθ ontoH³Ω¹. This uses only the classical Atiyah-trace/contraction identity. The same argument holds for the derived dual, whosech3 sign changes butch2 doesnot.

For the external product, the three Ext² Künneth pieces map to distinct Hochschild bidegrees(−2,0),(−1,−1),(0,−2). Each factor trace isinjective in degrees0,1,2, so each restriction isinjective and there is no cancellation. Its Ext² dimension is6+36+6=48. Negative Ext vanishes for each factor, including the derived dual by contravariant duality, and hence for the product. This closes the product semiregularity step directly, without any additional unobstructedness hypothesis.

## D-SR-03

A separately written six-generator exterior algebra program `audit_rankzero_fm.py` computes exp(s(a+c)(b+d)−tcd−cv+du) and integratescd in the basis ordera,b,c,d,u,v. It exactly reproduces the claimed one-plane transform, with all signs. It separately checks the equal-root factorization, the unequal-root factorization witht=−2−s, and the odd exponential polynomial. All tests pass over exact symbolic coefficients; output is in `audit_rankzero_fm_output.json`.

The volume factorΔ=1/N is necessary and correct. A useful independent normalization check is the specialization of the constant term: Fourier–Mukai sendsO_Z toO_0[−3]; its character is−[0_Zhat]=−θhat³/(6N), exactly whatΔ times the three one-plane constant transforms gives. Thus no missing principal-polarization assumption is present.

For T=[[-2,−1],[N,0]], the point endomorphism induces the transpose action on one-forms. Explicitly T*(s a−u)=s(s a−u), using s²+2s+N=0, so the asserted determinant forms really are the Weil lines. The matrix S(T+1)=[[0,−d],[d,0]] proves Rosati skewness. Positivity follows from(N−1)θ1+m*θ after the stated rational polarization identification. The two determinant tensors are nonzero and independent, and their conjugate nonzero coefficients yield a rational nonzero Weil class. The entire identity

    exp(−γ/2)ch(E)=t+2H−H³/(12d)+H⁵/(960d²)

therefore passes. Rankzero is harmless: S-14 assumes this exponential-twisted character, not a nonzero-rank normalization. Equivalence preserves the categorical trace and all self-Ext degrees, so its use here is valid.

For the determinant convention, one can add the following independent observation. The symmetric rational form q(x,y)=E_H(x,(T+1)y) has matrix(S(T+1))⊗E_θ and ishyperbolic: the first copy ofH¹(Z) is a half-dimensional isotropic rational subspace. The Hermitian splitting argument SF-CM04 therefore gives determinant[-1]. No Markman determinant theorem is needed for this step.

## D-SR-04

The three Fermat involution quotients have genusone by Riemann–Hurwitz andj=1728 from their quartic branch sets. Their three distinct V4 characters give the isogenyj:E_i³→J. Cross norm-pullback compositions arezero since distinct characters force each such homomorphism to equal itsnegative; Hom of abelian varieties is torsionfree. The diagonal compositions are[2]. Thusj*Θ=2θprod anddegj=8.

Forh=qj andr=2L, the two columns ofR=[[1,1],[bars,s]] are eigenvectors ofT+1 with eigenvaluesri,−ri. The mapf=Ndiag(h,φθh)R is integral becauseNθ is the norm-polarization class andNφθ is an actual homomorphism. It intertwines the specified balanced Gaussian action. Independent matrix multiplication givesR*SR=2dI, hencef*H=4dN²θprod. Alsodegk=(8N)²/N²=64, degR=(4d)³, anddeg[N]=N¹² on a sixfold. Their product is4096d³N¹². As a cross-check, χ(H)=d³ and χ(f*H)=(4dN²)^6, whose ratio is the same degree.

The canonical deck action is honest, coherent and lies in the actual subgroupkerf⊂E_i6×{0}. Descent identifies invariantExt² with the Ext² downstairs, and étale pullback commutes with full Atiyah trace. Cohomological pullback isinjective by the degree trace, so strong G-semiregularity follows.

The negative-Ext repair is essential and valid. Decomposef_*O into torsion Pic0 characters and use adjunction. UnderΦ^-1, tensoring by such a character becomes a translation and a Pic0 tensor onZ², hence a product operation. The first Ext factor compares coherent sheaves. The second compares derived duals of coherent sheaves and reverses to a coherent-sheaf Ext group in the same degree. Both vanish in negative degrees, and the Künneth convolution therefore vanishes in negative degrees. The argument verifies ordinary negative Ext, not only its invariants.

FinallyH0=4dN²θprod, so the source can indeed use the fixed very ample3θprod. B0=−f*γ/2 is algebraic rational andt0=f*t is nonzero. This supplies all object hypotheses of S-14 on the requested balanced Gaussian CM power.

## Scope retained

This is a proof of a specified finite-search construction and the complete object properties. It is not an execution of the enormous torsion search. The downstream deformation result retains the exact S-14/Perry status; no claim is made that its qualitative Chow/Baire argument already displays a numerical detector bound. The generalm extension retains split determinant and does not identify the non-Gaussian action on anE_i-isogenous sixfold with a balanced power ofE_K. The independent conditional Markman fallback SF-CM03 is logically unnecessary for the explicit Gaussian construction.


## D-SR-05 and D-SR-06 — independent complete proof checks

Date: 2026-11-21. Metadata: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION /root/sixfolds. The complete proof snapshot read for these checks has SHA-256 ac366d52e42cc7ee3ead0599112b3ad0953ffc0519ed7e63a6bb950aeda505dd. Outcome: **PASS in the stated scope**.

D-SR-05: q_H(v,w)=E_H(v,Jw) is symmetric; h=q_H+uE_H is conjugate-linear in the first argument and linear in the second with u²=-d. The rational theta-Lagrangian L gives the J-stable subspace L⊕L, which is K-dimensional three and totally isotropic. The space is therefore split. Adaptive P_m makes the finite torsion-avoidance bound valid for every positive squarefree m. For non-Gaussian K, the underlying CM sixfold is E_i-isogenous with the displayed K action, not an unproved identification with a balanced E_K power. The downstream S-14 conclusion remains qualified by the supplied Perry-preprint input.

D-SR-06: the explicit Gaussian pullback B_0=-f*gamma/2 is the integral Hermitian matrix 2N²[[1,-s],[-bar(s),1]] on the standard product. Its line-bundle twist produces an ordinary perfect object with zero B-field. Tensor conjugation preserves the actual finite group and coherent action. Inspection of Perry's full proof with b_0=0,n=1 gives the ordinary ambient category after its band changes, so the gerbe conclusion is justified. The Newton identities with c_1=0 give t_0=c_3/2+(16/3)d²N^6(1-8d)theta_prod³; the coefficient is integral and the specified class has denominator delta=2, not merely 6. Its self-pairing is -32768d^4N^12. The all-K map M k, M=2dN, gives degree 64M^12, integral B=-M²[[0,1],[1,0]], and self-pairing -2^21d^13N^12. Its polarization is the stated integral Theta_S, not principal. These conclusions supply a qualitative detector; they do not by themselves bound the regularity of the rank-zero output. SF-QC01–05 provide a separate positive-rank construction and the numerical bound.
