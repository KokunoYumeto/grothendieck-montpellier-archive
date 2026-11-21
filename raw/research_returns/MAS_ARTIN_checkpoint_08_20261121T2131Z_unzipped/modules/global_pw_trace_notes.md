# The actual finite Paley–Wiener quotient trace

Date: 21 November 2026. Agent: GPT-6 Astra Pro, /root/s5_audit, MAS_ARTIN. Effort is inherited and not externally exposed. MA-GP-009 was proposed by the parent; this agent developed the complete proof and exact half-line boundary calculation.

## Result

For s=0, 0<α<1/2, finite Y>0, and additive g compactly supported inside (0,∞), the actual half-line quotient H_[c,∞)/J_Y has trace Σ_(Reρ<1/2+α) mρ Mg(ρ−1/2), independent of c=−logY. The actual ambient convolution after the orthogonal complementary projection is trace class and has exactly that trace.

The two iterated traces of Mχ_R C_g Q_Y^glob are therefore:

- Position exhaustion first: minus the sum for Reρ<1/2+α.
- Global PW condensation first: minus the sum for 1/2−α<Reρ<1/2+α.

Their first-minus-second difference is minus the sum for Reρ≤1/2−α, including the lower boundary. No exterior zero is asserted to exist. No trace-norm or prescribed joint limit is asserted as Y and R both increase.

## Why this concerns the actual projection

The Hardy quotient only supplies a bounded similarity, since the actual half-line weight is R_c(y)=exp(2α|c+y|−2α(c+y)). The proof never substitutes its ordinary Hardy orthogonal projector for the actual weighted projector.

The Malmquist Poisson estimate is uniform as a zero approaches the right-half-plane boundary. It makes the compressed multipliers 1/(κ+z) and (κ+z)Mg(α−z) Hilbert–Schmidt. Their product gives quotient trace class, and the square of the resolvent is trace class.

For the actual lift, the adjoint unilateral generator is R^−1 ∂(Ru), with no boundary condition at zero. The resolvent square smooths into its second graph domain. Two integrations by parts give bounded bulk plus finite-rank endpoint and cusp terms. In terms of v=Ru and a=R^−1, the zero-endpoint term is [a(0)(2κk−k′)+a′(0+)k]v(0)−a(0)k v′(0). If c<0 and L=−c, the interior cusp term is −4α k(·−L)v(L). These terms are retained before proving trace class. For R=1 the formula is C_k(κ−∂)^2u=C_(κ²k−2κk′+k″)u+(2κk−k′)u(0)−k u′(0).

## Review state

The complete written module was read after writing, including the causal action, bounded similarity, Malmquist completeness, uniform tail estimate, quotient homomorphism, resolvent domains, both boundary signs, actual orthogonal trace cyclicity, and both iterated limits. Author check passed. Independent review is requested and is not predeclared here.
