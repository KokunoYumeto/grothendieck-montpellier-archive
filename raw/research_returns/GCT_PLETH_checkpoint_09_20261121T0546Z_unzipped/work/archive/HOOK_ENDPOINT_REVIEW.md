# A098. Closed endpoint for the hook jet map

## Result and reviewed scope

**PASS.** I read the complete T065 report, HE.1–HE.7 and all three proof sections, the complete endpoint evaluator and checker, the reused bounded-point enumerator in T064, and the saved endpoint receipt. I also independently opened the publisher's primary PDF and read the proof chain through Nagel–Trok Theorem 5.3, with the exact regularity convention. No repetition of the author's numerical sweep is claimed.

The result extends the actual jet-surjection map to every valid endpoint $a=2k$. For $m\ge4$, the allowed legs are exactly $0\le r\le\min(m-2,(m-4)k)$, which is the first-partition-gap condition for HE.1. The partition sum is $m(k+t)$, and the determinant comparison changes the outer label by conjugation precisely for odd $t$.

## 1. Primary input and the complete numerical specialization

The primary source is Uwe Nagel and Bill Trok, *Segre's regularity bound for fat point schemes*, Ann. Sc. Norm. Super. Pisa Cl. Sci. (5), XX (2020), 217–237:

https://journals.sns.it/index.php/annaliscienze/article/download/674/660/892

The exact locators are Lemma 3.1(a), p.225; Remark 4.3, p.228; and Theorem 5.3, p.233. I read §§2–5 through that theorem, including the matroid partition construction, the residual induction lemmas, the reduced-point step and Proposition 5.2. I visually checked pp.225 and 233 in the publisher PDF. The source retained by the author is `work/theta/unstable_hook/nagel_trok_2020.pdf`, with its extracted text beside it.

The regularity index is the degree of surjective restriction, rather than the ideal's regularity shifted by one. For a fat point scheme it is bounded by the maximum, over positive-dimensional linear spaces, of $\lceil(w_L-1)/\dim L\rceil$. The use in HE.4 therefore has the correct shift.

For the frame of $m$ points in $\mathbf P^{m-2}$, every $m-1$ representing vectors are independent. A proper $q$-plane has at most $q+1$ points, so its contribution at uniform multiplicity $k$ is at most
$$
k+\left\lceil\frac{k-1}{q}\right\rceil\le2k-1.
$$
The full-space contribution has the same bound because
$$
(2k-1)(m-2)-(mk-1)=(m-4)k-m+3\ge m-5\ge0
$$
for $m\ge5$, $k\ge2$. This checks both equality endpoints $m=5,k=2$ and the entire asserted range. It proves the rank of the exact scalar restriction map in degree $2k-1$.

In the source's final induction on p.233, the minimal generators of $I_P^{m-1}$ are the products $\ell_i h_j^{(i)}$, and the factors nonzero at $P$ are $q_j^{(i)}$. These are respectively the $g$ and $f$ roles of the stated claim and of Lemma 3.5. The intervening swapped letters are a notation slip; keeping these roles proves the claimed residual equality and does not change either product. In this application the exponent in Lemma 3.5 is $m-1$. The representable quotient constructions choose auxiliary points outside $P$, so the quotient vectors used in the matroid argument are nonzero.

## 2. The rational equivariant scalar splitting

The Taylor matrix $B$ uses actual homogeneous monomials and the specified affine charts $\ell_i=1$. The projective frame and all their representatives are rational. Its target is the direct sum of the local rings modulo their $k$th maximal-ideal powers, with the homogeneous line trivialized by the chosen representative.

The stabilizer of a frame vector fixes that vector exactly. It therefore acts trivially on this trivialized line, and its action on the transverse affine coordinates is the standard action already used in T062. There is no additional character in the scalar jet target.

The regularity result proves surjectivity over $\mathbb Q$: one can either apply its arbitrary-field formulation directly or extend the rational matrix to characteristic zero and descend its rank. Rational invariant positive forms are obtained by finite averaging. Hence
$$
S=B^*(BB^*)^{-1}
$$
exists, is rational, satisfies $BS=1$ and commutes with the group action. The adjoint is taken using those invariant forms. This supplies an exact map and a proved inverse matrix; its invertibility is not a remaining hypothesis.

## 3. Horizontalization and all exceptional endpoints

At point $i$, let $\phi$ lie in the exterior power of the transverse covectors and use
$$
H_i(\phi)=\iota_z(\ell_i\wedge\phi).
$$
This polynomial form has coefficient degree one and is horizontal because $\iota_z^2=0$. On the affine chart $\ell_i(z)=1$, restriction to tangent vectors in $\ker\ell_i$ gives exactly $\phi$: the term containing $\ell_i$ vanishes on those tangent vectors. Thus these are a genuine free local frame for the horizontal bundle, including all jets, rather than only its fiber at the central point.

Express the prescribed form jet in that frame. Apply $S$ to each scalar coefficient, supported at the one point, and multiply its scalar polynomial by the corresponding $H_i(\phi)$. The degree is exactly $(2k-1)+1=2k$. At every other point its scalar factor belongs to the $k$th maximal-ideal power; multiplication by a regular form preserves that vanishing. Summing over all points gives the required right inverse.

The construction is independent of the temporary exterior basis: it is evaluation and multiplication of the corresponding identity tensor. The charts and their transverse spaces are transported by permutations of the specified frame vectors. Since $S$ is equivariant, the resulting horizontal right inverse is also equivariant.

For $m=4$, the validity inequality forces $r=0$. The scalar degree-$2k$ interpolation map from T062 applies directly, with no horizontal factor. For $k=1$, validity forces $r\le m-4$, exactly the nonexceptional range of T061's degree-two adjoint map. These two cases cover all endpoints excluded from the scalar regularity calculation.

The kernel remains the same ideal-sheaf section space as in T062. The flag projection and determinant pairing therefore give HE.2, with the unchanged jet representation FK.6–FK.11 and the unchanged parity twist. No equality of characters is substituted for this map argument.

## 4. Positive point deletion and complexity

The endpoint enumerator calls the same complete bounded-point routine with $a_0=2k$. For a nontrivial label its lowest numerator degree is at least $r+1$, so the available excess is at most $2k-1$. This is inside the previously proved $2k+1$ bound. The hook-plus-at-most-$k$-boxes argument still bounds the diagonal width by $k+1$.

For the invariant label, a nonzero correction forces $r\le k-1$, and the total degree is at most $3k-1$. Its coin and retained-subset enumeration is likewise within the earlier fixed-order bounds. The actual surjection proves that there are at least $d_{m,k,r}(\nu)$ complete points available for deletion.

The code selects those distinct complete points directly at the endpoint; it applies no parity transport. Each lies in a unique current cell. Replacing that cell by its first-differing-coordinate alternatives partitions its lattice points after removing exactly the selected point. Every replacement adds $2N_{\rm poly}-1$ cells. Thus the final number is exactly
$1+d(2N_{\rm poly}-1)$, including $d=0$.

The rational scalar right inverse is part of the proof of availability. The numerical evaluator and exported matrices do not construct that potentially large interpolation matrix. They use the already bounded LR correction and tableau/coin enumeration. Consequently the fixed-order construction and binary-degree bounds are inherited from T064 with smaller search ranges.

I checked the endpoint parameter validator, partition size, determinant conjugation, coefficient branch, direct base-point call, unique-owner deletion loop and full-range routing. The complete checker compares to independent standard-hook and jet traces and checks the literal exported cells; its saved receipt reports 5,366 coefficient/parity comparisons, 1,378 point-selection cases and 133 literal-polytope cases. Those are the author's executed checks, read here and not rerun.

## Audit classification

This is a complete independent proof/code reading plus a primary-source application check. It establishes the exact endpoint map and positive-cell construction. It is not an independent rerun of the saved finite certificate and does not claim a new scalar regularity theorem.
