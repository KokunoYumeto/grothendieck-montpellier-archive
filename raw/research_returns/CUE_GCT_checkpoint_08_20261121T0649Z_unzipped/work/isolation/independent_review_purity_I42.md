# Independent whole-proof review of I-42

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/purity_zero_status`; run CUE_GCT-20261121-purity.

Actual complete review finished 2026-11-21 06:05:19 UTC during the checkpoint write freeze; record saved after release at 06:06:27 UTC. **PASS** for the complete standalone draft, SHA256 `444b46ebc4301e4ae539be61c72f71a70a66b55b3e1e9ef1ac55721e8d0b3923`.

## Exact reset-Hessian lemma

I rederived the first-nonzero-row argument. Earlier columns vanish by symmetry. The first row's three kernels force at least four nonzero future b-values. When the distance to the next reset is at most five, the first such b is at most two positions ahead. It is strictly before the next reset, so its own row sees the same block. Subtracting the known suffix sum gives the displayed relation among at most three distinct Vandermonde columns, contradicting a_i nonzero.

For distance at most six outside characteristic two, the only additional case is exactly four nonzero b-values beginning three positions ahead. The relation among four Vandermonde columns has every coefficient nonzero. I independently expanded the row at k+1 and obtained `(2*a_k*b_l-a_l*b_k)*v_k-a_l*b_l*v_l=0`. Independence of these two columns first gives a_l=0, then contradicts 2*a_k*b_l nonzero. No extra assumption about unobserved reset blocks is needed.

## Sharp abstract examples

The characteristic-two seven-node construction is correct: the support intervals overlap only at node4, and its middle-row residual is -2*a4*b4*v4, while every other row vanishes by one of the four-node Vandermonde relations. The matrix is nonzero and symmetric with zero diagonal. The disjoint eight-node construction works in every characteristic and is of exactly the displayed semiseparable form. These show the abstract thresholds are sharp, but the text correctly makes no fixed-polynomial integrability or ROABP-annihilator claim.

## Conditional actual-word consequence

The normalized I/P representation has precisely the reset form, with endpoint departures and arrivals included. The maximum distance to the next singular position or final endpoint is the invertible-run length plus one. The assumed preservation of all internal ranks and the nonzero active endpoint projections supplies every normalization hypothesis. The three tangent kernels then force H=0 at the claimed run bounds, and the previously checked state-path proof kills all output paths. This is a sufficient consequence with explicit rank/endpoint hypotheses, not a claim that those hypotheses always hold.

## Positive saturated-run class

Irreducibility supplies all strict internal ranks at least two, while the actual minimal affine representation has singular first and last internal factors. An isolated full-rank core gives a connector on at most three coordinates. A run of length equal to the global weight saturates the determinant budget and gives invariant three-dimensional bounding support spaces. Parity and contraction identify their adjacent two-dimensional standard modules and the actual Gamma^2 anchors in every characteristic, exactly as checked in I41.

After constant normalization, each full-rank core has only first-superdiagonal linear entries. Their product always has linear first-superdiagonal entries and a quadratic top-right entry: every product of three such strictly upper-triangular three-by-three matrices is zero. This remains true for three, four, or five core variables. The weight-m pairing is the same nonzero antidiagonal pairing as in I41. Hence the complete connector retains its nonzero square coefficient and unique double pole at the left anchor, independent of the run length.

All connectors and univariate pivots therefore survive at the same formal center, and the minimal endpoint argument needs only pairwise dominance. The new reset-Hessian lemma completes the scalar nonvanishing proof for weights3/4 in all characteristics and weight5 outside characteristic two, under the stated isolated-or-saturated maximal-run promise. The finite sampler and field caveat are exactly the prior I40 bound. No unproved closure of this promise under factorization or specialization is asserted.

No mathematical repair requested. The remaining nonsaturated connector lengths are correctly left open. No new source proof audit or numerical execution was needed for these algebraic deductions; the review uses the already checked I40/I41 inputs and is not a formal verification certificate.
