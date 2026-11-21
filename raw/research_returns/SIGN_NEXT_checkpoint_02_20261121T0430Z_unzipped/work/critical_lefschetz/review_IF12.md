# Independent review of IF-12

Reviewer: GPT-6 Astra Pro, effort not exposed, agent `/root/critical_lefschetz`.

## Verdict and scope

**Approved after the explicit `Crv D cc δ` precision.** I read the complete proof in `genuine_theta_noncommutator.tex`, independently derived its principal identities and inequalities, and reread the final arithmetic paragraph after correction. Final checked SHA256: `508e10994d9f844ff5998664cbd052570f3dfa5fbdeef3877166ae29d9b7d21c`. This is a human proof and source review, not a Lean compilation. Supplied imported arithmetic theorems were used, not independently reproved.

## Independent proof checks

The first-arrow weights give height multiplicities `(1,3,3,3,3,3,2,10)`. The unique height-one factor makes the selected root coefficient equal to `J_f(P)` for `P=(Z11-Z22)Q`; the other factors are killed by the chosen raising operator. The determinant insertion commutes with the root action. The degree is 155. The normalized cyclic tensor convention contributes no omitted projector scalar.

I expanded the exact unitary translation of the Gaussian theta product. Completing the square gives the stated shifted Gaussian sum, including the positive Gaussian prefactor in z. The heat-operator identity has coefficient `-1/(8πT)`: differentiating the prefactor and dividing by `(2πi)^155` supplies this negative sign. Normal convergence justifies differentiation term by term. The 12-fold lattice refinement makes the translation commutator integral and retains the permitted semicharacter; the proof does not pretend that the translated characteristic is automatically permitted on the original lattice.

Independently, the diagonal evaluation is `P(a)=-4^-128 3^-28`. The degree, determinant coefficient bound, heat correction and lattice tail all agree. An independent exact-rational calculation verifies that the displayed coarse errors are strictly smaller than half the lower bound for the main term at `T=10^400`. In particular, `qD²=4612800<10^7`; the heat correction is less than `4·10^-258`, the tail is less than `5·10^-661`, while the main term has absolute value greater than `10^-156`.

For the universal orbit statement, after removing the scalar Gaussian factor the jet is a polynomial in the conjugate translation coordinates with holomorphic coefficients. Its top conjugate-homogeneous coefficient is the nonzero polynomial `P_d(-πC conjugate(x))` times `f0(x)`. A conjugate derivative of total order d isolates a nonzero constant times f0, so the function is not identically zero. The nonzero set is open, and prime-power lattice torsion is dense in the underlying real vector space. This proves existence of a torsion translate without a splitting assumption on f0. The eight-factor polynomial has the stated degree in each factor and remains nonzero.

## Arithmetic and source scope

The actual nonzero source vector uses `B.StdOK`; the algebraicity assertion additionally uses `Crv D cc δ`, with both of its arithmetic components explicitly stated. I checked the complete relevant displayed proofs of `thZero_ne_zero`, `thZero_mem`, and the source theta identity, and the exact hypotheses of `thZero_coefIn` and `ta_thMoved`. The final paragraph correctly uses `ta_thMoved` and `coefIn_translate` to establish the arithmetic property; `TA.transl` only transports an already established property.

The finite coefficient-field extension and clearing of denominators preserve the nonzero commutator, but do not assert an integral unit or a Smith-factor conclusion. The characteristic-kernel expansion is one-way: a nonzero individual translate need not survive its prescribed finite linear combination. The text preserves that distinction and makes no claim of a nonzero global period, a particular self-dual D7 datum, or automatic fixed-global-block invariance.
