"""NN-C017 draft: append this definition to the working generator after checkpoint 01."""

def append_c017(add, E, SGATRACE, SGAFINITE):
    add('NN-C017','NEG_NIGHT-01',
        'Sparse equations over every fixed finite field by prime-adic total-order truncation',
r'''Fix a finite field $K=\mathbb F_{p^r}$ and constants $k,a,b$. Given $n$ variables over $K$ and at most $n(\log n)^a$ polynomial equations of degree at most $k$, with at most $(\log n)^b$ listed monomials per equation, their exact number of common zeros is computable deterministically in
\[
 \operatorname{poly}(L+n)\,
 2^{O_{K,k,a,b}(n(\log\log n)^2/\sqrt{\log n})}
\]
bit operations and polynomial space. Here $L$ is the explicit input length. Witness search and exact uniform sampling from a nonempty zero set have the same bound, with expected time for sampling. This extends NN-C002 to odd characteristic at the weaker Proposition 3.4 exponent; it does not assert the sharper Appendix D bound there.''',
        [dict(E,locator='Proposition 3.4; Lemmas 4.7--4.8; Lemmas 5.1--5.2; Proposition 5.3 and Appendix B; complete proofs of Lemmas 6.1--6.2'),
         {'source':'NN-C003','locator':'explicit common-denominator and Hermite-minor bit-cost method'},
         {'source':'NN-C002','locator':'prefix self-reduction and exact rejection sampling'}],
r'''We first count common zeros of $m\leq CN$ sparse bounded-degree polynomials in $N$ Boolean variables with coefficients in the fixed prime field $\mathbb F_p$. Choose integer representatives of their coefficients and let $L_i(x)$ be the resulting integer polynomials. On Boolean inputs they reduce to the prescribed polynomials modulo $p$. Set $Y_i=L_i^{p-1}$. Fermat's elementary identity gives $Y_i(x)\equiv0$ or $1\pmod p$, with the first case exactly when $L_i(x)\equiv0\pmod p$. For completeness, for $u\not\equiv0\pmod p$, multiplication by $u$ permutes the $p-1$ nonzero residues; comparing their products and cancelling $(p-1)!$ gives $u^{p-1}=1$ in $\mathbb F_p$.

Set $\ell=N+1$ and use exactly E Lemma 5.1's integer polynomial
\[
 p_\ell(Y)=(1-Y)^\ell\sum_{j=0}^{\ell-1}\binom{\ell+j-1}{j}Y^j
           =\sum_{j=0}^{\ell-1}e_j(Y)h(Y)^j,
 \qquad h(Y)=Y(Y-1),\quad\deg e_j\leq1.
\]
The proof of that lemma establishes the polynomial congruences $p_\ell\equiv1\pmod{Y^\ell}$ and $p_\ell\equiv0\pmod{(1-Y)^\ell}$, independently of characteristic. Therefore $p_\ell(Y_i(x))$ is the zero indicator modulo $p^\ell$, and $p\mid h(Y_i(x))$. In $\mathcal A=\mathbb Q[V]/(V^\ell)$ use
\[
 B_i(x,V)=\sum_{j<\ell}e_j(Y_i(x))h(Y_i(x))^jV^j.
\]
After multiplying all factors, sum the retained $V$ coefficients. Each discarded term has total $h$-order at least $\ell$ and is divisible by $p^\ell$ at every Boolean input. Thus the sum-product recovers the number of simultaneous zeros modulo $p^\ell$. Since $p^\ell>2^N$, its least nonnegative residue is the exact count. This readout is performed after multiplication, not as a ring homomorphism.

If the original degree is at most $d$, then $\deg Y_i\leq d(p-1)$. Even with independent input copies for every factor, every retained coefficient has degree at most
\[
 d(p-1)\bigl(m+2(\ell-1)\bigr)=O_{p,d,C}(N).
\]
Scopes remain polylogarithmic and total incidence is $N(\log N)^{O(1)}$. Add neutral unary factors for unused declared bits. If total incidence is $M$, branch on bits appearing in more than
$\max(1,\lceil M/N\rceil)\lceil\sqrt{\log_2N}\rceil$ scopes. At most $N/\sqrt{\log_2N}$ bits are branched; every branch retains $\Theta(N)$ declared bits and has polylogarithmic maximum incidence. E Lemmas 4.7--4.8 and Proposition 3.4 now apply. Factor evaluation computes the sparse $L_i$, its fixed power $p-1$, and successively the $h$ powers in the truncated algebra; it uses polynomially many rational operations and never enumerates a factor's entire scope.

The bit bound is explicit. With E's row denominator $d_{\rm den}=(R-1)!Q!$, a substituted $Y_i$ has denominator dividing $\Delta=d_{\rm den}^{d(p-1)}$. Each $B_i$ has denominator dividing $\Delta^{2\ell-1}$ and their product has denominator dividing $\Omega=\Delta^{m(2\ell-1)}$. Coefficient bits are polynomial by E Lemma 5.1 and Appendix B; the additional fixed power $p-1$ changes only constants. Clearing $\Omega$ bounds every Taylor datum by a polynomial-bit integer: a product has polynomially many polynomial-bit factors and summing the enumerated terms adds only the logarithm of their number. The integer Hermite matrix and its fraction-free minor bound are exactly as in NN-C003. Final integer reduction is modulo $p^\ell$, which has $O_p(N)$ bits. The time is the displayed weaker exponent and sequential evaluation gives polynomial space.

Next extend the equation count from $CN$ to $N(\log N)^{O(1)}$. E Lemma 6.1's graph, its shifts, its real-valued Walsh mixing estimate, and its shortening do not depend on the coefficient field. Keep its parameters
\[
 B=\max(1,\lceil m/N\rceil),\quad \mu=\lfloor\log_2m\rfloor+1,
 \quad P=20000B^2\mu^2,\quad D_0=320000B^2\mu^3.
\]
Use the same $d_G,q_G,c_G,\delta$ and replace only the binary local matrix by a uniformly random $c_G\times d_G$ matrix over $\mathbb F_p$. A fixed nonzero vector belongs to its kernel with probability $p^{-c_G}$. If $h=\lceil\delta d_G\rceil-1\geq1$, the number of nonzero vectors of weight at most $h$ is at most
\[
 \sum_{j=1}^h\binom{d_G}{j}(p-1)^j
 \leq(h+1)(p d_G)^h
 \leq(p d_G)^{2h}
 <p^{d_G/(25B)}.
\]
Indeed $d_G\leq m<2^\mu$, so $\log_p(p d_G)\leq1+\mu\leq2\mu$, while $h<d_G/(100B\mu)$. Since $c_G\geq d_G/(8B)$, the union bound is below one. If $h=0$ there is nothing to exclude. Exhaustive enumeration of local matrices and the low-weight vectors costs $\exp(\operatorname{poly}(B,\log(m+2)))$ for fixed $p$. The rest of Lemma 6.1 uses only supports and graph mixing, so it produces at most $3N$ rows, each of support at most $D_0$, whose nonzero kernel vectors have support at least $m/P$.

For the remaining greedy stage, use lists in $([m]\times\mathbb F_p)^P$. A list hits the support of a false survivor with probability at least $1-e^{-1}>1/2$. Conditional on a hit, one uniform coefficient makes the tested sum uniform in $\mathbb F_p$, even with repeated indices. Its rejection probability is consequently at least $(1-e^{-1})(1-1/p)>1/4$. A candidate minimizing the exact count leaves at most $3/4$ of the false survivors, exactly as in E Lemma 6.2. There are at most $2^N$ Boolean assignments, so $3N$ stages remove all false survivors. Every candidate has at most $6N$ equations and polylogarithmic monomial sparsity. The number of core calls is at most $3N(pm)^P=\exp((\log N)^{O(1)})$, absorbed by the claimed running time. All enumeration is sequential and uses polynomial space. This compression preserves the common zero set on the Boolean cube.

Finally encode the original $\mathbb F_{p^r}$ variables. Fix an $\mathbb F_p$ basis; each original variable has $r$ coordinates and each equation gives $r$ coordinate equations. A degree-$k$ monomial expands into at most a fixed multiple of $r^k$ coordinate monomials. Encode each prime-field coordinate by $t=\lceil\log_2p\rceil$ bits, interpreted as the integer $\sum_{j<t}2^jx_j$. Add one polynomial equation per coordinate saying that this bit code is below $p$: explicitly, take one minus the sum of the bit-pattern indicator monomials for $0,\ldots,p-1$. On bits it is zero exactly for valid codes. It has constant degree and at most $2^t$ expanded pattern terms times a fixed constant. There are $N=rtn=\Theta_K(n)$ bits, $rm+rn=N(\log N)^{O(1)}$ equations, fixed degree and polylogarithmic monomial sparsity. Valid codes are in bijection with the original field assignments. The Boolean prime-field counter therefore gives exactly the desired number. Prefix fixing adds only $O(N)$ linear equations, so NN-C002's search and exact sampling proofs apply unchanged.''',
        'Complete new deduction proved; complete self proof-check passed; independent review pending.',
r'''This removes an actual algorithmic restriction: sparse systems over fixed odd-characteristic fields now have a deterministic mildly subexponential exact counter with the original variable parameter, even when their scopes are polylogarithmic. The modulus and field extension degree must remain fixed; their powers and coordinate expansion enter the constants and cannot be hidden if they grow. The stronger characteristic-two Appendix D exponent has not been transferred. Neither polynomial-time counting nor a uniform identity test follows.''',
r'''After adjoining $x_i^{|K|}-x_i$, the original zero set is a finite reduced split scheme over $K$ whose rank is the count. The basis expansion and valid-code equations give a bijection of rational components with a finite Boolean scheme over $\mathbb F_p$; they are an effective coordinate presentation, not an identification of unrestricted affine zero schemes. The $p$-adic order in $h(Y)$ is a divisibility filtration on integer-valued indicators. The formal nilpotent $V$ records this filtration and is not a Frobenius coordinate or a Tate twist. On the resulting finite scheme, the component-idempotent basis makes counting the trace of the identity; SGA7 II XXII Corollary 3.2 supplies its mod-$p$ coherent trace expression and SGA4 XVII 6.2.3 the finite-trace formalism. The algorithm computes this succinctly presented rank without constructing the exponential basis and supplies no new representation-theoretic positivity statement.''',
        [E,SGATRACE,SGAFINITE])
