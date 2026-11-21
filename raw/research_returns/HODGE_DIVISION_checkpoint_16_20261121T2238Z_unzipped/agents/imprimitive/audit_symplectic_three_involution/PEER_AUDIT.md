# Whole-proof audit of D-HOS-17–19

**PASS. No mathematical repair requested.** I read the entire frozen proof, all of the author's checker, the complete new primary-source passages and proofs, and the invoked interfaces with the previously checked HOS results. I also wrote and executed a separate exact reconstruction using a different classification method.

Auditor: `/root/imprimitive`, GPT-6 Astra Pro, effort inherited/not exposed, run `HODGE_DIVISION`. Whole review completed by **2026-11-21 21:43:28 UTC**. Independent computation completed at **21:42:42 UTC**, in **0.347798531 seconds**.

Frozen proof: `agents/g34_eightfolds/bireflection/higher_odd_symplectic_three_involution_section.tex`, SHA-256 `f976dad03ec875a46b3c25e39da81bd7af7240d6ffc2f0029e9343c61b2a8d46`. The adjacent bibliography and `check_higher_symplectic_three_involution.py` were read completely. The author file was not modified.

## D-HOS-17: all symmetric-form orbits

I checked the finite-field conversion with `t^2=-1` explicitly. The identity `B(Ax,y)=-B(x,Ay)` makes

\[
 H(x,y)=B(x,y)+tB(x,Ay)
\]

Hermitian and linear in its first argument. The inverse operation is the coefficient of1. The radicals coincide, so Hermitian rank r becomes symmetric rank2r. In a Hermitian orthonormal basis, the underlying symmetric form has matrix `I_(2r)`, determinant square, and orthogonal type `(-1)^r` over F3. Odd symmetric ranks and the opposite even-rank type therefore have no fixed forms.

The two nondegenerate-form counts were independently derived from the **full** GL, U and O orders. No special-unitary or projective-group order is substituted. Their ratio is

\[
 R_r=2\,3^{-r(r+1)/2}
 \frac{\prod_{j<r}(3^j+(-1)^j)}{\prod_{j\le r}(3^{2j-1}-1)}.
\]

It gives `R1=1/3`, `R2=1/351`, and the displayed successive-ratio formula is strictly less than1 for every positive r. Choosing the radical first gives the quotient of Gaussian binomial coefficients in the proof. It is at most1 because the F9-subspaces are a subset of the corresponding F3-subspaces. The rank-two special quotient simplifies to `2/[3(3^(N-1)-1)]`, with maximum1/39 at N=4. This proves the claimed universal orbit bound rather than merely its finite examples.

## D-HOS-18: actual representation support

I checked all signs in the Hermitian form

\[
 \mathcal H(x,y)=\langle x,hy\rangle-t\langle x,y\rangle.
\]

Symplecticity and `h^2=-I` make it nondegenerate Hermitian, linear in the first variable. Its two opposite maximal isotropic spaces give an h-stable symplectic summand of dimension2n for even n and2n−2 for odd n. The complementary summand in the latter case is one symplectic plane, so the subgroup S0 is exactly the pointwise-complement restriction subgroup to which the cited branching result applies.

The two opposite Siegel radicals generate S0. The supplied transvection argument handles both nonzero and zero pairings between the two isotropic components, and the previously checked elementary generation by symplectic transvections applies. Thus their invariant spaces have equal dimension v0 and intersection of dimension b=dim(V^S0), giving `v0<=(a+b)/2`.

For even n, b=0. For odd n≥5, the natural dimension of S0 is2n−2≥8. The exact published inequality gives

\[
 b/a<3^{8/3-(2n-2)/2}=3^{11/3-n}\le3^{-4/3}<1/4.
\]

The final strict inequality is equivalent to81>64. In particular no use is made of the unknown asymptotic constant from the first sentence of the published proposition.

The matrix-trace pairing on symmetric matrices is nondegenerate in characteristic3. Its contragredient congruence convention has the same fixed forms as the direct convention. The Levi GL acts transitively on each previously counted orbit, so weight multiplicities are constant there, even though V restricted to S0 need not be irreducible. At most1/39 of the nonzero weight-space dimension is fixed. The remaining weights form pairs under h, and each eigenvector is determined by one component of a pair. This argument works for either central character of V. It gives precisely the bounds19a/78 for even n and strictly greater than19a/104 for odd n.

## D-HOS-19: the exact necessary inertia condition

The nonselfdual compatible-normalizer statement is the already checked scalar-times-inner result; the class-inverting nonsquare diagonal outer class cannot stabilize the character. Projective support decreases under taking powers and is unchanged by a central sign. Thus the new result completes the projective-prime cases of order2, including the square-minus-one lift; the previous order3 and fixed-plane odd-prime cases retain their stated constants.

The contrapositive argument is correctly quantified. If an inertia does not have every residual property, it is either a nontrivial factor permutation, a nonidentity scalar, or has at least one nonscalar factor component with a prohibited prime-order power. Each of these gives the required moving-rank lower bound on the full tensor product. Spectrum convolution is used only for factor-preserving operators; the separate quarter bound treats permutations.

The actual multiplicity Euler formula, degree lower bound and pointed-intermediate-cover dimension imply genus0 and at least12 genuine inertia points for rank9. The resulting ceilings are9 for even n and156/5 for odd n, contradicting respectively27 and81. Therefore at least one inertia has only the asserted odd-prime, no-natural-±1 component powers. Its projective factor orders are coprime to6. The scalar part of the actual inertia remains unrestricted, exactly as the statement says. The argument does not prove that such a residual class or source exists, and it does not identify the inducing character field with the original quadratic field.

## Fresh primary-source verification

1. Larsen–Shalev–Tiep, *The Waring problem for finite simple groups*, Annals **174** (2011),1885–1950, DOI10.4007/annals.2011.174.3.10. Official full PDF: <https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n3-p10-p.pdf>. I freshly read the complete restriction-map definition and Proposition4.2.3 with its entire proof, printed pp.1909–1912, including the symplectic step4 and summation step6. I also viewed the original displayed estimate on p.1909 to confirm the exponent8/3−N/2. Its natural-dimension threshold is8 and its input is a nontrivial irreducible representation of the full simply connected ambient group. The exact embedded S0 satisfies all these hypotheses.
2. D. E. Taylor, *The Geometry of the Classical Groups*, Heldermann1992, corrected author text: <https://www.maths.usyd.edu.au/u/don/papers/gcg.pdf>. I freshly read the full invoked classification and order calculations on printed pp.115–118 and138–141, including the norm-surjectivity proof, Hermitian Witt decomposition, basis counts, anisotropic binary description and orthogonal order formulas. Local PDF SHA-256: `825201a4831659f957bf30156f04e85ab3746c01d942c670284071c68b41e30e`.

The published branching bound is used as a known result, not presented as a new theorem of this run. Earlier Vinroot, cover/outer, tensor-cycle, degree and Hurwitz interfaces were already independently whole-checked in the preceding HOS audits and were rechecked at their points of use here.

## Independent finite reconstruction

`independent_check.py` imports no author arithmetic or row selections. The author code had been read beforehand; this is not a blind audit.

For all27 symmetric forms in dimension2 and all59,049 in dimension4, I evaluate the quadratic polynomial on every vector. The exact quadratic Gauss-sum norm recovers the rank, and its sign recovers the discriminant. This avoids the author's symmetric congruence-elimination routine. Fixedness is checked by permuting the vector evaluations under A. Every rank/type count agrees with the full-group-order formula. In dimension4 the nonzero fixed counts are20 among780 rank-two forms and60 among21,060 rank-four forms, giving1/39 and1/351.

For dimension6, I solve the21-coordinate linear fixed-form equations directly over F3; the kernel has dimension9. I enumerate all19,683 forms in that kernel and again use exact Gauss sums to classify rank and discriminant. The Hermitian ranks0,1,2,3 have counts1,182,5460,14040, respectively. This does not use the author's Hermitian-block construction.

All arithmetic constants and source ceilings also pass. The complete output is `independent_checked.json`; there was no failed attempt in this independent reconstruction. These computations supplement the universal proof and do not replace the published restriction estimate or the all-rank orbit argument.
