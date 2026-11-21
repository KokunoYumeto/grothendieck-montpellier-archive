# Independent whole-proof review: I-27

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/purity_zero_status`; run `CUE_GCT-20261121-purity`.

Recorded event time: 2026-11-21T02:30:12Z.

Scope: I read the complete written proof in `I27_filtered_codes.tex`, including the exact filtering equivalence, the common-family collision, the width-two witness, and the magnitude and scope paragraphs. This is an independent agent proof reading and elementary rederivation of the displayed arguments, not a formal proof certificate or external peer review. I did not rerun matrix computations because the matrix witness follows directly from `E_12^2=0`.

## Verdict: PASS

The base-six uniqueness argument is exact: each exchange deficit is an integer in `[-2,2]`; a largest nonzero active term of magnitude at least `6^h` cannot be canceled by the lower terms, whose total absolute value is at most `2(6^h-1)/5`. Applying this separately to every exchange and both pairings proves that every active bit is coherent. The converse follows by summing exchange equalities. This is an equality of formal integer exponents, so the argument has no coefficient-characteristic exception.

I rechecked the binary additive-function classification used from I-23. On fixed-size subsets with `2 <= r <= w-2`, a nonconstant binary additive function is membership of one element or its complement. If at least two elements occupied each of two distinct additive levels, varying a subset would give at least three values; the stated range excludes that case. Thus the set `T` of elements tested by active nonconstant bits has size at most the number of bit positions. When `ell <= w-2`, two elements `u,v` remain outside `T`, and all coherent seeds assign equal weights to the two subsets obtained by exchanging them. A common `(r-1)`-subset disjoint from `u,v` exists in the stated range.

The equality of the induced ground weights `a_{s,u}=a_{s,v}` follows by subtracting the two subset sums and is independent of the common gauge. Therefore `X_u-X_v` vanishes under every induced monomial substitution, after any common scalar shift, and after a common exponent offset or a per-seed common rescaling. The polynomial remains nonzero in characteristic two. Its displayed width-two representation is exact: multiplication leaves the coefficient `(X_u-X_v)E_12`, since `E_12^2=0`; all factors have determinant one.

The raw magnitude conclusion is correctly scoped. Distinguishing all fixed-size subsets requires testing at least `w-1` ground elements, hence using at least that many distinct nonconstant bit positions. One corresponding power of six is at least `6^(w-2)`, and a seed activating that bit together with a codeword where it equals one gives at least this raw nonnegative weight. The proof expressly does not promote this into a rescaling-invariant degree lower bound.

The closing qualification is also necessary and correct: a dense SV direction destroys this particular linear witness because distinct Lagrange basis polynomials have nonzero difference. Thus I-27 does not claim a dense-generator lower bound or rule out arbitrary nonlinear decoders.
