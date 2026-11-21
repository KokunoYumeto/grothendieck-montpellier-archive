# Independent whole-proof review: I-30

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/purity_zero_status`; run `CUE_GCT-20261121-purity`.

Recorded event time: 2026-11-21T02:42:01Z.

Scope: complete reading and independent rederivation of `I30_endpoint_absorption.tex`, using the previously completely reviewed I-21, I-28, and I-29. No numerical test was needed. This is an independent agent proof review, not a formal certification or external peer review.

## Verdict: PASS

For a nonzero constant row `u_0`, the chosen elementary rank-one update satisfies `u_0 B(Y)=u(Y)` by direct multiplication. Its determinant is exactly `u_j(Y)/(u_0)_j`, with value one at zero. The column construction is the transpose counterpart. The factors are consequently generically invertible and units in every truncated local ring at zero, in every characteristic.

An interval containing either new endpoint is an old prefix, suffix, or full interval multiplied by one or two invertible matrices. Generic ranks and constant ranks are preserved, since the new constants are identities. Determinantal rank ideals are likewise preserved in a local ring by invertible row and column operations. Intervals consisting only of added factors are invertible, including the empty-interior case. Both new variables remain distinct endpoint positions. Thus the original constant-endpoint support lemma applies to the enlarged word without adding to its support budget.

For rank-two local tests at the common transcendental center, selected endpoint vectors are nonzero: a nonzero selected contraction cannot have a zero polynomial endpoint vector, and each endpoint comes from one original univariate factor or a constant boundary. After absorption, the compound word has invertible constants and width three, so its coefficient-row space has a nonzero scalar monomial of support at most two. Two fresh interpolation pairs therefore preserve all these tests simultaneously.

At the next center `alpha_i=t+SV_(2,i)`, a nonzero original univariate polynomial cannot vanish: setting the first-stage amplitudes to zero gives its nonzero value at the indeterminate `t`. This also verifies the stated transcendence observation and holds in every characteristic. Consequently both endpoints of every selected rank-one test remain nonzero at their centers. Its internal interval ranks lie in `{2,3}` and are preserved by the preceding stage. Endpoint absorption preserves that profile, and I-29 with `w=3,r=2` gives support at most four for the entire test. This is a bound on actual coefficient supports, so direct SV specialization detects the full polynomial; no assertion about every lowest homogeneous monomial is required.

The finite product argument gives one simultaneous parameter field for all tests, earlier minors survive at zero new amplitudes, and I-21's local rank induction then preserves the augmented rank-one full word. The six-pair generator follows. The degrees in the common center, selectors, and total amplitudes are unchanged, so the exact grid and Newton-simplex cardinality are correct with six pairs and the stated field-extension convention.

The proof uses the two-rank lemma only inside rank-one test interiors. It does not impose a two-rank promise on the complete original width-three word. The earlier larger generators remain valid. No polynomial-size assertion for growing width is made.
