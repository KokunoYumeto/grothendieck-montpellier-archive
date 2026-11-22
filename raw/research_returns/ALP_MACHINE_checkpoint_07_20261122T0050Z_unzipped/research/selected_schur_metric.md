# AM-R-011: the selected Schur norms, their row normalization, and a finite projection denominator

Author: /root, GPT-6 Astra Pro, ALP_MACHINE, 21 November 2026 UTC.

This result inserts the **actual selected partitions** of AM-DO-025
into the Fischer metric and the coefficient normalization used by the
recovered source. It computes a concrete part of the archimedean cost,
and a valid integral denominator for projection onto a fixed finite
polynomial component. It does not identify that denominator with the
least denominator of the source row map, or compute a full DP44 gain.

## 1. The two partitions that must be distinguished

At one selected CM embedding use the notation of AM-DO-025:

\[
 a=N_j,\quad b=N_{j+1}=a+d,\quad
 w_j=\operatorname{lamTrue}_j,\quad
 \nu_j=w_j+e_j-\frac b2\mathbf1_a.
 \tag{R11.1}
\]

The source coefficient representation uses the partition obtained by
removing the final weight:

\[
 \eta_j=w_j-w_{j,a-1}\mathbf1_a,
 \qquad q_j=\nu_{j,a-1}.
 \tag{R11.2}
\]

Thus \(\eta_j\) is literally `DomWeight.natW`, and
\(w_{j,a-1}\) is `detShift`. AM-DO-025 proves \(q_j\ge1\)
and \(\nu_j\) is an integral partition. Consequently

\[
 \boxed{\nu_j=\eta_j+q_j\mathbf1_a,
 \qquad \eta_{j+1}=(\nu_j,0^d).}
 \tag{R11.3}
\]

For the second identity, the last block of the next weight has value
\(-e_j+a/2\). Every old entry exceeds that value by
\(\nu_{j,i}>0\), by the exact recurrence in AM-DO-025.
Subtracting the last entry therefore leaves precisely the displayed
partition. This proves (R11.3) from the actual weights, without
choosing a different representation. The partition \(\eta_j\)
describes the row coefficient metric; \(\nu_j\) describes the
homogeneous kernel polynomial. They generally have different degrees.

For a partition \(\lambda\), put

\[
 H_\lambda=\prod_{(i,l)\in\lambda}
       (\lambda_i-l+\lambda_l'-i+1),\qquad H_\varnothing=1.
 \tag{R11.4}
\]

These are ordinary hook products, not the DP44 height constant \(H\).
Trailing zero rows do not change them.

## 2. The normalized Fischer calculation

On a complex \(b\)-by-\(a\) matrix variable \(Z\), use the
Fischer inner product with distinct monomials orthogonal and

\[
 \|Z^\alpha\|_{\rm F}^2=\alpha!.
 \tag{R11.5}
\]

For \(\lambda_1\ge\cdots\ge\lambda_a\ge0\), let
\(\lambda_{a+1}=0\), and define the primitive polynomial

\[
 p_\lambda(Z)=\prod_{r=1}^a
       \det(Z_{[1,r],[1,r]})^{\lambda_r-\lambda_{r+1}}.
 \tag{R11.6}
\]

Its leading diagonal monomial has coefficient one. In particular it
is primitive in the ordinary integral monomial lattice. The exact norm is

\[
                         \boxed{\|p_\lambda\|_{\rm F}^2=H_\lambda.}
 \tag{R11.7}
\]

Here is a short derivation fixing the normalization, rather than a
new proof of Schur--Weyl duality. Let \(D=|\lambda|\), and let
\(f_\lambda\) be the dimension of the corresponding symmetric-group
representation. Schur--Weyl duality and the hook formula give
\(D!/f_\lambda=H_\lambda\). The exact references are Fulton
and Harris (1991), Theorem 6.3(2)--(4), pp.77--78; Hook Length
Formula 4.12, p.50; and the rectangular Cauchy decomposition in
Exercise 6.11(b), p.80. These results are cited, not re-proved.

Choose the standard unitary metrics on the Schur modules, with
highest vectors of norm one, compatible under the standard
isometric inclusion \(\mathbf C^a\subset\mathbf C^b\).
The degree-\(D\) Fischer reproducing kernel satisfies

\[
 \begin{aligned}
 \frac{(\operatorname{tr}(ZW^*))^D}{D!}
 &=\sum_{|\lambda|=D}\frac{f_\lambda}{D!}
                  \operatorname{tr}(S_\lambda(Z)S_\lambda(W)^*)\\
 &=\sum_{|\lambda|=D}\frac1{H_\lambda}
       \sum_{r,s}p_{rs}^\lambda(Z)\overline{p_{rs}^\lambda(W)}.
 \end{aligned}
 \tag{R11.8}
\]

The first equality is the trace of \((ZW^*)^{\otimes D}\)
under the cited tensor decomposition. Functoriality and the unitary
metrics give \(S_\lambda(W^*)=S_\lambda(W)^*\); this also follows
from singular-value decomposition and the diagonal action on weights.
The second equality expands the trace in orthonormal bases.
The matrix coefficients \(p_{rs}^\lambda\) are linearly independent
and exhaust the Cauchy summand. Comparison with the reproducing
kernel therefore gives their common squared norm \(H_\lambda\)
and their orthogonality. The highest-to-highest coefficient is
(R11.6): both are highest vectors and evaluate on a diagonal
matrix as \(\prod_i z_i^{\lambda_i}\), with coefficient one.
This proves (R11.7), including its scalar.

## 3. The determinant insertion has an exact scalar

Let \(V_\eta\) be the irreducible compact coefficient module
realized as the row orbit of \(p_\eta\) in square \(a\)-by-\(a\)
polynomials. Multiplication by the full determinant gives

\[
 M_q:V_\eta\longrightarrow V_{\eta+q\mathbf1_a},
                         \qquad f\longmapsto(\det Z)^q f.
 \tag{R11.9}
\]

This is an integral polynomial map. On \(U(a)\), it intertwines
the two representations after the unitary determinant twist. Hence
its pulled-back Fischer form is a scalar multiple of the invariant
form on \(V_\eta\). Evaluating on the highest vector and using
(R11.7) proves, for every \(f\in V_\eta\),

\[
 \boxed{\|M_qf\|_{\rm F}^2
      =\frac{H_{\eta+q\mathbf1_a}}{H_\eta}\|f\|_{\rm F}^2.}
 \tag{R11.10}
\]

The ratio has the explicit integral product

\[
 \frac{H_{\eta+q\mathbf1_a}}{H_\eta}
       =\prod_{i=1}^{a}\frac{(\eta_i+q+a-i)!}{(\eta_i+a-i)!}
       =\prod_{i=1}^{a}\prod_{r=1}^{q}(\eta_i+a-i+r).
 \tag{R11.11}
\]

Indeed the factorial/Vandermonde expression for the hook product
has the same Vandermonde denominator before and after the uniform
shift by \(q\). Cancelling it gives (R11.11). This is also the
hook-product expression directly used in the recovered source
`Divisibility/RecBridgeNum.lean`, theorem `logHook_eq`,
lines149--188. The displayed ratio is strictly positive.

The source defines its row metric as Fischer divided by the squared
Fischer norm of its extremal vector: `DataCoeff.lean`,
`normFock`, lines83--84, and `HermitianForms/IsLocBasis.lean`,
`nfAll`, lines19--20. Thus on the actual row partition it is

\[
             \|f\|_{\mathrm{row},j}^2
                         =\|f\|_{\rm F}^2/H_{\eta_j}.
 \tag{R11.12}
\]

Combining (R11.10) and (R11.12), the selected determinant insertion
has squared Fischer norm \(H_{\nu_j}\|f\|_{\mathrm{row},j}^2\).
In normalized coefficient metrics it is an isometry. This last
assertion concerns the coefficient map (R11.9); it is not a
theta-operator isometry or an identity between automorphic measures.

In particular its hook ratios obey the exact cancellation

\[
 \boxed{\prod_{j=0}^{m-1}\frac{H_{\nu_j}}{H_{\eta_j}}
              =\frac{H_{\eta_m}}{H_{\eta_0}}.}
 \tag{R11.13}
\]

This follows from (R11.3). It prevents counting the same row-metric
normalization repeatedly as an independent loss. No finite
projection denominator, class mass, branch map, theta value, or
DP44 term is asserted to cancel by (R11.13).

## 4. Actual common-host Fock norm

On \(E'=\mathbf Q(\zeta_{28})\), use the exact period and
coordinates of AM-R-009. Each of the six coordinates is
\(w_i^+=u_i+iv_i\) or \(w_i^-=u_i-iv_i\), and the actual
creation operator is the one read by \(\partial/\partial w_i^\pm\).
The monomial creation norm relative to the unit Gaussian is
\(\alpha!(\pi/(2G_i))^{|\alpha|}\). This is the explicit
orthogonal coordinate change in AM-R-009, retaining the factor
\(1/2\) in each derivative. Let \(i(\tau)\in\{1,2,3\}\)
name the underlying Jacobian coordinate of \(\tau\).

For a selected partition \(\nu_{j,\tau}\) at every real place,
set \(D_{j,\tau}=|\nu_{j,\tau}|\). The tensor product of the
primitive highest polynomials (R11.6), applied to the **actual**
Gaussian, has exact squared archimedean norm

\[
 \boxed{\|\phi_j^{\mathrm{hw}}\|_\infty^2
  =\det(2Y)^{-ab}
       \prod_{\tau\in\Phi'}
       H_{\nu_{j,\tau}}
       \left(\frac{\pi}{2G_{i(\tau)}}\right)^{D_{j,\tau}}.}
 \tag{R11.14}
\]

There are \(ab\) copies of \(A=J^2\), so the squared vacuum
norm is \(\det(2Y)^{-ab}\). At a fixed CM place all matrix
entries have the same creation scale; homogeneity supplies its
degree power and (R11.7) supplies its hook product. The CM
coordinate blocks are orthogonal. These three facts prove
(R11.14). Its square root is the norm, and its logarithm is

\[
 -\frac{ab}{2}\log\det(2Y)
   +\frac12\sum_\tau\left[
      \log H_{\nu_{j,\tau}}+
      D_{j,\tau}\log\frac{\pi}{2G_{i(\tau)}}\right].
 \tag{R11.15}
\]

The corresponding analytic-to-algebraic kernel still has period
\(C^{2ab}\), by AM-DO-026. Unit normalization divides that
kernel by the square root of (R11.14), and does not delete the
period. Finite-vacuum norm one was used only for the unmoved
standard vector; an additional finite linear combination retains
its actual finite norm. A compact coefficient isometric embedding
also retains the source Schur factor \(1/\dim V_{\eta_j}\) in
Haar integration, as proved in AM-DO-026.

## 5. A finite-degree integral projection bound

Let
\(L_D=\operatorname{Sym}^D(\mathbf Z^b\otimes(\mathbf Z^a)^*)\)
be the ordinary integral polynomial lattice. Let \(E_\lambda\)
be the rational projector onto its Cauchy component of shape
\(\lambda\), and let
\(L_\lambda=L_D\cap\operatorname{im}(E_\lambda)\).
Then

\[
 \boxed{L_\lambda\subset E_\lambda L_D
                \subset H_\lambda^{-1}L_\lambda.}
 \tag{R11.16}
\]

To prove this without assuming integral semisimplicity, start on
the tensor power
\((\mathbf Z^b)^{\otimes D}\otimes((\mathbf Z^a)^*)^{\otimes D}\).
Act on its first factor by the central symmetric-group idempotent

\[
 e_\lambda=\frac{f_\lambda}{D!}
             \sum_{\sigma\in S_D}\chi_\lambda(\sigma^{-1})\sigma
       =\frac1{H_\lambda}
             \sum_{\sigma\in S_D}\chi_\lambda(\sigma^{-1})\sigma.
 \tag{R11.17}
\]

The characters of the symmetric group are integers, and the
central numerator commutes with the simultaneous permutation of
both tensor factors. It therefore descends to the integral
coinvariant quotient \(L_D\). Its denominator divides
\(H_\lambda\). Over \(\mathbf Q\), Schur--Weyl duality identifies
the descended operator with exactly the stated Cauchy projector.
Hence \(H_\lambda E_\lambda L_D\subset L_\lambda\).
Conversely it fixes every vector of \(L_\lambda\), proving the
other inclusion in (R11.16).

At a prime \(p\), the possible saturation quotient is consequently
killed by \(p^{v_p(H_\lambda)}\); its length is at most
\(\operatorname{rank}(L_\lambda)v_p(H_\lambda)\). If every hook
is a \(p\)-unit, the projection is integral and split. In
particular \(p>\lambda_1+a-1\) suffices. This is an explicit
upper bound for one projector, not a least-denominator formula.
The source's particular Weyl/dual-Weyl lattice can admit a
strictly better comparison. For example multiplication by
\((\det Z)^q\) is already integral, so a large uniform shift
does not by itself force the denominator bound in (R11.17)
to be attained on that determinant-inserted submodule.

This finite-degree statement is consistent with AM-K019. It makes
no assertion about a lattice simultaneously stable under all
ordinary differential powers. Nor does a bound for a projector
prove that the theta jet matrix on its image has a prescribed
content or that a prescribed automorphic row belongs to that image.

## 6. A concrete source-rank illustration

Take the smallest displayed rank choice \(k=6,m=2,t=13,d=14\),
and saturate only the `HCParam` gaps as in AM-DO-025. Then

\[
 N_0=6,\quad N_1=20,\quad N_2=34,\qquad
 \nu_0=(1^6),\quad \nu_1=(3^6,2^{14}),
 \quad D_0=6,\quad D_1=46.
 \tag{R11.18}
\]

The row partitions are \(\eta_0=0\),
\(\eta_1=(1^6,0^{14})\), and
\(\eta_2=(3^6,2^{14},0^{14})\).
Thus \(H_{\nu_0}=6!=720\), and the second determinant
insertion ratio is

\[
 \frac{H_{\nu_1}}{720}
 =\prod_{i=1}^{20}\prod_{r=1}^{2}
                        (\eta_{1,i}+20-i+r).
 \tag{R11.19}
\]

All integers, prime valuations and the product identity for this
example are reproduced by `selected_schur_metric_certificate.py`.
The small-polynomial checks there also expand (R11.6) in ordinary
monomials and compare its exact Fischer norm to (R11.4); they are
finite checks of normalization, not the proof of the general formula.
The rank choice and gaps satisfy the conditions named here. No
claim is made that they satisfy all the further noncompact `Hyp3`
conditions or already form a nonzero global chain.

## 7. Framework and retained arithmetic gate

The polynomial lattices and determinant maps are defined over
\(\mathbf Z\); the rational projector in (R11.17) specifies
exactly which primes need inverting for that chosen splitting.
The associated Schur operations live in the representation
Grothendieck ring and the special lambda-ring formalism of SGA6,
Exposé V. The actual normalized metric and (R11.16) are stronger
data than an equality of virtual classes. The representation ring
is related to the flag construction by SGA6, Exposé VI, Theorem3.3,
with the carried-source qualification in the geometric dictionary.
The CM eigenspace splitting is the diagonalizable-group grading of
SGA3, Exposé I, Proposition4.7.3. The period in (R11.14) remains
the line-bundle metric of the Picard/theta construction, placed in
FGA232 Theorem3.1 and SGA7 I VII2.7/2.9 in that dictionary.

For DP_MULT Q3e these formulas supply the selected homogeneous
degrees, an exact archimedean creation norm and its relation to the
source's row metric. To produce actual \(g_j,e_j,H\), the next
required data are still the allowed finite jet matrix on these
partitions, its integral row realization, the actual nonzero
iteration and the endpoint detector. The separate logarithmic
quantities in (R11.15), (R11.16) and the class mass cannot simply
be added as independent losses without checking the source maps:
(R11.13) exhibits one exact normalization cancellation already.

### References and source locators

- Fulton, W., & Harris, J. (1991). *Representation theory: A first
  course*. Springer. Hook Length Formula4.12, p.50;
  Theorem6.3(2)--(4), pp.77--78; Exercise6.11(b), p.80.
  The cited theorem statements and formulas were directly read.
- Alpöge source, pinned commit recorded in the source audit:
  `Formalism/LocalRingCardinality/DataCoeff.lean`, `detShift`,
  `natW`, `extremal`, `normFock` and `normFockQ`, lines21--23,
  55--56 and83--87; `Formalism/LocalToGlobal/HermitianForms/IsLocBasis.lean`,
  `nfAll`, lines19--20; `Formalism/LocalToGlobal/Divisibility/RecBridgeNum.lean`,
  `logHook_eq`, lines149--188. These files were directly read.
- AM-DO-025, (DO25.5)--(DO25.17); AM-DO-026,
  (DO26.7)--(DO26.8) and (DO26.17)--(DO26.20);
  AM-R-009, corrected actual Gaussian norm; AM-K019,
  the full differential-module obstruction with its exact scope.

Whole-proof check events are recorded separately. No Lean execution
or automatic proof verification is asserted.
