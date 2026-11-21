# DET-13: independent full-proof check

Date: 2026-11-21. Checker: GPT-6 Astra Pro; effort not exposed; TRACE_DET_20261121 /root/masullo_bridge_check.

## Result and scope

**PASS.** I read the complete 140-line version of paper_positive_kernel.tex and independently reconstructed every mathematical step. No substantive correction is required. I suggested making the atomic weights explicitly nonnegative; the parent reports adding that clarification, with no other proof change. No master or paper file was edited by this checker.

The theorem constructs a positive trace-class operator family from a nonlinear normalization of the actual rank-zero signed Gram scalar. It does not identify a measure producing the Xi determinant, does not use RH, and does not claim that the untransformed signed kernel is positive definite. The source theorem is already known: the new comparison is the exact normalization in the named signed determinant and its explicit ordinary Fredholm family.

The checks below use the paper's global convention that Hilbert inner products are conjugate-linear in the first argument and linear in the second. In particular the rank-one operator associated with a vector v is f ↦ v⟨v,f⟩.

## 1. Actual source normalization

I read the complete relevant definitions and proposition statements in:

- work/source_extra/Formalism/FormalDegreeBessel/StatementG.lean.
- The copy in work/external_lean/lean/src/Formalism/FormalDegreeBessel/StatementG.lean has identical bytes.
- The SHA256 of both copies is 6e89a4393d81afa0f93b3477f5b48ba4c7681c7ff067105ca2878cb9b338bd60.

This is a mathematical reading of definitions, not a Lean-build claim.

The source defines its auxiliary pairing by

\[
\operatorname{herm}(H;v,w)=w^*Hv.
\]

Thus its argument order differs from the paper's standard notation \(h(z,z')=z^*Hz'\). This does not produce a conjugation error in the claimed normalization: the source's Zhat uses herm with those arguments already reversed.

At \(r=0\), the ambient dimension is \(k+1\). The off-diagonal hyperbolic-block clauses in Hpk are empty and its middle block is

\[
H=\operatorname{diag}(I_k,-1).
\]

The support condition inWb is vacuous. The frame fvec has the single vector z. At \(g=1\), Zhat is the one-entry matrix

\[
[\operatorname{herm}(H;z',z)]=[z^*Hz']=[h(z,z')].
\]

Consequently its order-zero leading determinant is \(D_0=1\), and its order-one determinant is \(D_1=h(z,z')\). Also

\[
T_z=-\operatorname{Re}\operatorname{herm}(H;z,z)=-h(z,z)=T(z),
\]

since H is Hermitian. Substituting in the source definition of Gf gives exactly

\[
G_f(k,0;z,z';1)=|h(z,z')|^2-T(z)T(z')=S(z,z').
\]

The same identity follows by direct expansion of its two-vector Gram matrix:

\[
\det\begin{pmatrix}
-T(z)&h(z,z')\\
\overline{h(z,z')}&-T(z')
\end{pmatrix}
=T(z)T(z')-|h(z,z')|^2=-S(z,z').
\]

This checks the source sign \((-1)^{r+1}=-1\), including the empty-minor normalization. It requires neither an assumed general GGram theorem nor the more extensive Bessel representation hypotheses.

Every negative vector has nonzero last coordinate; dividing by that coordinate gives the unique representative \((x,1)\) with \(\|x\|<1\). In these coordinates,

\[
T(x,1)=1-\|x\|^2,\qquad
h((x,1),(y,1))=\langle x,y\rangle-1.
\]

The denominator cannot vanish, since \(|\langle x,y\rangle|\le\|x\|\|y\|<1\). Scaling either original vector multiplies both numerator and denominator of the quotient \(T(z)T(z')/|h(z,z')|^2\) by the same positive factor. Therefore

\[
\left(1+\frac{S(z,z')}{T(z)T(z')}\right)^{-a}
=\frac{(1-\|x\|^2)^a(1-\|y\|^2)^a}
 {|1-\langle x,y\rangle|^{2a}}
\]

is well defined on negative projective lines. Simultaneous U(k,1) invariance follows directly from preservation of h. All powers in this displayed formula are powers of strictly positive real quantities.

## 2. Primary theorem comparison

I extracted and read the relevant text directly from the cached primary PDF:

work/programme_sources/Neretin_MatrixBalls_0012220v2.pdf.

Its SHA256 is 76048931edbc809c855ba10c45cb75d6f79b8291e9904b05a01c9018c3318385. The primary identifier is [arXiv:math/0012220v2](https://arxiv.org/pdf/math/0012220v2).

Theorem 3.8, printed pp. 11–12, gives positivity of the holomorphic matrix-ball kernel for parameters \(0,1,\ldots,p-1\) or greater than \(p-1\). With \(p=1,q=k\), this includes every \(a>0\). Section 4.1, formula (4.1), takes the product with the conjugate kernel. Section 4.4, formulas (4.7)–(4.9), gives exactly the normalized numerator and denominator above, its invariance, and the corresponding unitary action. Interchanging the positive and negative blocks identifies the source's U(1,k) description with the paper's U(k,1) description.

The theorem is therefore cited with the correct rank-one parameter range and normalization. The proof below also independently establishes this rank-one positivity; it does not depend on a proof of the general matrix-ball classification.

## 3. Independent feature-space and positivity proof

Fix \(a>0\), let \(E=\ell^2(\mathbb N^k)\), and for a multi-index \(\alpha\) put

\[
c_\alpha=\frac{(a)_{|\alpha|}}{\alpha!}>0.
\]

The binomial series on the unit disc and the finite multinomial identity give

\[
\sum_{\alpha\in\mathbb N^k}c_\alpha\overline{x}^{\alpha}y^\alpha
=(1-\langle x,y\rangle)^{-a}.
\]

The complex power here is the analytic branch given by that series, normalized to one at zero. Absolute convergence follows from

\[
\sum_j|x_jy_j|\le\|x\|\|y\|<1.
\]

In particular, evaluating at \(y=x\) shows that

\[
u_x=(1-\|x\|^2)^{a/2}
      (\sqrt{c_\alpha}\,x^\alpha)_\alpha
\]

belongs to E and has norm one. Its inner product is

\[
\langle u_x,u_y\rangle=
\frac{(1-\|x\|^2)^{a/2}(1-\|y\|^2)^{a/2}}
 {(1-\langle x,y\rangle)^a}.
\]

For the conjugate Hilbert space, \(\langle\overline{u_x},\overline{u_y}\rangle=\overline{\langle u_x,u_y\rangle}\). Thus

\[
v_x=u_x\otimes\overline{u_x},\qquad
\|v_x\|=1,\qquad
\langle v_x,v_y\rangle=
|\langle u_x,u_y\rangle|^2=F_a(x,y).
\]

The exponents are correct: tensoring the normalized holomorphic feature with its conjugate doubles the denominator exponent and turns each numerator exponent \(a/2\) into a.

For arbitrary finite scalars \(d_1,\ldots,d_N\),

\[
\sum_{i,j}\overline{d_i}d_j F_a(x_i,x_j)
=\left\|\sum_jd_jv_{x_j}\right\|^2\ge0.
\]

This proves positive definiteness in the usual kernel sense. It also proves \(0<F_a(x,y)\le1\), with \(F_a(x,x)=1\). The closed span \(\mathcal H_a\) of these vectors is separable because it is a closed subspace of the separable Hilbert tensor product \(E\otimes\overline E\).

The coordinate formula makes \(F_a\) continuous, and it is real and symmetric. Hence

\[
\|v_x-v_y\|^2=2-2F_a(x,y)
\]

proves norm continuity of the feature map.

For g in U(k,1), define \(U_gv_x=v_{gx}\) and extend linearly on finite spans. Invariance of the kernel preserves every squared norm, so relations are preserved and the assignment is well defined. Its inverse on this dense span is \(U_{g^{-1}}\). It therefore extends to a unitary operator on \(\mathcal H_a\), and the group law follows on the spanning vectors. The representation is strongly continuous as well: continuity first holds on each \(v_x\), then on finite spans, and finally on their completion by the uniform unitary norm bound.

For a fixed negative line \(x_0\), the group function \(g\mapsto F_a(x_0,gx_0)=\langle v_{x_0},U_gv_{x_0}\rangle\) is consequently a continuous unitary matrix coefficient. No projective-representation ambiguity remains.

## 4. Strong measurability, Bochner integral and finite-rank approximation

Define \(P_xf=v_x\langle v_x,f\rangle\). With the stated convention this is linear in f, selfadjoint, positive, rank one, and satisfies

\[
P_x^2=P_x,\qquad \|P_x\|_1=\operatorname{Tr}P_x=1.
\]

For vectors u and v the rank-one identity gives

\[
P_u-P_v=(u-v)\langle u,\cdot\rangle+
v\langle u-v,\cdot\rangle,
\]

so

\[
\|P_u-P_v\|_1
\le(\|u\|+\|v\|)\|u-v\|.
\]

Applied to unit feature vectors, this is the stated bound \(2\|v_x-v_y\|\). Thus \(x\mapsto P_x\) is trace-norm continuous. It is strongly measurable: the domain is separable, its continuous image is separable, and its values lie in the Banach space \(\mathcal S_1(\mathcal H_a)\). Equivalently, the compact partitions described next explicitly supply strongly measurable simple approximations. The measure can be completed for the usual Bochner definition without changing any integral.

For a finite positive Radon measure \(\nu\), the integrability condition is exact:

\[
\int\|P_x\|_1\,d\nu(x)=\nu(\mathbb B^k)=:M<\infty.
\]

Therefore \(T=\int P_x\,d\nu(x)\) exists as an \(\mathcal S_1\)-valued Bochner integral. Bounded evaluation on a fixed vector gives

\[
\langle f,Tf\rangle=\int|\langle v_x,f\rangle|^2\,d\nu(x)\ge0.
\]

The trace is a bounded linear functional on \(\mathcal S_1\), so it passes through the integral:

\[
\operatorname{Tr}T=\int\operatorname{Tr}P_x\,d\nu=M.
\]

In particular \(\|T\|_1=M\); positivity, trace class, and the exact trace are all proved.

For a direct construction on the same Hilbert space, choose compact sets \(K_j\) whose omitted masses tend to zero. Such sets follow from finite Radon regularity; here an exhaustion by closed balls of radii tending to one also works. On \(K_j\), trace-norm continuity is uniform. Cover \(K_j\) by finitely many sets of sufficiently small diameter, refine to a finite Borel partition \(E_{j,l}\), and choose a representative \(x_{j,l}\) in each nonempty cell. Then

\[
T_j=\sum_l\nu(E_{j,l})P_{x_{j,l}}
\]

is positive and finite rank in \(\mathcal H_a\), and

\[
\|T-T_j\|_1
\le\nu(\mathbb B^k\setminus K_j)
+\sum_l\nu(E_{j,l})
 \sup_{x\in E_{j,l}}\|P_x-P_{x_{j,l}}\|_1\longrightarrow0.
\]

The supremum in the second term can be chosen uniformly smaller than any prescribed tolerance, and the sum of its weights is at most M. This justifies the approximation without compactness of the entire open ball and without operator-valued integration of an unbounded family.

Kernel invariance alone does not make this arbitrary finite-measure frame operator invariant: that would require appropriate invariance of the measure. The paper does not assert such operator invariance.

## 5. Independent Fredholm principal-minor series proof

Let \(Q_m\) be increasing orthogonal projections onto finite spans of an orthonormal basis of \(\mathcal H_a\). Put \(T_m=Q_mTQ_m\). Then

\[
T_m=\int P_{Q_mv_x}\,d\nu(x).
\]

The general rank-one estimate above gives

\[
\|P_{v_x}-P_{Q_mv_x}\|_1
\le2\|v_x-Q_mv_x\|\longrightarrow0.
\]

Its right side is bounded by two. Dominated convergence proves \(\|T-T_m\|_1\to0\). This explicitly verifies the compression step even though \(Q_mv_x\) need not have unit norm.

For \(n\le m\), choose n coordinate indices I in the compressed space and let \(z_I(x)\) be the corresponding coordinate vector of \(Q_mv_x\). The associated principal minor of \(T_m\) is the determinant of the matrix of integrals \(\int z_I(x)z_I(x)^*\,d\nu(x)\). Expanding the determinant and symmetrizing the n independent integration variables proves

\[
\det\left(\int z_I(x)z_I(x)^*\,d\nu(x)\right)
=\frac1{n!}\int
 \left|\det[z_I(x_1)\ \cdots\ z_I(x_n)]\right|^2\,d\nu^n.
\]

There are only finitely many terms in this expansion, all bounded and integrable because the feature vectors have norm at most one and \(\nu\) is finite. Thus every application of scalar Fubini is justified. The \(n!\) factor comes from the n-variable permutation symmetrization, and no additional normalization factor is present.

Sum over I and apply the finite Cauchy–Binet formula. This yields

\[
\operatorname{Tr}(\Lambda^nT_m)
=\frac1{n!}\int
\|Q_mv_{x_1}\wedge\cdots\wedge Q_mv_{x_n}\|^2\,d\nu^n
=\frac1{n!}\int
\det[\langle Q_mv_{x_i},Q_mv_{x_j}\rangle]\,d\nu^n.
\]

For \(n>m\) both sides are zero. Exterior powers are equipped with the usual Hilbert norm in which wedges of distinct orthonormal basis vectors are orthonormal.

For each fixed tuple and n, strong convergence of \(Q_m\) gives convergence of its Gram matrix, hence of its determinant, to \(\det[F_a(x_i,x_j)]\). Gram positivity and Hadamard's inequality give the uniform bound

\[
0\le\det[\langle Q_mv_{x_i},Q_mv_{x_j}\rangle]
\le\prod_i\|Q_mv_{x_i}\|^2\le1.
\]

Consequently dominated convergence identifies the limiting nth coefficient with

\[
\frac1{n!}\int\det[F_a(x_i,x_j)]\,d\nu^n.
\]

The finite determinant expansions have the uniform termwise majorant

\[
\frac{|w|^n M^n}{n!},
\]

whose sum is \(e^{|w|M}\). This controls the series tails uniformly on compact w-discs, so it justifies interchanging the compression limit and determinant series. Trace-norm determinant continuity, as established in DET-05, identifies that limit with the ordinary Fredholm determinant of T. Therefore the full displayed formula in DET-13 is correct, with absolute locally uniform convergence. The \(n=0\) term uses the usual empty Gram determinant one.

## 6. Finite atomic determinant

Let \(\nu=\sum_{j=1}^Nb_j\delta_{x_j}\) with \(b_j\ge0\). Define \(V:\mathbb C^N\to\mathcal H_a\) by \(Ve_j=\sqrt{b_j}v_{x_j}\). With the conjugate-first convention,

\[
(V^*f)_j=\sqrt{b_j}\langle v_{x_j},f\rangle,
\qquad
(V^*V)_{ij}=\sqrt{b_ib_j}\langle v_{x_i},v_{x_j}\rangle.
\]

Thus \(VV^*=T\), and \(V^*V\) is precisely the matrix with entries \(\sqrt{b_ib_j}F_a(x_i,x_j)\). Restrict V to its finite-dimensional range and use the equality of the nonzero spectra of \(VV^*\) and \(V^*V\), or the finite Sylvester determinant identity. It follows that

\[
\det_{\mathcal H_a}(I-wT)
=\det_{\mathbb C^N}
 [\delta_{ij}-w\sqrt{b_ib_j}F_a(x_i,x_j)].
\]

No distinctness or positive lower bound on the weights is required. Zero weights and repeated points merely introduce additional zero eigenvalues, whose determinant factors are one.

## 7. Necessary first and second trace conditions

The product \((x,y)\mapsto P_xP_y\) is trace-norm continuous and

\[
\|P_xP_y\|_1\le\|P_x\|_1\|P_y\|\le1.
\]

It is therefore Bochner integrable against the finite product measure. Bilinearity and continuity of multiplication, first for simple approximations and then in trace norm, give

\[
T^2=\iint P_xP_y\,d\nu(x)d\nu(y).
\]

The trace passes through this absolutely integrable product, and a direct rank-one trace calculation gives

\[
\operatorname{Tr}(P_xP_y)
=\langle v_x,v_y\rangle\langle v_y,v_x\rangle
=|\langle v_x,v_y\rangle|^2=F_a(x,y)^2.
\]

The last equality is valid because this particular normalized kernel is real and nonnegative. Consequently

\[
\operatorname{Tr}T^2=\iint F_a(x,y)^2\,d\nu(x)d\nu(y).
\]

If its entire determinant equals \(G(w)=\det(I-wB)\), equality of the linear coefficient forces \(\operatorname{Tr}T=\operatorname{Tr}B\). Equality of the quadratic coefficient

\[
\tfrac12[(\operatorname{Tr}T)^2-\operatorname{Tr}T^2]
\]

then forces \(\operatorname{Tr}T^2=\operatorname{Tr}B^2\). Equivalently, compare the first two coefficients of the analytic logarithm of the determinants near zero. Thus both necessary equations stated in the final paragraph are correct. Higher exterior coefficients must also agree. These are restrictions on the still-unselected measure, not an established spectral identification.

## Final disposition

Every substantive claim in DET-13 survives the independent check: exact signed-source normalization, all \(a>0\), global conjugation conventions, separable feature space, continuity and unitary action, finite-measure Bochner integration, positive common-space finite-rank approximation, principal-minor Fredholm series, exact atomic determinant and the necessary second-trace equation.

The only suggested clarification was \(b_j\ge0\), reported applied by the parent. No further correction or missing operator bound was found. The known Berezin positivity is properly attributed; no proof of RH or historical/arithmetic identification follows merely from constructing this family.
