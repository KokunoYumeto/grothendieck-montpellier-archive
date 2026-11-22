# Adversarial audit of the corrected A1 range

Reviewer: GPT-6 Astra, OpenAI, agent part_a567. Date:19November2026. This is a new independent analytic audit requested by root after the original-source checks. No mathematical program was run. Active TeX/bib files were not changed during the build freeze.

## Scope and outcome

Read the complete current `sections/part_a2b_secondary.tex`, `sections/part_a1_range.tex`, and `sections/part_a2_limits.tex`. Independently read the actual Mondello source `sources/mondello/Triang-submitted.tex`, theorem `thm:grafting` and its finite-stratum proof; the theorem expressly gives a real-analytic diffeomorphism on every finite topological stratum, including prescribed zero boundary lengths. The Ahlfors--Bers parameter theorem is used with the source and exact locators already recorded in `part_a2b_secondary.bib`.

I tried to break the argument at five places: fixed-compactification seam regularity, the moving-boundary jump, recession on faces, finite-boundary minimizers, and equivariance of the common retract. I found no counterexample to the stated range theorem under its marking and fixed-stratum hypotheses. The most delicate step is the regularity lemma, and the explicit local construction below closes its compressed seam-trivialization argument. The complete metric must not be claimed analytic in the parameter at every fixed point across a moving seam; the existing lemma's reference to the two metric pieces, and the proof's use of their one-sided derivatives, avoid that false stronger assertion.

## 1. Regularity on the fixed compactification

Here is an explicit way to obtain the smooth, parameter-analytic complex structures to which the Beltrami theorem is applied. Work near a parameter s0, at one active boundary, and set lambda0=sqrt(s0_i), a(s)=lambda_i(s)/lambda0. Use the reference conformal collar coordinate zeta=x+iy with x of period2*pi*lambda0. On a sufficiently small band crossing the seam, identify the target collar by

    x_s = a(s)*x,     y_s = y.

The target hyperbolic metric pulls back to `sec(y)^2*(a(s)^2 dx^2+dy^2)` for y<0; the flat cylinder pulls back to `a(s)^2 dx^2+dy^2` for y>0. Their common complex structure has Beltrami coefficient `(a(s)-1)/(a(s)+1)` on **both** sides. Thus the nonsmooth curvature does not produce a nonsmooth complex structure or Beltrami coefficient.

On the cylinder choose a fixed smooth cutoff chi(y), zero near0 and one sufficiently far out, and replace the second formula by

    y_s = (1+(a(s)-1)*chi(y))*y.

For parameters sufficiently close to s0 this is increasing. Near the puncture the identification is `(x_s,y_s)=(a*x,a*y)`, so the compactifying coordinates `exp(i*zeta_s/lambda_s)` and `exp(i*zeta/lambda0)` agree exactly. The identification therefore extends smoothly across the fixed marked point. Its Beltrami coefficient is smooth in space and real-analytic in s, with no seam jump. A fixed small collar exists uniformly in the parameter neighbourhood. Analytic Fenchel--Nielsen representatives on the remaining core can be joined to these collar representatives by fixed smooth cutoffs; fixed cusp ends have standard cusp charts and receive no changing positive-length cylinder.

Normalized Beltrami solutions consequently depend real-analytically on s. Local elliptic parameter regularity gives the required spatial derivatives in these smooth charts. To make descent to the fixed marked Y explicit, choose three distinct attracting fixed points of **hyperbolic** deck transformations; a non-elementary punctured-surface group supplies them. They remain distinct and depend analytically on the Fuchsian matrices, since the hyperbolic fixed points are simple roots. The unique Möbius conjugacy specified by these points is analytic. Because the marked conformal structure is fixed, it conjugates the whole marked deck representation, not merely those three points. The resulting normalized maps descend to Y. Stability rules out a nonidentity holomorphic automorphism in the identity marking class.

The cap coordinate extends holomorphically across its seam through the geodesic collar. For nearby parameters these extensions contain a common neighbourhood of the initial cap closure. Differentiating its coordinate on the initial cap and its boundary is therefore legitimate even when the actual cap domain moves. This also justifies the exponentially decaying end expansions used in Green's identity.

A genuine warning about the stronger regularity reading: the local translated model with density `-log cos(y-V*t)` on y<V*t and density0 on y>V*t has, at y=0, parameter dependence `0.5*(V*t)_+^2+O(t^4)`. This is not real-analytic in t. It is a local illustration of the moving-interface regularity, not a global counterexample to canonical capping. The proof does not require this stronger analyticity. Its first variation is continuous and has exactly the claimed derivative jump.

## 2. Independent jump-sign and bilinear calculation

Let the fixed coordinate be zeta=x+iy with flat side y>0, and write the seam as y=t*V(x)+O(t^2). Equality of the first spatial derivatives of the two logarithmic densities on the moving seam gives

    h_y^- + V*u_yy^- = h_y^+ + V*u_yy^+.

At the initial seam `u_yy^-=1` and `u_yy^+=0`, hence `h_y^+-h_y^-=V`, with exactly the sign in A2b-jump. Tangential displacement creates no additional term, since the initial mixed derivative vanishes.

For `v=dot(log w)`, holomorphicity gives `Re(-i*lambda*v')=-lambda*(Re v)_y`. Therefore differentiating `lambda^2|dw/w|^2` yields `h=c-V_y` for `V=lambda*Re v`, `c=dot(lambda)/lambda`. Differentiating `log|w_t|=0` gives the same positive normal velocity V. These two calculations independently fix both signs.

For two variations a,b, use Green's identity with h_a multiplying the equation for h_b, and with V_b multiplying the equation for V_a. The seam terms are respectively `-integral h_a*V_b` and `integral h_a*V_b-c_a*integral V_b`, so they cancel. Since `integral V_b=-2*pi*lambda^2*dot(F)_b` and `dot(s)_a=2*lambda^2*c_a`, the remaining term is exactly `pi*dot(s)_a*dot(F)_b`. The energy pairing is symmetric, establishing the off-diagonal symmetry without incorrectly inferring it from positivity of the quadratic form alone.

At a fixed cusp put T=-log|z|. The stated expansion gives h=O(1/T), its radial derivative O(1/T^2), finite Dirichlet/potential energies, and a truncated boundary term O(1/T^3). At flat ends the derivatives decay exponentially. No omitted end term changes the sign. Vanishing energy forces h=0 on the nonempty hyperbolic core and then on every cylinder by bounded harmonic uniqueness; every c_i is zero.

## 3. Recession directions on every face

The passage from p>0 to p>=0 does not require a uniform positive lower bound on the coordinates or an unproved cap-domain convergence statement. Write b_i=log B_i. The derivative inequalities `F_i<=b_i` imply, for every epsilon>0,

    S(s0+t*p) >= S(s0+t*(p+epsilon*1))-t*epsilon*sum b_i.

This is valid even if some b_i are negative. The weighted-disc supremum gives `K(p+epsilon*1)<=K(p)+epsilon*sum b_i`; any one fixed nearly maximizing disc system gives the opposite limiting inequality. Thus `K(p+epsilon*1)->K(p)`. The upper recession bound follows directly from `p.F(s)<=K(p)`. This proves the claimed value on all faces; p=0 is immediate.

For completeness, full continuity of K on the normalized closed simplex also follows without assuming bounded lower radii. Set `L(p)=K(p)-b.p`. It is finite, lower semicontinuous, homogeneous, and coordinatewise nonincreasing, being the supremum of `p.(F-b)` over competing disc systems. If q approaches p in the nonnegative cone, then `q>=(1-delta)*p` for some delta->0, using only the positive coordinates of p. Consequently `L(q)<=(1-delta)*L(p)`. Together with lower semicontinuity this gives continuity. The range proof itself already obtains openness from its local inverse and does not depend on this optional continuity observation.

The escaping-sequence coercivity argument is sound: components of the normalized directions p_k can be slightly negative, but are bounded below by `-s0_i/||s_k-s0||`. Their limit is nonnegative. For fixed t the segment points remain interior; continuity of G at their limit is available. Convexity then makes G nonincreasing along a ray of strictly positive recession slope, a contradiction. No illicit exchange between variable directions and recession limits occurs.

## 4. Finite-boundary exclusion

The lsc closure is still convex and has a supporting affine lower bound. A bounded sublevel of its closure cannot acquire unbounded boundary points: approximate each such point by an interior point in a sublevel enlarged by1 and contradict interior boundedness. Thus the minimum is attained, and no negative-infinite boundary value is possible.

If b is a boundary point with finite closed value, convexity with the fixed interior point b+1 gives

    G(b+t*1) <= (1-t)*G(b)+t*G(b+1),    0<t<=1.

Lower semicontinuity supplies the reverse limiting inequality. Hence the inward diagonal tends to G(b), as required. The collar estimate gives at least one derivative term tending to minus infinity; all other terms have finite uniform **upper** bounds, so there is no compensating positive divergence. The derivative is negative on an initial interval; strict decrease between t/2 and t proves `G(b+t*1)<G(b)` for small t. This handles a face of any codimension, including the origin.

The collar estimate used here is uniform in the other lengths. Apply the disjoint-collar theorem to all doubled geodesic boundaries, not just an unspecified local collar. The open collar of conformal width `arctan(csch(pi*lambda_i))` avoids all other marks and gives a univalent cap extension to the stated larger **open** disc. Possible failure of injectivity exactly on the limiting collar boundary is irrelevant to the conformal-radius inequality.

The graph version adds two diverging branch terms per vanishing edge, including loop edges, and uses the same finite upper bounds on all remaining branches. Its incidence maps have no common kernel, so the Hessian remains positive definite.

## 5. Equivariance and the common retract

The choice `s_e=1` is invariant under graph automorphisms. Canonical cap uniqueness makes its shadow circle at each branch functorial under every allowed biholomorphism of the marked normalization. The product of the two branch circles is an intrinsic circle in the tensor line; swapping the branches of a loop uses the canonical tensor-factor flip and introduces no extra modulus choice. No phase section or global tangent frame is selected.

For a nonzero q in such a line the unique positive a with a^(-1)q on that intrinsic circle is well-defined without a Hermitian metric. It is continuous and real-analytic in local frames and commutes with every permitted edge permutation or automorphism. Thus `H_t(q)=a^(-t)q` is a genuine equivariant strong deformation retraction. On the image, its logarithm is the straight segment between two points of the convex radial fiber. The same formula works on the entire nonzero-tensor bundle. It therefore gives a homotopy equivalence of the quotient stacks as well as the stated orbifold fundamental-group isomorphism; twisting of the circle bundle creates no obstruction.

This reasoning depends on the explicit marking convention already present: actual toric seam phases lie in S1. A fully marked real Fenchel--Nielsen twist must be quotiented by its integral Dehn-twist translations, or the phase target must be lifted to the corresponding cover. Ignoring that convention would create a concrete failure of injectivity, but it is explicitly excluded in the current theorem.

## Conclusion of this audit

No actual analytic gap remains in the five requested places after the explicit collar-trivialization construction above. No global metric analyticity at a fixed moving-seam point, no uniform recession convergence over all directions, no choice of a phase section, and no source theorem asserting arbitrary-length radius injectivity are being used. This audit does not settle an additional source-access requirement and should not be counted as a new mathematical result or a new finite computation.

Source-access precision for this audit: the new direct web opening of the CIMAT Ahlfors--Bers URL returned403 (`turn394400129view0`). No workaround was attempted. This audit independently read the local Mondello original and supplied the explicit collar construction; it uses the earlier successful indexed Ahlfors--Bers opening recorded in `sources/part_a2b_secondary.bib` for the parameter theorem, rather than claiming a new successful opening during this round.

## Integration after checkpoint05 — 2026-11-19 15:00 UTC

After the root lifted the TeX/bibliography freeze, the explicit seam trivialization and the qualification of analytic metric dependence were integrated into `sections/part_a2b_secondary.tex`, Lemma `A2b-regularity`. The conjugacy normalization now specifies three distinct attracting fixed points of hyperbolic deck transformations. The whole edited proof was reread. This is exposition of the already audited proof, with no theorem-status change, new mathematical result, or additional computational test. Root was sent the exact file and label for independent rereading.
