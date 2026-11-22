# Complete independent review of MO021

The entire written proof in `polar_relative_trace.tex` was read and checked, followed by the final line-break changes and the two precise cutoff/support clarifications. The proof passes.

The trace-class operator used in the invariant exact sequence is E_g=C_g(1-P_plus), defined through the already proved actual full matrix and the finite-rank complement of P_minus. This distinction is necessary: the raw matrix D_g is not asserted to preserve W_plus. The source composition is p_plus i_plus=1+L, so the restriction of E_g to W_plus is exactly minus the local-source endomorphism. Its quotient is the actual convolution on H/J, established first on the original smooth source and then by continuity.

The finite-rank polar contribution is G(-1/2)+G(1/2); its computation does not require the chosen section range to be invariant. Upper-triangular compression in the orthogonal decomposition W_plus plus its complement gives both the trace relation and the Fredholm product. No formal algebraic exact sequence is substituted for these actual operators.

The explicit half-plane hypothesis is used twice and both uses are declared: first in MO018 to identify the original wide inverses with the positive narrow line on every E input, and again through the functional equation to retain the full nontrivial divisor in the quotient. The sum and maximum exponential weights give isomorphic completed quotients and similar convolution operators, so their trace is the same. The final full explicit formula is used only after the actual quotient trace has been established.

With g(0)=0, the local return trace is minus A0. Consequently p(g)+tau(g)-Tr_Q C_g is plus B(g). Keeping S={infinity} matters: the original Meyer argument chooses S to contain all primes seen by the test before setting the common trace to zero. The fixed-S matrix here correctly retains those prime terms. A test meeting the prime-power logarithms only at log2 has trace log2 divided by sqrt2.

Fresh source checks covered the supplied Meyer p_plus i_plus calculation and relative trace-additivity passage, the actual local-return normalization, the WP retained-jet and norm interface, and the original TR2/TR4 conventions. This is not a claim to have freshly rechecked the full external Meyer paper.
