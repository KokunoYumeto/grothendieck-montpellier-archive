# Focused adversarial audit: zero faces and inactive normalized components

Date: 2026-11-19. Auditor: Part A567. Manual proof-audit duration was not measured. This audit reads the current proof text and targets domain edge cases only; it does not repeat the general analytic audit or run any finite/numerical test. **No omitted hypothesis or mathematical gap was found.** No TeX correction or status change is required. This is verification, not progress movement.

## Exact proof locations

| Case or inference | Existing statement or displayed identity |
| --- | --- |
| Fixed positive cap stratum; remaining marks are cusps | `sections/part_a2b_secondary.tex`, opening notation and A2b-regularity |
| Support values for partially zero weights | A2b-support, A2b-support-extremal; zero-weight points allowed on the critical graph; K(0)=0 explicitly |
| Recession in all nonnegative directions, including zero entries | A2b-recession and A2b-recession-formula; final epsilon-approximation argument |
| Uniform exclusion of finite zero-length boundary faces | A2b-collar-bound and A2b-image |
| Disconnected normalization, zero local weight vectors and loops | A1-graph-potential and A1-graph-range, including explicit K_v(0)=0 |
| No active flags at a component; no external active legs | A1-bordered-shadow-range and its opening zero-contribution convention |
| Every imbalance d, including mixed signs and zero entries | A1-toric-domain, shifted orthant Omega_d and its global minimization proof |
| Componentwise large-length limit scope | A2-cap-limit, whose retained opening hypothesis is connected Y |

## 1. Zero weights are distinct from zero lengths

The radius diffeomorphism is on a fixed genuine-cap stratum s_i>0. Marked points assigned zero boundary length are left as cusps and omitted from that active set. Thus the theorem does not plug log(0) into its finite-dimensional logarithmic target. Approaching s_i=0 inside a positive stratum is used to exclude a finite boundary minimizer, not to assert that the positive-radius diffeomorphism extends across that face with finite logarithmic coordinate.

A weight p_i=0 is a support/recession direction, not an instruction that s_i=0. A2b-recession expressly handles such directions by comparison with p+epsilon*1, the coordinate upper bounds F_i<=log B_i, and the support supremum formula. If the entire local weight vector p_v is zero, its recession slope is literally0 because the argument s_v stays fixed; K_v(0)=0 is already defined. No Jenkins–Strebel differential at the all-zero vector is required.

## 2. Inactive components are zero-dimensional factors

For an empty local active set J_v, the convention that the vertex contributes zero means S_v=0, D_v=R^0={point}, and K_v(0)=0. It has its unique complete stable hyperbolic metric but no cap or length variable to recover. The standalone connected cap theorem assumes nonempty I; the graph construction extends it by this trivial zero-dimensional factor rather than applying that theorem outside its hypotheses.

A disconnected normalization causes no interaction between these local factors: D_Y is their product and S is their sum. In the actual connected stable-graph setting, a vertex with no active flag can only be isolated, hence can occur only when it is the sole vertex and E is empty (possibly with no active external legs). The existing factor convention also remains harmless algebraically if a disconnected graph is considered. The dimension formula in the manuscript concerns connected stable graphs, as specified in the opening of part_a1.tex; this audit does not silently extend that formula to disconnected curves.

## 3. Strict support inequalities survive pushforward

For nonzero p>=0 in the edge/active-leg coordinates, P_*^T p is nonnegative and nonzero, because every edge has two actual flags and every leg has one. On each component with nonzero local weight, A2b-image supplies a strict inequality; on components with zero local weight, both sides contribute0. Summing therefore remains strict because at least one component has nonzero weight. An inactive component cannot create equality in the global nonzero direction. A self-loop contributes two distinct local coordinates; it does not cancel or identify them.

The converse is furnished by the equal-length inverse A1-bordered-shadow-range. Thus P_*(D_Y) equals the strict support region without needing to infer that projection commutes with a closed-boundary description or that every individual local direction is positive. When L is empty, P=E and the same reasoning applies. When E and L are both empty, the domain and image are one point, there are no nonzero test weights, and the fiber dimension is0. The explicit empty-case clause in A1-toric-domain handles this instead of appealing to a nonzero recession direction.

## 4. Every finite imbalance d has an interior minimizer

Fix any d in R^E. Its domain is the nonempty shifted orthant t_e>|d_e|/2, t_l>0; for instance t_e=|d_e|/2+1 and t_l=1 is an interior point. The affine branch vector has entries t_e±d_e/2 and t_l. The block Hessian of S is positive definite on all actual flags; empty components contribute no directions. P_*^T is injective, so the restricted Hessian P_* Hess(S) P_*^T is positive definite whenever there is a variable.

An escaping sequence in this shifted orthant has, after normalization from a fixed interior point, a nonzero nonnegative limiting direction p. Its branch direction is P_*^T p. On components with zero local direction the potential stays constant; on the others A2b-recession gives the requisite K_v. Hence the total recession slope is K_Gamma,L(p), regardless of d or which components have zero weights. The strict support inequality gives a positive slope for Phi_d-y*t and contradicts an escaping bounded sublevel, exactly through the segment argument in A2b-image.

At a finite boundary point, an edge t_e=|d_e|/2 makes at least one branch length zero: exactly one if d_e is nonzero, both if d_e=0. A boundary leg likewise has zero length. Along the inward diagonal every branch coordinate has derivative+1. Thus the derivative of Phi_d-y*t is the sum of all branch/leg log radii, with each positive multiplicity, minus a finite constant. At least one term tends uniformly to minus infinity by A2b-collar-bound; the others are uniformly bounded above. This excludes a finite-valued boundary minimum; an infinite boundary value is already excluded. No assumption that both branches vanish, or that every component contributes a vanishing branch, is needed. The affine supporting lower bound and bounded sublevels give existence of the lower-semicontinuous minimum; strict convexity then gives uniqueness. The analytic inverse only uses the positive interior branch lengths, so d_e=0 is not an analytic singularity despite the absolute value in the domain description.

## 5. Limit caution checked against actual uses

A2-cap-limit proves collapse of zero-weight caps on a **connected** marked compactification with at least one positive limiting weight. It would be false to apply that collapse simultaneously to every component of a disconnected normalization when an entire component has zero limiting weight: its own cap parameters may remain fixed and its cap radii positive while another component's lengths grow. The graph-image and unequal-fiber proofs do not make this incorrect inference. They use the recession theorem, including K_v(0)=0, which needs no collapse on that component. The current statement and dependency chain are therefore correct.

## Conclusion and scope

Zero-length faces, partially and wholly zero local support weights, no active external marks, self-loops, disconnected normalizations and inactive vertices are all covered by the present conventions and lemmas. In particular the global minimizer exists for every finite d in the stated tensor/shadow target. The separate full-external-disc-shape target retains its A1-toric-full-discs qualification; no universal R^E-fiber assertion for that target has been inferred. No new theorem, source-opening claim, test output, correction row or closure event is warranted.
