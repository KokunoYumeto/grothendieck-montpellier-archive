# DP48: rational quadratic gauges cannot improve the primitive mixed-line slope

Date: 2026-11-21 UTC. Author: /root, GPT-6 Astra Pro; runtime reasoning effort not exposed. This is a local consequence of the complete DP41 and DP42 proofs. It concerns an ordinary logarithmic line, not a general harmonic projection.

## Statement

Use all hypotheses and notation of DP42: odd prime \(p\), \(h\ge3\), the invariant primitive kernel, an unramified coefficient ring \(\mathcal O\), unit line coefficient \(u\), primitive dual vector \(\mathbf v\), active restricted-\(p\) length \(k\), and a nonzero restriction
\[
V(t)=U(E_0(ut),E_H(\mathbf vt))
\]
of an integral formal function. Put \(s=1/(p-1)\) and \(w_k=sp^k/(p^k+1)\). Let \(\lambda\in\mathcal O^\times\) and \(c\in K=\operatorname{Frac}(\mathcal O)\), and define
\[
\Theta_c(t)=V(t)\exp\bigl(\lambda\beta(ut,\mathbf vt)+ct^2\bigr)
           =\sum_{n\ge0}a_nt^n.
\]
If \(c=0\), set \(r_c=-\infty\); otherwise set
\[
r_c=\frac{s-v_p(c)}2,\qquad R_c=\max\{w_k,r_c\}.
\]
Then for every rational \(w\ge0\),
\[
\nu_w(\Theta_c)=
\begin{cases}
-\infty,&w<R_c,\\
\nu_w(V)\in[0,\infty),&w\ge R_c.
\end{cases}
\]
Consequently
\[
v_p(n!a_n)\ge (s-R_c)n-\frac{s_p(n)}{p-1},
\qquad
\liminf_{n\to\infty}\frac{v_p(n!a_n)}n=s-R_c.
\]

An integral quadratic coefficient \(c\) leaves DP42's sharp slope unchanged. A nonintegral coefficient strictly worsens it: if \(v_p(c)=-M\), \(M\ge1\), then
\[
R_c=\frac{s+M}{2}>w_k,\qquad
\liminf_n\frac{v_p(n!a_n)}n=\frac{s-M}{2}<0.
\]
Thus no rational quadratic gauge improves the primitive-path slope over the stated unramified field.

## Complete proof

The case \(c=0\) is DP42. Suppose \(c\ne0\) and write \(m=v_p(c)\in\mathbb Z\); integrality of this valuation is used below.

First suppose \(m\ge0\). Then
\[
r_c=(s-m)/2\le s/2<w_k,
\]
because \(p^k/(p^k+1)>1/2\). For every \(w\ge w_k\), both exponential factors are integral after scaling \(t=\gamma T\), \(v_p(\gamma)=w\): DP42 proves this for the primitive factor, and the quadratic exponent has valuation \(m+2w\ge s\). The factorial estimate proves that \(\exp(c\gamma^2T^2)\) and its inverse are integral, both with coefficient infimum zero. The prefactor is integral and nonzero. Gauss multiplicativity therefore gives the claimed finite value \(\nu_w(V)\).

Choose rational \(w<w_k\) sufficiently close to \(w_k\) that \(w\ge r_c\) and \(w\) lies in DP42's explicit lower interval. At that weight DP42 proves that \(V\exp(\lambda\beta)\) has unbounded coefficients. Multiplication by the integral quadratic exponential cannot make it bounded: its inverse is integral as well, and would then make the original product bounded. Thus \(\nu_w(\Theta_c)=-\infty\) for all such \(w\). Monotonicity of weighted coefficient infima yields the same conclusion at every smaller nonnegative weight. This proves the exact threshold \(R_c=w_k\) in this case.

Now suppose \(m=-M\le-1\). Since \(p\) is odd, \(0<s\le1/2\), so
\[
r_c=(s+M)/2\ge(s+1)/2>s>w_k.
\]
At every \(w\ge r_c\), DP42 makes the primitive exponential integral with coefficient infimum zero, and the quadratic exponential is integral because its exponent has infimum \(m+2w\ge s\). The prefactor is integral and nonzero. Multiplicativity gives the claimed finite equality again.

For rational \(w<r_c\) sufficiently close to \(r_c\), we have \(w>w_k\) and
\[
0\le t_c:=m+2w<s.
\]
Thus \(f(T)=V(\gamma T)\exp(\lambda\beta(u\gamma T,\mathbf v\gamma T))\) is a nonzero bounded series. The initial form of \(z(T)=c\gamma^2T^2\) is a nonzero scalar multiple of \(T^2\), whose derivative is nonzero because \(p\) is odd. DP41's fraction-field multiplier lemma applies to \(z\) and \(f\); hence \(f\exp z\) has unbounded coefficients. Monotonicity extends that conclusion to every \(w<r_c\). This establishes the threshold \(R_c=r_c\).

At \(w=R_c\), integrality gives \(v_p(a_n)\ge-R_cn\). If \(\liminf v_p(a_n)/n>-R_c\), some rational \(w<R_c\) would give bounded weighted coefficient infimum, contradicting the already proved threshold. Therefore \(\liminf v_p(a_n)/n=-R_c\). Legendre's formula gives both the uniform factorial inequality and the exact liminf. This proves every assertion. \(\square\)

## Canonical-gauge application and exact scope

The recovered canonical-gauge independence interface says that two canonical logarithmic gauges differ by an adjoint-balanced symmetric biadditive form. After formal logarithms it is bilinear; after a linear logarithmic path and the pullback by the fixed linear endomorphism \(w_0\), its diagonal is a scalar \(ct^2\). Thus, **once** the prescribed geometric expression has been identified with the primitive mixed kernel up to this canonical-gauge ambiguity and an integral prefactor, DP48 applies. It does not supply that geometric identification.

The exact source interface is CocycleRightZeroThd.lean, FB.IsCanonGauge174–183 and hL185; the difference and selected-value theorem are the already read CanonGaugeIndependenceAll.lean, GlobalTheory.canonGauge_independence_all23–26, with the full trace in theta_normalization_harmonic_trace.md. Known source theorems are cited rather than reproved here. The new radius calculation is proved in full above.

The scalar result does not assert equality of arbitrary harmonic projections under the quadratic change. The source's precise annihilation condition remains necessary for its selected-value invariance theorem. The hypothesis that \(c\) belongs to the unramified coefficient field makes the two strict cases exhaustive. No claim about a ramified quadratic coefficient or a zero prefactor restriction is made in this statement.

