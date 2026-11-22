# Complete root review of the formal trace/index countermodel

Reviewer: `/root`; model: GPT-6 Astra Pro; effort: not exposed; run: GCT_POS.
Date: 21 November 2026, completed 23:22 UTC.

**PASS within its formal-character scope.** Read the complete theorem and proof in `branches/plethysm/trace_index_obstruction.tex`, the entire script `branches/plethysm/scripts/check_trace_index_obstruction.py`, and the independent Kronecker-branch review. Then replayed the script independently of the author's execution: all 34,730 degree checks in dimensions10,12,14 passed.

The complete proof was reconstructed, not inferred from the finite tests. The elementary inequalities start at even n=10 and persist under n to n+2. The truncated binomial sums agree with their polynomial extensions in every nonnegative degree because all potentially early upper arguments remain nonnegative. The hockey-stick bound, doubled-argument comparison, and mask lower bound prove nonnegative integral coefficients and f=g+3c with c nonnegative on the whole infinite tail. The rational C3 representation has exactly those dimensions and traces, degree by degree.

Direct reciprocal substitution gives the multiplier -t^(n^2) for every summand. The distinct pole orders at one follow from the strictly larger mask dimension. The explicit parity encoding, separate marker variable and distinct padding variable prove the tensor ambient bound in all degrees; this is an injection, not an asymptotic estimate. At the dyadic root only the specified auxiliary wave contributes, with unit residue above three and no higher collision poles. The tensor-model wave has precisely the primitive-3M denominator and no primitive-M pole.

The auxiliary strict saturation lower bound evaluates an actual constituent at an off-residue argument, rather than relying on attained values. Every tensor-model constituent is positive above S-1, and its actual zero at S-1 gives equality for its strict saturation index. Shifting by d_D makes all polynomial factors positive and the first product coefficientwise larger than the second; the constant margin absorbs every periodic correction. This proves the polynomial positivity-index upper bound.

The computation separately checks the mask by literal binomial sums at designated degrees, the complete wave blocks, all tested nonnegativity identities, and selected exact ambient bounds. These finite tests calibrate the written all-n proof.

Crucial limitation: G is not the actual auxiliary B_n, and F,G are not asserted to be invariant-ring Hilbert series or a graded algebra. The result excludes a transfer based only on the listed numerical and degreewise-representation facts. It does not answer either strict-index question for the actual tensor ring.
