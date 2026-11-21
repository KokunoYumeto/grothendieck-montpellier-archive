# The first pair correction for varying hook jets

## T-066. The complete boundary \(a=2k-1\)

Let \(m\ge4\), \(k\ge2\), \(t\ge0\), \(\mu\vdash m\), and
\[
0\le r\le\min\{m-2,(m-4)k-(m-2)\}.
\tag{PB.1}
\]
An upper bound below zero gives an empty parameter range. Put
\[
a=2k-1,\quad n=k-1+t,\quad
\lambda=((m-1)a+t-mk-r,a+t,(t+1)^r,t^{m-2-r}).
\tag{PB.2}
\]
Let \(\nu=\mu\) for even \(t\), and \(\nu=\mu'\) for odd
\(t\). Write \(c_{m,a,r}(\nu)\) for the stable-hook multiplicity
in G037, and \(d_{m,k,r}(\nu)\) for the explicit positive jet
correction FK.11. Define
\[
e_{m,r}(\nu)=
\begin{cases}
0,&r=0,\\
c^{\nu}_{(m-r-1,1^{r-1}),(2)},&r\ge1.
\end{cases}
\tag{PB.3}
\]
The last Littlewood–Richardson coefficient is the horizontal-two-strip
Pieri indicator, hence is zero or one. Then
\[
\boxed{p_{\mu,(n)}^\lambda
=c_{m,2k-1,r}(\nu)-d_{m,k,r}(\nu)+e_{m,r}(\nu).}
\tag{PB.4}
\]
More precisely, \(d_{m,k,r}(\nu)-e_{m,r}(\nu)\) is nonnegative
and at most \(D_k\) of FK.12. Deleting exactly that number of
explicit points from the stable-hook polytope gives a positive
disjoint-polytope formula with at most
\[
1+D_k\bigl(2(m^2+3m-4)-1\bigr)
\tag{PB.5}
\]
pieces, each with at most \(m^2+3m-4\) variables. The matrices
are generated in \(f(k)(m+k)^{2k+O(1)}\) times a polynomial in
the remaining input bit lengths. Exact coefficient evaluation has
the fixed-order bounds of T064. The ordinary binary-input
qualification remains unchanged: a polynomial bound in the stated
encoding requires that \(m\) be explicit/unary or represented by
the \(m\) positive output parts when \(t\ge1\).

Together with T064 and T065, this covers all valid parameters
\(a\ge2k-1\) in their hook family. At \(k=1,a=1\), the
partition inequality would give \(m-2\ge m+r\), so that missing
formal endpoint has no valid input.

### 1. The actual restriction complex and its degree

Set \(E=\mathfrak h_m\), \(R=m-2\), \(F=\mathbf Q^R\),
and
\[
\alpha=(a^{R-r},(a-1)^r),\qquad
N=|\alpha|=(m-2)a-r.
\tag{PB.6}
\]
Condition (PB.1) is exactly \(N\ge mk\), equivalently
\(\lambda_1\ge\lambda_2\). All entries in (PB.2) are
nonnegative and sum to \(mn\).

Use the specified ideals \(I_i=(\ell_i\otimes F)\) in
\(S=\operatorname{Sym}(E\otimes F)\). G027 FA.4 is an actual
exact complex in degree \(N\), with signed restriction maps and
the orientation of each selected subset. Its kernel is
\((J_k)_N\), where T049 identifies the intersection \(J_k\)
with the literal diagonal quotient of the product of block powers.
Applying the exact \(S_\alpha F\) multiplicity functor preserves
the complex and all \(S_m\) actions. The map back to the balanced
module is FA.6, with the precise factor
\(\operatorname{sgn}^{a+t}\).

For a selected subset of size \(q\), the stabilizer decomposition
FA.13 gives \(W=\mathfrak h_{m-q}\), of dimension
\(d=m-q-1=R-q+1\). The corresponding normal Schur shape
\(\rho\) has size at most \(q(k-1)\), because every selected
normal block is truncated below degree \(k\). Its residual
factor is \(S_{\alpha/\rho}W\).

A semistandard tableau on this skew shape with \(d\) possible
entries has at most \(d\) boxes in each column. This implies
\[
\rho_i\ge\alpha_{i+d}\quad(1\le i\le q-1).
\tag{PB.7}
\]
Indeed, if a column occurs in row \(i+d\) of \(\alpha\) but
not in row \(i\) of \(\rho\), that column of the skew shape
has at least \(d+1\) boxes. Consequently every nonzero residual
factor has
\[
|\rho|\ge(q-1)(a-1)=2(q-1)(k-1).
\tag{PB.8}
\]
For \(q\ge3\), this exceeds \(q(k-1)\), since \(k\ge2\).
Thus every term with at least three selected blocks is zero.
The degree-\(N\) complex therefore has only its ambient,
singleton and pair terms. This is concentration of an already
proved exact complex, rather than a conclusion from an Euler
character alone.

### 2. The ambient and singleton maps

Pad \(\alpha\) by one final zero to length \(\dim E=m-1\).
The perfect exterior-column pairing in the width-\(a\) rectangle
gives the actual map
\[
S_\alpha E\simeq(\det E)^a\otimes
S_{(a,1^r)}E^*.
\tag{PB.9}
\]
The invariant rational form identifies \(E\) with \(E^*\).
Multiplication by the factor \(\operatorname{sgn}^{a+t}\)
from FA.6 changes (PB.9) into precisely the common twist
\(\operatorname{sgn}^t\) of the stable-hook module.

For a singleton, \(W=\mathfrak h_{m-1}\) has dimension \(R\).
Its degree-\(u\) normal factor, \(0\le u<k\), has residual
module \(S_{\alpha/(u)}W\). Complementary exterior pairing
and Pieri give
\[
S_{\alpha/(u)}W\simeq
(\det W)^a\otimes
\bigl(\operatorname{Sym}^uW^*\otimes\Lambda^rW^*\bigr).
\tag{PB.10}
\]
Here every constituent on the right becomes polynomial after the
determinant twist: the largest first part of
\(\operatorname{Sym}^uW^*\otimes\Lambda^rW^*\), before
duality, is at most \(u+1\le k\le a\). More explicitly,
complementing a partition \(\beta\) in the \(a\)-rectangle
identifies a horizontal \(u\)-strip \(\alpha/\beta\) with
a horizontal \(u\)-strip added to \((1^r)\). The ordinary
Pieri rule then proves exactly the multiplicities in (PB.10),
including \(u=0\), \(r=0\), and \(r=R\).

The comparison can be made directly with the original jet map.
On the affine chart at the selected point, FA.8 is the literal
substitution
\(Y_{0a}\mapsto-\sum_jx_jY_{ja}\).
Its degree-\(u\) coefficient map preserves a nonzero least normal
degree, by the invertible generic-matrix argument FA.9. Thus its
associated graded map into the degree-\(u\) form jets is
injective. The complementary Pieri computation (PB.10) proves
equality of those finite dimensions. This is therefore an
isomorphism in each graded piece. The exterior pairing and the
horizontal trivializations HJ.7 give a triangular equivariant
isomorphism on the complete truncated jet spaces; its inverse is
finite triangular elimination. This proves that the singleton
restriction map is the actual hook jet evaluation under these
specified maps.

The determinant in (PB.10) cancels the exponent \(a\) in the
global twist. After removing \(\operatorname{sgn}^t\), the
singleton term is exactly
\[
T_{m,k,r}=\operatorname{Ind}_{S_{m-1}}^{S_m}
\left(\bigoplus_{u=0}^{k-1}\operatorname{Sym}^u
\mathfrak h_{m-1}\otimes\Lambda^r\mathfrak h_{m-1}\right).
\tag{PB.11}
\]
Its multiplicity is the positive formula FK.11 already proved
through actual homogenization, monomial-orbit decomposition,
restricted exterior powers and bounded Littlewood–Richardson
maps.

### 3. The unique pair term and all signs

For a pair, the residual dimension is \(R-1\). If \(r=0\),
condition (PB.7) requires \(\rho_1\ge a=2k-1\), while
the normal total degree is at most \(2k-2\); the term is zero.

For \(r\ge1\), (PB.7) gives \(\rho_1\ge a-1=2k-2\).
Both normal slots must therefore have degree exactly \(k-1\),
and their only surviving shape is \(\rho=(2k-2)\). The
ordinary polynomial multiplication
\[
\operatorname{Sym}^{k-1}F\otimes\operatorname{Sym}^{k-1}F
\longrightarrow\operatorname{Sym}^{2k-2}F
\tag{PB.12}
\]
is its unique Cartan projection. Its inverse on that summand is
the degree-\((k-1,k-1)\) polarization divided by its nonzero
binomial scalar. These are rational maps. Interchanging the two
slots acts trivially on the surviving summand, because (PB.12)
is ordinary commutative multiplication.

The residual Pieri strip must remove the whole bottom row of
\(\alpha\), which has length \(a-1\). That already uses
all normal boxes, so no other row changes. The residual partition
and its actual exterior pairing are
\[
\beta=(a^{R-r},(a-1)^{r-1}),\qquad
S_\beta W\simeq(\det W)^a\otimes\Lambda^{r-1}W^*,
\quad W=\mathfrak h_{m-2}.
\tag{PB.13}
\]
The pair restriction still carries the orientation
\(\operatorname{sgn}_{S_2}\). On its stabilizer
\(S_2\times S_{m-2}\), the factor from FA.6 is
\(\operatorname{sgn}_{S_2}^{a+t}
\operatorname{sgn}_{S_{m-2}}^{a+t}\), while
\((\det W)^a=\operatorname{sgn}_{S_{m-2}}^a\).
Since \(a=2k-1\) is odd, the total exponents on both subgroup
signs are congruent to \(t\). Hence, after the same common
\(\operatorname{sgn}^t\) twist, the pair term is
\[
U_{m,r}=\operatorname{Ind}_{S_2\times S_{m-2}}^{S_m}
\left(\mathbf1\otimes\Lambda^{r-1}\mathfrak h_{m-2}\right)
\quad(r\ge1),\qquad U_{m,0}=0.
\tag{PB.14}
\]
Frobenius induction identifies this with the product of \(h_2\)
and the hook Schur function in (PB.3), proving that indicator.

Every comparison above is equivariant. In particular the
remaining differential is the signed polynomial restriction
\((f_i)\mapsto(f_j|_{ij}-f_i|_{ij})_{i<j}\), composed with
the stated normal Cartan and exterior maps. Its signs are the
ordered-subset signs in FA.4.

### 4. The exact sequence and positive cells

Concentration and the actual comparisons prove the exact sequence
\[
0\longrightarrow\operatorname{sgn}^t\otimes
(S_\lambda\mathbf Q^m)_{(n^m)}
\longrightarrow S_{(a,1^r)}\mathfrak h_m
\longrightarrow T_{m,k,r}
\longrightarrow U_{m,r}\longrightarrow0.
\tag{PB.15}
\]
The left twist equals its own inverse. The last map is onto because
the next term of the exact restriction complex is zero. Thus the
image of the stable-hook jet map is an actual representation whose
\(\nu\)-multiplicity is \(d_{m,k,r}(\nu)-e_{m,r}(\nu)\).
This proves both its nonnegativity and formula (PB.4).

To obtain the positive formula, put
\(c=d_{m,k,r}(\nu)-e_{m,r}(\nu)\). If \(c=0\), retain
the stable-hook polytope. If \(c>0\), the label occurs in the
jet correction. The exact monomial-orbit proof of T064 therefore
gives the same diagonal-width bound \(k+1\); in the row-label
case it gives \(r\le k-1\). The least stable numerator degree
is at least \(r+1\), so the nonrow tableau/subset excess at
\(a=2k-1\) is at most \(2k-2\). In the row case the full
degree is at most \(3k-2\).

Enumerate the low-comajor tableaux, bounded retained-cell subsets
and coin variables exactly as in FK.13–FK.15, with this smaller
budget, and retain the first \(c\) distinct complete points.
For the row label use the same explicit star-basis points.
Sequence (PB.15) proves that the stable coefficient is at least
\(c\), so the exhaustive bounded search supplies all these
points. Each point is checked in the original constraint matrix.
There is no degree translation at this fixed endpoint.

Delete one point at a time from its unique current cell, using
the first coordinate where a lattice point differs, with the
two integral inequalities at that coordinate. All previous
coordinates are fixed to the deleted point. This partitions
the cell minus that point, introduces precisely \(2N_{\rm poly}-1\)
additional pieces, and never changes the underlying bounded
polytope constraints. Induction proves (PB.5), disjointness and
the exact lattice-point count. T064's explicit enumeration and
complexity proof applies with the smaller budget.

The file `pair_boundary_hook_positive.py` exports the literal
polytope matrices, the separate jet and pair multiplicities, and
the direct coefficient evaluator. Its `full_coefficient` and
`full_polytopes` routes combine this boundary with T065 and T064.
The correction uses only FK.11 and a two-cell Pieri test; the
runtime does not construct the restriction-complex matrices.

### 5. Sources and checks

The full actual-complex proof is G027 FA.1–FA.17, strengthened by
the complete diagonal-quotient proof T049 DP.1–DP.10. Those proofs
have been reread for this boundary, including the required
\(N\ge mk\) check and the equivariant subset orientations.
The exterior-column pairing and original hook/flag map are the
specified maps in G027 FA.11 and T062 HJ.2–HJ.3. The primary
Pieri locator is Macdonald, *Symmetric Functions and Hall
Polynomials*, I§5, (5.16)–(5.17), p.73; the Frobenius induction
locator is I§7, (7.1)–(7.3), pp.112–113. The complete
Littlewood–Richardson proof used by the finite correction was
read at I§9, pp.142–147. Primary text:
<https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf>.

The author has read the complete PB.1–PB.15 proof and executable,
including the exact singleton filtration comparison, all vanished
terms, the pair Cartan map and every determinant and orientation
factor. That reading passed. The author proof/code check and
numerical receipts are recorded separately. Root independently
read the complete proof and executable, rechecking the underlying
restriction and diagonal-quotient maps; that review passed.
Archive independently read the complete proof and code; that
review also passed. Its scope is
`work/archive/PAIR_BOUNDARY_HOOK_REVIEW.md` (A100).

The executed script `check_pair_boundary_hook.py` passed 3,193
pair multiplicity comparisons and 6,386 complete coefficient/parity
comparisons against original cycle traces, fixed-point jets and
literal unordered-pair induction. All 1,669 selected-point cases,
containing 18,844 points, passed the original matrices. In 105
literal cases, 36,012 exported cells partitioned 533 original
witnesses into precisely 62 retained witnesses and the prescribed
deleted points. The receipt is `PAIR_BOUNDARY_HOOK_RECEIPT.json`.

Rectangular's
original cycle-index/Murnaghan–Nakayama computation has already
passed 456 coefficient comparisons, including both determinant
parities and 324 coefficients with a nonzero pair-term parameter.
Its expected pair trace sums literal stable two-subsets and the
complementary exterior character, without using (PB.3). The
receipt is `work/rectangular/HOOK_JET_PAIR_ENDPOINT_MN_CHECK.tsv`.
