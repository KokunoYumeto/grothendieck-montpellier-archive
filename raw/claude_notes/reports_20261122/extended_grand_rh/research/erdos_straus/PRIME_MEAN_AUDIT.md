# A Chebotarev average of marked Type II decompositions

Fix a positive $R\equiv3\bmod4$. Let $K/\mathbf Q$ be finite Galois containing $\mathbf Q(i)$, and let the nonempty conjugacy class $C$ restrict trivially to $\mathbf Q(i)$. Let $L$ be a multiple of $4$, $R$, and $\operatorname{rad}|\Delta_K|$. Write $\delta_C=|C|/|\operatorname{Gal}(K/\mathbf Q)|$. Select $0<2\kappa<\min(1/2,2/[K:\mathbf Q])$ and put $D=\lfloor X^\kappa\rfloor$. For each unramified $p>R$ in $C$, count ordered positive pairs $(u,v)$ satisfying

$$
 u,v\le D,\qquad (u,v)=1,\qquad(uv,L)=1,\qquad
 u\equiv1,\quad v\equiv-1\bmod R,\qquad uv\mid p+R.
$$

Let that count be $M_D(p)$. The following unconditionally holds:

$$
 \sum_{\substack{R<p\le X\\ \mathrm{Frob}_p=C}} M_D(p)\log p
 \sim \delta_C\,\kappa^2 c_{R,L}\,X\log^2 X,\qquad
 c_{R,L}=\left(\frac{\varphi(L)}{L\varphi(R)}\right)^2
               \prod_{\ell\nmid L}(1+\ell^{-2}).
$$

Equivalently $c_{R,L}=(15/(\pi^2\varphi(R)^2))\prod_{\ell\mid L}(\ell-1)^2/(\ell^2+1)$. The mean per prime in the class, with or without logarithmic prime weights, is asymptotic to $\kappa^2c_{R,L}\log^2X$. For the unweighted version one applies the same argument directly with $\pi_C$ in place of $\vartheta_C$, keeping $D$ fixed during the sum at each $X$.

## Exact multiplicity and the prior representation

Set $a=(p+R)/4$, $S=pa$. The choice of $C$ ensures $p\equiv1\bmod4$. Since $(uv,4)=1$, $uv\mid a$; since $R\mid u+v$, the integers

$$
 y=\frac{S(u+v)}{Rv},\qquad z=\frac{S(u+v)}{Ru}
$$

satisfy $1/y+1/z=R/S=4/p-1/a$. Both multiples of $p$ are distinct, and $a<p$ is coprime to $p$. Their reduced ratio $y:z=u:v$ recovers the ordered coprime witness. The swap cannot satisfy the selected residue pair since $R\ge3$. Thus each mark gives a distinct unordered Type II triple at that prime. This is a selected subfamily of the Type II parametrization in Elsholtz–Tao, Proposition 2.6 and Corollary 2.7, whose divisibility criterion is $e\mid a+b$ and $4ab\mid n+e$. Here $e=R$ and their two variables are $u,v$. Their Theorem 1.1 treats total solution counts and already uses Bombieri–Vinogradov methods. [Elsholtz and Tao, *Counting the number of solutions to the Erdős–Straus equation on unit fractions*](https://arxiv.org/abs/1107.1010)

## Distribution of the marked moduli

For one eligible pair set $q=uv$. The prime congruence is $p\equiv-R\bmod q$ with $(q,R\Delta_K)=1$. Among all pairs, any modulus is repeated at most $\tau(q)$ times. Choose $2\kappa<\theta<\min(1/2,2/[K:\mathbf Q])$. The Murty–Murty theorem for Chebotarev sets gives, for any $A>0$,

$$
 \sum_{\substack{q\le X^\theta\\(q,\Delta_K)=1}}
   \max_{(b,q)=1}\max_{y\le X}
   \left|\pi_C(y;q,b)-\frac{\pi_C(y)}{\varphi(q)}\right|
 \ll_{K,A,\theta}\frac{X}{\log^A X}.
$$

Partial summation gives the same form, with any fixed log saving, for the log-weighted errors $E_q$ at $X$. Their elementary majorant is
$|E_q|\ll (X/q+1)\log(2X)+X/\varphi(q)$ for the eligible $q$. Consequently $\sum_{q\le X^{2\kappa}}\tau(q)^2|E_q|\ll X\log^8(2X)$: apply $q/\varphi(q)\le\tau(q)$ and $\tau^j\le d_{2^j}$, $j=2,3$, prime-power by prime-power. Cauchy–Schwarz with the unweighted error sum makes $\sum\tau(q)|E_q|\ll_A X/\log^A X$ after choosing a larger saving. The deletion of $p\le R$ costs at most a constant depending on $R$, as $uv\mid p+R$. Thus the main term is $\vartheta_C(X)S(D)$, with
$$ S(D)=\sum_{u,v}\frac1{\varphi(uv)}, $$
where the sum imposes only the witness size, congruence, unit and coprimality restrictions. Chebotarev gives $\vartheta_C(X)\sim\delta_C X$. The unweighted proof uses the same error argument centered on $\pi_C(X)$. [Murty and Vatwani, Theorem 1, pp. 3–4, restating the Murty–Murty theorem](https://mast.queensu.ca/~murty/Remark.pdf)

## Exact coefficient of the double logarithm

On pairs coprime to $L$ write $1_{(u,v)=1}/\varphi(uv)$ as the two-variable Dirichlet convolution of $1/(uv)$ with $h$. The Euler factors of the Dirichlet series for $h$, with $x=\ell^{-1-s}$, $y=\ell^{-1-t}$ at $\ell\nmid L$, are
$$
 (1-x)(1-y)\!\left(1+\frac{\ell}{\ell-1}
              \left(\frac{x}{1-x}+\frac{y}{1-y}\right)\right)
   =1+\frac{x+y}{\ell-1}-\frac{\ell+1}{\ell-1}xy .
$$
At $\ell\mid L$ take the factor $1$. The series of $|h(r,s)|(rs)^{1/4}$ converges. For any unit $b\bmod R$ the harmonic sum through $Y$ on $a\equiv b\bmod R$, $(a,L)=1$ is $\lambda\log Y+O_L(1)$ uniformly for $Y\ge1$, with $\lambda=\varphi(L)/(L\varphi(R))$. Indeed there are $\varphi(L)/\varphi(R)$ admissible residues modulo $L$. In the convolution apply this to the two residue classes $r^{-1}$ and $-s^{-1}$, cut off at $D/r,D/s$. The finite logarithmic moments and power tail of $h$ give
$$
 S(D)=\lambda^2\log^2D\sum_{r,s}h(r,s)+O_L(\log(2D))
     =\lambda^2\log^2D\prod_{\ell\nmid L}(1+\ell^{-2})+O_L(\log(2D)).
$$
For a single specified ordered pair of unit residues modulo $L$, take $\lambda=1/L$. This gives the original single-lift coefficient. Summing over all lifts gives precisely $c_{R,L}$.

The constant is independent of $C$ once the same $R,L,\kappa$ are used. The estimate concerns a fixed field, a fixed shift, and explicit marks with a growing size cutoff. It neither counts every shell solution nor asserts a lower bound at every prime.

## Agreement between sectors to every logarithmic order

For every fixed $A>0$ the ratio of the weighted marked count to $\vartheta_C(X)$ is $S(D)+O_{A,K,L,\kappa}((\log X)^{-A})$, since $\vartheta_C(X)\asymp_C X$. The unweighted ratio to $\pi_C(X)$ obeys the same estimate after choosing one additional logarithm in the error budget. Thus any two fixed compatible classes agree at this precision in either mean.

The common $S(D)$ admits a full quadratic polynomial in $z=\log D$. Define
$$
 \gamma(b)=\lim_{Y\to\infty}
   \left(\sum_{\substack{a\le Y\\(a,L)=1\\a\equiv b\bmod R}}\frac1a-\lambda\log Y\right).
$$
Periodic summation gives remainder $O_L(Y^{-1})$ after the constant. With $h(r,s)$ as above set
$$
 P(z)=\sum_{r,s}h(r,s)
 \bigl(\lambda z-\lambda\log r+\gamma(r^{-1})\bigr)
 \bigl(\lambda z-\lambda\log s+\gamma(-s^{-1})\bigr).
$$
Here inverses in $\gamma$ are taken modulo $R$. This is an absolutely converging polynomial coefficient formula. In fact $S(D)=P(\log D)+O_L(D^{-1/4})$. For $r,s\le D$ the error from either harmonic factor is $O_L(r/D+s/D)$ times $O_L(1+\log D)$; use $t\le t^{3/8}$ on $0\le t\le1$. For omitted $r>D$ or $s>D$, use $1_{r>D\text{ or }s>D}\le D^{-3/8}(r^{3/8}+s^{3/8})$. The Euler product gives finite absolute moments with $(rs)^\eta$ for every $\eta<1/2$, hence enough slack for the logarithms (for example $\eta=7/16$). This proves the claimed error. In particular all three coefficients, not only the leading density, are independent of the chosen class.

For any fixed positive integer $j$ with $2j\kappa<\min(1/2,2/[K:\mathbf Q])$, the same comparison between sectors holds for the normalized $j$th raw moment of $M_D$. Expand $M_D(p)^j$ in ordered tuples of marks and put $q=\operatorname{lcm}(u_1v_1,\ldots,u_jv_j)$. All prime restrictions reduce to $p\equiv-R\bmod q$. A modulus $q\le D^{2j}$ can occur at most $\tau(q)^{2j}$ times because each of the $2j$ entries divides $q$. The same Cauchy–Schwarz step works using fixed higher divisor moments and an arbitrarily large logarithmic saving. The common main term for this moment is the tuple sum of $1/\varphi(q)$; its asymptotic constant has not been computed here. This extension concerns fixed moments in the stated range.
