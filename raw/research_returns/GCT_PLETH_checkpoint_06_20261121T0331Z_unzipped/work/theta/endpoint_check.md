# Source-relative endpoint proof check

ID T-015; run GCT_PLETH-20261121-theta. This observation is included as a checked comparison with a source, not as a new best global bound.

The full proof in `work/external/quadratic_stabilization_2026.tex`, sections 2–4, lines 178–436, was read, including its diagonal-annihilator criterion, Fischer inner-product lemma, and four-step induction.

For `a>=3`, set `r=a-1` and `b=a(a-1)-1=r(r+1)-1`. The residual symmetric degree is `m=b-r=r^2-1`. Source Step 2 still has `p-q=m-i+1>=1` for every derivative insertion. In Step 3, `m=r^2-1>=r(r-1)` and `m>=1`, so the source's original Proposition 3 for `r` slots applies; no stronger induction claim is assumed. In Step 4 the shared destination degree is at most `r^2-1`, while the source degree before each derivative is at least `b-r+1=m+1=r^2`, so the injectivity inequality remains strict. The final multilinear spanning step is unchanged.

Thus the source proof also gives surjectivity of `h_{b,a}` at the one-lower endpoint; its original theorem covers all larger `b`. At `a=2,b=1` the map is the identity under the canonical symmetric-power identifications. The parent agent found a stronger recent bound and is separately checking it; this event does not certify that other paper.
