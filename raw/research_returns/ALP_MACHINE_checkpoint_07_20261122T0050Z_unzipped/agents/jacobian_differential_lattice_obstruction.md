# AM-K019 — what the full theta differential module cannot supply

Author: `/root/kummer_extension`, GPT-6 Astra Pro, ALP_MACHINE, 21 November 2026 UTC. This is a new, elementary obstruction to one proposed iteration argument. It does not obstruct a selected harmonic functional, an evaluated jet ideal, or a quotient with separately controlled saturation. The accepted source connection-integrality theorem is used as a theorem.

## 1. Exact statement

Let $J=\operatorname{Jac}(y^2=x^7-1)$, let $u_1,u_2,u_3$ be the invariant logarithmic coordinates of AM-K012, and let $f$ be either the actual translated, value-one reduced theta function $F$, or the actual trace-one reduced section $\sigma_q$. On the complement of its zero divisor put
\[
z_i=\partial_i\log f.
\tag{K20.1}
\]
The following assertions hold.

1. The six meromorphic functions $u_1,u_2,u_3,z_1,z_2,z_3$ are algebraically independent over the field $\mathbb C(J)$ of abelian functions. In particular, adjoining only the three logarithmic coordinate multipliers does not put $f$ in a finite-dimensional vector space over $\mathbb C(J)(u_1,u_2,u_3)$ preserved by ordinary invariant differentiation.
2. Adjoining the three $z_i$ does give the expected polynomial rank-one connection module. In its natural integral polynomial lattice, however, every ordinary differentiated vector $\partial_i^N f/f$ has a monic term $z_i^N$. No positive restricted power of that connection maps the whole lattice into $p$ times the lattice, and no lattice commensurable with it by a bounded power of $p$ can have that property.
3. The source's actual integral connection on its auxiliary-variable module has an analogous obstruction: its creation term produces a unit coefficient of auxiliary degree $N$ after $N$ iterations. At prime-to-$p$ tensor power and in a primitive tangent direction, a positive restricted power cannot map that whole integral module into $p$ times itself, even after a bounded-denominator commensurable change of lattice.

The distinction in assertion 2 is essential. The abstract polynomial lattice injects into the characteristic-zero evaluated Hurwitz series, but its reduction modulo $p$ need not inject. In the present translated value-one example, each $z_i$ has zero constant term, so $z_i^p=0$ in the reduced Hurwitz ring. Positive $p$-adic bounds on evaluated derivatives therefore coexist with the polynomial-lattice obstruction.

## 2. The lattice shifts span all six complex directions

Write $J(\mathbb C)=V/\Lambda$, where $V=\mathbb C^3$. Its principal polarization is represented by the nondegenerate positive Hermitian form $H$, linear in the first variable. The actual reduced theta multiplier, checked in AM-K018, is
\[
f(u+\lambda)=\alpha(\lambda)
 \exp\left(\pi H(u,\lambda)+\frac\pi2H(\lambda,\lambda)\right)f(u).
\tag{K20.2}
\]
Consequently
\[
z_i(u+\lambda)=z_i(u)+\pi H(e_i,\lambda).
\tag{K20.3}
\]
If a translated representative changes the semicharacter or a constant factor, differentiation removes that change, so (K20.3) is identical for $F$ and $\sigma_q$.

Let $C$ be the nonsingular complex matrix with
$(\pi H(e_i,\lambda))_i=C\overline\lambda$. The shift subgroup of the six displayed functions is
\[
\Gamma=\{(\lambda,C\overline\lambda):\lambda\in\Lambda\}
 \subset\mathbb C^6.
\tag{K20.4}
\]
Choose a real lattice basis $\lambda_1,\ldots,\lambda_6$. The six vectors
$(\lambda_j,C\overline{\lambda_j})$ are complex-linearly independent. Indeed, a complex-linear functional $(a,b)$ vanishing on them vanishes on their real span. Since the $\lambda_j$ span $\mathbb C^3$ over $\mathbb R$, this gives
\[
a\lambda+bC\overline\lambda=0\qquad(\lambda\in\mathbb C^3).
\]
Replacing $\lambda$ by $i\lambda$ and combining the two equations gives $a\lambda=0$ and $bC\overline\lambda=0$ for every $\lambda$. Thus $a=b=0$. The six-column square matrix has full complex rank.

It follows that $\Gamma$ is Zariski dense in $\mathbb C^6$: after an invertible complex linear transformation this is the familiar assertion that $\mathbb Z^6$ is Zariski dense. The latter follows by induction on the number of variables, applying the fact that a nonzero univariate polynomial has only finitely many roots.

Suppose a polynomial relation among $u,z$ has coefficients in $\mathbb C(J)$. Its pullback is an identity of meromorphic functions on $V$. Choose $u_0$ avoiding the finitely many coefficient poles and the zero divisor of $f$. Periodicity of the coefficient functions and of the theta divisor permits substitution of every $u_0+\lambda$. The polynomial with coefficients evaluated at $J(u_0)$ vanishes on
$(u_0,z(u_0))+\Gamma$, so Zariski density makes every one of those coefficients zero. Varying $u_0$ on a nonempty open set makes every original rational coefficient zero. This proves assertion 1's algebraic-independence claim.

The same independence holds after any algebraic extension of the abelian-function field, for example the finite ordered-divisor cover used in AM-K012. Algebraic extension does not change the transcendence degree of the composite field. Thus the explicit Abel-coordinate ring used for integral calculations causes no exception to the argument.

## 3. Monic derivatives exclude finite rank over abelian functions and $u$

Put $K=\mathbb C(J)$. The Hessians
\[
\partial_i z_j=-W_{ij}
\tag{K20.5}
\]
are abelian functions. For $F$ they are the translated Kleinian functions of AM-K012; for $\sigma_q$ they are the corresponding unshifted ones. In either case $D_iK\subset K$.

Fix $i$. Recursively set
\[
P_0(Z)=1,\qquad P_{N+1}(Z)=D_iP_N(Z)+ZP_N(Z),
\quad D_iZ=-W_{ii}.
\tag{K20.6}
\]
Then
\[
\frac{\partial_i^N f}{f}=P_N(z_i),\qquad
P_N(Z)=Z^N+\text{terms of degree below }N,
\quad P_N\in K[Z].
\tag{K20.7}
\]
Both statements follow by induction. Differentiating a coefficient preserves $K$; differentiating $Z^r$ lowers its $Z$-degree; multiplication by $Z$ produces the next unique leading term with coefficient one.

The $P_N(z_i)$ are linearly independent over $K(u_1,u_2,u_3)$, since $z_i$ is transcendental over that field and their degrees are strictly increasing. A finite-dimensional vector space over that field, consisting of actual meromorphic germs and containing $f$, cannot be preserved by $\partial_i$: otherwise the infinite sequence $f,\partial_i f,\partial_i^2 f,\ldots$ would be linearly dependent. This proves the stated finite-rank obstruction. It concerns ordinary differentiation on the actual reduced functions. It does not exclude a different connection on an auxiliary bundle, or assert that no rank-one connection exists after adjoining the $z_i$.

For algebraic constant-field variants, this conclusion persists on extension from a number field to a characteristic-zero completion. To see the needed elementary descent, clear the finitely many rational denominators in a hypothetical relation. It becomes a finite linear relation, over the extended constant field, among coefficientwise number-field formal germs. Linear independence of any finite collection of such germs is witnessed by a nonzero finite coefficient minor; that minor remains nonzero after constant-field extension. Hence no such new relation appears. This statement is about finitely many rational-function coefficients and does not assert descent of an infinite analytic relation.

## 4. The natural polynomial connection is integral but has no full-module gain

Let $\mathcal O$ be a good local coefficient DVR, with uniformizer $p$, and use the explicit $D$-stable integral ordered-divisor ring $R$ of AM-K012 near the translated non-effective characteristic. Thus $D_iR\subset R$, $W_{ij}\in R$, and all evaluated coefficients lie in the integral Hurwitz ring. A harmless unramified extension splits the branch points; no ramified change of uniformizer is being hidden.

Define
\[
A=R[Z_1,Z_2,Z_3],\qquad
\delta_i|_R=D_i,\qquad \delta_i Z_j=-W_{ij}.
\tag{K20.8}
\]
The derivations commute because the mixed third derivatives of the actual theta logarithm agree. On the free rank-one $A$-module $M=Ae$ define
\[
\nabla_i(ae)=(\delta_i a+Z_i a)e.
\tag{K20.9}
\]
Its characteristic-zero realization is $Z_i\mapsto z_i$, $e\mapsto F$. The algebraic independence above makes this realization faithful over the fraction field. Formula (K20.7) gives
\[
\nabla_i^Ne=P_N(Z_i)e,
\qquad [Z_i^N]P_N=1.
\tag{K20.10}
\]
All coefficients are integral; one of them is a unit. Therefore
\[
\nabla_i^Q M\not\subset pM\qquad\text{for every }Q\ge1.
\tag{K20.11}
\]
This conclusion does not depend on the nilpotence length of the derivation $D_i$ on $R/pR$.

Here is the precise bounded-denominator strengthening. Suppose a lattice $M'$ in $M[1/p]$ satisfies
\[
p^a e\in M',\qquad M'\subset p^{-C}M
\tag{K20.12}
\]
for fixed nonnegative integers $a,C$. These hypotheses hold for any lattice commensurable with $M$ by a bounded power of $p$. If, for some $Q\ge1$,
$\nabla_i^Q M'\subset pM'$, then iteration gives
\[
p^aP_{nQ}(Z_i)e=\nabla_i^{nQ}(p^ae)
 \in p^nM'\subset p^{n-C}M.
\tag{K20.13}
\]
The coefficient of $Z_i^{nQ}$ on the left is $p^a$. For $n>a+C$ this contradicts (K20.13). Thus no such commensurable lattice supplies the proposed uniform restricted-power divisibility.

### The evaluated Hurwitz image is a different lattice problem

For the translated $F$, $z_i(0)=0$. Reduction of a Hurwitz series with zero constant term has $p$-th power zero: the multinomial coefficients in a $p$-fold product cancel modulo $p$, equivalently the only surviving Frobenius term is the $p$-th power of the constant coefficient. Hence
\[
\operatorname{ev}(Z_i^p)=z_i^p=0
 \quad\text{in the characteristic-}p\text{ Hurwitz ring},
\tag{K20.14}
\]
whereas $Z_i^p\ne0$ in $A/pA$. The reduction of evaluation has a nontrivial kernel even though characteristic-zero evaluation is injective. It also admits additional integral elements after saturation in its characteristic-zero image; for instance the image of $Z_i^p/p$ is integral although the abstract polynomial is not in $A$.

Consequently (K20.11) does **not** refute the actual congruences of AM-K017, nor the actual all-order lower bounds of AM-K013–015. It refutes the attempt to infer those bounds by a uniform divisibility operator on this unsaturated polynomial lattice, or on a lattice differing from it by a fixed power of $p$. An iterative argument in the evaluated image must specify that image, its $p$-saturation, and the growth of the saturation cost. The isolated mod-$p$ theta identities supply none of those bounds by themselves.

## 5. The same issue is visible in the actual source connection

The source definition is `ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/TaylorDiscriminants/ConnectionKillsSeries.lean`, `sgOf` at 18–19, `sg1` at 21–22, `nabla` at 31–35, `Hset` at 41–43, and `ConnectionIntegrality` at 77–83. The accepted theorem realizing the latter is `WickVanishing/ExpConjConnectionIntegral.lean`, lines 40–82. These exact files were inspected; no rederivation of their established integral-connection assertion is made.

Use $X$ for its formal-group variables and $Z=(Z_1,\ldots,Z_d)$ for its auxiliary variables. Put $s_i(X)=-\partial_{Y_i}h(X,0)$. The source operator is
\[
\nabla_{u,\phi}
 =D_u^X+\sum_i(D_us_i+\phi_i)\partial_{Z_i}
  -\kappa\sum_i(Z_i-s_i)u_i.
\tag{K20.15}
\]
Its admitted integral lattice of directions has
$\phi=\phi_0-Su$ with $u,\phi_0$ integral and $S=ds(0)$. Conjugating by the source factor $\exp(\kappa h_L(X))$, which depends only on $X$, gives an operator of the form
\[
T=e^{-\kappa h_L}\nabla_{u,\phi}e^{\kappa h_L}
 =D_u^X+\sum_i A_i(X)\partial_{Z_i}
  -\kappa\sum_i u_iZ_i+b(X).
\tag{K20.16}
\]
The accepted source theorem states that $T$ preserves the integral formal-power-series module $\mathcal N=\mathcal O[[X,Z]]$. Equivalently the coefficients in this particular first-order expression are integral; this also follows directly by applying preservation to $1,X_j,Z_i$. For the argument below, preservation itself is sufficient.

Assume $p\nmid\kappa$ and $u$ is primitive, so some $u_j$ is a unit. Starting at $1$, $T^N1$ is polynomial in $Z$ of degree at most $N$, with coefficients in $\mathcal O[[X]]$. Every term of $T$ except multiplication by $-\kappa u\cdot Z$ preserves or lowers $Z$-degree. Induction therefore gives the exact highest homogeneous part
\[
\operatorname{top}_Z(T^N1)=(-\kappa u\cdot Z)^N.
\tag{K20.17}
\]
Its coefficient of $Z_j^N$ is $(-\kappa u_j)^N$, a unit. Hence
\[
T^Q\mathcal N\not\subset p\mathcal N
 \qquad(Q\ge1).
\tag{K20.18}
\]
The same argument as (K20.12)–(K20.13), replacing $e$ by $1$, rules out a bounded-denominator commensurable lattice with such a uniform gain. The source's integral connection preserves an integral lattice; it does not make a positive power of each creation operator divisible by $p$ on the whole lattice.

This is fully compatible with the source `ValueSt`, lines 71–75: after the specified constant-coefficient evaluation, the relevant connection polynomial gives an ordinary invariant derivative. That evaluation annihilates the positive auxiliary powers responsible for (K20.17). Harmonic contractions and other selected quotients can likewise remove them. Any stronger gain must be proved for the actual selected evaluation or quotient, including its saturation and normalization, rather than deduced from full-module nilpotence that is false.

## 6. Consequence for the current proof-transfer attempt

AM-K018 identifies the full-$\mathcal O_E$ source gauge with the actual Chern/Baker gauge on ordinary powers of $J$. The obstruction above does not undo that identification. It specifies why the full mixed mod-11 congruences of AM-K017 cannot automatically be iterated through a finite-rank ordinary-differential module, and why even the actual source integral connection does not supply the proposed uniform restricted-power inclusion on its full auxiliary module.

The viable remaining arithmetic question is therefore more precise: determine the actual evaluated or harmonic-selected theta image, bound its $p$-saturation in the required degree, and compare that bound with the projection and normalization costs. The accepted DP54/58/59 examples now apply in the exact Chern gauge at 11; DP45/53 at the order-six Frobenius classes remain bare integral-function inputs until their actual primitive theta kernel or selected-value interface is supplied.

Primary source for (K20.2): Bannai, K., & Kobayashi, S. (2010). Algebraic theta functions and the $p$-adic interpolation of Eisenstein–Kronecker numbers. *Duke Mathematical Journal, 153*(2), 229–295, Definition 1.8 in [arXiv:math/0610163v4](https://arxiv.org/pdf/math/0610163). The actual multiplier and source compatibility were proved in AM-K018; the arguments in §§2–5 above are new elementary arguments, with the accepted source integral-connection theorem explicitly separated.
