# Controlled local inputs for the rank-one theta lift

**Scope.** This follow-up to B14–B14a proves an analytic reduction for the actual rank-one Rallis norm, together with explicit test vectors. It separates preservation of an existing theta vector from the choice of a new vector of unit norm. Neither operation identifies the integral theta lattice with the lattice of algebraic homomorphisms used in the geometric construction. No conductor-only bound for a selected global Weil period is claimed.

**Main conclusion.** At a split finite place, every Schwartz input has a representative supported on one radial shell with the same local Rallis class, the same compact target level, and squared Schwartz norm equal to its raw local zeta integral. Replacing the input at finitely many places preserves the existing global theta vector, by the positive global Rallis identity. At a compact source torus the corresponding replacement is ordinary character projection. These replacements remove arbitrary radial presentation complexity. Their coefficients can acquire arithmetic denominators, and their norms retain the size of the specified output.

## LN1. Split local conventions and the exact shell operator

Let $F$ be a nonarchimedean local field, $\mathcal O$ its integers, $\varpi$ a uniformizer, and $q$ its residue cardinality. Normalize additive measure by $\operatorname{vol}(\mathcal O^3)=1$ and multiplicative measure by $\operatorname{vol}(\mathcal O^\times)=1$. Put

\[
 D(a)\phi(x)=|a|^{3/2}\phi(ax),\qquad
 \omega(a)=\rho(a)D(a),\qquad
 \eta=\rho\tau,\quad u=\eta(\varpi),
\]

where $\rho,\tau$ are smooth unitary characters of $F^\times$. The Hermitian pairing is linear in its first argument. The raw critical local zeta form is

\[
 Z_\eta(\phi,\psi)
 =\int_{F^\times}\eta(a)\langle D(a)\phi,\psi\rangle\,d^\times a.
 \tag{LN1.1}
\]

This is the split model of B14a. In Haan's conventions the source vector belongs to $\tau$ and the global lift is written $\theta(\bar f,\phi)$; this incorporates the apparent contragredient in (LN1.1).

Define $S_j=\varpi^j\mathcal O^3\setminus\varpi^{j+1}\mathcal O^3$, $\mathcal H_0=L^2(S_0)$, and

\[
 I_jb(x)=q^{3j/2}b(\varpi^{-j}x)\mathbf1_{S_j}(x),\qquad
 b_j(x)=q^{-3j/2}\phi(\varpi^j x),\quad x\in S_0.
\]

Each $I_j$ is unitary and $\phi=\sum_jI_jb_j$ away from the measure-zero origin. Let $R(v)b(x)=b(vx)$ for $v\in\mathcal O^\times$, and set

\[
 P_\eta=\int_{\mathcal O^\times}\eta(v)R(v)\,d^\times v,
 \qquad A_\eta\phi=\sum_{j\in\mathbb Z}u^jP_\eta b_j.
 \tag{LN1.2}
\]

Then $P_\eta$ is the orthogonal projector onto the $R(v)$-character $\eta^{-1}$, and

\[
 Z_\eta(\phi,\psi)=\langle A_\eta\phi,A_\eta\psi\rangle.
 \tag{LN1.3}
\]

**Proof, including convergence.** Compact support gives $b_j=0$ for $j\ll0$. Local constancy at zero gives, for some $J$,

\[
 b_j=q^{-3j/2}\phi(0)\mathbf1_{S_0}\quad(j\ge J).
\]

Thus $\sum_j\|b_j\|<\infty$, and likewise for the shell coefficients $c_l$ of $\psi$. The compact group average is self-adjoint and idempotent because $\eta$ is unitary. The identities $D(\varpi^k)I_j=I_{j-k}$ and $D(v)I_j=I_jR(v)$ show that integrating over units and then summing valuations gives

\[
 Z_\eta(\phi,\psi)
 =\sum_{j,l}u^{j-l}\langle P_\eta b_j,P_\eta c_l\rangle.
\]

The sum of absolute bounds is at most $(\sum_j\|b_j\|)(\sum_l\|c_l\|)$. It justifies the integrals and their interchange, and gives (LN1.3). In particular $Z_\eta(\phi,\phi)\ge0$. QED.

For later arithmetic use the tail is exactly

\[
 A_\eta\phi
 =\sum_{j<J}u^jP_\eta b_j
 +\phi(0)P_\eta\mathbf1_{S_0}
   \frac{(u q^{-3/2})^J}{1-u q^{-3/2}}.
 \tag{LN1.4}
\]

The first sum is finite. When $\eta$ is ramified on units, $P_\eta\mathbf1_{S_0}=0$, so the tail vanishes.

## LN2. A one-shell section preserves the existing theta class and compact level

Let $\mathcal H_\eta^\infty$ be the locally constant functions on $S_0$ with $R(v)h=\eta(v)^{-1}h$. Formula (LN1.4) shows that $A_\eta\phi$ belongs to this space. Define

\[
 s_\eta(h)=I_0h,\qquad
 C_\eta=s_\eta A_\eta:\mathcal S(F^3)\longrightarrow\mathcal S(F^3).
\]

Then

\[
 \begin{aligned}
 A_\eta s_\eta&=1,& C_\eta^2&=C_\eta,\\
 A_\eta(\phi-C_\eta\phi)&=0,&
 Z_\eta(\phi-C_\eta\phi,\phi-C_\eta\phi)&=0,\\
 \|C_\eta\phi\|_2^2
 &=Z_\eta(C_\eta\phi,C_\eta\phi)
 =Z_\eta(\phi,\phi).
 \end{aligned}
 \tag{LN2.1}
\]

Its weighted shell seminorm, for any exponent $1+\epsilon>1$ centered at shell zero, is exactly its squared norm. Thus the B14a weighted estimate can always be satisfied with one shell after this replacement; its right-hand side is the norm of the prescribed local output.

For $k\in K=GL_3(\mathcal O)$, allow the target action

\[
 V(k)\phi(x)=\kappa(\det k)\phi(k^t x)
\]

with any smooth unitary determinant twist $\kappa$. Then $C_\eta$ commutes with $K$. Consequently it preserves invariance under every subgroup of $K$, including principal congruence subgroups, and also preserves every $K$-type condition.

**Proof.** The extension by zero of a locally constant function on the compact open shell $S_0$ is Schwartz. Its only nonzero shell coefficient is $h$ at zero, and $P_\eta h=h$, proving the section and idempotence identities. Equation (LN1.3) proves the identities of norms and radicals. Every $k\in K$ preserves each shell; it acts on every $b_j$ by the same formula $V(k)b_j(x)=\kappa(\det k)b_j(k^t x)$. Scalar unit multiplication commutes with $k^t$, so $P_\eta$, $A_\eta$, and $s_\eta$ intertwine these compact actions. This proves level and type preservation. QED.

**Global preservation, using the actual positive norm identity.** Suppose the global rank-one theta lift is in the square-integrable setting where Haan's Theorem 3.4 applies, with all Haar measures and compatible splittings fixed as there. Write a pure Schwartz tensor as $\Phi=\phi_v\otimes\Phi^v$. Replace the one split finite factor by $C_{\eta_v}\phi_v$, retaining the same global source character and source vector. For the difference tensor

\[
 \Delta\Phi=(\phi_v-C_{\eta_v}\phi_v)\otimes\Phi^v,
\]

the local raw zeta factor at $v$ is zero. Its normalized factor is also zero: at the Rallis argument $3/2$ the local Euler factors are finite and nonzero. Haan's diagonal identity therefore gives

\[
 \|\theta(\bar f,\Delta\Phi)\|_{\mathrm{Pet}}^2=0.
\]

Positive definiteness of the Petersson norm implies that this automorphic theta vector is zero. Smoothness makes the equality an equality of functions, rather than just of almost-everywhere classes. Therefore the replacement preserves the **existing** theta vector. Applying this argument term by term proves the result for finite sums of pure tensors, and applying it sequentially proves the result at any finite set of selected places. The same statement holds componentwise for finite-dimensional differential-form coefficient spaces whose scalar components satisfy that identity. No assertion identifying the local zeta radical with an abstract small-theta kernel is required.

Only finitely many places may be changed in this argument: retain the distinguished unramified Schwartz vector at all other places. Replacing $\mathbf1_{\mathcal O_v^3}$ by a one-shell function at infinitely many unramified places generally does not define an element of the restricted adelic Schwartz space.

**Fixed output versus unit output.** If $h=A_\eta\phi\ne0$, $I_0h$ preserves the output and has norm $\|h\|$. The function $I_0(h/\|h\|)$ has norm one and raw zeta one, but scales the output by $\|h\|^{-1}$. These are different operations. Normalizing a selected geometric period may restore precisely this scale.

## LN3. No least Schwartz $L^2$ norm at fixed split output

For nonzero $h\in\mathcal H_\eta^\infty$, put

\[
 \phi_{M,h}=\frac1M\sum_{j=0}^{M-1}u^{-j}I_jh.
\]

Then

\[
 A_\eta\phi_{M,h}=h,\qquad
 \|\phi_{M,h}\|_2^2=\frac{\|h\|^2}{M},\qquad
 Z_\eta(\phi_{M,h},\phi_{M,h})=\|h\|^2.
 \tag{LN3.1}
\]

**Proof.** The first equality follows by applying $A_\eta I_jh=u^jh$ to each of the $M$ summands. Distinct shells are orthogonal, giving the squared norm. Apply (LN1.3) for the zeta identity. Every input is Schwartz, and compact target level is preserved if $h$ has that level. Since the zero Schwartz function cannot have output $h\ne0$, the infimum of the Schwartz squared norm over this fixed nonzero output is zero and is not attained. QED.

Thus a claim about a “minimal Schwartz input” needs an additional support or arithmetic-lattice constraint. The one-shell section is canonical after the choices of lattice and uniformizer, but it is not an unrestricted $L^2$ minimizer.

## LN4. Compact source tori: an actual least-norm representative

Let $T$ be a compact source torus with Haar volume $v_T>0$, let $\omega$ be its unitary action, and let $\tau$ be a unitary character. On smooth Schwartz vectors define

\[
 P_{\tau^{-1}}=\frac1{v_T}\int_T\tau(t)\omega(t)\,dt.
\]

Then $P_{\tau^{-1}}$ is the orthogonal character projector and

\[
 Z_T(\phi,\phi)
 :=\int_T\tau(t)\langle\omega(t)\phi,\phi\rangle\,dt
 =v_T\|P_{\tau^{-1}}\phi\|^2.
 \tag{LN4.1}
\]

Replacement by $P_{\tau^{-1}}\phi$ preserves the local zeta class and all commuting target levels; under the global hypotheses of LN2 it preserves the global theta vector. It has squared norm $Z_T(\phi,\phi)/v_T$, and is the unique least-norm representative among inputs with this projected output.

**Proof.** Translation invariance of Haar measure and unitarity give $P^2=P=P^*$, $\omega(t)P=\tau(t)^{-1}P$, and (LN4.1). The difference $\phi-P\phi$ lies in the zeta radical, so the same global Rallis argument applies. The commuting target action commutes with the average. If $P\psi=P\phi=h$, then $\psi=h+(1-P)\psi$ is an orthogonal decomposition, whence $\|\psi\|^2=\|h\|^2+\|(1-P)\psi\|^2\ge\|h\|^2$, with equality exactly when $\psi=h$. QED.

## LN5. Explicit integral split test vectors and conductor dependence

For any smooth unitary $\eta$, define

\[
 \phi_\eta(x_1,x_2,x_3)
 =\eta(x_1)^{-1}\mathbf1_{\mathcal O^\times\times\mathcal O\times\mathcal O}(x).
 \tag{LN5.1}
\]

Then $\phi_\eta$ is a one-shell Schwartz function with values zero or roots of unity, and

\[
 A_\eta\phi_\eta=\phi_\eta|_{S_0},\qquad
 Z_\eta(\phi_\eta,\phi_\eta)=\|\phi_\eta\|_2^2=1-q^{-1}.
 \tag{LN5.2}
\]

Thus an explicitly nonzero raw local zeta integral is bounded between $1/2$ and $1$, independently of the character conductor. Normalization to norm one costs at most $\sqrt2$. This is a choice of a nonzero local output, not a statement about any prescribed global period.

Set $K(0)=GL_3(\mathcal O)$ and $K(m)=1+\varpi^mM_3(\mathcal O)$ for $m\ge1$. Let $a(\eta)$ be the unit-character conductor, with value zero for an unramified character. In the untwisted linear target model, (LN5.1) is fixed by $K(m)=1+\varpi^mM_3(\mathcal O)$ for $m\ge\max(1,a(\eta))$. With determinant twist $\kappa$, $m\ge\max(1,a(\eta),a(\kappa))$ suffices. For ramified $\eta$, the untwisted model cannot have a $K(m)$-fixed input with nonzero $A_\eta$-image when $m<a(\eta)$.

**Proof.** Compactness of the unit group and smoothness give a finite unit-character image, hence roots of unity. On scalar units $R(v)\phi_\eta=\eta(v)^{-1}\phi_\eta$, so $P_\eta\phi_\eta=\phi_\eta$. Its support lies in $S_0$, and its additive volume is $1-q^{-1}$, giving (LN5.2). For $k\in K(m)$, $k^tx$ preserves the chart $x_1\in\mathcal O^\times,x_2,x_3\in\mathcal O$. Its first coordinate is $x_1(1+\varpi^m z)$ for $z\in\mathcal O$, so the character value is unchanged at the stated level; $\det k\in1+\varpi^m\mathcal O$ kills the twist as well. Conversely, in the untwisted model a scalar $vI_3\in K(m)$ forces any $K(m)$-fixed input, and therefore its $A_\eta$-image, to be $R(v)$-invariant. A nonzero $\eta^{-1}$-eigenvector can have this property only if $\eta(v)=1$. This forces $m\ge a(\eta)$. QED.

These are explicit Schwartz test vectors and a principal-level statement. They are not identified here with a representation-theoretic newform for another family's compact subgroups.

For unramified $\eta$, the spherical lattice vector $\phi_0=\mathbf1_{\mathcal O^3}$ instead has

\[
 \|\phi_0\|^2=1,\qquad
 Z_\eta(\phi_0,\phi_0)=\frac{1-q^{-3}}{|1-uq^{-3/2}|^2}.
 \tag{LN5.3}
\]

Its squared weighted shell norm with weight $(1+j)^2$ is

\[
 (1-q^{-3})\sum_{j\ge0}(1+j)^2q^{-3j}
 =\frac{1+q^{-3}}{(1-q^{-3})^2}\le\frac{72}{49}.
 \tag{LN5.4}
\]

Indeed its normalized shell coefficients are $\sqrt{1-q^{-3}}q^{-3j/2}$, and geometric-series summation gives both formulas. The rational function in $t=q^{-3}\le1/8$ in (LN5.4) is increasing. Under the standard unramified Euler normalization this lattice vector has normalized local zeta factor one, as in the unramified calculation Haan (3.1).

The split Euler multiplier retained in B14 is also uniformly controlled. If the two unramified parameters are $\lambda,\lambda^{-1}$, $|\lambda|=1$, it is

\[
 R_v=\frac{|1-\lambda q^{-3/2}|^2}{1-q^{-3}},\qquad
 \frac{1-q^{-3/2}}{1+q^{-3/2}}\le R_v\le
 \frac{1+q^{-3/2}}{1-q^{-3/2}}.
\]

If both local character factors are ramified, $R_v=(1-q^{-3})^{-1}$, within the same interval. Thus this multiplier does not spoil the uniform local bounds. This elementary estimate concerns the retained local Euler ratio, not any unstated global measure normalization.

## LN6. Arithmetic coefficient effects of the analytic section

Even cyclotomic-integral Schwartz data need not remain integral after $C_\eta$.

First choose a finite-index open subgroup $U\subset\mathcal O^\times$ killing both the unit action on a locally constant vector $b$ and $\eta$. With $N=[\mathcal O^\times:U]$, normalized averaging is

\[
 P_\eta b=\frac1N\sum_{v\in\mathcal O^\times/U}\eta(v)R(v)b.
 \tag{LN6.1}
\]

This can genuinely introduce the denominator $N$. For $\eta|_U=1$, take $b=\mathbf1_{U\times\mathcal O\times\mathcal O}$ on $S_0$. Directly, the units $v$ satisfying $vx_1\in U$ form $x_1^{-1}U$, so

\[
 P_\eta b=\frac1N\eta(x_1)^{-1}
  \mathbf1_{\mathcal O^\times\times\mathcal O\times\mathcal O}.
\]

Second, shell identification uses $b_j(x)=q^{-3j/2}\phi(\varpi^jx)$, which changes the integral normalization. The phases $u^j$ need not even be algebraic without an arithmetic hypothesis on the character. If they are algebraic, they and the geometric-tail denominator still need to be tracked in the relevant coefficient ring.

For an exact elementary example, take unramified $\eta$ with $u=1$. Formula (LN1.4) gives

\[
 C_\eta(\mathbf1_{\mathcal O^3})
 =\frac{\mathbf1_{S_0}}{1-q^{-3/2}}.
 \tag{LN6.2}
\]

When $q=p^2$, the coefficient is $p^3/(p^3-1)$, a rational noninteger. Its real absolute value is bounded, yet its denominator is $p^3-1$. Thus bounded archimedean size of the section is consistent with varying arithmetic denominators.

At a compact source torus, if a finite-index open subgroup $U\subset T$ fixes the smooth vector and kills $\tau$, then the normalized character projector is the analogous average with denominator $[T:U]$. Even if every group action in this finite sum preserves a chosen integral lattice, the average need not preserve that lattice. A Weil model whose group actions already have coefficient denominators requires additional accounting.

These explicit computations show why analytic preservation of a theta vector is compatible with a changed lattice of Schwartz representatives. They do not show that the integral geometric complexity grows: the global theta vector itself is unchanged by LN2.

## LN7. A model period can be small while the integral test vector has bounded norm

Let $\eta|_{\mathcal O^\times}$ be primitive of conductor $m\ge1$, and let $\psi:F\to\mathbb C^\times$ be an additive character trivial on $\mathcal O$ but nontrivial on $\varpi^{-1}\mathcal O$. For the integral-valued test vector (LN5.1), define the Fourier functional

\[
 \ell_m(\phi)=\int_{F^3}\phi(x)\psi(\varpi^{-m}x_1)\,dx.
\]

Then

\[
 |\ell_m(\phi_\eta)|=q^{-m/2},
 \qquad \|\phi_\eta\|^2=Z_\eta(\phi_\eta,\phi_\eta)=1-q^{-1}.
 \tag{LN7.1}
\]

**Proof.** Set $R=\mathcal O/\varpi^m\mathcal O$ and $\Psi(a)=\psi(\varpi^{-m}a)$, a primitive additive character of $R$. For $a\in R$, put

\[
 S(a)=\sum_{x\in R^\times}\eta(x)^{-1}\Psi(ax).
\]

For a unit $a$, substitution $y=ax$ gives $S(a)=\eta(a)S(1)$. If $m\ge2$, primitiveness provides $h\in1+\varpi^{m-1}\mathcal O$ with $\eta(h)\ne1$. For nonunit $a$, the substitution $x\mapsto hx$ does not change $\Psi(ax)$, so $S(a)=0$. For $m=1$, the only nonunit is zero and the nontrivial character sum is zero. Orthogonality of additive characters on the finite ring gives

\[
 \sum_{a\in R}|S(a)|^2
 =q^m\sum_{x\in R}|\mathbf1_{R^\times}(x)\eta(x)^{-1}|^2
 =q^m|R^\times|.
\]

There are $|R^\times|$ unit arguments, all with magnitude $|S(1)|$, so $|S(1)|^2=q^m$. Haar integration over unit residue classes gives $\ell_m(\phi_\eta)=q^{-m}S(1)$, proving (LN7.1). QED.

This is a model Fourier period, not the selected geometric Weil period. It proves a narrower point: integral values of the Schwartz input and a uniform Rallis norm do not imply a uniform lower bound for a Haar-averaged arithmetic functional. In this example forcing the displayed period to have absolute value one costs $q^{m/2}$ in input norm. No such growth is asserted for the actual construction.

## Primary-source ledger and exact scope

| Source | Exact locator read | Role and limit |
|---|---|---|
| Jaeho Haan, *The Bessel Period of U(3) and U(2) involving a non-tempered representation*, arXiv:1403.5061v7, <https://arxiv.org/pdf/1403.5061> | §2.3 equation (2.1), printed p.5; §3.1 equation (3.1), pp.6–7; §3.2 equation (3.3), p.8; §3.3 Theorem 3.4 and its short proof, p.8; §3.6.1, p.9 | Split linear Weil action, critical matrix coefficient section, normalized unramified factor, and positive global rank-one Rallis norm identity. The global identity is imported; its cited upstream theorem is not re-proved here. |
| Michitaka Miyauchi, *Conductors and newforms for non-supercuspidal representations of unramified U(2,1)*, arXiv:1112.4899v1, <https://arxiv.org/pdf/1112.4899> | Introduction pp.1–2; §1.2 Definition 1.2 and Theorem 1.3, p.5; §3.2 Proposition 3.2 and complete short proof, p.9 | The field extension is unramified quadratic and the residual characteristic odd. Newforms use his special $K_n$, not principal congruence subgroups. Generic representations admit newforms; Proposition 3.2 gives a nongeneric constituent with no $K_n$-fixed vectors. No identification with the actual 032 local representation or geometric period is made. |

The proofs LN1–LN7 are the elementary deductions given in full above. Miyauchi is a scope check, not an input to them: a theorem about a generic Whittaker newform cannot be substituted for the missing integral-Hom or selected-Weil-period comparison. This report has not independently proved Miyauchi's cited earlier theorem used in Proposition 3.2.

## Consequence for the remaining main gate

The arbitrary radial-growth obstruction of B14 is removable for a **specified existing** rank-one theta vector at finitely many split places, without changing that vector or its compact level. Compact source factors can likewise be projected. Alternatively, explicit integral local test vectors give uniformly nonzero local raw factors with conductor appearing only in an elementary level condition. Neither statement bounds the size of the particular theta vector that realizes a primitive integral algebraic homomorphism, nor its norm after a selected nonzero Weil period is normalized. The remaining arithmetic comparison concerns that specified output and its integral lattice, rather than arbitrary radial support of a Schwartz presentation.
