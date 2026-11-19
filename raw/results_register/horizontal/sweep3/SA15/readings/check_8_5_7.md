# Independent check of Grothendieck's remark 8.5.7 (cote 4, scan 8)

| | |
|---|---|
| Item | MPL_8_079-081+9+4+100 (4:8), "Remarques 8.5.7" (injectivity of $v$ in (8.5.2)) |
| Checker | Claude Opus 5.5 at effort max, agent a922466087ec53798, independent check; launched by agent a28ea31fa17dd65e1 (Claude Opus 5.5 at effort max) for sweep 3 of the Grothendieck Montpellier archive |
| Date (UTC) | 2026-11-18 |
| Check type | independent re-proof |
| Verdict | **True as stated, for every $d\ge 1$ and every $n\ge 2$, with no extra condition.** Both of Grothendieck's special cases are correct. |

**Independence.** I read the transcription pages
`C:/Users/user/Documents/grothendieck_archive_transcription_20261110/returns/MPL_8_079-081+9+4+100_unzipped/pages/MPL_8_079-081+9+4+100_4_scan006.tex`
to `..._4_scan009.tex` and the published sources listed in section 7. I did not open STUDY.md, HUNCHES.md,
RESEARCH_PACKAGES.md, CHECK_EVENTS.tsv or any other file of `results_register/horizontal/sweep3/SA15/` (the
`readings/` folder included), nor `results_register/horizontal/sweep2/_tools_a28ea31f/s3data_SA15.py`. The proof
below is my own.

## 1. Verdict

The homomorphism
$$v:\ H^{n-1}(X,\mathcal O_X)_{SS}\longrightarrow H^{n-1}(Y,\mathcal O_Y)_{SS}$$
is injective for every smooth hypersurface section $Y$ of $X$, of every degree $d\ge 1$, for every $n\ge 2$.
Grothendieck's "Je pense que l'homomorphisme $v$ ... est injectif" is a theorem, and his two cases ($n=2$;
$H^{n-1}(X,\mathcal O_X(-d))=0$) are special cases of it.

**Key step.** Let $r: H^{n-1}(X,\mathcal O_X)\to H^{n-1}(Y,\mathcal O_Y)$ be the restriction. Then
$\operatorname{Ker} r=\operatorname{Im}\big(H^{n-1}(X,\mathcal O_X(-d))\to H^{n-1}(X,\mathcal O_X)\big)$, the map
induced by multiplication by the equation $s$ of the hypersurface. Raising
functions to the $p^e$-th power maps the ideal $s\cdot\mathcal O_X(-d)$ of $Y$ into $s^{p^e}\cdot\mathcal O_X(-p^ed)$,
so $F^e$ maps $\operatorname{Ker} r$ into the image of $H^{n-1}(X,\mathcal O_X(-p^ed))$, and that group is $0$ once
$p^ed$ is large (SGA 2, XII, Cor. 1.4). So $F$ is nilpotent on $\operatorname{Ker} r$. On
$H^{n-1}(X,\mathcal O_X)_{SS}$ it is bijective. Hence $\operatorname{Ker} v=\operatorname{Ker} r\cap
H^{n-1}(X,\mathcal O_X)_{SS}=0$. Frobenius replaces $d$ by $p^ed$; this reduces every case to Grothendieck's second
case.

## 2. The statement as decided

**Setting** (scan 6, "Théorème" 8.5; scan 7, (8.5.2); scan 8, 8.5.7). $k$ is a perfect field of characteristic
$p>0$. $X\subset\mathbf P^r_k$ is a smooth projective connected $k$-scheme of dimension $n\ge 2$, with
$\mathcal O_X(1)$ the restriction of $\mathcal O_{\mathbf P^r}(1)$. $H\subset\mathbf P^r_k$ is a hypersurface of degree
$d\ge 1$ with equation $s\in H^0(\mathbf P^r_k,\mathcal O(d))$, and $Y=X\cap H$ (scheme-theoretic intersection) is smooth
of dimension $n-1$. $I\subset\mathcal O_X$ is the ideal sheaf of $Y$, $i:Y\to X$ the closed immersion.

For a scheme $Z$ over $k$, $F_Z$ denotes the absolute Frobenius action on $H^j(Z,\mathcal O_Z)$: it is
$H^j(Z,\Phi_Z)$ for the map of sheaves of abelian groups $\Phi_Z:\mathcal O_Z\to\mathcal O_Z$, $f\mapsto f^p$. It is
additive and $p$-linear: $F_Z(\lambda\xi)=\lambda^pF_Z(\xi)$ for $\lambda\in k$. For a finite-dimensional $k$-vector
space $V$ with a $p$-linear endomorphism $F$, $V_{SS}$ is the largest $F$-stable subspace on which $F$ is bijective
(section 3). The maps are:

- $r:H^{n-1}(X,\mathcal O_X)\to H^{n-1}(Y,\mathcal O_Y)$, the restriction, i.e. $H^{n-1}$ of $\mathcal O_X\to i_*\mathcal O_Y$
  followed by $H^{n-1}(X,i_*\mathcal O_Y)=H^{n-1}(Y,\mathcal O_Y)$; it is $k$-linear and $r\circ F_X=F_Y\circ r$;
- $v:H^{n-1}(X,\mathcal O_X)_{SS}\to H^{n-1}(Y,\mathcal O_Y)_{SS}$, the restriction of $r$ (it lands in the $SS$ part
  by Lemma 1(d)).

**Theorem.** In this setting:

1. $F_X$ is nilpotent on $\operatorname{Ker} r$.
2. $v$ is injective. (This is the claim of 8.5.7.)
3. (Beyond 8.5.7.) For every $i\le n-2$ the restriction $H^i(X,\mathcal O_X)_{SS}\to H^i(Y,\mathcal O_Y)_{SS}$ is
   bijective, and the sequence
   $0\to H^{n-1}(X,\mathcal O_X)_{SS}\xrightarrow{v}H^{n-1}(Y,\mathcal O_Y)_{SS}\xrightarrow{\delta}H^n(X,I)_{SS}\to
   H^n(X,\mathcal O_X)_{SS}\to 0$ is exact, so $\operatorname{Coker} v\cong\operatorname{Ker}\big(H^n(X,I)_{SS}\to
   H^n(X,\mathcal O_X)_{SS}\big)$, with the $p$-linear map on $H^n(X,I)\cong H^n(X,\mathcal O_X(-d))$ made explicit in
   6.2.

**What the proof uses, and what it does not.** It uses: $X$ projective over a field of characteristic $p$, integral
of dimension $n$, with $\operatorname{depth}\mathcal O_{X,x}\ge n$ at closed points (true for $X$ smooth); and $Y$ the zero
scheme of a nonzero section of $\mathcal O_X(d)$, $d\ge1$. It does not use the smoothness of $Y$, the connectedness of
$Y$, or the perfectness of $k$ beyond the definition of $(\ )_{SS}$. Section 6.4 gives the general form.

## 3. Linear algebra of $p$-linear maps

**Lemma 1.** Let $k$ be a perfect field of characteristic $p$, $V$ a finite-dimensional $k$-vector space and
$F:V\to V$ additive with $F(\lambda x)=\lambda^pF(x)$.

- (a) For $e\ge0$, $F^e(V)$ and $\operatorname{Ker}F^e$ are subspaces and
  $\dim\operatorname{Ker}F^e+\dim F^e(V)=\dim V$.
- (b) The subspaces $F^e(V)$ decrease and are constant for $e\ge e_0$, some $e_0\le\dim V$. The subspace
  $F^{e_0}(V)$ is $F$-stable, $F$ is bijective on it, and it contains every $F$-stable subspace on which $F$ is
  bijective. So $V_{SS}=F^e(V)$ for all $e\ge e_0$.
- (c) With $V_{nil}:=\operatorname{Ker}F^e$ for $e\ge\dim V$: $V=V_{SS}\oplus V_{nil}$. In particular $F$ is nilpotent
  on $V$ if and only if $V_{SS}=0$.
- (d) If $u:V\to W$ is $k$-linear with $u\circ F=F\circ u$, then $u(V_{SS})\subset W_{SS}$ and $u(V_{nil})\subset
  W_{nil}$. Consequently $(\ )_{SS}$ is an exact functor on finite-dimensional $k$-spaces with $p$-linear
  endomorphism (morphisms: $F$-equivariant $k$-linear maps), and for an $F$-stable subspace $K\subset V$,
  $K\cap V_{SS}=K_{SS}$.
- (e) If $k\subset K$ is an extension with $K$ perfect, and $F_K:=F\otimes(\lambda\mapsto\lambda^p)$ on $V\otimes_kK$,
  then $(V\otimes_kK)_{SS}=V_{SS}\otimes_kK$.
- (f) If $k$ is algebraically closed, then $V^{F=1}=\{x: Fx=x\}$ is an $\mathbf F_p$-subspace of $V_{SS}$ and the map
  $V^{F=1}\otimes_{\mathbf F_p}k\to V_{SS}$ is an isomorphism.

*Proof.* (a) Since $k$ is perfect, $\sigma^e:\lambda\mapsto\lambda^{p^e}$ is an automorphism of $k$. Let $V'$ be $V$
with scalar multiplication $\lambda*x=\lambda^{p^e}x$; it is a $k$-vector space with the same subspaces as $V$ and
$\dim V'=\dim V$, and $F^e:V\to V'$ is $k$-linear. Rank-nullity for this linear map gives (a).
(b) The chain $F^e(V)$ decreases, so it is constant from some $e_0\le\dim V$ on; then $F(F^{e_0}V)=F^{e_0+1}V=F^{e_0}V$,
so $F$ is surjective on $F^{e_0}V$, hence injective by (a) applied to $F^{e_0}V$. If $W$ is $F$-stable with $F|_W$
bijective, then $W=F^e(W)\subset F^e(V)$.
(c) For $e\ge\dim V$ (so $e\ge e_0$), $F^e$ is injective on $V_{SS}=F^e(V)$, so $V_{SS}\cap\operatorname{Ker}F^e=0$,
and the dimensions add up to $\dim V$ by (a).
(d) $u(F^eV)=F^e(uV)\subset F^eW$, and $F^ex=0\Rightarrow F^eu(x)=u(F^ex)=0$. So a complex $V'\to V\to V''$ of such
maps is the direct sum of its $SS$ part and its $nil$ part, and it is exact if and only if both parts are; this is the
exactness. For $K\subset V$ $F$-stable, exactness applied to $0\to K\to V\to V/K\to0$ gives
$K_{SS}=\operatorname{Ker}(V_{SS}\to(V/K)_{SS})=K\cap V_{SS}$.
(e) $A:=V_{SS}\otimes K$ is $F_K$-stable, and $F_K$ is surjective on it, because its image is a $K$-subspace (by (a)
over $K$) containing $F(V_{SS})\otimes1=V_{SS}\otimes1$; so $F_K$ is bijective on $A$ by (a), and
$A\subset(V\otimes K)_{SS}$. $F_K$ is nilpotent on $B:=V_{nil}\otimes K$, so $B\subset(V\otimes K)_{nil}$. Since
$V\otimes K=A\oplus B=(V\otimes K)_{SS}\oplus(V\otimes K)_{nil}$ (by (c) for $V$ and for $V\otimes K$), counting
dimensions gives $A=(V\otimes K)_{SS}$.
(f) A fixed vector satisfies $x=F^ex\in F^eV$, so $V^{F=1}\subset V_{SS}$. Injectivity: if $\mathbf F_p$-independent
fixed vectors $x_1,\dots,x_m$ had a shortest nontrivial relation $\sum\lambda_ix_i=0$ over $k$ with $\lambda_1=1$,
applying $F$ and subtracting gives $\sum(\lambda_i^p-\lambda_i)x_i=0$, shorter, so all $\lambda_i\in\mathbf F_p$, a
contradiction. Surjectivity: let $e_1,\dots,e_m$ be a basis of $W=V_{SS}$ and $F(e_j)=\sum_ia_{ij}e_i$, $A=(a_{ij})$
invertible. Then $x=\sum x_je_j$ is fixed if and only if $x^{(p)}=A^{-1}x$, where $x^{(p)}=(x_j^p)$. The $k$-algebra
$k[x_1,\dots,x_m]/(x_j^p-(A^{-1}x)_j)_j$ has the monomials $x^\alpha$, $0\le\alpha_j<p$, as a basis (the leading terms
$x_j^p$ are pairwise coprime), so it has dimension $p^m$, and it is étale because its Jacobian matrix is $-A^{-1}$. As
$k$ is algebraically closed it has exactly $p^m$ points, so $\dim_{\mathbf F_p}W^{F=1}=m$; with injectivity this gives
the isomorphism. $\square$

Only the definition of $V_{SS}$ (that $F$ is injective on it) is needed for the injectivity of $v$ (Step 4 below).
Parts (c)-(d) serve item 3 of the theorem; parts (e)-(f) serve the second route for $n=2$ (5.2).

## 4. Proof of the theorem

**Step 0 (the ideal of $Y$).** $X$ is integral: it is connected, and its local rings are regular (smooth over $k$),
hence domains, so no two irreducible components meet (locators: smooth implies regular, Hartshorne, *Algebraic
Geometry*, III, Thm. 10.2 (locator unverified); regular local rings are domains, Atiyah-Macdonald, *Introduction to
Commutative Algebra*, Lemma 11.23 (locator unverified)). The restriction $s|_X\in H^0(X,\mathcal O_X(d))$ is nonzero,
since otherwise $Y=X$, which has dimension $n\ne n-1$. A nonzero section of an invertible sheaf on an integral scheme
is a nonzerodivisor in every stalk. Hence multiplication by $s$, $\mathcal O_X(-d)\to\mathcal O_X$, is injective with
image $I$, and for every $q\ge1$ multiplication by $s^q$, $\mathcal O_X(-qd)\to\mathcal O_X$, is injective with image
$I^q$ (the $q$-th power of the ideal, locally generated by $s^q$). So
$$I^q\cong\mathcal O_X(-qd)\quad\text{as }\mathcal O_X\text{-modules, for all }q\ge1.\tag{0}$$

**Step 1 (Frobenius on the restriction sequence).** Let $\iota:I\to\mathcal O_X$ be the inclusion and
$\pi:\mathcal O_X\to i_*\mathcal O_Y$ the quotient map. The sequence $0\to I\xrightarrow{\iota}\mathcal O_X
\xrightarrow{\pi}i_*\mathcal O_Y\to0$ is exact. $\Phi_X$ maps $I$ into $I$ ($f\in I\Rightarrow f^p=f^{p-1}f\in I$);
put $\Phi_I:=\Phi_X|_I:I\to I$. Since $\pi$ is a ring map, $\pi\circ\Phi_X=i_*\Phi_Y\circ\pi$. So
$(\Phi_I,\Phi_X,i_*\Phi_Y)$ is an endomorphism of this short exact sequence of sheaves of abelian groups. Cohomology of
$\mathcal O_X$-modules is the same computed in abelian sheaves (Hartshorne, III, Prop. 2.6 (locator unverified)), and
$H^j(X,i_*\mathcal O_Y)=H^j(Y,\mathcal O_Y)$ (Hartshorne, III, Lemma 2.10 (locator unverified)), compatibly with
Frobenius since $i_*\Phi_Y$ is the image of $\Phi_Y$. By naturality of the long exact cohomology sequence, the sequence
$$\cdots\to H^j(X,I)\xrightarrow{\iota_*}H^j(X,\mathcal O_X)\xrightarrow{r}H^j(Y,\mathcal O_Y)\xrightarrow{\delta}
H^{j+1}(X,I)\to\cdots\tag{1}$$
is exact, its maps are $k$-linear, and they commute with $F_I:=H^j(X,\Phi_I)$, $F_X$ and $F_Y$ (all $p$-linear). In
particular $F_X\circ\iota_*=\iota_*\circ F_I$, and $\operatorname{Ker} r=\iota_*H^{n-1}(X,I)$.

**Step 2 (Frobenius on $I$ raises the twist).** Let $e\ge0$ and $q=p^e$. The map $\Phi_I^e:I\to I$, $f\mapsto f^q$,
factors as
$$I\xrightarrow{\ \varphi_e\ }I^q\xrightarrow{\ \iota_e\ }I,\qquad\varphi_e(f)=f^q,$$
with $\iota_e$ the inclusion: $\varphi_e$ is well defined because locally $f=sg$ gives $f^q=s^qg^q\in I^q$, and it is a
map of sheaves of abelian groups (additive in characteristic $p$). Hence
$$F_I^e=H^j(X,\iota_e)\circ H^j(X,\varphi_e)\ \text{ factors through }\ H^j(X,I^q)\cong H^j(X,\mathcal O_X(-p^ed))
\ \text{ by (0)}.\tag{2}$$

**Step 3 (vanishing).** There is $m_0$ such that
$$H^j(X,\mathcal O_X(-m))=0\quad\text{for all }j\le n-1\text{ and all }m\ge m_0.\tag{3}$$
This is SGA 2, Exp. XII, Cor. 1.4, applied with its integer "$n$" equal to our $n-1$ and $\mathcal F=\mathcal O_X$: for
a projective scheme with very ample $\mathcal O_X(1)$ (the paragraph after 1.4 extends 1.4 from $\mathbf P^r_k$ to
this case), "$H^i(X,\mathcal F(-m))=0$ pour $i\le n$ et $m$ grand" is equivalent to "$\operatorname{prof}(\mathcal
F_x)>n$ pour tout point fermé $x$". Here, for $x\in X$ closed, $\mathcal O_{X,x}$ is a regular local ring of dimension
$n$ ($X$ smooth and irreducible of dimension $n$; Hartshorne, III, Thm. 10.2, and II, Exercise 3.20 (locators
unverified)), hence Cohen-Macaulay (Serre, *Algèbre locale, multiplicités*, IV.D, Cor. 3), so
$\operatorname{prof}\mathcal O_{X,x}=n>n-1$. (Equivalently: Serre duality on the smooth projective $X$, SGA 2, XII,
Remarque after Thm. 1.1, gives $H^{n-1}(X,\mathcal O_X(-m))^\vee\cong H^1(X,\Omega^n_{X/k}(m))$, which vanishes for
$m\gg0$ by Serre's theorem, EGA III, 2.2.1 (locator unverified).)

Choose $e$ with $p^ed\ge m_0$ (possible since $d\ge1$). By (2) and (3), $F_I^e=0$ on $H^j(X,I)$ for every $j\le n-1$.
So $F_I$ is nilpotent on $H^j(X,I)$ and $H^j(X,I)_{SS}=0$ for $j\le n-1$ (Lemma 1(c)).

**Step 4 (injectivity of $v$).** Let $\xi\in H^{n-1}(X,\mathcal O_X)_{SS}$ with $v(\xi)=0$, that is, $r(\xi)=0$. By
exactness of (1), $\xi=\iota_*(\eta)$ for some $\eta\in H^{n-1}(X,I)$. With $e$ as in Step 3,
$$F_X^e(\xi)=F_X^e(\iota_*\eta)=\iota_*(F_I^e\eta)=\iota_*(0)=0.$$
$F_X$ is bijective on $H^{n-1}(X,\mathcal O_X)_{SS}$ by definition, so $F_X^e$ is injective there, and $\xi=0$. So $v$
is injective. The same computation shows $F_X^e(\operatorname{Ker} r)=0$, which is item 1; item 2 also reads
$\operatorname{Ker} v=\operatorname{Ker} r\cap H^{n-1}(X,\mathcal O_X)_{SS}=(\operatorname{Ker} r)_{SS}=0$ (Lemma 1(c),(d)).
$\square$

**Step 5 (item 3).** (1) is an exact sequence of finite-dimensional $k$-spaces with $p$-linear endomorphisms and
equivariant $k$-linear maps (finite dimension: $X$, $Y$ projective). Apply the exact functor $(\ )_{SS}$ (Lemma 1(d))
and use $H^j(X,I)_{SS}=0$ for $j\le n-1$ (Step 3). For $i\le n-2$, both neighbours $H^i(X,I)_{SS}$ and
$H^{i+1}(X,I)_{SS}$ of $H^i(X,\mathcal O_X)_{SS}\to H^i(Y,\mathcal O_Y)_{SS}$ vanish, so it is bijective. For $i=n-1$,
$H^{n-1}(X,I)_{SS}=0$ on the left and $H^n(Y,\mathcal O_Y)=0$ on the right ($\dim Y=n-1$; Hartshorne, III, Thm. 2.7
(locator unverified)) give the exact sequence of item 3. $\square$

## 5. Grothendieck's two cases

**5.1. The case $H^{n-1}(X,\mathcal O_X(-d))=0$.** By (0), $H^{n-1}(X,I)\cong H^{n-1}(X,\mathcal O_X(-d))=0$, so $r$ is
injective by (1), and so is its restriction $v$. Correct; it is the case $e=0$ of Steps 2-4, where no Frobenius is
needed. By (3) it covers every $d\ge m_0$, which is Grothendieck's "degré $d$ assez grand".

**5.2. The case $n=2$.** Correct. Two independent arguments:

- *Route A.* The proof of section 4 with $n-1=1$. Step 3 needs only $H^1(X,\mathcal O_X(-m))=0$ for $m\gg0$, i.e.
  depth $\ge2$ at closed points (SGA 2, XII, Cor. 1.3/1.4), which holds for any normal projective surface.
- *Route B* (étale $\mathbf F_p$-cohomology and Lefschetz for $\pi_1$; the page gives no argument for $n=2$, so this is
  my reconstruction of a route available to him, not his text). Let $\bar k$ be an algebraic closure of $k$. Flat base
  change (Hartshorne, III, Prop. 9.3 (locator unverified)) gives $H^1(X,\mathcal O_X)\otimes_k\bar k=H^1(X_{\bar k},
  \mathcal O)$, with $F_{X_{\bar k}}=F_X\otimes(\lambda\mapsto\lambda^p)$, and likewise for $Y$; by Lemma 1(e),
  $v\otimes_k\bar k=v_{\bar k}$, and $v$ is injective if and only if $v_{\bar k}$ is. For $Z$ proper and reduced over
  $\bar k$, the Artin-Schreier sequence $0\to\mathbf Z/p\to\mathcal O_Z\xrightarrow{f\mapsto f^p-f}\mathcal O_Z\to0$ on
  $Z_{\mathrm{et}}$ and its long exact sequence $H^i(Z,\mathbf Z/p)\to H^i(Z,\mathcal O_Z)\xrightarrow{F-1}
  H^i(Z,\mathcal O_Z)\to\cdots$ (SGA 7 II, Exp. XXII (N. Katz), 1.3, as given in the corpus excerpt listed in section
  7), together with $H^i(Z_{\mathrm{et}},\mathcal O_Z)=H^i(Z,\mathcal O_Z)$ (SGA 4, VII, 4.3 (locator unverified)) and
  the surjectivity of $F-1$ on $H^0(Z,\mathcal O_Z)$, give $H^1_{\mathrm{et}}(Z,\mathbf F_p)\cong H^1(Z,\mathcal
  O_Z)^{F=1}$, naturally in $Z$. ($F-1$ is surjective on every finite-dimensional $\bar k$-space $V$ with $p$-linear
  $F$: on $V_{nil}$ it has the inverse $-\sum_{i\ge0}F^i$; on $V_{SS}$, in a basis of fixed vectors (Lemma 1(f)), it
  is $x_i\mapsto x_i^p-x_i$ coordinatewise, surjective as $\bar k$ is algebraically closed.) By Lemma 1(f),
  $H^1(Z,\mathcal O_Z)_{SS}\cong H^1_{\mathrm{et}}(Z,\mathbf F_p)\otimes_{\mathbf F_p}\bar k$. So it suffices that
  $H^1_{\mathrm{et}}(X_{\bar k},\mathbf F_p)\to H^1_{\mathrm{et}}(Y_{\bar k},\mathbf F_p)$ be injective. Apply SGA 2,
  Exp. XII, Cor. 3.5 to $X_{\bar k}$, the ample sheaf $\mathcal O(d)$ and the section $s$ (regular, by flat base change
  of Step 0), $X_{\bar k}$ having depth $2$ at closed points: $\pi_0(Y_{\bar k})\to\pi_0(X_{\bar k})$ is bijective and
  $\pi_1(Y_\alpha)\to\pi_1(X_\alpha)$ is surjective for each component $X_\alpha$ and $Y_\alpha=Y_{\bar k}\cap
  X_\alpha$. A $\mathbf Z/p$-torsor on $X_\alpha$ corresponds to a continuous homomorphism $\pi_1(X_\alpha)\to\mathbf
  Z/p$ (SGA 1, Exp. V (locator unverified)); if it is trivial on $Y_\alpha$, the homomorphism vanishes on the image of
  $\pi_1(Y_\alpha)$, which is everything, so the torsor is trivial. Hence the map is injective and $v$ is injective.

  Route B stops at $n=2$: for $n\ge3$, $H^{n-1}_{\mathrm{et}}(X,\mathbf F_p)$ is no longer controlled by $\pi_1$. This
  fits the page, where Grothendieck states $n=2$ and the large-$d$ case and only "pense" the general case.

## 6. Remarks

**6.1. Why the semisimple parts matter.** $\operatorname{Ker} r=\iota_*H^{n-1}(X,\mathcal O_X(-d))$ (via (0)). In
characteristic $0$ the analogous kernel vanishes by Kodaira vanishing. In characteristic $p$ Kodaira vanishing can fail
(M. Raynaud, "Contre-exemple au vanishing theorem en caractéristique $p>0$", in *C. P. Ramanujam, a tribute*, Springer
1978, 273-278 (locator unverified)), which is why Grothendieck puts the hypothesis $H^{n-1}(X,\mathcal O_X(-d))=0$ on
his second case. I have not decided whether $r$ itself can fail to be injective for a smooth hypersurface section; the
proof does not need it. What it shows is that whatever $\operatorname{Ker} r$ is, $F$ is nilpotent on it.

**6.2. The $p$-linear map on $H^j(X,I)$ in terms of $\mathcal O_X(-d)$.** Under $\alpha:\mathcal O_X(-d)\xrightarrow
{\sim}I$, $g\mapsto sg$ (Step 0), $\Phi_I$ becomes $g\mapsto s^{p-1}g^p$ (since $(sg)^p=s\cdot s^{p-1}g^p$), i.e. the
$p$-th power $\mathcal O_X(-d)\to\mathcal O_X(-pd)$ followed by multiplication by $s^{p-1}$; and $\Phi_I^e$ becomes
$g\mapsto s^{p^e-1}g^{p^e}$. So the operator on $H^n(X,I)\cong H^n(X,\mathcal O_X(-d))$ in item 3 is
$\xi\mapsto s^{p-1}\xi^{[p]}$, which depends on $s$, not only on $d$.

**6.3. Consequences on the page.** With $\operatorname{Ker} v=0$, the term $-\dim\operatorname{Ker} v$ disappears from
(8.5.5) and from 8.5.8 ("aux termes $-\dim\operatorname{Ker} v$ près (sans doute toujours nul, cf. 8.5.7)"), as
Grothendieck expected. By item 3, $\dim\operatorname{Coker} v=\dim H^{n-1}(Y,\mathcal O_Y)_{SS}-\dim
H^{n-1}(X,\mathcal O_X)_{SS}$, and $\operatorname{Coker} v\cong\operatorname{Ker}(H^n(X,I)_{SS}\to H^n(X,\mathcal
O_X)_{SS})$. These statements are consequences of the theorem above; I have not checked the crystalline exact sequence
(8.5.1), which rests on the ingredients Grothendieck admits in 8.5.

**6.4. General form.** The proof gives: let $X$ be a projective scheme over a field of characteristic $p$, integral of
dimension $n\ge1$, with $\operatorname{depth}\mathcal O_{X,x}\ge n$ at closed points; let $L$ be an ample invertible
sheaf, $s\in H^0(X,L)$ nonzero, $Y=V(s)$ with ideal $I_Y=s\cdot L^{-1}\cong L^{-1}$. Then $F_{I_Y}$ is nilpotent on
$H^j(X,I_Y)$ for $j\le n-1$, and the restriction
$H^i(X,\mathcal O_X)_{SS}\to H^i(Y,\mathcal O_Y)_{SS}$ is bijective for $i\le n-2$ and injective for $i=n-1$. For $L$
not very ample, (3) for $L^{-m}$ follows from SGA 2, XII, 1.4 applied to the locally free sheaves $L^{-b}$,
$0\le b<N$, with $\mathcal O(1):=L^N$ very ample. The perfectness of $k$ is needed only to define $(\ )_{SS}$; the
injectivity argument (Step 4) works for any $p$-linear $F$ that is injective on the subspace considered.

## 7. Sources, locators and literature route

**Opened and read at the cited place (verified):**

- [SGA 2] A. Grothendieck et al., *Cohomologie locale des faisceaux cohérents et théorèmes de Lefschetz locaux et
  globaux (SGA 2)*, édition recomposée, arXiv:math/0511279v1. Corpus file:
  `F:\user\Documents\arxiv_latex\library\_recovered_from_papers\by_title\Cohomologie locale des faisceaux cohérents et théorèmes de Lefschetz locaux et globaux (SGA 2).pdf`.
  - Exp. XII, Thm. 1.1 and the Remarque after it (Serre duality, also for $X$ proper and smooth): p. 109 (PDF p. 117;
    original pagination 136).
  - Exp. XII, Cor. 1.3 (p. 110, PDF p. 118; original p. 138) and Cor. 1.4 with the paragraph following it
    ("ces résultats restent trivialement valables pour un schéma projectif quelconque $X$ ..."): p. 111, PDF p. 119;
    original p. 139. Used in Step 3.
  - Exp. XII, Cor. 3.5 ($\pi_0$ bijective, $\pi_1$ surjective for the zero scheme of a regular section of an ample sheaf
    on $X$ of depth $\ge2$ at closed points): p. 120, PDF p. 128; original p. 152. Used in 5.2, Route B.
- [Serre AL] J.-P. Serre, *Algèbre locale, multiplicités*, 3e éd., LNM 11. Corpus file:
  `C:\Users\user\Documents\Papors\OS\Lecture Notes in Mathematics - 0011 - Algèbre Locale, Multiplicités, 3e édition (Jean-Pierre Serre, Pierre Gabriel).pdf`.
  Ch. IV, §D "Les anneaux réguliers", Corollaire 3: "Tout anneau local régulier est un anneau de Cohen-Macaulay", p.
  IV-37 (PDF p. 115). Used in Step 3.
- [SGA 7 XXII, excerpt] Corpus file
  `F:\user\Documents\arxiv_latex\library\_recovered_from_papers\by_title\SGA 7-2 — Pages 351–444 (FINAL).pdf`, a
  retypeset excerpt of SGA 7 II, Exp. XX (end) to XXII. Exp. XXII (N. Katz), 1.3 ([the user's words, omitted]): the
  Artin-Schreier sequence $0\to\mathbf Z/p\mathbf Z\to\mathcal O_X\xrightarrow{\wp}\mathcal O_X\to0$, $\wp(f)=f^p-f$,
  and its long exact sequence with $F^*-1$, PDF p. 17. The original SGA 7 II pagination was not checked. The excerpt
  does not contain the comparison $V^{F=1}\otimes\bar k\cong V_{SS}$; Lemma 1(f) proves it instead. Used in 5.2,
  Route B.

**Not opened (locator unverified):** Hartshorne, *Algebraic Geometry*, II Ex. 3.20; III Prop. 2.6, Thm. 2.7, Lemma
2.10, Prop. 9.3, Thm. 10.2 (basic facts in Steps 0, 1, 3, 5 and Route B); Atiyah-Macdonald, Lemma 11.23 (regular local
rings are domains); EGA III, 2.2.1 (Serre's vanishing theorem, alternative in Step 3); SGA 4, VII, 4.3 (étale and
Zariski cohomology of quasi-coherent sheaves); SGA 1, Exp. V (torsors and $\pi_1$); Raynaud 1978 (6.1). The main
proof (Steps 0-4) rests on SGA 2 XII 1.4 and Serre AL IV.D Cor. 3, both verified, plus the basic facts on smooth
schemes and sheaf cohomology listed here.

**Corpus route.** Queried with
`python -I -B scripts/query_corpus.py --layer research_literature --index-level canonical --json "TERMS"` in
`C:\Users\user\Documents\Papors\Chatnotes\Zeta-Function-Foundation`: "Hartshorne"; "Enriques Severi Zariski";
"Cohomologie locale des faisceaux coherents"; "Lefschetz locaux et globaux"; "Kodaira vanishing characteristic
Frobenius"; "semisimple Frobenius cohomology structure sheaf"; "Artin-Schreier etale cohomology structure sheaf
Frobenius"; "p-linear endomorphism semisimple nilpotent"; "Fonctions L modulo"; "SGA 4 1/2"; "Groupes de monodromie en
geometrie algebrique"; "Sur la topologie des varietes algebriques en caracteristique"; "Mumford Abelian varieties";
"Matsumura Commutative ring theory"; "Elements de geometrie algebrique IV". Hits used: SGA 2 (two PDF copies; the
arXiv one read), Serre LNM 11, the SGA 7-2 excerpt. Not found in the corpus: Hartshorne, SGA 4½, Serre's 1958 Mexico
paper, Mumford's *Abelian varieties*, Matsumura. I did not find this argument stated in the sources I opened; it is
self-contained above.

## 8. Check event

Recorded in `check_8_5_7_CHECK_EVENTS.tsv` (same folder):

| id | date_utc | who | how | result | where |
|---|---|---|---|---|---|
| MPL_8_079-081+9+4+100 (4:8) | 2026-11-18 | Claude Opus 5.5 at effort max, a922466087ec53798, independent check | independent re-proof | proved: v is injective for every d >= 1 and every n >= 2 (no extra condition); Frobenius maps Ker r = Im H^{n-1}(X,O_X(-d)) into Im H^{n-1}(X,O_X(-p^e d)) = 0 for p^e d large (SGA 2 XII 1.4), while F is bijective on the SS part; his cases n = 2 and H^{n-1}(X,O_X(-d)) = 0 confirmed | C:/Users/user/Documents/results_register/horizontal/sweep3/SA15/readings/check_8_5_7.md |
