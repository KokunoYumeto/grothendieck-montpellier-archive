# DET-15 — independent check of the actual Bessel-model projections

## Verdict and scope

I read the whole saved proof in work/paper_bessel_projector.tex and checked its main source dependencies against the Lean export and definition files. **No mathematical fault was found in the stated consequence of the retained source hypotheses.** The passage from the source convolution identity to genuine orthogonal projections on one fixed closed Bessel subspace is justified. The infinite sequence, summable weighting, ordinary determinant and measurable integral kernel also pass.

This is an independent mathematical/source-reading check. It is not a Lean replay, not a recursive verification of all imported lemmas, and not an assertion that the retained hypotheses hold for arbitrary input data. In particular, existence of the factorizing Bessel map retains the source's smoothness, multiplicity-one and nonvanishing assumptions when obtained through its stated existence export.

The main construction gives an actual source convolution realization of B⊕0 after assigning the Xi-zero-dependent weights. It does not independently determine those weights from arithmetic, identify a historical finite determinant family, or prove their positivity without the corresponding zero-location input.

## 1. Exact source interfaces read

Paths below are relative to work/external_lean/lean/src/.

1. Development/AbelianVarietyTheory/Definitions/SemilocalFrames/MatrixOfBesselTwoSidedAction.lean, lines 40–55 and 119–121: coefficient convention, SchurH, algebraic orbit span DD, the complete Std bundle, and IsEll.
2. Development/AbelianVarietyTheory/Proofs/FlagMeasures/BesselModelProjectorOnLineStatement.lean, line 7, and the complete BesselModelProjectorOnLine.lean, lines 1–137: quotient support, full norm identity and actual rank-one convolution formula.
3. NormIdentityBesselCoefficientQuotientStatement.lean, line 7: equivariance, integrability, MemLp and the mixed inner-product identity for Afun.
4. BesselFormConvergesEquivariantHermitianStatement.lean, line 7: convergence, equivariance, Hermitian symmetry and continuity on G of the Bessel form on an invariant domain satisfying the retained decay bound.
5. LintegralBesselCoefficientCompactLe.lean, lines 29–53: the actual application of that continuity statement to DD and the passage to ambient almost-everywhere strong measurability.
6. WeilFormulaBesselUnitaryIntegrableStatement.lean, line 7: sigma-finiteness and G-support of ν, together with the integrable Weil formula under its specified subgroup hypotheses. BesselFunctionalStandardSide.lean, lines 59–73, explicitly supplies those hypotheses from Std and Side.
7. BesselFunctionalStandardSide.lean, lines 1–82: the change of variables, group-integrability input, quotient kernel integral and normalized convolution identity.
8. BesselFormalDegreeEqOfSchurOrthogonality.lean, lines 7–29: the elementary normalization fdegH=d for every nonzero representation vector.
9. ExistsBesselMapRankOneFactorisationTranslateSpanStatement.lean, line 7: the exact assumptions needed to produce IsEll, rather than treating its existence as automatic.
10. Formalism/PeriodIntegrals/BesselPeriodGGP.lean, lines 59–92: actual Haar/quotient-measure predicates, equivariance, l2SG, right convolution, formal degree and eFun.
11. Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean, lines 23–28 and 287–295: unitary representation, irreducibility and the restricted smooth-vector clauses of IsBesselMapSm.
12. Formalism/PeriodIntegrals/UpqRep.lean, lines 215–226: the defining Hermitian form Hpk, the group and the representation law.

The inner product is conjugate-linear in its first argument. The source defines coef σ u v(g)=〈v,σ(g)u〉. The paper's Schur relation, rank-one operator and convolution normalization respect that convention.

## 2. Measurability, equivariance and the common closed space

The model is defined as the closure in L²(ν;Wp) of equivalence classes of functions satisfying the exact source conditions: almost-everywhere strong measurability for both μG and ν, pointwise source equivariance on G, and finite l2SG norm. This is a legitimate closed Hilbert subspace, denoted ℬ. Its defining representative space is linear. It depends on the fixed side and measure data and not on the vector selected later.

The proof does not presume that this space equals the whole ambient L² space, nor that every equivalence class has a pointwise equivariant representative. This distinction matters because the source convolution theorem is stated on that precise representative domain. Closure is sufficient: the rank-one formula supplies the bounded extension.

For u∈D=DD(σ,w₀), choose v₀∈D with b₀=l(v₀)≠0 and set N=‖b₀‖². Define

\[
A_u(g)=\operatorname{be}(\sigma(g)u,v_0)b_0.
\]

D is invariant under G. IsEll therefore gives A_u(g)=N l(σ(g)u) on G. The source norm-identity export makes A_u equivariant and square integrable for ν. The Bessel-form continuity export applies to D, using the retained decay condition and its invariance, and makes A_u continuous on G.

G is closed in the finite-dimensional matrix space. Extending A_u/N by zero off G consequently gives a Borel measurable function with values in finite-dimensional Wp, hence a strongly measurable function for both measures. Both measures are supported on G. Source equivariance only compares points g and hmg inside G; zero extension therefore preserves the required equivariance. These representatives belong to the defining domain and yield [f_u]ν∈ℬ, where f_u(g)=l(σ(g)u) on G.

No global continuity or boundedness of l on Hσ is inferred. IsBesselMapSm only asserts its linearity/equivariance on smooth vectors; the present argument correctly obtains the required properties on D from the Bessel-form factorization and the mixed norm identity.

## 3. Isometry and the actual orthogonal projection

The mixed source identity gives

\[
\int\langle A_v(g),A_u(g)\rangle\,d\nu(g)
=\frac{\langle v,u\rangle
\langle b_0,\operatorname{be}(v_0,v_0)b_0\rangle}{d}
=\frac{N^2\langle v,u\rangle}{d}.
\]

Since A_u=Nf_u on G and both measures have the necessary support, cancellation of N² gives

\[
\eta_u=\sqrt d\,[f_u]_\nu,
\qquad
\langle\eta_v,\eta_u\rangle=\langle v,u\rangle.
\]

This is sufficient to establish complex linearity of u↦ηu on D. Expand the squared norm of the difference between the proposed linear combination and the image of the corresponding combination in D; every inner product is replaced by its source-space counterpart, giving zero. Thus no unproved pointwise linearity of l outside the smooth vectors enters the construction.

The source projector formula, applied to an admissible W, is exactly

\[
\operatorname{rconv}(e_{w_0})W(y)
=d\left(\int\langle f_{w_0}(g),W(g)\rangle\,d\nu(g)\right)f_{w_0}(y),
\qquad y\in G.
\]

The scalar integral is absolutely convergent by Cauchy–Schwarz. The underlying kernel proof also establishes integrability of the original group convolution. Passing to ν-equivalence classes is therefore justified, and the formula proves that the result depends only on [W]ν despite the different measures in the original and final expressions.

Because ‖w₀‖=1 and d>0 are explicit Std clauses, ηw₀ is a unit vector. The formula is the orthogonal projection

\[
P_{w_0}W=\langle\eta_{w_0},W\rangle\eta_{w_0}.
\]

It uniquely extends from the dense admissible domain to ℬ. It is positive, selfadjoint, idempotent, rank one and trace class, with trace 1 and determinant 1−w. The normalization check fdegH=d is correct: the Schur denominator is ‖u‖⁴/d. The source projection theorem is reapplied only to unit vectors; arbitrary vector scaling is not silently interpreted as an orthogonal projection.

## 4. Infinite dimension without an omitted Haar hypothesis

The proof that μG(G)=∞ is valid for the exact weak Haar predicate in the source. In particular, it does not require an unstated Radon or local-finiteness assumption.

The source's Hpk has a diagonal +1 at coordinate r and a diagonal −1 at coordinate r+k, with k≥1 ensuring these coordinates are distinct. A real Lorentz boost g(t) on this two-dimensional block preserves Hpk. For the row covector ℓ=eᵣᵀ+eᵣ₊ₖᵀ, one has ℓg(t)=eᵗℓ. All x∈G are invertible, since Hpk is invertible, so Q(x)=‖ℓx‖>0. The Borel bands

\[
E_n=\{x\in G:e^n\le Q(x)<e^{n+1}\},\quad n\in\mathbb Z,
\]

partition G, and g(1)E_n=E_{n+1}. Left invariance gives equal measure to all bands. A finite total measure would force that common value to be zero, and then the total measure would be zero. This contradicts the source's nonzero, G-supported measure.

If Hσ had finite dimension q≥1, unitarity would give

\[
\sum_{i,j=1}^q|\langle e_i,\sigma(g)e_j\rangle|^2=q
\]

on G. The Schur hypothesis makes every summand integrable with integral 1/d. Hence qμG(G)=q²/d<∞, contradicting the preceding result. Hσ is therefore infinite dimensional.

The closed orbit span of the nonzero w₀ is invariant under all bounded representation operators. The exact IsIrredOn predicate makes it all of Hσ. Gram–Schmidt within the linear space D consequently produces an infinite orthonormal sequence u_j∈D. The isometry above produces orthonormal η_j in the same ℬ.

## 5. Reapplying the source to every selected vector

For each unit u∈D, its algebraic orbit span D_u=DD(σ,u) is contained in D. The Std hypotheses for the same representation, measure, formal degree and decay exponent are unchanged; its unit-vector clause holds, and its decay clause restricts to D_u.

The IsEll rank-one factorization also restricts. Its Bessel-map clause is unchanged. Its nonvanishing clause on D_u follows from

\[
\int\|l(\sigma(g)u)\|^2\,d\nu(g)=1/d>0.
\]

Since ν is supported on G, some g∈G has nonzero l(σ(g)u), and σ(g)u lies in D_u. Thus every source hypothesis needed for the projector theorem holds after replacing w₀ by u. No additional smoothness or multiplicity-one assumption is introduced at this step: those enter only if one constructs the original l through the separate existence theorem.

It follows that each P_j=η_jη_j* is the bounded extension of its own actual source convolution with e_{u_j}. This is the essential step that distinguishes the construction from merely inserting abstract projections into the ambient Hilbert space.

## 6. Trace-class series and the measurable kernel

For complex weights with ∑|β_j|<∞, the mutually orthogonal rank-one ranges give

\[
T_\beta=\sum_j\beta_jP_j,
\quad \|T_\beta-T_N\|_1=\sum_{j>N}|\beta_j|,
\quad \operatorname{Tr}T_\beta=\sum_j\beta_j,
\quad \det(I-wT_\beta)=\prod_j(1-w\beta_j).
\]

Tβ is normal and is positive exactly when every βj is nonnegative real. Each finite sum is the bounded extension of the actual convolution with the finite kernel sum ∑_{j≤N}βje_{u_j}; group-integrability and finite linearity were checked through the cited kernel proof. The proof does not claim that the infinite operator is convolution by an independently justified infinite group kernel.

Its separate quotient integral kernel is rigorous. For measurable representatives ηj, put

\[
a(x)=\sum_j|\beta_j|\|\eta_j(x)\|^2.
\]

Tonelli gives ∫a=∑|βj|<∞. The series for

\[
K_\beta(x,y)=\sum_j\beta_j\eta_j(x)\eta_j(y)^*
\]

is absolutely convergent in matrix operator norm almost everywhere, because its sum of norms is bounded by √(a(x)a(y)). The same bound in finite-dimensional Hilbert–Schmidt norm places Kβ in product L². Applying it to tails proves product-L² convergence. The source quotient-measure theorem supplies sigma-finiteness needed for the product measure/Fubini steps.

For almost every x, the kernel integral against any W∈L² is absolutely convergent, with bound √a(x)(∑|βj|)^{1/2}‖W‖₂. Product-L² convergence of kernels implies operator-norm convergence of their integral operators by Cauchy–Schwarz. The finite kernels give exactly T_N, so the limiting kernel gives Tβ, including its restriction to ℬ.

## 7. The exact B embedding and remaining identification

Choosing βj=γj⁻² from the B-01 Xi-zero list gives summable absolute weights without RH. The isometry V:e_j↦η_j satisfies Tβ=VBV*, so Tβ is B on the closed image of V and zero on its orthogonal complement. The ordinary determinant is therefore G(w)=Xi(√w)/Xi(0), and positivity is equivalent to the same zero-location condition as positivity of B.

The source projections are already positive independently of this choice of weights. A nonnegative summable weighting gives a positive trace-class operator, but obtaining the particular determinant G requires the specified Xi-zero-dependent weighting. The paper states that dependence and the absence of a historical/arithmetic identification correctly.

## 8. Check completion

All parts of the saved proof were read: exact source hypotheses, common closed model, measurability, mixed normalization, convolution extension, infinite dimension, inheritance to the selected orbit spans, weighted trace-class formulas, the measurable kernel, and B⊕0. No corrective edit to the author file is requested. No master file was changed by this checker.
