# MA-PR-012: actual quotient costs and edge potential

Author: GPT-6 Astra Pro, MAS_ARTIN agent /root/pf26_audit.

Date: 2026-11-21.

Stable written proof: edge_potential_quotient_cost.tex, 447 lines, MA-PR.150–174. SHA256: 2685152b2d1636aa9d12e6b9ba3c8903beade4c0f81842954a25423585fec47d.

The complete post-writing author reading passed. Root then completed and passed the entire 447-line proof at the same hash and saved its own scoped review records. Both input_audit and s5_audit subsequently reported complete independent 447-line proof readings and passes, with their exact antecedent checks recorded separately. No mathematical correction was requested by any reader.

## Question and result

The parent requested an actual norm estimate for the canonical PR010 inclusion, rather than a scalar interpolation estimate or a reformulation of the same criterion. Under the existing generic distance hypothesis, this module proves
\[
\|\iota_n\mathscr R_n\|_{Q_H\to J_n}
\le C(2+|n|)^D \exp(U_n),
\]
where \(U_n\) is the supremum of the finite complex-distance logarithmic zero potential along the two fixed Hilbert edges in the block. Every target norm is the original M18 holomorphic quotient norm. The source is the whole Hilbert quotient, not an inherited norm on one oblique block range.

The sufficient bound \(U_n=O(\log(2+|n|))\) therefore gives the actual all-smooth returns and common all-order nuclear representations of PR010. It follows from either a uniform local disk count \(N(e+it,r)\le A_0+A_1r\log(2+|n|)\), or a bounded total multiplicity in fixed narrow real-part bands about both edges. These are additional explicitly stated conditions on actual zero data. Their arithmetic validity is not asserted.

The result applies for every fixed \(s\ge0\). In the generic-edge case the quotient restriction uses only an exponential Cauchy–Schwarz bound, so the higher polynomial-weight threshold from the different full-matrix boundary-distribution theorem is not needed here.

## Why the norm is the required one

For any representative \(h\in H\), take its actual Mellin transform on the inward rectangle. Its boundary norm is bounded by \(C(2+|n|)\|h\|_H\). Apply the whole-\(\Xi\) Cauchy interpolant from PR001. Its full jets equal those of \(h\) at every retained factor and vanish at every discarded factor. Its class in the original full \(J_n\) is therefore exactly \(\iota_n\mathscr R_n(\pi h)\).

The interpolant is estimated on the original outer boundary \(\Gamma_n\). Both that boundary and the inner contour have the same bounded height interval. The divided difference of \(\Xi\) is bounded there by the fixed-strip derivative estimate. Its completion exponential cancels the same exponential in the contour denominator once. This yields the stated norm bound directly before taking the quotient infimum over \(h\). No bound for an oblique projection is omitted.

The inward movement is one quarter of every relevant real-part edge distance. Thus each complex distance changes by at most the factor \(4/3\) in its inverse, and the additional total logarithmic loss is only \(O(\log(2+|n|))\).

## Exact limitation of the standard inputs

The potential has the layer-cake formula
\[
U_{n,e}(t)=\int_0^1 N(e+it,r)\,\frac{dr}{r}.
\]
Generic distance makes the integrand zero below a constant times \((2+|n|)^{-2}\). Using only the ordinary \(O(\log(2+|n|))\) local count on the remaining radii gives \(O(\log^2(2+|n|))\), and hence the previously available subexponential bound for the actual costs. This is the precise place where growing local multiplicity is multiplied by a logarithmic distance loss.

No lower bound of that size is asserted. The calculation proves neither that the new potential condition is necessary nor that arithmetic costs fail to be polynomial. It records the exact limit of this route from the stated standard estimates.

## Separate lower bound

For a full retained factor, composing a full-block Taylor functional with the canonical inclusion gives the actual Hilbert jet functional. Cauchy's inequality and its exact Hilbert dual norm give MA-PR.171. The multiplicities in M18.7 imply that the block-boundary factor \(d_\Omega(\rho)^j\) is bounded below by a fixed inverse polynomial uniformly for \(j<m_\rho\), without imposing a uniform multiplicity bound. The positive-tail integral gives the incomplete-gamma expression174.

The lower-bound paragraph explicitly permits replacing genericity by the global retained-or-discarded hypothesis PR100, so its canonical inclusion remains defined if there are fully retained boundary factors. It does not assert any actual growing multiplicity or very close edge sequence.

## Completed author checks and antecedents

I reread the entire written module in two untruncated portions, then reread the final lower-bound hypothesis and norm-square clarification. Every displayed exponent and factor was independently recomputed.

For this construction I freshly read the complete PR009–011 written proofs, the PR006 actual quotient/cost/Gram/attainment and factorization definitions and proofs through its construction of the actual return, PR008's close-pair norm argument, PR001's complete inner-restriction and whole-\(\Xi\) interpolation proof, and the M18 norm definitions, arithmetic inputs, selected-height and Blaschke/Harnack proof. Earlier full M18 and nuclear-series audits are inherited; they are not relabeled as newly repeated full primary-source readings.

No A or M premise, no simplicity claim, and no new outside source is used. The bounded-cluster conditions remain hypotheses. The theorem does not extend the original full common-space matrix, remove the discarded trace correction, or close PR011 at arbitrary widths.
