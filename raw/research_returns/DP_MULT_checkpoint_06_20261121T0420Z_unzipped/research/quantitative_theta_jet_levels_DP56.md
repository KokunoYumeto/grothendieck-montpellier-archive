# DP56 — linear jet interpolation and subexponential tensor levels

Date: 2026-11-21 UTC. Author: `/root/formal_bound`, GPT-6 Astra Pro; reasoning effort is not exposed. The parent reserved DP56. This is a quantitative strengthening of DP54; the checked DP54 files remain unchanged.

## 1. Statements and scope

Let \(R\) be a complete discrete valuation ring, let \(X/R\) be proper and smooth of relative dimension \(g\), let \(e\) be a section, and let \(\mathcal L\) be relatively ample. Write \(I\) for the ideal of \(e\).

**DP56(a), a linear integral jet-surjection threshold.** There are fixed integers \(r\ge1\) and \(b\ge0\), depending only on \((X,\mathcal L,e)\), such that for every \(n\ge0\) and every integer \(\kappa\ge rn+b\), restriction is surjective:

\[
H^0(X,\mathcal L^{\otimes\kappa})
\twoheadrightarrow
H^0\bigl(V(I^{n+1}),\mathcal L^{\otimes\kappa}|_{V(I^{n+1})}\bigr).
\tag{QL1}
\]

The proof is integral polynomial interpolation in a fixed projective embedding. It gives an actual linear bound, rather than merely a separate Serre threshold for each \(n\). No numerical value of the model-dependent constants \(r,b\) is asserted.

For the remaining statements, take the actual Jacobian and theta line of DP49/DP54 at \(p=11\), with \(R=W(\mathbf F_{11^3})\), \(K=\operatorname{Frac}R\), and the invariant product gauge. In particular \(\mathcal L=(1,w_0)^*\mathcal P_\lambda\) is relatively ample, and the normalized germ is

\[
\Theta_s(z)=f_s(z)U(z)^\kappa B(z)^{-\kappa},
\qquad U\in1+(z)R[[z]],\qquad B=\exp b.
\tag{QL2}
\]

Let \(\beta=b\circ E\) be the primitive logarithm in additive coordinates. The following coefficient argument applies generally to the odd-prime arbitrary-unit pairs of DP46; it is then used for this actual Jacobian.

**DP56(b), coefficientwise control in the tensor parameter.** Suppose a zero-constant series \(\gamma(Z_1,\ldots,Z_D)\in K[[\mathbf Z]]\), a rational weight \(w>0\), and \(s=1/(p-1)\) satisfy

\[
\inf_\alpha\{v_p([\mathbf Z^\alpha]\gamma)+w|\alpha|\}\ge s.
\tag{QL3}
\]

Put \(c=s-w\). For a nonzero integral homogeneous polynomial
\(P=\sum_{|\alpha|=n}P_\alpha\mathbf Z^\alpha\), define

\[
F_P(T)=P(\partial)\exp(-T\gamma)(0)\in K[T],
\qquad
\sigma(P)=s\max_{\alpha\in\operatorname{supp}P}
                    \sum_{i=1}^D s_p(\alpha_i).
\tag{QL4}
\]

Every coefficient of this polynomial in the indeterminate \(T\) satisfies

\[
v_p([T^m]F_P(T))\ge cn-\sigma(P).
\tag{QL5}
\]

The zero coefficient has valuation \(+\infty\). For \(n\ge1\),

\[
\sigma(P)\le D\bigl(1+\lfloor\log_p n\rfloor\bigr).
\tag{QL6}
\]

For an ordinary specified primitive line, (QL3) holds for its logarithm at the exact weight \(w_k\) of DP46, with \(D=1\) and \(c=c_k\). For the first-negative-row harmonic family on two copies, (QL3) holds for the sum of the two full logarithms at

\[
w_*=\frac{p^{h-1}}{(p-1)(p^{h-1}+1)},\qquad
c_*=\frac1{(p-1)(p^{h-1}+1)},\qquad D=2h.
\tag{QL7}
\]

**DP56(c), subexponential levels along sharp sequences.** Let \(P_\nu\) be either a sharp ordinary primitive-line sequence from DP46 or the first-negative-row two-column harmonic sequence from DP51 for the actual Jacobian at 11. Let \(n_\nu\to\infty\) be its degree, and write

\[
V_\nu=v_{11}(F_{P_\nu}(1))<\infty,
\qquad \frac{V_\nu}{n_\nu}\longrightarrow c,
\tag{QL8}
\]

where \(c\) is its exact local rate. There exist positive integers \(M_\nu\), with \(11\nmid M_\nu\), and global integral sections of \(\mathcal L^{\otimes M_\nu^2}\), such that the selected normalized value, including the source factor \(M_\nu^{-n_\nu}\), has valuation exactly \(V_\nu\), and

\[
\boxed{\log M_\nu=o(n_\nu),\qquad
       \log(M_\nu^2)=o(n_\nu).}
\tag{QL9}
\]

Here \(\log\) is the ordinary real logarithm. Equivalently, the tensor powers are \(\exp(o(n_\nu))\). The same powers may be retained when the sections are replaced by number-field sections integral at the selected prime, with the finite valuations preserved as in DP54.

This is a statement about the logarithm of the tensor level. It is not a bound for the archimedean norms or heights of the sections, the global cost of the resulting data, or their membership in a prescribed translated family.

## 2. Integral projective coordinates at the section

Since the base is affine and \(\mathcal L\) is relatively ample, choose \(r\ge1\) and an immersion

\[
\iota:X\longrightarrow\mathbf P^N_R,
\qquad \iota^*\mathcal O(1)\cong\mathcal L^{\otimes r}.
\tag{QL10}
\]

This known implication is Stacks Project Lemma 29.40.4, Tag [01VT](https://stacks.math.columbia.edu/tag/01VT), parts (2) and (5). Because \(X/R\) is proper, this immersion is closed. Denote the pulled-back homogeneous coordinate sections by \(h_0,\ldots,h_N\).

Choose a trivialization of \(e^*\mathcal L^{\otimes r}\). At least one coordinate section has unit value at the closed point of \(e\), since they generate the line there. Relabel it \(h_0\), and rescale by a unit of \(R\) so that \(h_0(e)=1\). Then \(h_0\) is nonvanishing along the entire section \(e\): its pullback is a unit on \(\operatorname{Spec}R\).

Replace each \(h_i\), for \(i>0\), by

\[
h_i-h_i(e)h_0.
\]

This is an invertible triangular change of the projective coordinates and makes every ratio \(t_i=h_i/h_0\) vanish along \(e\). On the affine chart \(h_0\ne0\), the closed immersion gives a surjection from a polynomial ring in these ratios to the coordinate ring of the chart. In particular their images generate the conormal module \(I/I^2\) along \(e\).

This conormal module is free of rank \(g\), by smoothness and the fact that the base is local. The map \(R^N\to I/I^2\) is surjective. Modulo the maximal ideal choose \(g\) columns that form a basis; their corresponding minor is a unit over \(R\). Relabel these selected sections \(h_1,\ldots,h_g\). Then

\[
t_i=h_i/h_0\quad(1\le i\le g)
\tag{QL11}
\]

are integral formal parameters. More explicitly, in any integral smooth formal parameters the linear coefficient matrix of the \(t_i\)'s is invertible over \(R\); formal inversion over \(R\) then gives

\[
\widehat{\mathcal O}_{X,e}\cong R[[t_1,\ldots,t_g]].
\tag{QL12}
\]

Only inverses of units occur in this inversion. The parameters and the three chosen sections in the Jacobian case have therefore introduced no \(p\)-denominators.

## 3. Homogenizing every integral jet

First consider the power \(\kappa=rn\). The section \(h_0^n\) is a frame along \(V(I^{n+1})\). Write an arbitrary target section in that frame as

\[
Q(t_1,\ldots,t_g)=\sum_{|\alpha|\le n}q_\alpha t^\alpha,
\qquad q_\alpha\in R.
\]

The global section

\[
\sum_{|\alpha|\le n}q_\alpha
h_0^{\,n-|\alpha|}h_1^{\alpha_1}\cdots h_g^{\alpha_g}
\in H^0(X,\mathcal L^{\otimes rn})
\tag{QL13}
\]

has exactly that target jet. Every exponent in this homogenization is nonnegative. The same formula works in any power \(rN\) with \(N\ge n\), replacing \(h_0^{n-|\alpha|}\) by \(h_0^{N-|\alpha|}\).

To cover every sufficiently large power rather than just multiples of \(r\), choose \(b\ge0\) such that \(\mathcal L^{\otimes m}\) is globally generated for all \(m\ge b\). The precise known result is Stacks Project Proposition 28.27.13(7), Tag [01Q3](https://stacks.math.columbia.edu/tag/01Q3), applied to \(\mathcal F=\mathcal O_X\).

If \(\kappa\ge rn+b\), put \(m=\kappa-rn\ge b\). Global generation provides a section \(\eta_m\in H^0(X,\mathcal L^{\otimes m})\) whose value at the closed point of \(e\) is a unit; hence it is a frame along all of \(e\) and on the infinitesimal thickening. Express the desired jet in the frame \(\eta_m h_0^n\), and multiply (QL13) by \(\eta_m\). This proves (QL1) for every such \(\kappa\), including \(n=0\).

The target can in particular be the inverse unit correction \(U^{-\kappa}\) in DP54. Changing from its specified integral frame to \(\eta_mh_0^n\) multiplies the target by an integral unit on the thickening. Thus the homogenization realizes exactly the normalized pure-kernel jet used there. The constants \(r,b\) are fixed once for the model and line; they do not depend on \(n\), the target, or the tensor exponent beyond the stated inequality.

The same construction can be made over the local number-field DVR \(\mathcal O_{\mathbf Q(\zeta_7),\mathfrak p}\), where the line is ample by DP54's same closed-fibre argument. It gives algebraic projective coordinate sections before completion. Targets with arbitrary coefficients in the completion still require the complete-ring interpolation or the finite approximation discussed in §7; the existence of algebraic coordinates does not make a general \(p\)-adic target coefficient algebraic.

## 4. The exponential estimate is coefficientwise in the indeterminate

We prove DP56(b), rather than infer it from bounds at integral values of \(T\). Those two assertions are different for polynomials with denominators.

Choose a finite ramified extension of \(K\) containing \(\varpi\) with \(v_p(\varpi)=w\), and put

\[
\widetilde\gamma(\mathbf Z)=\gamma(\varpi\mathbf Z).
\]

By (QL3), every coefficient of \(\widetilde\gamma\) has valuation at least \(s\). For every \(m\ge1\), every coefficient of

\[
\frac{\widetilde\gamma^m}{m!}
\]

has valuation at least

\[
ms-v_p(m!)=s\,s_p(m)\ge0.
\tag{QL14}
\]

All coefficient products and sums are well-defined because \(\widetilde\gamma\) has zero constant term. Thus

\[
\exp(-T\widetilde\gamma)
\in\mathcal O_{K'}[T][[Z_1,\ldots,Z_D]],
\tag{QL15}
\]

where the notation means that each \(\mathbf Z\)-coefficient is a polynomial in \(T\) with integral coefficients. No assertion of a finite degree bound in \(T\) for the entire infinite series is intended. At total \(\mathbf Z\)-degree \(n\), its degree in \(T\) is at most \(n\).

Write \(A_{\alpha,m}\) for the coefficient of \(\mathbf Z^\alpha T^m\) in \(\exp(-T\gamma)\). Equation (QL15) gives

\[
v_p(A_{\alpha,m})\ge-w|\alpha|.
\tag{QL16}
\]

On applying \(P(\partial)\) at zero, this coefficient is multiplied by \(P_\alpha\alpha!\). The integral coefficients of \(P\), Legendre's identity, and the triangle inequality yield

\[
\begin{split}
v_p([T^m]F_P)
&\ge\min_{\alpha\in\operatorname{supp}P}
  \left(-wn+sn-s\sum_i s_p(\alpha_i)\right)\\
&=cn-\sigma(P).
\end{split}
\]

This proves (QL5). For \(0\le a\le n\), \(n\ge1\), one has
\(s_p(a)\le(p-1)(1+\lfloor\log_p n\rfloor)\). Summing over the fixed number \(D\) of variables proves (QL6).

## 5. Verifying the logarithm hypothesis for the actual sharp families

For a fixed primitive logarithmic line in DP46, its entire initial-form calculation at the endpoint weight \(w_k\) proves

\[
\inf_n\{v_p([t^n]\beta(ut,vt))+w_kn\}=s.
\tag{QL17}
\]

This is a bound for the logarithm itself, stronger than the integrality of its exponential. It is preserved by the arbitrary unit arrows because the unique leading coefficient is multiplied by a unit. Taking \(\gamma(t)=\beta(ut,vt)\), \(D=1\), and the differential-symbol polynomial \(P(Z)=Z^n\) proves coefficientwise (QL5) for the ordinary derivative polynomial in the tensor parameter.

For the first-row two-column family, use the profile of DP42/DP46 at \(j=1\), \(w=w_*\). Its scalar and first dual weights are \(w_*\), while its later dual weights are

\[
\omega_i=s-p^{i-1}(s-w_*)<w_*\quad(i>1).
\tag{QL18}
\]

The contracted inverse group logarithms are integral. The full group-coordinate primitive logarithm at this profile has coefficient infimum \(s\). Giving every independent additive variable the common weight \(w_*\) supplies nonnegative extra factors at the later coordinates; composing with the integral contracted inverse maps cannot decrease that infimum. Hence

\[
\inf_\alpha\{v_p([\mathbf Z^\alpha]\beta)+w_*|\alpha|\}\ge s.
\tag{QL19}
\]

This is the logarithmic part of DP51's full-polydisc corollary, written explicitly before exponentiation. For two independent copies, their sum still has infimum at least \(s\) and has zero constant term. Taking \(D=2h\), \(\gamma=\beta(Z^{(1)})+\beta(Z^{(2)})\), and \(P=P_{a,b}\) gives (QL5) for the actual source-shaped harmonic family. The number of variables stays fixed as \(a+b\) increases.

These arguments justify the coefficientwise tensor estimate at the same rates as the sharp ordinary and harmonic families. They do not replace the chosen rate by a bare integral-function slope or discard the primitive normalization.

## 6. Exact integer congruence and level bounds

Fix one homogeneous differential polynomial of degree \(n\ge1\) in one of these families, and suppose \(F_P(1)\ne0\). Put

\[
V=v_p(F_P(1)),\qquad L=cn-\sigma(P),
\]

and choose the explicit nonnegative integer

\[
\boxed{B=\max\{1,\lfloor V-L\rfloor+1\}.}
\tag{QL20}
\]

In fact (QL5) implies \(V\ge L\), so the maximum is harmless. It makes the choice positive even in a degenerate case. Since \(B>V-L\), every integer \(T\equiv1\pmod{p^B}\) satisfies

\[
v_p(F_P(T)-F_P(1))\ge B+L>V,
\tag{QL21}
\]

by summing the coefficientwise estimates for \([T^m]F_P\,(T^m-1)\). Consequently

\[
v_p(F_P(T))=V.
\tag{QL22}
\]

This strict inequality handles exact integer and noninteger values of \(V-L\); no ceiling-rounding loss has been suppressed.

For the actual model in DP54 use its fixed \(r,b\) from §3, and set

\[
m_0=\max\{1,\lceil\sqrt{rn+b}\rceil\},\qquad
q_0=\left\lceil\frac{m_0-1}{p^B}\right\rceil,
\qquad M=1+q_0p^B.
\tag{QL23}
\]

Here \(q_0\ge0\) is an integer. Directly from the definition,

\[
M\equiv1\pmod{p^B},\qquad
M\ge m_0,\qquad
M<m_0+p^B\le\sqrt{rn+b}+1+p^B.
\tag{QL24}
\]

If \(rn+b=0\), the harmless maximum in \(m_0\) only changes the final bound by one; for the present \(n\ge1,r\ge1\) this case does not occur. Set \(\kappa=M^2\). Then \(\kappa\ge rn+b\), so the linear jet-surjection theorem realizes the pure exponent-\(-\kappa\) jet through degree \(n\). Also \(\kappa\equiv1\pmod{p^B}\), so (QL22) gives its selected value exactly the valuation \(V\). The source normalization \(M^{-n}\) is a unit and preserves it.

Now apply this choice along (QL8). Since \(D\) is fixed, (QL6) yields

\[
\begin{split}
\frac{B_\nu}{n_\nu}
&\le\frac{V_\nu-cn_\nu}{n_\nu}
  +\frac{\sigma(P_\nu)+1}{n_\nu}\\
&\longrightarrow0.
\end{split}
\tag{QL25}
\]

The left side is nonnegative. Even if \(V_\nu-cn_\nu\) is occasionally negative, the right side is nonnegative by the lower bound and tends to zero, so the squeeze is valid. Equation (QL24) then gives

\[
0\le\frac{\log M_\nu}{n_\nu}
\le\frac{\log(\sqrt{rn_\nu+b}+1+p^{B_\nu})}{n_\nu}
\longrightarrow0.
\tag{QL26}
\]

Multiplication by two proves the tensor-power assertion in (QL9). The construction is at one fixed prime; no simultaneous congruence at a growing set of primes is being imposed.

## 7. Local and number-field interpolation are different claims

The homogenization in §3 realizes every integral \(R\)-jet exactly. The coefficients of the target \(U^{-\kappa}\), the chosen actual display coordinates, and their changes to the projective coordinates can be arbitrary elements of the complete ring \(R\). Thus exact interpolation is initially a statement about global sections over \(R\).

For each already selected power \(\kappa=M_\nu^2\), DP54's flat-base-change argument identifies

\[
H^0(J_{R_0},\mathcal L^{\otimes\kappa})\otimes_{R_0}R
=H^0(J_R,\mathcal L^{\otimes\kappa}),
\qquad R_0=\mathcal O_{\mathbf Q(\zeta_7),\mathfrak p}.
\tag{QL27}
\]

The finite free \(R_0\)-module before tensoring is dense in its completion. The selected finite derivative, or the product-copy polynomial evaluation, is continuous in these finitely many section coordinates. Approximate the exact integral interpolant sufficiently closely to preserve its nonzero selected valuation. This does not change \(M_\nu\) or \(\kappa\), so the subexponential tensor-level conclusion survives unchanged for number-field sections integral at \(\mathfrak p\).

This approximation is not used to claim equality of the prescribed formal jet over the number field. No bound for the necessary approximation precision, denominators at other primes, coefficient heights in an arithmetic basis, or archimedean norms is included in this theorem.

## 8. What the quantitative refinement resolves

DP54's finite-jet algebraic realization can be made with a fixed linear interpolation threshold \(rn+b\), and its tensor congruence can be made with a sublinear exponent along the sharp sequences. Together these prove subexponential square tensor levels and retain the actual source normalization \(M^{-n}\).

The remaining data are not interchangeable with the logarithm of \(M\). A section may have large archimedean norm even when its tensor level satisfies (QL9), and the interpolation argument does not select an element of the source's prescribed translated family or a prescribed global row-degree sequence. In particular the theorem is not a cost comparison proving or obstructing a shorter lift chain. It narrows that question to the actual section norm/height, family, selected-weight and global admissibility requirements.

## 9. Sources and check record

The two additional known projective facts are cited at their exact official Stacks Project locators: Lemma 29.40.4, Tag 01VT, for a relatively very ample power; Proposition 28.27.13(7), Tag 01Q3, for generation of every sufficiently large power. Their official statements were directly opened and read in this pass. The formal-coordinate inversion and polynomial homogenization are proved above.

The actual model and positive-sign ampleness are DP49 and DP54. The exact logarithm profile and arbitrary-unit invariance are DP46; the full common-weight logarithm estimate and harmonic sharpness are DP51, including its §6 corollary. Flat base change in (QL27) is the same Stacks Project Lemma 30.5.2(2), Tag 02KH, already read for DP54.

Actual full-proof reading events, snapshots and hashes are recorded separately. No numerical experiment, Lean execution or machine formalization is claimed.
