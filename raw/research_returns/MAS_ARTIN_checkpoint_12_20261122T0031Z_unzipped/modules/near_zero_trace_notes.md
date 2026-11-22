# Uniform actual control at logarithmic zero

MA-NZ001 and MA-NZ002 are proved in `near_zero_trace.tex`. The module addresses the precise gap between compact tests supported away from0 and the source's complete class of smooth compact tests satisfyingg(0)=0. A formal positive/negative splitting is not used.

## The actual estimate

For every fixed smooth compactg withg(0)=0 and a cutoffchi equal to1 near0, putr_epsilon(t)=g(t)chi(t/epsilon). The theorem proves sup_(c<=0)||C_r_epsilon P_Zc||_1→0 in the same actual physical weighted Hilbert space, for every polynomial weights>=0. It applies to the rational and both requested character families because GW supplies their actual retained jets and exact closed-kernel assertion.

## Why a second resolvent power now suffices

The actual physical positive shifts satisfy ||U_t||<=exp(omega t), omega=alpha+s/4, uniformly in the half-line endpointc. The quotient and its adjoint inherit this bound. For a fixednu>omega, the actual adjoint resolventR_c therefore satisfies both inequalities (nu−omega)R_c*R_c<=ReR_c and (nu−omega)R_cR_c*<=ReR_c.

The exact GW kernel theorem gives density of the actual adjoint polynomial-exponential jet representatives inZ_c. Finite orthogonal projections onto their invariant spans compute the real-part resolvent trace as a positive sum ofr/(nu−lambda). Its real parts decay quadratically in height, so the fixed-function local count proves summability. Positivity then givesReR_c inS1, R_c inS2 and uniform left and right HS tails. ConsequentlyR_c² has a uniform finite-block S1 approximation. This is stronger than using a high resolvent power from the coarse contour estimates and is the reason only two derivatives of the shrinking test are needed.

The positivity here is ordinary Hilbert-space quasidissipativity. It is not an arithmetic positivity form or a zero-location premise.

## Finite blocks without a changing-norm constant

An elementary unitary triangularization puts a finite invariant generator block into upper triangular form. Positivity ofomegaI−ReB bounds every upper entry by twice the geometric mean of the corresponding diagonal deficits. The eigenvalue heights, real parts and dimension are fixed, so the generator norm is bounded uniformly inc without a zero-separation or basis-condition constant.

This supplies a weightedH1 bound and a uniformly normalized endpoint trace. For a block vector extended by zero to the whole line, translation by t differs byO_T(sqrt|t|): the interior givesO_T(|t|), while the moving endpoint jump contributes the square-root term. This explicit jump estimate is retained.

## Bulk and boundary calculations

The physical adjoint generator isL=w^−1D(w·), with no endpoint condition. Integrating its square twice gives the bulkC_r''−2C_r' M_(nu−ell)+C_r M_((nu−ell)²−ell'_reg), whereell=w'/w. The regular derivative is bounded; the jump at0 is recorded separately. The moving endpoint has the exact two graph-trace terms shown inMA-NZ.14, and the interior cusp gives−4alpha r(x)(wv)(0).

The shrinking test has ||r''||_1=O(1), integralr''=0, ||r'||_1=O(epsilon), ||r||_1=O(epsilon²), ||r'||_2=O(sqrt epsilon) and ||r||_2=O(epsilon^1.5). The integral cancellation and the finite-block translation estimate make the bulkO_T(sqrt epsilon) on each finite block. Uniform HS tails dispose of the remaining blocks.

At the moving endpoint, the output profiles contribute sqrt(w(c)); the coefficienta(c)=1/w(c) and the normalized graph functionals contribute the inverse factors. They cancel exactly. Thus the endpointS1 norm isO(sqrt epsilon) independently ofc. The cusp term isO(epsilon^1.5). The whole actualS1 operator therefore tends to0 uniformly.

## Passing to the full requested test class

For every fixedepsilon, g−r_epsilon is a genuine smooth test vanishing near0 and may be split into two smooth supported tests. If the positive and negative limits are separately proved there, the uniform estimate gives a Cauchy limit as epsilon→0 and proves the limit for the originalg. It does not claim C∞ convergence of the cutoff approximation.

For divisor expressions, each one-sided Mellin integral ofr_epsilon is bounded bymin(Cepsilon²,C/(1+gamma²)), with the first-derivative boundary term at0 kept. Summation givesO(epsilon log(2/epsilon)). Thus the already proved one-sided spectral formulas also extend. No derivative-of-delta ambiguity can remain on the requestedg(0)=0 class. An extension to all tests, if considered, can differ only by a multiple of evaluation at0; the theorem does not assert an unrenormalized limit for nonzero g(0).

The negative-time spectral formula is not part of this module. Root owns the complete FT synthesis after the AT proof. Complete author whole-proof QA passed; root and input complete readings were requested and are recorded separately when received. The resolvent-positivity route was proposed by the root agent; the finite-dimensional Schur shortcut and the fully written uniform endpoint proof were developed and checked here.
