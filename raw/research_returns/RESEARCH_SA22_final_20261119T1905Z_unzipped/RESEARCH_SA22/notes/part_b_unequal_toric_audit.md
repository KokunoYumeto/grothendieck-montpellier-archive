# Independent audit of unequal-length toric surgery

Auditor: GPT-6 Astra (OpenAI), `part_b_cycles`, 19 November 2026, 15:52 UTC. Requested by A567 and then the parent. Read the complete `sections/part_a567_toric_unequal.tex`, the precise `A2b-recession` and `A2b-image` proofs in `sections/part_a2b_secondary.tex`, the equal-length bordered range and full-shape criteria, `A1-tensor`, `A1-retained-discs`, and the analytic welding input. No finite program was run and no TeX was edited by this reviewer.

**Verdict: the new theorem, counterexample and full-disc criterion are correct after the one local all-seams correction described below. The global real-analytic R^E parametrization is proved, not merely inferred from contractibility.**

## Linear coordinates and exact fiber dimension

There are `|H|=2|E|+|L|` independent positive squared halfedge/leg lengths and `|P|=|E|+|L|` target logarithms. The map P sends the two branch log radii to their sum and leaves external log radii individually. Its transpose duplicates edge coordinates, so it is injective, including for self-loops. The support function on the projected nonnegative direction is exactly the previously defined `K_{Gamma,L}`.

The inclusion of the larger image in the support region follows from `P^T p>=0`. The converse uses the already proved equal-length solution, which is a permitted larger-domain solution. Thus image equality involves no assertion that a projection of an open convex set automatically equals some closed support intersection. A fixed target's full cap-logarithm fiber is the nonempty open convex slice `D_Y intersect P^{-1}(y)`, of dimension E. Its tensor phases fix the toric boundary maps uniquely once the caps are known.

## Global squared-difference coordinates

For an oriented edge write `s_+=t_e+d_e/2`, `s_-=t_e-d_e/2`; for an external leg use `s_l=t_l`. Thus the domain for t is exactly

`Omega_d = {t_e>|d_e|/2, t_l>0}`,

and every positive s is represented uniquely by its averages t and differences d. The Hessian of `Phi_d(t)=S(P^Tt+a(d))` is `P Hess(S) P^T`, positive definite by injectivity of `P^T` and the proved energy identity.

For every `p>=0`, the starting vector `P^Tt_0+a(d)` is positive and the direction `P^Tp` is nonnegative. The actual recession lemma therefore applies even when some components of p vanish. It gives exactly `K_{Gamma,L}(p)`, independently of d. No limit along a shifted vector with a nonpositive starting component is used.

Here is the full minimization check. Set `G_d=Phi_d-y.t` for y in the strict support region. If a sublevel escaped to infinity, normalize directions from one fixed `t_0 in Omega_d`. Because every coordinate has a fixed finite lower bound, a subsequential unit limiting direction p is nonnegative. Convexity along the segments to the escaping points gives `G_d(t_0+u p)<=G_d(t_0)` for every fixed `u>0`. This contradicts the strictly positive recession slope `K(p)-p.y`. Hence all sublevels are bounded.

The supporting affine function at any interior point prevents the lower semicontinuous closure from taking minus infinity at a finite point. A nonempty bounded sublevel and lower semicontinuity then give a minimizer of the closure. If a finite boundary point b had finite minimum value, the ray `b+epsilon*1` lies in the interior. Its values tend to the closure value at b: convexity against any fixed point on that ray gives the limsup, and lower semicontinuity gives the liminf. At least one branch coordinate of s on this ray tends to zero. The collar bound sends that cap logarithm uniformly to minus infinity; every other cap logarithm has its fixed finite upper bound. The derivative of `G_d` on the ray is their sum minus a finite constant, so it tends to minus infinity. This contradicts a boundary minimum. An infinite boundary value cannot be a minimum either.

The unique interior minimizer solves `P F(P^Tt+a(d))=y`. Strict convexity gives uniqueness. Its derivative in t is the positive Hessian, so the implicit function theorem gives a joint real-analytic inverse in y,d and the normalization. The absolute value in the domain inequality causes no singularity at d=0: the defining equation itself is analytic in t,d, and all its s coordinates remain positive in a neighborhood of any solution. Changes of tangent frames add linear terms to S and the matching translated target logarithms; they leave this intrinsic solution and d unchanged.

## Analytic seams and the geodesic submodel

Unequal hyperbolic lengths cause no analytic welding obstruction. In the two analytic cap coordinates the toric map is `zeta eta=c`, with `|c|=1`. The exterior collar on one side is glued to the exterior collar on the other using the holomorphic inversion `eta=c/zeta`. This furnishes a local analytic chart across the unit-circle seam. Hyperbolic circumference equality is needed to glue the metrics isometrically, not to glue their complex structures by this normalized-angle correspondence.

One local correction was required and has been applied by A567 in `sections/part_a567_toric_unequal.tex`, lines 157–162. The original converse said that if *a* seam was geodesic, restricting to all cut components recovered their canonical metrics. With several seams, other boundaries might be nongeodesic, so that inference was too broad. The corrected converse assumes **every seam is geodesic**, exactly as required to characterize the geodesic submodel. Every piece then has geodesic boundary and complete cusp ends, so uniqueness gives its canonical metric and equal paired lengths at every edge. Conversely, all d zero gives the previously proved simultaneous isometric gluing. The single-edge counterexample never had this problem.

## Automorphisms, topology, and the explicit witness

Intrinsic squared lengths make d transform by signed edge permutations. Uniqueness of the inverse makes this equivariant, including at self-loops. The total space is the corresponding real vector orbibundle over the geodesic image. A target stabilizer can act nontrivially on its R^E fiber; the statement explicitly does not identify the coarse quotient fiber with a smooth vector space. Scaling d to zero is equivariant and gives the stated strong deformation retraction. Combining it with the prior intrinsic radial retraction proves the asserted fundamental-group comparison to the unrestricted tensor/shadow target. The actual-circle-phase convention is essential and is expressly retained; fully marked real twists would require the corresponding covering target.

For the four-labelled-sphere witness, the one-cap range is `0<r<4`, so both radius pairs `(1,1)` and `(2,1/2)` exist uniquely. The explicit analytic weldings have equal product radius and phase, hence the same tensor. Labels preserve the sides. An isomorphism preserving the cut would preserve the canonical length of its first cut pant, whereas strict monotonicity gives `ell(1)!=ell(2)`. Thus they are distinct actual cut objects. The proof correctly makes no claim that their underlying uncut four-pointed surfaces must differ.

Finally, retaining full external shapes imposes exactly the matching-shape conditions on the unique systems indexed by d. The fiber is that subset of d, with its stated finite automorphism identifications. The R^E conclusion is deliberately restricted to the tensor/shadow target. The argument never assumes that discarding node caps preserves admissibility of the remaining external subsystem.

No further mathematical gap found. Separate independent events: `checks/part_b_unequal_toric_events.tsv`.
