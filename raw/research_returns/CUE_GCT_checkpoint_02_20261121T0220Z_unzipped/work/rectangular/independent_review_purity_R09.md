# Independent targeted review of R-09

Reviewer: GPT-6 Astra Pro, /root/purity_zero_status; effort not exposed. Run CUE_GCT-20261121-purity.

Read the complete R-09 statement and proof in work/rectangular/findings.tex, its cited tensor-subgroup projection, and the exact Bump–Gamburd ratios theorem (`t:1`, source lines1544–1563) in the supplied acp20.tex. This is a targeted whole-proof review, not a claim of formal verification or independent reproof of Bump–Gamburd.

## Outcome

The mathematical argument passes. One endpoint convention was requested: define S_0(n,d)=0, since the displayed monotonicity difference uses N−1 while the initial definition has N≥1. An explanatory sentence making the length cutoff explicit was also suggested. Both repairs have now been read in the revised statement and proof: S_0=0 is explicit, and the last paragraph explains g(λ,r,r)=0 for ℓ(λ)>n² through the vanishing Schur functor. The revised complete proof passes this targeted review.

## Checks

1. For t<1 the two Cauchy expansions converge absolutely and uniformly on the compact unitary factors. For example |s_lambda(U)|≤s_lambda(1^N), and comparison with the Cauchy identity at positive identity alphabets bounds the total absolute sum. Termwise integration is therefore justified.
2. The first expansion contributes t^{|lambda|}, and the second contributes t^{|mu|}. Since U is unitary, s_mu(U^{-1})=conjugate(s_mu(U)); orthogonality forces lambda=mu. Thus the surviving power is t^{2|lambda|}, not t^{|lambda|}.
3. Each pair of determinant twists is det(A)^{-d}det(B)^{-d}. Branching S_lambda(C^n tensor C^n) and Haar projection select both rectangular weights r=(d^n), hence |lambda|=nd and the coefficient g(lambda,r,r). There is no missing dual or conjugation on C,D: the inverse U already provided the character inner product, while each separate tensor pair is projected to its own determinant character.
4. The supplied Bump–Gamburd theorem explicitly assumes N≥Q,R, not N≥Q+R. Setting K=L=0, Q=R=n², and denominator parameters t times the eigenvalues of A tensor B and C tensor D gives exactly the determinant inverse on an n⁴-dimensional tensor product with t².
5. The Cauchy proof independently verifies the same stable expression. If length(lambda)>n², S_lambda(C^n tensor C^n)=0, so its rectangular branching multiplicity is zero. Hence stabilization at N=n² is valid also for the full symmetric-group norm.
6. The character of [r] tensor [r] is (chi^r)^2. Irreducible-character orthogonality gives sum_lambda g(lambda,r,r)^2 = (1/(nd)!)*sum_sigma chi^r(sigma)^4, using reality of symmetric-group characters. The factorial normalization is exact.
7. Monotonicity and the integer square-root upper bound follow directly from nonnegative integer squares. The projection is nonnegative after integration; the integrand is not claimed pointwise nonnegative. The text correctly preserves the orbit-ideal and symmetric-Kronecker distinctions elsewhere and does not turn this aggregate moment into a polynomial coefficient algorithm.
