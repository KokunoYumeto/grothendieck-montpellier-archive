# DET-15: actual source convolution projections in a common Bessel L2 space

Run TRACE_DET_20261121. Date 21 November 2026 (UTC). Agent /root/step1_history_route, GPT-6 Astra Pro; effort setting not exposed. All source paths are relative to work/external_lean/lean/src. Full integration-ready theorem statements and proofs are in work/paper_bessel_projector.tex; this note records the source identity, gate change, and read scope.

## Outcome

The actual source operator rconv(muG,eFun(muG,sigma,w)) is a **positive orthogonal rank-one projection** on a specified common closed Bessel subspace of L2(nu,Wp), under the exact source Std, Side, IsQuotMeas, and IsEll hypotheses. It is not an infinite-rank isotypic projection. The source Std condition already normalizes ||w||=1. The formal-degree identity is fdegH=d>0.

For f_u(g)=l(sigma(g)u), the source norm identity becomes

\[
\int\langle f_v(g),f_u(g)\rangle\,d\nu(g)=\langle v,u\rangle/d.
\]

Thus eta_u=sqrt(d) f_u is an isometric model of the cyclic orbit span. The actual convolution on admissible functions is

\[
P_w W=d\langle f_w,W\rangle f_w
=\langle\eta_w,W\rangle\eta_w.
\]

The proof in the TeX makes the passage to L2 equivalence classes and the bounded extension explicit. It does not assume all ambient L2 classes have equivariant representatives.

## Concrete gate reduction

The common-space question can be resolved for an actual source family without increasing the numerical shift cutoff q0.

1. The retained Std hypotheses force the source representation Hilbert space to be infinite dimensional. The proof uses explicit Lorentz-boost bands to show that the source invariant measure has infinite mass, then uses the finite sum of Schur-orthogonal matrix coefficients to rule out finite-dimensional unitary representations.
2. The orbit span DD(sigma,w0) is dense by irreducibility. Gram–Schmidt inside that linear span gives a countably infinite orthonormal sequence u_j.
3. For every unit u_j in that span, DD(sigma,u_j) is contained in the original orbit span, the same decay estimate restricts to it, and IsEll has a nonzero value on it because the model function has norm squared 1/d. Every Std and IsEll hypothesis required by the actual projector export is therefore retained.
4. The same source convolutions give mutually orthogonal rank-one projections P_j on a fixed common Bessel Hilbert space. Their target Wp may be finite dimensional, but their L2 function space is infinite dimensional.
5. For any complex summable weights beta_j, the actual finite convolutions with coefficient sum_(j<=N) beta_j eFun(sigma,u_j) extend to T_N=sum beta_j P_j. Their trace-norm limit has exact tail sum_(j>N)|beta_j| and determinant product_j(1-w beta_j). Nonnegative weights give positivity. For example beta_j=2^-j gives a positive trace-class construction independent of zeros, with trace 1 and tail 2^-N.

This supersedes any suggestion that finite-dimensional Wp itself prevents an infinite-rank realization through the actual Bessel L2 model. DET-14's degree obstruction remains valid only for its fixed-Wp frame operators, a different realization. Its q0 restriction remains valid for the displayed shifted-family theorem; DET-15 varies vectors within a single representation instead.

## Exact zero-based embedding, and what remains separate

Taking the already proved B-01 weights beta_j=gamma_j^-2 gives T=VBV*, where V:e_j -> eta_(u_j) is an isometric embedding. Hence the actual Bessel model carries B direct-summed with zero on the orthogonal complement, and its ordinary determinant is exactly

\[
\det(I-wT)=G(w)=\Xi(\sqrt w)/\Xi(0).
\]

No RH is needed for this trace-class normal realization or its determinant. It is positive precisely when RH holds, since positivity requires every inverse-square weight to be real and nonnegative. Under the cited RH theorem, the finite source convolutions in this particular weighted construction are positive.

The source projections are positive independently of RH; the final weights were selected from Xi's zeros. This is not an independent arithmetic derivation of the weights and is not an identification of the Remark's historical determinant family. The remaining independent arithmetic-to-Xi gate must state which source data or finite determinant coefficients choose the weights and prove the resulting spectral identity without inserting the zeros.

The proof also supplies a measurable operator-valued integral kernel

\[
K_\beta(x,y)=\sum_j\beta_j\eta_j(x)\eta_j(y)^*.
\]

It converges absolutely almost everywhere and in product L2. The proof uses a(x)=sum |beta_j| ||eta_j(x)||^2, Tonelli, and Cauchy–Schwarz; it does not claim pointwise convergence everywhere or continuity of the kernel.

## Exact source map and retained hypotheses

| Source | Locator | Used content |
|---|---|---|
| Development/AbelianVarietyTheory/Definitions/SemilocalFrames/MatrixOfBesselTwoSidedAction.lean | 42–55 | Schur relation; cyclic span DD; full Std, including k>=1, unit w, irreducibility, unitarity, formal-degree positivity and decay. |
| Same file | 60–75, 119–121 | Side; Bessel form be; Afun; rank-one convention; IsEll factorization and nonzero value on DD. |
| Formalism/PeriodIntegrals/BesselPeriodGGP.lean | 59–92 | Exact Haar/quotient definitions, equivariant function class, l2SG, rconv, fdegH, eFun. |
| Development/AbelianVarietyTheory/Proofs/FlagMeasures/BesselFormalDegreeEqOfSchurOrthogonality.lean | 7–29 | Complete elementary formal-degree proof; no missing unit-vector factor. Export in matching Statement.lean:7–8. |
| .../BesselModelProjectorOnLine.lean | 40–69, 71–137 | Support of quotient measure on the group; full projector proof, norm identity, and all input measurability/equivariance clauses. Exact export in matching Statement.lean:7–8. |
| .../BesselFunctionalStandardSide.lean | 41–55, 57–82 | Change of variables for rconv and full integrable Bessel kernel identity. Exact export in matching Statement.lean:7–8. |
| .../NormIdentityBesselCoefficientQuotient.lean | 19–100 | Complete displayed sequence of mixed/norm identity proofs, invoking the named analytic dependencies. Exact equivariance, integrability, MemLp and mixed inner product in matching Statement.lean:7–8. |
| .../BesselFormConvergesEquivariantHermitianStatement.lean | 7–8 | Continuity on the group of the Bessel form on the invariant decay domain. This imported analytic theorem is retained, not independently re-proved here. |
| .../LintegralBesselCoefficientCompactLe.lean | 18–131, especially 29–53 | Read full displayed proof; it applies the Bessel-form continuity export and obtains ambient almost-everywhere strong measurability. |
| .../WeilFormulaBesselUnitaryIntegrableStatement.lean | 7–8 | Sigma-finite quotient measure, support and integrable Weil formula under the closed-subgroup/Haar/unimodularity hypotheses used in the source projector chain. |
| .../SmoothVectorsDenseInvariantStatement.lean | 7–8 | Invariant orbit span and density under irreducibility; the elementary density argument is also independently included in DET-15. |
| .../ExistsBesselMapRankOneFactorisationTranslateSpanStatement.lean | 7–8 | Actual IsEll existence under Std, Side, smooth w, MultOne, quotient measure and NonVan. |
| .../ExistsBesselMapRankOneFactorisationTranslateSpan.lean | 103–154 | Read full final theorem body and retained its imported existence/rank-one lemmas; no claim to have read every prior helper in that file. |
| Formalism/PeriodIntegrals/UpqRep.lean | 258–276, 307–311 | Comparison: unitary continuity, irreducibility, square-integrability and IsDS definitions. DET-15 uses the stronger explicit Std/Schur input, not an inference from the file title. |

Here .../ abbreviates only Development/AbelianVarietyTheory/Proofs/FlagMeasures/. The table does not claim a complete mathematical audit of every imported dependency or a Lean replay. The cited RH/Dirichlet results are not audited.

## Measurability and domain issue resolved

Choose v0 in DD with b0=l(v0) != 0, and N=||b0||². On the group,

\[
A_u(g)=\operatorname{be}(\sigma(g)u,v_0)b_0=Nf_u(g).
\]

The norm identity supplies equivariance and MemLp for A_u. The Bessel-form theorem supplies continuity on the group. Since the group is closed in a finite-dimensional matrix space and Wp is finite dimensional, its zero extension off the group is a strongly measurable representative for both muG and nu. Their support on the group makes the replacement harmless. The resulting class belongs to the space whose closure defines the common Bessel Hilbert space.

The source convolution formula then equals a rank-one bounded map on that dense class. Its scalar integral is absolutely integrable by L2 Cauchy–Schwarz. Consequently it is independent of the representative modulo nu-null sets and extends uniquely to the closed model. No assumption that a point-evaluation map is bounded on the full representation Hilbert space is used.

## Verification

The complete 374-line initial TeX proof was read after saving. All normalization, sign, quotient representative, dense-domain, positivity, idempotence, infinite-dimension, inherited-hypothesis, complex-weight, kernel, and zero-dependent realization assertions passed the post-save check. Two subsequent additions clarify abbreviated source paths and the explicit beta=2^-j example; both were separately checked. Root has the proof path, and /root/masullo_spectral_bridge is conducting an independent proof check.
