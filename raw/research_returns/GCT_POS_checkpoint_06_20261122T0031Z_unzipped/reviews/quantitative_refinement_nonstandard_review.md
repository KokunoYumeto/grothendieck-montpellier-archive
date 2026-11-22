# Whole-proof review: quantitative cubic refinement

Date: 2026-11-21 (UTC; Europe/Berlin date identical).
Reviewer: GPT-6 Astra Pro, branch `/root/nonstandard`; effort setting not exposed.
Object read in full: `branches/plethysm/quantitative_refinement.tex`, containing PNEW-001--PNEW-005, as present during this review.
Event type: independent whole-proof reading / targeted proof check of all new estimates. This is not an independent verification of the complete inherited fixed-locus/residue chain.

## Outcome

**PASS for the stated new quantitative implications, conditional only on the explicitly identified inherited residue, amplitude, sibling and constituent identities. No unresolved mathematical gap was found in the new proofs.** The sufficient threshold 250000 is supported by the estimates. The mathematical minimum established inside the new displayed estimates is not claimed optimal.

## Checks performed

1. **PNEW-001.** In Q[z]/(z^4+1), the Salmon residue simplifies to (1+z+z^2+z^3)/8. Cyclotomic traces give 2W4(x)=±1/8 with the asserted four positive residues. The odd coefficient at x=19 is zero. The n=2 and n=3 degree normalizations are consistent with d0=n/gcd(n,3); their primitive waves cannot give a nonnegative witness. This verifies smallest rank for this particular dyadic-wave mechanism, not a globally smallest possible x or an asymptotic lower bound.
2. **PNEW-002.** Checked the increment's decomposition into B divisible factors and l exceptional factors, including exceptional weights 1 and 2 and assignment of weight 6. The initial dyadic block has odd numerator; a gap larger than R leaves a tail at most 1/(48·2^q_u). The factor lower bounds follow. Counts nR and the low-factor sine estimate are sufficient. At R≥6, the combined error constant is at most 4+7/R+193/(48R²)<16/3.
3. **PNEW-003.** Checked the distinct-subset valuation argument and layer count; the three-phase identity equals 3θ because w_{i+1}=-2w_i. Disjoint pairs yield disjoint lost cross factors. The omitted pair (2,3) is internal and is not subtracted as a cross-factor loss. Summing the elementary quadratic losses gives the stated cubic loss. Checked the two remaining factor families, the layer inequality for dyadic distances, and the bulk amplitude count and polynomial subtraction.
4. **PNEW-004.** Checked the triple/pair/singleton layer counts and summation. Re-read P-F56m in the supplied `positivity_paired_wave.tex` to check the normalization: P_n(b_n)=M_n|Z_n|, so the added n−1 is correct. The final cubic polynomial and discriminant comparison are consistent.
5. **PNEW-005 contraction.** Checked the near convex bound (including dropped negative terms), both endpoint substitutions, the far bound, the selected-sibling recurrence, and its iteration. Re-read P-F56ae and P-F56e' in the supplied source. Exact rational endpoint margins at N=72000 are:
   - near endpoint t=3/2: 242706000 below −N²/5;
   - near endpoint t=N/11: 58583913600000/121 below −N²/5;
   - far coefficient minus 11/5: 6729497/166375000 > 0.
   The exponent at 3N and geometric bound on the inhomogeneous term are sufficient for Q_n<1/4 at n≥216000.
6. **PNEW-005 phase and index step.** The inverse-residue phase step is k/r+1/(rM), with gcd(k,r)=1, so any r consecutive integers approximate the r equally spaced phases within 2π/M. The selected pair is at least |Z|/2; after remainder subtraction W≥|Z|/4 and hence 2W≥|Z|/2, exactly as used. The ambient-binomial estimate follows because m_n≤n³/5, d0≤n, x≤2^(n/8+1), and 2^(n/8)≥n² imply m_n+d0x≤4n·2^(n/8). The final difference n⁴/240−12n³/5−1 is already positive at n=1024 (30064771057/15). The constituent criterion gives p(f_n)>x and s(f_n)≥x, retaining the correct strict/non-strict distinctions.

## Scope and presentation qualifications

- This file is a quantitative refinement built on P-F19/P-F23--31/P-F56; it is not by itself the self-contained proof of that inherited chain requested in item 2.
- The classical n=2,3,4 invariant-ring descriptions are inherited/cited inputs. This review checks their use and normalizations; it does not replace primary-source verification.
- The exponent threshold 250000 is conservative: all displayed numerical conditions in this refinement are already met at 216000. Keeping 250000 is harmless.
- In the assembled paper W_n, Z_n and constituent notation must be defined before this section; they are supplied by the inherited wave section.
