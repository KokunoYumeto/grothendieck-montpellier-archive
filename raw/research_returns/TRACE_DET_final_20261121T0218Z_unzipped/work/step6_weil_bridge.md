# Step 6: an exact Weil quadratic form and the actual smoothed zeta scalar

Run TRACE_DET_20261121. Date 21 November 2026 (Europe/Berlin). Agent `/root/delivery_audit`, GPT-6 Astra Pro; effort setting not exposed. Source paths are relative to `work/external_lean/lean/src`, the release-mirror snapshot documented by the parent. This note proves an explicitly normalized mathematical bridge. It does not identify the undefined historical W of Remark steps 4, 6 or 7, and it does not audit the stipulated RH/Dirichlet-GRH theorem or replay Lean.

## Outcome

For the precise quadratic form defined below, the requested two-indicator test has an absolutely convergent zero sum and an exact trace on the same paired-zero Hilbert space as B-01/B-03. Moreover, its cross term is exactly the actual source's smoothed von Mangoldt scalar, after an explicit bounded correction. Thus this route supplies a mathematical correspondence beyond matching names or noticing a common residue denominator.

The plus sign in the note gives a **lower** bound on that scalar in this normalization. A minus sign gives the corresponding upper bound. The actual final source endpoint uses an upper bound on a weighted character family over power windows; it is not identical to the global, zeta-only lower bound here. Nevertheless, the global lower bound suffices for a short, independently proved Landau argument, and for 0<eta<=1/2 it gives zero-freeness in Re(s)>1-eta. The numerical half-plane shape in the note can therefore be reconstructed exactly for this candidate normalization. The historical identification and the passage from the actual period/determinant constructions to this quadratic form remain open.

## Conventions and admissibility

Let Z be the multiset of all nontrivial zeros rho of the Riemann zeta function, with full multiplicities. We use the classical facts 0<Re(rho)<1, rho is nonreal, reflection rho -> 1-rho and conjugation preserve multiplicity, and N(T)=O(T log T). The zero-count fact is the same input used in B-01; a precise published locator is Titchmarsh, *The Theory of the Riemann Zeta-function*, second edition, Theorem 9.4, p.214. No RH is needed for these facts.

For X>=1 and eta real, put

\[
g(x)=\mathbf1_{(0,1]}(x),\qquad
g_X(x)=\mathbf1_{(0,X^{-1}]}(x),\qquad
f_{X,\eta}^{\pm}=g\pm X^\eta g_X.
\]

For Re(s)>0 define the Mellin transform by

\[
\mathcal M f(s)=\int_0^\infty f(x)x^s\,\frac{dx}{x}.
\]

For these real functions define, in this note's explicit normalization,

\[
W_{\rm std}(f)=\sum_{\rho\in Z}\mathcal M f(\rho)\mathcal M f(1-\rho).
\tag{6.1}
\]

This is the real-test version of the usual sesquilinear zero form: the second factor is \(\overline{\mathcal M f(1-\bar\rho)}\). The functions are not compactly supported away from zero in the multiplicative variable. We do not silently appeal to a conventional compact-support test class: convergence and all needed operations for this family are proved below. Endpoint values have no effect on the Mellin integrals.

There is also a substantive **linear-versus-quadratic convention boundary**. With multiplicative convolution and \(f^\sharp(x)=x^{-1}\overline{f(x^{-1})}\), one has

\[
\mathcal M(f*_{\times} f^\sharp)(s)
 =\mathcal M f(s)\overline{\mathcal M f(1-\bar s)}
 \quad(0<\Re s<1).
\]

For the displayed indicator functions both factors are absolutely Mellin-integrable in this strip, so the convolution identity follows from Fubini and a change of variables. Hence (6.1) is the linear zero functional applied to the convolution \(f*_{\times} f^\sharp\), not necessarily the linear functional applied to f itself. For example, \(g*_{\times}g^\sharp(x)=\min(1,x^{-1})\). The historical text does not specify which convention its W uses.

## STEP6-01. Exact quadratic trace, convergence and positivity

Choose one representative rho_j from each reflection pair {rho,1-rho}, including multiplicities, and set

\[
\gamma_j=(\rho_j-1/2)/i,
\quad H=\ell^2(\{j\}),
\quad A e_j=\gamma_j e_j,
\quad C e_j=\frac{e_j}{\gamma_j^2+1/4}.
\]

One may consistently choose Im(rho_j)>0. The operator A has its maximal diagonal domain

\[
D(A)=\{v\in H:\sum_j|\gamma_j|^2|v_j|^2<\infty\}.
\]

It is a densely defined closed normal operator. Here \(|\Im\gamma_j|<1/2\), and

\[
\gamma_j^2+1/4=\rho_j(1-\rho_j).
\]

The bounded trace-class C is exactly the inverse of \(A^2+I/4\), interpreted as a map from H into the domain of that unbounded operator. It is also the same \(B(I+B/4)^{-1}\) used in B-03.

**Proposition.** Write L=log X and a=X^(eta-1/2). All sums and traces in the following identities converge absolutely:

\[
W_{\rm std}(f_{X,\eta}^{\pm})
=2\operatorname{Tr}\left[C\bigl((1+a^2)I\pm2a\cos(AL)\bigr)\right].
\tag{6.2}
\]

In particular,

\[
W_{\rm std}(g)=2\operatorname{Tr}C=2\lambda_1,
\tag{6.3}
\]

where lambda_1 is the Li coefficient in B-03. Under RH, A is selfadjoint, \(U=e^{iAL}\) is unitary, C is positive, and with \(F_\pm=I\pm aU\),

\[
W_{\rm std}(f_{X,\eta}^{\pm})
=2\operatorname{Tr}(C F_\pm^*F_\pm)
=2\|F_\pm C^{1/2}\|_{\mathcal S_2}^{2}\ge0.
\tag{6.4}
\]

**Complete proof.** Direct integration, valid absolutely for Re(s)>0, gives

\[
\mathcal M f_{X,\eta}^{\pm}(s)
=\frac{1\pm X^{\eta-s}}{s}.
\]

For a zero rho=beta+it, 0<beta<1, the absolute value of the product of the two numerators is at most (1+X^eta)^2. Also \(|\rho(1-\rho)|\ge t^2\). There are finitely many low zeros, none with rho=0 or 1. On the dyadic annulus \(2^m\le |t|<2^{m+1}\), the zero count is O(2^m(m+1)), so the sum of reciprocal denominator moduli on that annulus is O((m+1)2^(-m)). Summing proves

\[
\sum_{\rho\in Z}\frac1{|\rho(1-\rho)|}<\infty.
\]

Consequently (6.1) converges absolutely. The same estimate gives locally uniform convergence for X,eta in compact subsets of [1,infinity) x R. In particular, reindexing by reflection or conjugation is legitimate, and conjugation makes the total sum real.

The displayed reciprocal-denominator sum proves C is trace class. Its denominators never vanish. Since |gamma_j| tends to infinity, both the reciprocal denominators and \(\gamma_j^2/(\gamma_j^2+1/4)\) are bounded. Thus C maps H into \(D(A^2)=\{v:\sum |\gamma_j|^4|v_j|^2<\infty\}\), and the two inverse identities with \(A^2+I/4\) hold coordinatewise on their stated domains. This justifies the resolvent notation without using an inverse of an undefined everywhere-defined unbounded operator.

Define \(e^{\pm iAL}\) and \(\cos(AL)\) explicitly as diagonal operators with entries \(e^{\pm i\gamma_jL}\) and \(\cos(\gamma_jL)\). They are bounded, since

\[
|e^{\pm i\gamma_jL}|\le X^{1/2},\qquad
|\cos(\gamma_jL)|\le\cosh(L/2).
\]

Multiplication of these bounded operators by C therefore remains trace class. Expanding the Mellin product gives

\[
\mathcal M f^{\pm}(\rho)\mathcal M f^{\pm}(1-\rho)
=\frac{1+X^{2\eta-1}\pm X^{\eta-\rho}\pm X^{\eta-1+\rho}}
       {\rho(1-\rho)}
=\frac{1+a^2\pm2a\cos(\gamma L)}{\gamma^2+1/4}.
\]

The expression is even in gamma. Each reflection pair therefore contributes twice its representative's diagonal entry. Absolute convergence proves (6.2), with the factor two and multiplicities shown. Applying the same argument to g proves the first equality in (6.3). B-03 gives \(\lambda_1=\operatorname{Tr}C\); equivalently, the two Li terms 1/rho+1/(1-rho) sum to 1/[rho(1-rho)] per representative pair.

Under RH all gamma_j are real, so the maximal diagonal A is selfadjoint, U is unitary, and C has positive diagonal entries. C commutes with U and U*. Since a is real,

\[
F_\pm^*F_\pm=(1+a^2)I\pm a(U+U^*)
             =(1+a^2)I\pm2a\cos(AL).
\]

The square root C^(1/2) is Hilbert--Schmidt and F is bounded. Taking the trace of \((F C^{1/2})^*(F C^{1/2})\), either by the diagonal basis or the trace-ideal cyclic identity, gives (6.4). In particular \(C F^*F=C^{1/2}F^*F C^{1/2}\) is positive because these diagonal operators commute. This completes the proof. ∎

**Star and ordering boundary.** Without RH, the exact trace formula (6.2) still holds, but \(U^{-1}\) need not equal U*, and C need not be positive or selfadjoint. Replacing the cosine by (U+U*)/2 off RH would be invalid. The positive product and Hilbert--Schmidt norm in (6.4) are explicitly RH consequences, not an unconditional proof of their own positivity.

## STEP6-02. The exact arithmetic cross term, including completion terms

The actual source definition is `Formalism/StatementOC.lean:11–13`:

\[
S_\zeta(X)=\sum_{1\le n\le\lfloor X\rfloor}\Lambda(n)(X/n-1),
\qquad
G_\zeta(X)=S_\zeta(X)-X\log X+(1+\gamma_E)X.
\tag{6.5}
\]

Define the absolutely convergent zero sum and correction

\[
R(X)=\sum_{\rho\in Z}\frac{X^\rho}{\rho(1-\rho)},
\qquad
E(X)=\sum_{n=1}^{\infty}\frac{X^{-2n}}{2n(2n+1)},
\qquad
b(X)=\log(2\pi)-E(X).
\tag{6.6}
\]

Then, unconditionally for every real X>=1,

\[
\boxed{G_\zeta(X)=b(X)+R(X)
=b(X)+2\sqrt X\operatorname{Tr}\bigl(C\cos(A\log X)\bigr).}
\tag{6.7}
\]

For X>1 the correction also has the elementary expression

\[
b(X)=\log(2\pi)+\frac12\log(1-X^{-2})
 +\frac12\left(X\log\frac{X+1}{X-1}-2\right).
\tag{6.8}
\]

At X=1 the series gives its continuous value \(b(1)=\log(4\pi)-1\). In fact

\[
\log(4\pi)-1\le b(X)<\log(2\pi)\quad(X\ge1).
\tag{6.9}
\]

**Primary input and correction history.** The precise explicit-formula input is Olivier Ramaré, *Corrigendum to “Explicit estimates for the summatory function of Lambda(n)/n from the one of Lambda(n)”*, corrected Lemma 2.1 on p.1 and its integral expression on p.2. Author URL: <https://ramare-olivier.github.io/Maths/Corrigendum-PsiTildeSimple-Acta-02.pdf>. The original article is *Acta Arithmetica* 159 (2013), no.2, 113–122, DOI 10.4064/aa159-2-2. Its original Lemma 2.2 has sign errors, so the corrigendum is material here. The original paper's p.1 defines \(\psi(X)=\sum_{n\le X}\Lambda(n)\) and \(\widetilde\psi(X)=\sum_{n\le X}\Lambda(n)/n\); only those definitions, not the uncorrected explicit formula, are used from that version.

The corrected statement is

\[
\widetilde\psi(X)
=\log X-\gamma_E+\frac{\psi(X)-X}{X}
-\sum_\rho\frac{X^{\rho-1}}{\rho(\rho-1)}+\frac{b(X)}{X}.
\tag{6.10}
\]

The retrieved corrigendum is retained as `work/programme_sources/Ramare_Corrigendum_PsiTildeSimple_Acta.pdf`; SHA256 `ec315280a24bd5b5d2170aeb145b29a7abae6d00ea1304f78b4a2f3fbd9a6b5e`. The source manifest and a rendered first-page formula check are retained separately. The source's line describing the critical strip appears to print an imaginary-part symbol; throughout this note the zero set is explicitly the usual nontrivial zeros with 0<Re(rho)<1. The formulas and the author's reference to nontrivial zeros determine the intended zero set; no result here uses the displayed strip-symbol typo.

**Complete derivation from the cited explicit formula.** By (6.5), \(S_\zeta(X)=X\widetilde\psi(X)-\psi(X)\). Multiply (6.10) by X, subtract psi(X), and then subtract \(X\log X-(1+\gamma_E)X\). The remaining zero sum is

\[
-\sum_\rho\frac{X^\rho}{\rho(\rho-1)}
=\sum_\rho\frac{X^\rho}{\rho(1-\rho)}=R(X),
\]

so G_zeta=R+b. Absolute convergence follows from the earlier denominator bound and \(|X^\rho|=X^{\Re\rho}\le X\), locally uniformly in X>=1. It is legitimate to group the reflected zeros, which gives

\[
R(X)=\sum_j\frac{X^{\rho_j}+X^{1-\rho_j}}{\rho_j(1-\rho_j)}
=2\sqrt X\sum_j\frac{\cos(\gamma_j\log X)}{\gamma_j^2+1/4}.
\]

This proves the trace identity in (6.7) with the same C and A as STEP6-01.

The corrigendum's p.2 integral gives

\[
b(X)=X\int_X^\infty
 \left(\log(2\pi)+\tfrac12\log(1-t^{-2})\right)\frac{dt}{t^2}.
\]

Expand \(-\log(1-t^{-2})=\sum_{n\ge1}t^{-2n}/n\) and apply Tonelli to the nonnegative series. The result is precisely b=log(2pi)-E in (6.6). This also works at X=1: the logarithmic singularity in the integral is integrable, and the resulting coefficient series is summable. The partial-fraction identity

\[
\frac1{2n(2n+1)}=\frac1{2n}-\frac1{2n+1}
\]

gives E(1)=1-log 2. Every term decreases as X increases, is nonnegative, and is dominated by its summable value at 1. Thus b has the stated continuous endpoint value and bounds (6.9), and tends to log(2pi) at infinity. For X>1, summing the logarithm and inverse-hyperbolic-tangent power series gives (6.8), agreeing with the corrected source formula. At an integer or prime power the jump terms in \(X\widetilde\psi-\psi\) cancel because X/n-1 is zero when X=n. Hence there is no endpoint half-weight ambiguity in (6.7). This completes the derivation. ∎

The cited classical explicit formula is an input, not a claim that this note has independently reproved every contour-integral estimate behind it. The subsequent algebra, convergence, endpoint extension and operator trace representation are proved here.

As a constant check, X=1 gives

\[
2\lambda_1=R(1)=G_\zeta(1)-b(1)
=2+\gamma_E-\log(4\pi),
\]

consistent with the first Li coefficient. Under RH, (6.7) and C>=0 immediately give

\[
|G_\zeta(X)-b(X)|\le2\lambda_1\sqrt X.
\tag{6.11}
\]

This is an audit-derived representation of the actual source scalar by a weighted cosine trace. It is not a source declaration constructing A from the finite automorphic determinants.

## STEP6-03. Exact one-sided inequalities and the claimed half-plane shape

Absolute convergence and reflection in the cross terms give, without RH,

\[
\boxed{
W_{\rm std}(f_{X,\eta}^{\pm})
=2\lambda_1(1+X^{2\eta-1})
\pm2X^{\eta-1}\bigl(G_\zeta(X)-b(X)\bigr).}
\tag{6.12}
\]

Indeed the two cross sums become equal after rho -> 1-rho, and each equals X^(eta-1)R(X). The coefficient X^(eta-1) is positive. Therefore the exact pointwise equivalences are

\[
W_{\rm std}(f_{X,\eta}^{+})\ge0
\quad\Longleftrightarrow\quad
G_\zeta(X)\ge b(X)-\lambda_1(X^{1-\eta}+X^\eta),
\tag{6.13}
\]

\[
W_{\rm std}(f_{X,\eta}^{-})\ge0
\quad\Longleftrightarrow\quad
G_\zeta(X)\le b(X)+\lambda_1(X^{1-\eta}+X^\eta).
\tag{6.14}
\]

At X=1, f^+=2g and f^-=0, so (6.12) gives respectively 8lambda_1 and 0, agreeing with quadratic homogeneity. For 0<eta<1, both bounds have exponent theta=max(eta,1-eta)<1 after absorbing the bounded b into a constant. For 0<eta<=1/2, theta=1-eta, exactly the exponent suggested by Remark step 6. The constant can be bounded using |lambda_1|, so the following implication does not assume RH or use positivity of C.

### Global one-sided scalar criterion, with full proof

**Lemma.** Let 0<theta<1. If either \(G_\zeta(X)\ge-KX^\theta\) or \(G_\zeta(X)\le KX^\theta\) for some real K>=0 and all sufficiently large X, then zeta has no zero rho with Re(rho)>theta.

**Proof.** Direct termwise integration for Re(s)>1 gives

\[
\Phi(s):=\int_1^\infty G_\zeta(X)X^{-s}\frac{dX}{X}
=-\frac{\zeta'(s)}{\zeta(s)s(s-1)}
-\frac1{(s-1)^2}+\frac{1+\gamma_E}{s-1}.
\tag{6.15}
\]

For completeness, a single summand integrates to

\[
\int_n^\infty (X/n-1)X^{-s}\frac{dX}{X}
=\frac{n^{-s}}{s(s-1)}.
\]

For a real sigma>1 the integrands before taking the Dirichlet coefficients are nonnegative, and \(\sum_n\Lambda(n)n^{-\sigma}\) converges. Tonelli and then absolute convergence justify the interchange for complex s in this half-plane. The two main-term integrals are \(1/(s-1)^2\) and \(1/(s-1)\). This proves (6.15).

The right side continues meromorphically to Re(s)>0. At s=1, put h=s-1 and use the classical Laurent expansion \(-\zeta'/\zeta(s)=h^{-1}-\gamma_E+O(h)\). Its quotient by s(s-1) is \(h^{-2}-(1+\gamma_E)h^{-1}+O(1)\), so both polar terms in (6.15) cancel. At a nontrivial zero rho of multiplicity m, the residue is

\[
-\frac m{\rho(\rho-1)}=\frac m{\rho(1-\rho)}\ne0.
\tag{6.16}
\]

There are no real zeta zeros with 0<s<1: the alternating eta series is positive there and equals (1-2^(1-s))zeta(s), whose prefactor is negative. For s>1 the Euler product gives nonvanishing. Together with the cancellation at 1, these facts show Phi is analytic in a neighborhood of every positive real s.

Suppose first the lower bound holds, and choose u_0>=0 beyond its threshold after X=e^u. Define h(u)=0 for 0<=u<u_0 and \(h(u)=G_\zeta(e^u)+Ke^{\theta u}\) for u>=u_0. Then h is nonnegative and locally integrable. Also G_zeta(X)=O(X(1+log X)^2), for example by Lambda(n)<=log n in (6.5). Thus the Laplace integral H(s)=\(\int_0^\infty h(u)e^{-su}du\) converges for Re(s)>1. In that domain,

\[
H(s)=\Phi(s)-\int_0^{u_0}G_\zeta(e^u)e^{-su}\,du
+\frac{K e^{-(s-\theta)u_0}}{s-\theta}.
\tag{6.17}
\]

The compact-interval integral is entire. Consequently (6.17) continues H analytically through each real point s>theta, and its possible nonreal poles there are exactly the zeta poles (6.16).

Here is the elementary positive-Laplace fact needed to finish. Let sigma_c be the abscissa of convergence of the integral of a nonnegative locally integrable h, with finite convergence somewhere. If sigma_c is finite, its Laplace transform cannot be analytic through the real point sigma_c. Otherwise let delta>0 be the radius of a disc of analytic continuation about sigma_c, choose sigma_0=sigma_c+delta/4, and take r=delta/2. The function is analytic in the disc of radius 3delta/4 about sigma_0, which is contained in the original disc, while sigma_0-r=sigma_c-delta/4<sigma_c. At sigma_0, differentiation under the integral is valid: moments are dominated using convergence at a slightly smaller real point still above sigma_c. The Taylor series toward the left has nonnegative terms,

\[
\sum_{n\ge0}\frac{r^n}{n!}
 \int_0^\infty u^n h(u)e^{-\sigma_0u}\,du.
\]

It is finite because r lies strictly inside that Taylor disc. Tonelli identifies it with \(\int_0^\infty h(u)e^{-(\sigma_0-r)u}du\), contradicting the definition of sigma_c. This proves the fact; the case sigma_c=-infinity already has convergence everywhere.

In the present setting sigma_c<=1. If sigma_c>theta, (6.17) is analytic through that positive real point, contradicting the just-proved fact. Hence sigma_c<=theta. The nonnegative Laplace integral H is therefore holomorphic on Re(s)>theta. By (6.17) and meromorphic uniqueness, Phi has no nonremovable pole there. Equation (6.16) excludes every zeta zero in this half-plane. If the upper bound holds instead, use \(h(u)=Ke^{\theta u}-G_\zeta(e^u)\) beyond u_0; the same argument uses -Phi and the same nonzero poles. This proves both cases. ∎

**Consequence for the specified test.** For any fixed 0<eta<1, eventual nonnegativity of the plus-tests implies zero-freeness in Re(s)>max(eta,1-eta), by (6.13), boundedness of b, and the lemma. In particular, for 0<eta<=1/2 this is Re(s)>1-eta. The same implication follows from the minus-tests using (6.14). At eta=1/2 the plus-test family, even only for all sufficiently large X, is therefore RH-equivalent: the converse is (6.4), and the forward implication plus reflection puts every zero on the critical line. This equivalence belongs to the explicitly defined quadratic form (6.1), not an asserted historical definition of W.

**Robustness of the approximate amplitude.** The power X^eta can be replaced by any positive real q(X). The same expansion gives

\[
W_{\rm std}(g+q(X)g_X)
=2\lambda_1(1+q(X)^2/X)+2q(X)R(X)/X.
\]

Its nonnegativity is exactly \(G_\zeta(X)\ge b(X)-\lambda_1(X/q(X)+q(X))\). If positive constants c_1,c_2 satisfy \(c_1X^\eta\le q(X)\le c_2X^\eta\) for all sufficiently large X, this still gives a lower bound of order \(X^{\max(\eta,1-\eta)}\), using absolute values for lambda_1 if necessary. The scalar lemma therefore gives the same half-plane. This is the precise sense in which an approximately X^eta positive amplitude would suffice within the chosen quadratic normalization; it does not presume the historical symbol means that comparison.

### Actual-source comparison and exact remaining gate

`Formalism/StatementOC.lean:11–13` supplies exactly the zeta scalar in (6.5). Its lines 23 onward also contain propositions using lower bounds on **differences** Gz-Gchi; those should not be silently replaced by the zeta-only inequality above. In the final path already traced in DET-09, `Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ExplicitFormulaErrorOfHostConditions.lean:32–41` defines a character sum Gm with strictly positive weights. `Development/AutomorphicArithmetic/PrimitiveCosets/CoreGm.lean:12–15` supplies an upper bound for it. `Development/AutomorphicArithmetic/DedekindLFunctions/CharFamily.lean:24–46` defines the finite character family with positive weights and the window hypothesis, and `LandauTheorems/ZeroFreeOfRpowWindow.lean:11–14` invokes a criterion on arbitrarily large power windows. The present lemma is a complete proof for a global eventual bound and does not replace or reprove that stronger window mechanism.

The mathematical gate is now more precise. A proposed identification must specify whether the historical W is linear or quadratic; match its test via the multiplicative convolution/reflection if needed; fix overall normalization and the sign of the cross term; explain the stated approximately X^eta amplitude and its error; and, for the final source path, account for character averaging and window quantifiers. If these are supplied, (6.2), (6.7), (6.12) and the scalar lemma give a concrete dictionary to the designated zero-based operator. The present work supplies that dictionary for one fully specified candidate, while leaving its historical attribution unproved.

No finite GGP period determinant is identified with det(I-wB), no trace-norm compression limit is established, and no unconditional positivity of the candidate Weil quadratic form is deduced from the period source. The positive operator in (6.4) uses the stipulated RH, exactly as B-01 does. The converse scalar lemma is a structural equivalence, not a new proof that its positivity premise holds.

## Checks performed and evidence

The proofs of STEP6-01, the derivation in STEP6-02 from the corrected explicit-formula input, and the complete global scalar lemma in STEP6-03 were reread in full after composition. The check covered all domains; multiplicities and the factor two; the adjoint versus inverse distinction; trace ideals and the Hilbert--Schmidt ordering; both cross-term signs; the X=1 and integer endpoints; the bounded correction; Mellin/Laplace interchange; the cancellation at s=1; the real-axis nonvanishing input; the positive-Laplace Taylor/Tonelli argument; and the difference between global bounds and source window bounds. These are mathematical proof checks, not Lean certificates. The corrected primary formula itself was inspected in text and in the rendered p.1; its published analytic proof is cited rather than independently reverified in full.

An initial filesystem query guessed nonexistent `Formalism/Chebyshev*`, `Formalism/ChTop.lean` and top-level `Final.lean` paths. It did read the valid `Formalism/StatementOC.lean` and reported the three path errors. This was superseded by reading the actual located endpoint files above. An exact-name all-source search found no `smoothedGzeta` declaration: that phrase is descriptive; the actual identifiers here are `Formalism.Gz`, `Deduction.G` and the displayed `Gm` definitions. No absence conclusion rests on the guessed paths or the descriptive name.
