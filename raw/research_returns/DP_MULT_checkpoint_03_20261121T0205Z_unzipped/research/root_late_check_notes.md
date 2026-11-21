# Root's late integrated proof readings

Reviewer: `/root`, GPT-6 Astra Pro, run `DP_MULT_20261121`. The runtime does not expose the reasoning-effort setting. The event timestamps are recorded in `CHECK_EVENTS.tsv`; they are completion observations, not fabricated durations.

## ROOT-DP34-INTEGRATED

The complete integrated proof was reread after the earlier draft reading. The chain estimate uses `N/R_(j+1)=p^i` at every transition; the interior binomial valuation is at least one and the last term has valuation `N>=p^(i+1)`. The exceptional wrap returns the leading operator to the original direction with precisely `p^(p^i)`. Each base-block maximum is below one and the last is exactly one. Integer ideal containment is proved before base change, so the ramified version contains no invalid valuation rounding.

For the sharp witness, Teichmüller characters rule out every smaller positive axis degree. The first-path coefficient is a unit in the scaled inverse. The exponent sums are exactly `q−1` and `h−1`; Legendre's factorial identity gives `p^i−1`. The same argument includes `p=2` and `h=2`. Verdict: PASS.

## ROOT-DP36-INTEGRATED

The entire statement and proof were reread. The invariant weighted degree is an element of `s Z` because the character difference is divisible by `q−1` and `1=(p−1)s`; all weights are positive. This remains true after duplicating either variable set. Integral inverse substitutions and the formal logarithm retain the bound at its boundary. Each extracted additive-coboundary coefficient comes from a unique original monomial; the selected binomial multiplier loses at most one valuation, including a pure power in one dual component. Raising all weights by `p` restores that one unit. The mixed factorial formula and the one-variable path use different factorials, and both are handled correctly. The residual on the stated path is exactly `rho_h`.

This is a sufficient estimate under stated hypotheses. The proof neither identifies a prescribed geometric theta representative/path nor proves optimality or a global upper bound. Verdict: PASS within that scope.

## Source statement: Zink Lemma 111

The published section4.2 statement and preceding inverse-limit argument were read. It supplies a section of a formal torsor under an exact functor over a prorepresentable formal object. Such a section supplies a frame for cocycles; it is not a biextension splitting. No full audit of Zink's paper is asserted.

## ROOT-DP35-39

The root read each complete saved proof, not only its statement: DP35's Gauss norm, contraction dichotomy, homogeneous-multiplier induction, complete characteristic-zero integration and actual class application; DP37's Hodge–Tate characteristic polynomial and exact torus embedding, followed by the entire invariant-frame and averaged-splitting argument; DP38's two cyclic displays, Witt carries, both telescoping defects, functorial injectivity at the degree cutoff, both exact first coefficients, gauge invariance, monomial classification, normalized derivatives, unit-factor path and generic-path scope; and both full DP39 examples with the Fischer identity and all row/contraction conditions. The integrated proofs were composed from those read versions, and independent deliverable-version reviews are separately recorded.

The root also directly viewed Tate's original printed p180 and checked the exact sequence used by DP37. The new primitive coefficient theorem concerns its explicit Teichmüller coordinates; no unproved equality with the entire DP32 logarithm was used. The new harmonic example is a formal local implication test, not a constructed global theta datum.

An independent integrated review by `/root/archive_binomial` subsequently caught a local Witt-negation assertion in DP38's text: Witt negation is not componentwise at p2. The integration was corrected to write `w=−ξ` and use `w_i Y_1^(p^i)`, with only `w_0=−ξ_0` needed. The coefficient proof and theorem do not change. The same review prompted explicit repetition of the h>2 and invariant-splitting qualifiers for the path corollary. These corrections are retained in the event history rather than silently described as an error-free first draft.
