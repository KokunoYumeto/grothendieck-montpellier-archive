# Causal synthesis for the actual polynomial-weighted PW quotient

Date: 21 November 2026. Author/checker: GPT-6 Astra Pro, MAS_ARTIN /root/s5_audit. Effort is inherited and not externally exposed.

## Scope and result

The complete new proofs are MA-GW001–003 in global_weighted_pw.tex. They cover every s≥0, 0<α<1/2, every finite band Y>0, and additive compact smooth tests supported in (0,∞). They use no RH, A, M, generic-edge hypothesis, or zero-separation assumption.

The actual half-line closure retains every jet at zeros with β<1/2+α and precisely the jets 2j<s−1 at β=1/2+α, capped by the zero multiplicity. The actual quotient convolution and actual ambient convolution-after-orthogonal-projection are trace class. Their trace is the sum with these exact lengths.

The two iterated global PW/position cutoff limits differ by minus the full zero sum for β<1/2−α and minus the unretained lower-edge lengths m−min(m,b_s) for β=1/2−α. The upper-edge contributions cancel. No exterior zero or omitted edge jet is asserted to exist, and no unrestricted joint limit follows.

## The new range proof

After the logarithmic half-line change of variables, the actual norm is equivalent for fixed c to L2((0,∞),(1+y²)^(s/2)dy). This removes only the fixed finite interval modification, not the polynomial weight.

Set d=1/2−α and u=1−d. The bounded causal symbol is Φ(z)=(z−u)ζ(z+d)/(z+2)^N for a sufficiently large integer N. The canceled zeta pole has a nonzero removable value. Unconditional fixed-strip growth and right-half-plane Euler estimates show that its inverse Laplace kernel is causal and exponentially decreasing.

Every actual smooth band test, including one that is not flat at frequency zero, has a logarithmic primitive b with all derivatives exponentially decreasing and flat at the left endpoint. Its theta image is exactly 2Y^d Φ(z)(z+2)^N Lb(z). This proves inclusion in the actual bounded convolution range. Conversely, solve (∂+2)^N b=h for compact causal h and truncate b in the weighted graph norm. These compact primitives give actual source tests and prove the reverse range-closure inclusion. No false Schwartz density of annular frequency tests is used.

## The operator resolvent and finite rank

On the quotient by closure ran T_φ, the actual convolution T_φ is zero. The divided-difference kernel ψ_λ(r)=∫_r^∞ φ(t)e^{λ(t−r)}dt gives (λ−A)T_λ=Φ(−λ)I, with both inverse identities and generator domains checked. Thus the actual quotient resolvent is meromorphic, not merely a formally assigned quotient.

Each principal-part projection has dual range among solutions of (∂−λ)^m v=0. In the weighted dual those are exactly polynomial exponentials e^{λy}p(y), with all m jets when Reλ<0 and only 2j<s−1 when Reλ=0. The allowed functionals annihilate the actual convolution range and are fixed by the contour projection. This proves both finite rank and the exact lengths. At a critical odd s, the forbidden jet has logarithmically divergent norm; the proof never relies on a borderline Sobolev cutoff assertion.

## Uniform estimates and elimination of a residual subspace

The numerator operator T_λ is uniformly bounded on every left half-plane Reλ≤ε<η. On the entire far-left region the Euler lower bound gives ||R(λ)||≤C(1+|λ|)^(N−1), with one constant independent of how far left λ lies. M18's fully proved good-height minimum modulus is needed only in one fixed central strip. Hence the block contour bounds are polynomial and their ranks are O(log|n|).

For each compact causal test, Bromwich inversion and these bounds give a trace-norm convergent finite-block sum. Moving the last vertical line to negative infinity kills the remainder using the positive lower endpoint of the test support. A positive-time approximate identity then converges strongly to the identity, so there is no invisible residual quotient. The same argument with a sufficiently high rational resolvent power gives an actual trace-class power of the quotient resolvent.

The ambient lift uses the actual weighted adjoint generator W^−1∂(W·). The complete higher-order integration-by-parts boundary expression is included. It keeps the endpoint at zero and the cusp at −c, makes the bulk bounded, and makes all boundary terms finite rank after the trace-class resolvent power.

## Review state and inputs

The full finished proof was read after writing. The author check passed the source-range equality, causal-kernel construction, actual two-sided resolvent identity, finite-rank argument, all contour uniformities and remainder estimates, approximate-identity synthesis, exact edge counts, resolvent power, actual ambient lift, and limit signs. Root and input_audit subsequently completed independent whole-proof readings and both reported a pass. Input's scoped records are global_weighted_pw_input_review_events.tsv; root owns its independent review record.

The exact existing primary interfaces are the actual theta/Poisson formulas in GP001–005, NT-Z10's unconditional polynomial growth and local zero count, and the complete good-height/disk-Blaschke/Harnack argument MT-M18 equations M18.7–M18.8. The latter proof was freshly reread in full during this derivation. No new weighted invariant-subspace theorem is imported.
