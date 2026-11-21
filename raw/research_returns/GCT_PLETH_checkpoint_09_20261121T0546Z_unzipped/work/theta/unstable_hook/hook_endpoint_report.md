# The closed endpoint for hook jets

## T-065. Every valid parameter with \(a\ge2k\)

For \(m\ge4\), \(k\ge1\), \(t\ge0\), \(\mu\vdash m\), and
\[
0\le r\le\min\{m-2,(m-4)k\},
\]
put
\[
n=k+t,\qquad
\lambda=((m-2)k+t-r,2k+t,(t+1)^r,t^{m-2-r}).
\tag{HE.1}
\]
Let \(\nu=\mu\) for even \(t\), \(\nu=\mu'\) for odd \(t\).
Then T064's positive correction formula remains exact at the endpoint:
\[
p_{\mu,(n)}^\lambda
=c_{m,2k,r}(\nu)-d_{m,k,r}(\nu).
\tag{HE.2}
\]
The correction is the positive monomial-orbit/exterior/LR expression
FK.11. The endpoint has a disjoint positive-polytope formula with
the same bounds FK.2–FK.4. Combined with T064, this covers every
valid hook parameter
\[
a\ge2k,\qquad (m-2)a\ge mk+r
\tag{HE.3}
\]
in FK.1, in varying outer degree, leg and outer label. Exact
evaluation, fixed-order complexity and the encoding qualification
are unchanged.

### 1. The verified scalar regularity input

The primary result used here is Nagel–Trok, *Segre's regularity
bound for fat point schemes*, Ann. Sc. Norm. Super. Pisa Cl. Sci.
(5), XX (2020), 217–237, Theorem5.3 p233. With their notation,
\[
r(X)\le
\max_{\dim L>0}
\left\lceil\frac{w_L(X)-1}{\dim L}\right\rceil.
\tag{HE.4}
\]
Their Lemma3.1(a), p225, identifies \(r(X)\) with the least degree
at which the restriction to the fat point scheme is surjective.
Remark4.3 p228 gives the equivalent floor convention.
Primary publisher PDF:
<https://journals.sns.it/index.php/annaliscienze/article/download/674/660/892>.
The downloaded source and text are nagel_trok_2020.pdf and
nagel_trok_2020.txt in this directory. The complete proof chain
through Theorem5.3 was read, including the matroid partition argument,
the residual-ideal maps and the multiplicity induction; the known
regularity theorem is used with these exact conventions.

Apply it to \(m\) points of multiplicity \(k\) forming the frame
in \(\mathbb P^{m-2}\), with \(m\ge5,k\ge2\). A proper
\(q\)-dimensional linear space contains at most \(q+1\) frame
points: any \(m-1\) representing frame vectors are independent.
Its contribution to (HE.4) is at most
\[
\left\lceil\frac{(q+1)k-1}{q}\right\rceil
=k+\left\lceil\frac{k-1}{q}\right\rceil\le2k-1.
\]
The full-space contribution is also at most \(2k-1\), since
\[
mk-1\le(2k-1)(m-2)
\quad\Longleftrightarrow\quad
(m-4)k-m+3\ge0,
\tag{HE.5}
\]
and the last quantity is at least \(m-5\) in this range.
Consequently scalar restriction is onto in degree \(2k-1\):
\[
B:\operatorname{Sym}^{2k-1}E^*
\longrightarrow
\bigoplus_{i=1}^m
\mathcal O_{\mathbb P(E),[v_i]}/\mathfrak m_i^k.
\tag{HE.6}
\]
The pointwise homogeneous line is trivialized by the same specified
affine vectors \(v_i\) as in T062. Its scalar action on each
stabilizer is trivial. Characteristic-zero scalar extension preserves
the rank of this rational matrix, so the cited bound gives the
surjectivity over \(\mathbb Q\) as well.

### 2. An actual horizontal right inverse

Matrix \(B\) is explicitly the array of Taylor coefficients of
degree-\((2k-1)\) monomials at the frame points on the charts
\(\ell_i=1\). Equip its source and target with rational invariant
positive forms. The proved surjectivity gives the rational
equivariant right inverse
\[
S=B^*(BB^*)^{-1}.
\tag{HE.7}
\]
Thus (HE.6) is an exact algebraic map with a specified splitting,
not an unevaluated rank requirement.

Use T062's degree-one horizontal trivializations
\(H_i(\phi)=\iota_z(\ell_i\wedge\phi)\). Express a desired form
jet at point \(i\) in this basis, apply \(S\) to each scalar jet
supported at \(i\), and multiply the resulting scalar polynomial
by \(H_i(\phi)\). Its coefficient degree is
\((2k-1)+1=2k\), and it is horizontal. At every other point
the scalar jets vanish to order \(k\), so the resulting form jets
do also. Summing over \(i\) gives an actual rational
\(S_m\)-equivariant right inverse for the hook jet map at \(a=2k\).

There are two endpoint cases outside the regularity calculation.
For \(m=4\), validity of (HE.1) forces \(r=0\). The scalar
degree-\(2k\) interpolation HJ.8 already gives the required map,
without a horizontal factor. For \(k=1\), validity gives
\(r\le m-4\), and T061's exact degree-two adjoint/frame splitting
applies. These cover every parameter in (HE.1).

The same ideal-sheaf kernel, flag projection and determinant
comparison as in HJ.2–HJ.3 now give (HE.2). In particular the
jet target, its monomial-orbit action and its Specht correction
are exactly FK.6–FK.11; there is no new parity twist.

### 3. Explicit positive cells at the boundary

At \(a=2k\), the least hook numerator degree is at least \(r+1\).
Thus the tableaux and retained subsets needed in T064's point
selection have total excess at most \(2k-1\), smaller than
the already-proved bound. In the invariant branch, \(d>0\)
implies \(r\le k-1\), and the total degree is at most \(3k-1\).
Run the same finite enumeration directly at the endpoint and
choose the first \(d_{m,k,r}(\nu)\) distinct complete points.
The newly proved surjection ensures that enough points exist.
No parity translation is needed.

Delete those points by the unique-owner first-difference cells.
Their exact count is
\(1+d(2N_{\mathrm{poly}}-1)\), with \(d\le D_k\), proving
the same piece and variable bounds as FK.3. The enumeration has
smaller excess and degree than T064, so its full complexity proof
applies. The file endpoint_hook_positive.py exports all polytope constraint matrices
and supplies both the endpoint evaluator and a route combining
\(a=2k\) with the complete T064 range \(a\ge2k+1\).

The geometric input (HE.4) and the explicit Gram splitting prove
surjectivity; coefficient computation and polytope generation use
only FK.11 and the bounded enumeration. They do not build or
invert the input-sized matrix \(B\) at runtime.

## Proof and computation status

The author has read the complete proof and executable, including
the scalar bound, the actual horizontal right inverse, both
exceptional parameter ranges and the point-deletion cells; that
reading passed. Root independently read the full proof and code,
and separately checked the primary regularity statement and its
surrounding induction; that review passed. Archive independently
read the complete primary proof chain, every endpoint argument
and the executable; that review also passed. Its exact scope is
`work/archive/HOOK_ENDPOINT_REVIEW.md` (A098).

The executable `check_endpoint_hook.py` passed 5,366 coefficient
and determinant-parity comparisons using original standard-hook
cycle traces and literal fixed-point jets. The comparison side
uses no endpoint evaluator or LR correction. All 1,378 point
selection cases, containing 13,169 distinct removed points, passed
the original matrices. In 133 endpoint cases, 14,684 exported
polytope cells partitioned 279 original witnesses into exactly
82 retained witnesses and the prescribed deleted points. The
receipt is `ENDPOINT_HOOK_RECEIPT.json`.

Rectangular separately passed 338 original cycle-index/Murnaghan–Nakayama
plethysm comparisons for orders two and three, outer degrees four
through six, every valid leg and outer label, and both determinant
parities. That receipt is
`work/rectangular/HOOK_JET_ENDPOINT_MN_CHECK.tsv`.

Source readings, whole-proof reviews and executed endpoint
comparisons have separate ledger events. The result is a
reformulation and application of the cited regularity theorem
through the explicit hook/flag maps; no novelty claim is made
for the scalar regularity bound.

