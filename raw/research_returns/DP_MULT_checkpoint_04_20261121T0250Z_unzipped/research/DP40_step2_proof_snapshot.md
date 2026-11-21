# DP40: the maximal sum of cyclic CM directional slopes

Date: **2026-11-21 UTC**. Agent: `/root/step2_higher`. Model: **GPT-6 Astra Pro**. Effort setting: **not exposed**. The root reserved finding **DP40**. This memo proves the combinatorial comparison independently of the construction of the general cyclic formal-group model. The root is supplying that geometric/formal-group realization separately. No global theta-cost conclusion is asserted here.

## 1. Statement and normalization

Let $p>1$ (in the application, $p$ is prime), let $h\ge1$, set

\[
 q=p^h,\qquad \rho_h=\frac1{q-1},\qquad
 c_h=\frac1{p-1}-\frac1{p^h-1},\qquad c_2=\frac p{p^2-1}.
\]

Let $A\subset\mathbb Z/h\mathbb Z$ be a binary type. For every index $i$, define the directional number

\[
 \gamma_i(A)=\rho_h\sum_{\substack{j\in\mathbb Z/h\mathbb Z\\
                       1_A(j)\ne1_A(i)}}p^{[i-j]_h},
\tag{CM1}
\]

where $[i-j]_h\in\{0,\ldots,h-1\}$ is the least nonnegative residue. The exponent zero never occurs in this sum because the types of $i$ and $j$ differ. On $i\in A$, this is precisely the proposed cyclic-display formula, while on $A^c$ it is its complementary formula.

Put

\[
 N_k=|A\mathbin\triangle(A+k)|,
 \qquad
 S_h(A)=\sum_i\gamma_i(A).
\]

Then

\[
 \boxed{S_h(A)=\frac{\sum_{k=1}^{h-1}N_kp^k}{p^h-1}
       \le h\frac p{p^2-1}.}
\tag{CM2}
\]

Equality holds if and only if $h$ is even and $A$ is one of the two alternating types (the even or the odd indices). For odd $h$ the inequality is strict. For $A=\varnothing$ or the full cycle, the sum is zero.

The two complementary partial sums are always equal:

\[
 \sum_{i\in A}\gamma_i(A)
 =\sum_{i\notin A}\gamma_i(A)
 =\frac12 S_h(A).
\tag{CM3}
\]

Thus (CM2) compares the sum over the type **and its dual**, or equivalently all $h$ indices. It does not bound each directional number by $c_2$.

## 2. Counting the oriented pairs: the factor-two check

For a fixed displacement $k$, the terms with $i-j=k$ are exactly the indices $i$ for which $1_A(i)\ne1_A(i-k)$. There are $N_k$ such indices, proving the sum identity in (CM2).

The number of these pairs with $i\in A$ is

\[
 |A\setminus(A+k)|=|A|-|A\cap(A+k)|.
\]

The number with $i\notin A$ is

\[
 |(A+k)\setminus A|=|A|-|A\cap(A+k)|.
\]

They are equal because translation preserves $|A|$. Therefore each count is $N_k/2$, proving (CM3). In particular every $N_k$ is even. Also $N_k=N_{h-k}$ by translation, a useful independent orientation check.

Finally,

\[
 \rho_h\sum_{k=1}^{h-1}p^k
 =\frac{p^h-p}{(p-1)(p^h-1)}
 =c_h.
\tag{CM4}
\]

There is no extra factor of two in the total $S_h$, and there is exactly a factor of two between that total and either type's partial sum.

## 3. Complete Fourier proof and equality classification

Set $x_i=1$ on $A$ and $x_i=-1$ on $A^c$. For $1\le k<h$, put
$C_k=\sum_i x_ix_{i-k}$.
Then $C_k=h-2N_k$, so

\[
 S_h(A)=\frac12\left(hc_h-\rho_h\sum_{k=1}^{h-1}p^kC_k\right).
\tag{CM5}
\]

Define the real circulant operator

\[
 (Wx)_i=\rho_h\sum_{k=1}^{h-1}p^kx_{i-k}.
\]

It need not be symmetric, but $x^TWx$ equals the quadratic form of its symmetric part. At the discrete Fourier frequencies
$\theta_m=2\pi m/h$, $0\le m<h$,
that symmetric part has eigenvalue

\[
 \lambda_m=\rho_h\sum_{k=1}^{h-1}p^k\cos(k\theta_m).
\tag{CM6}
\]

**Important domain of the next identity:** it is evaluated at these $h$th-root frequencies. A finite sum of this shape is not the displayed rational function for arbitrary real $\theta$ without the root-of-unity condition.

For $z=e^{i\theta_m}$, $z^h=1$ gives

\[
 \rho_h\sum_{k=1}^{h-1}p^kz^k
   =\frac1{pz-1}-\rho_h.
\]

Taking real parts yields

\[
 \lambda_m
 =\frac{p\cos\theta_m-1}{p^2-2p\cos\theta_m+1}-\rho_h
 =\Re\left(\frac{p^{-1}e^{i\theta_m}}
                   {1-p^{-1}e^{i\theta_m}}\right)-\rho_h.
\tag{CM7}
\]

The function $(pt-1)/(p^2-2pt+1)$ is strictly increasing on $[-1,1]$, since its derivative is
$p(p^2-1)/(p^2-2pt+1)^2>0$.
Hence every eigenvalue is at least

\[
 \lambda_*=-\frac1{p+1}-\rho_h,
\tag{CM8}
\]

and equality requires $\cos\theta_m=-1$. Equivalently $h$ must be even and $m=h/2$.

Use normalized Fourier coefficients
$\widehat x_m=h^{-1/2}\sum_jx_je^{-2\pi imj/h}$.
Parseval gives $\sum_m|\widehat x_m|^2=\sum_jx_j^2=h$, and diagonalization gives

\[
 x^TWx=\sum_m\lambda_m|\widehat x_m|^2\ge h\lambda_*.
\]

Inserting this into (CM5),

\[
 S_h(A)\le\frac h2(c_h-\lambda_*)
 =\frac h2\left(\frac1{p-1}+\frac1{p+1}\right)
 =h\frac p{p^2-1}.
\]

If equality holds, every nonzero Fourier coefficient must occur at $m=h/2$. Thus $h$ is even and $x_j=a(-1)^j$ for a real scalar $a$. Since all $x_j$ are $\pm1$, $a=\pm1$, so the type is alternating. Conversely, an alternating type has $N_k=h$ for odd $k$ and zero for even $k$; the finite geometric sum gives $S_h(A)=hp/(p^2-1)$. This proves the full equality classification. ∎

An explicit nonnegative gap certificate is

\[
 \boxed{hc_2-S_h(A)=\frac{p(p-1)}{2(p+1)}
 \sum_{m=0}^{h-1}
 \frac{1+\cos\theta_m}{p^2-2p\cos\theta_m+1}
 |\widehat x_m|^2.}
\tag{CM9}
\]

It follows by subtracting (CM8) from (CM7):
$\lambda_m-\lambda_*=p(p-1)(1+\cos\theta_m)/((p+1)(p^2-2p\cos\theta_m+1))$.
This independently verifies the sign and equality case.

## 4. Optional stronger cardinality bound

If $r=|A|$, then

\[
 \boxed{S_h(A)\le\frac{4r(h-r)}h\,c_2.}
\tag{CM10}
\]

Indeed $\lambda_0=c_h$ and $|\widehat x_0|^2=(2r-h)^2/h$. Bound every other eigenvalue by $\lambda_*$, preserving the zeroth mode exactly in (CM5). As $c_h-\lambda_*=2c_2$, the result is

\[
 S_h(A)\le hc_2-c_2\frac{(2r-h)^2}{h}
           =\frac{4r(h-r)}h c_2.
\]

Equality in (CM10) holds only for the two constant types or for an even alternating type. For a nonconstant equality word, the only possible Fourier modes are zero and $h/2$, so $x_j=a+b(-1)^j$. Its two values being $\pm1$ forces them either to be equal (a constant type) or opposite (an alternating type). If $h$ is odd, the $h/2$ mode is absent. This refinement is not needed for (CM2), but explicitly separates the dimension imbalance of a type from the total equal-direction comparison.

Both bounds add over disjoint cyclic blocks. This is an algebraic statement about their sums; it does not identify the global theta costs with those sums.

## 5. Height six, three consecutive selected embeddings

Take $h=6$ and $A=\{0,1,2\}$. Direct counting gives

\[
 (N_1,N_2,N_3,N_4,N_5)=(2,4,6,4,2).
\]

For $i=0,1,2$, formula (CM1) gives

\[
 (\gamma_0,\gamma_1,\gamma_2)
 =\frac{(p+p^2+p^3,\ p^2+p^3+p^4,\ p^3+p^4+p^5)}{p^6-1}
 =\frac{(p,p^2,p^3)}{(p-1)(p^3+1)}.
\tag{CM11}
\]

The same triple occurs on the complementary indices $3,4,5$. Hence

\[
 \begin{aligned}
 S_6(A)
 &=\frac{2p+4p^2+6p^3+4p^4+2p^5}{p^6-1}\\
 &=\frac{2p(p^2+p+1)}{(p^2-1)(p^2-p+1)}\\
 &=6c_2-\frac{4p(p-1)}{p^3+1}.
 \end{aligned}
\tag{CM12}
\]

Its ratio to the alternating total is

\[
 \boxed{\frac{S_6(A)}{6c_2}
       =\frac{p^2+p+1}{3(p^2-p+1)}<1,}
\tag{CM13}
\]

because the denominator minus the numerator is $2(p-1)^2>0$. The ratio tends to $1/3$ as $p$ grows.

| Prime | Directional triple on the type | Total on type plus dual | Alternating total $6c_2$ | Ratio |
|---|---|---|---|---|
| $p=3$ | $(3,9,27)/56$ | $39/28$ | $9/4$ | $13/21$ |
| $p=5$ | $(5,25,125)/504$ | $155/252$ | $5/4$ | $31/63$ |

This is an **average/sum** limitation, not a componentwise one. In fact the largest direction in (CM11) satisfies

\[
 \gamma_2-c_2=\frac p{p^3+1}>0.
\tag{CM14}
\]

The other two losses more than offset it. Thus arbitrary unequal directional weights would require a separate analysis; concentrating weight on this last direction already defeats a proposed componentwise upper bound by $c_2$.

### The genus-three curve's Frobenius word

The CM type of the already constructed Jacobian of $y^2=x^7-1$ is $\Phi=\{1,2,3\}$ in $(\mathbb Z/7)^\times$ (DP22). For a good prime in residue class3, the Frobenius orbit beginning at1 is

\[
 (1,3,2,6,4,5),
\]

so the first three positions are selected. For residue class5, begin at2; its orbit is

\[
 (2,3,1,5,4,6),
\]

and again the first three positions are selected. Both are full length-six orbits, and complex conjugation is shift3 because $3^3\equiv5^3\equiv-1\pmod7$. Thus their binary word is exactly $A=\{0,1,2\}$ up to cyclic reindexing. There are three holomorphic directions; their proposed sum is $S_6(A)/2$, so their equal-direction mean is $S_6(A)/6$. These calculations use the established CM type and elementary residue arithmetic. Identification of (CM11) with the actual directional formal-group slopes uses the separate general cyclic-display theorem, not the Fourier argument alone.

## 6. Scope and actual checks

The proved comparison is for the explicitly defined numbers (CM1). Once the root's cyclic-display realization identifies those numbers with sharp directional slopes, (CM2) says that the equal-direction sum on a CM block together with its dual is maximized precisely by alternating type. It does not state that the global theta-lift main term or costs are proportional to this sum. It does not prohibit larger gain in one direction, a different weighted selection, cancellation of a specified gauge, or a different shorter correspondence. Equation (CM14) is a concrete warning against that extrapolation.

Actual proof checks by `/root/step2_higher`, GPT-6 Astra Pro, effort not exposed:

* **CM40-P001:** Independently derived and checked the oriented crossing counts, factor two, symmetry $N_k=N_{h-k}$, and the identity $\sum p^k/(q-1)=c_h$.
* **CM40-P002:** Independently derived the Fourier eigenvalues at the discrete root frequencies, monotonicity, the exact gap certificate, Parseval normalization, and both directions of the alternating equality classification, including $h=1,2$.
* **CM40-P003:** Independently proved the cardinality refinement and its equality classification; checked that it does not assert a componentwise bound.
* **CM40-P004:** Independently calculated all five height-six crossing counts, six directional numbers, factorization of the total, exact ratios at3 and5, the positive last-direction excess, and both Frobenius orbit orderings for the genus-three type.
* **CM40-N001:** At the observed clock **2026-11-21 02:03:57 UTC**, an exact rational finite check enumerated every binary word for $h=1,\ldots,10$ and $p\in\{2,3,5,11\}$: **8,184 word/parameter cases**. All factor-two identities, symmetry/parity checks, universal bounds/equality cases and cardinality-refinement/equality cases passed. Results are in `dp40_cyclic_sum_finite_checks.json`. This is a finite cross-check, not the proof for arbitrary $h$ or $p$.

The final whole-memo reread, version hashes, and separately attributed independent reviewer reports are recorded in `dp40_cyclic_sum_checks.json` after completion. No Lean formalization or computation of a global theta cost is claimed.
