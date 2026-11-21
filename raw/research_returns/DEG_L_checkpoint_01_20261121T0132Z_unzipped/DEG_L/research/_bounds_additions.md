## B10. An integral Hom covolume bound replaces individual coefficient bounds

**Setup.** Let $Y$ be a smooth projective variety of dimension $d\ge1$, with an integral ample class $H$, and fix a base point for its Albanese map $\alpha:Y\to B=\operatorname{Alb}(Y)$. Let $(A_i,L_i)$ be polarized abelian varieties, for $1\le i\le k$. Put
\[
 \Lambda_i=\operatorname{Hom}(B,A_i),\qquad
 E_i(u)=\int_Y (u\alpha)^*c_1(L_i)H^{d-1},\qquad
 V=\int_YH^d.
\]
Here maps are homomorphisms; translations do not affect the forms, energies or degrees. Assume $r_i=\operatorname{rank}\Lambda_i>0$. Let $q_i$ be the real quadratic metric with square norm $E_i$, let $C_i$ be the Euclidean covolume of $\Lambda_i$ for $q_i$, and let $\mu_i>0$ be any known lower bound for $E_i(u)$ for nonzero integral $u$. One may always take $\mu_i=1$. Set
\[
 v_r=\frac{\pi^{r/2}}{\Gamma(1+r/2)},\qquad
 R_i=\frac{2^{r_i}}{v_{r_i}}\frac{C_i}{\mu_i^{(r_i-1)/2}}.
\]

**Statement.** The lattice $\Lambda_i$ contains $r_i$ independent homomorphisms $u_{ij}$, spanning $\Lambda_i\otimes\mathbb Q$, such that $E_i(u_{ij})\le R_i^2$. Suppose a specified real-multilinear period $P$ on $\prod_i(\Lambda_i\otimes\mathbb R)$ is nonzero. Some tuple of these homomorphisms has $P(u_{1j_1},\ldots,u_{kj_k})\ne0$. If the period is the integral of a wedge of $2d$ pulled-back one-forms, its nonvanishing implies that the product map
\[
 F=(u_{1j_1}\alpha,\ldots,u_{kj_k}\alpha):Y\longrightarrow\prod_i A_i
\]
has a $d$-dimensional image $Z$. For the product polarization $L=\bigotimes_i\operatorname{pr}_i^*L_i$, and the actual generic degree $\delta_F$ of $F$ onto $Z$,
\[
 \deg_L Z\le\frac{(\sum_iR_i^2)^d}{\delta_F V^{d-1}}.
\tag{B10.1}
\]
For 032, $d=2$ and $k=4$. More generally, if a target polarization $L'$ satisfies $B c_1(L)-c_1(L')$ nef for a known $B>0$, the right side is multiplied by $B^d$.

**Proof.** Homomorphisms inject into homomorphisms of their integral first homology lattices, so $\Lambda_i$ is a finitely generated free abelian group. Pullback on invariant one-forms depends linearly on the homomorphism. Writing a polarization as a positive sum of $i\eta\wedge\bar\eta$ shows that $E_i$ is a positive semidefinite real quadratic form. Its kernel is zero: if all pulled-back one-forms vanish on $Y$, the map $u\alpha$ has zero derivative and is constant; because $\alpha(Y)$ generates $B$ and both maps preserve the chosen origins, $u=0$. The intersection expression for $E_i$ is integral. Consequently its positive values on nonzero lattice vectors are at least one.

Let $\lambda_1\le\cdots\le\lambda_{r_i}$ be the successive minima of the Euclidean unit ball for this metric. Minkowski's second theorem gives
\[
 v_{r_i}\prod_j\lambda_j\le 2^{r_i}C_i.
\]
Since every $\lambda_j\ge\sqrt{\mu_i}$, one obtains $\lambda_{r_i}\le R_i$. The minima are attained, giving the required independent maps. They need not be an integral basis, and none is asserted: a rational spanning set is enough. If $P$ vanished on every tuple from these spanning sets, multilinearity would make it vanish identically, a contradiction. A map with image dimension smaller than $d$ pulls every smooth real $2d$-form back to zero, so the nonzero wedge period gives the image-dimension assertion.

For the degree bound, write $\beta=F^*c_1(L)$, a nef class. Its energy is $E=\beta H^{d-1}=\sum_iE_i(u_{ij_i})\le\sum_iR_i^2$. The mixed-intersection inequality
\[
 \beta^d\le\frac{(\beta H^{d-1})^d}{(H^d)^{d-1}}
\tag{B10.2}
\]
follows directly from surface Hodge index: for rational ample $\beta,H$, take smooth complete-intersection surfaces of suitable very ample multiples of $j-1$ copies of $\beta$ and $d-j-1$ copies of $H$, for $1\le j\le d-1$. Hodge index on each surface gives $a_j^2\ge a_{j-1}a_{j+1}$ for $a_j=\beta^jH^{d-j}$. These inequalities imply $a_d\le a_1^d/a_0^{d-1}$. Approximating nef $\beta$ by $\beta+\varepsilon H$ proves the required nef case by continuity. For $d=1$ it is equality, and for $d=2$ it is B5. Projection formula gives $\beta^d=\delta_F\deg_L Z$, proving (B10.1). Finally nefness of $Bc_1(L)-c_1(L')$ gives $E_{L'}\le B E_L$ after pullback and intersection with $H^{d-1}$, so the same argument proves the last assertion. QED.

**Exact imported lattice source.** Martin Henk, *Successive minima and lattice points*, arXiv:math/0204158v1, Theorem 1.3, printed p.2, and its proof in §3, printed pp.5--7, <https://arxiv.org/pdf/math/0204158>. The statement and complete proof were read; only the displayed upper-product inequality is imported here.

**What determinant is required.** On the real Hom space, let $w_1,\ldots,w_r$ be a basis of normalized analytic vectors, with real Gram matrix $G$. If the columns of $B$ express an integral basis of $\Lambda$ in these coordinates, then exactly
\[
 C_\Lambda^2=\det(B^{\mathsf t}GB)=|\det B|^2\det G.
\tag{B10.3}
\]
Replacing the analytic basis by an orthonormal one replaces $B$ by $G^{1/2}B$ and preserves this covolume. Rallis can contribute to $G$ after the CM-period and measure comparisons are fixed; it does not identify $B$. If $\Gamma=\sum\mathbb Zw_j$ is commensurable with $\Lambda$, then
\[
 \frac{C_\Lambda}{C_\Gamma}
 =\frac{[\Gamma:\Gamma\cap\Lambda]}{[\Lambda:\Gamma\cap\Lambda]}.
\]
Thus a proved integral analytic sublattice $\Gamma\subset\Lambda$ with bounded Gram determinant already gives $C_\Lambda\le C_\Gamma$; no saturation-index upper bound is then needed. If instead $\Lambda\subset\Gamma$, its index contributes in the numerator and must be bounded. A uniform integer $M$ with $M\Gamma\subset\Lambda$ gives the sufficient bound $C_\Lambda\le M^r\sqrt{\det G}$. This identifies the exact direction of the integral comparison that a theta-index theorem would have to supply.

**Variation and normalization.** The ranks $r_i$ may grow when genuinely new cohomology appears at deeper source levels. Neither a rank-independent constant nor a uniform covolume is supplied by finite generation. For the fixed sublattice of old maps pulled through a degree-$e$ cover of the source, pull back $H$ as well. Then $E_i\mapsto eE_i$, $C_i\mapsto e^{r_i/2}C_i$, and a known $\mu_i$ becomes $e\mu_i$. Consequently $R_i\mapsto\sqrt e R_i$, $V\mapsto eV$, and $\delta_F\mapsto e\delta_F$; the reduced-image bound (B10.1) is unchanged. The actual generic degree in that bound must be retained. Replacing it by the trivial lower bound one can lose an essential cancellation. This proposition gives a sufficient determinant criterion for producing a small witness from prescribed source lattices. It is not a necessary condition for intrinsic bounded witness degree.

## B11. A fixed-order CM Hecke example separates the Hom regulator from witness degree

Let
\[
 E=\mathbb C/(\mathbb Z+i\mathbb Z),\qquad
 E_m=\mathbb C/(\mathbb Z+mi\mathbb Z),\quad m\ge1,
\]
with their degree-one polarizations. Then
\[
 \operatorname{Hom}(E,E_m)=m\mathbb Z[i],\qquad
 \deg(m(a+bi))=m(a^2+b^2).
\tag{B11.1}
\]
In particular the least positive degree grows with $m$, despite fixed rank and fixed CM field.

**Proof.** A homomorphism is multiplication by a complex number $\gamma$ with $\gamma\mathbb Z[i]\subset\mathbb Z+mi\mathbb Z$. Write $\gamma=x+mi y$ with $x,y\in\mathbb Z$. The further requirement $i\gamma\in\mathbb Z+mi\mathbb Z$ forces $m\mid x$. Thus $\gamma=m(a+bi)$, and the converse is immediate. The degree is the index of $\gamma\mathbb Z[i]$ in the target lattice, namely $|\gamma|^2/m=m(a^2+b^2)$. These elliptic curves are algebraic and have CM; multiplication by $m$ gives a degree-$m$ isogeny, so they lie in one polarized Hecke orbit. QED.

Here is a version with a fixed integral quadratic action and actual Weil witnesses. Put $A_m=E_m^4$ with product principal polarization $L_m$, and let $\mathbb Z[i]$ act by sending $i$ to
\[
 J=\operatorname{diag}\left(
 \begin{pmatrix}0&-1\\1&0\end{pmatrix},
 \begin{pmatrix}0&-1\\1&0\end{pmatrix}\right).
\]
This is an integral action for every $m$, has Rosati involution $J^\dagger=-J$, and has multiplicities $(2,2)$ on $H^{1,0}$, so $A_m$ is of Weil type for the same order. The diagonal isogeny $E^4\to E_m^4$ given by multiplication by $m$ commutes with this action and pulls the target polarization back to $m$ times the source polarization. Thus the example stays in the corresponding polarized quadratic-action Hecke orbit.

Let $Y=E^2$, $H$ its product degree-one polarization, and consider
\[
 f_m(x,y)=(mx,0,my,0),\qquad
 Z_m=E_m\times\{0\}\times E_m\times\{0\}\subset A_m.
\]
The image has $\deg_{L_m}Z_m=2$. Its Weil projection is nonzero: the extreme $i$-eigenline contains the nonzero $(2,2)$-form
\[
 (dz_1+i,dz_2)\wedge(dz_3+i,dz_4)
 \wedge(d\bar z_1+i,d\bar z_2)
 \wedge(d\bar z_3+i,d\bar z_4),
\]
whose restriction to $Z_m$ is $dz_1\wedge dz_3\wedge d\bar z_1\wedge d\bar z_3$ and has nonzero integral. Pairing with this Weil form detects the nonzero projection, by the Poincaré self-adjoint projector in B6.

The full fixed-source Hom lattice is
\[
 \operatorname{Hom}(E^2,A_m)=M_{4\times2}(m\mathbb Z[i]),
\]
of rank $16$. In the integral basis furnished by the real and imaginary matrix units, its energy metric is $m I_{16}$: the polarization form on $E_m$ is $\frac{i}{2m}dz\wedge d\bar z$, so multiplication by $m\gamma$ contributes $m|\gamma|^2$ to the energy. Consequently its least nonzero energy is $m$, its Gram determinant is $m^{16}$, and its metric covolume is $m^8$. Orthonormalizing the analytic coordinates transfers the factor $\sqrt m$ to the integral coefficients and changes none of these intrinsic metric quantities.

For the selected two-dimensional map, however,
\[
 f_m^*c_1(L_m)=mH,\quad
 E_{f_m}=2m,\quad V=H^2=2,\quad \delta_{f_m}=m^2,
\]
and therefore
\[
 \frac{E_{f_m}^2}{\delta_{f_m}V}=2=\deg_{L_m}Z_m.
\]
All assertions follow by the lattice-index calculation, product intersection, and the displayed invariant form. This supplies a precise counterexample to any claim that finite generation or an orthonormal analytic basis uniformly bounds integral map energy on a CM Hecke orbit. At the same time it supplies bounded nonzero Weil witnesses. It therefore does **not** refute intrinsic bounded division; it shows that a raw Hom-regulator bound is sufficient but unnecessary, and that generic-degree cancellation is mathematically essential.

## B12. The exact geometric quantity is an infimum of normalized energies

For a polarized Weil-type abelian $2n$-fold $(A,L)$, let $D_W(A,L)$ be the least degree of an effective integral $n$-cycle with nonzero Weil projection, or $+\infty$ if none exists. Then
\[
 D_W(A,L)=\inf_{(Y,f,H)}
 \frac{\bigl(f^*c_1(L)\cdot H^{n-1}\bigr)^n}
 {\delta_f (H^n)^{n-1}},
\tag{B12.1}
\]
where $Y$ runs over smooth projective $n$-folds, $f:Y\to A$ over morphisms generically finite onto an image $Z$ with nonzero Weil projection, $\delta_f$ is the generic mapping degree, and $H$ runs over integral ample classes on $Y$. The infimum of the empty set is understood to be $+\infty$.

**Proof.** The mixed-intersection inequality B10.2 and projection formula show that every expression on the right is at least $\deg_L Z\ge D_W(A,L)$. If a witness exists, at least one irreducible component has nonzero Weil projection and no larger degree. Positive degrees are integers, so a least-degree irreducible witness $Z$ exists. Take a projective resolution $f:Y\to Z\subset A$, with $\delta_f=1$, and put $\beta=f^*c_1(L)$. This is integral, big and nef, and $\beta^n=\deg_L Z=D_W(A,L)$. Fix an integral ample $H_0$. The classes $H_j=j\beta+H_0$ are integral ample. As $j\to\infty$,
\[
 \beta H_j^{n-1}=j^{n-1}D_W+O(j^{n-2}),\qquad
 H_j^n=j^nD_W+O(j^{n-1}).
\]
For $n=1$ the expression is already equality; for $n\ge2$ the quotient in B12.1 tends to $D_W$. This proves the reverse inequality and hence equality. QED.

This is an exact variational characterization, not an effective construction. It explains what a successful automorphic estimate would have to control: normalized energies for some witnesses, allowing their actual mapping degrees and source volumes. Requiring every theta coefficient or the entire Hom regulator to remain bounded is stronger than necessary. B10 provides one workable sufficient criterion with explicit constants. B11 shows why it is not an equivalence on a prescribed source. The infimum in B12 allows resolutions and polarizations of the unknown witnesses, so it does not close the open existence or uniformity problem by itself.

