# Independent whole-proof review: threshold 79000

Date: 2026-11-21 UTC. Reviewer: GPT-6 Astra Pro, `/root/nonstandard`; effort setting not exposed.
Object read completely: `deliverables/branches/plethysm/quantitative_refinement.tex`, PNEW-001--PNEW-005, version displaying threshold 79000 and N=39500.
Event type: independent whole-proof reading of the new quantitative section, with exact arithmetic checks. This does not re-verify the complete inherited cubic fixed-locus and residue chain.

## Outcome

**PASS for the new quantitative deductions, conditional on the explicitly cited inherited exact residue, selected-sibling, and paired-constituent identities. No unresolved mathematical gap found.** This review supersedes the numerical conclusions of the earlier 250000/216000 review but preserves that earlier review as a distinct event.

## Bounds checked

1. PNEW-001: retained the earlier checked cyclotomic residue and degree normalizations. The primitive-wave obstruction at rank four and x=19 is correct; minimality concerns this particular primitive dyadic-wave mechanism. The exact p=s=23 calibration is an inherited input.
2. PNEW-002: re-read the entire dyadic-block, low/high-factor, and exceptional-factor argument. The odd-numerator lower bound survives the discarded tail; the divisible and exceptional counts, including the singleton weights 1, 2, and 6, are correct. The final error 4+7/R+193/(48R²) is below 16/3 at R≥6.
3. PNEW-003 layers: distinct subset sums follow from the unique smallest 2-adic valuation. Fixed early subsets leave at most two late representatives in the required open interval. The identity y_uv+y_(u+1,v)+y_(u,v+1)=3θ excludes at least one cross-factor per disjoint pair of index-pairs when J>3·2^r. The omitted factor (2,3) is internal and does not invalidate the counted loss. For r≥6, the floor-binomial loss dominates (r−5)²/8; summation dominates (log₂J−8)_+³/24. The two residual families give the asserted total layer bound.
4. PNEW-003 selected amplitude: checked that the bulk correction sum is at most 2(n−5)+1, the 2+w_k correction at most 1, and the weight-6 correction below 1. At n=5 the bulk is empty and the bound still holds. The exact sum of l−k over the divisible weights is C(n−1,3)−n+4. The integer inequality 44^12<2^13·21^12 was verified exactly. Subtracting the selected lower bound gives 25n²/24+67n/24−11/6≤25n²/24+3n.
5. PNEW-004: checked triple, pair, and singleton layers and the subtraction for the actual number of factors. For active triples, |w_i+w_j+w_k|<2^(k+1) and the selected factor is at most 8·2^k/M_n. The two disjoint deleted families have total lower-bound contribution (n−3)(n−8)/2+(n−7). The new selected amplitude expands exactly to n⁴/24−3n³/4+59n²/24−3n/4−1. The mass bound is exactly log₂ Q_n≤2n³/3+10n/3−4.
6. PNEW-005 near endpoints: the displayed F_n drops only negative terms from PNEW-002. The t=19/12 endpoint is permitted because 3^12>2^19. Both normalized endpoint expressions decrease with n; for t=cn the linear coefficient is −4526/29296875<0. The exact positive margins at N=39500 are 19/59724000 and 8303507/86406250.
7. PNEW-005 far endpoint: exact margin 1676026865671/255978515625000>0. The derivative of (cn−8)^3/n² is (cn−8)²(cn+16)/n³>0; the remaining −3/n term also increases. Thus the far bound persists for all n≥N.
8. Recurrence iteration: the two lifts of a nonselected parent are nonselected; selected parents contribute the two siblings. The inherited sibling bound yields the stated inhomogeneous term. Start the iteration at Q_(N−1), bounded by PNEW-004 at N−1 and then by the larger cubic expression at N. The displayed exponent harmlessly drops the additional −4. Summing k² by the indicated integral is valid. At n=2N the displayed exponent is exactly −445603261, and thereafter decreases. The inhomogeneous geometric sum is at most 4·2^(−N³/12), so Q_n<1/4.
9. Phase and index conversion: a_*r=1+kM_n implies gcd(k,r)=1, giving the equally spaced comparison within 2π/M_n. The selected conjugate pair is at least |Z_n|/2; after the remainder, W_n≥|Z_n|/4 and 2W_n≥|Z_n|/2. The new amplitude lower bound is stronger than the coarser n⁴/24−2n³ used in the last step. The ambient binomial estimate and its positive final gap hold already at n=1024. The paired-constituent criterion retains p(f_n)>x and s(f_n)≥x, hence the displayed conclusions.

## Scope and optional clarification

The full inherited chain remains a dependency, as the section says. For readability only, the iteration sentence could explicitly say that the initial term is Q_(N−1), bounded by the larger mass estimate at N; this is a harmless overestimate and not a gap. The sufficient threshold 79000 is supported by the displayed proof and is not asserted optimal.
