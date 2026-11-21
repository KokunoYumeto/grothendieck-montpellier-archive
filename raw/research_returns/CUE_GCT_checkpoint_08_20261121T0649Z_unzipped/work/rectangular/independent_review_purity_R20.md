# Independent whole-proof review: R-20

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/purity_zero_status`; run `CUE_GCT-20261121-purity`.

Recorded event time: 2026-11-21T02:34:18Z.

Scope: complete reading of `r20_fragment.tex`, `staircase5_certificate.py`, `staircase5_certificate.json`, and `check_staircase5_local.py`. I also reread the base-character and geometric-product formulas in R-16. This review includes an independent derivation of the Fourier shifts, clearing estimates, root counts, and global independence argument, plus the limited exact computations described below. It is an independent agent proof review, not a formal certification or external peer review.

## Verdict: PASS

The proof establishes the uniform dimension bound

\[
\dim\mathcal P_{m,4}\ge 2m^2+2+8\left\lfloor\frac{m-97}{5}\right\rfloor(m-317)
\]

for every integer `m >= 8,000,001`. With the previously reviewed padding, invariant, and effective-degree results, this proves the claimed eventual rectangular range `m < n < 4m/3`. The argument uses one simultaneous pencil and one common nonzero deformation parameter.

## 1. Local identities and simultaneous supports

The five-row blocks at starts `5j` are disjoint. Every block's four interior rows have support only in its five designated columns, and its four interior columns have support only in its five designated rows. Adjacent blocks share only a boundary column; their off-diagonal entries do not enter another block's four interior columns. Consequently both row and column complementary-permanent factorizations hold with all blocks present.

I independently checked the general `4 x 5` identity, with independent symbols for every diagonal, superdiagonal, and remaining entry. SymPy's permanent and determinant routines gave zero constant and first-order difference for all five minors. Their second-order terms agreed exactly with the displayed `6,9,6` terms, including zero endpoint terms. This was a separate calculation from the author's explicit 24-permutation implementation.

Substituting the stated motif into those generic formulas reproduced all eight highest bidegree forms. Their `(z,w)` degrees were exactly `[4,5,4,3]` and `[2,3,4,4]`. The determinant cofactor relation has leading term `a_i E_i-b_i E_(i+1)` because its off-bidiagonal coefficients already carry one factor of the deformation parameter. All terms of lower bidegree remain in the full vector; the proof correctly postpones their treatment instead of projecting the actual differential image.

The outside factors at zero follow from the forced remaining cycle matching. The alignment choices `s=k+5-g` and `c=m+g-k` put the highest component in bidegree `(m-k,k)`, with every deleted index outside the local support in the stated range. Translation around the cycle preserves this property even when an external deletion wraps around.

## 2. Exact rational matrices and degree bounds

I recomputed the full stored certificate from its defining interpolation systems and compared the resulting JSON object with the supplied JSON; they were identical. I also used a separate elementary modular Gaussian elimination implementation on the displayed matrices. The row and column determinants are respectively `16` and `15` modulo `41`; the eight interpolation determinants are `[29,1,29,38]` and `[25,6,32,32]`.

The polynomial clearing bounds check independently. For the row basis, entries have `q` degree at most `a(a+1)/2`, adjugate entries at most `18`, and adjugate `K` degree at most `9`. Together with the local form's degree at most `20`, the substitutions and residual factors give the claimed cleared row bounds `105,12,9` in `(q,K,X)`. Negative `q` powers are covered by the factor `q^60`, and `X^5` covers the character powers.

For the column basis, multiplying each basis polynomial by `K^a` gives entry degrees at most `4a,a`, and adjugate degrees at most `36,9`. The equation for the coefficients gains the factor `K^a`. In the transformed coefficients, the total `K` degree is at most `9+a+(5-a)+j <= 17`; all additional `q` powers are nonpositive, and the conservative negative bound in the proof is sufficient. Thus the cleared bounds `116,17,5` hold. The two base columns satisfy the stated `31,4,0` bounds after multiplication by `q^25`.

Using the proof's common bounds `150,20,10` for each of four transformed columns gives `662,88,40` for either six-column determinant. Multiplying both determinants and all eight interpolation determinants gives the sharper aggregate bounds `1708,272,80`, hence the rounded `2000,300,80` bounds. The clearing is by monomials and polynomial determinants, so the resulting expression is an integer polynomial. At the certificate point, the product of the eight interpolation determinants is `20`; the displayed value of the combined polynomial is indeed `22` modulo `41`. This proves that it is nonzero as a polynomial, rather than making an extrapolation from numerical Jacobian ranks.

## 3. Fourier normalization and joint independence

For the row form, the outside `(x,y)` factor together with the `j`th basis polynomial completes exactly `A(x,q^j y)`. Dividing its `y^r` coefficient by `A_r` yields `X^j q^(-js)` because `r+s=t`. Shifting the remaining `(z,w)` factors by `q^(-j)` produces roots `5-j` through `k+a-1-j`. Their common part is exactly `H_R`, with the two residual root intervals used in the row transform.

For the column form, the corresponding completion is `A(x,q^(5-k-j)y)`. Multiplication by the nonzero character scalar `X^(k-5)` leaves the factor `X^(-j) q^((k-5+j)s)`. The shifted outside roots run from `-a+j` through `k-6+j`; their common part and residual intervals agree exactly with the column transform. Thus both matrices represent the required character spaces. The range for `t` excludes the second congruence possibility `r+s=t+m`.

After dividing out the common factor `H`, the row and column spaces are the multiples of two degree-four binary forms with disjoint roots, each by all binary quintics. Their intersection is their product times the binary linear forms, exactly the two-dimensional old base space. Their sum has dimension ten and fills all binary forms of degree nine. This checks joint independence; the separate six-column determinants alone would not imply it.

The allowed coefficient interval contains ten consecutive indices because `k,t` both lie between `9` and `m-9`. The multiplication determinant is the stated ten-by-ten Toeplitz determinant. In its Schur specialization there are `N=k-9` consecutive geometric variables, with alternant exponents at most `N+9=k<m`; their powers of the primitive root are distinct. The Vandermonde argument is therefore valid. When `N=0`, the resulting coefficient matrix is the identity. All eight classes remain independent after restriction modulo the entire old character space.

## 4. Uniform mode count and one global rank increase

The proof correctly uses the number of primitive roots rather than replacing it by `m`. The elementary factorization gives `phi(m)^2/m >= 1/2`; for `m >= 8,000,001`, it follows that `phi(m)>2000`. A nonzero coefficient polynomial in `q` of degree at most `2000` therefore survives at some primitive root. For this root, at most `300` values `q^k` make the polynomial identically zero in `X`. This leaves at least `m-317` good bidegrees. Each has at most `80` bad character values, leaving at least `m-97` good characters.

At starts `5j`, the Fourier factors are `(q^(5t))^j`. Each value has at most `gcd(5,m) <= 5` preimages, so the good characters supply at least `floor((m-97)/5)` distinct values. The associated ordinary Vandermonde systems imply independent translated normal classes for all eight families in each good bidegree.

For the full, not necessarily bihomogeneous limits, taking the largest bidegree in a relation and descending is valid because every omitted local component has strictly smaller `(z,w)` degree and the old space is bigraded. This proves independence of the full limits modulo the old space. Finally, each family divided by the second power of the deformation parameter is polynomial and lies in the actual differential image at every nonzero parameter. An augmented minor nonzero at zero stays nonzero at a common generic nonzero parameter. This establishes the claimed simultaneous rank increase at one pencil.

## 5. Padding range

The integer bound `floor((m-97)/5) >= (m-101)/5` is correct. Its substitution yields exactly the displayed quadratic difference from `32m^2/9`, and the nonconstant part is positive for `m>15048`. Thus the much larger uniform threshold suffices for every `m<n<4m/3`. The leading coefficient is `18/5`, giving the asymptotic general dimension ratio `3/sqrt(5)`. The prior G-12 exclusion correctly forces the additional gaps above `4/3` to be nonrectangular.

No further revisions are requested. The finite computations verify the local algebraic certificate only; the root-count and degree argument is what makes the result uniform in `m`.
