# DP41: revised integrated whole-proof and preservation review

Reviewer: `/root/archive_binomial`, **GPT-6 Astra Pro**, inherited model; runtime reasoning effort **not exposed**. Date: **2026-11-21 UTC**. Event **ABA-CE43**. The initial complete fragment reading was at **02:35:52 UTC**; after the three requested precision edits, I read the complete exact current fragment again during **02:39:58–02:40:45 UTC**. No main-paper edits.

## Outcome and version

**PASS.** The complete integrated statement, proof, prefactor conclusion, and following scope paragraph preserve the checked DP41 theorem and the stronger fraction-field multiplier lemma DP41-M. The exact entire fragment occurs once, byte-for-byte, in the current `DP_MULT.tex`.

- Entire integrated fragment SHA-256: `562f8ad84584c988216b97bc88cdb53f3cc4c87d1bd3328b4f68e315a031ca2a`.
- Complete theorem and proof SHA-256: `6c40128f2f82415833951b15970078ccd6eb0cad0a760aa53a73a52f3f5645df`.
- Frozen copy: `late_proof_snapshots/DP41_integrated_complete_checked.tex`.
- Metadata: `late_proof_snapshots/DP41_DP43_DP45_integrated_check_metadata.json`.

The three precision edits are now present: the nilpotent truncation explicitly has `D≥2`; Zink Proposition106 is located at p.226 separately from (218) at p.239; and uniqueness is explicitly for **this fixed frame**. These were precision recommendations rather than counterexamples to the mathematical theorem.

## Entire-proof check

The divided-ghost operator, normal-submodule projection, finite-support rational lifts and bounded-denominator integral completion are all retained. The complete matrix-cycle calculation identifies the logarithms in the actual Teichmüller coordinates. The comparison of the Teichmüller and additive bilinear sections retains both cocycle factors, their inverse for the splitting scalar, and Zink's negative `hex` convention. The exact triple sum and product sum therefore have the checked signs and denominator exponents. The fixed-frame qualification prevents an invalid conclusion of equality across different integral invariant frames.

I rechecked the two term-family inequalities after the common ramified contraction. For odd `p`, only `n=l=0` in the first family and `u=l=0, h−j=1` in the second survive at valuation `as−1`. Their initial form is `−Σ S^(p^j)Y_j+SY_d^p`. Its `Y_1` derivative is `−S^p`, also when `d=1`; no perfect-residue assumption is being substituted for this derivative calculation.

The multiplier proof is complete, rather than merely an assertion that a nonunit prefactor cannot help. The bounded-series Gauss valuation extends to the fraction field, whose residue field is the fraction field of the residual power-series ring. If a nonzero bounded multiplier cleared the exponential, the exponential itself would be in that field. Its `p`th-power identity forces residual value one. The two cases for the valuation of `E−1` then give either an impossible strict valuation or a rational `p`th-power initial form, contradicted by the formal derivative. This applies to arbitrary nonzero bounded multipliers, including series vanishing at the origin.

The interval `[p−1,p)` is excluded by that lemma. The endpoint `a=p` and all larger contractions follow from the factorial bound. Monotonicity supplies smaller `a`, and the integral contracted coordinate changes with integral inverse transfer both boundedness and unboundedness between group and additive coordinates. The final prefactor statement correctly distinguishes finite coefficient infimum for arbitrary nonzero integral prefactors from infimum zero when the constant term is a unit.

## Sources and limits

The integrated proof retains the already checked exact primary-source locations: Zink (147)–(156), pp.204–207; Proposition106, p.226; (196), p.232; (210)–(211), p.236; and (218), p.239. This event checks their preserved use and the complete new proof, not a new rereading of the entire external source proofs. Earlier complete DP41 and DP41-M checks are ABA-CE37 and ABA-CE38.

The theorem remains for odd primes, the specified actual Honda/dual pair, and its fixed invariant primitive frame. It proves an exact multivariate inflation threshold and a multiplier result. A restriction may cancel an initial form or annihilate a prefactor; neither a universal path threshold nor a global theta-cost conclusion follows here.
