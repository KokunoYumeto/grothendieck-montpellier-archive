# MA-MO-032: fixed physical cutoff, varying test

Complete post-writing author reading passed on 2026-11-21. Final file has 526 lines, tags MA-MO.1100–1123, SHA256 6903a24f09943d6595c09ec080d0d754f52b45f4d31334049ee256b8c2987020. Root and PF complete independent whole readings passed with no mathematical or scope correction. The proof bytes remain unchanged.

## Quantifiers and conclusion

The real physical cutoff is fixed in advance, with its normalized endpoints and compact smooth derivative. The test varies in the single Frechet space of smooth functions supported in [1,2], so every test has value zero at the origin. Universal boundedness for real tests, universal boundedness for complex tests and universal trace-class scope are all equivalent to polynomial growth of the actual reciprocal on the generic line.

Under stipulated A, the fixed-gap theorem RS004 supplies that polynomial bound. This module does not establish it independently without zero-location input. If the bound fails, bad tests form a residual subset of both real and complex support spaces. Their actual fixed-core operators are unbounded and the actual finite-frequency operator norms diverge, although the trace limit still exists.

## Quantitative proof

The normalized step has p(0)=−1. Choose a fixed small positive displacement interval on which i p(v)/(2pi v) is nonzero. In a finite disk centered at2+iT, the local zero count is O(log|T|). Averaging the sum of logarithmic inverse distances over that fixed displacement interval produces one nearby ordinate t_T with |A(t_T)| bounded below by a fixed negative power of height. The finite-disk Harnack factor and finite Euler factors are retained. This is a selected nearby value, not a reciprocal bound at the original T.

The modulated test e^(−ax)e^(−it_Tx)b(x), with fixed nonnegative b supported in(1,2), has Mellin transform B(t−t_T) and derivative seminorms polynomial in T. The generic logarithmic derivative controls j on an input packet near T; the forward derivative bound and the selected lower value control A on an output packet near t_T. Both packet widths are one fixed negative power of height. All four kernel ratios differ from1 by at most1/100, and the output packet carries the exact central phase. The real part of the double integral is therefore bounded below. The other summand has uniformly bounded norm. This gives a lower bound proportional to |j(T)| times a negative power of height.

If every test were bounded, the actual map from the compact-support Frechet space into bounded operators has closed graph: core outputs converge for smooth test convergence. A direct Baire argument yields a finite derivative estimate. Applying it to the modulated tests forces polynomial j. Real universal scope complexifies before complex modulations are used.

When polynomial growth fails, the closed sets of tests with operator norm at most n have empty interior; their complement is residual. This produces actual fixed bad tests, by Baire rather than by a claimed numerical arithmetic example. Unboundedness gives unit compact-frequency core vectors. The finite operators converge on each core vector to the actual core formula, so their norms cannot remain bounded.

For a fixed Gevrey cutoff, the original sequential inverse-domain check depends only on the cutoff derivative and the compact-frequency input; the left compact smooth convolution is bounded. Thus this conditional failure is not merely a missing sequential domain: the whole fixed core remains valid and the actual sequential operator is unbounded.

## Limits

The theorem fixes the cutoff and resolves the universal-test quantifier. It does not decide a single individual pair, prove nonpolynomial arithmetic growth, or replace the two-sided ideal cancellation of MO028. Full-source boundary distributions and FT002 remain separate. The primary finite-disk ingredients are inherited and explicitly rederived at the needed selected-ordinate scope.
