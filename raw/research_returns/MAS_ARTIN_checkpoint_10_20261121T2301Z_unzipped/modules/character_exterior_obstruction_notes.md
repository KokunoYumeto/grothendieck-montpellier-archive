# MO024: a strict-exterior obstruction on actual common-source inputs

The complete proof is character_exterior_obstruction.tex, MA-MO.550–577. It concerns the full nontrivial compact-character common-sum action with the exact inherited two-sided polynomial norm. It does not concern only a raw coordinate diagonal or an independently chosen multiplier continuation.

## New actual operator argument

Fix a strictly right-exterior completed zero lambda=rho-1/2 and any nonzero complex compact smooth test g. For a compact h, the original wide Mobius inverse F=J_geom h has a finite right support endpoint. Translate h far to the right. The dual inverse input is then supported too far left to meet q=1-phi, so that entire source term vanishes exactly before Fourier transformation. The remaining source vector q U_t F is an actual compact norm-source vector.

Pair the actual output against a compact smooth v, using the bilinear transpose v_g=C_(g reflected)v without complex conjugation of g. The resulting scalar is the finite theta pairing

f(t) = integral q(y) W_(v_g)(y) F(y-t) dy.

Absolute ideal Euler estimates justify its Laplace transform for Re w>1/2. The exact result is

L f(w) = H_h(w) V_g(-w) - H_h(w) B_v(w)/A_eta(w) - R_(h,v)(w).

B_v is entire because phi W_(v_g) has compact support. The remainder is also entire: its actual double integral has y between max(ell,c) and beta+t0, and u between y-t0 and beta. The compact support of h, not a speculative decay estimate for a narrow inverse, supplies this fact.

## Why arbitrary nonzero smoothing cannot cancel the coefficient

At lambda, B_v(lambda) is the pairing of v with C_g b_lambda. The left-supported smooth function b_lambda is a finite cutoff theta sum at each point. Near its last support edge only the unit ideal contributes, so it is nonzero. A direct convergent Dedekind-zeta majorant gives an exponential bound at its left end. Its one-sided Mellin transform therefore exists on a genuine half-plane. Product uniqueness there proves C_g b_lambda is nonzero for every nonzero complex compact g, even if G(lambda)=0. A compact output test v can consequently detect it. A compact h=e^(-lambda x)h0 gives H_h(lambda) nonzero.

If the source action were bounded in H_Sigma, the weighted translation estimate would make L f holomorphic on Re w>a. Multiplication by A_eta clears the denominator on that connected half-plane. At lambda the resulting identity has zero left side and nonzero right side. A zero of any multiplicity is covered, since the numerator was chosen nonzero. The same argument forces a divergent normalized translated sequence of actual smooth inputs and outputs.

Exact source Fourier duality and Poisson reflection cover left-exterior zeros. All finite conductor and Fourier phases remain in those source maps.

## Scope retained

There is no assertion that an exterior arithmetic zero exists. At a fixed width, absence of strictly exterior zeros is necessary; the previously proved MO022 uniform interior containment is sufficient. Boundary zeros and no-margin sufficiency are not settled. The proof's holomorphy domain is the open half-plane Re w>a, and no boundary polynomial-weight threshold is inferred.

At every positive width, the necessary condition and MO022 sufficiency yield an explicit equivalence with own-character RH. This is a criterion for the actual original operator, not an arithmetic proof or a smaller FT002 gate. The three requested test moments may all vanish; a nonzero compact test of the form (d²/dx²-1/4)h0 with h0 supported in (1,2) shows that subclass is nonempty.

The complete written proof and final changes received a full author reading. Root and PF independently read all 482 stable lines and each passed the complete proof, including the actual source domains, compact remainder, complex-test nonannihilation, higher-order zero contradiction and final criterion. Their independent events are recorded separately. The source interfaces were the already freshly checked Meyer structural coinvariant, Schwartz-cup and actual projection/Poisson definitions, together with the literal ideal Euler coefficients of MA-CC.
