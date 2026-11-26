# A one-sided test for the cubic splitting race

**Scope.** Fix a positive multiple $m$ of 3. Put $B=\mathbf Q(\zeta_m)$, $E=\mathbf Q(\omega,\sqrt[3]{269})$, and let $\rho$ be the standard two-dimensional representation of $\operatorname{Gal}(E/\mathbf Q)=S_3$. For primes $p\nmid 3\cdot269m$, put $a(p)=\#\{t\in\mathbf F_p:t^3=269\}-1$. Write $R_m(x)=\sum_{p\le x,\ p\equiv1\pmod m}a(p)\log p$, always omitting the excluded primes. Such primes satisfy $p\equiv1\pmod3$, and $a(p)$ is 2 for a cube and −1 otherwise.

**Conclusion.** The following are equivalent.

1. Every nontrivial zero of every primitive Artin function $L(s,\rho\otimes\chi)$, for finite characters of $\operatorname{Gal}(B/\mathbf Q)$, has real part $1/2$.
2. For every $\epsilon>0$ there is a constant $C_{m,\epsilon}$ such that $R_m(k^2)\ge -C_{m,\epsilon}k^{1+\epsilon}$ for every integer $k\ge 2$.

This is a fixed-modulus assertion. No rate uniform in the modulus has been established.

## Why the Artin factors have positive multiplicities

The non-Galois field $F=\mathbf Q(\sqrt[3]{269})$ has degree three by Eisenstein. It cannot be contained in an abelian extension. Thus $X^3-269$ stays irreducible over $B$ because one root would give $F\subset B$ as $B$ contains $\omega$. The extension $BE/B$ is cyclic of order three. The permutation representation on its three embeddings over $B$ is the restriction of $1+\rho$. Artin induction of the restricted representation back to $\mathbf Q$ tensors it with the regular representation of $\operatorname{Gal}(B/\mathbf Q)$. Consequently the exact identity, including the ramified local factors, is

$$
 J(s)=\frac{\zeta_{BE}(s)}{\zeta_B(s)}
     =\prod_{\chi\in\widehat{\operatorname{Gal}(B/\mathbf Q)}} L(s,\rho\otimes\chi).
$$

The factors here use the primitive Artin local convention, even for a Dirichlet character presented at an imprimitive modulus. Each is obtained by Hecke induction of a nontrivial finite-order character of $\mathbf Q(\omega)$. Indeed the original order-three character stays nontrivial on $\operatorname{Gal}(BE/B)$, whereas every twisting character is trivial there. Hecke's theorem gives entireness, and there are no poles cancelling zeros in this product. Its zero set is invariant under $s\mapsto1-\overline s$ after taking the family together. The positive, finite value $J(1)$ also follows directly by dividing the two Dedekind residues.

Let $\Psi_J(x)$ sum the coefficients through $x$ of $-J'/J$. Frobenius gives $a(p)=\operatorname{tr}\rho(\operatorname{Frob}_p)$. Character orthogonality now gives

$$
 \Psi_J(x)=\varphi(m)R_m(x)+O_m(\sqrt x\log^2(2x)).
$$

The remaining prime powers $p^j\le x, j\ge2$, contribute at most $2\varphi(m)\sum_{j\ge2}\sum_{p\le x^{1/j}}\log p$. The finitely many excluded primes contribute $O_m(\log x)$. These bounds use finite image, including on inertia invariants.

## Why a lower bound detects complex and real zeros

The ordinary explicit formula for a fixed primitive finite-order Hecke $L$-function gives $\Psi_J(x)=O_{m,\delta}(x^{1/2+\delta})$ for every $\delta>0$ under item 1. One can also shift truncated Perron at $\lfloor x\rfloor+1/2$ to $\Re s=1/2+\delta/2$ with height $T=x^2$. The Hadamard logarithmic derivative bound on this line and to its right through $\Re s=2$ is $O_{m,\delta}(\log(|\Im s|+3))$, by comparison at $2+i\Im s$ and the unit-window zero count for a fixed Hecke function. Coefficients have magnitude at most $2\varphi(m)\Lambda(n)$. The shift gives $O_{m,\delta}(x^{1/2+\delta/2}\log^2 x)$, sufficient for item 2 after choosing $\delta$.

Conversely, there are at most $2k+1$ possible integer summands between $k^2$ and $(k+1)^2$, each of magnitude at most $2\log((k+1)^2)$. Thus the bound at squares implies, for any fixed $1/2<\theta<1$, that $\Psi_J(x)\ge-Cx^\theta$ for all $x\ge1$, after using a smaller exponent in item 2 and increasing the constant. For $g(x)=\Psi_J(x)+Cx^\theta\ge0$, its Mellin integral on $\Re s>1$ is

$$
 M(s)=\int_1^\infty g(x)x^{-s-1}\,dx
     =-\frac{J'(s)}{sJ(s)}+\frac C{s-\theta}.
$$

If the real abscissa of convergence $\sigma_c$ were greater than $\theta$, Landau's theorem for nonnegative Mellin integrands would force a singularity at $\sigma_c$. For completeness, if $M$ extended analytically around $\sigma_c$, expand at $\sigma_c+\eta$ for sufficiently small positive $\eta$. The disk of analyticity reaches past $\sigma_c$. Taylor expansion to the left has nonnegative integral terms $g(x)x^{-(\sigma_c+\eta)-1}(h\log x)^n/n!$; monotone convergence would make the integral finite to the left of its abscissa. This proves Landau's assertion here.

In the half-plane to the right of $\theta$ the only possible real singularity of the displayed meromorphic expression is a zero of $J$. At a real zero $\sigma_c$ of order $d>0$ the residue would be $-d/\sigma_c<0$. Thus $M(s)\to-\infty$ along the real axis from the right, contradicting the nonnegative integral. It follows that $\sigma_c\le\theta$, allowing convergence everywhere. The integral supplies a holomorphic function on $\Re s>\theta$. The displayed identity then excludes every zero there, real or nonreal. Let $\theta\downarrow1/2$, and apply the functional equations. No maximal real part of a zero is assumed. The sign of the one-sided test matters.

## A weaker-looking sufficient first moment

Write $v^-=\max(0,-v)$ and $v^+=\max(0,v)$. The two conditions above are also equivalent to

$$
\text{for every }\epsilon>0,\qquad
\sum_{2\le k\le K}R_m(k^2)^-\ll_{m,\epsilon}K^{2+\epsilon}.
$$

The pointwise bound gives this by summation. Conversely set $\Psi=\Psi_J$. The prime-power estimate and the bound between consecutive squares give
$\Psi(x)^-\le\varphi(m)R_m(k^2)^-+O_m(k\log^2(2k))$ throughout $k^2\le x<(k+1)^2$. For $\sigma>1/2$, integration of $x^{-\sigma-1}$ over the interval costs $O_\sigma(k^{-2\sigma-1})$. The displayed first moment and partial summation make the weighted sum of deficits finite, by taking $\epsilon<2\sigma-1$. The error series converges as well. The Mellin transform $M_-(s)$ of $\Psi^-$ is therefore holomorphic on $\Re s>1/2$. The Mellin transform of the nonnegative function $\Psi^+$ agrees there by meromorphic continuation from $\Re s>1$ with $-J'(s)/(sJ(s))+M_-(s)$. At every possible real convergence boundary greater than $1/2$, the same negative-residue contradiction applies. Landau then gives holomorphy throughout $\Re s>1/2$ and hence zero-freeness of $J$ there.

A first-moment bound for the negative part is sufficient even when there is no stated control at particular squares. Finite data alone do not establish this asymptotic estimate. The argument proves no uniformity in the number of exceptional samples, the modulus or the twist conductor.

## A signed first moment with the sharp normalization

The sharpest averaged criterion checked here permits cancellation in the sample:

$$
\liminf_{K\to\infty}\frac{1}{K^2}\sum_{k\le K}R_m(k^2)>-\infty
\quad\Longleftrightarrow\quad \mathrm{RH}\ \text{for }J.
$$

Let $b(n)$ be the coefficients of $-J'/J$. Put $W(x)=\sum_{n\le x}b(n)(1-\sqrt{n/x})$ and $U_m(x)=\sum_{p\le x,\,p\equiv1\bmod m}a(p)\log p(1-\sqrt{p/x})$. At $x=K^2$, the integer count $K-\lceil\sqrt p\rceil+1$ differs from $K-\sqrt p$ by at most one. Chebyshev's elementary $\sum_{p\le y}\log p\ll y$ gives $K^{-1}\sum_{k\le K}R_m(k^2)=U_m(K^2)+O(K)$. Also $W(x)=\varphi(m)U_m(x)+O_m(\sqrt x)$: the squares cost $O_m(\sqrt x)$, powers of exponent at least three cost $O_m(x^{1/3}\log(2x))$, and excluded primes cost $O_m(\log x)$. Between consecutive squares, every positive-part weight $(1-\sqrt{n/x})_+$ changes by $O(1/K)$ and $\sum_{n\le(K+1)^2}|b(n)|=O_m(K^2)$. Consequently the liminf condition implies $W(x)\ge-C_m\sqrt x$ for all $x\ge1$.

Initially on $\Re s>1$ the Mellin transform of $W$ is $-J'(s)/[s(2s+1)J(s)]$. Adding $C_m\sqrt x$ to $W$ makes the integrand nonnegative and adds $C_m/(s-1/2)$ to the transform. A real zero of order $d$ at $\sigma>1/2$ has residue $-d/[\sigma(2\sigma+1)]<0$, so the preceding Landau argument yields the reverse direction. Under RH, shift the inverse Mellin line to $\Re s=1/4$. Here $J'/J$ is $O_m(\log(3+|t|))$ by the Hadamard formula and the horizontal distance $1/4$ from its nontrivial zeros. Choose heights whose distance from every nearby ordinate is $\gg_m 1/\log T$, using the unit-window zero count. Along the two horizontal segments the logarithmic derivative is $O_m(\log^2 T)$ and the kernel decays quadratically. No trivial or kernel pole is crossed. With multiplicities counted this gives

$$
 W(x)=-\sum_{\rho\in Z(J)}
     \frac{x^\rho}{\rho(2\rho+1)}+O_m(x^{1/4}),
\qquad
 \sum_{\rho\in Z(J)}\frac1{|\rho(2\rho+1)|}<\infty .
$$

In particular $W(x)=O_m(\sqrt x)$ with no logarithm, proving the forward direction and the asserted normalization.

### The mean of the continuous prime weights

The limit under RH of the logarithmic average of $U_m(x)/\sqrt x$ is

$$
 -\frac{\operatorname{ord}_{1/2}J+\tfrac12|(\mathbf Z/m\mathbf Z)^{\times}[2]|}{\varphi(m)}.
$$

Indeed, Chebotarev gives the mean of the prime-square coefficient $b(p^2)/\log p$ as the group average of $\operatorname{tr}V(g^2)$, where $V=\rho\otimes\mathrm{reg}_{\operatorname{Gal}(B/\mathbf Q)}$. The coefficient vanishes unless the cyclotomic component $a$ has $a^2=1$. For half of these $a$ the component in $\operatorname{Gal}(\mathbf Q(\omega)/\mathbf Q)$ is conjugation, by pairing $a$ with $-a$. Above such $a$ every cubic permutation is a transposition and its square has trace 2. Above each of the other $a$ the three even cubic permutations are equidistributed; their squares have traces $2,-1,-1$. Including the regular-character factor and averaging gives $c=|(\mathbf Z/m\mathbf Z)^\times[2]|$. By partial summation the prime squares contribute $(c/2+o_m(1))\sqrt x$ to $W(x)$; higher powers are $o_m(\sqrt x)$. In the absolutely convergent zero sum, logarithmic averaging kills every nonzero frequency, and the term of a central zero has denominator one. This proves the formula without a linear independence hypothesis. More generally the nonzero logarithmic Fourier coefficient at ordinate $t$ is $-\operatorname{ord}_{1/2+it}J/[\varphi(m)(1/2+it)(2+2it)]$. These exact mean and frequency statements concern the continuous weight $1-\sqrt{p/x}$. The $O(K)$ rounding comparison alone cannot transfer the mean to the raw discrete average at its natural normalization.

Prime-square and central-zero biases are classical parts of prime-race theory. Related general mean formulas and prior work are discussed by [Lucile Devin, *Chebyshev's bias for analytic L-functions*](https://www-lmpa.univ-littoral.fr/~ldevin/Chebyshev_bias.pdf).

## The Gaussian sign isolates a second test

At $m=12$, the characters are $1,\chi_{-3},\chi_{-4},\chi_{12}$. Since $\rho\otimes\chi_{-3}\simeq\rho$,

$$
 J(s)=L(s,\rho)^2 L(s,\rho\otimes\chi_{-4})^2.
$$

Write $T_j(x)=\sum_{p\le x,\ p\equiv j\bmod12}a(p)\log p$. For $p\equiv2\bmod3$ the cube map on $\mathbf F_p^\times$ is bijective and $a(p)=0$. Thus $T_1+T_7$ tests the untwisted $L$-function and $T_1-T_7$ tests the Gaussian twist alone. More precisely the same one-sided bound at squares for $T_1-T_7$ is equivalent to RH for $L(s,\rho\otimes\chi_{-4})$, with no prior assumption about the untwisted function. For a complex character $\chi$, weighting $a(p)\log p$ by $2\Re\chi(p)$ similarly tests $L(s,\rho\otimes\chi)L(s,\rho\otimes\bar\chi)$. Vanishing away from the line is conjugation-invariant between these factors.

## Sources and scope of the search

For Artin factorization of a non-Galois cubic field and its standard character, see §3.1 of [Shankar, Södergren and Templier, *Central values of zeta functions of non-Galois cubic fields*](https://link.springer.com/article/10.1007/s00222-025-01373-6). An alternative forward implication, given GRH for $\zeta_B$, follows by applying the fixed-field prime ideal theorem to $BE$ and $B$ separately. [Grenié and Molteni, *Explicit versions of the prime ideal theorem for Dedekind zeta functions under GRH*](https://arxiv.org/abs/1312.4463)

The local ALP_MACHINE AM-H04 and ALP_CONNES workshop references already use a signed Landau argument for the untwisted Kummer character in a smoothed window. A search of the two downloaded CP29 and CP22 archives and the earlier split-zero and overnight records found the smoothed-window references and other twists of the 269 character. It did not identify the integer-square, fixed-progression test or its $T_1-T_7$ isolation. This search establishes neither priority nor absence elsewhere. No bound on the cubic splitting race has been proved in this check.
