# HD-AST07–09 independent whole-proof audit

Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, inherited effort not exposed, HODGE_DIVISION. **Result: PASS.** I read the complete frozen proof, every line of the root checker, and the final complete actual output. I did not contribute to the new Cauchy/grid-index derivation before receiving this proof. The root and `/root/imprimitive` contributions remain attributed as stated in its authorship paragraph.

Reviewed proof: `research/alternating_standard_two_factor_section.tex`, SHA-256 `32b5cc512a130b41b5d6f3d8e0d4f2d5fa02e3714ce9d6ba6d6b89d5a4163108`. Reviewed root checker: `research/check_standard_two_factor.py`, SHA-256 `8b46b34e0002f5083a629ff59bb0d82173643b8c2577a074725777cdd35efa77`. The final root execution was 2026-11-21 22:50:10.834636 UTC, 6.773588782 seconds. Its 160,926 partition pairs, 7,886,278 spectral entries and 4,000 weighted swaps are the root's execution, not my own.

## Uniform tensor index estimate

I independently checked the full proof of AST2.1 for every target eigenvalue. On a letter module, every eigenvalue multiplicity is at most the number of cycles, and the sum of multiplicities is `n`. Deleting the trivial line changes the squared-multiplicity sum by exactly `-2c+1`, since the one-eigenspace has dimension `c`. This gives `(n-2)c+1`. Cauchy–Schwarz on a common cyclic eigenvalue group, followed by the arithmetic–geometric mean inequality, gives the baseline support `(n-2)k/2`. The common cyclic group merely pads zero entries and introduces no multiplicity or field assumption.

For `k>=n`, the baseline already exceeds the required `((n-3)k+n)/2`. For `1<=k<n`, a nonreal eigenspace has its distinct complex conjugate with the same multiplicity because the actual tensor operator is rational. Its support is at least `e/2`, greater than the desired bound, whose value at `k=n` is `(e-1)/2`. An absent target has full support. Thus the remaining real-target case split is exhaustive.

At target one, the grid-cycle count is `sum gcd(l_i,m_j)`. Deleting the two trivial lines and restoring their intersection gives exactly `C-c-d+1`. The support excess over the baseline is the nonnegative quantity `G`. The fixed-point/nontrivial-cycle terms contribute `(f_y k_x+f_x k_y)/2`. The inequalities `f_x>=n-2k_x`, `f_y>=n-2k_y` remain valid even when their right sides are negative because they are multiplied by nonnegative indices. The next step is exactly `4k_xk_y<=k^2`. Thus `G>=k(n-k)/2>=(n-k)/2`, supplying the missing margin.

At target minus one, a grid cycle is even precisely when at least one of its constituent cycles is even. The subtraction of the two letter modules gives the printed multiplicity without an added trivial-line term. Therefore the support excess is `H-u-v+1`. Odd–odd pairs contribute at least one to `H`; odd–even pairs contribute at least one half because their numerator is a positive odd integer; even–even pairs contribute nonnegatively. This proves AST2.9.

I checked each endpoint of its subsequent case split. If both cycle counts are at least three, their coefficients in AST2.9 are at least one and `u+v>=2(c+d-n)=2L`, giving at least `1+L`. If the smaller count is two, both coefficients are nonnegative and `0<L<=2`, so the constant one suffices. If the smaller count is one, `L>0` forces the other to be `n`: an `n`-cycle paired with the identity. Its deleted minus-one multiplicity is zero or one, and the tensor support is at least `a(a-1)`, exceeding the required baseline margin. These cases include both parities and exhaust all positive cycle counts. No numerical scan is used to infer the universal inequality.

## Weighted swaps and the actual scalar projection

I reread the complete uniqueness/normalizer portion of HD-AST04. Its conclusion uses the ordinary rational tensor-wreath realization, irreducibility of the represented core, `Aut(A_n)=S_n` in the stated range, and trivial centralizer of `A_n` in `S_n`. Its scalar intersection is trivial, so scalar-forgetting is an actual homomorphism. This part requires no conductor condition and is correctly reused for every original field.

The weighted-swap formula is the already reviewed exact word formula, now applied to the standard representation. A constant eigenbasis word contributes its eigenvalue, and a nonconstant unordered pair contributes the two square roots of the product. The resulting multiplicity is `(N_z+d_+-d_-)/2`, bounded by `(a(a-nu(Uh))+a)/2`. Thus the first support bound is `(e-a)/2` for every scalar. Every full-letter eigenspace of `h` has dimension at most its cycle count; deletion cannot increase it, giving `nu(Uh)>=ind(h)-1`. This weaker bound is valid even at the identity, and gives the second weighted-swap bound without any scalar-order hypothesis.

The rational wreath action on two blocks is faithful and transitive: the ordinary core is transitive in each block, and a swap joins the blocks. A length-`l` cycle of the actual cycle product gives a length-`2l` cycle on the letters. Hence the claimed permutation index is exact, not a representation-dimension analogy.

## Actual source contradiction and field scope

The proof retains the previously established intermediate-cover/period factorization. The inducing multiplicity is six, so genus at least two is impossible at the given degree; genus one has at most six genuine marks and cannot have period rank nine. The connected genus-zero cover therefore has a generating product-one tuple with `r>=12` and actual moving-rank sum `2e+6`. This argument does not identify an inducing character field with the original field and does not infer dominance from an abstract branch profile.

Every genuine inertia moves at least `a` dimensions. A nonidentity within-factor permutation acts nonscalarly on the standard module, so its projective support is at least one; tensor convolution multiplies this by `a`. A genuine scalar moves everything. A swap satisfies the same bound because `(e-a)/2>=a`. The swap count is positive and even. Four swaps plus eight further genuine marks exceed `2e+6`, so there are exactly two. No arithmetic scalar marks are used.

For every non-swap, AST2.1 gives `AI+B`; when both permutations are the identity, genuine scalar inertia still satisfies it since `I=0` and `e>=B`. The two swaps contribute `e+(a/2)H-2a`. Taking a letter stabilizer in the actual connected cover gives the actual degree-`2n` quotient. Riemann–Hurwitz gives `N+H>=2n-2`, after subtracting the two base swap indices. Scalar marks have zero quotient index and remain in the coefficient moving-rank sum.

Since `a/2-A=1` and `H>=0`, the summed lower bound is at least `2e+a+5`, strictly greater than `2e+6`. I checked the identity and every inequality direction. The theorem therefore excludes exactly the stated transitive two-standard-factor source for all original imaginary quadratic fields, including the Eisenstein field. It does not require a non-Eisenstein premise borrowed from the adjacent scalar-conductor section.

The `n=100`, Gaussian two-factor numerical profile satisfies the older necessary gates but violates this new obstruction; the text appropriately makes no prior existence claim. Larger tensor counts and other core configurations are not silently included in this theorem.

## Independent exact reconstruction

Files: `audit_standard_two_factor.py` and `audit_standard_two_factor.json`. The full root code was read before this implementation was written. No author code, output, grid-cycle table or selected row is imported. My program obtains the deleted-letter spectra and convolves them directly, rather than using the root program's grid-cycle subtraction. It also constructs actual rational standard matrices in the basis `e_i-e_n`, forms their tensor-swap matrices, factors their exact characteristic polynomials, and derives eigenvalue multiplicities from those factors.

Actual successful execution: **2026-11-21 22:55:22.433180 UTC**, **13.119050608 seconds**. It passed:

- All **160,926** nonidentity partition pairs for `15<=n<=18`, with **7,886,278** convolution spectral entries and **46,237** low-index real-target checks.
- **60** actual rational deleted-basis weighted-swap matrices, of degrees 9 through 49, with their exact square identities and characteristic-polynomial multiplicities.
- **616** actual two-block quotient permutations, checking doubled cycle lengths and the index formula.
- Four universal symbolic endpoint identities and positivity checks.

The independently obtained minimum twice-gaps are `1,0,1,0` for `n=15,16,17,18`, agreeing with the root output. The first run passed; there was no failed certificate assertion or repair. This is a finite supplement, not an extrapolation to arbitrary `n`, a tuple enumeration, or a replacement for the actual-cover proof.

## Sources, status and boundary

The new Cauchy and cycle-count estimates are proved entirely in the frozen section. The exact ordinary-normalizer and intermediate-cover inputs are previously reviewed results; I reread their invoked scalar-projection and field-scope passages here. The weighted-swap input is the fully reviewed D-ATT05 proof, whose universal dimension scope is correct. No new external classification, Markman, Severn or032 theorem is introduced. No fresh reconstruction of `Aut(A_n)` classification or the earlier polarized Shapiro theorem is claimed by this audit.

The complete proof, author code and final output pass without repair. There is no TeX compilation claim. The independent result is a whole-proof/source-interface/code audit, separate from the root and sibling contributions to the new derivation.
