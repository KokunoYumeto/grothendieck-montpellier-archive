## 6. DP39(a): unbounded gauge denominators can be completely invisible to harmonic jets

**Proposition.** For every prime $p$, there are integral formal-biextension data satisfying all the source's canonical-gauge identities, two canonical gauges, and a primitive integral algebraic germ $f=1$, such that the normalized series in one gauge has unbounded denominators but all the selected harmonic values are unchanged. More strongly, the equality holds for every germ $f$ when the polynomial is killed by the relevant contraction.

**Construction and proof.** Let $R=\mathbb Z_p$, $K=\mathbb Q_p$, let $F=\widehat{\mathbb G}_a^2$, and put $O=\mathbb Z\times\mathbb Z$ with involution $(a,b)^*=(b,a)$. Let $(a,b)$ act by $(X_1,X_2)\mapsto(aX_1,bX_2)$. Give the biextension the trivial cocycles `ph1=ph2=sy=ad=1`, namely the source's `FB.triv`.

Both

\[
 h_0(X,Y)=0,\qquad
 h_1(X,Y)=X_1Y_2+X_2Y_1
\]

are canonical gauges. The axes vanish. Biadditivity makes both addition coboundaries zero. Symmetry gives $h_1(Y,X)-h_1(X,Y)=0$. Finally

\[
 h_1((aX_1,bX_2),Y)
 =aX_1Y_2+bX_2Y_1
 =h_1(X,(bY_1,aY_2)),
\]

which is exactly the adjoint condition.

Take $w_0=(1,0)$. Then $w_0+w_0^*=1_O$ and
$h_{1,L}(X)=h_1(X,(X_1,0))=X_1X_2$.
For $k=1$ and $f=1$ the normalized series is

\[
 \exp(X_1X_2)=\sum_{n\ge0}(X_1X_2)^n/n!.
\]

Its coefficient valuations $-v_p(n!)$ tend to $-\infty$. Nevertheless, if
$\partial_U\partial_VP=0$,
then $P$ is a sum of a polynomial in $U$ alone and one in $V$ alone. Restricting $\exp(X_1X_2)$ to either axis gives one, so for every $f$,

\[
 P(\partial_1,\partial_2)\bigl(f\exp(X_1X_2)\bigr)(0)
 =P(\partial_1,\partial_2)f(0).
\]

Equivalently this follows from (TN7) for $Q=X_1X_2$. In the source's `AdmissibilitySecond` normalization, the matrix of the diagonal quadratic has off-diagonal entries one, so the displayed `secondOrder` is $2\partial_U\partial_V$. Its kernel over $K$ is the same. For $f=1$ all positive-degree harmonic values vanish and the constant value is one. ∎

This example concerns a trivial additive formal biextension. It is not claimed to be an ample theta divisor or a primitive Poincaré class. Its purpose is exact: even a primitive initial term of $f$ and unbounded full-series denominators do not by themselves imply a failure of harmonic selected-jet integrality.

## 7. DP39(b): the actual-pair two-column test defeats the stronger shortcut

This part uses the explicit primitive Poincaré coefficient proved in **DP38**, `primitive_poincare_first_coefficient_DP38.md`, SHA256 `4209c45180d5d45f8a8837c30d05642b110e00a13c6c7fd5d6aff74c0123d6d3`. I independently read and challenged that whole saved memo, including its cyclic-display calculation against the displayed Zink source formulas, and reported PASS at the observed clock01:56:49 UTC. The calculation below is independent of that display derivation. The exact required input is restated for clarity.

**Input.** Let $p$ be odd, $h\ge2$, $d=h-1$, and use the actual pair $G_h\times H$, $H=G_h^D$, of DP32. In logarithm coordinates let $B(x,\mathbf y)$ be a normalized rational splitting of the primitive Poincaré class with

\[
 B(x,0)=B(0,\mathbf y)=1,
 \qquad [x^p y_1]B=\kappa/p,
 \quad\kappa\in R^\times.
\tag{TN9}
\]

DP38's explicit invariant normalization has $\kappa=1$; only the fact that it is a unit is used. Define a two-copy kernel

\[
 \Theta=B(x_1,\mathbf y^{(1)})^{1/2}
             B(x_2,\mathbf y^{(2)})^{1/2}
\]

and the integral polynomial

\[
 P=X_1^pY_{1,1}-pX_1^{p-1}X_2Y_{1,2}.
\tag{TN10}
\]

**Claim 1: the full displayed HaO-type conditions hold.** Give the positive type one row, the negative type $d$ rows, and use two columns. Put row degrees $p$ on the positive row, $1$ on the first negative row and $0$ on its other rows. Coefficients are integral. Each monomial has exactly these row degrees. The sole positive row admits no row operation. The polynomial uses only the first negative row; the source's operations add an earlier row to a later row and therefore do not change it. Finally, for

\[
 \Delta_i=\partial_{X_1}\partial_{Y_{i,1}}
            +\partial_{X_2}\partial_{Y_{i,2}},
\]

one has $\Delta_iP=0$ for $i>1$ because these variables do not occur, and

\[
 \Delta_1P=pX_1^{p-1}-pX_1^{p-1}=0.
\]

Thus this polynomial satisfies the exact formal `harmK`, `RowInv`, `RowDeg`, and integral-coefficient requirements. It need not satisfy the stronger separate per-column contractions: the first contraction of the first term is nonzero.

**Claim 2: its primitive-kernel value is a unit.** Because $B-1$ vanishes on each axis, every monomial in it has positive $x$-degree and positive total $\mathbf y$-degree. Hence terms of order at least two in $(B-1)$ cannot contribute to a coefficient linear in $y_1$. The binomial expansion gives
$[x^p y_1]B^{1/2}=\kappa/(2p)$.
The first monomial in (TN10) therefore contributes

\[
 p!\,\kappa/(2p)=\kappa(p-1)!/2.
\]

The second contributes zero: on the first copy it takes $p-1>0$ derivatives in $x_1$ with all $\mathbf y^{(1)}=0$, and that factor is identically one. Thus

\[
 P(\partial)\Theta(0)=\kappa(p-1)!/2\in R^\times.
\tag{TN11}
\]

**Claim 3: every integral function on the actual product has a value divisible by $p$ for the same invariant polynomial.** Let $f$ be any integral function on $(G_h\times H)^2$. The coefficientwise height-$\ge2$ derivative bound gives
$D_{x_1}^p(R[[G_h\times H\times G_h\times H]])\subset pR[[G_h\times H\times G_h\times H]]$.
This also follows directly from the general bound at $n=p<q$: $v_p(p!)=1$ and $\lfloor(p-1)/(q-1)\rfloor=0$.
The remaining integral invariant derivations preserve that ideal and commute. The second summand in $P(D)$ has its explicit factor $p$ and otherwise only integral invariant derivations. Therefore

\[
 P(D)f(0)\in pR.
\tag{TN12}
\]

Equations (TN11)–(TN12) refute the proposed implication that the source's **summed harmonicity alone** transfers the entire integral-formal-function derivative bound through the primitive Poincaré exponential. All statements are stable under replacing the exponent $1/2$ by any $p$-adic unit, with the corresponding unit factor in (TN11).

**Scope.** This is an actual-formal-pair test with precisely the source-shaped HaO algebraic conditions, using the independently checked DP38 coefficient. It does not assert that $U=1$ is the algebraic germ of a global theta section, or that these row labels already define a new mixed-type global correspondence. It disproves a local implication; it does not exclude all possible weighted selected-connection estimates, all extra vanishing conditions on geometric theta sections, or all shorter global chains.

