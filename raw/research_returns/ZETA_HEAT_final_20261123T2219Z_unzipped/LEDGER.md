# Research ledger

Session began 2026-11-23 16:09 UTC (17:09 Europe/Berlin). The first three-hour review is due around 20:09 Berlin; later reviews hourly. Checkpoint ZIPs are due every 45 minutes of active work, starting around 17:54 Berlin, under unique names.

## Initial gates

1. Global simplicity: prove divergence of the scaled Toeplitz detection order or Jensen degree. No global proof established.
2. Positive-density growth: determine the exact index set and transfer map; a local density statement must not silently become a global time statement.
3. Zeta collisions: prove the isolated-pair formula and identify the zero-gap input needed for any statistical transfer.
4. Bounded-height multiplicities: check heat determinant orders and coefficients, rotation-averaged Hurwitz discriminants, and two-prime finite precision.
5. Spectral comparison: verify Suzuki attribution and convergence; check the original trial ratio and parity implications; seek a quantitative Weil estimate.

## 2026-11-23 16:18 UTC: first substantive changes

- Primary Alpöge announcement, Lean FRO/Mathlib report, and Waterloo GRH verification report located and opened. Used as published background; no claim of our own Lean replay.
- The exact heat and Hurwitz tangent maps identified. The sine criterion measures the Hurwitz translation. The arithmetic-coordinate heat derivative is purely imaginary at a real simple endpoint.
- Heat-minor source program reproduced: 66 partitions, 416 principal minors through degree eight. Phase model program reproduced: 28 local and 12 two-cluster exact cases, with numerical examples separately identified.
- Explicit contour determinant and Taylor-coefficient error estimates derived and written into the draft. Their constants expose the remaining height dependence.
- Independent re-proof of an explicit original two-tent probe lower bound completed. A stronger compact exponential-autocorrelation probe is present in the attachment and will be used for the main comparison.
- Spectral trial reduction strengthened in quantifiers: a vanishing liminf of the exact ratio, along one subsequence, suffices once the parity/product proof is applied on that subsequence. The quantitative ratio estimate itself remains open.

These are proof and scope findings, not a claim that the all-simplicity estimate is proved. The later review will distinguish genuine reductions of the main gate from supporting results.

## 2026-11-23 16:52 UTC: first checkpoint preparation

The assembled draft compiles. Exact finite detection, fixed-character signed counts, survival, CUE collisions, local contour reconstruction and spectral comparisons have full written proofs. Independent main-theorem reproofs continue; check events state their completed scope. A stronger elementary orbital variance bound transports each finite trace defect D_N into the global detection lower bounds pi*sqrt(15)/(4*sqrt(D_N)) and 1/D_N; finite_detection independently re-proved these inequalities. The quantitative all-height estimate is still open. No scheduled three-hour review has occurred yet.

Next work: attack an actual Weil or moment estimate; finish independent S47, height and CUE-label checks; add all main statements and complete historical context to the introduction; perform full assembled-document visual and two-pass reading checks. First checkpoint is a working draft, not a finished-paper claim.

## 2026-11-23 17:32 UTC: arithmetic certificates and exact spectral targets

- Higher even trace powers give a complete finite arithmetic simplicity test at each fixed height. The exact supremum of certified heights equals the first multiple ordinate. This removes the first-power test's obstruction from multiplicities above the target packet; it does not establish an unbounded sequence of certificates.
- Six rigorous arithmetic compressions, using finite prime sums and archimedean integrals, certify all zeros through height97.632 simple. Level6 has dimension766. No zero ordinate is an input. Root replayed levels1–3 at a different precision and checked the complete program.
- The same matrices give alpha6>7e−17, all gaps through90>6e−10, and reciprocal spectral separation at45>1.48e−13. This supplies explicit separation for the probe/contour comparison. The operator-approximation and contour-error inequalities still need to be met at those scales before claiming a common numerical rounding certificate.
- The sharp elementary orbital transport is now pi/sqrt(D_N), replacing the weaker pi*sqrt(15)/(4sqrt(D_N)). The higher-power supremum also gives the exact Jensen constant.
- The original even trial has exponent9; an odd trial tending to K′ gives the second-eigenvalue upper exponent13+epsilon. The attached source's lower target is exponent9+alpha,0<alpha≤4. The prompt omitted the9. Exact normalization and source equation are recorded.
- An explicit finite Legendre matrix lower certificate for the actual Weil operator now includes a legal frequency cutoff, norm error and a stronger quadratic-coupling error. Its asymptotic arithmetic eigenvalue inequality remains open. RH prime-count remainder bounds cancel the leading pole kernel but leave a derivative loss too large for this target.
- Gaussian restricted moments, anisotropic common Hurwitz continuation and conductor-uniform bounds have full proofs in the paper. Multiple-zero and tangent second jets have been checked whole. Independent same-model S47, height, CUE labels and S52 reproofs have completed; scope is specified in events.
- A positive-kernel finite surgery has been derived and independently re-proved, preserving the positive even superexponential heat class and threshold0 while imposing a double endpoint. Its exact Dirichlet-series change remains the arithmetic obstruction. The full proof is being integrated before checkpoint2.

The first formal three-hour review is still due at19:09:28UTC (20:09:28Berlin). No no-movement review has been counted. The main simplicity and statistical zeta-collision questions remain open.

## 2026-11-23 18:19 UTC: third checkpoint preparation

The common finite-height gate is closed through20 by an actual arithmetic spectral residual/projection certificate and an independent entire-edge contour certificate. The contour alone reaches45 with eight simple real centers and common real heat interval1e-257; arithmetic trace matrices reach97.632. No indexed zero ordinate is used in these certificates. A full independent moment audit repaired the mu-only coefficient edge case and the Bernstein coefficient extraction definition without changing the actual application constants.

The elementary actual multiplicity bound m_gamma<(3/4)log gamma yields global Toeplitz/window limit>216.88 and Jensenlimit>4766.003712, plus a proved quantitative two-sided comparison. Surviving positive-density packets have all3 detection indices infinite on the same heat interval; exact maps to the complementary factor are proved. Higher trace powers now control operator error and show necessary dimension/moment growth.

The theta hierarchy has full raw/physical maps, repeated-divisor sampling norms, endpoint expansions and compact-cutoff bounds. They give upper estimates at exp(-2pi lambda²). The required actual one-mode lower estimate at the sharper prolate scale remains open. Poisson and prime-ramp multiplicity reconstruction is explicit; its needed strict upper bound remains open. Primitive-conductor scalar limits are obstructed by functional reflection, for complex characters as well as real ones.

This is a progress entry, not the formal three-hour review. That review remains scheduled19:09:28UTC. The all-height simplicity theorem and statistical arithmetic collision laws remain open. Final whole-document visual and expert/newcomer readings remain pending.


## First formal review — 2026-11-23, approximately 19:09 UTC

The three-hour review records genuine movement since session start: COMMON-HEIGHT and DENSITY-DETECTION have been closed with proved actual statements and independent checks, and the higher-trace finite arithmetic criterion strictly reduces the main detection gate. The remaining all-zero simplicity estimate is open: no unbounded sequence of heights has zero integer inertia defect or a certified higher-trace defect below its complete detection threshold. The new Montgomery–Taylor constants, uniform lower rate, precision estimate, Möbius identities and commutator residual improve analysis but are not counted as new movement under the stopping rule. Consecutive reviews without movement: 0. Next formal review: 20:09:28 UTC; subsequent reviews hourly.

The 147-page paper has a fresh standalone build with no unresolved references or overfull-box warnings. Selected visual inspection covers opening pages 1–2 only at this checkpoint; the complete expert reading remains in progress and the final every-page visual and newcomer readings remain due. No final verification is claimed.

Review recorded at 2026-11-23T19:09:17.217485+00:00

### Row-by-row state at the first formal review

| Question | State | Strongest current gate or proved resolution |
|---|---|---|
| MAIN-SIMPLE | open | Prove sup_{N,k}(2/D_{N,k})^(1/(2k))=infinity, equivalently scaled Toeplitz/Jensen divergence. Finite actual certificates through97.632 proved. Equivalent integer test ind_+(TH_N−G_N)=n(T) at unbounded zero-free heights; N=O_eta(logT) realizes densityd_MT−eta but does not close integer deficit. Vanishing liminf of original Rayleigh ratio suffices; actual finite matrix lower certificate specified, asymptotic margin unproved. |
| MAIN-MOMENTS | open | For every height find a polynomial P(0)=1 whose certified squared-value sum over the endpoint divisor is below2; current leading asymptotics leave error proportional to N(T). |
| MAIN-CONTOURS | open | Uniformly certify growing contours, complex-time nonvanishing, separation, leading coefficients and remainder budgets. Fixed-contour partition theorem proved. |
| MAIN-TRACE | open | For every T obtain some finite N,k and certified D_N,k<2/T^(2k). Exact completeness and operator/dimension estimates proved; no unbounded height estimate obtained. |
| MAIN-RATIO | open | Need quantitative estimate for actual Weil a2 relative to the fixed original trial. Sharp-trial upper bound proved. Actual all-window lower exp[−C lambda^(2/d_MT)loglambda(1+logloglambda)] proved; comparison leaves target denominator estimate open. |
| MOTION-Q1 | refuted | Zero1169 rigorous Arb certificate; corrected phase shift δ=arctan(1/(2γ)) is exact. |
| MOTION-Q2 | proved | Universal square-mollifier moment inequality plus mixed phase and signed cancellation yields >1/12960000000000>10^-14 under established zero-location theorem. |
| MOTION-Q3 | open | Need fixed periodic odd-mode information or joint phase limit; all nonzero even weighted Fourier modes and all Gaussian normalized moments are transported by an explicit example with constant sine sign. Finite Abel inequality isolates odd modes and near-integer mass. |
| PAIR-Q1 | proved | Centered canonical product and uniform Gaussian transform yield ac=δ²(1/8+κ/32+Oκ²), unique crossing, κ=δ²S. |
| PAIR-Q2 | open | Need exterior inverse-square control and distinct simple endpoints. Scalar implication alone refuted by periodic triple-cluster real-entire function with2/3 short gaps butκ≥4/9. |
| PAIR-Q3 | refuted | Lagarias–Rodgers Theorem3.1 gives deterministic half-integer-separated unit-density sequence matching those identities; cite exact test class. |
| PAIR-Q4 | open | Need proved marked extreme-gap limit at shrinking scale together with uniform pair isolation, no short triples, singleton exclusion and tightness. No theorem asserted from unavailable assumptions. |
| PERSISTENCE-Q1 | proved | Montgomery–Taylor cosine approximation in the Rudnick–Sarnak pair test, reversed packing, Markov, Gaussian Rouché and bounded drift. |
| PERSISTENCE-Q2 | proved | Dobner uniform approximation plus finite simultaneous recurrence gives exp(exp(C/√a)), simple zero with Im z≤−1/2. |
| CUE-Q1 | proved | BAB gap PPP plus checked deterministic isolation/cluster controls; Weibull3/2 and intensity(3/2)√v. |
| CUE-Q2 | proved | Joint marked limit and Fredholm integer-gap series; rigorous interval width<4e−27 recomputed in independent basis. |
| CUE-Q3 | proved | L1 local density CLT for Palm jth gap gives fixed-frequency cancellation; sequential N→∞ thenj→∞. |
| COMMON-HEIGHT | proved | Actual independent arithmetic spectral probe and whole-edge heat contour certificates both succeed through20; contour alone45, trace alone97.632. |
| DENSITY-DETECTION | proved | All3 packet indices infinite uniformly on the common interval; exact convolution and differential maps compare full and complementary factors. |
| THETA-LOWER | open | Need b_L>=c lambda^(9+alpha)exp(-4pi lambda²) along unbounded windows. Exact theta/raw maps and direct cutoff upper bounds proved. |

The table expands the review recorded at19:09:17 UTC. It adds no new movement claim.


## Second formal review — 2026-11-23, 20:09 UTC

No open question has changed status since the first formal review, and no main question has been reduced to a strictly smaller proved gate. The gcd/Mobius continuation, Nyman and rational-cotangent Gram comparisons, Burnol physical-window and Weil-jet maps, classical multiplicity transport, finite deflation, and prime-ramp/packet-rank attempt make the remaining estimates explicit but leave the unbounded zero integer-deficit requirement unchanged. They are not counted as movement.

The prime-ramp test has an exactly proved sign-changing differential kernel; the AF full-Gram comparison still needs a smallest eigenvalue exceeding its omitted-zero tail, with the source grid-count error kept at its correct absolute scale O(T). The finite deflation map preserves the intrinsic trace excess and leaves a growing-family cross-term estimate open. The compact Burnol cutoff requires a simultaneous R/window/height tail estimate. These are precise records of the attempted routes, without claims that all possible consequences of those constructions have been excluded.

Consecutive scheduled reviews without movement: **1**. The next review is **21:09:28 UTC**. Research continues until that review; two consecutive no-movement reviews trigger the research stop and completion of all verification and delivery. Next checkpoint: **20:39:28 UTC**.

The 157-page fresh candidate has no unresolved references or overfull boxes. The expert and separate exposition source readings cover every one of the 47 TeX inputs; two editorial changes have been checked separately. Every-page visual inspection is in progress. The fresh statement-only contour derivation has established the fixed-character baseline moments using its named additive-transfer input; the uniform step and the Gaussian/localization families have separately scoped fresh checks in progress. Those check statuses are not new mathematical movement.

### Row-by-row state at the second formal review

| Question | State | Strongest current gate or proved resolution |
|---|---|---|
| MAIN-SIMPLE | open | Prove sup_{N,k}(2/D_{N,k})^(1/(2k))=infinity, equivalently scaled Toeplitz/Jensen divergence. Finite actual certificates through97.632 proved. Equivalent integer test ind_+(TH_N−G_N)=n(T) at unbounded zero-free heights; N=O_eta(logT) realizes densityd_MT−eta but does not close integer deficit. Vanishing liminf of original Rayleigh ratio suffices; actual finite matrix lower certificate specified, asymptotic margin unproved. |
| MAIN-MOMENTS | open | For every height find a polynomial P(0)=1 whose certified squared-value sum over the endpoint divisor is below2; current leading asymptotics leave error proportional to N(T). |
| MAIN-CONTOURS | open | Uniformly certify growing contours, complex-time nonvanishing, separation, leading coefficients and remainder budgets. Fixed-contour partition theorem proved. |
| MAIN-TRACE | open | For every T obtain some finite N,k and certified D_N,k<2/T^(2k). Exact completeness and operator/dimension estimates proved; no unbounded height estimate obtained. |
| MAIN-RATIO | open | Need quantitative estimate for actual Weil a2 relative to the fixed original trial. Sharp-trial upper bound proved. Actual all-window lower exp[−C lambda^(2/d_MT)loglambda(1+logloglambda)] proved; comparison leaves target denominator estimate open. |
| MOTION-Q1 | refuted | Zero1169 rigorous Arb certificate; corrected phase shift δ=arctan(1/(2γ)) is exact. |
| MOTION-Q2 | proved | Universal square-mollifier moment inequality plus mixed phase and signed cancellation yields >1/12960000000000>10^-14 under established zero-location theorem. |
| MOTION-Q3 | open | Need fixed periodic odd-mode information or joint phase limit; all nonzero even weighted Fourier modes and all Gaussian normalized moments are transported by an explicit example with constant sine sign. Finite Abel inequality isolates odd modes and near-integer mass. |
| PAIR-Q1 | proved | Centered canonical product and uniform Gaussian transform yield ac=δ²(1/8+κ/32+Oκ²), unique crossing, κ=δ²S. |
| PAIR-Q2 | open | Need exterior inverse-square control and distinct simple endpoints. Scalar implication alone refuted by periodic triple-cluster real-entire function with2/3 short gaps butκ≥4/9. |
| PAIR-Q3 | refuted | Lagarias–Rodgers Theorem3.1 gives deterministic half-integer-separated unit-density sequence matching those identities; cite exact test class. |
| PAIR-Q4 | open | Need proved marked extreme-gap limit at shrinking scale together with uniform pair isolation, no short triples, singleton exclusion and tightness. No theorem asserted from unavailable assumptions. |
| PERSISTENCE-Q1 | proved | Montgomery–Taylor cosine approximation in the Rudnick–Sarnak pair test, reversed packing, Markov, Gaussian Rouché and bounded drift. |
| PERSISTENCE-Q2 | proved | Dobner uniform approximation plus finite simultaneous recurrence gives exp(exp(C/√a)), simple zero with Im z≤−1/2. |
| CUE-Q1 | proved | BAB gap PPP plus checked deterministic isolation/cluster controls; Weibull3/2 and intensity(3/2)√v. |
| CUE-Q2 | proved | Joint marked limit and Fredholm integer-gap series; rigorous interval width<4e−27 recomputed in independent basis. |
| CUE-Q3 | proved | L1 local density CLT for Palm jth gap gives fixed-frequency cancellation; sequential N→∞ thenj→∞. |
| COMMON-HEIGHT | proved | Actual independent arithmetic spectral probe and whole-edge heat contour certificates both succeed through20; contour alone45, trace alone97.632. |
| DENSITY-DETECTION | proved | All3 packet indices infinite uniformly on the common interval; exact convolution and differential maps compare full and complementary factors. |
| THETA-LOWER | open | Need b_L>=c lambda^(9+alpha)exp(-4pi lambda²) along unbounded windows. Exact theta/raw maps and direct cutoff upper bounds proved. |

Review recorded at 2026-11-23T20:09:28.000514+00:00


## Research additions after the second review: boundary and conductor attempts

The derivative-companion attempt has exact common-divisor, kernel, Clark-mass, global-jet and trace maps. The proposed Hopf step fails with the explicitly computed subharmonic sign and the model F=z²; the arithmetic canonical-system route still lacks a normalized linear boundary-energy lower bound. The positive-kernel surgery realizes the same cubic shifted-kernel decay at a double zero. These are checked comparisons, not a smaller main gate.

The conductor-variation attempt now has a fixed-radius uniform lower count, independently re-proved before proof exposure, and its zero-free holomorphic factor/Rouche consequence. It closes this particular local approximation construction but does not change any of the20 question-row states or reduce an all-height gate. Matching small prime values through a growing range, and universality restricted to nonvanishing targets in the open strip, were checked through their exact source maps. Finite removal of certified simple coordinates preserves the entire intrinsic multiplicity excess; the growing-remnant cross-term estimate remains missing.

Additional verification is separate from research movement: fresh contour independent fixed-character and exposed uniform checks; fresh localization independent arbitrary-fixed-polynomial-conductor proof and exposed paper check; ongoing blind weighted-Gaussian continuation. Quiet-review count remains1 until the scheduled third review at21:09:28UTC. No review is inferred from this interim entry.

## Fixed-family cutoff calculation after review02

The simultaneous physical cutoff of each fixed endpoint-vanishing Burnol polynomial now has a proved asymptotic: q(chi_L H_R) and q((1-chi_L)H_R) are asymptotic to m_gamma|a|^2 A^2 L^(2M+2)/R^(2M+1), while the physical squared norm is asymptotic to |a|^2 B L^(2M+1)/R^(2M+1). The resulting Rayleigh quotient grows like m_gamma(A^2/B)L, including L=c loglogR. A separately independently derived multiplier lemma gives the stronger exponential local remainder. The original simultaneous-height and growing-jet-family gate is unchanged. This fixed-family calculation and the sharper primitive Gauss-factor error change no question-row status and do not count as movement. The scheduled21:09:28 review has not yet occurred.

## Third formal review —23November2026,21:09:28UTC

Recorded at 2026-11-23T21:11:20.897484+00:00. All20 question rows and their main gates are unchanged from review02. No open row closed and no main question reduced to a strictly smaller gate. Consecutive no-movement reviews: **2**. The user stopping rule now ends research. Remaining work is final record reconciliation, verification and delivery.

- Fixed-family Burnol cutoff norms are now computed, but the joint height/growing-order gate remains unchanged.
- HB/common-divisor/Clark maps preserve the exact multiplicity margin; no boundary lower estimate closes it.
- Conductor local counts close a particular approximation construction, not any of the20 question rows.
- Finite simple deletion preserves the full multiplicity excess; growing-remnant cross terms remain uncontrolled.
- The inspected adaptive Nyman--Beurling claim retains the multiplicity-squared excess and is not an imported analytic input.
- Additional independent derivations, exposed audits, sharper conductor errors and final packaging do not count as movement.

### Row-by-row state at the research stop

| Question | State | Strongest gate or resolution |
|---|---|---|
| MAIN-SIMPLE | open | Prove sup_{N,k}(2/D_{N,k})^(1/(2k))=infinity, equivalently scaled Toeplitz/Jensen divergence. Finite actual certificates through97.632 proved. Equivalent integer test ind_+(TH_N−G_N)=n(T) at unbounded zero-free heights; N=O_eta(logT) realizes densityd_MT−eta but does not close integer deficit. Vanishing liminf of original Rayleigh ratio suffices; actual finite matrix lower certificate specified, asymptotic margin unproved. |
| MAIN-MOMENTS | open | For every height find a polynomial P(0)=1 whose certified squared-value sum over the endpoint divisor is below2; current leading asymptotics leave error proportional to N(T). |
| MAIN-CONTOURS | open | Uniformly certify growing contours, complex-time nonvanishing, separation, leading coefficients and remainder budgets. Fixed-contour partition theorem proved. |
| MAIN-TRACE | open | For every T obtain some finite N,k and certified D_N,k<2/T^(2k). Exact completeness and operator/dimension estimates proved; no unbounded height estimate obtained. |
| MAIN-RATIO | open | Need quantitative estimate for actual Weil a2 relative to the fixed original trial. Sharp-trial upper bound proved. Actual all-window lower exp[−C lambda^(2/d_MT)loglambda(1+logloglambda)] proved; comparison leaves target denominator estimate open. |
| MOTION-Q1 | refuted | Zero1169 rigorous Arb certificate; corrected phase shift δ=arctan(1/(2γ)) is exact. |
| MOTION-Q2 | proved | Universal square-mollifier moment inequality plus mixed phase and signed cancellation yields >1/12960000000000>10^-14 under established zero-location theorem. |
| MOTION-Q3 | open | Need fixed periodic odd-mode information or joint phase limit; all nonzero even weighted Fourier modes and all Gaussian normalized moments are transported by an explicit example with constant sine sign. Finite Abel inequality isolates odd modes and near-integer mass. |
| PAIR-Q1 | proved | Centered canonical product and uniform Gaussian transform yield ac=δ²(1/8+κ/32+Oκ²), unique crossing, κ=δ²S. |
| PAIR-Q2 | open | Need exterior inverse-square control and distinct simple endpoints. Scalar implication alone refuted by periodic triple-cluster real-entire function with2/3 short gaps butκ≥4/9. |
| PAIR-Q3 | refuted | Lagarias–Rodgers Theorem3.1 gives deterministic half-integer-separated unit-density sequence matching those identities; cite exact test class. |
| PAIR-Q4 | open | Need proved marked extreme-gap limit at shrinking scale together with uniform pair isolation, no short triples, singleton exclusion and tightness. No theorem asserted from unavailable assumptions. |
| PERSISTENCE-Q1 | proved | Montgomery–Taylor cosine approximation in the Rudnick–Sarnak pair test, reversed packing, Markov, Gaussian Rouché and bounded drift. |
| PERSISTENCE-Q2 | proved | Dobner uniform approximation plus finite simultaneous recurrence gives exp(exp(C/√a)), simple zero with Im z≤−1/2. |
| CUE-Q1 | proved | BAB gap PPP plus checked deterministic isolation/cluster controls; Weibull3/2 and intensity(3/2)√v. |
| CUE-Q2 | proved | Joint marked limit and Fredholm integer-gap series; rigorous interval width<4e−27 recomputed in independent basis. |
| CUE-Q3 | proved | L1 local density CLT for Palm jth gap gives fixed-frequency cancellation; sequential N→∞ thenj→∞. |
| COMMON-HEIGHT | proved | Actual independent arithmetic spectral probe and whole-edge heat contour certificates both succeed through20; contour alone45, trace alone97.632. |
| DENSITY-DETECTION | proved | All3 packet indices infinite uniformly on the common interval; exact convolution and differential maps compare full and complementary factors. |
| THETA-LOWER | open | Need b_L>=c lambda^(9+alpha)exp(-4pi lambda²) along unbounded windows. Exact theta/raw maps and direct cutoff upper bounds proved. |
