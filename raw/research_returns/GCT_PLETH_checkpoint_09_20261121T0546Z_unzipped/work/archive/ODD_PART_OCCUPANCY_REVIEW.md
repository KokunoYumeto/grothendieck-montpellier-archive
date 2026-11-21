# A099. Odd-part occupancy and the actual canonical-map range

## Complete review

**PASS.** I read all of R049, OO.1–OO.25 and its six sections, both verification scripts, and the exact supporting passages TM.4, TM.8, TM.12, TM.14 and TM.16–TM.18 in R046. This is an independent whole-proof check of the map and its improved range. The author's finite sweeps are not rerun here.

The central conclusion is the actual isotypic surjectivity of $h_{n,a}$ for
$$
n\ge M(\nu)=\left\lfloor
\frac{|\nu|+\nu_1-\lceil(o-(\nu_1\bmod2))/3\rceil}{2}
\right\rfloor.
$$
The proof supplies the needed actual restriction map, its kernel injection, the faithful moment evaluation and the normalized canonical factorization. It does not infer a rank from matching numerical multiplicities.

## 1. The specified restriction and its kernel

The linear map $\widetilde q$ sends the first $s$ basis vectors to their counterparts and each extra basis vector to $\bar e_s$. Its sum on all $S$ basis vectors is $S\bar e_s$, so it sends $\bar e_S$ exactly to $\bar e_s$. It consequently sends $P_Se_i$ to $P_se_i$ for $i\le s$ and to zero for $i>s$. This is the orthogonal transpose of zero-padding on the mean-zero summands.

The decomposition $E_s=\mathbb Q\bar e_s\oplus W_s$ is specified by these vectors. Its exterior-algebra decomposition is natural for this very map, so the induced map on invariant exterior algebras is literally
$$
1_{\Lambda T}\otimes\Lambda(q\otimes1).
$$
The map is equivariant for the subgroup permuting the first $s$ rows, which is enough to take $S_S$-invariants to $S_s$-invariants.

The centered map is surjective: its row-power-sum generators go to the target generators with scalar one. Their generation follows either from the signed row-orbit proof of TM.8/TM.12 or from its explicit row inclusion–exclusion followed by the centering projection. Thus the uncentered map is also onto. There is consequently the actual injective map on kernels $v\mapsto1\otimes v$ used in OO.7.

The row-orbit decomposition is the symmetric or exterior power of each row type, according to its parity. Its unit factor fills the unused rows. For a fixed occupied tuple, the same $GL(T)$ module occurs at every row count at least its occupancy. Hence the difference of source and target characters is exactly the sum of the tuples that do not fit in $s$ rows. Since the specified map has already been proved onto, that difference is its actual kernel character. This proves the use of the omitted tuple modules without claiming that they are the coordinate subspaces of this particular kernel.

## 2. The alternating-weight bound

For a dominant rational weight $\alpha$, write
$A(\alpha)=\alpha_1-\alpha_2+\cdots+(-1)^{t-1}\alpha_t$.
The full paired-row decomposition of $\operatorname{Sym}(\Lambda^2T)$, independently checked in A094, has $A=0$.

In a row-orbit tuple, the singleton exterior factor is $\Lambda^{e_1}T$ with $e_1\le t$. Put $u=t-e_1$. The perfect exterior pairing gives the exact determinant-twisted duality
$$
\Lambda^{e_1}T=\det T\otimes\Lambda^uT^*.
$$
Every symmetric or exterior factor at a row degree $i\ge3$ embeds by its rational normalized projector into $(\Lambda^iT)^{\otimes e_i}$. No enlargement of a coefficient is assumed without this injection.

The determinant twist changes $A$ by $\epsilon=t\bmod2$. The dual exterior Pieri map removes a vertical $u$-strip, and each other exterior map adds a vertical $i$-strip. Each affected box changes the fixed alternating sum by $1$ or $-1$. Thus every resulting highest weight satisfies
$$
A(\gamma)\le\epsilon+u+\sum_{i\ge3}ie_i.
$$
The assertion remains valid for rational intermediate weights. Indeed dual exterior Pieri follows from
$\Lambda^uT^*=\det^{-1}T\otimes\Lambda^{t-u}T$; adding the complementary vertical strip and then subtracting the full determinant subtracts exactly one in the complementary $u$ rows. No positivity of the last intermediate coordinate is required.

The occupancy and degree identities give
$$
D+t-2k=u+\sum_{i\ge3}(i-2)e_i.
$$
Since $i\le3(i-2)$ for every $i\ge3$, the displayed bound implies
$A(\gamma)\le\epsilon+3(D+t-2k)$.

At $\gamma=\nu^{\mathsf t}$, $A(\gamma)$ is exactly the number $o$ of odd parts of $\nu$: each row contributes the alternating sum across its own boxes. Therefore
$$
k\le\left\lfloor\frac{D+t-q}{2}\right\rfloor,
\qquad q=\left\lceil\frac{o-\epsilon}{3}\right\rceil.
$$
The largest part contributes an odd part exactly when $t$ is odd. Removing that largest part also proves $0\le q\le o-\epsilon\le D-t$, so $M(\nu)\ge t$. This verifies every small and zero-improvement endpoint.

This contains R048's one-row improvements: in its equal-parity cases, $D+t$ is even and the required odd-part hypothesis gives $q\ge1$, lowering the floor by at least one.

## 3. Faithful evaluation and the exact canonical map

For $S\ge s\ge M(\nu)$, no omitted tuple in the actual uncentered kernel character contains $S_{\nu^{\mathsf t}}T$. The injection of centered kernels then proves zero kernel on that component. Surjectivity was already supplied by the row generators, so the same actual Schur map
$$
S_\nu(q):(S_\nu W_S)^{S_S}\longrightarrow(S_\nu W_s)^{S_s}
$$
is an isomorphism.

The ordinary and skew-Cauchy multiplicity maps are identical because the rational tensor Young projectors commute with tensor powers of $q$. With $S\ge\max(s,D)$, the full equality-partition triangular basis makes the ordinary moment evaluation $p_S$ an isomorphism in degree $D$. Its commutative relation with $q$ is scalar one on every generator. This proves precisely the componentwise isomorphism of $p_s$ used in OO.18.

The remaining factorization is the already checked literal map
$h_{a,n}|_\nu=p_n\Psi_nE_a$.
The Young column bound gives separate row degree at most $t$, so the highest-vector homogenization is polynomial at every $n\ge M(\nu)\ge t$. Independent-row polarization $E_a$ remains injective after normalizing the constant and mean coordinates. The split-moment substitution has diagonal coefficient
$(-1)^{d-1}(d-1)!/(n)_d$ in every generator degree $2\le d\le t$. Those denominators and coefficients are nonzero in this range, and its lower terms only use smaller-degree generators. It is the explicit triangular automorphism, with its recursive inverse.

Faithful $p_n$ therefore makes the opposite canonical map injective on the full highest multiplicity space. The scalar-one transpose identity gives the asserted surjectivity of $h_{n,a}$. Applying the same reasoning in both directions proves the isomorphism when $a,n\ge M(\nu)$. These statements are natural in the ambient vector space and extend over every characteristic-zero field through the rational maps.

## 4. The positive family and its full scalar

The wedge $dp_2\wedge\cdots\wedge dp_{r+2}$ has coefficient degree
$(r+1)(r+2)/2$ and form degree $r+1$. Euler contraction therefore has coefficient degree
$t_0=(r^2+3r+4)/2$, form degree $r$, and square-zero contraction makes it horizontal. Each $p_d$ is invariant under the row permutations, so the form is invariant.

Exterior Pieri has exactly the two displayed Schur summands in the polynomial-form domain. Contraction is nonzero on the highest vector of $S_{(t_0+1,1^{r-1})}$: the coefficient of
$x_1^{t_0+1}dx_2\wedge\cdots\wedge dx_r$ is nonzero. The other summand has no occurrence in the target. This identifies the whole kernel with $S_{(t_0,1^r)}$ by the actual contraction map, including $r=1$.

For the nonzero evaluation, set $a_0=r+2$ and use the centered consecutive coordinates in OO.24. The vector $x$ is
$\sum_{j<a_0}x_j(e_j-e_{a_0})$. On the listed $r$ arguments, all terms except $j=1$ repeat an exterior argument. The determinant is therefore exactly $x_1$ times the displayed derivative determinant.

Factoring the row constants gives $a_0!$. Factoring the column differences $x_j-x_{a_0}$ gives sign $(-1)^{a_0-1}$ times the missing Vandermonde factors. The remaining monic polynomials have successive degrees $0,\ldots,a_0-2$, hence determinant equal to the smaller Vandermonde. Finally $x_1=-(a_0-1)/2$ gives precisely
$$
(-1)^{a_0}\frac{a_0-1}{2}\,a_0!
\prod_{i<j}(x_j-x_i),
$$
with no scalar or sign omitted. The chosen arguments and coordinates remain in the centered subspace after adding zero rows, and the same value proves nonvanishing there.

Multiplication by $p_2^up_3^v$ preserves horizontality and the invariant action. Both factors are nonzero for $a\ge3$; the polynomial-form module is free over an integral domain, so their product with the form is nonzero. Evaluation on the auxiliary centered columns is the actual highest-vector map: a raising operation into the first column inserts the Euler vector, while a raising operation between later columns repeats an alternating argument. Both give zero. Homogenization then supplies the required target vector at every stated inner degree.

For the hook tail, $o=r+\epsilon$, so its threshold is exactly
$t+\lfloor(r-\lceil r/3\rceil)/2\rfloor$. Substituting $r=6s+2$ gives $t=18s^2+21s+7+2u+3v$ and threshold $t+2s$. The previous $t+3s+1$ threshold is larger by $s+1$. The example $(426,46,1^8)$ has total degree $480=10\cdot48$, the required first gap and a nonzero actual target vector.

## Verification scope

The two saved verification programs correctly separate finite character comparisons from actual map rank. I read their complete implementations. The 493 stability comparisons and 20 contracted-form scalar evaluations are the author's recorded executions. I did not rerun them. The present event is the complete proof audit of the refined kernel bound, canonical factorization and explicit positive family.
