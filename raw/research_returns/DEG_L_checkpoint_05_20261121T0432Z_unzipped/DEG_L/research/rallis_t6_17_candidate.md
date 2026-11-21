# Candidate T6.17: fixed-source CM tensor normalization

Status: whole-proof review passed by author, root, and bounds agent; promoted to the checked report and TeX module on 2026-11-21. This file retains the separately reviewed candidate text. Actor: GPT-6 Astra Pro; effort not exposed; /root/rallis_t6. This extends the checked Hom-lattice calculation B19.1–B19.2 and is intended to apply to a fixed witness supplied by T6.16. The period in the estimates is normalized by the polarization metric, not by an unspecified algebraic Betti generator.

## Proposed theorem T6.17

For \(1\le i\le4\), fix a CM field \(E_i\) of degree \(2g_i\), a CM type \(\Phi_i\) (not necessarily primitive), an invertible fractional \(\mathcal O_{E_i}\)-ideal \(I_{i,0}\), and a polarized abelian variety
\[
A_{i,0}=\mathbf C^{g_i}/\Phi_i(I_{i,0}),\qquad L_{i,0},\qquad
V_{i,0}=\chi(L_{i,0}).
\tag{T17.1}
\]
Assume the \(E_i\) action has rank one on rational homology and the Rosati involution restricts to complex conjugation. Fix a smooth projective surface \(Y\), a Kähler form \(\omega_Y\), actual morphisms \(f_{i,0}:Y\to A_{i,0}\), and one holomorphic CM eigenline in each factor. Choose polarization-unit invariant eigenforms \(\beta_{i,0}\) in these four lines and suppose that
\[
p_0=\int_Y f_{1,0}^*\beta_{1,0}\wedge f_{2,0}^*\beta_{2,0}
            \wedge\overline{f_{3,0}^*\beta_{3,0}\wedge f_{4,0}^*\beta_{4,0}}
\ne0.
\tag{T17.2}
\]
The metric normalization and the chosen lines are fixed starting data.

Let the targets \((A_i,L_i)\) vary through the corresponding \(E_i\)-linear CM isogeny classes, with the same Rosati condition. In compatible CM coordinates write \(A_i=\mathbf C^{g_i}/\Phi_i(\Lambda_i)\), put \(V_i=\chi(L_i)\), and set
\[
\Lambda_i^- =\{x\in\Lambda_i:\mathcal O_{E_i}x\subset\Lambda_i\},\quad
J_i=[\Lambda_i:\Lambda_i^-],\quad
x_i=\frac{V_i}{V_{i,0}}J_i,\quad t_i=x_i^{1/g_i}.
\tag{T17.3}
\]
Define field constants
\[
K_i=\frac2\pi\bigl(g_i!\sqrt{|D_{E_i}|}\bigr)^{1/g_i},\qquad
c_i=
\begin{cases}
1,&g_i=1,\\
\bigl((g_i-1)/K_i\bigr)^{g_i-1},&g_i\ge2.
\end{cases}
\tag{T17.4}
\]
There exist actual \(E_i\)-linear isogenies \(h_i:A_{i,0}\to A_i\) and positive integers \(M_i\) such that the actual maps
\[
f_i=[M_i]\circ h_i\circ f_{i,0},\qquad f=(f_i):Y\to\prod_iA_i
\tag{T17.5}
\]
have a nonzero selected four-factor period and uniformly bounded period-normalized energy. Precisely, write \(\omega_i,\omega_{i,0}\) for invariant polarization representatives, let \(\beta_i\) be any polarization-unit eigenform in the corresponding target line, and put
\[
\begin{aligned}
p&=\int_Yf_1^*\beta_1\wedge f_2^*\beta_2
                   \wedge\overline{f_3^*\beta_3\wedge f_4^*\beta_4},\\
E&=\int_Y\Bigl(\sum_i f_i^*\omega_i\Bigr)\wedge\omega_Y,\qquad
E_{i,0}=\int_Y f_{i,0}^*\omega_{i,0}\wedge\omega_Y,\\
C_E&=\frac{4\sum_iK_iE_{i,0}}
               {|p_0|^{1/2}\bigl(\prod_i c_i\bigr)^{1/4}},\qquad
V_Y=\int_Y\omega_Y^2.
\end{aligned}
\tag{T17.6}
\]
Then
\[
p\ne0,\qquad \frac{E}{|p|^{1/2}}\le C_E,
\qquad
\frac{\deg_{\boxtimes_iL_i}(f_*[Y])}{|p|}
\le\frac{C_E^2}{V_Y}.
\tag{T17.7}
\]
The constants depend only on the fixed fields, polarized source factors, source surface and its four maps; they are independent of the target lattices, their endomorphism orders, and their polarization volumes. The denominator in (T17.7) is the specified metric period \(p\). These inequalities do not bound the unnormalized integral degree.

If the finitely many source coordinate pullbacks lie in the span of a fixed finite basis of genuine rank-one theta forms on \(Y\), then the common normalization \(|p|^{-1/4}\) gives theta presentations of all target polarization coordinates with uniformly bounded coefficients and every fixed Schwartz seminorm. Any one finite cover needed for theta spanning is taken at the outset and included in the fixed data.

## Proof

### 1. Every CM metric eigenvalue is controlled by a short integral isogeny

For each factor choose a nonzero integral \(E_i\)-linear homomorphism minimizing the squared complex Hilbert–Schmidt norm
\[
Q_i(h)=\operatorname{tr}_{\omega_{i,0}}(h^*\omega_i).
\]
The ideal-lattice argument of B19.1–B19.2 applies without primitivity. Indeed rank-one \(E_i\)-homology identifies every \(E_i\)-linear rational homomorphism with multiplication by an element of \(E_i\). The integral Hom lattice is \((\Lambda_i:I_{i,0})\), and its product with \(I_{i,0}\) is \(\Lambda_i^-\). The Rosati condition diagonalizes the polarization metrics. None of these statements uses simplicity. Every nonzero such field scalar is an isogeny. The exact covolume and minimum bound are therefore
\[
\operatorname{covol}_{Q_i}\operatorname{Hom}_{E_i}(A_{i,0},A_i)
=2^{-g_i}\sqrt{|D_{E_i}|}\,x_i,
\qquad Q_i(h_i)\le K_i t_i,
\qquad \deg h_i\ge J_i.
\tag{T17.8}
\]
Here the last inequality is the elementary inclusion \(h_i I_{i,0}\subset\Lambda_i^-\). The constant in the middle inequality is the Minkowski ball constant computed in B19.2.

Let \(\lambda_{i,\sigma}\) be the positive eigenvalues of \(h_i^*\omega_i\) relative to \(\omega_{i,0}\) in the CM eigenlines. They satisfy
\[
\sum_\sigma\lambda_{i,\sigma}\le K_i t_i,
\qquad
\prod_\sigma\lambda_{i,\sigma}
=\deg h_i\frac{V_i}{V_{i,0}}\ge x_i=t_i^{g_i}.
\tag{T17.9}
\]
For \(g_i\ge2\), arithmetic–geometric mean on the other \(g_i-1\) eigenvalues gives
\[
\lambda_{i,\sigma}
\ge\frac{t_i^{g_i}}
           {(K_i t_i/(g_i-1))^{g_i-1}}
=c_i t_i.
\]
For \(g_i=1\) the product inequality gives the same bound with \(c_i=1\). The trace gives the upper bound. Thus
\[
c_i t_i\,\omega_{i,0}
\le h_i^*\omega_i\le K_i t_i\,\omega_{i,0}.
\tag{T17.10}
\]
This is a bound in every CM eigenline, not merely a trace estimate.

### 2. Integral multiplication balances the four factors

Put
\[
T=\max_i t_i,\qquad
M_i=\left\lceil\sqrt{T/t_i}\right\rceil.
\tag{T17.11}
\]
Since \(T/t_i\ge1\),
\[
T\le M_i^2t_i\le4T.
\]
Multiplication by \(M_i\) is an actual endomorphism, so every map in (T17.5) is integral. The corresponding metric eigenvalues satisfy
\[
c_iT\le M_i^2\lambda_{i,\sigma}\le4K_iT.
\tag{T17.12}
\]
Pullback preserves the inequalities of positive forms, and integration on \(Y\) gives
\[
T\sum_i c_i E_{i,0}\le E\le4T\sum_iK_iE_{i,0}.
\tag{T17.13}
\]

Because the chosen period is a **fixed eigenmonomial**, there is no sum of potentially canceling scalars under this transport. Write
\[
([M_i]h_i)^*\beta_i=b_i\beta_{i,0}.
\]
The rank-one eigenline and the polarization-unit convention give
\[
|b_i|^2=M_i^2\lambda_{i,\sigma_i},\qquad
p=b_1b_2\overline{b_3b_4}\,p_0.
\tag{T17.14}
\]
Consequently
\[
|p_0|\bigl(\prod_i c_i\bigr)^{1/2}T^2
\le |p|
\le16|p_0|\bigl(\prod_iK_i\bigr)^{1/2}T^2.
\tag{T17.15}
\]
The lower bound proves nonvanishing and, together with the upper energy bound in (T17.13), gives the first inequality in (T17.7). Set \(\beta=\sum_i f_i^*\omega_i\). The Hodge index inequality on the fixed Kähler surface gives
\[
\int_Y\beta^2\le\frac{(\int_Y\beta\wedge\omega_Y)^2}{V_Y}.
\]
The left side is the degree of the effective pushforward, with its actual generic multiplicity, by T6.1. Dividing by \(|p|\) proves the second inequality in (T17.7). No division by an unverified generic degree has occurred. Also \(p\ne0\) implies that the first pulled-back wedge is nonzero, so \(f(Y)\) is a surface.

### 3. A single common analytic normalization bounds every theta coordinate

Choose a polarization-unit invariant CM coframe in every target. Multiply **all** its pulled-back one-forms by
\[
r=|p|^{-1/4}.
\]
The selected four-factor period then has absolute value one. The sum of the coordinate energies is exactly \(r^2E\), hence at most \(C_E\). This is a common scalar normalization of the four actual maps constructed above; the preceding balancing was by integral endomorphisms.

Now assume the fixed source coordinate pullbacks have a finite theta expansion, as supplied by T6.9 in its stated setting. Since each \(h_i\) is diagonal in the CM eigenlines, all varying target coordinate pullbacks lie in the same fixed finite-dimensional space. Take the span of the finitely many actual theta forms used in expansions of its fixed generators; this is a possibly larger finite-dimensional space containing all the pullbacks. Select a basis \(\theta_1,\ldots,\theta_q\) from those actual theta generators. Let \(G\) be its positive energy Gram matrix, using the convention
\[
\mathcal E(\eta)=\int_Y\frac i2\eta\wedge\bar\eta\wedge\omega_Y.
\]
If the normalized coordinate forms are \(\eta_j=\sum_k a_{jk}\theta_k\), then
\[
\lambda_{\min}(G)\sum_{j,k}|a_{jk}|^2
\le\sum_j\mathcal E(\eta_j)
=r^2E\le C_E.
\tag{T17.16}
\]
Fix once and for all one theta presentation for each basis vector. Linear combination gives a linear section from this finite coefficient space to a finite collection of Schwartz/source-vector spaces. Every fixed seminorm on its finite-dimensional image is bounded by a constant times the coefficient norm. Thus the normalized inputs have uniformly bounded seminorms, including the weighted local shell seminorms of B14a at the finitely many nonstandard places. The standard tails, global characters, and levels come from a fixed finite list. This proves the analytic-presentation assertion. QED.

## Exact scope and relation to the arithmetic construction

The initial data required here exist for the explicit T6.16 witness. Each of its four CM factors can first be replaced, once and for all, by an \(E\)-linearly isogenous factor with maximal-order action; composing the initial maps with those fixed isogenies preserves the nonzero selected period and the first wedge's automorphic constituent. The two imprimitive types in (T16.2) cause no difficulty because the proof above only uses rank-one \(E\)-homology, not simplicity. A single further fixed cover may supply the theta spanning statement. Thereafter the target lattices and their conductors may vary arbitrarily inside these four fixed \(E\)-linear isogeny classes.

The multiplication factors \(M_i\) do not introduce a new normalized divisor-kernel Chow class. Under the exact birigidified-kernel hypotheses of T6.5, they multiply both the kernel output and its selected **algebraically normalized Betti period** by \(\prod_iM_i\), so the quotient cancels exactly. This assertion only concerns the integral multiplications at a fixed target; it does not claim cancellation of the varying isogenies \(h_i\).

The period \(p\) in (T17.7) is instead defined by polarization-unit eigenforms. It need not equal the Betti-algebraic coefficient used to divide a Chow correspondence. The final common scalar \(|p|^{-1/4}\) generally changes the integral Betti lattice. Accordingly the theorem supplies bounded analytic theta presentations in a fixed-source construction and a uniform ratio of degree to metric period. It does not supply a conductor-independent effective integral degree, a bounded denominator for the Betti-algebraic normalization, or bounds uniform over varying CM fields or initial witnesses. In particular T6.16's actual nonmonomial rank-two constituent remains compatible with the finite rank-one Hecke-energy upper bound: the latter is an inequality using all normalized coordinates, not an identity that replaces the rank-two spectral factor by a character.

## Check status

The proof imports the checked exact CM Hom covolume and Minkowski bound of B19.1–B19.2, and the already checked geometric degree/Hodge-index and theta-spanning statements T6.1/T6.9. The new steps to check are the lower bound for each metric eigenvalue, the integer balancing inequalities, the noncanceling eigenmonomial period, the common fourth-root normalization, and the distinction between metric and Betti period. This candidate is not yet included in the checked main module.
