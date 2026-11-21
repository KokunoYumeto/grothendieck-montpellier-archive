# Independent targeted whole-proof review: I-14–I-18

Reviewer: GPT-6 Astra Pro, `/root/purity_zero_status`; effort not exposed. Run CUE_GCT-20261121-purity.

Read every statement, proof, counterexample, and scope paragraph for I-14 through I-18 in `work/isolation/findings.tex`. This is an independent-agent targeted proof review, not a claim of formal verification, complete literature verification, or a new execution of all examples.

## Outcome

All five arguments pass. One scope precision was requested in I-18's final paragraph and has been applied and reread: the sampled values generating an ideal inside εR are from **fixed F-valued samples**. Arbitrary K-valued coordinates with poles would not admit the claimed specialization. The general matrix assertion already imposed an integral compression and was correct.

## I-14: joint coefficient compression

The coefficient grouping matrix P has the correct orientation: a column of CP is the sum of original coefficients at one selected weight. Full row rank is equivalent to injectivity of Pᵀ on im(Cᵀ), because Cᵀ is injective. The dual-functional quantifier is over all nonzero functionals on V=span coefficients, so no spurious ambient annihilators occur.

Cauchy–Binet gives exactly the displayed signed linear forms in the Plücker coordinates, one for each r-column subset T. Consequently the rank-failure locus is a linear section of the Grassmannian in its Plücker embedding. The proof does not replace values of the minors by their zero/nonzero matroid pattern.

Both examples were checked algebraically. The substitutions of e₁(x₁−x₂)+e₂(x₂−x₃) give respectively (1−t)e₂ and (t−1)e₁, so individual rank is one while joint rank is two. Rows (1,1) and (1,−1) have the same matroid and different compressed values when characteristic is not two, as stipulated. The nonnegative-weight degree bound nδB and subsequent root-count test are exact.

## I-15: bounded affine seed decoding

The pigeonhole map has k+1 integer coordinates, each in [−nM,nM], giving the precise threshold 2ⁿ>(2nM+1)^(k+1). Equal images imply equality of the two integer monomial weights for every seed, not just for Boolean seeds. The binomial is formally nonzero also in characteristic two. The diagonal two-state ROABP representation works in every variable order.

For the more general span assertion, a rational basis can indeed be selected from the bounded integer weight vectors themselves. Equality of Boolean-exponent dot products on that basis forces equality on the entire family. Taking logarithms gives k≥n/log₂(2nB+1). Fixed-degree polynomial functions of O(log n) Boolean bits span at most the number of their multilinear seed monomials; that is eventually below the required Ω(n/log n) dimension for polynomial B.

The application to the stated Hoza formula uses only its actual linear dependence on the common seed bits. The direct alphabet decoder assigns the same layer factor to layers 1 and 3, so x₁−x₃ is an exact obstruction. The text correctly leaves nonlinear decoders with sufficient output span and unbounded weights outside its conclusion.

## I-16: row states and finite-field hitting

The final row-state scalar is exactly the coefficient uᵀA₁,a₁⋯Aₙ,aₙv. Thus cancellation is already incorporated, unlike an unsigned support graph. There are at most qʷ row states. Subdividing by the pair (current state, letter) removes parallel edges while preserving word-labelled paths; the width (δ+1)qʷ and length 2n+1 are correct. The construction remains coefficient dependent and can cost exponentially in w.

The hitting lower bound counts binomial(q,δ)ⁿ distinct products of monic root-set factors. Each point hits exactly binomial(q−1,δ)ⁿ of them. The covering inequality therefore gives (q/(q−δ))ⁿ without a probabilistic independence assumption on the hitting set. The endpoint δ=q−1 forces all qⁿ points, and the full-grid interpolation proof supplies sufficiency. The δ≥q polynomial x₁^q−x₁ is an appropriate formally nonzero obstruction. The base-field versus extension-field distinction is retained.

## I-17: invertible-factor sampling

The common shift a exists because the product of the determinant polynomials is nonzero of degree at most nwδ. With Pᵢ=A₁(a)⋯Aᵢ(a), the displayed Mᵢ=Pᵢ₋₁Aᵢ(a+y)Pᵢ⁻¹ has constant term I, and multiplication telescopes in the stated order.

The row spaces are nested. In the induction, a previously retained coefficient row remains an actual coefficient after multiplying by the next constant I. New rows are spanned by retained basis rows multiplied by nonconstant coefficients of Mᵢ. Because the variables are disjoint, each such product remains an actual coefficient row and adds at most one variable to its support. A dimension increase supplies the inequality dᵢ₋₁≤dᵢ−1. This proves the support bound without assuming commutativity of matrix coefficients.

A scalar projection nonzero on the complete row space is nonzero on some retained basis row. Setting all other shifted variables to zero preserves that coefficient. Root counting on a (δ+1)-element grid then gives the promised point. The sample family is permutation invariant and its count uses exactly δ nonzero choices per selected coordinate. The nilpotent-chain example shows sharpness of the support bound for this row-space argument. No claim is made that it solves the singular-factor class.

## I-18: generic rank versus the special fiber

The matrix product L(x)R(y) equals diag(y−x,0), so the displayed pairs compute the product of disjoint differences in every characteristic. A perturbation of support less than m leaves at least one pair unchanged and forces vanishing.

Adding εI makes each factor generically invertible. At zero, the displayed triangular pair has first diagonal entry ε(1+ε); the mth power therefore has (1,1)-entry εᵐ(1+ε)ᵐ. This is nonzero in K while all original restricted samples vanish after specialization.

Over the DVR R, nonzero maximal minors characterize generic rank; unit maximal minors characterize rank of the reduction. A unit minor gives a surjective map onto Rʳ, and surjectivity gives a full-rank reduction and hence a unit minor. These are exact equivalences. The coefficient module of the scalar regularization is R because its special fiber contains a nonzero coefficient, while the fixed-sample image is a nonzero ideal inside εR. Saturation therefore loses the valuation information needed to certify a nonzero evaluation of the original polynomial. The repaired wording excludes Laurent-series sample poles and makes this argument precise.
