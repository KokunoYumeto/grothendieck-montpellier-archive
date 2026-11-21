# A-076. Complete independent audit of the three-dimensional block R-041

**Status: PASS.** Reviewer: GPT-6 Astra Pro; effort not exposed; run
/root/archive_audit. The complete `four_even_tail_canonical_block.md`,
QE.1–QE.20 and all seven sections, was read and checked. An independent
exact matrix reconstruction was also executed; the original literal
pairing/MN sweeps were not rerun or claimed here.

## 1. Highest generators and the exact degree-four extension

For $m\ge2$, $a\ge m+1$, $n\ge4$, the first part of
$\lambda=(an-2m-2,4,2^{m-1})$ is at least $2m+2$.
All three centered polynomials have determinant-square weight
$(2^m)$ and two uncontracted covariant indices equal to one.
Their exact congruence and complementary-minor transformations
therefore give highest weight $(4,2^{m-1})$. Row symmetry
and translation invariance follow from the centered sums.

The coefficient identity for $P_3$ is the determinant's second
coefficient and has exactly the factor one half in QE.4.
The three weighted Cauchy–Binet identities were checked directly.
For the first, $\det(R^tR)=a\det S$. For the second, row weights
$1+t s_i^2$ have top-left derivative $S_{11}$ and lower-block
derivative $D$; the off-diagonal derivatives do not contribute at
first order. For the third, weights $1+t s_i$ give the block matrix

$$
\begin{pmatrix}a&t(Se_1)^t\\tSe_1&S+tC\end{pmatrix}.
$$

Its second coefficient is $aP_3-(Se_1)^t\operatorname{adj}S(Se_1)
=aP_3-P_1$. Thus QE.5 has the stated signs and scalar factors.
Every determinant square has row degree at most two, and each
centered weight has total degree two and hence row degree at most
two. The three polynomials have row degree at most four.
Multiplication by $u^n$ after dehomogenization is therefore the
actual polynomial extension for every $n\ge4$.

## 2. Unit bounds and the finite-row surjection

The transpose tail is $\gamma=(m,m,1,1)$.
In the exact four-column invariant algebra, exterior degree zero
contributes the two paired-shape solutions
$(l,q,p)=(0,1,m)$ and $(1,0,m-1)$.
Exterior degree two is $\det T\otimes\Lambda^2T$.
Its fourth part forces $q=l=0$, and its unique vertical two-strip
adds rows one and two to $(m-1,m-1,1,1)$.
This remains valid at $m=2$. Exterior degree four has fourth
part at least three and cannot contribute. Odd exterior degrees
have the wrong total parity. These actual Young/Pieri maps give
the bound three.

The finite-row comparison is an actual surjection, not a
dimension extrapolation. Padding zero coordinates gives
$\iota:\mathfrak h_a\hookrightarrow\mathfrak h_{A_0}$.
For the ordinary dot products its transpose satisfies
$q(P_{A_0}e_i)=P_ae_i$ for $i\le a$, and zero otherwise:
pairing with every centered vector proves this formula directly.
The exterior algebra map $\Lambda(q\otimes1_T)$ sends each
row power-sum generator to the same generator with $a$ rows.
Those generators span the whole target invariant algebra by the
signed equality-partition proof already checked in A-071.
Thus restriction is onto, and it is $GL(T)$-equivariant.
Taking the actual skew-Cauchy Young summand gives the asserted
surjection on the desired Schur invariant spaces.

Its polynomial realization is restriction along $\iota$, using
the invariant dot products and functorial Young projections.
Since centered rows sum to zero, zero-padding leaves $S,C,D$
unchanged. Every $P_j$ therefore restricts with scalar one.
Once independence is established at a large row count, this
surjection proves that the same three generators span at every
smaller count.

## 3. Independent moment-table derivation and finite dimensions

For a fixed subset of size $k=m+1$, the two-determinant pairing
is $k!\det U$. Its first weighted derivative by $w_1^2$ gives
$k!(Q+R)$. The second coefficient with weight $w_1$ is
$k!(T-Q)$. Hence $T_I^2=U_I+2e_2(w_I)$ gives
$k!(R+2T-Q)$. Independent outside rows have zero first
moments and squared-sum expectation $lU_{11}$, $l=a-k$.
These observations prove every entry of the displayed six-row
expectation table.

The three centered weights are exactly the ones displayed in the
report: expanding $s_i=w_{i1}-T_{\rm all}/a$ gives them term
by term. Returning to the generators uses
$P_1=A/a$, $P_2=(B-P_1)/a$, and $P_3=(C'+P_1)/a$.
There are $\binom ak$ subsets, giving the common factor $(a)_k$.

The independent script `check_four_even_tail_symbolic.py` starts
from these six expectation identities and these three changes
of generators. It reconstructs all nine entries of $\mathcal C$
and compares them exactly with QE.11. Every entry agrees, and
its determinant is exactly

$$
\det\mathcal C_{a,m}
=\frac{(a-m-2)(a-m-1)^2}{a^5}.
$$

The formal variables $Q,R,T$ are independent: at $U=I$,
zero higher moments give $(1,0,0)$; varying the symmetric fourth
entry changes $R$; the admissible symmetric third tensor with
$C_{111}=C_{122}=1$ has a slice with two diagonal ones and
gives $T=1$. These are arbitrary formal linear-functional moments,
so no positivity assumption is needed. Thus for $a\ge m+3$
the actual $P_j$ are independent and, with the bound three,
span the whole invariant space.

At $a=m+1$ the sole subset is the full centered row set, so
$B=A$ and $C'=-A/2$. This gives both relations QE.13.
The centered simplex has $P_1=2(m+1)$, hence dimension one.
At $a=m+2$, each subset omits one row; the centered identities
give $B+C'=A/2$, hence $P_2+P_3=P_1/2$.
The independently reconstructed first-two-row/column minor is
$(m-1)/(m+2)^3\ne0$, proving dimension two.
For $a\le m$, all subset sums are empty, and the proved
finite-row spanning implies dimension zero. This proves exactly
$r_a=\min(3,\max(0,a-m))$.

Every generator extends at $n\ge4$; dehomogenization injects
the full highest space and has the displayed inverse on its
spanning generators. The target multiplicity is therefore $r_a$.

## 4. Normalized split-form matrix and all endpoint ranks

The centered fourth split-form moment is the ordered-index
inclusion–exclusion expression consisting of the three two-pair
products minus six times the four-equal term. It gives QE.15,
including repeated coordinate labels. The second and third
moments have the stated factors $-1/N_2$ and $2/N_3$.

For $Q$, the combined sign is $(-1)^{m+1}=(-1)^{m-1}$.
For $R$, adjugate scaling gives the middle row of $\mathcal D$,
using $\operatorname{tr}(\operatorname{adj}S\,S)=m\det S$
and $(Se_1)^t\operatorname{adj}S(Se_1)=P_1$.
The remaining ratio is $N_2^2/N_4=u_n$.
For $T$, its degree is $m-2$ in $S$ and two in the third
slice, giving the ratio $-4N_2^3/N_3^2=-4v_n$.
This verifies all signs and denominators in QE.16–QE.18.

The report uses rows for the images of the three source
generators, so the column-coordinate matrix is
$c_{a,n,m}(\mathcal C_{a,m}\mathcal D_{n,m})^t$.
Its stated inverse has the correct order:
$c^{-1}(\mathcal C^{-1})^t(\mathcal D^{-1})^t$.
All factors are nonzero in the full three-dimensional range,
and the scalar-one canonical pairing fixes the normalization.

The $a=3$ endpoint is handled precisely. Individual target
expressions may be homogeneous rational functions, but they
are independent after multiplication by the common nonzero
power of $u$ on the chart. The displayed linear combinations
are the actual polynomial images. The matrix-rank argument
therefore uses a valid injection into that rational function
space and makes no unsupported assertion that each individual
generator extends in inner degree three.

The independent symbolic reconstruction also gives every
printed finite endpoint expression exactly:

- one-dimensional square: $(m-2)/(m-1)$;
- two-dimensional square determinant:
  $-2(m+1)(3m+2)/(m^3(m+2))$;
- mixed second coefficient:
  $-2(m+2)^2(3m-2)/(m^2(m-1)(m+1))$.

The first is used only at $m\ge3$, since $m=2,n=3$
is outside the theorem. The other two are nonzero for every
declared $m\ge2$. In mixed large/small sizes, either the full
matrix is invertible before projecting to the finite target
span, or the relevant one/two source rows of $\mathcal C$
are independent and multiplication by $\mathcal D$ preserves
that rank. This proves the smaller rank in each direction.
For $n\le m$, the target generators vanish and source length
also gives zero. The exact scalar-one transposition transfers
these ranks to the requested map $h_{n,a}$.

Thus the full law is $\min(r_a,r_n)$, including every finite
endpoint. The rational tensor, exterior-column, Young and
determinant maps give the stated rank and bundle transport.
The Chow interpretation is the previously checked actual
coordinate-ring pullback.

## 5. Executed verification scope

The complete proof was independently read. The new symbolic
execution reconstructs all **nine** matrix entries, the full
determinant, the finite-row independence minor, and the **three**
endpoint reductions from the independent formal moment table.
All pass with exact rational arithmetic.

The executable and receipt are `check_four_even_tail_symbolic.py`
and `FOUR_EVEN_TAIL_SYMBOLIC_RECEIPT.json`. No repeat of the
original 246 literal pairings or 42 multiplicity checks is claimed.
