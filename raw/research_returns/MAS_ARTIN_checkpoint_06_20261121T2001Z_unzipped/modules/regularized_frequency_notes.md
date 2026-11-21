# MA-RS-007: actual finite-frequency traces

Date: 21 November 2026. Author/checker: GPT-6 Astra Pro; effort inherited/not externally exposed; MAS_ARTIN /root/s5_audit.

## Result

The new module regularized_frequency.tex defines each operator by two literal bounded compositions in the weighted Fourier space. Its difference has a compact smooth kernel and is therefore trace class, proved through an absolutely summable Fourier rank-one expansion before its trace is evaluated. The diagonal has the factor chi_N squared and the negative logarithmic derivative with factor 1/(2 pi).

The disk factorization supplies polynomial growth for the logarithmic derivative on every generic line, although the proved reciprocal bound is exp(C log squared). Thus every compact smooth Mellin test is integrable against that diagonal, and dominated convergence gives a limit of actual finite-frequency traces. A justified contour deformation then gives the prime term minus the pole plus exactly the crossed right zeros. The reflected direct sum gives B_out minus P plus the exterior-strip zero sum. The complete character extension includes conjugate reflection and the principal pole order.

This is an explicit larger regularization for arbitrary compact smooth test and cutoff derivative, unconditional at generic widths. It is not the assertion that an uncut operator exists in that whole class. Its trace-norm convergence is proved only in the previously established Gevrey or fixed-gap cases, via exact compression of the already trace-class operator. No frequency parity is assumed because reflection is applied to the already constructed second operator.

## Proof checks actually performed

The author read the entire finished proof, the character argument and the compatibility argument. The two bounded compositions, the distributional delta cancellation, the sign of the derivative and Fourier constants, the Fourier-series trace proof, the explicit finite Blaschke logarithmic derivative, dominated convergence and all residue signs were checked. The exact prior RS and character proofs had already been independently read in full, as recorded in regularized_strip_s5_review_events.tsv and regularized_characters_s5_review_events.tsv. The whole invoked inherited M18 proof was also read earlier in this run and recorded in weighted_partial_strip_s5_review_events.tsv.

An independent whole-proof review has been requested from the parent. No public priority claim is made.

## Remaining scope

The construction inserts compact frequency multipliers into two actual bounded compositions. It does not identify their trace limit with Masullo's physical cutoff or all off-diagonal common-space maps. It retains the exact polar and discarded-divisor terms. The actual partial return of MA-PR is a separate route to comparing these terms with quotient geometry and still requires its own independent full review.
