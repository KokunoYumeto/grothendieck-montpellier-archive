# A067 — complete third-order fixed-twist proof and independent certificate audit

Reviewed by GPT-6 Astra Pro, effort setting not exposed, run `/root/archive_audit`, on 2026-11-21 UTC. I read the full G032 report, FT.1–FT.10 and §§5–7, and the complete implementations `fixed_twist_arrangement.py`, `third_power_fixed_twist_certificate.py`, and `third_power_fixed_twist_positive.py`. **PASS after the explicit prefix-product bound repair described below.** The mathematical formulas did not change.

The independent exhaustive reconstruction passed **all 1,552,320 constants**. All **189 label-array hashes**, extrema, positive-order minima, active orders, and exact zero sets match the saved certificate. This independent implementation imports no root Python module. It uses unexpanded normal monomials, literal Weyl shifts, closed complete-character formulas, independently reconstructed symmetric-group characters, and Python unbounded integers for every trace product, character sum, and finite difference.

## 1. Partition parameters and actual module maps

For \(a=b+x\), the three-row parameter is
\[
\alpha=(a+c,b+c,c),\qquad |\alpha|=2b+x+3c.
\]
Substitution into FA.5 gives literally
\[
\lambda_2-\lambda_5=a+c,\quad
\lambda_2-\lambda_4=b+c,\quad
\lambda_2-\lambda_3=c,\quad
\lambda_2-n=3.
\]
Moreover \(\lambda_1-\lambda_2=|\alpha|-15\), so FT.1 is a partition exactly under its displayed inequality, and FA.4 applies in the required degree. All other consecutive differences are \(c,b,x,d\) as specified.

The sign in FA.6 is \(\operatorname{sgn}^{\lambda_2}=\operatorname{sgn}^{d+a+c}\). Independently, the actual determinant-column pairing gives
\[
S_\alpha Q=(\det Q)^c\otimes S_{(a,b)}Q,\qquad
\det Q=\det E\otimes\mathcal O(1).
\]
Since \(\det E=\operatorname{sgn}\), this gives FT.3's sign \(\operatorname{sgn}^c\); its product with FT.2's sign is \(\operatorname{sgn}^{d+a}\), as required by the earlier sheaf convention. The coefficient formula correctly uses the former sign when applied directly to the arrangement module \(M\). The evaluator uses \(d+b+x+c\), which is the same exponent.

The quotient substitution, Schur extraction, and inverse balanced homogenization are the actual maps established in G027 and T049. I reread FA.1–FA.9 and its parameter formulas for this application. No dimension-only replacement is used here.

## 2. Rank-three normal extraction and orientation

The product FT.5 is the literal cyclic trace of the truncated row space \(\mathbf Q\oplus F\oplus\operatorname{Sym}^2F\). Multiplication by the rank-three Vandermonde gives FT.6 with the shifts \(\rho+\delta-\sigma\delta\). The expansion includes negative Schur coefficients; none may be dropped merely because a particular monomial is absent.

I independently verified all seven saved expansions by enumerating semistandard tableaux of each listed three-row shape and reconstructing the entire normal polynomial coefficient by coefficient. This uses the monomial definition of a Schur polynomial, not the saved six-shift extraction. In particular the displayed three-cycle expansion, including its negative \(s_{21},s_{321},s_{51}\) terms, is correct.

For a stable selected subset, the quotient variables split into the stated normal factors and the standard module on its complement. Skew Cauchy coefficient extraction on the latter gives the three-by-three determinant
\[
\det\bigl(h_\gamma(\alpha_i-\rho_j-i+j)\bigr).
\]
The containment condition is correct, including rank-deficient complementary standard modules. The skew Jacobi–Trudi source locator is the already read Macdonald I§5(5.3)–(5.4), p.70, with (5.7), p.71; this review does not claim another primary-source read.

The orientation of a selected \(s\)-set is \((-1)^{s-\#\text{cycles}}\). Combining it with complex degree \((-1)^s\) gives exactly \((-1)^{\#\text{cycles}}\). Terms on four selected rows have maximum degree eight, and the final all-normal term has maximum degree ten. They vanish at \(N\ge15\). Thus FT.7 is the trace of the actual exact restriction complex in every stated input.

## 3. Exact polynomial domains and degree bounds

For the empty selected subset and identity permutation, the Weyl dimension product is precisely
\[
\frac{(x+1)(b+x+2)(b+x+c+3)(b+1)(b+c+2)(c+1)}{12}.
\]
Its total degree is five and its separate degrees in \(x,b\) are three and four.

After expansion along the fixed third row, all other terms are combinations of two-by-two determinants. On every fixed residue class, the quadratic leading coefficient of a complete trace on a three-dimensional identity standard module, or on the transposition class of the four-dimensional standard module, is independent of the shift. Their degree-four products therefore cancel. This proves the stated total-degree-three bound in those cases. Other nonidentity classes have at most linear complete traces. For a two-element selection the identity complete traces are linear with identical leading coefficients, so their degree-two products cancel; nonidentity complementary traces are periodic. For three selected elements the complement is a line, so its nonnegative-index traces are periodic. These give every total and separate bound used in FT.9.

The generating functions are proper rational functions whose poles have orders dividing sixty. Their partial fractions give the residue polynomials from every nonnegative index, with no further initial correction.

In the bulk \(b\ge8\), \(\rho_1\le6\) makes every first-two-row index nonnegative. In fact the least potentially restrictive second-row index is \(b+c-\rho_1-1\ge1\). Both varying containment tests are automatic; the third-row values and containment are fixed by \(c\).

For each of the 24 boundary branches, \(x=X+q_{b,c}\) enforces exactly the partition condition. The least possible \(b+x+c\) is seven. Thus every first-row index is nonnegative and first-row containment is automatic from the branch origin. All remaining negative-index conventions and containment tests are constant in \(X\). This proves the degree-three residue polynomial on the entire boundary half-line, including the branches with \(q=0\).

The 17 possible nonzero bulk orders are precisely the pairs with \(i\le3\), \(j\le4\), \(i+j\le5\). The three excluded pairs are \((2,4),(3,3),(3,4)\).

## 4. Independent exhaustive reconstruction

The independent script is `check_third_power_fixed_twist_independent.py`. Its computational path is:

1. Enumerate selected unions of the actual cycles, retaining multiplicities of equal-length cycles and the orientation sign.
2. Multiply the unexpanded three-variable truncated normal factors.
3. Apply the six Weyl shifts directly to those monomials. No normal Schur decomposition or skew determinant is used in the trace computation.
4. Evaluate the complementary complete traces by closed formulas for every partition of sizes two through five. For example the five-row classes give \(\binom{n+3}{3}\), \((\lfloor n/2\rfloor+1)(\lceil n/2\rceil+1)\), the even-index function \(n/2+1\), \(\lfloor n/3\rfloor+1\), and the respective six-, four-, and five-periodic functions. Negative indices are zero.
5. Reconstruct the seven \(S_5\) character rows from the literal Frobenius power-sum alternant in five variables and verify their weighted orthogonality.
6. Evaluate the integer traces and multiplicities with Python unbounded integers, then use successive finite differences rather than the certificate's binomial-sum implementation.

The trace, character, and finite-difference arrays have object dtype, so their additions and multiplications have no int64 overflow. The short closed complete formulas use bounded indices at most 550; their elementary intermediate products are independently below \(553^3\). Conversion to little-endian int64 occurs only for the final nonnegative constant arrays after their range is checked, so the saved array hashes use the same byte format as the supplied receipt.

All three sets of 504,000 bulk constants and all 24 sets of 1,680 boundary constants agree exactly. The maximum fixed constant is **1,453,555,800**, and the smallest positive-order constant across all branches is **258**. The maximum absolute class trace encountered by this independent reconstruction is **1,734,367,047,840**.

The receipt is `THIRD_POWER_FIXED_TWIST_INDEPENDENT_RECEIPT.json`. It records the input hash, all reconstructed array hashes, minima, maxima, zero sets, character rows, and method.

### The repaired arithmetic-bound detail

The original vectorized implementation checked the full product of three factor maxima. A zero third factor made that bound zero without itself bounding the earlier two-factor product. The actual indices here keep that earlier product safely inside int64, but the stated operation-by-operation argument needed the missing prefix check.

I reported this point. The root added an assertion immediately after each factor is multiplied into the running maximum product. I reread the saved correction. Together with the existing accumulated absolute term bound, character-sum bound, and \(2^7\) or \(2^3\) difference bounds, it now bounds every multiplication and partial sum actually executed. The saved maximum trace-operation bound is **4,176,326,138,215,440**, below \(2^{63}\). The independent unbounded-integer reconstruction verifies the numerical result without relying on this bound.

## 5. Literal positive counts, support, and evaluator transport

Newton interpolation is exact by §3. The exhaustive computation proves the nonnegative constants, with every allowed positive-order constant strictly positive. The two-chain construction in FT.10 therefore gives the exact count: two fixed quotient variables, one coefficient-interval variable, and at most five chain variables, hence at most eight variables. The boundary version has at most five. The constraints define bounded integer sets; omitted zero constants give no points.

The printed support table was parsed and compared with the certificate. All **51 nonempty boundary rows**, comprising **101 boundary zeros**, agree, including every shift \(q_{b,c}\). The bulk has exactly the two recorded zeros. Since the first positive differences are strictly positive, these are finite points, not periodic families.

A separate independent continuation test covers every one of the **27 branches** at parameters beyond the interpolation grids. It checks both determinant parities and all seven labels: **378 coefficients**, **2,038 literal polytope matrices**, and **1,134 actual witness tuples** pass. The matrix check verifies the quotient equalities, nonnegative coefficient interval, every strict-chain difference inequality, the variable bounds, and the sum of the resulting binomial counts. The receipt is `THIRD_POWER_FIXED_TWIST_EVALUATOR_RECEIPT.json`; the script is `check_third_power_fixed_twist_evaluator.py`.

## 6. Coverage and exact complement

The disjoint twists \(c=0,1,2\) here, \(c=3\) from T051, \(c=4\) from T050, \(c=5\) from T045, and \(c\ge6\) from G021 cover every third-order input. The previously proved first and second orders supply the other two orders. At order zero, the exact stable chart and multiplication by \(u^{n-\lambda_2}\) transport the component with row degree \(\lambda_2\) to the original one.

For the complementary partition, the exterior-column pairing is an actual perfect map into \((\det\mathbf Q^5)^H\). On balanced weights it pairs row degree \(n\) with \(H-n\), with symmetric-group character \(\operatorname{sgn}^H\). The complementary order is literally
\[
\max(0,(H-\lambda_4)-(H-n))=\max(0,n-\lambda_4).
\]
This proves the claimed complementary coverage and its label transpose. The scheme, sheaf, and exact-class dictionary is applied to the specified quotient, restriction, and projector maps, within the previously checked locator scopes. No unproved cohomology rank or coefficient oracle is used by the fixed formulas.

