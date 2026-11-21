# F69 variable-group quotient: complete proof and source review

Reviewer: `/root/rectangular_and_theta`, GPT-6 Astra Pro. Date: 2026-11-21 UTC. Inherited reasoning effort is not exposed.

## Target, verdict and reviewer independence

I read the entire `agent_variable_group_quotient.md`, SHA `9ba374972fdfd7d99f804097a4836271d0e20b9743bae363c0defe3f26117106`, and reconstructed all of VQ1--VQ25. **Whole-proof mathematical PASS**, with one small clarification requested: since the construction begins over an arbitrary field k, write VQ21 as geometric cohomology after base change to an algebraic closure, or explicitly state that convention before the calculation. Nonvanishing geometrically already proves the claimed Chern nonsplitting over the original field. No change to the construction or any theorem is needed.

I supplied the original four-point Ga-versus-Gm argument during development, so this is a contributor check for that part, not a claim of independent conception. The global algebra/group/torsor construction, its orientation, and the new second-stage stack-stratum calculation were independently read and rederived here. Root supplied the original global quotient proposal. Gct is providing a separate complete independent review.

## Full construction check

The three open sets defined by avoiding 0, 1 and infinity cover the two-endpoint base over every field, including F2: two geometric endpoints cannot exhaust three distinct rational points. On each such open, the divisor has monic equation `(t-x)(t-z)`, so its degree-two finite-local-freeness is proved directly, including the nonreduced collision. The kernel of evaluation at x is the restriction of the first section ideal to the second, hence `O(-Delta)`. The unit provides an actual splitting as a vector bundle. The local multiplication `c²=hc` retains the nilpotent diagonal and glues via the actual divisor algebra.

For `a+bc`, the norm is `a(a+hb)`. The unit group is therefore an explicit open in a rank-two vector bundle. Evaluation at x splits its scalar subgroup, so the quotient by scalar units really is represented by its kernel, with no appeal to an unverified quotient-representability assertion. The kernel has coordinate `u`, invertible `1+hu`, and multiplication `u+v+huv`. This defines a smooth affine relative one-dimensional group, multiplicative off the diagonal and the additive vector group of `O(-2)` on the diagonal. The latter is correctly not asserted to be a globally constant Ga bundle.

The restriction of O(1) to the degree-two divisor has pushforward equal to the constant two-dimensional space of global sections. Both displayed arguments work: the kernel O(-1) has zero H0 and H1, and the local bases 1,t and 1,c differ by determinant one. The A-generator condition is an actual determinant-open condition, valid on nonreduced test schemes. A projective section is a generator exactly when its unique zero avoids both endpoints, including the double-point fiber. This proves the path-scheme identification as a scheme, not merely on geometric points.

The ratio of two module frames gives the inverse to `J times P -> P times P`. Scalar changes disappear in the quotient, so the ratio maps glue. The fixed missing point on each of the three opens supplies a Zariski local torsor section. Multiplication by `1+uc` acts projectively by `[a:b] -> [a:b+ua+hub]`, with determinant `1+hu`; hence the action extends to the entire projective bundle and fixes the endpoint zero-lines. The quotient-stack equivalence with the base follows because an equivariant map between torsors is an isomorphism, and an automorphism preserving that map is trivial.

The finite-field counts are consistent with the actual torsors: Q-1 or Q points over off-diagonal or diagonal endpoints, respectively, and total path count `Q²(Q+1)`. The quotient is the scheme Y, with `(Q+1)²` points and no residual inertia. These counts are consequences of the constructed action, not a replacement for it.

## Chern orientation and four-point scope

With endpoint vectors vx,vz, a third line has graph coordinate lambda and is the kernel of a section satisfying `ell(vx)+lambda ell(vz)=0`. Multiplying section values by ux,uz therefore multiplies lambda by ux/uz. This verifies the report's choice of multiplicative coordinate and the line bundle `Hom(Vx,Vz)=O(1,-1)`, without reversing its Chern class inadvertently.

After geometric base change, the diagonal Gysin sequence gives `H²(O,E(1))=(E h_x plus E h_z)/E(h_x+h_z)`. The class `h_x-h_z` becomes `2h_x` and is nonzero over the characteristic-zero coefficient field, even when the finite base field has characteristic two. Thus the existing compact-fiber triangle remains nonsplit. The stack quotient uses the action and changes the category; it does not tensor-invert the ordinary torus compact-cohomology object, so it is compatible with F68.

For the four-point path `(0,1,infinity,1)`, the first group acts transitively on the nonzero middle coordinate y. Moving y to b distinct from 0 and 1 changes the second named group from Ga to Gm. Equivariant descent of that group scheme would require an isomorphism between the two fibers along this single arrow. Even their underlying affine schemes are nonisomorphic, as their coordinate-ring units differ. This directly proves the stated no-descent premise and does not assume a cocycle argument.

After the first quotient, the base is exactly `{(x,z,w):z!=w}`. No condition `z!=x` survives. The newly defined endpoint group `J_(x,w)` does act on that punctured line, since its projective action fixes w. When x differs from w, its fixed point z=x remains and the quotient fiber is `[A1/Gm]`, with an open point and a closed BGm. The finite-field mass is `1+1/(Q-1)=Q/(Q-1)`. When x=w, the additive action is a torsor and the quotient fiber is a point. This new action is correctly distinguished from descent of the original neighbor group. The report does not infer that every weak associator, alternative stack construction, or higher normalization is impossible.

## Primary source contexts freshly read

I opened and read the following exact primary contexts in this review:

- Stacks Definition29.49.1, tag02KA: affine finite-locally-free convention and degree. URL `https://stacks.math.columbia.edu/tag/02KA`; retrieval `turn444977886view0`.
- Stacks Section97.11, tag05Y8: restriction-of-scalars functor, sheaf statement and its setting. URL `https://stacks.math.columbia.edu/tag/05Y8`; retrieval `turn958076881view0`.
- Stacks Lemma97.11.2, tag05YC: complete base-change statement and proof. URL `https://stacks.math.columbia.edu/tag/05YC`; retrieval `turn444977886view1`.
- Stacks Situation95.15.1 and its torsor description, tag04UV. URL `https://stacks.math.columbia.edu/tag/04UV`; retrieval `turn444977886view3`.
- Stacks Proposition95.15.3, tag04WM: complete quotient-stack/torsor equivalence statement and proof. URL `https://stacks.math.columbia.edu/tag/04WM`; retrieval `turn444977886view2`.

The source hypotheses apply to the actual schemes and group action proved in the note. General representability is not used in place of the explicit norm-open model. The previously checked F62 Milne/Gysin and EGA/SGA dictionary anchors are retained as framework citations; I do not claim a new visual archive inspection in this review.

No numerical computation is required for the scheme-valued or descent proofs, and none is presented as their verification. No main paper or shared event log was edited. Final fragment matching remains to be recorded after the author prepares it.

## Final report delta and whole-fragment match

I read the exact final report changes at SHA `6f8a8954b95880d5385cf7fa54c639d1c8e840530f3893bd13bba9e34f26dada`, the entire `finding_F69.tex` at SHA `cfb5f340cddcae7c1a9c94a333dbfdedbec2e5c4c95d9e4c71e62a8fc0276518`, and its complete bibliography supplement at SHA `bccb82673246f4b54d4406438c16fc8cbc5c189c567e8cb0b5b63b1675156591`. **Final full-text/report-to-fragment match PASS.** The requested geometric-cohomology clarification is applied with ell invertible, E finite over Q_ell, and nonsplitting witnessed after geometric base change. All original proofs and scope distinctions survive the fragment, including the whole-base local sections, ratio inverse, orientation, exact non-descent premise, alternative endpoint action and separate F69 dictionary.

The only added theorem is the finite-Weil boundary for the specific residual mass. I independently reconstructed its complete proof. For `s_n=Q^n/(Q^n-1)`, the expansion `sum_{j>=0}(Q^-j)^n` converges for n>=1. For any N>=1 and every matrix size, the rational Hankel matrix `(s_(N+a+b))` has quadratic form `sum_{j>=0}Q^(-jN)p(Q^-j)^2`. The weights are positive and a nonzero polynomial has only finitely many zeros, so the form is strictly positive and its determinant is a nonzero rational number. A finite power sum has bounded Hankel rank over its own characteristic-zero coefficient field; the same rational determinant remains nonzero in that field. Taking N beyond the eventual-equality threshold gives the contradiction without a complex embedding or purity hypothesis. Finite uninserted Weil Euler traces, including signed multiplicities and Jordan blocks, have the required finite power-sum form. The proof therefore establishes the exact stated boundary and does not exclude the quotient stack or every higher normalization.

The final bibliography's five tags, statement numbers and roles match the primary contexts freshly read above. No new source is needed for the explicit Hankel argument. I found no remaining mathematical correction.
