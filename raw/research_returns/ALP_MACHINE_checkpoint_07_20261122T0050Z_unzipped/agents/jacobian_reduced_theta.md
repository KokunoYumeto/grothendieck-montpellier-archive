# AM-K012–016 — actual reduced theta germs and derivative bounds on y²=x⁷−1

Author: GPT-6 Astra Pro, ALP_MACHINE agent /root/kummer_extension, 21 November 2026 UTC. This note supplies actual germs on the specified Jacobian. The accepted Alpöge theorem is not re-examined. The distinction between the translated non-effective characteristic and the source trace-one line is maintained.

## 0. Statements and conventions

Let \(E=\mathbb Q(\zeta)\), \(\zeta=\zeta _7\), and
\[
C:y^2=x^7-1,\quad J=\operatorname{Jac}(C),\quad
\omega_i=x^{i-1}dx/y,\quad u_i=\int\omega_i\quad(1\leq i\leq3).
\]
Write \(P_a=(\zeta^a,0)\). The translated characteristic is \(D=P_1+P_3+P_5-\infty\). Its value-one Chern-reduced germ is AM-R-004's
\[
F(u)=e^{\pi z^tY^{-1}z/2}\frac{\theta(z,\tau)}{\theta(0,\tau)},
\qquad z=P^{-1}u,\quad Y=\operatorname{Im}\tau.
\tag{K12.1}
\]
ALP-LIFT-07 identifies this characteristic exactly and proves that the value-one normalization is primitive at every odd good prime. The source trace-one line is instead \(L_\infty=L_{2\infty}\). Let \(s_q\) denote its theta section normalized by the determinant-of-cohomology tangent cone
\[
q(u)=u_1u_3-u_2^2.
\]
Its Chern-reduced germ is denoted \(\sigma_q(u)\). ALP-LIFT-08 identifies this exact scalar normalization with an actual primitive section at every \(p\nmid14\).

A “Hurwitz coefficient” means \(\partial^\alpha f(0)\), so \(f=\sum_\alpha\partial^\alpha f(0)u^\alpha/\alpha!\). It does **not** mean the divided Taylor coefficient. Valuations satisfy \(v_{\mathfrak p}(p)=1\).

The results are:

1. **AM-K012.** The canonical Schiffer bidifferential equals the explicit algebraic Baker bidifferential. Consequently \(F\) is precisely the Baker even sigma function for \(D\), with no unrecorded quadratic exponential. An algebraic recursion determines all its Hurwitz coefficients, which belong to \(\mathcal O_E[1/14]\). In particular
   \[
   \partial_1\partial_3F(0)=-\zeta^2/4.
   \tag{K12.2}
   \]
2. **AM-K013.** At every prime above 11,
   \[
   v_{\mathfrak p}(\partial_i^nF(0))
   \geq\max\left\{0,c_in-\frac{s_{11}(n)}{10}\right\},
   \quad c_1=c_3=\frac1{20},\quad c_2=\frac1{220}.
   \tag{K13.1}
   \]
   Here \(s_p(n)\) is the base-\(p\) digit sum. The proof uses a stable integral ring for the actual logarithmic Hessian and three finite exact coefficient checks.
3. **AM-K014.** The actual source-line germ is
   \[
   \sigma_q(u)=4\sigma(u_1/2,u_2/2,u_3/2),
   \tag{K14.1}
   \]
   where \(\sigma\) is the algebraically normalized \((2,7)\) sigma function in half-differential coordinates. An explicit integer determinant formula determines every coefficient. Thus \(\partial^\alpha\sigma_q(0)\in2^{2-|\alpha|}\mathbb Z\). It is even, has CM weight 4 modulo 7, and
   \[
   \partial_1\partial_3\sigma_q(0)=1,\quad
   \partial_2^2\sigma_q(0)=-2,\quad
   \partial_1^4\sigma_q(0)=2,\quad
   \partial_3^6\sigma_q(0)=1.
   \tag{K14.2}
   \]
4. **AM-K015.** The bounds (K13.1) hold for \(\sigma_q\) too, by the actual integral algebraic ratio
   \[
   \sigma_q(2u)=r(u)F(2u).
   \tag{K15.1}
   \]
   Pullback by \([2]\) trivializes the two-torsion difference of the lines. This is a comparison of germs; the final section belongs to \(L_\infty\), and no even value is inserted into the source's odd Level.M.
5. **AM-K016.** Each actual pure restriction \(f_i(t)=\sigma_q(te_i)\) is an entire function of order 2 and exact type \(\pi/(2G_i)\). Its nonzero coefficient orders form an infinite computable sequence \(n_{i,k}\) satisfying \(n_{i,k+1}/n_{i,k}\to1\), within the necessary congruence class in (K14.11). The coefficient limsup is
   \[
   \limsup_{n\to\infty}
     \left(\frac{|\partial_i^n\sigma_q(0)|}{\sqrt{n!}}\right)^{1/n}
     =\sqrt{\pi/G_i}.
   \tag{K16.1}
   \]
   The support and growth assertions are archimedean; they do not bound finite-place valuations above.

These statements do not establish nonvanishing in every admissible degree, identify a prescribed automorphic harmonic row, or prove the terminal every-\(\varepsilon\) window.

## 1. AM-K012: identify the actual reduced frame

Set \(f(x)=x^7-1\) and \(\mathcal F(x,z)=x^3z^3(x+z)-2\). The Baker fundamental bidifferential is
\[
\Omega_B(P,Q)=
\frac{\mathcal F(x,z)+2y(P)y(Q)}
 {4(x-z)^2y(P)y(Q)}\,dx\,dz.
\tag{K12.3}
\]
The \(2y(P)y(Q)\) term removes a spurious pole on the conjugate diagonal. This symmetric differential has diagonal leading term \(dt_Pdt_Q/(t_P-t_Q)^2\) and no other poles. Exact general formulas: Buchstaber, Enolskii, and Leykin (1997), §1.2, equations (1.7)–(1.9); Edelstein, Gómez-Reino, and Mariño (2001), equations (3.3)–(3.6).

Let \(B_0\) be the normalized fundamental bidifferential with zero \(a\)-periods and let \(\nu=P^{-1}\omega\) be the column of normalized holomorphic differentials. The Schiffer bidifferential is
\[
\Omega_S=B_0-\pi\nu(P)^tY^{-1}\nu(Q).
\tag{K12.4}
\]
It is independent of the symplectic marking. Its period relation pairs its periods with those of the intrinsic Bergman reproducing kernel and characterizes it without a marking. Shramchenko (2004), §4, printed p.1468, gives (K12.4) and these period relations. Thus every curve automorphism preserves \(\Omega_S\).

The automorphism \(a:(x,y)\mapsto(\zeta x,y)\) preserves (K12.3): \(\mathcal F\) has only terms of degree 7 and a constant, and \(dx\,dz/(x-z)^2\) is invariant. Moreover \(a^*\omega_i=\zeta^i\omega_i\). The difference \(\Omega_B-\Omega_S\) is a global holomorphic bidifferential, hence a linear combination of \(\omega_i(P)\omega_j(Q)\). Every term has weight \(i+j\in\{2,3,4,5,6\}\), none divisible by 7. Invariance forces every coefficient to vanish:
\[
\boxed{\Omega_B=\Omega_S.}
\tag{K12.5}
\]
This uniqueness proof makes no inference about finite-place integrality from a Hodge splitting.

The quadratic normalization includes a factor of two. If Baker's sigma theta expression has exponential \(e^{u^tKu}\), its normalized bidifferential is
\[
B_0=\Omega_B+2\omega(P)^tK\omega(Q).
\]
This follows by taking \(a\)-periods of the second-kind differential identity, equivalently Edelstein et al., equations (3.14)–(3.18). Comparison gives
\[
2K=\pi P^{-t}Y^{-1}P^{-1}.
\tag{K12.6}
\]
Hence the exponential is exactly \(e^{\pi z^tY^{-1}z/2}\). The characteristic is zero by ALP-LIFT-07, and normalization at zero divides by \(\theta(0,\tau)\). This proves (K12.1). The same calculation applies to the characteristic \(2\infty\).

## 2. Actual algebraic logarithmic Hessian and recursion

Let \(a_1=\zeta,a_2=\zeta^3,a_3=\zeta^5\). Near the ordered divisor \(((a_1,0),(a_2,0),(a_3,0))\), put
\[
U(X)=\prod_j(X-x_j),\qquad
\ell_j(X)=\frac{\prod_{m\ne j}(X-x_m)}{U'(x_j)}
         =\sum_{i=1}^3q_{ji}X^{i-1}.
\]
The matrix \(q\) is the inverse of \(V_{ij}=x_j^{i-1}\). The invariant derivatives are
\[
D_ix_j=y_jq_{ji},\qquad D_iy_j=\tfrac72x_j^6q_{ji}.
\tag{K12.7}
\]
The first formula inverts \(\sum_jx_j^{k-1}dx_j/y_j=du_k\); the second differentiates \(y_j^2=x_j^7-1\). They are regular at the branch points. The \(D_i\) commute because they lift the commuting invariant derivatives on \(J\).

Let \(s_1=\sum x_j,s_2=\sum_{j<m}x_jx_m,s_3=x_1x_2x_3\). The symmetric Kleinian matrix \(W\) is determined by
\[
W_{33}=s_1/4,\quad W_{23}=-s_2/4,\quad W_{13}=s_3/4
\tag{K12.8}
\]
and
\[
\sum_{i,k}W_{ik}x_j^{i-1}x_m^{k-1}
=\frac{\mathcal F(x_j,x_m)-2y_jy_m}{4(x_j-x_m)^2},
\qquad j<m.
\tag{K12.9}
\]
These are Buchstaber et al. (1997), Corollary 2.1.2, equation (2.9), and Theorem 2.2, equations (2.10)–(2.14). Their canonical model has leading coefficient 4. Passing from \(Y^2=4(x^7-1)\), \(du^{\rm can}=dx/Y\), to our \(u=2u^{\rm can}\) divides the logarithmic Hessian by 4 and gives exactly these factors.

After the last row is inserted, the unknowns \(W_{11},W_{12},W_{22}\) have coefficient rows \((1,x_j+x_m,x_jx_m)\). The determinant is a signed product of the three differences. Here is explicit elimination:
\[
\begin{split}
R_{jm}={}&\frac{\mathcal F(x_j,x_m)-2y_jy_m}{4(x_j-x_m)^2}
-W_{13}(x_j^2+x_m^2)\\
&-W_{23}(x_j^2x_m+x_jx_m^2)-W_{33}x_j^2x_m^2,\\
t_1={R_{13}-R_{12}\over x_3-x_2},\qquad
t_2={R_{23}-R_{12}\over x_3-x_1}.
\end{split}
\]
Then
\[
W_{22}={t_1-t_2\over x_1-x_2},\quad W_{12}=t_1-x_1W_{22},\quad
W_{11}=R_{12}-(x_1+x_2)W_{12}-x_1x_2W_{22}.
\tag{K12.10}
\]

For \(h=\log F\), \(h(0)=0\), the characteristic translation gives
\[
\partial_i\partial_jh(u)=-W_{ij}(a+u),
\quad a=\operatorname{AJ}(P_1+P_3+P_5-3\infty).
\tag{K12.11}
\]
This is the Hessian of the specified actual theta germ. Translating changes an affine exponential only, whose Hessian is zero; evenness and \(F(0)=1\) fix the first and zeroth derivatives. Thus (K12.11) determines \(F\) uniquely.

### Stable integral ring

Let \(R_0=\mathcal O_E[1/14]\), and
\[
\mathcal R=R_0[x_1,x_2,x_3,y_1,y_2,y_3,
(x_1x_2x_3\prod_{j<m}(x_j-x_m))^{-1}]
/(y_j^2-x_j^7+1)_{j=1}^3.
\tag{K12.12}
\]
Every \(D_i\) preserves this ring, by (K12.7), the quotient rule, and differentiation of the defining relations. Every \(W_{ij}\) belongs to it. Evaluation \(e:\mathcal R\to R_0\) at \((x_j,y_j)=(a_j,0)\) is defined: these roots are units, and root differences have prime divisors only above 7.

The Abel map from this ordered-divisor open set to \(J\) is étale. In a branch chart the local parameters \(y_j\) give the differential matrix
\[
\left(2x_j^{i-1}/(7x_j^6)\right)_{ij},
\]
with invertible determinant. At nonbranch points use \(x_j\); the same Vandermonde criterion applies. This concerns algebraic formal coordinates on \(J\); it is **not** a claim that the Abelian logarithms \(u_i\) are integral formal parameters.

For \(|\alpha|\geq2\), choose \(i,j\) with \(\alpha-e_i-e_j\geq0\). Then
\[
h_\alpha:=\partial^\alpha h(0)
=-e(D^{\alpha-e_i-e_j}W_{ij})\in R_0.
\tag{K12.13}
\]
The result is independent of the choice by the Kleinian Hessian identity. Also \(h_0=h_{e_i}=0\). If \(S_\alpha=\partial^\alpha F(0)\), then
\[
S_0=1,\qquad
S_\alpha=\sum_{0\leq\beta\leq\alpha-e_i}
{\alpha-e_i\choose\beta}h_{\beta+e_i}S_{\alpha-e_i-\beta}
\quad(\alpha_i>0).
\tag{K12.14}
\]
This is \(\partial_iF=F\partial_ih\). It involves integer binomial coefficients and no division by an order, proving \(S_\alpha\in R_0\).

### Initial matrix and checks

Let \(Q(X)=\prod_{a\in\{1,3,5\}}(X-\zeta^a)\), \(R(X)=f(X)/Q(X)\). Bolza's formula is
\[
\sum_{i,j}W_{ij}(a)X^{i-1}Z^{j-1}
=\frac{\mathcal F(X,Z)-Q(X)R(Z)-Q(Z)R(X)}{4(X-Z)^2}.
\tag{K12.15}
\]
See Edelstein et al. (2001), equation (3.24), reversing their descending basis. Explicitly, \(4W(a)\) is
\[
\begin{pmatrix}
-\zeta^5-\zeta^4-2\zeta^2+\zeta-2&\zeta^3+1&\zeta^2\\
\zeta^3+1&-2\zeta^4+\zeta^3-\zeta^2+\zeta-2&
\zeta^5+\zeta^3+\zeta^2+1\\
\zeta^2&\zeta^5+\zeta^3+\zeta^2+1&\zeta^5+\zeta^3+\zeta
\end{pmatrix}.
\tag{K12.16}
\]
This proves (K12.2). Exact polynomial division modulo \(\Phi_7\) is checked in jacobian_theta_hessian_check.py.

A separate numerical diagnostic, not a proof premise, used 65-digit independent theta summation with AM-R-004's periods. Its Hessian agrees with \(-W(a)\) to \(6.85\cdot10^{-66}\). Pure jets of orders 2,4,6,8 agree with the independent flow/Bell recurrence, largest observed discrepancy \(4.55\cdot10^{-64}\). Results and diagnostic scope are retained in jacobian_theta_hessian_check.json.

## 3. AM-K013: invariant-derivative nilpotence and actual logarithmic bounds

Fix an odd prime \(p\ne7\) and complete \(R_0\) at a prime above \(p\). The reduction is a smooth abelian variety with the order-seven automorphism. The \(D_i\) form an integral invariant basis, with distinct CM labels \(i\in\{1,2,3\}\).

In characteristic \(p\), the \(p\)-fold composition of a derivation is a derivation, because the intermediate binomial coefficients in the Leibniz formula vanish. Translation invariance is retained. The CM weight is multiplied by \(p\), so a label \(pi\bmod7\) outside \(\{1,2,3\}\) forces \(D_i^p=0\). If the label is inside this set, \(D_i^p\) is a scalar multiple of its uniquely labelled invariant derivative. Iteration gives
\[
D_i^{q_i}=0\text{ on the special fibre},\qquad q_i=p^{h_i},
\tag{K13.2}
\]
with these sufficient exponents:

| \(p\bmod7\) | \(h_1\) | \(h_2\) | \(h_3\) |
|---|---:|---:|---:|
| 2 | 2 | 1 | 1 |
| 3 | 3 | 1 | 2 |
| 4 | 1 | 2 | 1 |
| 5 | 1 | 3 | 2 |
| 6 | 1 | 1 | 1 |

For \(p\equiv1\bmod7\), this argument supplies no exponent. The table is obtained by multiplying a label successively by \(p\bmod7\) until it leaves \(\{1,2,3\}\); no classification of the Newton polygon is needed.

Because the Abel map in §2 is étale, the zero derivation on the target has only the zero lift. Thus (K13.2) holds on \(\mathcal R/p\mathcal R\), and
\[
D_i^{q_i}\mathcal R\subset p\mathcal R.
\tag{K13.3}
\]
This is an operator assertion on a stable integral ring. Since \(D_i\mathcal R\subset\mathcal R\) and \(D_i(p)=0\), it may genuinely be iterated:
\[
D_i^m\mathcal R\subset p^{\lfloor m/q_i\rfloor}\mathcal R.
\tag{K13.4}
\]
For \(\ell_n=\partial_i^n\log F(0)\), applying this to \(W_{ii}\) gives
\[
v_{\mathfrak p}(\ell_n)\geq
\max\{0,\lfloor(n-2)/q_i\rfloor\}\quad(n\geq2).
\tag{K13.5}
\]
Also \(\ell_n=0\) for odd \(n\).

### Bell–Legendre lemma, with all losses

Let \(p\) be odd, \(q=p^h\), and
\[
H(t)=\sum_{j\geq2}\ell_jt^j/j!,\qquad
e^{H(t)}=\sum_{n\geq0}S_nt^n/n!.
\]
Suppose \(H\) is even, all \(\ell_j\) are integral, and (K13.5) holds. Then
\[
v(S_n)\geq
\max\left\{0,\frac{n}{(p-1)(q+1)}-\frac{s_p(n)}{p-1}\right\}.
\tag{K13.6}
\]
If additionally \(v(\ell_{q+1})\geq1\), then
\[
v(S_n)\geq
\max\left\{0,\frac{n}{2p^{h-1}(p-1)}-\frac{s_p(n)}{p-1}\right\}.
\tag{K13.7}
\]

To prove this, a complete Bell-polynomial term, indexed by \(m_j\geq0\), \(\sum jm_j=n\), is
\[
\frac{n!}{\prod_jm_j!(j!)^{m_j}}\prod_j\ell_j^{m_j}.
\]
Only even \(j\) occur. Legendre's formula bounds its valuation below by
\[
-\frac{s_p(n)}{p-1}
+\sum_jm_j\left(v(\ell_j)+\frac{s_p(j)-1}{p-1}\right)
+\frac{\sum_js_p(m_j)}{p-1}.
\tag{K13.8}
\]
The final summand is nonnegative.

For (K13.6), even \(j>0\) has \(s_p(j)\geq2\). If \(j\leq q+1\), then
\((p-1)v(\ell_j)+s_p(j)-1\geq1\geq j/(q+1)\).
If \(j\geq q+3\), put \(k=\lfloor(j-2)/q\rfloor\geq1\). Since \(j\leq(k+1)q+1\),
\[
(p-1)v(\ell_j)+s_p(j)-1\geq(p-1)k+1\geq j/(q+1).
\]
Insert this into (K13.8). Integrality supplies the maximum with zero.

For (K13.7), if \(2\leq j<q\), then \(j\leq p^{h-1}s_p(j)\), while \(s_p(j)-1\geq s_p(j)/2\). Thus the lower bound is \(j/(2p^{h-1})\). The sole even gap is \(j=q+1\): the additional assumption gives a lower bound at least \(p\), larger than \((q+1)/(2p^{h-1})\). For \(j\geq q+3\), retain \(k=\lfloor(j-2)/q\rfloor\). If \(k=1\), evenness gives \(j\leq2q\), so the lower bound \(p\) suffices. If \(k\geq2\),
\[
(p-1)k+1-\frac{(k+1)q+1}{2p^{h-1}}
=\left(\frac p2-1\right)k+1-\frac p2-\frac1{2p^{h-1}}\geq0.
\]
This holds for \(p\geq3,k\geq2,h\geq1\); its smallest case \(p=3,k=2,h=1\) is zero. Substitution into (K13.8) proves (K13.7).

Therefore (K13.6) is already an unconditional directional lower bound for the actual translated theta at every residue class in the table, including \(p\equiv3,5\bmod7\).

### Exact finite certificate for the improved 11-adic constants

At \(p=11\), \(q_1=q_3=11\) and \(q_2=121\). The only additional checks needed are
\[
\partial_1^{12}\log F(0)\equiv0,\qquad
\partial_3^{12}\log F(0)\equiv0,\qquad
\partial_2^{122}\log F(0)\equiv0\pmod{11}.
\tag{K13.9}
\]
All three were verified by exact arithmetic in
\[
B=\mathbb F_{11}[Z]/(1+Z+\cdots+Z^6),
\]
the product of the two residue fields above 11. Zero in \(B\) proves zero at both primes.

The reproducible recurrence is jacobian_theta_direction_jets.py. Its inputs are (K12.7)–(K12.10). To avoid power-series division, add \(z_{jm}=(x_j-x_m)^{-1}\) with
\[
D_iz_{jm}=-z_{jm}^2(D_ix_j-D_ix_m).
\]
This is a polynomial differential system over \(B\). The \(n\)-th Hurwitz coefficient of a product is \(\sum_{k=0}^n\binom nk a_kb_{n-k}\). The coefficient of order \(n\) in a variable's prescribed derivative gives its coefficient of order \(n+1\), with no division by \(n+1\). Initial branch-difference inverses are obtained by Euclidean polynomial inversion modulo \(\Phi_7\). Finally \(\ell_{n+2}=-D_i^nW_{ii}|_a\).

The executed command was:

    python work/agents/jacobian_theta_direction_jets.py --prime 11 --order 160 --output jacobian_theta_direction_jets_mod11.json

It retains all nonzero coefficient vectors. In each of (K13.9), all six coordinates in \(1,Z,\ldots,Z^5\) are zero. The companion jacobian_theta_11_certificate.py checks the saved tables, checks the unit status of the retained coefficients, and regenerates the three exceptional coefficients using the stated recurrence.

The operator proof (K13.3)–(K13.5), the three exact checks, and (K13.7) now prove (K13.1) for every \(n\). The finite computation is used only for these three coefficients; no pattern is extrapolated.

There are exact all-order mod-11 consequences as well. In the reduced one-variable Hurwitz algebra, \(b^{11}=b(0)^{11}\): a positive divided-power monomial has zero 11-th power, as follows from \(v_{11}((11k)!/(k!)^{11})=s_{11}(k)>0\). The universal Bell/Jacobson identity is
\[
\partial^{11}e^H/e^H=(H')^{11}+\partial^{11}H.
\]
Iteration gives \(\partial^{11^h}e^H/e^H=\partial^{11^h}H\), since each constant \(H^{(11^j)}(0)\) is zero by evenness. Formula (K13.3) kills the logarithmic derivatives of orders at least \(q_i+2\) modulo 11; (K13.9) and oddness supply the two preceding orders. Hence
\[
\partial_1^nF(0)\equiv\partial_3^nF(0)\equiv0\ (n\geq11),
\qquad\partial_2^nF(0)\equiv0\ (n\geq121).
\tag{K13.10}
\]
This establishes a first congruence only. Repeated valuation gain in (K13.1) comes instead from the stable-ring estimate (K13.4) and the Bell lemma.

## 4. AM-K014: an explicit determinant formula for the actual source sigma

The standard theta divisor based at infinity is \(W_2\), hence its line is \(L_{2\infty}\). Buchstaber et al. (1997), Definition 1 and equation (2.2), printed pp.7–8, normalize its Baker sigma by initial homogeneous term \(v_1v_3-v_2^2\) in the canonical half-differential coordinates. The construction below fixes the whole series and its sign, including the non-leading terms.

Use the integral arithmetic parameter \(t=-x^3/y\) at infinity. There is a unique \(A\in1+t^{14}\mathbb Z[[t^{14}]]\) satisfying
\[
A=1-t^{14}A^7,\qquad x=t^{-2}A^{-1},\qquad y=-t^{-7}A^{-3}.
\tag{K14.3}
\]
Substitution verifies both the curve equation and \(t=-x^3/y\). Coefficients of \(A\) are recursively determined without division, and all inverse powers \(A^{-m}\) are integral. With \(T=t^{14}\),
\[
[T^0]A^{-m}=1,\qquad
[T^k]A^{-m}=\frac m k(-1)^{k-1}{7k-m-1\choose k-1}\quad(k\geq1).
\tag{K14.4}
\]
For \(m=0,k>0\) this is zero. Formula (K14.4) is Lagrange inversion applied to \(1-A=T A^7\); its expression is an integer because \(A^{-m}\in\mathbb Z[[T]]\). The division in this closed expression may be avoided entirely by the recursion (K14.3).

Let the increasing nongaps be
\[
n_1,n_2,\ldots=0,2,4,6,7,8,9,\ldots .
\]
For even \(n=2k\), take \(\phi_n=x^k\); for odd \(n=2k+7\), take \(\phi_n=-x^ky\). Then
\[
t^2\phi_n=t^{2-n}A^{-\lfloor n/2\rfloor}.
\tag{K14.5}
\]
Thus the basis of \(t^2H^0(C-\{\infty\},\mathcal O_C)\) has leading exponents
\[
2,0,-2,-4,-5,-6,\ldots ,
\]
corresponding to the partition \(\lambda=(3,2,1)\).

Here is a finite algorithm for every coefficient. For any partition \(\mu\), choose \(L\geq\max(3,\operatorname{length}\mu)\), append zeros to \(\mu\), and define
\[
\xi_\mu=
\det\left([t^{\,\mu_i-i-(2-n_j)}]\,
A(t)^{-\lfloor n_j/2\rfloor}\right)_{1\leq i,j\leq L}.
\tag{K14.6}
\]
A negative power or a power not divisible by 14 has coefficient zero. Enlarging \(L\) adds an upper triangular identity tail and leaves the determinant unchanged. Each \(\xi_\mu\) is therefore an explicitly computable integer. It vanishes unless \(\mu\geq(3,2,1)\) and \(|\mu|=6+14k\) for some \(k\geq0\); \(\xi_{321}=1\).

Define polynomials \(p_m\) by
\[
\sum_{m\geq0}p_m(v)z^m
=\exp(v_3z+v_2z^3+v_1z^5),\quad p_m=0\ (m<0),
\]
and put
\[
S_\mu(v)=\det(p_{\mu_i-i+j}(v))_{1\leq i,j\leq L}.
\]
Then the actual Baker sigma is
\[
\boxed{\sigma(v_1,v_2,v_3)=\sum_\mu\xi_\mu S_\mu(v).}
\tag{K14.7}
\]
This is Nakayashiki's tau/sigma theorem, specialized explicitly: Nakayashiki (2010), §§4–5, equation (7), and Theorem 8; for the arithmetic parameter version, Ônishi (2015), Theorem 6.5. The affine-ring embedding is shifted by \(g-1=2\), exactly as in (K14.5), not by an unspecified convention. The monomial frame is upper unitriangularly equivalent to the normalized frame and has identical Plücker coordinates. Formula (K14.6) is its finite determinant.

We verify why there is no omitted exponential or coordinate correction in this specialization. The half-differentials \(x^{i-1}dx/(2y)\) have leading terms \(t^{6-2i}dt\); all later terms have exponents shifted by multiples of 14. Hence the gap-coordinate submatrix \(B\), at gaps \(1,3,5\), is the identity after the displayed reversal. The linear correction coefficients \(c_w\) vanish at these gaps because the square-root logarithm of the normalized highest differential contains powers only \(t^{14k}\). Likewise the regular coefficients \(q_{ij}\) of \(\Omega_B-dt_1dt_2/(t_1-t_2)^2\) vanish unless \(14\mid i+j\). Indeed the combination of \(a\) and the hyperelliptic involution acts on \(t\) by the primitive fourteenth root \(-\zeta^3\) and preserves \(\Omega_B\). For \(i,j\in\{1,3,5\}\), \(i+j\leq10\), so every retained \(q_{ij}\) vanishes. These are exactly the exponential corrections in the tau/sigma theorem.

Ônishi and Nakayashiki sometimes use \(-x^{i-1}dx/f_y\) rather than \(+x^{i-1}dx/(2y)\). Applying their convention to the identical model with \(Y=-y\) makes these differentials exactly ours. Equivalently a simultaneous sign of all three coordinates has no effect because the genus-three sigma here is even. The leading Schur polynomial fixes the remaining overall sign.

Every desired monomial has one finite weight \(5\alpha_1+3\alpha_2+\alpha_3\), so only finitely many partitions contribute to its coefficient in (K14.7). This is a checkable all-order construction of this particular function.

Each Schur polynomial in exponential times is Hurwitz integral: equivalently its coefficient of \(\prod_jT_j^{m_j}/m_j!\) is the integral symmetric-group character at cycle type \(1^{m_1}2^{m_2}\cdots\). One may instead use Ayano (2024), Lemma 7.2, or Ônishi (2015), Theorem 1.8. Since the \(\xi_\mu\) are integers, (K14.7) is Hurwitz integral over \(\mathbb Z\). Changing to \(u=2v\) and multiplying by 4 proves
\[
\partial^\alpha\sigma_q(0)\in2^{2-|\alpha|}\mathbb Z.
\tag{K14.8}
\]
This includes 7-adic integrality in the original, nonprimitive at 7, \(\omega\)-coordinates. It does not contradict ALP-LIFT-08's finite scalar content in primitive coordinates.

By (K12.5), the Baker gauge is the actual Chern-reduced gauge for this characteristic. The leading quadratic is \(q\); the principal theta space is one-dimensional. Thus (K14.1) agrees with the actual \(q\)-normalized section of ALP-LIFT-08, not merely with an abstractly isomorphic line.

### Leading coefficients and selection

The weight-six term of (K14.7) is
\[
S_{321}(v)=v_1v_3-v_2^2-\tfrac13v_2v_3^3+\tfrac1{45}v_3^6.
\tag{K14.9}
\]
All subsequent weights are \(6+14k\). At weight 20, the coefficient of \(v_1^4\) is \(1/3\). This follows directly from (K14.6), or from the first-order frame shifts \(r\mapsto r+14\). In the latter calculation the only nonzero contributions after setting \(v_2=v_3=0\) are
\[
(-1)(-1/6)+3(-1/2)+(-6)(-1/2)+8(-1/6)=1/3.
\]
These terms come respectively from the partitions
\((15,4,1)\), \((10,4,3,2,1)\),
\((5,4,3,2,1^6)\), and \((3,2,2,2,1^{11})\).
The script jacobian_sigma_determinant_certificate.py checks these values without using the shift shortcut. It evaluates (K14.6) for all 627 partitions of 20, checks two extra identity-tail sizes for every nonzero coordinate, and computes the Schur determinants exactly. The retained JSON contains all 13 nonzero weight-20 Plücker coordinates and the four nonzero contributions above. It also checks (K14.9) symbolically and all four jets in (K14.2).

Consequently the beginning contains
\[
\sigma_q(u)
=u_1u_3-u_2^2-\frac1{12}u_2u_3^3
+\frac1{720}u_3^6+\frac1{12}u_1^4
+\text{other terms of weights at least 20}.
\tag{K14.10}
\]
In this notation \(u_1,u_2,u_3\) have weights \(5,3,1\); the displayed \(u_1^4\) is the indicated weight-20 term, and the last phrase excludes it. This proves (K14.2).

Every monomial is even in total degree, and its CM weight
\(\alpha_1+2\alpha_2+3\alpha_3\) is \(4\bmod7\), since
\[
\alpha_1+2\alpha_2+3\alpha_3
\equiv3(5\alpha_1+3\alpha_2+\alpha_3)\equiv18\equiv4\pmod7.
\]
Thus the necessary pure-direction congruences are
\[
n\equiv4\pmod{14}\ (i=1),\qquad
n\equiv2\pmod{14}\ (i=2),\qquad
n\equiv6\pmod{14}\ (i=3).
\tag{K14.11}
\]
These are selection rules, not assertions that every permitted coefficient is nonzero.

## 5. AM-K015: transfer to the actual source section

Fix \(p\nmid14\). On the good abelian scheme, the rigidified line difference is
\[
L_D^{\rm rig}=L_\infty^{\rm rig}\otimes\mathcal P_T,\qquad 2T=0.
\]
The canonical rigidified Poincaré isomorphism gives
\([2]^*\mathcal P_T\simeq\mathcal P_{2T}\simeq\mathcal O\), integrally. Hence the two pulled-back theta sections can be divided to give the actual rational function \(r\) of (K15.1). The denominator has unit origin value by ALP-LIFT-07. The numerator is integral in the \(q\)-normalization by ALP-LIFT-08. Therefore \(r\) is regular and integral on an affine neighborhood \(\mathcal U\) of the origin.

The identity (K15.1) uses exactly the Chern-reduced gauges. The metrics of the two lines have the same translation-invariant curvature; their quotient is the flat metric on \(\mathcal P_T\). The normalized rigidified trivialization of \([2]^*\mathcal P_T\) is parallel and has value one at the origin. Thus it introduces neither a linear nor a quadratic exponential. Equivalently, the ratio of the two analytic reduced multipliers at \(2u\) is periodic: the difference semicharacter has order two. This confirms that the analytic ratio is the same algebraic \(r\), with no unknown scalar.

The invariant derivatives preserve \(\mathcal A=\Gamma(\mathcal U,\mathcal O)\): regular derivations preserve a localization of a regular function algebra. The CM-label proof (K13.2) applies on this actual abelian scheme, so
\[
D_i^{q_i}\mathcal A\subset p\mathcal A,\qquad
v_{\mathfrak p}(D_i^kr(0))\geq\lfloor k/q_i\rfloor.
\tag{K15.2}
\]
This is a separate stable-ring application. It does not assert that a Chern frame itself is an integral formal frame.

Suppose a bound already proved for \(F\) is
\[
v_{\mathfrak p}(\partial_i^nF(0))
\geq c n-s_p(n)/(p-1).
\]
Both constants used in §3 satisfy
\[
cq_i\leq1,\qquad c\leq 1/(p^{h_i-1}(p-1)).
\tag{K15.3}
\]
Differentiate (K15.1) \(n\) times along \(u_i\). Since \(2\) is a \(p\)-adic unit, the \(k\)-th Leibniz term has valuation at least
\[
\begin{split}
&v_p{n\choose k}+\lfloor k/q_i\rfloor
+c(n-k)-s_p(n-k)/(p-1)\\
&=cn-s_p(n)/(p-1)
+\lfloor k/q_i\rfloor+s_p(k)/(p-1)-ck.
\end{split}
\tag{K15.4}
\]
Write \(k=aq_i+b\), \(0\leq b<q_i=p^{h_i}\). Then
\[
s_p(k)=s_p(a)+s_p(b),\qquad
b\leq p^{h_i-1}s_p(b).
\]
Using (K15.3),
\[
\lfloor k/q_i\rfloor+s_p(k)/(p-1)
\geq a+b/(p^{h_i-1}(p-1))\geq c(aq_i+b)=ck.
\]
Thus every term satisfies the claimed lower bound. The sum does too. All coefficients of \(\sigma_q\) are integral at \(p\) by (K14.8), giving the maximum with zero.

This proves (K13.1) for the actual source-line germ, and also transfers the generic bound (K13.6) at every prime in the table. In particular, it gives explicit positive linear lower slopes with a logarithmic digit-sum loss at every \(p\equiv3,5\bmod7\).

The argument respects the source's odd level condition. The auxiliary map \([2]\) is used only to compare two already constructed sections and their derivatives. The section whose bounds are concluded is \(s_q\in H^0(J,L_\infty)\). A later odd-\(M\) pullback of this section has the exact normalization
\[
M^{-n}\partial_i^n\sigma_q(Mu)|_{u=0}=\partial_i^n\sigma_q(0).
\]
No translated \(D\)-line is substituted for \(L_\infty\).

The first congruence (K13.10) transfers too. Modulo 11, \(D_i^{q_i}\) is a derivation and kills the actual integral function \(r\). Applying it to (K15.1) and using the corresponding identity for \(F\) gives
\[
\partial_1^n\sigma_q(0)\equiv\partial_3^n\sigma_q(0)\equiv0\ (n\geq11),
\qquad \partial_2^n\sigma_q(0)\equiv0\ (n\geq121).
\tag{K15.5}
\]
The even order sets \(0,2,\ldots,10\) and \(0,2,\ldots,120\) found to consist of units for \(F\) are not asserted to be unit sets for \(\sigma_q\). Its different characteristic has its own selection rules.

## 6. AM-K016: exact archimedean growth and controlled nonvanishing

Fix \(i\), and put
\[
f(t)=\sigma_q(te_i)=\sum_{n\geq0}a_nt^n,
\qquad \alpha=\frac{\pi}{2G_i}>0,\qquad
M(R)=\max_{|t|\leq R}|f(t)|.
\]
The exact metric matrix is AM-R-004's diagonal \(G\). AM-R-006 gives the explicit bound
\[
|f(t)|\leq C e^{\alpha|t|^2},\qquad C=6125/16.
\tag{K16.2}
\]
The initial jets (K14.2) prove that \(f\) is nonzero for each \(i\). We now prove statements about this actual function, rather than all entire functions satisfying (K16.2).

### A lower growth bound from the compact theta metric

The Chern norm of the section is a continuous function on the compact torus \(J(\mathbb C)\). After a fixed constant normalization it pulls back along \(t\mapsto te_i\) as
\[
g(t)=|f(t)|e^{-\alpha|t|^2}.
\tag{K16.3}
\]
Restrict temporarily to real \(t\), and let \(K\) be the closure in \(J(\mathbb C)\) of this real one-parameter subgroup. It is a compact subgroup. Some real \(t_0\) has \(f(t_0)\ne0\), since otherwise the identity theorem would make \(f\) zero. Choose \(\varepsilon>0\) such that the relatively open set
\[
V=\{x\in K:\|s_q(x)\|>\varepsilon\}
\]
is nonempty, with the same fixed norm normalization as (K16.3).

The nonnegative real orbit is dense in \(K\). Here is an elementary justification. Its closure \(S\) is a compact subsemigroup of the torus. For any \(x\in S\), a pigeonhole argument applied to integer multiples of \(x\) in a successively finer finite cover produces positive multiples approaching zero. These return multiples may be chosen unbounded: if a bounded subsequence already returns arbitrarily close, one of its positive indices is an exact period and its multiples give unbounded exact returns. If the return indices are \(m_j\to\infty\), then \((m_j-1)x\to-x\), so \(-x\in S\). Thus \(S\) is a subgroup and must equal the closure \(K\) of the full real orbit. Positive translates of every \(x\in K\) therefore meet \(V\).

For each \(x\in K\), choose \(t_x\geq0\) with \(x+t_xe_i\in V\). The open sets \(V-t_xe_i\) cover \(K\); compactness supplies a finite subcover. Let \(L\) be the largest time used. For every \(r\geq0\), at least one \(t\in[r,r+L]\) has \(g(t)>\varepsilon\). Therefore
\[
\varepsilon e^{\alpha(R-L)^2}\leq M(R)\leq Ce^{\alpha R^2}
\qquad(R\geq L).
\tag{K16.4}
\]
In particular,
\[
\log M(R)=\alpha R^2+O(R),
\tag{K16.5}
\]
and \(f\) has order 2 and exact type \(\alpha\). It cannot be a polynomial, so it has infinitely many nonzero coefficients. The constants \(L,\varepsilon\) and the resulting thresholds are not made effective by this compactness argument.

### Exact coefficient limsup

Optimizing Cauchy's bound at radius \(\sqrt{n/(2\alpha)}\) gives
\[
|a_n|\leq C\left(\frac{2e\alpha}{n}\right)^{n/2}\quad(n>0).
\tag{K16.6}
\]
Consequently \(\limsup n|a_n|^{2/n}\leq2e\alpha\). If this inequality were strict, choose \(0<\beta<\alpha\) with
\(|a_n|\leq(2e\beta/n)^{n/2}\) for all sufficiently large \(n\). With \(N=2\beta R^2\), a term at radius \(R\) is then at most
\[
\exp\left(\frac N2\varphi(n/N)\right),
\qquad \varphi(x)=x(1-\log x),\qquad \varphi(1)=1.
\]
The first \(\lceil e^2N\rceil\) terms sum to \(O(N+1)e^{N/2}\), and the remaining terms have a bounded geometric tail because the derivative of their logarithmic bound is at most \(-1\). The finitely many excluded terms form a fixed polynomial. Hence \(\log M(R)\leq\beta R^2+O(\log(R+2))\), contradicting (K16.5). We have proved
\[
\limsup_{n\to\infty}n|a_n|^{2/n}=2e\alpha=\pi e/G_i.
\tag{K16.7}
\]
Since \(\partial_i^n\sigma_q(0)=n!a_n\), Stirling's formula converts (K16.7) exactly to (K16.1). This is a limsup over all orders, with zero terms allowed. It does not assert that every nonzero derivative attains the upper bound.

### Every sufficiently large multiplicative window contains support

Fix \(0<\delta<1\). We claim that every sufficiently large real \(N\) has a nonzero coefficient with index in
\[
[(1-\delta)N,(1+\delta)N].
\tag{K16.8}
\]
Suppose instead that the whole window is zero and put \(R=\sqrt{N/(2\alpha)}\). By (K16.6), each other term is bounded by
\(C\exp(N\varphi(n/N)/2)\). Define
\[
\kappa_\delta=1-\max\{\varphi(1-\delta),\varphi(1+\delta)\}>0.
\]
There are at most \(N+1\) terms below the window, each bounded by
\(C\exp((1-\kappa_\delta)N/2)\). Above the window the derivative of the logarithmic bound with respect to \(n\) is at most
\(-\tfrac12\log(1+\delta)\), so those terms sum to a geometric tail with ratio at most \((1+\delta)^{-1/2}\). The constant term is zero for this source section; even if it were present it would satisfy the same estimate for large \(N\). Thus
\[
M(R)\leq C\left(N+1+\frac1{1-(1+\delta)^{-1/2}}\right)
e^{(1-\kappa_\delta)N/2}.
\tag{K16.9}
\]
But (K16.4) gives
\(\log M(R)\geq N/2-O(\sqrt N)\), a contradiction for large \(N\). This proves (K16.8).

List the nonzero orders increasingly as \(n_1<n_2<\cdots\). If \(n_{k+1}/n_k\) stayed at least \(1+\eta\) along a subsequence, the interval between these two indices would contain a multiplicative window (K16.8) of a fixed positive relative width: take its midpoint and any \(\delta<\eta/(2+\eta)\). This contradicts (K16.8). Hence
\[
\frac{n_{k+1}}{n_k}\longrightarrow1.
\tag{K16.10}
\]
These orders can be enumerated exactly by (K14.6)–(K14.7): for a proposed pure order only one finite weight and finitely many partitions occur, and all coefficients are rational. The enumeration is therefore an actual algorithm with provable infinitely many outputs. Neither bounded additive gaps nor a nonzero coefficient at every allowed order is proved.

## 7. What the new bounds do and do not supply to the arithmetic gate

The actual all-order finite lower bound at a prime in the table is
\[
v_{\mathfrak p}(\partial_i^n\sigma_q(0))
\geq\max\{0,c_i(p)n-s_p(n)/(p-1)\},
\quad c_i(p)=\frac1{(p-1)(p^{h_i}+1)}.
\tag{K17.1}
\]
At 11 the three finite checks replace these constants by the larger constants in (K13.1). For the two inert orbit classes specifically requested, the generic constants are

| Prime class | \(c_1(p)\) | \(c_2(p)\) | \(c_3(p)\) |
|---|---|---|---|
| \(p\equiv3\pmod7\) | \(1/((p-1)(p^3+1))\) | \(1/((p-1)(p+1))\) | \(1/((p-1)(p^2+1))\) |
| \(p\equiv5\pmod7\) | \(1/((p-1)(p+1))\) | \(1/((p-1)(p^3+1))\) | \(1/((p-1)(p^2+1))\) |

These are uniform actual-section bounds. They are not claimed sharp. In particular, the accepted DP45/DP53 bare integral-function bounds cannot simply be assigned to this Chern-reduced germ. In the fixed global direction order, their comparison at 11 is

| Direction | Accepted bare sharp slope from DP53 | Actual theta lower slope proved here | Difference of the two stated constants |
|---|---:|---:|---:|
| \(\omega_1\) | \(121/1330\) | \(1/20\) | \(109/2660\) |
| \(\omega_2\) | \(11/1330\) | \(1/220\) | \(109/29260\) |
| \(\omega_3\) | \(132/1330\) | \(1/20\) | \(131/2660\) |

The supplied exact locators are `RETURN_DP_MULT_checkpoint_06_20261121T0420Z/research/DP45_integrated_fragment.tex`, the DP45 theorem, and `DP53_integrated_fragment.tex`, displayed global label table and its proof paragraph beginning “For a=3”. Their accepted \(p\equiv3,5\) triples are respectively
\((p,p^3,p^2)/((p-1)(p^3+1))\) and
\((p^3,p,p^2)/((p-1)(p^3+1))\).
The numerical differences in the table are not proved losses of the actual theta section: its optimal finite slopes are still unknown.

There is also a uniform, explicit but much weaker upper bound on each **nonzero** actual pure jet. For \(n\geq2\), (K14.8) makes
\(I_n=2^{n-2}\partial_i^n\sigma_q(0)\) a nonzero rational integer. For every odd prime \(p\), \(p^{v_p(I_n)}\leq|I_n|\). Using (K16.6) gives
\[
v_p(\partial_i^n\sigma_q(0))
\leq\frac{\log(6125/16)+(n-2)\log2+\log(n!)
+\frac n2\log\!\left(\frac{\pi e}{nG_i}\right)}{\log p}.
\tag{K17.2}
\]
Thus the finitely computable nonzero pure derivatives have both the actual linear lower bounds and an actual \(O(n\log n)\) upper bound. Formula (K17.2) applies at every prime above \(p\) because these derivatives are rational. It supplies no matching linear upper bound, optimal finite slope, or finite-prime analogue of (K16.1).

All mixed actual derivatives are determined by the Sato determinant and are integral away from 2. The positive linear finite bounds proved here concern the three pure directions. AM-K016 supplies nonzero pure derivatives with support ratios tending to one, and an exact archimedean limsup, but it does not ensure nonvanishing of a prescribed mixed harmonic row or charge. No transfer from one pure sequence to a source-selected harmonic image is claimed. Matching linear finite upper bounds, effective support thresholds, and the prescribed-row image comparison remain additional gates.

The full finite data for the translated \(F\) have useful but limited scope: modulo 11 its even derivatives through order 10 in directions 1 and 3, and through order 120 in direction 2, are units at both primes above 11. The exact certificate checks this by polynomial gcd with \(\Phi_7\); it does not convert those finite lists into an asymptotic finite upper bound for \(F\), much less for \(\sigma_q\).

## 8. Primary sources, exact locators, and reproducibility

The literature supplies the general bidifferential, Kleinian, and tau/sigma identities cited here. The CM uniqueness argument, stable-ring estimates, Bell–Legendre constants, algebraic comparison, and growth/support arguments are proved in this note. No claim that integral Hodge eigenvectors give an integral Chern frame is used; the supplied THETA3 C11 and C19 counterexamples and actual-theta method remain consistent with every assertion above.

1. Buchstaber, V. M., Enolskii, V. Z., & Leykin, D. V. (1997). Hyperelliptic Kleinian functions and applications. *American Mathematical Society Translations, Series 2, 179*, 1–33. [Author-hosted primary PDF](https://homepage.mi-ras.ru/~buchstab/download/advmathsci.2.179.1.pdf). Used: §1.2, equations (1.7)–(1.9); §2.1, Definition 1 and equations (2.1)–(2.2), pp.7–8; Corollary 2.1.2, equation (2.9), p.10; Theorem 2.2, equations (2.10)–(2.14), p.11. Local retrieved source: `theta_sources/BEL1997.pdf` and `.txt`.
2. Edelstein, J. D., Gómez-Reino, M., & Mariño, M. (2001). *Blowup formulae in Donaldson–Witten theory and integrable hierarchies* (arXiv:hep-th/0006113v3). [Primary PDF](https://arxiv.org/pdf/hep-th/0006113). Used: equations (3.3)–(3.6) for the explicit polar and bidifferential; (3.14)–(3.18) for the quadratic period normalization; (3.24), p.12, for the branch-partition Hessian. Local source: `theta_sources/Edelstein2001.pdf` and `.txt`.
3. Shramchenko, V. (2004). New Frobenius structures on Hurwitz spaces in terms of Schiffer and Bergmann kernels. *Proceedings of the Institute of Mathematics of the NAS of Ukraine, 50*(3), 1466–1473. [Primary proceedings PDF](https://www.slac.stanford.edu/econf/C0306234/papers/shramchenko.pdf). Used: §4, p.1468, Schiffer formula and its intrinsic period characterization.
4. Nakayashiki, A. (2010). Sigma function as a tau function. *International Mathematics Research Notices, 2010*(3), 373–394. [Author preprint, arXiv:0904.0846v2](https://arxiv.org/pdf/0904.0846v2). The cited v2 was revised in 2012; the journal article is from 2010. Used: §4, Plücker and Schur definitions and equation (7); §5, the shift by \(g-1\) and leading partition; §7, Theorem 4; §8, Theorem 8, normalized tau/sigma equality. All page references in this note concern the arXiv version.
5. Ônishi, Y. (2015). *Hurwitz integrality of power series expansion of the sigma function for a plane curve* (arXiv:1510.03002v1). [Primary PDF](https://arxiv.org/pdf/1510.03002). Used: equation (2.6) for the differential sign convention; Theorem 1.8 for the general Hurwitz result; Theorem 6.5, printed p.21, for the arithmetic-parameter determinant and exponential corrections; Proposition 6.7 for weights. Local source: `theta_sources/Onishi2015.pdf` and `.txt`. The stronger integral statement in this specialization is proved directly from its integer frame and vanishing corrections, not imported from the general theorem without checking powers of 2.
6. Ayano, T. (2025). Hurwitz integrality of the power series expansion of the sigma function for a telescopic curve. *Journal of the Mathematical Society of Japan, 77*(3), 833–867. https://doi.org/10.2969/jmsj/90129012. [Primary preprint, arXiv:2208.10079v2](https://arxiv.org/pdf/2208.10079v2), revised 14 April 2024. Used only as corroboration: Lemma 7.2 for Schur Hurwitz integrality and Theorem 7.5 for the tau/sigma relation. The reference in §4 to “Ayano (2024)” denotes this exact preprint version.

Reproducible artifact paths, all relative to this report's directory:

| Artifact | Actual check and scope |
|---|---|
| `jacobian_theta_direction_jets.py` / `.json` | Exact algebraic ODE and Bell recurrence; rational pure \(F\) jets through order 8. |
| `jacobian_theta_direction_jets_mod11.json` | Exact coefficient vectors modulo 11 through order 160 in all three directions. |
| `jacobian_theta_11_certificate.py` / `.json` | Regenerates the three exceptional log derivatives, checks saved coefficients and finite unit lists at both residue primes; PASS. |
| `jacobian_theta_hessian_check.py` / `.json` | Exact Bolza polynomial identity plus an independent finite theta-sum diagnostic for Hessians and initial \(F\) and \(\sigma_q\) jets; numerical comparisons are not proof premises. |
| `jacobian_sigma_determinant_certificate.py` / `.json` | Exhaustive exact weight-20 Plücker determinants, Schur polynomial, and four source-section jets; PASS. |

The imported normalization statements are ALP-LIFT-07 in `finite_theta_null_normalization.md`, ALP-LIFT-08 in `trace_one_leading_jet.md`, AM-R-004 in `../research/jacobian_period_theta.md`, and AM-R-006 in `../research/trace_one_theta_scalar.md`. This report's own checks are recorded separately in `kummer_extension_CHECK_EVENTS.tsv`; an author's whole-proof recheck is distinguished there from the parent's independent review.
