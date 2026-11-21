# MAS-10: closing the actual quotient trace-ideal gate by a Green operator

Run **TRACE_DET_20261121**, 21 November 2026. Author/checker `/root/step1_history_route`; GPT-6 Astra Pro (inherited developer label), effort setting not exposed. The proof was developed independently of the heat-integral trace-norm route and checked against root's and `/root/masullo_bridge_check`'s separate calculations.

## Outcome and dependencies

**The ordinary trace-class gate closes.** In the actual weighted Hilbert quotient, a shifted Green operator is sectorial. Completeness of the draft's full spectral jets then makes the real part of that Green operator positive with a finite orthonormal diagonal sum. This proves trace class without assuming a Riesz basis, uniformly bounded biorthogonal vectors, orthogonality of zero modes, or any small-time heat trace-norm estimate.

The proof needs the full spectral annihilator description in **Masullo, Theorem10.2.2.1, equations(10.2.2.4)–(10.2.2.6), PDFp.446**, with the weighted quotient of Definition10.1.1.1/(10.2.2.1). Choose alpha=1/2, so the classical strict critical strip contains every nontrivial zero in its interior. **RH is not used.** Nor is Theorem10.3.2.1, the asserted nuclearity theorem, used. The conclusion is conditional only on the spectral-quotient claim of the draft, together with the classical zeta facts already stated. This strengthens the initially checked version that used RH and a narrower strip.

The Green construction below gives an actual bounded operator on the theta quotient and proves it trace class. Its even part has the ordinary determinant Ξ(sqrt(w))/Ξ(0), with full multiplicity. Equality of determinants does not give a unitary identification with the diagonal B, and it does not establish positivity in the actual quotient metric.

## 1. Precise setup

Fix F=Q, a=1/2 and the trivial character of the compact norm-one idele class group. Choose

\[
\alpha=1/2,\qquad s>1,\qquad
w(u)=e^{2\alpha|u|}(1+u^2)^{s/2},\qquad
H=L^2(\mathbb R,w(u)\,du).
\]

The compact Haar factor is normalized to have mass1. Let V be the closed theta-image subspace in this radial sector, and let E=H/V, with its actual Hilbert quotient norm. In the draft's notation this is the relevant isotype of H^s_{Q,1/2,[-1/2,1/2]}.

Let rho range over the distinct nontrivial zeros of zeta, with multiplicity N_rho, and put z_rho=rho−1/2. Classically 0<Re(rho)<1, and xi(1/2) is nonzero. Thus |Re(z_rho)|<1/2 and z_rho is nonzero. The strict-strip assertion follows from the Euler product, the functional equation, and the classical zero-free line Re(s)=1; an exact locator for the latter is Titchmarsh, second edition, §3.2, pp46–47, together with §2.12 for reflection. No RH is invoked. Symmetry gives N_(1−rho)=N_rho and z_(1−rho)=−z_rho.

The claimed full spectral-annihilator theorem says that the continuous linear functionals

\[
\ell_{\rho,m}(f)=\int_{\mathbb R}f(u)e^{z_\rho u}u^m\,du,
\qquad 0\le m<N_\rho,
\]

annihilate V and their linear span is norm dense in the Hilbert dual E'. Equivalently, their Riesz representatives have dense span in V-perp. Every zero is interior to the chosen strip. The endpoints0,1 are not zeros of the completed xi function, and the meromorphic zeta pole at1 is not a zero, so no boundary cap enters. For each fixed rho and m, continuity follows from

\[
\int_{\mathbb R}e^{2\operatorname{Re}(z_\rho)u}|u|^{2m}w(u)^{-1}\,du<\infty.
\]

The standard zero count, already used in B-01, gives

\[
\sum_\rho N_\rho(1+|\operatorname{Im}\rho|^2)^{-1}<\infty.
\]

No uniform bound on N_rho, no zero separation and no simplicity assumption is made.

## 2. Bounded translations and the Green operator on the ambient space

Put

\[
b(u)=\tfrac12(\log w)'(u)
=\alpha\operatorname{sgn}(u)+\frac{s u}{2(1+u^2)}
\quad\text{a.e.},\qquad B_0=\alpha+s/4.
\]

Then |b(u)|≤B0. The function log(sqrt(w)) is globally B0-Lipschitz. For translations T_v f(u)=f(u−v),

\[
\|T_v f\|_H\le e^{B_0|v|}\|f\|_H.
\]

Translations are strongly continuous: this holds first on compactly supported smooth functions by local uniform bounds on the weight, and then on H by density and the displayed uniform bound for v near0.

The jet formula is

\[
\ell_{\rho,m}(T_v f)
=e^{z_\rho v}\sum_{j=0}^m {m\choose j}v^{m-j}\ell_{\rho,j}(f).
\]

It follows either from the draft's invariance statement or directly from the complete annihilator description that T_vV is contained in V for every real v. The integral formula is absolutely justified by the continuity of the jets and the exponential weight; substitution u=x+v proves it first for compactly supported functions, then for H by continuity.

Choose a real **shift parameter μ>B0**, distinct from the fixed centering parameter a=1/2. Define

\[
g_\mu(v)=\frac{e^{-\mu|v|}}{2\mu},\qquad
K_\mu f=\int_{\mathbb R}g_\mu(v)T_v f\,dv.
\]

This is a vector-valued Bochner integral for each f in H. It is not asserted to be a Bochner integral with values in the operator-norm space B(H). Since

\[
\int_{\mathbb R}|g_\mu(v)|e^{B_0|v|}\,dv<\infty,
\]

it defines a bounded operator. It preserves V because each integrand belongs to V when f does and V is closed. Denote the induced quotient operator by K, identifying E isometrically with V-perp:

\[
K=P_{V^\perp}K_\mu|_{V^\perp}.
\]

### Weak derivatives and the cusp at zero

The kernels gμ and gμ' both belong to the same exponentially weighted L1 space, and their distributional identity is

\[
g_\mu''=\mu^2g_\mu-\delta_0.
\]

Consequently, if y=Kμf, then y,y',y'' belong to H, with y''=μ²y−f in the distributional sense. For example, this follows first on compactly supported smooth f; weighted convolution bounds then pass to limits in H and in distributions. Thus Kμ is a right inverse for μ²−d²/du² on its natural maximal weighted domain.

Let U:H→L²(R) be the unitary map Uy=sqrt(w)y, and put h=Uy. Then h belongs to H¹(R), and

\[
U y'=h'-bh=:Dh,\qquad
D=\partial_u-b.
\]

Since y' and y'' belong to H, Dh also belongs to H¹(R), and

\[
U y''=D^2h.
\]

No derivative of b is needed. In particular the jump of b at0, inherited from |u|, does not invalidate the calculation. The conditions h in H¹ and Dh in H¹ precisely justify the integrations by parts below.

## 3. The numerical range is contained in a fixed sector

For h as above, the H¹ integration-by-parts identity gives

\[
\langle(\mu^2-D^2)h,h\rangle
=\|h'\|_2^2+\mu^2\|h\|_2^2-\|bh\|_2^2
+\langle h',bh\rangle-\langle bh,h'\rangle.
\]

Either standard inner-product convention gives the same real part and absolute imaginary part. Set δ=μ²−B0²>0 and c=B0/sqrt(δ). Then

\[
\operatorname{Re}\langle(\mu^2-D^2)h,h\rangle
\ge\|h'\|_2^2+\delta\|h\|_2^2,
\]

and

\[
\left|\operatorname{Im}\langle(\mu^2-D^2)h,h\rangle\right|
\le2B_0\|h'\|_2\|h\|_2
\le c\bigl(\|h'\|_2^2+\delta\|h\|_2^2\bigr).
\]

The last step is 2XY≤X²+Y² applied with X=||h'|| and Y=sqrt(δ)||h||. Thus the absolute imaginary part is at most c times the real part.

For arbitrary f in H, take y=Kμf. Since (μ²−d²/du²)y=f, the preceding calculation shows

\[
\operatorname{Re}\langle K_\mu f,f\rangle\ge0,
\qquad
|\operatorname{Im}\langle K_\mu f,f\rangle|
\le c\operatorname{Re}\langle K_\mu f,f\rangle.
\]

Indeed <Kμf,f> is the conjugate of <(μ²−d²)y,y>, so its real part and absolute imaginary part are unchanged. Compression to V-perp preserves these inequalities because <PKμx,x>=<Kμx,x> there. Hence the **actual quotient K** has the same sector bound. Its adjoint K* has the same symmetric sector bound as well.

This step is what supplies information about singular values. Mere summability of the spectrum would not suffice.

## 4. The complete spectral jets give an orthonormal triangular basis

For |Re(z)|<mu, direct integration gives

\[
F_\mu(z)=\int_{\mathbb R}g_\mu(v)e^{zv}\,dv
=\frac1{\mu^2-z^2}.
\]

The translation formula and the vector-valued integral imply on the dual jets

\[
K'\ell_{\rho,m}
=\sum_{j=0}^m {m\choose j}
F_\mu^{(m-j)}(z_\rho)\ell_{\rho,j}.
\]

The integrals and derivatives converge absolutely because |Re(z_rho)|<alpha<mu and the kernel has exponential decay. Write

\[
\lambda_\rho=F_\mu(z_\rho)=\frac1{\mu^2-z_\rho^2}.
\]

These numbers need not be real. If z_rho=b+it, then the real part of the denominator is A_rho=mu²−b²+t²>0. Consequently

\[
\operatorname{Re}\lambda_\rho
=\frac{A_\rho}{A_\rho^2+4b^2t^2}>0,
\quad
|\lambda_\rho|\le\frac1{\mu^2-\alpha^2+t^2},
\quad
\sum_\rho N_\rho|\lambda_\rho|<\infty.
\]

Enumerate the distinct zeros in any sequence and, within each zero's finite block, list jets in the order0,1,...,N_rho−1. Their Riesz representatives form a total linearly independent sequence in E. Every finite prefix spans a K*-invariant space. Gram–Schmidt therefore produces an orthonormal basis e1,e2,... with the same finite-prefix spaces. The anti-linear Riesz identification conjugates the diagonal eigenvalues: for each n,

\[
K^*e_n-\overline{\lambda_n}e_n
\in\operatorname{span}\{e_1,\ldots,e_{n-1}\},
\quad
\langle e_n,K^*e_n\rangle=\overline{\lambda_n},
\]

with the inner product conjugate-linear in its first argument. Each lambda_rho occurs N_rho times. No norm bound on the original jets or on a biorthogonal sequence is used, and no Riesz-basis assertion is used.

## 5. Sectoriality plus the diagonal sum proves trace class

Here is the elementary operator lemma needed for this step.

**Lemma.** Let T be a bounded operator on a separable Hilbert space such that

\[
\operatorname{Re}\langle Tx,x\rangle\ge0,
\qquad |\operatorname{Im}\langle Tx,x\rangle|
\le c\operatorname{Re}\langle Tx,x\rangle.
\]

If some orthonormal basis en satisfies

\[
\sum_n\operatorname{Re}\langle Te_n,e_n\rangle<\infty,
\]

then T is trace class. More precisely, writing A=(T+T*)/2,

\[
\|T\|_1\le\sqrt{1+c^2}\operatorname{Tr}A.
\]

**Proof.** A is positive. The finite diagonal sum gives

\[
\sum_n\|A^{1/2}e_n\|^2
=\sum_n\langle Ae_n,e_n\rangle<\infty.
\]

Thus A^(1/2) is Hilbert–Schmidt and A is trace class. Put Q=(T−T*)/(2i). The sector inequality is the pair of quadratic-form inequalities −cA≤Q≤cA. These imply

\[
Q=A^{1/2}CA^{1/2}
\]

for a bounded selfadjoint C of norm at most c on the closure of Ran(A^(1/2)). For completeness, define the form on that range by

β(A^(1/2)x,A^(1/2)y)=<Qx,y>.

It is well defined: if x is in ker A, the positive operators cA±Q have zero quadratic value at x, hence annihilate x, so Qx=0. Their positive-form Cauchy–Schwarz inequalities show β is bounded. Its diagonal bound |β(u,u)|≤c||u||² extends to the closure and represents a bounded selfadjoint C with ||C||≤c. Extend C by zero on the orthogonal complement if needed. Consequently

\[
T=A^{1/2}(I+iC)A^{1/2}.
\]

The product of two Hilbert–Schmidt operators with a bounded operator between them is trace class. Finally ||I+iC||≤sqrt(1+c²), because C is selfadjoint, giving the stated bound. This proves the lemma.

Apply the lemma to T=K*. By the previous section,

\[
\sum_n\operatorname{Re}\langle K^*e_n,e_n\rangle
=\sum_\rho N_\rho\operatorname{Re}\lambda_\rho<\infty.
\]

Therefore **K is trace class**, with the explicit estimate

\[
\boxed{\|K\|_1\le
\frac{\mu}{\sqrt{\mu^2-B_0^2}}
\sum_\rho N_\rho\operatorname{Re}\frac1{\mu^2-z_\rho^2}.}
\]

This deduction proves trace class *before* using compactness or a spectral trace theorem. It therefore makes no circular inference from a trace formula or from summable eigenvalues alone. In particular, Theorem10.3.2.1 has not been used.

## 6. Exact spectrum and invertibility: no hidden spectral part

Since K is trace class, K* is compact. Let Pn project onto the first n orthonormal vectors from the invariant flags. Compactness and strong convergence Pn→I imply

\[
\|(I-P_n)K^*\|\longrightarrow0.
\]

Indeed, approximate K* in norm by a finite-rank operator and use uniform convergence of Pn on its finite-dimensional range.

Relative to PnE plus (I−Pn)E, K* has block form

\[
\begin{pmatrix}T_n&B_n\\0&D_n\end{pmatrix},
\]

where Tn is finite triangular with diagonal conjugate(lambda1),...,conjugate(lambdan), and ||Dn||→0. Given nonzero q unequal to every conjugate(lambda_j), choose n with ||Dn||<|q|. Then Tn−qI is invertible, as is Dn−qI by a Neumann series. The full block operator K*−qI is invertible by its upper-triangular block inverse. Conversely each conjugate(lambda_j) is an eigenvalue in a sufficiently large invariant finite prefix. For a fixed nonzero eigenvalue, choose n past all its occurrences and with ||Dn|| smaller than its modulus; all generalized eigenvectors then lie in the finite prefix because the tail block minus that eigenvalue is invertible. Algebraic multiplicity is exactly the finite triangular multiplicity.

Thus the nonzero spectrum of K consists exactly of the lambda_rho, with the stated multiplicities, and there is no additional nonzero spectral part. Equality of two such values is equivalent to z_rho²=z_rho'², hence to rho'=rho or1−rho; each repeated value therefore has only finitely many occurrences.

Because z_rho is nonzero,

\[
\lambda_\rho=1/(\mu^2-z_\rho^2)\ne1/\mu^2.
\]

Hence I−mu²K is boundedly invertible. Define

\[
\boxed{R=K(I-\mu^2K)^{-1}.}
\]

This is an actual trace-class operator on E. On a jet block its multiplier is the rational composition

\[
\frac{F_\mu(z)}{1-\mu^2F_\mu(z)}=-\frac1{z^2}.
\]

This identity holds with all derivatives at z=z_rho, since the denominator is nonzero there; equivalently it holds in C[epsilon]/(epsilon^N_rho). Thus R has eigenvalue −z_rho^(−2) with full jet multiplicity. The same compact triangular argument gives its exact nonzero spectrum and multiplicities.

The construction is independent of mu: two choices give the same action on every dual jet, and those jets separate E. Under RH, if MAS-08 is constructed on this same quotient, its heat inverse-square operator also equals R by the same separating-jet argument. No heat construction or RH is needed for the Green proof itself.

## 7. Even quotient and the ordinary Xi determinant

The involution Jf(u)=f(−u) is unitary on H because w is even. Its dual action is

\[
\ell_{\rho,m}(Jf)=(-1)^m\ell_{1-\rho,m}(f).
\]

The complete annihilator description and zero symmetry imply JV=V, so J descends to a unitary involution of E. The even Green kernel gives commutation of K and R with J. Let E+ be the +1 eigenspace and R+=R|E+. It is a trace-class operator on the actual even Hilbert quotient.

For each pair {rho,1−rho}, reflection interchanges two independent jet spaces of dimension N_rho. Its +1 eigenspace has dimension N_rho. The even jets have dense span in the even dual by applying (I+J')/2 to the dense full jet span. Consequently R+ has precisely one eigenvalue −z_rho^(−2) per pair, with algebraic multiplicity N_rho.

For a representative of each pair put gamma_rho=−i z_rho, a possibly complex zero of Xi. Then gamma_rho^(−2)=−z_rho^(−2). The ordinary trace-class determinant theorem of cote1 and B-01 give

\[
\det_{E_+}(I-wR_+)
=\prod_{\{\rho,1-\rho\}}
\left(1+\frac{w}{z_\rho^2}\right)^{N_\rho}
=\frac{\Xi(\sqrt w)}{\Xi(0)}.
\]

All products converge absolutely locally uniformly. This is an ordinary Fredholm determinant on Masullo's actual quotient, conditional on the spectral-quotient claim alone. No RH, zero simplicity, Riesz basis, or nuclearity theorem from the draft is needed for this conclusion.

## 8. Scope, checks, and source qualifications

- The only substantive Masullo input is the exact full-jet annihilator description of the closed theta quotient in Theorem10.2.2.1; all uses remain conditional on that draft claim.
- The classical strict critical strip and zero count put the full nontrivial zeta spectrum inside the alpha=1/2 strip and make the inverse-square sum finite. RH is not used or inferred.
- The proof avoids the boundary cap by the strict critical-strip theorem at alpha=1/2, and avoids the draft's claims about uniform norms of biorthogonal vectors entirely.
- It uses neither a Riesz basis nor a spectral eigenvalue-summability criterion falsely applied to arbitrary nonnormal operators. The positive real-part sector estimate is the extra hypothesis that makes the argument work.
- It does not prove R+ is selfadjoint or positive in the quotient metric; MAS-09's metric obstruction remains a separate question/result.
- In particular, equality of the ordinary determinants does not identify R+ unitarily with B. Their determinant spectra agree, but the actual metric and any Jordan structure remain distinct data.

After composition, I reread the entire proof, including strong-integral bounds, weak derivatives, the cusp at zero, sector compression, dual/Riesz conventions, finite invariant flags, the trace-ideal factorization, compact triangular spectrum and multiplicity argument, inverse independence, reflection and determinant normalization. No gap found in that check. Further independent checking by root and `/root/masullo_bridge_check` is recorded separately by those agents.

Late strengthening check: the initial narrower-strip/RH proof was replaced by alpha=1/2 and complex z_rho. The entire revised proof was reread, specifically checking conjugated K* diagonals, positive real parts rather than positive eigenvalues, absolute summability, absence of zeros on strip edges, exact paired multiplicities, and the plus sign in product(1+w/z_rho²). The proof remains valid and now has no RH input.
