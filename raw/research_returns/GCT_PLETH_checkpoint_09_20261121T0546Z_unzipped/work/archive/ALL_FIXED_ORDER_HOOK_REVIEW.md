# A102. All valid hook tails at fixed positive ideal order

## Complete result and scope

**PASS.** I read the whole T067 report, AF.1–AF.21 and all seven sections, and the full executable. I independently reconstructed the complementary hook calculation and all finite bounds and signs. I also executed a separate rational highest-space check of every normal Schur label for $1\le q\le3$, $1\le k\le4$: all 124 spaces and 322 cycle traces agree with the executable's formula.

The actual first differential has an image that is a quotient of the ambient stable-hook module. The inequality after AF.21 follows from that surjection. I requested this precise wording in place of “image inclusion in the ambient”; the proof uses the displayed quotient map and requires no additional embedding.

## 1. Valid range and finite concentration

The physical first-gap inequality is $(m-2)a\ge mk+r$, so $a>k$ and therefore $a\ge k+1$. It gives $n=a+t-k\ge1$ and precisely $N=|\alpha|\ge mk$, where the exact signed restriction complex applies. The balanced-flag map and the $S_\alpha F$ multiplicity functor preserve the actual differentials and subset orientations.

At a selected subset of size $q$, the residual space has dimension $d=m-q-1$. The same skew-column argument checked in A100 forces $\rho_i\ge\alpha_{i+d}$ for $1\le i\le q-1$. Thus
$q(k-1)\ge(q-1)(a-1)$ and
$$
q\le\min\left(m-2,\left\lfloor\frac{a-1}{a-k}\right\rfloor\right)\le k.
$$
All further terms vanish in the actual complex. The case $k=1$ has only the singleton term and is included.

## 2. Complete complement list and the residual tensor map

Pad $\alpha$ to the full dimension $m-1$. Its width-$a$ rectangle complement is the hook $\beta=(a,1^r)$. On the specified direct sum of the selected space $P$ and residual space $W$, the full exterior-column pairing pairs a normal type $\rho$ only with
$\gamma=(a-\rho_q,\ldots,a-\rho_1)$.
Contracting the perfect normal pairing leaves a nondegenerate pairing of the multiplicity spaces, with the residual determinant factor $(\det W)^a$. This is the map in AF.11.

The normal total degree is less than $qa$, so $\gamma$ is nonempty. Its containment in the hook forces
$\gamma=(a-A,1^s)$.
The skew diagram $\beta/\gamma$ then has one row of length $A$ and one column of length $r-s$. They share neither a row nor a column. With the fixed ordering of their tensor positions, the normalized row and column projectors act on disjoint factors, giving the actual tensor isomorphism
$\operatorname{Sym}^A W^*\otimes\Lambda^{r-s}W^*$.
This also proves the empty-row and empty-column endpoints.

Complementing back gives exactly
$$
\rho=(a^{q-s-1},(a-1)^s,A).
$$
The conditions $s\le\min(q-1,r)$ and $r-s\le m-q-1$ express the hook containment and the residual dimension; the latter also says that all $a$-rows of $\rho$ fit inside $\alpha$. Its degree bound is
$$
0\le A\le q(k-1)-(q-1)a+s\le k-q.
$$
Together with $A\le a-1$, these are precisely AF.14. Since $A<a-1$, no displayed labels are duplicated by merging the last part with an earlier part.

This verifies the whole list, rather than only a necessary vanishing bound. For $q\ge2$, a surviving term also forces $a\le2k-1$. For $q=1$, the normal shape is the row $(A)$ with $A<k$, independent of the possibly binary-large $a$.

## 3. Normal modules and exact character extraction

The normal module is realized on monomials in $q$ blocks of $q$ variables, each block degree less than $k$. The common kernel of the simple raising operators at weight $\rho$ is its actual highest multiplicity space. Simple raisings generate the upper unipotent action, so no additional highest equations are omitted. Block permutations commute with all those equations.

Padding the weight by zero coordinates to the original rank $R\ge q$ gives an actual inclusion. Every polynomial of the padded weight uses only the first $q$ variables, and every added raising equation vanishes. Thus this inclusion identifies the whole highest space and its block-permutation action.

For a slot cycle of length $\ell$, a diagonal matrix contributes only from equal monomials around that cycle. This gives the factor
$\sum_{u<k}h_u(X_1^\ell,\ldots,X_q^\ell)$.
Multiplication by the Schur alternant then extracts exactly the dominant label $\rho$, with exponent $\rho+\delta-\sigma\delta$ and the displayed sign. The small symmetric-group character is obtained by the same coefficient calculation on the product of power sums. Averaging over cycle classes therefore gives precisely the genuine nonnegative Specht multiplicities of this already constructed normal module.

All normal dimensions and degrees depend only on $k$: $q\le k$ and total degree at most $q(k-1)$. There is no dependence on a large input degree hidden in these arrays.

## 4. Stabilizer signs and bounded induction

The selected subset contributes its orientation sign. The global determinant factor restricted to the stabilizer has exponent $a+t$ on both factors, and the residual determinant contributes exponent $a$ on $S_{m-q}$. Removing the common exponent $t$ leaves exactly $\operatorname{sgn}_{S_q}^{a+1}$ on the normal module, and no complementary sign. Hence the selected label is conjugated exactly when $a$ is even.

The standard symmetric decoration is computed through the actual split sequence induced by
$\mathbb Q^L=\mathbb Q u\oplus\mathfrak h_L$:
the kernel of coordinate-mean projection in degree $A$ is multiplication by $u$ on the preceding symmetric degree. Tensoring with the exterior factor and induction preserve this exact sequence. The difference used by the evaluator is therefore the multiplicity of the actual standard symmetric factor.

The permutation-symmetric factor has monomial orbits with at most $A$ occupied positions. Restricting the standard representation to their stabilizer gives the block standards and one fewer trivial factor than the number of nonempty blocks. Taking exterior powers produces precisely the listed block hooks and binomial coefficients. The selected normal label adds $q$ boxes; all remaining small factors add at most $A$ boxes. Thus at most $q+A\le k$ cells are added to the one large hook. When the zero block is empty, the entire group size is at most $k$.

The large leg is determined by the exterior-degree equation. It is not an additional unbounded search. Distinct intermediate LR shapes are counted by the stated tableau coefficients; individual corner-removal orders add no multiplicity.

## 5. Actual image correction and positive matrices

At $q=1$, the normal representation is scalar and the residual module is exactly the established full jet representation. Its comparison with the original map uses the literal normal substitution and its nonzero leading coefficient map. The complementary Pieri dimensions agree with every graded jet piece because $A<k<a$. The truncated comparison is therefore triangular with invertible diagonal blocks; its inverse is finite triangular elimination. Horizontal local frames complete the actual identification of the first differential with hook jet evaluation.

The signed exact complex proves that the alternating correction is the multiplicity in the image of that differential. Hence it is nonnegative, at most the jet multiplicity, at most $D_k$, and at most the ambient multiplicity by the ambient surjection onto the image. Its kernel is the original balanced module under the specified flag map.

For $a\ge2k$, the concentration bound gives one nonambient term; at $a=2k-1$ it gives exactly the pair correction of T066. Thus these are direct comparisons with the earlier maps, including the endpoint previously proved by scalar regularity.

A positive correction places the label in the jet support, so the previously proved bounded diagonal width applies. At $a\le2k$, the nonrow excess is at most $a-1\le2k-1$; for the invariant label, total degree is at most $3k-1$. These are inside the complete bounded-point enumeration already checked in A096/A098. At larger $a$, the correction is the full jet multiplicity and the previously checked parity transport applies.

The actual image bound proves that enough distinct complete points exist. First-difference deletion from their unique owner cells removes exactly those points, preserves boundedness and produces the stated number of disjoint pieces. Ordering the retained points and the rational nullspace basis of the Young-projected first map specifies the asserted linear bijection to the original multiplicity space. Its rank has already been evaluated by the finite correction; it is not an oracle in the positive evaluator.

For fixed $k$, every correction shape differs from one large hook by at most $k$ cells. The possible small diagrams and their branching depend only on $k$; scanning the large shape and checking its leg has polynomial cost in $m$. The normal arrays depend only on $k$. Exact correction values therefore have the stated fixed-order bit bounds. Positive matrix generation has the displayed bounded-excess tableau count, parameter-sized subset window, small coin degree and at most $D_k$ deletions. All endpoints and the explicit-$m$ encoding qualification are retained.

## 6. Independent rational execution

The reproducible script is `work/archive/check_hook_normal_highest_spaces.py`. It constructs the monomial weight spaces independently, builds the literal matrices
$\sum_i y_{ij}\partial_{y_{i,j+1}}$, takes their rational nullspaces, and restricts actual block-permutation matrices to those nullspaces. Each restricted action is checked by the exact identity $KX=PK$.

For all $q=1,2,3$, $k=1,2,3,4$, and every partition of degree at most $q(k-1)$ with at most $q$ parts, the outcome is:

| Check | Count |
|---|---:|
| Rational highest spaces | 124 |
| Literal cycle traces | 322 |
| Total monomial weight-space dimensions | 2,442 |
| Total highest-space dimensions | 496 |
| Largest individual weight space | 132 |

Every trace agrees with the author's alternating-coefficient formula. The independent side uses neither that Weyl formula nor a character average. Only the final comparison calls the author's `normal_trace`. The receipt `HOOK_NORMAL_HIGHEST_SPACE_RECEIPT.json` records every case, its actual traces and a hash of the raising matrix and rational kernel.

The complete report and executable have been read. The author's large outer-degree scan is separate from this computation and is not rerun here.
