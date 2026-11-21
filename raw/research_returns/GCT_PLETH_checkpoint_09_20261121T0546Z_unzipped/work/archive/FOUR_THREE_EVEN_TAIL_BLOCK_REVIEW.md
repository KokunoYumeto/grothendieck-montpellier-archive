# A-083. Whole-proof review of R043

**Status: PASS.** I read all of `work/rectangular/four_three_even_tail_canonical_block.md`, ME.1–ME.20 and all seven sections. I independently derived its raw expectation matrix, determinant, finite unit endpoint and cubic cancellation. The full two-dimensional block and all finite/cubic/quadratic endpoints pass.

## 1. Entire invariant span and actual generators

The generators
$\Phi_1=S_{11}f_2-S_{12}f_1$ and
$\Phi_2=\mathcal B_S(D_{11},C_2)-\mathcal B_S(D_{12},C_1)$
have weight $(4,3,2^{m-2})$. Congruence gives their common determinant-square factor and three free covariant indices. The raising operator $E_{12}$ sends the two terms of each difference to the same all-first-index component; every other raising operator kills the selected highest components.

The actual four-column invariant-algebra surjection bounds the multiplicity by two. For transpose shape $(m,m,2,1)$, only exterior degree one contributes: exterior degree three already contains two determinant columns. The two possible paired shapes are $(m-1,m-1,1,1)$ with no separate determinant and $(m-2,m-2,0,0)$ with one determinant. Each takes the unique vertical strip in rows one, two and three. These choices remain valid at $m=2$.

Weighted Cauchy–Binet gives ME.6–ME.8. In the latter mixed derivative, the lower block contributes $a\Phi_2$, the top-left quadratic entry contributes $\Phi_1$, and the two off-diagonal terms are both $-2\det(S)C_{112}$, so they cancel in the difference. This checks the exact coefficient one in $a\Phi_2+\Phi_1$.

Each raw cubic weight has zero cubic leading term in any fixed varying original row, since that term is a multiple of $v_1^2v_2-v_1v_2v_1$. The determinant square has row degree at most two, so both $\Phi_j$ have row degree at most four and homogenize by the displayed slot map for $n\ge4$.

## 2. Independent derivation of the moment matrix

Let $k=m+1$, $l=a-k$. Dividing the fixed-subset expectations by $k!$, the inside mixed derivative gives $F_2+F_1$. Its $l$ outside quadratic terms add $lF_1$. Thus
$L(Xf_I)/k!=F_2+(l+1)F_1$.
For $Y-X$, independent outside first moments vanish and its same-row cubic difference is zero, proving the same value for $Y$. For $Z$, completely inside terms cancel; outside linear terms vanish; the outside second moments give $lF_1$.

The centered contribution to $a^2\Phi_1$ is $aX-kY-Z$, giving
$l^2F_1/a^2+lF_2/a^2$.
The other centered weight has expectation $l(F_1+F_2)/a$. Using ME.8 then gives

$$
\mathcal E_{a,m}=
\begin{pmatrix}
l^2/a^2&l/a^2\\
kl/a^3&(a-1)l/a^3
\end{pmatrix},
\qquad
\det\mathcal E_{a,m}=\frac{l^2(l-1)}{a^4}.
$$

These are independent equality-pattern derivations of all four entries, not deductions from the proposed final matrix.

At $U=I$, the third tensor $C_{222}=1$ gives $F_1=1$; varying $D_{1111}$ changes $F_2$ independently. Hence the determinant proves independence for $a\ge m+3$. The actual zero-padding/orthogonal-projection maps preserve every centered moment tensor with scalar one. The invariant-algebra generators therefore prove that the finite-row images of these two generators span every smaller invariant space.

At $a=m+2$, the complement of each affine-minor subset is one row. Directly substituting its centered first and second sums gives
$\Phi_2=(a-1)\Phi_1/a$, with $\Phi_1\ne0$.
At $a=m+1$, every subset is the whole row set, whose centered first sums vanish; at smaller $a$ there are no such subsets. Thus the exact dimension is $\min(2,\max(0,a-m-1))$.

## 3. Split moments, inverse and finite ranks

The common split-moment factor is
$2(-1)^m/[n^{m+1}(n-1)^{m+1}(n-2)]$.
The first generator contains $m$ second moments and one third moment, which gives that factor directly. For the second, the fourth-moment numerator and the mixed determinant derivative give
$(m+1)\Phi_1-6\Phi_2$.
Indeed $\mathcal B_S(S,C_p)=(m-1)f_p$, and the rank-one terms supply the remaining $2\Phi_1$ after cancellation of their $C_{112}$ terms. The denominator ratio is exactly $u_n=n(n-1)/((n-2)(n-3))$.

This proves the matrix $\mathcal H_{n,m}$ and the entire ME.16 identity under the actual normalized split-form pairing. The column-coordinate matrix is the transpose of $\mathcal E\mathcal H$, so the inverse order in ME.17 is correct.

For full two-dimensional blocks both determinants are nonzero. For a mixed one/two-dimensional endpoint, either the invertible larger matrix maps onto the finite target span or the nonzero endpoint row remains nonzero in the full target. At the remaining unit square $a=n=m+2$, substituting the finite relation gives

$$
\frac{m^2-3m-2}{(m+2)m(m-1)}.
$$

I reconstructed this fraction independently. Its numerator takes values $-4,-2,2$ at $m=2,3,4$ and thereafter increases by $2m-2>0$, so it never vanishes for an integer $m\ge2$. This proves every asserted rank endpoint.

## 4. Cubic and quadratic endpoints

The exact outside-subset identity for
$\Psi=a\Phi_2-(a-1)\Phi_1$
is ME.19. For a row inside the determinant subset, its only occurrence in the complementary cubic weight is through a common mean, and that dependence is linear. For an outside row the determinant is independent of it. Thus every row degree is at most three.

Above the finite endpoint, $\Psi$ is nonzero. The first row of $\mathcal E$ has nonzero genuine fourth-moment dependence, so $\Phi_1$ does not extend to degree three. This proves that the whole cubic extension is exactly the displayed line; at the unit endpoint the line vanishes and the remaining invariant still has degree four.

The independent expectation combination is
$L^{\otimes a}\Psi=-(a)_{m+1}l(l-1)F_1/a$.
Fourth moments cancel before specialization. At three split factors $F_1$ is a scalar multiple of $\Phi_{1;3}$, which vanishes because $3\le m+1$. Thus the actual cubic image is zero.

For degree two, the exact symmetric-matrix LDL and principal-minor maps of R042 show that a highest polynomial has even parts. The present part equal to three excludes the target. These endpoint conclusions concern the full multiplicity spaces.

## 5. Executed scope

`check_mixed_width_four_symbolic.py` reconstructs the four entries, determinant, unit-square fraction and cubic cancellation by exact rational arithmetic. `MIXED_WIDTH_FOUR_SYMBOLIC_RECEIPT.json` records their PASS together with the R042 scalar reconstruction. The original 78 literal pairings and 59 target/source coefficient checks are attributed to their original report and were not rerun.
