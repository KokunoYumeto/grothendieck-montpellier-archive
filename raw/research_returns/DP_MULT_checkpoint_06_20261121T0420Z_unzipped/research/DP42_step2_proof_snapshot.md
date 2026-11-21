# DP42: exact radius on every mixed line with primitive projections

Date: **2026-11-21 UTC**. Agent: `/root/step2_higher`. Model: **GPT-6 Astra Pro**. Effort: **not exposed**. The parent reserved finding **DP42** and proposed the successive last-axis, eigenaxis and primitive-vector extensions. This memo independently derives a unified proof, including the explicit initial coefficient and the nonzero-multiplier strengthening. It does not edit the main paper or assert a global theta-lift consequence.

## 1. Statement

Let $p$ be odd, $h\ge3$, $q=p^h$, $d=h-1$, and $\mathcal O=W(\mathbb F_q)$ with $v(p)=1$. Put

\[
 s=\frac1{p-1},\qquad \rho_h=\frac1{q-1}.
\]

Use the actual Honda line $G_h$, its Cartier dual $H$, and the integral Teichmüller coordinates and invariant primitive Poincaré frame of DP38–DP41. Their logarithms are exactly

\[
 L_0(S)=\sum_{m\ge0}\frac{S^{q^m}}{p^m},\qquad
 L_H(\mathbf Y)=\sum_{n\ge0}\frac{M^{\circ n}(\mathbf Y)}{p^n},
\]

where $M_1=Y_d^{p^2}$ and $M_i=Y_{i-1}^p$ for $2\le i\le d$. Write $E_0,E_H$ for the inverse logarithms, and

\[
 \beta(x,\mathbf y)=b(E_0(x),E_H(\mathbf y))
\]

for the invariant primitive logarithmic splitting in additive coordinates.

Choose $u\in\mathcal O^\times$ and a primitive vector $\mathbf v=(v_1,\ldots,v_d)\in\mathcal O^d$. Let

\[
 j=\min\{i:v_i\in\mathcal O^\times\},\qquad k=h-j,
 \qquad N_k=p^k+1,\qquad S_k=\frac{p^k-1}{p-1},
\]

and set

\[
 w_k=\frac{p^k}{(p-1)(p^k+1)},\qquad
 c_k^{\mathrm{path}}=s-w_k=\frac1{(p-1)(p^k+1)}.
\tag{PL1}
\]

Let $\lambda\in\mathcal O^\times$. For any integral formal function $U\in\mathcal O[[S,\mathbf Y]]$, assume only that its restriction

\[
 V(t)=U(E_0(ut),E_H(\mathbf v t))
\tag{PL2}
\]

is **not identically zero**. Its constant coefficient need not be a unit, and it may vanish at the origin. Define

\[
 \Theta(t)=V(t)\exp\bigl(\lambda\beta(ut,\mathbf v t)\bigr)
           =\sum_{n\ge0}a_nt^n.
\tag{PL3}
\]

For a rational $w\ge0$ put $\nu_w(F)=\inf_n(v([t^n]F)+wn)$. Then

\[
 \boxed{
 \nu_w(\Theta)=
 \begin{cases}
 -\infty,&0\le w<w_k,\\
 \nu_w(V)\in[0,\infty),&w\ge w_k.
 \end{cases}}
\tag{PL4}
\]

In the second line the value is finite. If $U(0)$ is a unit, it equals zero. In particular

\[
 v(n!a_n)\ge c_k^{\mathrm{path}}n-\frac{s_p(n)}{p-1},
 \qquad
 \boxed{\liminf_{n\to\infty}\frac{v(n!a_n)}n
       =c_k^{\mathrm{path}}.}
\tag{PL5}
\]

Here $v(0)=+\infty$. There is also an exact logarithmic coefficient:

\[
 \boxed{
 p^{S_k}[t^{N_k}]\beta(ut,\mathbf v t)
 \equiv(-1)^{k-1}u v_j^{p^k}\pmod p.}
\tag{PL6}
\]

Thus that coefficient has valuation exactly $-S_k$.

The integer $k$ is intrinsically the nilpotency length of the reduction of the dual direction under the restricted $p$-operation on $\operatorname{Lie}(H_{\mathbb F_q})$. Among these mixed lines the largest possible factorial slope is attained at $k=1$ and equals

\[
 c_1^{\mathrm{path}}=\frac1{p^2-1}=\rho_2.
\tag{PL7}
\]

It is independent of $h$. For the last eigenaxis $\mathbf v=\epsilon e_d$, with any unit $\epsilon$, (PL4) has threshold $w_1=p/(p^2-1)=c_2$. All other single eigenaxes have smaller factorial slope. This theorem requires both the line projection and the dual projection to be primitive. It does not cover a zero or nonprimitive projection, a different class or normalization, a selected harmonic operator, or a global theta correspondence.

## 2. The full primitive logarithm used in the proof

The sign-corrected display calculation in DP41 gives the exact identity

\[
 \begin{split}
 b(S,\mathbf Y)
 ={}&-\sum_{i=1}^d\sum_{l,n\ge0}
 \frac{S^{p^{n+lh+i}}Y_i^{p^n}}{p^{n+l+1}}\\
 &+\left(\sum_{a\ge0}\frac{S^{q^a}}{p^a}\right)
   \left(\sum_{i=1}^d\sum_{l\ge0}
     \frac{Y_i^{p^{lh+h-i}}}{p^{dl+h-i}}\right).
 \end{split}
\tag{PL8}
\]

Every fixed ordinary degree has finitely many terms. Possible cancellations between the two displayed families do not impair the argument: the weights below isolate a single surviving monomial. Formula (PL8) uses Zink's negative `hex` convention, so its first ordinary homogeneous part is $(-S^pY_1+SY_d^p)/p$.

For completeness, all subsequent statements are proved from this exact identity, the exact logarithms in Section 1, and elementary formal-series algebra. No optimal one-variable radius is inferred solely from the first ordinary-degree pole.

## 3. An explicit interval of useful weights

Fix the active index $j$ and $k=h-j$. Work throughout the rational interval

\[
 I_k=\left[\frac{S_k}{p^k+1},\frac{p^k s}{p^k+1}\right]
     =[w_k^-,w_k].
\tag{PL9}
\]

For $w\in I_k$ set $\delta=s-w$ and define coordinate weights

\[
 \omega_0=w,\qquad
 \omega_i=s-p^{i-j}\delta\quad(1\le i\le d).
\tag{PL10}
\]

In particular $\omega_j=\omega_0=w$. The parameter ranges are

\[
 \frac{s}{p^k+1}\le\delta\le\frac{2s}{p^k+1}<s,
 \qquad
 0\le\tau:=2s-(p^k+1)\delta
          =(p^k+1)w-S_k\le s.
\tag{PL11}
\]

The weights are positive and strictly dominate the original dual contraction weights $r_i=s-p^i\rho_h$. Indeed, since $p\ge3$, $2s\le1$, and

\[
 \delta\le\frac{2s}{p^k+1}
 \le\frac1{p^k+1}
 <\frac1{p^k-p^{-j}}=p^j\rho_h,
\]

we have $\omega_i-r_i=p^i(\rho_h-p^{-j}\delta)>0$. Also

\[
 w\ge w_k^-\ge\frac1{p+1}>\rho_h.
\tag{PL12}
\]

The middle inequality follows because $(p^k-1)/(p^k+1)$ increases with $k$. These observations give the useful strict bounds

\[
 w(q-1)>1,
 \qquad p^{h-i}\omega_i(q-1)>d.
\tag{PL13}
\]

For the second, its right-hand expression with $\omega_i$ replaced by $r_i$ is

\[
 p^{h-i}r_i(q-1)
 =p^{h-i}s(q-1)-q
 \ge\frac{q-p}{p-1}
 =p+p^2+\cdots+p^{h-1}>d.
\]

## 4. Integral scaled logarithms and their reductions

Choose a positive integer $e$ clearing all weight denominators, and extend the coefficient field by a root $\pi$ of $\pi^e=p$. Put $\alpha_i=\pi^{e\omega_i}$ and $\gamma=\alpha_0=\alpha_j$. The extension is used only to represent rational weights as coefficient valuations.

The contracted line logarithm is $\alpha_0^{-1}L_0(\alpha_0S)$. Its nonlinear coefficient at $S^{q^m}$ has valuation

\[
 (q^m-1)w-m>0
\]

by (PL13) and $(q^m-1)/(q-1)\ge m$. Its reduction is the identity.

For the ordinary dual arrows, direct calculation gives

\[
 p\omega_{i-1}-\omega_i=1\quad(2\le i\le d).
\]

The exceptional arrow has strictly larger defect:

\[
 p^2\omega_d-\omega_1
 =p+1-p^{1-j}(q-1)\delta>1,
\tag{PL14}
\]

because $\delta<p^j\rho_h$. Iterating monomial arrows gives a weight increment at least $1+p+\cdots+p^{n-1}$ after $n$ arrows. Hence each term $M^{\circ n}/p^n$ with $n\ge2$ is strictly positive in the contracted coefficient valuation. Only the ordinary first arrows survive reduction. Because $\pi^e=p$, their unit coefficients are exactly one. Therefore the contracted dual logarithm has reduction

\[
 \overline{\widetilde L}_1=Y_1,\qquad
 \overline{\widetilde L}_i=Y_i+Y_{i-1}^p\quad(2\le i\le d).
\tag{PL15}
\]

Both contracted logarithms are integral formal maps with identity linear term, so their inverses are integral by coefficientwise formal inversion. This proves the required assertion about the full inverse maps, not just their first terms.

Now substitute the actual additive line. The contracted dual input is

\[
 z_i(T)=v_i\gamma\alpha_i^{-1}T.
\]

For $i>j$, its coefficient has positive valuation because $\omega_i<w$. For $i<j$, $v_i\in p\mathcal O$ by the choice of $j$, whereas

\[
 0<\omega_i-w=\delta(1-p^{i-j})<s<1.
\]

Thus these input coefficients also have positive valuation. This is where the unramified integral lattice matters: a nonunit coefficient has valuation at least one. Only $z_j=v_jT$ survives reduction. The contracted scalar input is $uT$.

Solving (PL15) recursively gives

\[
 \overline{\widetilde E}_i(z(T))=
 \begin{cases}
 0,&i<j,\\
 (-1)^{i-j}\bar v_j^{p^{i-j}}T^{p^{i-j}},&i\ge j,
 \end{cases}
\tag{PL16}
\]

and $\overline{\widetilde E}_0(uT)=\bar uT$. Oddness of $p$ preserves the indicated signs under taking $p$th powers. In particular

\[
 \overline{\widetilde E}_d(z(T))
 =(-1)^{k-1}\bar v_j^{p^{k-1}}T^{p^{k-1}}.
\]

## 5. The unique weighted initial monomial

Let $b_{\boldsymbol\omega}(S,\mathbf Y)=b(\alpha_0S,\alpha_1Y_1,\ldots,\alpha_dY_d)$. We prove that its coefficient infimum is $\tau$ and that, with

\[
 \mu=\frac{\alpha_0\alpha_d^p}{p},\qquad v(\mu)=\tau,
\]

its full initial form is

\[
 \boxed{\overline{\mu^{-1}b_{\boldsymbol\omega}}=SY_d^p.}
\tag{PL17}
\]

### First family in (PL8)

For the dual index $i$, put

\[
 A_i=p^iw+\omega_i
     =s+p^i\bigl(s-\delta(1+p^{-j})\bigr).
\]

The quantity in parentheses is positive, because $\delta\le2s/(p^k+1)$ and $p^k+1>2(1+p^{-j})$. Thus $A_i$ strictly increases with $i$. Its smallest baseline satisfies

\[
 A_1-1-\tau
 =\delta\bigl(p^k-p+1-p^{1-j}\bigr)>0.
\tag{PL18}
\]

The strict inequality uses $h=j+k>2$: if $k=1$, then $j>1$ and the bracket is $1-p^{1-j}>0$; if $k>1$, it is positive even when $j=1$. Consequently every first-family baseline lies strictly above $\tau$, and $A_i>1$ because $\tau\ge0$.

The general first-family term has valuation

\[
 p^n\bigl(p^{lh+i}w+\omega_i\bigr)-n-l-1.
\]

Its excess over the baseline $A_i-1$ is

\[
 (p^n-1)A_i-n+p^{n+i}w(q^l-1)-l.
\tag{PL19}
\]

Both summands are nonnegative, and each is strictly positive when its respective index $n$ or $l$ is positive, using $A_i>1$, $p^n-1\ge n$, and (PL13). Hence the entire first family is strictly above $\tau$.

### Product family in (PL8)

Write $a\ge0$ for the line-logarithm index and $e_i=h-i$. Its valuation is

\[
 q^a w+p^{lh+e_i}\omega_i-a-dl-e_i.
\]

At $a=l=0$, the excess over $\tau$ is

\[
 w+p^{e_i}\omega_i-e_i-\tau
 =\frac{p^{e_i}-1}{p-1}-e_i.
\tag{PL20}
\]

This is zero precisely when $e_i=1$, that is, $i=d$; it is positive for $e_i>1$. The higher-index excess over this baseline is

\[
 w(q^a-1)-a+p^{e_i}\omega_i(q^l-1)-dl.
\tag{PL21}
\]

Again both summands are nonnegative, and strictly positive for a positive corresponding index, by (PL13). Therefore the unique term with valuation $\tau$ is the $+SY_d^p/p$ term. Its scalar is exactly $\mu$, proving (PL17). No cancellation with another displayed term is possible at this weight.

## 6. Restriction of the full initial form

Composing (PL17) with the integral contracted inverse maps preserves integrality of $\mu^{-1}b_{\boldsymbol\omega}$. Reduction commutes with this formal composition. By (PL16),

\[
 \boxed{
 \overline{\mu^{-1}\beta(u\gamma T,\mathbf v\gamma T)}
 =(-1)^{k-1}\bar u\bar v_j^{p^k}T^{p^k+1}.}
\tag{PL22}
\]

The right side is nonzero, so the logarithmic restriction has coefficient infimum exactly $\tau$. Its derivative is nonzero in residue characteristic $p$, since $p^k+1\equiv1\pmod p$.

Moreover

\[
 \mu=\frac{\gamma^{p^k+1}}{p^{S_k}},
\]

as follows from $p\omega_d-1-p^kw=-S_k$ and the chosen common uniformizer. Taking the coefficient of $T^{p^k+1}$ in (PL22) therefore proves (PL6). The coefficient belongs to the original unramified field, so a positive valuation after scaling means divisibility by $p$ in the stated congruence.

This passage verifies the entire initial form after the inverse-logarithm restriction. It is stronger than merely finding one nonintegral coefficient in the unrestricted series.

## 7. A nonzero bounded multiplier cannot remove this obstruction

Here is the exact elementary strengthening needed for a theta germ which may vanish at the origin. Let $R$ be a complete discrete valuation ring of mixed characteristic with $v(p)=1$, let $\pi$ be a uniformizer, and let

\[
 B=R[[T]][1/\pi]
\]

be the ring of formal series with bounded coefficient denominators. Its coefficient infimum $\nu$ is multiplicative: divide each nonzero series by its attained minimum power of $\pi$ and reduce the product in the domain $k[[T]]$. It extends to a valuation on $F=\operatorname{Frac}(B)$. The residue field of this valuation is $\operatorname{Frac}(k[[T]])$: any fraction of valuation zero can be normalized to have numerator and denominator of coefficient infimum zero, and conversely every such residue fraction has lifts.

**Lemma.** Suppose $z\in B$ has zero constant term, $\nu(z)=t\in[0,s)$, and its initial form has a nonzero formal derivative. Then for every nonzero $f\in B$, the series $f\exp z$ has coefficient infimum $-\infty$.

**Proof.** The exponential $\exp(pz)$ is integral, and

\[
 \nu(\exp(pz)-1)=1+t,
\]

with initial form that of $pz$. For exponential order $n\ge2$, the valuation exceeds $1+t$ because

\[
 n(1+t)-v_p(n!)\ge n(1+t)-(n-1)s>1+t
\]

for odd $p$ and $t\ge0$.

If $f\exp z$ were bounded, then $E=\exp z$ would be an element of $F$. Its identity $E^p=\exp(pz)$ would force $\nu(E)=0$ and $\bar E^p=1$, hence $\bar E=1$ in the residue fraction field. Put $\eta=E-1$ and $a=\nu(\eta)>0$. If $a\ge s$, every term in $(1+\eta)^p-1$ has valuation at least $1+s>1+t$, a contradiction. If $a<s$, its unique lowest binomial term is $\eta^p$, of valuation $pa$. The initial form of $E^p-1$ is then a scalar multiple of a $p$th power in $\operatorname{Frac}(k[[T]])$. Its derivative is zero. The initial form of $pz$ has nonzero derivative, which is unchanged as a condition by multiplication by a nonzero scalar. Formal differentiation extends to the fraction field by the quotient rule, so this is again a contradiction. Thus $f\exp z$ is not bounded. ∎

The argument uses neither a unit constant coefficient nor a primitive leading term of $f$. A nonzero-multiplier hypothesis is necessary: the zero restriction would make every resulting jet zero. The independently written companion `DP41_bounded_multiplier_lemma.md` gives the same fraction-field argument in any finite number of variables.

## 8. Exact threshold and factorial slope

For $w\in[w_k^-,w_k)$, the number $\tau$ lies in $[0,s)$. Apply the lemma to

\[
 z(T)=\lambda\beta(u\gamma T,\mathbf v\gamma T).
\]

Its initial form has nonzero derivative by (PL22), since $\lambda$ is a unit. The restricted factor $V(\gamma T)$ is integral: the contracted inputs and inverse maps are integral by Section 4, all $\alpha_i$ are integral, and $U$ has integral coefficients. It is nonzero by (PL2). Hence $\nu_w(\Theta)=-\infty$ throughout this interval. For $0\le w<w_k^-$, monotonicity of weighted infima gives the same conclusion.

At $w=w_k$ the logarithmic coefficient infimum is $\tau=s$. The usual factorial inequality makes its exponential integral, with coefficient infimum zero because its constant term is one. The factor $V(\gamma T)$ is integral and nonzero. Gauss multiplicativity therefore gives

\[
 \nu_{w_k}(\Theta)=\nu_{w_k}(V)\in[0,\infty).
\]

For $w>w_k$, the two factors remain bounded by monotonicity. The exponential still has infimum zero, and multiplication again proves the finite equality in (PL4). If $U(0)$ is a unit, $V(0)$ is that same unit, and all these finite infima are zero.

In particular $v(a_n)\ge-w_kn$ for every $n$. If $\liminf v(a_n)/n$ exceeded $-w_k$, then some rational $w<w_k$ sufficiently close to $w_k$ would give a bounded weighted infimum, contradicting (PL4). Thus

\[
 \liminf_{n\to\infty}\frac{v(a_n)}n=-w_k.
\]

Legendre's exact identity $v(n!)=sn-s_p(n)/(p-1)$ gives both parts of (PL5), since $s_p(n)/n\to0$. The argument applies with zero coefficients assigned valuation $+\infty$; the unbounded alternative already forces infinitely many nonzero coefficients.

## 9. Intrinsic meaning of the active index

Let $D_i$ be the normalized integral invariant directions on $H$. For $i<d$, the exact logarithm along the $i$th coordinate has, through degree $p$,

\[
 L_H(te_i)=te_i+\frac{t^p}{p}e_{i+1}+O(t^{p+1}).
\]

The integral translation coefficient at degree $p$ is therefore

\[
 \frac{D_i^p}{p!}+\frac{D_{i+1}}p.
\]

Consequently, modulo $p$, $\bar D_i^{[p]}$ is a nonzero scalar multiple of $\bar D_{i+1}$. Along the last axis the first nonlinear logarithmic term has degree $p^2$, so $D_d^p/p!$ is integral and $\bar D_d^{[p]}=0$. These are the single restricted-$p$ chain of DP30, now read in the exact coordinates of DP41.

Invariant directions commute. Thus the restricted $p$-operation on a constant linear combination is additive and Frobenius-semilinear. The reduction of $\sum_i v_iD_i$ starts at its first nonzero index $j$, survives through its $(k-1)$st restricted power, and vanishes at its $k$th power, where $k=d-j+1=h-j$. Later indices cannot cancel this leading surviving chain component. This proves the intrinsic description in Section 1.

Since $k\ge1$,

\[
 c_k^{\mathrm{path}}=\frac{s}{p^k+1}\le\frac{s}{p+1}=\rho_2,
\]

with equality exactly at $k=1$. The lower coefficients $v_i\in p\mathcal O$ do not change this answer, as the scaled-input calculation explicitly proves.

## 10. Scope and check status

This is an exact result for the invariant primitive Poincaré kernel on the actual pair and every logarithmic line whose two projections are primitive in the stated unramified lattices. It permits an arbitrary integral theta-type prefactor with nonzero restriction. It supplies a concrete upper limitation on the asymptotic derivative slope along those lines, and improves DP36's sufficient last-axis residual from $\rho_h$ to the sharp $\rho_2$.

It does not identify a prescribed global theta normalization with this primitive kernel. It does not cover nonprimitive or zero projections, nonunit exponential parameters, arbitrary other local gauges, or selected harmonic differential polynomials. A geometric construction must still identify its prescribed expression, lattice and path; a shorter lift count still needs its global numerical inequality. No nonexistence theorem for all shorter chains is asserted.

The proof uses DP41's exact formula (ER10) and exact coordinate logarithms, whose source is Zink's display pairing and the cited actual-dual construction. The weighted initial-form argument, arbitrary primitive-vector reduction, fraction-field multiplier proof, coefficient congruence and factorial slope were independently derived here. Actual complete-proof rereads, input hashes and independent reviewer reports are recorded in `dp42_mixed_line_checks.json` after the saved text is checked. No Lean execution or machine proof is claimed.
