# Step 1 adaptive source search

Run TRACE_DET_20261121, 21 November 2026. Agent `/root/step1_structural`; model GPT-6 Astra Pro (inherited developer label), effort setting not exposed.

## Scope and outcome

The note's entire step 1 is the chronological phrase “10/6/26: Stepanov determinant” (Remark, §2, p.3). Its earlier introductory discussion associates Stepanov with a divisor carrying multiplicity and the challenge of finding an integer/automorphic counterpart. The supplied source map §4 gives no matched declaration; its Wronskian/Hasse-derivative names were explicitly only nearest neighbors.

The independent structural search below finds **several actual finite determinant mechanisms**, with exact entries, and rules out taking the first Wronskian name as an established historical match. It does **not** identify one of them uniquely as the note's step-1 determinant. The surviving gate is an exact correspondence from that chronological phrase to a declaration/parameter choice, or to an explicit auxiliary-function/divisor construction with its multiplicity and point-count interpretation. No conclusion about the truth of the stipulated Alpöge theorem is drawn, and no Lean build was attempted.

Paths below are relative to the downloaded public mirror's `lean/src` tree. The root's provenance audit applies; this is not a separately authenticated author archive.

## 1. Wronskian route: a concrete false identification avoided

`Development/AbelianVarietyTheory/Proofs/FoundationProofs/EisensteinWronskianNeZero.lean`, lines81–82, defines

\[
\mathrm{wr}=2E_4 D E_6-3E_6 D E_4,
\]

with normalized derivative D. The theorem `wronskian_E₄_E₆_ne_zero` at162–168 is the nonvanishing of the corresponding ordinary-derivative expression on the complex upper half-plane. Its declaration wrapper is `EisensteinWronskianNeZeroStatement.lean:9–10`. The nearby `ExistsLevelOneSimpleZeroFormAtPoint.lean` uses it in constructing modular forms with a simple zero.

This is a modular-form Wronskian over C, with weight12 and discriminant nonvanishing in the inspected proof's endpoint (lines155–160). It is not, on the basis of that name or statement, a finite-field Stepanov auxiliary-function determinant. The exact domain and formula therefore eliminate a tempting but unsupported identification. The full modular-form proof was not independently verified.

`GroundTheory/AutomorphicForms/ArchimedeanWhittaker/WronskianEqZeroOfModerate.lean` is another unrelated Wronskian neighborhood: the inspected beginning treats a scalar ODE, moderate growth, and exponential-growth contradictions (e.g. lines53–67). It does not resolve the chronological attribution either.

## 2. Theta evaluation determinant route

`Development/AbelianVarietyTheory/Proofs/FoundationProofs/ColA.lean:18–23` defines three elliptic theta columns

\[
A(z)=\sigma_*(z)^3,\quad
B_v(z)=\sigma_*(z)(\mathrm{sqTh}_v(z)+\wp(v)\sigma_*(z)^2),
\]
\[
C_v(z)=\sigma_*(z)\mathrm{sqTh}_v'(z)-2\sigma_*'(z)\mathrm{sqTh}_v(z).
\]

`FrobeniusStickelbergerSigmaStarDetComplex.lean:20`, theorem `sgStar_cube_det_cplx`, states the explicit 3×3 determinant of these columns at z_0,z_1,z_2 equals

\[
2\sigma_*(z_0+z_1+z_2)\sigma_*(z_0-z_1)
\sigma_*(z_1-z_2)\sigma_*(z_2-z_0).
\]

The assumptions are a complex lattice Λ, v outside Λ, and arbitrary three complex inputs. The displayed matrix and its theta zero factors offer an actual evaluation/multiplicity mechanism. They do not identify the note's earlier Stepanov determinant; the sources inspected do not supply a Xi spectral parameter or a positive Hilbert operator. The statement and column definitions were checked, not the complete theta-function proof.

## 3. Finite monomial interpolation over a residue field

`ReciprocityTheory/DualLattices/MonomialDeterminantStatement.lean:11–20` gives a valuation statement about the matrix

\[
M_{x,\alpha}=\prod_j u_j(x)^{\alpha_j},\qquad
x,\alpha\in(\mathbf Z/p)^\iota.
\]

The exponents use the standard representatives in {0,...,p−1}, exactly `.val` in the source. Here the finite-coordinate functions u_j reduce modulo the valuation ideal to an invertible linear change Λ of the coordinates; the proposition asserts valuation1 of the determinant and a precise valuation product after rescaling by ε_j. Its type is a finite monomial-evaluation matrix, not a Fredholm operator.

`LiftMonomialDeterminantStatement.lean:18–26` defines `xL`, `monX`, the finite matrix `valM`, the inverse-matrix interpolation coefficients `coefX`, and their selected linear coefficient `linX`. Lines36–41 state determinant nonvanishing under its Hodge–Tate/lift data. The proof is furnished in `LiftMonomialDeterminantStatementHolds.lean` through the finite residue matrix `MuR`, the factorization `valM_eq` and `det_valM_ne`, ending in `liftMonomialDeterminantStatement_holds`. The underlying finite-field matrix nonvanishing is `ProdEraseUpdate.lean:223`, `det_monF_ne_zero`, reached via `span_monF_eq_top` at195 and finite delta functions at171–175.

This is a stronger structural candidate than a name search: it is genuinely a determinant controlling interpolation and integrality. But the displayed context is a finite Hodge–Tate/residue-field calculation, not a documented equation equating this determinant to the note's step1. No such correspondence is claimed.

## 4. Hasse derivatives of polynomial minors

`Formalism/ThetaLogCoordinates/UniformThetaSubstitution/StatementAB.lean:19–27` defines directional Hasse derivatives as the coefficients of Q(X+Σ_k b_k Y_k). It defines the finite minor polynomial at53–57:

\[
\mathrm{minorAt}(s,T,I)
=\det\left(\sum_a T_{ia}X_{s,a,I(c)}\right)_{i,c\in\operatorname{Fin}(l)}.
\]

`MinorHits` (59–66), `HitsCap` (68–74) and `HitsColumns` (76–82) formulate vanishing when directional hits exceed the multilinear capacities of rows/columns or miss the relevant block. These are definitions of propositions, not proof declarations. The neighboring `FrobeniusLiftNorms/MinorProdBlockDegree.lean` contains `HitsCapPos_of`, `HitsColumnsPos_of`, `hasseDerivSupport` and `minorProdBlockDegree`, giving finite combinatorial/degree reductions.

This is actual determinant-plus-multiplicity algebra, of the type relevant to the broad Stepanov analogy. It has no Xi operator in its definition. Its exact identity with the chronology remains unestablished; a structural resemblance is not a source citation for that identity.

## 5. Frobenius/Moore route

`Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/TwistStep.lean:93–96`, proposition `Moore`, uses

\[
\det(\varphi^i(a_j))_{i,j\in\operatorname{Fin}(k)}\ne0
\]

for linearly independent vectors in a p-adic period ring satisfying φ^h(a_j)=l a_j and the source predicate `Plus T`. `Proofs/InertiaEigenvalues/MooreDeterminantCrisPlusNeZero.lean:32–39` gives its general finite determinant induction template `moore_core`; lines154 onward supply `moore_statement` in the p-adic setting.

A separate definition `Definitions/NonGaloisDescent/MooreNorm.lean:57–60` asserts the ultrametric norm of the characteristic-p finite Moore determinant (λ_j^{p^r}), subject to the stated orthogonality and monotonicity assumptions. The same file's `GLCount` at33–37 concerns zeros of a finite additive polynomial system. These are finite Frobenius interpolation/period matrices, not a scalar Xi Fredholm determinant or a signed Hermitian Gram operator. They do not isolate the note's historical Step1 either.

## 6. Approaches tried, with explicit limits

1. Read the actual note and the supplied map rather than treating “Stepanov” as an established declaration name.
2. Search filename candidates for derivatives, jets, auxiliary polynomials, multiplicities and interpolation; 8,023 candidate paths were retained for orientation, not all read.
3. Search Wronskian/Hasse/auxiliary-polynomial text; 36 files matched the selected patterns. Read the actual modular Wronskian definition and statement, and the Hasse-minor definition branch.
4. Follow concrete determinant inputs through theta evaluation and finite monomial interpolation rather than assuming they are generic Gram matrices.
5. Search Moore/confluent/Vandermonde/evaluation-matrix patterns; 505 matching files were retained. Read the finite period-ring and characteristic-p Moore definitions and the principal finite monomial branch. The retained search results are candidate lists, not an exhaustive proof audit.
6. Inspect the function-field definition/declaration neighborhood: it supplies places, divisors and the Riemann–Roch inequality (ExistsBoundDegSubFinrankL.lean:160), but the inspected route did not connect a determinant to the note's chronological Step1.

**Smallest remaining gate:** identify which specific finite matrix, auxiliary section or differential operator the note calls its Stepanov determinant, together with the specialization that supplies multiplicity. The present mathematical comparison already applies to every fixed finite characteristic determinant as DET-03 states; identifying a compatible positive trace-class limit would still require DET-05's extra operator/spectral bridge. No bounded text search proves that no unnamed implementation or future transformation exists.
