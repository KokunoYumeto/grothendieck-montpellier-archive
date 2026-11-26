# Sampling the cubic prime race at integer squares

Let $m$ be a fixed multiple of three. Use $R_m$, $J$, $\varphi(m)$, $\Psi_J$, $W$ and $U_m$ as in [the proof check](PROOF_CHECK.md). Thus $R_m$ is the signed sum with log weights on primes in the progression $1\bmod m$, and $U_m$ uses the additional weight $1-\sqrt{p/x}$. Under RH for $J$ alone,

$$
\frac1K\sum_{k\le K}R_m(k^2)-U_m(K^2)
   =O_m\!\left(K^{2/3}\log^2(2K)\right)=o_m(K).
$$

In particular the discrete statistic $D_m(K)=K^{-2}\sum_{k\le K}R_m(k^2)$ has the same limiting logarithmic mean as $U_m(K^2)/K$. The mean is

$$
\lim_{X\to\infty}\frac1{\log X}\sum_{K\le X}\frac{D_m(K)}{K}
=-\frac{\operatorname{ord}_{1/2}J+\tfrac12|(\mathbf Z/m\mathbf Z)^\times[2]|}{\varphi(m)}.
$$

A qualitative route from the literature uses a slightly different analytic input. Amita Malik and Neha Prabhu, Theorem 1.1 and its Corollary 4, jointly equidistribute $\{\sqrt p\}$ with Frobenius conjugacy classes under GRH for the full compositum's Dedekind zeta function. Integration over the fractional-part threshold and partial summation for the factor $\log p$ give cancellation in the signed sum, because the class weight has group mean zero. Together with cyclotomic RH, RH for $J$ gives the needed Dedekind hypothesis. The argument below uses only the zeros of the given product $J$. [Malik and Prabhu, journal version, Theorem 1.1 and Corollary 4](https://sites.math.rutgers.edu/~am2365/JointDistribution.pdf)

## Sampling the explicit formula

Write $-J'(s)/J(s)=\sum b(n)n^{-s}$ for $\Re s>1$; $|b(n)|\le 2\varphi(m)\Lambda(n)$. Put $T\asymp K^{4/3}$ and choose it at distance $\gg_m1/\log T$ from all nearby zero ordinates at both $T$ and $-T$. The standard unit-window zero count $O_m(\log(2+T))$ for fixed primitive Hecke functions ensures such heights. Uniformly for integers $2\le y\le K^2$ one has

$$
\Psi_J(y)=-\sum_{|\gamma|\le T}\frac{y^{1/2+i\gamma}}{1/2+i\gamma}
 +O_m\!\left((1+y/T)\log^2(2KT)\right).
$$

Here each ordinate occurs with multiplicity. To see the truncation directly, truncate Perron on $c=1+1/\log(2y)$. The endpoint coefficient is $O_m(\log(2y))$. For $n\ne y$ with $y/2<n<2y$, bound the truncated-kernel error by $O(y/(T|n-y|))$ times $O_m(\log(2y))$. Away from this interval the absolute Dirichlet series is $O_m((c-1)^{-1})$ by Chebyshev. Shift to $\Re s=-1/4$, crossing the nontrivial zeros and the kernel pole at $0$. Any extra term from a trivial zero at $0$ is $O_m(1+\log y)$. On the two horizontal segments $J'/J=O_m(\log^2(2T))$ by the good height and the local logarithmic derivative formula. The remaining vertical segment contributes $O_m(y^{-1/4}\log^2(2T))$ by the functional equation and Stirling. These errors also allow inclusion of $k=1$ at the end. This derivation assumes no cancellation among large zero ordinates.

Set $H=K^{2/3}$ and $\rho=1/2+i\gamma$. Comparing the sum of $\Psi_J(k^2)/K^2$ with $W(K^2)/K$ amounts to comparing

$$
 A_K(\gamma)=K^{-2}\sum_{k\le K}k^{1+2i\gamma}
 \quad\text{and}\quad B_K(\gamma)=\frac{K^{2i\gamma}}{2+2i\gamma}
$$

with weights $1/\rho$. For $|\gamma|\le H$, first-order comparison of the sum with the integral gives $|A_K-B_K|\ll(1+|\gamma|)/K$. The contribution summed with multiplicity is $O_m(H\log(2H)/K)$.

For $|\gamma|>H$ the second derivative of $\gamma\log t/\pi$ on $L<t\le2L$ has size $\asymp|\gamma|/L^2$. The van der Corput second-derivative bound therefore gives $\left|\sum_{L<k\le 2L}k^{2i\gamma}\right|\ll\sqrt{|\gamma|}+L/\sqrt{|\gamma|}$, also for partial dyadic intervals. Partial summation inserts the weight $k$; summing dyadically gives $|A_K(\gamma)|\ll\sqrt{|\gamma|}/K+1/\sqrt{|\gamma|}$. The unit-window zero count then yields

$$
\sum_{H<|\gamma|\le T}\frac{|A_K(\gamma)|}{|\rho|}
 \ll_m \frac{\sqrt T\log(2T)}{K}+\frac{\log(2H)}{\sqrt H}.
$$

The continuous tail $\sum_{|\gamma|>H}|B_K(\gamma)/\rho|$ is $O_m(\log(2H)/H)$. The smoothed explicit formula in the main proof has residual error $O_m((K^2)^{1/4}/K)=O_m(K^{-1/2})$. The normalized truncation errors for the discrete sum total $O_m((K^{-1}+K/T)\log^2(2KT))$. With the stated $H,T$ all errors are $O_m(K^{-1/3}\log^2(2K))$ or smaller. Hence

$$
 \frac1{K^2}\sum_{k\le K}\Psi_J(k^2)-\frac{W(K^2)}K
=O_m(K^{-1/3}\log^2(2K)).
$$

To pass to primes, in the difference between the two sides of the last formula each coefficient $b(n)$ is weighted by $(1+\sqrt n-\lceil\sqrt n\rceil)/K^2$. The omitted prime powers contribute $O_m(1/K)$ since their total absolute coefficient mass through $K^2$ is $O_m(K)$. The finitely many ramified primes also satisfy this bound. Orthogonality supplies the factor $\varphi(m)$ at the remaining primes. This proves the assertion.

## Discrete mean and the limits of the prime number theorem

The continuous smoothed spectrum is absolutely convergent after the normalization by $\sqrt x$. For every fixed nonzero real $t$, $\sum_{k\le X}k^{-1+it}=O_t(1)$ by comparison to the integral, whereas $\sum_{k\le X}1/k\sim\log X$. Termwise logarithmic averaging at $x=K^2$ therefore yields the displayed mean, including the prime-square correction in the main proof. It also preserves each nonzero frequency, with ordinate $t$ in $\log x$ read at frequency $2t$ in $\log K$.

Fixed-field prime counts alone prescribe coarse marginal distribution. They provide no abstract estimate for the signed correlation with $\{\sqrt n\}$. For example $b_n=\{\sqrt n\}-1/2$ has partial sums $O(\sqrt x)$: on each interval $k^2\le n<(k+1)^2$ the normalized fractional parts differ by $O(1/k)$ from an equally spaced grid. Yet $x^{-1}\sum_{n\le x}b_n\{\sqrt n\}\to1/12$ by the same grids. This synthetic sequence illustrates why exchanging the averaging order alone cannot prove the arithmetic cancellation. It does not demonstrate that the actual Frobenius problem requires RH. The source-qualified result here uses the Hecke explicit formula with the same RH assumption as the continuous mean.
