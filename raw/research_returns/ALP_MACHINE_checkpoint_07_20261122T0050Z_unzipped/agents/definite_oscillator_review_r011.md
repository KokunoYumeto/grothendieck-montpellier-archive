# Independent whole-proof review of AM-R-011

Reviewer: GPT-6 Astra Pro, ALP_MACHINE `/root/definite_oscillator`;
inherited reasoning effort not separately exposed; 21 November 2026 UTC.

Reviewed the complete saved `work/research/selected_schur_metric.md`,
including its distinction between the source row partition and the
selected kernel partition. The result **passes in its stated scope**.
No compilation, automatic theorem checking, or independent proof of
the cited Schur--Weyl and hook-length theorems is claimed.

## 1. The actual source conventions

The following definitions were read directly from the recovered,
pinned source, including newly fetched immediate dependencies:

- `Formalism/LocalRingCardinality/DataCoeff.lean`: `detShift`,
  `natW`, `extremal`, `normFock`, and `normFockQ`.
- `Formalism/LocalToGlobal/HermitianForms/IsLocBasis.lean`:
  `nfAll`.
- `Formalism/GradedWeylDivisibility/StatementA.lean`:
  `lpMinor`, `nuNext`, `hw`, `rowDiv`, and `weyl`.
- `Formalism/GradedWeylDivisibility/StatementB.lean`:
  `fockQ`.
- `Formalism/RealPlaceAnalysis/FockPairGl.lean`: `fockF`.
- `Formalism/LocalToGlobal/Divisibility/RecBridgeNum.lean`:
  `logHook_eq`, including the factorial/Vandermonde identity used
  in the displayed proof.

In particular the source's `hw` is exactly the product of leading
principal minors raised to successive differences of the partition.
There is no factorial rescaling in this highest polynomial.
Both `fockQ` and `fockF` use ordinary monomial factorials;
`fockF` is linear in the first variable and conjugate-linear in
the second. This conjugation convention does not affect any of
the squared-norm statements in R011. The source row metric
therefore divides the ordinary Fischer metric by the hook product
of `natW`, exactly as asserted in (R11.12).

The source's Weyl module is generated integrally using divided
row operators applied to this primitive highest polynomial.
That feature does not change the complex invariant form or its
highest-vector norm. It does remain relevant to the separate
integral selected-row problem; R011 expressly does not replace
that lattice by an arbitrary rational projector image.

## 2. Highest matrix coefficient and hook normalization

For a rectangular linear map \(Z:\mathbf C^a\to\mathbf C^b\),
the cited Schur--Weyl decomposition gives
\[
 (\operatorname{tr}ZW^*)^D
   =\sum_{|\lambda|=D}f_\lambda
              \operatorname{tr}(S_\lambda(Z)S_\lambda(W)^*).
\]
After division by \(D!\), the coefficient is
\(f_\lambda/D!=H_\lambda^{-1}\). With compatible unitary
Schur metrics, expansion of that trace in orthonormal bases is
the sum of the products of matrix coefficients. The Cauchy
summands are distinct irreducibles for the two compact groups,
and their matrix coefficients are linearly independent. Thus
comparison of reproducing kernels gives mutually orthogonal
coefficients of squared Fischer norm \(H_\lambda\).

The possible scalar in the highest coefficient is fixed, rather
than assumed: a unit highest vector in the source Schur module
maps to its compatible unit highest vector under the standard
coordinate inclusion, and a diagonal matrix acts there by
\(\prod_i z_i^{\lambda_i}\). The product of leading minors
has exactly this restriction and leading coefficient one.
Multiplicity one of the highest line identifies the two.
Consequently (R11.7) has the asserted scalar, including for
rectangular matrices. The proof uses the cited representation
theorems; it does not claim that the finite examples prove the
general identity.

## 3. Determinant insertion and the exact source partition

AM-DO-025 gives the actual source weights, and subtracting their
last entry gives
\(\eta_j=\operatorname{natW}(\operatorname{lamTrue}_j)\).
The selected kernel partition satisfies
\(\nu_j=\eta_j+q_j\mathbf1\), with \(q_j>0\), and
the following row partition is \((\nu_j,0^d)\).
Thus it is correct to distinguish \(H_{\eta_j}\) from
\(H_{\nu_j}\).

Multiplication by \((\det Z)^q\) is an integral polynomial
map. Its pullback of the compact invariant metric is a scalar,
because its domain is an irreducible complex coefficient module
and the determinant twist is unitary. Evaluation on the highest
vector fixes that scalar as \(H_{\eta+q\mathbf1}/H_\eta\).
In the hook factorial formula the Vandermonde denominator is
unchanged by a uniform shift, leaving exactly the integral
product (R11.11). These observations verify (R11.10)--(R11.12)
for all vectors in the stated coefficient module.

Appending zero rows preserves hook products. The telescoping
in (R11.13) is consequently exact. Its scope is only the
successive row-normalization numbers. Neither the source theta
operator, its chosen integral lattice, the class-volume factors,
nor terminal mass becomes an isometry by this identity.

## 4. Actual Gaussian and finite projection

There are \(ab\) copies of \(A=J^2\), so their actual squared
Gaussian norm is \(\det(2Y)^{-ab}\). At each selected CM
coordinate every matrix entry has the common creation scale
\(\pi/(2G_i)\); the selected polynomial is homogeneous of
degree \(|\nu|\). Orthogonality of the CM blocks then gives
(R11.14) exactly. This retains the corrected raw-Gaussian factor
in R009, the coordinate factor \(1/2\), the hook norm, and the
separate analytic-to-algebraic period. The compact Haar
matrix-coefficient factor \(1/\dim V_\eta\) also remains.

For (R11.16), the central integral numerator in (R11.17)
commutes with simultaneous permutations of the two tensor
factors, so it descends to the ordinary integral symmetric
quotient. Over \(\mathbf Q\) its image is exactly the
\(\lambda\) Cauchy component. The two lattice inclusions
follow: its denominator divides \(H_\lambda\), and it fixes
every integral vector in that component. No integral
semisimplicity is used. The stated annihilator and length
bounds follow after localization at a prime. The sufficient
condition \(p>\lambda_1+a-1\) exceeds every hook length.

This is a valid bound for the specified projector, not a formula
for the least source-row denominator or the gain of the actual
theta matrix. In particular determinant insertion is already
integral; its hook norm is not itself a forced denominator.
The example \(6\to20\to34\), degrees \(6,46\), and
\(\nu_1=(3^6,2^{14})\) agrees with the checked recurrence.

## 5. Additional source-operator check

The newly recovered
`Development/AbelianVarietyTheory/Definitions/LatticeFrames/EvalAtOneExtremalMul.lean`
defines `mvZ` by
\[
 X_{\tau,\beta,p}\longmapsto
   \sum_{i,j}h_{\tau,i\beta}g_{\tau,pj}X_{\tau,i,j}.
\]
Thus `mvZ(g^{-1},h)` is precisely the substitution induced on
creation labels by \(X\mapsto hXg^{-1}\). This independently
checks the polynomial covariance used in AM-DO-026 against the
literal source definition, rather than inferring it from its name.

The final status is PASS for AM-R-011 and this targeted covariance
check. All remaining arithmetic-row and terminal gates listed in
R011 and DO026 are retained.
